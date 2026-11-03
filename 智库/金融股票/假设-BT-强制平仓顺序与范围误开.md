# 假设 BT · 强制平仓顺序与范围误开 / 用核对日最优序或最小范围铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BS 补丁已交（复检在途）、写下一纸面 BT；清单撞题规则另选正交执行缺口（**强制平仓触发后的平仓顺序/范围** ≠ 维持担保比例强平闸门是否误关 ≠ 融资利率档位 ≠ 融资利息假零息 ≠ 融券借券费 ≠ 授信额度上限 ≠ 标的调出后存量续持 ≠ 融券权益补偿 ≠ 追保后禁新开 ≠ 担保品提取 ≠ 开仓保证金比例 ≠ 融资买入名单 ≠ 转融券券源 ≠ 合约期限到期了结 ≠ 证管费）；选题自两融业务公开口径：维持担保比例触发追保/强制平仓后，会员/合同对**平仓标的顺序、平仓范围（全仓类 vs 仅减至恢复线）、平仓侧（担保品 / 融资买入证券 / 融券了结）**有当时有效规则；顺序与范围按**施行日/生效日** PIT，不得默认「永远按对客户最有利顺序 / 永远只平最小名义刚好恢复维持线 / 用核对日最优序或最小范围规则铺满历史」；2010-03-31 前无此通道；**BC 正文主测「永不触发强平 / 维持线闸门误关」**（强平闸门 on/off），本页主测**闸门已触发后发明假最优平仓序或假最小平仓范围** → 自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BT ≠ 单字母 B**）/ **T（证管费误抽；双字母 BT ≠ 单字母假设-T；严禁复用预检T题面或证管费口径）** / Z（**开仓**融资/融券保证金比例；**BT≠Z**）/ BA–BS（两融族已冻/在途；**BT≠BA…BS**；**尤其不改 BS 正文**）/ **K（融券空头名单 PIT；BT≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BT≠AB**）/ BC（**维持担保比例强制平仓误关**；**BT≠BC**；闸门 on/off ≠ 触发后顺序/范围；**尤其不改假设-BC**）/ BS（**融资利率档位优惠档**；**BT≠BS**；利率档 ≠ 强平序；**尤其不改假设-BS**）/ BO（**融资利息与逾期罚息假零息**；**BT≠BO**）/ BR（**融券借券费**；**BT≠BR**）/ BH（**授信额度上限**；**BT≠BH**）/ BQ（**标的调出后存量假续持**；**BT≠BQ**）/ BP（**融券权益补偿**；**BT≠BP**）/ BN（**信用/普通账户串用**；**BT≠BN**；并带过 **BN≠BI/BJ/BL/BM、params.N≠BN**）/ BM（**追保后禁新开**；**BT≠BM**；并带过 **BM≠BC、BM≠BL**）/ BL（**担保品提取**；**BT≠BL**；并带过 **BL≠BC**）/ BB（**转融券券源**；**BT≠BB**）/ BF（**两融合约期限到期强制了结**；**BT≠BF**；期限到 ≠ 维持线触发后的平仓序）/ BI（**融券卖出所得用途**；**BT≠BI**）/ BJ（**融资卖出还债优先**；**BT≠BJ**）/ BD（**担保品折算率**；**BT≠BD**）/ BE（**市场25pct余额暂停**；**BT≠BE**）/ BG（**可充抵名单**；**BT≠BG**）/ BK（**客户单票集中度**；**BT≠BK**）/ W（除权板价；**BT≠W**）/ E（整手）/ AN–BS（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BT**  
状态：**草稿 · 待预检**（结论栏空；禁止把「强平触发后永远按对客户最有利顺序 / 永远只平最小名义刚好恢复维持线 / 用核对日最优序或最小范围铺满」当诚实强平路径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BS 及其他 A/D–BS 已交正文与冻结补丁；尤其不改假设-BS；尤其不改假设-BC；不改假设-T；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BS；不改假设-AB；勿再改 BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BT（约 #77）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **维持线已触发强制平仓后的平仓顺序与范围**。**双字母 BT ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BT ≠ 单字母 B**。与假设 **T（证管费误抽）** **硬分列（专节强调）**：T = 证监会监管费费率切片；本页 = 信用账户**强制平仓顺序/范围**；证管费 ≠ 强平序。**双字母 BT ≠ 单字母假设-T**；**严禁复用预检T题面或 T 口径键**。与假设 **BC（维持担保比例强制平仓误关）** **硬分列**：BC = 发明**永不检查维持线 / 永不触发强平**（闸门 on/off）；本页 = **闸门已触发后**发明假最优平仓序或假最小平仓范围；闸门 ≠ 顺序/范围；**禁止**把「未触发强平（BC 天真组）」静默写成「已按诚实顺序强平」；**禁止**把「已触发强平」静默写成「已按对客户最有利序最小范围处理」；**不占** BC 的 primary_demo；**尤其不改假设-BC**。**BT≠BC**。与假设 **BS（融资利率档位）** **硬分列**：BS = 融资利率档位/优惠档误用；本页 = 强平序/范围；利率档 ≠ 强平序；**尤其不改假设-BS**。**BT≠BS**。与假设 **BO / BR / BH / BQ / BP / BN / BM / BL / BB / BF** **硬分列**：假零息 / 借券费 / 授信天花板 / 调出后存量 / 权益补偿 / 账户串用 / 追保禁开 / 高维持提取 / 转融券源 / 合约期限到期了结 ≠ 强平触发后的顺序与范围；并**带过 BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 **K / AB / Z / W / BA / BD / BE / BG / BK / BI / BJ** **硬分列**：融券名单 / 空头价限 / 开仓保证金 / 除权板价 / 融资名单 / 折算率 / 市场25pct / 可充抵 / 客户集中度 / 融券所得用途 / 融资还债优先 ≠ 强平序。与假设 AN–BS **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BT** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 T**（证管费误抽；**严禁复用预检T**）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BT / 假设-BT / hypothesis_id=BT / 组 BT0·BT1·BT2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BT 混读或互改。亦**禁止**把实验字母 BT 与单字母 **A**、单字母 **B**、单字母 **T**、单字母 **K**、单字母 **Z**、双字母 **BA–BS**、双字母 **BC**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bt0_*` 以外的实验页混读。**双字母 BT ≠ 单字母 A ≠ 单字母 B ≠ 单字母 T ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BS ≠ 双字母 BC ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BQ ≠ 双字母 BP ≠ 双字母 BN ≠ 双字母 BM ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BT**；**params.G ≠ 实验字母 BT**；**params.N ≠ 实验字母 BT**。**带过：双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BT ≠ 单字母假设-T；且 ≠ 假设-BC / 假设-BS / 假设-BO / 假设-BR / 假设-BH / 假设-BQ / 假设-BP / 假设-BN / 假设-BM；带过 BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BT（双字母） |
|------|--------|----------------------|
| 题面 T | 证管费费率切片（预检T旧题） | **强制平仓顺序与范围**误开：假最优序/假最小范围 vs 按生效日平仓序 PIT；**严禁复用 T 题面** |
| 题面 BC | **维持担保比例强制平仓误关**（闸门 on/off） | **闸门已触发后的顺序/范围**；闸门 ≠ 序/范围；**BT≠BC**；**不改 BC** |
| 题面 BS | **融资利率档位优惠档**（复检在途） | 利率档 ≠ 强平序；**BT≠BS**；**不改 BS** |
| 题面 BO / BR | 融资假零息 / 融券借券费 | 计息/计费 ≠ 强平序；**BT≠BO≠BR** |
| 题面 BH / BQ / BP | 授信天花板 / 调出后存量 / 权益补偿 | 本页不覆盖；**BT≠BH≠BQ≠BP** |
| 题面 BN / BM / BL | 账户隔离 / 追保禁开 / 高维持提取 | 本页不覆盖；**带过**消歧链；**BT≠BN≠BM≠BL** |
| 题面 K / AB | 融券名单 / 空头价限 | 本页不覆盖；**BT≠K≠AB**；**带过 BK≠K** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_force_close_best_order_or_min_scope` |
| 文档 | `假设-T-…` / `假设-BC-…` / `假设-BS-…`（**只读；禁止改写**） | `假设-BT-强制平仓顺序与范围误开.md`（新建） |
| 预检键 | 实验字母 T / BC / BS | 实验字母 **BT** / `bt0_primary_demo`；**不得**占用或改写预检 T/BC/BS |

**禁止**：把 BT 写成「T/BC/BS 的续篇」；把「未触发强平 / 融资已假零息 / 融券已计借券费 / 授信够 / 利率档已诚实」静默写成「已按诚实强平序最小范围处理」；覆盖或补丁改写假设-T / 假设-BC / 假设-BS / 假设-BO / 假设-BR 正文；把 `params.Y/G/N` 与实验字母 BT 混读；**禁** `bt0_primary_demo` 与 `invent_asof_leak_force_close_order_scope` **双挂主报**；**禁** BT1 半泄露升格并列主报；**禁**复用预检T（证管费）题面或口径键。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有/滚动两融路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/授信/合约期限/维持担保闸门/追保禁开/账户隔离/折算率等输入（Z/BA/BH/BF/BC/BM/BN/BD 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/授信天花板/合约期限/维持线闸门 on-off/追保禁开/账户隔离/折算率主病」）下，把「强制平仓触发后永远按对客户最有利顺序平仓，或永远只平最小名义刚好恢复维持线，永不检查当时有效平仓顺序/范围规则」或「全样本用核对日当天最优序或最小范围规则回放历史」当成默认，相对「每个交易日按当时有效强制平仓顺序与范围规则 PIT（担保品/融资买入证券/融券了结之优先序；全仓类 vs 减至恢复线之范围；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假最优/假最小范围强平路径并高估强平后残余名义、低估被动减仓冲击与强平失败率**；差异应**集中在强制平仓顺序与范围误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假最优序/假最小范围贡献差、残余名义差、强平冲击差在标定噪声带内可忽略，且「假最优序最小范围 / 核对日泄露 / 正常强平窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·BS·K·AB·B·H·W·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 强制平仓顺序/范围 ≠ 维持线闸门 on/off；≠ 融资利率档；≠ 融资假零息；≠ 融券借券费；≠ 授信额度上限；≠ 标的调出后存量；≠ 融券权益补偿；≠ 追保禁开；≠ 担保品提取；≠ 合约期限到期了结；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；待预检；纸面占位建议如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BT；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 T；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BT
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BT；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.force_close_order_honest        写死 pit_by_effective_date
# params.force_close_order_scope         写死 collateral_financed_short_priority_and_unwind_scope
# params.force_close_order_over_policy   写死 apply_or_fail_missing_order_rule
# params.force_close_min_scope_naive     写死 invent_min_notional_to_restore_maint
# params.force_close_best_order_naive    写死 invent_client_best_liquidation_order
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page   # 闸门 on/off 交 BC；本页只测触发后序/范围；BT≠BC
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
# params.list_removal_stock_handoff      写死 bq_page
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page   # 融资利率档交 BS；BT≠BS；不改 BS
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.csrc_fee_handoff                写死 t_page    # 证管费交 T；BT≠T；禁复用预检T
# params.exit_period_handoff             写死 h_page
# params.bt0_primary_demo                建议 invent_force_close_best_order_or_min_scope  # 主报：假最优序或假最小范围；禁与 invent_asof_leak_force_close_order_scope 双挂争主表；BT1半泄露不得升格并列主报
# params.bt0_invent_best_order_or_min_scope 写死 True
# params.bt1_asof_leak_force_close_order_scope_only 写死 True
# params.bt2_pit_force_close_order_scope 写死 True
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
# params.universe_rule                   写死 sse_szse_force_close_order_scope_check
# params.missing_force_close_order_policy 写死 skip
# params.day_freq_proxy                  写死 force_close_order_scope_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BT；params.G≠实验字母BT；params.N≠实验字母BT；亦≠单字母实验A/B/T/Z；待预检写死；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
```

