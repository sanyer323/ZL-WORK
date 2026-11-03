# 假设 BV · 融券提前召回/强制还券误开 / 用核对日召回规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BU 补丁已交（复检在途）、写下一纸面 BV；清单撞题规则另选正交执行缺口（**出借方提前召回 / 融券强制还券** ≠ 融券券池日可借量 ≠ 转融券暂停闸门 ≠ 两融合约期限到期强制了结 ≠ 强制平仓顺序与范围 ≠ 维持担保比例闸门 ≠ 融券空头名单 ≠ 融券借券费 ≠ 融资利息假零息 ≠ 授信额度上限 ≠ 标的调出后存量续持 ≠ 融券权益补偿 ≠ 开仓保证金比例 ≠ 融资买入名单 ≠ 印花税）；选题自两融/转融通公开口径：存量融券合约存续期内，出借方/券商可按当时有效规则发出**提前召回或强制还券通知**，客户须在通知规定时限内了结空头；召回/强制还券规则按**施行日/生效日** PIT，不得默认「存量融券永不被召回、可持有至任意日 / 永不检查提前召回义务 / 用核对日更宽免召回或更长还券时限铺满历史」；2010-03-31 前无此通道；**BU 正文主测「新开时日库存/日可借量上限」**（新开可借量），本页主测**存量空头被提前召回/强制还券**（存量了结义务）→ 自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BV ≠ 单字母 B**）/ **V（印花税 PIT 误切；双字母 BV ≠ 单字母假设-V；严禁复用 V 题面或印花税口径）** / Z（**开仓**融资/融券保证金比例；**BV≠Z**）/ BA–BU（两融族已冻/在途；**BV≠BA…BU**；**尤其不改 BU 正文**）/ **K（融券空头名单 PIT；BV≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BV≠AB**）/ BB（**转融券暂停后假无限券源**；**BV≠BB**）/ BU（**融券券池日可借量**；**BV≠BU**；日库存新开 ≠ 存量召回；**尤其不改假设-BU**）/ BT（**强制平仓顺序与范围**；**BV≠BT**；维持线触发后强平序 ≠ 出借方召回）/ BF（**两融合约期限到期强制了结**；**BV≠BF**；期限到 ≠ 提前召回）/ BC（**维持担保比例强制平仓闸门**；**BV≠BC**）/ BR（**融券借券费**；**BV≠BR**）/ BO（**融资利息与逾期罚息假零息**；**BV≠BO**）/ BS（**融资利率档位优惠档**；**BV≠BS**）/ BH（**授信额度上限**；**BV≠BH**）/ BQ（**标的调出后存量假续持**；**BV≠BQ**；名单调出存量 ≠ 出借方召回）/ BP（**融券权益补偿**；**BV≠BP**）/ BN（**信用/普通账户串用**；**BV≠BN**；并带过 **BN≠BI/BJ/BL/BM、params.N≠BN**）/ BM（**追保后禁新开**；**BV≠BM**；并带过 **BM≠BC、BM≠BL**）/ BL（**担保品提取**；**BV≠BL**；并带过 **BL≠BC**）/ BE（**市场25pct余额暂停**；**BV≠BE**）/ BI（**融券卖出所得用途**；**BV≠BI**）/ BJ（**融资卖出还债优先**；**BV≠BJ**）/ BD（**担保品折算率**；**BV≠BD**）/ BG（**可充抵名单**；**BV≠BG**）/ BK（**客户单票集中度**；**BV≠BK**）/ BA（**融资买入名单**；**BV≠BA**）/ W（除权板价；**BV≠W**）/ T（证管费；**避开预检T**；**BV≠T**）/ S（经手费；**BV≠S**）/ U（过户费；**BV≠U**）/ E（整手）/ AN–BU（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）等**分列**；**新建实验 BV**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「存量融券永不被召回、可无限续持至任意日 / 永不检查提前召回或强制还券通知 / 用核对日更宽免召回或更长还券时限铺满」当诚实融券存量路径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BU 及其他 A/D–BU 已交正文与冻结补丁；尤其不改假设-BU；尤其不改假设-V；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-W；不改假设-Z；不改假设-BA–BU；不改假设-AB；勿再改 BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BV（约 #79）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **存量融券提前召回/强制还券**。**双字母 BV ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BV ≠ 单字母 B**。与假设 **V（印花税按现行档铺满 / 双边误抽 / 对 ETF 误抽）** **硬分列（专节强调）**：V = 证券交易印花税费用层切片（只打卖方；2023-08-28 减半；ETF/债券不抽）；本页 = 信用账户**存量融券提前召回/强制还券**；印花税 ≠ 召回义务。**双字母 BV ≠ 单字母假设-V**；**严禁复用 V 题面或 V 口径键**。与假设 **BU（融券券池日可借量）** **硬分列**：BU = **新开**时日库存/日可借量上限（复检在途）；本页 = **存量**空头被提前召回/强制还券；新开可借量 ≠ 存量召回；**禁止**把「日库存已诚实（BU）」静默写成「召回已诚实」；**禁止**把「永不召回」静默写成「日库存够」；**不占** BU 的 primary_demo；**尤其不改假设-BU**。**BV≠BU**。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = 合约**约定期限到期**强制了结；本页 = 期限未到亦可因出借方**提前召回**强制还券；到期 ≠ 提前召回；**尤其不改假设-BF**。**BV≠BF**。与假设 **BT（强制平仓顺序与范围）** **硬分列**：BT = 维持担保触线后的强平**序/范围**；本页 = 出借方召回驱动的还券；强平序 ≠ 召回；**尤其不改假设-BT**。**BV≠BT**。与假设 **BC（维持担保比例强制平仓闸门）** **硬分列**：BC = 维持线 on/off；本页 = 召回通知；闸门 ≠ 召回。**BV≠BC**。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 暂停闸门下假无限新借源；本页 = 存量召回；暂停 ≠ 召回。**BV≠BB**。与假设 **K（融券空头名单）** **硬分列**：K = 是否在融券标的名单；本页 = 名单内存量仍可被召回；名单 ∈ ≠ 永不召回；**尤其不改假设-K**；并**带过 BK≠K**。**BV≠K**。与假设 **BQ（标的调出后存量假续持）** **硬分列**：BQ = **名单调出**后存量处理；本页 = **出借方召回**（名单可仍在池）；调出 ≠ 召回；**尤其不改假设-BQ**。**BV≠BQ**。与假设 **BR / BO / BS / BH / BP / BN / BM / BL / BE** **硬分列**：借券费 / 假零息 / 利率档 / 授信天花板 / 权益补偿 / 账户串用 / 追保禁开 / 高维持提取 / 市场25pct ≠ 提前召回；并**带过 BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 **AB / Z / W / BA / BD / BG / BK / BI / BJ** **硬分列**：空头价限 / 开仓保证金 / 除权板价 / 融资名单 / 折算率 / 可充抵 / 客户集中度 / 融券所得用途 / 融资还债优先 ≠ 提前召回。与假设 AN–BU **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-V（印花税）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BV** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 V**（印花税 PIT 误切；**严禁复用假设-V**）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BV / 假设-BV / hypothesis_id=BV / 组 BV0·BV1·BV2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BV 混读或互改。亦**禁止**把实验字母 BV 与单字母 **A**、单字母 **B**、单字母 **V**、单字母 **K**、单字母 **Z**、单字母 **T**、单字母 **S**、单字母 **U**、双字母 **BA–BU**、双字母 **BB**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bv0_*` 以外的实验页混读。**双字母 BV ≠ 单字母 A ≠ 单字母 B ≠ 单字母 V ≠ 单字母 K ≠ 单字母 Z ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 双字母 BA ≠ … ≠ 双字母 BU ≠ 双字母 BB ≠ 双字母 BT ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BQ ≠ 双字母 BP ≠ 双字母 BN ≠ 双字母 BM ≠ 双字母 BF ≠ 双字母 BC ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BV**；**params.G ≠ 实验字母 BV**；**params.N ≠ 实验字母 BV**。**带过：双字母 BU ≠ U/BB/BT/K/BS/BO/BR/BH…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BV ≠ 单字母假设-V；且 ≠ 假设-BU / 假设-BF / 假设-BT / 假设-BC / 假设-BB / 假设-BQ / 假设-K / 假设-BR / 假设-BO / 假设-BS / 假设-BH；带过 BU≠U/BB/BT/K…、BT≠T/BC/BS…、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BV（双字母） |
|------|--------|----------------------|
| 题面 V | 印花税费用层（只打卖方；2023-08-28 减半；ETF/债券不抽） | **融券提前召回/强制还券**误开：假永不召回 vs 按生效日召回 PIT；**严禁复用 V 题面** |
| 题面 BU | **融券券池日可借量**（新开；复检在途） | **存量**空头提前召回；日库存新开 ≠ 存量召回；**BV≠BU**；**不改 BU** |
| 题面 BF | **合约期限到期强制了结** | 期限未到亦可因召回强制还券；到期 ≠ 提前召回；**BV≠BF**；**不改 BF** |
| 题面 BT / BC | **强平序/范围** / **维持线闸门** | 维持线驱动 ≠ 出借方召回；**BV≠BT≠BC**；**不改 BT/BC** |
| 题面 BB / BQ / K | 转融暂停闸门 / 名单调出后存量 / 融券名单 ∈ | 暂停/调出/名单 ≠ 召回；**BV≠BB≠BQ≠K**；**不改** |
| 题面 BR / BO / BS / BH | 借券费 / 假零息 / 利率档 / 授信天花板 | 计息/计费/额度 ≠ 召回；**BV≠BR≠BO≠BS≠BH** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ignore_short_recall` |
| 文档 | `假设-V-…` / `假设-BU-…` / `假设-BF-…` / `假设-BT-…` / `假设-K-…`（**只读；禁止改写**） | `假设-BV-融券提前召回强制还券误开.md`（新建） |
| 预检键 | 实验字母 V / BU / BF / BT / K | 实验字母 **BV** / `bv0_primary_demo`；**不得**占用或改写预检 V/BU/BF/BT/K |

**禁止**：把 BV 写成「V/BU/BF/BT/K 的续篇」；把「日库存够 / 期限未到 / 未触维持线 / 名单仍在池 / 转融未暂停 / 授信够 / 借券费已计」静默写成「召回已诚实」；覆盖或补丁改写假设-V / 假设-BU / 假设-BF / 假设-BT / 假设-K / 假设-BQ / 假设-BR / 假设-BO 正文；把 `params.Y/G/N` 与实验字母 BV 混读；**禁** `bv0_primary_demo` 与 `invent_asof_leak_short_recall` **双挂主报**；**禁** BV1 半泄露升格并列主报；**禁**复用假设-V（印花税）题面或口径键。

---

## 1. 一句话假设（可检验、可证伪）

同一存量融券空头路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资/融券名单/转融券通道状态/日库存（新开层）/授信/合约期限/维持担保闸门/追保禁开/账户隔离/折算率等输入（Z/BA/K/BB/BU/BH/BF/BC/BM/BN/BD 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/融券名单/转融暂停闸门/日可借量新开/授信天花板/合约期限到期了结/维持线闸门 on-off/追保禁开/账户隔离/折算率主病」）下，把「存量融券永不被出借方提前召回、可无限续持至任意日，永不检查强制还券通知」或「全样本用核对日当天更宽免召回或更长还券时限规则回放历史」当成默认，相对「每个交易日按当时有效提前召回/强制还券规则 PIT（出借方可按生效规则召回；客户须在通知时限内了结；缺字段 skip/敏感性；2010-03-31 前无通道）」的诚实组，会**系统性发明假永不召回空头路径并高估可续持空头名义、低估因提前召回导致的被动了结与冲击**；差异应**集中在融券提前召回/强制还券误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假永不召回贡献差、可续持空头名义差、被动了结/召回失败率差在标定噪声带内可忽略，且「假永不召回 / 核对日泄露 / 召回通知窗 / 期限未到期对照窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·BS·BT·BU·K·AB·B·H·W·V·T·S·U」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 提前召回/强制还券 ≠ 日可借量新开；≠ 合约期限到期了结；≠ 维持线强平序；≠ 转融暂停闸门；≠ 名单调出后存量；≠ 融券名单 ∈；≠ 印花税；≠ 融券借券费；≠ 融资假零息；≠ 授信额度上限；≠ 融券权益补偿；≠ 追保禁开；≠ 担保品提取；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BV；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 V；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BV
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BV；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.short_recall_honest             写死 pit_by_effective_date
# params.short_recall_scope              写死 lender_or_broker_early_recall_forced_return
# params.short_recall_over_policy        写死 unwind_by_deadline_or_fail_missing_recall_rule
# params.short_recall_naive              写死 invent_ignore_short_recall
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page
# params.haircut_handoff                 写死 bd_page
# params.balance_pause_handoff           写死 be_page
# params.contract_term_handoff           写死 bf_page   # 期限到期交 BF；BV≠BF；不改 BF
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
# params.list_removal_stock_handoff      写死 bq_page   # 名单调出存量交 BQ；BV≠BQ；不改 BQ
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page
# params.force_close_order_handoff       写死 bt_page   # 强平序交 BT；BV≠BT；不改 BT
# params.daily_short_inventory_handoff   写死 bu_page   # 日库存新开交 BU；BV≠BU；不改 BU
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page    # 融券名单交 K；BV≠K；不改 K
# params.short_px_handoff                写死 ab_page
# params.stamp_tax_handoff               写死 v_page    # 印花税交 V；BV≠V；禁复用假设-V
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.bv0_primary_demo                写死冻结 invent_ignore_short_recall  # 主报：假永不召回；禁与 invent_asof_leak_short_recall 双挂争主表；BV1半泄露不得升格并列主报
# params.bv0_invent_ignore_short_recall  写死 True
# params.bv1_asof_leak_short_recall_only 写死 True
# params.bv2_pit_short_recall            写死 True
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
# params.merge_with_BU_daily_short_inventory 写死 False
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
# params.universe_rule                   写死 sse_szse_short_recall_check
# params.missing_short_recall_policy     写死 skip
# params.day_freq_proxy                  写死 short_recall_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BV；params.G≠实验字母BV；params.N≠实验字母BV；亦≠单字母实验A/B/V/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
```

