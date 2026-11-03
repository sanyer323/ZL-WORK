# 假设 BR · 融券借券费/融出费率计提误关 / 用核对日费率规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BQ 补丁已交（复检在途）、写下一纸面 BR；清单撞题规则另选正交执行缺口（**融券未了结期间借券费/融出费率按生效日计提** ≠ 融资利息与逾期罚息 ≠ 融券权益补偿 ≠ 转融券券源可借量 ≠ 融券空头名单 ≠ 融券卖出价限 ≠ 标的调出后存量续持 ≠ 开仓保证金比例 ≠ 授信额度 ≠ 账户串用 ≠ 合约期限/到期了结 ≠ 融资买入标的名单 ≠ 维持担保强平 ≠ 担保品折算率 ≠ 市场25pct暂停 ≠ 可充抵名单 ≠ 客户单票集中度 ≠ 担保品提取 ≠ 追保后禁新开 ≠ 融券所得用途 ≠ 融资卖出还债优先）；选题自两融业务公开口径：融券卖出未了结期间，融券方须按合同/细则向出借方/券商支付**借券费/融出费率**（按日或按约定；券商可加严）；费率与起息规则按**施行日/生效日** PIT，不得默认「永不收借券费/零费率」或用核对日更宽零费率/低费率规则回放全历史；2010-03-31 前无此通道；BO 正文已明示「融券费用另桶、本页不主测融券借券费」→ 本页自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BR ≠ 单字母 B**）/ **R（股票ETF假回转；双字母 BR ≠ 单字母假设-R）** / Z（**开仓**融资/融券保证金比例；**BR≠Z**）/ BA–BQ（两融族已冻/在途；**BR≠BA…BQ**；**尤其不改 BQ 正文**）/ **K（融券空头名单 PIT；BR≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BR≠AB**）/ BO（**融资利息与逾期罚息**；**BR≠BO**；融资计息 ≠ 融券借券费；BO 已另桶预留）/ BP（**融券权益补偿**；**BR≠BP**；现金红利/红股/配股补偿 ≠ 借券费；不占 invent_zero_short_corp_action_comp）/ BB（**转融券券源**；**BR≠BB**；可借量 ≠ 借到后费率）/ BQ（**标的调出后存量假续持**；**BR≠BQ**；调出存量 ≠ 借券费；**不改 BQ**）/ BI（**融券卖出所得用途**；**BR≠BI**）/ BJ（**融资卖出还债优先**；**BR≠BJ**）/ BF（**两融合约期限到期强制了结**；**BR≠BF**）/ BH（**授信额度**；**BR≠BH**）/ BN（**信用/普通账户串用**；**BR≠BN**；并带过 **BN≠BI/BJ/BL/BM、params.N≠BN**）/ BM（**追保后禁新开**；**BR≠BM**；并带过 **BM≠BC、BM≠BL**）/ BL（**担保品提取**；**BR≠BL**；并带过 **BL≠BC**）/ BC（**维持担保强平**；**BR≠BC**）/ W（除权板价；**BR≠W**）/ E（整手）/ AN–BQ（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BR**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「融券永不收借券费/零费率/用核对日零费率铺满」当诚实空头成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BQ 及其他 A/D–BQ 已交正文与冻结补丁；尤其不改假设-BQ；不改假设-H；不改假设-A；不改假设-B；不改假设-R；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BQ；不改假设-AB；勿再改 BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BR（约 #75）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融券未了结期间是否按生效日计提借券费/融出费率**。**双字母 BR ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BR ≠ 单字母 B**。与假设 **R（股票ETF假回转）** **硬分列（专节强调）**：R = 股票 ETF 是否假当日回转；本页 = 信用账户**融券借券费/融出费率计提**；ETF 回转 ≠ 借券费。**双字母 BR ≠ 单字母假设-R**。与假设 **BO（融资利息与逾期罚息）** **硬分列**：BO = **融资**负债计息/逾期罚息；本页 = **融券**借券费/融出费率；融资计息 ≠ 融券借券费；**禁止**把「融资已计息」静默写成「融券借券费已计提」；BO 已明示融券费用另桶。**BR≠BO**。与假设 **BP（融券权益补偿）** **硬分列**：BP = 现金红利/红股/配股**权益补偿**；本页 = 日常**借券费费率**；权益事件补偿 ≠ 借券费；**不占** `invent_zero_short_corp_action_comp`。**BR≠BP**。与假设 **BB（转融券券源）** **硬分列**：BB = 转融通/券源是否可借；本页 = 借到之后的**费率成本**；有券 ≠ 零费率。**BR≠BB**。与假设 **BQ（标的调出后存量假续持）** **硬分列**：BQ = 名单调出后存量续持/展期；本页 = 借券费计提；调出存量 ≠ 费率；**尤其不改 BQ 正文**。**BR≠BQ**。与假设 **K（融券空头名单 PIT）** **硬分列**：K = 当日是否在**交易所融券标的名单**内；本页 = 已开融券后是否收借券费；名单内可空 ≠ 零费率。**BR≠K**；并**带过**：双字母 **BK ≠ 单字母假设-K / 预检K**。与假设 **AB（融券卖出价限）** **硬分列**：不重开空头价限/当日平。与假设 **BI/BJ/BF/BH/BN/BM/BL/BC** **硬分列**：所得用途 / 还债优先 / 合约期限强了 / 授信 / 账户串用 / 追保禁开 / 高维持提取 / 低维持强平 ≠ 借券费；并**带过 BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 **BA/BD/BE/BG/BK/Z/W** **硬分列**：融资名单 / 折算率 / 市场25pct / 可充抵名单 / 客户单票集中度 / 开仓保证金比例 / 除权板价 ≠ 借券费。与假设 AN–BQ **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BR** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 R**（股票ETF假回转）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BR / 假设-BR / hypothesis_id=BR / 组 BR0·BR1·BR2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BR 混读或互改。亦**禁止**把实验字母 BR 与单字母 **A**、单字母 **B**、单字母 **R**、单字母 **K**、单字母 **Z**、双字母 **BA–BQ**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `br0_*` 以外的实验页混读。**双字母 BR ≠ 单字母 A ≠ 单字母 B ≠ 单字母 R ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BQ ≠ 双字母 BO ≠ 双字母 BP ≠ 双字母 BB ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H ≠ 双字母 T**；**params.Y ≠ 实验字母 BR**；**params.G ≠ 实验字母 BR**；**params.N ≠ 实验字母 BR**。**带过：双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BR ≠ 单字母假设-R；且 ≠ 假设-BO / 假设-BP / 假设-BB；带过 BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BR（双字母） |
|------|--------|----------------------|
| 题面 R | 股票 ETF 假当日回转 | **融券借券费/融出费率计提**误关：假零费率 vs 按生效日费率 PIT |
| 题面 BO | **融资**利息与逾期罚息计提 | **融券**借券费；融资计息 ≠ 融券借券费；**BR≠BO**；BO 已另桶预留 |
| 题面 BP | 融券**权益补偿**（现金红利/红股/配股） | 日常**借券费费率**；权益补偿 ≠ 借券费；**BR≠BP**；不占 invent_zero_short_corp_action_comp |
| 题面 BB | 转融券**券源可借量** | 借到后的**费率成本**；有券 ≠ 零费率；**BR≠BB** |
| 题面 BQ | 标的调出后**存量假续持**（复检在途） | 借券费计提；调出存量 ≠ 费率；**BR≠BQ**；**不改 BQ** |
| 题面 K / AB | 融券名单 / 空头价限 | 名单内可空 / 价限 ≠ 零费率；**BR≠K≠AB**；**带过 BK≠K** |
| 题面 BN 链 | 账户隔离等（**BN≠BI/BJ/BL/BM**；**params.N≠BN**） | 本页不覆盖；**带过**消歧链；并带过 **BO≠O/BF/BJ/BH/BN、BQ 撞题链** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_zero_short_borrow_fee` |
| 文档 | `假设-R-…` / `假设-BO-…` / `假设-BP-…` / `假设-BB-…` / `假设-BQ-…` / `假设-K-…`（**只读；禁止改写**） | `假设-BR-融券借券费融出费率计提误关.md`（新建） |
| 预检键 | 实验字母 R / BO / BP / BB / BQ / K | 实验字母 **BR** / `br0_primary_demo`；**不得**占用或改写预检 R/BO/BP/BB/BQ/K |

**禁止**：把 BR 写成「R/BO/BP/BB/BQ 的续篇」；把「融资已计息 / 权益已补偿 / 有转融券源 / 名单内可空 / 调出后已处理存量」静默写成「融券借券费零」；覆盖或补丁改写假设-R / 假设-BO / 假设-BP / 假设-BB / 假设-BQ / 假设-K 正文；把 `params.Y/G/N` 与实验字母 BR 混读；**禁** `br0_primary_demo` 与 `invent_asof_leak_short_borrow_fee` **双挂主报**；**禁** BR1 半泄露升格并列主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有/滚动融券空头路径、同一未复权价、同一 T+1、同一开仓保证金比例与融券名单/转融券源/融券价限/融资计息/权益补偿/账户隔离输入（Z/K/BB/AB/BO/BP/BN 层诚实或显式旁路声明「本页不重开开仓比例/融券名单/转融券源/空头价限/融资利息/权益补偿/账户隔离/调出后存量」）下，把「融券永不收借券费/融出费率、费率成本恒为 0」或「全样本用核对日当天借券费率规则（含券商当日更宽零费率/低费率口径）回放历史」当成默认，相对「每个交易日按当时有效融券借券费/融出费率规则 PIT（按日或按约定计费；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假零借券费空头路径并高估净收益、低估融券持仓真实成本**；差异应**集中在融券借券费/融出费率计提误关桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假零借券费贡献差、净收益差、应计借券费差在标定噪声带内可忽略，且「假零借券费 / 核对日泄露 / 正常计费窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·K·AB·R·B·H·W·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融券借券费 ≠ 融资利息罚息；≠ 融券权益补偿；≠ 转融券券源；≠ 标的调出后存量；≠ 融券名单；≠ 空头价限；≠ 开仓保证金比例；≠ 授信额度；≠ 账户串用；≠ 合约期限强了；≠ 追保禁开；≠ 担保品提取；≠ ETF假回转；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BR；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 R；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BR
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BR；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.short_borrow_fee_honest         写死 pit_by_effective_date
# params.short_borrow_fee_scope          写死 short_borrow_fee_or_lend_rate
# params.short_borrow_fee_over_policy    写死 accrue_or_fail_missing_rate
# params.broker_waive_fee_bucket         写死 separate_sensitivity
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
# params.list_removal_stock_handoff      写死 bq_page
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.etf_rotation_handoff            写死 r_page
# params.exit_period_handoff             写死 h_page
# params.br0_primary_demo                写死冻结 invent_zero_short_borrow_fee  # 主报：融券借券费永不计提/零费率；禁与 invent_asof_leak_short_borrow_fee 双挂争主表；BR1半泄露不得升格并列主报
# params.br0_invent_zero_short_borrow_fee 写死 True
# params.br1_asof_leak_short_borrow_fee_only 写死 True
# params.br2_pit_short_borrow_fee        写死 True
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
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_R_etf_rotation       写死 False
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
# params.merge_with_L_mkt                写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_P_index_halt         写死 False
# params.universe_rule                   写死 sse_szse_short_borrow_fee_check
# params.missing_short_borrow_fee_policy 写死 skip
# params.day_freq_proxy                  写死 short_borrow_fee_accrual_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BR；params.G≠实验字母BR；params.N≠实验字母BR；亦≠单字母实验A/B/R/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
short_borrow_fee_honest = "pit_by_effective_date"
params.br0_primary_demo = "invent_zero_short_borrow_fee"  # 单一主报·已冻结；禁与 invent_asof_leak_short_borrow_fee 双挂
```

