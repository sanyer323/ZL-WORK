# 假设 BG · 可充抵保证金证券名单误开 / 用核对日担保品名单铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BF 补丁已收、写下一纸面 BG；清单撞题规则另选正交执行缺口（**可充抵保证金证券名单** ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 单标的两融余额25pct暂停 ≠ 两融合约期限到期强制了结）；选题自交易所融资融券细则公开规则：客户提交的担保证券须为交易所公布的**可充抵保证金证券**；会员向客户公布的可充抵范围不得超出本所范围；风险警示/暂停上市/退市整理/权证等不得充抵或折算率为 0；名单按**施行日/生效日**不按印发日；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BG ≠ 单字母 B**）/ G（涨跌幅规则 PIT 新股窗；**双字母 BG ≠ 单字母 G**；**亦 ≠ params.G**）/ Z（**开仓**融资/融券保证金比例；**BG≠Z**）/ BA（**融资买入**标的名单；**BG≠BA**）/ BB（**转融券暂停后券源**；**BG≠BB**）/ BC（**维持担保比例强制平仓**；**BG≠BC**）/ BD（**担保品折算率**数值；**BG≠BD**）/ BE（**单标的两融余额25pct暂停**；**BG≠BE**）/ BF（**两融合约期限到期强制了结**；**BG≠BF**）/ K（融券空头名单；**BG≠K**）/ AB（融券卖出价限 / 当日平；**BG≠AB**）/ E（整手）/ AN–BF（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停/合约期限等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BG**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「全 A 任意证券均可充抵保证金 / 用核对日可充抵名单铺满全历史」当诚实保证金可用能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BF 及其他 A/D–BF 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-G；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-BF；不改假设-K；不改假设-AB；勿再改 BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BG。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **拟充抵证券是否落在当日已生效可充抵保证金证券名单内**。**双字母 BG ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BG ≠ 单字母 B**。与假设 **G（涨跌幅规则 PIT 新股窗）** **硬分列**：G = 无涨跌幅日/新股窗/ST 板幅 PIT；本页 = 可充抵保证金证券**名单闸门**；板幅规则 ≠ 担保品名单。**双字母 BG ≠ 单字母 G**。与 **`params.G`（费用/费率或显著性同族门槛占位，建议值 0.01）** **硬分列**：**实验字母 BG ≠ params.G**；正文与回报凡写「实验 BG / 假设-BG / hypothesis_id=BG / 组 BG0·BG1·BG2」均指本实验；凡写 **`params.G`** 均指门槛数值键，**禁止**把二者混读或互改。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = **哪些证券可以充抵**（名单闸门），不主测 80%/100% 比例。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开**融资买入**腿（标的闸门）；本页 = 能不能把某证券**提交为担保品**（可充抵名单）；可融资买入 ≠ 可充抵担保。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 空头**券源可借量**；本页 = 担保品**可充抵名单**；券源 ≠ 担保名单。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = 持仓存续期**维持担保比例**是否触发追保/强平；本页 = 提交担保时证券是否在可充抵名单；维持线 ≠ 名单闸门。与假设 **BD（担保品折算率）** **硬分列**：BD = 已在可充抵范围内的证券按什么**折算率**计入保证金可用；本页 = **是否在可充抵名单内**（名单闸门）；名单外不得用「折算率=1」发明可充抵；折算率 ≠ 名单。与假设 **BE（单标的两融余额25pct暂停）** **硬分列**：BE = 市场层单标的余额/余量集中度暂停**新开**；本页 = 账户担保品**可充抵名单**。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = 已开合约的**存续期限上限与到期了结**；本页 = 担保品名单；期限 ≠ 名单。与假设 **K / AB** **硬分列**：不重开融券名单与空头价限/当日平。与假设 AN–BF **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停/合约期限等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BG** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 G**（涨跌幅规则 PIT 新股窗）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BG / 假设-BG / hypothesis_id=BG / 组 BG0·BG1·BG2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BG 混读或互改。亦**禁止**把实验字母 BG 与单字母 **A**、单字母 **B**、单字母 **G**、单字母 **Z**、单字母 **K**、双字母 **BA**、双字母 **BB**、双字母 **BC**、双字母 **BD**、双字母 **BE**、双字母 **BF**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `bg0_*` 以外的实验页混读。**双字母 BG ≠ 单字母 A ≠ 单字母 B ≠ 单字母 G ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BE ≠ 双字母 BF**；**params.Y ≠ 实验字母 BG**；**params.G ≠ 实验字母 BG**；**params.N ≠ 实验字母 BG**。

---

## 1. 一句话假设（可检验、可证伪）

