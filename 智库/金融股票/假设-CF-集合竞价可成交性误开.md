# 假设 CF · 集合竞价可成交性误开 / 默认开盘或收盘集合竞价订单必能按目标价或参考价全额成交（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CE 两条补丁已交（tip=`ab1ef36`；复检/入库另线并行后写下一纸面 CF）；清单撞题规则另选正交执行缺口（**回测默认「开盘/收盘集合竞价时段订单必能按目标价或参考价全额成交」** ≠ 假设-CD 涨停板可成交性误开（连续竞价涨停侧） ≠ 假设-CE 跌停板可成交性误开（连续竞价跌停侧） ≠ 假设-A 板上枯竭/一字与封板容量主实验 ≠ 假设-Y 集合量分母 ≠ 假设-AN 集合剩单 ≠ 假设-D 成交时点开vs收与停牌假成交 ≠ 假设-F 涨跌停价取整 ≠ 假设-C 股票池当时名单 ≠ 假设-CA/CB/CC 两融族）；选题自 `事实与坑`「集合竞价未匹配/部分成交与价格偏离；回测用目标价/参考价一律全额成交等于假设永远可成」+ 口径「执行鸿沟」+ 与 CD/CE 连续竞价涨跌停侧正交；本页**假定板上容量层（A）/ 排队位次层（AR）/ 成交时点与停牌层（D）/ 超涨跌停价无效层（AG）/ 涨停可成交误开层（CD）/ 跌停可成交误开层（CE）/ 集合量分母层（Y）/ 集合剩单层（AN）诚实或显式旁路**，主病只在**发明「开盘/收盘集合竞价订单必能按目标价或参考价全额成交」这一误开默认**；**A 正文主测「涨停可成交性/板上枯竭」真数队列**（**双字母 CF ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 续篇；不抢 A 真数队列**），**CD 正文主测「涨停板可成交性误开」**（`invent_assume_limit_up_always_fillable`；连续竞价涨停全额可成 ≠ 集合竞价全额可成；**严禁改 CD**），**CE 正文主测「跌停板可成交性误开」**（`invent_assume_limit_down_always_fillable`；连续竞价跌停全额可卖出 ≠ 集合竞价全额可成；**严禁改 CE**），**Y 正文主测「集合量分母」**（集合成交量作仓位分母 ≠ 集合竞价订单是否全额可成；**严禁改 Y**），**F 正文主测「涨跌停价取整」**（**双字母 CF ≠ 单字母假设-F；严禁复用 F**），**C 正文主测「股票池当时名单」**（**双字母 CF ≠ 单字母假设-C；严禁复用 C**），**CA/CB/CC 正文主测两融族**（与本页正交；**严禁改 CA/CB/CC**）→ 自立；与假设 H/B/Z/BA–CE/AG/AF/E/L/G/X/W/K/AB/M/N/AN 等**分列**；**新建实验 CF**  
状态：**草稿 · 待入库预检**（结论栏空；禁止把「开盘/收盘集合竞价订单必能按目标价或参考价全额成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CE 及其他 A/D–CE 已交正文与冻结补丁；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-A；尤其不改假设-Y；尤其不改假设-C；尤其不改假设-F；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；勿再改 CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CF（约 #89）。与假设 **CE（跌停板可成交性误开）** **硬分列（专节强调）**：CE = 回测是否默认「触及跌停仍可按目标价/收盘价**全额卖出**成交」（连续竞价跌停侧）；本页 = 回测是否默认「**开盘/收盘集合竞价**时段订单必能按目标价或参考价**全额**成交」；连续竞价跌停侧 ≠ 集合竞价撮合可成；**严禁复用 CE 题面或 `invent_assume_limit_down_always_fillable`**；**尤其不改假设-CE**。**CF≠CE**。与假设 **CD（涨停板可成交性误开）** **硬分列（专节强调）**：CD = 连续竞价涨停侧全额可成误开；本页 = 集合竞价时段全额可成误开；**严禁复用 CD 题面或 `invent_assume_limit_up_always_fillable`**；**尤其不改假设-CD**。**CF≠CD**。与假设 **A（涨停可成交性/板上枯竭）** **硬分列（专节强调）**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成的**主实验与真数队列**；本页 = **纸面机制误开点**：回测/仿真是否默认发明「集合竞价订单必能按目标价/参考价全额成交」并系统性高估集合竞价可实现成交、低估未匹配/部分成交与价格偏离；容量门槛 ≠ 集合竞价全额可成默认；**双字母 CF ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不占** A 的 A0/A1 主报与真数席位；**尤其不改假设-A**。**CF≠A**。与假设 **Y（集合量分母）** **硬分列（专节强调）**：Y = 集合竞价成交量作仓位/冲击分母是否诚实；本页 = 集合竞价订单是否默认全额可成；分母口径 ≠ 可成交性误开；**禁止**复用 Y 主报当本页主报；**尤其不改假设-Y**。**CF≠Y**。与假设 **F（涨跌停价取整）** **硬分列**：F = ±10%/±20% 取整误判；本页 = 集合竞价全额可成误开；取整 ≠ 集合撮合可成；**双字母 CF ≠ 单字母假设-F**；**严禁复用 F**。**CF≠F**。与假设 **C（股票池当时名单）** **硬分列**：C = 成分/股票池 PIT；本页 = 集合竞价全额可成误开；**双字母 CF ≠ 单字母假设-C**；**严禁复用 C**。**CF≠C**。与假设 **D（成交时点与停牌）** **硬分列**：D = 开 vs 收成交时点与停牌假成交；本页 = 集合竞价时段是否仍按目标价/参考价**全额**记成；开收时点 ≠ 集合全额可成；**严禁复用 D**。**CF≠D**。与假设 **CA/CB/CC** **硬分列**：两融公式/展期/调出了结时限 ≠ 集合竞价全额可成；**尤其不改 CA/CB/CC**。**CF≠CA≠CB≠CC**。与假设 **AR/AG/AN/M/N/BZ/BY/BX/BW…** 及两融审批/费用族 **硬分列**：假队首/超板无效/集合剩单/收盘机制/收盘假GTC/两融审批费用 ≠ 集合竞价全额可成默认。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A / 假设-C / 假设-F / 假设-CD / 假设-CE / 假设-Y**。**严禁改写/续写假设-CE / 假设-CD / 假设-CA / 假设-CB / 假设-CC**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CF** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 F**（涨跌停价取整；**严禁复用假设-F**）≠ **单字母实验 Y**（集合量分母；**严禁改写假设-Y**；亦≠ `params.Y`）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **双字母实验 CB**（融资展期审批；**严禁改写假设-CB**）≠ **双字母实验 CC**（调出强制了结时点；**严禁改写假设-CC**）≠ **双字母实验 CD**（涨停板可成交性误开；**严禁改写假设-CD**）≠ **双字母实验 CE**（跌停板可成交性误开；**严禁改写假设-CE**）≠ **单字母实验 B** ≠ **单字母实验 Z** ≠ **单字母实验 K** ≠ **单字母实验 D** ≠ **单字母实验 E**。全文凡写「实验 CF / 假设-CF / hypothesis_id=CF / 组 CF0·CF1·CF2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CF 混读或互改；**尤其 params.Y ≠ 实验字母 CF ≠ 单字母假设-C ≠ 单字母假设-F ≠ 单字母假设-Y ≠ 单字母假设-A ≠ 双字母假设-CA ≠ 双字母假设-CB ≠ 双字母假设-CC ≠ 双字母假设-CD ≠ 双字母假设-CE**。亦**禁止**把实验字母 CF 与单字母 **A/B/C/D/E/F/Z/K/Y/T/S/U/V/W/X**、双字母 **BA–CE**、双字母 **CA/CB/CC/CD/CE/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `cf0_*` 以外的实验页混读。**双字母 CF ≠ 单字母 C ≠ 单字母 F ≠ 单字母 Y ≠ 单字母 A ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 D ≠ 单字母 E ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 CC ≠ 双字母 CD ≠ 双字母 CE ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 AN ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BF ≠ 双字母 BQ ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 CF**；**params.G ≠ 实验字母 CF**；**params.N ≠ 实验字母 CF**。**带过：双字母 CE ≠ C/E/CA/CB/CC/CD/AR…；双字母 CD ≠ A/C/D/CA/CB/CC/AR…；双字母 CC ≠ C/CA/CB/BQ/BY/BZ/BF…；双字母 CB ≠ B/C/CA/BF/BZ…；双字母 CA ≠ A/C/BZ/BY…；双字母 AR ≠ A/R/AQ…；双字母 BZ ≠ Z/BY/BX…；双字母 BY ≠ Y/BX/BW…；双字母 BX ≠ X/BW…；双字母 BW ≠ W/BV…；双字母 BV ≠ V/BU/BT…；双字母 BU ≠ U/BB/BT/K…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BP ≠ P/BO/W；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CF ≠ 单字母假设-A / 假设-C / 假设-F / 假设-Y；且 ≠ 假设-CA / 假设-CB / 假设-CC / 假设-CD / 假设-CE；带过 CE≠CD、CD≠A…、params.Y≠CF（硬）

