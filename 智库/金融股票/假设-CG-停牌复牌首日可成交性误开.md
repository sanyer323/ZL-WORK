# 假设 CG · 停牌复牌首日可成交性误开 / 默认停牌复牌首日订单必能按目标价或开盘价或收盘价全额成交（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CF 补丁已交（tip=`3b769d6`；复检/入库另线并行后写下一纸面 CG）；清单撞题规则另选正交执行缺口（**回测默认「停牌复牌首日订单必能按目标价/开盘价/收盘价全额成交」** ≠ 假设-CF 集合竞价可成交性误开 ≠ 假设-CE 跌停板可成交性误开 ≠ 假设-CD 涨停板可成交性误开 ≠ 假设-A 板上枯竭/一字与封板容量主实验 ≠ 假设-D 成交时点开vs收与停牌假成交（开收时点/停牌期间假成交 ≠ 复牌首日全额可成默认） ≠ 假设-C 股票池当时名单 ≠ 假设-G 市价保护相关（**双字母 CG ≠ 单字母假设-G**） ≠ 假设-CA/CB/CC 两融族）；选题自 `事实与坑`「停牌复牌首日开盘大幅偏离、临时停牌续停与流动性枯竭；回测用目标价/开盘价/收盘价一律全额成交等于假设永远可成」+ 口径「执行鸿沟」+ 与 CD/CE/CF 可成交性族正交；本页**假定板上容量层（A）/ 排队位次层（AR）/ 成交时点与停牌层（D）/ 超涨跌停价无效层（AG）/ 涨停可成交误开层（CD）/ 跌停可成交误开层（CE）/ 集合竞价可成交误开层（CF）诚实或显式旁路**，主病只在**发明「停牌复牌首日订单必能按目标价/开盘价/收盘价全额成交」这一误开默认**；**A 正文主测「涨停可成交性/板上枯竭」真数队列**（**双字母 CG ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 续篇；不抢 A 真数队列**），**CF 正文主测「集合竞价可成交性误开」**（`invent_assume_call_auction_always_fillable`；集合竞价全额可成 ≠ 复牌首日全额可成；**严禁改 CF**），**CE 正文主测「跌停板可成交性误开」**（`invent_assume_limit_down_always_fillable`；跌停全额可卖出 ≠ 复牌首日全额可成；**严禁改 CE**），**CD 正文主测「涨停板可成交性误开」**（`invent_assume_limit_up_always_fillable`；涨停全额可成 ≠ 复牌首日全额可成；**严禁改 CD**），**D 正文主测「成交时点开vs收与停牌假成交」**（开收时点/停牌期间假成交 ≠ 复牌首日全额可成默认；**双字母 CG ≠ 单字母假设-D；严禁复用 D**），**C 正文主测「股票池当时名单」**（**双字母 CG ≠ 单字母假设-C；严禁复用 C**），**G 正文主测市价保护相关**（**双字母 CG ≠ 单字母假设-G；严禁复用 G；且 params.G ≠ 实验字母 CG**），**CA/CB/CC 正文主测两融族**（与本页正交；**严禁改 CA/CB/CC**）→ 自立；与假设 H/B/Z/BA–CF/AG/AF/E/L/F/Y/X/W/K/AB/M/N/AN 等**分列**；**新建实验 CG**  
状态：**草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；禁止把「停牌复牌首日订单必能按目标价/开盘价/收盘价全额成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CF 及其他 A/D–CF 已交正文与冻结补丁；尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-A；尤其不改假设-D；尤其不改假设-C；尤其不改假设-G；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；勿再改 CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CG（约 #90）。与假设 **CF（集合竞价可成交性误开）** **硬分列（专节强调）**：CF = 回测是否默认「**开盘/收盘集合竞价**时段订单必能按目标价或参考价**全额**成交」；本页 = 回测是否默认「**停牌复牌首日**订单必能按目标价/开盘价/收盘价**全额**成交」；集合竞价撮合 ≠ 复牌首日可成交；**严禁复用 CF 题面或 `invent_assume_call_auction_always_fillable`**；**尤其不改假设-CF**。**CG≠CF**。与假设 **CE（跌停板可成交性误开）** **硬分列（专节强调）**：CE = 连续竞价跌停侧全额可卖出误开；本页 = 复牌首日全额可成误开；**严禁复用 CE 题面或 `invent_assume_limit_down_always_fillable`**；**尤其不改假设-CE**。**CG≠CE**。与假设 **CD（涨停板可成交性误开）** **硬分列（专节强调）**：CD = 连续竞价涨停侧全额可成误开；本页 = 复牌首日全额可成误开；**严禁复用 CD 题面或 `invent_assume_limit_up_always_fillable`**；**尤其不改假设-CD**。**CG≠CD**。与假设 **A（涨停可成交性/板上枯竭）** **硬分列（专节强调）**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成的**主实验与真数队列**；本页 = **纸面机制误开点**：回测/仿真是否默认发明「停牌复牌首日订单必能按目标价/开盘价/收盘价全额成交」并系统性高估复牌日可实现成交、低估开盘大幅偏离、临时停牌续停与流动性枯竭；容量门槛 ≠ 复牌首日全额可成默认；**双字母 CG ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不占** A 的 A0/A1 主报与真数席位；**尤其不改假设-A**。**CG≠A**。与假设 **D（成交时点与停牌）** **硬分列（专节强调）**：D = 开 vs 收成交时点与停牌期间假成交；本页 = 复牌首日是否仍按目标价/开盘价/收盘价**全额**记成；开收时点/停牌假成交 ≠ 复牌首日全额可成；**双字母 CG ≠ 单字母假设-D**；**严禁复用 D 题面**；**尤其不改假设-D**。**CG≠D**。与假设 **C（股票池当时名单）** **硬分列**：C = 成分/股票池 PIT；本页 = 复牌首日全额可成误开；**双字母 CG ≠ 单字母假设-C**；**严禁复用 C**。**CG≠C**。与假设 **G（市价保护相关）** **硬分列**：G = 市价保护相关；本页 = 复牌首日全额可成误开；**双字母 CG ≠ 单字母假设-G**；**严禁复用 G**；**且 params.G ≠ 实验字母 CG**。**CG≠G**。与假设 **CA/CB/CC** **硬分列**：两融公式/展期/调出了结时限 ≠ 复牌首日全额可成；**尤其不改 CA/CB/CC**。**CG≠CA≠CB≠CC**。与假设 **AR/AG/AN/M/N/BZ/BY/BX/BW…** 及两融审批/费用族 **硬分列**：假队首/超板无效/集合剩单/收盘机制/收盘假GTC/两融审批费用 ≠ 复牌首日全额可成默认。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A / 假设-C / 假设-G / 假设-D / 假设-CD / 假设-CE / 假设-CF**。**严禁改写/续写假设-CF / 假设-CE / 假设-CD / 假设-CA / 假设-CB / 假设-CC**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CG** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01；**尤重 params.G ≠ 实验字母 CG**）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 G**（市价保护相关；**严禁复用假设-G**）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **单字母实验 D**（成交时点与停牌；**严禁复用假设-D**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **双字母实验 CB**（融资展期审批；**严禁改写假设-CB**）≠ **双字母实验 CC**（调出强制了结时点；**严禁改写假设-CC**）≠ **双字母实验 CD**（涨停板可成交性误开；**严禁改写假设-CD**）≠ **双字母实验 CE**（跌停板可成交性误开；**严禁改写假设-CE**）≠ **双字母实验 CF**（集合竞价可成交性误开；**严禁改写假设-CF**）≠ **单字母实验 B** ≠ **单字母实验 Z** ≠ **单字母实验 K** ≠ **单字母实验 Y** ≠ **单字母实验 F** ≠ **单字母实验 E**。全文凡写「实验 CG / 假设-CG / hypothesis_id=CG / 组 CG0·CG1·CG2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CG 混读或互改；**尤其 params.Y ≠ 实验字母 CG ≠ 单字母假设-C ≠ 单字母假设-G ≠ 单字母假设-A ≠ 单字母假设-D ≠ 双字母假设-CA ≠ 双字母假设-CB ≠ 双字母假设-CC ≠ 双字母假设-CD ≠ 双字母假设-CE ≠ 双字母假设-CF**；**尤其 params.G ≠ 实验字母 CG**。亦**禁止**把实验字母 CG 与单字母 **A/B/C/D/E/F/G/Z/K/Y/T/S/U/V/W/X**、双字母 **BA–CF**、双字母 **CA/CB/CC/CD/CE/CF/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `cg0_*` 以外的实验页混读。**双字母 CG ≠ 单字母 C ≠ 单字母 G ≠ 单字母 A ≠ 单字母 D ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 Y ≠ 单字母 F ≠ 单字母 E ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 CC ≠ 双字母 CD ≠ 双字母 CE ≠ 双字母 CF ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 AN ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BF ≠ 双字母 BQ ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 CG**；**params.G ≠ 实验字母 CG**；**params.N ≠ 实验字母 CG**。**带过：双字母 CF ≠ C/F/CA/CB/CC/CD/CE/A/Y…；双字母 CE ≠ C/E/CA/CB/CC/CD/AR…；双字母 CD ≠ A/C/D/CA/CB/CC/AR…；双字母 CC ≠ C/CA/CB/BQ/BY/BZ/BF…；双字母 CB ≠ B/C/CA/BF/BZ…；双字母 CA ≠ A/C/BZ/BY…；双字母 AR ≠ A/R/AQ…；双字母 BZ ≠ Z/BY/BX…；双字母 BY ≠ Y/BX/BW…；双字母 BX ≠ X/BW…；双字母 BW ≠ W/BV…；双字母 BV ≠ V/BU/BT…；双字母 BU ≠ U/BB/BT/K…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BP ≠ P/BO/W；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CG ≠ 单字母假设-A / 假设-C / 假设-G / 假设-D；且 ≠ 假设-CA / 假设-CB / 假设-CC / 假设-CD / 假设-CE / 假设-CF；带过 CF≠CE/CD、CE≠CD、params.Y≠CG、params.G≠CG（硬）

