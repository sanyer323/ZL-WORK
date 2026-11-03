# 假设 BJ · 融资买入卖出所得优先偿还融资负债误关 / 用核对日还债优先规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BI 补丁已收、写下一纸面 BJ；清单撞题规则另选正交执行缺口（**融资买入证券卖出所得须优先偿还融资负债** ≠ 融券卖出所得资金用途限制 ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 单标的两融余额25pct暂停 ≠ 两融合约期限到期强制了结 ≠ 可充抵保证金证券名单 ≠ 两融授信额度上限）；选题自交易所融资融券细则公开口径：投资者卖出信用证券账户内融资买入证券所得价款，应当优先偿还该投资者的融资负债；规则按**施行日/生效日** PIT，不得用核对日更宽「卖出所得可自由用」回放全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BJ ≠ 单字母 B**）/ J（无板日临停；**双字母 BJ ≠ 单字母 J**）/ Z（**开仓**融资/融券保证金比例；**BJ≠Z**）/ BA（**融资买入**标的名单；**BJ≠BA**）/ BB（**转融券暂停后券源**；**BJ≠BB**）/ BC（**维持担保比例强制平仓**；**BJ≠BC**）/ BD（**担保品折算率**；**BJ≠BD**）/ BE（**单标的两融余额25pct暂停**；**BJ≠BE**）/ BF（**两融合约期限到期强制了结**；**BJ≠BF**）/ BG（**可充抵保证金证券名单**；**BJ≠BG**）/ BH（**两融授信额度上限**；**BJ≠BH**）/ BI（**融券卖出所得资金用途限制**；**BJ≠BI**）/ K（融券空头名单；**BJ≠K**）/ AB（融券卖出价限 / 当日平；**BJ≠AB**）/ E（整手）/ AN–BI（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停/合约期限/可充抵名单/授信额度/融券所得用途等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BJ**  
状态：**草稿 · 待风控预检**（结论栏空；禁止把「融资买入证券卖出所得=普通可用现金 / 可不优先偿还融资负债」当诚实执行能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BI 及其他 A/D–BI 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-J；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-BF；不改假设-BG；不改假设-BH；不改假设-BI；不改假设-K；不改假设-AB；勿再改 BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BJ。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融资买入证券卖出所得是否须优先偿还融资负债**。**双字母 BJ ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BJ ≠ 单字母 B**。与假设 **J（无板日临停）** **硬分列**：J = 无板日临停规则；本页 = 融资买入卖出所得**还债优先闸门**；临停 ≠ 还债优先。**双字母 BJ ≠ 单字母 J**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 已开融资买入腿**卖出后价款如何分配**；比例够 ≠ 卖出所得可自由用。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开**融资买入**腿（标的闸门）；本页 = 已融资买入证券**卖出所得**是否优先还债。与假设 **BI（融券卖出所得资金用途限制）** **硬分列**：BI = **融券卖出**所得资金用途（空头侧）；本页 = **融资买入证券卖出**所得优先偿还融资负债（多头侧）；融券所得用途 ≠ 融资卖出还债优先。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 空头**券源可借量**；本页 = 融资卖出所得还债；券源 ≠ 还债优先。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = 持仓存续期**维持担保比例**是否触发追保/强平；本页 = 卖出融资证券所得分配；维持线 ≠ 还债优先。与假设 **BD（担保品折算率）** **硬分列**：BD = 折算率计入保证金可用；本页 = 卖出所得还债；折算率 ≠ 还债优先。与假设 **BE（单标的两融余额25pct暂停）** **硬分列**：BE = 市场层单标的余额集中度暂停**新开**；本页 = 账户层融资卖出所得分配。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = 已开合约的**存续期限上限与到期了结**；本页 = 卖出所得还债；期限 ≠ 还债优先。与假设 **BG（可充抵保证金证券名单）** **硬分列**：BG = **哪些证券可以充抵**；本页 = 融资买入证券卖出所得分配。与假设 **BH（两融授信额度上限）** **硬分列**：BH = 客户**授信/可用额度**上限；本页 = 额度内已产生融资买入后的卖出所得分配；额度够 ≠ 卖出所得可自由用。与假设 **K / AB** **硬分列**：不重开融券名单与空头价限/当日平。与假设 AN–BI **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停/合约期限/可充抵名单/授信额度/融券所得用途等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BJ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 J**（无板日临停）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BJ / 假设-BJ / hypothesis_id=BJ / 组 BJ0·BJ1·BJ2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BJ 混读或互改。亦**禁止**把实验字母 BJ 与单字母 **A**、单字母 **B**、单字母 **J**、单字母 **Z**、单字母 **K**、双字母 **BA**、双字母 **BB**、双字母 **BC**、双字母 **BD**、双字母 **BE**、双字母 **BF**、双字母 **BG**、双字母 **BH**、双字母 **BI**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `bj0_*` 以外的实验页混读。**双字母 BJ ≠ 单字母 A ≠ 单字母 B ≠ 单字母 J ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BE ≠ 双字母 BF ≠ 双字母 BG ≠ 双字母 BH ≠ 双字母 BI**；**params.Y ≠ 实验字母 BJ**；**params.G ≠ 实验字母 BJ**；**params.N ≠ 实验字母 BJ**。

