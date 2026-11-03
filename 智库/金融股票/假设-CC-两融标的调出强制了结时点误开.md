# 假设 CC · 两融标的调出强制了结时点误开 / 用核对日无限拖或随意续作时限铺满（执行鸿沟）

更新：2026-11-04  
来源：总管线 / A/D–CB纸面齐（tip=`e5a2c18`；复检通过后写下一纸面 CC）；清单撞题规则另选正交执行缺口（**标的从两融标的池调出后的强制了结/了结时限** ≠ 股票池当时名单/幸存者偏差 ≠ 维持担保比例分子分母 ≠ 融资合约展期/续作审批 ≠ 追保宽限期/强平通知时限 ≠ 融资提前了结手续费/违约金 ≠ 标的调出后存量假续持（能否续持） ≠ 合约期限到期强制了结 ≠ 融资买入新开名单 ≠ 板上枯竭）；选题自融资融券业务公开口径：融资买入/融券标的名单按生效日调整；**调出后存量一般须在约定期限内强制了结**（了结时限/强制平仓时点按细则/合同与会员加严）；规则按**施行日/生效日** PIT；不得默认「调出后强制了结时限可无限拖、或当日即可随意续作/无限顺延」，或用核对日更宽无限拖/随意续作时限规则铺满历史；本页**假定调出后存量层（BQ）/追保宽限层（BY）/合约期限到期层（BF）/展期审批层（CB）/维持比公式层（CA）/提前了结费层（BZ）/开仓保证金（Z）/融资名单新开（BA）诚实或显式旁路**，主病只在**两融标的调出后强制了结时点/了结时限**；2010-03-31 前无此通道；**C 正文主测「股票池当时名单/幸存者偏差」**（**双字母 CC ≠ 单字母假设-C；严禁复用 C 题面**），**CA 正文主测「维持担保比例分子分母口径」**（A/D–CA已纸面齐；**严禁改 CA**），**CB 正文主测「融资合约展期/续作审批」**（A/D–CB纸面齐；`invent_always_allow_financing_rollover`；**严禁改 CB**），**BY 正文主测「追保宽限期/强平通知时限」**（`invent_ignore_margin_call_grace_or_force_deadline`；追保宽限 ≠ 调出了结时限；**严禁改 BY**），**BZ 正文主测「融资提前了结手续费/违约金」**（**严禁改 BZ**），**BQ 正文主测「标的调出后存量假续持」**（`invent_keep_open_after_list_removal`；能否假续持 ≠ 了结时限日历；**严禁改 BQ**），**BF 正文主测「合约期限到期强制了结」**（到期日闸门 ≠ 名单调出了结时限；**严禁改 BF**），本页主测**两融标的调出强制了结时点被误开**（`invent_ignore_margin_universe_delist_force_deadline`）→ 自立；与假设 A（板上；**CC≠A**）/ H（退市整理）/ B（历史清单实验 B 旧位；**双字母 CC ≠ 单字母 B；CC≠B**）/ **C（股票池当时名单；双字母 CC ≠ 单字母假设-C；严禁复用 C；CC≠C）** / **CA（维持比分子分母；CC≠CA；公式 ≠ 调出了结时限；尤其不改假设-CA）** / **CB（融资展期审批；CC≠CB；展期审批 ≠ 调出了结时限；尤其不改假设-CB）** / Z（开仓保证金比例；**CC≠Z**）/ BA–CB（两融族已冻/在途；**CC≠BA…CB**；**尤其不改 CB/CA/BQ/BY/BZ/BF**）/ **BQ（调出后存量假续持；CC≠BQ；假续持 ≠ 了结时限；尤其不改假设-BQ）** / **BY（追保宽限期；CC≠BY；追保宽限 ≠ 调出了结时限；尤其不改假设-BY）** / **BZ（提前了结费；CC≠BZ；尤其不改假设-BZ）** / **BF（合约期限到期强制了结；CC≠BF；尤其不改假设-BF）** / BW/BV/BU/BS/BO/BR/BH/BX/BC/BT/BD/BL 等**分列**；**新建实验 CC**  
状态：**草稿 · 待入库预检**（结论栏空；禁止把「假无限拖调出了结时限 / 用核对日无限拖或随意续作时限规则铺满」当诚实调出强制了结时点口径；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CB 及其他 A/D–CB 已交正文与冻结补丁；尤其不改假设-C；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-BQ；尤其不改假设-BY；尤其不改假设-BZ；尤其不改假设-BF；尤其不改假设-A；不改假设-H；不改假设-K；不改假设-BA–CB；不改假设-AB；勿再改 CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CC（约 #86）。与假设 **C（股票池当时名单/幸存者偏差）** **硬分列（专节强调）**：C = 成分/股票池 PIT 与幸存者偏差；本页 = **两融标的调出后强制了结时点/了结时限**；幸存者偏差 ≠ 调出了结时限。**双字母 CC ≠ 单字母假设-C**；**严禁复用 C 题面**；**绝不可做成 C 续篇**。与假设 **CA（维持担保比例分子分母口径）** **硬分列（专节强调）**：CA = 维持比**怎么算**；本页 = 调出后**何时必须强制了结**；公式 ≠ 了结时限；**禁止**把「分子分母已诚实（CA）」静默写成「调出了结时限已诚实」；**不占** CA 的 `invent_wrong_maint_guarantee_ratio_num_den`；**尤其不改假设-CA**。**CC≠CA**。与假设 **CB（融资合约展期/续作审批）** **硬分列（专节强调）**：CB = 合约到期前展期/续作是否须审批；本页 = 名单调出后强制了结时限；展期审批 ≠ 调出了结时限；**禁止**把「展期审批已诚实（CB）」静默写成「调出了结时限已诚实」；**不占** CB 的 `invent_always_allow_financing_rollover`；**尤其不改假设-CB**。**CC≠CB**。与假设 **BQ（标的调出后存量假续持）** **硬分列（专节强调）**：BQ = 调出后是否仍假可无限续持/展期加仓（**能否**续持）；本页 = 调出后强制了结的**时限日历**（**何时**必须了结）；假续持 ≠ 了结时限；**禁止**把「存量处理已诚实（BQ）」静默写成「了结时限已诚实」；**不占** BQ 的 `invent_keep_open_after_list_removal`；**尤其不改假设-BQ**。**CC≠BQ**。与假设 **BY（追保宽限期/强平通知时限）** **硬分列（专节强调）**：BY = 追保通知后宽限几天；本页 = **名单调出**后强制了结时限；追保宽限 ≠ 调出了结时限；**禁止**复用 BY 的 `invent_ignore_margin_call_grace_or_force_deadline` 当本页主报；**尤其不改假设-BY**。**CC≠BY**。与假设 **BZ（融资提前了结手续费/违约金）** **硬分列**：BZ = 主动提前了结费；本页 = 调出了结时限；提前了结费 ≠ 调出了结时限；**尤其不改假设-BZ**。**CC≠BZ**。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = **合约期限到期日**是否强制了结；本页 = **名单调出**后的强制了结时限；到期了结 ≠ 调出了结时限；**尤其不改假设-BF**。**CC≠BF**。与假设 **BA（融资买入新开名单）** **硬分列**：BA = **新开**是否在融资名单；本页 = 调出后存量了结时限；新开 ≠ 调出了结时限。**CC≠BA**。与假设 **BW / BV / BU / BS / BO / BR / BH / BX / BC / BT / BD / BL / BM / Z / K / AB** **硬分列**：占用 / 召回 / 日库存 / 利率档 / 假零息 / 借券费 / 额度 / 起息 / 闸门 / 强平序 / 折算 / 提取 / 追保禁开 / 开仓比例 / 融券名单 / 空头价限 ≠ 调出了结时限；并**带过 CB≠B/C/CA/BF/BZ…、CA≠A/C/BZ/BY…、BZ≠Z/BY/BX…、BY≠Y/BX…、BQ≠BA/K/BF/BC…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K、BH≠H**。与假设 AN–CB **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-C（股票池当时名单）**。**严禁改写/续写假设-CA / 假设-CB / 假设-BQ / 假设-BY / 假设-BZ / 假设-BF**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CC** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **双字母实验 CB**（融资展期审批；**严禁改写假设-CB**）≠ **单字母实验 A** ≠ **单字母实验 B** ≠ **单字母实验 Z** ≠ **单字母实验 K** ≠ **单字母实验 Y**。全文凡写「实验 CC / 假设-CC / hypothesis_id=CC / 组 CC0·CC1·CC2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CC 混读或互改；**尤其 params.Y ≠ 实验字母 CC ≠ 单字母假设-C ≠ 双字母假设-CA ≠ 双字母假设-CB**。亦**禁止**把实验字母 CC 与单字母 **A/B/C/Z/K/Y/T/S/U/V/W/X**、双字母 **BA–CB**、双字母 **CA/CB/BQ/BY/BZ/BF/BC/BT/BD/BL/BW/BV/BU/BS/BO/BR/BH**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `cc0_*` 以外的实验页混读。**双字母 CC ≠ 单字母 C ≠ 单字母 A ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 Y ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BQ ≠ 双字母 BY ≠ 双字母 BF ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 CC**；**params.G ≠ 实验字母 CC**；**params.N ≠ 实验字母 CC**。**带过：双字母 CB ≠ B/C/CA/BF/BZ/BY…；双字母 CA ≠ A/C/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/Z…；双字母 BZ ≠ Z/BY/BX…；双字母 BY ≠ Y/BX/BW…；双字母 BQ ≠ BA/K/BF/BC…；双字母 BX ≠ X/BW…；双字母 BW ≠ W/BV…；双字母 BV ≠ V/BU/BT…；双字母 BU ≠ U/BB/BT/K…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BP ≠ P/BO/W；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CC ≠ 单字母假设-C；且 ≠ 假设-CA / 假设-CB / 假设-BQ / 假设-BY / 假设-BZ / 假设-BF；带过 CB≠B/C/CA…、CA≠A/C/BZ…、BQ≠BA/K/BF…、params.Y≠CC（硬）

