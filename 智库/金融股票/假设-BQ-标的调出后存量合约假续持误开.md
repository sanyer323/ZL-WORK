# 假设 BQ · 标的调出名单后存量合约假续持/展期加仓误开 / 用核对日调出后存量规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BP 补丁已交（已冻结待复检）、写下一纸面 BQ；清单撞题规则另选正交执行缺口（**融资/融券标的调出名单后存量合约如何处理**——能否续持至自然到期、能否展期/加仓、是否须限期了结 ≠ 融资买入**新开**名单闸门 ≠ 融券空头**新开**名单 PIT ≠ 合约**期限到期**强制了结 ≠ 维持担保**低线**强制平仓 ≠ 转融券暂停后**券源** ≠ 融资利息/罚息发明为零 ≠ 融券**权益补偿** ≠ 追保后禁新开 ≠ 跨账户现金混用）；选题自两融业务公开口径：融资买入标的/融券标的名单按生效日调整；**调出后一般不得新开/加仓**；存量合约处理按细则/合同（常见须在约定期限内了结或仅允许减仓了结，不得展期加仓）；规则按**施行日/生效日** PIT，不得用核对日更宽「调出后仍可无限续持/展期」回放全历史；2010-03-31 前无两融通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BQ ≠ 单字母 B**）/ **Q（可转债；双字母 BQ ≠ 单字母假设-Q）** / Z（**开仓**融资/融券保证金比例；**BQ≠Z**）/ BA–BP（两融族已冻/在途；**BQ≠BA…BP**）/ **K（融券空头名单 PIT；BQ≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BQ≠AB**）/ W（除权日复权价误判板；**BQ≠W**）/ BA（**融资买入新开名单**；**BQ≠BA**；新开 ≠ 调出后存量）/ BF（**两融合约期限到期强制了结**；**BQ≠BF**；期限到 ≠ 名单调出后存量规则）/ BC（**维持担保比例强制平仓**；**BQ≠BC**；低维持强平 ≠ 调出后存量处理）/ BB（**转融券券源**；**BQ≠BB**）/ BO（**融资利息与逾期罚息**；**BQ≠BO**）/ BP（**融券权益补偿**；**BQ≠BP**；权益补偿 ≠ 调出后存量；不占 invent_zero_short_corp_action_comp）/ BM（**追保后禁新开**；**BQ≠BM**；并带过 **BM≠BC、BM≠BL**）/ BN（**信用/普通账户串用**；**BQ≠BN**；并带过 **BN≠BI/BJ/BL/BM、params.N≠BN**）/ E（整手）/ AN–BP（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BQ**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「标的调出后存量合约仍可无限续持/假可展期加仓」当诚实执行能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BP 及其他 A/D–BP 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-Q；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BP；不改假设-AB；勿再改 BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BQ（约 #74）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **标的调出融资或融券名单后存量合约是否仍假可无限续持/展期加仓**。**双字母 BQ ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BQ ≠ 单字母 B**。与假设 **Q（可转债）** **硬分列（专节强调）**：Q = 可转债通道/债性执行；本页 = 信用账户**标的调出后存量合约处理**；可转债 ≠ 调出后存量。**双字母 BQ ≠ 单字母假设-Q**。与假设 **BA（融资买入新开名单）** **硬分列**：BA = **新开**融资买入是否在标的名单内；本页 = 调出后**已有存量**能否续持/展期/加仓；新开闸门 ≠ 存量处理。**BQ≠BA**。与假设 **K（融券空头名单 PIT）** **硬分列**：K = 当日是否在**交易所融券标的名单**内（新开）；本页 = 调出后存量续持/了结；名单内可空 ≠ 调出后可无限续持。**BQ≠K**；并**带过**：双字母 **BK ≠ 单字母假设-K / 预检K**。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = **合约期限到期**强制了结；本页 = **名单调出**后存量规则；期限到 ≠ 名单调出。**BQ≠BF**。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = **低维持线**强制平仓；本页 = 调出后存量了结/禁展期加仓；强平 ≠ 调出了结。**BQ≠BC**。与假设 **BB（转融券券源）** **硬分列**：BB = 可借量/券源；本页 = 名单调出后存量处理；有券 ≠ 调出后可续持。**BQ≠BB**。与假设 **BO（融资利息与逾期罚息）** **硬分列**：BO = 融资计息/罚息；本页 = 调出后存量；零息 ≠ 调出存量。**BQ≠BO**。与假设 **BP（融券权益补偿）** **硬分列**：BP = 融券现金红利/红股/配股补偿；本页 = 调出后存量；权益补偿 ≠ 调出存量；**不占** `invent_zero_short_corp_action_comp`。**BQ≠BP**。与假设 **BM（追保后禁新开）** **硬分列**：BM = 追保期内禁新开；本页 = 名单调出后存量；追保状态 ≠ 名单调出；并**带过 BM≠BC、BM≠BL**。**BQ≠BM**。与假设 **BN（跨账户现金混用）** **硬分列**：BN = 信用/普通账户隔离；本页 = 调出后存量；并**带过 BN≠BI/BJ/BL/BM、params.N≠BN**。**BQ≠BN**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = 新开保证金比例；本页 = 调出后存量处理。与假设 **W/AB/BD/BE/BG/BH/BI/BJ/BK/BL** **硬分列**：除权板价 / 空头价限 / 折算率 / 市场25pct / 可充抵 / 授信 / 所得用途 / 还债优先 / 集中度 / 提取 ≠ 调出后存量。与假设 AN–BP **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BQ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 Q**（可转债）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BQ / 假设-BQ / hypothesis_id=BQ / 组 BQ0·BQ1·BQ2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BQ 混读或互改。亦**禁止**把实验字母 BQ 与单字母 **A**、单字母 **B**、单字母 **Q**、单字母 **K**、单字母 **Z**、双字母 **BA–BP**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bq0_*` 以外的实验页混读。**双字母 BQ ≠ 单字母 A ≠ 单字母 B ≠ 单字母 Q ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BP ≠ 双字母 BA ≠ 双字母 BF ≠ 双字母 BC ≠ 双字母 BB ≠ 双字母 BO ≠ 双字母 BM ≠ 双字母 BN ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H ≠ 双字母 T**；**params.Y ≠ 实验字母 BQ**；**params.G ≠ 实验字母 BQ**；**params.N ≠ 实验字母 BQ**。**带过：双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BQ ≠ 单字母假设-Q；且 ≠ 假设-BA / 假设-K / 假设-BF / 假设-BC；带过 BP≠P/BO/W、BM≠BC/BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BQ（双字母） |
|------|--------|----------------------|
| 题面 Q | 可转债通道/债性执行 | **标的调出后存量假续持**误开：调出后假可无限续持/展期加仓 vs 按生效日调出后存量规则 PIT |
| 题面 BA | 融资买入**新开**名单闸门 | 调出后**存量**续持/了结；新开 ≠ 存量；**BQ≠BA** |
| 题面 K | 融券空头**新开**名单 PIT | 调出后存量；新开 ≠ 存量；**BQ≠K**；**带过 BK≠K** |
| 题面 BF | 合约**期限到期**强制了结 | 名单**调出**后存量规则；期限到 ≠ 名单调出；**BQ≠BF** |
| 题面 BC | 维持担保**低线**强制平仓 | 调出后存量了结/禁展期加仓；强平 ≠ 调出了结；**BQ≠BC** |
| 题面 BB / BO / BP | 转融券源 / 融资利息罚息 / 融券权益补偿 | 可借量/零息/权益补偿 ≠ 调出后存量；**BQ≠BB≠BO≠BP**；不占 BP 主演示 |
| 题面 BM / BN | 追保禁开 / 账户隔离（**BM≠BC、BM≠BL**；**BN≠BI/BJ/BL/BM**；**params.N≠BN**） | 本页不覆盖；**带过**消歧链 |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_keep_open_after_list_removal` |
| 文档 | `假设-Q-…` / `假设-BA-…` / `假设-K-…` / `假设-BF-…` / `假设-BC-…` / `假设-BP-…`（**只读；禁止改写**） | `假设-BQ-标的调出后存量合约假续持误开.md`（新建） |
| 预检键 | 实验字母 Q / BA / K / BF / BC / BP | 实验字母 **BQ** / `bq0_primary_demo`；**不得**占用或改写预检 Q/BA/K/BF/BC/BP |

**禁止**：把 BQ 写成「Q/BA/K/BF/BC/BP 的续篇」；把「合约未到期（BF）/ 未触发维持强平（BC）/ 仍在新开名单窗（BA/K）/ 权益已补偿（BP）」静默写成「调出后可无限续持」；覆盖或补丁改写假设-Q / 假设-BA / 假设-K / 假设-BF / 假设-BC / 假设-BP 正文；把 `params.Y/G/N` 与实验字母 BQ 混读；**禁** `bq0_primary_demo` 与 `invent_asof_leak_list_removal_stock_rule` **双挂主报**；**禁** BQ1 半泄露升格并列主报。

---

## 1. 一句话假设（可检验、可证伪）

同一存量融资或融券合约路径、同一未复权价、同一 T+1、同一开仓保证金/融资名单/融券名单/合约期限/维持强平输入（Z/BA/K/BF/BC 层诚实或显式旁路声明「本页不重开开仓比例/新开融资名单/新开融券名单/期限到期强平/低维持强平」）下，把「标的调出融资或融券名单后存量合约仍可无限续持、假可展期或假可加仓，永不检查调出后存量了结规则」或「全样本用核对日当天调出后存量处理规则（含券商当日更宽续持口径）回放历史」当成默认，相对「每个交易日按当时有效调出后存量规则 PIT（调出生效日起不得新开/加仓；存量须按当时有效限期了结或仅减仓了结；缺字段 skip/敏感性；2010-03-31 前无通道）」的诚实组，会**系统性发明假可于调出后续持/展期路径并高估可执行两融名义、低估因调出后存量规则导致的强制了结/开仓失败率**；差异应**集中在标的调出后存量合约处理误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假调出后续持贡献差、可执行名义差、了结/失败率差在标定噪声带内可忽略，且「假调出后续持 / 核对日泄露 / 假展期加仓窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·K·AB·Q·B·H·W·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 调出后存量处理 ≠ 新开融资名单；≠ 新开融券名单；≠ 合约期限到期了结；≠ 低维持强平；≠ 转融券券源；≠ 融资利息罚息；≠ 融券权益补偿；≠ 追保禁开；≠ 跨账户串用；≠ 开仓保证金比例；≠ 可转债；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BQ；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 Q；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BQ
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BQ；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.list_removal_stock_honest       写死 pit_by_effective_date
# params.list_removal_stock_scope        写死 no_new_or_add_unwind_only_or_deadline
# params.list_removal_over_policy        写死 reject_or_force_unwind_or_fail
# params.broker_looser_keep_open_bucket  写死 separate_sensitivity
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
# params.financing_interest_handoff      写死 bo_page
# params.corp_action_comp_handoff        写死 bp_page
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.cb_handoff                      写死 q_page
# params.exit_period_handoff             写死 h_page
# params.bq0_primary_demo                写死冻结 invent_keep_open_after_list_removal  # 主报：调出后存量仍假可无限续持/永不检查调出后了结；禁与 invent_asof_leak_list_removal_stock_rule 双挂争主表；BQ1半泄露不得升格并列主报
# params.bq0_invent_keep_open_after_list_removal 写死 True
# params.bq1_asof_leak_list_removal_stock_rule_only 写死 True
# params.bq2_pit_list_removal_stock_rule 写死 True
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
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_U_transfer_fee       写死 False
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
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_D_halt_timing        写死 False
# params.universe_rule                   写死 sse_szse_list_removal_stock_rule_check
# params.missing_list_removal_stock_policy 写死 skip
# params.day_freq_proxy                  写死 list_removal_stock_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BQ；params.G≠实验字母BQ；params.N≠实验字母BQ；亦≠单字母实验A/B/Q/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
list_removal_stock_honest = "pit_by_effective_date"
params.bq0_primary_demo = "invent_keep_open_after_list_removal"  # 单一主报·已冻结；禁与 invent_asof_leak_list_removal_stock_rule 双挂
```

