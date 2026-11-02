# 假设 M · 盘后定价通道误套全历史 / 竞价剩单自动进盘后（盘后补成交）

更新：2026-11-02  
来源：总管线 / L 风控四条已交后恢复写 M；清单实验 M  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「收盘价盘后一定能补上」当实盘预期；不抢实验 A 真数队列；L 不开回测）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 M 对齐。与假设 A（板上可成交，盘后默认关）、D（开/收时点）、G（无板日 PIT）、H（退市整理）、L（市价通道）、O（大宗/三条盘后通道）互补：本页专测**盘后固定价格通道**被当成「凡收盘价都能再补一笔」或「竞价剩单自动进 15:05」时，对可成交量与失败笔数的高估。**比较通道写死为盘后固定价格；禁止与深市盘后定价大宗、沪市大宗固定价格申报混成同一张主表却不标注通道（那是实验 O）。**

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1 下，把「收盘价总能再通过盘后固定价格补上一笔」当成默认成交（并可把竞价未成交部分自动记进 15:05），相对「每个交易日只用当日已生效通道、盘后必须另下一笔收盘定价申报、仍要有对手盘、停牌至 15:00 记失败」的 PIT 诚实组，会在主板扩围前、创业板注册制前**显著高估可成交量与盘后补成交贡献**；再把核对日现行「全 A+ETF 都有盘后」铺满全样本（泄露组），会在主板 `<2026-07-06`、创业板 `<2020-08-24`、北交所等切片进一步错标可成交。

证伪方向：若天真组 / 泄露组相对诚实组的盘后补成交贡献差、失败笔数差、（可选）净值差在标定噪声带内可忽略，且「主板 2026-07-06 前 / 创业板 2020-08-24 前 / 科创板 / 北交所」分桶不改变结论，则本假设在该样本与撮合设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 盘后固定价格通道（按成交日当时规则；未复权；与大宗分列）

