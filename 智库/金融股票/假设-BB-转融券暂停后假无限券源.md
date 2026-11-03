# 假设 BB · 转融券暂停后假无限券源 / 名单内假任意量可借（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BA 补丁已收、写下一纸面 BB；清单撞题规则另选正交执行缺口（转融券通道/券源可借量 ≠ 融券标的名单 ≠ 融资买入名单 ≠ 保证金比例）；选题自 `事实与坑`「标的名单 ≠ 一定借得到；证监会 2024-07-10 批准中证金融自 2024-07-11 暂停转融券，存量不得晚于 2024-09-30 了结；暂停转融券不等于融券标的消失（券商自有券源仍可能出借），但回测不要假设名单里每只都能按任意量、任意日借到」公开规则；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」印花税时点·财务可见日·除权误判等旧位；**双字母 BB ≠ 单字母 B**）/ K（**融券空头名单** PIT；**BB≠K**：名单闸门 ≠ 券源可借量）/ BA（**融资买入**标的名单；**BB≠BA**）/ Z（保证金比例；**BB≠Z**）/ AB（融券卖出价限 / 禁市价 / 当日平；**BB≠AB**）/ E（整手）/ M（盘后）/ O（大宗）/ N（收盘切日/假 GTC）/ Q（可转债）/ R（股票 ETF 假回转）/ S/T/U/V（费用层；**避开预检T旧题**）/ W（除权判板）/ L（市价通道）/ D（开/收时点与停牌）/ AN–BA（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单等）/ Y（集合量计入日线；**实验字母 Y ≠ params.Y**）/ AA–BA / AC–BA 等**分列**；**新建实验 BB**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-03）**（结论栏空；禁止把「在融券名单内 = 任意量任意日一定借得到 / 2024-07-11 后仍按无限转融券源回放」当诚实空头可成交能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BA 及其他 A/D–BA 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-K；不改假设-BA；不改假设-Z；不改假设-AB；勿再改 BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BB。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **空头腿在转融券暂停后是否仍发明无限券源**。**双字母 BB ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BB ≠ 单字母 B**。与假设 **K（融券空头名单）** **硬分列**：K = **能不能进空头名单闸门**（PIT 名单）；本页 = **进名单后转融券通道/券源是否按任意量可借**；名单内 ≠ 一定借得到；禁止捆成「融券名单一张表=无限券源」。与假设 **BA（融资买入标的名单）** **硬分列**：BA = **多头融资买入**可融名单；本页 = **空头券源/转融通道**可借量；融资买入 ≠ 融券券源。与假设 **Z（保证金比例）** **硬分列**：Z = 已允许融资/融券后的**比例/可开名义**；本页 = **转融暂停后的券源可成交性**，不主测 80%/100% 比例。与假设 **AB（融券卖出价限）** **硬分列**：AB = 融券卖出价限/禁市价/当日平；本页不主测空头价限。与假设 AN–BA **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BB** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 K**（融券名单）。全文凡写「实验 BB / 假设-BB / hypothesis_id=BB / 组 BB0·BB1·BB2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 BB 混读或互改。亦**禁止**把实验字母 BB 与单字母 **A**、单字母 **B**、单字母 **K**、单字母 **Z**、双字母 **BA**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `bb0_*` 以外的实验页混读。**双字母 BB ≠ 单字母 A ≠ 单字母 B ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 AB ≠ 双字母 AZ**；**params.Y ≠ 实验字母 BB**；**params.N ≠ 实验字母 BB**。

---

## 1. 一句话假设（可检验、可证伪）

