# 假设 AY · 基金/ETF 最小价位误套股票 0.01（执行鸿沟 / 回测诚信）

更新：2026-11-03  
来源：总管线 / AX 补丁已收、写下一纸面 AY；清单撞题规则另选正交微观结构缺口（基金 tick≠股票 tick）；选题自 `事实与坑`「A 股默认最小价位 0.01；基金是 0.001，不要和股票混用」；与假设 A（板上可成交）/ H（退市整理）/ Y（集合竞价量计入日线；**实验字母 Y ≠ 本页 AY**）/ E（整手与科创 200）/ F（**股票**涨跌停价取整；`tick=0.01` 仅 A 股股票、禁基金 0.001 进 F 主表）/ M（盘后）/ O（大宗）/ N（收盘切日/假 GTC）/ Q（可转债；债 tick 0.001 另档）/ R（股票 ETF 假回转）/ S/T/U/V（费用层）/ W（除权判板）/ L（市价通道）/ I（价格笼子）/ AX（**ETF 基金经手费**；费用≠价位）/ AW（收盘集合失败回落）/ AN–AV 等**分列**；**新建实验 AY**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「基金/ETF 也按股票 0.01 元取整 / 或把股票腿发明成 0.001」当诚实价位；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AX 及其他 A/D–AX 已交正文与冻结补丁；不改假设-H；不改假设-F；不改假设-E；不改假设-Q；不改假设-AX；不改假设-AW；勿再改 AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` 对齐；清单开跑前下一序号挂实验 AY。与假设 **F（股票涨跌停价取整）** **硬分列**：F = 未复权前收盘×板幅后按 **股票 tick=0.01** 四舍五入判板；F 已写死 `tick=0.01` 仅 A 股股票、**禁基金 0.001** 进 F 主切片；本页 = **证券类别维的最小价位误套**（基金/ETF 诚实 tick=0.001 vs 误套 0.01；及反向「股票腿发明 0.001」诊断）。与假设 **AX（ETF/基金经手费）** **硬分列**：AX = 经手费费率档；本页 = **申报/限制价最小变动单位**，费用≠价位，禁止捆。与假设 **E（整手）** **硬分列**：E = 股数整手/科创 200；本页 = 价格 tick。与假设 **Q（可转债）** **硬分列**：Q 可含债 tick 0.001，但本页主宇宙是场内基金/ETF，不重开转债规则。与假设 **A（板上枯竭）** **硬分列**：A = 有板日能否成交；本页 = 价位取整误套导致的**假有效限价 / 假板上价 / 假废单**。**双字母 AY ≠ 单字母 A ≠ 单字母 Y**。与假设 AN–AX **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/基金经手费。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AY** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 Y**（集合竞价量计入日线）≠ **单字母实验 A**（涨停可成交性）。全文凡写「实验 AY / 假设-AY / hypothesis_id=AY / 组 AY0·AY1·AY2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AY 混读或互改。亦**禁止**把实验字母 AY 与单字母 **A**、单字母 **Y**、双字母 **AX**、双字母 **AW**、或 params 键名 `ay0_*` 以外的实验页混读。**双字母 AY ≠ 单字母 A ≠ 单字母 Y ≠ 双字母 AX ≠ 双字母 AW**；**params.Y ≠ 实验字母 AY**；**params.N ≠ 实验字母 AY**。

---

## 1. 一句话假设（可检验、可证伪）

同一 ETF/场内基金信号、同一未复权价格路径、同一 T+1 下，把基金/ETF 腿的申报价、涨跌停限制价、有效申报范围按**股票默认最小价位 0.01 元**取整（或把股票腿发明成基金 **0.001**），相对「基金/ETF 诚实 tick=0.001、股票诚实 tick=0.01；限制价/申报价按所属证券类别最小变动单位四舍五入」的 PIT 诚实组，会**系统性改写假有效限价、假板上价差 1 分/1 厘、假废单与可成交路径**——基金腿套 0.01 会把本可挂的 0.001 分位抹平或错标限制价；反向发明 0.001 上股票腿会制造交易所不接受的假精细价；差异应**集中在最小价位误套桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的标签差异率、废单率差、净值/冲击代理差在标定噪声带内可忽略，且「基金套0.01 / 股票发明0.001 / 低价基金腿 / 限制价取整桶 / vs F·E·AX·A·Q」分桶不改变结论，则本假设在该样本与价位设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 基金 tick ≠ 股票 tick；≠ 经手费；≠ 整手；≠ 股票取整页 F

```
# 配置写死键（见 §7；待预检建议值如下，预检通过后冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AY；≠ 实验字母 A；≠ 实验字母 Y
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AY
# params.asof_check_date                 写死默认 2026-10-05  # 与事实与坑「最小价位」核对日同向（整手/取整周）
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.stock_tick                      写死 0.01
# params.fund_tick                       写死 0.001
# params.cb_tick_handoff                 写死 q_page         # 可转债 0.001 交 Q，本页不重开
# params.stock_limit_round_handoff       写死 f_page         # 股票板上取整主病交 F
# params.lot_size_handoff                写死 e_page         # 整手交 E
# params.fund_fee_handoff                写死 ax_page        # 基金经手费交 AX；费用≠价位
# params.ay0_primary_demo                建议 invent_stock_tick_on_fund  # 主报：基金/ETF 套股票 0.01；禁与 invent_fund_tick_on_stock 双挂争主表；AY1半泄露不得升格并列主报
# params.ay0_invent_stock_tick_on_fund   写死 True
# params.ay1_invent_fund_tick_on_stock   写死 True          # 半泄露/混口径：仅股票腿发明 0.001
# params.ay2_pit                         写死 True
# params.round_mode                      写死 round_half_up_to_tick
# params.limit_band_uses_tick            写死 True           # 涨跌停/有效范围结果取至 tick
# params.min_one_tick_floor              写死 True           # 与 F 同向：差不到 1 个价位则 ±1 tick；算出价 <1 tick 则以 1 tick
# params.merge_with_A_fill               写死 False
# params.merge_with_Y_call_volume        写死 False         # 实验字母 Y ≠ 本页 AY
# params.merge_with_F_round              写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_AX_fund_fee          写死 False
# params.merge_with_AW_close_fail        写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_S_ashare_handling    写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AQ_halt_cage         写死 False
# params.merge_with_AR_queue             写死 False
# params.merge_with_AS_ioc_fok           写死 False
# params.merge_with_AT_best5_to_limit    写死 False
# params.merge_with_AU_own_opp_best      写死 False
# params.merge_with_AV_call_match        写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_P_index_halt         写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_AL_session_gap       写死 False
# params.merge_with_AM_halt              写死 False
# params.universe_rule                   写死 sse_szse_fund_etf_tick_check
# params.missing_sec_type_policy         写死 skip
# params.missing_px_policy               写死 skip
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # 待预检写死；params.Y≠实验字母AY；params.N≠实验字母AY；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-05"
px_basis = "unadj"
stock_tick = 0.01
fund_tick = 0.001
ay0_primary_demo = "invent_stock_tick_on_fund"  # 待预检冻结；禁与 invent_fund_tick_on_stock 双挂
round_mode = "round_half_up_to_tick"
limit_band_uses_tick = True
min_one_tick_floor = True
universe_rule = "sse_szse_fund_etf_tick_check"
missing_sec_type_policy = "skip"
missing_px_policy = "skip"

