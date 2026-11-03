# 假设 BC · 维持担保比例强制平仓误关 / 用核对日维持线铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BB 补丁已收、写下一纸面 BC；清单撞题规则另选正交执行缺口（**维持担保比例/强制平仓** ≠ 开仓保证金比例 ≠ 融资买入名单 ≠ 转融券券源）；选题自交易所融资融券细则公开规则：维持担保比例不得低于 **130%**；低于 130% 须在约定期限（不超过 2 个交易日）追保，追保后不得低于 **150%**；超过 **300%** 可提取，提取后不得低于 300%；会员可加严不得低于本所标准；未能按期交足担保物可强制平仓（上交所《融资融券交易实施细则》维持担保比例条款；深市同口径下限；券商合同可另设警戒/追保/盘中紧急线，本页以**交易所下限**为最宽可维持仓）；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BC ≠ 单字母 B**）/ C（清单「实验 C」股票池当时名单/幸存者偏差；**双字母 BC ≠ 单字母 C**）/ Z（**开仓**融资/融券保证金比例；**BC≠Z**）/ BA（**融资买入**标的名单；**BC≠BA**）/ BB（**转融券暂停后券源**；**BC≠BB**）/ K（融券空头名单；**BC≠K**）/ AB（融券卖出价限；**BC≠AB**）/ E（整手）/ M（盘后）/ O（大宗）/ N（收盘切日/假 GTC）/ Q（可转债）/ R（股票 ETF 假回转）/ S/T/U/V（费用层；**避开预检T旧题**）/ W（除权判板）/ L（市价通道）/ D（开/收时点与停牌）/ AN–BB（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源等）/ Y（集合量计入日线；**实验字母 Y ≠ params.Y**）/ AA–BB / AC–BB 等**分列**；**新建实验 BC**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「两融仓永不触发强制平仓 / 维持担保比例永不检查 / 用核对日现行维持线+券商加严线铺满全历史」当诚实可维持杠杆能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BB 及其他 A/D–BB 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-K；不改假设-AB；勿再改 BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BC。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **已开两融仓后维持担保比例是否触发追保/强制平仓**。**双字母 BC ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BC ≠ 单字母 B**。与假设 **C（股票池当时名单）** **硬分列**：C = 幸存者偏差/成分 PIT；本页 = 维持担保/强平执行；**双字母 BC ≠ 单字母 C**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金比例/可开名义；本页 = **持仓存续期**维持担保比例与强制平仓；开仓比例 ≠ 维持比例 ≠ 强平路径。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开融资买入腿（名单闸门）；本页 = 开仓后会不会因维持担保触发强平。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 空头**券源可借量**；本页 = 多空仓**维持担保/强平**；券源 ≠ 维持线。与假设 **K / AB** **硬分列**：不重开融券名单与空头价限。与假设 AN–BB **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BC** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 C**（股票池当时名单）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BC / 假设-BC / hypothesis_id=BC / 组 BC0·BC1·BC2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 BC 混读或互改。亦**禁止**把实验字母 BC 与单字母 **A**、单字母 **B**、单字母 **C**、单字母 **Z**、单字母 **K**、双字母 **BA**、双字母 **BB**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `bc0_*` 以外的实验页混读。**双字母 BC ≠ 单字母 A ≠ 单字母 B ≠ 单字母 C ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB**；**params.Y ≠ 实验字母 BC**；**params.N ≠ 实验字母 BC**。

---

## 1. 一句话假设（可检验、可证伪）