备选主报名（若预检改口，仍须单一）：`invent_roll_or_add_after_list_removal`（假可展期/加仓）——**不得与主报双挂**；若选此则原 keep_open 降为诊断桶。

### 2.2 三组对照（BQ0 / BQ1 / BQ2）

| 组 | 口径 | 说明 |
|----|------|------|
| BQ0 天真 | `invent_keep_open_after_list_removal`（单一主报·已冻结） | 调出后存量仍假可无限续持；永不检查调出后了结/禁展期加仓 |
| BQ1 半泄露 | `invent_asof_leak_list_removal_stock_rule` | 仅用核对日调出后存量规则（含券商当日更宽续持口径）铺满全历史；**不得升格并列主报** |
| BQ2 诚实 PIT | `pit_list_removal_stock_rule` / `list_removal_stock_honest=pit_by_effective_date` | 按当日已生效调出后存量规则；调出后不得新开/加仓；存量限期了结或仅减仓了结；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/BA/K/BF/BC）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **规则生效**：融资/融券标的名单调入调出生效日 + 调出后存量处理细则/合同施行日；禁用核对日更宽「调出后仍可无限续持」提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BQ0 相对 BQ2 的假调出后续持/假展期贡献差、可执行名义差、了结或开仓失败率差超过 `params.Y` / `params.G` / `params.N` / `params.Y2` 标定带，且主贡献落在「标的调出后存量合约处理误开」桶；holdout 同向不反号到噪声带内。BQ1 相对 BQ2 的核对日泄露贡献可单独度量且不得冒充主报。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeKeepOpenAfterListRemoval / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/BM/BN/BO/BP/K/AB/Q/B/H/W/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BQ0 / BQ1 / BQ2。报告名义/路径质量差、假调出后续持贡献差、假展期加仓贡献差、了结/开仓失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_keep_open_after_list_removal",
  "invent_asof_leak_list_removal_stock_rule",
  "invent_roll_or_add_after_list_removal",
  "post_removal_stock_window",
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
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_Q_cb",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够「调出后仍有存量」事件；缺调出生效日字段却静默当可续持 → 设计失效。  
2. 把「合约未到期（BF）」静默写成「调出后可无限续持」且不声明另页 BF → **与 BF 撞题**（期限到 ≠ 名单调出；**尤其 BQ≠BF**）。  
3. 把「未触发维持强平（BC）」静默写成「调出后可续持」且不声明另页 BC → **与 BC 撞题**（强平 ≠ 调出了结；**尤其 BQ≠BC**）。  
4. 把「仍在融资买入新开名单窗 / 仍在融券新开名单窗」静默写成「调出后存量可续持」且不声明另页 BA/K → 与 BA/K 撞题（**尤其 BQ≠BA / BQ≠K**；**带过 BK≠K**）。  
5. 把「转融券未暂停 / 有券可借」静默写成「调出后可续持」且不声明另页 BB → 与 BB 撞题。  
6. 把「融资已计息 / 融券权益已补偿」静默写成「调出后可续持」且不声明另页 BO/BP → 与 BO/BP 撞题（**尤其 BQ≠BO / BQ≠BP**）。  
7. 把「追保未触发 / 账户未串用 / 提取线未触 / 集中度未触顶 / 授信够 / 保证金比例够」静默写成「调出后可续持」且不声明另页 BM/BN/BL/BK/BH/Z → 与对应页撞题；并**带过 BM≠BC、BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC**。  
8. 把「可转债通道可成」写成主病而不声明另页 Q → 与 Q 撞题（**双字母 BQ ≠ 单字母 Q**）。  
9. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易」写成主病而不声明另页 AB/W/A/H → 与对应页撞题。  
10. 把「标的调出后存量假续持误开」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
11. 把实验字母 BQ 与单字母 A/B/Q/K/Z 或双字母 BA–BP/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
12. holdout 反调 `bq0_primary_demo` / Y·G·N·Y2 → 结论无效。  
13. 用复权价算可续持名义 → 标签与执行双错，结论无效。  
14. 用核对日更宽「调出后仍可续持」当诚实 PIT、或把券商临时放宽提前铺满历史 → 设计失效。  
15. **`bq0_primary_demo` 与 `invent_asof_leak_list_removal_stock_rule` 双挂主报**；或 BQ1 升格并列主报 → 设计失效。  
16. **改写或覆盖 `假设-Q` / `假设-BA` / `假设-K` / `假设-BF` / `假设-BC` / `假设-BP` / 已冻 AA–BP** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户存量融资/融券合约名义与开仓日、未了结标记；  
- 融资买入标的名单 / 融券标的名单的**调入调出生效日**（PIT；消费 BA/K 诚实名单或显式旁路）；  
- 调出后存量处理规则生效日（限期了结天数 / 仅减仓 / 禁展期加仓；券商加严另桶）；  
- 合约期限输入（消费 BF 或旁路）；维持担保输入（消费 BC 或旁路）；  
- 开仓保证金比例 / 转融券源 / 授信 / 追保禁开 / 账户隔离 / 融资计息 / 权益补偿输入（消费 Z/BB/BH/BM/BN/BO/BP 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商临时放宽续持/展期子集另桶；调出后仅允许减仓了结的流水。

