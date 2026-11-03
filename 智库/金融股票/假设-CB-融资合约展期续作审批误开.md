# 假设 CB · 融资合约展期/续作审批误开 / 用核对日免审或无限展期规则铺满（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CA 补丁已交（复检在途）、写下一纸面 CB；清单撞题规则另选正交执行缺口（**融资合约到期前展期/续作是否须审批、可否自动续作** ≠ 合约期限到期强制了结 ≠ 提前了结手续费/违约金 ≠ 维持担保比例分子分母公式 ≠ 股票池当时名单 ≠ 板上枯竭 ≠ 印花税/财务可见/除权旧 B 位）；选题自融资融券业务公开口径：融资合约有约定期限，到期前展期/续作通常须满足资格与审批（客户申请、券商审核、维持担保比例/授信/名单等前提）；不得默认「到期前永远自动免审展期、无限续作，或用核对日更宽免审/无限展期规则铺满历史」；本页**假定合约期限层（BF）/提前了结费层（BZ）/维持比公式层（CA）/开仓保证金（Z）/融资名单（BA）/授信占用（BW）诚实或显式旁路**，主病只在**融资合约展期/续作审批**；2010-03-31 前无此通道；**BF 正文主测「期限到期强制了结」**（到期日闸门），**BZ 正文主测「主动提前了结手续费/违约金」**，**CA 正文主测「维持担保比例分子分母口径」**（复检在途；`invent_wrong_maint_guarantee_ratio_num_den`；**严禁改 CA**），**B 正文主测历史实验 B 旧位（印花税时点+T+1 / 财务可见日 / 除权日复权价误判等；已迁 V/W 等）**（**双字母 CB ≠ 单字母假设-B；严禁复用 B 题面**），**C 正文主测「股票池当时名单/幸存者偏差」**（**双字母 CB ≠ 单字母假设-C；严禁复用 C 题面**），本页主测**融资合约展期/续作审批被误开**（`invent_always_allow_financing_rollover`）→ 自立；与假设 A（板上；**CB≠A**）/ H（退市整理）/ **B（历史清单实验 B 旧位；双字母 CB ≠ 单字母 B；严禁复用 B；CB≠B）** / **C（股票池当时名单；双字母 CB ≠ 单字母假设-C；严禁复用 C；CB≠C）** / **CA（维持比分子分母；复检在途；CB≠CA；公式 ≠ 展期审批；尤其不改假设-CA）** / Z（开仓保证金比例；**CB≠Z**）/ BA–BZ（两融族已冻/在途；**CB≠BA…BZ**；**尤其不改 BZ/BF**）/ **BF（合约期限到期强制了结；CB≠BF；到期了结 ≠ 到期前展期审批；尤其不改假设-BF）** / **BZ（提前了结手续费；CB≠BZ；提前了结费 ≠ 展期审批；尤其不改假设-BZ）** / BW/BV/BU/BS/BO/BR/BH/BX/BY/BC/BT/BD/BL 等**分列**；**新建实验 CB**  
状态：**草稿 · 待预检**（结论栏空；禁止把「假无限展期 / 用核对日免审无限续作规则铺满」当诚实展期审批口径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–CA 及其他 A/D–CA 已交正文与冻结补丁；尤其不改假设-B；尤其不改假设-C；尤其不改假设-CA；尤其不改假设-BF；尤其不改假设-BZ；尤其不改假设-A；不改假设-H；不改假设-K；不改假设-BA–BZ；不改假设-AB；勿再改 CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CB（约 #85）。与假设 **B（历史实验 B 旧位）** **硬分列（专节强调）**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 CB ≠ 单字母 B**；**严禁复用 B 题面**；**绝不可做成 B 旧位续篇**。与假设 **C（股票池当时名单/幸存者偏差）** **硬分列（专节强调）**：C = 成分/股票池 PIT 与幸存者偏差；本页 = 融资合约**到期前展期/续作审批**；幸存者偏差 ≠ 展期审批。**双字母 CB ≠ 单字母假设-C**；**严禁复用 C 题面**；**绝不可做成 C 续篇**。与假设 **CA（维持担保比例分子分母口径）** **硬分列（专节强调）**：CA = 维持比**怎么算**（分子分母计项；复检在途）；本页 = 合约到期前**能否展期/续作及审批**；公式 ≠ 展期审批；**禁止**把「分子分母已诚实（CA）」静默写成「展期审批已诚实」；**不占** CA 的 `invent_wrong_maint_guarantee_ratio_num_den`；**尤其不改假设-CA**。**CB≠CA**。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = **到期日**是否强制了结；本页 = **到期前**展期/续作是否须审批、可否自动续；到期了结 ≠ 展期审批；**尤其不改假设-BF**。**CB≠BF**。与假设 **BZ（融资提前了结手续费/违约金）** **硬分列**：BZ = 主动提前了结费；本页 = 展期/续作审批；提前了结费 ≠ 展期审批；**尤其不改假设-BZ**。**CB≠BZ**。与假设 **BY / BC / BT / BW / BO / BS / BX / BH / BR / BA–BN / BP/BQ/BB/BD/BL/BM/Z/K/AB** **硬分列**：宽限 / 闸门 / 强平序 / 占用 / 假零息 / 利率档 / 起息 / 额度 / 借券费 / 融资名单等 ≠ 展期审批；并**带过 CA≠A/C/BZ/BY…、BZ≠Z/BY/BX…、BY≠Y/BX…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K、BH≠H**。与假设 AN–CA **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-B（旧位）**。**严禁复用假设-C（股票池当时名单）**。**严禁改写/续写假设-CA（维持比公式）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CB** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 B**（历史实验 B 旧位；**严禁复用假设-B**）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **单字母实验 A** ≠ **单字母实验 Z** ≠ **单字母实验 K** ≠ **单字母实验 Y**。全文凡写「实验 CB / 假设-CB / hypothesis_id=CB / 组 CB0·CB1·CB2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CB 混读或互改；**尤其 params.Y ≠ 实验字母 CB ≠ 单字母假设-B ≠ 单字母假设-C ≠ 双字母假设-CA**。亦**禁止**把实验字母 CB 与单字母 **A/B/C/Z/K/Y/T/S/U/V/W/X**、双字母 **BA–CA**、双字母 **BF/BZ/BY/BC/BT/BD/BL/BW/BV/BU/BS/BO/BR/BH**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `cb0_*` 以外的实验页混读。**双字母 CB ≠ 单字母 B ≠ 单字母 C ≠ 单字母 A ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 Y ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 CA ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BF ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 CB**；**params.G ≠ 实验字母 CB**；**params.N ≠ 实验字母 CB**。**带过：双字母 CA ≠ A/C/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/Z…；双字母 BZ ≠ Z/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH…；双字母 BY ≠ Y/BX/BW/BV/BU/BT/BS/BO/BR/BH/BM/BC…；双字母 BX ≠ X/BW…；双字母 BW ≠ W/BV…；双字母 BV ≠ V/BU/BT…；双字母 BU ≠ U/BB/BT/K…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC…；双字母 BP ≠ P/BO/W；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CB ≠ 单字母假设-B；且 ≠ 单字母假设-C；且 ≠ 假设-CA / 假设-BF / 假设-BZ；带过 CA≠A/C/BZ…、BZ≠Z/BY…、params.Y≠CB（硬）

