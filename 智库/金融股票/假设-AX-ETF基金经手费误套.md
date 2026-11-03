# 假设 AX · ETF/场内基金经手费误套 A 股档 / 货币债基误抽 / 2023-08-28 假改档（成本诚信）

更新：2026-11-03  
来源：总管线 / AW 补丁已收、写下一纸面 AX；清单第 54/55 条「费用层：基金经手费；字母待派，勿占 AW」→ **自立实验 AX**；选题自 `事实与坑`「ETF / 基金经手费 ≠ 股票」公开收费表与 2021-07-19 切日；与假设 A（板上可成交/枯竭）/ H（退市整理）/ X（主板 ST）/ E（整手）/ M（盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ N（收盘切日/假 GTC）/ S（**沪深 A 股**经手费现行档误铺）/ T（证管费；**避开预检T旧题**）/ U（过户费）/ V（印花税）/ W（除权判板）/ L（市价通道）/ AN–AW（集合剩单/盘后错侧/临停笼子/假队首/剩撤FOK/五档转限/空簿假成/集合三原则/收盘失败回落）/ I/F/J/G/K/P/AC–AF 等**分列**；**新建实验 AX**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「A 股 0.0341‰ 套 ETF / 货币债基抽基金或股票档 / 2023-08-28 股票降 30% 写成基金也改档 / 基金大宗按股票下浮 30% / REITs 表价当已收」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AW 及其他 A/D–AW 已交正文与冻结补丁；不改假设-H；不改假设-S；不改假设-T；不改假设-R；不改假设-AW；勿再改 AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 第 54/55 条对齐；清单费用层缺口字母待派，本页自立实验 AX 标准件。与假设 **S（沪深 A 股竞价经手费）** **硬分列**：S = A 股三切日（2012-09-01 / 2015-08-01 / 2023-08-28）与「30%≠减半 / 已含代收禁双计」；S 已写死 `apply_ashare_fee_to_etf=False`，ETF/基金档**另页本页**。与假设 **T（证管费误抽）** **硬分列**：**明确避开预检T旧题**——T = 股票 0.02‰ 证管费是否误改档/对 ETF 误抽证管费；本页 = **交易所经手费（handling）基金档**，不是证监会对交易所的监管费。与假设 **R（股票 ETF 假回转）** **硬分列**：R = 3.1.5 当日回转名单；本页 = 经手费费率档，**回转名单 ≠ 经手费档，禁止捆**。与假设 **U/V（过户费/印花税对 ETF 误抽）** **分列**：本页不重开过户/印花。与假设 **A（板上枯竭）** **硬分列**：A = 有板日可成交；本页 = ETF/基金腿**成交成本费率**误设。双字母 **AX ≠ 单字母 A**。与假设 **X（主板 ST 涨跌幅）** **硬分列**：X = ST 板幅 PIT；本页 = 基金经手费。双字母 **AX ≠ 单字母 X**。与假设 **AW（收盘集合失败回落）** **硬分列**：AW = 收盘价失败回落链；本页 = 费用层。与假设 AN–AV **硬分列**：不重开撮合/剩单/空簿类执行鸿沟。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AX** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AX / 假设-AX / hypothesis_id=AX / 组 AX0·AX1·AX2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AX 混读或互改。亦**禁止**把实验字母 AX 与单字母实验 **A**、单字母实验 **X**、单字母实验 **S**、双字母实验 **AW**、或 params 键名 `ax0_*` 以外的实验页混读。**双字母 AX ≠ 单字母 A ≠ 单字母 X ≠ 单字母 S ≠ 双字母 AW**；**params.Y ≠ 实验字母 AX**；**params.N ≠ 实验字母 AX**。

---

## 1. 一句话假设（可检验、可证伪）

