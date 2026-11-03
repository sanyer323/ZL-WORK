# 假设 BP · 融券权益补偿（现金红利/红股/配股）误开 / 用核对日权益补偿规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BO 补丁已收（复检在途）、写下一纸面 BP；清单撞题规则另选正交执行缺口（**融券未了结期间对出借方的现金红利/红股/配股等权益补偿** ≠ 融资利息与逾期罚息 ≠ 融券卖出所得用途 ≠ 融资买入卖出还债优先 ≠ 转融券券源 ≠ 融券空头名单 ≠ 融券卖出价限 ≠ 除权日复权价误判板 ≠ 开仓保证金比例 ≠ 授信额度 ≠ 账户串用 ≠ 合约期限/到期了结 ≠ 融资买入标的名单 ≠ 维持担保强平 ≠ 担保品折算率 ≠ 市场25pct暂停 ≠ 可充抵名单 ≠ 客户单票集中度 ≠ 担保品提取 ≠ 追保后禁新开）；选题自两融业务公开口径：融券卖出未了结期间，标的发生现金分红/送转红股/配股等，融券方须按合同/细则向出借方做**权益补偿**（现金补偿或等值处理）；补偿规则与除权/股权登记口径按**生效日/除权除息日** PIT，不得默认「永不补偿/零补偿」或用核对日更宽免补偿规则回放全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BP ≠ 单字母 B**）/ **P（指数点位停牌假成交权重；双字母 BP ≠ 单字母假设-P）** / Z（**开仓**融资/融券保证金比例；**BP≠Z**）/ BA–BO（两融族已冻/在途；**BP≠BA…BO**）/ **K（融券空头名单 PIT；BP≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BP≠AB**）/ W（**除权日复权价误判板**；**BP≠W**；板上价/涨跌停判定 ≠ 融券权益补偿负债）/ BO（**融资利息与逾期罚息**；**BP≠BO**；融资计息 ≠ 融券权益补偿；BO 正文已明示权益补偿另桶）/ BI（**融券卖出所得用途**；**BP≠BI**；所得怎么用 ≠ 是否欠出借方权益补偿）/ BJ（**融资卖出还债优先**；**BP≠BJ**）/ BB（**转融券券源**；**BP≠BB**）/ BF（**两融合约期限到期强制了结**；**BP≠BF**）/ BH（**授信额度**；**BP≠BH**）/ BN（**信用/普通账户串用**；**BP≠BN**；并带过 **BN≠BI/BJ/BL/BM、params.N≠BN**）/ BM（**追保后禁新开**；**BP≠BM**；并带过 **BM≠BC、BM≠BL**）/ BL（**担保品提取**；**BP≠BL**；并带过 **BL≠BC**）/ BC（**维持担保强平**；**BP≠BC**）/ E（整手）/ AN–BO（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BP**  
状态：**草稿 · 待预检**（结论栏空；禁止把「融券永不做权益补偿/零补偿/用核对日免补偿铺满」当诚实空头成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BO 及其他 A/D–BO 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-P；不改假设-O；不改假设-N；不改假设-K；不改假设-M；不改假设-W；不改假设-Z；不改假设-BA–BO；不改假设-AB；勿再改 BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BP（约 #73）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融券未了结期间是否按生效日向出借方做现金红利/红股/配股权益补偿**。**双字母 BP ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BP ≠ 单字母 B**。与假设 **P（指数点位停牌假成交权重）** **硬分列（专节强调）**：P = 指数点位/权重在停牌日的假成交或假权重；本页 = 信用账户**融券权益补偿负债**；指数权重 ≠ 权益补偿。**双字母 BP ≠ 单字母假设-P**。与假设 **W（除权日复权价误判板）** **硬分列**：W = 除权除息后**涨跌停价/板上价**是否用错复权口径；本页 = 融券方对出借方的**补偿义务是否计提**；板价误判 ≠ 补偿义务。**BP≠W**。与假设 **K（融券空头名单 PIT）** **硬分列**：K = 当日是否在**交易所融券标的名单**内；本页 = 已开融券后遇权益事件是否补偿；名单内可空 ≠ 零补偿。**BP≠K**；并**带过**：双字母 **BK ≠ 单字母假设-K / 预检K**。与假设 **BO（融资利息与逾期罚息）** **硬分列**：BO = **融资**负债计息/逾期罚息；本页 = **融券**权益补偿；融资计息 ≠ 融券补偿；**禁止**把「融资已计息」静默写成「融券权益已补偿」。与假设 **BI（融券卖出所得用途）** **硬分列**：BI = 融券所得资金**怎么用**；本页 = 是否另欠出借方权益补偿；用途放开 ≠ 零补偿。与假设 **BJ（融资买入卖出还债优先）** **硬分列**：BJ = 融资卖出所得**优先还本**；本页 = 融券权益补偿；还本 ≠ 补偿。与假设 **BB（转融券券源）** **硬分列**：BB = 转融通/券源是否可借；本页 = 借到之后的权益事件补偿；有券 ≠ 零补偿。与假设 **AB（融券卖出价限）** **硬分列**：不重开空头价限/当日平。与假设 **BF/BH/BN/BM/BL/BC** **硬分列**：合约期限强了 / 授信 / 账户串用 / 追保禁开 / 高维持提取 / 低维持强平 ≠ 融券权益补偿；并**带过 BO≠O/BF/BJ/BH/BN、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 **BA/BD/BE/BG/BK/Z** **硬分列**：融资名单 / 折算率 / 市场25pct / 可充抵名单 / 客户单票集中度 / 开仓保证金比例 ≠ 融券权益补偿。与假设 AN–BO **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BP** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 P**（指数点位停牌假成交权重）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BP / 假设-BP / hypothesis_id=BP / 组 BP0·BP1·BP2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BP 混读或互改。亦**禁止**把实验字母 BP 与单字母 **A**、单字母 **B**、单字母 **P**、单字母 **K**、单字母 **Z**、双字母 **BA–BO**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bp0_*` 以外的实验页混读。**双字母 BP ≠ 单字母 A ≠ 单字母 B ≠ 单字母 P ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BO ≠ 双字母 BI ≠ 双字母 BJ ≠ 双字母 BB ≠ 双字母 W ≠ 双字母 AB**；**params.Y ≠ 实验字母 BP**；**params.G ≠ 实验字母 BP**；**params.N ≠ 实验字母 BP**。**带过：双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BP ≠ 单字母假设-P；且 ≠ 假设-BO / 假设-W / 假设-BI；带过 BO≠O/BF/BJ/BH/BN、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BP（双字母） |
|------|--------|----------------------|
| 题面 P | 指数点位/停牌假成交权重 | **融券权益补偿**误开：假零补偿 vs 按除权/生效日 PIT 计提现金红利/红股/配股补偿 |
| 题面 BO | **融资**利息与逾期罚息计提 | **融券**权益补偿；融资计息 ≠ 融券补偿；**BP≠BO**；BO 已明示权益补偿另桶 |
| 题面 W | 除权日**复权价/板上价**误判 | 补偿**义务是否计提**；板价判定 ≠ 补偿负债；**BP≠W** |
| 题面 BI | 融券所得资金**用途**限制 | 是否欠出借方权益补偿；用途 ≠ 补偿；**BP≠BI** |
| 题面 BJ | 融资卖出所得**优先还本** | 融券权益补偿；还本 ≠ 补偿；**BP≠BJ** |
| 题面 BB / K / AB | 转融券源 / 融券名单 / 空头价限 | 有券可空 / 价限 ≠ 零补偿；**BP≠BB≠K≠AB**；**带过 BK≠K** |
| 题面 BN 链 | 账户隔离等（**BN≠BI/BJ/BL/BM**；**params.N≠BN**） | 本页不覆盖；**带过**消歧链；并带过 **BO≠O/BF/BJ/BH/BN** |
| 题面 BM/BL/BC | 追保禁开 / 高维持提取 / 低维持强平（**BM≠BC、BM≠BL、BL≠BC**） | 权益补偿；本页不覆盖；**带过**上述分列 |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_zero_short_corp_action_comp` |
| 文档 | `假设-P-…` / `假设-BO-…` / `假设-W-…` / `假设-BI-…` / `假设-BJ-…` / `假设-BB-…` / `假设-K-…` / `假设-BK-…`（**只读；禁止改写**） | `假设-BP-融券权益补偿现金红利红股误开.md`（新建） |
| 预检键 | 实验字母 P / BO / W / BI / BJ / BB / K / BK | 实验字母 **BP** / `bp0_primary_demo`；**不得**占用或改写预检 P/BO/W/BI/BJ/BB/K/BK |

**禁止**：把 BP 写成「P/BO/W/BI 的续篇」；把「融资已计息 / 所得用途已受限 / 除权板价已诚实 / 名单内可空 / 有转融券源」静默写成「融券权益零补偿」；覆盖或补丁改写假设-P / 假设-BO / 假设-W / 假设-BI / 假设-BJ / 假设-BB / 假设-K / 假设-BK 正文；把 `params.Y/G/N` 与实验字母 BP 混读。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有/滚动融券空头路径、同一未复权价、同一 T+1、同一开仓保证金比例与融券名单/转融券源/融券价限/融资计息/所得用途/账户隔离输入（Z/K/BB/AB/BO/BI/BN 层诚实或显式旁路声明「本页不重开开仓比例/融券名单/转融券源/空头价限/融资利息/融券所得用途/账户隔离/除权板价」）下，把「融券永不做现金红利/红股/配股权益补偿、补偿成本恒为 0」或「全样本用核对日当天权益补偿规则（含券商当日更宽免补偿口径）回放历史」当成默认，相对「每个交易日/每个权益事件按当时有效融券权益补偿规则 PIT（现金红利补偿、红股/送转补偿、配股补偿按生效日或除权除息日；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假零权益补偿空头路径并高估净收益、低估融券持仓真实成本与除权窗口负债**；差异应**集中在融券权益补偿（现金红利/红股/配股）误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假零补偿贡献差、净收益差、应计权益补偿差在标定噪声带内可忽略，且「假零补偿 / 核对日泄露 / 现金红利窗 / 红股送转窗 / 配股窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·K·AB·W·P·B·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融券权益补偿 ≠ 融资利息罚息；≠ 除权板价；≠ 融券所得用途；≠ 融资还债优先；≠ 转融券券源；≠ 融券名单；≠ 空头价限；≠ 开仓保证金比例；≠ 授信额度；≠ 账户串用；≠ 合约期限强了；≠ 追保禁开；≠ 担保品提取；≠ 指数停牌权重；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；待预检冻结；建议终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BP；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 P；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BP
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BP；≠ 单字母假设-N（收盘机制）；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.short_corp_action_comp_honest   写死 pit_by_ex_or_effective_date
# params.short_corp_action_scope         写死 cash_div_bonus_share_rights_issue
# params.short_corp_action_over_policy   写死 accrue_or_fail_missing_event
# params.broker_waive_comp_bucket        写死 separate_sensitivity
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
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.index_halt_weight_handoff       写死 p_page
# params.exit_period_handoff             写死 h_page
# params.bp0_primary_demo                建议 invent_zero_short_corp_action_comp  # 主报：融券权益永不补偿/零补偿；禁与 invent_asof_leak_short_corp_action_comp 双挂争主表；BP1半泄露不得升格并列主报
# params.bp0_invent_zero_short_corp_action_comp 写死 True
# params.bp1_asof_leak_short_corp_action_comp_only 写死 True
# params.bp2_pit_short_corp_action_comp  写死 True
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
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_P_index_halt         写死 False
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
# params.merge_with_Q_cb                 写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_D_halt_timing        写死 False
# params.universe_rule                   写死 sse_szse_short_corp_action_comp_check
# params.missing_corp_action_policy      写死 skip
# params.day_freq_proxy                  写死 short_corp_action_comp_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BP；params.G≠实验字母BP；params.N≠实验字母BP；亦≠单字母实验A/B/P/Z；禁null/holdout/跑后改口；待预检写死冻结
# params.date_start / date_end           写死主窗并待冻结 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期并待冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

### 2.2 三组对照（BP0 / BP1 / BP2）

| 组 | 角色 | 行为 |
|----|------|------|
| **BP0** | 天真主报 | 按 `bp0_primary_demo=invent_zero_short_corp_action_comp`（单一主报·待预检冻结）：融券权益永不补偿、零现金/零红股/零配股补偿；**单一主报**；禁与半泄露双挂 |
| **BP1** | 半泄露 | 仅 `invent_asof_leak_short_corp_action_comp`：全样本用核对日权益补偿规则回放；**不得升格并列主报** |
| **BP2** | 诚实 PIT | `short_corp_action_comp_honest=pit_by_ex_or_effective_date`：按除权/生效日规则计提现金红利/红股/配股补偿；缺字段 skip |

### 2.3 标签与样本区间口径

- **PIT 锚**：权益事件股权登记日/除权除息日、补偿规则生效日；`asof_check_date=2026-10-16` 仅用于 BP1 半泄露对照，**不得**当 BP2 诚实组。  
- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/K/BB/AB/BO/BI/BN/W）。  
- **额度窗内日频可落点（写明但不真跑）**：日终融券空头数量 × 当日生效现金红利每股金额 → 当日应计现金补偿；红股/送转按比例增加应还券数量或等值现金补偿；配股按认购/补偿细则记负债；缺事件字段 → skip（敏感性另桶）。  
- **通道前**：`margin_channel_start=2010-03-31` 前无本页融券权益补偿通道。  
- **px_basis=unadj**；禁止用复权价同时「抹掉」除权又「免掉」补偿（与 W 板价题分列：本页测补偿义务，不测板价）。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

BP0 相对 BP2：假零补偿贡献差、净收益高估、应计现金/红股/配股补偿漏计差显著超过 `params.Y/G/N/Y2` 门槛带，且差异集中在「融券权益补偿（现金红利/红股/配股）误开」桶；BP1 相对 BP2 的核对日泄露贡献可单独度量且不得冒充主报。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 BO 融资计息、W 除权板价、BI 所得用途、BJ 还本优先、BB 券源、K 名单、T 证管费等他页桶吸走；或 holdout 反调 `bp0_primary_demo` / Y·G·N·Y2；或 BP0 与 asof_leak 双挂主报。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1、同一未复权价，对照 BP0 / BP1 / BP2；报告名义净收益差、ΔFakeZeroCorpActionComp、ΔCashDivComp、ΔBonusShareComp、ΔRightsIssueComp；按分桶报告。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

- `invent_zero_short_corp_action_comp`  
- `invent_asof_leak_short_corp_action_comp`  
- `cash_dividend_window`  
- `bonus_share_window`  
- `rights_issue_window`  
- `pre_margin_channel`  
- `vs_A_limit_fill` / `vs_Z_margin_ratio` / `vs_BA_margin_buy_list` / `vs_BB_refinance` / `vs_BC_maint_force` / `vs_BD_haircut` / `vs_BE_balance_pause` / `vs_BF_contract_term` / `vs_BG_collateral_list` / `vs_BH_credit_quota` / `vs_BI_short_proceeds` / `vs_BJ_financing_sale_repay` / `vs_BK_client_conc` / `vs_BL_collateral_withdraw` / `vs_BM_margin_call_open_ban` / `vs_BN_cross_account` / `vs_BO_financing_interest` / `vs_K_shortable` / `vs_AB_short_px` / `vs_W_exright` / `vs_P_index_halt` / `vs_B_legacy` / `vs_H_exit` / `vs_T_csrc_fee`

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺权益事件/补偿字段静默当零补偿。  
2. 把「融资已计息 / 所得用途已限 / 除权板价已诚实 / 名单内可空 / 有转融券源 / 授信够 / 未强平」写成「零权益补偿」。  
3. 把融资利息/罚息（BO）写成主病 → 与 BO 撞题。  
4. 把除权板价/复权（W）写成主病 → 与 W 撞题。  
5. 把融券所得用途（BI）写成主病 → 与 BI 撞题。  
6. 把融资卖出还债优先（BJ）写成主病 → 与 BJ 撞题。  
7. 把转融券券源（BB）或融券名单（K）写成主病 → 与 BB/K 撞题。  
8. 把指数停牌权重（P）写成主病 → 与 P 撞题（**双字母 BP ≠ 单字母 P**）。  
9. 把「证管费误抽」写成主病 → **撞预检T**。  
10. 实验字母 BP 与单字母 A/B/P/K/Z 或双字母 BA–BO/AB/W 或 `params.Y/G/N` 混读互改。  
11. holdout 反调 `bp0_primary_demo` / Y·G·N·Y2。  
12. 用复权价既抹除权又免补偿，或把 W 板价差当成本页主结论。  
13. 用核对日免补偿规则当诚实 PIT。  
14. **改写或覆盖**已冻/在途 AA–BO / 假设-P / 假设-BO / 假设-W / 假设-H / 假设-K 等 → 硬边界违规。  
15. `bp0_primary_demo` 与 `invent_asof_leak_short_corp_action_comp` **双挂主报**；或 BP1 升格并列主报。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融券空头日终数量/名义代理、开仓日与未了结标记；  
- 现金红利/送转红股/配股事件表（股权登记日、除权除息日、每股金额或比例）及当时有效融券权益补偿规则生效日；  
- 开仓保证金比例 / 融券名单 / 转融券源 / 空头价限 / 融资计息 / 融券所得用途 / 账户隔离 / 除权板价输入（消费 Z/K/BB/AB/BO/BI/BN/W 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商更宽免补偿/现金替代细则另桶；融资侧股息到账另桶（本页主测**融券方对出借方的补偿义务**，不主测融资多头股息到账，亦不主测融资利息）。

**禁止**：用核对日「今天免补偿」铺满当唯一诚实组；用复权价抹掉补偿义务；把开仓比例/低维持强平/高维持提取/折算率/可充抵名单/融资名单/转融券通道/市场25pct/合约期限展期/总授信/融券所得用途/融资卖出还债优先/客户单票集中度/追保禁开/账户串用/融资计息/除权板价当成零补偿依据；把 Z/BA–BO/K/AB/A/P/B/H/W/T 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BP`  
- **组**：BP0 / BP1 / BP2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`short_corp_action_comp_honest=pit_by_ex_or_effective_date`；`short_corp_action_scope=cash_div_bonus_share_rights_issue`；`short_corp_action_over_policy=accrue_or_fail_missing_event`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`index_halt_weight_handoff=p_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_short_corp_action_comp_check`；`missing_corp_action_policy=skip`；`day_freq_proxy=short_corp_action_comp_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`（待预检写死冻结）**（**params.Y≠实验字母 BP**；**params.G≠实验字母 BP**；**params.N≠实验字母 BP**；亦≠单字母实验 A/B/P/Z；禁 null/holdout/跑后改口）；**`params.bp0_primary_demo` 建议 `invent_zero_short_corp_action_comp`（待预检写死冻结）**（禁与 invent_asof_leak_short_corp_action_comp 双挂；BP1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BP0/BP1/BP2 净收益/成本质量、ΔFakeZeroCorpActionComp、ΔCashDivComp、ΔBonusShareComp、ΔRightsIssueComp；分桶（权益补偿误开 / 核对日泄露 / 现金红利 / 红股送转 / 配股 / 通道前 / vs A·Z·BA–BO·K·AB·W·P·B·H·T）。  
- 自检布尔：BP2 是否 pit_by_ex_or_effective_date；BP0 是否单一主报；BP1 是否仅核对日泄露；是否未与 A/Z/BA–BO/K/AB/W/P/B/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BP 与 A/B/P/K/Z/BA–BO 或 params.Y/G/N 混用**；**是否特别写清双字母 BP≠单字母假设-P；BP≠BO；BP≠W；BP≠BI；带过 BO≠O/BF/BJ/BH/BN、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BO 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-P / 假设-O / 假设-N / 假设-K / 假设-M / 假设-W / 假设-Z / 假设-BA–BO / 假设-AB**；**是否未再改 BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把零补偿或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BO 及其他 A/D–BO 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-P**；**不改假设-O**；**不改假设-N**；**不改假设-K**；**不改假设-M**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BO**；**不改假设-AB**；**勿再改 BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息（BO）、融券空头名单（K）、除权板价（W）之外，**融券权益补偿**须按当时有效规则 PIT；不得默认零补偿。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BP** 标准件，**不改口径主线**，**不改假设 A–BO 正文**，**尤其不改假设-P / 假设-BO / 假设-W / 假设-BI / 假设-BJ / 假设-BB / 假设-K / 假设-BK**。与实验 A/Z/BA–BO/K/AB/W/P/B/H/T 分工：**A=板上枯竭；Z=开仓保证金比例；BA–BO=两融族既有页；K=融券空头名单；AB=融券卖出价限；W=除权板价；P=指数停牌权重；B=历史实验B旧位；H=退市整理；T=证管费（避开）；BP=融券权益补偿（现金红利/红股/配股）误开（BP≠A≠B≠P≠K≠Z≠BA≠…≠BO≠BI≠BJ≠BB≠W≠AB≠T；带过 BO≠O/BF/BJ/BH/BN、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K；params.Y/G/N≠实验字母BP）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待预检 |
| 数据 | 待接入（字段见 §6；日频融券空头数量+权益事件/补偿规则生效日即可起步；额度窗内日频可落点写明但不真跑） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**short_corp_action_comp_honest=pit_by_ex_or_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（待预检写死冻结；params.Y≠实验字母 BP；params.G≠实验字母 BP；params.N≠实验字母 BP；亦≠单字母实验 A/B/P/Z；禁 null/holdout/跑后改口）**；**bp0_primary_demo 建议 invent_zero_short_corp_action_comp（待预检写死冻结；禁双挂 invent_asof_leak_short_corp_action_comp；BP1半泄露不得升格并列主报）**；锚点保留 short_corp_action_comp_honest=pit_by_ex_or_effective_date / short_corp_action_scope=cash_div_bonus_share_rights_issue / short_corp_action_over_policy=accrue_or_fail_missing_event / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**建议写死冻结**；**params.Y≠BP**；**params.G≠BP**；**params.N≠BP**；禁 null/holdout）  
2. `params.bp0_primary_demo` = `invent_zero_short_corp_action_comp`（**建议写死冻结**；禁与 `invent_asof_leak_short_corp_action_comp` 双挂；BP1不升格主报）  
3. 权益补偿锚：`short_corp_action_comp_honest=pit_by_ex_or_effective_date`；`short_corp_action_scope=cash_div_bonus_share_rights_issue`；`short_corp_action_over_policy=accrue_or_fail_missing_event`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/P/A/Z/BA–BO/K/AB/H/W；**尤其 BP≠P（双字母≠单字母指数停牌权重）**；**尤其 BP≠BO（融券权益补偿≠融资利息罚息）**；**尤其 BP≠W（补偿义务≠除权板价）**；**尤其 BP≠BI（补偿≠融券所得用途）**；**尤其 BP≠BJ（补偿≠还本优先）**；**尤其 BP≠BB（补偿≠转融券源）**；**带过 BO≠O/BF/BJ/BH/BN、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BO 补丁已收 → 写假设-BP；自立 BP，勿占 BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/P/A/Z/K/W；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BP**；**双字母 BP ≠ 单字母 P**；**BP≠BO/W/BI/BJ/BB**；**带过 BO≠O/BF/BJ/BH/BN、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**）。选题：融券权益补偿（现金红利/红股/配股）误开（正交于 BO 融资计息 / W 除权板价 / BI 所得用途 / BJ 还本优先 / BB 券源 / K 名单；**承接 BO「融券费用/权益补偿另桶」分列**）。
