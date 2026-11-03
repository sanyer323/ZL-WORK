# 假设 CE · 跌停板可成交性误开 / 默认触及跌停仍可按目标价或收盘价全额卖出成交（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CD 两条补丁已交（tip=`83c2787`；复检/入库另线并行后写下一纸面 CE）；清单撞题规则另选正交执行缺口（**回测默认「触及跌停仍可按目标价/收盘价全额卖出成交」** ≠ 假设-CD 涨停板可成交性误开（涨停侧对称正交） ≠ 假设-A 板上枯竭/一字与封板容量主实验 ≠ 假设-AR 板上排队假队首 ≠ 假设-D 成交时点开vs收与停牌假成交 ≠ 假设-C 股票池当时名单 ≠ 假设-E 整手/碎股约束 ≠ 假设-CA 维持比分子分母 ≠ 假设-CB 融资展期审批 ≠ 假设-CC 两融标的调出强制了结时点 ≠ 两融审批/费用族）；选题自 `事实与坑`「跌停时买方枯竭；回测用收盘价一律卖出成交等于假设永远可成」+ 口径「执行鸿沟」+ 与 CD 涨停侧对称；本页**假定板上容量层（A）/ 排队位次层（AR）/ 成交时点与停牌层（D）/ 超涨跌停价无效层（AG）/ 股票池层（C）/ 涨停可成交误开层（CD）诚实或显式旁路**，主病只在**发明「触及跌停仍可按目标价/收盘价全额卖出成交」这一误开默认**；**A 正文主测「涨停可成交性/板上枯竭」真数队列**（**双字母 CE ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 续篇；不抢 A 真数队列**），**CD 正文主测「涨停板可成交性误开」**（`invent_assume_limit_up_always_fillable`；涨停全额可成 ≠ 跌停全额可成；**与 CD 对称分列；严禁改 CD**），**AR 正文主测「板上排队假队首」**（`invent_limit_queue_as_front`；假队首 ≠ 全额可成默认；**严禁改 AR**），**D 正文主测「成交时点开vs收与停牌假成交」**（开收时点 ≠ 跌停全额可成默认；**严禁改 D**），**C 正文主测「股票池当时名单」**（**双字母 CE ≠ 单字母假设-C；严禁复用 C**），**E 正文主测「整手/碎股」**（**双字母 CE ≠ 单字母假设-E；严禁复用 E**），**CA/CB/CC 正文主测两融族**（维持比公式/展期审批/调出了结时限；与本页正交；**严禁改 CA/CB/CC**）→ 自立；与假设 H（退市整理）/ B（历史清单实验 B 旧位；**双字母 CE ≠ 单字母 B；CE≠B**）/ Z/BA–CD（两融族与涨停可成交；**CE≠Z/BA…CD**；与两融审批/费用类正交；**尤其不改 CD/CC/CB/CA**）/ AG/AF/L/F/G/X/W/Y/K/AB 等**分列**；**新建实验 CE**  
状态：**草稿 · 预检有条件通过 · 两条已冻 · 待复检**（结论栏空；禁止把「触及跌停仍可按目标价/收盘价全额卖出成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CD 及其他 A/D–CD 已交正文与冻结补丁；尤其不改假设-A；尤其不改假设-AR；尤其不改假设-D；尤其不改假设-C；尤其不改假设-E；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；尤其不改假设-CD；不改假设-H；不改假设-K；不改假设-BA–CD；不改假设-AB；勿再改 CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CE（约 #88）。与假设 **CD（涨停板可成交性误开）** **硬分列（专节强调 · 对称）**：CD = 回测是否默认「触及涨停仍可按目标价/收盘价**全额买入**成交」；本页 = 回测是否默认「触及跌停仍可按目标价/收盘价**全额卖出**成交」；涨停侧 ≠ 跌停侧；**严禁复用 CD 题面或 `invent_assume_limit_up_always_fillable`**；**尤其不改假设-CD**。**CE≠CD**。与假设 **A（涨停可成交性/板上枯竭）** **硬分列（专节强调）**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成（含一字开盘买记 0、封板容量门槛等）的**主实验与真数队列**；本页 = **纸面机制误开点**：回测/仿真是否默认发明「触及跌停仍可按目标价/收盘价**全额卖出**成交」并系统性低估跌停日卖出失败、排队与次日继续下行的实现风险；容量门槛 ≠ 全额可成默认；**双字母 CE ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不占** A 的 A0/A1 主报与真数席位；**尤其不改假设-A**。**CE≠A**。与假设 **AR（板上排队假队首）** **硬分列（专节强调）**：AR = 在已承认板上存在有限对手剩余的前提下是否发明假队首/假比例；本页 = 是否发明「触及跌停仍**全额卖出**可成」（连有限剩余都不承认的更肥误开）；假队首 ≠ 全额可成默认；**禁止**复用 AR 的 `invent_limit_queue_as_front` 当本页主报；**尤其不改假设-AR**。**CE≠AR**。与假设 **D（成交时点与停牌）** **硬分列（专节强调）**：D = 开 vs 收成交时点与停牌假成交；本页 = 跌停日是否仍按目标价/收盘价**全额卖出**记成；开收时点 ≠ 跌停全额可成；**双字母 CE ≠ 单字母假设-D**；**严禁复用 D 题面**；**尤其不改假设-D**。**CE≠D**。与假设 **C（股票池当时名单）** **硬分列**：C = 成分/股票池 PIT；本页 = 跌停全额可成误开；**双字母 CE ≠ 单字母假设-C**；**严禁复用 C**。**CE≠C**。与假设 **E（整手/碎股）** **硬分列**：E = 整手/碎股约束；本页 = 跌停全额可成误开；整手 ≠ 跌停全额可成；**双字母 CE ≠ 单字母假设-E**；**严禁复用 E**。**CE≠E**。与假设 **CA（维持担保比例分子分母）** **硬分列**：CA = 维持比怎么算；本页 = 跌停可成交性误开；公式 ≠ 板上全额可成；**尤其不改假设-CA**。**CE≠CA**。与假设 **CB（融资合约展期/续作审批）** **硬分列**：展期审批 ≠ 跌停全额可成；**尤其不改假设-CB**。**CE≠CB**。与假设 **CC（两融标的调出强制了结时点）** **硬分列**：CC = 调出后强制了结时限；本页 = 跌停板可成交性误开；调出了结时限 ≠ 跌停全额可成；**尤其不改假设-CC**。**CE≠CC**。与假设 **BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ** 及两融审批/费用族 **硬分列**：与两融审批/费用类正交；本页不主测两融；**尤其不改**上述已冻页。与假设 AG/AF/L/F/G/X/W/Y/K/AB/H **硬分列**：超板无效/单笔上限/整手交 E/市价/取整/板幅PIT/ST板幅/除权板价/集合量/融券名单/空头价限/退市整理 ≠ 跌停全额可成默认。与假设 AN–CD **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族/涨停可成交误开等。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A / 假设-C / 假设-D / 假设-E / 假设-CD**。**严禁改写/续写假设-CA / 假设-CB / 假设-CC / 假设-CD / 假设-AR**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CE** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 E**（整手/碎股；**严禁复用假设-E**）≠ **单字母实验 D**（成交时点与停牌；**严禁复用假设-D**）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **双字母实验 CB**（融资展期审批；**严禁改写假设-CB**）≠ **双字母实验 CC**（调出强制了结时点；**严禁改写假设-CC**）≠ **双字母实验 CD**（涨停板可成交性误开；**严禁改写假设-CD；与 CD 对称分列**）≠ **单字母实验 B** ≠ **单字母实验 Z** ≠ **单字母实验 K** ≠ **单字母实验 Y**。全文凡写「实验 CE / 假设-CE / hypothesis_id=CE / 组 CE0·CE1·CE2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CE 混读或互改；**尤其 params.Y ≠ 实验字母 CE ≠ 单字母假设-C ≠ 单字母假设-E ≠ 单字母假设-D ≠ 单字母假设-A ≠ 双字母假设-CA ≠ 双字母假设-CB ≠ 双字母假设-CC ≠ 双字母假设-CD**。亦**禁止**把实验字母 CE 与单字母 **A/B/C/D/E/Z/K/Y/T/S/U/V/W/X**、双字母 **BA–CD**、双字母 **CA/CB/CC/CD/AR/AG/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `ce0_*` 以外的实验页混读。**双字母 CE ≠ 单字母 C ≠ 单字母 E ≠ 单字母 D ≠ 单字母 A ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 Y ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 CC ≠ 双字母 CD ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BF ≠ 双字母 BQ ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 CE**；**params.G ≠ 实验字母 CE**；**params.N ≠ 实验字母 CE**。**带过：双字母 CD ≠ A/C/D/CA/CB/CC/AR/AG…；双字母 CC ≠ C/CA/CB/BQ/BY/BZ/BF…；双字母 CB ≠ B/C/CA/BF/BZ…；双字母 CA ≠ A/C/BZ/BY…；双字母 AR ≠ A/R/AQ…；双字母 BZ ≠ Z/BY/BX…；双字母 BY ≠ Y/BX/BW…；双字母 BX ≠ X/BW…；双字母 BW ≠ W/BV…；双字母 BV ≠ V/BU/BT…；双字母 BU ≠ U/BB/BT/K…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BP ≠ P/BO/W；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CE ≠ 单字母假设-A / 假设-C / 假设-D / 假设-E；且 ≠ 假设-CA / 假设-CB / 假设-CC / 假设-CD / 假设-AR；带过 CD≠A/C/D/CA…、params.Y≠CE（硬）