---

## 1. 一句话假设（可检验、可证伪）

同一拟卖出融资买入证券路径、同一未复权价、同一 T+1、同一开仓保证金比例与可充抵/折算/授信/融券所得用途输入（Z/BD/BG/BH/BI 层诚实或显式旁路声明「本页不重开开仓比例/折算率/可充抵名单/授信额度/融券所得用途」）下，把「融资买入证券卖出所得=普通可用现金、可不优先偿还融资负债」或「全样本用核对日当天还债优先规则（含券商当日更宽自由用途）回放历史」当成默认，相对「每个交易日按当时有效融资买入卖出所得优先偿还融资负债 PIT（卖出价款优先还该投资者融资负债；未还清前不得当普通现金任意动用；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假可自由动用融资卖出所得路径并高估可执行买入/转出名义、低估因还债优先导致的动用失败率**；差异应**集中在融资买入卖出所得优先偿还融资负债误关桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假自由融资卖出所得贡献差、可执行名义差、失败率差在标定噪声带内可忽略，且「假自由融资卖出所得 / 核对日泄露 / 未还债先动用窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·K·AB·J·B·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融资买入卖出所得还债优先 ≠ 融券所得用途；≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 维持担保强平；≠ 担保品折算率；≠ 单标的余额25pct暂停；≠ 合约期限；≠ 可充抵名单；≠ 授信额度；≠ 融券名单；≠ 空头价限/当日平；≠ 无板日临停；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；阶段0纸面建议；待风控预检后冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BJ；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 J；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BJ
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BJ
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 还债优先腿
# params.financing_sale_repay_honest     写死 pit_by_effective_date  # 还债优先按生效日 PIT
# params.financing_sale_repay_scope      写死 priority_repay_financing_liability  # 卖出融资买入证券价款优先还融资负债
# params.financing_sale_free_use_policy  写死 reject_or_fail  # 未还清前当普通现金动用 → 拒开/记失败；禁静默自由用
# params.broker_wider_free_sale_bucket   写死 separate_sensitivity  # 券商更宽自由用途另桶；不得默认=核对日更宽
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BJ≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BJ≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BJ≠BB
# params.maint_force_handoff             写死 bc_page        # 维持担保强平交 BC；BJ≠BC
# params.haircut_handoff                 写死 bd_page        # 担保品折算率交 BD；BJ≠BD
# params.balance_pause_handoff           写死 be_page        # 单标的余额25pct暂停交 BE；BJ≠BE
# params.contract_term_handoff           写死 bf_page        # 合约期限交 BF；BJ≠BF
# params.collateral_list_handoff         写死 bg_page        # 可充抵名单交 BG；BJ≠BG
# params.credit_quota_handoff            写死 bh_page        # 授信额度交 BH；BJ≠BH
# params.short_proceeds_use_handoff      写死 bi_page        # 融券所得用途交 BI；BJ≠BI
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K
# params.short_px_handoff                写死 ab_page        # 融券卖出价限/当日平交 AB
# params.halt_no_limit_handoff           写死 j_page         # 无板日临停交 J；BJ≠J
# params.exit_period_handoff             写死 h_page         # 退市整理交 H；BJ≠H
# params.bj0_primary_demo                建议 invent_financing_sale_proceeds_free_use  # 主报：融资买入卖出所得=普通现金可自由用/不优先还债；禁与 invent_asof_leak_financing_sale_repay 双挂争主表；BJ1半泄露不得升格并列主报
# params.bj0_invent_financing_sale_free  写死 True
# params.bj1_asof_leak_financing_sale_repay_only 写死 True   # 半泄露：仅用核对日还债优先规则铺满历史
# params.bj2_pit_financing_sale_repay    写死 True
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
# params.merge_with_BI_short_proceeds    写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_J_halt               写死 False
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
# params.merge_with_G_nolimit_pct        写死 False
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
# params.merge_with_BI_short_proceeds    写死 False
# params.universe_rule                   写死 sse_szse_financing_sale_repay_check
# params.missing_financing_sale_repay_policy 写死 skip
# params.day_freq_proxy                  写死 financing_sale_repay_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BJ；params.G≠实验字母BJ；params.N≠实验字母BJ；亦≠单字母实验A/B/J/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
financing_sale_repay_honest = "pit_by_effective_date"
params.bj0_primary_demo = "invent_financing_sale_proceeds_free_use"  # 单一主报建议；禁与 invent_asof_leak_financing_sale_repay 双挂
```

### 2.2 三组对照（BJ0 / BJ1 / BJ2）

| 组 | 口径 | 说明 |
|----|------|------|
| BJ0 天真 | `invent_financing_sale_proceeds_free_use`（单一主报建议） | 融资买入证券卖出所得=普通可用现金；可不优先偿还融资负债 |
| BJ1 半泄露 | `invent_asof_leak_financing_sale_repay` | 仅用核对日还债优先规则（含券商当日更宽自由用途）铺满全历史；**不得升格并列主报** |
| BJ2 诚实 PIT | `pit_by_effective_date` | 按当日已生效还债优先；未还清前自由动用拒开/记失败；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/BA/BG/BD/BH/BI）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **规则生效**：细则/合同施行日或生效日；禁用核对日更宽「卖出所得自由用」提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BJ0 相对 BJ2 的假自由融资卖出所得贡献差、动用/开仓失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「融资买入卖出所得优先偿还融资负债误关」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeFreeFinancingSaleProceeds / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/K/AB/J/B/H/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BJ0 / BJ1 / BJ2。报告名义/路径质量差、假自由融资卖出所得贡献差、动用失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_financing_sale_proceeds_free_use",
  "invent_asof_leak_financing_sale_repay",
  "unrepaid_financing_then_free_use",
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
  "vs_BI_short_proceeds_use",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_J_halt_no_limit",
  "vs_H_exit_period",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺还债优先字段却静默当「融资卖出所得=普通现金可任意用」→ 设计失效。  
2. 把「融券卖出所得用途放开/限制」静默写成「融资买入卖出还债优先」且不声明另页 BI → 与 BI 撞题（融券所得用途 ≠ 融资卖出还债优先）。  
3. 把「在融资买入名单内」静默写成「卖出所得可自由用」且不声明另页 BA → 与 BA 撞题。  
4. 把「授信额度未用尽」静默写成「融资卖出所得可自由用」且不声明另页 BH → 与 BH 撞题。  
5. 把「开仓保证金比例够」静默写成「卖出所得可任意用」且不声明另页 Z → 与 Z 撞题。  
6. 把「维持担保比例够 / 可提取」静默写成「融资卖出所得可任意用」且不声明另页 BC → 与 BC 撞题。  
7. 把「可充抵名单内 / 折算率有值」静默写成「融资卖出所得可任意用」且不声明另页 BG/BD → 与 BG/BD 撞题。  
8. 把「转融券未暂停 / 券源够」静默写成「融资卖出所得可自由用」且不声明另页 BB → 与 BB 撞题。  
9. 把「单标的余额未达 25% 暂停」静默写成「融资卖出所得可任意用」且不声明另页 BE → 与 BE 撞题。  
10. 把「合约未到期」静默写成「还债优先放开」且不声明另页 BF → 与 BF 撞题。  
11. 把「融券空头名单可空 / 空头价限 / 当日平」写成主病而不声明另页 K/AB → 与 K/AB 撞题。  
12. 把「无板日临停」写成主病而不声明另页 J → 与 J 撞题（**双字母 BJ ≠ 单字母 J**）。  
13. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
14. 把「退市整理期当普通可交易」写成主病而不声明另页 H → 与 H 撞题。  
15. 把「融资买入卖出所得优先偿还融资负债误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
16. 把实验字母 BJ 与单字母 A/B/J/Z 或双字母 BA/BB/BC/BD/BE/BF/BG/BH/BI/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
17. holdout 反调 `bj0_primary_demo` / Y·G·N·Y2 → 结论无效。  
18. 用复权价算卖出名义/可动用名义 → 标签与执行双错，结论无效。  
19. 用核对日更宽自由用途当诚实 PIT、或把券商临时放宽还债优先提前铺满历史 → 设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资买入持仓腿 / 卖出成交名义；  
- 对应融资负债余额代理；  
- 拟用卖出所得买入/转出路径；  
- 当时有效**融资买入卖出所得优先偿还融资负债**规则及生效日（细则/合同）；  
- 开仓保证金比例 / 可充抵名单 / 折算率 / 授信额度 / 融券所得用途输入（消费 Z/BG/BD/BH/BI 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商加严还债比例；卖出所得分户记账标记；部分偿还流水。

**禁止**：用核对日「今天可自由用融资卖出所得」铺满当唯一诚实组；用复权价；把开仓保证金比例/维持担保/折算率数值/融资名单/转融券通道暂停/余额25pct暂停/合约期限/可充抵名单/授信额度/融券所得用途当成融资卖出还债优先放开；把 Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/K/AB/A/J/B/H/T/AN–BI 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BJ`  
- **组**：BJ0 / BJ1 / BJ2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`financing_sale_repay_honest=pit_by_effective_date`；`financing_sale_repay_scope=priority_repay_financing_liability`；`financing_sale_free_use_policy=reject_or_fail`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`halt_no_limit_handoff=j_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_financing_sale_repay_check`；`missing_financing_sale_repay_policy=skip`；`day_freq_proxy=financing_sale_repay_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BJ**；**params.G≠实验字母 BJ**；**params.N≠实验字母 BJ**；亦≠单字母实验 A/B/J/Z；禁 null/holdout/跑后改口；待预检后冻结）；**`params.bj0_primary_demo` 建议 `invent_financing_sale_proceeds_free_use`**（禁与 invent_asof_leak_financing_sale_repay 双挂；BJ1半泄露不得升格并列主报；待预检后冻结）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BJ0/BJ1/BJ2 可执行名义/路径质量、ΔFakeFreeFinancingSaleProceeds、ΔFail；分桶（融资卖出还债优先误关 / 核对日泄露 / 未还债先动用窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·K·AB·J·H·T）。  
- 自检布尔：BJ2 是否 pit_by_effective_date；BJ0 是否单一主报；BJ1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/K/AB/J/B/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BJ 与 A 或 B 或 J 或 Z 或 BA–BI 或 params.Y 或 params.G 或 params.N 混用**；**是否未改 Y/Z/AA–BI 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-J / 假设-Z / 假设-BA–BI / 假设-K / 假设-AB**；**是否未再改 BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把还债优先误关或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BI 及其他 A/D–BI 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-J**；**不改假设-Z**；**不改假设-BA–BI**；**不改假设-K**；**不改假设-AB**；**勿再改 BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）之外，**融资买入证券卖出所得优先偿还融资负债**须按当时有效规则 PIT；不得默认卖出所得=普通现金任意用。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BJ** 标准件，**不改口径主线**，**不改假设 A–BI 正文**。与实验 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/K/AB/J/B/H/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓；BD=担保品折算率；BE=单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；BG=可充抵保证金证券名单；BH=两融授信额度上限；BI=融券卖出所得资金用途限制；K=融券空头名单；AB=融券卖出价限；J=无板日临停；B=历史实验B旧位；H=退市整理；T=证管费（避开）；BJ=融资买入卖出所得优先偿还融资负债误关（BJ≠A≠B≠J≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠K≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待风控预检 |
| 数据 | 待接入（字段见 §6；日频融资买入卖出名义+融资负债代理+还债优先规则生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**financing_sale_repay_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BJ；params.G≠实验字母 BJ；params.N≠实验字母 BJ；亦≠单字母实验 A/B/J/Z；禁 null/holdout/跑后改口；待预检冻结）**；**bj0_primary_demo 建议 invent_financing_sale_proceeds_free_use（禁双挂 invent_asof_leak_financing_sale_repay；BJ1半泄露不得升格并列主报；待预检冻结）**；锚点保留 financing_sale_repay_honest=pit_by_effective_date / financing_sale_repay_scope=priority_repay_financing_liability / financing_sale_free_use_policy=reject_or_fail / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单（供总管/风控）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：建议 `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BJ**；**`params.G` ≠ 实验字母 BJ**；**`params.N` ≠ 实验字母 BJ**；亦≠单字母实验 A/B/J/Z；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bj0_primary_demo`**：建议 **`invent_financing_sale_proceeds_free_use`**；禁与 **`invent_asof_leak_financing_sale_repay`** 双挂争主表；**BJ1 半泄露不得升格并列主报**。  
3. **PIT/政策锚**：`financing_sale_repay_honest=pit_by_effective_date`；`financing_sale_repay_scope=priority_repay_financing_liability`；`financing_sale_free_use_policy=reject_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`；`missing_financing_sale_repay_policy=skip`。

**与 BA–BI/Z/K/AB/B/J/A/H 硬分列（保留）**：本页 = **融资买入卖出所得优先偿还融资负债**；BI = **融券卖出所得资金用途**；Z = **开仓**保证金比例；BA = **融资买入**标的名单；BB = **转融券暂停后券源**；BC = **维持担保比例强制平仓**；BD = **担保品折算率**；BE = **单标的两融余额25pct暂停**；BF = **两融合约期限到期强制了结**；BG = **可充抵保证金证券名单**；BH = **两融授信额度上限**；A = **板上枯竭**；K = **融券空头名单**；AB = **融券卖出价限**；J = **无板日临停**；B = 历史实验 B 旧位；H = **退市整理期**；融资卖出还债优先 ≠ 融券所得用途 ≠ 开仓比例 ≠ 融资可买名单 ≠ 转融券源 ≠ 维持强平 ≠ 折算率 ≠ 余额25pct暂停 ≠ 合约期限 ≠ 可充抵名单 ≠ 授信额度 ≠ 板上枯竭 ≠ 融券名单 ≠ 空头价限 ≠ 无板日临停 ≠ 退市整理；**双字母 BJ ≠ 单字母 A ≠ 单字母 B ≠ 单字母 J ≠ 单字母 Z ≠ 双字母 BA–BI ≠ 双字母 AB ≠ 单字母 K**；**params.Y ≠ 实验字母 BJ**；**params.G ≠ 实验字母 BJ**；**params.N ≠ 实验字母 BJ**；禁止捆成「两融一张表=融资卖出所得随便花」；**尤其不改假设-H**；不改假设-J；不改假设-B；不改假设-Z；不改假设-BA–BI；不改假设-A；不改假设-K；不改假设-AB。

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BI 补丁已收 → 写假设-BJ；自立 BJ，勿占 BI/BH/BG/BF/BE/BD/BC/BB/BA/B/J/A/Z；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BJ**）。选题：融资买入卖出所得优先偿还融资负债误关（正交于 BI 融券卖出所得用途 / BA 融资买入名单 / BH 授信额度 / Z 开仓比例 / BC 维持强平；**双字母 BJ ≠ 单字母 B ≠ 单字母 J**）。