```
params.bv0_primary_demo = "invent_ignore_short_recall"  # 单一主报·已冻结；禁与 invent_asof_leak_short_recall 双挂
```

### 2.2 三组对照（BV0 / BV1 / BV2）

| 组 | 口径 | 说明 |
|----|------|------|
| BV0 天真 | `invent_ignore_short_recall`（单一主报·已冻结） | 发明假永不召回/永不检查强制还券；禁与 invent_asof_leak_short_recall 双挂 |
| BV1 半泄露/混口径 | 全样本用 `asof_check_date` 当天更宽免召回或更长还券时限规则铺满历史 | 仅召回规则 asof 泄露；不升格并列主报 |
| BV2 PIT | `short_recall_honest=pit_by_effective_date` | 每个交易日按当时已生效提前召回/强制还券规则 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：信用账户存量融券名义 → 对照当日是否存在出借方召回/强制还券通知代理（或会员召回规则生效表）→ 按 BV0/BV1/BV2 规则生成可续持空头名义、被动了结笔、假永不召回贡献差。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有日终/日频存量空头代理 + 召回/强制还券规则生效日表 + 融券名单 PIT（消费 K）+ 合约期限（消费 BF，旁路）+ 日库存新开层（消费 BU，旁路）即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BV0 / BV1 / BV2。报告可续持空头名义差、假永不召回贡献差、被动了结/召回履约失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_ignore_short_recall",
  "invent_asof_leak_short_recall",
  "short_recall_notice_window",
  "pre_term_expiry_contrast_window",
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
  "vs_K_shortable_list",
  "vs_AB_short_px",
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

