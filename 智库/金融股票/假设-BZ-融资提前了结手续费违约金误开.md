# 假设 BZ · 融资提前了结手续费/违约金误开 / 用核对日减免或零费规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BY 补丁已交（复检在途）、写下一纸面 BZ；清单撞题规则另选正交执行缺口（**融资负债提前了结时手续费/违约金/提前还款费怎么计** ≠ 开仓融资/融券保证金比例 ≠ 融资假零息 ≠ 融资利率档 ≠ 起息日/计息天数 ≠ 追保宽限期/强平通知时限 ≠ 授信占用 ≠ 融券借券费 ≠ 交易所经手/证管/过户/印花税）；选题自两融合同与会员公开口径：融资合约在到期前主动提前了结（或协议提前还款）时，除已按档计提的利息外，可能另计**提前了结手续费/违约金/提前还款费**（按剩余本金×费率、或固定档、或会员加严）；规则按**施行日/生效日** PIT；不得默认「提前了结永远零费/永不罚、或永远按核对日更宽减免规则铺满历史」；本页**假定融资利息层（BO）/利率档（BS）/起息日基数（BX）诚实或显式旁路**，主病只在**提前了结手续费/违约金是否按当时规则计收**；2010-03-31 前无此通道；**Z 正文主测「开仓保证金比例现行档误铺」**（`flat_one_times` / 开仓比例切日），**BO 正文主测「融资假零息」**，**BS 正文主测「融资利率档」**，**BX 正文主测「起息日/计息天数」**，**BY 正文主测「追保宽限期/强平通知时限」**（复检在途；**严禁改 BY**），本页主测**提前了结手续费/违约金被误开**（`invent_ignore_early_repay_fee_or_penalty`）→ 自立；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BZ ≠ 单字母 B**）/ **Z（开仓融资/融券保证金比例；双字母 BZ ≠ 单字母假设-Z；严禁复用 Z 题面或开仓比例主表；BZ≠Z）** / BA–BY（两融族已冻/在途；**BZ≠BA…BY**；**尤其不改 BY 正文**）/ **BO（融资假零息；BZ≠BO；是否计息 ≠ 提前了结手续费；尤其不改假设-BO）** / **BS（融资利率档；BZ≠BS；哪档利率 ≠ 提前了结费；尤其不改假设-BS）** / **BX（起息日/计息天数；BZ≠BX；起息 ≠ 提前了结费；尤其不改假设-BX）** / **BY（追保宽限期；BZ≠BY；时限 ≠ 提前了结费；尤其不改假设-BY）** / BW/BV/BU/BT/BR/BH 等**分列**；**新建实验 BZ**  
状态：**草稿 · 待预检**（结论栏空；禁止把「提前了结永远零费 / 用核对日更宽减免铺满」当诚实提前了结费口径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BY 及其他 A/D–BY 已交正文与冻结补丁；尤其不改假设-Z；尤其不改假设-BY；尤其不改假设-BO；尤其不改假设-BS；尤其不改假设-BX；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-BA–BY；不改假设-AB；勿再改 BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BZ（约 #83）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融资提前了结手续费/违约金**。**双字母 BZ ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BZ ≠ 单字母 B**。与假设 **Z（开仓融资/融券保证金比例）** **硬分列（专节强调）**：Z = 开仓时保证金比例现行档误铺（`flat_one_times` / 切日 80%→100% 等）；本页 = 融资负债**提前了结时**另计的手续费/违约金；开仓比例 ≠ 提前了结费。**双字母 BZ ≠ 单字母假设-Z**；**严禁复用 Z 题面或开仓比例主表/口径键**；**绝不可做成开仓保证金比例续篇**。与假设 **BO（融资假零息）** **硬分列**：BO = 利息/罚息是否按有息计；本页 = 提前了结时**另计手续费/违约金**；是否计息 ≠ 提前了结费；**禁止**把「假零息已关（BO）」静默写成「提前了结费已诚实」；**不占** BO 的 primary_demo；**尤其不改假设-BO**。**BZ≠BO**。与假设 **BS（融资利率档）** **硬分列**：BS = 哪一档年化利率；本页 = 提前了结一次性费/违约金；档位 ≠ 提前了结费；**尤其不改假设-BS**。**BZ≠BS**。与假设 **BX（融资利息起息日/计息天数）** **硬分列**：BX = 利息从哪天起算几天；本页 = 提前了结费是否计收；起息 ≠ 提前了结费；**尤其不改假设-BX**。**BZ≠BX**。与假设 **BY（追保宽限期/强平通知时限）** **硬分列**：BY = 追保通知后宽限几天（复检在途）；本页 = 主动提前了结费；时限 ≠ 提前了结费；**尤其不改假设-BY**。**BZ≠BY**。与假设 **BW / BV / BU / BT / BR / BH / BL / BF / BB / BA / BD / BG / BC / BM / K / AB** **硬分列**：占用 / 召回 / 日库存 / 强平序 / 借券费 / 额度上限 / 提取 / 合约期限 / 转融暂停 / 融资名单 / 折算率 / 可充抵 / 维持闸门 / 追保禁开 / 融券名单 / 空头价限 ≠ 提前了结手续费；并**带过 BY≠Y/BX/BW/BV/BU/BT/BS/BO/BR/BH/BM/BC…、BX≠X/BW/BV/BU/BT/BS/BO/BR/BH…、BW≠W/BV/BU/BT/BS/BO/BR/BH…、BV≠V/BU/BT/BF/BC/BB/BQ/K…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**。与假设 AN–BY **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。与假设 **T/S/U/V（交易所/结算费用族）** **硬分列**：经手/证管/过户/印花税 ≠ 两融合同层**提前了结手续费/违约金**（会员合同费，非交易所标准费）。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-Z（开仓保证金比例）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BZ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 Z**（开仓保证金比例；**严禁复用假设-Z**）≠ **单字母实验 K**（融券空头名单）≠ **单字母实验 Y**。全文凡写「实验 BZ / 假设-BZ / hypothesis_id=BZ / 组 BZ0·BZ1·BZ2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BZ 混读或互改；**尤其 params.Y ≠ 实验字母 BZ ≠ 单字母假设-Z**。亦**禁止**把实验字母 BZ 与单字母 **A**、单字母 **B**、单字母 **Z**、单字母 **K**、单字母 **Y**、单字母 **T**、单字母 **S**、单字母 **U**、单字母 **V**、单字母 **W**、单字母 **X**、双字母 **BA–BY**、双字母 **BO**、双字母 **BS**、双字母 **BX**、双字母 **BY**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bz0_*` 以外的实验页混读。**双字母 BZ ≠ 单字母 A ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 Y ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 BA ≠ … ≠ 双字母 BY ≠ 双字母 BO ≠ 双字母 BS ≠ 双字母 BX ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BT ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 BZ**；**params.G ≠ 实验字母 BZ**；**params.N ≠ 实验字母 BZ**。**带过：双字母 BY ≠ Y/BX/BW/BV/BU/BT/BS/BO/BR/BH/BM/BC…；双字母 BX ≠ X/BW/BV/BU/BT/BS/BO/BR/BH…；双字母 BW ≠ W/BV/BU/BT/BS/BO/BR/BH…；双字母 BV ≠ V/BU/BT/BF/BC/BB/BQ/K…；双字母 BU ≠ U/BB/BT/K/BS/BO/BR/BH…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 BZ ≠ 单字母假设-Z；且 ≠ 假设-BY / 假设-BO / 假设-BS / 假设-BX / 假设-BW / 假设-BV / 假设-BU / 假设-BT / 假设-BR / 假设-BH；带过 BY≠Y/BX…、BX≠X/BW…、BS≠S/BO/BR/BH、params.Y≠BZ（硬）

