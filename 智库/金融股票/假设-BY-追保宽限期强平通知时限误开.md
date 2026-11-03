# 假设 BY · 追保宽限期/强平通知时限误开 / 用核对日宽限期或强平时限规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BX 补丁已交（复检在途）、写下一纸面 BY；清单撞题规则另选正交执行缺口（**追保通知后宽限期与强平通知时限怎么算** ≠ 追保期内禁新开 ≠ 强制平仓顺序与范围 ≠ 维持担保强平闸门 ≠ 担保品提取 ≠ 融资利息起息日/日基数 ≠ 授信占用 ≠ 融资假零息 ≠ 融资利率档 ≠ 集合竞价量计入日线）；选题自两融会员风控公开口径：维持担保比例触及追保线并发出追保通知后，客户须在**当时有效宽限期/通知时限**内补足担保（常见按交易日计的宽限期；会员可加严）；逾期未到位须按当时规则进入强制平仓流程；规则按**施行日/生效日** PIT；不得默认「追保通知后永不计时/无限宽限、或永远按核对日更宽长宽限期铺满历史」；本页**假定追保通知已发、禁新开闸门（BM）与强平闸门（BC）层诚实或显式旁路**，主病只在**宽限期长度与强平通知时限**；2010-03-31 前无此通道；**BM 正文主测「追保期内仍假可新开」**（`invent_new_open_after_margin_call`），**BT 正文主测「强平触发后序与范围」**（`invent_force_close_best_order_or_min_scope`），**BC 正文主测「低维持强平闸门 on/off」**，本页主测**追保已通知后宽限期/时限被误开**（`invent_ignore_margin_call_grace_or_force_deadline`）→ 自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BY ≠ 单字母 B**）/ **Y（集合竞价量计入日线；双字母 BY ≠ 单字母假设-Y；严禁复用 Y 题面或集合量分母口径）** / Z（**开仓**融资/融券保证金比例；**BY≠Z**）/ BA–BX（两融族已冻/在途；**BY≠BA…BX**；**尤其不改 BX 正文**）/ **BM（追保禁新开；BY≠BM；尤其不改假设-BM）** / **BT（强平序与范围；BY≠BT；尤其不改假设-BT）** / **BC（维持线强平闸门；BY≠BC；尤其不改假设-BC）** / BW/BV/BU/BS/BO/BR/BH/BX 等**分列**；**新建实验 BY**  
状态：**草稿 · 待预检**（结论栏空；禁止把「追保通知后无限宽限 / 用核对日更宽长时限铺满」当诚实追保时限口径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BX 及其他 A/D–BX 已交正文与冻结补丁；尤其不改假设-BX；尤其不改假设-Y；尤其不改假设-BM；尤其不改假设-BT；尤其不改假设-BC；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-Z；不改假设-BA–BX；不改假设-AB；勿再改 BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BY（约 #82）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **追保宽限期/强平通知时限**。**双字母 BY ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BY ≠ 单字母 B**。与假设 **Y（集合竞价量计入日线）** **硬分列（专节强调）**：Y = 日总量当连续可冲击分母（开盘/收盘集合量并进）；本页 = 信用账户**追保通知后宽限期与强平通知时限**；集合量分母 ≠ 追保时限。**双字母 BY ≠ 单字母假设-Y**；**严禁复用 Y 题面或 Y 口径键**；**亦强调 params.Y（显著性门槛键）≠ 实验字母 BY ≠ 单字母假设-Y**。与假设 **BM（追保通知后仍假可新开仓）** **硬分列**：BM = 追保期内**能否新开**；本页 = 追保通知后**几天内须到位、逾期是否按当时时限进入强平通知**；禁新开 ≠ 宽限期长度；**禁止**把「禁新开已诚实（BM）」静默写成「宽限期已诚实」；**不占** BM 的 primary_demo；**尤其不改假设-BM**。**BY≠BM**。与假设 **BT（强制平仓顺序与范围）** **硬分列**：BT = 强平**已触发后**平哪条腿、平多少；本页 = **触发前**宽限期/通知时限；序与范围 ≠ 时限；**尤其不改假设-BT**。**BY≠BT**。与假设 **BC（维持担保比例强制平仓闸门）** **硬分列**：BC = 低维持线强平闸门 **on/off**；本页 = 追保已通知后的**计时宽限**；闸门 ≠ 时限；**尤其不改假设-BC**。**BY≠BC**。与假设 **BX（融资利息起息日/计息天数）** **硬分列**：BX = 利息从哪天起算几天（复检在途）；本页 = 追保宽限几天；起息 ≠ 追保时限；**尤其不改假设-BX**。**BY≠BX**。与假设 **BW / BV / BU / BS / BO / BR / BH / BL / BF / BB / BA / BD / BG / Z / K / AB** **硬分列**：占用 / 召回 / 日库存 / 利率档 / 假零息 / 借券费 / 额度上限 / 提取 / 合约期限 / 转融暂停 / 融资名单 / 折算率 / 可充抵 / 开仓比例 / 融券名单 / 空头价限 ≠ 追保宽限期；并**带过 BX≠X/BW/BV/BU/BT/BS/BO/BR/BH…、BW≠W/BV/BU/BT/BS/BO/BR/BH…、BV≠V/BU/BT/BF/BC/BB/BQ/K…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 AN–BX **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-Y（集合竞价量计入日线）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BY** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 Y**（集合竞价量计入日线；**严禁复用假设-Y**）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BY / 假设-BY / hypothesis_id=BY / 组 BY0·BY1·BY2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BY 混读或互改；**尤其 params.Y ≠ 实验字母 BY ≠ 单字母假设-Y**。亦**禁止**把实验字母 BY 与单字母 **A**、单字母 **B**、单字母 **Y**、单字母 **K**、单字母 **Z**、单字母 **T**、单字母 **S**、单字母 **U**、单字母 **V**、单字母 **W**、单字母 **X**、双字母 **BA–BX**、双字母 **BM**、双字母 **BT**、双字母 **BC**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `by0_*` 以外的实验页混读。**双字母 BY ≠ 单字母 A ≠ 单字母 B ≠ 单字母 Y ≠ 单字母 K ≠ 单字母 Z ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 BA ≠ … ≠ 双字母 BX ≠ 双字母 BM ≠ 双字母 BT ≠ 双字母 BC ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BY**；**params.G ≠ 实验字母 BY**；**params.N ≠ 实验字母 BY**。**带过：双字母 BX ≠ X/BW/BV/BU/BT/BS/BO/BR/BH…；双字母 BW ≠ W/BV/BU/BT/BS/BO/BR/BH…；双字母 BV ≠ V/BU/BT/BF/BC/BB/BQ/K…；双字母 BU ≠ U/BB/BT/K/BS/BO/BR/BH…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 BY ≠ 单字母假设-Y；且 ≠ 假设-BM / 假设-BT / 假设-BC / 假设-BX / 假设-BW / 假设-BV / 假设-BU / 假设-BS / 假设-BO / 假设-BR / 假设-BH；带过 BX≠X/BW…、BW≠W/BV…、BT≠T/BC/BS…、BM≠BC、BM≠BL、params.Y≠BY（硬）