同一空头信号、同一未复权价、同一 T+1、同一融券名单输入（K 层诚实 PIT 或显式旁路声明「本页不重开名单」）下，把「在融券标的名单内即可任意量、任意日借到券」在 **2024-07-11 转融券暂停后**仍按**无限转融券源**回放（或把暂停日当成未发生），相对「暂停后转融券通道关闭/券源不保证，缺券源记空头失败或按 `day_freq_proxy` 敏感性加严；券商自有券源另桶、不得默认=无限转融；存量了结不得晚于 2024-09-30；缺券源字段 skip/敏感性」的 PIT 诚实组，会**系统性发明假空头成交路径并高估可开空头名义 / 低估空头失败率**；差异应**集中在转融券暂停后假无限券源桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假空头腿贡献差、可开空头名义差、失败率差在标定噪声带内可忽略，且「暂停后无限转融 / 忽略暂停日 / 券商自有券源桶 / vs A·K·BA·Z·AB·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 转融券通道/券源可借量 ≠ 融券标的名单；≠ 融资买入名单；≠ 保证金比例；≠ 融券卖出价限；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-03）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BB；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 K
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BB
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/转融券暂停」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.refinance_pause_start           写死 2024-07-11     # 中证金融暂停转融券起始
# params.refinance_stock_unwind_deadline 写死 2024-09-30     # 存量不得晚于该日了结
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K；BB≠K
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BB≠BA
# params.margin_ratio_handoff            写死 z_page         # 保证金比例交 Z；BB≠Z
# params.short_px_handoff                写死 ab_page        # 融券卖出价限交 AB
# params.bb0_primary_demo                写死 invent_unlimited_borrow_post_pause  # 风控补丁冻结；主报：暂停后仍发明无限转融券源；禁与 invent_ignore_refinance_pause 双挂争主表；BB1半泄露不得升格并列主报
# params.bb0_invent_unlimited_post_pause 写死 True
# params.bb1_ignore_pause_only           写死 True           # 半泄露：仅把暂停日当成未发生 / 忽略 pause 切片
# params.bb2_pit_cap_or_skip             写死 True
# params.borrow_honest                   写死 refinance_pause_cap_or_skip
# params.broker_own_inventory_bucket     写死 separate_sensitivity  # 券商自有券源另桶；不得默认=无限转融
# params.merge_with_A_fill               写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_AL_session_gap       写死 False
# params.merge_with_AM_halt              写死 False
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AQ_halt_cage         写死 False
# params.merge_with_AR_queue             写死 False
# params.merge_with_AS_ioc_fok           写死 False
# params.merge_with_AT_best5_to_limit    写死 False
# params.merge_with_AU_own_opp_best      写死 False
# params.merge_with_AV_call_match        写死 False
# params.merge_with_AW_close_fail        写死 False
# params.merge_with_AX_fund_fee          写死 False
# params.merge_with_AY_fund_tick         写死 False
# params.merge_with_AZ_open_fail         写死 False
# params.merge_with_BA_margin_buy        写死 False
# params.universe_rule                   写死 sse_szse_short_borrow_inventory_check
# params.missing_borrow_policy           写死 skip
# params.day_freq_proxy                  写死 refinance_pause_borrow_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y≠实验字母BB；params.N≠实验字母BB；亦≠单字母实验A/B/K；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
refinance_pause_start = "2024-07-11"
refinance_stock_unwind_deadline = "2024-09-30"
shortable_list_handoff = "k_page"
margin_buy_list_handoff = "ba_page"
margin_ratio_handoff = "z_page"
short_px_handoff = "ab_page"
bb0_primary_demo = "invent_unlimited_borrow_post_pause"  # 写死冻结；禁与 invent_ignore_refinance_pause 双挂；BB1半泄露不得升格并列主报
bb0_invent_unlimited_post_pause = True
bb1_ignore_pause_only = True
bb2_pit_cap_or_skip = True
borrow_honest = "refinance_pause_cap_or_skip"
broker_own_inventory_bucket = "separate_sensitivity"
universe_rule = "sse_szse_short_borrow_inventory_check"
missing_borrow_policy = "skip"
day_freq_proxy = "refinance_pause_borrow_sensitivity"

