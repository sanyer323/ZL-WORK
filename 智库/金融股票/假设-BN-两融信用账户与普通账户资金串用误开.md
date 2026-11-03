# 假设 BN · 两融信用账户与普通账户资金串用误开 / 用核对日账户隔离规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BM 补丁已收（复检在途）、写下一纸面 BN；清单撞题规则另选正交执行缺口（**信用账户与普通账户资金/证券隔离** ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 市场25pct暂停 ≠ 合约期限 ≠ 可充抵保证金证券名单 ≠ 两融授信额度 ≠ 融券卖出所得用途 ≠ 融资买入卖出还债优先 ≠ 客户单票集中度 ≠ 担保品提取转出限制 ≠ 追保通知后禁新开 ≠ 开仓保证金比例 ≠ 融券空头名单）；选题自两融业务公开口径：信用账户资金与证券须与普通账户**分账隔离**，不得默认串用/混用为同一可用池；规则按**施行日/生效日** PIT，不得用核对日更宽「可串用」回放全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BN ≠ 单字母 B**）/ **N（收盘机制与假GTC；双字母 BN ≠ 单字母假设-N；且尤其 params.N ≠ 实验字母 BN）** / Z（**开仓**融资/融券保证金比例；**BN≠Z**）/ BA–BM（两融族已冻/在途；**BN≠BA…BM**）/ **K（融券空头名单 PIT；BN≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BN≠AB**）/ BI（**融券卖出所得资金用途**；**BN≠BI**；信用账户内用途限制 ≠ 信用↔普通串用）/ BJ（**融资买入卖出还债优先**；**BN≠BJ**；信用账户内还债优先 ≠ 跨账户串用）/ BL（**担保品提取转出限制**；**BN≠BL**；高维持提取闸门 ≠ 默认可任意串用；并带过 **BL≠BC**）/ BM（**追保通知后禁新开**；**BN≠BM**；追保禁开 ≠ 账户隔离；并带过 **BM≠BC、BM≠BL**）/ BC（**维持担保比例强制平仓**；**BN≠BC**）/ BD（**担保品折算率**；**BN≠BD**）/ BG（**可充抵保证金证券名单**；**BN≠BG**）/ E（整手）/ AN–BM（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BN**  
状态：**草稿 · 待预检**（结论栏空；禁止把「信用账户与普通账户资金可任意串用」当诚实执行能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BM 及其他 A/D–BM 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-N；不改假设-K；不改假设-M；不改假设-Z；不改假设-BA–BM；不改假设-AB；勿再改 BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BN（约 #71）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **信用账户与普通账户资金/证券是否允许串用**。**双字母 BN ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BN ≠ 单字母 B**。与假设 **N（收盘机制与假GTC）** **硬分列（专节强调）**：N = 收盘集合/收盘价机制与假 GTC 挂单；本页 = 信用↔普通**账户隔离**；收盘机制 ≠ 账户串用。**双字母 BN ≠ 单字母假设-N**。**尤其：纸面费率/显著性参数 `params.N` ≠ 实验字母 BN ≠ 单字母假设-N**（三者同字不同义，禁止混读互改）。与假设 **K（融券空头名单 PIT）** **硬分列**：K = 当日是否在**交易所融券标的名单**内；本页 = 信用与普通账户是否可串用；名单内可空 ≠ 可跨账户串用。**BN≠K**；并**带过**：双字母 **BK ≠ 单字母假设-K / 预检K**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 比例够之后，信用资金/证券是否仍被当成普通可用池；比例够 ≠ 可串用。与假设 **BI（融券卖出所得资金用途）** **硬分列**：BI = **信用账户内**融券所得只能买担保品/还融资等；本页 = **信用账户与普通账户之间**不得默认资金/证券串用；账户内用途限制 ≠ 跨账户串用放开。与假设 **BJ（融资买入卖出还债优先）** **硬分列**：BJ = 融资买入证券卖出所得**优先还融资负债**；本页 = 跨账户隔离；还债优先 ≠ 可把信用资金当普通现金。与假设 **BL（担保品提取转出限制）** **硬分列**：BL = **高维持线**提取/转出闸门（超过 300% 可提取）；本页 = **默认隔离**、不得把信用资产当普通账户可用；提取闸门通过 ≠ 默认可任意串用；并**带过 BL≠BC**。与假设 **BM（追保通知后禁新开）** **硬分列**：BM = 追保未到位禁新开；本页 = 账户隔离；追保禁开 ≠ 串用放开；并**带过 BM≠BC、BM≠BL**。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = 低维持强平；本页 = 账户隔离。与假设 **BD/BG** **硬分列**：折算率 / 可充抵名单 ≠ 跨账户串用。与假设 **BA/BB/BE/BF/BH/BK** **硬分列**：融资名单 / 转融券源 / 市场25pct / 合约期限 / 总授信 / 客户单票集中度 ≠ 账户隔离。与假设 **AB** **硬分列**：不重开空头价限/当日平。与假设 AN–BM **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BN** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名；**尤其 params.N ≠ 实验字母 BN**）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 N**（收盘机制与假GTC）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BN / 假设-BN / hypothesis_id=BN / 组 BN0·BN1·BN2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BN 混读或互改；亦**禁止**把 **`params.N`** 与 **单字母假设-N** 混读。亦**禁止**把实验字母 BN 与单字母 **A**、单字母 **B**、单字母 **N**、单字母 **K**、单字母 **Z**、双字母 **BA–BM**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bn0_*` 以外的实验页混读。**双字母 BN ≠ 单字母 A ≠ 单字母 B ≠ 单字母 N ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BM ≠ 双字母 BI ≠ 双字母 BJ ≠ 双字母 BL ≠ 双字母 BC ≠ 双字母 BK ≠ 双字母 AB**；**params.Y ≠ 实验字母 BN**；**params.G ≠ 实验字母 BN**；**params.N ≠ 实验字母 BN**。**带过：双字母 BM ≠ 双字母 BC、双字母 BM ≠ 双字母 BL、双字母 BL ≠ 双字母 BC**；**双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BN ≠ 单字母假设-N；且 params.N ≠ 实验字母 BN；且 ≠ BI/BJ/BL；带过 BM≠BC、BM≠BL、BL≠BC、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BN（双字母） |
|------|--------|----------------------|
| 题面 N | 收盘机制与假 GTC | **信用账户与普通账户资金串用**误开：假可串用 vs 按生效日账户隔离 PIT |
| 参数 N | `params.N`=失败/废单率差门槛（建议 0.05） | **实验字母 BN**；**params.N ≠ 实验字母 BN ≠ 单字母假设-N** |
| 题面 BI | 信用账户**内**融券所得用途限制 | 信用↔普通**跨账户**隔离；用途限制 ≠ 串用放开；**BN≠BI** |
| 题面 BJ | 融资买入卖出所得**优先还债**（账户内） | 跨账户隔离；还债优先 ≠ 可当普通现金；**BN≠BJ** |
| 题面 BL | 高维持提取/转出闸门（**BL≠BC**） | 默认隔离 ≠ 提取线通过后的合规转出；**BN≠BL**；**带过 BL≠BC** |
| 题面 BM | 追保通知后禁新开（**BM≠BC、BM≠BL**） | 账户隔离 ≠ 追保禁开；**BN≠BM**；**带过 BM≠BC、BM≠BL** |
| 题面 K / BK | K=融券空头**名单**；BK=客户**单票集中度**（**BK≠K**） | 账户隔离；本页**不覆盖** K/BK；**BN≠K≠BK**；**带过 BK≠K** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_cross_account_cash_fungible` |
| 文档 | `假设-N-收盘机制与假GTC.md` / `假设-BI-…` / `假设-BJ-…` / `假设-BL-…` / `假设-BM-…` / `假设-K-…` / `假设-BK-…`（**只读；禁止改写**） | `假设-BN-两融信用账户与普通账户资金串用误开.md`（新建） |
| 预检键 | 实验字母 N / BI / BJ / BL / BM / K / BK；键名 `params.N` | 实验字母 **BN** / `bn0_primary_demo`；**不得**占用或改写预检 N/BI/BJ/BL/BM/K/BK；**不得**把 `params.N` 改写成实验字母 |

**禁止**：把 BN 写成「N/BI/BJ/BL/BM/K/BK 的续篇」；把「融券所得可买担保品 / 融资卖出须还债 / 提取线已通过 / 追保未触发」静默写成「信用资金可当普通现金串用」；覆盖或补丁改写假设-N / 假设-BI / 假设-BJ / 假设-BL / 假设-BM / 假设-K / 假设-BK 正文；把 `params.N` 与实验字母 BN 或单字母假设-N 混读。

---

## 1. 一句话假设（可检验、可证伪）

同一拟用「信用账户资金/证券」去执行本应走普通账户路径（或反向把普通账户资金当信用可用保证金池）的交易意图、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/融券名单/授信/融券所得用途/融资还债优先/提取线/追保禁开输入（Z/BA/K/BH/BI/BJ/BL/BM 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/融券名单/总授信/融券所得用途/融资还债优先/高维持提取/追保禁开」）下，把「信用账户与普通账户资金/证券可任意串用、永不检查账户隔离」或「全样本用核对日当天账户隔离规则（含券商当日更宽可串用口径）回放历史」当成默认，相对「每个交易日按当时有效账户隔离 PIT（信用↔普通不得默认串用；串用拒开/记失败；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假可跨账户串用路径并高估可执行名义、低估因账户隔离导致的开仓/动用失败率**；差异应**集中在两融信用账户与普通账户资金串用误关桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假串用贡献差、可执行名义差、失败率差在标定噪声带内可忽略，且「假串用 / 核对日泄露 / 跨账户动用窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·K·AB·N·B·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 账户隔离 ≠ 融券所得用途；≠ 融资卖出还债优先；≠ 担保品提取；≠ 追保禁开；≠ 开仓保证金比例；≠ 客户单票集中度；≠ 授信额度；≠ 融资买入名单；≠ 转融券券源；≠ 担保品折算率；≠ 可充抵名单；≠ 市场25pct暂停；≠ 合约期限；≠ 融券名单；≠ 收盘机制/假GTC；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；草稿建议值；待预检写死）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BN；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 N；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BN
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BN；≠ 单字母假设-N（收盘机制）
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.cross_account_segregation_honest 写死 pit_by_effective_date
# params.cross_account_scope             写死 credit_vs_normal_cash_securities
# params.cross_account_over_policy       写死 reject_or_fail
# params.broker_tighter_segregation_bucket 写死 separate_sensitivity
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
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.close_gtc_handoff               写死 n_page
# params.exit_period_handoff             写死 h_page
# params.bn0_primary_demo                建议 invent_cross_account_cash_fungible  # 主报：信用↔普通可任意串用/永不检查账户隔离；禁与 invent_asof_leak_cross_account_segregation 双挂争主表；BN1半泄露不得升格并列主报
# params.bn0_invent_cross_account_fungible 写死 True
# params.bn1_asof_leak_cross_account_segregation_only 写死 True
# params.bn2_pit_cross_account_segregation 写死 True
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
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_AC_bse               写死 False
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
# params.merge_with_BA_margin_buy        写死 False
# params.merge_with_BB_refinance         写死 False
# params.merge_with_BC_maint             写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance           写死 False
# params.merge_with_BF_term              写死 False
# params.merge_with_BG_collateral        写死 False
# params.merge_with_BH_credit            写死 False
# params.merge_with_BI_short_proceeds    写死 False
# params.merge_with_BJ_financing_sale    写死 False
# params.merge_with_BK_client_conc       写死 False
# params.merge_with_BL_withdraw          写死 False
# params.merge_with_BM_margin_call       写死 False
# params.universe_rule                   写死 sse_szse_cross_account_segregation_check
# params.missing_cross_account_segregation_policy 写死 skip
# params.day_freq_proxy                  写死 cross_account_segregation_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BN；params.G≠实验字母BN；params.N≠实验字母BN；亦≠单字母实验A/B/N/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
cross_account_segregation_honest = "pit_by_effective_date"
params.bn0_primary_demo = "invent_cross_account_cash_fungible"  # 建议主报；禁与 invent_asof_leak_cross_account_segregation 双挂争主表；BN1半泄露不得升格并列主报
```