| 维度 | 对照页 | 本页假设-BY（双字母） |
|------|--------|----------------------|
| 题面 Y | 集合竞价量计入日线假连续流动性（`day_total_as_continuous`） | **追保宽限期/强平通知时限**误开：假无限宽限 vs 按生效日宽限/时限 PIT；**严禁复用 Y 题面** |
| 题面 BM | **追保期内仍假可新开**（`invent_new_open_after_margin_call`） | **宽限期长度与逾期强平通知时限**；禁新开 ≠ 时限；**BY≠BM**；**不改 BM** |
| 题面 BT | **强平触发后顺序与范围**（`invent_force_close_best_order_or_min_scope`） | **触发前宽限/通知时限**；序范围 ≠ 时限；**BY≠BT**；**不改 BT** |
| 题面 BC | **维持线强平闸门 on/off**（`invent_no_force_close`） | 闸门 ≠ 宽限天数；**BY≠BC**；**不改 BC** |
| 题面 BX | **融资利息起息日/计息天数**（复检在途；`invent_wrong_financing_interest_start_or_daycount`） | 起息 ≠ 追保时限；**BY≠BX**；**不改 BX** |
| 题面 BW/BV/BU/BS/BO/BR/BH | 占用 / 召回 / 日库存 / 利率档 / 假零息 / 借券费 / 额度 | 各页主病 ≠ 追保宽限；**BY≠…** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ignore_margin_call_grace_or_force_deadline` |
| 文档 | `假设-Y-…` / `假设-BM-…` / `假设-BT-…` / `假设-BC-…` / `假设-BX-…`（**只读；禁止改写**） | `假设-BY-追保宽限期强平通知时限误开.md`（新建） |
| 预检键 | 实验字母 Y / BM / BT / BC / BX | 实验字母 **BY** / `by0_primary_demo`；**不得**占用或改写预检 Y/BM/BT/BC/BX |

**禁止**：把 BY 写成「Y/BM/BT/BC/BX 的续篇」；把「禁新开已诚实（BM）/ 强平序已诚实（BT）/ 闸门已诚实（BC）/ 起息已诚实（BX）/ 占用已诚实 / 召回已诚实」静默写成「宽限期与强平通知时限已诚实」；覆盖或补丁改写假设-Y / 假设-BM / 假设-BT / 假设-BC / 假设-BX 正文；把 `params.Y/G/N` 与实验字母 BY 混读；**禁** `by0_primary_demo` 与 `invent_asof_leak_margin_call_grace` **双挂主报**；**禁** BY1 半泄露升格并列主报；**禁**复用假设-Y（集合竞价量计入日线）题面或口径键；**禁**复用 BM 的 `invent_new_open_after_margin_call` 或 BT 的 `invent_force_close_best_order_or_min_scope` 当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有信用账户路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/融券名单/授信/追保禁开/维持强平闸门/强平序/提取线/融资利息层等输入（Z/BA/K/BH/BM/BC/BT/BL/BO 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/融券名单/总授信/追保禁新开/低维持强平闸门/强平序与范围/高维持提取/假零息主病」）下，把「追保通知后永不计时、无限宽限、逾期亦不进入强平通知」或「全样本用核对日当天更宽长宽限期/更松强平通知时限规则回放历史」当成默认，相对「每个交易日按当时有效追保宽限期与强平通知时限 PIT（通知发出后按当时规则计宽限交易日/自然日；逾期未到位 → 按当时规则进入强平通知或强制流程；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假无限宽限/假永不超时路径并高估可续持两融名义、低估因逾期未追保到位导致的被动强平冲击**；差异应**集中在追保宽限期/强平通知时限误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假无限宽限贡献差、可续持名义差、逾期强平冲击差在标定噪声带内可忽略，且「假无限宽限 / 核对日泄露 / 正常宽限窗 / 时限切日窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·BS·BT·BU·BV·BW·BX·K·AB·Y·B·H·W·V·T·S·U·X」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 追保宽限期/强平通知时限 ≠ 追保禁新开（BM）；≠ 强平序与范围（BT）；≠ 强平闸门（BC）；≠ 融资起息日基数（BX）；≠ 授信占用（BW）；≠ 集合量分母（Y）；≠ 开仓保证金比例（Z）；≠ 板上枯竭（A）；≠ 证管费（T）

```
# 配置写死键（见 §7；草稿·待预检；终值建议如下，待风控冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BY；≠ 单字母假设-Y；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 Z；≠ 实验字母 BM；≠ 实验字母 BT；≠ 实验字母 BC；≠ 实验字母 BX
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BY
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BY；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.margin_call_grace_honest        写死 pit_by_effective_date
# params.margin_call_grace_scope         写死 grace_period_and_force_notice_deadline
# params.margin_call_grace_over_policy   写死 apply_or_fail_missing_grace_rule
# params.margin_call_grace_naive         写死 invent_ignore_margin_call_grace_or_force_deadline
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page   # 强平闸门交 BC；BY≠BC；不改 BC
# params.haircut_handoff                 写死 bd_page
# params.balance_pause_handoff           写死 be_page
# params.contract_term_handoff           写死 bf_page
# params.collateral_list_handoff         写死 bg_page
# params.credit_quota_handoff            写死 bh_page
# params.short_proceeds_use_handoff      写死 bi_page
# params.financing_sale_repay_handoff    写死 bj_page
# params.client_conc_handoff             写死 bk_page
# params.collateral_withdraw_handoff     写死 bl_page
# params.margin_call_open_ban_handoff    写死 bm_page   # 追保禁新开交 BM；BY≠BM；本页主病是宽限/时限不是禁新开；不改 BM
# params.cross_account_handoff           写死 bn_page
# params.financing_interest_handoff      写死 bo_page
# params.corp_action_comp_handoff        写死 bp_page
# params.list_removal_stock_handoff      写死 bq_page
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page
# params.force_close_order_handoff       写死 bt_page   # 强平序交 BT；BY≠BT；不改 BT
# params.daily_short_inventory_handoff   写死 bu_page
# params.short_recall_handoff            写死 bv_page
# params.credit_usage_handoff            写死 bw_page
# params.interest_start_daycount_handoff 写死 bx_page   # 起息/日基数交 BX；BY≠BX；不改 BX（复检在途亦勿改）
# params.margin_call_grace_handoff       写死 self      # 本页主病：追保宽限期与强平通知时限
# params.auction_vol_handoff             写死 y_page    # 集合量分母交 Y；BY≠Y；严禁复用假设-Y
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.st_limit_handoff                写死 x_page
# params.stamp_tax_handoff               写死 v_page
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.by0_primary_demo                建议 invent_ignore_margin_call_grace_or_force_deadline  # 主报建议：假无限宽限/假忽略强平通知时限；禁与 invent_asof_leak_margin_call_grace 双挂争主表；BY1半泄露不得升格并列主报；待预检冻结
# params.by0_invent_ignore_margin_call_grace_or_force_deadline  写死 True
# params.by1_asof_leak_margin_call_grace_only 写死 True
# params.by2_pit_margin_call_grace       写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False  # BY≠BC；不改 BC
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_BF_contract_term     写死 False
# params.merge_with_BG_collateral_list   写死 False
# params.merge_with_BH_credit_quota      写死 False
# params.merge_with_BI_short_proceeds    写死 False
# params.merge_with_BJ_financing_sale_repay 写死 False
# params.merge_with_BK_client_conc       写死 False
# params.merge_with_BL_collateral_withdraw 写死 False
# params.merge_with_BM_margin_call_open_ban 写死 False  # BY≠BM；不改 BM
# params.merge_with_BN_cross_account     写死 False
# params.merge_with_BO_financing_interest 写死 False
# params.merge_with_BP_corp_action_comp  写死 False
# params.merge_with_BQ_list_removal_stock 写死 False
# params.merge_with_BR_short_borrow_fee  写死 False
# params.merge_with_BS_financing_rate_tier 写死 False
# params.merge_with_BT_force_close_order 写死 False  # BY≠BT；不改 BT
# params.merge_with_BU_daily_short_inventory 写死 False
# params.merge_with_BV_short_recall      写死 False
# params.merge_with_BW_credit_usage      写死 False
# params.merge_with_BX_interest_start_daycount 写死 False  # BY≠BX；不改 BX
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_Y_auction_vol        写死 False  # BY≠Y；严禁复用假设-Y
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.missing_grace_rule_policy       写死 skip
# params.day_freq_proxy                  写死 margin_call_grace_deadline_sensitivity
# params.universe_rule                   写死 sse_szse_margin_call_grace_deadline_check
# params.fail_policy                     写死 skip
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # 待预检；params.Y≠实验字母BY；params.G≠实验字母BY；params.N≠实验字母BY；亦≠单字母实验A/B/Y/Z；禁 null/holdout/跑后改口
# params.date_start / date_end           写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改宽限规则、时限、Y/G/N/Y2、主窗/oos、by0_primary_demo

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
margin_channel_start = "2010-03-31"
margin_call_grace_honest = "pit_by_effective_date"
margin_call_grace_scope = "grace_period_and_force_notice_deadline"
margin_call_grace_over_policy = "apply_or_fail_missing_grace_rule"
margin_call_grace_naive = "invent_ignore_margin_call_grace_or_force_deadline"
by0_primary_demo = "invent_ignore_margin_call_grace_or_force_deadline"  # 单一主报建议·待预检冻结；禁与 invent_asof_leak_margin_call_grace 双挂
by1_asof_leak_margin_call_grace_only = True
by2_pit_margin_call_grace = True
merge_with_BM_margin_call_open_ban = False
merge_with_BT_force_close_order = False
merge_with_BC_maint_force = False
merge_with_BX_interest_start_daycount = False
merge_with_Y_auction_vol = False
fail_policy = "skip"
```

### 2.2 三组对照（BY0 / BY1 / BY2）

| 组 | 口径 | 说明 |
|----|------|------|
| BY0 天真 | `invent_ignore_margin_call_grace_or_force_deadline`（单一主报建议·待预检） | 发明假无限宽限/假忽略强平通知时限路径；禁与 invent_asof_leak_margin_call_grace 双挂 |
| BY1 半泄露/混口径 | 全样本用 `asof_check_date` 当天更宽长宽限期或更松时限规则铺满历史 | 仅宽限/时限规则 asof 泄露；不升格并列主报 |
| BY2 PIT | `margin_call_grace_honest=pit_by_effective_date` | 每个交易日按当时已生效追保宽限期与强平通知时限规则 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：日终维持担保比例代理 + 追保通知发出标记 + 当日生效宽限期/强平通知时限规则 → 是否仍在宽限内 / 是否应进入强平通知；缺宽限/时限字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有日终维持担保比例代理 + 追保通知日 + 宽限期/强平通知时限规则生效日表 + 禁新开层（消费 BM，旁路）+ 强平闸门层（消费 BC，旁路）即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。  
- **通道前**：`margin_channel_start=2010-03-31` 前无本页追保时限通道。

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

天真组 / 半泄露组相对诚实组的假无限宽限贡献差、可续持名义差、逾期强平冲击差超出标定噪声带，且差异集中在「追保宽限期/强平通知时限误开」桶，不被 BM 禁新开、BT 强平序、BC 闸门、BX 起息、Y 集合量分母等他页桶吸走。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 BM 禁新开、BT 强平序、BC 闸门、BL 提取、BF 期限、BX 起息、Y 集合量、T 证管费等他页桶吸走；或 holdout 反调 `by0_primary_demo` / Y·G·N·Y2；或 BY0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BY0 / BY1 / BY2。报告可续持名义差、假无限宽限贡献差、逾期强平冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_ignore_margin_call_grace_or_force_deadline",
  "invent_asof_leak_margin_call_grace",
  "grace_period_window",
  "force_notice_deadline_cut_window",
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
  "vs_BV_short_recall",
  "vs_BW_credit_usage",
  "vs_BX_interest_start_daycount",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_Y_auction_vol",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_X_st_limit_avoid",
  "vs_V_stamp_tax_avoid",
  "vs_U_transfer_fee_avoid",
  "vs_T_csrc_fee_avoid",
  "vs_S_handling_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够追保通知腿或宽限/时限字段；缺字段却静默当无限宽限 → 设计失效。  
2. 把「追保禁新开已诚实（BM）」静默写成「宽限期已诚实」且不声明另页 BM → **与 BM 撞题**（能否新开 ≠ 宽限天数；**尤其 BY≠BM**；**不改 BM**）。  
3. 把「强平序已诚实（BT）」静默写成「宽限期已诚实」且不声明另页 BT → **与 BT 撞题**（序范围 ≠ 时限；**尤其 BY≠BT**；**不改 BT**）。  
4. 把「强平闸门已诚实（BC）」静默写成「宽限期已诚实」→ **与 BC 撞题**（闸门 ≠ 时限；**尤其 BY≠BC**；**不改 BC**）。  
5. 把「起息/日基数已诚实（BX）」写成主病或不声明另页 BX → **撞假设-BX**，设计失效（**尤其 BY≠BX**；**不改 BX**）。  
6. 把「集合量分母已诚实（Y）」写成主病或不声明另页 Y → **撞假设-Y**，设计失效（**双字母 BY ≠ 单字母 Y**；**严禁复用 Y**）。  
7. 把「提取线未触（BL）/ 期限未到（BF）/ 授信够（BH）/ 账户未串用（BN）」静默写成「宽限正确」→ 与对应页撞题（**尤其 BY≠BL≠BF≠BH≠BN**）。  
8. 把「占用已诚实（BW）/ 召回已诚实（BV）/ 日库存够（BU）/ 利率档诚实（BS）/ 假零息已关（BO）/ 借券费已计（BR）」静默写成「宽限正确」→ 与对应页撞题（**尤其 BY≠BW≠BV≠BU≠BS≠BO≠BR**）。  
9. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易 / 证管费」写成主病而不声明另页 AB/W/A/H/T → 与对应页撞题。  
10. 把实验字母 BY 与单字母 A/B/Y/K/Z/T/S/U/V/W/X 或双字母 BA–BX/BM/BT/BC/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `by0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价算维持担保比例代理 → 标签与执行双错，结论无效。  
13. 用核对日更宽「长宽限/松时限」当诚实 PIT、或把券商临时更宽宽限提前铺满历史 → 设计失效。  
14. **`by0_primary_demo` 与 `invent_asof_leak_margin_call_grace` 双挂主报**；或 BY1 升格并列主报 → 设计失效。  
15. **改写或覆盖 `假设-Y` / `假设-BM` / `假设-BT` / `假设-BC` / `假设-BX` / 已冻 AA–BX** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户维持担保比例代理、追保通知发出日/标记、宽限期与强平通知时限规则及生效日；  
- 开仓保证金比例 / 融资名单 / 融券名单 / 授信 / 追保禁新开 / 维持强平闸门 / 强平序 / 提取线输入（消费 Z/BA/K/BH/BM/BC/BT/BL 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商更严宽限子集；与 BM 禁开窗、BT 强平序窗、BC 闸门窗对照但不混主结论；盘中紧急时限另桶敏感性（主报仍在日终宽限/通知时限）。

