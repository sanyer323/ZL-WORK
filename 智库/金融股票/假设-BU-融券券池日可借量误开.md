# 假设 BU · 融券券池日可借量/日频库存上限误开 / 用核对日无限或更宽日库存铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BT 补丁已交（复检在途）、写下一纸面 BU；清单撞题规则另选正交执行缺口（**融券券池日可借量/日频库存上限** ≠ 转融券暂停后假无限券源 ≠ 融券空头名单是否在池 ≠ 过户费现行档 ≠ 强制平仓顺序与范围 ≠ 融资利率档 ≠ 融资利息假零息 ≠ 融券借券费 ≠ 授信额度上限 ≠ 标的调出后存量续持 ≠ 融券权益补偿 ≠ 追保后禁新开 ≠ 担保品提取 ≠ 开仓保证金比例 ≠ 融资买入名单 ≠ 合约期限到期了结 ≠ 市场25pct余额暂停 ≠ 证管费）；选题自两融业务公开口径：即便标的在融券名单、转融通道未暂停，券商/出借方**当日可借库存或日可借量上限**仍按当时有效规则约束新开空头名义；日库存/日可借量按**施行日/生效日** PIT，不得默认「名单内即可任意量任意日借满 / 永不检查日库存上限 / 用核对日更宽日库存或无限库存铺满历史」；2010-03-31 前无此通道；**BB 正文主测「转融券暂停后仍假无限转融券源」**（暂停闸门），本页主测**通道正常时仍发明假无限日库存或假忽略日可借量上限** → 自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BU ≠ 单字母 B**）/ **U（过户费现行档误铺；双字母 BU ≠ 单字母假设-U；严禁复用 U 题面或过户费口径）** / Z（**开仓**融资/融券保证金比例；**BU≠Z**）/ BA–BT（两融族已冻/在途；**BU≠BA…BT**；**尤其不改 BT 正文**）/ **K（融券空头名单 PIT；BU≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BU≠AB**）/ BB（**转融券暂停后假无限券源**；**BU≠BB**；暂停后假无限源 ≠ 正常通道下日库存上限；**尤其不改假设-BB**）/ BT（**强制平仓顺序与范围**；**BU≠BT**；强平序 ≠ 日可借量；**尤其不改假设-BT**）/ BS（**融资利率档位优惠档**；**BU≠BS**）/ BO（**融资利息与逾期罚息假零息**；**BU≠BO**）/ BR（**融券借券费**；**BU≠BR**）/ BH（**授信额度上限**；**BU≠BH**）/ BQ（**标的调出后存量假续持**；**BU≠BQ**）/ BP（**融券权益补偿**；**BU≠BP**）/ BN（**信用/普通账户串用**；**BU≠BN**；并带过 **BN≠BI/BJ/BL/BM、params.N≠BN**）/ BM（**追保后禁新开**；**BU≠BM**；并带过 **BM≠BC、BM≠BL**）/ BL（**担保品提取**；**BU≠BL**；并带过 **BL≠BC**）/ BE（**市场25pct余额暂停**；**BU≠BE**；市场层余额占比暂停 ≠ 券商日库存上限）/ BF（**两融合约期限到期强制了结**；**BU≠BF**）/ BI（**融券卖出所得用途**；**BU≠BI**）/ BJ（**融资卖出还债优先**；**BU≠BJ**）/ BD（**担保品折算率**；**BU≠BD**）/ BG（**可充抵名单**；**BU≠BG**）/ BK（**客户单票集中度**；**BU≠BK**）/ BC（**维持担保比例强制平仓闸门**；**BU≠BC**）/ BA（**融资买入名单**；**BU≠BA**）/ W（除权板价；**BU≠W**）/ T（证管费；**避开预检T**；**BU≠T**）/ S（经手费；**BU≠S**）/ E（整手）/ AN–BT（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ V（印花税）等**分列**；**新建实验 BU**  
状态：**草稿 · 待预检**（结论栏空；禁止把「名单内即可任意量任意日借满 / 永不检查日库存上限 / 用核对日更宽日库存或无限库存铺满」当诚实融券可借路径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BT 及其他 A/D–BT 已交正文与冻结补丁；尤其不改假设-BT；尤其不改假设-BB；尤其不改假设-U；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BT；不改假设-AB；勿再改 BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BU（约 #78）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融券券池日可借量/日频库存上限**。**双字母 BU ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BU ≠ 单字母 B**。与假设 **U（过户费现行档误铺）** **硬分列（专节强调）**：U = 中国结算股票交易过户费费率切片（买卖双边、2015-08-01 / 2022-04-29 切日）；本页 = 信用账户**融券日可借量/券池日库存**；过户费 ≠ 日可借量。**双字母 BU ≠ 单字母假设-U**；**严禁复用 U 题面或 U 口径键**。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 2024-07-11 转融暂停后仍发明假无限转融源（暂停闸门）；本页 = **通道未暂停时**仍发明假无限日库存或假忽略日可借量上限；暂停闸门 ≠ 日库存上限；**禁止**把「暂停后仍可无限借（BB 天真组）」静默写成「日库存已诚实」；**禁止**把「日库存无限」静默写成「转融未暂停」；**不占** BB 的 primary_demo；**尤其不改假设-BB**。**BU≠BB**。与假设 **BT（强制平仓顺序与范围）** **硬分列**：BT = 强平触发后的序/范围；本页 = 日可借量；强平序 ≠ 日库存；**尤其不改假设-BT**。**BU≠BT**。与假设 **K（融券空头名单）** **硬分列**：K = 是否在融券标的名单（可空/不可空）；本页 = 名单内仍须受日库存/日可借量上限约束；名单 ∈ ≠ 日库存够；**尤其不改假设-K**；并**带过 BK≠K**。**BU≠K**。与假设 **BS / BO / BR / BH / BQ / BP / BN / BM / BL / BE / BF** **硬分列**：利率档 / 假零息 / 借券费 / 授信天花板 / 调出后存量 / 权益补偿 / 账户串用 / 追保禁开 / 高维持提取 / 市场25pct / 合约期限到期了结 ≠ 日可借量；并**带过 BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 **AB / Z / W / BA / BD / BG / BK / BI / BJ / BC** **硬分列**：空头价限 / 开仓保证金 / 除权板价 / 融资名单 / 折算率 / 可充抵 / 客户集中度 / 融券所得用途 / 融资还债优先 / 维持线闸门 ≠ 日可借量。与假设 AN–BT **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BU** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 U**（过户费现行档误铺；**严禁复用假设-U**）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BU / 假设-BU / hypothesis_id=BU / 组 BU0·BU1·BU2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BU 混读或互改。亦**禁止**把实验字母 BU 与单字母 **A**、单字母 **B**、单字母 **U**、单字母 **K**、单字母 **Z**、单字母 **T**、单字母 **S**、双字母 **BA–BT**、双字母 **BB**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bu0_*` 以外的实验页混读。**双字母 BU ≠ 单字母 A ≠ 单字母 B ≠ 单字母 U ≠ 单字母 K ≠ 单字母 Z ≠ 单字母 T ≠ 单字母 S ≠ 双字母 BA ≠ … ≠ 双字母 BT ≠ 双字母 BB ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BQ ≠ 双字母 BP ≠ 双字母 BN ≠ 双字母 BM ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BU**；**params.G ≠ 实验字母 BU**；**params.N ≠ 实验字母 BU**。**带过：双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BU ≠ 单字母假设-U；且 ≠ 假设-BB / 假设-BT / 假设-BS / 假设-BO / 假设-BR / 假设-BH / 假设-BQ / 假设-BP / 假设-BN / 假设-BM / 假设-K；带过 BT≠T/BC/BS…、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BU（双字母） |
|------|--------|----------------------|
| 题面 U | 过户费费率切片（买卖双边；2015-08-01 / 2022-04-29） | **融券券池日可借量/日频库存上限**误开：假无限日库存 vs 按生效日日库存 PIT；**严禁复用 U 题面** |
| 题面 BB | **转融券暂停后假无限券源**（暂停闸门） | **通道正常时日库存/日可借量上限**；暂停闸门 ≠ 日库存；**BU≠BB**；**不改 BB** |
| 题面 BT | **强制平仓顺序与范围**（复检在途） | 强平序 ≠ 日可借量；**BU≠BT**；**不改 BT** |
| 题面 K | **融券空头名单**（是否在池） | 名单 ∈ ≠ 日库存够；**BU≠K**；**不改 K**；**带过 BK≠K** |
| 题面 BS / BO / BR | 融资利率档 / 融资假零息 / 融券借券费 | 计息/计费 ≠ 日库存；**BU≠BS≠BO≠BR** |
| 题面 BH / BQ / BP | 授信天花板 / 调出后存量 / 权益补偿 | 本页不覆盖；**BU≠BH≠BQ≠BP** |
| 题面 BN / BM / BL / BE | 账户隔离 / 追保禁开 / 高维持提取 / 市场25pct | 本页不覆盖；**带过**消歧链；**BU≠BN≠BM≠BL≠BE** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_unlimited_daily_short_inventory` |
| 文档 | `假设-U-…` / `假设-BB-…` / `假设-BT-…` / `假设-K-…`（**只读；禁止改写**） | `假设-BU-融券券池日可借量误开.md`（新建） |
| 预检键 | 实验字母 U / BB / BT / K | 实验字母 **BU** / `bu0_primary_demo`；**不得**占用或改写预检 U/BB/BT/K |

**禁止**：把 BU 写成「U/BB/BT/K 的续篇」；把「转融未暂停 / 名单内可空 / 授信够 / 强平序已诚实 / 过户费已诚实」静默写成「日库存已诚实」；覆盖或补丁改写假设-U / 假设-BB / 假设-BT / 假设-K / 假设-BS / 假设-BO / 假设-BR 正文；把 `params.Y/G/N` 与实验字母 BU 混读；**禁** `bu0_primary_demo` 与 `invent_asof_leak_daily_short_inventory` **双挂主报**；**禁** BU1 半泄露升格并列主报；**禁**复用假设-U（过户费）题面或口径键。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有/滚动融券空头路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资/融券名单/转融券通道状态/授信/合约期限/维持担保闸门/追保禁开/账户隔离/折算率等输入（Z/BA/K/BB/BH/BF/BC/BM/BN/BD 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/融券名单/转融暂停闸门/授信天花板/合约期限/维持线闸门 on-off/追保禁开/账户隔离/折算率主病」）下，把「只要在融券名单内即可任意量任意日借满、永不检查券商/出借方当日可借库存或日可借量上限」或「全样本用核对日当天更宽日库存或无限库存规则回放历史」当成默认，相对「每个交易日按当时有效日库存/日可借量上限规则 PIT（名单内仍受当日可借量约束；缺库存字段 skip/敏感性；2010-03-31 前无通道）」的诚实组，会**系统性发明假无限日库存空头路径并高估可开空头名义、低估借不到/部分可借失败率**；差异应**集中在融券券池日可借量误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假无限日库存贡献差、可开空头名义差、借券失败率差在标定噪声带内可忽略，且「假无限日库存 / 核对日泄露 / 正常通道窗 / 转融暂停对照窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·BS·BT·K·AB·B·H·W·U·T·S」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 日可借量/日库存上限 ≠ 转融暂停闸门；≠ 融券名单 ∈；≠ 过户费；≠ 强制平仓序；≠ 融资利率档；≠ 融资假零息；≠ 融券借券费；≠ 授信额度上限；≠ 市场25pct余额暂停；≠ 标的调出后存量；≠ 融券权益补偿；≠ 追保禁开；≠ 担保品提取；≠ 合约期限到期了结；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；待预检；建议终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BU；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 U；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BU
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BU；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.daily_short_inventory_honest    写死 pit_by_effective_date
# params.daily_short_inventory_scope     写死 broker_or_lender_daily_borrowable_qty_cap
# params.daily_short_inventory_over_policy 写死 reject_or_partial_or_fail_missing_inventory
# params.daily_short_inventory_naive     写死 invent_unlimited_daily_short_inventory
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page   # 转融暂停闸门交 BB；本页只测日库存；BU≠BB
# params.maint_force_handoff             写死 bc_page
# params.haircut_handoff                 写死 bd_page
# params.balance_pause_handoff           写死 be_page   # 市场25pct交 BE；BU≠BE
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
# params.financing_rate_tier_handoff     写死 bs_page
# params.force_close_order_handoff       写死 bt_page   # 强平序交 BT；BU≠BT；不改 BT
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page    # 融券名单交 K；BU≠K；不改 K
# params.short_px_handoff                写死 ab_page
# params.transfer_fee_handoff            写死 u_page    # 过户费交 U；BU≠U；禁复用假设-U
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.bu0_primary_demo                建议 invent_unlimited_daily_short_inventory  # 主报：假无限日库存；禁与 invent_asof_leak_daily_short_inventory 双挂争主表；BU1半泄露不得升格并列主报
# params.bu0_invent_unlimited_daily_short_inventory 写死 True
# params.bu1_asof_leak_daily_short_inventory_only 写死 True
# params.bu2_pit_daily_short_inventory   写死 True
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
# params.merge_with_BT_force_close_order 写死 False
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
# params.merge_with_S_handling_fee       写死 False
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
# params.universe_rule                   写死 sse_szse_daily_short_inventory_check
# params.missing_daily_short_inventory_policy 写死 skip
# params.day_freq_proxy                  写死 daily_short_inventory_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BU；params.G≠实验字母BU；params.N≠实验字母BU；亦≠单字母实验A/B/U/Z；待预检写死；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
```