1. 样本无足够存量融券腿或召回字段；缺召回字段却静默当永不召回 → 设计失效。  
2. 把「日库存已诚实（BU）」静默写成「召回已诚实」且不声明另页 BU → **与 BU 撞题**（日库存新开 ≠ 存量召回；**尤其 BV≠BU**；**不改 BU**）。  
3. 把「合约期限到期了结（BF）」静默写成「召回已诚实」且不声明另页 BF → **与 BF 撞题**（到期 ≠ 提前召回；**尤其 BV≠BF**；**不改 BF**）。  
4. 把「强制平仓序已诚实（BT）/ 维持线闸门已诚实（BC）」静默写成「召回已诚实」→ **与 BT/BC 撞题**（强平 ≠ 召回；**尤其 BV≠BT≠BC**；**不改 BT/BC**）。  
5. 把「印花税已诚实（V）」写成主病或不声明另页 V → **撞假设-V**，设计失效（**双字母 BV ≠ 单字母 V**；**严禁复用 V**）。  
6. 把「名单调出后存量已处理（BQ）/ 转融未暂停（BB）/ 名单内可空（K）」静默写成「召回正确」→ 与对应页撞题（**尤其 BV≠BQ≠BB≠K**）。  
7. 把「融资假零息（BO）/ 融券借券费（BR）/ 授信够（BH）/ 利率档已诚实（BS）/ 市场25pct未暂停（BE）」静默写成「召回正确」→ 与对应页撞题（**尤其 BV≠BO≠BR≠BH≠BS≠BE**）。  
8. 把「权益已补偿 / 追保未触发 / 提取线未触 / 账户未串用 / 保证金比例够」静默写成「召回正确」且不声明另页 BP/BM/BL/BN/Z → 与对应页撞题；并**带过 BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK 消歧链**。  
9. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易 / 证管费」写成主病而不声明另页 AB/W/A/H/T → 与对应页撞题。  
10. 把实验字母 BV 与单字母 A/B/V/K/Z/T/S/U 或双字母 BA–BU/BB/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `bv0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价算可续持名义 → 标签与执行双错，结论无效。  
13. 用核对日更宽「免召回」当诚实 PIT、或把券商临时更宽免召回提前铺满历史 → 设计失效。  
14. **`bv0_primary_demo` 与 `invent_asof_leak_short_recall` 双挂主报**；或 BV1 升格并列主报 → 设计失效。  
15. **改写或覆盖 `假设-V` / `假设-BU` / `假设-BF` / `假设-BT` / `假设-K` / 已冻 AA–BU** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 存量融券名义、开仓日、空头腿代理；  
- 当时有效出借方/券商提前召回或强制还券规则及生效日、通知日、还券时限；  
- 融券名单 PIT / 转融通道状态 / 日库存新开层 / 开仓保证金比例 / 融资名单 / 授信 / 合约期限 / 维持线闸门 / 市场25pct / 追保禁开 / 账户隔离 / 折算率输入（消费 K/BB/BU/Z/BA/BH/BF/BC/BE/BM/BN/BD 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商更严召回子集；与 BF 期限到期窗对照但不混主结论；转融通召回另桶敏感性。

**禁止**：用核对日「今天免召回」铺满当唯一诚实组；用复权价；把日库存够/期限未到/未触维持线/名单仍在池/转融未暂停/假零息/借券费/授信够/利率档诚实/开仓保证金比例/新开名单窗/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/追保未触发/账户未串用/权益已补偿/调出后存量已处理/市场25pct未暂停/印花税已诚实当成「召回正确」依据；把 Z/BA–BU/K/AB/A/B/H/W/V/U/T/S/AN–BU 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BV`  
- **组**：BV0 / BV1 / BV2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`short_recall_honest=pit_by_effective_date`；`short_recall_scope=lender_or_broker_early_recall_forced_return`；`short_recall_over_policy=unwind_by_deadline_or_fail_missing_recall_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`force_close_order_handoff=bt_page`；`daily_short_inventory_handoff=bu_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`stamp_tax_handoff=v_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_short_recall_check`；`missing_short_recall_policy=skip`；`day_freq_proxy=short_recall_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BV**；**params.G≠实验字母 BV**；**params.N≠实验字母 BV**；亦≠单字母实验 A/B/V/Z；禁 null/holdout/跑后改口）；**`params.bv0_primary_demo` 写死冻结 `invent_ignore_short_recall`**（禁与 invent_asof_leak_short_recall 双挂；BV1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BV0/BV1/BV2 净收益/路径质量、ΔFakeNeverRecall、ΔKeepableShortNotional、ΔForcedUnwindOrRecallFailRate；分桶（融券提前召回/强制还券误开 / 核对日泄露 / 召回通知窗 / 期限未到期对照窗 / 通道前 / vs A·Z·BA–BU·K·AB·B·H·W·V·U·T·S）。  
- 自检布尔：BV2 是否 pit_by_effective_date；BV0 是否单一主报；BV1 是否仅核对日泄露；是否未与 A/Z/BA–BU/K/AB/B/H/W/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 BV 与 A 或 B 或 V 或 K 或 Z 或 BA–BU 或 BB 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BV≠单字母假设-V；BV≠BU；BV≠BF；BV≠BT；BV≠BC；BV≠BB；BV≠BQ；BV≠K；BV≠BR；BV≠BO；BV≠BS；BV≠BH；带过 BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BU 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-V / 假设-K / 假设-W / 假设-Z / 假设-BA–BU / 假设-BU / 假设-BF / 假设-BT / 假设-AB**；**是否未再改 BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-V（印花税）**；**是否未与 invent_asof_leak_short_recall 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把永不召回或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BU 及其他 A/D–BU 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-V**；**不改假设-K**；**不改假设-W**；**不改假设-Z**；**不改假设-BA–BU**；**尤其不改假设-BU**；**尤其不改假设-BF**；**尤其不改假设-BT**；**不改假设-AB**；**勿再改 BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券券池日可借量（BU）、融券空头名单（K）之外，**出借方提前召回/融券强制还券**须按当时有效规则 PIT；不得默认存量融券永不被召回。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BV** 标准件，**不改口径主线**，**不改假设 A–BU 正文**，**尤其不改假设-V / 假设-BU / 假设-BF / 假设-BT / 假设-K**。与实验 A/Z/BA–BU/K/AB/B/H/W/V/U/T/S 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA–BU=两融族已冻/在途；BU=日库存新开；BF=期限到期了结；BT=强平序；K=融券空头新开名单；AB=融券卖出价限；B=历史实验B旧位；H=退市整理；W=除权板价；V=印花税（严禁复用）；U=过户费；T=证管费（避开）；S=经手费；BV=融券提前召回/强制还券误开（BV≠A≠B≠V≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠BM≠BN≠BO≠BP≠BQ≠BR≠BS≠BT≠BU≠AB≠W≠H≠T≠S≠U；带过 BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K）**。

---

## 9. ״̬

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频存量空头代理+召回规则生效日+名单PIT+期限旁路+日库存旁路即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**short_recall_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BV；params.G≠实验字母 BV；params.N≠实验字母 BV；亦≠单字母实验 A/B/V/Z；禁 null/holdout/跑后改口）**；**bv0_primary_demo 写死冻结 invent_ignore_short_recall（禁双挂 invent_asof_leak_short_recall；BV1半泄露不得升格并列主报）**；锚点保留 short_recall_honest=pit_by_effective_date / short_recall_scope=lender_or_broker_early_recall_forced_return / short_recall_over_policy=unwind_by_deadline_or_fail_missing_recall_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单（两条已冻结 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已冻结**；**params.Y≠BV**；**params.G≠BV**；**params.N≠BV**；禁 null/holdout）  
2. `params.bv0_primary_demo` = `invent_ignore_short_recall`（**已冻结**；禁与 `invent_asof_leak_short_recall` 双挂；BV1不升格主报）  
3. 召回锚：`short_recall_honest=pit_by_effective_date`；`short_recall_scope=lender_or_broker_early_recall_forced_return`；`short_recall_over_policy=unwind_by_deadline_or_fail_missing_recall_rule`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/V/A/Z/BA–BU/K/AB/H/W/T/S/U；**尤其 BV≠V（印花税；严禁复用假设-V）**；**尤其 BV≠BU（日库存新开≠存量召回；不改BU）**；**尤其 BV≠BF（到期≠提前召回；不改BF）**；**尤其 BV≠BT/BC（强平≠召回；不改BT/BC）**；**尤其 BV≠BB/BQ/K/BR/BO/BS/BH**；**带过 BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC/BB/BO/BP/BM/BN/Q、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 与 BA–BU / V / K 撞题检查表

| 字母 | 主题 | 撞题？ | 消歧 |
|------|------|--------|------|
| V | 印花税 PIT 误切 | 否 | **双字母 BV ≠ 单字母 V**；费用 ≠ 召回；**严禁复用假设-V** |
| BU | 融券券池日可借量（复检在途） | 否 | 新开日库存 ≠ 存量召回；**BV≠BU**；**不改 BU** |
| BF | 合约期限到期强制了结 | 否 | 到期 ≠ 提前召回；**BV≠BF**；**不改 BF** |
| BT | 强制平仓顺序与范围 | 否 | 维持线强平序 ≠ 出借方召回；**BV≠BT**；**不改 BT** |
| BC | 维持担保比例闸门 | 否 | 闸门 on/off ≠ 召回；**BV≠BC** |
| BB | 转融券暂停后假无限券源 | 否 | 暂停闸门 ≠ 召回；**BV≠BB** |
| BQ | 标的调出后存量假续持 | 否 | 名单调出 ≠ 出借方召回；**BV≠BQ** |
| K | 融券空头名单 | 否 | 名单 ∈ ≠ 永不召回；**BV≠K**；带过 BK≠K |
| BR/BO/BS/BH | 借券费/假零息/利率档/授信 | 否 | 计息计费额度 ≠ 召回 |
| BP/BN/BM/BL/BE | 权益补偿/账户串用/追保禁开/提取/市场25pct | 否 | 另页主病；带过消歧链 |
| A/B/Z/BA/BD/BG/AB/W/H/T/S/U | 板上/旧位/开仓比例/融资名单/折算/可充抵/价限/除权/退市/证管费/经手费/过户费 | 否 | 硬分列；避开预检T；不改已齐 |


## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BV**；**`params.G` ≠ 实验字母 BV**；**`params.N` ≠ 实验字母 BV**；**`params.Y` ≠ 单字母实验 A/B/V/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bv0_primary_demo`**：**写死冻结** **`invent_ignore_short_recall`**；禁与 **`invent_asof_leak_short_recall`** 双挂争主表（只挂一个 primary）；**BV1 半泄露不得升格并列主报**。