```
params.bt0_primary_demo = "invent_force_close_best_order_or_min_scope"  # 单一主报建议；禁与 invent_asof_leak_force_close_order_scope 双挂
```

### 2.2 三组对照（BT0 / BT1 / BT2）

| 组 | 口径 | 说明 |
|----|------|------|
| BT0 天真 | `invent_force_close_best_order_or_min_scope`（单一主报建议） | 发明假最优平仓序或假最小平仓范围；禁与 invent_asof_leak_force_close_order_scope 双挂 |
| BT1 半泄露/混口径 | 全样本用 `asof_check_date` 当天最优序/最小范围规则铺满历史 | 仅序/范围 asof 泄露；不升格并列主报 |
| BT2 PIT | `force_close_order_honest=pit_by_effective_date` | 每个交易日按当时已生效强制平仓顺序与范围 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：信用账户日终维持担保比例代理触线后，按 BT0/BT1/BT2 规则生成平仓腿 → 残余名义、被动减仓名义、假最优序/假最小范围贡献差。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有日终维持担保比例代理 + 持仓腿（担保品/融资买入/融券）+ 当时有效平仓序/范围规则生效日表即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BT0 / BT1 / BT2。报告残余名义差、假最优序/假最小范围贡献差、被动减仓冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_force_close_best_order_or_min_scope",
  "invent_asof_leak_force_close_order_scope",
  "force_close_order_scope_window",
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
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够维持线触线日或持仓腿字段；缺平仓序字段却静默当最优序/最小范围 → 设计失效。  
2. 把「永不触发强平（BC）」静默写成「已按诚实序强平」且不声明另页 BC → **与 BC 撞题**（闸门 ≠ 序/范围；**尤其 BT≠BC**；**不改 BC**）。  
3. 把「融资利率档已诚实（BS）」静默写成「强平序已诚实」且不声明另页 BS → **与 BS 撞题**（利率档 ≠ 强平序；**尤其 BT≠BS**；**不改 BS**）。  
4. 把「融资假零息（BO）/ 融券借券费（BR）/ 授信够（BH）」静默写成「强平序正确」→ 与对应页撞题（**尤其 BT≠BO≠BR≠BH**）。  
5. 把「证管费已诚实（T）」写成主病或不声明另页 T → **撞预检T旧题 / 假设-T**，设计失效（**双字母 BT ≠ 单字母 T**；**严禁复用预检T**）。  
6. 把「调出后存量已处理 / 权益已补偿 / 追保未触发 / 提取线未触 / 账户未串用 / 期限未到期 / 名单内可融资 / 保证金比例够」静默写成「强平序正确」且不声明另页 BQ/BP/BM/BL/BN/BF/BA/Z → 与对应页撞题；并**带过 BS/BR/BQ/BP/BO/BN/BM/BL/BK 消歧链**。  
7. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易」写成主病而不声明另页 AB/W/A/H → 与对应页撞题。  
8. 把实验字母 BT 与单字母 A/B/T/K/Z 或双字母 BA–BS/BC/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
9. holdout 反调 `bt0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算强平名义 → 标签与执行双错，结论无效。  
11. 用核对日更宽「最优序/最小范围」当诚实 PIT、或把券商临时更宽序提前铺满历史 → 设计失效。  
12. **`bt0_primary_demo` 与 `invent_asof_leak_force_close_order_scope` 双挂主报**；或 BT1 升格并列主报 → 设计失效。  
13. **改写或覆盖 `假设-T` / `假设-BC` / `假设-BS` / 已冻 AA–BS** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户维持担保比例代理、触线/追保/强平触发标记；担保品 / 融资买入证券 / 融券空头分腿名义；  
- 当时有效强制平仓顺序与范围规则及生效日（优先序；全仓类 vs 减至恢复线）；  
- 开仓保证金比例 / 融资名单 / 授信 / 合约期限 / 维持线闸门 / 追保禁开 / 账户隔离 / 折算率输入（消费 Z/BA/BH/BF/BC/BM/BN/BD 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商合同加严序/盘中紧急强平另桶；与 BC 闸门对照但不混主结论。

**禁止**：用核对日「今天最优序/最小范围」铺满当唯一诚实组；用复权价；把维持线未触发/假零息/借券费/授信够/利率档诚实/开仓保证金比例/合约期限未到期/新开名单窗/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/追保未触发/账户未串用/权益已补偿/调出后存量已处理当成「强平序正确」依据；把 Z/BA–BS/K/AB/A/B/H/W/T/AN–BS 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BT`  
- **组**：BT0 / BT1 / BT2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`force_close_order_honest=pit_by_effective_date`；`force_close_order_scope=collateral_financed_short_priority_and_unwind_scope`；`force_close_order_over_policy=apply_or_fail_missing_order_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`csrc_fee_handoff=t_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_force_close_order_scope_check`；`missing_force_close_order_policy=skip`；`day_freq_proxy=force_close_order_scope_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BT**；**params.G≠实验字母 BT**；**params.N≠实验字母 BT**；亦≠单字母实验 A/B/T/Z；待预检写死；禁 null/holdout/跑后改口）；**`params.bt0_primary_demo` 建议 `invent_force_close_best_order_or_min_scope`**（禁与 invent_asof_leak_force_close_order_scope 双挂；BT1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BT0/BT1/BT2 净收益/路径质量、ΔFakeBestOrderOrMinScope、ΔResidualNotionalAfterForceClose、ΔForcedUnwindImpact；分桶（强制平仓顺序与范围误开 / 核对日泄露 / 强平窗 / 通道前 / vs A·Z·BA–BS·K·AB·B·H·W·T）。  
- 自检布尔：BT2 是否 pit_by_effective_date；BT0 是否单一主报；BT1 是否仅核对日泄露；是否未与 A/Z/BA–BS/K/AB/B/H/W/T 混主结论；holdout 是否未反调；**是否未把实验字母 BT 与 A 或 B 或 T 或 K 或 Z 或 BA–BS 或 BC 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BT≠单字母假设-T；BT≠BC；BT≠BS；BT≠BO；BT≠BR；BT≠BH；BT≠BQ；BT≠BP；BT≠BN；BT≠BM；带过 BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BS 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-T / 假设-K / 假设-W / 假设-Z / 假设-BA–BS / 假设-BC / 假设-AB**；**是否未再改 BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未与 invent_asof_leak_force_close_order_scope 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把最优序/最小范围或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BS 及其他 A/D–BS 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-T**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BS**；**尤其不改假设-BS**；**尤其不改假设-BC**；**不改假设-AB**；**勿再改 BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、融券空头名单（K）之外，**强制平仓触发后的顺序与范围**须按当时有效规则 PIT；不得默认假最优序或假最小范围。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BT** 标准件，**不改口径主线**，**不改假设 A–BS 正文**，**尤其不改假设-T / 假设-BC / 假设-BS**。与实验 A/Z/BA–BS/K/AB/B/H/W/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA–BS=两融族已冻/在途；BC=维持线闸门；K=融券空头新开名单；AB=融券卖出价限；B=历史实验B旧位；H=退市整理；W=除权板价；T=证管费（避开）；BT=强制平仓顺序与范围误开（BT≠A≠B≠T≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠BM≠BN≠BO≠BP≠BQ≠BR≠BS≠AB≠W≠H；带过 BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待预检 |
| 数据 | 待接入（字段见 §6；日频维持线触线+分腿名义+平仓序生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**force_close_order_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BT；params.G≠实验字母 BT；params.N≠实验字母 BT；亦≠单字母实验 A/B/T/Z；待预检写死；禁 null/holdout/跑后改口）**；**bt0_primary_demo 建议 invent_force_close_best_order_or_min_scope（禁双挂 invent_asof_leak_force_close_order_scope；BT1半泄露不得升格并列主报）**；锚点保留 force_close_order_honest=pit_by_effective_date / force_close_order_scope=collateral_financed_short_priority_and_unwind_scope / force_close_order_over_policy=apply_or_fail_missing_order_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（建议写死；**params.Y≠BT**；**params.G≠BT**；**params.N≠BT**；禁 null/holdout）  
2. `params.bt0_primary_demo` = `invent_force_close_best_order_or_min_scope`（建议写死；禁与 `invent_asof_leak_force_close_order_scope` 双挂；BT1不升格主报）  
3. 序/范围锚：`force_close_order_honest=pit_by_effective_date`；`force_close_order_scope=collateral_financed_short_priority_and_unwind_scope`；`force_close_order_over_policy=apply_or_fail_missing_order_rule`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/T/A/Z/BA–BS/K/AB/H/W；**尤其 BT≠T（证管费；严禁复用预检T）**；**尤其 BT≠BC（闸门≠序/范围；不改BC）**；**尤其 BT≠BS（利率档≠强平序；不改BS）**；**尤其 BT≠BO/BR/BH/BQ/BP/BN/BM**；**带过 BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 与 BA–BS 撞题检查表

