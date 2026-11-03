# 假设 CH · 盘后固定价格可成交性误开 / 默认盘后固定价格交易时段订单必能按收盘价或固定价全额成交（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CG 补丁已交（tip=`4e10fef`；复检/入库另线并行后写下一纸面 CH）；清单撞题规则另选正交执行缺口（**回测默认「盘后固定价格交易时段订单必能按收盘价/固定价全额成交」** ≠ 假设-CG 停牌复牌首日可成交性误开 ≠ 假设-CF 集合竞价可成交性误开 ≠ 假设-CE 跌停板可成交性误开 ≠ 假设-CD 涨停板可成交性误开 ≠ 假设-M 盘后补成交/通道是否存在与剩单自动进盘后 ≠ 假设-H 退市整理退出期（**双字母 CH ≠ 单字母假设-H**） ≠ 假设-A 板上枯竭/一字与封板容量主实验 ≠ 假设-D 成交时点开vs收与停牌假成交 ≠ 假设-C 股票池当时名单 ≠ 假设-N 收盘机制/收盘假GTC ≠ 假设-O 大宗量价 ≠ 假设-CA/CB/CC 两融族）；选题自 `事实与坑`「盘后固定价格未匹配/额度限制与次日缺口；回测用收盘价/固定价一律全额成交等于假设永远可成」+ 口径「执行鸿沟」+ 与 CD/CE/CF/CG 可成交性族正交、与 M 通道存在性正交；本页**假定板上容量层（A）/ 排队位次层（AR）/ 成交时点与停牌层（D）/ 超涨跌停价无效层（AG）/ 涨停可成交误开层（CD）/ 跌停可成交误开层（CE）/ 集合竞价可成交误开层（CF）/ 停牌复牌首日可成交误开层（CG）/ 盘后通道存在与自动滚入层（M）诚实或显式旁路**，主病只在**发明「盘后固定价格交易时段订单必能按收盘价/固定价全额成交」这一误开默认**；**A 正文主测「涨停可成交性/板上枯竭」真数队列**（**双字母 CH ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 续篇；不抢 A 真数队列**），**M 正文主测「盘后补成交/通道误套全历史与竞价剩单自动进盘后」**（通道是否存在/扩围切日/自动滚入 ≠ 盘后时段内是否默认全额可成；**严禁改 M**），**H 正文主测「退市整理退出期」**（**双字母 CH ≠ 单字母假设-H；严禁复用 H**），**CG 正文主测「停牌复牌首日可成交性误开」**（`invent_assume_resume_from_halt_always_fillable`；复牌首日全额可成 ≠ 盘后固定价全额可成；**严禁改 CG**），**CF 正文主测「集合竞价可成交性误开」**（`invent_assume_call_auction_always_fillable`；集合竞价全额可成 ≠ 盘后固定价全额可成；**严禁改 CF**），**CE 正文主测「跌停板可成交性误开」**（`invent_assume_limit_down_always_fillable`；跌停全额可卖出 ≠ 盘后固定价全额可成；**严禁改 CE**），**CD 正文主测「涨停板可成交性误开」**（`invent_assume_limit_up_always_fillable`；涨停全额可成 ≠ 盘后固定价全额可成；**严禁改 CD**），**C 正文主测「股票池当时名单」**（**双字母 CH ≠ 单字母假设-C；严禁复用 C**），**CA/CB/CC 正文主测两融族**（与本页正交；**严禁改 CA/CB/CC**）→ 自立；与假设 B/Z/BA–CG/AG/AF/E/L/G/X/W/K/AB/N/O/AN 等**分列**；**新建实验 CH**  
状态：**草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；禁止把「盘后固定价格交易时段订单必能按收盘价/固定价全额成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CG 及其他 A/D–CG 已交正文与冻结补丁；尤其不改假设-CG；尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-M；尤其不改假设-H；尤其不改假设-A；尤其不改假设-C；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；勿再改 CG/CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN/M/N/O**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CH（约 #91）。与假设 **CG（停牌复牌首日可成交性误开）** **硬分列（专节强调）**：CG = 回测是否默认「**停牌复牌首日**订单必能按目标价/开盘价/收盘价**全额**成交」；本页 = 回测是否默认「**盘后固定价格交易时段**订单必能按收盘价/固定价**全额**成交」；复牌首日 ≠ 盘后固定价时段；**严禁复用 CG 题面或 `invent_assume_resume_from_halt_always_fillable`**；**尤其不改假设-CG**。**CH≠CG**。与假设 **CF（集合竞价可成交性误开）** **硬分列（专节强调）**：CF = 开盘/收盘集合竞价全额可成误开；本页 = 盘后固定价全额可成误开；集合撮合 ≠ 盘后固定价撮合；**严禁复用 CF 题面或 `invent_assume_call_auction_always_fillable`**；**尤其不改假设-CF**。**CH≠CF**。与假设 **CE（跌停板可成交性误开）** **硬分列（专节强调）**：CE = 连续竞价跌停侧全额可卖出误开；本页 = 盘后固定价全额可成误开；**严禁复用 CE 题面或 `invent_assume_limit_down_always_fillable`**；**尤其不改假设-CE**。**CH≠CE**。与假设 **CD（涨停板可成交性误开）** **硬分列（专节强调）**：CD = 连续竞价涨停侧全额可成误开；本页 = 盘后固定价全额可成误开；**严禁复用 CD 题面或 `invent_assume_limit_up_always_fillable`**；**尤其不改假设-CD**。**CH≠CD**。与假设 **M（盘后补成交/通道）** **硬分列（专节强调）**：M = 盘后通道是否按切日存在、竞价剩单是否自动滚入盘后、扩围前是否发明通道；本页 = **在通道已诚实存在（或显式旁路声明交 M）的前提下**，是否仍默认「盘后固定价格订单必能按收盘价/固定价全额成交」；通道存在性 ≠ 盘后时段内全额可成；**严禁复用 M 题面**；**尤其不改假设-M**。**CH≠M**。与假设 **H（退市整理退出期）** **硬分列（专节强调）**：H = 退市整理/退出期规则；本页 = 盘后固定价全额可成误开；**双字母 CH ≠ 单字母假设-H**；**严禁复用 H**；**尤其不改假设-H**。**CH≠H**。与假设 **A（涨停可成交性/板上枯竭）** **硬分列（专节强调）**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成的**主实验与真数队列**；本页 = **纸面机制误开点**：回测/仿真是否默认发明「盘后固定价格订单必能按收盘价/固定价全额成交」并系统性高估盘后可实现成交、低估未匹配/额度限制与次日缺口；容量门槛 ≠ 盘后全额可成默认；**双字母 CH ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不占** A 的 A0/A1 主报与真数席位；**尤其不改假设-A**。**CH≠A**。与假设 **C（股票池当时名单）** **硬分列**：C = 成分/股票池 PIT；本页 = 盘后固定价全额可成误开；**双字母 CH ≠ 单字母假设-C**；**严禁复用 C**。**CH≠C**。与假设 **N（收盘机制）/ O（大宗）** **硬分列**：收盘价产生方式/假GTC ≠ 盘后全额可成；大宗量价 ≠ 盘后固定价可成；**尤其不改 N/O**。**CH≠N≠O**。与假设 **CA/CB/CC** **硬分列**：两融公式/展期/调出了结时限 ≠ 盘后固定价全额可成；**尤其不改 CA/CB/CC**。**CH≠CA≠CB≠CC**。与假设 **AR/AG/AN/BZ/BY/BX/BW…** 及两融审批/费用族 **硬分列**：假队首/超板无效/集合剩单/两融审批费用 ≠ 盘后固定价全额可成默认。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A / 假设-C / 假设-H / 假设-M / 假设-CD / 假设-CE / 假设-CF / 假设-CG**。**严禁改写/续写假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-M / 假设-H / 假设-CA / 假设-CB / 假设-CC**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CH** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 H**（退市整理退出期；**严禁复用假设-H**）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **单字母实验 M**（盘后补成交/通道；**严禁改写假设-M**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **双字母实验 CB**（融资展期审批；**严禁改写假设-CB**）≠ **双字母实验 CC**（调出强制了结时点；**严禁改写假设-CC**）≠ **双字母实验 CD**（涨停板可成交性误开；**严禁改写假设-CD**）≠ **双字母实验 CE**（跌停板可成交性误开；**严禁改写假设-CE**）≠ **双字母实验 CF**（集合竞价可成交性误开；**严禁改写假设-CF**）≠ **双字母实验 CG**（停牌复牌首日可成交性误开；**严禁改写假设-CG**）≠ **单字母实验 B** ≠ **单字母实验 Z** ≠ **单字母实验 K** ≠ **单字母实验 D** ≠ **单字母实验 N** ≠ **单字母实验 O**。全文凡写「实验 CH / 假设-CH / hypothesis_id=CH / 组 CH0·CH1·CH2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CH 混读或互改；**尤其 params.Y ≠ 实验字母 CH ≠ 单字母假设-C ≠ 单字母假设-H ≠ 单字母假设-A ≠ 单字母假设-M ≠ 双字母假设-CA ≠ 双字母假设-CB ≠ 双字母假设-CC ≠ 双字母假设-CD ≠ 双字母假设-CE ≠ 双字母假设-CF ≠ 双字母假设-CG**。亦**禁止**把实验字母 CH 与单字母 **A/B/C/D/E/F/G/H/K/M/N/O/T/S/U/V/W/X/Y/Z**、双字母 **BA–CG**、双字母 **CA/CB/CC/CD/CE/CF/CG/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `ch0_*` 以外的实验页混读。**双字母 CH ≠ 单字母 C ≠ 单字母 H ≠ 单字母 A ≠ 单字母 M ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 D ≠ 单字母 N ≠ 单字母 O ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 CC ≠ 双字母 CD ≠ 双字母 CE ≠ 双字母 CF ≠ 双字母 CG ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 AN ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BF ≠ 双字母 BQ ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB**；**params.Y ≠ 实验字母 CH**；**params.G ≠ 实验字母 CH**；**params.N ≠ 实验字母 CH**。**带过：双字母 CG ≠ C/G/CA–CF/A/D…；双字母 CF ≠ C/F/CA–CE/A/Y…；双字母 CE ≠ C/E/CA/CB/CC/CD/AR…；双字母 CD ≠ A/C/D/CA/CB/CC/AR…；双字母 CC ≠ C/CA/CB/BQ/BY/BZ/BF…；双字母 CB ≠ B/C/CA/BF/BZ…；双字母 CA ≠ A/C/BZ/BY…；双字母 AR ≠ A/R/AQ…；双字母 BZ ≠ Z/BY/BX…；双字母 BY ≠ Y/BX/BW…；双字母 BX ≠ X/BW…；双字母 BW ≠ W/BV…；双字母 BV ≠ V/BU/BT…；双字母 BU ≠ U/BB/BT/K…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BP ≠ P/BO/W；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CH ≠ 单字母假设-A / 假设-C / 假设-H / 假设-M；且 ≠ 假设-CA / 假设-CB / 假设-CC / 假设-CD / 假设-CE / 假设-CF / 假设-CG；带过 CG≠CF/CE/CD、params.Y≠CH（硬）