**禁止**：用核对日「今天更长宽限」铺满当唯一诚实组；用复权价；把禁新开已诚实/强平序诚实/闸门已诚实/起息已诚实/占用已诚实/日库存够/期限未到/名单仍在池/转融未暂停/借券费已计/授信够/开仓保证金比例/新开名单窗/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/账户未串用/权益已补偿/调出后存量已处理/市场25pct未暂停/集合量分母已诚实当成「宽限正确」依据；把 Z/BA–BX/K/AB/A/B/H/W/Y/X/V/U/T/S/AN–BX 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BY`  
- **组**：BY0 / BY1 / BY2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`margin_call_grace_honest=pit_by_effective_date`；`margin_call_grace_scope=grace_period_and_force_notice_deadline`；`margin_call_grace_over_policy=apply_or_fail_missing_grace_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`force_close_order_handoff=bt_page`；`daily_short_inventory_handoff=bu_page`；`short_recall_handoff=bv_page`；`credit_usage_handoff=bw_page`；`interest_start_daycount_handoff=bx_page`；`auction_vol_handoff=y_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`st_limit_handoff=x_page`；`stamp_tax_handoff=v_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_margin_call_grace_deadline_check`；`missing_grace_rule_policy=skip`；`day_freq_proxy=margin_call_grace_deadline_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`（待预检；params.Y≠实验字母 BY；params.G≠实验字母 BY；params.N≠实验字母 BY；亦≠单字母实验 A/B/Y/Z；禁 null/holdout/跑后改口）**；**`params.by0_primary_demo` 建议 `invent_ignore_margin_call_grace_or_force_deadline`（待预检；禁与 invent_asof_leak_margin_call_grace 双挂；BY1半泄露不得升格并列主报）**；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BY0/BY1/BY2 净收益/成本质量、ΔFakeInfiniteGrace、ΔHoldableNotional、ΔOverdueForceImpact；分桶（追保宽限期时限误开 / 核对日泄露 / 宽限窗 / 时限切日窗 / 通道前 / vs A·Z·BA–BX·K·AB·Y·B·H·W·X·V·U·T·S）。  
- 自检布尔：BY2 是否 pit_by_effective_date；BY0 是否单一主报；BY1 是否仅核对日泄露；是否未与 A/Z/BA–BX/K/AB/Y/B/H/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 BY 与 A 或 B 或 Y 或 K 或 Z 或 BA–BX 或 BM 或 BT 或 BC 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BY≠单字母假设-Y；params.Y≠实验字母 BY；BY≠BM；BY≠BT；BY≠BC；BY≠BX；BY≠BW；BY≠BV；BY≠BU；BY≠BS；BY≠BO；BY≠BR；BY≠BH；带过 BX≠X/BW/BV/BU/BT/BS/BO/BR/BH…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BX 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-Y / 假设-K / 假设-W / 假设-Z / 假设-BA–BX / 假设-BM / 假设-BT / 假设-BC / 假设-BX / 假设-AB**；**是否未再改 BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-Y（集合竞价量计入日线）**；**是否未与 invent_asof_leak_margin_call_grace 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假无限宽限或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BX 及其他 A/D–BX 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-Y**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BX**；**尤其不改假设-BX；不改假设-BM**；**尤其不改假设-BT**；**尤其不改假设-BC**；**不改假设-AB**；**勿再改 BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券券池日可借量（BU）、融券提前召回（BV）、授信占用口径（BW）、融资利息起息日/计息天数（BX）、融券空头名单（K）之外，**追保通知后宽限期与强平通知时限**须按当时有效规则 PIT；不得默认永远无限宽限，或用核对日更宽长时限规则铺满。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BY** 标准件，**不改口径主线**，**不改假设 A–BX 正文**，**尤其不改假设-Y / 假设-BM / 假设-BT / 假设-BC / 假设-BX**。与实验 A/Z/BA–BX/K/AB/B/H/W/Y/X/V/U/T/S 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA–BX=两融族已冻/在途；BM=追保禁新开；BT=强平序；BC=强平闸门；BX=起息日基数；Y=集合量分母（严禁复用）；BY=追保宽限期/强平通知时限误开（BY≠A≠B≠Y≠K≠Z≠BA≠…≠BX≠BM≠BT≠BC≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AB≠W≠H≠T≠S≠U≠V≠X；带过 BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 待预检**（结论栏空；**未标纸面齐**） |
| 标准件路径 | `假设-BY-追保宽限期强平通知时限误开.md` |
| 清单序号 | 约 #82 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**margin_call_grace_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（待预检；params.Y≠实验字母 BY；params.G≠实验字母 BY；params.N≠实验字母 BY；亦≠单字母实验 A/B/Y/Z；禁 null/holdout/跑后改口）**；**by0_primary_demo 建议 invent_ignore_margin_call_grace_or_force_deadline（待预检；禁双挂 invent_asof_leak_margin_call_grace；BY1半泄露不得升格并列主报）**；锚点建议 margin_call_grace_honest=pit_by_effective_date / margin_call_grace_scope=grace_period_and_force_notice_deadline / margin_call_grace_over_policy=apply_or_fail_missing_grace_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **BY≠Y/BX/BW/BV/BU/BT/BS/BO/BR/BH/BM/BC**（及 ≠B/A/Z/BA–BX/K/AB/H/W/T/S/U/V/X）；**严禁复用假设-Y**；**尤其不改假设-Y/BM/BT/BC/BX**；**params.Y≠实验字母 BY** |
| 结论栏 | 空 |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**待预检冻结**；**params.Y≠实验字母 BY**；**params.G≠实验字母 BY**；**params.N≠实验字母 BY**；禁 null/holdout）  
2. `params.by0_primary_demo` = `invent_ignore_margin_call_grace_or_force_deadline`（**待预检冻结**；禁与 `invent_asof_leak_margin_call_grace` 双挂；BY1不升格主报）  
3. 锚点建议：`margin_call_grace_honest=pit_by_effective_date` / `margin_call_grace_scope=grace_period_and_force_notice_deadline` / `margin_call_grace_over_policy=apply_or_fail_missing_grace_rule` / `margin_channel_start=2010-03-31` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`

