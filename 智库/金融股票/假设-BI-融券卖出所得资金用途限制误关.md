# 假设 BI · 融券卖出所得资金用途限制误关 / 用核对日所得用途规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BH 补丁已收、写下一纸面 BI；清单撞题规则另选正交执行缺口（**融券卖出所得资金用途限制** ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 单标的两融余额25pct暂停 ≠ 两融合约期限到期强制了结 ≠ 可充抵保证金证券名单 ≠ 两融授信额度上限）；选题自交易所融资融券细则公开口径：融券卖出所得资金用途受限（通常仅可用于买担保品/还融资/细则与合同允许用途；不得当作普通现金任意买非担保品/任意股）；规则按**施行日/生效日** PIT，不得用核对日更宽用途回放全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BI ≠ 单字母 B**）/ I（价格笼子远限价；**双字母 BI ≠ 单字母 I**）/ Z（**开仓**融资/融券保证金比例；**BI≠Z**）/ BA（**融资买入**标的名单；**BI≠BA**）/ BB（**转融券暂停后券源**；**BI≠BB**）/ BC（**维持担保比例强制平仓**；**BI≠BC**）/ BD（**担保品折算率**；**BI≠BD**）/ BE（**单标的两融余额25pct暂停**；**BI≠BE**）/ BF（**两融合约期限到期强制了结**；**BI≠BF**）/ BG（**可充抵保证金证券名单**；**BI≠BG**）/ BH（**两融授信额度上限**；**BI≠BH**）/ K（融券空头名单；**BI≠K**）/ AB（融券卖出价限 / 当日平；**BI≠AB**）/ E（整手）/ AN–BH（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停/合约期限/可充抵名单/授信额度等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BI**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「融券卖出所得=普通可用现金 / 可任意买非担保品或任意股」当诚实执行能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BH 及其他 A/D–BH 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-I；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-BF；不改假设-BG；不改假设-BH；不改假设-K；不改假设-AB；勿再改 BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BI。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融券卖出所得资金能否按当时有效用途限制动用**。**双字母 BI ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BI ≠ 单字母 B**。与假设 **I（价格笼子远限价）** **硬分列**：I = 连续竞价远限价笼子有效性；本页 = 融券所得**资金用途闸门**；笼子 ≠ 所得用途。**双字母 BI ≠ 单字母 I**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 已产生的融券卖出所得**怎么用**；比例够 ≠ 所得可自由使用。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开**融资买入**腿（标的闸门）；本页 = 融券所得能不能去买某证券（用途闸门）；可融资买入 ≠ 可用融券所得买。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 空头**券源可借量**；本页 = 卖出所得**用途**；券源 ≠ 所得用途。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = 持仓存续期**维持担保比例**是否触发追保/强平；本页 = 所得资金用途；维持线 ≠ 所得用途。与假设 **BD（担保品折算率）** **硬分列**：BD = 已在可充抵范围内的证券按什么**折算率**计入保证金可用；本页 = 融券所得是否可用来买某证券；折算率 ≠ 所得用途。与假设 **BE（单标的两融余额25pct暂停）** **硬分列**：BE = 市场层单标的余额/余量集中度暂停**新开**；本页 = 账户层融券所得用途。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = 已开合约的**存续期限上限与到期了结**；本页 = 所得用途；期限 ≠ 用途。与假设 **BG（可充抵保证金证券名单）** **硬分列**：BG = **哪些证券可以充抵**（名单闸门）；本页 = 融券所得可否用于买入某证券；可充抵 ≠ 所得可任意用。与假设 **BH（两融授信额度上限）** **硬分列**：BH = 客户**授信/可用额度**上限；本页 = 额度内已产生的融券所得**用途限制**；额度够 ≠ 所得可自由用。与假设 **K / AB** **硬分列**：不重开融券名单与空头价限/当日平（AB 当日平仓约束 ≠ 所得资金用途）。与假设 AN–BH **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停/合约期限/可充抵名单/授信额度等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BI** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 I**（价格笼子远限价）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BI / 假设-BI / hypothesis_id=BI / 组 BI0·BI1·BI2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BI 混读或互改。亦**禁止**把实验字母 BI 与单字母 **A**、单字母 **B**、单字母 **I**、单字母 **Z**、单字母 **K**、双字母 **BA**、双字母 **BB**、双字母 **BC**、双字母 **BD**、双字母 **BE**、双字母 **BF**、双字母 **BG**、双字母 **BH**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `bi0_*` 以外的实验页混读。**双字母 BI ≠ 单字母 A ≠ 单字母 B ≠ 单字母 I ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BE ≠ 双字母 BF ≠ 双字母 BG ≠ 双字母 BH**；**params.Y ≠ 实验字母 BI**；**params.G ≠ 实验字母 BI**；**params.N ≠ 实验字母 BI**。