| 维度 | 对照页 | 本页假设-CH（双字母） |
|------|--------|----------------------|
| 题面 CG | **停牌复牌首日可成交性误开**（`invent_assume_resume_from_halt_always_fillable`） | **盘后固定价格可成交性误开**：默认「盘后固定价格订单必能按收盘价/固定价全额成交」vs 诚实盘后撮合/额度约束；复牌首日 ≠ 盘后固定价；**严禁复用 CG 题面**；**CH≠CG**；**不改 CG** |
| 题面 CF | **集合竞价可成交性误开**（`invent_assume_call_auction_always_fillable`） | 集合竞价 ≠ 盘后固定价；**严禁复用 CF 题面**；**CH≠CF**；**不改 CF** |
| 题面 CE | **跌停板可成交性误开**（`invent_assume_limit_down_always_fillable`；连续竞价跌停侧） | 连续竞价跌停侧 ≠ 盘后固定价全额可成；**严禁复用 CE 题面**；**CH≠CE**；**不改 CE** |
| 题面 CD | **涨停板可成交性误开**（`invent_assume_limit_up_always_fillable`；连续竞价涨停侧） | 连续竞价涨停侧 ≠ 盘后固定价全额可成；**严禁复用 CD 题面**；**CH≠CD**；**不改 CD** |
| 题面 M | **盘后补成交/通道误套全历史与剩单自动进盘后** | 通道存在/扩围切日/自动滚入 ≠ 盘后时段内全额可成；**严禁复用 M 题面**；**CH≠M**；**不改 M** |
| 题面 H | **退市整理退出期**（清单实验 H） | 退出期规则 ≠ 盘后全额可成；**双字母 CH ≠ 单字母假设-H**；**严禁复用 H**；**CH≠H**；**不改 H** |
| 题面 A | **涨停可成交性/板上枯竭**（清单实验 A；真数队列） | 容量门槛 ≠ 盘后全额可成默认；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不抢 A 真数队列**；**CH≠A** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 股票池 ≠ 盘后全额可成；**严禁复用 C**；**CH≠C** |
| 题面 N | **收盘机制/收盘假GTC** | 收盘价产生方式 ≠ 盘后全额可成；**CH≠N**；**不改 N** |
| 题面 O | **大宗量价并进竞价** | 大宗 ≠ 盘后固定价可成；**CH≠O**；**不改 O** |
| 题面 CA | **维持担保比例分子分母口径** | 公式 ≠ 盘后全额可成；**CH≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批** | 展期审批 ≠ 盘后全额可成；**CH≠CB**；**不改 CB** |
| 题面 CC | **两融标的调出强制了结时点** | 调出了结时限 ≠ 盘后全额可成；**CH≠CC**；**不改 CC** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_assume_after_hours_fixed_price_always_fillable`（建议主挂；待预检冻结） |
| 文档 | 清单实验 A / C / H / M / N / O / `假设-CA-…` / `假设-CB-…` / `假设-CC-…` / `假设-CD-…` / `假设-CE-…` / `假设-CF-…` / `假设-CG-…`（**只读；禁止改写**） | `假设-CH-盘后固定价格可成交性误开.md`（新建） |
| 预检键 | 实验字母 A / C / H / M / N / O / CA / CB / CC / CD / CE / CF / CG | 实验字母 **CH** / `ch0_primary_demo`；**不得**占用或改写预检 A/C/H/M/N/O/CA/CB/CC/CD/CE/CF/CG |

**禁止**：把 CH 写成「A/CG/CF/CE/CD/M/H/C/N/O/CA/CB/CC 的续篇」；把「板上容量已诚实（A）/ 复牌首日可成交已诚实（CG）/ 集合竞价可成交已诚实（CF）/ 跌停可成交已诚实（CE）/ 涨停可成交已诚实（CD）/ 盘后通道已诚实（M）/ 退出期已诚实（H）/ 股票池已诚实（C）/ 收盘机制已诚实（N）/ 大宗已诚实（O）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「盘后固定价格可成交性已诚实」；覆盖或补丁改写假设-A / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-M / 假设-H / 假设-C / 假设-N / 假设-O / 假设-CA / 假设-CB / 假设-CC 正文；把 `params.Y/G/N` 与实验字母 CH 混读；**禁** `ch0_primary_demo` 与 `invent_asof_leak_after_hours_fixed_price_always_fillable` **双挂主报**；**禁** CH1 半泄露升格并列主报；**禁**复用假设-A / 假设-C / 假设-H / 假设-M / 假设-CD / 假设-CE / 假设-CF / 假设-CG 题面或口径键；**禁**复用 CG/CF/CE/CD/M/H/CA/CB/CC 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有路径、同一未复权价、同一 T+1、同一板上容量/排队位次/成交时点与停牌/涨跌停可成交/集合竞价可成交/复牌首日可成交/盘后通道存在等输入（A/AR/D/CD/CE/CF/CG/M 层诚实或显式旁路声明「本页不重开板上容量门槛/假队首/开收时点与停牌期间假成交/连续竞价涨跌停全额可成/集合竞价全额可成/复牌首日全额可成/盘后通道存在与自动滚入」）下，把「盘后固定价格交易时段订单必能按收盘价/固定价全额成交」或「全样本用核对日当天更宽『盘后固定价格一律全额可成』规则回放历史」当成默认，相对「每个交易日按当时有效盘后固定价格撮合/额度约束 PIT（未匹配记未成/部分成交；额度限制按事先写死规则或记未成；次日缺口单列；缺字段 skip/敏感性；不抢 A 真数席位）」的诚实组，会**系统性发明假全额可成路径并高估盘后可实现成交、低估未匹配/额度限制与次日缺口**；差异应**集中在盘后固定价格可成交性误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、未匹配/额度限制差、次日缺口差在标定噪声带内可忽略，且「假全额可成 / 核对日泄露 / 盘后固定价窗 / vs A·CG·CF·CE·CD·M·H·C·N·O·CA·CB·CC·AR·AG·AN·W·X·K·AB·T·S·U·V」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 与 ch0 与锚 **三条已冻**）

```
# 配置写死键（见 §7；预检有条件通过 · 三条已冻 · 待复检；下列已写死冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CH；≠ 单字母假设-C；≠ 单字母假设-H；≠ 单字母假设-A；≠ 单字母假设-M；≠ 双字母假设-CA/CB/CC/CD/CE/CF/CG
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CH
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CH；≠ 单字母假设-N；亦≠实验字母 BN
# params.fill_time 写死冻结 next_open
# params.asof_check_date 写死冻结 2026-10-16
# params.px_basis 建议 unadj
# params.after_hours_fill_honest 写死冻结 pit_by_aft_fixed_price_fill_rule
# params.after_hours_fill_scope 写死冻结 assume_after_hours_fixed_price_always_fillable_at_close_or_fixed
# params.after_hours_fill_over_policy 写死冻结 fail_or_partial_or_fail_missing_aft_fill_rule
# params.board_capacity_handoff 建议 a_page     # 板上容量/枯竭交 A；CH≠A；严禁复用假设-A；不抢 A 真数
# params.queue_handoff 建议 ar_page    # 排队假队首交 AR；CH≠AR；不改 AR
# params.fill_time_suspend_handoff 建议 d_page     # 开收时点与停牌交 D；CH≠D；严禁复用假设-D
# params.beyond_limit_handoff 建议 ag_page    # 超涨跌停价无效交 AG；CH≠AG
# params.limit_up_fill_handoff 建议 cd_page    # 涨停可成交误开交 CD；CH≠CD；不改 CD
# params.limit_down_fill_handoff 建议 ce_page    # 跌停可成交误开交 CE；CH≠CE；不改 CE
# params.call_auction_fill_handoff 建议 cf_page    # 集合竞价可成交误开交 CF；CH≠CF；不改 CF
# params.resume_halt_fill_handoff 建议 cg_page    # 复牌首日可成交误开交 CG；CH≠CG；不改 CG
# params.aft_channel_handoff 建议 m_page     # 盘后通道存在/自动滚入交 M；CH≠M；不改 M
# params.exit_period_handoff 建议 h_page     # 退市整理退出期交 H；CH≠H；严禁复用假设-H
# params.close_mech_handoff 建议 n_page     # 收盘机制交 N；CH≠N；不改 N
# params.block_trade_handoff 建议 o_page     # 大宗交 O；CH≠O；不改 O
# params.auction_vol_handoff 建议 y_page
# params.auction_leftover_handoff 建议 an_page
# params.lot_size_handoff 建议 e_page
# params.limit_round_handoff 建议 f_page
# params.universe_pool_handoff 建议 c_page     # 股票池交 C；CH≠C；严禁复用假设-C
# params.maint_ratio_formula_handoff 建议 ca_page    # 维持比分子分母交 CA；CH≠CA；不改 CA
# params.financing_rollover_handoff 建议 cb_page    # 展期审批交 CB；CH≠CB；不改 CB
# params.delist_force_deadline_handoff 建议 cc_page    # 调出了结时限交 CC；CH≠CC；不改 CC
# params.after_hours_fill_handoff 建议 self       # 本页主病：盘后固定价格可成交性误开（全额可成默认）
# params.exright_board_handoff 建议 w_page
# params.st_limit_handoff 建议 x_page
# params.shortable_list_handoff 建议 k_page
# params.short_px_handoff 建议 ab_page
# params.stamp_tax_handoff 建议 v_page
# params.transfer_fee_handoff 建议 u_page
# params.csrc_fee_handoff 建议 t_page
# params.handling_fee_handoff 建议 s_page
# params.ch0_primary_demo                写死冻结 invent_assume_after_hours_fixed_price_always_fillable  # 主报：假全额可成；禁与 invent_asof_leak_after_hours_fixed_price_always_fillable 双挂争主表；CH1半泄露不得升格并列主报
# params.ch0_invent_assume_after_hours_fixed_price_always_fillable 建议 True
# params.ch1_asof_leak_after_hours_fixed_price_always_fillable_only 建议 True
# params.ch2_pit_after_hours_fill 建议 True
# params.merge_with_A_fill 建议 False  # CH≠A；严禁复用假设-A
# params.merge_with_AR_queue 建议 False  # CH≠AR；不改 AR
# params.merge_with_D_fill_time 建议 False  # CH≠D；严禁复用假设-D
# params.merge_with_C_universe_pool 建议 False  # CH≠C；严禁复用假设-C
# params.merge_with_H_exit 建议 False  # CH≠H；严禁复用假设-H
# params.merge_with_M_aft 建议 False  # CH≠M；不改 M
# params.merge_with_N_close_gtc 建议 False  # CH≠N；不改 N
# params.merge_with_O_block 建议 False  # CH≠O；不改 O
# params.merge_with_CA_maint_ratio_formula 建议 False  # CH≠CA；不改 CA
# params.merge_with_CB_financing_rollover 建议 False  # CH≠CB；不改 CB
# params.merge_with_CC_delist_force_deadline 建议 False  # CH≠CC；不改 CC
# params.merge_with_CD_limit_up_fill 建议 False  # CH≠CD；不改 CD
# params.merge_with_CE_limit_down_fill 建议 False  # CH≠CE；不改 CE
# params.merge_with_CF_call_auction_fill 建议 False  # CH≠CF；不改 CF
# params.merge_with_CG_resume_halt_fill 建议 False  # CH≠CG；不改 CG
# params.merge_with_AG_beyond_limit 建议 False
# params.merge_with_B_legacy 建议 False  # CH≠B
# params.merge_with_Z_margin_ratio 建议 False  # 与两融审批/费用类正交
# params.merge_with_BA_margin_buy_list 建议 False
# params.merge_with_BB_refinance_borrow 建议 False
# params.merge_with_BC_maint_force 建议 False
# params.merge_with_BD_haircut 建议 False
# params.merge_with_BE_balance_pause 建议 False
# params.merge_with_BF_contract_term 建议 False
# params.merge_with_BG_collateral_list 建议 False
# params.merge_with_BH_credit_quota 建议 False
# params.merge_with_BI_short_proceeds 建议 False
# params.merge_with_BJ_financing_sale_repay 建议 False
# params.merge_with_BK_client_conc 建议 False
# params.merge_with_BL_collateral_withdraw 建议 False
# params.merge_with_BM_margin_call_open_ban 建议 False
# params.merge_with_BN_cross_account 建议 False
# params.merge_with_BO_financing_interest 建议 False
# params.merge_with_BP_corp_action_comp 建议 False
# params.merge_with_BQ_list_removal_stock 建议 False
# params.merge_with_BR_short_borrow_fee 建议 False
# params.merge_with_BS_financing_rate_tier 建议 False
# params.merge_with_BT_force_close_order 建议 False
# params.merge_with_BU_daily_short_inventory 建议 False
# params.merge_with_BV_short_recall 建议 False
# params.merge_with_BW_credit_usage 建议 False
# params.merge_with_BX_interest_start_daycount 建议 False
# params.merge_with_BY_margin_call_grace 建议 False
# params.merge_with_BZ_early_repay_fee 建议 False
# params.merge_with_K_shortable_list 建议 False
# params.merge_with_AB_short_px 建议 False
# params.merge_with_Y_auction_vol 建议 False
# params.merge_with_AN_auction_leftover 建议 False
# params.merge_with_W_exright 建议 False
# params.merge_with_X_st_limit 建议 False
# params.missing_after_hours_fill_policy 建议 skip
# params.day_freq_proxy 建议 after_hours_fill_sensitivity
# params.universe_rule 建议 sse_szse_after_hours_fill_misopen_check
# params.fail_policy 写死冻结 skip
# params.redline_v0_exempt_scope 建议 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母CH；params.G≠实验字母CH；params.N≠实验字母CH；亦≠单字母实验C/H/A/M/Z；禁 null/holdout/跑后改口；勿改他字母已冻 Y/G/N/Y2
# params.date_start / date_end 建议 2019-01-01..2026-09-30
# params.oos_split.*                     建议四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改盘后固定价格可成交误开口径、Y/G/N/Y2、主窗/oos、ch0_primary_demo
```

可编码摘要（伪代码，不开跑）：

```
asof = params.asof_check_date  # 写死冻结 2026-10-16
# CH0：假全额可成——盘后固定价格订单按收盘价/固定价 100% 成交
# CH1：仅 asof 日更宽「盘后固定价格一律全额可成」规则泄露铺满
# CH2：每个交易日 d 按当日已生效盘后固定价格撮合/额度约束 PIT（消费 A/AR/D/CD/CE/CF/CG/M 诚实或旁路）
# 缺盘后可成交约束字段 → skip（params.missing_after_hours_fill_policy）
```

```
fill_time = "next_open"  # 写死冻结
asof_check_date = "2026-10-16"  # 写死冻结
px_basis = "unadj"
after_hours_fill_honest = "pit_by_aft_fixed_price_fill_rule"  # 写死冻结
after_hours_fill_scope = "assume_after_hours_fixed_price_always_fillable_at_close_or_fixed"  # 写死冻结
after_hours_fill_over_policy = "fail_or_partial_or_fail_missing_aft_fill_rule"  # 写死冻结
ch0_primary_demo = "invent_assume_after_hours_fixed_price_always_fillable"  # 写死冻结单一主报；禁与 invent_asof_leak_after_hours_fixed_price_always_fillable 双挂
ch0_invent_assume_after_hours_fixed_price_always_fillable = True
ch1_asof_leak_after_hours_fixed_price_always_fillable_only = True
ch2_pit_after_hours_fill = True
merge_with_A_fill = False
merge_with_AR_queue = False
merge_with_D_fill_time = False
merge_with_C_universe_pool = False
merge_with_H_exit = False
merge_with_M_aft = False
merge_with_N_close_gtc = False
merge_with_O_block = False
merge_with_CA_maint_ratio_formula = False
merge_with_CB_financing_rollover = False
merge_with_CC_delist_force_deadline = False
merge_with_CD_limit_up_fill = False
merge_with_CE_limit_down_fill = False
merge_with_CF_call_auction_fill = False
merge_with_CG_resume_halt_fill = False
fail_policy = "skip"
```

### 2.2 三组对照（CH0 / CH1 / CH2）

| 组 | 口径 | 说明 |
|----|------|------|
| CH0 天真 | `invent_assume_after_hours_fixed_price_always_fillable`（建议单一主报） | 发明假全额可成路径；禁与 invent_asof_leak_after_hours_fixed_price_always_fillable 双挂 |
| CH1 半泄露·混口径 | 全样本用 `asof_check_date` 当天更宽「盘后固定价格一律全额可成」规则铺满历史 | 仅盘后全额可成 asof 泄露；不升格并列主报 |
| CH2 PIT | `after_hours_fill_honest=pit_by_aft_fixed_price_fill_rule`（已冻结） | 每个交易日按当时已生效盘后固定价格撮合/额度约束 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：盘后固定价格窗标签代理 + 收盘价/固定价全额成交默认 vs 诚实未匹配/额度限制/次日缺口 → 当日可实现成交与失败笔；缺字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有未复权 OHLC + 盘后通道/额度代理 + 成交意图代理即可纸面起步；**本页不开回测、不拉真数、不派回测岗、不抢 A 真数队列**。

### 3.1 oos_split（建议四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、未匹配/额度限制差、次日缺口差超出标定噪声带，且差异集中在「盘后固定价格可成交性误开」桶，不被 A 板上容量、CG 复牌首日、CF 集合竞价、CE 跌停可成交、CD 涨停可成交、M 盘后通道、H 退出期、C 股票池、N 收盘机制、O 大宗、CA/CB/CC 两融族等他页桶吞并。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 A/CG/CF/CE/CD/M/H/C/N/O/CA/CB/CC/AR/AG/AN/T 等他页桶吞并；或 holdout 反调 `ch0_primary_demo` / Y·G·N·Y2；或 CH0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CH0 / CH1 / CH2。报告可实现成交差、假全额可成贡献差、未匹配/额度限制差、次日缺口差。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_assume_after_hours_fixed_price_always_fillable",
  "invent_asof_leak_after_hours_fixed_price_always_fillable",
  "aft_fixed_price_window",
  "quota_cap_window",
  "next_day_gap_window",
  "vs_A_limit_up_fill",
  "vs_CG_resume_halt_fill",
  "vs_CF_call_auction_fill",
  "vs_CE_limit_down_fill",
  "vs_CD_limit_up_fill",
  "vs_M_aft_channel",
  "vs_H_exit_period",
  "vs_N_close_mech",
  "vs_O_block_trade",
  "vs_C_universe_pool",
  "vs_D_fill_time_suspend",
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
  "vs_X_st_limit_avoid",
  "vs_V_stamp_tax_avoid",
  "vs_U_transfer_fee_avoid",
  "vs_T_csrc_fee_avoid",
  "vs_S_handling_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够盘后固定价格窗/撮合与额度约束字段；缺字段却静默当假全额可成 → 设计失效。  
2. 把「板上容量已诚实（A）」静默写成「盘后固定价格可成交性已诚实」且不声明另页 A → **与 A 撞题**（**尤其 CH≠A**；**严禁复用假设-A**；**绝不可做成 A 续篇**；**不抢 A 真数队列**）。  
3. 把「复牌首日可成交已诚实（CG）」静默写成「盘后固定价格可成交性已诚实」 → **与 CG 撞题**（复牌首日 ≠ 盘后固定价；**尤其 CH≠CG**；**不改 CG**）。  
4. 把「集合竞价可成交已诚实（CF）」静默写成「盘后固定价格可成交性已诚实」 → **与 CF 撞题**（**尤其 CH≠CF**；**不改 CF**）。  
5. 把「跌停可成交已诚实（CE）」静默写成「盘后固定价格可成交性已诚实」 → **与 CE 撞题**（**尤其 CH≠CE**；**不改 CE**）。  
6. 把「涨停可成交已诚实（CD）」静默写成「盘后固定价格可成交性已诚实」 → **与 CD 撞题**（**尤其 CH≠CD**；**不改 CD**）。  
7. 把「盘后通道已诚实（M）」静默写成「盘后固定价格可成交性已诚实」 → **与 M 撞题**（通道存在/自动滚入 ≠ 盘后时段内全额可成；**尤其 CH≠M**；**不改 M**）。  
8. 把「退出期已诚实（H）」静默写成「盘后固定价格可成交性已诚实」 → **与 H 撞题**（**尤其 CH≠H**；**双字母 CH ≠ 单字母假设-H**；**严禁复用假设-H**）。  
9. 把「股票池已诚实（C）」静默写成「盘后固定价格可成交性已诚实」 → **与 C 撞题**（**尤其 CH≠C**；**严禁复用假设-C**）。  
10. 把「收盘机制已诚实（N）/ 大宗已诚实（O）」静默写成「盘后固定价格可成交性已诚实」 → **与 N/O 撞题**（**尤其 CH≠N / CH≠O**）。  
11. 把「分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「盘后固定价格可成交性已诚实」 → **与 CA/CB/CC 撞题**（与两融审批/费用类正交；**尤其 CH≠CA / CH≠CB / CH≠CC**；**不改 CA/CB/CC**）。  
12. 把「集合剩单/超板无效/整手/单笔上限/集合量分母已诚实」写成主病或不声明另页 → 与 AN/AG/E/AF/Y 撞题。  
13. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「盘后固定价格可成交性已诚实」→ 与交易所费用族撞题（**明确避开预检T**）。  
14. 把实验字母 CH 与单字母 A/B/C/D/E/F/G/H/K/M/N/O/T/S/U/V/W/X/Y/Z 或双字母 BA–CG/CA/CB/CC/CD/CE/CF/CG/AR/AG/AN/BZ/BY/BF/BQ/BC/BT/BD/BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
15. holdout 反调 `ch0_primary_demo` / Y·G·N·Y2 → 结论无效。  
16. 用复权价代理盘后可成交路径 → 标签与执行双错，结论无效。  
17. 用核对日更宽「假全额可成」当诚实 PIT、或把临时宽口径铺满历史 → 设计失效。  
18. **`ch0_primary_demo` 与 `invent_asof_leak_after_hours_fixed_price_always_fillable` 双挂主报**；或 CH1 升格并列主报 → 设计失效。  
19. **改写或覆盖 `假设-A` / `假设-CG` / `假设-CF` / `假设-CE` / `假设-CD` / `假设-M` / `假设-H` / `假设-C` / `假设-N` / `假设-O` / `假设-CA` / `假设-CB` / `假设-CC` / 已冻 AA–CG** → 硬边界违约，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块、盘后固定价格窗标签代理；  
- 成交意图量、收盘价/固定价全额成交默认 vs 诚实未匹配/额度限制/次日缺口规则及生效日；  
- 板上容量 / 排队位次 / 开收时点与停牌 / 涨跌停可成交误开 / 集合竞价可成交误开 / 复牌首日可成交误开 / 盘后通道存在输入（消费 A/AR/D/CD/CE/CF/CG/M 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历。

可选：额度封顶分段；与 A 容量窗、CG 复牌窗、CF 集合竞价窗、CE/CD 涨跌停窗、M 通道切日窗对照但不混主结论；缺盘后约束原因码敏感性（主报仍在盘后固定价格可成交性误开）。

**禁止**：用核对日「今天盘后固定价格一律全额可成」铺满当唯一诚实组；用复权价；把板上容量已诚实/复牌首日可成交已诚实/集合竞价可成交已诚实/跌停可成交已诚实/涨停可成交已诚实/盘后通道已诚实/退出期已诚实/股票池已诚实/收盘机制已诚实/大宗已诚实/两融审批费用已诚实当成「盘后固定价格可成交性正确」依据；把 A/CG/CF/CE/CD/M/H/C/N/O/CA/CB/CC/AR/AG/AN/Z/BA–CG/K/AB/W/X/V/U/T/S 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`CH`  
- **组**：CH0 / CH1 / CH2  
- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`after_hours_fill_honest=pit_by_aft_fixed_price_fill_rule`；`after_hours_fill_scope=assume_after_hours_fixed_price_always_fillable_at_close_or_fixed`；`after_hours_fill_over_policy=fail_or_partial_or_fail_missing_aft_fill_rule`；`board_capacity_handoff=a_page`；`queue_handoff=ar_page`；`fill_time_suspend_handoff=d_page`；`beyond_limit_handoff=ag_page`；`limit_up_fill_handoff=cd_page`；`limit_down_fill_handoff=ce_page`；`call_auction_fill_handoff=cf_page`；`resume_halt_fill_handoff=cg_page`；`aft_channel_handoff=m_page`；`exit_period_handoff=h_page`；`close_mech_handoff=n_page`；`block_trade_handoff=o_page`；`universe_pool_handoff=c_page`；`maint_ratio_formula_handoff=ca_page`；`financing_rollover_handoff=cb_page`；`delist_force_deadline_handoff=cc_page`；其余 handoff 见 §2.1；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_after_hours_fill_misopen_check`；`missing_after_hours_fill_policy=skip`；`day_freq_proxy=after_hours_fill_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议占位 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 CH**；**params.G≠实验字母 CH**；**params.N≠实验字母 CH**；亦≠单字母实验 C/H/A/M/Z；禁 null/holdout/跑后改口；**勿改他字母已冻 Y/G/N/Y2**）；**`params.ch0_primary_demo` 建议 `invent_assume_after_hours_fixed_price_always_fillable`**（禁与 invent_asof_leak_after_hours_fixed_price_always_fillable 双挂；CH1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期建议写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- CH0/CH1/CH2 净收益/成本质量、ΔFakeAlwaysFillable、ΔRealizableFill、ΔUnmatchedOrQuotaFail、ΔNextDayGap；分桶（盘后固定价格可成交性误开 / 核对日泄露 / 盘后固定价窗 / 额度封顶窗 / 次日缺口窗 / vs A·CG·CF·CE·CD·M·H·C·N·O·CA·CB·CC·AR·AG·AN·Z·BA–CG·K·AB·W·X·V·U·T·S）。  
- 自检气泡：CH2 是否 pit_by_aft_fixed_price_fill_rule；CH0 是否单一主报；CH1 是否仅核对日泄露；是否未与 A/CG/CF/CE/CD/M/H/C/N/O/CA/CB/CC/AR/AG/AN/Z/BA–CG/K/AB/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 CH 与 C 或 H 或 A 或 M 或 CG 或 CF 或 CE 或 CD 或 CA 或 CB 或 CC 或 N 或 O 或 B 或 Z 或 K 或 BA–CG 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 CH≠单字母假设-A；CH≠单字母假设-C；CH≠单字母假设-H；CH≠单字母假设-M；CH≠双字母假设-CG；CH≠双字母假设-CF；CH≠双字母假设-CE；CH≠双字母假设-CD；CH≠双字母假设-CA；CH≠双字母假设-CB；CH≠双字母假设-CC；params.Y≠实验字母 CH**；**是否未改 Y/Z/AA–CG 冻结补丁正文**；**是否未改假设-A / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-M / 假设-H / 假设-C / 假设-N / 假设-O / 假设-CA / 假设-CB / 假设-CC**；**是否未重做预检T**；**是否未复用假设-A / 假设-C / 假设-H / 假设-M / 假设-CD / 假设-CE / 假设-CF / 假设-CG**；**是否未与 invent_asof_leak_after_hours_fixed_price_always_fillable 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假全额可成或核对日泄露吹成诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不占本机 8765 席位；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–CG 及其他 A/D–CG 已交正文**；**尤其不改假设-CG；尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-M；尤其不改假设-H；尤其不改假设-A；尤其不改假设-C；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC**；**勿再改 CG/CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN/M/N/O**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 执行鸿沟同向：板上枯竭（A）、板上排队（AR）、成交时点与停牌（D）、超涨跌停价无效（AG）、涨停板可成交性误开（CD）、跌停板可成交性误开（CE）、集合竞价可成交性误开（CF）、停牌复牌首日可成交性误开（CG）、盘后通道存在与自动滚入（M）之外，**回测不得默认「盘后固定价格交易时段订单必能按收盘价/固定价全额成交」**；须按当时有效盘后固定价格撮合/额度约束 PIT。与两融审批/费用族（Z/BA–CC 等）正交，本页不主测两融。与 CD 连续竞价涨停侧、CE 连续竞价跌停侧、CF 集合竞价时段、CG 复牌首日、M 通道存在性**正交分列**，本页专测盘后固定价格时段内可成交误开。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 CH** 标准件，**不改口径主线**，**不改假设 A–CG 正文**，**尤其不改假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-M / 假设-H / 假设-A / 假设-C / 假设-CA / 假设-CB / 假设-CC**。与实验 A/CG/CF/CE/CD/M/H/C/N/O/CA/CB/CC/AR/AG/AN/Z/BA–CG/K/AB/W/X/V/U/T/S 分工：**A=板上枯竭主实验（严禁复用；不抢真数）；CG=停牌复牌首日可成交性误开（严禁改）；CF=集合竞价可成交性误开（严禁改）；CE=跌停板可成交性误开（严禁改）；CD=涨停板可成交性误开（严禁改）；M=盘后通道存在/自动滚入（严禁改）；H=退市整理退出期（严禁复用）；C=股票池；N=收盘机制；O=大宗；CA=维持比分子分母；CB=展期审批；CC=调出了结时限；CH=盘后固定价格可成交性误开（CH≠A≠CG≠CF≠CE≠CD≠M≠H≠C≠N≠O≠CA≠CB≠CC≠B≠Z≠K≠BA≠…≠BZ≠BY≠BF≠BQ≠BC≠BT≠BD≠BL≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AR≠AG≠AN≠AB≠W≠T≠S≠U≠V≠X）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；**禁止标任何纸面齐**） |
| 标准件路径 | `假设-CH-盘后固定价格可成交性误开.md` |
| 清单序号 | 约 #91 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死冻结**；**after_hours_fill_honest=pit_by_aft_fixed_price_fill_rule 写死冻结**；diff_buckets 默认名待复检；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 CH；params.G≠实验字母 CH；params.N≠实验字母 CH；亦≠单字母实验 C/H/A/M/Z；禁 null/holdout/跑后改口）**；**ch0_primary_demo 写死冻结 invent_assume_after_hours_fixed_price_always_fillable（禁双挂 invent_asof_leak_after_hours_fixed_price_always_fillable；CH1半泄露不得升格并列主报）**；锚升格写死 after_hours_fill_honest=pit_by_aft_fixed_price_fill_rule / after_hours_fill_scope=assume_after_hours_fixed_price_always_fillable_at_close_or_fixed / after_hours_fill_over_policy=fail_or_partial_or_fail_missing_aft_fill_rule / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **CH≠C/H/CA/CB/CC/CD/CE/CF/CG/A/M/N/O/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ/Z/B**（及 ≠BA–CG/K/AB/W/T/S/U/V/X/Y/F/E/D/G），**严禁复用假设-A / 假设-C / 假设-H / 假设-M / 假设-CD / 假设-CE / 假设-CF / 假设-CG**；**尤其 CH≠CG（勿撞停牌复牌首日可成交性）**；**尤其 CH≠CF（勿撞集合竞价可成交性）**；**尤其 CH≠CE（勿撞跌停可成交性）**；**尤其 CH≠CD（勿撞涨停可成交性）**；**尤其 CH≠M（通道存在 ≠ 盘后全额可成）**；**尤其 CH≠H（双字母 CH ≠ 单字母假设-H）**；**尤其 CH≠A（不抢实验A真数队列）**；**尤其 CH≠C**；**尤其不改假设-CG/CF/CE/CD/M/H/A/C/CA/CB/CC**；**params.Y≠实验字母 CH**；**params.G≠实验字母 CH**；与两融审批/费用类正交 |
| 结论栏 | 空 |

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-04）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 CH**；**`params.G` ≠ 实验字母 CH**；**`params.N` ≠ 实验字母 CH**；**`params.Y` ≠ 单字母实验 C/H/A/M/Z**；尤重**双字母 CH ≠ 单字母假设-A**；**双字母 CH ≠ 单字母假设-C**；**双字母 CH ≠ 单字母假设-H**；**双字母 CH ≠ 单字母假设-M**；**双字母 CH ≠ 双字母假设-CA**；**双字母 CH ≠ 双字母假设-CB**；**双字母 CH ≠ 双字母假设-CC**；**双字母 CH ≠ 双字母假设-CD**；**双字母 CH ≠ 双字母假设-CE**；**双字母 CH ≠ 双字母假设-CF**；**双字母 CH ≠ 双字母假设-CG**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.ch0_primary_demo`**：**写死冻结** **`invent_assume_after_hours_fixed_price_always_fillable`**；禁与 **`invent_asof_leak_after_hours_fixed_price_always_fillable`** 双挂争主表（只挂一个 primary）；**CH1 半泄露不得升格并列主报**。  
3. **盘后固定价格可成交性锚升格写死（不可再写「建议」）**：`params.after_hours_fill_honest=pit_by_aft_fixed_price_fill_rule`；`params.after_hours_fill_scope=assume_after_hours_fixed_price_always_fillable_at_close_or_fixed`；`params.after_hours_fill_over_policy=fail_or_partial_or_fail_missing_aft_fill_rule`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有盘后固定价格可成交相关锚点；不改口）。

