# 假设 N · 沪市收盘价产生方式误套 + 限价单隔夜有效（收盘机制与假 GTC）

更新：2026-11-02  
来源：总管线 / M 草稿已收后写 N；清单实验 N  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「收盘=14:57 集合 / 限价隔夜 GTC」当实盘预期；不抢实验 A 真数队列；本页不开回测；M 预检回来后优先补 M，不由本页抢）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 N 对齐。与假设 D（开/收时点）、M（盘后补成交 / 竞价剩单不自动进盘后）、L（市价通道）、O（大宗通道）互补：本页专测两件事——（1）把现行「收盘=14:57 集合竞价」误套到 **沪市股票 `<2018-08-20`** 或 **沪市基金/ETF `<2026-07-06`**；（2）把未成交限价当成 **次日仍在簿上（假 GTC）**。**深市股票收盘集合竞价更早切日本页不写死**（事实与坑未核到官方首日）。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1 下，把全样本收盘价都当成「14:57 收盘集合竞价一次价」，并把未成交限价单留到次日开盘继续排队（假 GTC），相对「每个交易日按当时收盘产生方式使用收盘价、未成交限价当日作废且次日必须重新申报」的 PIT 诚实组，会在沪市股票 `<2018-08-20`、沪市基金/ETF `<2026-07-06` 切片**显著错标尾盘冲击形态**，并在隔夜跳空样本上**高估排队成交 / 假 GTC 吃到的那截**；再把核对日现行收盘机制铺满全样本（泄露组），会进一步放大误套。

证伪方向：若天真组 / 泄露组相对诚实组的净值差、隔夜跳空差、假 GTC 贡献差在标定噪声带内可忽略，且「沪市股票 2018-08-20 前 / 沪市基金 2026-07-06 前 / 深市对照」分桶不改变结论，则本假设在该样本与撮合设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 收盘价产生方式 + 限价有效期（按成交日当时规则；未复权）