---

## 1. 一句话假设（可检验、可证伪）

同一拟用融券卖出所得资金路径、同一未复权价、同一 T+1、同一开仓保证金比例与可充抵/折算/授信输入（Z/BD/BG/BH 层诚实或显式旁路声明「本页不重开开仓比例/折算率/可充抵名单/授信额度」）下，把「融券卖出所得=普通可用现金、可任意买入非担保品或任意股」或「全样本用核对日当天所得用途规则（含券商当日更宽用途）回放历史」当成默认，相对「每个交易日按当时有效融券卖出所得资金用途限制 PIT（仅允许买担保品/还融资/细则与合同列明用途；买非担保品或用途外申报拒开或记失败；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假可自由动用融券所得路径并高估可执行买入名义、低估因用途限制导致的开仓/动用失败率**；差异应**集中在融券卖出所得资金用途限制误关桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假自由用途贡献差、可执行名义差、失败率差在标定噪声带内可忽略，且「假自由用途 / 核对日泄露 / 用途外买入窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·K·AB·I·B·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融券卖出所得资金用途限制 ≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 维持担保强平；≠ 担保品折算率；≠ 单标的余额25pct暂停；≠ 合约期限；≠ 可充抵名单；≠ 授信额度；≠ 融券名单；≠ 空头价限/当日平；≠ 价格笼子；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BI；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 I；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BI
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BI
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 所得用途腿
# params.short_proceeds_use_honest       写死 pit_by_effective_date  # 所得用途按生效日 PIT
# params.short_proceeds_allowed_uses     写死 collateral_buy_or_repay_financing  # 允许：买担保品/还融资/细则合同列明；禁任意股
# params.short_proceeds_over_policy      写死 reject_or_fail  # 用途外动用 → 拒开/记失败；禁静默当成普通现金
# params.broker_wider_use_bucket         写死 separate_sensitivity  # 券商更宽用途另桶；不得默认=核对日更宽
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BI≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BI≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BI≠BB
# params.maint_force_handoff             写死 bc_page        # 维持担保强平交 BC；BI≠BC
# params.haircut_handoff                 写死 bd_page        # 担保品折算率交 BD；BI≠BD
# params.balance_pause_handoff           写死 be_page        # 单标的余额25pct暂停交 BE；BI≠BE
# params.contract_term_handoff           写死 bf_page        # 合约期限交 BF；BI≠BF
# params.collateral_list_handoff         写死 bg_page        # 可充抵名单交 BG；BI≠BG
# params.credit_quota_handoff            写死 bh_page        # 授信额度交 BH；BI≠BH
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K
# params.short_px_handoff                写死 ab_page        # 融券卖出价限/当日平交 AB
# params.cage_handoff                    写死 i_page         # 价格笼子交 I；BI≠I
# params.exit_period_handoff             写死 h_page         # 退市整理交 H；BI≠H
# params.bi0_primary_demo                写死冻结 invent_short_proceeds_free_use  # 主报：融券所得=普通现金可任意用；禁与 invent_asof_leak_short_proceeds_use 双挂争主表；BI1半泄露不得升格并列主报
# params.bi0_invent_short_proceeds_free  写死 True
# params.bi1_asof_leak_short_proceeds_use_only 写死 True     # 半泄露：仅用核对日所得用途规则铺满历史
# params.bi2_pit_short_proceeds_use      写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_BF_contract_term     写死 False
# params.merge_with_BG_collateral_list   写死 False
# params.merge_with_BH_credit_quota      写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_I_cage               写死 False
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
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance           写死 False
# params.merge_with_BF_term              写死 False
# params.merge_with_BG_collateral        写死 False
# params.merge_with_BH_credit            写死 False
# params.universe_rule                   写死 sse_szse_short_proceeds_use_check
# params.missing_short_proceeds_use_policy 写死 skip
# params.day_freq_proxy                  写死 short_proceeds_use_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BI；params.G≠实验字母BI；params.N≠实验字母BI；亦≠单字母实验A/B/I/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
short_proceeds_use_honest = "pit_by_effective_date"
params.bi0_primary_demo = "invent_short_proceeds_free_use"  # 写死冻结；禁与 invent_asof_leak_short_proceeds_use 双挂
```

### 2.2 三组对照（BI0 / BI1 / BI2）

| 组 | 口径 | 说明 |
|----|------|------|
| BI0 天真 | `invent_short_proceeds_free_use`（单一主报·已冻结） | 融券卖出所得=普通可用现金；可任意买非担保品/任意股 |
| BI1 半泄露 | `invent_asof_leak_short_proceeds_use` | 仅用核对日所得用途规则（含券商当日更宽用途）铺满全历史；**不得升格并列主报** |
| BI2 诚实 PIT | `pit_by_effective_date` | 按当日已生效用途限制；用途外拒开/记失败；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/BA/BG/BD/BH）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **用途生效**：细则/合同施行日或生效日；禁用核对日更宽用途提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BI0 相对 BI2 的假自由用途贡献差、动用/开仓失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「融券卖出所得资金用途限制误关」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeFreeProceedsUse / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/K/AB/I/B/H/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BI0 / BI1 / BI2。报告名义/路径质量差、假自由用途贡献差、动用失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_short_proceeds_free_use",
  "invent_asof_leak_short_proceeds_use",
  "non_collateral_buy_with_short_proceeds",
  "pre_margin_channel_20100331",
  "vs_A_limit_up_fill",
  "vs_Z_margin_ratio",
  "vs_BA_margin_buy_list",
  "vs_BB_refinance_borrow",
  "vs_BC_maint_force",
  "vs_BD_haircut",
  "vs_BE_balance_pause",
  "vs_BF_contract_term",
  "vs_BG_collateral_list",
  "vs_BH_credit_quota",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_I_cage",
  "vs_H_exit_period",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺所得用途字段却静默当「普通现金可任意用」→ 设计失效。  
2. 把「在融资买入名单内」静默写成「可用融券所得买」且不声明另页 BA → 与 BA 撞题（可融资买入 ≠ 可用融券所得买）。  
3. 把「在可充抵名单内 / 折算率有值」静默写成「融券所得可任意买该股」且不声明另页 BG/BD → 与 BG/BD 撞题。  
4. 把「授信额度未用尽」静默写成「所得可自由用」且不声明另页 BH → 与 BH 撞题（额度够 ≠ 用途放开）。  
5. 把「开仓保证金比例够」静默写成「所得可任意用」且不声明另页 Z → 与 Z 撞题。  
6. 把「维持担保比例够 / 可提取」静默写成「融券所得可任意买」且不声明另页 BC → 与 BC 撞题。  
7. 把「转融券未暂停 / 券源够」静默写成「所得可自由用」且不声明另页 BB → 与 BB 撞题。  
8. 把「单标的余额未达 25% 暂停」静默写成「所得可任意买」且不声明另页 BE → 与 BE 撞题。  
9. 把「合约未到期」静默写成「所得用途放开」且不声明另页 BF → 与 BF 撞题。  
10. 把「融券空头名单可空 / 空头价限 / 当日平」写成主病而不声明另页 K/AB → 与 K/AB 撞题（价限/当日平 ≠ 所得用途）。  
11. 把「价格笼子远限价」写成主病而不声明另页 I → 与 I 撞题（**双字母 BI ≠ 单字母 I**）。  
12. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
13. 把「退市整理期当普通可交易」写成主病而不声明另页 H → 与 H 撞题。  
14. 把「融券卖出所得资金用途限制误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
15. 把实验字母 BI 与单字母 A/B/I/Z 或双字母 BA/BB/BC/BD/BE/BF/BG/BH/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
16. holdout 反调 `bi0_primary_demo` / Y·G·N·Y2 → 结论无效。  
17. 用复权价算所得名义/可买名义 → 标签与执行双错，结论无效。  
18. 用核对日更宽用途当诚实 PIT、或把券商临时放宽用途提前铺满历史 → 设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融券卖出成交名义 / 所得资金余额代理；  
- 拟用所得资金买入的证券代码与是否担保品代理；  
- 当时有效**融券卖出所得资金用途限制**规则及生效日（细则/合同）；  
- 开仓保证金比例 / 可充抵名单 / 折算率 / 授信额度输入（消费 Z/BG/BD/BH 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商加严用途子集；还融资流水；所得资金分户记账标记。

**禁止**：用核对日「今天用途规则」铺满当唯一诚实组；用复权价；把开仓保证金比例/维持担保/折算率数值/融资名单/转融券通道暂停/余额25pct暂停/合约期限/可充抵名单/授信额度当成所得用途放开；把 Z/BA/BB/BC/BD/BE/BF/BG/BH/K/AB/A/I/B/H/T/AN–BH 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BI`  
- **组**：BI0 / BI1 / BI2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`short_proceeds_use_honest=pit_by_effective_date`；`short_proceeds_allowed_uses=collateral_buy_or_repay_financing`；`short_proceeds_over_policy=reject_or_fail`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`cage_handoff=i_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_short_proceeds_use_check`；`missing_short_proceeds_use_policy=skip`；`day_freq_proxy=short_proceeds_use_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BI**；**params.G≠实验字母 BI**；**params.N≠实验字母 BI**；亦≠单字母实验 A/B/I/Z；禁 null/holdout/跑后改口）；**`params.bi0_primary_demo` 写死冻结 `invent_short_proceeds_free_use`**（禁与 invent_asof_leak_short_proceeds_use 双挂；BI1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BI0/BI1/BI2 可执行名义/路径质量、ΔFakeFreeProceedsUse、ΔFail；分桶（所得用途误关 / 核对日泄露 / 用途外买入窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·K·AB·I·H·T）。  
- 自检布尔：BI2 是否 pit_by_effective_date；BI0 是否单一主报；BI1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/K/AB/I/B/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BI 与 A 或 B 或 I 或 Z 或 BA 或 BB 或 BC 或 BD 或 BE 或 BF 或 BG 或 BH 或 params.Y 或 params.G 或 params.N 混用**；**是否未改 Y/Z/AA–BH 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-I / 假设-Z / 假设-BA / 假设-BB / 假设-BC / 假设-BD / 假设-BE / 假设-BF / 假设-BG / 假设-BH / 假设-K / 假设-AB**；**是否未再改 BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把所得用途误关或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BH 及其他 A/D–BH 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-I**；**不改假设-Z**；**不改假设-BA**；**不改假设-BB**；**不改假设-BC**；**不改假设-BD**；**不改假设-BE**；**不改假设-BF**；**不改假设-BG**；**不改假设-BH**；**不改假设-K**；**不改假设-AB**；**勿再改 BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）之外，**融券卖出所得资金用途限制**须按当时有效规则 PIT；不得默认所得=普通现金任意用。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BI** 标准件，**不改口径主线**，**不改假设 A–BH 正文**。与实验 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/K/AB/I/B/H/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓；BD=担保品折算率；BE=单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；BG=可充抵保证金证券名单；BH=两融授信额度上限；K=融券空头名单；AB=融券卖出价限；I=价格笼子；B=历史实验B旧位；H=退市整理；T=证管费（避开）；BI=融券卖出所得资金用途限制误关（BI≠A≠B≠I≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠K≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频融券所得余额+拟用所得买入腿+用途规则生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**short_proceeds_use_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BI；params.G≠实验字母 BI；params.N≠实验字母 BI；亦≠单字母实验 A/B/I/Z；禁 null/holdout/跑后改口）**；**bi0_primary_demo 写死冻结 invent_short_proceeds_free_use（禁双挂 invent_asof_leak_short_proceeds_use；BI1半泄露不得升格并列主报）**；锚点保留 short_proceeds_use_honest=pit_by_effective_date / short_proceeds_allowed_uses=collateral_buy_or_repay_financing / short_proceeds_over_policy=reject_or_fail / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BI**；**`params.G` ≠ 实验字母 BI**；**`params.N` ≠ 实验字母 BI**；**`params.Y` ≠ 单字母实验 A/B/I/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bi0_primary_demo`**：**写死冻结** **`invent_short_proceeds_free_use`**；禁与 **`invent_asof_leak_short_proceeds_use`** 双挂争主表（只挂一个 primary）；**BI1 半泄露不得升格并列主报**。