| 维度 | 对照页 | 本页假设-CB（双字母） |
|------|--------|----------------------|
| 题面 B | **历史实验 B 旧位**（印花税时点+T+1 / 财务可见日 / 除权日复权价误判等；已迁 V/W） | **融资合约展期/续作审批**误开：假无限免审展期 vs 按生效日审批 PIT；**严禁复用 B 题面**；**绝不可做成 B 旧位续篇** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 幸存者偏差 ≠ 展期审批；**严禁复用 C 题面**；**绝不可做成 C 续篇**；**CB≠C** |
| 题面 CA | **维持担保比例分子分母口径**（复检在途；`invent_wrong_maint_guarantee_ratio_num_den`） | **到期前展期/续作是否须审批**；公式 ≠ 展期审批；**CB≠CA**；**不改 CA** |
| 题面 BF | **合约期限到期强制了结**（到期日闸门） | **到期前**展期/续作审批；到期了结 ≠ 展期审批；**CB≠BF**；**不改 BF** |
| 题面 BZ | **融资提前了结手续费/违约金**（`invent_ignore_early_repay_fee_or_penalty`） | 提前了结费 ≠ 展期审批；**CB≠BZ**；**不改 BZ** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_always_allow_financing_rollover` |
| 文档 | 清单实验 B / 清单实验 C / `假设-CA-…` / `假设-BF-…` / `假设-BZ-…`（**只读；禁止改写**） | `假设-CB-融资合约展期续作审批误开.md`（新建） |
| 预检键 | 实验字母 B / C / CA / BF / BZ | 实验字母 **CB** / `cb0_primary_demo`；**不得**占用或改写预检 B/C/CA/BF/BZ |

**禁止**：把 CB 写成「B/C/CA/BF/BZ 的续篇」；把「旧 B 已诚实 / 股票池已诚实（C）/ 分子分母已诚实（CA）/ 到期了结已诚实（BF）/ 提前了结费已诚实（BZ）」静默写成「展期审批已诚实」；覆盖或补丁改写假设-B / 清单实验 C / 假设-CA / 假设-BF / 假设-BZ 正文；把 `params.Y/G/N` 与实验字母 CB 混读；**禁** `cb0_primary_demo` 与 `invent_asof_leak_financing_rollover` **双挂主报**；**禁** CB1 半泄露升格并列主报；**禁**复用假设-B / 假设-C 题面或口径键；**禁**复用 CA 的 `invent_wrong_maint_guarantee_ratio_num_den` 或 BF/BZ 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有信用账户融资路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/授信占用/合约期限到期闸门/提前了结费/维持比公式等输入（Z/BA/BW/BF/BZ/CA 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/授信占用/到期强制了结/提前了结费/维持比分子分母」）下，把「融资合约到期前永远自动免审展期、无限续作」或「全样本用核对日当天更宽免审/无限展期规则回放历史」当成默认，相对「每个交易日按当时有效融资合约展期/续作审批规则 PIT（须客户申请+券商审核；可附维持比/授信/名单前提；拒批或到期未获批则按 BF 层到期了结或显式失败；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假无限展期路径并高估可续持融资名义、低估因展期拒批/未获批导致的被动了结冲击**；差异应**集中在融资合约展期/续作审批误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假无限展期贡献差、可续持名义差、被动了结冲击差在标定噪声带内可忽略，且「假无限展期 / 核对日泄露 / 正常审批窗 / 审批切日窗 / 通道前 / vs A·B·C·CA·Z·BA–BZ·BF·BZ·K·AB·Y·H·W·V·T·S·U·X」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融资合约展期/续作审批 ≠ 到期强制了结（BF）；≠ 提前了结费（BZ）；≠ 维持比分子分母（CA）；≠ 股票池当时名单（C）；≠ 历史实验 B 旧位

```
# 配置写死键（见 §7；草稿·待预检；建议值如下；终值待风控预检冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CB；≠ 单字母假设-B；≠ 单字母假设-C；≠ 双字母假设-CA；≠ 实验字母 BF；≠ 实验字母 BZ
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CB
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CB；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.financing_rollover_honest       写死 pit_by_effective_date
# params.financing_rollover_scope        写死 financing_contract_rollover_or_renewal_approval
# params.financing_rollover_over_policy  写死 approve_or_reject_or_fail_missing_rollover_rule
# params.financing_rollover_naive        写死 invent_always_allow_financing_rollover
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page
# params.haircut_handoff                 写死 bd_page
# params.balance_pause_handoff           写死 be_page
# params.contract_term_handoff           写死 bf_page   # 到期强制了结交 BF；CB≠BF；本页主病是到期前展期审批不是到期了结；不改 BF
# params.collateral_list_handoff         写死 bg_page
# params.credit_quota_handoff            写死 bh_page
# params.short_proceeds_use_handoff      写死 bi_page
# params.financing_sale_repay_handoff    写死 bj_page
# params.client_conc_handoff             写死 bk_page
# params.collateral_withdraw_handoff     写死 bl_page
# params.margin_call_open_ban_handoff    写死 bm_page
# params.cross_account_handoff           写死 bn_page
# params.financing_interest_handoff      写死 bo_page
# params.corp_action_comp_handoff        写死 bp_page
# params.list_removal_stock_handoff      写死 bq_page
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page
# params.force_close_order_handoff       写死 bt_page
# params.daily_short_inventory_handoff   写死 bu_page
# params.short_recall_handoff            写死 bv_page
# params.credit_usage_handoff            写死 bw_page
# params.interest_start_daycount_handoff 写死 bx_page
# params.margin_call_grace_handoff       写死 by_page
# params.early_repay_fee_handoff         写死 bz_page   # 提前了结费交 BZ；CB≠BZ；不改 BZ
# params.maint_ratio_formula_handoff     写死 ca_page   # 维持比分子分母交 CA；CB≠CA；复检在途亦勿改 CA
# params.financing_rollover_handoff      写死 self      # 本页主病：融资合约展期/续作审批
# params.universe_pool_handoff           写死 c_page    # 股票池当时名单交 C；CB≠C；严禁复用假设-C
# params.auction_vol_handoff             写死 y_page
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.st_limit_handoff                写死 x_page
# params.stamp_tax_handoff               写死 v_page
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.cb0_primary_demo                建议 invent_always_allow_financing_rollover  # 主报：假无限免审展期；禁与 invent_asof_leak_financing_rollover 双挂争主表；CB1半泄露不得升格并列主报
# params.cb0_invent_always_allow_financing_rollover  建议 True
# params.cb1_asof_leak_financing_rollover_only 建议 True
# params.cb2_pit_financing_rollover      建议 True
# params.merge_with_A_fill               写死 False
# params.merge_with_B_legacy             写死 False  # CB≠B；严禁复用假设-B
# params.merge_with_C_universe_pool      写死 False  # CB≠C；严禁复用假设-C
# params.merge_with_CA_maint_ratio_formula 写死 False  # CB≠CA；不改 CA
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_BF_contract_term     写死 False  # CB≠BF；不改 BF
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
# params.merge_with_BV_short_recall      写死 False
# params.merge_with_BW_credit_usage      写死 False
# params.merge_with_BX_interest_start_daycount 写死 False
# params.merge_with_BY_margin_call_grace 写死 False
# params.merge_with_BZ_early_repay_fee   写死 False  # CB≠BZ；不改 BZ
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_Y_auction_vol        写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.missing_financing_rollover_policy 写死 skip
# params.day_freq_proxy                  写死 financing_rollover_sensitivity
# params.universe_rule                   写死 sse_szse_financing_rollover_check
# params.fail_policy                     写死 skip
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.Y / G / N / Y2                  待预检建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母CB；params.G≠实验字母CB；params.N≠实验字母CB；亦≠单字母实验B/C/A/Z；禁 null/holdout/跑后改口
# params.date_start / date_end           写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改展期审批口径、Y/G/N/Y2、主窗/oos、cb0_primary_demo
```

可编码摘要（伪代码，不开跑）：

```
asof = params.asof_check_date  # 2026-10-16
# CB0：假无限免审展期——到期前永不检查审批、永远自动续作
# CB1：仅 asof 日更宽免审/无限展期规则泄露铺满
# CB2：每个交易日 d 按当日已生效展期/续作审批规则 PIT
# 消费 BF 诚实到期了结（或旁路声明本页不重开到期闸门）；消费 CA 维持比公式/BZ 提前了结费为旁路输入
# 缺审批字段 → skip（params.missing_financing_rollover_policy）
```

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
margin_channel_start = "2010-03-31"
financing_rollover_honest = "pit_by_effective_date"
financing_rollover_scope = "financing_contract_rollover_or_renewal_approval"
financing_rollover_over_policy = "approve_or_reject_or_fail_missing_rollover_rule"
cb0_primary_demo = "invent_always_allow_financing_rollover"  # 单一主报建议；禁与 invent_asof_leak_financing_rollover 双挂
cb0_invent_always_allow_financing_rollover = True
cb1_asof_leak_financing_rollover_only = True
cb2_pit_financing_rollover = True
merge_with_B_legacy = False
merge_with_C_universe_pool = False
merge_with_CA_maint_ratio_formula = False
merge_with_BF_contract_term = False
merge_with_BZ_early_repay_fee = False
merge_with_Z_margin_ratio = False
fail_policy = "skip"
```