| 字母 | 主题 | 撞题？ | 消歧 |
|------|------|--------|------|
| BA | 融资买入新开名单 | 否 | — |
| BB | 转融券券源 | 否 | — |
| BC | 维持强平闸门 | 否 | 闸门 on/off ≠ 触发后顺序/范围；**不改 BC** |
| BD | 折算率 | 否 | — |
| BE | 市场25pct暂停 | 否 | — |
| BF | 合约期限到期了结 | 否 | 期限到 ≠ 维持线触发后的平仓序 |
| BG | 可充抵名单 | 否 | — |
| BH | 授信额度 | 否 | 额度天花板 ≠ 强平序 |
| BI | 融券所得用途 | 否 | — |
| BJ | 融资卖出还债优先 | 否 | — |
| BK | 客户单票集中度 | 否 | — |
| BL | 担保品提取 | 否 | 高维持提取 ≠ 强平序 |
| BM | 追保后禁新开 | 否 | 追保禁开 ≠ 强平序 |
| BN | 跨账户现金混用 | 否 | — |
| BO | 融资利息罚息零 | 否 | 假零息 ≠ 强平序 |
| BP | 融券权益补偿 | 否 | — |
| BQ | 调出后存量续持 | 否 | — |
| BR | 融券借券费零 | 否 | 借券费 ≠ 强平序 |
| BS | 融资利率档位优惠档 | 否 | 利率档 ≠ 强平序；**不改 BS** |
| K | 融券新开名单 | 否 | — |
| Z | 开仓保证金比例 | 否 | — |
| AB | 融券价限/当日平 | 否 | — |
| A/B/H/W/T | 板上/旧B/退市/除权/证管费 | 否 | **尤其避开预检T；双字母 BT ≠ 单字母 T** |

**撞题检查：通过（纸面）** — 入库后对照正式清单 #77 再核一次 primary_demo 唯一性。

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BS 补丁已交复检在途 → 写假设-BT；自立 BT，勿占 BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/T/A/Z/K/W；**尤重 BT≠T**；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BT**；**双字母 BT ≠ 单字母 T**；**BT≠BC/BS/BO/BR/BH/BQ/BP/BN/BM**；选题：BC 维持线闸门旁的**强制平仓顺序与范围误开**；`bt0_primary_demo=invent_force_close_best_order_or_min_scope`；半泄露 `invent_asof_leak_force_close_order_scope` 禁双挂/升格；**不改假设-BS**；**不改假设-BC**；**不改假设-T**；不改 Y/Z/AA–BS）。结论栏空。