```
# 配置写死（见 §7）
# params.asof_check_date              写死默认 2026-10-19  # 事实与坑盘后落地核对日；泄露组「现行」锚点
# params.star_aft_start               写死默认 2019-07-22  # 科创板开市首日；开市起即有盘后固定价格
# params.chinext_aft_start            写死默认 2020-08-24  # 创业板盘后定价落地（首只注册制创业板上市日）
# params.main_etf_aft_start           写死默认 2026-07-06  # 沪深主板 A 股 + ETF 扩围日
# params.bse_aft_on_20260706          写死默认 False      # 北交所 2026-07-06 暂不实施
# params.chinext_exit_exclude_on_cut  写死默认 True       # 2020-08-24 当日仍在退市整理期的存量创业板 → 整理期内不引入盘后
# params.sh_accept_start              写死默认 "09:30"    # 沪市盘后申报接受起算；禁写成 09:15
# params.sz_accept_start              写死默认 "09:15"    # 深市盘后申报接受起算
# params.match_window                 写死默认 "15:05-15:30"
# params.fill_time                     写死 next_close_plus_aft  # 信号默认仍可与 A/D 的 next_open 主腿分列；本页测的是「收盘后再补盘后」那一截
# params.primary_leg_fill_time        写死 next_open      # 主腿与 A/D 对齐；盘后为同日附加腿，不是次日
# params.m0_auto_roll_auction_remainder 写死默认 True     # 天真：竞价剩单自动进 15:05（发明通道）
# params.m1_auto_roll_auction_remainder 写死默认 False    # 诚实：必须另下收盘定价申报
# params.day_freq_mode                写死 channel_avail_plus_kappa  # 无独立盘后量时：只做通道可用性+κ敏感性，禁声称精确盘后复盘
# params.kappa                        写死默认 0.01       # 盘后可成量 ≤ floor(κ·当日竞价成交量) 占位；拉数前冻结
# params.opponent_policy              写死 kappa_cap|skip  # 本页默认 kappa_cap；无量/无对手 → skip
# params.diff_buckets                 写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2               写死具体数并冻结；禁 holdout 标定
# params.date_start / date_end        写死主窗并冻结
# params.oos_split.*                  写死四日期并冻结；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 fill_time·切日·auto_roll·kappa·Y/G/N/Y2·主窗/oos

tick = 0.01  # A 股股票默认；基金/ETF 价位另案，本页主样本股票
fill_primary = next_open
match_window = "15:05-15:30"
sh_accept_start = "09:30"
sz_accept_start = "09:15"
bse_aft_on_20260706 = False
chinext_exit_exclude_on_cut = True
day_freq_mode = "channel_avail_plus_kappa"
opponent_policy = "kappa_cap"
kappa = 0.01

def aft_channel_on(board, exchange, asof_date, in_exit_period_on_chinext_cut):
    # 北交所：扩围日仍无
    if exchange == "BJ" or board == "BSE":
        return False  # params.bse_aft_on_20260706=False；另行通知前保持 False
    # 科创板：开市起
    if board == "STAR":
        return asof_date >= params.star_aft_start
    # 创业板：2020-08-24 起；切日当日仍在整理期的存量整理股除外
    if board in ("ChiNext", "CYB"):
        if asof_date < params.chinext_aft_start:
            return False
        if (asof_date == params.chinext_aft_start
            and in_exit_period_on_chinext_cut
            and params.chinext_exit_exclude_on_cut):
            return False
        # 切日后若仍处整理期：本页默认仍按「整理期内不引入」只绑切日存量说明；
        # 切日之后新进整理期是否有盘后 → 未在本页另核，缺旗则 fail_policy=skip
        return True
    # 沪深主板 A 股（及 ETF 分桶）：2026-07-06 起
    if board in ("Main", "SH_Main", "SZ_Main"):
        return asof_date >= params.main_etf_aft_start
    return False  # 未知板块 → skip

def suspended_to_1500(i, t, suspend_flag):
    # 当日 15:00 仍停牌 → 不做盘后；已接受的收盘定价申报无效
    return suspend_flag.get((i, t), False)

def naive_aft_fill(side, close, intent_qty, day_vol):
    # M0：凡有收盘价就允许再按收盘价补一笔；可自动把竞价剩单滚进 15:05
    if close is None or close <= 0:
        return 0
    return intent_qty  # 无限量；不看通道、不看停牌、不看对手盘

def honest_aft_fill(side, close, intent_qty, day_vol, channel_on, susp_1500):
    if not channel_on or susp_1500 or close is None or close <= 0:
        return 0  # fail / skip
    # 必须另下收盘定价申报（auto_roll=False）；买限价≥收盘、卖限价≤收盘才有效——日频默认按「限价=收盘」可进簿
    if params.opponent_policy == "skip":
        return 0 if (day_vol is None or day_vol <= 0) else min(intent_qty, intent_qty)  # 有量才试；精确对手未知
    # kappa_cap：盘后可成 ≤ floor(κ · 当日成交量占位)；无独立盘后量时禁止声称精确复盘
    if day_vol is None or day_vol <= 0:
        return 0
    cap = int(params.kappa * day_vol)
    return max(0, min(intent_qty, cap))
```

- **PIT 诚实（M1）**：每个交易日只用当日已生效通道（科创开市起 / 创业板 `2020-08-24` / 主板+ETF `2026-07-06`；北交所该日仍无）。盘后 = **单独的收盘定价申报**，竞价剩单**不**自动进 15:05。撮合窗 **15:05–15:30**，按**当日未复权收盘价、时间优先**。停牌至 15:00 → 失败。仍要有对手盘（日频用 `opponent_policy`+`kappa`，禁假装无限量）。盘后仍是**当日**成交，**不**改变股票 T+1，**不**绕开涨停。  
- **天真（M0）**：凡收盘价都允许按收盘价再成交一笔盘后量；`m0_auto_roll_auction_remainder=True`（发明通道）。可忽略板块切日与停牌。  
- **泄露（M2）**：全样本用核对日现行「全 A + ETF 都有盘后」（`asof_check_date=2026-10-19` 锚点），含主板 `<2026-07-06`、创业板 `<2020-08-24`、甚至北交所错标。  
- **申报窗诊断（非主对照改口项）**：沪市接受盘后单自 **09:30**；深市自 **09:15**。误把沪市写成 09:15 起算 → 计入 `sh_accept_mislabel_0915` 诊断桶，**不**改主结论定义。  
- **与 O 分列**：O = 大宗量价 / 盘后定价大宗 / 沪市大宗固定价格；M = **股票盘后固定价格**通道。主报告分表。  
- **禁止**：用复权收盘价；把盘后当成绕开涨停或绕开 T+1；北交所 2026-07-06 写成已开通；竞价剩单默认滚进 15:05 却标成诚实；与 O 混主表不标注；把差异写成选股。

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺交易所/板块、缺切日无法判通道、创业板切日整理期旗缺失却硬开通道、15:00 停牌旗缺失却当成可盘后、把北交所硬开盘后 → **跳过该盘后腿**，不按收盘价假补仓。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 三组对照（本实验编码）