| 维度 | 对照页 | 本页假设-CF（双字母） |
|------|--------|----------------------|
| 题面 CE | **跌停板可成交性误开**（`invent_assume_limit_down_always_fillable`；连续竞价跌停侧） | **集合竞价可成交性误开**：默认「开盘/收盘集合竞价订单必能按目标价/参考价全额成交」vs 诚实撮合约束；连续竞价跌停侧 ≠ 集合竞价撮合；**严禁复用 CE 题面**；**CF≠CE**；**不改 CE** |
| 题面 CD | **涨停板可成交性误开**（`invent_assume_limit_up_always_fillable`；连续竞价涨停侧） | 连续竞价涨停侧 ≠ 集合竞价撮合；**严禁复用 CD 题面**；**CF≠CD**；**不改 CD** |
| 题面 A | **涨停可成交性/板上枯竭**（清单实验 A；真数队列） | 容量门槛 ≠ 集合竞价全额可成默认；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不抢 A 真数队列**；**CF≠A** |
| 题面 Y | **集合量分母**（集合成交量作仓位/冲击分母） | 分母口径 ≠ 集合竞价全额可成；**禁复用 Y 主报**；**CF≠Y**；**不改 Y** |
| 题面 F | **涨跌停价取整**（清单实验 F） | 取整 ≠ 集合竞价全额可成；**严禁复用 F**；**CF≠F** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 股票池 ≠ 集合竞价全额可成；**严禁复用 C**；**CF≠C** |
| 题面 D | **成交时点开vs收与停牌假成交**（清单实验 D） | 开收时点 ≠ 集合竞价全额可成；**严禁复用 D**；**CF≠D**；**不改 D** |
| 题面 CA | **维持担保比例分子分母口径** | 公式 ≠ 集合竞价全额可成；**CF≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批** | 展期审批 ≠ 集合竞价全额可成；**CF≠CB**；**不改 CB** |
| 题面 CC | **两融标的调出强制了结时点** | 调出了结时限 ≠ 集合竞价全额可成；**CF≠CC**；**不改 CC** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_assume_call_auction_always_fillable` |
| 文档 | 清单实验 A / C / F / Y / D / `假设-CA-…` / `假设-CB-…` / `假设-CC-…` / `假设-CD-…` / `假设-CE-…`（**只读；禁止改写**） | `假设-CF-集合竞价可成交性误开.md`（新建） |
| 预检键 | 实验字母 A / C / F / Y / D / CA / CB / CC / CD / CE | 实验字母 **CF** / `cf0_primary_demo`；**不得**占用或改写预检 A/C/F/Y/D/CA/CB/CC/CD/CE |

**禁止**：把 CF 写成「A/CE/CD/Y/F/C/D/CA/CB/CC 的续篇」；把「板上容量已诚实（A）/ 跌停可成交已诚实（CE）/ 涨停可成交已诚实（CD）/ 集合量分母已诚实（Y）/ 取整已诚实（F）/ 股票池已诚实（C）/ 开收时点已诚实（D）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「集合竞价可成交性已诚实」；覆盖或补丁改写假设-A / 假设-CE / 假设-CD / 假设-Y / 假设-C / 假设-F / 假设-D / 假设-CA / 假设-CB / 假设-CC 正文；把 `params.Y/G/N` 与实验字母 CF 混读；**禁** `cf0_primary_demo` 与 `invent_asof_leak_call_auction_always_fillable` **双挂主报**；**禁** CF1 半泄露升格并列主报；**禁**复用假设-A / 假设-C / 假设-F / 假设-CD / 假设-CE / 假设-Y 题面或口径键；**禁**复用 CE/CD/Y/CA/CB/CC 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有路径、同一未复权价、同一 T+1、同一板上容量/排队位次/成交时点与停牌/涨跌停可成交等输入（A/AR/D/CD/CE 层诚实或显式旁路声明「本页不重开板上容量门槛/假队首/开收时点与停牌/连续竞价涨跌停全额可成」；Y/AN 层诚实或显式旁路声明「本页不重开集合量分母/集合剩单主病」）下，把「开盘/收盘集合竞价时段订单必能按目标价或参考价全额成交」或「全样本用核对日当天更宽『集合竞价一律全额可成』规则回放历史」当成默认，相对「每个交易日按当时有效集合竞价撮合约束 PIT（未匹配记未成/部分成交按事先写死的撮合规则或记未成；价格偏离按参考价偏离计；缺字段 skip/敏感性；不抢 A 真数席位）」的诚实组，会**系统性发明假全额可成路径并高估集合竞价可实现成交、低估未匹配/部分成交与价格偏离**；差异应**集中在集合竞价可成交性误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、未匹配/部分成交差、价格偏离冲击差在标定噪声带内可忽略，且「假全额可成 / 核对日泄露 / 开盘集合窗 / 收盘集合窗 / vs A·CE·CD·Y·F·C·D·CA·CB·CC·AR·AG·AN·H·W·X·K·AB·T·S·U·V」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 与 cf0 建议占位待预检）

```
# 配置写死键（见 §7；草稿·待入库预检；建议占位如下，待预检冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CF；≠ 单字母假设-C；≠ 单字母假设-F；≠ 单字母假设-Y；≠ 单字母假设-A；≠ 双字母假设-CA/CB/CC/CD/CE
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CF
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CF；≠ 单字母假设-N；亦≠实验字母 BN
# params.fill_time                        写死 next_open
# params.asof_check_date                 写死 2026-10-16
# params.px_basis                        写死 unadj
# params.call_auction_fill_honest        建议 pit_by_auction_match_rule
# params.call_auction_fill_scope         建议 assume_call_auction_always_fillable_at_target_or_ref
# params.call_auction_fill_over_policy   建议 fail_or_partial_or_fail_missing_match_rule
# params.board_capacity_handoff          写死 a_page     # 板上容量/枯竭交 A；CF≠A；严禁复用假设-A；不抢 A 真数
# params.queue_handoff                   写死 ar_page    # 排队假队首交 AR；CF≠AR；不改 AR
# params.fill_time_suspend_handoff        写死 d_page     # 开收时点与停牌交 D；CF≠D；严禁复用假设-D
# params.beyond_limit_handoff            写死 ag_page    # 超涨跌停价无效交 AG；CF≠AG
# params.limit_up_fill_handoff           写死 cd_page    # 涨停可成交误开交 CD；CF≠CD；不改 CD
# params.limit_down_fill_handoff         写死 ce_page    # 跌停可成交误开交 CE；CF≠CE；不改 CE
# params.auction_vol_handoff             写死 y_page     # 集合量分母交 Y；CF≠Y；不改 Y
# params.auction_leftover_handoff        写死 an_page    # 集合剩单交 AN；CF≠AN
# params.lot_size_handoff                写死 e_page
# params.limit_round_handoff             写死 f_page     # 涨跌停取整交 F；CF≠F；严禁复用假设-F
# params.universe_pool_handoff           写死 c_page     # 股票池交 C；CF≠C；严禁复用假设-C
# params.maint_ratio_formula_handoff     写死 ca_page    # 维持比分子分母交 CA；CF≠CA；不改 CA
# params.financing_rollover_handoff      写死 cb_page    # 展期审批交 CB；CF≠CB；不改 CB
# params.delist_force_deadline_handoff   写死 cc_page    # 调出了结时限交 CC；CF≠CC；不改 CC
# params.call_auction_fill_handoff       写死 self       # 本页主病：集合竞价可成交性误开（全额可成默认）
# params.exright_board_handoff           写死 w_page
# params.st_limit_handoff                写死 x_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.stamp_tax_handoff               写死 v_page
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.cf0_primary_demo                建议 invent_assume_call_auction_always_fillable  # 主报建议：假全额可成；禁与 invent_asof_leak_call_auction_always_fillable 双挂争主表；CF1半泄露不得升格并列主报；待预检冻结
# params.cf0_invent_assume_call_auction_always_fillable  建议 True
# params.cf1_asof_leak_call_auction_always_fillable_only 建议 True
# params.cf2_pit_call_auction_fill       建议 True
# params.merge_with_A_fill               写死 False  # CF≠A；严禁复用假设-A
# params.merge_with_AR_queue             写死 False  # CF≠AR；不改 AR
# params.merge_with_D_fill_time          写死 False  # CF≠D；严禁复用假设-D
# params.merge_with_C_universe_pool      写死 False  # CF≠C；严禁复用假设-C
# params.merge_with_F_limit_round        写死 False  # CF≠F；严禁复用假设-F
# params.merge_with_Y_auction_vol        写死 False  # CF≠Y；不改 Y
# params.merge_with_AN_auction_leftover  写死 False  # CF≠AN
# params.merge_with_CA_maint_ratio_formula 写死 False  # CF≠CA；不改 CA
# params.merge_with_CB_financing_rollover 写死 False  # CF≠CB；不改 CB
# params.merge_with_CC_delist_force_deadline 写死 False  # CF≠CC；不改 CC
# params.merge_with_CD_limit_up_fill     写死 False  # CF≠CD；不改 CD
# params.merge_with_CE_limit_down_fill   写死 False  # CF≠CE；不改 CE
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_B_legacy             写死 False  # CF≠B
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
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.missing_call_auction_fill_policy 写死 skip
# params.day_freq_proxy                  写死 call_auction_fill_sensitivity
# params.universe_rule                   写死 sse_szse_call_auction_fill_misopen_check
# params.fail_policy                     写死 skip
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.Y / G / N / Y2                  建议占位 0.02/0.01/0.05/0.015  # params.Y≠实验字母CF；params.G≠实验字母CF；params.N≠实验字母CF；亦≠单字母实验C/F/Y/A/Z；禁 null/holdout/跑后改口；待预检冻结；勿改他字母已冻 Y/G/N/Y2
# params.date_start / date_end           写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改集合竞价可成交误开口径、Y/G/N/Y2、主窗/oos、cf0_primary_demo
```

可编码摘要（伪代码，不开跑）：

```
asof = params.asof_check_date  # 2026-10-16
# CF0：假全额可成——开盘/收盘集合竞价订单按目标价/参考价 100% 成交
# CF1：仅 asof 日更宽「集合竞价一律全额可成」规则泄露铺满
# CF2：每个交易日 d 按当日已生效集合竞价撮合约束 PIT（消费 A/AR/D/CD/CE/Y/AN 诚实或旁路）
# 缺撮合约束字段 → skip（params.missing_call_auction_fill_policy）
```

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
call_auction_fill_honest = "pit_by_auction_match_rule"
call_auction_fill_scope = "assume_call_auction_always_fillable_at_target_or_ref"
call_auction_fill_over_policy = "fail_or_partial_or_fail_missing_match_rule"
cf0_primary_demo = "invent_assume_call_auction_always_fillable"  # 单一主报建议·待预检；禁与 invent_asof_leak_call_auction_always_fillable 双挂
cf0_invent_assume_call_auction_always_fillable = True
cf1_asof_leak_call_auction_always_fillable_only = True
cf2_pit_call_auction_fill = True
merge_with_A_fill = False
merge_with_AR_queue = False
merge_with_D_fill_time = False
merge_with_C_universe_pool = False
merge_with_F_limit_round = False
merge_with_Y_auction_vol = False
merge_with_AN_auction_leftover = False
merge_with_CA_maint_ratio_formula = False
merge_with_CB_financing_rollover = False
merge_with_CC_delist_force_deadline = False
merge_with_CD_limit_up_fill = False
merge_with_CE_limit_down_fill = False
fail_policy = "skip"
```

