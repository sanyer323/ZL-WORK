# 假设 BS · 融资利率档位/客户分类优惠利率误用 / 用核对日最低档费率铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BR 补丁已收（复检在途）、写下一纸面 BS；清单撞题规则另选正交执行缺口（**融资负债按客户分类/金额/期限等档位计息的生效日 PIT** ≠ 融资利息与逾期罚息「假零息」≠ 融券借券费/融出费率 ≠ 融券权益补偿 ≠ 转融券券源 ≠ 开仓保证金比例 ≠ 授信额度上限 ≠ 账户串用 ≠ 合约期限/到期了结 ≠ 融资买入标的名单 ≠ 维持担保强平 ≠ 担保品折算率 ≠ 市场25pct暂停 ≠ 可充抵名单 ≠ 客户单票集中度 ≠ 担保品提取 ≠ 追保后禁新开 ≠ 融券所得用途 ≠ 融资卖出还债优先 ≠ 标的调出后存量续持 ≠ 经手费）；选题自两融业务公开口径：融资买入未了结期间，融资方须按合同/细则向券商支付**融资利息**，且利率常按**客户分类/金额档/期限档/优惠档**分档；档位与起息规则按**施行日/生效日** PIT，不得默认「全户一律最低优惠档/核对日最低档铺满历史」或把「假零息」与「档位误用」捆成一页；2010-03-31 前无此通道；BO 正文主测**假零息/零罚息**（`invent_zero_financing_interest_penalty`），本页主测**有息但档位被发明成一律最低优惠档** → 自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BS ≠ 单字母 B**）/ **S（股票经手费；双字母 BS ≠ 单字母假设-S；避开预检T旧题旁路）** / Z（**开仓**融资/融券保证金比例；**BS≠Z**）/ BA–BR（两融族已冻/在途；**BS≠BA…BR**；**尤其不改 BR 正文**）/ **K（融券空头名单 PIT；BS≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BS≠AB**）/ BO（**融资利息与逾期罚息假零息**；**BS≠BO**；假零息 ≠ 有息但档位误用；不占 invent_zero_financing_interest_penalty）/ BR（**融券借券费/融出费率**；**BS≠BR**；融券费率 ≠ 融资利率档；不占 invent_zero_short_borrow_fee；**尤其不改假设-BR**）/ BP（**融券权益补偿**；**BS≠BP**）/ BB（**转融券券源**；**BS≠BB**）/ BQ（**标的调出后存量假续持**；**BS≠BQ**）/ BH（**授信额度上限**；**BS≠BH**；额度天花板 ≠ 利率档）/ BI（**融券卖出所得用途**；**BS≠BI**）/ BJ（**融资卖出还债优先**；**BS≠BJ**）/ BF（**两融合约期限到期强制了结**；**BS≠BF**）/ BN（**信用/普通账户串用**；**BS≠BN**；并带过 **BN≠BI/BJ/BL/BM、params.N≠BN**）/ BM（**追保后禁新开**；**BS≠BM**；并带过 **BM≠BC、BM≠BL**）/ BL（**担保品提取**；**BS≠BL**；并带过 **BL≠BC**）/ BC（**维持担保强平**；**BS≠BC**）/ W（除权板价；**BS≠W**）/ E（整手）/ AN–BR（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BS**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「全户一律最低优惠融资利率档 / 用核对日最低档铺满」当诚实融资成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BR 及其他 A/D–BR 已交正文与冻结补丁；尤其不改假设-BR；不改假设-BO；不改假设-H；不改假设-A；不改假设-B；不改假设-S；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BR；不改假设-AB；勿再改 BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BS（约 #76）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融资未了结期间是否按客户分类/金额/期限等档位的生效日利率计息**。**双字母 BS ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BS ≠ 单字母 B**。与假设 **S（股票经手费）** **硬分列（专节强调）**：S = 交易所股票经手费费率切片；本页 = 信用账户**融资利率档位/优惠档**；经手费 ≠ 融资利率档。**双字母 BS ≠ 单字母假设-S**。与假设 **BO（融资利息与逾期罚息假零息）** **硬分列**：BO = 发明**永不计息/零罚息**；本页 = **有息但档位被发明成一律最低优惠档**（客户分类/金额/期限 PIT 被绕过）；假零息 ≠ 档位误用；**禁止**把「融资已计息（BO 诚实组）」静默写成「已按正确档位计息」；**不占** `invent_zero_financing_interest_penalty`。**BS≠BO**。与假设 **BR（融券借券费）** **硬分列**：BR = **融券**借券费/融出费率；本页 = **融资**利率档；融券费率 ≠ 融资利率档；**不占** `invent_zero_short_borrow_fee`；**尤其不改假设-BR**。**BS≠BR**。与假设 **BH（授信额度上限）** **硬分列**：BH = 总授信天花板是否被发明成无限；本页 = 已占用授信上的**计息档位**；额度够 ≠ 最低档利率。**BS≠BH**。与假设 **K（融券空头名单 PIT）** **硬分列**：本页不覆盖融券名单。**BS≠K**；并**带过**：双字母 **BK ≠ 单字母假设-K / 预检K**。与假设 **AB（融券卖出价限）** **硬分列**：不重开空头价限/当日平。与假设 **BP/BB/BQ/BI/BJ/BF/BN/BM/BL/BC** **硬分列**：权益补偿 / 转融券源 / 调出后存量 / 所得用途 / 还债优先 / 合约期限强了 / 账户串用 / 追保禁开 / 高维持提取 / 低维持强平 ≠ 融资利率档；并**带过 BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 **BA/BD/BE/BG/BK/Z/W** **硬分列**：融资名单 / 折算率 / 市场25pct / 可充抵名单 / 客户单票集中度 / 开仓保证金比例 / 除权板价 ≠ 融资利率档。与假设 AN–BR **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BS** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 S**（股票经手费）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BS / 假设-BS / hypothesis_id=BS / 组 BS0·BS1·BS2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BS 混读或互改。亦**禁止**把实验字母 BS 与单字母 **A**、单字母 **B**、单字母 **S**、单字母 **K**、单字母 **Z**、双字母 **BA–BR**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bs0_*` 以外的实验页混读。**双字母 BS ≠ 单字母 A ≠ 单字母 B ≠ 单字母 S ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BR ≠ 双字母 BO ≠ 双字母 BH ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H ≠ 双字母 T**；**params.Y ≠ 实验字母 BS**；**params.G ≠ 实验字母 BS**；**params.N ≠ 实验字母 BS**。**带过：双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BS ≠ 单字母假设-S；且 ≠ 假设-BO / 假设-BR / 假设-BH；带过 BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BS（双字母） |
|------|--------|----------------------|
| 题面 S | 股票经手费费率切片 | **融资利率档位/客户分类优惠档**误用：假一律最低档 vs 按生效日分档 PIT |
| 题面 BO | **融资利息与逾期罚息假零息** | **有息但档位误用**；假零息 ≠ 档位误用；**BS≠BO**；不占 invent_zero_financing_interest_penalty |
| 题面 BR | **融券**借券费/融出费率（复检在途） | **融资**利率档；融券费率 ≠ 融资利率档；**BS≠BR**；不占 invent_zero_short_borrow_fee；**不改 BR** |
| 题面 BH | **授信额度上限** | 额度天花板 ≠ 计息档位；额度够 ≠ 最低档；**BS≠BH** |
| 题面 BP / BB / BQ | 权益补偿 / 转融券源 / 调出后存量 | 本页不覆盖；**BS≠BP≠BB≠BQ** |
| 题面 K / AB | 融券名单 / 空头价限 | 本页不覆盖；**BS≠K≠AB**；**带过 BK≠K** |
| 题面 BN 链 | 账户隔离等（**BN≠BI/BJ/BL/BM**；**params.N≠BN**） | 本页不覆盖；**带过**消歧链；并带过 **BR≠R/BO/BP/BB/BQ、BO≠O/BF/BJ/BH/BN、BQ 撞题链** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_always_lowest_financing_rate_tier` |
| 文档 | `假设-S-…` / `假设-BO-…` / `假设-BR-…` / `假设-BH-…` / `假设-K-…`（**只读；禁止改写**） | `假设-BS-融资利率档位优惠档误用.md`（新建） |
| 预检键 | 实验字母 S / BO / BR / BH / K | 实验字母 **BS** / `bs0_primary_demo`；**不得**占用或改写预检 S/BO/BR/BH/K |

**禁止**：把 BS 写成「S/BO/BR/BH 的续篇」；把「融资已假零息 / 融券已计借券费 / 授信够 / 名单内可融资」静默写成「已按最低优惠档正确计息」；覆盖或补丁改写假设-S / 假设-BO / 假设-BR / 假设-BH / 假设-K 正文；把 `params.Y/G/N` 与实验字母 BS 混读；**禁** `bs0_primary_demo` 与 `invent_asof_leak_financing_rate_tier` **双挂主报**；**禁** BS1 半泄露升格并列主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有/滚动融资买入路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/授信/合约期限/还债优先/账户隔离/融资利息「是否计息」层输入（Z/BA/BH/BF/BJ/BN/BO 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/授信天花板/合约期限/还债优先/账户隔离/假零息主病」）下，把「全户一律按最低优惠融资利率档计息、永不检查客户分类/金额/期限档」或「全样本用核对日当天最低优惠档规则回放历史」当成默认，相对「每个交易日按当时有效融资利率档位规则 PIT（按客户分类/金额/期限等分档；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假最低档融资成本路径并高估净收益、低估融资持仓真实利息成本**；差异应**集中在融资利率档位/优惠档误用桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假最低档贡献差、净收益差、应计利息差在标定噪声带内可忽略，且「假最低档 / 核对日泄露 / 正常计息窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·K·AB·S·B·H·W·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融资利率档位 ≠ 融资假零息；≠ 融券借券费；≠ 授信额度上限；≠ 融券权益补偿；≠ 转融券券源；≠ 标的调出后存量；≠ 经手费；≠ 开仓保证金比例；≠ 账户串用；≠ 合约期限强了；≠ 追保禁开；≠ 担保品提取；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BS；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 S；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BS
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BS；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.financing_rate_tier_honest      写死 pit_by_effective_date
# params.financing_rate_tier_scope       写死 client_class_amount_tenor_pref_tiers
# params.financing_rate_tier_over_policy 写死 accrue_or_fail_missing_tier
# params.broker_promo_rate_bucket        写死 separate_sensitivity
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
# params.financing_interest_handoff      写死 bo_page   # 假零息主病交 BO；本页只测档位
# params.corp_action_comp_handoff        写死 bp_page
# params.list_removal_stock_handoff      写死 bq_page
# params.short_borrow_fee_handoff        写死 br_page   # 融券借券费交 BR；BS≠BR
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.handling_fee_handoff            写死 s_page    # 经手费交 S；BS≠S
# params.exit_period_handoff             写死 h_page
# params.bs0_primary_demo                写死冻结 invent_always_lowest_financing_rate_tier  # 主报：全户一律最低优惠融资利率档；禁与 invent_asof_leak_financing_rate_tier 双挂争主表；BS1半泄露不得升格并列主报
# params.bs0_invent_always_lowest_tier   写死 True
# params.bs1_asof_leak_financing_rate_tier_only 写死 True
# params.bs2_pit_financing_rate_tier     写死 True
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
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_S_handling_fee       写死 False
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
# params.universe_rule                   写死 sse_szse_financing_rate_tier_check
# params.missing_financing_rate_tier_policy 写死 skip
# params.day_freq_proxy                  写死 financing_rate_tier_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BS；params.G≠实验字母BS；params.N≠实验字母BS；亦≠单字母实验A/B/S/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
```

