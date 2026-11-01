# 聚宽 jqdatasdk 安装/鉴权草稿（DRAFT · 未执行）

> 总管令：凭据就绪前 **不要** pip install、**不要** uth。本文件仅命令草稿。

## 1. 安装（待令后执行）

`	ext
python -m pip install -U jqdatasdk
python -c "import jqdatasdk as jq; print(jq.__version__)"
`

## 2. 鉴权形态（本地 sdk）

`	ext
python -c "from jqdatasdk import auth; auth(\"<手机或邮箱>\", \"<密码>\"); print(\"ok\")"
`

- 凭据来源：Vault / Secure Form（一次性）；**禁止**把密码写进本仓库任何文件。
- 成功后再跑最小拉数脚本（另开，仍限 ≤3 个月、极少票）。

## 3. 本实验约定（提醒）

- vendor=聚宽；禁实盘/荐股/holdout 反调
- 字段：未复权 OHLC、前收盘/除权参考、板块/ST、上市日、退市整理窗、停牌/无成交、成交量
- 落盘：data/ + 更新 data_manifest.txt（as_of、哈希）

## 4. 状态

- 草稿写入：2026-10-31
- install：未执行
- auth：未执行