### 2.2 三组对照（CF0 / CF1 / CF2）

| 组 | 口径 | 说明 |
|----|------|------|
| CF0 天真 | `invent_assume_call_auction_always_fillable`（单一主报建议·待预检） | 发明假全额可成路径；禁与 invent_asof_leak_call_auction_always_fillable 双挂 |
| CF1 半泄露·混口径 | 全样本用 `asof_check_date` 当天更宽「集合竞价一律全额可成」规则铺满历史 | 仅集合竞价全额可成 asof 泄露；不升格并列主报 |
| CF2 PIT | `call_auction_fill_honest=pit_by_auction_match_rule` | 每个交易日按当时已生效集合竞价撮合约束 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：开盘/收盘集合竞价窗标签代理 + 目标价/参考价全额成交默认 vs 诚实未匹配/部分成交/价格偏离 → 当日可实现成交与失败笔；缺字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有未复权 OHLC + 集合竞价成交量/未匹配代理 + 成交意图代理即可纸面起步；**本页不开回测、不拉真数、不派回测岗、不抢 A 真数队列**。

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

天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、未匹配/部分成交差、价格偏离冲击差超出标定噪声带，且差异集中在「集合竞价可成交性误开」桶，不被 A 板上容量、CE 跌停可成交、CD 涨停可成交、Y 集合量分母、F 取整、C 股票池、D 开收时点、CA/CB/CC 两融族、AN 集合剩单等他页桶吞并。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 A/CE/CD/Y/F/C/D/CA/CB/CC/AR/AG/AN/T 等他页桶吞并；或 holdout 反调 `cf0_primary_demo` / Y·G·N·Y2；或 CF0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CF0 / CF1 / CF2。报告可实现成交差、假全额可成贡献差、未匹配/部分成交差、价格偏离冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_assume_call_auction_always_fillable",
  "invent_asof_leak_call_auction_always_fillable",
  "open_call_auction_window",
  "close_call_auction_window",
  "vs_A_limit_up_fill",
  "vs_CE_limit_down_fill",
  "vs_CD_limit_up_fill",
  "vs_Y_auction_vol",
  "vs_AN_auction_leftover",
  "vs_F_limit_round",
  "vs_AR_queue_front",
  "vs_D_fill_time_suspend",
  "vs_C_universe_pool",
  "vs_CA_maint_ratio_formula",
  "vs_CB_financing_rollover",
  "vs_CC_delist_force_deadline",
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

