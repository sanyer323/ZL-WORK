# 假设 BL · 担保品提取转出限制误关 / 用核对日提取线规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BK 补丁已收、写下一纸面 BL；清单撞题规则另选正交执行缺口（**担保品提取/转出限制** ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 可充抵保证金证券名单 ≠ 客户单票集中度 ≠ 两融授信额度 ≠ 融券所得用途 ≠ 融资卖出还债优先 ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 单标的两融余额25pct暂停 ≠ 两融合约期限 ≠ 融券空头名单）；选题自交易所融资融券细则公开口径：维持担保比例**超过 300%** 时可提取，提取后不得低于 300%；会员可加严；规则按**施行日/生效日** PIT，不得用核对日更宽「可任意提取/转出担保品」回放全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BL ≠ 单字母 B**）/ **L（市价通道；双字母 BL ≠ 单字母假设-L）** / Z（**开仓**融资/融券保证金比例；**BL≠Z**）/ BA–BK（两融族已冻；**BL≠BA…BK**）/ **K（融券空头名单 PIT；BL≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BL≠AB**）/ BC（**维持担保比例强制平仓**；**BL≠BC**；低维持强平 ≠ 高维持提取闸门）/ BD（**担保品折算率**；**BL≠BD**）/ BG（**可充抵保证金证券名单**；**BL≠BG**）/ E（整手）/ AN–BK（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BL**  
状态：**草稿 · 待预检**（结论栏空；禁止把「担保品可任意提取/转出、永不检查提取线」当诚实执行能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BK 及其他 A/D–BK 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-L；不改假设-K；不改假设-Z；不改假设-BA–BK；不改假设-AB；勿再改 BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BL（约 #69）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **担保品提取/转出是否过提取线闸门**。**双字母 BL ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BL ≠ 单字母 B**。与假设 **L（市价通道）** **硬分列**：L = 市价申报通道/保护限价等；本页 = 信用账户**担保品提取/转出**闸门；市价通道 ≠ 提取线。**双字母 BL ≠ 单字母假设-L**。与假设 **K（融券空头名单 PIT）** **硬分列**：K = 当日是否在**交易所融券标的名单**内；本页 = 维持担保比例是否允许**提取/转出**担保品；名单内可空 ≠ 可任意提担保品。**BL≠K**；并**带过**：双字母 **BK ≠ 单字母假设-K / 预检K**（BK=客户单票集中度；K=融券名单；本页不覆盖、不混读二者）。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 持仓存续期**提取担保品**闸门；比例够 ≠ 可任意提。与假设 **BC（维持担保比例强制平仓）** **硬分列（专节强调）**：BC = **低维持线**追保/强制平仓（主演示 invent_no_force_close；130%/150%）；本页 = **高维持线**提取/转出限制（超过 300% 可提取，提取后不得低于 300%）；强平误关 ≠ 提取误关。与假设 **BD（担保品折算率）** **硬分列**：BD = 折算率计入保证金可用；本页 = 折算后权益够之后能否**提出**；折算率 ≠ 提取闸门。与假设 **BG（可充抵保证金证券名单）** **硬分列**：BG = **哪些证券可以充抵**；本页 = 已充抵证券能否**提取/转出**。与假设 **BK（客户单票两融集中度）** **硬分列**：BK = 单票敞口占比上限；本页 = 提取线；集中度 ≠ 提取。与假设 **BA/BB/BE/BF/BH/BI/BJ** **硬分列**：融资名单 / 转融券源 / 市场25pct / 合约期限 / 总授信 / 融券所得用途 / 融资卖出还债优先 ≠ 担保品提取闸门。与假设 **AB** **硬分列**：不重开空头价限/当日平。与假设 AN–BK **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BL** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 L**（市价通道）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BL / 假设-BL / hypothesis_id=BL / 组 BL0·BL1·BL2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BL 混读或互改。亦**禁止**把实验字母 BL 与单字母 **A**、单字母 **B**、单字母 **L**、单字母 **K**、单字母 **Z**、双字母 **BA–BK**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bl0_*` 以外的实验页混读。**双字母 BL ≠ 单字母 A ≠ 单字母 B ≠ 单字母 L ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BK ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BG ≠ 双字母 AB**；**params.Y ≠ 实验字母 BL**；**params.G ≠ 实验字母 BL**；**params.N ≠ 实验字母 BL**。**带过：双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BL ≠ 单字母假设-L；且 ≠ 假设-BC；带过 BK≠K（硬）

