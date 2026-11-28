# -*- coding: utf-8 -*-
"""
FY301 研发讲解成片：片头卡 + 5段仿真（拉长对齐旁白）+ 中文字幕 + TTS旁白
输出：
  out/FY301_研发原理讲解_完整版.mp4
  out/FY301_研发原理讲解.srt
  旁白文案_完整版.txt
"""
from __future__ import annotations

import asyncio
import subprocess
import sys
import textwrap
from pathlib import Path

import imageio_ffmpeg

from fy301_common import ffmpeg_fontfile_esc, find_sim, load_storyboard, subtitle_force_style

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
OUT.mkdir(exist_ok=True)
FF = imageio_ffmpeg.get_ffmpeg_exe()

# 分段：源视频文件名、目标时长(秒)、章节标题、旁白（研发浓缩版）
SEGMENTS = [
    {
        "src": "01_压电陶瓷原理.mp4",
        "dur": 22,
        "title": "① 压电陶瓷：逆压电效应与低功耗驱动",
        "narration": (
            "理解 FY301 气动核心，先看压电陶瓷。"
            "逆压电效应使陶瓷在电场下发生形变：电压升高，压电盘弯曲，充当喷嘴前方的挡板。"
            "运行监控电压大约三十到七十伏。"
            "电气上它近似电容，只有充放电瞬间有电流，稳态近乎零功耗，因此整机可在三点八毫安两线回路下工作。"
        ),
    },
    {
        "src": "02_喷嘴挡板先导级.mp4",
        "dur": 20,
        "title": "② 喷嘴挡板先导级：间隙调制先导压力",
        "narration": (
            "气源经节流孔向喷嘴供恒定小气流，压电盘作挡板调制间隙。"
            "电压升高，挡板靠近喷嘴，排气受阻，先导室压力升高；电压降低则先导压力下降。"
            "手册 FYCAL 参考：供气二十磅时，零伏约两磅，五十伏约六磅，一百伏约十二到十三磅。"
            "先导压力精确但流量小，必须进入下一级放大。"
        ),
    },
    {
        "src": "03_膜片放大与滑阀.mp4",
        "dur": 20,
        "title": "③ 膜片伺服放大与滑阀 OUT1 / OUT2",
        "narration": (
            "先导压力作用在大膜片上，经连杆与小膜片力平衡，把微小压力变化放大为滑阀位移。"
            "滑阀上移时，供气进入 OUT1；下移时 OUT1 排气，双作用时 OUT2 方向相反。"
            "失电故障安全：OUT1 到零，OUT2 到供气压力，执行机构回到安全位。"
        ),
    },
    {
        "src": "04_霍尔反馈与闭环.mp4",
        "dur": 18,
        "title": "④ 霍尔非接触反馈与闭环定位",
        "narration": (
            "阀杆磁铁与霍尔传感器非接触测位，安装间隙目标二到四毫米。"
            "设定值与实际位置比较，经比例积分修正压电驱动电压，偏差逐步收敛。"
            "无杠杆磨损，适合高精度长期运行。"
        ),
    },
    {
        "src": "05_全系统闭环信号流.mp4",
        "dur": 18,
        "title": "⑤ 全系统电–气–机闭环信号流",
        "narration": (
            "完整链路：四到二十毫安经模数转换进入 CPU，数模与隔离驱动压电盘，"
            "调制先导压力，膜片放大推动滑阀，OUT1 OUT2 驱动执行器，霍尔回馈位置。"
            "电气蓝路径与气动橙路径并行，形成智能定位闭环。这就是 FY301 的工作原理。"
        ),
    },
]


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stderr[-2000:] if r.stderr else r.stdout, flush=True)
        raise RuntimeError(f"cmd failed: {cmd[:3]}...")


