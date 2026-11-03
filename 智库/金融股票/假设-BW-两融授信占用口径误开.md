# 假设 BW · 两融授信占用口径误开 / 用核对日更宽低占用公式铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BV 补丁已交（A/D–BV 纸面齐）、写下一纸面 BW；清单撞题规则另选正交执行缺口（**授信已占用/剩余额度口径吹瘦** ≠ 授信额度上限闸门 ≠ 融券提前召回 ≠ 融券券池日可借量 ≠ 强制平仓顺序与范围 ≠ 融资利率档 ≠ 融券借券费 ≠ 融资假零息 ≠ 开仓保证金比例 ≠ 担保品折算率 ≠ 可充抵名单 ≠ 除权日复权价误判板）；选题自两融会员风控公开口径：客户融资买入/融券卖出占用授信额度，了结后释放；**已占用额度怎么算**（是否计入应计利息/罚息、融券市值重估、未到账负债、在途委托占用等）按当时有效占用规则 PIT；不得默认「占用永远按本金或成本低估 / 永不计入应计与市值重估 / 用核对日更宽低占用公式铺满历史」；本页**假定授信额度天花板仍按 BH 诚实或显式旁路检查**，主病只在**占用口径吹瘦→假高剩余额度**；2010-03-31 前无此通道；**BH 正文主测「额度天花板无限/永不检查上限」**（`invent_unlimited_credit_quota`），本页主测**有天花板前提下占用公式被吹瘦**（`invent_understate_credit_usage`）→ 自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BW ≠ 单字母 B**）/ **W（除权日复权价误判板；双字母 BW ≠ 单字母假设-W；严禁复用 W 题面或除权板价口径）** / Z（**开仓**融资/融券保证金比例；**BW≠Z**）/ BA–BV（两融族已冻/已齐；**BW≠BA…BV**；**尤其不改 BV 正文**）/ **BH（授信额度上限；BW≠BH；尤其不改假设-BH）** / K（融券空头名单；**BW≠K**；并带过 BK≠K）/ AB（融券卖出价限；**BW≠AB**）/ BD（担保品折算率；**BW≠BD**）/ BG（可充抵名单；**BW≠BG**）/ BV（融券提前召回；**BW≠BV**；已齐亦**不改 BV**）/ BU/BT/BS/BO/BR/BQ/BP/BN/BM/BL/BE/BC/BB/BA 等**分列**；**新建实验 BW**  
状态：**草稿 · 待预检**（结论栏空；禁止把「授信占用永远按本金低估 / 永不计入应计利息与融券市值重估 / 用核对日更宽低占用公式铺满」当诚实授信占用口径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BV 及其他 A/D–BV 已交正文与冻结补丁；尤其不改假设-BV；尤其不改假设-W；尤其不改假设-BH；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-Z；不改假设-BA–BV；不改假设-AB；勿再改 BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BW（约 #80）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **授信已占用/剩余额度怎么算**。**双字母 BW ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BW ≠ 单字母 B**。与假设 **W（除权日复权价误判板）** **硬分列（专节强调）**：W = 除权日用不复权/复权价误判涨跌停板与板上可成交；本页 = 信用账户**授信占用口径**；除权板价 ≠ 授信占用。**双字母 BW ≠ 单字母假设-W**；**严禁复用 W 题面或 W 口径键**。与假设 **BH（两融授信额度上限）** **硬分列**：BH = **额度天花板闸门**（永不检查上限 / `invent_unlimited_credit_quota`）；本页 = **有天花板前提下已占用怎么算**（占用吹瘦 / `invent_understate_credit_usage`）；无限额度 ≠ 假低占用；**禁止**把「额度无限（BH）」静默写成「占用已诚实」；**禁止**把「假低占用」静默写成「额度无限」；**不占** BH 的 primary_demo；**尤其不改假设-BH**。**BW≠BH**。与假设 **BV（融券提前召回）** **硬分列**：BV = 存量空头提前召回（已齐）；本页 = 授信占用口径；召回 ≠ 占用；**尤其不改假设-BV**。**BW≠BV**。与假设 **BU / BT / BS / BO / BR / BQ / BP / BN / BM / BL / BF / BC / BB / BA / BD / BG / Z / K / AB** **硬分列**：日库存 / 强平序 / 利率档 / 假零息 / 借券费 / 调出后存量 / 权益补偿 / 账户串用 / 追保禁开 / 提取 / 合约期限 / 维持线闸门 / 转融暂停 / 融资名单 / 折算率 / 可充抵 / 开仓比例 / 融券名单 / 空头价限 ≠ 授信占用公式；并**带过 BV≠V/BU/BT/BF/BC/BB/BQ/K…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 AN–BV **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-W（除权板价）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BW** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 W**（除权日复权价误判板；**严禁复用假设-W**）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BW / 假设-BW / hypothesis_id=BW / 组 BW0·BW1·BW2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BW 混读或互改。亦**禁止**把实验字母 BW 与单字母 **A**、单字母 **B**、单字母 **W**、单字母 **K**、单字母 **Z**、单字母 **T**、单字母 **S**、单字母 **U**、单字母 **V**、双字母 **BA–BV**、双字母 **BH**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bw0_*` 以外的实验页混读。**双字母 BW ≠ 单字母 A ≠ 单字母 B ≠ 单字母 W ≠ 单字母 K ≠ 单字母 Z ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 双字母 BA ≠ … ≠ 双字母 BV ≠ 双字母 BH ≠ 双字母 BU ≠ 双字母 BT ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BQ ≠ 双字母 BP ≠ 双字母 BN ≠ 双字母 BM ≠ 双字母 BF ≠ 双字母 BC ≠ 双字母 BB ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BW**；**params.G ≠ 实验字母 BW**；**params.N ≠ 实验字母 BW**。**带过：双字母 BV ≠ V/BU/BT/BF/BC/BB/BQ/K…；双字母 BU ≠ U/BB/BT/K/BS/BO/BR/BH…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 BW ≠ 单字母假设-W；且 ≠ 假设-BV / 假设-BH / 假设-BU / 假设-BT / 假设-BS / 假设-BO / 假设-BR / 假设-BD / 假设-BG / 假设-Z；带过 BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS…、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BW（双字母） |
|------|--------|----------------------|
| 题面 W | 除权日复权价误判板（板价/可成交） | **授信占用口径**误开：假低占用 vs 按生效日占用 PIT；**严禁复用 W 题面** |
| 题面 BH | **授信额度上限**（天花板；`invent_unlimited_credit_quota`） | **有天花板下占用公式吹瘦**；无限额度 ≠ 假低占用；**BW≠BH**；**不改 BH** |
| 题面 BV | **融券提前召回**（已齐） | 召回 ≠ 占用；**BW≠BV**；**不改 BV** |
| 题面 BU / BT / BS / BO / BR | 日库存 / 强平序 / 利率档 / 假零息 / 借券费 | 计息计费库存强平 ≠ 占用公式；**BW≠BU≠BT≠BS≠BO≠BR** |
| 题面 BD / BG / Z | 折算率全1 / 可充抵名单 / 开仓保证金比例 | 保证金可用 ≠ 授信占用；**BW≠BD≠BG≠Z** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_understate_credit_usage` |
| 文档 | `假设-W-…` / `假设-BH-…` / `假设-BV-…`（**只读；禁止改写**） | `假设-BW-两融授信占用口径误开.md`（新建） |
| 预检键 | 实验字母 W / BH / BV | 实验字母 **BW** / `bw0_primary_demo`；**不得**占用或改写预检 W/BH/BV |

**禁止**：把 BW 写成「W/BH/BV 的续篇」；把「额度无限（BH）/ 召回已诚实（BV）/ 日库存够 / 利率档诚实 / 假零息已计 / 折算率够 / 可充抵 ∈ / 保证金比例够」静默写成「占用已诚实」；覆盖或补丁改写假设-W / 假设-BH / 假设-BV 正文；把 `params.Y/G/N` 与实验字母 BW 混读；**禁** `bw0_primary_demo` 与 `invent_asof_leak_credit_usage` **双挂主报**；**禁** BW1 半泄露升格并列主报；**禁**复用假设-W（除权板价）题面或口径键；**禁**复用 BH 的 `invent_unlimited_credit_quota` 当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟开/加仓两融路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资/融券名单/授信额度天花板/折算率/可充抵名单/转融通道/日库存/合约期限/维持担保闸门/追保禁开/账户隔离等输入（Z/BA/K/BH/BD/BG/BB/BU/BF/BC/BM/BN 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/融券名单/授信额度天花板闸门/折算率/可充抵名单/转融暂停/日可借量/合约期限/维持线闸门 on-off/追保禁开/账户隔离主病」）下，把「授信已占用永远只按本金或成本低估、永不计入应计利息/罚息与融券市值重估/在途委托占用」或「全样本用核对日当天更宽低占用公式回放历史」当成默认，相对「每个交易日按当时有效授信占用规则 PIT（占用含当时规则要求计入的应计利息/罚息、融券市值重估、在途占用等；剩余额度=授信天花板−已占用；超剩余拒开或记失败；缺字段 skip/敏感性；2010-03-31 前无通道）」的诚实组，会**系统性发明假低占用/假高剩余授信路径并高估可开两融名义、低估因占用口径不足导致的开仓失败率**；差异应**集中在两融授信占用口径误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假低占用贡献差、可开名义差、开仓失败率差在标定噪声带内可忽略，且「假低占用 / 核对日泄露 / 应计与市值重估窗 / 在途占用窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·BS·BT·BU·BV·K·AB·B·H·W·V·T·S·U」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 授信占用口径 ≠ 授信额度上限（BH）；≠ 融券提前召回（BV）；≠ 日可借量新开（BU）；≠ 强平序（BT）；≠ 利率档（BS）；≠ 假零息（BO）；≠ 借券费（BR）；≠ 折算率（BD）；≠ 可充抵（BG）；≠ 开仓保证金比例（Z）；≠ 除权板价（W）；≠ 板上枯竭（A）；≠ 证管费（T）

```
# 配置写死键（见 §7；待预检；建议终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BW；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 W；≠ 实验字母 V；≠ 实验字母 Z；≠ 实验字母 BV；≠ 实验字母 BH
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BW
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BW；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.credit_usage_honest             写死 pit_by_effective_date
# params.credit_usage_scope              写死 used_quota_incl_accrual_mtm_pending
# params.credit_usage_over_policy        写死 reject_or_fail_missing_usage_rule
# params.credit_usage_naive              写死 invent_understate_credit_usage
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page
# params.haircut_handoff                 写死 bd_page
# params.balance_pause_handoff           写死 be_page
# params.contract_term_handoff           写死 bf_page   # 期限到期交 BF；BW≠BF；不改 BF
# params.collateral_list_handoff         写死 bg_page
# params.credit_quota_handoff            写死 bh_page   # 授信额度天花板交 BH；BW≠BH；本页主病是占用口径不是上限；不改 BH
# params.short_proceeds_use_handoff      写死 bi_page
# params.financing_sale_repay_handoff    写死 bj_page
# params.client_conc_handoff             写死 bk_page
# params.collateral_withdraw_handoff     写死 bl_page
# params.margin_call_open_ban_handoff    写死 bm_page
# params.cross_account_handoff           写死 bn_page
# params.financing_interest_handoff      写死 bo_page
# params.corp_action_comp_handoff        写死 bp_page
# params.list_removal_stock_handoff      写死 bq_page   # 名单调出存量交 BQ；BW≠BQ；不改 BQ
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page
# params.force_close_order_handoff       写死 bt_page   # 强平序交 BT；BW≠BT；不改 BT
# params.daily_short_inventory_handoff   写死 bu_page   # 日库存新开交 BU；BW≠BU；不改 BU
# params.short_recall_handoff            写死 bv_page   # 融券提前召回交 BV；BW≠BV；不改 BV（复检已齐亦勿改）
# params.credit_usage_handoff            写死 self      # 本页主病：授信占用口径；≠ BH 额度天花板
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page    # 融券名单交 K；BW≠K；不改 K
# params.short_px_handoff                写死 ab_page
# params.stamp_tax_handoff               写死 v_page    # 印花税交 V；BW≠V；V页不改；除权板价交 W；BW≠W；严禁复用假设-W
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.bw0_primary_demo                写死建议 invent_understate_credit_usage  # 主报：假低授信占用/假高剩余额度；禁与 invent_asof_leak_credit_usage 双挂争主表；BW1半泄露不得升格并列主报
# params.bw0_invent_understate_credit_usage  写死 True
# params.bw1_asof_leak_credit_usage_only 写死 True
# params.bw2_pit_credit_usage            写死 True
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
# params.merge_with_BL_collateral_withdraw 写死 False
# params.merge_with_BM_margin_call_open_ban 写死 False
# params.merge_with_BN_cross_account     写死 False
# params.merge_with_BO_financing_interest 写死 False
# params.merge_with_BP_corp_action_comp  写死 False
# params.merge_with_BQ_list_removal_stock 写死 False
# params.merge_with_BR_short_borrow_fee  写死 False
# params.merge_with_BS_financing_rate_tier 写死 False
# params.merge_with_BT_force_close_order 写死 False
# params.merge_with_BU_daily_short_inventory 写死 False
# params.merge_with_BV_short_recall         写死 False  # BW≠BV；不改 BV
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_AA_bar_tz            写死 False
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
# params.universe_rule                   写死 sse_szse_short_recall_check
# params.missing_short_recall_policy     写死 skip
# params.day_freq_proxy                  写死 short_recall_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BV；params.G≠实验字母BV；params.N≠实验字母BV；亦≠单字母实验A/B/V/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
```

```
params.bw0_primary_demo = "invent_understate_credit_usage"  # 单一主报建议；禁与 invent_asof_leak_credit_usage 双挂
```

### 2.2 三组对照（BW0 / BW1 / BW2）

| 组 | 口径 | 说明 |
|----|------|------|
| BW0 天真 | `invent_understate_credit_usage`（单一主报建议） | 发明假低授信占用/假高剩余额度/永不检查占用吹瘦；禁与 invent_asof_leak_credit_usage 双挂 |
| BW1 半泄露/混口径 | 全样本用 `asof_check_date` 当天更宽免占用或更长还券时限规则铺满历史 | 仅占用规则 asof 泄露；不升格并列主报 |
| BW2 PIT | `credit_usage_honest=pit_by_effective_date` | 每个交易日按当时已生效授信占用口径规则 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：信用账户存量融券名义 → 对照当日是否存在出借方占用/占用吹瘦通知代理（或会员占用规则生效表）→ 按 BW0/BW1/BW2 规则生成可续持空头名义、被动了结笔、假低授信占用/假高剩余额度贡献差。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有日终/日频授信占用代理 + 占用/占用吹瘦规则生效日表 + 融券名单 PIT（消费 K）+ 合约期限（消费 BF，旁路）+ 日库存新开层（消费 BU，旁路）即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BW0 / BW1 / BW2。报告可续持空头名义差、假低授信占用/假高剩余额度贡献差、被动了结/占用履约失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_understate_credit_usage",
  "invent_asof_leak_credit_usage",
  "short_recall_notice_window",
  "pre_term_expiry_contrast_window",
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
  "vs_BL_collateral_withdraw",
  "vs_BM_margin_call_open_ban",
  "vs_BN_cross_account",
  "vs_BO_financing_interest",
  "vs_BP_corp_action_comp",
  "vs_BQ_list_removal_stock",
  "vs_BR_short_borrow_fee",
  "vs_BS_financing_rate_tier",
  "vs_BT_force_close_order",
  "vs_BU_daily_short_inventory",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_V_stamp_tax_avoid",
  "vs_U_transfer_fee_avoid",
  "vs_T_csrc_fee_avoid",
  "vs_S_handling_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够存量融券腿或占用字段；缺占用字段却静默当占用吹瘦 → 设计失效。  
2. 把「日库存已诚实（BU）」静默写成「占用已诚实」且不声明另页 BU → **与 BU 撞题**（日库存新开 ≠ 存量占用；**尤其 BW≠BU**；**不改 BU**）。  
3. 把「合约期限到期了结（BF）」静默写成「占用已诚实」且不声明另页 BF → **与 BF 撞题**（到期 ≠ 授信占用；**尤其 BW≠BF**；**不改 BF**）。  
4. 把「强制平仓序已诚实（BT）/ 维持线闸门已诚实（BC）」静默写成「占用已诚实」→ **与 BT/BC 撞题**（强平 ≠ 占用；**尤其 BW≠BT≠BC**；**不改 BT/BC**）。  
5. 把「印花税已诚实（V）」写成主病或不声明另页 V → **撞假设-V**，设计失效（**双字母 BW ≠ 单字母 V**；**严禁复用 V**）。  
6. 把「名单调出后存量已处理（BQ）/ 转融未暂停（BB）/ 名单内可空（K）」静默写成「占用正确」→ 与对应页撞题（**尤其 BW≠BQ≠BB≠K**）。  
7. 把「融资假零息（BO）/ 融券借券费（BR）/ 授信够（BH）/ 利率档已诚实（BS）/ 市场25pct未暂停（BE）」静默写成「占用正确」→ 与对应页撞题（**尤其 BW≠BO≠BR≠BH≠BS≠BE**）。  
8. 把「权益已补偿 / 追保未触发 / 提取线未触 / 账户未串用 / 保证金比例够」静默写成「占用正确」且不声明另页 BP/BM/BL/BN/Z → 与对应页撞题；并**带过 BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK 消歧链**。  
9. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易 / 证管费」写成主病而不声明另页 AB/W/A/H/T → 与对应页撞题。  
10. 把实验字母 BW 与单字母 A/B/V/K/Z/T/S/U 或双字母 BA–BV/BB/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `bw0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价算可续持名义 → 标签与执行双错，结论无效。  
13. 用核对日更宽「免占用」当诚实 PIT、或把券商临时更宽免占用提前铺满历史 → 设计失效。  
14. **`bw0_primary_demo` 与 `invent_asof_leak_credit_usage` 双挂主报**；或 BW1 升格并列主报 → 设计失效。  
15. **改写或覆盖 `假设-V` / `假设-BU` / `假设-BF` / `假设-BT` / `假设-K` / 已冻 AA–BV** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 存量融券名义、开仓日、空头腿代理；  
- 当时有效出借方/券商授信占用或占用吹瘦规则及生效日、通知日、还券时限；  
- 融券名单 PIT / 转融通道状态 / 日库存新开层 / 开仓保证金比例 / 融资名单 / 授信 / 合约期限 / 维持线闸门 / 市场25pct / 追保禁开 / 账户隔离 / 折算率输入（消费 K/BB/BU/Z/BA/BH/BF/BC/BE/BM/BN/BD 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商更严占用子集；与 BF 期限到期窗对照但不混主结论；转融通占用另桶敏感性。