| 维度 | 对照页 | 本页假设-BL（双字母） |
|------|--------|----------------------|
| 题面 L | 市价通道 / 保护限价等 | **担保品提取/转出限制**误关：假可任意提 vs 按生效日提取线 PIT |
| 题面 BC | 维持担保**低线**追保/强制平仓（invent_no_force_close） | 维持担保**高线**提取闸门（超过 300% 可提；提取后≥300%） |
| 题面 K / BK | K=融券空头**名单**；BK=客户**单票集中度**（**BK≠K**） | 提取闸门；本页**不覆盖** K/BK；**BL≠K≠BK** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_unlimited_collateral_withdrawal` |
| 文档 | `假设-L-市价通道.md` / `假设-BC-…` / `假设-K-…` / `假设-BK-…`（**只读；禁止改写**） | `假设-BL-担保品提取转出限制误关.md`（新建） |
| 预检键 | 实验字母 L / BC / K / BK | 实验字母 **BL** / `bl0_primary_demo`；**不得**占用或改写预检 L/BC/K/BK |

**禁止**：把 BL 写成「L/BC/K/BK 的续篇」；把「维持比例未触发强平」静默写成「可任意提取」；把「在可充抵名单内 / 折算率有值」静默写成「可任意提取」；覆盖或补丁改写假设-L / 假设-BC / 假设-K / 假设-BK 正文。

---

## 1. 一句话假设（可检验、可证伪）

同一拟提取/转出担保品路径、同一未复权价、同一 T+1、同一开仓保证金比例与可充抵/折算/维持强平输入（Z/BG/BD/BC 层诚实或显式旁路声明「本页不重开开仓比例/可充抵名单/折算率/低维持强平」）下，把「担保品可任意提取/转出、永不检查提取线」或「全样本用核对日当天提取线规则（含券商当日更宽可提口径）回放历史」当成默认，相对「每个交易日按当时有效担保品提取线 PIT（超过 300% 可提取，提取后不得低于 300%；会员可加严；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假可任意提取/转出担保品路径并高估可抽回现金/证券名义、低估因提取线导致的提取失败率**；差异应**集中在担保品提取转出限制误关桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假任意提取贡献差、可抽回名义差、失败率差在标定噪声带内可忽略，且「假任意提取 / 核对日泄露 / 未达提取线仍提窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·K·AB·L·B·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 担保品提取闸门 ≠ 低维持强平；≠ 折算率；≠ 可充抵名单；≠ 客户单票集中度；≠ 授信额度；≠ 融券所得用途；≠ 融资卖出还债优先；≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 市场25pct暂停；≠ 合约期限；≠ 融券名单；≠ 市价通道；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；待预检；建议终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BL；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 L；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BL
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BL
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.collateral_withdraw_honest      写死 pit_by_effective_date
# params.collateral_withdraw_line        写死 3.00
# params.collateral_withdraw_scope       写死 cash_or_sec_out_of_credit_account
# params.collateral_over_withdraw_policy 写死 reject_or_fail
# params.broker_tighter_withdraw_bucket  写死 separate_sensitivity
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page
# params.haircut_handoff                 写死 bd_page
# params.balance_pause_handoff           写死 be_page
# params.contract_term_handoff           写死 bf_page
# params.collateral_list_handoff         写死 bg_page
# params.credit_quota_handoff            写死 bh_page
# params.short_proceeds_use_handoff      写死 bi_page
# params.financing_sale_repay_handoff    写死 bj_page
# params.client_conc_handoff             写死 bk_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.mkt_order_handoff               写死 l_page
# params.exit_period_handoff             写死 h_page
# params.bl0_primary_demo                建议 invent_unlimited_collateral_withdrawal
# params.bl0_invent_unlimited_withdraw   写死 True
# params.bl1_asof_leak_collateral_withdraw_only 写死 True
# params.bl2_pit_collateral_withdraw     写死 True
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
# params.merge_with_BJ_financing_sale_repay 写死 False
# params.merge_with_BK_client_conc       写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
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
# params.merge_with_BJ_financing_sale    写死 False
# params.merge_with_BK_client_conc       写死 False
# params.universe_rule                   写死 sse_szse_collateral_withdraw_check
# params.missing_collateral_withdraw_policy 写死 skip
# params.day_freq_proxy                  写死 collateral_withdraw_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议写死 0.02/0.01/0.05/0.015
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
collateral_withdraw_honest = "pit_by_effective_date"
params.bl0_primary_demo = "invent_unlimited_collateral_withdrawal"
```