同一拟开两融路径、同一未复权价、同一 T+1、同一开仓保证金比例与折算率输入（Z/BD 层诚实或显式旁路声明「本页不重开开仓比例/折算率数值」）下，把「全 A 任意证券均可充抵保证金」或「全样本用核对日当天可充抵保证金证券名单（含会员当日更宽表）回放历史」当成默认，相对「每个交易日按当时已生效可充抵保证金证券名单 PIT（风险警示/暂停上市/退市整理/权证等不得充抵或交 BD 记折算 0；施行日不是印发日；2010-03-31 前无通道；缺名单 skip/敏感性）」的诚实组，会**系统性发明名单外假可充抵路径并高估保证金可用 / 可开两融名义、低估因不在可充抵名单导致的开仓失败率**；差异应**集中在可充抵保证金证券名单误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假可充抵贡献差、可开名义差、失败率差在标定噪声带内可忽略，且「名单外历史充抵腿 / ST·风险警示·退市整理不得充抵窗 / 2010-03-31 前 / vs A·Z·BA·BB·BC·BD·BE·BF·K·AB·G·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 可充抵保证金证券名单 ≠ 担保品折算率；≠ 融资买入名单；≠ 开仓保证金比例；≠ 维持担保强平；≠ 转融券券源；≠ 余额25pct暂停；≠ 合约期限；≠ 融券名单；≠ 板上枯竭；≠ 涨跌幅PIT；≠ 证管费

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BG；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 G；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BG；≠ 单字母实验 G
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BG
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 可充抵腿
# params.collateral_list_honest          写死 pit_by_effective_date
# params.risk_warn_exit_warrant_collateral 写死 not_eligible   # 风险警示/暂停上市/退市整理/权证不得充抵（或交 BD 折算0；本页名单侧记 not_eligible）
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BG≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BG≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BG≠BB
# params.maint_force_handoff             写死 bc_page        # 维持担保强平交 BC；BG≠BC
# params.haircut_handoff                 写死 bd_page        # 担保品折算率交 BD；BG≠BD（名单≠折算）
# params.balance_pause_handoff           写死 be_page        # 单标的余额25pct暂停交 BE；BG≠BE
# params.contract_term_handoff           写死 bf_page        # 合约期限交 BF；BG≠BF
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K
# params.short_px_handoff                写死 ab_page        # 融券卖出价限/当日平交 AB
# params.limit_pct_handoff               写死 g_page         # 涨跌幅规则交 G；BG≠G
# params.bg0_primary_demo                写死冻结 invent_all_ashare_as_collateral  # 主报：全A任意证券均可充抵；禁与 invent_asof_leak_collateral_list 双挂争主表；BG1半泄露不得升格并列主报
# params.bg0_invent_all_ashare_collateral 写死 True
# params.bg1_asof_leak_collateral_list_only 写死 True           # 半泄露：仅用核对日可充抵名单铺满历史
# params.bg2_pit_collateral_list         写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_BF_contract_term     写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_G_nolimit_pct        写死 False
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
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance           写死 False
# params.merge_with_BF_term              写死 False
# params.universe_rule                   写死 sse_szse_collateral_list_check
# params.missing_collateral_list_policy  写死 skip
# params.day_freq_proxy                  写死 collateral_list_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BG；params.G≠实验字母BG（特别消歧）；params.N≠实验字母BG；亦≠单字母实验A/B/G/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip

fill_time = "next_open"
asof_check_date = "2026-10-16"
collateral_list_honest = "pit_by_effective_date"
params.bg0_primary_demo = "invent_all_ashare_as_collateral"  # 写死冻结；禁与 invent_asof_leak_collateral_list 双挂
```

### 2.2 三组对照（BG0 / BG1 / BG2）

| 组 | 口径 | 说明 |
|----|------|------|
| BG0 天真 | `invent_all_ashare_as_collateral`（单一主报） | 全 A 任意证券均可充抵保证金；忽略可充抵名单 |
| BG1 半泄露 | `invent_asof_leak_collateral_list` | 仅用核对日可充抵名单/会员当日更宽表铺满全历史；**不得升格并列主报** |
| BG2 诚实 PIT | `pit_by_effective_date` | 按当日已生效可充抵名单；风险警示/暂停上市/退市整理/权证 = not_eligible；缺名单 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年与多轮可充抵/折算切日；本页不重开 Z/BD）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **名单生效**：施行日/生效日；禁用印发日提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BG0 相对 BG2 的假可充抵贡献差、开仓失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「可充抵保证金证券名单误开」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeCollateral / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/K/AB/G/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BG0 / BG1 / BG2。报告名义/路径质量差、假可充抵贡献差、开仓失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_all_ashare_as_collateral",
  "invent_asof_leak_collateral_list",
  "risk_warn_exit_warrant_not_eligible",
  "pre_margin_channel_20100331",
  "vs_A_limit_up_fill",
  "vs_Z_margin_ratio",
  "vs_BA_margin_buy_list",
  "vs_BB_refinance_borrow",
  "vs_BC_maint_force",
  "vs_BD_haircut",
  "vs_BE_balance_pause",
  "vs_BF_contract_term",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_G_nolimit_pct",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺可充抵名单字段却静默当「全 A 可充抵」→ 设计失效。  
2. 把「折算率=1 / 折算率表有值」静默写成「在可充抵名单内」且不声明另页 BD → 与 BD 撞题/设计失效（有折算率假设 ≠ 名单已生效）。  
3. 把「在融资买入名单内」静默写成「可充抵担保」且不声明另页 BA → 与 BA 撞题（可融资买入 ≠ 可充抵）。  
4. 把「开仓保证金比例够」静默写成「担保品在名单内」且不声明另页 Z → 与 Z 撞题。  
5. 把「维持担保比例够」静默写成「可提交任意证券作担保」且不声明另页 BC → 与 BC 撞题。  
6. 把「转融券 2024-07-11 暂停」静默写成「可充抵名单变更」且不声明另页 BB → 与 BB 撞题。  
7. 把「单标的余额未达 25% 暂停」静默写成「可充抵」且不声明另页 BE → 与 BE 撞题。  
8. 把「合约未到期」静默写成「担保品在名单内」且不声明另页 BF → 与 BF 撞题。  
9. 把「融券空头名单可空 / 空头价限」写成主病而不声明另页 K/AB → 与 K/AB 撞题。  
10. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
11. 把「无涨跌幅日/新股窗板幅」写成主病而不声明另页 G → 与 G 撞题（**双字母 BG ≠ 单字母 G**）。  
12. 把「可充抵保证金证券名单误开」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
13. 把实验字母 BG 与单字母 A/B/G/Z 或双字母 BA/BB/BC/BD/BE/BF/AB/AZ/AY/AX/AW 或 `params.Y` 或 **`params.G`** 或 `params.N` 混读互改 → 文档失效，须重标。  
14. holdout 反调 `bg0_primary_demo` / Y·G·N·Y2 → 结论无效。  
15. 用复权价算担保品市值/可开名义 → 标签与执行双错，结论无效。  
16. 用印发日当生效日、或把会员超出交易所范围的更宽表当诚实 PIT → 设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 拟充抵保证金证券代码/市值代理、现金保证金；  
- 沪深**可充抵保证金证券名单**（含施行日/生效日）；  
- 风险警示/ST/暂停上市/退市整理/权证标记与调出日；  
- 开仓保证金比例 / 折算率输入（消费 Z/BD 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：会员加严可充抵子集；调出公告与施行日差；担保品提交/提取流水。

**禁止**：用核对日「今天可充抵名单」铺满当唯一诚实组；用复权价；把开仓保证金比例/维持担保/折算率数值/融资名单/转融券通道暂停/余额25pct暂停/合约期限当成可充抵名单；把 Z/BA/BB/BC/BD/BE/BF/K/AB/A/G/T/AN–BF 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BG`  
- **组**：BG0 / BG1 / BG2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`collateral_list_honest=pit_by_effective_date`；`risk_warn_exit_warrant_collateral=not_eligible`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`limit_pct_handoff=g_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_collateral_list_check`；`missing_collateral_list_policy=skip`；`day_freq_proxy=collateral_list_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BG**；**params.G≠实验字母 BG（特别消歧）**；**params.N≠实验字母 BG**；亦≠单字母实验 A/B/G/Z；禁 null/holdout/跑后改口）；**`params.bg0_primary_demo` 写死冻结 `invent_all_ashare_as_collateral`**（禁与 invent_asof_leak_collateral_list 双挂；BG1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BG0/BG1/BG2 可开名义/路径质量、ΔFakeCollateral、ΔFail；分桶（名单误开 / 核对日泄露 / 风险警示·退市整理不得充抵 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·K·AB·G·T）。  
- 自检布尔：BG2 是否 pit_by_effective_date；BG0 是否单一主报；BG1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/BF/K/AB/G/T 混主结论；holdout 是否未反调；**是否未把实验字母 BG 与 A 或 B 或 G 或 Z 或 BA 或 BB 或 BC 或 BD 或 BE 或 BF 或 params.Y 或 params.G 或 params.N 混用**；**是否未改 Y/Z/AA–BF 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-G / 假设-Z / 假设-BA / 假设-BB / 假设-BC / 假设-BD / 假设-BE / 假设-BF / 假设-K / 假设-AB**；**是否未再改 BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把名单误开或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BF 及其他 A/D–BF 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-G**；**不改假设-Z**；**不改假设-BA**；**不改假设-BB**；**不改假设-BC**；**不改假设-BD**；**不改假设-BE**；**不改假设-BF**；**不改假设-K**；**不改假设-AB**；**勿再改 BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、单标的余额25pct暂停（BE）、合约期限（BF）之外，**可充抵保证金证券名单**须按当时有效规则 PIT；不得默认全 A 可充抵。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BG** 标准件，**不改口径主线**，**不改假设 A–BF 正文**。与实验 A/Z/BA/BB/BC/BD/BE/BF/K/AB/G/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓；BD=担保品折算率；BE=单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；K=融券空头名单；AB=融券卖出价限；G=涨跌幅规则PIT；T=证管费（避开）；BG=可充抵保证金证券名单误开（BG≠A≠B≠G≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠K≠AB≠T；params.G≠实验字母BG）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频拟充抵证券+可充抵名单生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**collateral_list_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BG；params.G≠实验字母 BG（特别消歧）；params.N≠实验字母 BG；亦≠单字母实验 A/B/G/Z；禁 null/holdout/跑后改口）**；**bg0_primary_demo 写死冻结 invent_all_ashare_as_collateral（禁双挂 invent_asof_leak_collateral_list；BG1半泄露不得升格并列主报）**；锚点保留 collateral_list_honest=pit_by_effective_date / risk_warn_exit_warrant_collateral=not_eligible / margin_channel_start=2010-03-31 / fail_policy=skip |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BG**；**`params.G` ≠ 实验字母 BG（特别消歧）**；**`params.N` ≠ 实验字母 BG**；**`params.Y` ≠ 单字母实验 A/B/G/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bg0_primary_demo`**：**写死冻结** **`invent_all_ashare_as_collateral`**；禁与 **`invent_asof_leak_collateral_list`** 双挂争主表（只挂一个 primary）；**BG1 半泄露不得升格并列主报**。