```
# 配置写死（见 §7）
# params.asof_check_date              写死默认 2026-10-19  # 事实与坑核对日；泄露组「现行」锚点
# params.sh_stock_close_auction_start 写死默认 2018-08-20  # 沪市股票收盘改 14:57–15:00 集合竞价
# params.sh_fund_close_auction_start  写死默认 2026-07-06  # 沪市基金/ETF 尾盘改收盘集合竞价
# params.sz_stock_close_auction_start 写死默认 None / leave_unsliced  # 深市更早切日未核 → 不写死具体日
# params.close_mech_mode              写死 pit_by_exch_sec_type
# params.fill_time                     写死 next_close      # 本页主测收盘腿；与 D 的开/收对照互补，不抢 A 的 next_open 主队列
# params.n0_treat_all_close_as_auction 写死默认 True   # 天真：全样本收盘=集合竞价一次成交
# params.n0_limit_gtc                 写死默认 True   # 天真：未成交限价留到次日开盘
# params.n1_limit_day_only            写死默认 True   # 诚实：申报当日有效；次日须重报
# params.n1_no_auto_aft               写死默认 True   # 诚实：未成交限价不自动进盘后（与 M 一致）
# params.fake_gtc_fill_proxy          写死 next_open_if_touched  # 日频假 GTC 代理：次日开盘价触及原限价则记「假成交」；禁假装精确簿上排队
# params.diff_buckets                 写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2               写死具体数并冻结；禁 holdout 标定
# params.date_start / date_end        写死主窗并冻结
# params.oos_split.*                  写死四日期并冻结；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 fill_time·切日·假GTC代理·Y/G/N/Y2·主窗/oos

tick = 0.01  # A 股股票默认；基金/ETF 价位另案，本页主样本可含沪市基金桶但须分列
fill_time = "next_close"
asof_check_date = "2026-10-19"
sh_stock_close_auction_start = "2018-08-20"
sh_fund_close_auction_start = "2026-07-06"
sz_stock_close_auction_start = None  # leave_unsliced：深市切日未核，不写死
fake_gtc_fill_proxy = "next_open_if_touched"

def close_mech(exch, sec_type, asof_date):
    # 返回: "closing_auction_1457" | "continuous_last_min_vwap" | "unknown_skip"
    if exch == "SH" and sec_type in ("stock", "A_share"):
        if asof_date >= sh_stock_close_auction_start:
            return "closing_auction_1457"
        return "continuous_last_min_vwap"  # 2018-08-20 前尾盘连续；收盘=最后一分钟加权类定义
    if exch == "SH" and sec_type in ("fund", "ETF"):
        if asof_date >= sh_fund_close_auction_start:
            return "closing_auction_1457"
        return "continuous_last_min_vwap"  # 2026-07-06 前基金尾盘仍连续
    if exch == "SZ" and sec_type in ("stock", "A_share"):
        # 深市股票收盘集合更早，但官方首日未核 → 本页不写死切日；
        # 对照桶可报「深市现行集合」诊断，禁把随便一天填进 params
        if sz_stock_close_auction_start is None:
            return "sz_stock_unsliced_diagnostic"
        if asof_date >= sz_stock_close_auction_start:
            return "closing_auction_1457"
        return "unknown_skip"
    if exch == "SZ" and sec_type in ("fund", "ETF"):
        # 事实与坑：深市基金尾盘此前已是集合；2026 修订不作变更 → 本页默认按集合诊断，不另造切日
        return "closing_auction_1457"
    return "unknown_skip"

def naive_close_fill(intent_qty, close):
    # N0：凡有收盘价 → 一律当 14:57 集合一次价全成
    if close is None or close <= 0:
        return 0
    return intent_qty

def honest_close_fill(intent_qty, close, mech):
    if mech in ("unknown_skip",) or close is None or close <= 0:
        return 0  # fail_policy=skip
    # 日频：诚实组仍可用当日未复权收盘价成交，但必须打上 mech 标签；
    # 禁止把 continuous_last_min_vwap 样本的冲击/跳空统计并进 closing_auction_1457 主桶
    return intent_qty

def naive_gtc_carry(unfilled_qty, limit_px, next_open):
    # N0 假 GTC：未成交限价留到次日；代理 = 次日开盘触及则「吃到」
    if unfilled_qty <= 0 or limit_px is None or next_open is None:
        return 0
    # 买：next_open <= limit；卖：next_open >= limit（方向由 side 传入；此处示意）
    return unfilled_qty  # 天真甚至可不看触及，直接全留次日——本页默认仍用 touched 代理以便可比

def honest_day_only(unfilled_qty):
    # N1：当日有效；未成交作废；次日必须重新申报 → 假 GTC 贡献 = 0
    return 0
```

- **PIT 诚实（N1）**：
  - 沪市股票：`≥2018-08-20` 收盘=14:57–15:00 集合竞价；此前按当时尾盘连续/最后一分钟加权类定义使用收盘价，**不**假设 14:57 集合。
  - 沪市基金/ETF：`≥2026-07-06` 才与股票对齐为收盘集合；此前尾盘连续，**不**按股票收盘集合处理。
  - 深市股票收盘集合更早切日：**不写死**；诊断桶可对照，禁随便填日。
  - 限价：**当日有效**；未成交只进**当日**后续竞价；**不隔夜**；**不**自动变盘后单（与 M 一致）。次日必须重新申报。
  - 9:20–9:25、14:57–15:00 不可撤单 = **当日**该时段约束，**不是**把有效期延长到次日。
- **天真（N0）**：全样本收盘价当集合竞价一次成交；未成交限价留到次日开盘（假 GTC）。
- **泄露（N2）**：全样本用核对日现行收盘机制（`asof_check_date=2026-10-19`：沪市股票/基金均已是 14:57 集合），铺到切日前样本。
- **禁止**：用复权收盘价；深市股票收盘集合切日随便填；把 9:20–9:25 不可撤单写成隔夜有效；把假 GTC 写成选股；与 M 的「剩单进盘后」混成同一主结论却不标注（M=盘后通道；N=收盘机制+隔夜有效期）。

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺交易所/证券类别、深市切日未核却硬按某日切片、收盘价缺失、无法判 mech → **跳过该腿**，不按 14:57 集合假成、不按假 GTC 留仓。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 三组对照（本实验编码）