| 维度 | 对照页 | 本页假设-CG（双字母） |
|------|--------|----------------------|
| 题面 CF | **集合竞价可成交性误开**（`invent_assume_call_auction_always_fillable`；开盘/收盘集合竞价全额可成） | **停牌复牌首日可成交性误开**：默认「复牌首日订单必能按目标价/开盘价/收盘价全额成交」vs 诚实复牌日可成交约束；集合竞价 ≠ 复牌首日；**严禁复用 CF 题面**；**CG≠CF**；**不改 CF** |
| 题面 CE | **跌停板可成交性误开**（`invent_assume_limit_down_always_fillable`；连续竞价跌停侧） | 连续竞价跌停侧 ≠ 复牌首日全额可成；**严禁复用 CE 题面**；**CG≠CE**；**不改 CE** |
| 题面 CD | **涨停板可成交性误开**（`invent_assume_limit_up_always_fillable`；连续竞价涨停侧） | 连续竞价涨停侧 ≠ 复牌首日全额可成；**严禁复用 CD 题面**；**CG≠CD**；**不改 CD** |
| 题面 A | **涨停可成交性/板上枯竭**（清单实验 A；真数队列） | 容量门槛 ≠ 复牌首日全额可成默认；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不抢 A 真数队列**；**CG≠A** |
| 题面 D | **成交时点开vs收与停牌假成交**（清单实验 D） | 开收时点/停牌假成交 ≠ 复牌首日全额可成；**严禁复用 D**；**CG≠D**；**不改 D** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 股票池 ≠ 复牌首日全额可成；**严禁复用 C**；**CG≠C** |
| 题面 G | **市价保护相关**（清单实验 G） | 市价保护 ≠ 复牌首日全额可成；**严禁复用 G**；**CG≠G**；**params.G≠实验字母CG** |
| 题面 CA | **维持担保比例分子分母口径** | 公式 ≠ 复牌首日全额可成；**CG≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批** | 展期审批 ≠ 复牌首日全额可成；**CG≠CB**；**不改 CB** |
| 题面 CC | **两融标的调出强制了结时点** | 调出了结时限 ≠ 复牌首日全额可成；**CG≠CC**；**不改 CC** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_assume_resume_from_halt_always_fillable`（已冻结） |
| 文档 | 清单实验 A / C / G / D / `假设-CA-…` / `假设-CB-…` / `假设-CC-…` / `假设-CD-…` / `假设-CE-…` / `假设-CF-…`（**只读；禁止改写**） | `假设-CG-停牌复牌首日可成交性误开.md`（新建） |
| 预检键 | 实验字母 A / C / G / D / CA / CB / CC / CD / CE / CF | 实验字母 **CG** / `cg0_primary_demo`；**不得**占用或改写预检 A/C/G/D/CA/CB/CC/CD/CE/CF |

**禁止**：把 CG 写成「A/CF/CE/CD/D/C/G/CA/CB/CC 的续篇」；把「板上容量已诚实（A）/ 集合竞价可成交已诚实（CF）/ 跌停可成交已诚实（CE）/ 涨停可成交已诚实（CD）/ 开收时点/停牌已诚实（D）/ 股票池已诚实（C）/ 市价保护已诚实（G）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「停牌复牌首日可成交性已诚实」；覆盖或补丁改写假设-A / 假设-CF / 假设-CE / 假设-CD / 假设-D / 假设-C / 假设-G / 假设-CA / 假设-CB / 假设-CC 正文；把 `params.Y/G/N` 与实验字母 CG 混读；**禁** `cg0_primary_demo` 与 `invent_asof_leak_resume_from_halt_always_fillable` **双挂主报**；**禁** CG1 半泄露升格并列主报；**禁**复用假设-A / 假设-C / 假设-G / 假设-D / 假设-CD / 假设-CE / 假设-CF 题面或口径键；**禁**复用 CF/CE/CD/D/CA/CB/CC 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有路径、同一未复权价、同一 T+1、同一板上容量/排队位次/成交时点与停牌/涨跌停可成交/集合竞价可成交等输入（A/AR/D/CD/CE/CF 层诚实或显式旁路声明「本页不重开板上容量门槛/假队首/开收时点与停牌期间假成交/连续竞价涨跌停全额可成/集合竞价全额可成」）下，把「停牌复牌首日订单必能按目标价/开盘价/收盘价全额成交」或「全样本用核对日当天更宽『复牌首日一律全额可成』规则回放历史」当成默认，相对「每个交易日按当时有效复牌首日可成交约束 PIT（开盘大幅偏离按参考偏离计；临时停牌续停记未成/部分成交；流动性枯竭按事先写死的复牌日撮合/容量规则或记未成；缺字段 skip/敏感性；不抢 A 真数席位）」的诚实组，会**系统性发明假全额可成路径并高估复牌日可实现成交、低估开盘大幅偏离、临时停牌续停与流动性枯竭**；差异应**集中在停牌复牌首日可成交性误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、开盘偏离冲击差、续停/枯竭失败差在标定噪声带内可忽略，且「假全额可成 / 核对日泄露 / 普通复牌窗 / 临停续停窗 / vs A·CF·CE·CD·D·C·G·CA·CB·CC·AR·AG·AN·H·W·X·K·AB·T·S·U·V」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 与 cg0 与锚 三条已冻）

```
# 配置写死键（见 §7；三条已冻 · 待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CG；≠ 单字母假设-C；≠ 单字母假设-G；≠ 单字母假设-A；≠ 单字母假设-D；≠ 双字母假设-CA/CB/CC/CD/CE/CF
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CG；尤重 params.G ≠ 实验字母 CG ≠ 单字母假设-G
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CG；≠ 单字母假设-N；亦≠实验字母 BN
# params.fill_time 写死 next_open
# params.asof_check_date 写死 2026-10-16
# params.px_basis 写死 unadj
# params.resume_halt_fill_honest 写死 pit_by_resume_fill_rule
# params.resume_halt_fill_scope 写死 assume_resume_from_halt_always_fillable_at_target_or_open_or_close
# params.resume_halt_fill_over_policy 写死 fail_or_partial_or_fail_missing_resume_rule
# params.board_capacity_handoff 写死 a_page     # 板上容量/枯竭交 A；CG≠A；严禁复用假设-A；不抢 A 真数
# params.queue_handoff 写死 ar_page    # 排队假队首交 AR；CG≠AR；不改 AR
# params.fill_time_suspend_handoff 写死 d_page     # 开收时点与停牌交 D；CG≠D；严禁复用假设-D（本页主病≠D开收/停牌期间假成交）
# params.beyond_limit_handoff 写死 ag_page    # 超涨跌停价无效交 AG；CG≠AG
# params.limit_up_fill_handoff 写死 cd_page    # 涨停可成交误开交 CD；CG≠CD；不改 CD
# params.limit_down_fill_handoff 写死 ce_page    # 跌停可成交误开交 CE；CG≠CE；不改 CE
# params.call_auction_fill_handoff 写死 cf_page    # 集合竞价可成交误开交 CF；CG≠CF；不改 CF
# params.auction_vol_handoff 写死 y_page
# params.auction_leftover_handoff 写死 an_page
# params.lot_size_handoff 写死 e_page
# params.limit_round_handoff 写死 f_page
# params.mkt_protect_handoff 写死 g_page     # 市价保护交 G；CG≠G；严禁复用假设-G
# params.universe_pool_handoff 写死 c_page     # 股票池交 C；CG≠C；严禁复用假设-C
# params.maint_ratio_formula_handoff 写死 ca_page    # 维持比分子分母交 CA；CG≠CA；不改 CA
# params.financing_rollover_handoff 写死 cb_page    # 展期审批交 CB；CG≠CB；不改 CB
# params.delist_force_deadline_handoff 写死 cc_page    # 调出了结时限交 CC；CG≠CC；不改 CC
# params.resume_halt_fill_handoff 写死 self       # 本页主病：停牌复牌首日可成交性误开（全额可成默认）
# params.exright_board_handoff 写死 w_page
# params.st_limit_handoff 写死 x_page
# params.shortable_list_handoff 写死 k_page
# params.short_px_handoff 写死 ab_page
# params.stamp_tax_handoff 写死 v_page
# params.transfer_fee_handoff 写死 u_page
# params.csrc_fee_handoff 写死 t_page
# params.handling_fee_handoff 写死 s_page
# params.exit_period_handoff 写死 h_page
# params.cg0_primary_demo                写死冻结 invent_assume_resume_from_halt_always_fillable  # 主报：假全额可成；禁与 invent_asof_leak_resume_from_halt_always_fillable 双挂争主表；CG1半泄露不得升格并列主报
# params.cg0_invent_assume_resume_from_halt_always_fillable 写死 True
# params.cg1_asof_leak_resume_from_halt_always_fillable_only 写死 True
# params.cg2_pit_resume_halt_fill 写死 True
# params.merge_with_A_fill 写死 False  # CG≠A；严禁复用假设-A
# params.merge_with_AR_queue 写死 False  # CG≠AR；不改 AR
# params.merge_with_D_fill_time 写死 False  # CG≠D；严禁复用假设-D
# params.merge_with_C_universe_pool 写死 False  # CG≠C；严禁复用假设-C
# params.merge_with_G_mkt_protect 写死 False  # CG≠G；严禁复用假设-G
# params.merge_with_CA_maint_ratio_formula 写死 False  # CG≠CA；不改 CA
# params.merge_with_CB_financing_rollover 写死 False  # CG≠CB；不改 CB
# params.merge_with_CC_delist_force_deadline 写死 False  # CG≠CC；不改 CC
# params.merge_with_CD_limit_up_fill 写死 False  # CG≠CD；不改 CD
# params.merge_with_CE_limit_down_fill 写死 False  # CG≠CE；不改 CE
# params.merge_with_CF_call_auction_fill 写死 False  # CG≠CF；不改 CF
# params.merge_with_AG_beyond_limit 写死 False
# params.merge_with_B_legacy 写死 False  # CG≠B
# params.merge_with_Z_margin_ratio 写死 False  # 与两融审批/费用类正交
# params.merge_with_BA_margin_buy_list 写死 False
# params.merge_with_BB_refinance_borrow 写死 False
# params.merge_with_BC_maint_force 写死 False
# params.merge_with_BD_haircut 写死 False
# params.merge_with_BE_balance_pause 写死 False
# params.merge_with_BF_contract_term 写死 False
# params.merge_with_BG_collateral_list 写死 False
# params.merge_with_BH_credit_quota 写死 False
# params.merge_with_BI_short_proceeds 写死 False
# params.merge_with_BJ_financing_sale_repay 写死 False
# params.merge_with_BK_client_conc 写死 False
# params.merge_with_BL_collateral_withdraw 写死 False
# params.merge_with_BM_margin_call_open_ban 写死 False
# params.merge_with_BN_cross_account 写死 False
# params.merge_with_BO_financing_interest 写死 False
# params.merge_with_BP_corp_action_comp 写死 False
# params.merge_with_BQ_list_removal_stock 写死 False
# params.merge_with_BR_short_borrow_fee 写死 False
# params.merge_with_BS_financing_rate_tier 写死 False
# params.merge_with_BT_force_close_order 写死 False
# params.merge_with_BU_daily_short_inventory 写死 False
# params.merge_with_BV_short_recall 写死 False
# params.merge_with_BW_credit_usage 写死 False
# params.merge_with_BX_interest_start_daycount 写死 False
# params.merge_with_BY_margin_call_grace 写死 False
# params.merge_with_BZ_early_repay_fee 写死 False
# params.merge_with_K_shortable_list 写死 False
# params.merge_with_AB_short_px 写死 False
# params.merge_with_Y_auction_vol 写死 False
# params.merge_with_AN_auction_leftover 写死 False
# params.merge_with_W_exright 写死 False
# params.merge_with_H_exit 写死 False
# params.merge_with_N_close_gtc 写死 False
# params.merge_with_M_aft 写死 False
# params.missing_resume_halt_fill_policy 写死 skip
# params.day_freq_proxy 写死 resume_halt_fill_sensitivity
# params.universe_rule 写死 sse_szse_resume_halt_fill_misopen_check
# params.fail_policy 写死 skip
# params.redline_v0_exempt_scope 写死 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母CG；params.G≠实验字母CG；params.N≠实验字母CG；亦≠单字母实验C/G/A/D/Z；禁 null/holdout/跑后改口；勿改他字母已冻 Y/G/N/Y2
# params.date_start / date_end 写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改复牌首日可成交误开口径、Y/G/N/Y2、主窗/oos、cg0_primary_demo
```

可编码摘要（伪代码，不开跑）：

```
asof = params.asof_check_date  # 2026-10-16
# CG0：假全额可成——停牌复牌首日订单按目标价/开盘价/收盘价 100% 成交
# CG1：仅 asof 日更宽「复牌首日一律全额可成」规则泄露铺满
# CG2：每个交易日 d 按当日已生效复牌首日可成交约束 PIT（消费 A/AR/D/CD/CE/CF 诚实或旁路）
# 缺复牌约束字段 → skip（params.missing_resume_halt_fill_policy）
```

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
resume_halt_fill_honest = "pit_by_resume_fill_rule"
resume_halt_fill_scope = "assume_resume_from_halt_always_fillable_at_target_or_open_or_close"
resume_halt_fill_over_policy = "fail_or_partial_or_fail_missing_resume_rule"
cg0_primary_demo = "invent_assume_resume_from_halt_always_fillable"  # 单一主报·已冻结；禁与 invent_asof_leak_resume_from_halt_always_fillable 双挂
cg0_invent_assume_resume_from_halt_always_fillable = True
cg1_asof_leak_resume_from_halt_always_fillable_only = True
cg2_pit_resume_halt_fill = True
merge_with_A_fill = False
merge_with_AR_queue = False
merge_with_D_fill_time = False
merge_with_C_universe_pool = False
merge_with_G_mkt_protect = False
merge_with_CA_maint_ratio_formula = False
merge_with_CB_financing_rollover = False
merge_with_CC_delist_force_deadline = False
merge_with_CD_limit_up_fill = False
merge_with_CE_limit_down_fill = False
merge_with_CF_call_auction_fill = False
fail_policy = "skip"
```