| 维度 | 对照页 | 本页假设-BZ（双字母） |
|------|--------|----------------------|
| 题面 Z | **开仓**融资/融券保证金比例现行档误铺（`flat_one_times` / 切日比例） | **融资提前了结手续费/违约金**误开：假零费 vs 按生效日提前了结费 PIT；**严禁复用 Z 题面**；**绝不可做成开仓保证金比例续篇** |
| 题面 BY | **追保宽限期/强平通知时限**（复检在途；`invent_ignore_margin_call_grace_or_force_deadline`） | 时限 ≠ 提前了结费；**BZ≠BY**；**不改 BY** |
| 题面 BO | **融资假零息**（`invent_zero_financing_interest` 族） | 是否计息 ≠ 提前了结一次性费；**BZ≠BO**；**不改 BO** |
| 题面 BS | **融资利率档**（`invent_wrong_financing_rate_tier` 族） | 年化档 ≠ 提前了结费；**BZ≠BS**；**不改 BS** |
| 题面 BX | **起息日/计息天数**（`invent_wrong_financing_interest_start_or_daycount`） | 起息 ≠ 提前了结费；**BZ≠BX**；**不改 BX** |
| 题面 BW/BV/BU/BT/BR/BH | 占用 / 召回 / 日库存 / 强平序 / 借券费 / 额度 | 各页主病 ≠ 提前了结费；**BZ≠…** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ignore_early_repay_fee_or_penalty` |
| 文档 | `假设-Z-…` / `假设-BY-…` / `假设-BO-…` / `假设-BS-…` / `假设-BX-…`（**只读；禁止改写**） | `假设-BZ-融资提前了结手续费违约金误开.md`（新建） |
| 预检键 | 实验字母 Z / BY / BO / BS / BX | 实验字母 **BZ** / `bz0_primary_demo`；**不得**占用或改写预检 Z/BY/BO/BS/BX |

**禁止**：把 BZ 写成「Z/BY/BO/BS/BX 的续篇」；把「开仓比例已诚实（Z）/ 宽限期已诚实（BY）/ 假零息已关（BO）/ 利率档已诚实（BS）/ 起息已诚实（BX）/ 占用已诚实 / 召回已诚实」静默写成「提前了结费已诚实」；覆盖或补丁改写假设-Z / 假设-BY / 假设-BO / 假设-BS / 假设-BX 正文；把 `params.Y/G/N` 与实验字母 BZ 混读；**禁** `bz0_primary_demo` 与 `invent_asof_leak_early_repay_fee` **双挂主报**；**禁** BZ1 半泄露升格并列主报；**禁**复用假设-Z（开仓保证金比例）题面或口径键；**禁**复用 BY 的 `invent_ignore_margin_call_grace_or_force_deadline` 或 BO/BS/BX 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有融资负债路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/利率档/假零息层/起息日基数/授信占用等输入（Z/BA/BS/BO/BX/BW 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/利率档/假零息主病/起息日基数/授信占用」）下，把「融资提前了结永远零手续费、永不计违约金」或「全样本用核对日当天更宽减免/零费提前了结规则回放历史」当成默认，相对「每个交易日按当时有效融资提前了结手续费/违约金规则 PIT（主动提前还款/提前了结按当时费率或违约金公式计收；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假零提前了结费路径并高估提前了结净收益、低估因提前了结费导致的真实融资成本**；差异应**集中在融资提前了结手续费/违约金误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假零提前了结费贡献差、提前了结净收益差、融资真实成本差在标定噪声带内可忽略，且「假零提前了结费 / 核对日泄露 / 正常费窗 / 费率切日窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·BS·BT·BU·BV·BW·BX·BY·K·AB·Y·B·H·W·V·T·S·U·X」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融资提前了结手续费/违约金 ≠ 开仓保证金比例（Z）；≠ 假零息（BO）；≠ 利率档（BS）；≠ 起息日基数（BX）；≠ 追保宽限期（BY）；≠ 交易所费用族（T/S/U/V）；≠ 板上枯竭（A）

```
# 配置写死键（见 §7；草稿·待预检；建议值如下，终值待预检冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BZ；≠ 单字母假设-Z；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 BY；≠ 实验字母 BO；≠ 实验字母 BS；≠ 实验字母 BX
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BZ
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BZ；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.early_repay_fee_honest          写死 pit_by_effective_date
# params.early_repay_fee_scope           写死 financing_early_close_fee_or_penalty
# params.early_repay_fee_over_policy     写死 charge_or_fail_missing_fee_rule
# params.early_repay_fee_naive           写死 invent_ignore_early_repay_fee_or_penalty
# params.margin_ratio_handoff            写死 z_page   # 开仓比例交 Z；BZ≠Z；严禁复用假设-Z；不改 Z
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
# params.financing_interest_handoff      写死 bo_page   # 假零息交 BO；BZ≠BO；不改 BO
# params.corp_action_comp_handoff        写死 bp_page
# params.list_removal_stock_handoff      写死 bq_page
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page   # 利率档交 BS；BZ≠BS；不改 BS
# params.force_close_order_handoff       写死 bt_page
# params.daily_short_inventory_handoff   写死 bu_page
# params.short_recall_handoff            写死 bv_page
# params.credit_usage_handoff            写死 bw_page
# params.interest_start_daycount_handoff 写死 bx_page   # 起息/日基数交 BX；BZ≠BX；不改 BX
# params.margin_call_grace_handoff       写死 by_page   # 追保宽限交 BY；BZ≠BY；复检在途亦勿改 BY
# params.early_repay_fee_handoff         写死 self      # 本页主病：融资提前了结手续费/违约金
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
# params.bz0_primary_demo                建议 invent_ignore_early_repay_fee_or_penalty  # 主报建议：假零提前了结费/假忽略违约金；禁与 invent_asof_leak_early_repay_fee 双挂争主表；BZ1半泄露不得升格并列主报；终值待预检冻结
# params.bz0_invent_ignore_early_repay_fee_or_penalty  建议 True
# params.bz1_asof_leak_early_repay_fee_only 建议 True
# params.bz2_pit_early_repay_fee         建议 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False  # BZ≠Z；严禁复用假设-Z；不改 Z
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
# params.merge_with_BO_financing_interest 写死 False  # BZ≠BO；不改 BO
# params.merge_with_BP_corp_action_comp  写死 False
# params.merge_with_BQ_list_removal_stock 写死 False
# params.merge_with_BR_short_borrow_fee  写死 False
# params.merge_with_BS_financing_rate_tier 写死 False  # BZ≠BS；不改 BS
# params.merge_with_BT_force_close_order 写死 False
# params.merge_with_BU_daily_short_inventory 写死 False
# params.merge_with_BV_short_recall      写死 False
# params.merge_with_BW_credit_usage      写死 False
# params.merge_with_BX_interest_start_daycount 写死 False  # BZ≠BX；不改 BX
# params.merge_with_BY_margin_call_grace 写死 False  # BZ≠BY；不改 BY（复检在途）
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_Y_auction_vol        写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.missing_early_repay_fee_rule_policy 写死 skip
# params.day_freq_proxy                  写死 early_repay_fee_penalty_sensitivity
# params.universe_rule                   写死 sse_szse_financing_early_repay_fee_check
# params.fail_policy                     写死 skip
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BZ；params.G≠实验字母BZ；params.N≠实验字母BZ；亦≠单字母实验A/B/Z；禁 null/holdout/跑后改口；终值待预检冻结
# params.date_start / date_end           写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改提前了结费规则、Y/G/N/Y2、主窗/oos、bz0_primary_demo

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
margin_channel_start = "2010-03-31"
early_repay_fee_honest = "pit_by_effective_date"
early_repay_fee_scope = "financing_early_close_fee_or_penalty"
early_repay_fee_over_policy = "charge_or_fail_missing_fee_rule"
early_repay_fee_naive = "invent_ignore_early_repay_fee_or_penalty"
bz0_primary_demo = "invent_ignore_early_repay_fee_or_penalty"  # 单一主报建议；禁与 invent_asof_leak_early_repay_fee 双挂；终值待预检冻结
bz1_asof_leak_early_repay_fee_only = True
bz2_pit_early_repay_fee = True
merge_with_Z_margin_ratio = False
merge_with_BO_financing_interest = False
merge_with_BS_financing_rate_tier = False
merge_with_BX_interest_start_daycount = False
merge_with_BY_margin_call_grace = False
fail_policy = "skip"
```

### 2.2 三组对照（BZ0 / BZ1 / BZ2）

| 组 | 口径 | 说明 |
|----|------|------|
| BZ0 天真 | `invent_ignore_early_repay_fee_or_penalty`（单一主报建议） | 发明假零提前了结费/假忽略违约金路径；禁与 invent_asof_leak_early_repay_fee 双挂 |
| BZ1 半泄露/混口径 | 全样本用 `asof_check_date` 当天更宽减免或零费提前了结规则铺满历史 | 仅提前了结费规则 asof 泄露；不升格并列主报 |
| BZ2 PIT | `early_repay_fee_honest=pit_by_effective_date` | 每个交易日按当时已生效融资提前了结手续费/违约金规则 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：融资负债日终余额 + 主动提前了结/提前还款标记 + 当日生效提前了结手续费/违约金规则 → 应计提前了结费；缺费规则字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有融资负债余额代理 + 提前了结/提前还款事件标记 + 提前了结费/违约金规则生效日表 + 假零息层（消费 BO，旁路）+ 利率档层（消费 BS，旁路）+ 起息层（消费 BX，旁路）即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。  
- **通道前**：`margin_channel_start=2010-03-31` 前无本页提前了结费通道。

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

天真组 / 半泄露组相对诚实组的假零提前了结费贡献差、提前了结净收益差、融资真实成本差超出标定噪声带，且差异集中在「融资提前了结手续费/违约金误开」桶，不被 Z 开仓比例、BO 假零息、BS 利率档、BX 起息、BY 宽限、T/S/U/V 交易所费等他页桶吸走。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 Z 开仓比例、BO 假零息、BS 利率档、BX 起息、BY 宽限、BF 期限、T 证管费等他页桶吸走；或 holdout 反调 `bz0_primary_demo` / Y·G·N·Y2；或 BZ0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BZ0 / BZ1 / BZ2。报告提前了结净收益差、假零提前了结费贡献差、融资真实成本差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_ignore_early_repay_fee_or_penalty",
  "invent_asof_leak_early_repay_fee",
  "early_repay_fee_window",
  "early_repay_fee_cut_window",
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
  "vs_BV_short_recall",
  "vs_BW_credit_usage",
  "vs_BX_interest_start_daycount",
  "vs_BY_margin_call_grace",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_Y_auction_vol",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_X_st_limit_avoid",
  "vs_V_stamp_tax_avoid",
  "vs_U_transfer_fee_avoid",
  "vs_T_csrc_fee_avoid",
  "vs_S_handling_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够融资提前了结腿或费规则字段；缺字段却静默当零费 → 设计失效。  
2. 把「开仓保证金比例已诚实（Z）」静默写成「提前了结费已诚实」且不声明另页 Z → **与 Z 撞题**（开仓比例 ≠ 提前了结费；**尤其 BZ≠Z**；**严禁复用假设-Z**；**不改 Z**）。  
3. 把「假零息已关（BO）」静默写成「提前了结费已诚实」且不声明另页 BO → **与 BO 撞题**（是否计息 ≠ 提前了结费；**尤其 BZ≠BO**；**不改 BO**）。  
4. 把「利率档已诚实（BS）」静默写成「提前了结费已诚实」→ **与 BS 撞题**（档位 ≠ 提前了结费；**尤其 BZ≠BS**；**不改 BS**）。  
5. 把「起息/日基数已诚实（BX）」写成主病或不声明另页 BX → **撞假设-BX**，设计失效（**尤其 BZ≠BX**；**不改 BX**）。  
6. 把「追保宽限期已诚实（BY）」写成主病或不声明另页 BY → **撞假设-BY**，设计失效（**尤其 BZ≠BY**；**不改 BY**）。  
7. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「提前了结费已诚实」→ 与交易所费用族撞题（合同层提前了结费 ≠ 交易所标准费；**明确避开预检T**）。  
8. 把「期限未到（BF）/ 授信够（BH）/ 占用已诚实（BW）/ 账户未串用（BN）」静默写成「提前了结费正确」→ 与对应页撞题（**尤其 BZ≠BF≠BH≠BW≠BN**）。  
9. 把「空头价限 / 除权板价 / 板上能否按板上价成交 / 退市整理期当普通可交易」写成主病而不声明另页 AB/W/A/H → 与对应页撞题。  
10. 把实验字母 BZ 与单字母 A/B/Z/K/Y/T/S/U/V/W/X 或双字母 BA–BY/BO/BS/BX/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `bz0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价算融资负债/提前了结费代理 → 标签与执行双错，结论无效。  
13. 用核对日更宽「减免/零费」当诚实 PIT、或把券商临时减免提前铺满历史 → 设计失效。  
14. **`bz0_primary_demo` 与 `invent_asof_leak_early_repay_fee` 双挂主报**；或 BZ1 升格并列主报 → 设计失效。  
15. **改写或覆盖 `假设-Z` / `假设-BY` / `假设-BO` / `假设-BS` / `假设-BX` / 已冻 AA–BY** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资负债日终余额、主动提前了结/提前还款事件标记、提前了结手续费/违约金规则及生效日；  
- 开仓保证金比例 / 融资名单 / 假零息层 / 利率档 / 起息日基数 / 授信占用输入（消费 Z/BA/BO/BS/BX/BW 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：券商更严提前了结费子集；与 BO 利息窗、BS 档位窗、BX 起息窗、BF 到期强制了结对照但不混主结论；被动强平了结另桶敏感性（主报仍在主动提前了结费）。