# 待预检建议（通过后写死冻结；禁 null/holdout/跑后改口）
Y = 0.02   # 建议；相对门槛 ≠ 实验字母 AY；≠ 实验字母 Y
G = 0.01   # 建议
N = 0.05   # 建议；失败率门槛键 params.N ≠ 实验字母 AY
Y2 = 0.015 # 建议

def round_to_tick(px, tick):
    """四舍五入到最小变动单位（与 F 同向 round_half_up）。"""
    if px is None or tick is None or tick <= 0:
        return None
    # 纸面：用十进制语义；实现侧须避免二进制浮点漂移
    n = round(px / tick)   # round half up 语义须在实现注明
    return n * tick

def pit_tick(sec_type):
    """
    诚实 PIT 最小价位。
    sec_type ∈ {stock, stock_etf, gold_etf, cross_border_etf, commodity_futures_etf,
                money_etf, bond_etf, lof, closed_end, reits, other_fund}
    可转债不进主宇宙（handoff Q）。
    """
    if sec_type == "stock":
        return stock_tick
    if sec_type in (
        "stock_etf", "gold_etf", "cross_border_etf", "commodity_futures_etf",
        "money_etf", "bond_etf", "lof", "closed_end", "reits", "other_fund",
    ):
        return fund_tick
    return None  # skip