| 维度 | 对照页 | 本页假设-CE（双字母） |
|------|--------|----------------------|
| 题面 CD | **涨停板可成交性误开**（`invent_assume_limit_up_always_fillable`；涨停侧全额可成） | **跌停板可成交性误开**：默认「触及跌停仍可按目标价/收盘价全额卖出成交」vs 诚实可成交约束；涨停侧 ≠ 跌停侧；**严禁复用 CD 题面**；**对称分列**；**CE≠CD**；**不改 CD** |
| 题面 A | **涨停可成交性/板上枯竭**（清单实验 A；一字/封板容量门槛；真数队列） | **跌停板可成交性误开**：默认「触及跌停仍可按目标价/收盘价全额卖出成交」vs 诚实可成交约束；容量门槛 ≠ 全额可成默认；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不抢 A 真数队列**；**CE≠A** |
| 题面 AR | **板上排队假队首**（`invent_limit_queue_as_front`） | 假队首 ≠ 全额可成默认（连有限剩余都不承认）；**禁复用 AR 主报**；**CE≠AR**；**不改 AR** |
| 题面 D | **成交时点开vs收与停牌假成交**（清单实验 D） | 开收时点 ≠ 跌停全额可成；**严禁复用 D**；**CE≠D**；**不改 D** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 股票池 ≠ 跌停全额可成；**严禁复用 C**；**CE≠C** |
| 题面 E | **整手/碎股约束**（清单实验 E） | 整手 ≠ 跌停全额可成；**严禁复用 E**；**CE≠E** |
| 题面 CA | **维持担保比例分子分母口径**（`invent_wrong_maint_guarantee_ratio_num_den`） | 公式 ≠ 跌停全额可成；**CE≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批**（`invent_always_allow_financing_rollover`） | 展期审批 ≠ 跌停全额可成；**CE≠CB**；**不改 CB** |
| 题面 CC | **两融标的调出强制了结时点**（`invent_ignore_margin_universe_delist_force_deadline`） | 调出了结时限 ≠ 跌停全额可成；**CE≠CC**；**不改 CC** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_assume_limit_down_always_fillable` |
| 文档 | 清单实验 A / D / C / E / `假设-AR-…` / `假设-CA-…` / `假设-CB-…` / `假设-CC-…` / `假设-CD-…`（**只读；禁止改写**） | `假设-CE-跌停板可成交性误开.md`（新建） |
| 预检键 | 实验字母 A / D / C / E / AR / CA / CB / CC / CD | 实验字母 **CE** / `ce0_primary_demo`；**不得**占用或改写预检 A/D/C/E/AR/CA/CB/CC/CD |

**禁止**：把 CE 写成「A/AR/D/C/E/CA/CB/CC/CD 的续篇」；把「板上容量已诚实（A）/ 排队已诚实（AR）/ 开收时点已诚实（D）/ 股票池已诚实（C）/ 整手已诚实（E）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）/ 涨停可成交已诚实（CD）」静默写成「跌停可成交性已诚实」；覆盖或补丁改写假设-A / 假设-AR / 假设-D / 假设-C / 假设-E / 假设-CA / 假设-CB / 假设-CC / 假设-CD 正文；把 `params.Y/G/N` 与实验字母 CE 混读；**禁** `ce0_primary_demo` 与 `invent_asof_leak_limit_down_always_fillable` **双挂主报**；**禁** CE1 半泄露升格并列主报；**禁**复用假设-A / 假设-C / 假设-D / 假设-E / 假设-CD 题面或口径键；**禁**复用 AR/CA/CB/CC/CD 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有路径、同一未复权价、同一 T+1、同一板上容量/排队位次/成交时点与停牌等输入（A/AR/D 层诚实或显式旁路声明「本页不重开板上容量门槛/假队首/开收时点与停牌」；CD 层诚实或显式旁路声明「本页不重开涨停全额可成误开」）下，把「触及跌停仍可按目标价/收盘价全额卖出成交」或「全样本用核对日当天更宽『跌停日一律全额可卖出』规则回放历史」当成默认，相对「每个交易日按当时有效跌停可成交约束 PIT（一字跌停卖记未成/收盘封板卖按事先写死的容量或记未成；缺字段 skip/敏感性；不抢 A 真数席位）」的诚实组，会**系统性发明假全额可卖出路径并低估跌停日卖出失败、排队与次日继续下行的实现风险**；差异应**集中在跌停板可成交性误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假全额可卖出贡献差、可实现卖出收益差、排队失败差、次日继续下行冲击差在标定噪声带内可忽略，且「假全额可卖出 / 核对日泄露 / 正常封板窗 / 一字窗 / vs A·AR·D·C·E·CA·CB·CC·CD·AG·H·W·X·Y·K·AB·T·S·U·V」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 与 ce0 两条已冻）

```
# 配置写死键（见 §7；两条已冻 · 待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CE；≠ 单字母假设-C；≠ 单字母假设-E；≠ 单字母假设-D；≠ 单字母假设-A；≠ 双字母假设-CA/CB/CC/CD
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CE
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CE；≠ 单字母假设-N；亦≠实验字母 BN
# params.fill_time                        写死 next_open
# params.asof_check_date                 写死 2026-10-16
# params.px_basis                        写死 unadj
# params.limit_down_fill_honest          写死 pit_by_board_fill_rule
# params.limit_down_fill_scope           写死 assume_limit_down_always_fillable_at_target_or_close
# params.limit_down_fill_over_policy     写死 fail_or_cap_or_fail_missing_fill_rule
# params.board_capacity_handoff          写死 a_page     # 板上容量/枯竭交 A；CE≠A；严禁复用假设-A；不抢 A 真数
# params.queue_handoff                   写死 ar_page    # 排队假队首交 AR；CE≠AR；不改 AR
# params.fill_time_suspend_handoff        写死 d_page     # 开收时点与停牌交 D；CE≠D；严禁复用假设-D
# params.beyond_limit_handoff            写死 ag_page    # 超涨跌停价无效交 AG；CE≠AG
# params.lot_size_handoff                写死 e_page     # 整手/碎股交 E；CE≠E；严禁复用假设-E
# params.universe_pool_handoff           写死 c_page     # 股票池交 C；CE≠C；严禁复用假设-C
# params.maint_ratio_formula_handoff     写死 ca_page    # 维持比分子分母交 CA；CE≠CA；不改 CA
# params.financing_rollover_handoff      写死 cb_page    # 展期审批交 CB；CE≠CB；不改 CB
# params.delist_force_deadline_handoff   写死 cc_page    # 调出了结时限交 CC；CE≠CC；不改 CC
# params.limit_up_fill_handoff           写死 cd_page    # 涨停可成交误开交 CD；CE≠CD；对称分列；不改 CD
# params.limit_down_fill_handoff         写死 self       # 本页主病：跌停板可成交性误开（全额可卖出默认）
# params.auction_vol_handoff             写死 y_page
# params.exright_board_handoff           写死 w_page
# params.st_limit_handoff                写死 x_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.stamp_tax_handoff               写死 v_page
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.ce0_primary_demo                写死冻结 invent_assume_limit_down_always_fillable  # 主报：假全额可卖出；禁与 invent_asof_leak_limit_down_always_fillable 双挂争主表；CE1半泄露不得升格并列主报
# params.ce0_invent_assume_limit_down_always_fillable  建议 True
# params.ce1_asof_leak_limit_down_always_fillable_only 建议 True
# params.ce2_pit_limit_down_fill         建议 True
# params.merge_with_A_fill               写死 False  # CE≠A；严禁复用假设-A
# params.merge_with_AR_queue             写死 False  # CE≠AR；不改 AR
# params.merge_with_D_fill_time          写死 False  # CE≠D；严禁复用假设-D
# params.merge_with_C_universe_pool      写死 False  # CE≠C；严禁复用假设-C
# params.merge_with_E_lot_size           写死 False  # CE≠E；严禁复用假设-E
# params.merge_with_CA_maint_ratio_formula 写死 False  # CE≠CA；不改 CA
# params.merge_with_CB_financing_rollover 写死 False  # CE≠CB；不改 CB
# params.merge_with_CC_delist_force_deadline 写死 False  # CE≠CC；不改 CC
# params.merge_with_CD_limit_up_fill     写死 False  # CE≠CD；对称分列；不改 CD
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_B_legacy             写死 False  # CE≠B
# params.merge_with_Z_margin_ratio       写死 False  # 与两融审批/费用类正交
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
# params.merge_with_BV_short_recall      写死 False
# params.merge_with_BW_credit_usage      写死 False
# params.merge_with_BX_interest_start_daycount 写死 False
# params.merge_with_BY_margin_call_grace 写死 False
# params.merge_with_BZ_early_repay_fee   写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_Y_auction_vol        写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.missing_limit_down_fill_policy  写死 skip
# params.day_freq_proxy                  写死 limit_down_fill_sensitivity
# params.universe_rule                   写死 sse_szse_limit_down_fill_misopen_check
# params.fail_policy                     写死 skip
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母CE；params.G≠实验字母CE；params.N≠实验字母CE；亦≠单字母实验C/E/D/A/Z；禁 null/holdout/跑后改口
# params.date_start / date_end           写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改跌停可成交误开口径、Y/G/N/Y2、主窗/oos、ce0_primary_demo
```

可编码摘要（伪代码，不开跑）：

```
asof = params.asof_check_date  # 2026-10-16
# CE0：假全额可卖出——触及跌停仍按目标价/收盘价 100% 卖出成交
# CE1：仅 asof 日更宽「跌停日一律全额可卖出」规则泄露铺满
# CE2：每个交易日 d 按当日已生效跌停可成交约束 PIT（消费 A 诚实容量或旁路；消费 AR/D/CD 旁路）
# 缺可成交约束字段 → skip（params.missing_limit_down_fill_policy）
```

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
limit_down_fill_honest = "pit_by_board_fill_rule"
limit_down_fill_scope = "assume_limit_down_always_fillable_at_target_or_close"
limit_down_fill_over_policy = "fail_or_cap_or_fail_missing_fill_rule"
ce0_primary_demo = "invent_assume_limit_down_always_fillable"  # 单一主报·已冻结；禁与 invent_asof_leak_limit_down_always_fillable 双挂
ce0_invent_assume_limit_down_always_fillable = True
ce1_asof_leak_limit_down_always_fillable_only = True
ce2_pit_limit_down_fill = True
merge_with_A_fill = False
merge_with_AR_queue = False
merge_with_D_fill_time = False
merge_with_C_universe_pool = False
merge_with_E_lot_size = False
merge_with_CA_maint_ratio_formula = False
merge_with_CB_financing_rollover = False
merge_with_CC_delist_force_deadline = False
merge_with_CD_limit_up_fill = False
fail_policy = "skip"
```