### 2.2 三组对照（CG0 / CG1 / CG2）

| 组 | 口径 | 说明 |
|----|------|------|
| CG0 天真 | `invent_assume_resume_from_halt_always_fillable`（单一主报·已冻结） | 发明假全额可成路径；禁与 invent_asof_leak_resume_from_halt_always_fillable 双挂 |
| CG1 半泄露·混口径 | 全样本用 `asof_check_date` 当天更宽「复牌首日一律全额可成」规则铺满历史 | 仅复牌首日全额可成 asof 泄露；不升格并列主报 |
| CG2 PIT | `resume_halt_fill_honest=pit_by_resume_fill_rule` | 每个交易日按当时已生效复牌首日可成交约束 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：停牌复牌首日标签代理 + 目标价/开盘价/收盘价全额成交默认 vs 诚实开盘偏离/临停续停/流动性枯竭 → 当日可实现成交与失败笔；缺字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有未复权 OHLC + 停牌/复牌标签代理 + 成交意图代理即可纸面起步；**本页不开回测、不拉真数、不派回测岗、不抢 A 真数队列**。

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

天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、开盘偏离冲击差、续停/枯竭失败差超出标定噪声带，且差异集中在「停牌复牌首日可成交性误开」桶，不被 A 板上容量、CF 集合竞价、CE 跌停可成交、CD 涨停可成交、D 开收时点/停牌、C 股票池、G 市价保护、CA/CB/CC 两融族等他页桶吞并。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 A/CF/CE/CD/D/C/G/CA/CB/CC/AR/AG/AN/T 等他页桶吞并；或 holdout 反调 `cg0_primary_demo` / Y·G·N·Y2；或 CG0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CG0 / CG1 / CG2。报告可实现成交差、假全额可成贡献差、开盘偏离冲击差、续停/枯竭失败差。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_assume_resume_from_halt_always_fillable",
  "invent_asof_leak_resume_from_halt_always_fillable",
  "ordinary_resume_window",
  "temp_halt_rehalt_window",
  "vs_A_limit_up_fill",
  "vs_CF_call_auction_fill",
  "vs_CE_limit_down_fill",
  "vs_CD_limit_up_fill",
  "vs_D_fill_time_suspend",
  "vs_C_universe_pool",
  "vs_G_mkt_protect",
  "vs_AR_queue_front",
  "vs_CA_maint_ratio_formula",
  "vs_CB_financing_rollover",
  "vs_CC_delist_force_deadline",
  "vs_AG_beyond_limit",
  "vs_Y_auction_vol",
  "vs_AN_auction_leftover",
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