**禁止**：用核对日「今天减免/零费」铺满当唯一诚实组；用复权价；把开仓保证金比例已诚实/假零息已关/利率档诚实/起息已诚实/宽限期已诚实/占用已诚实/日库存够/期限未到/名单仍在池/转融未暂停/借券费已计/授信够/新开名单窗/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/提取线未触/账户未串用/权益已补偿/调出后存量已处理/市场25pct未暂停/交易所费已诚实当成「提前了结费正确」依据；把 Z/BA–BY/K/AB/A/B/H/W/Y/X/V/U/T/S/AN–BY 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BZ`  
- **组**：BZ0 / BZ1 / BZ2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`early_repay_fee_honest=pit_by_effective_date`；`early_repay_fee_scope=financing_early_close_fee_or_penalty`；`early_repay_fee_over_policy=charge_or_fail_missing_fee_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`force_close_order_handoff=bt_page`；`daily_short_inventory_handoff=bu_page`；`short_recall_handoff=bv_page`；`credit_usage_handoff=bw_page`；`interest_start_daycount_handoff=bx_page`；`margin_call_grace_handoff=by_page`；`auction_vol_handoff=y_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`st_limit_handoff=x_page`；`stamp_tax_handoff=v_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_financing_early_repay_fee_check`；`missing_early_repay_fee_rule_policy=skip`；`day_freq_proxy=early_repay_fee_penalty_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BZ**；**params.G≠实验字母 BZ**；**params.N≠实验字母 BZ**；亦≠单字母实验 A/B/Z；禁 null/holdout/跑后改口；终值待预检冻结）；**`params.bz0_primary_demo` 建议 `invent_ignore_early_repay_fee_or_penalty`**（禁与 invent_asof_leak_early_repay_fee 双挂；BZ1半泄露不得升格并列主报；终值待预检冻结）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BZ0/BZ1/BZ2 净收益/成本质量、ΔFakeZeroEarlyRepayFee、ΔEarlyCloseNet、ΔFinancingTrueCost；分桶（融资提前了结手续费违约金误开 / 核对日泄露 / 正常费窗 / 费率切日窗 / 通道前 / vs A·Z·BA–BY·K·AB·Y·B·H·W·X·V·U·T·S）。  
- 自检布尔：BZ2 是否 pit_by_effective_date；BZ0 是否单一主报；BZ1 是否仅核对日泄露；是否未与 A/Z/BA–BY/K/AB/Y/B/H/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 BZ 与 A 或 B 或 Z 或 K 或 Y 或 BA–BY 或 BO 或 BS 或 BX 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 BZ≠单字母假设-Z；params.Y≠实验字母 BZ；BZ≠BY；BZ≠BO；BZ≠BS；BZ≠BX；BZ≠BW；BZ≠BV；BZ≠BU；BZ≠BT；BZ≠BR；BZ≠BH；带过 BY≠Y/BX/BW/BV/BU/BT/BS/BO/BR/BH/BM/BC…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BY 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-Z / 假设-K / 假设-W / 假设-BA–BY / 假设-BO / 假设-BS / 假设-BX / 假设-BY / 假设-AB**；**是否未再改 BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-Z（开仓保证金比例）**；**是否未与 invent_asof_leak_early_repay_fee 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假零提前了结费或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BY 及其他 A/D–BY 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-Z**；**不改假设-K**；**不改假设-W**；**不改假设-BA–BY**；**尤其不改假设-Z；尤其不改假设-BY；尤其不改假设-BO；尤其不改假设-BS；尤其不改假设-BX**；**不改假设-AB**；**勿再改 BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券券池日可借量（BU）、融券提前召回（BV）、授信占用口径（BW）、融资利息起息日/计息天数（BX）、追保宽限期/强平通知时限（BY）、融券空头名单（K）之外，**融资提前了结手续费/违约金**须按当时有效规则 PIT；不得默认永远零费，或用核对日更宽减免规则铺满。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BZ** 标准件，**不改口径主线**，**不改假设 A–BY 正文**，**尤其不改假设-Z / 假设-BY / 假设-BO / 假设-BS / 假设-BX**。与实验 A/Z/BA–BY/K/AB/B/H/W/Y/X/V/U/T/S 分工：**A=板上枯竭门槛；Z=开仓保证金比例（严禁复用）；BA–BY=两融族已冻/在途；BO=假零息；BS=利率档；BX=起息日基数；BY=追保宽限期；BZ=融资提前了结手续费/违约金误开（BZ≠A≠B≠Z≠K≠Y≠BA≠…≠BY≠BO≠BS≠BX≠BW≠BV≠BU≠BT≠BR≠BH≠AB≠W≠H≠T≠S≠U≠V≠X；带过 BY≠Y/BX/BW…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 待预检**（结论栏空；**未标纸面齐**） |
| 标准件路径 | `假设-BZ-融资提前了结手续费违约金误开.md` |
| 清单序号 | 约 #83 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**early_repay_fee_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BZ；params.G≠实验字母 BZ；params.N≠实验字母 BZ；亦≠单字母实验 A/B/Z；禁 null/holdout；终值待预检冻结）**；**bz0_primary_demo 建议 invent_ignore_early_repay_fee_or_penalty（禁双挂 invent_asof_leak_early_repay_fee；BZ1半泄露不得升格并列主报；终值待预检冻结）**；锚点建议 early_repay_fee_honest=pit_by_effective_date / early_repay_fee_scope=financing_early_close_fee_or_penalty / early_repay_fee_over_policy=charge_or_fail_missing_fee_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **BZ≠Z/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH**（及 ≠B/A/Y/BA–BY/K/AB/H/W/T/S/U/V/X）；**严禁复用假设-Z**；**尤其不改假设-Z/BY/BO/BS/BX**；**params.Y≠实验字母 BZ** |
| 结论栏 | 空 |