def tick_for_group(group, sec_type):
    if group == "AY0" and ay0_primary_demo == "invent_stock_tick_on_fund":
        # 主报：凡基金/ETF 腿套股票 0.01；股票腿仍 0.01（与天真「全市场一刀切 0.01」同向）
        return stock_tick
    if group == "AY1":
        # 半泄露：仅股票腿发明基金 0.001；基金腿走 PIT 0.001
        if sec_type == "stock":
            return fund_tick
        return pit_tick(sec_type)
    # AY2 PIT
    return pit_tick(sec_type)

def snap_limit_px(raw_limit, prev_close, tick):
    """限制价取整；差不到 1 tick 则 ±1 tick；低于 1 tick 则以 1 tick（与 F/交易所同向）。"""
    if raw_limit is None or tick is None:
        return None
    snapped = round_to_tick(raw_limit, tick)
    if prev_close is not None and abs(snapped - prev_close) < tick:
        snapped = prev_close + tick if raw_limit >= prev_close else prev_close - tick
        snapped = round_to_tick(snapped, tick)
    if snapped is not None and snapped < tick:
        snapped = tick
    return snapped
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺未复权价、缺证券类别、把 F 股票取整主病 / E 整手 / AX 基金经手费 / Q 转债 tick / A 板上枯竭 / 实验 Y 集合量 混进本页主表、把可转债并进主宇宙却不标注 → **跳过该日该券该腿**，不静默记假价位。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AY）

| 组 | 最小价位口径 | 说明 |
|----|--------------|------|
| AY0 天真 | 按 `ay0_primary_demo` 单一主报（**建议** `invent_stock_tick_on_fund`） | 基金/ETF（及天真全市场）套股票 0.01；禁与 invent_fund_tick_on_stock 双挂 |
| AY1 半泄露/混口径 | 仅股票腿发明 0.001；基金腿 PIT 0.001 | 反向假精细价 |
| AY2 PIT 诚实 | 股票 0.01 / 基金·ETF 0.001；限制价按所属 tick 取整 | 与公开规则同向 |

同一信号。本页**主测最小价位是否被跨证券类别误套**，不主测股票板上取整公式细节（见 F）、不主测整手（见 E）、不主测基金经手费（见 AX）、不主测证管费（**避开预检T**）、不主测 ETF 回转（见 R）、不主测板上枯竭主病（见 A）、不主测集合竞价量（见实验 Y）、不主测收盘失败回落（见 AW）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/Y/F/E/Q/AX/AW/AN–AV/R/S/T/U/V/I/L/H/M/N/O/G/J/K/P/W/AA–AM）**。

**待预检键建议（预检通过后写死冻结；禁 holdout；禁 null；禁双挂；禁跑后改口）**：