同一两融持仓路径、同一未复权价、同一 T+1、同一开仓保证金输入（Z 层诚实或显式旁路声明「本页不重开开仓比例」）下，把「维持担保比例永不检查 / 永不触发强制平仓 / 两融仓可无限期按原名义持有」或「全样本用核对日当天维持担保线（含券商加严线）回放历史」当成默认，相对「每个交易日按当时有效交易所维持担保下限（不得低于 130%；低于则约定期限追保且追保后不得低于 150%；超过 300% 可提取且提取后不得低于 300%；会员可加严但本页以交易所下限为最宽可维持；触发未追保则强制减仓或记强平失败；缺字段 skip/敏感性）」的 PIT 诚实组，会**系统性发明假可维持杠杆仓并高估可持有名义 / 低估强平失败率与被动减仓冲击**；差异应**集中在维持担保比例强制平仓误关桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假可维持仓贡献差、可持有名义差、强平/失败率差在标定噪声带内可忽略，且「永不强平 / 核对日维持线泄露 / 低于 130% 未追保窗 / vs A·Z·BA·BB·K·AB·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 维持担保比例/强制平仓 ≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 融券名单；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；待预检；纸面占位建议如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BC；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 C；≠ 实验字母 Z
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BC
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 维持腿
# params.maint_ratio_floor               写死 1.30           # 交易所维持担保比例下限 130%
# params.maint_ratio_after_call          写死 1.50           # 追保后不得低于 150%
# params.maint_ratio_withdraw            写死 3.00           # 提取线 300%；提取后不得低于 300%
# params.maint_call_max_days             写死 2              # 追保期限不得超过 2 个交易日（交易所上限）
# params.maint_honest                    写死 exchange_floor_then_force_close
# params.broker_stricter_bucket          写死 separate_sensitivity  # 券商加严线另桶；不得默认=交易所下限更松
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BC≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BC≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BC≠BB
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K
# params.short_px_handoff                写死 ab_page        # 融券卖出价限交 AB
# params.bc0_primary_demo                建议 invent_no_force_close  # 待预检写死；主报：永不检查维持担保/永不强制平仓；禁与 invent_asof_leak_maint_ratio 双挂争主表；BC1半泄露不得升格并列主报
# params.bc0_invent_no_force_close       写死 True
# params.bc1_asof_leak_maint_only        写死 True           # 半泄露：仅用核对日维持线（含加严）铺满历史
# params.bc2_pit_maint_force             写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
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
# params.universe_rule                   写死 sse_szse_margin_maint_force_check
# params.missing_maint_policy            写死 skip
# params.day_freq_proxy                  写死 maint_force_close_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  纸面占位建议 0.02/0.01/0.05/0.015  # 待预检写死；params.Y≠实验字母BC；params.N≠实验字母BC；亦≠单字母实验A/B/C/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
margin_channel_start = "2010-03-31"
maint_ratio_floor = 1.30
maint_ratio_after_call = 1.50
maint_ratio_withdraw = 3.00
maint_call_max_days = 2
maint_honest = "exchange_floor_then_force_close"
broker_stricter_bucket = "separate_sensitivity"
margin_ratio_handoff = "z_page"
margin_buy_list_handoff = "ba_page"
refinance_borrow_handoff = "bb_page"
shortable_list_handoff = "k_page"
short_px_handoff = "ab_page"
bc0_primary_demo = "invent_no_force_close"  # 待预检写死；禁与 invent_asof_leak_maint_ratio 双挂；BC1半泄露不得升格并列主报
bc0_invent_no_force_close = True
bc1_asof_leak_maint_only = True
bc2_pit_maint_force = True
universe_rule = "sse_szse_margin_maint_force_check"
missing_maint_policy = "skip"
day_freq_proxy = "maint_force_close_sensitivity"
fail_policy = "skip"