---

## 与 BA–BX / Y / K 撞题检查表

| 对照 | 是否撞题 | 说明 |
|------|----------|------|
| 假设-Y | **否（硬分列）** | 集合量分母 ≠ 追保时限；**BY≠Y**；**严禁复用**；**params.Y≠BY** |
| 假设-BM | **否（硬分列）** | 禁新开 ≠ 宽限天数；**BY≠BM**；不改 BM |
| 假设-BT | **否（硬分列）** | 强平序范围 ≠ 时限；**BY≠BT**；不改 BT |
| 假设-BC | **否（硬分列）** | 闸门 ≠ 宽限；**BY≠BC**；不改 BC |
| 假设-BX | **否（硬分列）** | 起息 ≠ 追保时限；**BY≠BX**；不改 BX |
| 假设-BW/BV/BU/BS/BO/BR/BH | **否** | 占用/召回/日库存/利率档/假零息/借券费/额度 ≠ 宽限 |
| 假设-BA–BN/BP/BQ/BF/BL/BB/BD/BG/Z/K/AB | **否** | 各页主病旁路；本页不重开 |
| 假设-A/B/H/W/X/V/U/T/S | **否** | 板上/旧位/退市/除权/ST板幅/印花税/过户/证管/经手 ≠ 宽限 |

---

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-03 | 新建草稿·待预检（总管线 BX 补丁已交后写 BY；选题追保宽限期/强平通知时限误开；**BY≠Y/BX/BW/BV/BU/BT/BS/BO/BR/BH/BM/BC**；primary_demo 建议=`invent_ignore_margin_call_grace_or_force_deadline`；Y/G/N/Y2 待预检；不开回测；未改 BX/BM/BT/BC/Y 及其他已齐字母；**未标纸面齐**）。 |