| 组 | 收盘机制假设 | 未成交限价 |
|----|--------------|------------|
| N0 天真-全集合+假GTC | 全样本收盘=14:57 集合一次成交 | **留到次日开盘**（`n0_limit_gtc=True`） |
| N1 PIT 诚实 | **每个交易日**按交易所×证券类别×切日判 mech；沪股 `<2018-08-20` / 沪基 `<2026-07-06` 不按集合 | **当日有效**；作废；次日重报（`n1_limit_day_only=True`）；不自动进盘后 |
| N2 泄露-现行铺满 | 全样本抄核对日现行（股票+沪市基金均已集合） | 本页默认与 N1 同（只测机制泄露）；若开假 GTC 须另声明且不得标成诚实 |

同一信号、同一 T+1、同一成本开关（本页可先零成本只比机制差）。**`params.fill_time=next_close` 写死**（本页主测收盘腿；与假设 D 开/收对照互补）。禁止把假 GTC 腿报成「诚实排队」。

**`params.fake_gtc_fill_proxy`（写死；拉数前冻结）**：`next_open_if_touched`——日频无真实委托簿时，只做「次日开盘触及原限价」敏感性；**禁止**声称精确隔夜簿上排队复盘。

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股股票为主；沪市基金/ETF 作 `sh_fund_pre_20260706` 分桶（可进对照，不强制进主权重）。不含可转债主样本（那是实验 Q）。  
- **排除（默认）**：调仓日未上市；成交日缺未复权收盘价或无法识别交易所/证券类别；把深市切日随便填进主结论。  
- **股票池 PIT**：每个调仓日只用当日已生效名单（可与实验 C 共用）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2017-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖沪市股票 `2018-08-20` 与沪市基金 `2026-07-06` 前后。  
  - 稳健分桶：见 `params.diff_buckets`。  
- **PIT 切片原则**：该日该交易所该证券类别收盘价如何产生、限价是否当日有效，一律按成交日当时规则。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2017-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调切日、三组定义、假 GTC 代理、显著性阈值或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。holdout 含 `2026-07-06` 沪市基金收盘机制切换，便于一次性观察泄露/天真在切日前后的差，**不是**用来回改 N1 定义。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **N0 ? N1**：天真「全集合 + 假 GTC」相对 PIT 诚实——净值差、隔夜跳空差、假 GTC 贡献差、失败/跳过笔数差。  
2. **N2 ? N1**：现行收盘机制铺满相对 PIT——看沪市股票 `<2018-08-20`、沪市基金 `<2026-07-06` 是否被系统性错标。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "sh_stock_pre_20180820",      # 沪市股票切日前（尾盘连续；N1 不按 14:57 集合）
  "sh_stock_post_20180820",     # 沪市股票切日后（应收盘集合）
  "sh_fund_pre_20260706",       # 沪市基金/ETF 切日前
  "sh_fund_post_20260706",      # 沪市基金/ETF 切日后
  "sz_stock_diagnostic",        # 深市股票（切日未核；只诊断，不进主切日结论）
  "fake_gtc_overnight_gap",     # 假 GTC × 隔夜跳空（N0 敏感）
  "no_cancel_0920_or_1457",     # 误把当日不可撤单写成隔夜有效（诊断桶）
  "vs_M_auto_roll_aft",         # 与 M「剩单进盘后」分列诊断（禁混主表）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 净值差 ΔNAV（N0?N1、N2?N1）；  
2. 隔夜跳空差 ΔGap（假 GTC / 机制误套对开盘跳空的抹平或错标）；  
3. 假 GTC 贡献差 ΔGTC（被「留到次日」吃到的那截量或收益）；  
4. 失败/跳过笔数差 ΔFail（mech 未知、缺字段）。