**禁止**：用核对日「今天免占用」铺满当唯一诚实组；用复权价；把日库存够/期限未到/未触维持线/名单仍在池/转融未暂停/假零息/借券费/授信够/利率档诚实/开仓保证金比例/新开名单窗/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/追保未触发/账户未串用/权益已补偿/调出后存量已处理/市场25pct未暂停/印花税已诚实当成「占用正确」依据；把 Z/BA–BV/K/AB/A/B/H/W/V/U/T/S/AN–BV 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BV`  
- **组**：BW0 / BW1 / BW2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`credit_usage_honest=pit_by_effective_date`；`credit_usage_scope=used_quota_incl_accrual_mtm_pending`；`credit_usage_over_policy=reject_or_fail_missing_usage_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`force_close_order_handoff=bt_page`；`daily_short_inventory_handoff=bu_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`stamp_tax_handoff=v_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_short_recall_check`；`missing_short_recall_policy=skip`；`day_freq_proxy=short_recall_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BW**；**params.G≠实验字母 BW**；**params.N≠实验字母 BW**；亦≠单字母实验 A/B/V/Z；禁 null/holdout/跑后改口）；**`params.bw0_primary_demo` 写死建议 `invent_understate_credit_usage`**（禁与 invent_asof_leak_credit_usage 双挂；BW1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BW0/BW1/BW2 净收益/路径质量、ΔFakeNeverRecall、ΔKeepableShortNotional、ΔForcedUnwindOrRecallFailRate；分桶（两融授信占用口径误开 / 核对日泄露 / 占用通知窗 / 期限未到期对照窗 / 通道前 / vs A·Z·BA–BV·K·AB·B·H·W·V·U·T·S）。  
- 自检布尔：BW2 是否 pit_by_effective_date；BW0 是否单一主报；BW1 是否仅核对日泄露；是否未与 A/Z/BA–BV/K/AB/B/H/W/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 BW 与 A 或 B 或 V 或 K 或 Z 或 BA–BV 或 BB 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BW≠单字母假设-V；BW≠BU；BW≠BF；BW≠BT；BW≠BC；BW≠BB；BW≠BQ；BW≠K；BW≠BR；BW≠BO；BW≠BS；BW≠BH；带过 BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BV 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-V / 假设-K / 假设-W / 假设-Z / 假设-BA–BV / 假设-BU / 假设-BF / 假设-BT / 假设-AB**；**是否未再改 BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-V（印花税）**；**是否未与 invent_asof_leak_credit_usage 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把占用吹瘦或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BV 及其他 A/D–BV 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-V**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BV**；**尤其不改假设-BV；不改假设-BU**；**尤其不改假设-BF**；**尤其不改假设-BT**；**不改假设-AB**；**勿再改 BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券券池日可借量（BU）、融券空头名单（K）之外，**出借方授信占用/融券占用吹瘦**须按当时有效规则 PIT；不得默认存量融券永不被占用。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BW** 标准件，**不改口径主线**，**不改假设 A–BU 正文**，**尤其不改假设-V / 假设-BU / 假设-BF / 假设-BT / 假设-K**。与实验 A/Z/BA–BV/K/AB/B/H/W/V/U/T/S 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA–BV=两融族已冻/在途；BU=日库存新开；BF=期限到期了结；BT=强平序；K=融券空头新开名单；AB=融券卖出价限；B=历史实验B旧位；H=退市整理；W=除权板价；V=印花税（严禁复用）；U=过户费；T=证管费（避开）；S=经手费；BV=两融授信占用口径误开（BW≠A≠B≠V≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠BM≠BN≠BO≠BP≠BQ≠BR≠BS≠BT≠BU≠AB≠W≠H≠T≠S≠U；带过 BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K）**。