---

## 待预检键清单

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**待预检冻结**；**params.Y≠实验字母 BZ**；**params.G≠实验字母 BZ**；**params.N≠实验字母 BZ**；禁 null/holdout）  
2. `params.bz0_primary_demo` = `invent_ignore_early_repay_fee_or_penalty`（**待预检冻结**；禁与 `invent_asof_leak_early_repay_fee` 双挂；BZ1不升格主报）  
3. 锚点建议：`early_repay_fee_honest=pit_by_effective_date` / `early_repay_fee_scope=financing_early_close_fee_or_penalty` / `early_repay_fee_over_policy=charge_or_fail_missing_fee_rule` / `margin_channel_start=2010-03-31` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`

---

## 与 BA–BY / Z / K 撞题检查表

| 对照 | 是否撞题 | 说明 |
|------|----------|------|
| 假设-Z | **否（硬分列）** | 开仓保证金比例 ≠ 提前了结费；**BZ≠Z**；**严禁复用**；绝不可做成开仓比例续篇 |
| 假设-BY | **否（硬分列）** | 追保宽限期 ≠ 提前了结费；**BZ≠BY**；不改 BY（复检在途） |
| 假设-BO | **否（硬分列）** | 假零息 ≠ 提前了结费；**BZ≠BO**；不改 BO |
| 假设-BS | **否（硬分列）** | 利率档 ≠ 提前了结费；**BZ≠BS**；不改 BS |
| 假设-BX | **否（硬分列）** | 起息/日基数 ≠ 提前了结费；**BZ≠BX**；不改 BX |
| 假设-BW/BV/BU/BT/BR/BH | **否** | 占用/召回/日库存/强平序/借券费/额度 ≠ 提前了结费 |
| 假设-BA–BN/BP/BQ/BF/BL/BB/BD/BG/BC/BM/K/AB | **否** | 各页主病旁路；本页不重开 |
| 假设-A/B/H/W/X/V/U/T/S/Y | **否** | 板上/旧位/退市/除权/ST板幅/印花税/过户/证管/经手/集合量 ≠ 提前了结费 |

---

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-03 | 新建草稿·待预检（总管线 BY 补丁已交后写 BZ；选题融资提前了结手续费/违约金误开；**BZ≠Z/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH**；primary_demo 建议=`invent_ignore_early_repay_fee_or_penalty`；Y/G/N/Y2 待预检；不开回测；未改 Z/BY/BO/BS/BX 及其他已齐字母；**未标纸面齐**）。 |