### 2.2 三组对照（BL0 / BL1 / BL2）

| 组 | 口径 | 说明 |
|----|------|------|
| BL0 天真 | `invent_unlimited_collateral_withdrawal`（单一主报·建议） | 担保品可任意提取/转出；永不检查提取线 |
| BL1 半泄露 | `invent_asof_leak_collateral_withdrawal` | 仅用核对日提取线规则（含券商当日更宽可提口径）铺满全历史；**不得升格并列主报** |
| BL2 诚实 PIT | `pit_by_effective_date` | 按当日已生效提取线；未达线仍提拒开/记失败；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/BG/BD/BC）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **规则生效**：细则/合同/券商风控表施行日或生效日；禁用核对日更宽「可任意提取」提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BL0 相对 BL2 的假任意提取贡献差、提取失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「担保品提取转出限制误关」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeUnlimitedCollateralWithdraw / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/K/AB/L/B/H/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BL0 / BL1 / BL2。报告名义/路径质量差、假任意提取贡献差、提取失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_unlimited_collateral_withdrawal",
  "invent_asof_leak_collateral_withdrawal",
  "below_withdraw_line_still_out",
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
  "vs_BJ_financing_sale_repay",
  "vs_BK_client_conc",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_L_mkt_order",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺提取线字段却静默当「担保品可任意提取/转出」→ 设计失效。  
2. 把「维持担保比例未触发强平 / 高于 130%」静默写成「可任意提取」且不声明另页 BC → **与 BC 撞题**（低维持强平 ≠ 高维持提取；**尤其 BL≠BC**）。  
3. 把「可充抵名单内」静默写成「可任意提取」且不声明另页 BG → 与 BG 撞题。  
4. 把「折算率有值 / 折算后可用够」静默写成「可任意提取」且不声明另页 BD → 与 BD 撞题。  
5. 把「开仓保证金比例够」静默写成「提取放开」且不声明另页 Z → 与 Z 撞题。  
6. 把「总授信未用尽 / 集中度未触顶」静默写成「可任意提取」且不声明另页 BH/BK → 与 BH/BK 撞题。  
7. 把「融券所得用途放开 / 融资卖出还债优先放开」写成主病而不声明另页 BI/BJ → 与 BI/BJ 撞题。  
8. 把「在融资买入名单内 / 转融券未暂停 / 市场未达25pct / 合约未到期」静默写成「可任意提取」且不声明另页 BA/BB/BE/BF → 与 BA/BB/BE/BF 撞题。  
9. 把「在融券空头名单内」静默写成「可任意提取」且不声明另页 K → 与 K 撞题；亦不得混读 BK（**带过 BK≠K**）。  
10. 把「市价通道可报」写成主病而不声明另页 L → 与 L 撞题（**双字母 BL ≠ 单字母 L**）。  
11. 把「空头价限 / 当日平」写成主病而不声明另页 AB → 与 AB 撞题。  
12. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
13. 把「退市整理期当普通可交易」写成主病而不声明另页 H → 与 H 撞题。  
14. 把「担保品提取转出限制误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
15. 把实验字母 BL 与单字母 A/B/L/K/Z 或双字母 BA–BK/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
16. holdout 反调 `bl0_primary_demo` / Y·G·N·Y2 → 结论无效。  
17. 用复权价算担保品市值/可抽回名义 → 标签与执行双错，结论无效。  
18. 用核对日更宽可提口径当诚实 PIT、或把券商临时放宽提取线提前铺满历史 → 设计失效。  
19. **改写或覆盖 `假设-L` / `假设-BC` / `假设-K` / `假设-BK` / 已冻 AA–BK** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户拟提取/转出现金或担保证券名义；  
- 提取前/后维持担保比例代理（分子：现金+折算后担保品；分母：融资负债+融券负债市值等）；  
- 当时有效**担保品提取线**规则及生效日（细则/合同/券商风控表；默认 300%）；  
- 开仓保证金比例 / 可充抵名单 / 折算率 / 低维持强平输入（消费 Z/BG/BD/BC 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商加严提取线；部分提取流水；转普通账户标记。