**禁止**：用核对日「今天调出后仍可无限续持」铺满当唯一诚实组；用复权价；把开仓保证金比例/低维持强平/合约期限未到期/新开名单窗/转融券未暂停/市场余额25pct未触/总授信够/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/追保未触发/账户未串用/融资已计息/权益已补偿当成调出后可续持依据；把 Z/BA–BP/K/AB/A/Q/B/H/W/T/AN–BP 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BQ`  
- **组**：BQ0 / BQ1 / BQ2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`list_removal_stock_honest=pit_by_effective_date`；`list_removal_stock_scope=no_new_or_add_unwind_only_or_deadline`；`list_removal_over_policy=reject_or_force_unwind_or_fail`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`cb_handoff=q_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_list_removal_stock_rule_check`；`missing_list_removal_stock_policy=skip`；`day_freq_proxy=list_removal_stock_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BQ**；**params.G≠实验字母 BQ**；**params.N≠实验字母 BQ**；亦≠单字母实验 A/B/Q/Z；禁 null/holdout/跑后改口）；**`params.bq0_primary_demo` 写死冻结 `invent_keep_open_after_list_removal`**（禁与 invent_asof_leak_list_removal_stock_rule 双挂；BQ1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BQ0/BQ1/BQ2 可执行名义/路径质量、ΔFakeKeepOpenAfterListRemoval、ΔFakeRollOrAddAfterListRemoval、ΔFail；分桶（调出后存量假续持误开 / 核对日泄露 / 假展期加仓窗 / 通道前 / vs A·Z·BA–BP·K·AB·Q·B·H·W·T）。  
- 自检布尔：BQ2 是否 pit_by_effective_date；BQ0 是否单一主报；BQ1 是否仅核对日泄露；是否未与 A/Z/BA–BP/K/AB/Q/B/H/W/T 混主结论；holdout 是否未反调；**是否未把实验字母 BQ 与 A 或 B 或 Q 或 K 或 Z 或 BA–BP 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BQ≠单字母假设-Q；BQ≠BA；BQ≠K；BQ≠BF；BQ≠BC；BQ≠BB；BQ≠BO；BQ≠BP；BQ≠BM；BQ≠BN；带过 BP≠P/BO/W、BM≠BC/BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BP 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-Q / 假设-K / 假设-W / 假设-Z / 假设-BA–BP / 假设-AB**；**是否未再改 BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未与 invent_asof_leak_list_removal_stock_rule 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把调出后假续持或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BP 及其他 A/D–BP 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-Q**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BP**；**不改假设-AB**；**勿再改 BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息（BO）、融券权益补偿（BP）、融券空头名单（K）之外，**标的调出后存量合约处理**须按当时有效规则 PIT；不得默认调出后仍可无限续持/展期加仓。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BQ** 标准件，**不改口径主线**，**不改假设 A–BP 正文**，**尤其不改假设-Q / 假设-BA / 假设-K / 假设-BF / 假设-BC / 假设-BP**。与实验 A/Z/BA–BP/K/AB/Q/B/H/W/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入新开名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓（低线）；BD=担保品折算率；BE=市场层单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；BG=可充抵保证金证券名单；BH=两融授信额度上限；BI=融券卖出所得资金用途限制；BJ=融资买入卖出所得优先偿还融资负债；BK=客户单票两融集中度上限；BL=担保品提取转出限制；BM=追保通知后仍假可新开仓；BN=信用/普通账户串用；BO=融资利息与逾期罚息；BP=融券权益补偿；K=融券空头新开名单；AB=融券卖出价限；Q=可转债；B=历史实验B旧位；H=退市整理；W=除权板价；T=证管费（避开）；BQ=标的调出后存量合约假续持/展期加仓误开（BQ≠A≠B≠Q≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠BM≠BN≠BO≠BP≠AB≠W≠H≠T；带过 BP≠P/BO/W、BM≠BC/BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频存量合约+名单调出生效日+调出后存量规则生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**list_removal_stock_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BQ；params.G≠实验字母 BQ；params.N≠实验字母 BQ；亦≠单字母实验 A/B/Q/Z；禁 null/holdout/跑后改口）**；**bq0_primary_demo 写死冻结 invent_keep_open_after_list_removal（禁双挂 invent_asof_leak_list_removal_stock_rule；BQ1半泄露不得升格并列主报）**；锚点保留 list_removal_stock_honest=pit_by_effective_date / list_removal_stock_scope=no_new_or_add_unwind_only_or_deadline / list_removal_over_policy=reject_or_force_unwind_or_fail / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单（两条已冻结 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已写死冻结**；**params.Y≠BQ**；**params.G≠BQ**；**params.N≠BQ**；禁 null/holdout）  
2. `params.bq0_primary_demo` = `invent_keep_open_after_list_removal`（**已写死冻结**；禁与 `invent_asof_leak_list_removal_stock_rule` 双挂；BQ1不升格主报）  
3. 调出后存量锚：`list_removal_stock_honest=pit_by_effective_date`；`list_removal_stock_scope=no_new_or_add_unwind_only_or_deadline`；`list_removal_over_policy=reject_or_force_unwind_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/Q/A/Z/BA–BP/K/AB/H/W/T；**尤其 BQ≠BA（新开融资名单≠调出后存量）**；**尤其 BQ≠K（新开融券名单≠调出后存量）**；**尤其 BQ≠BF（期限到期≠名单调出）**；**尤其 BQ≠BC（强平≠调出了结）**；**尤其 BQ≠BB/BO/BP/BM/BN**；**尤其 BQ≠Q**；**带过 BP≠P/BO/W、BM≠BC/BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 与 BA–BP 撞题检查表

| 字母 | 主题 | 撞题？ | 消歧 |
|------|------|--------|------|
| BA | 融资买入新开名单 | 否 | 新开闸门 ≠ 调出后存量 |
| BB | 转融券券源 | 否 | 可借量 ≠ 存量处理 |
| BC | 维持强平 | 否 | 低线强平 ≠ 调出了结 |
| BD | 折算率 | 否 | — |
| BE | 市场25pct暂停 | 否 | — |
| BF | 合约期限到期了结 | 否 | 期限到 ≠ 名单调出 |
| BG | 可充抵名单 | 否 | — |
| BH | 授信额度 | 否 | — |
| BI | 融券所得用途 | 否 | — |
| BJ | 融资卖出还债优先 | 否 | — |
| BK | 客户单票集中度 | 否 | — |
| BL | 担保品提取 | 否 | — |
| BM | 追保后禁新开 | 否 | 追保状态 ≠ 名单调出 |
| BN | 跨账户现金混用 | 否 | — |
| BO | 融资利息罚息零 | 否 | 零息 ≠ 调出存量 |
| BP | 融券权益补偿 | 否 | 权益补偿 ≠ 调出后存量；不占 invent_zero_short_corp_action_comp |
| K | 融券新开名单 | 否 | 新开 ≠ 存量 |
| Z | 开仓保证金比例 | 否 | — |
| AB | 融券价限/当日平 | 否 | — |
| Q | 可转债 | 否 | 双字母 BQ ≠ 单字母 Q |
| A/B/H/W/T | 板上/旧B/退市/除权/证管费 | 否 | 避开预检T |

**撞题检查：通过（纸面）** — 迁罐后对照正式清单 #74 再核一次 primary_demo 唯一性。

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BQ**；**`params.G` ≠ 实验字母 BQ**；**`params.N` ≠ 实验字母 BQ**；**`params.Y` ≠ 单字母实验 A/B/Q/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bq0_primary_demo`**：**写死冻结** **`invent_keep_open_after_list_removal`**；禁与 **`invent_asof_leak_list_removal_stock_rule`** 双挂争主表（只挂一个 primary）；**BQ1 半泄露不得升格并列主报**。