# 风控补丁写死冻结（2026-11-03；禁 null/holdout/跑后改口）
Y = 0.02   # 写死冻结；相对门槛 ≠ 实验字母 BB；≠ 单字母实验 A/B/K
G = 0.01   # 写死冻结
N = 0.05   # 写死冻结；失败/废单率差门槛 ≠ 实验字母 BB
Y2 = 0.015 # 写死冻结
```

### 2.2 组定义（BB0 / BB1 / BB2）

| 组 | 转融券暂停后券源 | 说明 |
|----|------------------|------|
| BB0 天真 | 按 `bb0_primary_demo` 单一主报（**写死冻结** `invent_unlimited_borrow_post_pause`） | 暂停后仍发明无限转融券源；禁与 invent_ignore_refinance_pause 双挂 |
| BB1 半泄露/混口径 | 仅把暂停日当成未发生 / 忽略 `refinance_pause_start` 切片 | 半泄露对照；不升格并列主报 |
| BB2 PIT 诚实 | 暂停后转融通道关闭或券源不保证 → cap/skip；自有券源另桶敏感性；存量 ≤2024-09-30；缺字段 skip | 诚实券源闸门 |

### 2.3 与近邻硬分列（merge_with_* 全 False）

- **≠A**：板上枯竭 ≠ 转融券源可借量。  
- **≠B**：不重开历史实验 B（印花税时点/财务可见/除权误判）旧题。  
- **≠K**：融券空头**名单** ≠ 转融券**券源/通道**可借量；名单内 ≠ 一定借得到。  
- **≠BA**：融资买入标的名单 ≠ 空头券源。  
- **≠Z**：保证金比例 ≠ 券源可借。  
- **≠AB**：融券卖出价限 ≠ 券源可借。  
- **≠T**：证管费误抽（**避开预检T**）≠ 本页。  
- **≠AN–BA**：不重开集合/失败回落/基金费用价位/融资买入名单链。

**风控补丁两条（已写死冻结 · 2026-11-03；禁 holdout；禁 null；禁双挂；禁跑后改口）**：

```
params.Y                            = 0.02                              # 写死冻结；名义差显著门槛；≠实验字母 BB；≠单字母实验 A/B/K
params.G                            = 0.01                              # 写死冻结；假空头腿桶相对对照差
params.N                            = 0.05                              # 写死冻结；失败/废单率差门槛；≠实验字母 BB
params.Y2                           = 0.015                             # 写死冻结；BB1（忽略暂停）相对 BB2 专项门槛
params.bb0_primary_demo             = invent_unlimited_borrow_post_pause # 写死冻结主报：暂停后仍发明无限转融券源；禁与 invent_ignore_refinance_pause 双挂争主表；BB1半泄露不得升格并列主报
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股拟开**融券卖出/空头腿**且消费 K 诚实名单（或显式声明本页不重开名单、仅测券源层）的样本（`universe_rule=sse_szse_short_borrow_inventory_check`）。融资买入腿交 BA，不进本页主宇宙。  
- **排除（默认）**：把 K/BA/Z/AB/A/T 主结论并进本页主表；缺券源字段却静默当无限可借；把「在名单内」写成「一定借得到」且不声明另页；把证管费误抽并进主病（交 T；**避开预检T**）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：转融券自 **2024-07-11** 起按暂停处理；存量了结不得晚于 **2024-09-30**；**禁止**用核对日「今天仍按无限转融」回放暂停后；**禁止**把融券标的名单（K）静默当成无限券源。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `bb0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **BB0 − BB2**：暂停后仍无限转融相对诚实券源闸门——假空头腿 / 可开空头名义吹胖、失败率低估。  
2. **BB1 − BB2**：忽略暂停日相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_unlimited_borrow_post_pause",
  "invent_ignore_refinance_pause",
  "honest_refinance_pause_cap_or_skip",
  "broker_own_inventory_sensitivity",
  "post_20240711_pause_window",
  "post_20240930_unwind_passed",
  "on_list_but_no_borrow",
  "vs_A_fill",
  "vs_K_shortable_list",
  "vs_BA_margin_buy_list",
  "vs_Z_margin_ratio",
  "vs_AB_short_px",
  "vs_T_csrc_fee",
  "vs_AE_stock_t0",
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可开空头名义/路径质量差 ΔNotional（BB0/BB1 相对 BB2）；  
2. 假空头腿贡献差 ΔFakeShortBorrow；  
3. 失败/废单率差 ΔFail；  
4. （可选）占用/可开倍数代理差 ΔCapacity（声明消费 Z 诚实比例或不测比例，不重开 Z）。

**相对判据（草稿）**：若 |ΔNotional| **≥ params.Y** 或 |ΔFakeShortBorrow 桶贡献| **≥ params.G** 或 |ΔNotional_(BB1−BB2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「转融券暂停后券源执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结 2026-11-03；与实验字母 BB / 单字母实验 A/B/K 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义差显著门槛（≠实验字母 BB；≠单字母实验 A/B/K） | **写死冻结** `0.02` |
| params.G | 假空头腿桶相对对照差 | **写死冻结** `0.01` |
| params.N | 失败/废单率差门槛（≠实验字母 BB） | **写死冻结** `0.05` |
| params.Y2 | BB1−BB2 专项门槛 | **写死冻结** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-16` |
| fill_time | 成交时点 | **写死** `next_open` |
| bb0_primary_demo | 天真主报枚举 | **写死冻结** `invent_unlimited_borrow_post_pause`（禁与 invent_ignore_refinance_pause 双挂；BB1半泄露不得升格并列主报） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 refinance_pause_cap_or_skip；禁与 A/K/BA/Z/AB/T 混主结论；禁荐股）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实暂停后券源闸门」与「无限转融 / 忽略暂停」，或无券源代理且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把融券空头名单（K）、融资买入名单（BA）、保证金比例（Z）、融券卖出价限（AB）、板上枯竭（A）、证管费（T）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「转融券暂停后假无限券源」写成「融券空头名单可空」为主病而不声明另页 K → 与 K 撞题，设计失效。  
4. 把「转融券暂停后假无限券源」写成「融资买入标的名单误开」而不声明另页 BA → 与 BA 撞题，设计失效。  
5. 把「转融券暂停后假无限券源」写成「保证金比例误铺」而不声明另页 Z → 与 Z 撞题，设计失效。  
6. 把「转融券暂停后假无限券源」写成「融券卖出价限/当日平」而不声明另页 AB → 与 AB 撞题，设计失效。  
7. 把「转融券暂停后假无限券源」写成「板上能否按板上价成交」而不声明另页 A → 与 A 撞题，设计失效。  
8. 把「转融券暂停后假无限券源」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
9. 把实验字母 BB 与单字母 A 或单字母 B 或单字母 K 或单字母 Z 或双字母 BA/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
10. holdout 反调 `bb0_primary_demo` / Y·G·N·Y2 → 结论无效。  
11. 用复权价算名义 → 标签与执行双错，结论无效。  
12. 把券商自有券源静默写成「等于无限转融券源」且不另桶 → 设计失效。  
13. 把「在融券名单内」静默写成「一定借得到」且不声明本页与 K 分列 → 与 K 撞题/设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融券卖出/空头腿标记（或拟开空头信号）；  
- 融券标的名单输入（消费 K 诚实 PIT，或显式旁路声明本页不重开名单）；  
- 转融券暂停日起始 `2024-07-11`、存量了结截止 `2024-09-30`；  
- 交易日历；可选券商自有券源/出借量代理；可选保证金比例输入（消费 Z，不重开）。