额度窗内日频可落点（写明但不真跑）：日终融券空头名义 × 当日生效年化借券费率 / 计息日基数 → 当日应计借券费；缺费率字段 → skip（敏感性另桶）。本页**不开回测 / 不真跑**。

### 2.2 三组对照（BR0 / BR1 / BR2）

| 组 | 口径 | 说明 |
|----|------|------|
| BR0 天真 | `invent_zero_short_borrow_fee`（单一主报·已冻结） | 融券借券费永不计提/零费率；永不检查费率规则 |
| BR1 半泄露 | `invent_asof_leak_short_borrow_fee` | 仅用核对日借券费率规则（含券商当日更宽零/低费率口径）铺满全历史；**不得升格并列主报** |
| BR2 诚实 PIT | `pit_short_borrow_fee` / `short_borrow_fee_honest=pit_by_effective_date` | 按当日已生效借券费/融出费率 PIT；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/K/BB/BO/BP）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **规则生效**：融券借券费/融出费率合同或细则施行日/生效日；禁用核对日更宽「零费率」提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BR0 相对 BR2 的假零借券费贡献差、净收益差、应计借券费差超过 `params.Y` / `params.G` / `params.N` / `params.Y2` 标定带，且主贡献落在「融券借券费/融出费率计提误关」桶；holdout 同向不反号到噪声带内。BR1 相对 BR2 的核对日泄露贡献可单独度量且不得冒充主报。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeZeroShortBorrowFee / ΔPnL 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA–BQ/K/AB/R/B/H/W/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BR0 / BR1 / BR2。报告净收益差、假零借券费贡献差、应计借券费差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_zero_short_borrow_fee",
  "invent_asof_leak_short_borrow_fee",
  "short_borrow_fee_accrual_window",
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
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_R_etf_rotation",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够融券空头日终余额；缺费率字段却静默当零费率 → 设计失效。  
2. 把「融资已计息（BO）」静默写成「融券借券费已计提」且不声明另页 BO → **与 BO 撞题**（融资计息 ≠ 融券借券费；**尤其 BR≠BO**）。  
3. 把「权益已补偿（BP）」静默写成「借券费已计提」且不声明另页 BP → **与 BP 撞题**（权益补偿 ≠ 借券费；**尤其 BR≠BP**）。  
4. 把「有转融券源/可借（BB）」静默写成「零费率」且不声明另页 BB → 与 BB 撞题（**尤其 BR≠BB**）。  
5. 把「调出后存量已处理（BQ）」静默写成「零借券费」且不声明另页 BQ → 与 BQ 撞题（**尤其 BR≠BQ**；**不改 BQ**）。  
6. 把「名单内可空 / 价限已诚实 / 授信够 / 未强平 / 账户未串用 / 保证金比例够」静默写成「零借券费」且不声明另页 K/AB/BH/BC/BN/Z → 与对应页撞题；并**带过 BQ/BP/BO/BN/BM/BL/BK 消歧链**。  
7. 把「股票 ETF 假回转可成」写成主病而不声明另页 R → 与 R 撞题（**双字母 BR ≠ 单字母 R**）。  
8. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易」写成主病而不声明另页 AB/W/A/H → 与对应页撞题。  
9. 把「融券借券费计提误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
10. 把实验字母 BR 与单字母 A/B/R/K/Z 或双字母 BA–BQ/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `br0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价算借券费名义 → 标签与执行双错，结论无效。  
13. 用核对日更宽「零费率」当诚实 PIT、或把券商临时免息提前铺满历史 → 设计失效。  
14. **`br0_primary_demo` 与 `invent_asof_leak_short_borrow_fee` 双挂主报**；或 BR1 升格并列主报 → 设计失效。  
15. **改写或覆盖 `假设-R` / `假设-BO` / `假设-BP` / `假设-BB` / `假设-BQ` / 已冻 AA–BQ** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户融券空头日终数量/名义与开仓日、未了结标记；  
- 当时有效融券借券费/融出费率规则及生效日（年化或按日；券商加严/免息另桶）；  
- 开仓保证金比例 / 融券名单 / 转融券源 / 空头价限 / 融资计息 / 权益补偿 / 账户隔离 / 调出后存量输入（消费 Z/K/BB/AB/BO/BP/BN/BQ 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商临时免息/优惠费率子集另桶；转融出专项费率档。

**禁止**：用核对日「今天零费率」铺满当唯一诚实组；用复权价；把融资利息/权益补偿/转融券源/调出后存量/开仓保证金比例/低维持强平/合约期限未到期/新开名单窗/授信够/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/追保未触发/账户未串用当成零借券费依据；把 Z/BA–BQ/K/AB/A/R/B/H/W/T/AN–BQ 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BR`  
- **组**：BR0 / BR1 / BR2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`short_borrow_fee_honest=pit_by_effective_date`；`short_borrow_fee_scope=short_borrow_fee_or_lend_rate`；`short_borrow_fee_over_policy=accrue_or_fail_missing_rate`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`etf_rotation_handoff=r_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_short_borrow_fee_check`；`missing_short_borrow_fee_policy=skip`；`day_freq_proxy=short_borrow_fee_accrual_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BR**；**params.G≠实验字母 BR**；**params.N≠实验字母 BR**；亦≠单字母实验 A/B/R/Z；禁 null/holdout/跑后改口）；**`params.br0_primary_demo` 写死冻结 `invent_zero_short_borrow_fee`**（禁与 invent_asof_leak_short_borrow_fee 双挂；BR1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BR0/BR1/BR2 净收益/路径质量、ΔFakeZeroShortBorrowFee、ΔAccruedShortBorrowFee；分桶（融券借券费假零费率误关 / 核对日泄露 / 计费窗 / 通道前 / vs A·Z·BA–BQ·K·AB·R·B·H·W·T）。  
- 自检布尔：BR2 是否 pit_by_effective_date；BR0 是否单一主报；BR1 是否仅核对日泄露；是否未与 A/Z/BA–BQ/K/AB/R/B/H/W/T 混主结论；holdout 是否未反调；**是否未把实验字母 BR 与 A 或 B 或 R 或 K 或 Z 或 BA–BQ 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BR≠单字母假设-R；BR≠BO；BR≠BP；BR≠BB；BR≠BQ；带过 BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BQ 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-R / 假设-K / 假设-W / 假设-Z / 假设-BA–BQ / 假设-AB**；**是否未再改 BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未与 invent_asof_leak_short_borrow_fee 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把零借券费或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BQ 及其他 A/D–BQ 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-R**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BQ**；**尤其不改假设-BQ**；**不改假设-AB**；**勿再改 BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券空头名单（K）之外，**融券借券费/融出费率**须按当时有效规则 PIT；不得默认永不收借券费/零费率。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BR** 标准件，**不改口径主线**，**不改假设 A–BQ 正文**，**尤其不改假设-R / 假设-BO / 假设-BP / 假设-BB / 假设-BQ**。与实验 A/Z/BA–BQ/K/AB/R/B/H/W/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA–BQ=两融族已冻/在途；K=融券空头新开名单；AB=融券卖出价限；R=股票ETF假回转；B=历史实验B旧位；H=退市整理；W=除权板价；T=证管费（避开）；BR=融券借券费/融出费率计提误关（BR≠A≠B≠R≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠BM≠BN≠BO≠BP≠BQ≠AB≠W≠H≠T；带过 BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频融券空头名义+费率生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**short_borrow_fee_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BR；params.G≠实验字母 BR；params.N≠实验字母 BR；亦≠单字母实验 A/B/R/Z；禁 null/holdout/跑后改口）**；**br0_primary_demo 写死冻结 invent_zero_short_borrow_fee（禁双挂 invent_asof_leak_short_borrow_fee；BR1半泄露不得升格并列主报）**；锚点保留 short_borrow_fee_honest=pit_by_effective_date / short_borrow_fee_scope=short_borrow_fee_or_lend_rate / short_borrow_fee_over_policy=accrue_or_fail_missing_rate / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单（两条已冻结 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已写死冻结**；**params.Y≠BR**；**params.G≠BR**；**params.N≠BR**；禁 null/holdout）  
2. `params.br0_primary_demo` = `invent_zero_short_borrow_fee`（**已写死冻结**；禁与 `invent_asof_leak_short_borrow_fee` 双挂；BR1不升格主报）  
3. 借券费锚：`short_borrow_fee_honest=pit_by_effective_date`；`short_borrow_fee_scope=short_borrow_fee_or_lend_rate`；`short_borrow_fee_over_policy=accrue_or_fail_missing_rate`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/R/A/Z/BA–BQ/K/AB/H/W/T；**尤其 BR≠BO（融资计息≠融券借券费）**；**尤其 BR≠BP（权益补偿≠借券费）**；**尤其 BR≠BB（券源≠费率）**；**尤其 BR≠BQ（调出存量≠费率；不改BQ）**；**尤其 BR≠R**；**带过 BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 与 BA–BQ 撞题检查表

| 字母 | 主题 | 撞题？ | 消歧 |
|------|------|--------|------|
| BA | 融资买入新开名单 | 否 | — |
| BB | 转融券券源 | 否 | 可借量 ≠ 借到后费率 |
| BC | 维持强平 | 否 | — |
| BD | 折算率 | 否 | — |
| BE | 市场25pct暂停 | 否 | — |
| BF | 合约期限到期了结 | 否 | — |
| BG | 可充抵名单 | 否 | — |
| BH | 授信额度 | 否 | — |
| BI | 融券所得用途 | 否 | — |
| BJ | 融资卖出还债优先 | 否 | — |
| BK | 客户单票集中度 | 否 | — |
| BL | 担保品提取 | 否 | — |
| BM | 追保后禁新开 | 否 | — |
| BN | 跨账户现金混用 | 否 | — |
| BO | 融资利息罚息零 | 否 | 融资计息 ≠ 融券借券费；BO 已另桶预留 |
| BP | 融券权益补偿 | 否 | 权益补偿 ≠ 借券费；不占 invent_zero_short_corp_action_comp |
| BQ | 调出后存量续持 | 否 | 调出存量 ≠ 费率；**不改 BQ** |
| K | 融券新开名单 | 否 | 名单内可空 ≠ 零费率 |
| Z | 开仓保证金比例 | 否 | — |
| AB | 融券价限/当日平 | 否 | — |
| R | 股票ETF假回转 | 否 | 双字母 BR ≠ 单字母 R |
| A/B/H/W/T | 板上/旧B/退市/除权/证管费 | 否 | 避开预检T |

**撞题检查：通过（纸面）** — 入库后对照正式清单 #75 再核一次 primary_demo 唯一性。

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BR**；**`params.G` ≠ 实验字母 BR**；**`params.N` ≠ 实验字母 BR**；**`params.Y` ≠ 单字母实验 A/B/R/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.br0_primary_demo`**：**写死冻结** **`invent_zero_short_borrow_fee`**；禁与 **`invent_asof_leak_short_borrow_fee`** 双挂争主表（只挂一个 primary）；**BR1 半泄露不得升格并列主报**。

