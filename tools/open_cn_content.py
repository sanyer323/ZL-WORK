#!/usr/bin/env python3
"""Open 今日头条 / 抖音 links and extract text for prompt use.

ByteDance pages are JS shells. Plain curl of the share URL is not enough.
This script uses the working public endpoints found in this environment:

  头条图文/视频: GET https://m.toutiao.com/i{id}/info/
  抖音视频文案: GET https://www.douyin.com/video/{id}  (Googlebot UA)
  短链: follow redirects, then parse id

Chrome dump-dom is a last-resort fallback (slow). Prefer this script first.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.request
from dataclasses import dataclass, field

UA_MOBILE = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 "
    "Mobile/15E148 Safari/604.1"
)
UA_BOT = (
    "Mozilla/5.0 (compatible; Googlebot/2.1; "
    "+http://www.google.com/bot.html)"
)
UA_PC = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)


@dataclass
class Extract:
    url: str
    platform: str
    ok: bool
    title: str = ""
    author: str = ""
    published: str = ""
    kind: str = ""
    body: str = ""
    notes: list[str] = field(default_factory=list)

    def as_markdown(self) -> str:
        lines = [
            f"# {self.title or '(无标题)'}",
            "",
            f"- 平台: {self.platform}",
            f"- 链接: {self.url}",
        ]
        if self.author:
            lines.append(f"- 作者/来源: {self.author}")
        if self.published:
            lines.append(f"- 时间: {self.published}")
        if self.kind:
            lines.append(f"- 类型: {self.kind}")
        lines.append("")
        lines.append("## 正文 / 文案")
        lines.append("")
        lines.append(self.body.strip() or "（未能抽出正文。把链接、截图或口播文字发过来。）")
        if self.notes:
            lines.append("")
            lines.append("## 抽取说明")
            lines.append("")
            for n in self.notes:
                lines.append(f"- {n}")
        return "\n".join(lines) + "\n"


def fetch(url: str, ua: str, timeout: int = 20) -> tuple[str, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": ua,
            "Accept": "text/html,application/json,application/xhtml+xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        final = resp.geturl()
        raw = resp.read()
        ctype = resp.headers.get("Content-Type", "")
        enc = "utf-8"
        m = re.search(r"charset=([\w-]+)", ctype, re.I)
        if m:
            enc = m.group(1)
        text = raw.decode(enc, errors="replace")
        return final, text


def strip_html(s: str) -> str:
    s = re.sub(r"(?is)<script.*?>.*?</script>", " ", s)
    s = re.sub(r"(?is)<style.*?>.*?</style>", " ", s)
    s = re.sub(r"(?is)<br\s*/?>", "\n", s)
    s = re.sub(r"(?is)</p>", "\n", s)
    s = re.sub(r"(?is)</div>", "\n", s)
    s = re.sub(r"(?is)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def first_id(patterns: list[str], text: str) -> str | None:
    for p in patterns:
        m = re.search(p, text)
        if m:
            return m.group(1)
    return None


def resolve(url: str) -> str:
    try:
        final, _ = fetch(url, UA_PC, timeout=15)
        return final
    except Exception:
        return url


def toutiao_id(url: str) -> str | None:
    return first_id(
        [
            r"toutiao\.com/article/(\d+)",
            r"toutiao\.com/video/(\d+)",
            r"toutiao\.com/a(\d+)",
            r"m\.toutiao\.com/i(\d+)",
            r"toutiao\.com/i(\d+)",
            r"[?&]group_id=(\d+)",
        ],
        url,
    )


def douyin_id(url: str) -> str | None:
    return first_id(
        [
            r"douyin\.com/video/(\d+)",
            r"douyin\.com/shipin/(\d+)",
            r"douyin\.com/note/(\d+)",
            r"iesdouyin\.com/share/video/(\d+)",
            r"[?&]modal_id=(\d+)",
            r"/(\d{19})",
        ],
        url,
    )


def extract_toutiao(url: str) -> Extract:
    tid = toutiao_id(url)
    if not tid and ("toutiao.com" in url or "v.douyin.com" not in url):
        resolved = resolve(url)
        tid = toutiao_id(resolved) or tid
        url = resolved
    if not tid:
        return Extract(url, "toutiao", False, notes=["无法从链接解析文章 ID"])

    info_url = f"https://m.toutiao.com/i{tid}/info/"
    try:
        _, text = fetch(info_url, UA_MOBILE)
        data = json.loads(text).get("data") or {}
    except Exception as e:
        return Extract(url, "toutiao", False, notes=[f"info 接口失败: {e}"])

    if not data:
        return Extract(
            url,
            "toutiao",
            False,
            notes=["info 接口无 data。可能已删或需登录。"],
        )

    media = data.get("media_user") or {}
    author = (
        data.get("source")
        or media.get("name")
        or data.get("detail_source")
        or ""
    )
    published = str(data.get("publish_time") or "")
    if published.isdigit():
        import datetime

        published = datetime.datetime.fromtimestamp(
            int(published), datetime.timezone.utc
        ).strftime("%Y-%m-%d %H:%M")

    body = strip_html(data.get("content") or "")
    kind = data.get("biz_tag") or ""
    if body in ("视频加载中...", "视频加载中") or (
        "tt-video-box" in (data.get("content") or "") and len(body) < 40
    ):
        kind = kind or "视频"
        body = data.get("title") or body
        notes = ["这是头条视频，info 接口只有标题/简介，没有口播全文。"]
    else:
        notes = ["来源: m.toutiao.com/i{id}/info/"]

    return Extract(
        url=f"https://www.toutiao.com/article/{tid}/",
        platform="toutiao",
        ok=bool(data.get("title") or body),
        title=data.get("title") or "",
        author=author,
        published=published,
        kind=kind or "图文",
        body=body,
        notes=notes,
    )


def _meta(html_text: str, name: str) -> str:
    m = re.search(
        rf'<meta[^>]+(?:name|property)="{re.escape(name)}"[^>]+content="([^"]*)"',
        html_text,
        re.I,
    )
    if not m:
        m = re.search(
            rf'<meta[^>]+content="([^"]*)"[^>]+(?:name|property)="{re.escape(name)}"',
            html_text,
            re.I,
        )
    return html.unescape(m.group(1)).strip() if m else ""


def extract_douyin(url: str) -> Extract:
    original = url
    if "v.douyin.com" in url or "iesdouyin.com/share/video" in url:
        url = resolve(url)
    vid = douyin_id(url) or douyin_id(original)
    if not vid:
        return Extract(original, "douyin", False, notes=["无法从链接解析视频 ID"])

    page = f"https://www.douyin.com/video/{vid}"
    try:
        _, html_text = fetch(page, UA_BOT)
    except Exception as e:
        return Extract(page, "douyin", False, notes=[f"页面拉取失败: {e}"])

    title = _meta(html_text, "lark:url:video_title")
    desc = _meta(html_text, "description")
    author = ""
    published = ""
    body = ""

    for jm in re.finditer(
        r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',
        html_text,
        re.S | re.I,
    ):
        try:
            obj = json.loads(jm.group(1))
        except json.JSONDecodeError:
            continue
        if not isinstance(obj, dict):
            continue
        if obj.get("@type") == "VideoObject":
            title = title or obj.get("name") or ""
            body = body or obj.get("name") or ""
            uploaded = obj.get("uploadDate") or ""
            if uploaded:
                published = uploaded[:10]
            a = obj.get("author")
            if isinstance(a, dict):
                author = author or a.get("name") or ""
            elif isinstance(a, str):
                author = author or a
        if obj.get("@type") == "BreadcrumbList":
            for item in obj.get("itemListElement") or []:
                name = item.get("name") or ""
                link = item.get("item") or ""
                if "douyin.com/user/" in str(link) and name and name != "抖音":
                    author = author or name

    if not author:
        pm = re.search(r"(.+?)于(20\d{6}|20\d{2}-\d{2}-\d{2})发布在抖音", desc)
        if pm:
            author = pm.group(1).split(" - ")[-1].strip()
            published = published or pm.group(2)

    body = (title or body or desc).strip()
    body = re.split(r"\s+-\s+.+于20\d{6}发布在抖音", body)[0].strip()
    title_line = body.split("\n", 1)[0].strip() if body else ""

    return Extract(
        url=page,
        platform="douyin",
        ok=bool(body),
        title=title_line[:80],
        author=author,
        published=published,
        kind="短视频文案",
        body=body,
        notes=[
            "来源: douyin.com/video/{id} + Googlebot UA，可拿到封面文案。",
            "口播「AI 文稿」多数页面不直接给。需要口播全文时，发 /shipin/ 链接、截图，或把文稿贴过来。",
        ],
    )


def detect(url: str) -> str:
    u = url.lower()
    if any(x in u for x in ("toutiao.com", "toutiaocdn.com")):
        return "toutiao"
    if any(x in u for x in ("douyin.com", "iesdouyin.com", "amemv.com")):
        return "douyin"
    return "unknown"


def extract_one(url: str) -> Extract:
    url = url.strip()
    kind = detect(url)
    if kind == "unknown" and "v.douyin.com" in url:
        kind = "douyin"
    if kind == "toutiao":
        return extract_toutiao(url)
    if kind == "douyin":
        return extract_douyin(url)
    return Extract(
        url,
        "unknown",
        False,
        notes=["还不识别这个站点。把全文、截图发过来，或告诉我平台名。"],
    )


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="提取头条/抖音正文供 prompt 使用")
    p.add_argument("urls", nargs="+", help="文章或视频链接")
    args = p.parse_args(argv)
    blocks = []
    any_ok = False
    for u in args.urls:
        r = extract_one(u)
        any_ok = any_ok or r.ok
        blocks.append(r.as_markdown())
        if not r.ok:
            print(r.as_markdown(), file=sys.stderr)
        else:
            print(r.as_markdown())
    return 0 if any_ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