**禁止**：用核对日「今天可任意提取」铺满当唯一诚实组；用复权价；把开仓保证金比例/低维持强平/折算率数值/可充抵名单/融资名单/转融券通道暂停/市场余额25pct暂停/合约期限/总授信/融券所得用途/融资卖出还债优先/客户单票集中度当成提取放开；把 Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/K/AB/A/L/B/H/T/AN–BK 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BL`  
- **组**：BL0 / BL1 / BL2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`collateral_withdraw_honest=pit_by_effective_date`；`collateral_withdraw_line=3.00`；`collateral_withdraw_scope=cash_or_sec_out_of_credit_account`；`collateral_over_withdraw_policy=reject_or_fail`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`mkt_order_handoff=l_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_collateral_withdraw_check`；`missing_collateral_withdraw_policy=skip`；`day_freq_proxy=collateral_withdraw_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议写死 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BL**；**params.G≠实验字母 BL**；**params.N≠实验字母 BL**；亦≠单字母实验 A/B/L/Z；禁 null/holdout/跑后改口）；**`params.bl0_primary_demo` 建议 `invent_unlimited_collateral_withdrawal`**（禁与 invent_asof_leak_collateral_withdrawal 双挂；BL1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BL0/BL1/BL2 可执行名义/路径质量、ΔFakeUnlimitedCollateralWithdraw、ΔFail；分桶（担保品提取误关 / 核对日泄露 / 未达提取线仍提窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·K·AB·L·B·H·T）。  
- 自检布尔：BL2 是否 pit_by_effective_date；BL0 是否单一主报；BL1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/K/AB/L/B/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BL 与 A 或 B 或 L 或 K 或 Z 或 BA–BK 或 params.Y 或 params.G 或 params.N 混用**；**是否未改 Y/Z/AA–BK 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-L / 假设-K / 假设-Z / 假设-BA–BK / 假设-AB**；**是否未再改 BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否带过并尊重 BK≠K**。  
- **禁止输出**：具体买卖标的列表当「建议」；把提取误关或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BK 及其他 A/D–BK 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-L**；**不改假设-K**；**不改假设-Z**；**不改假设-BA–BK**；**不改假设-AB**；**勿再改 BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、融券空头名单（K）之外，**担保品提取/转出限制**须按当时有效提取线 PIT；不得默认可任意提取。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BL** 标准件，**不改口径主线**，**不改假设 A–BK 正文**，**尤其不改假设-L / 假设-BC / 假设-K / 假设-BK**。与实验 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/K/AB/L/B/H/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓（低线）；BD=担保品折算率；BE=市场层单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；BG=可充抵保证金证券名单；BH=两融授信额度上限；BI=融券卖出所得资金用途限制；BJ=融资买入卖出所得优先偿还融资负债；BK=客户单票两融集中度上限；K=融券空头名单；AB=融券卖出价限；L=市价通道；B=历史实验B旧位；H=退市整理；T=证管费（避开）；BL=担保品提取转出限制误关（BL≠A≠B≠L≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠AB≠T；带过 BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待预检 |
| 数据 | 待接入（字段见 §6；日频维持担保比例代理+拟提取名义+提取线生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**collateral_withdraw_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BL；params.G≠实验字母 BL；params.N≠实验字母 BL；亦≠单字母实验 A/B/L/Z；禁 null/holdout/跑后改口）**；**bl0_primary_demo 建议 invent_unlimited_collateral_withdrawal（禁双挂 invent_asof_leak_collateral_withdrawal；BL1半泄露不得升格并列主报）**；锚点保留 collateral_withdraw_honest=pit_by_effective_date / collateral_withdraw_line=3.00 / collateral_withdraw_scope=cash_or_sec_out_of_credit_account / collateral_over_withdraw_policy=reject_or_fail / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**params.Y≠BL**；**params.G≠BL**；**params.N≠BL**；禁 null/holdout）  
2. `params.bl0_primary_demo` = `invent_unlimited_collateral_withdrawal`（禁与 `invent_asof_leak_collateral_withdrawal` 双挂；BL1不升格主报）  
3. 提取锚：`collateral_withdraw_honest=pit_by_effective_date`；`collateral_withdraw_line=3.00`；`collateral_withdraw_scope=cash_or_sec_out_of_credit_account`；`collateral_over_withdraw_policy=reject_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/L/A/Z/BA–BK/K/AB/H；**尤其 BL≠BC（提取≠强平）**；**尤其 BL≠L**；**带过 BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BK 补丁已收 → 写假设-BL；自立 BL，勿占 BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/L/A/Z/K；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BL**；**双字母 BL ≠ 单字母 L**；**BL≠BC**；**带过 BK≠K**）。选题：担保品提取/转出限制误关（正交于 BC 低维持强平 / BD 折算率 / BG 可充抵名单 / BK 客户单票集中度）。