同一 ETF/场内基金信号、同一未复权成交金额、同一 T+1、同一印花税/证管费/过户费切片下，把基金腿经手费按**沪深 A 股现行 0.0341‰**（或股票档历史切日）铺满、或对**货币 ETF / 债券 ETF**按基金档/股票档发明收费、或把 **2023-08-28 股票降 30%** 写成基金也改档、或基金大宗按下浮 **30%**（非竞价下浮 50%）、或把公募 REITs **表上 0.0045% 当已收**，相对「股票/黄金/跨境/商品期货 ETF·LOF·封闭式按基金竞价 PIT（2021-07-19 前沪 0.0045%/深 0.00487%，之后两所 0.04‰=0.004% 双边；货币/债券 ETF=0；基金大宗竞价下浮 50%；REITs 试点暂免；佣金若已含代收则不再叠）」的 PIT 诚实组，会**系统性改写「成本吃掉的那截」与高换手基金腿净值**——A 股档套股票 ETF **略低估**（0.0341<0.04），货币/债基误抽 **发明收费偏悲观**，2023-08-28 假改档 **错标切日后成本**；差异应**集中在基金经手费误套桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的成本差、净值差、失败率差在标定噪声带内可忽略，且「股票ETF套A股档 / 货币债基误抽 / 2023-08-28假改档 / 基金大宗误下浮30% / REITs表价当已收 / 2021-07-19前沪深分档」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 基金经手费 ≠ A 股经手费；≠ 证管费；≠ ETF 回转；切日 2021-07-19 ≠ 2023-08-28