**借券费锚保留（已通写死）**：`params.short_borrow_fee_honest=pit_by_effective_date`；`params.short_borrow_fee_scope=short_borrow_fee_or_lend_rate`；`params.short_borrow_fee_over_policy=accrue_or_fail_missing_rate`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有 `missing_short_borrow_fee_policy=skip` 等锚点；不改口）。

**与 BA–BQ/Z/AB/B/A/H/R/K/W/T 硬分列（保留）**：本页 = **融券借券费/融出费率计提误关**；R = **股票ETF假回转**（**尤其双字母 BR ≠ 单字母假设-R**）；BO = **融资利息与逾期罚息**（**尤其 BR≠BO**；融资计息 ≠ 融券借券费）；BP = **融券权益补偿**（**尤其 BR≠BP**；不占 invent_zero_short_corp_action_comp）；BB = **转融券券源**（**尤其 BR≠BB**；可借量 ≠ 费率）；BQ = **标的调出后存量假续持**（**尤其 BR≠BQ**；调出存量 ≠ 费率；**尤其不改假设-BQ**）；K = **融券空头名单**（**尤其 BR≠K**；并**带过 BK≠K**）；AB = **融券卖出价限**；Z = **开仓**保证金比例；W = **除权板价**；A = **板上枯竭**；B = 历史实验 B 旧位；H = **退市整理期**；T = **证管费**（避开预检T）；借券费 ≠ ETF假回转 ≠ 融资计息 ≠ 权益补偿 ≠ 转融券源 ≠ 调出后存量 ≠ 融券名单 ≠ 空头价限 ≠ 开仓比例 ≠ 除权板价 ≠ 板上枯竭 ≠ 退市整理 ≠ 证管费；**双字母 BR ≠ 单字母 A ≠ 单字母 B ≠ 单字母 R ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BQ ≠ 双字母 BO ≠ 双字母 BP ≠ 双字母 BB ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H ≠ 双字母 T**；**params.Y ≠ 实验字母 BR**；**params.G ≠ 实验字母 BR**；**params.N ≠ 实验字母 BR**；禁止捆成「两融一张表=零借券费」；**尤其不改假设-R**；**尤其不改假设-BO**；**尤其不改假设-BP**；**尤其不改假设-BB**；**尤其不改假设-BQ**；**尤其不改假设-K**；**尤其不改假设-H**；不改假设-B；不改假设-Z；不改假设-BA–BQ；不改假设-A；不改假设-AB；不改假设-W。

