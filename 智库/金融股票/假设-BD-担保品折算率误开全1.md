# 假设 BD · 担保品折算率误开全1 / 用核对日折算率铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BC 补丁已收、写下一纸面 BD；清单撞题规则另选正交执行缺口（**可充抵保证金证券折算率** ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓）；选题自交易所融资融券细则公开规则：可充抵保证金证券按市值×**折算率**计入保证金可用余额；交易所公布名单与折算率上限（上证180成分股最高不超过 **70%**、其他 A 股最高不超过 **65%**、ETF 最高不超过 **90%**、国债/货币基金/券商现金管理产品最高不超过 **95%**、其他基金与债券最高不超过 **80%**；被实施风险警示、暂停上市或进入退市整理期的 A 股、权证折算率为 **0%**；2016-12-12 起静态市盈率 ≥300 倍或为负的股票折算率下调为 **0%**）；会员公布折算率不得高于本所标准，可动态加严；本所可调整名单与折算率并公布（上交所《融资融券交易实施细则》保证金与担保物章；深市同口径上限族）；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BD ≠ 单字母 B**）/ D（次日开/收时点与停牌；**双字母 BD ≠ 单字母 D**）/ Z（**开仓**融资/融券保证金比例；**BD≠Z**）/ BA（**融资买入**标的名单；**BD≠BA**）/ BB（**转融券暂停后券源**；**BD≠BB**）/ BC（**维持担保比例强制平仓**；**BD≠BC**）/ K（融券空头名单；**BD≠K**）/ AB（融券卖出价限；**BD≠AB**）/ E（整手）/ M（盘后）/ O（大宗）/ N（收盘切日/假 GTC）/ Q（可转债）/ R（股票 ETF 假回转）/ S/T/U/V（费用层；**避开预检T旧题**）/ W（除权判板）/ L（市价通道）/ AN–BC（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平等）/ Y（集合量计入日线；**实验字母 Y ≠ params.Y**）/ AA–BC / AC–BC 等**分列**；**新建实验 BD**  
状态：**草稿 · 待数据 · 待跑 · 预检有条件通过·两条已冻结待复检**（结论栏空；禁止把「担保品折算率全按 1.0 / 用核对日折算率表铺满全历史」当诚实保证金可用余额；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BC 及其他 A/D–BC 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-K；不改假设-AB；勿再改 BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BD。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **可充抵保证金证券折算率是否把市值诚实折成保证金可用**。**双字母 BD ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BD ≠ 单字母 B**。与假设 **D（成交时点与停牌）** **硬分列**：D = 次日开/收成交时点与停牌不可交易；本页 = 折算率/保证金可用；**双字母 BD ≠ 单字母 D**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值（如 50%/80%/100% 切日）；本页 = 可充抵保证金证券的**折算率**与名单是否诚实计入保证金可用余额；开仓比例 ≠ 折算率。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开**融资买入**腿（标的闸门）；本页 = 已持/拟充抵证券按多少折算率进保证金可用；标的可买 ≠ 折算率。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 空头**券源可借量**；本页 = 担保品**折算**；券源 ≠ 折算率。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = 持仓存续期**维持担保比例**是否触发追保/强平（交易所维持公式用证券**市值总和**，不乘本页折算率）；本页 = **开仓/加仓能力侧**保证金可用余额计算中的折算率；维持线 ≠ 折算率。与假设 **K / AB** **硬分列**：不重开融券名单与空头价限。与假设 AN–BC **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BD** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 D**（成交时点与停牌）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BD / 假设-BD / hypothesis_id=BD / 组 BD0·BD1·BD2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 BD 混读或互改。亦**禁止**把实验字母 BD 与单字母 **A**、单字母 **B**、单字母 **D**、单字母 **Z**、单字母 **K**、双字母 **BA**、双字母 **BB**、双字母 **BC**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `bd0_*` 以外的实验页混读。**双字母 BD ≠ 单字母 A ≠ 单字母 B ≠ 单字母 D ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC**；**params.Y ≠ 实验字母 BD**；**params.N ≠ 实验字母 BD**。