def make_title_card(path: Path, title: str, seconds: float = 2.5) -> None:
    # drawtext with YaHei; escape for ffmpeg
    # Use lavfi color + drawtext
    font = ffmpeg_fontfile_esc()
    # wrap title
    lines = textwrap.wrap(title, width=22) or [title]
    # build stacked drawtext
    filters = []
    base_y = f"(h-{'*'.join(['24']*len(lines)) if False else str(28 * len(lines))})/2"
    for i, line in enumerate(lines):
        safe = (
            line.replace("\\", "\\\\")
            .replace(":", "\\:")
            .replace("'", "\\'")
            .replace("%", "\\%")
        )
        y = f"(h-{28 * len(lines)})/2+{i * 32}"
        filters.append(
            f"drawtext=fontfile='{font}':text='{safe}':fontsize=28:fontcolor=white:"
            f"x=(w-text_w)/2:y={y}:shadowcolor=black@0.6:shadowx=2:shadowy=2"
        )
    vf = ",".join(filters)
    run(
        [
            FF,
            "-y",
            "-f",
            "lavfi",
            "-i",
            f"color=c=0x0b1220:s=1280x720:d={seconds}:r=20",
            "-vf",
            vf,
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-t",
            str(seconds),
            str(path),
        ]
    )


def trim_clip(src: Path, dst: Path, seconds: float) -> None:
    run(
        [
            FF,
            "-y",
            "-i",
            str(src),
            "-t",
            str(seconds),
            "-vf",
            "scale=1280:720,fps=20",
            "-an",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(dst),
        ]
    )


def concat_videos(paths: list[Path], dst: Path, list_file: Path) -> None:
    concat_list(paths, list_file)
    run(
        [
            FF,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(list_file),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-r",
            "20",
            str(dst),
        ]
    )