### 2.2 三组对照（BN0 / BN1 / BN2）

| 组 | 口径 | 说明 |
|----|------|------|
| BN0 天真 | `invent_cross_account_cash_fungible`（单一主报·建议） | 信用账户与普通账户资金/证券可任意串用；永不检查账户隔离 |
| BN1 半泄露 | `invent_asof_leak_cross_account_segregation` | 仅用核对日账户隔离规则（含券商当日更宽可串用口径）铺满全历史；**不得升格并列主报** |
| BN2 诚实 PIT | `pit_by_effective_date` | 按当日已生效账户隔离；串用拒开/记失败；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/BA/K/BH/BI/BJ/BL/BM）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **规则生效**：细则/合同/券商风控表施行日或生效日；禁用核对日更宽「可串用」提前纳入。  
- **额度窗内日频可落点（写明但不真跑）**：日频用「信用可用资金代理 vs 普通可用资金代理」与「拟跨账户动用名义」对照；仅纸面敏感性，不开回测、不接真数。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BN0 相对 BN2 的假串用贡献差、开仓/动用失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「两融信用账户与普通账户资金串用误关」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeCrossAccountFungible / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/BM/K/AB/N/B/H/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BN0 / BN1 / BN2。报告名义/路径质量差、假串用贡献差、开仓/动用失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_cross_account_cash_fungible",
  "invent_asof_leak_cross_account_segregation",
  "credit_to_normal_spend",
  "normal_to_credit_margin_pool",
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
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_N_close_gtc",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺账户类型/隔离规则字段却静默当「信用↔普通可任意串用」→ 设计失效。  
2. 把「融券所得可买担保品 / 用途内动用」静默写成「可当普通现金」且不声明另页 BI → **与 BI 撞题**（账户内用途 ≠ 跨账户串用；**尤其 BN≠BI**）。  
3. 把「融资卖出所得优先还债后余额」静默写成「可转普通账户自由用」且不声明另页 BJ → 与 BJ 撞题（**尤其 BN≠BJ**）。  
4. 把「维持担保比例够提取」静默写成「可任意串用到普通账户」且不声明另页 BL → 与 BL 撞题（合规提取 ≠ 默认串用；**尤其 BN≠BL**；**带过 BL≠BC**）。  
5. 把「追保未触发 / 可新开」静默写成「可跨账户串用」且不声明另页 BM → 与 BM 撞题（**尤其 BN≠BM**；**带过 BM≠BC、BM≠BL**）。  
6. 把「开仓保证金比例够 / 总授信未用尽 / 集中度未触顶」静默写成「可串用」且不声明另页 Z/BH/BK → 与 Z/BH/BK 撞题；亦不得混读 K（**带过 BK≠K**）。  
7. 把「在融资买入名单内 / 转融券未暂停 / 市场未达25pct / 合约未到期 / 可充抵 / 折算率有值 / 未触发强平」静默写成「可串用」且不声明另页 BA/BB/BE/BF/BG/BD/BC → 与对应页撞题。  
8. 把「在融券空头名单内」静默写成「可跨账户串用」且不声明另页 K → 与 K 撞题。  
9. 把「收盘机制/假GTC」写成主病而不声明另页 N → 与 N 撞题（**双字母 BN ≠ 单字母 N**）。  
10. 把「空头价限 / 当日平」写成主病而不声明另页 AB → 与 AB 撞题。  
11. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
12. 把「退市整理期当普通可交易」写成主病而不声明另页 H → 与 H 撞题。  
13. 把「账户串用误开」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
14. 把实验字母 BN 与单字母 A/B/N/K/Z 或双字母 BA–BM/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
15. holdout 反调 `bn0_primary_demo` / Y·G·N·Y2 → 结论无效。  
16. 用复权价算可用资金/可开名义 → 标签与执行双错，结论无效。  
17. 用核对日更宽「可串用」当诚实 PIT、或把券商临时放宽隔离提前铺满历史 → 设计失效。  
18. **改写或覆盖 `假设-N` / `假设-BI` / `假设-BJ` / `假设-BL` / `假设-BM` / `假设-K` / `假设-BK` / 已冻 AA–BM** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户可用资金/证券代理、普通账户可用资金/证券代理；  
- 拟跨账户动用名义（信用→普通花费，或普通→信用保证金池）；  
- 当时有效**账户隔离/分账**规则及生效日（细则/合同/券商风控表）；  
- 开仓保证金比例 / 融资名单 / 融券名单 / 总授信 / 融券所得用途 / 融资还债优先 / 提取线 / 追保禁开输入（消费 Z/BA/K/BH/BI/BJ/BL/BM 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商加严隔离；银证转账/担保品划转流水另桶（本页主测默认串用误开，不主测合规划转时效）。