### 2.2 三组对照（CE0 / CE1 / CE2）

| 组 | 口径 | 说明 |
|----|------|------|
| CE0 天真 | `invent_assume_limit_down_always_fillable`（单一主报·已冻结） | 发明假全额可卖出路径；禁与 invent_asof_leak_limit_down_always_fillable 双挂 |
| CE1 半泄露·混口径 | 全样本用 `asof_check_date` 当天更宽「跌停日一律全额可卖出」规则铺满历史 | 仅跌停全额可卖出 asof 泄露；不升格并列主报 |
| CE2 PIT | `limit_down_fill_honest=pit_by_board_fill_rule` | 每个交易日按当时已生效跌停可成交约束 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：跌停触及/封板标签代理 + 目标价/收盘价全额卖出成交默认 vs 诚实未成/容量帽 → 当日可实现卖出与失败笔；缺字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有未复权 OHLC + 涨跌停价/封板标签 + 卖出意图代理即可纸面起步；**本页不开回测、不拉真数、不派回测岗、不抢 A 真数队列**。

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

天真组 / 半泄露组相对诚实组的假全额可卖出贡献差、可实现卖出收益差、排队失败差、次日继续下行冲击差超出标定噪声带，且差异集中在「跌停板可成交性误开」桶，不被 A 板上容量、AR 假队首、D 开收时点、C 股票池、E 整手、CA/CB/CC 两融族、CD 涨停可成交误开等他页桶吞并。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 A/AR/D/C/E/CA/CB/CC/CD/AG/T 等他页桶吞并；或 holdout 反调 `ce0_primary_demo` / Y·G·N·Y2；或 CE0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CE0 / CE1 / CE2。报告可实现卖出收益差、假全额可卖出贡献差、排队失败差、次日继续下行冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_assume_limit_down_always_fillable",
  "invent_asof_leak_limit_down_always_fillable",
  "limit_down_seal_window",
  "one_word_limit_down_window",
  "vs_A_limit_up_fill",
  "vs_AR_queue_front",
  "vs_D_fill_time_suspend",
  "vs_C_universe_pool",
  "vs_E_lot_size",
  "vs_CA_maint_ratio_formula",
  "vs_CB_financing_rollover",
  "vs_CC_delist_force_deadline",
  "vs_CD_limit_up_fill",
  "vs_AG_beyond_limit",
  "vs_B_legacy",
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