# 待预检键 / 纸面占位建议（拉数前须冻结；禁 null/holdout/跑后改口）
Y = 0.02   # 建议；相对门槛 ≠ 实验字母 BC；≠ 单字母实验 A/B/C/Z
G = 0.01   # 建议
N = 0.05   # 建议；失败/强平率差门槛 ≠ 实验字母 BC
Y2 = 0.015 # 建议
```

### 2.2 组定义（BC0 / BC1 / BC2）

| 组 | 维持担保/强平 | 说明 |
|----|----------------|------|
| BC0 天真 | 按 `bc0_primary_demo` 单一主报（建议 `invent_no_force_close`） | 永不检查维持担保 / 永不强制平仓；禁与 invent_asof_leak_maint_ratio 双挂 |
| BC1 半泄露/混口径 | 仅用核对日维持线（含券商加严）铺满历史 | 半泄露对照；不升格并列主报 |
| BC2 PIT 诚实 | exchange_floor_then_force_close；低于 130%→约定期限追保；未追保→强平/记失败；券商加严另桶；缺字段 skip | 诚实维持/强平闸门 |

### 2.3 与近邻硬分列（merge_with_* 全 False）

- **≠A**：板上枯竭 ≠ 维持担保强平。  
- **≠B**：不重开历史实验 B（印花税时点/财务可见/除权误判）旧题。  
- **≠C**：股票池当时名单 ≠ 维持担保强平。  
- **≠Z**：**开仓**保证金比例 ≠ **维持**担保比例/强平。  
- **≠BA**：融资买入**名单** ≠ 开仓后维持/强平。  
- **≠BB**：转融券**券源** ≠ 维持担保/强平。  
- **≠K / AB**：融券名单 / 空头价限 ≠ 维持线。  
- **≠T**：证管费误抽（**避开预检T**）≠ 本页。  
- **≠AN–BB**：不重开集合/失败回落/基金费价位/融资名单/转融券源等。

**待预检键建议（纸面占位；禁 holdout；禁 null；禁双挂；禁跑后改口；待风控写死）**：

```
params.Y                            = 0.02                              # 建议；名义差显著门槛；≠实验字母 BC；≠单字母实验 A/B/C/Z
params.G                            = 0.01                              # 建议；假可维持仓桶相对对照差
params.N                            = 0.05                              # 建议；失败/强平率差门槛；≠实验字母 BC
params.Y2                           = 0.015                             # 建议；BC1（核对日维持线泄露）相对 BC2 专项门槛
params.bc0_primary_demo             = invent_no_force_close             # 建议主报：永不强制平仓/永不检查维持担保；禁与 invent_asof_leak_maint_ratio 双挂争主表；BC1半泄露不得升格并列主报
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股拟开/已开**融资或融券**且消费 Z 诚实开仓比例（或显式声明本页不重开开仓比例）的信用账户代理样本（`universe_rule=sse_szse_margin_maint_force_check`）。融资买入名单交 BA，转融券源交 BB，不进本页主病。  
- **排除（默认）**：把 Z/BA/BB/K/AB/A/T 主结论并进本页主表；缺维持字段却静默当永不强平；把「开仓保证金够」写成「永可维持」且不声明另页 Z；把证管费误抽并进主病（交 T；**避开预检T**）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：维持担保下限按交易所当时有效文本（现行 130%/追保后 150%/提取 300%）；**禁止**用核对日「今天券商加严线」回放全历史当唯一诚实组；**禁止**把开仓保证金比例（Z）静默当成维持担保比例。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `bc0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **BC0 vs BC2**：永不强平相对诚实维持闸门——假可维持仓 / 可持有名义吹胖、强平失败率低估。  
2. **BC1 vs BC2**：核对日维持线泄露相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_no_force_close",
  "invent_asof_leak_maint_ratio",
  "honest_exchange_floor_then_force_close",
  "below_130_no_call_window",
  "after_call_below_150",
  "withdraw_above_300_sensitivity",
  "broker_stricter_sensitivity",
  "vs_A_fill",
  "vs_Z_margin_ratio",
  "vs_BA_margin_buy_list",
  "vs_BB_refinance_borrow",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_T_csrc_fee",
  "vs_AE_stock_t0",
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可持有两融名义/路径质量差 ΔNotional（BC0/BC1 相对 BC2）；  
2. 假可维持仓贡献差 ΔFakeMaintHold；  
3. 强平/失败率差 ΔFail；  
4. （可选）被动减仓冲击代理差 ΔForceImpact（声明日频敏感性，不冒充 Level-2 精确强平路径）。

**相对判据（草稿）**：若 |ΔNotional| **≥ params.Y** 或 |ΔFakeMaintHold 桶贡献| **≥ params.G** 或 |ΔNotional_(BC1 vs BC2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「维持担保比例强制平仓执行鸿沟显著」。

**params.Y / G / N / Y2（纸面占位建议；待预检写死；与实验字母 BC / 单字母实验 A/B/C/Z 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义差显著门槛（≠实验字母 BC；≠单字母实验 A/B/C/Z） | **建议** `0.02`（待预检写死） |
| params.G | 假可维持仓桶相对对照差 | **建议** `0.01` |
| params.N | 失败/强平率差门槛（≠实验字母 BC） | **建议** `0.05` |
| params.Y2 | BC1 vs BC2 专项门槛 | **建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-16` |
| fill_time | 成交时点 | **写死** `next_open` |
| bc0_primary_demo | 天真主报枚举 | **建议** `invent_no_force_close`（禁与 invent_asof_leak_maint_ratio 双挂；BC1半泄露不得升格并列主报） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 exchange_floor_then_force_close；禁与 A/Z/BA/BB/K/AB/T 混主结论；禁荐股）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实维持/强平闸门」与「永不强平 / 核对日维持线泄露」，或无维持代理且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、融券名单（K）、融券卖出价限（AB）、板上枯竭（A）、证管费（T）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「维持担保强制平仓误关」写成「开仓保证金比例误铺」而不声明另页 Z → 与 Z 撞题，设计失效。  
4. 把「维持担保强制平仓误关」写成「融资买入标的名单误开」而不声明另页 BA → 与 BA 撞题，设计失效。  
5. 把「维持担保强制平仓误关」写成「转融券暂停后假无限券源」而不声明另页 BB → 与 BB 撞题，设计失效。  
6. 把「维持担保强制平仓误关」写成「融券空头名单可空」为主病而不声明另页 K → 与 K 撞题，设计失效。  
7. 把「维持担保强制平仓误关」写成「板上能否按板上价成交」而不声明另页 A → 与 A 撞题，设计失效。  
8. 把「维持担保强制平仓误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
9. 把实验字母 BC 与单字母 A 或单字母 B 或单字母 C 或单字母 Z 或双字母 BA/BB/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
10. holdout 反调 `bc0_primary_demo` / Y·G·N·Y2 → 结论无效。  
11. 用复权价算担保物市值/债务 → 标签与执行双错，结论无效。  
12. 把券商加严线静默写成「等于交易所下限更松」且不另桶 → 设计失效。  
13. 把「开仓保证金够」静默写成「永可维持、永不强平」且不声明本页与 Z 分列 → 与 Z 撞题/设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资/融券持仓或拟开两融腿标记、融资买入金额/融券数量代理、利息及费用代理（可粗）；  
- 开仓保证金比例输入（消费 Z 诚实 PIT，或显式旁路声明本页不重开开仓比例）；  
- 维持担保比例计算所需担保物市值与债务代理（日频收盘即可起步）；  
- 交易日历；可选券商加严维持线分桶。