**专节保留 · 双字母 BR ≠ 单字母假设-R；且 ≠ 假设-BO / 假设-BP / 假设-BB；带过 BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）**：正文「### 专节 · 双字母 BR ≠ 单字母假设-R；且 ≠ 假设-BO / 假设-BP / 假设-BB；带过 BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K」保留不删；**禁止**覆盖/混读/改写 `假设-R` / `假设-BO` / `假设-BP` / `假设-BB` / `假设-BQ` / `假设-K`。

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BR**；**params.G≠实验字母 BR**；**params.N≠实验字母 BR**；亦≠单字母实验 A/B/R/Z；禁 null/holdout/跑后改口）；② `params.br0_primary_demo=invent_zero_short_borrow_fee`（禁与 `invent_asof_leak_short_borrow_fee` 双挂争主表；BR1半泄露不得升格并列主报）。借券费锚保留：`short_borrow_fee_honest=pit_by_effective_date`；`short_borrow_fee_scope=short_borrow_fee_or_lend_rate`；`short_borrow_fee_over_policy=accrue_or_fail_missing_rate`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。与 BA–BQ/Z/AB/B/A/H/R/K/W/T 硬分列保留；**专节保留 BR≠R / BR≠BO / BR≠BP / BR≠BB / BR≠BQ / 带过 BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K**。参考总管派令 / 风控预检有条件通过（`预检-假设BR-20261103.md`；草稿 HEAD=e2cb45e）。未改 Y/Z/AA–BQ 及其他已冻结补丁；**不改假设-BQ**；**不改假设-BP**；不改假设-H；不改假设-A；不改假设-B；不改假设-R；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BQ；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BQ 补丁已交复检在途 → 写假设-BR；自立 BR，勿占 BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/R/A/Z/K/W；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BR**；**双字母 BR ≠ 单字母 R**；**BR≠BO/BP/BB/BQ**；选题：BO 已另桶预留的融券借券费/融出费率；`br0_primary_demo=invent_zero_short_borrow_fee`；半泄露 `invent_asof_leak_short_borrow_fee` 禁双挂/升格；**不改假设-BQ**；不改 Y/Z/AA–BQ）。结论栏空。