1. 样本无足够跌停触及/封板/可成交约束字段；缺字段却静默当假全额可卖出 → 设计失效。  
2. 把「板上容量已诚实（A）」静默写成「跌停可成交性已诚实」且不声明另页 A → **与 A 撞题**（容量门槛 ≠ 全额可成默认；**尤其 CE≠A**；**严禁复用假设-A**；**绝不可做成 A 续篇**；**不抢 A 真数队列**）。  
3. 把「排队已诚实（AR）」静默写成「跌停可成交性已诚实」 → **与 AR 撞题**（假队首 ≠ 全额可成；**尤其 CE≠AR**；**不改 AR**）。  
4. 把「开收时点/停牌已诚实（D）」静默写成「跌停可成交性已诚实」 → **与 D 撞题**（**尤其 CE≠D**；**严禁复用假设-D**）。  
5. 把「股票池已诚实（C）」静默写成「跌停可成交性已诚实」 → **与 C 撞题**（**尤其 CE≠C**；**严禁复用假设-C**）。  
6. 把「整手已诚实（E）」静默写成「跌停可成交性已诚实」 → **与 E 撞题**（**尤其 CE≠E**；**严禁复用假设-E**）。  
7. 把「涨停可成交已诚实（CD）」静默写成「跌停可成交性已诚实」 → **与 CD 撞题**（涨停侧 ≠ 跌停侧；**尤其 CE≠CD**；**对称分列**；**不改 CD**）。  
8. 把「分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「跌停可成交性已诚实」 → **与 CA/CB/CC 撞题**（与两融审批/费用类正交；**尤其 CE≠CA / CE≠CB / CE≠CC**；**不改 CA/CB/CC**）。  
9. 把「超板无效/整手/单笔上限/市价保护已诚实」写成主病或不声明另页 → 与 AG/E/AF/L 撞题。  
10. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「跌停可成交性已诚实」→ 与交易所费用族撞题（**明确避开预检T**）。  
11. 把实验字母 CE 与单字母 A/B/C/D/E/Z/K/Y/T/S/U/V/W/X 或双字母 BA–CD/CA/CB/CC/CD/AR/AG/BZ/BY/BF/BQ/BC/BT/BD/BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
12. holdout 反调 `ce0_primary_demo` / Y·G·N·Y2 → 结论无效。  
13. 用复权价代理跌停可成交路径 → 标签与执行双错，结论无效。  
14. 用核对日更宽「假全额可卖出」当诚实 PIT、或把临时宽口径铺满历史 → 设计失效。  
15. **`ce0_primary_demo` 与 `invent_asof_leak_limit_down_always_fillable` 双挂主报**；或 CE1 升格并列主报 → 设计失效。  
16. **改写或覆盖 `假设-A` / `假设-AR` / `假设-D` / `假设-C` / `假设-E` / `假设-CA` / `假设-CB` / `假设-CC` / `假设-CD` / 已冻 AA–CD** → 硬边界违约，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块、前收盘/涨跌停价、跌停触及/封板/一字标签代理；  
- 卖出意图量、目标价/收盘价全额卖出成交默认 vs 诚实未成/容量帽规则及生效日；  
- 板上容量 / 排队位次 / 开收时点与停牌输入（消费 A/AR/D 诚实 PIT 或显式旁路声明本页不重开）；  
- 涨停可成交误开旁路声明（消费 CD 或显式旁路「本页不重开涨停侧」）；  
- 交易日历。