| 维度 | 对照页 | 本页假设-CC（双字母） |
|------|--------|----------------------|
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | **两融标的调出后强制了结时点/了结时限**误开：假无限拖或随意续作时限 vs 按生效日调出了结时限 PIT；**严禁复用 C 题面**；**绝不可做成 C 续篇**；**CC≠C** |
| 题面 CA | **维持担保比例分子分母口径**（A/D–CA已纸面齐；`invent_wrong_maint_guarantee_ratio_num_den`） | **调出后何时必须强制了结**；公式 ≠ 了结时限；**CC≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批**（A/D–CB纸面齐；`invent_always_allow_financing_rollover`） | 展期审批 ≠ 调出了结时限；**CC≠CB**；**不改 CB** |
| 题面 BQ | **标的调出后存量假续持**（`invent_keep_open_after_list_removal`） | **能否**假续持 ≠ **何时**必须了结；**CC≠BQ**；**不改 BQ** |
| 题面 BY | **追保宽限期/强平通知时限**（`invent_ignore_margin_call_grace_or_force_deadline`） | 追保宽限 ≠ 调出了结时限；**禁复用 BY 主报**；**CC≠BY**；**不改 BY** |
| 题面 BZ | **融资提前了结手续费/违约金**（`invent_ignore_early_repay_fee_or_penalty`） | 提前了结费 ≠ 调出了结时限；**CC≠BZ**；**不改 BZ** |
| 题面 BF | **合约期限到期强制了结**（到期日闸门） | 名单**调出**了结时限 ≠ 合约**到期**了结；**CC≠BF**；**不改 BF** |
| 题面 BA | **融资买入新开名单** | 新开 ≠ 调出了结时限；**CC≠BA**；**不改 BA** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ignore_margin_universe_delist_force_deadline` |
| 文档 | 清单实验 C / `假设-CA-…` / `假设-CB-…` / `假设-BQ-…` / `假设-BY-…` / `假设-BZ-…` / `假设-BF-…`（**只读；禁止改写**） | `假设-CC-两融标的调出强制了结时点误开.md`（新建） |
| 预检键 | 实验字母 C / CA / CB / BQ / BY / BZ / BF | 实验字母 **CC** / `cc0_primary_demo`；**不得**占用或改写预检 C/CA/CB/BQ/BY/BZ/BF |

**禁止**：把 CC 写成「C/CA/CB/BQ/BY/BZ/BF 的续篇」；把「股票池已诚实（C）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 存量处理已诚实（BQ）/ 追保宽限已诚实（BY）/ 提前了结费已诚实（BZ）/ 到期了结已诚实（BF）」静默写成「调出强制了结时限已诚实」；覆盖或补丁改写假设-C / 假设-CA / 假设-CB / 假设-BQ / 假设-BY / 假设-BZ / 假设-BF 正文；把 `params.Y/G/N` 与实验字母 CC 混读；**禁** `cc0_primary_demo` 与 `invent_asof_leak_margin_universe_delist_force_deadline` **双挂主报**；**禁** CC1 半泄露升格并列主报；**禁**复用假设-C 题面或口径键；**禁**复用 CA/CB/BQ/BY/BZ/BF 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有信用账户两融路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/调出后存量处理/追保宽限/合约期限到期闸门/展期审批/维持比公式/提前了结费等输入（Z/BA/BQ/BY/BF/CB/CA/BZ 层诚实或显式旁路声明「本页不重开开仓比例/融资新开名单/调出后能否续持/追保宽限/到期强制了结/展期审批/维持比分子分母/提前了结费」）下，把「标的从两融标的池调出后的强制了结时限可无限拖、或当日即可随意续作/无限顺延」或「全样本用核对日当天更宽无限拖/随意续作时限规则回放历史」当成默认，相对「每个交易日按当时有效两融标的调出后强制了结时点/了结时限规则 PIT（调出生效日起按当时有效时限日历强制了结或记失败；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假无限拖调出了结时限路径并高估可续持两融名义、低估因调出强制了结时限导致的被迫平仓冲击与成本**；差异应**集中在两融标的调出强制了结时点误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假无限拖调出了结时限贡献差、可续持名义差、被迫平仓冲击差在标定噪声带内可忽略，且「假无限拖调出了结时限 / 核对日泄露 / 正常时限窗 / 时限切日窗 / 通道前 / vs A·B·C·CA·CB·Z·BA–CB·BQ·BY·BZ·BF·K·AB·Y·H·W·V·T·S·U·X」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑）

```
# params.fill_time                        写死 next_open
# params.asof_check_date                 写死 2026-10-16
# params.px_basis                        写死 unadj
# params.margin_channel_start            写死 2010-03-31
# params.delist_force_deadline_honest    写死 pit_by_effective_date
# params.delist_force_deadline_scope     写死 post_delist_forced_unwind_deadline
# params.delist_force_deadline_over_policy 写死 unwind_by_deadline_or_fail_missing_deadline_rule
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page
# params.haircut_handoff                 写死 bd_page
# params.balance_pause_handoff           写死 be_page
# params.contract_term_handoff           写死 bf_page    # 合约期限到期交 BF；CC≠BF；不改 BF
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
# params.list_removal_stock_handoff      写死 bq_page    # 调出后能否续持交 BQ；CC≠BQ；假续持≠了结时限；不改 BQ
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page
# params.force_close_order_handoff       写死 bt_page
# params.daily_short_inventory_handoff   写死 bu_page
# params.short_recall_handoff            写死 bv_page
# params.credit_usage_handoff            写死 bw_page
# params.interest_start_daycount_handoff 写死 bx_page
# params.margin_call_grace_handoff       写死 by_page    # 追保宽限交 BY；CC≠BY；追保宽限≠调出了结时限；不改 BY
# params.early_repay_fee_handoff         写死 bz_page    # 提前了结费交 BZ；CC≠BZ；不改 BZ
# params.maint_ratio_formula_handoff     写死 ca_page    # 维持比分子分母交 CA；CC≠CA；不改 CA
# params.financing_rollover_handoff      写死 cb_page    # 展期审批交 CB；CC≠CB；不改 CB（A/D–CB纸面齐）
# params.delist_force_deadline_handoff   写死 self      # 本页主病：两融标的调出强制了结时点/了结时限
# params.universe_pool_handoff           写死 c_page    # 股票池当时名单交 C；CC≠C；严禁复用假设-C
# params.auction_vol_handoff             写死 y_page
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.st_limit_handoff                写死 x_page
# params.stamp_tax_handoff               写死 v_page
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.cc0_primary_demo                建议 invent_ignore_margin_universe_delist_force_deadline  # 主报建议：假无限拖调出了结时限；禁与 invent_asof_leak_margin_universe_delist_force_deadline 双挂争主表；CC1半泄露不得升格并列主报
# params.cc0_invent_ignore_margin_universe_delist_force_deadline  建议 True
# params.cc1_asof_leak_margin_universe_delist_force_deadline_only 建议 True
# params.cc2_pit_delist_force_deadline   建议 True
# params.merge_with_A_fill               写死 False
# params.merge_with_B_legacy             写死 False  # CC≠B
# params.merge_with_C_universe_pool      写死 False  # CC≠C；严禁复用假设-C
# params.merge_with_CA_maint_ratio_formula 写死 False  # CC≠CA；不改 CA
# params.merge_with_CB_financing_rollover 写死 False  # CC≠CB；不改 CB
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_BF_contract_term     写死 False  # CC≠BF；不改 BF
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
# params.merge_with_BQ_list_removal_stock 写死 False  # CC≠BQ；不改 BQ
# params.merge_with_BR_short_borrow_fee  写死 False
# params.merge_with_BS_financing_rate_tier 写死 False
# params.merge_with_BT_force_close_order 写死 False
# params.merge_with_BU_daily_short_inventory 写死 False
# params.merge_with_BV_short_recall      写死 False
# params.merge_with_BW_credit_usage      写死 False
# params.merge_with_BX_interest_start_daycount 写死 False
# params.merge_with_BY_margin_call_grace 写死 False  # CC≠BY；不改 BY
# params.merge_with_BZ_early_repay_fee   写死 False  # CC≠BZ；不改 BZ
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_Y_auction_vol        写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.missing_delist_force_deadline_policy 写死 skip
# params.day_freq_proxy                  写死 delist_force_deadline_sensitivity
# params.universe_rule                   写死 sse_szse_margin_universe_delist_force_deadline_check
# params.fail_policy                     写死 skip
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母CC；params.G≠实验字母CC；params.N≠实验字母CC；亦≠单字母实验C/A/B/Z；占位·待冻结；禁 null/holdout/跑后改口
# params.date_start / date_end           写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改调出了结时限口径、Y/G/N/Y2、主窗/oos、cc0_primary_demo
```

可编码摘要（伪代码，不开跑）：

```
asof = params.asof_check_date  # 2026-10-16
# CC0：假无限拖调出了结时限——调出后永不检查强制了结时限、永远可拖/随意续作
# CC1：仅 asof 日更宽无限拖/随意续作时限规则泄露铺满
# CC2：每个交易日 d 按当日已生效两融标的调出后强制了结时点/了结时限规则 PIT
# 消费 BQ 诚实存量处理（或旁路声明本页不重开能否续持）；消费 BY 追保宽限 / BF 到期闸门 / CB 展期审批 / CA 维持比公式 / BZ 提前了结费为旁路输入
# 缺了结时限字段 → skip（params.missing_delist_force_deadline_policy）
```

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
margin_channel_start = "2010-03-31"
delist_force_deadline_honest = "pit_by_effective_date"
delist_force_deadline_scope = "post_delist_forced_unwind_deadline"
delist_force_deadline_over_policy = "unwind_by_deadline_or_fail_missing_deadline_rule"
cc0_primary_demo = "invent_ignore_margin_universe_delist_force_deadline"  # 单一主报建议；禁与 invent_asof_leak_margin_universe_delist_force_deadline 双挂
cc0_invent_ignore_margin_universe_delist_force_deadline = True
cc1_asof_leak_margin_universe_delist_force_deadline_only = True
cc2_pit_delist_force_deadline = True
merge_with_C_universe_pool = False
merge_with_CA_maint_ratio_formula = False
merge_with_CB_financing_rollover = False
merge_with_BQ_list_removal_stock = False
merge_with_BY_margin_call_grace = False
merge_with_BZ_early_repay_fee = False
merge_with_BF_contract_term = False
merge_with_Z_margin_ratio = False
fail_policy = "skip"
```