可选：追保通知日/强平申报标识；提取事件；盘中紧急平仓线敏感性（另桶，不进主报）。

**禁止**：用核对日「今天券商加严线」铺满当唯一诚实组；用复权价；把开仓保证金比例当维持担保比例；把 Z/BA/BB/K/AB/A/T/AN–BB 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BC`  
- **组**：BC0 / BC1 / BC2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`maint_ratio_floor=1.30`；`maint_ratio_after_call=1.50`；`maint_ratio_withdraw=3.00`；`maint_call_max_days=2`；`maint_honest=exchange_floor_then_force_close`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`broker_stricter_bucket=separate_sensitivity`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_margin_maint_force_check`；`missing_maint_policy=skip`；`day_freq_proxy=maint_force_close_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 纸面占位建议 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 BC；**params.N≠实验字母 BC**；亦≠单字母实验 A/B/C/Z；待预检写死；禁 null/holdout）；**`params.bc0_primary_demo` 建议 `invent_no_force_close`**（禁与 invent_asof_leak_maint_ratio 双挂；BC1半泄露不得升格并列主报；待预检写死）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BC0/BC1/BC2 可持有名义/路径质量、ΔFakeMaintHold、ΔFail；分桶（永不强平 / 核对日维持线泄露 / 低于 130% 未追保 / vs A·Z·BA·BB·K·AB·T）。  
- 自检布尔：BC2 是否 exchange_floor_then_force_close；BC0 是否单一主报；BC1 是否仅核对日泄露；是否未与 A/Z/BA/BB/K/AB/T 混主结论；holdout 是否未反调；**是否未把实验字母 BC 与 A 或 B 或 C 或 Z 或 BA 或 BB 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–BB 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-Z / 假设-BA / 假设-BB / 假设-K / 假设-AB**；**是否未再改 BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把永不强平或核对日维持线泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BB 及其他 A/D–BB 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-Z**；**不改假设-BA**；**不改假设-BB**；**不改假设-K**；**不改假设-AB**；**勿再改 BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）之外，持仓存续须过维持担保/强平闸门；交易所下限 130%/追保后 150%/提取 300%；券商可加严。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BC** 标准件，**不改口径主线**，**不改假设 A–BB 正文**。与实验 A/Z/BA/BB/K/AB/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；K=融券空头名单；AB=融券卖出价限；T=证管费（避开）；BC=维持担保比例强制平仓误关（BC≠A≠B≠C≠Z≠BA≠BB≠K≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频担保物/债务代理 + 维持线表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**maint_honest=exchange_floor_then_force_close 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 纸面占位建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BC；params.N≠实验字母 BC；亦≠单字母实验 A/B/C/Z；待预检写死）**；**bc0_primary_demo 建议 invent_no_force_close（禁双挂；BC1半泄露不得升格并列主报；待预检写死）** |

---

## 变更

- 2026-11-03：新建纸面草稿假设-BC（维持担保比例强制平仓误关）。待预检键建议 Y/G/N/Y2=0.02/0.01/0.05/0.015；bc0_primary_demo=invent_no_force_close（禁双挂 invent_asof_leak_maint_ratio）。与 A/B/C/Z/BA/BB/K/AB/T/AN–BB 硬分列；**双字母 BC ≠ 单字母 B ≠ 单字母 C**；明确避开预检T旧题。未改 Y/Z/AA–BB 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-K；不改假设-AB；勿再改 BB/BA/AZ/AY/AX/AW；结论栏仍空；不开回测；不抢 A。