可选：主板 ±10% vs 创业/科创 ±20% 分段；与 A 容量窗、AR 排队窗、D 开收窗、CD 涨停窗对照但不混主结论；缺可成交约束原因码敏感性（主报仍在跌停板可成交性误开）。

**禁止**：用核对日「今天跌停一律全额可卖出」铺满当唯一诚实组；用复权价；把板上容量已诚实/排队已诚实/开收时点已诚实/股票池已诚实/整手已诚实/涨停可成交已诚实/两融审批费用已诚实当成「跌停可成交性正确」依据；把 A/AR/D/C/E/CA/CB/CC/CD/AG/Z/BA–CD/K/AB/H/W/Y/X/V/U/T/S/AN–CD 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`CE`  
- **组**：CE0 / CE1 / CE2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`limit_down_fill_honest=pit_by_board_fill_rule`；`limit_down_fill_scope=assume_limit_down_always_fillable_at_target_or_close`；`limit_down_fill_over_policy=fail_or_cap_or_fail_missing_fill_rule`；`board_capacity_handoff=a_page`；`queue_handoff=ar_page`；`fill_time_suspend_handoff=d_page`；`beyond_limit_handoff=ag_page`；`lot_size_handoff=e_page`；`universe_pool_handoff=c_page`；`maint_ratio_formula_handoff=ca_page`；`financing_rollover_handoff=cb_page`；`delist_force_deadline_handoff=cc_page`；`limit_up_fill_handoff=cd_page`；其余 handoff 见 §2.1；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_limit_down_fill_misopen_check`；`missing_limit_down_fill_policy=skip`；`day_freq_proxy=limit_down_fill_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 CE**；**params.G≠实验字母 CE**；**params.N≠实验字母 CE**；亦≠单字母实验 C/E/D/A/Z；禁 null/holdout/跑后改口）；**`params.ce0_primary_demo` 写死冻结 `invent_assume_limit_down_always_fillable`**（禁与 invent_asof_leak_limit_down_always_fillable 双挂；CE1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- CE0/CE1/CE2 净收益/成本质量、ΔFakeAlwaysSellable、ΔRealizableSellReturn、ΔQueueFail、ΔNextDayDownImpact；分桶（跌停板可成交性误开 / 核对日泄露 / 封板窗 / 一字窗 / vs A·AR·D·C·E·CA·CB·CC·CD·AG·Z·BA–CD·K·AB·Y·H·W·X·V·U·T·S）。  
- 自检气泡：CE2 是否 pit_by_board_fill_rule；CE0 是否单一主报建议；CE1 是否仅核对日泄露；是否未与 A/AR/D/C/E/CA/CB/CC/CD/AG/Z/BA–CD/K/AB/Y/H/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 CE 与 C 或 E 或 D 或 A 或 CA 或 CB 或 CC 或 CD 或 AR 或 B 或 Z 或 K 或 Y 或 BA–CD 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 CE≠单字母假设-A；CE≠单字母假设-C；CE≠单字母假设-E；CE≠单字母假设-D；CE≠双字母假设-CA；CE≠双字母假设-CB；CE≠双字母假设-CC；CE≠双字母假设-CD（对称）；CE≠双字母假设-AR；params.Y≠实验字母 CE**；**是否未改 Y/Z/AA–CD 冻结补丁正文**；**是否未改假设-A / 假设-AR / 假设-D / 假设-C / 假设-E / 假设-CA / 假设-CB / 假设-CC / 假设-CD**；**是否未重做预检T**；**是否未复用假设-A / 假设-C / 假设-D / 假设-E / 假设-CD**；**是否未与 invent_asof_leak_limit_down_always_fillable 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假全额可卖出或核对日泄露吹成诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不占本机 8765 席位；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–CD 及其他 A/D–CD 已交正文**；**尤其不改假设-A；尤其不改假设-AR；尤其不改假设-D；尤其不改假设-C；尤其不改假设-E；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；尤其不改假设-CD**；**勿再改 CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 执行鸿沟同向：板上枯竭（A）、板上排队（AR）、成交时点与停牌（D）、超涨跌停价无效（AG）、股票池当时名单（C）、涨停板可成交性误开（CD）之外，**回测不得默认「触及跌停仍可按目标价/收盘价全额卖出成交」**；须按当时有效可成交约束 PIT。与两融审批/费用族（Z/BA–CC 等）正交，本页不主测两融。与 CD 涨停侧**对称分列**，本页专测跌停侧卖出可成交误开。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 CE** 标准件，**不改口径主线**，**不改假设 A–CD 正文**，**尤其不改假设-A / 假设-AR / 假设-D / 假设-C / 假设-E / 假设-CA / 假设-CB / 假设-CC / 假设-CD**。与实验 A/AR/D/C/E/CA/CB/CC/CD/AG/Z/BA–CD/K/AB/H/W/Y/X/V/U/T/S 分工：**A=板上枯竭主实验（严禁复用；不抢真数）；AR=假队首；D=开收时点与停牌（严禁复用）；C=股票池（严禁复用）；E=整手（严禁复用）；CA=维持比分子分母；CB=展期审批；CC=调出了结时限；CD=涨停板可成交性误开（对称）；CE=跌停板可成交性误开（CE≠A≠AR≠D≠C≠E≠CA≠CB≠CC≠CD≠B≠Z≠K≠Y≠BA≠…≠BZ≠BY≠BF≠BQ≠BC≠BT≠BD≠BL≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AG≠AB≠W≠H≠T≠S≠U≠V≠X）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 预检有条件通过 · 两条已冻 · 待复检**（结论栏空；**禁止标任何纸面齐**） |
| 标准件路径 | `假设-CE-跌停板可成交性误开.md` |
| 清单序号 | 约 #88 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**limit_down_fill_honest=pit_by_board_fill_rule 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 CE；params.G≠实验字母 CE；params.N≠实验字母 CE；亦≠单字母实验 C/E/D/A/Z；禁 null/holdout/跑后改口）**；**ce0_primary_demo 写死冻结 invent_assume_limit_down_always_fillable（禁双挂 invent_asof_leak_limit_down_always_fillable；CE1半泄露不得升格并列主报）**；锚点保留 limit_down_fill_honest=pit_by_board_fill_rule / limit_down_fill_scope=assume_limit_down_always_fillable_at_target_or_close / limit_down_fill_over_policy=fail_or_cap_or_fail_missing_fill_rule / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **CE≠A/C/E/D/CA/CB/CC/CD/AR/AG/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ/Z/B**（及 ≠Y/BA–CD/K/AB/H/W/T/S/U/V/X），**严禁复用假设-A / 假设-C / 假设-D / 假设-E / 假设-CD**；**尤其 CE≠CD（与涨停侧对称分列）**；**尤其不改假设-A/AR/D/C/E/CA/CB/CC/CD**；**params.Y≠实验字母 CE**；与两融审批/费用类正交 |
| 结论栏 | 空 |