### 2.2 三组对照（CC0 / CC1 / CC2）

| 组 | 口径 | 说明 |
|----|------|------|
| CC0 天真 | `invent_ignore_margin_universe_delist_force_deadline`（单一主报建议） | 发明假无限拖调出了结时限路径；禁与 invent_asof_leak_margin_universe_delist_force_deadline 双挂 |
| CC1 半泄露·混口径 | 全样本用 `asof_check_date` 当天更宽无限拖/随意续作时限规则铺满历史 | 仅调出了结时限 asof 泄露；不升格并列主报 |
| CC2 PIT | `delist_force_deadline_honest=pit_by_effective_date` | 每个交易日按当时已生效两融标的调出后强制了结时点/了结时限规则 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：两融标的调出事件/生效日代理 + 调出后强制了结时限日历代理 + 当日生效了结时限规则 → 当日是否须强制了结；缺时限字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有两融标的调出生效日代理 + 调出后强制了结时限规则生效日表 + 存量处理（消费 BQ，旁路）+ 追保宽限（消费 BY，旁路声明「本页假定宽限层诚实」）即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。  
- **通道前**：`margin_channel_start=2010-03-31` 前无本页调出了结时限通道。

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

天真组 / 半泄露组相对诚实组的假无限拖调出了结时限贡献差、可续持名义差、被迫平仓冲击差超出标定噪声带，且差异集中在「两融标的调出强制了结时点误开」桶，不被 C 股票池、CA 维持比公式、CB 展期审批、BQ 假续持、BY 追保宽限、BZ 提前了结费、BF 到期了结等他页桶吞并。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 C/CA/CB/BQ/BY/BZ/BF/A/Z/T 等他页桶吞并；或 holdout 反调 `cc0_primary_demo` / Y·G·N·Y2；或 CC0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CC0 / CC1 / CC2。报告可续持名义差、假无限拖调出了结时限贡献差、被迫平仓冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_ignore_margin_universe_delist_force_deadline",
  "invent_asof_leak_margin_universe_delist_force_deadline",
  "delist_force_deadline_window",
  "delist_force_deadline_cut_window",
  "pre_margin_channel_20100331",
  "vs_A_limit_up_fill",
  "vs_B_legacy",
  "vs_C_universe_pool",
  "vs_CA_maint_ratio_formula",
  "vs_CB_financing_rollover",
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
  "vs_BX_interest_start_daycount",
  "vs_BY_margin_call_grace",
  "vs_BZ_early_repay_fee",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_Y_auction_vol",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_X_st_limit_avoid",
  "vs_V_stamp_tax_avoid",
  "vs_U_transfer_fee_avoid",
  "vs_T_csrc_fee_avoid",
  "vs_S_handling_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够两融标的调出/强制了结时限字段；缺字段却静默当假无限拖 → 设计失效。  