---

## 1. 一句话假设（可检验、可证伪）

同一两融开仓/加仓路径、同一未复权价、同一 T+1、同一开仓保证金比例输入（Z 层诚实或显式旁路声明「本页不重开开仓比例」）下，把「可充抵保证金证券折算率一律按 1.0（市值全额当保证金）」或「全样本用核对日当天折算率表（含券商加严）回放历史」当成默认，相对「每个交易日按当时有效交易所公布折算率上限族与可充抵名单 PIT（股票/ETF/国债货币/其他基金债券分档；风险警示/暂停上市/退市整理/权证=0；2016-12-12 起高市盈或亏损股=0；会员可加严但不得高于本所；缺字段 skip/敏感性）」的诚实组，会**系统性发明假保证金可用余额并高估可开名义 / 低估因折算率不足导致的开仓失败率**；差异应**集中在担保品折算率误开全1桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假可用保证金贡献差、可开名义差、开仓失败率差在标定噪声带内可忽略，且「折算率全1 / 核对日折算率泄露 / 风险警示·退市整理折算0 / 高市盈折算0切日 / vs A·Z·BA·BB·BC·K·AB·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 担保品折算率 ≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 维持担保强平；≠ 融券名单；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；待预检；纸面占位建议如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BD；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 D；≠ 实验字母 Z
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BD
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 折算腿
# params.haircut_cap_sse180              写死 0.70           # 上证180成分股折算率上限
# params.haircut_cap_other_ashare        写死 0.65           # 其他 A 股上限
# params.haircut_cap_etf                 写死 0.90
# params.haircut_cap_mmf_treasury        写死 0.95           # 货币基金/国债/券商现金管理
# params.haircut_cap_other_fund_bond     写死 0.80
# params.haircut_risk_warn_exit_warrant  写死 0.00           # 风险警示/暂停上市/退市整理/权证
# params.haircut_high_pe_zero_start      写死 2016-12-12     # 静态市盈≥300或负 → 0%
# params.haircut_high_pe_threshold       写死 300
# params.haircut_honest                  写死 exchange_cap_pit_then_broker_stricter_bucket
# params.broker_stricter_haircut_bucket  写死 separate_sensitivity  # 券商加严折算另桶；不得默认=交易所上限更松
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BD≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BD≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BD≠BB
# params.maint_force_handoff             写死 bc_page        # 维持担保强平交 BC；BD≠BC
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K
# params.short_px_handoff                写死 ab_page        # 融券卖出价限交 AB
# params.bd0_primary_demo                写死冻结 invent_haircut_all_one  # 主报：折算率全按1.0；禁与 invent_asof_leak_haircut 双挂争主表；BD1半泄露不得升格并列主报
# params.bd0_invent_haircut_all_one      写死 True
# params.bd1_asof_leak_haircut_only      写死 True           # 半泄露：仅用核对日折算率表铺满历史
# params.bd2_pit_haircut                 写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_K_shortable_list     写死 False
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
# params.merge_with_BB_refinance         写死 False
# params.merge_with_BC_maint             写死 False
# params.universe_rule                   写死 sse_szse_collateral_haircut_check
# params.missing_haircut_policy          写死 skip
# params.day_freq_proxy                  写死 collateral_haircut_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  纸面占位建议 0.02/0.01/0.05/0.015  # 待预检写死；params.Y≠实验字母BD；params.N≠实验字母BD；亦≠单字母实验A/B/D/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
margin_channel_start = "2010-03-31"
haircut_cap_sse180 = 0.70
haircut_cap_other_ashare = 0.65
haircut_cap_etf = 0.90
haircut_cap_mmf_treasury = 0.95
haircut_cap_other_fund_bond = 0.80
haircut_risk_warn_exit_warrant = 0.00
haircut_high_pe_zero_start = "2016-12-12"
haircut_high_pe_threshold = 300
haircut_honest = "exchange_cap_pit_then_broker_stricter_bucket"
broker_stricter_haircut_bucket = "separate_sensitivity"
margin_ratio_handoff = "z_page"
margin_buy_list_handoff = "ba_page"
refinance_borrow_handoff = "bb_page"
maint_force_handoff = "bc_page"
shortable_list_handoff = "k_page"
short_px_handoff = "ab_page"
bd0_primary_demo = "invent_haircut_all_one"  # 待预检建议主报；禁与 invent_asof_leak_haircut 双挂；BD1半泄露不得升格并列主报
bd0_invent_haircut_all_one = True
bd1_asof_leak_haircut_only = True
bd2_pit_haircut = True
universe_rule = "sse_szse_collateral_haircut_check"
missing_haircut_policy = "skip"
day_freq_proxy = "collateral_haircut_sensitivity"
fail_policy = "skip"