1. 样本无足够开盘/收盘集合竞价窗/撮合约束字段；缺字段却静默当假全额可成 → 设计失效。  
2. 把「板上容量已诚实（A）」静默写成「集合竞价可成交性已诚实」且不声明另页 A → **与 A 撞题**（**尤其 CF≠A**；**严禁复用假设-A**；**绝不可做成 A 续篇**；**不抢 A 真数队列**）。  
3. 把「跌停可成交已诚实（CE）」静默写成「集合竞价可成交性已诚实」 → **与 CE 撞题**（连续竞价跌停侧 ≠ 集合竞价；**尤其 CF≠CE**；**不改 CE**）。  
4. 把「涨停可成交已诚实（CD）」静默写成「集合竞价可成交性已诚实」 → **与 CD 撞题**（连续竞价涨停侧 ≠ 集合竞价；**尤其 CF≠CD**；**不改 CD**）。  
5. 把「集合量分母已诚实（Y）」静默写成「集合竞价可成交性已诚实」 → **与 Y 撞题**（分母 ≠ 全额可成；**尤其 CF≠Y**；**不改 Y**）。  
6. 把「涨跌停取整已诚实（F）」静默写成「集合竞价可成交性已诚实」 → **与 F 撞题**（**尤其 CF≠F**；**严禁复用假设-F**）。  
7. 把「股票池已诚实（C）」静默写成「集合竞价可成交性已诚实」 → **与 C 撞题**（**尤其 CF≠C**；**严禁复用假设-C**）。  
8. 把「开收时点/停牌已诚实（D）」静默写成「集合竞价可成交性已诚实」 → **与 D 撞题**（**尤其 CF≠D**；**严禁复用假设-D**）。  
9. 把「分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「集合竞价可成交性已诚实」 → **与 CA/CB/CC 撞题**（与两融审批/费用类正交；**尤其 CF≠CA / CF≠CB / CF≠CC**；**不改 CA/CB/CC**）。  
10. 把「集合剩单/超板无效/整手/单笔上限/市价保护已诚实」写成主病或不声明另页 → 与 AN/AG/E/AF/L 撞题。  
11. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「集合竞价可成交性已诚实」→ 与交易所费用族撞题（**明确避开预检T**）。  
12. 把实验字母 CF 与单字母 A/B/C/D/E/F/Z/K/Y/T/S/U/V/W/X 或双字母 BA–CE/CA/CB/CC/CD/CE/AR/AG/AN/BZ/BY/BF/BQ/BC/BT/BD/BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
13. holdout 反调 `cf0_primary_demo` / Y·G·N·Y2 → 结论无效。  
14. 用复权价代理集合竞价可成交路径 → 标签与执行双错，结论无效。  
15. 用核对日更宽「假全额可成」当诚实 PIT、或把临时宽口径铺满历史 → 设计失效。  
16. **`cf0_primary_demo` 与 `invent_asof_leak_call_auction_always_fillable` 双挂主报**；或 CF1 升格并列主报 → 设计失效。  
17. **改写或覆盖 `假设-A` / `假设-CE` / `假设-CD` / `假设-Y` / `假设-C` / `假设-F` / `假设-D` / `假设-CA` / `假设-CB` / `假设-CC` / 已冻 AA–CE** → 硬边界违约，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块、开盘/收盘集合竞价窗标签代理；  
- 成交意图量、目标价/参考价全额成交默认 vs 诚实未匹配/部分成交/价格偏离规则及生效日；  
- 板上容量 / 排队位次 / 开收时点与停牌 / 涨跌停可成交误开输入（消费 A/AR/D/CD/CE 诚实 PIT 或显式旁路声明本页不重开）；  
- 集合量分母 / 集合剩单旁路声明（消费 Y/AN 或显式旁路「本页不重开分母/剩单主病」）；  
- 交易日历。