1. 样本无足够停牌复牌首日窗/复牌可成交约束字段；缺字段却静默当假全额可成 → 设计失效。  
2. 把「板上容量已诚实（A）」静默写成「停牌复牌首日可成交性已诚实」且不声明另页 A → **与 A 撞题**（**尤其 CG≠A**；**严禁复用假设-A**；**绝不可做成 A 续篇**；**不抢 A 真数队列**）。  
3. 把「集合竞价可成交已诚实（CF）」静默写成「停牌复牌首日可成交性已诚实」 → **与 CF 撞题**（集合竞价 ≠ 复牌首日；**尤其 CG≠CF**；**不改 CF**）。  
4. 把「跌停可成交已诚实（CE）」静默写成「停牌复牌首日可成交性已诚实」 → **与 CE 撞题**（**尤其 CG≠CE**；**不改 CE**）。  
5. 把「涨停可成交已诚实（CD）」静默写成「停牌复牌首日可成交性已诚实」 → **与 CD 撞题**（**尤其 CG≠CD**；**不改 CD**）。  
6. 把「开收时点/停牌已诚实（D）」静默写成「停牌复牌首日可成交性已诚实」 → **与 D 撞题**（开收时点/停牌期间假成交 ≠ 复牌首日全额可成；**尤其 CG≠D**；**严禁复用假设-D**）。  
7. 把「股票池已诚实（C）」静默写成「停牌复牌首日可成交性已诚实」 → **与 C 撞题**（**尤其 CG≠C**；**严禁复用假设-C**）。  
8. 把「市价保护已诚实（G）」静默写成「停牌复牌首日可成交性已诚实」 → **与 G 撞题**（**尤其 CG≠G**；**严禁复用假设-G**；**params.G≠实验字母CG**）。  
9. 把「分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「停牌复牌首日可成交性已诚实」 → **与 CA/CB/CC 撞题**（与两融审批/费用类正交；**尤其 CG≠CA / CG≠CB / CG≠CC**；**不改 CA/CB/CC**）。  
10. 把「集合剩单/超板无效/整手/单笔上限/集合量分母已诚实」写成主病或不声明另页 → 与 AN/AG/E/AF/Y 撞题。  
11. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「停牌复牌首日可成交性已诚实」→ 与交易所费用族撞题（**明确避开预检T**）。  
12. 把实验字母 CG 与单字母 A/B/C/D/E/F/G/Z/K/Y/T/S/U/V/W/X 或双字母 BA–CF/CA/CB/CC/CD/CE/CF/AR/AG/AN/BZ/BY/BF/BQ/BC/BT/BD/BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
13. holdout 反调 `cg0_primary_demo` / Y·G·N·Y2 → 结论无效。  
14. 用复权价代理复牌首日可成交路径 → 标签与执行双错，结论无效。  
15. 用核对日更宽「假全额可成」当诚实 PIT、或把临时宽口径铺满历史 → 设计失效。  
16. **`cg0_primary_demo` 与 `invent_asof_leak_resume_from_halt_always_fillable` 双挂主报**；或 CG1 升格并列主报 → 设计失效。  
17. **改写或覆盖 `假设-A` / `假设-CF` / `假设-CE` / `假设-CD` / `假设-D` / `假设-C` / `假设-G` / `假设-CA` / `假设-CB` / `假设-CC` / 已冻 AA–CF** → 硬边界违约，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块、停牌/复牌首日标签代理；  
- 成交意图量、目标价/开盘价/收盘价全额成交默认 vs 诚实开盘偏离/临停续停/流动性枯竭规则及生效日；  
- 板上容量 / 排队位次 / 开收时点与停牌 / 涨跌停可成交误开 / 集合竞价可成交误开输入（消费 A/AR/D/CD/CE/CF 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历。

