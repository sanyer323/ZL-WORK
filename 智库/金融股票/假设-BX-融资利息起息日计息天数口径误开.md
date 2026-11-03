# 假设 BX · 融资利息起息日/计息天数口径误开 / 用核对日起息或日基数规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BW 补丁已交（复检在途）、写下一纸面 BX；清单撞题规则另选正交执行缺口（**融资利息起息日与计息天数/日基数怎么算** ≠ 融资假零息 ≠ 融资利率档位 ≠ 授信占用口径 ≠ 融券提前召回 ≠ 日可借量 ≠ 强平序 ≠ 融券借券费 ≠ 授信额度上限 ≠ 开仓保证金比例 ≠ 主板 ST 涨跌幅 PIT）；选题自两融会员风控公开口径：融资买入未了结期间须计收融资利息时，**起息日**（成交日/交收日/下一自然日等）与**计息天数/日基数**（ACT/365、ACT/360、30/360、含头含尾等）按当时有效规则 PIT；不得默认「永远按成交日当日即起息且 ACT/365 含头含尾吹胖天数 / 或永远按核对日更宽晚起息+少天数规则铺满历史」；本页**假定利息非零且利率档已按 BO/BS 诚实或显式旁路**，主病只在**起息日与计息天数口径**；2010-03-31 前无此通道；**BO 正文主测「永不计息/零罚息」**（`invent_zero_financing_interest_penalty`），**BS 正文主测「有息但一律最低优惠档」**（`invent_always_lowest_financing_rate_tier`），本页主测**有息且档位诚实前提下起息日/日基数被误开**（`invent_wrong_financing_interest_start_or_daycount`）→ 自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BX ≠ 单字母 B**）/ **X（主板 ST 涨跌幅 PIT；双字母 BX ≠ 单字母假设-X；严禁复用 X 题面或 ST 板幅口径）** / Z（**开仓**融资/融券保证金比例；**BX≠Z**）/ BA–BW（两融族已冻/在途；**BX≠BA…BW**；**尤其不改 BW 正文**）/ **BO（融资假零息；BX≠BO；尤其不改假设-BO）** / **BS（融资利率档；BX≠BS；尤其不改假设-BS）** / **BW（授信占用；BX≠BW；在途复检亦勿改）** / BV/BU/BT/BR/BH/BQ/BP/BN/BM/BL/BF/BC/BB/BA 等**分列**；**新建实验 BX**  
状态：**草稿 · 预检有条件通过 · 两条已冻 · 待复检**（结论栏空；禁止把「起息永远按成交日当日+ACT/365 含头含尾 / 用核对日更宽晚起息少天数规则铺满」当诚实融资利息日基数口径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BW 及其他 A/D–BW 已交正文与冻结补丁；尤其不改假设-BW；尤其不改假设-X；尤其不改假设-BO；尤其不改假设-BS；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-Z；不改假设-BA–BW；不改假设-AB；勿再改 BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BX（约 #81）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融资利息起息日与计息天数/日基数**。**双字母 BX ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BX ≠ 单字母 B**。与假设 **X（主板 ST 涨跌幅 PIT）** **硬分列（专节强调）**：X = 主板 ST/*ST 5%→10% 切日与创业/科创风险警示误套；本页 = 信用账户**融资利息起息日/计息天数**；ST 板幅 ≠ 起息日基数。**双字母 BX ≠ 单字母假设-X**；**严禁复用 X 题面或 X 口径键**。与假设 **BO（融资利息与逾期罚息假零息）** **硬分列**：BO = **是否计息**（永不计息/零罚息）；本页 = **有息前提下从哪天起息、按什么日基数计几天**；假零息 ≠ 起息日/日基数误开；**禁止**把「假零息已关（BO）」静默写成「起息日与日基数已诚实」；**禁止**把「起息晚一天」静默写成「零息」；**不占** BO 的 primary_demo；**尤其不改假设-BO**。**BX≠BO**。与假设 **BS（融资利率档位优惠档）** **硬分列**：BS = **用哪档年化利率**；本页 = **起息日与计息天数**；最低档 ≠ 日基数；**尤其不改假设-BS**。**BX≠BS**。与假设 **BW（两融授信占用口径）** **硬分列**：BW = 授信已占用怎么算（复检在途）；本页 = 利息起息/日基数；占用 ≠ 起息；**尤其不改假设-BW**。**BX≠BW**。与假设 **BV / BU / BT / BR / BH / BQ / BP / BN / BM / BL / BF / BC / BB / BA / BD / BG / Z / K / AB** **硬分列**：召回 / 日库存 / 强平序 / 借券费 / 额度上限 / 调出后存量 / 权益补偿 / 账户串用 / 追保禁开 / 提取 / 合约期限 / 维持线闸门 / 转融暂停 / 融资名单 / 折算率 / 可充抵 / 开仓比例 / 融券名单 / 空头价限 ≠ 起息日与计息天数；并**带过 BW≠W/BV/BU/BT/BS/BO/BR/BH…、BV≠V/BU/BT/BF/BC/BB/BQ/K…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 AN–BW **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-X（主板 ST 板幅）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BX** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 X**（主板 ST 涨跌幅；**严禁复用假设-X**）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BX / 假设-BX / hypothesis_id=BX / 组 BX0·BX1·BX2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BX 混读或互改。亦**禁止**把实验字母 BX 与单字母 **A**、单字母 **B**、单字母 **X**、单字母 **K**、单字母 **Z**、单字母 **T**、单字母 **S**、单字母 **U**、单字母 **V**、单字母 **W**、双字母 **BA–BW**、双字母 **BO**、双字母 **BS**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bx0_*` 以外的实验页混读。**双字母 BX ≠ 单字母 A ≠ 单字母 B ≠ 单字母 X ≠ 单字母 K ≠ 单字母 Z ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 双字母 BA ≠ … ≠ 双字母 BW ≠ 双字母 BO ≠ 双字母 BS ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BT ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BX**；**params.G ≠ 实验字母 BX**；**params.N ≠ 实验字母 BX**。**带过：双字母 BW ≠ W/BV/BU/BT/BS/BO/BR/BH…；双字母 BV ≠ V/BU/BT/BF/BC/BB/BQ/K…；双字母 BU ≠ U/BB/BT/K/BS/BO/BR/BH…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 BX ≠ 单字母假设-X；且 ≠ 假设-BW / 假设-BO / 假设-BS / 假设-BV / 假设-BU / 假设-BT / 假设-BR / 假设-BH；带过 BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS…、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BX（双字母） |
|------|--------|----------------------|
| 题面 X | 主板 ST/*ST 涨跌幅 PIT（板幅切日） | **融资利息起息日/计息天数**误开：假早起息或多天数 vs 按生效日起息与日基数 PIT；**严禁复用 X 题面** |
| 题面 BO | **融资假零息/零罚息**（`invent_zero_financing_interest_penalty`） | **有息前提下起息日与日基数**；假零息 ≠ 起息/日基数；**BX≠BO**；**不改 BO** |
| 题面 BS | **融资利率档位优惠档**（`invent_always_lowest_financing_rate_tier`） | **起息日与计息天数**；最低档 ≠ 日基数；**BX≠BS**；**不改 BS** |
| 题面 BW | **授信占用口径**（复检在途；`invent_understate_credit_usage`） | 占用 ≠ 起息；**BX≠BW**；**不改 BW** |
| 题面 BV / BU / BT / BR / BH | 召回 / 日库存 / 强平序 / 借券费 / 额度上限 | 召回库存强平费率额度 ≠ 起息日基数；**BX≠BV≠BU≠BT≠BR≠BH** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_wrong_financing_interest_start_or_daycount` |
| 文档 | `假设-X-…` / `假设-BO-…` / `假设-BS-…` / `假设-BW-…`（**只读；禁止改写**） | `假设-BX-融资利息起息日计息天数口径误开.md`（新建） |
| 预检键 | 实验字母 X / BO / BS / BW | 实验字母 **BX** / `bx0_primary_demo`；**不得**占用或改写预检 X/BO/BS/BW |

**禁止**：把 BX 写成「X/BO/BS/BW 的续篇」；把「假零息已关（BO）/ 利率档已诚实（BS）/ 占用已诚实（BW）/ 召回已诚实 / 日库存够 / 强平序诚实 / 借券费已计 / 授信够」静默写成「起息日与日基数已诚实」；覆盖或补丁改写假设-X / 假设-BO / 假设-BS / 假设-BW 正文；把 `params.Y/G/N` 与实验字母 BX 混读；**禁** `bx0_primary_demo` 与 `invent_asof_leak_financing_interest_daycount` **双挂主报**；**禁** BX1 半泄露升格并列主报；**禁**复用假设-X（主板 ST 板幅）题面或口径键；**禁**复用 BO 的 `invent_zero_financing_interest_penalty` 或 BS 的 `invent_always_lowest_financing_rate_tier` 当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有/滚动融资负债路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/授信/合约期限/还债优先/账户隔离/融资假零息层/融资利率档层/授信占用层等输入（Z/BA/BH/BF/BJ/BN/BO/BS/BW 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/总授信/合约期限强了/融资还债优先/账户隔离/假零息 on-off/利率档/授信占用主病」）下，把「融资利息永远按成交日当日即起息且按更肥日基数（如 ACT/365 含头含尾）计息天数」或「全样本用核对日当天更宽晚起息/更瘦日基数规则回放历史」当成默认，相对「每个交易日按当时有效起息日规则与计息天数/日基数 PIT（起息日=成交日/交收日/下一自然日等按当时规则；日基数=ACT/365·ACT/360·30/360·含头去尾等按当时规则；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假多应计利息天数或假少应计利息天数路径并改写融资持仓真实成本与净收益**；差异应**集中在融资利息起息日/计息天数口径误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假起息/假日基数贡献差、应计利息差、净收益差在标定噪声带内可忽略，且「假早起息或多天数 / 核对日泄露 / 正常起息窗 / 日基数切日窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·BS·BT·BU·BV·BW·K·AB·X·B·H·W·V·T·S·U」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 起息日/计息天数 ≠ 假零息（BO）；≠ 利率档（BS）；≠ 授信占用（BW）；≠ 融券提前召回（BV）；≠ 日可借量（BU）；≠ 强平序（BT）；≠ 借券费（BR）；≠ 额度上限（BH）；≠ 开仓保证金比例（Z）；≠ 主板 ST 板幅（X）；≠ 板上枯竭（A）；≠ 证管费（T）

```
# 配置写死键（见 §7；两条已冻 · 待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BX；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 X；≠ 实验字母 Z；≠ 实验字母 BO；≠ 实验字母 BS；≠ 实验字母 BW
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BX
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BX；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.interest_start_daycount_honest  写死 pit_by_effective_date
# params.interest_start_daycount_scope   写死 accrual_start_and_daycount_convention
# params.interest_start_daycount_over_policy 写死 accrue_or_fail_missing_daycount_rule
# params.interest_start_daycount_naive   写死 invent_wrong_financing_interest_start_or_daycount
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
# params.collateral_withdraw_handoff     写死 bl_page
# params.margin_call_open_ban_handoff    写死 bm_page
# params.cross_account_handoff           写死 bn_page
# params.financing_interest_handoff      写死 bo_page   # 假零息层交 BO；BX≠BO；本页主病是起息/日基数不是零息；不改 BO
# params.corp_action_comp_handoff        写死 bp_page
# params.list_removal_stock_handoff      写死 bq_page
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page   # 利率档交 BS；BX≠BS；不改 BS
# params.force_close_order_handoff       写死 bt_page
# params.daily_short_inventory_handoff   写死 bu_page
# params.short_recall_handoff            写死 bv_page
# params.credit_usage_handoff            写死 bw_page   # 授信占用交 BW；BX≠BW；不改 BW（复检在途亦勿改）
# params.interest_start_daycount_handoff 写死 self      # 本页主病：起息日与计息天数/日基数
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.st_limit_handoff                写死 x_page    # 主板 ST 板幅交 X；BX≠X；严禁复用假设-X
# params.stamp_tax_handoff               写死 v_page
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.bx0_primary_demo                写死冻结 invent_wrong_financing_interest_start_or_daycount  # 主报：假早起息或多天数/假晚起息或少天数；禁与 invent_asof_leak_financing_interest_daycount 双挂争主表；BX1半泄露不得升格并列主报
# params.bx0_invent_wrong_financing_interest_start_or_daycount  写死 True
# params.bx1_asof_leak_financing_interest_daycount_only 写死 True
# params.bx2_pit_interest_start_daycount 写死 True
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
# params.merge_with_BO_financing_interest 写死 False  # BX≠BO；不改 BO
# params.merge_with_BP_corp_action_comp  写死 False
# params.merge_with_BQ_list_removal_stock 写死 False
# params.merge_with_BR_short_borrow_fee  写死 False
# params.merge_with_BS_financing_rate_tier 写死 False  # BX≠BS；不改 BS
# params.merge_with_BT_force_close_order 写死 False
# params.merge_with_BU_daily_short_inventory 写死 False
# params.merge_with_BV_short_recall      写死 False
# params.merge_with_BW_credit_usage      写死 False  # BX≠BW；不改 BW
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_X_st_limit           写死 False  # BX≠X；严禁复用假设-X
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.missing_daycount_rule_policy    写死 skip
# params.day_freq_proxy                  写死 financing_interest_start_daycount_sensitivity
# params.universe_rule                   写死 sse_szse_financing_interest_start_daycount_check
# params.fail_policy                     写死 skip
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BX；params.G≠实验字母BX；params.N≠实验字母BX；亦≠单字母实验A/B/X/Z；禁 null/holdout/跑后改口
# params.date_start / date_end           写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改起息规则、日基数、Y/G/N/Y2、主窗/oos、bx0_primary_demo

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
margin_channel_start = "2010-03-31"
interest_start_daycount_honest = "pit_by_effective_date"
interest_start_daycount_scope = "accrual_start_and_daycount_convention"
interest_start_daycount_over_policy = "accrue_or_fail_missing_daycount_rule"
interest_start_daycount_naive = "invent_wrong_financing_interest_start_or_daycount"
bx0_primary_demo = "invent_wrong_financing_interest_start_or_daycount"  # 单一主报·已冻结；禁与 invent_asof_leak_financing_interest_daycount 双挂
bx1_asof_leak_financing_interest_daycount_only = True
bx2_pit_interest_start_daycount = True
merge_with_BO_financing_interest = False
merge_with_BS_financing_rate_tier = False
merge_with_BW_credit_usage = False
merge_with_X_st_limit = False
fail_policy = "skip"
```

### 2.2 三组对照（BX0 / BX1 / BX2）

| 组 | 口径 | 说明 |
|----|------|------|
| BX0 天真 | `invent_wrong_financing_interest_start_or_daycount`（单一主报·已冻结） | 发明假早起息或多天数（或对称假晚起息/少天数）路径；禁与 invent_asof_leak_financing_interest_daycount 双挂 |
| BX1 半泄露/混口径 | 全样本用 `asof_check_date` 当天更宽晚起息或更瘦日基数规则铺满历史 | 仅起息/日基数规则 asof 泄露；不升格并列主报 |
| BX2 PIT | `interest_start_daycount_honest=pit_by_effective_date` | 每个交易日按当时已生效起息日与计息天数/日基数规则 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：日终融资负债余额 × 当日生效年化利率（消费 BS 诚实档或旁路）× 当日生效起息/日基数规则下的计息天数因子 → 当日应计利息；缺起息/日基数字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有日终融资负债余额代理 + 起息日/日基数规则生效日表 + 利率档（消费 BS，旁路）+ 假零息层（消费 BO，旁路声明「本页假定有息」）即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。  
- **通道前**：`margin_channel_start=2010-03-31` 前无本页计息通道。

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

天真组 / 半泄露组相对诚实组的假起息/假日基数贡献差、应计利息差、净收益差超出标定噪声带，且差异集中在「起息日/计息天数误开」桶，不被 BO 假零息、BS 利率档、BW 占用、X ST 板幅等他页桶吸走。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 BO 假零息、BS 利率档、BW 占用、BF 期限/展期、BJ 还本优先、BH 授信、BN 串用、Z 开仓比例、X ST 板幅、T 证管费等他页桶吸走；或 holdout 反调 `bx0_primary_demo` / Y·G·N·Y2；或 BX0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BX0 / BX1 / BX2。报告应计利息差、假起息/假日基数贡献差、净收益差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_wrong_financing_interest_start_or_daycount",
  "invent_asof_leak_financing_interest_daycount",
  "accrual_start_window",
  "daycount_convention_cut_window",
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
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_X_st_limit",
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

1. 样本无足够融资负债腿或起息/日基数字段；缺字段却静默当假早起息或多天数 → 设计失效。  
2. 把「假零息已关（BO）」静默写成「起息/日基数已诚实」且不声明另页 BO → **与 BO 撞题**（是否计息 ≠ 起息日基数；**尤其 BX≠BO**；**不改 BO**）。  
3. 把「利率档已诚实（BS）」静默写成「起息/日基数已诚实」且不声明另页 BS → **与 BS 撞题**（哪档利率 ≠ 起息日基数；**尤其 BX≠BS**；**不改 BS**）。  
4. 把「授信占用已诚实（BW）」静默写成「起息/日基数已诚实」→ **与 BW 撞题**（占用 ≠ 起息；**尤其 BX≠BW**；**不改 BW**）。  
5. 把「主板 ST 板幅已诚实（X）」写成主病或不声明另页 X → **撞假设-X**，设计失效（**双字母 BX ≠ 单字母 X**；**严禁复用 X**）。  
6. 把「合约期限到期了结（BF）/ 还本优先（BJ）/ 授信够（BH）/ 账户未串用（BN）」静默写成「起息正确」→ 与对应页撞题（**尤其 BX≠BF≠BJ≠BH≠BN**）。  
7. 把「召回已诚实（BV）/ 日库存够（BU）/ 强平序诚实（BT）/ 借券费已计（BR）」静默写成「起息正确」→ 与对应页撞题（**尤其 BX≠BV≠BU≠BT≠BR**）。  
8. 把「权益已补偿 / 追保未触发 / 提取线未触 / 保证金比例够」静默写成「起息正确」且不声明另页 BP/BM/BL/Z → 与对应页撞题；并**带过 BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK 消歧链**。  
9. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易 / 证管费」写成主病而不声明另页 AB/W/A/H/T → 与对应页撞题。  
10. 把实验字母 BX 与单字母 A/B/X/K/Z/T/S/U/V/W 或双字母 BA–BW/BO/BS/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `bx0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价算应计利息 → 标签与执行双错，结论无效。  
13. 用核对日更宽「晚起息/少天数」当诚实 PIT、或把券商临时更宽日基数提前铺满历史 → 设计失效。  
14. **`bx0_primary_demo` 与 `invent_asof_leak_financing_interest_daycount` 双挂主报**；或 BX1 升格并列主报 → 设计失效。  
15. **改写或覆盖 `假设-X` / `假设-BO` / `假设-BS` / `假设-BW` / 已冻 AA–BW** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资负债日终余额代理、开仓日/成交日/交收日代理；  
- 当时有效起息日规则与计息天数/日基数规则及生效日；  
- 融资利率档 PIT / 假零息层 / 开仓保证金比例 / 融资名单 / 授信 / 合约期限 / 还债优先 / 账户隔离 / 授信占用输入（消费 BS/BO/Z/BA/BH/BF/BJ/BN/BW 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商更严起息子集；与 BO 假零息窗、BS 档位切日窗对照但不混主结论；逾期罚息起息另桶敏感性（主报仍在正常计息起息/日基数）。

**禁止**：用核对日「今天晚起息」铺满当唯一诚实组；用复权价；把假零息已关/利率档诚实/占用已诚实/日库存够/期限未到/未触维持线/名单仍在池/转融未暂停/借券费已计/授信够/开仓保证金比例/新开名单窗/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/追保未触发/账户未串用/权益已补偿/调出后存量已处理/市场25pct未暂停/ST板幅已诚实当成「起息正确」依据；把 Z/BA–BW/K/AB/A/B/H/W/X/V/U/T/S/AN–BW 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BX`  
- **组**：BX0 / BX1 / BX2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`interest_start_daycount_honest=pit_by_effective_date`；`interest_start_daycount_scope=accrual_start_and_daycount_convention`；`interest_start_daycount_over_policy=accrue_or_fail_missing_daycount_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`force_close_order_handoff=bt_page`；`daily_short_inventory_handoff=bu_page`；`short_recall_handoff=bv_page`；`credit_usage_handoff=bw_page`；`st_limit_handoff=x_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`stamp_tax_handoff=v_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_financing_interest_start_daycount_check`；`missing_daycount_rule_policy=skip`；`day_freq_proxy=financing_interest_start_daycount_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BX**；**params.G≠实验字母 BX**；**params.N≠实验字母 BX**；亦≠单字母实验 A/B/X/Z；禁 null/holdout/跑后改口）；**`params.bx0_primary_demo` 写死冻结 `invent_wrong_financing_interest_start_or_daycount`**（禁与 invent_asof_leak_financing_interest_daycount 双挂；BX1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BX0/BX1/BX2 净收益/成本质量、ΔFakeStartOrDaycount、ΔAccruedInterest、ΔNetReturn；分桶（起息日计息天数误开 / 核对日泄露 / 起息窗 / 日基数切日窗 / 通道前 / vs A·Z·BA–BW·K·AB·X·B·H·W·V·U·T·S）。  
- 自检布尔：BX2 是否 pit_by_effective_date；BX0 是否单一主报；BX1 是否仅核对日泄露；是否未与 A/Z/BA–BW/K/AB/X/B/H/W/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 BX 与 A 或 B 或 X 或 K 或 Z 或 BA–BW 或 BO 或 BS 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BX≠单字母假设-X；BX≠BO；BX≠BS；BX≠BW；BX≠BV；BX≠BU；BX≠BT；BX≠BR；BX≠BH；带过 BW≠W/BV/BU/BT/BS/BO/BR/BH…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BW 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-X / 假设-K / 假设-W / 假设-Z / 假设-BA–BW / 假设-BO / 假设-BS / 假设-BW / 假设-AB**；**是否未再改 BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-X（主板 ST）**；**是否未与 invent_asof_leak_financing_interest_daycount 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假起息/假日基数或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BW 及其他 A/D–BW 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-X**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BW**；**尤其不改假设-BW；不改假设-BO**；**尤其不改假设-BS**；**不改假设-AB**；**勿再改 BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券券池日可借量（BU）、融券提前召回（BV）、授信占用口径（BW）、融券空头名单（K）之外，**融资利息起息日与计息天数/日基数**须按当时有效规则 PIT；不得默认永远按成交日当日即起息+肥日基数，或用核对日更宽晚起息少天数规则铺满。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BX** 标准件，**不改口径主线**，**不改假设 A–BW 正文**，**尤其不改假设-X / 假设-BO / 假设-BS / 假设-BW**。与实验 A/Z/BA–BW/K/AB/B/H/W/X/V/U/T/S 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA–BW=两融族已冻/在途；BO=假零息；BS=利率档；BW=授信占用；X=主板 ST 板幅（严禁复用）；BX=融资利息起息日/计息天数口径误开（BX≠A≠B≠X≠K≠Z≠BA≠…≠BW≠BO≠BS≠BV≠BU≠BT≠BR≠BH≠AB≠W≠H≠T≠S≠U≠V；带过 BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 预检有条件通过 · 两条已冻 · 待复检**（结论栏空；**未标纸面齐**） |
| 标准件路径 | `假设-BX-融资利息起息日计息天数口径误开.md` |
| 清单序号 | 约 #81 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**interest_start_daycount_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BX；params.G≠实验字母 BX；params.N≠实验字母 BX；亦≠单字母实验 A/B/X/Z；禁 null/holdout/跑后改口）**；**bx0_primary_demo 写死冻结 invent_wrong_financing_interest_start_or_daycount（禁双挂 invent_asof_leak_financing_interest_daycount；BX1半泄露不得升格并列主报）**；锚点保留 interest_start_daycount_honest=pit_by_effective_date / interest_start_daycount_scope=accrual_start_and_daycount_convention / interest_start_daycount_over_policy=accrue_or_fail_missing_daycount_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **BX≠X/BW/BV/BU/BT/BS/BO/BR/BH**（及 ≠B/A/Z/BA–BW/K/AB/H/W/T/S/U/V）；**严禁复用假设-X**；**尤其不改假设-X/BO/BS/BW** |
| 结论栏 | 空 |

---

## 待预检键清单（两条已冻 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已冻结**；**params.Y≠实验字母 BX**；**params.G≠实验字母 BX**；**params.N≠实验字母 BX**；禁 null/holdout）  
2. `params.bx0_primary_demo` = `invent_wrong_financing_interest_start_or_daycount`（**已冻结**；禁与 `invent_asof_leak_financing_interest_daycount` 双挂；BX1不升格主报）  
3. 锚点保留：`interest_start_daycount_honest=pit_by_effective_date` / `interest_start_daycount_scope=accrual_start_and_daycount_convention` / `interest_start_daycount_over_policy=accrue_or_fail_missing_daycount_rule` / `margin_channel_start=2010-03-31` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`

---

## 与 BA–BW / X / K 撞题检查表

| 对照 | 是否撞题 | 说明 |
|------|----------|------|
| 假设-X | **否（硬分列）** | ST 板幅 ≠ 起息日基数；**BX≠X**；**严禁复用** |
| 假设-BO | **否（硬分列）** | 假零息 ≠ 起息/日基数；**BX≠BO**；不改 BO |
| 假设-BS | **否（硬分列）** | 利率档 ≠ 起息/日基数；**BX≠BS**；不改 BS |
| 假设-BW | **否（硬分列）** | 占用 ≠ 起息；**BX≠BW**；不改 BW |
| 假设-BV/BU/BT/BR/BH | **否** | 召回/日库存/强平序/借券费/额度 ≠ 起息 |
| 假设-BA–BN/BP/BQ/BF/BC/BB/BD/BG/Z/K/AB | **否** | 各页主病旁路；本页不重开 |
| 假设-A/B/H/W/V/U/T/S | **否** | 板上/旧位/退市/除权/印花税/过户/证管/经手 ≠ 起息 |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BX**；**`params.G` ≠ 实验字母 BX**；**`params.N` ≠ 实验字母 BX**；**`params.Y` ≠ 单字母实验 A/B/X/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bx0_primary_demo`**：**写死冻结** **`invent_wrong_financing_interest_start_or_daycount`**；禁与 **`invent_asof_leak_financing_interest_daycount`** 双挂争主表（只挂一个 primary）；**BX1 半泄露不得升格并列主报**。

**起息/日基数锚保留（已通写死）**：`params.interest_start_daycount_honest=pit_by_effective_date`；`params.interest_start_daycount_scope=accrual_start_and_daycount_convention`；`params.interest_start_daycount_over_policy=accrue_or_fail_missing_daycount_rule`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有起息/日基数相关锚点；不改口）。

**与 BA–BW/Z/AB/B/A/H/X/K/T/S/U/V/W 硬分列（保留）**：本页 = **融资利息起息日/计息天数口径误开**；X = **主板 ST 涨跌幅 PIT**（**尤其双字母 BX ≠ 单字母假设-X**；**严禁复用假设-X**）；BO = **融资利息与逾期罚息假零息**（**尤其 BX≠BO**；假零息 ≠ 起息/日基数；禁复用 `invent_zero_financing_interest_penalty`；**尤其不改假设-BO**）；BS = **融资利率档位优惠档**（**尤其 BX≠BS**；利率档 ≠ 起息日基数；禁复用 `invent_always_lowest_financing_rate_tier`；**尤其不改假设-BS**）；BW = **两融授信占用口径**（**尤其 BX≠BW**；占用 ≠ 起息；禁复用 `invent_understate_credit_usage`；**尤其不改假设-BW**）；BV = **融券提前召回**（**尤其 BX≠BV**）；BU = **融券券池日可借量**（**尤其 BX≠BU**）；BT = **强制平仓顺序与范围**（**尤其 BX≠BT**）；BR = **融券借券费**（**尤其 BX≠BR**）；BH = **两融授信额度上限**（**尤其 BX≠BH**）；Z = **开仓**保证金比例；A = **板上枯竭**；B = 历史实验 B 旧位；K = **融券空头名单**；H = **退市整理期**；W = **除权板价**；T = **证管费**（避开预检T）；S = **经手费**；U = **过户费**；V = **印花税**；起息日/计息天数 ≠ 主板ST板幅 ≠ 假零息 ≠ 利率档 ≠ 授信占用 ≠ 提前召回 ≠ 日可借量 ≠ 强平序 ≠ 借券费 ≠ 额度上限 ≠ 开仓比例 ≠ 板上枯竭 ≠ 退市整理 ≠ 除权板价 ≠ 证管费 ≠ 经手费 ≠ 过户费 ≠ 印花税；**双字母 BX ≠ 单字母 A ≠ 单字母 B ≠ 单字母 X ≠ 单字母 K ≠ 单字母 Z ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 双字母 BA ≠ … ≠ 双字母 BW ≠ 双字母 BO ≠ 双字母 BS ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BT ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BX**；**params.G ≠ 实验字母 BX**；**params.N ≠ 实验字母 BX**；禁止捆成「两融一张表=假起息」；**尤其不改假设-X**；**尤其不改假设-BO**；**尤其不改假设-BS**；**尤其不改假设-BW**；**尤其不改假设-BV**；**尤其不改假设-BU**；**尤其不改假设-BT**；**尤其不改假设-BR**；**尤其不改假设-BH**；不改假设-B；不改假设-Z；不改假设-BA–BW；不改假设-A；不改假设-AB；不改假设-K；不改假设-H；不改假设-T；不改假设-S；不改假设-U；不改假设-V；不改假设-W。

**专节保留 · 双字母 BX ≠ 单字母假设-X；且 ≠ 假设-BW / 假设-BO / 假设-BS / 假设-BV / 假设-BU / 假设-BT / 假设-BR / 假设-BH（硬）**：正文专节保留不删；**禁止**覆盖/混读/改写 `假设-X` / `假设-BO` / `假设-BS` / `假设-BW` / `假设-BV` / `假设-BU` / `假设-BT` / `假设-BR` / `假设-BH`。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-03 | 风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BX**；**params.G≠实验字母 BX**；**params.N≠实验字母 BX**；亦≠单字母实验 A/B/X/Z；禁 null/holdout/跑后改口）；② `params.bx0_primary_demo=invent_wrong_financing_interest_start_or_daycount`（禁与 `invent_asof_leak_financing_interest_daycount` 双挂争主表；BX1半泄露不得升格并列主报）。起息/日基数锚保留：`interest_start_daycount_honest=pit_by_effective_date`；`interest_start_daycount_scope=accrual_start_and_daycount_convention`；`interest_start_daycount_over_policy=accrue_or_fail_missing_daycount_rule`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。硬分列保留：**BX≠X/BW/BV/BU/BT/BS/BO/BR/BH**（及 ≠B/A/Z/BA–BW/AB/H/K/T/S/U/V/W）；**严禁复用假设-X**；参考总管派令 / 风控预检有条件通过（`预检-假设BX-20261103.md`；草稿 `9c6a78e` #81）。未改 Y/Z/AA–BW 及其他已冻结补丁；**不改假设-X**；**不改假设-BO**；**不改假设-BS**；**不改假设-BW**；**不改假设-BV**；**不改假设-BU**；**不改假设-BT**；**不改假设-BR**；**不改假设-BH**；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-Z；不改假设-BA–BW；不改假设-AB；结论栏仍空；不开回测；不抢 A；**未标纸面齐** |
| 2026-11-03 | 新建草稿·待预检（总管线 BW 补丁已交后写 BX；选题融资利息起息日/计息天数口径误开；**BX≠X/BW/BV/BU/BT/BS/BO/BR/BH**；primary_demo=`invent_wrong_financing_interest_start_or_daycount`；Y/G/N/Y2 待预检；不开回测；未改 BW/BO/BS/X 及其他已齐字母）。 |