```
params.Y                            = 0.02                         # 建议；标签/净值差显著门槛；≠实验字母 AY；≠实验字母 Y
params.G                            = 0.01                         # 建议；误套桶相对对照差
params.N                            = 0.05                         # 建议；失败/废单率差门槛；≠实验字母 AY
params.Y2                           = 0.015                        # 建议；AY1（股票发明0.001）相对 AY2 专项门槛
params.ay0_primary_demo             = invent_stock_tick_on_fund    # 建议主报：基金/ETF套股票0.01；禁与 invent_fund_tick_on_stock 双挂争主表；AY1半泄露不得升格并列主报
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深场内基金/ETF 为主（`universe_rule=sse_szse_fund_etf_tick_check`），须能分 `stock_etf / gold_etf / cross_border_etf / commodity_futures_etf / money_etf / bond_etf / lof / closed_end / reits`；可附带对照股票腿（仅用于 AY1 反向桶与 vs F 分桶，**不把 F 主病并进主结论**）。可转债**不进主宇宙**（交 Q）。  
- **排除（默认）**：缺证券类别；缺未复权价；把 F/E/AX/A/Y/Q/AW 主结论并进本页主表；用复权价当申报/限制价基准；把「基金经手费免/暂免」理解成「基金无最小价位约束」。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：每个交易日按证券类别取当时最小价位；核对日未核到「按股价高低分档 tick」表则**不切片分档**（与 F 同向：分档未核验不切片）；**禁止**用股票 0.01 静默铺满基金腿却不声明天真组。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ay0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AY0 − AY2**：基金/ETF 套 0.01 相对诚实 0.001——限制价/申报价标签差、废单差、假精细分位抹平。  
2. **AY1 − AY2**：股票腿发明 0.001 相对诚实 0.01——假精细价/假有效申报。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_stock_tick_on_fund",
  "invent_fund_tick_on_stock",
  "low_price_fund_leg",
  "limit_band_snap_diff",
  "order_px_snap_diff",
  "stock_etf_leg",
  "money_bond_etf_leg",
  "reits_lof_closed_leg",
  "vs_F_stock_limit_round",
  "vs_E_lot",
  "vs_AX_fund_fee",
  "vs_A_fill",
  "vs_Q_cb_tick",
  "vs_Y_call_volume",
  "vs_AW_close_fail",
  "vs_R_etf_rotation",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 标签差异率 ΔTag（限制价/申报价取整后是否与诚实 tick 不一致）；  
2. 废单/失败率差 ΔFail；  
3. 假价位贡献差 ΔFakeTick；  
4. 净值/冲击代理差 ΔNet（声明为价位误套传导，不冒充选基）。

**相对判据（草稿）**：若 |ΔTag| 或 |ΔNet| **≥ params.Y** 或 |ΔFakeTick 桶贡献| **≥ params.G** 或 |ΔTag_(AY1−AY2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「基金/ETF 最小价位执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AY / 实验字母 Y 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 标签/净值差显著门槛（≠实验字母 AY；≠实验字母 Y） | **建议** `0.02`（预检后冻结） |
| params.G | 误套桶相对对照差 | **建议** `0.01` |
| params.N | 失败/废单率差门槛（≠实验字母 AY） | **建议** `0.05` |
| params.Y2 | AY1−AY2 专项门槛 | **建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-05` |
| fill_time | 成交时点 | **写死** `next_open` |
| ay0_primary_demo | 天真主报枚举 | **建议** `invent_stock_tick_on_fund`（禁与 invent_fund_tick_on_stock 双挂；AY1半泄露不得升格并列主报） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须按证券类别 tick；禁与 F/E/AX/A/Y 混主结论；禁荐股）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实基金 0.001」与「套股票 0.01」，或缺证券类别且未声明 skip → 本假设不可检。  
2. 把股票涨跌停取整主病（F）、整手（E）、基金经手费（AX）、板上枯竭（A）、集合竞价量（实验 Y）、可转债规则（Q）、收盘失败回落（AW）、证管费（T）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「基金 tick 误套」写成「股票板上取整」而不声明另页 F → 与 F 撞题，设计失效。  
4. 把「基金 tick 误套」写成「ETF/基金经手费误套」→ 与 AX 撞题，设计失效。  
5. 把「基金 tick 误套」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
6. 把「基金 tick 误套」写成「涨停能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
7. 把「基金 tick 误套」写成「集合竞价量是否计入日线」而不声明另页实验 Y → 与 Y 撞题，设计失效。  
8. 把实验字母 AY 与单字母 A 或单字母 Y 或双字母 AX/AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
9. holdout 反调 `ay0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算限制价/申报价 → 标签双错，结论无效。  
11. 未核验的「按股价分档 tick」却切片当主结论 → 与 F 纪律冲突，设计失效。  
12. 把可转债 0.001 当成本页/基金页主宇宙却不 handoff Q → 与 Q 撞题，设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价（申报代理价/前收盘/限制价原料）、买卖方向、交易所（沪/深）、证券类别（须能分股票 vs 各类 ETF/LOF/封闭式/REITs）；  
- 交易日；  
- 交易日历。

可选：交易所限制价官方值（核对取整）；与 F/E/AX 对照输入（消费、不重开）。

**禁止**：用股票 0.01 静默当基金诚实 tick；用复权价；把普通股票取整主病当本页主结论；把 AX 费率当价位；把预检T证管费重做；把实验字母 AY 与 A/Y/params.Y 混用。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AY`  
- **组**：AY0 / AY1 / AY2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-05`；`stock_tick=0.01`；`fund_tick=0.001`；`round_mode=round_half_up_to_tick`；`limit_band_uses_tick=True`；`min_one_tick_floor=True`；`stock_limit_round_handoff=f_page`；`lot_size_handoff=e_page`；`fund_fee_handoff=ax_page`；`cb_tick_handoff=q_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_fund_etf_tick_check`；`missing_sec_type_policy=skip`；`missing_px_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AY；**params.N≠实验字母 AY**；≠实验字母 Y；禁 null/holdout；待预检冻结）；**`params.ay0_primary_demo` 建议 `invent_stock_tick_on_fund`**（禁与 invent_fund_tick_on_stock 双挂；AY1半泄露不得升格并列主报；待预检冻结）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AY0/AY1/AY2 ΔTag、ΔFakeTick、ΔNet、ΔFail；分桶（基金套0.01 / 股票发明0.001 / 低价基金腿 / 限制价取整差 / vs F·E·AX·A·Q·Y·AW·R）。  
- 自检布尔：AY2 是否按证券类别 tick；AY0 是否单一主报；AY1 是否仅股票腿发明 0.001；是否未与 F/E/AX/A/Y/T 混主结论；holdout 是否未反调；**是否未把实验字母 AY 与 A 或 Y 或 AX 或 AW 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AX 冻结补丁正文**；**是否未改假设-H / 假设-F / 假设-E / 假设-Q / 假设-AX / 假设-AW**；**是否未再改 AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把股票 0.01 当基金诚实 tick；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AX 及其他 A/D–AX 已交正文**；**不改假设-H**；**不改假设-F**；**不改假设-E**；**不改假设-Q**；**不改假设-A**；**不改假设-Y**；**不改假设-AX**；**不改假设-AW**；**勿再改 AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：A 股股票默认最小价位 0.01 元；基金是 0.001 元，不要和股票混用；限制价结果按最小变动单位四舍五入。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 AY** 标准件，**不改口径主线**，**不改假设 A–AX 正文**。与实验 F/E/AX/A/Y/Q/AW 分工：**F=股票板上取整；E=整手；AX=基金经手费；A=板上枯竭；Y=集合量计入日线；Q=可转债；AW=收盘失败回落；AY=基金/ETF 最小价位误套（AY≠A≠Y≠F≠E≠AX≠AW）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-05；**fill_time=next_open 写死**；stock_tick/fund_tick 写死；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AY；params.N≠实验字母 AY；≠实验字母 Y；待预检冻结）**；**ay0_primary_demo 建议 invent_stock_tick_on_fund（禁双挂；AY1半泄露不得升格并列主报；待预检冻结）** |

---

## 待预检键 / demo 键名建议（交风控）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：建议写死 `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AY**；**`params.N` ≠ 实验字母 AY**；**`params.Y` ≠ 实验字母 Y**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.ay0_primary_demo`**：建议写死 **`invent_stock_tick_on_fund`**；禁与 **`invent_fund_tick_on_stock`** 双挂争主表（只挂一个 primary）；**AY1 半泄露不得升格并列主报**。

---

## 变更

- 2026-11-03：新建标准件（总管线：AX 补丁已收后写下一纸面 AY；Y/Z/AA–AX 补丁/正文已交不改；清单撞题规则另选「基金/ETF 最小价位误套股票 0.01」；选题自 `事实与坑`；**与 A/H/Y/E/F/M/O/N/Q/R/S/T/U/V/W/L/I/AX/AW/AN–AV 硬分列**；**双字母 AY ≠ 单字母 A ≠ 单字母 Y**；**不与 AN–AX 重复**；**明确避开预检T旧题（证管费误抽）**；**勿占 AX（ETF基金经手费）/AW**；结论栏空；不开回测；不抢 A；**勿再改 AX/AW**）。