def stretch_video(src: Path, dst: Path, target_dur: float) -> None:
    # probe duration roughly via ffmpeg -i
    probe = subprocess.run([FF, "-i", str(src)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    import re

    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", probe.stderr or "")
    if not m:
        raise RuntimeError(f"cannot probe {src}")
    src_dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    factor = target_dur / max(src_dur, 0.1)
    # setpts slows/speeds; also loop if needed for very short
    run(
        [
            FF,
            "-y",
            "-stream_loop",
            "2",
            "-i",
            str(src),
            "-filter:v",
            f"setpts={factor}*PTS,fps=20,scale=1280:720",
            "-an",
            "-t",
            str(target_dur),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-preset",
            "fast",
            str(dst),
        ]
    )


def srt_timestamp(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def split_narration_cues(text: str, start: float, end: float) -> list[tuple[float, float, str]]:
    # split by Chinese punctuation into subtitle cues
    parts = []
    buf = ""
    for ch in text:
        buf += ch
        if ch in "。；！？":
            parts.append(buf.strip())
            buf = ""
    if buf.strip():
        parts.append(buf.strip())
    parts = [p for p in parts if p]
    if not parts:
        return [(start, end, text)]
    total_chars = sum(len(p) for p in parts)
    cues = []
    t = start
    span = end - start
    for p in parts:
        dur = max(1.6, span * (len(p) / total_chars))
        cues.append((t, min(t + dur, end), p))
        t += dur
    # fix last end
    if cues:
        cues[-1] = (cues[-1][0], end, cues[-1][2])
    return cues


async def synthesize_tts(text: str, mp3: Path) -> bool:
    try:
        import edge_tts
    except ImportError:
        print("edge_tts not installed", flush=True)
        return False
    voice = "zh-CN-YunxiNeural"  # male clear
    communicate = edge_tts.Communicate(text, voice, rate="-5%")
    await communicate.save(str(mp3))
    return mp3.exists() and mp3.stat().st_size > 1000


def concat_list(paths: list[Path], list_file: Path) -> None:
    lines = []
    for p in paths:
        # ffmpeg concat demuxer needs escaped single quotes
        ap = p.resolve().as_posix().replace("'", "'\\''")
        lines.append(f"file '{ap}'")
    list_file.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    story = load_storyboard()
    master_cfg = story.get("master_edition") or {}
    prefer_blender = bool(master_cfg.get("prefer_blender_sims", True))
    broll_map = master_cfg.get("product_parts_broll") or {}
    broll_seconds = float(master_cfg.get("broll_seconds", 4.0))

    # 1) write narration doc
    narr_doc = ROOT / "旁白文案_完整版.txt"
    blocks = []
    t_cursor = 0.0
    timeline = []  # (start, end, title, narration, stretched_path)
    title_dur = 2.5

    work = OUT / "_build"
    work.mkdir(exist_ok=True)

    for i, seg in enumerate(SEGMENTS):
        seg_id = f"{i + 1:02d}"
        src = find_sim(seg["src"], prefer_blender=prefer_blender)

        card = work / f"card_{i:02d}.mp4"
        stretched = work / f"seg_{i:02d}.mp4"
        make_title_card(card, seg["title"], title_dur)
        stretch_video(src, stretched, seg["dur"])

        seg_body = stretched
        extra_broll = 0.0
        broll_rel = broll_map.get(seg_id)
        if broll_rel:
            broll_src = ROOT / str(broll_rel)
            if broll_src.exists() and broll_src.stat().st_size > 1000:
                broll = work / f"broll_{i:02d}.mp4"
                trim_clip(broll_src, broll, broll_seconds)
                combined = work / f"seg_body_{i:02d}.mp4"
                concat_videos([broll, stretched], combined, work / f"pair_{i:02d}.txt")
                seg_body = combined
                extra_broll = broll_seconds
                print(f"broll[{seg_id}]: {broll_src.name} (+{broll_seconds}s)", flush=True)
            else:
                print(f"warn: broll missing for segment {seg_id}: {broll_rel}", flush=True)

        seg_dur = seg["dur"] + extra_broll

        t0 = t_cursor
        t1 = t0 + title_dur
        t2 = t1 + seg_dur
        timeline.append(
            {
                "card": card,
                "seg": seg_body,
                "title": seg["title"],
                "narration": seg["narration"],
                "t_card0": t0,
                "t_card1": t1,
                "t_seg0": t1 + extra_broll,
                "t_seg1": t2,
            }
        )
        blocks.append(f"[{srt_timestamp(t1)} - {srt_timestamp(t2)}] {seg['title']}\n{seg['narration']}\n")
        t_cursor = t2

    narr_doc.write_text("\n".join(blocks), encoding="utf-8")
    print("wrote", narr_doc, flush=True)

    # 2) SRT (title + narration cues)
    srt_path = OUT / "FY301_研发原理讲解.srt"
    cues_all = []
    idx = 1
    srt_lines = []
    for item in timeline:
        srt_lines.append(str(idx))
        srt_lines.append(f"{srt_timestamp(item['t_card0'])} --> {srt_timestamp(item['t_card1'])}")
        srt_lines.append(item["title"])
        srt_lines.append("")
        idx += 1
        for a, b, text in split_narration_cues(item["narration"], item["t_seg0"], item["t_seg1"]):
            srt_lines.append(str(idx))
            srt_lines.append(f"{srt_timestamp(a)} --> {srt_timestamp(b)}")
            # wrap long lines
            wrapped = textwrap.wrap(text, width=28) or [text]
            srt_lines.append("\n".join(wrapped))
            srt_lines.append("")
            idx += 1
            cues_all.append((a, b, text))
    srt_path.write_text("\n".join(srt_lines), encoding="utf-8")
    print("wrote", srt_path, flush=True)

    # 3) concat silent video
    parts = []
    for item in timeline:
        parts.append(item["card"])
        parts.append(item["seg"])
    list_file = work / "concat.txt"
    concat_list(parts, list_file)
    silent = work / "silent_master.mp4"
    run(
        [
            FF,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(list_file),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-r",
            "20",
            str(silent),
        ]
    )

    # 4) TTS full narration with gaps for title cards
    full_text_parts = []
    for item in timeline:
        # brief pause represented by punctuation; edge-tts can't pause easily — insert ellipsis
        full_text_parts.append(item["narration"])
    full_text = "".join(full_text_parts)
    voice_mp3 = work / "narration.mp3"
    has_voice = asyncio.run(synthesize_tts(full_text, voice_mp3))

    # Burn subtitles (soft ASS via srt) — use subtitles filter; escape path for Windows
    burned = OUT / "FY301_研发原理讲解_完整版.mp4"
    srt_esc = str(srt_path.resolve()).replace("\\", "/").replace(":", "\\:")
    sub_style = subtitle_force_style(font_size=18).replace("MarginV=26", "MarginV=28")

    if has_voice:
        # mux: stretch/pad audio? Use -shortest after delaying audio for first title
        # Simpler: generate per-segment TTS and concat audio with silences
        audio_parts = []
        for i, item in enumerate(timeline):
            silence = work / f"sil_{i:02d}.mp3"
            # title silence
            run(
                [
                    FF,
                    "-y",
                    "-f",
                    "lavfi",
                    "-i",
                    f"anullsrc=r=24000:cl=mono",
                    "-t",
                    str(title_dur),
                    "-q:a",
                    "9",
                    "-acodec",
                    "libmp3lame",
                    str(silence),
                ]
            )
            seg_mp3 = work / f"narr_{i:02d}.mp3"
            ok = asyncio.run(synthesize_tts(item["narration"], seg_mp3))
            if not ok:
                has_voice = False
                break
            # pad/trim narration to segment duration
            narr_pad = work / f"narrpad_{i:02d}.mp3"
            run(
                [
                    FF,
                    "-y",
                    "-i",
                    str(seg_mp3),
                    "-af",
                    f"apad=whole_dur={item['t_seg1']-item['t_seg0']}",
                    "-t",
                    str(item["t_seg1"] - item["t_seg0"]),
                    str(narr_pad),
                ]
            )
            audio_parts.append(silence)
            audio_parts.append(narr_pad)

        if has_voice:
            alist = work / "acodet.txt"
            concat_list(audio_parts, alist)
            voice_all = work / "voice_all.mp3"
            run(
                [
                    FF,
                    "-y",
                    "-f",
                    "concat",
                    "-safe",
                    "0",
                    "-i",
                    str(alist),
                    "-c",
                    "copy",
                    str(voice_all),
                ]
            )
            run(
                [
                    FF,
                    "-y",
                    "-i",
                    str(silent),
                    "-i",
                    str(voice_all),
                    "-vf",
                    f"subtitles='{srt_esc}':force_style='{sub_style}'",
                    "-c:v",
                    "libx264",
                    "-pix_fmt",
                    "yuv420p",
                    "-c:a",
                    "aac",
                    "-b:a",
                    "128k",
                    "-shortest",
                    str(burned),
                ]
            )
        else:
            has_voice = False

    if not has_voice:
        print("TTS unavailable — exporting subtitled silent master", flush=True)
        run(
            [
                FF,
                "-y",
                "-i",
                str(silent),
                "-vf",
                f"subtitles='{srt_esc}':force_style='{sub_style}'",
                "-c:v",
                "libx264",
                "-pix_fmt",
                "yuv420p",
                "-an",
                str(burned),
            ]
        )

    # also copy soft-sub version without burn for editing
    soft = OUT / "FY301_研发原理讲解_软字幕.mp4"
    if has_voice and (work / "voice_all.mp3").exists():
        run(
            [
                FF,
                "-y",
                "-i",
                str(silent),
                "-i",
                str(work / "voice_all.mp3"),
                "-i",
                str(srt_path),
                "-map",
                "0:v",
                "-map",
                "1:a",
                "-map",
                "2",
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                "-c:s",
                "mov_text",
                "-metadata:s:s:0",
                "language=zho",
                "-shortest",
                str(soft),
            ]
        )
    else:
        run(
            [
                FF,
                "-y",
                "-i",
                str(silent),
                "-i",
                str(srt_path),
                "-map",
                "0:v",
                "-map",
                "1",
                "-c:v",
                "copy",
                "-c:s",
                "mov_text",
                "-metadata:s:s:0",
                "language=zho",
                "-an",
                str(soft),
            ]
        )

    print("DONE", burned, flush=True)
    print("SOFT", soft, flush=True)
    print("SRT", srt_path, flush=True)


if __name__ == "__main__":
    main()