---

## 9. ״̬

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待预检 |
| 数据 | 待接入（字段见 §6；日频授信占用代理+占用规则生效日+名单PIT+期限旁路+日库存旁路即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**credit_usage_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BW；params.G≠实验字母 BW；params.N≠实验字母 BW；亦≠单字母实验 A/B/V/Z；禁 null/holdout/跑后改口）**；**bw0_primary_demo 写死建议 invent_understate_credit_usage（禁双挂 invent_asof_leak_credit_usage；BW1半泄露不得升格并列主报）**；锚点保留 credit_usage_honest=pit_by_effective_date / credit_usage_scope=used_quota_incl_accrual_mtm_pending / credit_usage_over_policy=reject_or_fail_missing_usage_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单（草稿 · 待预检）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**待预检写死**；**params.Y≠BW**；**params.G≠BW**；**params.N≠BW**；禁 null/holdout）  
2. `params.bw0_primary_demo` = `invent_understate_credit_usage`（**待预检写死**；禁与 `invent_asof_leak_credit_usage` 双挂；BW1不升格主报）  
3. 占用锚：`credit_usage_honest=pit_by_effective_date`；`credit_usage_scope=used_quota_incl_accrual_mtm_pending`；`credit_usage_over_policy=reject_or_fail_missing_usage_rule`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/V/A/Z/BA–BV/K/AB/H/W/T/S/U；**尤其 BW≠V（印花税；严禁复用假设-W）**；**尤其 BW≠BU（日库存新开≠存量占用；不改BU）**；**尤其 BW≠BF（到期≠授信占用；不改BF）**；**尤其 BW≠BT/BC（强平≠占用；不改BT/BC）**；**尤其 BW≠BB/BQ/K/BR/BO/BS/BH**；**带过 BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 与 BA–BV / V / K 撞题检查表