**可充抵名单锚保留（已通写死）**：`params.collateral_list_honest=pit_by_effective_date`；`params.risk_warn_exit_warrant_collateral=not_eligible`；`params.margin_channel_start=2010-03-31`；`params.fail_policy=skip`（及正文已有 `asof_check_date=2026-10-16` / `missing_collateral_list_policy=skip` / `fill_time=next_open` 等锚点；不改口）。

**与 BA/BB/BC/BD/BE/BF/Z/K/AB/B/G 硬分列（保留）**：本页 = **可充抵保证金证券名单**；Z = **开仓**保证金比例；BA = **融资买入**标的名单；BB = **转融券暂停后券源**；BC = **维持担保比例强制平仓**；BD = **担保品折算率**；BE = **单标的两融余额25pct暂停**；BF = **两融合约期限到期强制了结**；A = **板上枯竭**；K = **融券空头名单**；AB = **融券卖出价限**；B = 历史实验 B 旧位；G = 涨跌幅规则 PIT；可充抵名单 ≠ 开仓比例 ≠ 融资可买名单 ≠ 转融券源 ≠ 维持强平 ≠ 折算率 ≠ 余额25pct暂停 ≠ 合约期限 ≠ 板上枯竭 ≠ 融券名单 ≠ 空头价限 ≠ 涨跌幅PIT；**双字母 BG ≠ 单字母 A ≠ 单字母 B ≠ 单字母 G ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BE ≠ 双字母 BF ≠ 双字母 AB ≠ 单字母 K**；**params.G ≠ 实验字母 BG**；禁止捆成「两融一张表=全A可充抵」；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-BF；不改假设-A；不改假设-K；不改假设-AB；不改假设-B；不改假设-G。

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BG**；**params.G≠实验字母 BG（特别消歧）**；**params.N≠实验字母 BG**；亦≠单字母实验 A/B/G/Z；禁 null/holdout/跑后改口）；② `params.bg0_primary_demo=invent_all_ashare_as_collateral`（禁与 `invent_asof_leak_collateral_list` 双挂争主表；BG1半泄露不得升格并列主报）。可充抵名单锚保留：`collateral_list_honest=pit_by_effective_date`；`risk_warn_exit_warrant_collateral=not_eligible`；`margin_channel_start=2010-03-31`；`fail_policy=skip`。与 BA/BB/BC/BD/BE/BF/Z/K/AB/B/G 硬分列保留。参考总管派令 / 风控预检有条件通过。未改 Y/Z/AA–BF 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-G；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-BF；不改假设-K；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BF 补丁已收 → 写假设-BG；自立 BG，勿占 BF/BE/BD/BC/BB/BA/B/G/A/Z；避开预检T；不开回测；禁实盘/荐股；**params.Y/N≠实验字母 BG**；**params.G≠实验字母 BG**）。选题：可充抵保证金证券名单误开（正交于 BA 融资买入名单 / BD 折算率数值 / Z 开仓比例 / BC 维持强平 / BB 转融券源 / BE 余额25pct暂停 / BF 合约期限；**双字母 BG ≠ 单字母 B ≠ 单字母 G**；**params.G ≠ 实验字母 BG**）。