可选：普通复牌 vs 临停续停分段；与 A 容量窗、CF 集合竞价窗、CE/CD 涨跌停窗、D 开收/停牌窗对照但不混主结论；缺复牌约束原因码敏感性（主报仍在停牌复牌首日可成交性误开）。

**禁止**：用核对日「今天复牌首日一律全额可成」铺满当唯一诚实组；用复权价；把板上容量已诚实/集合竞价可成交已诚实/跌停可成交已诚实/涨停可成交已诚实/开收时点已诚实/股票池已诚实/市价保护已诚实/两融审批费用已诚实当成「停牌复牌首日可成交性正确」依据；把 A/CF/CE/CD/D/C/G/CA/CB/CC/AR/AG/AN/Z/BA–CF/K/AB/H/W/X/V/U/T/S 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`CG`  
- **组**：CG0 / CG1 / CG2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`resume_halt_fill_honest=pit_by_resume_fill_rule`（写死）；`resume_halt_fill_scope=assume_resume_from_halt_always_fillable_at_target_or_open_or_close`（写死）；`resume_halt_fill_over_policy=fail_or_partial_or_fail_missing_resume_rule`（写死）；`board_capacity_handoff=a_page`；`queue_handoff=ar_page`；`fill_time_suspend_handoff=d_page`；`beyond_limit_handoff=ag_page`；`limit_up_fill_handoff=cd_page`；`limit_down_fill_handoff=ce_page`；`call_auction_fill_handoff=cf_page`；`mkt_protect_handoff=g_page`；`universe_pool_handoff=c_page`；`maint_ratio_formula_handoff=ca_page`；`financing_rollover_handoff=cb_page`；`delist_force_deadline_handoff=cc_page`；其余 handoff 见 §2.1；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_resume_halt_fill_misopen_check`；`missing_resume_halt_fill_policy=skip`；`day_freq_proxy=resume_halt_fill_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 CG**；**params.G≠实验字母 CG**；**params.N≠实验字母 CG**；亦≠单字母实验 C/G/A/D/Z；禁 null/holdout/跑后改口；**勿改他字母已冻 Y/G/N/Y2**）；**`params.cg0_primary_demo` 写死冻结 `invent_assume_resume_from_halt_always_fillable`**（禁与 invent_asof_leak_resume_from_halt_always_fillable 双挂；CG1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- CG0/CG1/CG2 净收益/成本质量、ΔFakeAlwaysFillable、ΔRealizableFill、ΔOpenDeviationImpact、ΔRehaltOrDryFail；分桶（停牌复牌首日可成交性误开 / 核对日泄露 / 普通复牌窗 / 临停续停窗 / vs A·CF·CE·CD·D·C·G·CA·CB·CC·AR·AG·AN·Z·BA–CF·K·AB·H·W·X·V·U·T·S）。  
- 自检气泡：CG2 是否 pit_by_resume_fill_rule；CG0 是否单一主报已冻；CG1 是否仅核对日泄露；是否未与 A/CF/CE/CD/D/C/G/CA/CB/CC/AR/AG/AN/Z/BA–CF/K/AB/H/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 CG 与 C 或 G 或 A 或 D 或 CF 或 CE 或 CD 或 CA 或 CB 或 CC 或 B 或 Z 或 K 或 BA–CF 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 CG≠单字母假设-A；CG≠单字母假设-C；CG≠单字母假设-G；CG≠单字母假设-D；CG≠双字母假设-CF；CG≠双字母假设-CE；CG≠双字母假设-CD；CG≠双字母假设-CA；CG≠双字母假设-CB；CG≠双字母假设-CC；params.Y≠实验字母 CG；params.G≠实验字母 CG**；**是否未改 Y/Z/AA–CF 冻结补丁正文**；**是否未改假设-A / 假设-CF / 假设-CE / 假设-CD / 假设-D / 假设-C / 假设-G / 假设-CA / 假设-CB / 假设-CC**；**是否未重做预检T**；**是否未复用假设-A / 假设-C / 假设-G / 假设-D / 假设-CD / 假设-CE / 假设-CF**；**是否未与 invent_asof_leak_resume_from_halt_always_fillable 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假全额可成或核对日泄露吹成诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不占本机 8765 席位；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–CF 及其他 A/D–CF 已交正文**；**尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-A；尤其不改假设-D；尤其不改假设-C；尤其不改假设-G；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC**；**勿再改 CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 执行鸿沟同向：板上枯竭（A）、板上排队（AR）、成交时点与停牌（D）、超涨跌停价无效（AG）、涨停板可成交性误开（CD）、跌停板可成交性误开（CE）、集合竞价可成交性误开（CF）之外，**回测不得默认「停牌复牌首日订单必能按目标价/开盘价/收盘价全额成交」**；须按当时有效复牌首日可成交约束 PIT。与两融审批/费用族（Z/BA–CC 等）正交，本页不主测两融。与 CD 连续竞价涨停侧、CE 连续竞价跌停侧、CF 集合竞价时段**正交分列**，本页专测停牌复牌首日可成交误开。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 CG** 标准件，**不改口径主线**，**不改假设 A–CF 正文**，**尤其不改假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-D / 假设-C / 假设-G / 假设-CA / 假设-CB / 假设-CC**。与实验 A/CF/CE/CD/D/C/G/CA/CB/CC/AR/AG/AN/Z/BA–CF/K/AB/H/W/X/V/U/T/S 分工：**A=板上枯竭主实验（严禁复用；不抢真数）；CF=集合竞价可成交性误开（严禁改）；CE=跌停板可成交性误开（严禁改）；CD=涨停板可成交性误开（严禁改）；D=开收时点与停牌；C=股票池；G=市价保护；CA=维持比分子分母；CB=展期审批；CC=调出了结时限；CG=停牌复牌首日可成交性误开（CG≠A≠CF≠CE≠CD≠D≠C≠G≠CA≠CB≠CC≠B≠Z≠K≠BA≠…≠BZ≠BY≠BF≠BQ≠BC≠BT≠BD≠BL≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AR≠AG≠AN≠AB≠W≠H≠T≠S≠U≠V≠X）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；**禁止标任何纸面齐**） |
| 标准件路径 | `假设-CG-停牌复牌首日可成交性误开.md` |
| 清单序号 | 约 #90 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**resume_halt_fill_honest=pit_by_resume_fill_rule 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 CG；params.G≠实验字母 CG；params.N≠实验字母 CG；亦≠单字母实验 C/G/A/D/Z；禁 null/holdout/跑后改口；勿改他字母已冻值）**；**cg0_primary_demo 写死冻结 invent_assume_resume_from_halt_always_fillable（禁双挂 invent_asof_leak_resume_from_halt_always_fillable；CG1半泄露不得升格并列主报）**；锚点写死 resume_halt_fill_honest=pit_by_resume_fill_rule / resume_halt_fill_scope=assume_resume_from_halt_always_fillable_at_target_or_open_or_close / resume_halt_fill_over_policy=fail_or_partial_or_fail_missing_resume_rule / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **CG≠C/G/CA/CB/CC/CD/CE/CF/A/D/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ/Z/B**（及 ≠BA–CF/K/AB/H/W/T/S/U/V/X/Y/F/E），**严禁复用假设-A / 假设-C / 假设-G / 假设-D / 假设-CD / 假设-CE / 假设-CF**；**尤其 CG≠CF（勿撞集合竞价可成交性）**；**尤其 CG≠CE（勿撞跌停可成交性）**；**尤其 CG≠CD（勿撞涨停可成交性）**；**尤其 CG≠A（不抢实验A真数队列）**；**尤其 CG≠D（开收时点/停牌 ≠ 复牌首日全额可成）**；**尤其 CG≠C / CG≠G**；**尤其不改假设-CF/CE/CD/A/D/C/G/CA/CB/CC**；**params.Y≠实验字母 CG**；**params.G≠实验字母 CG**；与两融审批/费用类正交 |
| 结论栏 | 空 |