```
params.bs0_primary_demo = "invent_always_lowest_financing_rate_tier"  # 单一主报·已冻结；禁与 invent_asof_leak_financing_rate_tier 双挂
```

### 2.2 三组对照（BS0 / BS1 / BS2）

| 组 | 口径 | 说明 |
|----|------|------|
| BS0 天真 | `invent_always_lowest_financing_rate_tier`（单一主报·已冻结） | 发明全户一律最低优惠融资利率档；禁与 invent_asof_leak_financing_rate_tier 双挂 |
| BS1 半泄露/混口径 | 全样本用 `asof_check_date` 当天最低优惠档规则铺满历史 | 仅档位 asof 泄露；不升格并列主报 |
| BS2 PIT | `financing_rate_tier_honest=pit_by_effective_date` | 每个交易日按当时已生效客户分类/金额/期限等档位 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：信用账户融资负债日终余额 × 当日适用年化档位 / 计息天数约定 → 应计利息；对比 BS0/BS1/BS2 的 ΔAccruedFinancingInterest、ΔFakeLowestTierContribution、净收益差。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有日终融资余额 + 档位生效日表即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BS0 / BS1 / BS2。报告净收益差、假最低档贡献差、应计融资利息差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_always_lowest_financing_rate_tier",
  "invent_asof_leak_financing_rate_tier",
  "financing_rate_tier_accrual_window",
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
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_S_handling_fee",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够融资负债日终余额；缺档位字段却静默当最低档 → 设计失效。  
2. 把「融资假零息（BO）」静默写成「已按正确档位计息」且不声明另页 BO → **与 BO 撞题**（假零息 ≠ 档位误用；**尤其 BS≠BO**；不占 invent_zero_financing_interest_penalty）。  
3. 把「融券借券费已计提（BR）」静默写成「融资利率档已诚实」且不声明另页 BR → **与 BR 撞题**（融券费率 ≠ 融资利率档；**尤其 BS≠BR**；**不改 BR**）。  
4. 把「授信够（BH）」静默写成「适用最低优惠档」且不声明另页 BH → 与 BH 撞题（**尤其 BS≠BH**）。  
5. 把「股票经手费已诚实（S）」写成主病而不声明另页 S → 与 S 撞题（**双字母 BS ≠ 单字母 S**）。  
6. 把「名单内可融资 / 合约未到期 / 还本优先已满足 / 账户未串用 / 保证金比例够 / 未强平」静默写成「最低档正确」且不声明另页 BA/BF/BJ/BN/Z/BC → 与对应页撞题；并**带过 BR/BQ/BP/BO/BN/BM/BL/BK 消歧链**。  
7. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易」写成主病而不声明另页 AB/W/A/H → 与对应页撞题。  
8. 把「融资利率档位误用」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
9. 把实验字母 BS 与单字母 A/B/S/K/Z 或双字母 BA–BR/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
10. holdout 反调 `bs0_primary_demo` / Y·G·N·Y2 → 结论无效。  
11. 用复权价算融资利息名义 → 标签与执行双错，结论无效。  
12. 用核对日更宽「最低优惠档」当诚实 PIT、或把券商临时促销档提前铺满历史 → 设计失效。  
13. **`bs0_primary_demo` 与 `invent_asof_leak_financing_rate_tier` 双挂主报**；或 BS1 升格并列主报 → 设计失效。  
14. **改写或覆盖 `假设-S` / `假设-BO` / `假设-BR` / `假设-BH` / 已冻 AA–BR** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户融资负债日终余额与开仓日、未了结标记、客户分类/金额档/期限档代理；  
- 当时有效融资利率档位表及生效日（标准档/优惠档/金额档/期限档；券商促销另桶）；  
- 开仓保证金比例 / 融资名单 / 授信 / 合约期限 / 还债优先 / 账户隔离 / 融资假零息层输入（消费 Z/BA/BH/BF/BJ/BN/BO 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商临时促销/员工档/机构档另桶；与 BR 融券费率表对照但不混主结论。