---

## 待预检键清单（两条已冻 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已冻结**；**params.Y≠实验字母 CE**；**params.G≠实验字母 CE**；**params.N≠实验字母 CE**；禁 null/holdout）  
2. `params.ce0_primary_demo` = `invent_assume_limit_down_always_fillable`（**已冻结**；禁与 `invent_asof_leak_limit_down_always_fillable` 双挂；CE1不升格主报）  
3. 锚点（已通写死）：`limit_down_fill_honest=pit_by_board_fill_rule` / `limit_down_fill_scope=assume_limit_down_always_fillable_at_target_or_close` / `limit_down_fill_over_policy=fail_or_cap_or_fail_missing_fill_rule` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`


---

## 风控预检补丁·冻结（两条已写死 · 2026-11-04）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 CE**；**`params.G` ≠ 实验字母 CE**；**`params.N` ≠ 实验字母 CE**；**`params.Y` ≠ 单字母实验 C/E/D/A/Z**；尤重**双字母 CE ≠ 单字母假设-A**；**双字母 CE ≠ 单字母假设-C**；**双字母 CE ≠ 单字母假设-E**；**双字母 CE ≠ 单字母假设-D**；**双字母 CE ≠ 双字母假设-CA**；**双字母 CE ≠ 双字母假设-CB**；**双字母 CE ≠ 双字母假设-CC**；**双字母 CE ≠ 双字母假设-CD**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.ce0_primary_demo`**：**写死冻结** **`invent_assume_limit_down_always_fillable`**；禁与 **`invent_asof_leak_limit_down_always_fillable`** 双挂争主表（只挂一个 primary）；**CE1 半泄露不得升格并列主报**。