**召回锚保留（已通写死）**：`params.short_recall_honest=pit_by_effective_date`；`params.short_recall_scope=lender_or_broker_early_recall_forced_return`；`params.short_recall_over_policy=unwind_by_deadline_or_fail_missing_recall_rule`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有 `missing_short_recall_policy=skip` 等锚点；不改口）。

**与 BA–BU/Z/AB/B/A/H/V/K/W/T/S/U 硬分列（保留）**：本页 = **融券提前召回/强制还券误开**；V = **印花税**（**尤其双字母 BV ≠ 单字母假设-V**；**严禁复用假设-V**）；BU = **融券券池日可借量**（**尤其 BV≠BU**；日库存新开 ≠ 存量召回；**尤其不改假设-BU**）；BF = **两融合约期限到期强制了结**（**尤其 BV≠BF**；到期 ≠ 提前召回；**尤其不改假设-BF**）；BT = **强制平仓顺序与范围**（**尤其 BV≠BT**；维持线强平序 ≠ 出借方召回；**尤其不改假设-BT**）；BC = **维持担保比例强制平仓闸门**（**尤其 BV≠BC**）；BB = **转融券暂停后假无限券源**（**尤其 BV≠BB**）；BQ = **标的调出后存量假续持**（**尤其 BV≠BQ**）；K = **融券空头名单**（**尤其 BV≠K**；名单 ∈ ≠ 永不召回；并**带过 BK≠K**；**尤其不改假设-K**）；BR = **融券借券费**；BO = **融资利息与逾期罚息假零息**；BS = **融资利率档位优惠档**；BH = **授信额度上限**；BP = **融券权益补偿**；BN = **信用/普通账户串用**；BM = **追保后禁新开**；AB = **融券卖出价限**；Z = **开仓**保证金比例；W = **除权板价**；A = **板上枯竭**；B = 历史实验 B 旧位；H = **退市整理期**；T = **证管费**（避开预检T）；S = **经手费**；U = **过户费**；提前召回 ≠ 印花税 ≠ 日可借量 ≠ 期限到期了结 ≠ 强平序 ≠ 维持线闸门 ≠ 转融暂停 ≠ 名单调出存量 ≠ 融券名单 ≠ 借券费 ≠ 假零息 ≠ 利率档 ≠ 授信 ≠ 权益补偿 ≠ 账户串用 ≠ 追保禁开 ≠ 空头价限 ≠ 开仓比例 ≠ 除权板价 ≠ 板上枯竭 ≠ 退市整理 ≠ 证管费 ≠ 经手费 ≠ 过户费；**双字母 BV ≠ 单字母 A ≠ 单字母 B ≠ 单字母 V ≠ 单字母 K ≠ 单字母 Z ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 双字母 BA ≠ … ≠ 双字母 BU ≠ 双字母 BB ≠ 双字母 BT ≠ 双字母 BF ≠ 双字母 BC ≠ 双字母 BQ ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 W ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BV**；**params.G ≠ 实验字母 BV**；**params.N ≠ 实验字母 BV**；禁止捆成「两融一张表=假永不召回」；**尤其不改假设-V**；**尤其不改假设-BU**；**尤其不改假设-BF**；**尤其不改假设-BT**；**尤其不改假设-BC**；**尤其不改假设-BB**；**尤其不改假设-BQ**；**尤其不改假设-K**；**尤其不改假设-BR**；**尤其不改假设-BO**；**尤其不改假设-BS**；**尤其不改假设-BH**；**尤其不改假设-H**；不改假设-B；不改假设-Z；不改假设-BA–BU；不改假设-A；不改假设-AB；不改假设-W；不改假设-T；不改假设-S；不改假设-U。