| 组 | 通道假设 | 竞价剩单 | 停牌至 15:00 / 对手盘 |
|----|----------|----------|----------------------|
| M0 天真-收盘必补 | 凡有收盘价即可盘后补一笔 | **自动滚进 15:05**（`m0_auto_roll=True`） | 不停牌挡；无限量 |
| M1 PIT 诚实 | **每个交易日**用当日已生效通道；无通道→盘后腿 skip | **必须另下**收盘定价申报（`m1_auto_roll=False`） | 停牌→失败；`opponent_policy=kappa_cap`（默认） |
| M2 泄露-现行铺满 | 全样本抄核对日「全 A+ETF 有盘后」 | 可与 M0 同或单独声明；本页默认**不**自动滚，只测通道泄露 | 同 M1 的停牌/对手盘开关，避免与通道泄露缠死 |

同一信号、同一 T+1、同一成本开关（本页可先零成本只比盘后通道差）。**主腿**成交时点 **`primary_leg_fill_time=next_open` 写死**（与 A/D 对齐）；**盘后附加腿**在信号日/成交日**当日** 15:05–15:30（若通道开）。禁止把盘后腿报成「次日开盘」。

**`params.day_freq_mode`（写死；拉数前冻结）**：`channel_avail_plus_kappa`——无独立「盘后成交量」字段时，只报通道可用性差、失败笔数、κ 敏感性；**禁止**声称精确盘后吃单复盘。有独立盘后量字段时可增强，但不得事后改主结论口径。

**`params.kappa`（写死默认；拉数前冻结）**：`0.01`。用于 M1/M2 对手盘帽；**禁 holdout 改 κ**。

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股股票。不含可转债主样本；股票 ETF 仅作 `board_etf_post_20260706` 诊断/稳健分桶（ETF 扩围同日，但不进主宇宙权重）。北交所若入样本，只用于证明 `bse_aft_on_20260706=False`，默认**不**进主宇宙。  
- **排除（默认）**：调仓日未上市；成交日缺收盘价或无法识别交易所/板块；把深市盘后定价大宗腿误标成盘后固定价格。  
- **股票池 PIT**：每个调仓日只用当日已生效名单（可与实验 C 共用）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2020-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖创业板 `2020-08-24` 与主板/ETF `2026-07-06` 前后，并含科创开市后样本。  
  - 稳健分桶：见 `params.diff_buckets`。  
- **PIT 切片原则**：该日该板块是否有盘后固定价格、申报窗、停牌是否挡盘后，一律按成交日当时规则。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2020-01-01
params.oos_split.is_end         = 2025-12-31
params.oos_split.holdout_start  = 2026-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调切日、三组定义、`kappa`、`auto_roll`、显著性阈值或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。holdout 含 `2026-07-06` 主板扩围，便于一次性观察泄露/天真在扩围前后的差，**不是**用来回改 M1 定义。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **M0 ? M1**：天真「收盘必补 + 剩单自动进盘后」相对 PIT 诚实——盘后补成交量/贡献差、失败笔数差、（可选）净值差。  
2. **M2 ? M1**：现行全 A+ETF 铺满相对 PIT——看主板 `<2026-07-06`、创业板 `<2020-08-24`、北交所是否被系统性错标。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "main_pre_20260706",           # 沪深主板扩围前（M1 应无盘后；M0/M2 易错成）
  "chinext_pre_20200824",        # 创业板注册制/盘后前
  "chinext_exit_on_20200824",    # 切日当日仍在整理期的存量创业板
  "board_star",                  # 科创板（开市起应有）
  "bse_on_or_after_20260706",    # 北交所（应仍无）
  "suspend_to_1500",             # 停牌至 15:00（M1 应失败）
  "auto_roll_remainder",         # 竞价剩单自动进盘后（仅 M0 发明）
  "sh_accept_mislabel_0915",     # 沪市误从 09:15 起算（诊断桶）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 盘后补成交贡献差 ΔAft（量或对该腿收益贡献）；  
2. 失败/跳过笔数差 ΔFail（无通道、停牌、无对手）；  
3. 净值差 ΔNAV（M0?M1、M2?M1）——**可选**，有信号臂时才报，不得单独当「能买」证据。