可选：转融通出借量历史；券商券源分桶；空头失败笔数字段。

**禁止**：用核对日「今天仍无限转融」铺满暂停后；用复权价；把融券名单当无限券源；把 K/BA/Z/AB/A/T/AN–BA 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BB`  
- **组**：BB0 / BB1 / BB2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`refinance_pause_start=2024-07-11`；`refinance_stock_unwind_deadline=2024-09-30`；`borrow_honest=refinance_pause_cap_or_skip`；`shortable_list_handoff=k_page`；`margin_buy_list_handoff=ba_page`；`margin_ratio_handoff=z_page`；`short_px_handoff=ab_page`；`broker_own_inventory_bucket=separate_sensitivity`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_short_borrow_inventory_check`；`missing_borrow_policy=skip`；`day_freq_proxy=refinance_pause_borrow_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 BB；**params.N≠实验字母 BB**；亦≠单字母实验 A/B/K；禁 null/holdout；风控补丁冻结 2026-11-03）；**`params.bb0_primary_demo` 写死冻结 `invent_unlimited_borrow_post_pause`**（禁与 invent_ignore_refinance_pause 双挂；BB1半泄露不得升格并列主报；风控补丁冻结 2026-11-03）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BB0/BB1/BB2 可开空头名义/路径质量、ΔFakeShortBorrow、ΔFail；分桶（暂停后无限转融 / 忽略暂停 / 自有券源敏感性 / vs A·K·BA·Z·AB·T）。  
- 自检布尔：BB2 是否 refinance_pause_cap_or_skip；BB0 是否单一主报；BB1 是否仅忽略暂停；是否未与 A/K/BA/Z/AB/T 混主结论；holdout 是否未反调；**是否未把实验字母 BB 与 A 或 B 或 K 或 Z 或 BA 或 AB 或 AZ 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–BA 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-K / 假设-BA / 假设-Z / 假设-AB**；**是否未再改 BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把无限转融或忽略暂停冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BA 及其他 A/D–BA 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-K**；**不改假设-BA**；**不改假设-Z**；**不改假设-AB**；**勿再改 BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：融券标的名单 ≠ 一定借得到；转融券自 2024-07-11 暂停；券商自有券源可能仍出借但不得默认=无限转融。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BB** 标准件，**不改口径主线**，**不改假设 A–BA 正文**。与实验 A/K/BA/Z/AB/T 分工：**A=板上枯竭门槛；K=融券空头名单；BA=融资买入标的名单；Z=保证金比例；AB=融券卖出价限；T=证管费（避开）；BB=转融券暂停后假无限券源（BB≠A≠B≠K≠BA≠Z≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；转融暂停切日 + 日频券源敏感性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**borrow_honest=refinance_pause_cap_or_skip 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死 0.02/0.01/0.05/0.015（params.Y≠实验字母 BB；params.N≠实验字母 BB；亦≠单字母实验 A/B/K；风控补丁冻结 2026-11-03）**；**bb0_primary_demo 写死 invent_unlimited_borrow_post_pause（禁双挂；BB1半泄露不得升格并列主报；风控补丁冻结 2026-11-03）** |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BB**；**`params.Y` ≠ 单字母实验 A/B/K**；**`params.N` ≠ 实验字母 BB**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bb0_primary_demo`**：**写死冻结** **`invent_unlimited_borrow_post_pause`**；禁与 **`invent_ignore_refinance_pause`** 双挂争主表（只挂一个 primary）；**BB1 半泄露不得升格并列主报**。