2. 把「调出后存量假续持已诚实（BQ）」静默写成「调出了结时限已诚实」且不声明另页 BQ → **与 BQ 撞题**（假续持 ≠ 了结时限；**尤其 CC≠BQ**；**不改 BQ**）。  
3. 把「追保宽限期已诚实（BY）」静默写成「调出了结时限已诚实」 → **与 BY 撞题**（**尤其 CC≠BY**；**不改 BY**）。  
4. 把「合约期限到期了结已诚实（BF）」静默写成「调出了结时限已诚实」 → **与 BF 撞题**（到期了结 ≠ 调出了结时限；**尤其 CC≠BF**；**不改 BF**）。  
5. 把「展期审批已诚实（CB）」静默写成「调出了结时限已诚实」 → **与 CB 撞题**（**尤其 CC≠CB**；**不改 CB**）。  
6. 把「维持比分子分母已诚实（CA）」静默写成「调出了结时限已诚实」 → **与 CA 撞题**（公式 ≠ 了结时限；**尤其 CC≠CA**；**不改 CA**）。  
7. 把「股票池已诚实（C）」或「提前了结费已诚实（BZ）」静默写成「调出了结时限已诚实」→ **撞假设-C / 假设-BZ**（**严禁复用假设-C**；**尤其 CC≠C / CC≠BZ**；**绝不可做成 C 续篇**）。  
8. 把「开仓比例/名单/占用/闸门/强平序已诚实」写成主病或不声明另页 → 与 Z/BA/BW/BC/BT 等撞题。  
9. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「调出了结时限已诚实」→ 与交易所费用族撞题（**明确避开预检T**）。  
10. 把实验字母 CC 与单字母 A/B/C/Z/K/Y/T/S/U/V/W/X 或双字母 BA–CB/BQ/BY/BZ/BF/BC/BT/BD/BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `cc0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价代理调出了结时限路径 → 标签与执行双错，结论无效。  
13. 用核对日更宽「假无限拖调出了结时限」当诚实 PIT、或把券商临时宽口径铺满历史 → 设计失效。  
14. **`cc0_primary_demo` 与 `invent_asof_leak_margin_universe_delist_force_deadline` 双挂主报**；或 CC1 升格并列主报 → 设计失效。  
15. **改写或覆盖 `假设-C` / `假设-CA` / `假设-CB` / `假设-BQ` / `假设-BY` / `假设-BZ` / `假设-BF` / 已冻 AA–CB** → 硬边界违约，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 两融标的调出事件/生效日代理、调出后强制了结时限日历代理、了结时限规则及生效日；  
- 开仓保证金比例 / 融资名单 / 调出后存量处理 / 追保宽限 / 合约期限到期闸门 / 展期审批 / 维持比公式 / 提前了结费输入（消费 Z/BA/BQ/BY/BF/CB/CA/BZ 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：会员加严调出了结时限子集；与 BQ 假续持窗、BY 追保宽限窗、BF 到期窗、CB 展期窗对照但不混主结论；缺时限原因码敏感性（主报仍在调出强制了结时点）。

**禁止**：用核对日「今天无限拖调出了结时限」铺满当唯一诚实组；用复权价；把存量假续持已诚实/追保宽限已诚实/到期了结已诚实/展期审批已诚实/分子分母已诚实/股票池已诚实/提前了结费已诚实/开仓比例已诚实/占用已诚实当成「调出了结时限正确」依据；把 Z/BA–CB/BQ/BY/BZ/BF/K/AB/A/B/C/H/W/Y/X/V/U/T/S/AN–CB 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`CC`  
- **组**：CC0 / CC1 / CC2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`delist_force_deadline_honest=pit_by_effective_date`；`delist_force_deadline_scope=post_delist_forced_unwind_deadline`；`delist_force_deadline_over_policy=unwind_by_deadline_or_fail_missing_deadline_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`list_removal_stock_handoff=bq_page`；`margin_call_grace_handoff=by_page`；`contract_term_handoff=bf_page`；`financing_rollover_handoff=cb_page`；`maint_ratio_formula_handoff=ca_page`；`early_repay_fee_handoff=bz_page`；`universe_pool_handoff=c_page`；其余 handoff 见 §2.1；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_margin_universe_delist_force_deadline_check`；`missing_delist_force_deadline_policy=skip`；`day_freq_proxy=delist_force_deadline_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 CC**；**params.G≠实验字母 CC**；**params.N≠实验字母 CC**；亦≠单字母实验 C/A/B/Z；占位·待冻结；禁 null/holdout/跑后改口）；**`params.cc0_primary_demo` 建议 `invent_ignore_margin_universe_delist_force_deadline`**（禁与 invent_asof_leak_margin_universe_delist_force_deadline 双挂；CC1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- CC0/CC1/CC2 净收益/成本质量、ΔFakeInfiniteDelistDeadline、ΔSustainableNotional、ΔForcedUnwindImpact；分桶（两融标的调出强制了结时点误开 / 核对日泄露 / 正常时限窗 / 时限切日窗 / 通道前 / vs A·B·C·CA·CB·Z·BA–CB·BQ·BY·BZ·BF·K·AB·Y·H·W·X·V·U·T·S）。  
- 自检气泡：CC2 是否 pit_by_effective_date；CC0 是否单一主报；CC1 是否仅核对日泄露；是否未与 A/B/C/CA/CB/Z/BA–CB/BQ/BY/BZ/BF/K/AB/Y/H/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 CC 与 C 或 CA 或 CB 或 A 或 B 或 Z 或 K 或 Y 或 BA–CB 或 BQ 或 BY 或 BZ 或 BF 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 CC≠单字母假设-C；CC≠双字母假设-CA；CC≠双字母假设-CB；params.Y≠实验字母 CC；CC≠BQ；CC≠BY；CC≠BZ；CC≠BF；带过 CB≠B/C/CA/BF/BZ…、CA≠A/C/BZ…、BZ≠Z/BY…、BY≠Y/BX…、BQ≠BA/K/BF/BC…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–CB 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-C / 假设-CA / 假设-CB / 假设-BQ / 假设-BY / 假设-BZ / 假设-BF / 假设-Z / 假设-K / 假设-BA–CB / 假设-AB**；**是否未再改 CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-C**；**是否未与 invent_asof_leak_margin_universe_delist_force_deadline 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假无限拖调出了结时限或核对日泄露吹成诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不占本机 8765 席位；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–CB 及其他 A/D–CB 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-C**；**不改假设-CA**；**不改假设-CB**；**不改假设-BQ**；**不改假设-BY**；**不改假设-BZ**；**不改假设-BF**；**不改假设-Z**；**不改假设-K**；**不改假设-BA–CB**；**尤其不改假设-C；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-BQ；尤其不改假设-BY；尤其不改假设-BZ；尤其不改假设-BF**；**不改假设-AB**；**勿再改 CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限到期强制了结（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量假续持（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券券池日可借量（BU）、融券提前召回（BV）、授信占用口径（BW）、融资利息起息日/计息天数（BX）、追保宽限期/强平通知时限（BY）、融资提前了结手续费/违约金（BZ）、维持担保比例分子分母口径（CA）、融资合约展期/续作审批（CB）、融券空头名单（K）、股票池当时名单（C）、历史实验 B 旧位之外，**两融标的调出后强制了结时点/了结时限**须按当时有效规则 PIT；不得默认调出后强制了结时限可无限拖或当日随意续作，或用核对日更宽规则铺满。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 CC** 标准件，**不改口径主线**，**不改假设 A–CB 正文**，**尤其不改假设-C / 假设-CA / 假设-CB / 假设-BQ / 假设-BY / 假设-BZ / 假设-BF**。与实验 A/B/C/CA/CB/Z/BA–CB/BQ/BY/BZ/BF/K/AB/H/W/Y/X/V/U/T/S 分工：**C=股票池当时名单（严禁复用）；CA=维持比分子分母；CB=展期审批（A/D–CB纸面齐，严禁改写）；BQ=调出后存量假续持；BY=追保宽限；BZ=提前了结费；BF=到期强制了结；CC=两融标的调出强制了结时点误开（CC≠C≠CA≠CB≠A≠B≠Z≠K≠Y≠BA≠…≠BZ≠BQ≠BY≠BF≠BC≠BT≠BD≠BL≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AB≠W≠H≠T≠S≠U≠V≠X；带过 CB≠B/C/CA/BF/BZ…、CA≠A/C/BZ…、BZ≠Z/BY…、BY≠Y/BX…、BQ≠BA/K/BF/BC…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 待入库预检**（结论栏空；**禁止标任何纸面齐**） |
| 标准件路径 | `假设-CC-两融标的调出强制了结时点误开.md` |
| 清单序号 | 约 #86 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**delist_force_deadline_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 CC；params.G≠实验字母 CC；params.N≠实验字母 CC；亦≠单字母实验 C/A/B/Z；占位·待冻结；禁 null/holdout/跑后改口）**；**cc0_primary_demo 建议 invent_ignore_margin_universe_delist_force_deadline（禁双挂 invent_asof_leak_margin_universe_delist_force_deadline；CC1半泄露不得升格并列主报）**；锚点建议 delist_force_deadline_honest=pit_by_effective_date / delist_force_deadline_scope=post_delist_forced_unwind_deadline / delist_force_deadline_over_policy=unwind_by_deadline_or_fail_missing_deadline_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **CC≠C/CA/CB/BQ/BY/BZ/BF/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/Z/A/B**（及 ≠Y/BA–CB/K/AB/H/W/T/S/U/V/X），**严禁复用假设-C**；**尤其不改假设-C/CA/CB/BQ/BY/BZ/BF**；**params.Y≠实验字母 CC** |
| 结论栏 | 空 |

---

## 待预检键清单（草稿 · 待入库预检；未冻结）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**建议·待冻结**；**params.Y≠实验字母 CC**；**params.G≠实验字母 CC**；**params.N≠实验字母 CC**；禁 null/holdout）  
2. `params.cc0_primary_demo` = `invent_ignore_margin_universe_delist_force_deadline`（**建议·待冻结**；禁与 `invent_asof_leak_margin_universe_delist_force_deadline` 双挂；CC1不升格主报）  