**相对判据（草稿）**：若 |ΔAft| **≥ G** 或 |ΔFail| **≥ N** 或 |ΔNAV| **≥ Y**，记「盘后通道执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 净值差显著门槛 | **写死** `params.Y=0.02` 并冻结 |
| G | 盘后补成交贡献/量差门槛 | **写死** `params.G=0.01` 并冻结 |
| N | 失败笔数率差门槛 | **写死** `params.N=0.05` 并冻结 |
| Y2 | 稳健子窗净值差门槛（可选） | **写死** `params.Y2=0.015` 并冻结 |
| asof_check_date | 泄露组「现行」核对日 | **写死默认** `2026-10-19`；拉数前冻结 |
| star_aft_start | 科创盘后起 | **写死默认** `2019-07-22` |
| chinext_aft_start | 创业板盘后起 | **写死默认** `2020-08-24` |
| main_etf_aft_start | 主板+ETF 扩围 | **写死默认** `2026-07-06` |
| kappa | 对手盘量帽 | **写死默认** `0.01` |
| fill / primary | 时点 | **写死** `primary_leg_fill_time=next_open` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**`params.Y` / `params.G` / `params.N` / `params.Y2` 写入冻结（具体数已写入；禁继续 null；禁 holdout 标定）**：

```
# 纸面冻结默认（机制实验相对门槛；一经写入即冻结）
# 单位：Y/Y2 = abs(ΔNAV) 年化；G = abs(ΔAft) 相对（盘后腿贡献或量占比）；N = abs(ΔFail) 失败率（小数）
params.Y  = 0.02    # 净值差显著门槛 ≥ 2pp 年化
params.G  = 0.01    # 盘后补成交贡献差门槛 ≥ 1pp
params.N  = 0.05    # 失败率差门槛 ≥ 5pp
params.Y2 = 0.015   # 稳健子窗净值差门槛 ≥ 1.5pp 年化
```

门槛已在纸面写入并冻结；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、切日、`kappa`、`auto_roll`、主窗/`oos_split` 开工拉数前必须保持冻结；**禁止跑后改口**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「盘后通道无关」或「收盘价一定能补上」。

结论栏：空。跑完只写「该假设下差多少」，不写「这类票因盘后能买/该规避」。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验盘后固定价格通道 / 竞价剩单是否自动进盘后**，**不为组合策略放行实盘**。

- **显式豁免**：数值红线 v0（单票仓位、行业集中、回撤熔断等组合约束）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权、PIT 切日、禁 holdout 反调、禁荐股/禁当实盘预期、日频不假装精确盘后复盘、禁把盘后当绕开涨停/T+1、禁北交所假开通）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **主板/ETF `<2026-07-06` 进 M1 却开盘后**：该段属 M0/M2 敏感，不是 M1。  
2. **创业板 `<2020-08-24` 开盘后**，或切日当日仍在整理期的存量创业板被写成已引入盘后。  
3. **北交所 2026-07-06 写成已开通盘后**。  
4. **竞价剩单自动进 15:05 却标成诚实（M1）**：发明通道；仅允许出现在 M0。  
5. **停牌至 15:00 仍记盘后成交**。  
6. **用复权收盘价撮合**。  
7. **把盘后当成绕开涨停或绕开 T+1**。  
8. **与实验 O（大宗/盘后定价大宗/沪市大宗固定价格）混报主结论且不标注通道**。  
9. **无独立盘后量却报「精确盘后复盘」**。  
10. **宇宙泄露 / holdout 反调**：看完 OOS 再改切日、`kappa` 或 `auto_roll`。  
11. **把差异写成选股/「这类票能买」**。  
12. **沪市盘后申报误从 09:15 起算却不进诊断桶**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | |
| exchange (SH/SZ/BJ) | 通道与申报窗路由 | **必填** |
| board / market | 科创/主板/创业/北交 | 按日 PIT |
| close（未复权） | 盘后撮合价 | **禁复权** |
| volume / amount | κ 帽；是否含盘后须注明 | 切日之后日总量才含盘后 |
| volume_auction_only（可选） | 更干净的 κ 分母 | **非纸面最小集** |
| volume_aft（可选） | 独立盘后量 | 有则可增强；无则 channel_avail_plus_kappa |
| is_suspended_to_1500 / tradable_flag | 挡盘后 | 勿用收益=0 代替 |
| in_exit_period | 创业板切日整理期除外 | 可与假设 H 共用 |
| list_date | 宇宙 / 科创开市后样本 | |
| 信号表（可选） | 选股臂 | 无信号可先跑「盘后腿 × 通道标签」差 |
| 盘后通道规则表 | 切日与接受窗 | 可用本页 §2.1 编码，不必新开数据商 |