```
params.bu0_primary_demo = "invent_unlimited_daily_short_inventory"  # 单一主报建议；禁与 invent_asof_leak_daily_short_inventory 双挂
```

### 2.2 三组对照（BU0 / BU1 / BU2）

| 组 | 口径 | 说明 |
|----|------|------|
| BU0 天真 | `invent_unlimited_daily_short_inventory`（单一主报建议） | 发明假无限日库存/永不检查日可借量上限；禁与 invent_asof_leak_daily_short_inventory 双挂 |
| BU1 半泄露/混口径 | 全样本用 `asof_check_date` 当天更宽日库存或无限库存规则铺满历史 | 仅日库存 asof 泄露；不升格并列主报 |
| BU2 PIT | `daily_short_inventory_honest=pit_by_effective_date` | 每个交易日按当时已生效日库存/日可借量上限 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：信用账户拟新开融券名义 → 对照当日券池可借量代理（或会员日可借上限表）→ 按 BU0/BU1/BU2 规则生成可开空头名义、借不到失败笔、假无限日库存贡献差。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有日终/日频可借量代理 + 融券名单 PIT（消费 K）+ 转融通道状态（消费 BB）+ 当时有效日库存规则生效日表即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BU0 / BU1 / BU2。报告可开空头名义差、假无限日库存贡献差、借券失败/部分可借率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_unlimited_daily_short_inventory",
  "invent_asof_leak_daily_short_inventory",
  "daily_short_inventory_window",
  "refinance_pause_contrast_window",
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
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_U_transfer_fee_avoid",
  "vs_T_csrc_fee_avoid",
  "vs_S_handling_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够融券新开腿或日库存字段；缺日库存字段却静默当无限可借 → 设计失效。  