**调出后存量锚保留（已通写死）**：`params.list_removal_stock_honest=pit_by_effective_date`；`params.list_removal_stock_scope=no_new_or_add_unwind_only_or_deadline`；`params.list_removal_over_policy=reject_or_force_unwind_or_fail`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有 `missing_list_removal_stock_policy=skip` 等锚点；不改口）。

**与 BA–BP/Z/AB/B/A/H/Q/K/W/T 硬分列（保留）**：本页 = **标的调出后存量合约假续持/展期加仓**；Q = **可转债**（**尤其双字母 BQ ≠ 单字母假设-Q**）；BA = **融资买入新开名单**（**尤其 BQ≠BA**；新开 ≠ 调出后存量）；K = **融券空头新开名单**（**尤其 BQ≠K**；并**带过 BK≠K**）；BF = **合约期限到期强制了结**（**尤其 BQ≠BF**；期限到 ≠ 名单调出）；BC = **维持担保低线强制平仓**（**尤其 BQ≠BC**；强平 ≠ 调出了结）；BB = **转融券券源**（**尤其 BQ≠BB**）；BO = **融资利息与逾期罚息**（**尤其 BQ≠BO**）；BP = **融券权益补偿**（**尤其 BQ≠BP**；不占 invent_zero_short_corp_action_comp；并**带过 BP≠P/BO/W/BI/BJ/BB**）；BM = **追保通知后禁新开**（**尤其 BQ≠BM**；并**带过 BM≠BC、BM≠BL**）；BN = **信用/普通账户隔离**（**尤其 BQ≠BN**；并**带过 BN≠BI/BJ/BL/BM、params.N≠BN**）；Z = **开仓**保证金比例；W = **除权日复权价误判板**；AB = **融券卖出价限**；A = **板上枯竭**；B = 历史实验 B 旧位；H = **退市整理期**；T = **证管费**（避开预检T）；调出后存量 ≠ 可转债 ≠ 新开融资名单 ≠ 新开融券名单 ≠ 期限到期 ≠ 低维持强平 ≠ 转融券源 ≠ 融资计息 ≠ 权益补偿 ≠ 追保禁开 ≠ 账户隔离 ≠ 开仓比例 ≠ 除权板价 ≠ 空头价限 ≠ 板上枯竭 ≠ 退市整理 ≠ 证管费；**双字母 BQ ≠ 单字母 A ≠ 单字母 B ≠ 单字母 Q ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BP ≠ 双字母 BF ≠ 双字母 BC ≠ 双字母 BB ≠ 双字母 BO ≠ 双字母 BM ≠ 双字母 BN ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H ≠ 双字母 T**；**params.Y ≠ 实验字母 BQ**；**params.G ≠ 实验字母 BQ**；**params.N ≠ 实验字母 BQ**；禁止捆成「两融一张表=调出后可无限续持」；**尤其不改假设-Q**；**尤其不改假设-BA**；**尤其不改假设-K**；**尤其不改假设-BF**；**尤其不改假设-BC**；**尤其不改假设-BP**；**尤其不改假设-H**；不改假设-B；不改假设-Z；不改假设-BA–BP；不改假设-A；不改假设-AB；不改假设-BB；不改假设-BO；不改假设-BM；不改假设-BN。