### 2.2 三组对照（CB0 / CB1 / CB2）

| 组 | 口径 | 说明 |
|----|------|------|
| CB0 天真 | `invent_always_allow_financing_rollover`（单一主报建议） | 发明假无限免审展期路径；禁与 invent_asof_leak_financing_rollover 双挂 |
| CB1 半泄露·混口径 | 全样本用 `asof_check_date` 当天更宽免审/无限展期规则铺满历史 | 仅展期审批 asof 泄露；不升格并列主报 |
| CB2 PIT | `financing_rollover_honest=pit_by_effective_date` | 每个交易日按当时已生效融资合约展期/续作审批规则 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：融资合约到期日/剩余期限代理 + 展期申请/审批结果代理 + 当日生效展期审批规则 → 当日是否获批续作；缺审批字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有融资合约到期日代理 + 展期审批规则生效日表 + 到期了结（消费 BF，旁路）+ 维持比（消费 CA，旁路声明「本页假定公式层诚实」）即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。  
- **通道前**：`margin_channel_start=2010-03-31` 前无本页展期审批通道。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组 / 半泄露组相对诚实组的假无限展期贡献差、可续持名义差、被动了结冲击差超出标定噪声带，且差异集中在「融资合约展期/续作审批误开」桶，不被 B 旧位、C 股票池、CA 维持比公式、BF 到期了结、BZ 提前了结费等他页桶吞并。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 B/C/CA/BF/BZ/A/Z/T 等他页桶吞并；或 holdout 反调 `cb0_primary_demo` / Y·G·N·Y2；或 CB0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CB0 / CB1 / CB2。报告可续持名义差、假无限展期贡献差、被动了结冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_always_allow_financing_rollover",
  "invent_asof_leak_financing_rollover",
  "financing_rollover_window",
  "financing_rollover_cut_window",
  "pre_margin_channel_20100331",
  "vs_A_limit_up_fill",
  "vs_B_legacy",
  "vs_C_universe_pool",
  "vs_CA_maint_ratio_formula",
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
  "vs_BV_short_recall",
  "vs_BW_credit_usage",
  "vs_BX_interest_start_daycount",
  "vs_BY_margin_call_grace",
  "vs_BZ_early_repay_fee",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_Y_auction_vol",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_X_st_limit_avoid",
  "vs_V_stamp_tax_avoid",
  "vs_U_transfer_fee_avoid",
  "vs_T_csrc_fee_avoid",
  "vs_S_handling_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够融资合约到期/展期字段；缺字段却静默当假无限展期 → 设计失效。  