2. 把「转融暂停后仍假无限源（BB）」静默写成「日库存已诚实」且不声明另页 BB → **与 BB 撞题**（暂停闸门 ≠ 日库存；**尤其 BU≠BB**；**不改 BB**）。  
3. 把「强制平仓序已诚实（BT）」静默写成「日库存已诚实」且不声明另页 BT → **与 BT 撞题**（强平序 ≠ 日可借量；**尤其 BU≠BT**；**不改 BT**）。  
4. 把「在融券名单内（K）」静默写成「日库存够」→ **与 K 撞题**（名单 ∈ ≠ 日库存够；**尤其 BU≠K**；**不改 K**）。  
5. 把「过户费已诚实（U）」写成主病或不声明另页 U → **撞假设-U**，设计失效（**双字母 BU ≠ 单字母 U**；**严禁复用 U**）。  
6. 把「融资假零息（BO）/ 融券借券费（BR）/ 授信够（BH）/ 利率档已诚实（BS）/ 市场25pct未暂停（BE）」静默写成「日库存正确」→ 与对应页撞题（**尤其 BU≠BO≠BR≠BH≠BS≠BE**）。  
7. 把「调出后存量已处理 / 权益已补偿 / 追保未触发 / 提取线未触 / 账户未串用 / 期限未到期 / 名单内可融资 / 保证金比例够」静默写成「日库存正确」且不声明另页 BQ/BP/BM/BL/BN/BF/BA/Z → 与对应页撞题；并**带过 BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK 消歧链**。  
8. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易 / 证管费」写成主病而不声明另页 AB/W/A/H/T → 与对应页撞题。  
9. 把实验字母 BU 与单字母 A/B/U/K/Z/T/S 或双字母 BA–BT/BB/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
10. holdout 反调 `bu0_primary_demo` / Y·G·N·Y2 → 结论无效。  
11. 用复权价算可借名义 → 标签与执行双错，结论无效。  
12. 用核对日更宽「无限日库存」当诚实 PIT、或把券商临时更宽库存提前铺满历史 → 设计失效。  
13. **`bu0_primary_demo` 与 `invent_asof_leak_daily_short_inventory` 双挂主报**；或 BU1 升格并列主报 → 设计失效。  
14. **改写或覆盖 `假设-U` / `假设-BB` / `假设-BT` / `假设-K` / 已冻 AA–BT** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 拟新开融券名义、信用账户空头腿代理；  
- 当时有效券商/出借方日库存或日可借量上限及生效日；  
- 融券名单 PIT / 转融通道状态 / 开仓保证金比例 / 融资名单 / 授信 / 合约期限 / 维持线闸门 / 市场25pct / 追保禁开 / 账户隔离 / 折算率输入（消费 K/BB/Z/BA/BH/BF/BC/BE/BM/BN/BD 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商更严日库存子集；与 BB 暂停窗对照但不混主结论；自有券源另桶敏感性。