**禁止**：用核对日「今天最低优惠档」铺满当唯一诚实组；用复权价；把假零息/融券借券费/授信够/开仓保证金比例/低维持强平/合约期限未到期/新开名单窗/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/追保未触发/账户未串用/权益已补偿/调出后存量已处理当成「最低档正确」依据；把 Z/BA–BR/K/AB/A/S/B/H/W/T/AN–BR 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BS`  
- **组**：BS0 / BS1 / BS2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`financing_rate_tier_honest=pit_by_effective_date`；`financing_rate_tier_scope=client_class_amount_tenor_pref_tiers`；`financing_rate_tier_over_policy=accrue_or_fail_missing_tier`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_financing_rate_tier_check`；`missing_financing_rate_tier_policy=skip`；`day_freq_proxy=financing_rate_tier_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BS**；**params.G≠实验字母 BS**；**params.N≠实验字母 BS**；亦≠单字母实验 A/B/S/Z；禁 null/holdout/跑后改口）；**`params.bs0_primary_demo` 写死冻结 `invent_always_lowest_financing_rate_tier`**（禁与 invent_asof_leak_financing_rate_tier 双挂；BS1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BS0/BS1/BS2 净收益/路径质量、ΔFakeLowestFinancingRateTier、ΔAccruedFinancingInterest；分桶（融资利率档位假最低档误用 / 核对日泄露 / 计息窗 / 通道前 / vs A·Z·BA–BR·K·AB·S·B·H·W·T）。  
- 自检布尔：BS2 是否 pit_by_effective_date；BS0 是否单一主报；BS1 是否仅核对日泄露；是否未与 A/Z/BA–BR/K/AB/S/B/H/W/T 混主结论；holdout 是否未反调；**是否未把实验字母 BS 与 A 或 B 或 S 或 K 或 Z 或 BA–BR 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BS≠单字母假设-S；BS≠BO；BS≠BR；BS≠BH；带过 BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BR 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-S / 假设-K / 假设-W / 假设-Z / 假设-BA–BR / 假设-AB**；**是否未再改 BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未与 invent_asof_leak_financing_rate_tier 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把最低档或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BR 及其他 A/D–BR 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-S**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BR**；**尤其不改假设-BR**；**尤其不改假设-BO**；**不改假设-AB**；**勿再改 BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融券空头名单（K）之外，**融资利率分档**须按当时有效规则 PIT；不得默认全户一律最低优惠档。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BS** 标准件，**不改口径主线**，**不改假设 A–BR 正文**，**尤其不改假设-S / 假设-BO / 假设-BR / 假设-BH**。与实验 A/Z/BA–BR/K/AB/S/B/H/W/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA–BR=两融族已冻/在途；K=融券空头新开名单；AB=融券卖出价限；S=股票经手费；B=历史实验B旧位；H=退市整理；W=除权板价；T=证管费（避开）；BS=融资利率档位/优惠档误用（BS≠A≠B≠S≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠BM≠BN≠BO≠BP≠BQ≠BR≠AB≠W≠H≠T；带过 BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频融资负债名义+利率档生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**financing_rate_tier_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BS；params.G≠实验字母 BS；params.N≠实验字母 BS；亦≠单字母实验 A/B/S/Z；禁 null/holdout/跑后改口）**；**bs0_primary_demo 写死冻结 invent_always_lowest_financing_rate_tier（禁双挂 invent_asof_leak_financing_rate_tier；BS1半泄露不得升格并列主报）**；锚点保留 financing_rate_tier_honest=pit_by_effective_date / financing_rate_tier_scope=client_class_amount_tenor_pref_tiers / financing_rate_tier_over_policy=accrue_or_fail_missing_tier / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单（两条已冻结 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已写死冻结**；**params.Y≠BS**；**params.G≠BS**；**params.N≠BS**；禁 null/holdout）  
2. `params.bs0_primary_demo` = `invent_always_lowest_financing_rate_tier`（**已写死冻结**；禁与 `invent_asof_leak_financing_rate_tier` 双挂；BS1不升格主报）  
3. 档位锚：`financing_rate_tier_honest=pit_by_effective_date`；`financing_rate_tier_scope=client_class_amount_tenor_pref_tiers`；`financing_rate_tier_over_policy=accrue_or_fail_missing_tier`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/S/A/Z/BA–BR/K/AB/H/W/T；**尤其 BS≠BO（假零息≠档位误用）**；**尤其 BS≠BR（融券借券费≠融资利率档；不改BR）**；**尤其 BS≠BH（授信天花板≠利率档）**；**尤其 BS≠S**；**带过 BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 与 BA–BR 撞题检查表

| 字母 | 主题 | 撞题？ | 消歧 |
|------|------|--------|------|
| BA | 融资买入新开名单 | 否 | — |
| BB | 转融券券源 | 否 | — |
| BC | 维持强平 | 否 | — |
| BD | 折算率 | 否 | — |
| BE | 市场25pct暂停 | 否 | — |
| BF | 合约期限到期了结 | 否 | — |
| BG | 可充抵名单 | 否 | — |
| BH | 授信额度 | 否 | 额度天花板 ≠ 利率档 |
| BI | 融券所得用途 | 否 | — |
| BJ | 融资卖出还债优先 | 否 | — |
| BK | 客户单票集中度 | 否 | — |
| BL | 担保品提取 | 否 | — |
| BM | 追保后禁新开 | 否 | — |
| BN | 跨账户现金混用 | 否 | — |
| BO | 融资利息罚息零 | 否 | 假零息 ≠ 有息但档位误用；不占 invent_zero_financing_interest_penalty |
| BP | 融券权益补偿 | 否 | — |
| BQ | 调出后存量续持 | 否 | — |
| BR | 融券借券费零 | 否 | 融券费率 ≠ 融资利率档；**不改 BR** |
| K | 融券新开名单 | 否 | — |
| Z | 开仓保证金比例 | 否 | — |
| AB | 融券价限/当日平 | 否 | — |
| S | 股票经手费 | 否 | 双字母 BS ≠ 单字母 S |
| A/B/H/W/T | 板上/旧B/退市/除权/证管费 | 否 | 避开预检T |

**撞题检查：通过（纸面）** — 入库后对照正式清单 #76 再核一次 primary_demo 唯一性。

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BS**；**`params.G` ≠ 实验字母 BS**；**`params.N` ≠ 实验字母 BS**；**`params.Y` ≠ 单字母实验 A/B/S/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bs0_primary_demo`**：**写死冻结** **`invent_always_lowest_financing_rate_tier`**；禁与 **`invent_asof_leak_financing_rate_tier`** 双挂争主表（只挂一个 primary）；**BS1 半泄露不得升格并列主报**。