**禁止**：用核对日「今天可串用」铺满当唯一诚实组；用复权价；把开仓保证金比例/低维持强平/高维持提取/折算率/可充抵名单/融资名单/转融券通道暂停/市场余额25pct暂停/合约期限/总授信/融券所得用途/融资卖出还债优先/客户单票集中度/追保禁开当成账户隔离放开；把 Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/BM/K/AB/A/N/B/H/T/AN–BM 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BN`  
- **组**：BN0 / BN1 / BN2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`cross_account_segregation_honest=pit_by_effective_date`；`cross_account_scope=credit_vs_normal_cash_securities`；`cross_account_over_policy=reject_or_fail`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`close_gtc_handoff=n_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_cross_account_segregation_check`；`missing_cross_account_segregation_policy=skip`；`day_freq_proxy=cross_account_segregation_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BN**；**params.G≠实验字母 BN**；**params.N≠实验字母 BN**；亦≠单字母实验 A/B/N/Z；禁 null/holdout/跑后改口）；**`params.bn0_primary_demo` 建议 `invent_cross_account_cash_fungible`**（禁与 invent_asof_leak_cross_account_segregation 双挂；BN1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BN0/BN1/BN2 可执行名义/路径质量、ΔFakeCrossAccountFungible、ΔFail；分桶（账户串用误关 / 核对日泄露 / 信用→普通 / 普通→信用保证金池 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·K·AB·N·B·H·T）。  
- 自检布尔：BN2 是否 pit_by_effective_date；BN0 是否单一主报；BN1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/BM/K/AB/N/B/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BN 与 A 或 B 或 N 或 K 或 Z 或 BA–BM 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清 params.N≠实验字母BN≠单字母假设-N**；**是否未改 Y/Z/AA–BM 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-N / 假设-K / 假设-M / 假设-Z / 假设-BA–BM / 假设-AB**；**是否未再改 BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否带过并尊重 BM≠BC、BM≠BL、BL≠BC、BK≠K**。  
- **禁止输出**：具体买卖标的列表当「建议」；把账户串用误开或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BM 及其他 A/D–BM 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-N**；**不改假设-K**；**不改假设-M**；**不改假设-Z**；**不改假设-BA–BM**；**不改假设-AB**；**勿再改 BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、融券空头名单（K）之外，**信用账户与普通账户资金/证券隔离**须按当时有效规则 PIT；不得默认可任意串用。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BN** 标准件，**不改口径主线**，**不改假设 A–BM 正文**，**尤其不改假设-N / 假设-BI / 假设-BJ / 假设-BL / 假设-BM / 假设-K / 假设-BK**。与实验 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/BM/K/AB/N/B/H/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓（低线）；BD=担保品折算率；BE=市场层单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；BG=可充抵保证金证券名单；BH=两融授信额度上限；BI=融券卖出所得资金用途限制；BJ=融资买入卖出所得优先偿还融资负债；BK=客户单票两融集中度上限；BL=担保品提取转出限制；BM=追保通知后仍假可新开仓误开；K=融券空头名单；AB=融券卖出价限；N=收盘机制与假GTC；B=历史实验B旧位；H=退市整理；T=证管费（避开）；BN=两融信用账户与普通账户资金串用误开（BN≠A≠B≠N≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠BM≠AB≠T；带过 BM≠BC、BM≠BL、BL≠BC、BK≠K；params.N≠实验字母BN）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待预检 |
| 数据 | 待接入（字段见 §6；日频信用/普通可用代理+拟跨账户动用名义+隔离规则生效日即可起步；额度窗内日频可落点写明但不真跑） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**cross_account_segregation_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BN；params.G≠实验字母 BN；params.N≠实验字母 BN；亦≠单字母实验 A/B/N/Z；禁 null/holdout/跑后改口）**；**bn0_primary_demo 建议 invent_cross_account_cash_fungible（禁双挂 invent_asof_leak_cross_account_segregation；BN1半泄露不得升格并列主报）**；锚点保留 cross_account_segregation_honest=pit_by_effective_date / cross_account_scope=credit_vs_normal_cash_securities / cross_account_over_policy=reject_or_fail / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（建议待写死；**params.Y≠BN**；**params.G≠BN**；**params.N≠BN**；禁 null/holdout）  
2. `params.bn0_primary_demo` = `invent_cross_account_cash_fungible`（建议待写死；禁与 `invent_asof_leak_cross_account_segregation` 双挂；BN1不升格主报）  
3. 账户隔离锚：`cross_account_segregation_honest=pit_by_effective_date`；`cross_account_scope=credit_vs_normal_cash_securities`；`cross_account_over_policy=reject_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/N/A/Z/BA–BM/K/AB/H；**尤其 BN≠BI（跨账户串用≠账户内融券所得用途）**；**尤其 BN≠BJ（跨账户串用≠融资卖出还债优先）**；**尤其 BN≠BL（默认隔离≠高维持提取）**；**尤其 BN≠BM（账户隔离≠追保禁开）**；**尤其 BN≠N（双字母≠单字母收盘机制）**；**尤其 params.N≠实验字母BN≠单字母假设-N**；**带过 BM≠BC、BM≠BL、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BM 补丁已收 → 写假设-BN；自立 BN，勿占 BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/N/A/Z/K；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BN**；**双字母 BN ≠ 单字母 N**；**尤其 params.N≠实验字母BN≠单字母假设-N**；**BN≠BI/BJ/BL/BM**；**带过 BM≠BC、BM≠BL、BL≠BC、BK≠K**）。选题：两融信用账户与普通账户资金串用误开（正交于 BI 账户内融券所得用途 / BJ 融资卖出还债优先 / BL 高维持提取 / BM 追保禁开 / Z 开仓比例）。