**切日保留（已通写死）**：`params.refinance_pause_start=2024-07-11`；`params.refinance_stock_unwind_deadline=2024-09-30`（不改口）。

**与 BA/K/AB 硬分列（保留）**：本页 = **转融券暂停后券源/通道可借量**；BA = **融资买入**标的名单；K = **融券空头名单**闸门；AB = **融券卖出价限**；名单内 ≠ 一定借得到 ≠ 融资可买 ≠ 空头价限；禁止捆成「两融名单一张表=无限券源」；不改假设-BA；不改假设-K；不改假设-AB。

---

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BB**；亦≠单字母实验 A/B/K；**params.N≠实验字母 BB**；禁 null/holdout/跑后改口）；② `params.bb0_primary_demo=invent_unlimited_borrow_post_pause`（禁与 `invent_ignore_refinance_pause` 双挂争主表；BB1半泄露不得升格并列主报）。切日保留：`refinance_pause_start=2024-07-11`；`refinance_stock_unwind_deadline=2024-09-30`。与 BA/K/AB 硬分列保留。参考总管派令 / 风控预检有条件通过。未改 Y/Z/AA–BA 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-BA；不改假设-Z；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿假设-BB（转融券暂停后假无限券源）。待预检键建议 Y/G/N/Y2=0.02/0.01/0.05/0.015；bb0_primary_demo=invent_unlimited_borrow_post_pause（禁双挂 invent_ignore_refinance_pause）。与 A/B/K/BA/Z/AB/T/AN–BA 硬分列；**双字母 BB ≠ 单字母 B**；明确避开预检T旧题。未改 Y/Z/AA–BA 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-K；不改假设-BA；不改假设-Z；不改假设-AB；勿再改 BA/AZ/AY/AX/AW；结论栏仍空；不开回测；不抢 A。