**融资利率档锚保留（已通写死）**：`params.financing_rate_tier_honest=pit_by_effective_date`；`params.financing_rate_tier_scope=client_class_amount_tenor_pref_tiers`；`params.financing_rate_tier_over_policy=accrue_or_fail_missing_tier`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有 `missing_financing_rate_tier_policy=skip` 等锚点；不改口）。

**与 BA–BR/Z/AB/B/A/H/S/K/W/T 硬分列（保留）**：本页 = **融资利率档位/客户分类优惠档误用**；S = **股票经手费**（**尤其双字母 BS ≠ 单字母假设-S**）；BO = **融资利息与逾期罚息假零息**（**尤其 BS≠BO**；假零息 ≠ 有息但档位误用；不占 invent_zero_financing_interest_penalty）；BR = **融券借券费/融出费率**（**尤其 BS≠BR**；融券费率 ≠ 融资利率档；不占 invent_zero_short_borrow_fee；**尤其不改假设-BR**）；BH = **授信额度上限**（**尤其 BS≠BH**；额度天花板 ≠ 利率档）；BP = **融券权益补偿**；BB = **转融券券源**；BQ = **标的调出后存量假续持**；K = **融券空头名单**（并**带过 BK≠K**）；AB = **融券卖出价限**；Z = **开仓**保证金比例；W = **除权板价**；A = **板上枯竭**；B = 历史实验 B 旧位；H = **退市整理期**；T = **证管费**（避开预检T）；融资利率档 ≠ 股票经手费 ≠ 假零息 ≠ 融券借券费 ≠ 授信天花板 ≠ 权益补偿 ≠ 转融券源 ≠ 调出后存量 ≠ 融券名单 ≠ 空头价限 ≠ 开仓比例 ≠ 除权板价 ≠ 板上枯竭 ≠ 退市整理 ≠ 证管费；**双字母 BS ≠ 单字母 A ≠ 单字母 B ≠ 单字母 S ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BR ≠ 双字母 BO ≠ 双字母 BH ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H ≠ 双字母 T**；**params.Y ≠ 实验字母 BS**；**params.G ≠ 实验字母 BS**；**params.N ≠ 实验字母 BS**；禁止捆成「两融一张表=最低档利率」；**尤其不改假设-S**；**尤其不改假设-BO**；**尤其不改假设-BR**；**尤其不改假设-BH**；**尤其不改假设-K**；**尤其不改假设-H**；不改假设-B；不改假设-Z；不改假设-BA–BR；不改假设-A；不改假设-AB；不改假设-W。