**相对判据（草稿）**：若 |ΔNAV| **≥ Y** 或 |ΔGap| / |ΔGTC| **≥ G** 或 |ΔFail| **≥ N**，记「收盘机制 / 假 GTC 执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 净值差显著门槛 | **写死** `params.Y=0.02` 并冻结 |
| G | 隔夜跳空差 / 假 GTC 贡献差门槛 | **写死** `params.G=0.01` 并冻结 |
| N | 失败笔数率差门槛 | **写死** `params.N=0.05` 并冻结 |
| Y2 | 稳健子窗净值差门槛（可选） | **写死** `params.Y2=0.015` 并冻结 |
| asof_check_date | 泄露组「现行」核对日 | **写死默认** `2026-10-19`；拉数前冻结 |
| sh_stock_close_auction_start | 沪市股票收盘集合起 | **写死默认** `2018-08-20` |
| sh_fund_close_auction_start | 沪市基金收盘集合起 | **写死默认** `2026-07-06` |
| sz_stock_close_auction_start | 深市股票切日 | **写死** `None` / `leave_unsliced`；禁随便填日 |
| fill_time | 成交时点 | **写死** `next_close` |
| fake_gtc_fill_proxy | 假 GTC 日频代理 | **写死** `next_open_if_touched` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**`params.Y` / `params.G` / `params.N` / `params.Y2` 写入冻结（具体数已写入；禁继续 null；禁 holdout 标定）**：

```
# 纸面冻结默认（机制实验相对门槛；一经写入即冻结）
# 单位：Y/Y2 = abs(ΔNAV) 年化；G = abs(ΔGap) 或 abs(ΔGTC) 相对；N = abs(ΔFail) 失败率（小数）
params.Y  = 0.02    # 净值差显著门槛 ≥ 2pp 年化
params.G  = 0.01    # 隔夜跳空/假GTC贡献差门槛 ≥ 1pp
params.N  = 0.05    # 失败率差门槛 ≥ 5pp
params.Y2 = 0.015   # 稳健子窗净值差门槛 ≥ 1.5pp 年化
```

门槛已在纸面写入并冻结；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、切日、假 GTC 代理、主窗/`oos_split` 开工拉数前必须保持冻结；**禁止跑后改口**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「收盘机制无关」或「限价可以隔夜」。

结论栏：空。跑完只写「该假设下差多少」，不写「这类票因收盘集合/假 GTC 能买/该规避」。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验收盘价产生方式误套 + 限价当日有效（反假 GTC）**，**不为组合策略放行实盘**。

- **显式豁免**：数值红线 v0（单票仓位、行业集中、回撤熔断等组合约束）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权、PIT 切日、禁 holdout 反调、禁荐股/禁当实盘预期、日频不假装精确簿上排队、禁把不可撤单写成隔夜、禁深市切日瞎填）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **沪市股票 `<2018-08-20` 进 N1 却按 14:57 集合**：该段属 N0/N2 敏感，不是 N1。  
2. **沪市基金/ETF `<2026-07-06` 按股票收盘集合处理**。  
3. **深市股票收盘集合切日随便填进 params 并进主结论**（本页 `leave_unsliced`）。  
4. **未成交限价隔夜 / 假 GTC 却标成诚实（N1）**：发明规则；仅允许出现在 N0。  
5. **把 9:20–9:25 或 14:57–15:00 不可撤单写成隔夜有效**。  
6. **用复权收盘价撮合**。  
7. **与实验 M（竞价剩单自动进盘后）混报主结论且不标注**：M=盘后通道；N=收盘机制+有效期。  
8. **无委托簿却报「精确隔夜排队复盘」**。  
9. **宇宙泄露 / holdout 反调**：看完 OOS 再改切日、假 GTC 代理或显著性门槛。  
10. **把差异写成选股/「这类票能买」**。  
11. **把可转债收盘规则套进本页主样本**（那是实验 Q）。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | |
| exchange (SH/SZ) | 收盘机制路由 | **必填** |
| sec_type (stock/fund/ETF) | 沪市股票 vs 基金切日 | **必填**（ETF 归 fund 桶） |
| close（未复权） | 收盘腿成交价 | **禁复权** |
| open（未复权，次日） | 假 GTC 触及代理 / 隔夜跳空 | 日频最小集 |
| high/low（可选） | 增强触及判定 | **非纸面最小集** |
| board / market | 分桶稳健 | 按日 PIT |
| list_date | 宇宙 | |
| 信号表（可选） | 选股臂 | 无信号可先跑「收盘机制标签 × 假GTC开关」差 |
| 收盘机制规则表 | 切日 | 可用本页 §2.1 编码，不必新开数据商 |