```
# 配置写死键（见 §7；待预检键名稳、建议值如下；拉数前须冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AX；≠ 实验字母 A；≠ 实验字母 X
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AX
# params.asof_check_date                 写死默认 2026-10-30  # 与事实与坑「ETF/基金经手费」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.fund_fee_cut_20210719           写死 2021-07-19
# params.fund_handling_bps_post_20210719 写死 0.04          # ‰；=0.004%；双边各收
# params.fund_handling_pct_sse_pre       写死 0.0045        # %；沪市切日前
# params.fund_handling_pct_szse_pre      写死 0.00487       # %；深市切日前；禁用深旧档回放沪、反之亦然
# params.money_bond_etf_fee_bps          写死 0.0           # 货币/债券 ETF 暂免
# params.reits_table_pct                 写死 0.0045        # 表上%；试点暂免 → PIT=0
# params.reits_pilot_exempt              写死 True
# params.fund_block_discount_pct         写死 0.50          # 基金大宗相对竞价下浮 50%
# params.stock_block_discount_pct_wrong  写死 0.30          # 误用股票大宗 30%
# params.ashare_handling_bps_current     写死 0.0341        # 仅作误套对照；≠基金档
# params.stock_cut_20230828              写死 2023-08-28    # 股票经手费切日；基金档该日未改
# params.ax0_primary_demo                待预检建议 invent_ashare_fee_on_etf
#                                        # 禁与 invent_charge_money_bond_etf 双挂争主表
# params.ax0_invent_ashare_on_etf        写死 True
# params.ax1_charge_money_bond           写死 True          # 半泄露/混口径：仅货币债基误抽基金档
# params.ax1b_fake_stock_cut_on_fund     写死 True          # 诊断：2023-08-28 假改基金档（可进分桶，不与 ax0 双挂主报）
# params.ax2_pit                         写死 True
# params.side                            写死 both
# params.commission_includes_agency      写死 True          # 已含代收 → AX2 不再叠经手费
# params.ax2_stack_if_included           写死 False
# params.ashare_fee_handoff              写死 s_page        # A 股经手费交 S，本页不重开三切日主病
# params.csrc_fee_handoff                写死 t_page        # 证管费交 T；避开预检T
# params.etf_rotation_handoff            写死 r_page        # 回转交 R
# params.transfer_fee_handoff            写死 u_page
# params.stamp_tax_handoff               写死 v_page
# params.merge_with_A_fill               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_S_ashare_handling    写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_AW_close_fail        写死 False
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AQ_halt_cage         写死 False
# params.merge_with_AR_queue             写死 False
# params.merge_with_AS_ioc_fok           写死 False
# params.merge_with_AT_best5_to_limit    写死 False
# params.merge_with_AU_own_opp_best      写死 False
# params.merge_with_AV_call_match        写死 False
# params.merge_with_O_block              写死 False         # 大宗通道另页 O；本页只测基金大宗费率下浮
# params.merge_with_Q_cb                 写死 False         # 可转债经手费本轮不展开
# params.merge_with_H_exit               写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_P_index_halt         写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_Y_call_volume        写死 False
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
# params.universe_rule                   写死 sse_szse_etf_fund_handling_check
# params.missing_notional_policy         写死 skip
# params.missing_sec_type_policy         写死 skip
# params.missing_exchange_policy         写死 skip          # 切日前须分沪/深旧档
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  待预检建议 0.02/0.01/0.05/0.015
#                                        # params.Y≠实验字母 AX；params.N≠实验字母 AX；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-30"
px_basis = "unadj"
fund_fee_cut_20210719 = "2021-07-19"
fund_handling_bps_post_20210719 = 0.04   # ‰
fund_handling_pct_sse_pre = 0.0045       # %
fund_handling_pct_szse_pre = 0.00487     # %
money_bond_etf_fee_bps = 0.0
reits_table_pct = 0.0045
reits_pilot_exempt = True
fund_block_discount_pct = 0.50
stock_block_discount_pct_wrong = 0.30
ashare_handling_bps_current = 0.0341
stock_cut_20230828 = "2023-08-28"
ax0_primary_demo = "invent_ashare_fee_on_etf"  # 待预检；禁双挂
side = "both"
commission_includes_agency = True
ax2_stack_if_included = False
universe_rule = "sse_szse_etf_fund_handling_check"
missing_notional_policy = "skip"
missing_sec_type_policy = "skip"
missing_exchange_policy = "skip"

# 待预检建议（键名稳；值待风控确认后冻结；禁 null/holdout）
Y = 0.02   # 建议；相对门槛 ≠ 实验字母 AX
G = 0.01
N = 0.05   # 建议；失败率门槛键 params.N ≠ 实验字母 AX
Y2 = 0.015

def pct_to_bps(pct):
    """0.004% → 0.04‰"""
    return pct * 10.0

def pit_fund_handling_bps(d, exchange, sec_type, is_block=False):
    """
    诚实 PIT：基金竞价经手费（‰，单边；双边各收）。
    sec_type ∈ {stock_etf, gold_etf, cross_border_etf, commodity_futures_etf, lof, closed_end,
                money_etf, bond_etf, reits, other_fund}
    """
    if sec_type in ("money_etf", "bond_etf"):
        return 0.0
    if sec_type == "reits" and reits_pilot_exempt:
        return 0.0
    if d >= fund_fee_cut_20210719:
        bps = fund_handling_bps_post_20210719
    else:
        if exchange == "SSE":
            bps = pct_to_bps(fund_handling_pct_sse_pre)
        elif exchange == "SZSE":
            bps = pct_to_bps(fund_handling_pct_szse_pre)
        else:
            return None  # skip
    if is_block:
        bps = bps * (1.0 - fund_block_discount_pct)
    return bps

def handling_bps_for_group(group, d, exchange, sec_type, is_block=False):
    if group == "AX0" and ax0_primary_demo == "invent_ashare_fee_on_etf":
        # 主报：凡 ETF/基金腿套 A 股现行 0.0341‰（可叠历史股票档诊断，但不改主报键）
        return ashare_handling_bps_current
    if group == "AX1":
        # 半泄露：仅货币/债基误抽基金档；其余走 PIT
        if sec_type in ("money_etf", "bond_etf"):
            if d >= fund_fee_cut_20210719:
                return fund_handling_bps_post_20210719
            return pct_to_bps(fund_handling_pct_sse_pre if exchange == "SSE" else fund_handling_pct_szse_pre)
        return pit_fund_handling_bps(d, exchange, sec_type, is_block)
    # AX2 PIT
    bps = pit_fund_handling_bps(d, exchange, sec_type, is_block)
    if bps is None:
        return None
    if commission_includes_agency and (not ax2_stack_if_included):
        return 0.0
    return bps

def handling_cost(notional, bps, side="both"):
    if bps is None:
        return None
    mult = 2.0 if side == "both" else 1.0
    return notional * (bps / 1000.0) * mult
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺未复权成交金额、缺证券类别、切日前缺交易所却硬套单一旧档、把 S 的 A 股三切日主病 / T 证管费 / R 回转 / U 过户 / V 印花 / A 板上 / X ST 板幅混进本页主表、把可转债经手费并进主宇宙却不标注 → **跳过该日该券该腿**，不静默记假成本。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AX）

| 组 | 基金经手费口径 | 说明 |
|----|----------------|------|
| AX0 天真 | 按 `ax0_primary_demo` 单一主报（建议 `invent_ashare_fee_on_etf`） | 用 A 股 0.0341‰ 套 ETF/基金腿 |
| AX1 半泄露/混口径 | 仅货币/债基误抽基金档；其余 PIT | 发明收费路径 |
| AX2 PIT 诚实 | 基金档 PIT + 货币债基 0 + REITs 暂免 + 基金大宗下浮 50%；已含代收不叠 | 与公开收费表同向 |

同一信号、同一 ETF/场内基金宇宙。本页**主测基金经手费是否被 A 股档/假切日/误抽暂免品种替换**，不主测 A 股经手费三切日（见 S）、不主测证管费（见 T；**避开预检T**）、不主测 ETF 回转（见 R）、不主测过户/印花（见 U/V）、不主测板上枯竭（见 A）、不主测 ST 板幅（见 X）、不主测收盘失败回落（见 AW）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/X/S/T/R/U/V/AW/AN–AV/O/Q/H/E/M/N/L/I/F/G/J/K/P/W/Y/AA–AF/AG–AM）**。

**待预检两条（键名稳；建议值；拉数前须冻结；禁 holdout；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 建议；成本/净值差显著门槛；≠实验字母 AX
params.G                            = 0.01                      # 建议；误套桶相对对照差
params.N                            = 0.05                      # 建议；失败/废单率差门槛；≠实验字母 AX
params.Y2                           = 0.015                     # 建议；AX1（货币债基误抽）相对 AX2 专项门槛
params.ax0_primary_demo             = invent_ashare_fee_on_etf  # 建议主报：A股档套ETF/基金；禁与 invent_charge_money_bond_etf 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深场内基金/ETF（`universe_rule=sse_szse_etf_fund_handling_check`），须能分 `stock_etf / gold_etf / cross_border_etf / commodity_futures_etf / money_etf / bond_etf / lof / closed_end / reits`。普通 A 股**不进主宇宙**（A 股经手费交 S）。可转债本轮不进主宇宙（另档，本轮不展开）。  
- **排除（默认）**：缺证券类别；切日前缺交易所；把 S/T/R/U/V/A/X/AW 主结论并进本页主表；把「ETF 免证管费」理解成「ETF 免经手费」；用复权价当成交金额。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - 须覆盖 **2021-07-19** 基金档切日；**禁止**用核对日 0.04‰ 铺满切日前却不声明泄露组。  
- **PIT 切片原则**：每个交易日用当日已生效基金经手费档；沪/深切日前旧档分列；2023-08-28 **不改**基金档；货币/债券 ETF=0；REITs 试点暂免；**禁止**把股票经手费切日抄到基金。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ax0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AX0 − AX2**：A 股档套 ETF/基金相对诚实基金档——成本低估（股票 ETF）或错档。  
2. **AX1 − AX2**：仅货币/债基误抽相对诚实暂免——发明收费偏悲观。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_ashare_fee_on_etf",
  "invent_charge_money_bond_etf",
  "invent_stock_cut_20230828_on_fund",
  "invent_fund_block_as_stock_30pct",
  "invent_reits_table_as_charged",
  "pre_20210719_sse_vs_szse_split",
  "stock_etf_leg",
  "gold_cross_commodity_etf_leg",
  "money_bond_etf_leg",
  "reits_leg",
  "high_turnover",
  "vs_S_ashare_handling",
  "vs_T_csrc_fee",
  "vs_R_etf_rotation",
  "vs_U_transfer",
  "vs_V_stamp",
  "vs_A_fill",
  "vs_X_st_limit",
  "vs_AW_close_fail",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 成本差 ΔCost（AX0/AX1 相对 AX2）；  
2. 误套腿贡献差 ΔFakeFee；  
3. 净值/冲击代理差 ΔNet（声明为成本传导，不冒充选基）；  
4. 失败/废单率差 ΔFail（缺类别 skip 等）。

**相对判据（草稿）**：若 |ΔCost| 或 |ΔNet| **≥ params.Y** 或 |ΔFakeFee 桶贡献| **≥ params.G** 或 |ΔCost_(AX1−AX2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「ETF/基金经手费执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AX 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 成本/净值差显著门槛（≠实验字母 AX） | **待预检建议** `0.02` |
| params.G | 误套桶相对对照差 | **待预检建议** `0.01` |
| params.N | 失败/废单率差门槛（≠实验字母 AX） | **待预检建议** `0.05` |
| params.Y2 | AX1−AX2 专项门槛 | **待预检建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-30` |
| fill_time | 成交时点 | **写死** `next_open` |
| ax0_primary_demo | 天真主报枚举 | **待预检建议** `invent_ashare_fee_on_etf`（禁与 invent_charge_money_bond_etf 双挂） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须基金档 PIT；禁与 S/T/R/A/X 混主结论；禁荐股）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实基金档」与「A 股档/货币债基误抽」，或缺证券类别且未声明 skip → 本假设不可检。  
2. 把 A 股经手费三切日（S）、证管费（T）、ETF 回转（R）、过户（U）、印花（V）、板上枯竭（A）、ST 板幅（X）、收盘失败回落（AW）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「基金经手费误套」写成「股票经手费现行档误铺」而不声明另页 S → 与 S 撞题，设计失效。  
4. 把「基金经手费误套」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
5. 把「基金经手费误套」写成「股票 ETF 假回转」而不声明另页 R → 与 R 撞题，设计失效。  
6. 把「基金经手费误套」写成「板上能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
7. 把「基金经手费误套」写成「主板 ST 涨跌幅 PIT」而不声明另页 X → 与 X 撞题，设计失效。  
8. 把回转名单（3.1.5）与经手费档捆成一句主结论 → 设计失效。  
9. holdout 反调 `ax0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算成交金额 → 标签与成本双错，结论无效。  
11. 把实验字母 AX 与单字母 A 或单字母 X 或单字母 S 或双字母 AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
12. 用深市旧档回放沪市（或反过来）却不进分桶/不 skip → 结论无效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权成交金额、买卖方向、交易所（沪/深）、证券类别（须能分股票/黄金/跨境/商品期货 ETF、货币/债券 ETF、LOF、封闭式、REITs）；  
- 交易日；2021-07-19、2023-08-28 切日标记（后者仅作「基金未改档」对照）；  
- 是否大宗（可选；主跑可竞价-only）；  
- 佣金是否已含代收经手费开关；  
- 交易日历。

可选：基金管理人/收费公告核对字段；与 S/T/U/V 对照输入（消费、不重开）。

**禁止**：用核对日基金 0.04‰ 静默铺满 2021-07-19 前却不声明泄露；用 A 股 0.0341‰ 当诚实基金档；对货币/债券 ETF 抽费当诚实；把 2023-08-28 写成基金改档；把 REITs 表价当已收；用复权价；把普通 A 股混进主宇宙却不标注；把 S/T/R/A/X/AW 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AX`  
- **组**：AX0 / AX1 / AX2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-30`；`fund_fee_cut_20210719=2021-07-19`；`fund_handling_bps_post_20210719=0.04`；`fund_handling_pct_sse_pre=0.0045`；`fund_handling_pct_szse_pre=0.00487`；`money_bond_etf_fee_bps=0`；`reits_pilot_exempt=True`；`fund_block_discount_pct=0.50`；`ashare_fee_handoff=s_page`；`csrc_fee_handoff=t_page`；`etf_rotation_handoff=r_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_etf_fund_handling_check`；`missing_notional_policy=skip`；`missing_sec_type_policy=skip`；`missing_exchange_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 待预检建议 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AX；**params.N≠实验字母 AX**；禁 null/holdout）；**`params.ax0_primary_demo` 待预检建议 `invent_ashare_fee_on_etf`**（禁与 invent_charge_money_bond_etf 双挂）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AX0/AX1/AX2 成本、ΔFakeFee、ΔNet、ΔFail；分桶（A股档套ETF / 货币债基误抽 / 2023-08-28假改档 / 基金大宗误30% / REITs表价 / 切日前沪深分档 / vs S·T·R·U·V·A·X·AW）。  
- 自检布尔：AX2 是否基金档 PIT；AX0 是否单一主报；AX1 是否仅货币债基误抽；是否未与 S/T/R/A/X/AW 混主结论；holdout 是否未反调；**是否未把实验字母 AX 与 A 或 X 或 S 或 AW 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AW 冻结补丁正文**；**是否未改假设-H / 假设-S / 假设-T / 假设-R / 假设-AW**；**是否未再改 AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把 A 股档/误抽暂免品种当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AW 及其他 A/D–AW 已交正文**；**不改假设-H**；**不改假设-S**；**不改假设-T**；**不改假设-R**；**不改假设-A**；**不改假设-X**；**不改假设-AW**；**勿再改 AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：ETF/场内基金经手费走基金档（核对日 0.04‰ 双边），不是 A 股 0.0341‰；货币/债券 ETF 暂免；切日 2021-07-19；2023-08-28 未改基金档；REITs 试点暂免；基金大宗下浮 50%。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单第 54/55 条字母待派，本页**新增实验 AX** 收成标准件，**不改口径主线**，**不改假设 A–AW 正文**。与实验 S/T/R/A/X/AW 分工：**S=A股经手费；T=证管费（避开）；R=ETF回转；A=板上枯竭；X=ST板幅；AW=收盘失败回落；AX=ETF/基金经手费误套（AX≠A≠X≠S≠T≠R≠AW）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-30；**fill_time=next_open 写死**；基金档切日/费率写死；diff_buckets 写死待冻结；**Y/G/N/Y2 待预检建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AX；params.N≠实验字母 AX）**；**ax0_primary_demo 待预检建议 invent_ashare_fee_on_etf（禁双挂）** |

---

## 变更

- 2026-11-03：新建标准件（总管线：AW 补丁已收后写下一纸面 AX；Y/Z/AA–AW 补丁/正文已交不改；清单第 54/55 条基金经手费缺口字母待派 → 自立实验 AX；选题自 `事实与坑`「ETF/基金经手费≠股票」；**与 A/H/X/E/M/O/R/Q/N/S/T/U/V/W/L/AN–AW 硬分列**；**双字母 AX ≠ 单字母 A ≠ 单字母 X**；**不与 AN–AW 重复**；**明确避开预检T旧题（证管费误抽）**；结论栏空；不开回测；不抢 A；**勿再改 AW**）。