# 纸面占位（待预检写死冻结；禁 null/holdout/跑后改口）
Y = 0.02   # 占位建议；相对门槛 ≠ 实验字母 BD；≠ 单字母实验 A/B/D/Z
G = 0.01   # 占位建议
N = 0.05   # 占位建议；失败/开仓失败率差门槛 ≠ 实验字母 BD
Y2 = 0.015 # 占位建议
```

### 2.2 组定义（BD0 / BD1 / BD2）

| 组 | 担保品折算率 | 说明 |
|----|----------------|------|
| BD0 天真 | 按 `bd0_primary_demo` 单一主报（建议 `invent_haircut_all_one`） | 折算率一律 1.0（市值全额当保证金）；禁与 invent_asof_leak_haircut 双挂 |
| BD1 半泄露/混口径 | 仅用核对日折算率表（含券商加严）铺满历史 | 半泄露对照；不升格并列主报 |
| BD2 PIT 诚实 | exchange_cap_pit_then_broker_stricter_bucket；按当时有效上限族+名单；风险警示/退市整理/权证=0；高市盈切日后=0；券商加严另桶；缺字段 skip | 诚实折算闸门 |

### 2.3 与近邻硬分列（merge_with_* 全 False）

- **≠A**：板上枯竭 ≠ 担保品折算率。  
- **≠B**：不重开历史实验 B（印花税时点/财务可见/除权误判）旧题。  
- **≠D**：成交时点/停牌 ≠ 折算率。  
- **≠Z**：**开仓**保证金**比例** ≠ **折算率**/可充抵名单。  
- **≠BA**：融资买入**名单** ≠ 折算率。  
- **≠BB**：转融券**券源** ≠ 折算率。  
- **≠BC**：**维持担保比例强平**（市值总和进维持公式）≠ **折算率**（进保证金可用余额）。  
- **≠K / AB**：融券名单 / 空头价限 ≠ 折算率。  
- **≠T**：证管费误抽（**避开预检T**）≠ 本页。  
- **≠AN–BC**：不重开集合/失败回落/基金费价位/融资名单/转融券源/维持强平等。

**待预检键（纸面占位建议；禁 holdout；禁 null；禁双挂；禁跑后改口）**：

```
params.Y                            = 0.02                              # 占位建议；名义差显著门槛；≠实验字母 BD；≠单字母实验 A/B/D/Z
params.G                            = 0.01                              # 占位建议；假可用保证金桶相对对照差
params.N                            = 0.05                              # 占位建议；失败/开仓失败率差门槛；≠实验字母 BD
params.Y2                           = 0.015                             # 占位建议；BD1（核对日折算率泄露）相对 BD2 专项门槛
params.bd0_primary_demo             = invent_haircut_all_one            # 待预检建议主报：折算率全1；禁与 invent_asof_leak_haircut 双挂争主表；BD1半泄露不得升格并列主报
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股拟开/已开**融资或融券**且消费 Z 诚实开仓比例（或显式声明本页不重开开仓比例）、并以证券充抵保证金的信用账户代理样本（`universe_rule=sse_szse_collateral_haircut_check`）。融资买入名单交 BA，转融券源交 BB，维持强平交 BC，不进本页主病。  
- **排除（默认）**：把 Z/BA/BB/BC/K/AB/A/T 主结论并进本页主表；缺折算字段却静默当折算率=1；把「开仓保证金比例够」写成「折算率=1」且不声明另页 Z；把证管费误抽并进主病（交 T；**避开预检T**）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：折算率按交易所当时有效公布上限族与可充抵名单；**禁止**用核对日「今天折算率表」回放全历史当唯一诚实组；**禁止**把开仓保证金比例（Z）静默当成折算率；**禁止**把维持担保比例公式（BC，市值不乘折算）与本页保证金可用余额公式混成一句。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `bd0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **BD0 vs BD2**：折算率全1相对诚实折算闸门——假可用保证金 / 可开名义吹胖、开仓失败率低估。  
2. **BD1 vs BD2**：核对日折算率泄露相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_haircut_all_one",
  "invent_asof_leak_haircut",
  "honest_exchange_cap_pit",
  "risk_warn_exit_warrant_zero",
  "high_pe_zero_post_20161212",
  "sse180_vs_other_ashare_cap",
  "etf_vs_stock_cap",
  "broker_stricter_haircut_sensitivity",
  "vs_A_fill",
  "vs_Z_margin_ratio",
  "vs_BA_margin_buy_list",
  "vs_BB_refinance_borrow",
  "vs_BC_maint_force",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_T_csrc_fee",
  "vs_AE_stock_t0",
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可开两融名义/路径质量差 ΔNotional（BD0/BD1 相对 BD2）；  
2. 假可用保证金贡献差 ΔFakeMarginAvail；  
3. 开仓失败率差 ΔFail；  
4. （可选）折算率分档敏感性差 ΔHaircutBucket（声明日频敏感性，不冒充逐券商实时折算精确复盘）。

**相对判据（草稿）**：若 |ΔNotional| **≥ params.Y** 或 |ΔFakeMarginAvail 桶贡献| **≥ params.G** 或 |ΔNotional_(BD1 vs BD2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「担保品折算率执行鸿沟显著」。

**params.Y / G / N / Y2（已写死冻结；与实验字母 BD / 单字母实验 A/B/D/Z 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义差显著门槛（≠实验字母 BD；≠单字母实验 A/B/D/Z） | **写死冻结** `0.02` |
| params.G | 假可用保证金桶相对对照差 | **写死冻结** `0.01` |
| params.N | 失败/开仓失败率差门槛（≠实验字母 BD） | **写死冻结** `0.05` |
| params.Y2 | BD1 vs BD2 专项门槛 | **写死冻结** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-16` |
| fill_time | 成交时点 | **写死** `next_open` |
| bd0_primary_demo | 天真主报枚举 | **写死冻结** `invent_haircut_all_one`（禁与 invent_asof_leak_haircut 双挂；BD1半泄露不得升格并列主报） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 exchange_cap_pit；禁与 A/Z/BA/BB/BC/K/AB/T 混主结论；禁荐股）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实折算闸门」与「折算率全1 / 核对日折算率泄露」，或无折算代理且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、融券名单（K）、融券卖出价限（AB）、板上枯竭（A）、证管费（T）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「担保品折算率误开全1」写成「开仓保证金比例误铺」而不声明另页 Z → 与 Z 撞题，设计失效。  
4. 把「担保品折算率误开全1」写成「融资买入标的名单误开」而不声明另页 BA → 与 BA 撞题，设计失效。  
5. 把「担保品折算率误开全1」写成「转融券暂停后假无限券源」而不声明另页 BB → 与 BB 撞题，设计失效。  
6. 把「担保品折算率误开全1」写成「维持担保比例强制平仓误关」而不声明另页 BC → 与 BC 撞题，设计失效（维持公式用市值、不用本页折算）。  
7. 把「担保品折算率误开全1」写成「融券空头名单可空」为主病而不声明另页 K → 与 K 撞题，设计失效。  
8. 把「担保品折算率误开全1」写成「板上能否按板上价成交」而不声明另页 A → 与 A 撞题，设计失效。  
9. 把「担保品折算率误开全1」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
10. 把实验字母 BD 与单字母 A 或单字母 B 或单字母 D 或单字母 Z 或双字母 BA/BB/BC/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `bd0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价算可充抵证券市值 → 标签与执行双错，结论无效。  
13. 把券商加严折算静默写成「等于交易所上限更松」且不另桶 → 设计失效。  
14. 把「维持担保比例够」静默写成「折算率=1、可任意加仓」且不声明本页与 BC/Z 分列 → 撞题/设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资/融券拟开腿标记、拟充抵保证金证券代码/市值代理、现金保证金；  
- 开仓保证金比例输入（消费 Z 诚实 PIT，或显式旁路声明本页不重开开仓比例）；  
- 可充抵保证金证券名单与折算率 PIT 表（或按上限族+风险警示/退市整理/高市盈规则代理）；  
- 交易日历；可选券商加严折算分桶；静态市盈率字段（供 2016-12-12 后 0% 切日）。

可选：交易所逐日公布折算率明细；会员加严表；可充抵名单调入调出公告日。

**禁止**：用核对日「今天折算率表」铺满当唯一诚实组；用复权价；把开仓保证金比例当折算率；把维持担保比例公式当成乘折算；把 Z/BA/BB/BC/K/AB/A/T/AN–BC 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BD`  
- **组**：BD0 / BD1 / BD2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`haircut_cap_sse180=0.70`；`haircut_cap_other_ashare=0.65`；`haircut_cap_etf=0.90`；`haircut_cap_mmf_treasury=0.95`；`haircut_cap_other_fund_bond=0.80`；`haircut_risk_warn_exit_warrant=0.00`；`haircut_high_pe_zero_start=2016-12-12`；`haircut_high_pe_threshold=300`；`haircut_honest=exchange_cap_pit_then_broker_stricter_bucket`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`broker_stricter_haircut_bucket=separate_sensitivity`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_collateral_haircut_check`；`missing_haircut_policy=skip`；`day_freq_proxy=collateral_haircut_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 BD；**params.N≠实验字母 BD**；亦≠单字母实验 A/B/D/Z；禁 null/holdout/跑后改口）；**`params.bd0_primary_demo` 写死冻结 `invent_haircut_all_one`**（禁与 invent_asof_leak_haircut 双挂；BD1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BD0/BD1/BD2 可开名义/路径质量、ΔFakeMarginAvail、ΔFail；分桶（折算率全1 / 核对日折算率泄露 / 风险警示·退市整理折算0 / 高市盈折算0 / vs A·Z·BA·BB·BC·K·AB·T）。  
- 自检布尔：BD2 是否 exchange_cap_pit；BD0 是否单一主报；BD1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/K/AB/T 混主结论；holdout 是否未反调；**是否未把实验字母 BD 与 A 或 B 或 D 或 Z 或 BA 或 BB 或 BC 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–BC 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-Z / 假设-BA / 假设-BB / 假设-BC / 假设-K / 假设-AB**；**是否未再改 BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把折算率全1或核对日折算率泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BC 及其他 A/D–BC 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-Z**；**不改假设-BA**；**不改假设-BB**；**不改假设-BC**；**不改假设-K**；**不改假设-AB**；**勿再改 BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）与维持担保强平（BC）之外，保证金可用余额须按可充抵证券**折算率**诚实折算；交易所上限族与 0% 特例（风险警示/退市整理/高市盈等）不得默认=1。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BD** 标准件，**不改口径主线**，**不改假设 A–BC 正文**。与实验 A/Z/BA/BB/BC/K/AB/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓；K=融券空头名单；AB=融券卖出价限；T=证管费（避开）；BD=担保品折算率误开全1（BD≠A≠B≠D≠Z≠BA≠BB≠BC≠K≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频可充抵市值 + 折算率 PIT/上限族代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**haircut_honest=exchange_cap_pit_then_broker_stricter_bucket 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BD；params.N≠实验字母 BD；亦≠单字母实验 A/B/D/Z；禁 null/holdout/跑后改口）**；**bd0_primary_demo 写死冻结 invent_haircut_all_one（禁双挂 invent_asof_leak_haircut；BD1半泄露不得升格并列主报）**；锚点保留 haircut_cap_sse180=0.70 / other_ashare=0.65 / etf=0.90 / mmf_treasury=0.95 / other_fund_bond=0.80 / risk_warn_exit_warrant=0.00 / high_pe_zero_start=2016-12-12 / margin_channel_start=2010-03-31 |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BD**；**`params.Y` ≠ 单字母实验 A/B/D/Z**；**`params.N` ≠ 实验字母 BD**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bd0_primary_demo`**：**写死冻结** **`invent_haircut_all_one`**；禁与 **`invent_asof_leak_haircut`** 双挂争主表（只挂一个 primary）；**BD1 半泄露不得升格并列主报**。

**折算率锚保留（已通写死）**：`params.haircut_cap_sse180=0.70`；`params.haircut_cap_other_ashare=0.65`；`params.haircut_cap_etf=0.90`；`params.haircut_cap_mmf_treasury=0.95`；`params.haircut_cap_other_fund_bond=0.80`；`params.haircut_risk_warn_exit_warrant=0.00`；`params.haircut_high_pe_zero_start=2016-12-12`；`params.margin_channel_start=2010-03-31`（及正文已有 `haircut_high_pe_threshold=300` / `haircut_honest=exchange_cap_pit_then_broker_stricter_bucket` 等锚点；不改口）。

**与 Z/BA/BB/BC/A/K/AB/B/D 硬分列（保留）**：本页 = **可充抵保证金证券折算率 / 保证金可用余额**；Z = **开仓**保证金比例；BA = **融资买入**标的名单；BB = **转融券暂停后券源**；BC = **维持担保比例强制平仓**；A = **板上枯竭**；K = **融券空头名单**；AB = **融券卖出价限**；B = 历史实验 B 旧位；D = 次日开/收时点与停牌；折算率 ≠ 开仓比例 ≠ 融资可买 ≠ 转融券源 ≠ 维持强平 ≠ 板上枯竭 ≠ 融券名单 ≠ 空头价限 ≠ 成交时点；**双字母 BD ≠ 单字母 A ≠ 单字母 B ≠ 单字母 D ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 AB ≠ 单字母 K**；禁止捆成「两融一张表=折算率全1」；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-A；不改假设-K；不改假设-AB；不改假设-B；不改假设-D。

---

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BD**；亦≠单字母实验 A/B/D/Z；**params.N≠实验字母 BD**；禁 null/holdout/跑后改口）；② `params.bd0_primary_demo=invent_haircut_all_one`（禁与 `invent_asof_leak_haircut` 双挂争主表；BD1半泄露不得升格并列主报）。折算率锚保留：`haircut_cap_sse180=0.70`；`other_ashare=0.65`；`etf=0.90`；`mmf_treasury=0.95`；`other_fund_bond=0.80`；`risk_warn_exit_warrant=0.00`；`haircut_high_pe_zero_start=2016-12-12`；`margin_channel_start=2010-03-31`。与 Z/BA/BB/BC/A/K/AB/B/D 硬分列保留。参考总管派令 / 风控预检有条件通过。未改 Y/Z/AA–BC 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-D；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-K；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BC 补丁已收 → 写假设-BD；自立 BD，勿占 BC/BB/BA/B/D/A/Z；避开预检T；不开回测；禁实盘/荐股；params.Y/N≠实验字母 BD）。