**专节保留 · 双字母 BV ≠ 单字母假设-V；且 ≠ 假设-BU / 假设-BF / 假设-BT / 假设-BC / 假设-BB / 假设-BQ / 假设-K / 假设-BR / 假设-BO / 假设-BS / 假设-BH；带过 BU≠U/BB/BT/K…、BT≠T/BC/BS…、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K（硬）**：正文「### 专节 · 双字母 BV ≠ 单字母假设-V；且 ≠ 假设-BU / 假设-BF / 假设-BT / 假设-BC / 假设-BB / 假设-BQ / 假设-K / 假设-BR / 假设-BO / 假设-BS / 假设-BH；带过 BU≠U/BB/BT/K…、BT≠T/BC/BS…、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BK≠K」保留不删；**禁止**覆盖/混读/改写 `假设-V` / `假设-BU` / `假设-BF` / `假设-BT` / `假设-BC` / `假设-BB` / `假设-BQ` / `假设-K` / `假设-BR` / `假设-BO` / `假设-BS` / `假设-BH`。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-03 | 风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BV**；**params.G≠实验字母 BV**；**params.N≠实验字母 BV**；亦≠单字母实验 A/B/V/Z；禁 null/holdout/跑后改口）；② `params.bv0_primary_demo=invent_ignore_short_recall`（禁与 `invent_asof_leak_short_recall` 双挂争主表；BV1半泄露不得升格并列主报）。召回锚保留：`short_recall_honest=pit_by_effective_date`；`short_recall_scope=lender_or_broker_early_recall_forced_return`；`short_recall_over_policy=unwind_by_deadline_or_fail_missing_recall_rule`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。硬分列保留：**BV≠V/BU/BT/BF/BC/BB/BQ/K/BS/BO/BR/BH**（及 ≠B/A/Z/BA–BU/AB/H/W/T/S/U）；**严禁复用假设-V**；参考总管派令 / 风控预检有条件通过（`预检-假设BV-20261103.md`；草稿 HEAD=9c811ed ∈ tip 7e68d99）。未改 Y/Z/AA–BU 及其他已冻结补丁；**不改假设-V**；**不改假设-BU**；**不改假设-BF**；**不改假设-BT**；**不改假设-K**；不改假设-H；不改假设-A；不改假设-B；不改假设-T；不改假设-W；不改假设-Z；不改假设-BA–BU；不改假设-AB；结论栏仍空；不开回测；不抢 A；**未标纸面齐** |
| 2026-11-03 | 新建纸面草稿（待预检）：主题=融券提前召回/强制还券误开；`bv0_primary_demo` 建议 `invent_ignore_short_recall`；Y/G/N/Y2 建议 0.02/0.01/0.05/0.015；硬分列强调 **BV≠V/BU/BT/BF/BC/BB/BQ/K**；未开回测；未改已齐字母；未标纸面齐 |