可选：开盘集合 vs 收盘集合分段；与 A 容量窗、CE/CD 涨跌停窗、Y 集合量窗、AN 剩单窗对照但不混主结论；缺撮合约束原因码敏感性（主报仍在集合竞价可成交性误开）。

**禁止**：用核对日「今天集合竞价一律全额可成」铺满当唯一诚实组；用复权价；把板上容量已诚实/跌停可成交已诚实/涨停可成交已诚实/集合量分母已诚实/取整已诚实/股票池已诚实/开收时点已诚实/两融审批费用已诚实当成「集合竞价可成交性正确」依据；把 A/CE/CD/Y/F/C/D/CA/CB/CC/AR/AG/AN/Z/BA–CE/K/AB/H/W/X/V/U/T/S 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`CF`  
- **组**：CF0 / CF1 / CF2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`call_auction_fill_honest=pit_by_auction_match_rule`（建议）；`call_auction_fill_scope=assume_call_auction_always_fillable_at_target_or_ref`（建议）；`call_auction_fill_over_policy=fail_or_partial_or_fail_missing_match_rule`（建议）；`board_capacity_handoff=a_page`；`queue_handoff=ar_page`；`fill_time_suspend_handoff=d_page`；`beyond_limit_handoff=ag_page`；`limit_up_fill_handoff=cd_page`；`limit_down_fill_handoff=ce_page`；`auction_vol_handoff=y_page`；`auction_leftover_handoff=an_page`；`limit_round_handoff=f_page`；`universe_pool_handoff=c_page`；`maint_ratio_formula_handoff=ca_page`；`financing_rollover_handoff=cb_page`；`delist_force_deadline_handoff=cc_page`；其余 handoff 见 §2.1；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_call_auction_fill_misopen_check`；`missing_call_auction_fill_policy=skip`；`day_freq_proxy=call_auction_fill_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议占位 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 CF**；**params.G≠实验字母 CF**；**params.N≠实验字母 CF**；亦≠单字母实验 C/F/Y/A/Z；禁 null/holdout/跑后改口；**待预检冻结**；**勿改他字母已冻 Y/G/N/Y2**）；**`params.cf0_primary_demo` 建议 `invent_assume_call_auction_always_fillable`**（禁与 invent_asof_leak_call_auction_always_fillable 双挂；CF1半泄露不得升格并列主报；**待预检冻结**）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- CF0/CF1/CF2 净收益/成本质量、ΔFakeAlwaysFillable、ΔRealizableFill、ΔUnmatchedOrPartial、ΔPxDeviationImpact；分桶（集合竞价可成交性误开 / 核对日泄露 / 开盘集合窗 / 收盘集合窗 / vs A·CE·CD·Y·F·C·D·CA·CB·CC·AR·AG·AN·Z·BA–CE·K·AB·H·W·X·V·U·T·S）。  
- 自检气泡：CF2 是否 pit_by_auction_match_rule；CF0 是否单一主报建议；CF1 是否仅核对日泄露；是否未与 A/CE/CD/Y/F/C/D/CA/CB/CC/AR/AG/AN/Z/BA–CE/K/AB/H/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 CF 与 C 或 F 或 Y 或 A 或 CE 或 CD 或 CA 或 CB 或 CC 或 D 或 B 或 Z 或 K 或 BA–CE 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 CF≠单字母假设-A；CF≠单字母假设-C；CF≠单字母假设-F；CF≠单字母假设-Y；CF≠双字母假设-CE；CF≠双字母假设-CD；CF≠双字母假设-CA；CF≠双字母假设-CB；CF≠双字母假设-CC；params.Y≠实验字母 CF**；**是否未改 Y/Z/AA–CE 冻结补丁正文**；**是否未改假设-A / 假设-CE / 假设-CD / 假设-Y / 假设-C / 假设-F / 假设-D / 假设-CA / 假设-CB / 假设-CC**；**是否未重做预检T**；**是否未复用假设-A / 假设-C / 假设-F / 假设-CD / 假设-CE / 假设-Y**；**是否未与 invent_asof_leak_call_auction_always_fillable 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假全额可成或核对日泄露吹成诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不占本机 8765 席位；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–CE 及其他 A/D–CE 已交正文**；**尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-A；尤其不改假设-Y；尤其不改假设-C；尤其不改假设-F；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC**；**勿再改 CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 执行鸿沟同向：板上枯竭（A）、板上排队（AR）、成交时点与停牌（D）、超涨跌停价无效（AG）、涨停板可成交性误开（CD）、跌停板可成交性误开（CE）、集合量分母（Y）、集合剩单（AN）之外，**回测不得默认「开盘/收盘集合竞价时段订单必能按目标价或参考价全额成交」**；须按当时有效集合竞价撮合约束 PIT。与两融审批/费用族（Z/BA–CC 等）正交，本页不主测两融。与 CD 连续竞价涨停侧、CE 连续竞价跌停侧**正交分列**，本页专测集合竞价时段可成交误开。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 CF** 标准件，**不改口径主线**，**不改假设 A–CE 正文**，**尤其不改假设-CE / 假设-CD / 假设-A / 假设-Y / 假设-C / 假设-F / 假设-CA / 假设-CB / 假设-CC**。与实验 A/CE/CD/Y/F/C/D/CA/CB/CC/AR/AG/AN/Z/BA–CE/K/AB/H/W/X/V/U/T/S 分工：**A=板上枯竭主实验（严禁复用；不抢真数）；CE=跌停板可成交性误开（严禁改）；CD=涨停板可成交性误开（严禁改）；Y=集合量分母（严禁改）；F=涨跌停取整（严禁复用）；C=股票池（严禁复用）；D=开收时点与停牌；CA=维持比分子分母；CB=展期审批；CC=调出了结时限；CF=集合竞价可成交性误开（CF≠A≠CE≠CD≠Y≠F≠C≠D≠CA≠CB≠CC≠B≠Z≠K≠BA≠…≠BZ≠BY≠BF≠BQ≠BC≠BT≠BD≠BL≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AR≠AG≠AN≠AB≠W≠H≠T≠S≠U≠V≠X）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 待入库预检**（结论栏空；**禁止标任何纸面齐**） |
| 标准件路径 | `假设-CF-集合竞价可成交性误开.md` |
| 清单序号 | 约 #89 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**call_auction_fill_honest=pit_by_auction_match_rule 建议**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议占位 0.02/0.01/0.05/0.015（params.Y≠实验字母 CF；params.G≠实验字母 CF；params.N≠实验字母 CF；亦≠单字母实验 C/F/Y/A/Z；禁 null/holdout/跑后改口；待预检冻结；勿改他字母已冻值）**；**cf0_primary_demo 建议 invent_assume_call_auction_always_fillable（禁双挂 invent_asof_leak_call_auction_always_fillable；CF1半泄露不得升格并列主报；待预检冻结）**；锚点建议 call_auction_fill_honest=pit_by_auction_match_rule / call_auction_fill_scope=assume_call_auction_always_fillable_at_target_or_ref / call_auction_fill_over_policy=fail_or_partial_or_fail_missing_match_rule / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **CF≠C/F/CA/CB/CC/CD/CE/A/Y/D/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ/Z/B**（及 ≠BA–CE/K/AB/H/W/T/S/U/V/X），**严禁复用假设-A / 假设-C / 假设-F / 假设-CD / 假设-CE / 假设-Y**；**尤其 CF≠CE（勿撞跌停可成交性）**；**尤其 CF≠CD（勿撞涨停可成交性）**；**尤其 CF≠A（不抢实验A真数队列）**；**尤其不改假设-CE/CD/A/Y/C/F/CA/CB/CC**；**params.Y≠实验字母 CF**；与两融审批/费用类正交 |
| 结论栏 | 空 |

