# 假设 BO · 融资利息与逾期罚息计提误关 / 用核对日利率规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BN 补丁已收（复检在途）、写下一纸面 BO；清单撞题规则另选正交执行缺口（**融资利息与逾期罚息按生效日计提** ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 市场25pct暂停 ≠ 合约期限/到期了结 ≠ 可充抵保证金证券名单 ≠ 两融授信额度 ≠ 融券卖出所得用途 ≠ 融资买入卖出还债优先 ≠ 客户单票集中度 ≠ 担保品提取转出限制 ≠ 追保通知后禁新开 ≠ 信用/普通账户串用 ≠ 开仓保证金比例 ≠ 融券空头名单 ≠ 大宗假流动性）；选题自两融业务公开口径：融资买入未了结期间须按合同/细则**计收融资利息**，逾期未还另计**罚息/逾期利息**；利率与起息规则按**施行日/生效日** PIT，不得默认「永不计息/零利息/零罚息」或用核对日更宽低息规则回放全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BO ≠ 单字母 B**）/ **O（大宗假流动性；双字母 BO ≠ 单字母假设-O）** / Z（**开仓**融资/融券保证金比例；**BO≠Z**）/ BA–BN（两融族已冻/在途；**BO≠BA…BN**）/ **K（融券空头名单 PIT；BO≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BO≠AB**）/ BF（**两融合约期限到期强制了结**；**BO≠BF**；到期强了 ≠ 利息/罚息计提）/ BH（**授信额度**；**BO≠BH**）/ BJ（**融资卖出还债优先**；**BO≠BJ**；还债优先 ≠ 利息计提）/ BN（**信用/普通账户串用**；**BO≠BN**；账户隔离 ≠ 利息；并带过 **BN≠BI/BJ/BL/BM、params.N≠BN**）/ BM（**追保后禁新开**；**BO≠BM**；并带过 **BM≠BC、BM≠BL**）/ BL（**担保品提取**；**BO≠BL**；并带过 **BL≠BC**）/ BC（**维持担保强平**；**BO≠BC**）/ E（整手）/ AN–BN（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BO**  
状态：**草稿 · 待预检**（结论栏空；禁止把「融资永不计息/零罚息/用核对日低息铺满」当诚实持仓成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BN 及其他 A/D–BN 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-O；不改假设-N；不改假设-K；不改假设-M；不改假设-Z；不改假设-BA–BN；不改假设-AB；勿再改 BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BO（约 #72）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融资利息与逾期罚息是否按生效日计提**。**双字母 BO ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BO ≠ 单字母 B**。与假设 **O（大宗假流动性）** **硬分列（专节强调）**：O = 大宗/盘后量价通道假流动性；本页 = 信用账户**融资利息与逾期罚息计提**；大宗通道 ≠ 利息计提。**双字母 BO ≠ 单字母假设-O**。与假设 **K（融券空头名单 PIT）** **硬分列**：K = 当日是否在**交易所融券标的名单**内；本页 = 融资余额是否按日计息/逾期罚息；名单内可空 ≠ 融资零利息。**BO≠K**；并**带过**：双字母 **BK ≠ 单字母假设-K / 预检K**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 开仓后持仓期间的**利息/罚息成本**；比例够 ≠ 零利息。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = 合约**期限/到期强制了结**（及展期惯例泄露）；本页 = **利息与逾期罚息计提**；到期强了 ≠ 计息规则；**禁止**把「可展期」静默写成「展期后零利息」。与假设 **BJ（融资买入卖出还债优先）** **硬分列**：BJ = 卖出所得**优先还融资负债本金**；本页 = 负债存续期间的**利息/罚息**；还本优先 ≠ 计息。与假设 **BH（授信额度）** **硬分列**：BH = 总授信上限；本页 = 已占用融资的利息成本；授信够 ≠ 零息。与假设 **BN（信用/普通账户串用）** **硬分列**：BN = 跨账户隔离；本页 = 信用账户内融资计息；串用 ≠ 计息；并**带过 BN≠BI/BJ/BL/BM、params.N≠BN**。与假设 **BM/BL/BC** **硬分列**：追保禁开 / 高维持提取 / 低维持强平 ≠ 利息计提；并**带过 BM≠BC、BM≠BL、BL≠BC**。与假设 **BA/BB/BD/BE/BG/BI/BK** **硬分列**：融资名单 / 转融券源 / 折算率 / 市场25pct / 可充抵名单 / 融券所得用途 / 客户单票集中度 ≠ 利息计提。与假设 **AB** **硬分列**：不重开空头价限/当日平。与假设 AN–BN **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BO** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 O**（大宗假流动性）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BO / 假设-BO / hypothesis_id=BO / 组 BO0·BO1·BO2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BO 混读或互改。亦**禁止**把实验字母 BO 与单字母 **A**、单字母 **B**、单字母 **O**、单字母 **K**、单字母 **Z**、双字母 **BA–BN**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bo0_*` 以外的实验页混读。**双字母 BO ≠ 单字母 A ≠ 单字母 B ≠ 单字母 O ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BN ≠ 双字母 BF ≠ 双字母 BJ ≠ 双字母 BH ≠ 双字母 AB**；**params.Y ≠ 实验字母 BO**；**params.G ≠ 实验字母 BO**；**params.N ≠ 实验字母 BO**。**带过：双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BO ≠ 单字母假设-O；且 ≠ 假设-BF；带过 BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BO（双字母） |
|------|--------|----------------------|
| 题面 O | 大宗/盘后量价假流动性 | **融资利息与逾期罚息计提**误关：假零息/零罚息 vs 按生效日利率 PIT |
| 题面 BF | 合约**期限到期强制了结**（及展期惯例泄露） | 持仓期间**利息/罚息计提**；到期强了 ≠ 计息；**BO≠BF**；禁把展期写成零息 |
| 题面 BJ | 融资卖出所得**优先还本** | 负债存续**利息/罚息**；还本 ≠ 计息；**BO≠BJ** |
| 题面 BH | 两融**总授信**上限 | 已占用融资的计息；授信够 ≠ 零息；**BO≠BH** |
| 题面 BN | 信用?普通**账户隔离**（**BN≠BI/BJ/BL/BM**；**params.N≠BN**） | 信用账户内计息 ≠ 跨账户串用；**BO≠BN**；**带过 BN 消歧链** |
| 题面 BM/BL/BC | 追保禁开 / 高维持提取 / 低维持强平（**BM≠BC、BM≠BL、BL≠BC**） | 利息计提；本页不覆盖；**带过**上述分列 |
| 题面 K / BK | K=融券空头**名单**；BK=客户**单票集中度**（**BK≠K**） | 利息计提；本页**不覆盖** K/BK；**BO≠K≠BK**；**带过 BK≠K** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_zero_financing_interest_penalty` |
| 文档 | `假设-O-大宗假流动性.md` / `假设-BF-…` / `假设-BJ-…` / `假设-BH-…` / `假设-BN-…` / `假设-K-…` / `假设-BK-…`（**只读；禁止改写**） | `假设-BO-融资利息与逾期罚息计提误关.md`（新建） |
| 预检键 | 实验字母 O / BF / BJ / BH / BN / K / BK | 实验字母 **BO** / `bo0_primary_demo`；**不得**占用或改写预检 O/BF/BJ/BH/BN/K/BK |

**禁止**：把 BO 写成「O/BF/BJ/BH/BN 的续篇」；把「合约可展期 / 未触发强平 / 授信未用尽 / 还本优先已满足」静默写成「融资零利息、零罚息」；覆盖或补丁改写假设-O / 假设-BF / 假设-BJ / 假设-BH / 假设-BN / 假设-K / 假设-BK 正文；把 `params.Y/G/N` 与实验字母 BO 混读。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有/滚动融资负债路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/授信/合约期限/还债优先/账户隔离输入（Z/BA/BH/BF/BJ/BN 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/总授信/合约期限强了/融资还债优先/账户隔离」）下，把「融资永不计息、逾期永不罚息、利息成本恒为 0」或「全样本用核对日当天利率/罚息规则（含券商当日更宽低息口径）回放历史」当成默认，相对「每个交易日按当时有效融资利率与逾期罚息规则 PIT（按日/按约定计息；逾期另计罚息；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假零息杠杆路径并高估净收益、低估融资持仓真实成本与逾期惩罚**；差异应**集中在融资利息与逾期罚息计提误关桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假零息贡献差、净收益差、利息/罚息计提差在标定噪声带内可忽略，且「假零息 / 核对日泄露 / 正常计息窗 / 逾期罚息窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·K·AB·O·B·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融资利息/逾期罚息 ≠ 合约期限强了；≠ 融资卖出还债优先；≠ 授信额度；≠ 账户串用；≠ 开仓保证金比例；≠ 追保禁开；≠ 担保品提取；≠ 融券所得用途；≠ 融资买入名单；≠ 转融券券源；≠ 担保品折算率；≠ 可充抵名单；≠ 市场25pct暂停；≠ 客户单票集中度；≠ 融券名单；≠ 大宗假流动性；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；待预检；建议值如下；拉数前须冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BO；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 O；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BO
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BO；≠ 单字母假设-N（收盘机制）；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.interest_accrual_honest         写死 pit_by_effective_date
# params.interest_scope                  写死 financing_interest_and_overdue_penalty
# params.interest_over_policy            写死 accrue_or_fail_missing_rate
# params.broker_lower_rate_bucket        写死 separate_sensitivity
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
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.block_liq_handoff               写死 o_page
# params.exit_period_handoff             写死 h_page
# params.bo0_primary_demo                建议 invent_zero_financing_interest_penalty  # 主报：融资永不计息/逾期零罚息；禁与 invent_asof_leak_financing_interest 双挂争主表；BO1半泄露不得升格并列主报
# params.bo0_invent_zero_interest_penalty 写死 True
# params.bo1_asof_leak_financing_interest_only 写死 True
# params.bo2_pit_financing_interest      写死 True
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
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_W_exright            写死 False
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
# params.universe_rule                   写死 sse_szse_financing_interest_accrual_check
# params.missing_interest_rate_policy    写死 skip
# params.day_freq_proxy                  写死 financing_interest_accrual_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BO；params.G≠实验字母BO；params.N≠实验字母BO；亦≠单字母A/B/O/Z；禁null/holdout
# params.date_start / date_end           写死主窗并待冻结 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期并待冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

### 2.2 三组对照（BO0 / BO1 / BO2）

| 组 | 角色 | 行为 |
|----|------|------|
| **BO0** | 天真主报 | 按 `bo0_primary_demo=invent_zero_financing_interest_penalty`：融资永不计息、逾期零罚息；**单一主报**；禁与半泄露双挂 |
| **BO1** | 半泄露 | 仅 `invent_asof_leak_financing_interest`：全样本用核对日利率/罚息规则回放；**不得升格并列主报** |
| **BO2** | 诚实 PIT | `interest_accrual_honest=pit_by_effective_date`：按生效日利率与逾期罚息规则计息；缺字段 skip |

### 2.3 标签与样本区间口径

- **PIT 锚**：利率表/罚息表/起息日规则的**生效日**；`asof_check_date=2026-10-16` 仅用于 BO1 半泄露对照，**不得**当 BO2 诚实组。  
- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/BA/BH/BF/BJ/BN）。  
- **额度窗内日频可落点（写明但不真跑）**：日终融资负债余额 × 当日生效年化利率 / 计息日基数 → 当日应计利息；逾期标记为真时叠加罚息率；缺利率字段 → skip（敏感性另桶）。  
- **通道前**：`margin_channel_start=2010-03-31` 前无本页计息通道。  
- **px_basis=unadj**；禁止用复权价算负债名义或利息。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

BO0 相对 BO2：假零息贡献差、净收益高估、应计利息/罚息漏计差显著超过 `params.Y/G/N/Y2` 门槛带，且差异集中在「融资利息与逾期罚息计提误关」桶；BO1 相对 BO2 的核对日泄露贡献可单独度量且不得冒充主报。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 BF 期限/展期、BJ 还本优先、BH 授信、BN 串用、Z 开仓比例、T 证管费等他页桶吸走；或 holdout 反调 `bo0_primary_demo` / Y·G·N·Y2；或 BO0 与 asof_leak 双挂主报。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1、同一未复权价，对照 BO0 / BO1 / BO2；报告名义净收益差、ΔFakeZeroInterest、ΔAccruedInterest、ΔPenalty；按分桶报告。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

- `invent_zero_financing_interest_penalty`  
- `invent_asof_leak_financing_interest`  
- `normal_accrual_window`  
- `overdue_penalty_window`  
- `pre_margin_channel`  
- `vs_A_limit_fill` / `vs_Z_margin_ratio` / `vs_BA_margin_buy_list` / `vs_BB_refinance` / `vs_BC_maint_force` / `vs_BD_haircut` / `vs_BE_balance_pause` / `vs_BF_contract_term` / `vs_BG_collateral_list` / `vs_BH_credit_quota` / `vs_BI_short_proceeds` / `vs_BJ_financing_sale_repay` / `vs_BK_client_conc` / `vs_BL_collateral_withdraw` / `vs_BM_margin_call_open_ban` / `vs_BN_cross_account` / `vs_K_shortable` / `vs_AB_short_px` / `vs_O_block` / `vs_B_legacy` / `vs_H_exit` / `vs_T_csrc_fee`

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺利率/罚息字段静默当零息。  
2. 把「授信够 / 可展期 / 未强平 / 还本优先已满足 / 账户未串用」写成「零利息」。  
3. 把合约期限/展期（BF）写成主病 → 与 BF 撞题。  
4. 把融资卖出还债优先（BJ）写成主病 → 与 BJ 撞题。  
5. 把授信额度（BH）写成主病 → 与 BH 撞题。  
6. 把账户串用（BN）写成主病 → 与 BN 撞题。  
7. 把开仓保证金比例（Z）写成主病 → 与 Z 撞题。  
8. 把大宗假流动性（O）写成主病 → 与 O 撞题（**双字母 BO ≠ 单字母 O**）。  
9. 把「证管费误抽」写成主病 → **撞预检T**。  
10. 实验字母 BO 与单字母 A/B/O/K/Z 或双字母 BA–BN/AB 或 `params.Y/G/N` 混读互改。  
11. holdout 反调 `bo0_primary_demo` / Y·G·N·Y2。  
12. 用复权价算负债名义/利息。  
13. 用核对日低息当诚实 PIT。  
14. **改写或覆盖**已冻/在途 AA–BN / 假设-O / 假设-BF / 假设-H / 假设-K 等 → 硬边界违规。  
15. `bo0_primary_demo` 与 `invent_asof_leak_financing_interest` **双挂主报**；或 BO1 升格并列主报。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资负债日终余额代理、起息日/计息天数代理；  
- 当时有效融资年化利率表及生效日；  
- 逾期标记与当时有效罚息/逾期利率表及生效日；  
- 开仓保证金比例 / 融资名单 / 总授信 / 合约期限 / 还债优先 / 账户隔离输入（消费 Z/BA/BH/BF/BJ/BN 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商更低优惠利率另桶；融券费用/权益补偿另桶（本页主测**融资利息+逾期罚息**，不主测融券借券费或权益补偿）。

**禁止**：用核对日「今天低息」铺满当唯一诚实组；用复权价；把开仓比例/低维持强平/高维持提取/折算率/可充抵名单/融资名单/转融券通道/市场25pct/合约期限展期/总授信/融券所得用途/融资卖出还债优先/客户单票集中度/追保禁开/账户串用当成零息依据；把 Z/BA–BN/K/AB/A/O/B/H/T 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BO`  
- **组**：BO0 / BO1 / BO2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`interest_accrual_honest=pit_by_effective_date`；`interest_scope=financing_interest_and_overdue_penalty`；`interest_over_policy=accrue_or_fail_missing_rate`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`block_liq_handoff=o_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_financing_interest_accrual_check`；`missing_interest_rate_policy=skip`；`day_freq_proxy=financing_interest_accrual_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BO**；**params.G≠实验字母 BO**；**params.N≠实验字母 BO**；亦≠单字母实验 A/B/O/Z；禁 null/holdout/跑后改口；**拉数前须冻结**）；**`params.bo0_primary_demo` 建议 `invent_zero_financing_interest_penalty`**（禁与 invent_asof_leak_financing_interest 双挂；BO1半泄露不得升格并列主报；**拉数前须冻结**）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BO0/BO1/BO2 净收益/成本质量、ΔFakeZeroInterest、ΔAccruedInterest、ΔPenalty；分桶（利息罚息误关 / 核对日泄露 / 正常计息 / 逾期罚息 / 通道前 / vs A·Z·BA–BN·K·AB·O·B·H·T）。  
- 自检布尔：BO2 是否 pit_by_effective_date；BO0 是否单一主报；BO1 是否仅核对日泄露；是否未与 A/Z/BA–BN/K/AB/O/B/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BO 与 A/B/O/K/Z/BA–BN 或 params.Y/G/N 混用**；**是否特别写清双字母 BO≠单字母假设-O；BO≠BF；带过 BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BN 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-O / 假设-N / 假设-K / 假设-M / 假设-Z / 假设-BA–BN / 假设-AB**；**是否未再改 BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把零息或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BN 及其他 A/D–BN 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-O**；**不改假设-N**；**不改假设-K**；**不改假设-M**；**不改假设-Z**；**不改假设-BA–BN**；**不改假设-AB**；**勿再改 BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融券空头名单（K）之外，**融资利息与逾期罚息**须按当时有效规则 PIT；不得默认零息。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BO** 标准件，**不改口径主线**，**不改假设 A–BN 正文**，**尤其不改假设-O / 假设-BF / 假设-BJ / 假设-BH / 假设-BN / 假设-K / 假设-BK**。与实验 A/Z/BA–BN/K/AB/O/B/H/T 分工：**A=板上枯竭；Z=开仓保证金比例；BA–BN=两融族既有页；K=融券空头名单；AB=融券卖出价限；O=大宗假流动性；B=历史实验B旧位；H=退市整理；T=证管费（避开）；BO=融资利息与逾期罚息计提误关（BO≠A≠B≠O≠K≠Z≠BA≠…≠BN≠BF≠BJ≠BH≠AB≠T；带过 BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K；params.Y/G/N≠实验字母BO）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待预检 |
| 数据 | 待接入（字段见 §6；日频融资负债余额+利率/罚息生效日即可起步；额度窗内日频可落点写明但不真跑） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**interest_accrual_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BO；params.G≠实验字母 BO；params.N≠实验字母 BO；亦≠单字母实验 A/B/O/Z；禁 null/holdout/跑后改口；拉数前须冻结）**；**bo0_primary_demo 建议 invent_zero_financing_interest_penalty（禁双挂 invent_asof_leak_financing_interest；BO1半泄露不得升格并列主报；拉数前须冻结）**；锚点保留 interest_accrual_honest=pit_by_effective_date / interest_scope=financing_interest_and_overdue_penalty / interest_over_policy=accrue_or_fail_missing_rate / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（建议；**params.Y≠BO**；**params.G≠BO**；**params.N≠BO**；禁 null/holdout；拉数前须冻结）  
2. `params.bo0_primary_demo` = `invent_zero_financing_interest_penalty`（建议单一主报；禁与 `invent_asof_leak_financing_interest` 双挂；BO1不升格主报；拉数前须冻结）  
3. 利息锚：`interest_accrual_honest=pit_by_effective_date`；`interest_scope=financing_interest_and_overdue_penalty`；`interest_over_policy=accrue_or_fail_missing_rate`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/O/A/Z/BA–BN/K/AB/H；**尤其 BO≠O（双字母≠单字母大宗）**；**尤其 BO≠BF（计息≠合约期限/展期强了）**；**尤其 BO≠BJ（计息≠还本优先）**；**尤其 BO≠BH（计息≠总授信）**；**尤其 BO≠BN（计息≠账户串用）**；**带过 BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BN 补丁已收 → 写假设-BO；自立 BO，勿占 BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/O/A/Z/K；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BO**；**双字母 BO ≠ 单字母 O**；**BO≠BF/BJ/BH/BN**；**带过 BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**）。选题：融资利息与逾期罚息计提误关（正交于 BF 合约期限强了 / BJ 还本优先 / BH 授信 / BN 账户串用 / Z 开仓比例；**不重开 BF 展期题面**）。