---

## 待预检键清单（三条已冻 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已冻结**；**params.Y≠实验字母 CG**；**params.G≠实验字母 CG**；**params.N≠实验字母 CG**；禁 null/holdout；**勿改他字母已冻 Y/G/N/Y2**）  
2. `params.cg0_primary_demo` = `invent_assume_resume_from_halt_always_fillable`（**已冻结**；禁与 `invent_asof_leak_resume_from_halt_always_fillable` 双挂；CG1不升格主报）  
3. 锚点（**已升格写死**）：`resume_halt_fill_honest=pit_by_resume_fill_rule` / `resume_halt_fill_scope=assume_resume_from_halt_always_fillable_at_target_or_open_or_close` / `resume_halt_fill_over_policy=fail_or_partial_or_fail_missing_resume_rule` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`

## 风控预检补丁·冻结（三条已写死 · 2026-11-04）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 CG**；**`params.G` ≠ 实验字母 CG**；**`params.N` ≠ 实验字母 CG**；**`params.Y` ≠ 单字母实验 C/G/A/D/Z**；尤重**双字母 CG ≠ 单字母假设-A**；**双字母 CG ≠ 单字母假设-C**；**双字母 CG ≠ 单字母假设-G**；**双字母 CG ≠ 单字母假设-D**；**双字母 CG ≠ 双字母假设-CA**；**双字母 CG ≠ 双字母假设-CB**；**双字母 CG ≠ 双字母假设-CC**；**双字母 CG ≠ 双字母假设-CD**；**双字母 CG ≠ 双字母假设-CE**；**双字母 CG ≠ 双字母假设-CF**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.cg0_primary_demo`**：**写死冻结** **`invent_assume_resume_from_halt_always_fillable`**；禁与 **`invent_asof_leak_resume_from_halt_always_fillable`** 双挂争主表（只挂一个 primary）；**CG1 半泄露不得升格并列主报**。  
3. **停牌复牌首日可成交性锚升格写死（不可再写「建议」）**：`params.resume_halt_fill_honest=pit_by_resume_fill_rule`；`params.resume_halt_fill_scope=assume_resume_from_halt_always_fillable_at_target_or_open_or_close`；`params.resume_halt_fill_over_policy=fail_or_partial_or_fail_missing_resume_rule`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有停牌复牌首日可成交相关锚点；不改口）。