**所得用途锚保留（已通写死）**：`params.short_proceeds_use_honest=pit_by_effective_date`；`params.short_proceeds_allowed_uses=collateral_buy_or_repay_financing`；`params.short_proceeds_over_policy=reject_or_fail`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有 `missing_short_proceeds_use_policy=skip` 等锚点；不改口）。

**与 BA/BB/BC/BD/BE/BF/BG/BH/Z/K/AB/B/I/A/H 硬分列（保留）**：本页 = **融券卖出所得资金用途限制**；Z = **开仓**保证金比例；BA = **融资买入**标的名单；BB = **转融券暂停后券源**；BC = **维持担保比例强制平仓**；BD = **担保品折算率**；BE = **单标的两融余额25pct暂停**；BF = **两融合约期限到期强制了结**；BG = **可充抵保证金证券名单**；BH = **两融授信额度上限**；A = **板上枯竭**；K = **融券空头名单**；AB = **融券卖出价限**；I = **价格笼子**；B = 历史实验 B 旧位；H = **退市整理期**；所得用途 ≠ 开仓比例 ≠ 融资可买名单 ≠ 转融券源 ≠ 维持强平 ≠ 折算率 ≠ 余额25pct暂停 ≠ 合约期限 ≠ 可充抵名单 ≠ 授信额度 ≠ 板上枯竭 ≠ 融券名单 ≠ 空头价限 ≠ 价格笼子 ≠ 退市整理；**双字母 BI ≠ 单字母 A ≠ 单字母 B ≠ 单字母 I ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BE ≠ 双字母 BF ≠ 双字母 BG ≠ 双字母 BH ≠ 双字母 AB ≠ 单字母 K**；**params.Y ≠ 实验字母 BI**；**params.G ≠ 实验字母 BI**；**params.N ≠ 实验字母 BI**；禁止捆成「两融一张表=融券所得随便花」；**尤其不改假设-H**；不改假设-I；不改假设-B；不改假设-Z；不改假设-BA–BH；不改假设-A；不改假设-K；不改假设-AB。

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BI**；**params.G≠实验字母 BI**；**params.N≠实验字母 BI**；亦≠单字母实验 A/B/I/Z；禁 null/holdout/跑后改口）；② `params.bi0_primary_demo=invent_short_proceeds_free_use`（禁与 `invent_asof_leak_short_proceeds_use` 双挂争主表；BI1半泄露不得升格并列主报）。所得用途锚保留：`short_proceeds_use_honest=pit_by_effective_date`；`short_proceeds_allowed_uses=collateral_buy_or_repay_financing`；`short_proceeds_over_policy=reject_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。与 BA/BB/BC/BD/BE/BF/BG/BH/Z/K/AB/B/I/A/H 硬分列保留。参考总管派令 / 风控预检有条件通过。未改 Y/Z/AA–BH 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-I；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-BF；不改假设-BG；不改假设-BH；不改假设-K；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BH 补丁已收 → 写假设-BI；自立 BI，勿占 BH/BG/BF/BE/BD/BC/BB/BA/B/I/A/Z；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BI**）。选题：融券卖出所得资金用途限制误关（正交于 BA 融资买入名单 / BG 可充抵名单 / BD 折算率 / Z 开仓比例 / BC 维持强平 / BB 转融券源 / BE 余额25pct暂停 / BF 合约期限 / BH 授信额度；**双字母 BI ≠ 单字母 B ≠ 单字母 I**）。