**硬分列保留**：CH≠C/H/CA/CB/CC/CD/CE/CF/CG/A/M/N/O/AR/AG…；**尤其 CH≠CG / CH≠CF / CH≠CE / CH≠CD / CH≠A / CH≠M / CH≠H**；**双字母 CH ≠ 单字母假设-H**；**严禁复用假设-C / 假设-H / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-M**；**params.Y/G/N ≠ 实验字母 CH**。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 风控预检补丁·冻结三条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CH**；**params.G≠实验字母 CH**；**params.N≠实验字母 CH**；亦≠单字母实验 C/H/A/M/Z；尤重**双字母 CH ≠ 单字母假设-A/C/H/M**；**双字母 CH ≠ 双字母假设-CG/CF/CE/CD/CA/CB/CC**；禁 null/holdout/跑后改口）；② `params.ch0_primary_demo=invent_assume_after_hours_fixed_price_always_fillable`（禁与 `invent_asof_leak_after_hours_fixed_price_always_fillable` 双挂争主表；CH1半泄露不得升格并列主报）；③ 锚升格写死：`after_hours_fill_honest=pit_by_aft_fixed_price_fill_rule`；`after_hours_fill_scope=assume_after_hours_fixed_price_always_fillable_at_close_or_fixed`；`after_hours_fill_over_policy=fail_or_partial_or_fail_missing_aft_fill_rule`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。硬分列保留：**CH≠C/H/CA/CB/CC/CD/CE/CF/CG/A/M…**；**尤其 CH≠CG（勿撞停牌复牌首日可成交性）**；**尤其 CH≠CF（勿撞集合竞价可成交性）**；**尤其 CH≠CE（勿撞跌停可成交性）**；**尤其 CH≠CD（勿撞涨停可成交性）**；**尤其 CH≠A（不抢实验A真数队列）**；**尤其 CH≠H（双字母 CH ≠ 单字母假设-H）**；不改 CG/Y–CG 已冻正文；**未标纸面齐**；状态→**预检有条件通过 · 三条已冻 · 待复检**。 |
| 2026-11-04 | 新建草稿·待入库预检（总管线：CG 补丁 tip=`4e10fef` 已交后写 CH；选题盘后固定价格可成交性误开；**CH≠C/H/CA/CB/CC/CD/CE/CF/CG/A/M/N/O…**；尤其 **CH≠CG（勿撞停牌复牌首日可成交性）**、**CH≠CF（勿撞集合竞价可成交性）**、**CH≠CE（勿撞跌停可成交性）**、**CH≠CD（勿撞涨停可成交性）**、**CH≠M（通道存在 ≠ 盘后全额可成）**、**CH≠H（双字母 CH ≠ 单字母假设-H）**、**CH≠A（不抢实验A真数队列）**、**CH≠C**；primary_demo 建议=`invent_assume_after_hours_fixed_price_always_fillable`；Y/G/N/Y2 建议占位 `0.02/0.01/0.05/0.015` 待预检；不开回测；未改 CG/CF/CE/CD/M/H/A/C/CA/CB/CC 及其他已齐字母；**未标纸面齐**）。 |