**禁止**：用核对日「今天无限日库存」铺满当唯一诚实组；用复权价；把转融未暂停/名单内可空/假零息/借券费/授信够/利率档诚实/强平序诚实/过户费诚实/开仓保证金比例/合约期限未到期/新开名单窗/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/追保未触发/账户未串用/权益已补偿/调出后存量已处理/市场25pct未暂停当成「日库存正确」依据；把 Z/BA–BT/K/AB/A/B/H/W/U/T/S/AN–BT 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BU`  
- **组**：BU0 / BU1 / BU2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`daily_short_inventory_honest=pit_by_effective_date`；`daily_short_inventory_scope=broker_or_lender_daily_borrowable_qty_cap`；`daily_short_inventory_over_policy=reject_or_partial_or_fail_missing_inventory`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`force_close_order_handoff=bt_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_daily_short_inventory_check`；`missing_daily_short_inventory_policy=skip`；`day_freq_proxy=daily_short_inventory_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BU**；**params.G≠实验字母 BU**；**params.N≠实验字母 BU**；亦≠单字母实验 A/B/U/Z；待预检写死；禁 null/holdout/跑后改口）；**`params.bu0_primary_demo` 建议 `invent_unlimited_daily_short_inventory`**（禁与 invent_asof_leak_daily_short_inventory 双挂；BU1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BU0/BU1/BU2 净收益/路径质量、ΔFakeUnlimitedDailyInventory、ΔOpenableShortNotional、ΔBorrowFailOrPartialRate；分桶（融券券池日可借量误开 / 核对日泄露 / 正常通道窗 / 转融暂停对照窗 / 通道前 / vs A·Z·BA–BT·K·AB·B·H·W·U·T·S）。  
- 自检布尔：BU2 是否 pit_by_effective_date；BU0 是否单一主报；BU1 是否仅核对日泄露；是否未与 A/Z/BA–BT/K/AB/B/H/W/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 BU 与 A 或 B 或 U 或 K 或 Z 或 BA–BT 或 BB 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BU≠单字母假设-U；BU≠BB；BU≠BT；BU≠K；BU≠BS；BU≠BO；BU≠BR；BU≠BH；BU≠BQ；BU≠BP；BU≠BN；BU≠BM；BU≠BE；带过 BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BT 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-U / 假设-K / 假设-W / 假设-Z / 假设-BA–BT / 假设-BB / 假设-BT / 假设-AB**；**是否未再改 BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-U（过户费）**；**是否未与 invent_asof_leak_daily_short_inventory 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把无限日库存或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BT 及其他 A/D–BT 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-U**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BT**；**尤其不改假设-BT**；**尤其不改假设-BB**；**不改假设-AB**；**勿再改 BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券空头名单（K）之外，**融券券池日可借量/日频库存上限**须按当时有效规则 PIT；不得默认名单内即可任意量任意日借满。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BU** 标准件，**不改口径主线**，**不改假设 A–BT 正文**，**尤其不改假设-U / 假设-BB / 假设-BT / 假设-K**。与实验 A/Z/BA–BT/K/AB/B/H/W/U/T/S 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA–BT=两融族已冻/在途；BB=转融暂停闸门；K=融券空头新开名单；AB=融券卖出价限；B=历史实验B旧位；H=退市整理；W=除权板价；U=过户费（严禁复用）；T=证管费（避开）；S=经手费；BU=融券券池日可借量误开（BU≠A≠B≠U≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠BM≠BN≠BO≠BP≠BQ≠BR≠BS≠BT≠AB≠W≠H≠T≠S；带过 BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待预检 |
| 数据 | 待接入（字段见 §6；日频可借量代理+名单PIT+通道状态+库存生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**daily_short_inventory_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BU；params.G≠实验字母 BU；params.N≠实验字母 BU；亦≠单字母实验 A/B/U/Z；待预检写死；禁 null/holdout/跑后改口）**；**bu0_primary_demo 建议 invent_unlimited_daily_short_inventory（禁双挂 invent_asof_leak_daily_short_inventory；BU1半泄露不得升格并列主报）**；锚点保留 daily_short_inventory_honest=pit_by_effective_date / daily_short_inventory_scope=broker_or_lender_daily_borrowable_qty_cap / daily_short_inventory_over_policy=reject_or_partial_or_fail_missing_inventory / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**待预检写死**；**params.Y≠BU**；**params.G≠BU**；**params.N≠BU**；禁 null/holdout）  
2. `params.bu0_primary_demo` = `invent_unlimited_daily_short_inventory`（**待预检写死**；禁与 `invent_asof_leak_daily_short_inventory` 双挂；BU1不升格主报）  
3. 日库存锚：`daily_short_inventory_honest=pit_by_effective_date`；`daily_short_inventory_scope=broker_or_lender_daily_borrowable_qty_cap`；`daily_short_inventory_over_policy=reject_or_partial_or_fail_missing_inventory`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/U/A/Z/BA–BT/K/AB/H/W/T/S；**尤其 BU≠U（过户费；严禁复用假设-U）**；**尤其 BU≠BB（暂停闸门≠日库存；不改BB）**；**尤其 BU≠BT（强平序≠日可借量；不改BT）**；**尤其 BU≠K（名单≠日库存；不改K）**；**尤其 BU≠BS/BO/BR/BH/BQ/BP/BN/BM/BE**；**带过 BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 与 BA–BT / U / K 撞题检查表