| 字母 | 主题 | 撞题？ | 消歧 |
|------|------|--------|------|
| V | 印花税 PIT 误切 | 否 | **双字母 BW ≠ 单字母 V**；费用 ≠ 占用；**严禁复用假设-W** |
| BU | 融券券池日可借量（复检在途） | 否 | 新开日库存 ≠ 存量占用；**BW≠BU**；**不改 BU** |
| BF | 合约期限到期强制了结 | 否 | 到期 ≠ 授信占用；**BW≠BF**；**不改 BF** |
| BT | 强制平仓顺序与范围 | 否 | 维持线强平序 ≠ 出借方占用；**BW≠BT**；**不改 BT** |
| BC | 维持担保比例闸门 | 否 | 闸门 on/off ≠ 占用；**BW≠BC** |
| BB | 转融券暂停后假无限券源 | 否 | 暂停闸门 ≠ 占用；**BW≠BB** |
| BQ | 标的调出后存量假续持 | 否 | 名单调出 ≠ 出借方占用；**BW≠BQ** |
| K | 融券空头名单 | 否 | 名单 ∈ ≠ 占用公式吹瘦；**BW≠K**；带过 BK≠K |
| BR/BO/BS/BH | 借券费/假零息/利率档/授信 | 否 | 计息计费额度 ≠ 占用 |
| BP/BN/BM/BL/BE | 权益补偿/账户串用/追保禁开/提取/市场25pct | 否 | 另页主病；带过消歧链 |
| A/B/Z/BA/BD/BG/AB/W/H/T/S/U | 板上/旧位/开仓比例/融资名单/折算/可充抵/价限/除权/退市/证管费/经手费/过户费 | 否 | 硬分列；避开预检T；不改已齐 |

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-03 | 新建纸面草稿（待预检）：主题=两融授信占用口径误开；`bw0_primary_demo`=`invent_understate_credit_usage`；Y/G/N/Y2=0.02/0.01/0.05/0.015；硬分列强调 **BW≠W/BV/BU/BT/BS/BO/BR/BH**；未开回测；未改已齐字母；未标纸面齐 |