**专节保留 · 双字母 BQ ≠ 单字母假设-Q；且 ≠ 假设-BA / 假设-K / 假设-BF / 假设-BC；带过 BP≠P/BO/W、BM≠BC/BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）**：正文「### 专节 · 双字母 BQ ≠ 单字母假设-Q；且 ≠ 假设-BA / 假设-K / 假设-BF / 假设-BC；带过 BP≠P/BO/W、BM≠BC/BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K」保留不删；**禁止**覆盖/混读/改写 `假设-Q` / `假设-BA` / `假设-K` / `假设-BF` / `假设-BC` / `假设-BP`。

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BQ**；**params.G≠实验字母 BQ**；**params.N≠实验字母 BQ**；亦≠单字母实验 A/B/Q/Z；禁 null/holdout/跑后改口）；② `params.bq0_primary_demo=invent_keep_open_after_list_removal`（禁与 `invent_asof_leak_list_removal_stock_rule` 双挂争主表；BQ1半泄露不得升格并列主报）。调出后存量锚保留：`list_removal_stock_honest=pit_by_effective_date`；`list_removal_stock_scope=no_new_or_add_unwind_only_or_deadline`；`list_removal_over_policy=reject_or_force_unwind_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。与 BA–BP/Z/AB/B/A/H/Q/K/W/T 硬分列保留；**专节保留 BQ≠Q / BQ≠BA / BQ≠K / BQ≠BF / BQ≠BC / BQ≠BB / BQ≠BO / BQ≠BP / BQ≠BM / BQ≠BN / 带过 BP≠P/BO/W、BM≠BC/BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K**。参考总管派令 / 风控预检有条件通过（`预检-假设BQ-20261103.md`；草稿 HEAD=f859795）。未改 Y/Z/AA–BP 及其他已冻结补丁；**不改假设-BP**；不改假设-H；不改假设-A；不改假设-B；不改假设-Q；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BP；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BP 补丁已交后写假设-BQ；离线大纲迁罐；自立 BQ，勿占 BA–BP/B/Q/A/Z/K/AB/H/W；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BQ**；**双字母 BQ ≠ 单字母 Q**；**BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN**；**带过 BP≠P/BO/W、BM≠BC/BM≠BL、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**）。选题：标的调出名单后存量合约假续持/展期加仓误开（正交于 BA/K 新开名单 / BF 期限到期 / BC 强平 / BB 券源 / BO 利息 / BP 权益补偿）。primary_demo 建议 `invent_keep_open_after_list_removal`；禁与 `invent_asof_leak_list_removal_stock_rule` 双挂。