**明确**：不依赖聚宽；**不要求新开 L2/委托簿数据商**——日频未复权 OHLC + 交易所/证券类别 + 本页切日表即可起步「机制可用性 + 假 GTC 触及敏感性」。真实簿上排队为增强项。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=N`，`groups=[N0,N1,N2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-19`**，**`params.sh_stock_close_auction_start=2018-08-20`**，**`params.sh_fund_close_auction_start=2026-07-06`**，**`params.sz_stock_close_auction_start=None`（leave_unsliced；禁随便填日）**，**`params.close_mech_mode=pit_by_exch_sec_type`**，**`params.fill_time=next_close`（写死）**，**`params.n0_treat_all_close_as_auction=True`**，**`params.n0_limit_gtc=True`**，**`params.n1_limit_day_only=True`**，**`params.n1_no_auto_aft=True`**，**`params.fake_gtc_fill_proxy=next_open_if_touched`（写死；拉数前冻结）**，**`params.diff_buckets=[sh_stock_pre_20180820,sh_stock_post_20180820,sh_fund_pre_20260706,sh_fund_post_20260706,sz_stock_diagnostic,fake_gtc_overnight_gap,no_cancel_0920_or_1457,vs_M_auto_roll_aft]`（写死默认；拉数前冻结）**，**`params.Y=0.02` / `params.G=0.01` / `params.N=0.05` / `params.Y2=0.015`（写死具体数并冻结；禁 holdout 标定；禁 null）**，`universe_rule`，**`params.date_start=2017-01-01` / `params.date_end=2026-09-30`（写死；覆盖 2018-08-20 与 2026-07-06）**，**`oos_split.{is_start=2017-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；见 §4.3），`overlay_D=on`（建议 on：开/收时点对照共用），`overlay_M=off`（默认 off；盘后剩单分表），`overlay_A=off`，`cost_switch=off`（N 主跑）。  
- 行情与规则表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- N0/N1/N2 净值、隔夜跳空、假 GTC 贡献、失败笔数；分桶（沪股切日前/后、沪基切日前/后、深市诊断、假GTC×跳空、不可撤单误标、vs M）。  
- 自检布尔：是否未复权；是否 PIT 切日；沪基 2026-07-06 前是否未按股票集合；深市切日是否未瞎填；N1 是否禁假 GTC；是否未把不可撤单写成隔夜；是否未与 M 混主表；切日/代理是否已冻结；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把天真全集合/假 GTC 当实盘预期；催跑抢 A 真数队列。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；M 预检回来后优先补 M，不由本页抢。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` 一致：收盘价产生方式要按当时规则切片；申报当日有效、未成交不隔夜、不自动进盘后。与 `事实与坑.md` 2026-10-19 条一致：沪市股票 2018-08-20 起 14:57 集合；沪市基金 2026-07-06 才改；深市股票更早切日未核不写死；9:20–9:25 / 14:57–15:00 不可撤单管当日不是隔夜。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 N 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A/D/E/F/G/H/I/J/K/L/M 正文**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权 OHLC + 交易所/证券类别 + 切日表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2017-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免；asof_check_date=2026-10-19 / sh_stock_close_auction_start=2018-08-20 / sh_fund_close_auction_start=2026-07-06 / sz_stock_close_auction_start=None(leave_unsliced)；**fill_time=next_close 写死**；**n0 全集合+假GTC / n1 当日有效+不进盘后**；**fake_gtc_fill_proxy=next_open_if_touched 写死冻结**；diff_buckets 八桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死具体数并冻结、禁 holdout 标定、禁 null** |

---

## 变更

- 2026-11-02：新建标准件（总管线：M 草稿已收后写 N；选型对齐清单实验 N；机制类预埋 fail_policy/oos/红线豁免/params 冻结；**不抢实验 A**；**不派回测**；**本页不开回测**；M 预检回来后优先补 M）。