2. 把「到期强制了结已诚实（BF）」静默写成「展期审批已诚实」且不声明另页 BF → **与 BF 撞题**（到期了结 ≠ 展期审批；**尤其 CB≠BF**；**不改 BF**）。  
3. 把「提前了结费已诚实（BZ）」静默写成「展期审批已诚实」 → **与 BZ 撞题**（**尤其 CB≠BZ**；**不改 BZ**）。  
4. 把「维持比分子分母已诚实（CA）」静默写成「展期审批已诚实」 → **与 CA 撞题**（公式 ≠ 展期；**尤其 CB≠CA**；**不改 CA**；复检在途亦勿改）。  
5. 把「股票池已诚实（C）」或「历史 B 旧位已诚实」静默写成「展期审批已诚实」→ **撞假设-C / 假设-B**（**严禁复用**；**尤其 CB≠C / CB≠B**；**绝不可做成 C/B 续篇**）。  
6. 把「开仓比例/名单/占用/宽限/闸门/强平序已诚实」写成主病或不声明另页 → 与 Z/BA/BW/BY/BC/BT 等撞题。  
7. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「展期审批已诚实」→ 与交易所费用族撞题（**明确避开预检T**）。  
8. 把实验字母 CB 与单字母 A/B/C/Z/K/Y/T/S/U/V/W/X 或双字母 BA–CA/BF/BZ/BY/BC/BT/BD/BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
9. holdout 反调 `cb0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价代理合约到期/展期路径 → 标签与执行双错，结论无效。  
11. 用核对日更宽「假无限展期」当诚实 PIT、或把券商临时宽口径铺满历史 → 设计失效。  
12. **`cb0_primary_demo` 与 `invent_asof_leak_financing_rollover` 双挂主报**；或 CB1 升格并列主报 → 设计失效。  
13. **改写或覆盖 `假设-B` / 清单实验 C / `假设-CA` / `假设-BF` / `假设-BZ` / 已冻 AA–CA** → 硬边界违约，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资合约开仓日/到期日/剩余期限代理、展期申请与审批结果代理、展期/续作审批规则及生效日；  
- 开仓保证金比例 / 融资名单 / 授信占用 / 合约期限到期闸门 / 提前了结费 / 维持比公式输入（消费 Z/BA/BW/BF/BZ/CA 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：会员加严展期审批子集；与 BF 到期窗、CA 维持比窗、BZ 提前了结费窗对照但不混主结论；拒批原因码敏感性（主报仍在展期审批）。

**禁止**：用核对日「今天免审无限展期」铺满当唯一诚实组；用复权价；把到期了结已诚实/提前了结费已诚实/分子分母已诚实/股票池已诚实/旧 B 已诚实/开仓比例已诚实/占用已诚实/名单仍在池/授信够当成「展期审批正确」依据；把 Z/BA–CA/BF/BZ/K/AB/A/B/C/H/W/Y/X/V/U/T/S/AN–CA 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`CB`  
- **组**：CB0 / CB1 / CB2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`financing_rollover_honest=pit_by_effective_date`；`financing_rollover_scope=financing_contract_rollover_or_renewal_approval`；`financing_rollover_over_policy=approve_or_reject_or_fail_missing_rollover_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`force_close_order_handoff=bt_page`；`daily_short_inventory_handoff=bu_page`；`short_recall_handoff=bv_page`；`credit_usage_handoff=bw_page`；`interest_start_daycount_handoff=bx_page`；`margin_call_grace_handoff=by_page`；`early_repay_fee_handoff=bz_page`；`maint_ratio_formula_handoff=ca_page`；`universe_pool_handoff=c_page`；`auction_vol_handoff=y_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`st_limit_handoff=x_page`；`stamp_tax_handoff=v_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_financing_rollover_check`；`missing_financing_rollover_policy=skip`；`day_freq_proxy=financing_rollover_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 待预检建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 CB**；**params.G≠实验字母 CB**；**params.N≠实验字母 CB**；亦≠单字母实验 B/C/A/Z；禁 null/holdout/跑后改口）；**`params.cb0_primary_demo` 建议 `invent_always_allow_financing_rollover`**（禁与 invent_asof_leak_financing_rollover 双挂；CB1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- CB0/CB1/CB2 净收益/成本质量、ΔFakeInfiniteRollover、ΔSustainableNotional、ΔForcedUnwindImpact；分桶（融资合约展期/续作审批误开 / 核对日泄露 / 正常审批窗 / 审批切日窗 / 通道前 / vs A·B·C·CA·Z·BA–BZ·BF·BZ·K·AB·Y·H·W·X·V·U·T·S）。  
- 自检气泡：CB2 是否 pit_by_effective_date；CB0 是否单一主报；CB1 是否仅核对日泄露；是否未与 A/B/C/CA/Z/BA–BZ/BF/BZ/K/AB/Y/H/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 CB 与 B 或 C 或 CA 或 A 或 Z 或 K 或 Y 或 BA–BZ 或 BF 或 BZ 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 CB≠单字母假设-B；CB≠单字母假设-C；CB≠双字母假设-CA；params.Y≠实验字母 CB；CB≠BF；CB≠BZ；带过 CA≠A/C/BZ…、BZ≠Z/BY…、BY≠Y/BX…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–CA 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-C / 假设-CA / 假设-BF / 假设-BZ / 假设-Z / 假设-K / 假设-BA–BZ / 假设-AB**；**是否未再改 CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-B / 假设-C**；**是否未与 invent_asof_leak_financing_rollover 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假无限展期或核对日泄露吹成诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不占本机 8765 席位；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–CA 及其他 A/D–CA 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-C**；**不改假设-CA**；**不改假设-BF**；**不改假设-BZ**；**不改假设-Z**；**不改假设-K**；**不改假设-BA–BZ**；**尤其不改假设-B；尤其不改假设-C；尤其不改假设-CA；尤其不改假设-BF；尤其不改假设-BZ**；**不改假设-AB**；**勿再改 CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限到期强制了结（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券券池日可借量（BU）、融券提前召回（BV）、授信占用口径（BW）、融资利息起息日/计息天数（BX）、追保宽限期/强平通知时限（BY）、融资提前了结手续费/违约金（BZ）、维持担保比例分子分母口径（CA）、融券空头名单（K）、股票池当时名单（C）、历史实验 B 旧位之外，**融资合约展期/续作审批**须按当时有效规则 PIT；不得默认永远免审无限展期，或用核对日更宽规则铺满。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 CB** 标准件，**不改口径主线**，**不改假设 A–CA 正文**，**尤其不改假设-B / 假设-C / 假设-CA / 假设-BF / 假设-BZ**。与实验 A/B/C/CA/Z/BA–BZ/BF/BZ/K/AB/H/W/Y/X/V/U/T/S 分工：**B=历史旧位（严禁复用）；C=股票池当时名单（严禁复用）；CA=维持比分子分母（复检在途，严禁改写）；BF=到期强制了结；BZ=提前了结费；CB=融资合约展期/续作审批误开（CB≠B≠C≠CA≠A≠Z≠K≠Y≠BA≠…≠BZ≠BF≠BY≠BC≠BT≠BD≠BL≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AB≠W≠H≠T≠S≠U≠V≠X；带过 CA≠A/C/BZ…、BZ≠Z/BY…、BY≠Y/BX…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 待预检**（结论栏空；**未标纸面齐**） |
| 标准件路径 | `假设-CB-融资合约展期续作审批误开.md` |
| 清单序号 | 约 #85 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**financing_rollover_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 待预检建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 CB；params.G≠实验字母 CB；params.N≠实验字母 CB；亦≠单字母实验 B/C/A/Z；禁 null/holdout/跑后改口）**；**cb0_primary_demo 建议 invent_always_allow_financing_rollover（禁双挂 invent_asof_leak_financing_rollover；CB1半泄露不得升格并列主报）**；锚点建议 financing_rollover_honest=pit_by_effective_date / financing_rollover_scope=financing_contract_rollover_or_renewal_approval / financing_rollover_over_policy=approve_or_reject_or_fail_missing_rollover_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **CB≠B/C/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BF/BC/BD/BL/Z/A**（及 ≠Y/BA–CA/K/AB/H/W/T/S/U/V/X），**严禁复用假设-B / 假设-C**；**尤其不改假设-B/C/CA/BF/BZ**；**params.Y≠实验字母 CB** |
| 结论栏 | 空 |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**待预检**；**params.Y≠实验字母 CB**；**params.G≠实验字母 CB**；**params.N≠实验字母 CB**；禁 null/holdout）  
2. `params.cb0_primary_demo` = `invent_always_allow_financing_rollover`（**待预检**；禁与 `invent_asof_leak_financing_rollover` 双挂；CB1不升格主报）  
3. 锚点（已通写死建议）：`financing_rollover_honest=pit_by_effective_date` / `financing_rollover_scope=financing_contract_rollover_or_renewal_approval` / `financing_rollover_over_policy=approve_or_reject_or_fail_missing_rollover_rule` / `margin_channel_start=2010-03-31` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`

---

## 与 BA–CA / B / C / BF / BZ 撞题检查表

| 对照 | 是否撞题 | 说明 |
|------|----------|------|
| 假设-B | **否（硬分列）** | 历史旧位（印花税/财务可见/除权） ≠ 展期审批；**CB≠B**；**严禁复用**；绝不可做成 B 续篇 |
| 假设-C | **否（硬分列）** | 股票池当时名单 ≠ 展期审批；**CB≠C**；**严禁复用**；绝不可做成 C 续篇 |
| 假设-CA | **否（硬分列）** | 维持比分子分母 ≠ 展期审批；**CB≠CA**；不改 CA（复检在途） |
| 假设-BF | **否（硬分列）** | 到期强制了结 ≠ 到期前展期审批；**CB≠BF**；不改 BF |
| 假设-BZ | **否（硬分列）** | 提前了结费 ≠ 展期审批；**CB≠BZ**；不改 BZ |
| 假设-BY/BC/BT/BW/BO/BS/BX/BH/BR | **否** | 宽限/闸门/序/占用/假零息/利率档/起息/额度/借券费 ≠ 展期 |
| 假设-BA–BN/BP/BQ/BB/BD/BL/BM/Z/K/AB | **否** | 各页主病岔路；本页不重开 |
| 假设-A/H/W/X/V/U/T/S/Y | **否** | 板上/退市/除权/ST板幅/印花税/过户/证管/经手/集合量 ≠ 展期 |

---

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 新建草稿·待预检（总管线：CA 补丁已交后写 CB；选题融资合约展期/续作审批误开；**CB≠B/C/CA/BF/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH…**；primary_demo 建议=`invent_always_allow_financing_rollover`；Y/G/N/Y2 待预检；不开回测；未改 B/C/CA/BF/BZ 及其他已齐字母；**未标纸面齐**）。 |