| 字母 | 主题 | 撞题？ | 消歧 |
|------|------|--------|------|
| BA | 融资买入新开名单 | 否 | — |
| BB | 转融券暂停后假无限券源 | 否 | 暂停闸门 ≠ 日库存上限；**不改 BB** |
| BC | 维持强平闸门 | 否 | — |
| BD | 折算率 | 否 | — |
| BE | 市场25pct暂停 | 否 | 市场层余额占比 ≠ 券商日库存 |
| BF | 合约期限到期了结 | 否 | — |
| BG | 可充抵名单 | 否 | — |
| BH | 授信额度 | 否 | 额度天花板 ≠ 日库存 |
| BI | 融券所得用途 | 否 | — |
| BJ | 融资卖出还债优先 | 否 | — |
| BK | 客户单票集中度 | 否 | — |
| BL | 担保品提取 | 否 | — |
| BM | 追保后禁新开 | 否 | — |
| BN | 跨账户现金混用 | 否 | — |
| BO | 融资利息罚息零 | 否 | — |
| BP | 融券权益补偿 | 否 | — |
| BQ | 调出后存量续持 | 否 | — |
| BR | 融券借券费零 | 否 | 借券费 ≠ 日库存 |
| BS | 融资利率档位优惠档 | 否 | 利率档 ≠ 日库存 |
| BT | 强制平仓顺序与范围 | 否 | 强平序 ≠ 日可借量；**不改 BT** |
| K | 融券新开名单 | 否 | 名单 ∈ ≠ 日库存够；**不改 K** |
| Z | 开仓保证金比例 | 否 | — |
| AB | 融券价限/当日平 | 否 | — |
| U | 过户费现行档 | 否 | **尤其双字母 BU ≠ 单字母 U；严禁复用** |
| A/B/H/W/T/S | 板上/旧B/退市/除权/证管费/经手费 | 否 | **尤其避开预检T；BU≠T≠S** |

**撞题检查：通过（纸面）** — 入库后对照正式清单 #78 再核一次 primary_demo 唯一性。

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BT 补丁已交复检在途 → 写假设-BU；自立 BU，勿占 BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/U/A/Z/K/W/T/S；**尤重 BU≠U**；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BU**；**双字母 BU ≠ 单字母 U**；**BU≠BB/BT/K/BS/BO/BR/BH/BQ/BP/BN/BM/BE**；选题：BB 转融暂停闸门旁的**融券券池日可借量/日频库存上限误开**；`bu0_primary_demo=invent_unlimited_daily_short_inventory`；半泄露 `invent_asof_leak_daily_short_inventory` 禁双挂/升格；**不改假设-BT**；**不改假设-BB**；**不改假设-U**；**不改假设-K**；不改 Y/Z/AA–BT）。结论栏空；**未标纸面齐**。