**硬分列保留**：CG≠C/G/CA/CB/CC/CD/CE/CF/A/D/AR/AG…；**尤其 CG≠CF / CG≠CE / CG≠CD / CG≠A / CG≠D**；**严禁复用假设-C / 假设-G / 假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-D**；**params.Y/G/N ≠ 实验字母 CG**。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 风控预检补丁·冻结三条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CG**；**params.G≠实验字母 CG**；**params.N≠实验字母 CG**；亦≠单字母实验 C/G/A/D/Z；尤重**双字母 CG ≠ 单字母假设-A**；**双字母 CG ≠ 单字母假设-C**；**双字母 CG ≠ 单字母假设-G**；**双字母 CG ≠ 单字母假设-D**；**双字母 CG ≠ 双字母假设-CF/CE/CD/CA/CB/CC**；禁 null/holdout/跑后改口）；② `params.cg0_primary_demo=invent_assume_resume_from_halt_always_fillable`（禁与 `invent_asof_leak_resume_from_halt_always_fillable` 双挂争主表；CG1半泄露不得升格并列主报）；③ 锚升格写死：`resume_halt_fill_honest=pit_by_resume_fill_rule`；`resume_halt_fill_scope=assume_resume_from_halt_always_fillable_at_target_or_open_or_close`；`resume_halt_fill_over_policy=fail_or_partial_or_fail_missing_resume_rule`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。硬分列保留：**CG≠C/G/CA/CB/CC/CD/CE/CF/A/D…**；**尤其 CG≠CF（勿撞集合竞价可成交性）**；**尤其 CG≠CE（勿撞跌停可成交性）**；**尤其 CG≠CD（勿撞涨停可成交性）**；**尤其 CG≠A（不抢实验A真数队列）**；**尤其 CG≠D**；**严禁复用假设-C / 假设-G / 假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-D**；参考总管派令 / 风控预检有条件通过（草稿 tip=`084290f`；基线叠至 `d75f333`；清单 #90）。未改 Y/Z/AA–CF 及其他已冻结补丁；**不改假设-CF**；**不改假设-CE**；**不改假设-CD**；**不改假设-A**；**不改假设-D**；**不改假设-C**；**不改假设-G**；**不改假设-CA**；**不改假设-CB**；**不改假设-CC**；结论栏仍空；不开回测；不催 A；**未标纸面齐**。 |
| 2026-11-04 | 新建草稿·待入库预检（总管线：CF 补丁 tip=`3b769d6` 已交后写 CG；选题停牌复牌首日可成交性误开；**CG≠C/G/CA/CB/CC/CD/CE/CF/A/D…**；尤其 **CG≠CF（勿撞集合竞价可成交性）**、**CG≠CE（勿撞跌停可成交性）**、**CG≠CD（勿撞涨停可成交性）**、**CG≠A（不抢实验A真数队列）**、**CG≠D**、**CG≠C**、**CG≠G**；primary_demo 建议=`invent_assume_resume_from_halt_always_fillable`；Y/G/N/Y2 建议占位 `0.02/0.01/0.05/0.015` 待预检；不开回测；未改 CF/CE/CD/A/D/C/G/CA/CB/CC 及其他已齐字母；**未标纸面齐**）。 |