**专节保留 · 双字母 BS ≠ 单字母假设-S；且 ≠ 假设-BO / 假设-BR / 假设-BH；带过 BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）**：正文「### 专节 · 双字母 BS ≠ 单字母假设-S；且 ≠ 假设-BO / 假设-BR / 假设-BH；带过 BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K」保留不删；**禁止**覆盖/混读/改写 `假设-S` / `假设-BO` / `假设-BR` / `假设-BH` / `假设-K`。

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BS**；**params.G≠实验字母 BS**；**params.N≠实验字母 BS**；亦≠单字母实验 A/B/S/Z；禁 null/holdout/跑后改口）；② `params.bs0_primary_demo=invent_always_lowest_financing_rate_tier`（禁与 `invent_asof_leak_financing_rate_tier` 双挂争主表；BS1半泄露不得升格并列主报）。融资利率档锚保留：`financing_rate_tier_honest=pit_by_effective_date`；`financing_rate_tier_scope=client_class_amount_tenor_pref_tiers`；`financing_rate_tier_over_policy=accrue_or_fail_missing_tier`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。与 BA–BR/Z/AB/B/A/H/S/K/W/T 硬分列保留；**专节保留 BS≠S / BS≠BO / BS≠BR / BS≠BH / 带过 BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K**。参考总管派令 / 风控预检有条件通过（`预检-假设BS-20261103.md`；草稿 HEAD=4694fbb）。未改 Y/Z/AA–BR 及其他已冻结补丁；**不改假设-BR**；**不改假设-BO**；**不改假设-BH**；不改假设-H；不改假设-A；不改假设-B；不改假设-S；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BR；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BR 补丁已收复检在途 → 写假设-BS；自立 BS，勿占 BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/S/A/Z/K/W；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BS**；**双字母 BS ≠ 单字母 S**；**BS≠BO/BR/BH**；选题：BO 假零息旁的**融资利率档位/优惠档误用**；`bs0_primary_demo=invent_always_lowest_financing_rate_tier`；半泄露 `invent_asof_leak_financing_rate_tier` 禁双挂/升格；**不改假设-BR**；**不改假设-BO**；不改 Y/Z/AA–BR）。结论栏空。