**明确**：不依赖聚宽；**不要求新开盘后分笔数据商**——日频未复权收盘 + 交易所/板块 + 停牌旗 + 本页切日表即可起步「通道可用性 + κ 敏感性」。独立盘后量/委托簿为增强项。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=M`，`groups=[M0,M1,M2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-19`**，**`params.star_aft_start=2019-07-22`**，**`params.chinext_aft_start=2020-08-24`**，**`params.main_etf_aft_start=2026-07-06`**，**`params.bse_aft_on_20260706=False`**，**`params.chinext_exit_exclude_on_cut=True`**，**`params.sh_accept_start=09:30`**，**`params.sz_accept_start=09:15`**，**`params.match_window=15:05-15:30`**，**`params.primary_leg_fill_time=next_open`（写死）**，**`params.m0_auto_roll_auction_remainder=True`**，**`params.m1_auto_roll_auction_remainder=False`**，**`params.day_freq_mode=channel_avail_plus_kappa`**，**`params.opponent_policy=kappa_cap`**，**`params.kappa=0.01`（写死默认；拉数前冻结）**，**`params.diff_buckets=[main_pre_20260706,chinext_pre_20200824,chinext_exit_on_20200824,board_star,bse_on_or_after_20260706,suspend_to_1500,auto_roll_remainder,sh_accept_mislabel_0915]`（写死默认；拉数前冻结）**，**`params.Y=0.02` / `params.G=0.01` / `params.N=0.05` / `params.Y2=0.015`（写死具体数并冻结；禁 holdout 标定；禁 null）**，`universe_rule`，**`params.date_start=2020-01-01` / `params.date_end=2026-09-30`（写死；覆盖 2020-08-24 与 2026-07-06）**，**`oos_split.{is_start=2020-01-01,is_end=2025-12-31,holdout_start=2026-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；见 §4.3），`overlay_A=off`（默认 off；A 盘后默认关，叠加须声明），`overlay_H=on`（建议 on：整理期旗共用），`overlay_O=off`（默认 off；大宗分表），`cost_switch=off`（M 主跑）。  
- 行情与规则表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- M0/M1/M2 盘后补成交贡献、失败笔数、（可选）净值；分桶（主板扩围前 / 创业板切日前 / 切日整理期 / 科创 / 北交所 / 停牌 / auto_roll / 沪市 09:15 误标）。  
- 自检布尔：是否未复权；是否 PIT 切日；北交所是否未假开通；M1 是否禁 auto_roll；停牌至 15:00 是否失败；是否未把盘后当绕开涨停/T+1；是否未与 O 混主表；`kappa`/切日是否已冻结；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把天真盘后必成当实盘预期；催跑抢 A 真数队列。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**L 不开回测**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` 一致：盘后固定价格按板块落地（不是 2026-07-06 起全历史都有）；申报当日有效、竞价剩单不自动变盘后单；盘后仍当日成交、不改 T+1。与 `事实与坑.md` 2026-10-19 条一致：科创开市起；创业板 2020-08-24（整理期除外）；主板+ETF 2026-07-06；北交所该日暂不实施；15:05–15:30 收盘价时间优先；停牌至 15:00 不做；沪市申报自 09:30、深市自 09:15。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 M 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A/D/E/F/G/H/I/J/K/L 正文**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权收盘 + 交易所/板块 + 停牌旗 + 切日表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；L 不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2020-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免；asof_check_date=2026-10-19 / star_aft_start=2019-07-22 / chinext_aft_start=2020-08-24 / main_etf_aft_start=2026-07-06 / bse_aft_on_20260706=False / chinext_exit_exclude_on_cut=True；**primary_leg_fill_time=next_open 写死**；**m0_auto_roll=True / m1_auto_roll=False**；**day_freq_mode=channel_avail_plus_kappa**；**opponent_policy=kappa_cap / kappa=0.01 写死冻结**；diff_buckets 八桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死具体数并冻结、禁 holdout 标定、禁 null** |

---

## 变更

- 2026-11-02：新建标准件（总管线：L 风控四条已交后恢复写 M；选型对齐清单实验 M；机制类预埋 fail_policy/oos/红线豁免/params 冻结；**不抢实验 A**；**不派回测**；**L 不开回测**）。