---

## 待预检键清单（建议占位 · 待冻结）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**建议占位·待预检冻结**；**params.Y≠实验字母 CF**；**params.G≠实验字母 CF**；**params.N≠实验字母 CF**；禁 null/holdout；**勿改他字母已冻 Y/G/N/Y2**）  
2. `params.cf0_primary_demo` = `invent_assume_call_auction_always_fillable`（**建议·待预检冻结**；禁与 `invent_asof_leak_call_auction_always_fillable` 双挂；CF1不升格主报）  
3. 锚点（建议写死待预检确认）：`call_auction_fill_honest=pit_by_auction_match_rule` / `call_auction_fill_scope=assume_call_auction_always_fillable_at_target_or_ref` / `call_auction_fill_over_policy=fail_or_partial_or_fail_missing_match_rule` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 新建草稿·待入库预检（总管线：CE 补丁 tip=`ab1ef36` 已交后写 CF；选题集合竞价可成交性误开；**CF≠C/F/CA/CB/CC/CD/CE/A/Y…**；尤其 **CF≠CE（勿撞跌停可成交性）**、**CF≠CD（勿撞涨停可成交性）**、**CF≠A（不抢实验A真数队列）**、**CF≠C**、**CF≠F**、**CF≠Y**；primary_demo 建议=`invent_assume_call_auction_always_fillable`；Y/G/N/Y2 建议占位 `0.02/0.01/0.05/0.015` 待预检；不开回测；未改 CE/CD/A/Y/C/F/CA/CB/CC 及其他已齐字母；**未标纸面齐**）。 |