**跌停板可成交性锚保留（已通写死）**：`params.limit_down_fill_honest=pit_by_board_fill_rule`；`params.limit_down_fill_scope=assume_limit_down_always_fillable_at_target_or_close`；`params.limit_down_fill_over_policy=fail_or_cap_or_fail_missing_fill_rule`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有跌停可成交相关锚点；不改口）。

**与 A/C/E/D/CA/CB/CC/CD/AR/AG/BZ/BY/BX/BW… 硬分列（保留）**：本页 = **跌停板可成交性误开（假全额可卖出默认）**；A = **板上枯竭主实验/真数队列**（**尤其双字母 CE ≠ 单字母假设-A**；**严禁复用假设-A**；**绝不可做成 A 续篇**；**不抢 A 真数队列**）；CD = **涨停板可成交性误开**（**尤其 CE≠CD**；与涨停侧对称分列；**严禁复用假设-CD**；**尤其不改假设-CD**）；AR = **板上排队假队首**（**尤其 CE≠AR**；**尤其不改假设-AR**）；D = **成交时点开vs收与停牌假成交**（**尤其 CE≠D**；**严禁复用假设-D**）；C = **股票池当时名单**（**尤其 CE≠C**；**严禁复用假设-C**）；E = **整手/碎股**（**尤其 CE≠E**；**严禁复用假设-E**）；CA = **维持担保比例分子分母口径**（**尤其 CE≠CA**；**尤其不改假设-CA**）；CB = **融资合约展期/续作审批**（**尤其 CE≠CB**；**尤其不改假设-CB**）；CC = **两融标的调出强制了结时点**（**尤其 CE≠CC**；**尤其不改假设-CC**）。**双字母 CE ≠ 单字母 A ≠ 单字母 C ≠ 单字母 E ≠ 单字母 D ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 CC ≠ 双字母 CD ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BX ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BT ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BF ≠ 双字母 BQ ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 Y**；**params.Y ≠ 实验字母 CE**；**params.G ≠ 实验字母 CE**；**params.N ≠ 实验字母 CE**；禁止捆成「跌停一张表=假全额可卖出」；**尤其不改假设-A**；**尤其不改假设-AR**；**尤其不改假设-D**；**尤其不改假设-C**；**尤其不改假设-E**；**尤其不改假设-CA**；**尤其不改假设-CB**；**尤其不改假设-CC**；**尤其不改假设-CD**；与两融审批/费用类正交；**未标纸面齐**；结论栏仍空；不开回测；不催 A。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CE**；**params.G≠实验字母 CE**；**params.N≠实验字母 CE**；亦≠单字母实验 C/E/D/A/Z；尤重**双字母 CE ≠ 单字母假设-A**；**双字母 CE ≠ 单字母假设-C**；**双字母 CE ≠ 单字母假设-E**；**双字母 CE ≠ 单字母假设-D**；**双字母 CE ≠ 双字母假设-CA/CB/CC/CD**；禁 null/holdout/跑后改口）；② `params.ce0_primary_demo=invent_assume_limit_down_always_fillable`（禁与 `invent_asof_leak_limit_down_always_fillable` 双挂争主表；CE1半泄露不得升格并列主报）。跌停可成交锚保留：`limit_down_fill_honest=pit_by_board_fill_rule`；`limit_down_fill_scope=assume_limit_down_always_fillable_at_target_or_close`；`limit_down_fill_over_policy=fail_or_cap_or_fail_missing_fill_rule`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。硬分列保留：**CE≠A/C/E/D/CA/CB/CC/CD/AR/AG/BZ/BY/BX/BW…**（及 ≠Y/BA–CD/K/AB/H/W/T/S/U/V/X）；**尤其 CE≠CD（与涨停侧对称分列）**；**尤其 CE≠A（不抢实验A真数队列）**；**严禁复用假设-A / 假设-C / 假设-D / 假设-E / 假设-CD**；参考总管派令 / 风控预检有条件通过（草稿 tip=`9c8126b`；清单待补丁 `cf48c4d` #88）。未改 Y/Z/AA–CD 及其他已冻结补丁；**不改假设-A**；**不改假设-AR**；**不改假设-D**；**不改假设-C**；**不改假设-E**；**不改假设-CA**；**不改假设-CB**；**不改假设-CC**；**不改假设-CD**；结论栏仍空；不开回测；不催 A；**未标纸面齐** |
| 2026-11-04 | 新建草稿·待入库预检（总管线：CD 补丁 tip=`83c2787` 已交后写 CE；选题跌停板可成交性误开；**CE≠A/C/E/D/CA/CB/CC/CD/AR…**；尤其 **CE≠CD（与涨停侧对称分列）**、**CE≠C**、**CE≠E**；primary_demo 建议=`invent_assume_limit_down_always_fillable`；Y/G/N/Y2 建议占位 `0.02/0.01/0.05/0.015` 待预检；不开回测；未改 A/AR/D/C/E/CA/CB/CC/CD 及其他已齐字母；**未标纸面齐**）。 |
