# 假设 CK · 协议大宗可成交性误开 / 默认协议/成交申报大宗订单必能按目标价或谈妥价全额成交（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CJ 补丁已交（tip=`991e4cf`；A/D–CJ纸面齐 HEAD=`6204049`；复检/入库另线并行后写下一纸面 CK）；清单撞题规则另选正交执行缺口（**回测默认「协议/成交申报大宗订单必能按目标价或谈妥价全额成交」** ≠ 假设-CJ 退市整理期可成交性误开 ≠ 假设-CI 新股上市首日可成交性误开 ≠ 假设-CH 盘后固定价格可成交性误开 ≠ 假设-CG 停牌复牌首日可成交性误开 ≠ 假设-CF 集合竞价可成交性误开 ≠ 假设-CE 跌停板可成交性误开 ≠ 假设-CD 涨停板可成交性误开 ≠ 假设-O 大宗假流动性（**双字母 CK ≠ 单字母假设-O**；O=大宗量价并进竞价/三通道混用 ≠ 协议大宗腿假全额可成） ≠ 假设-A 板上枯竭/一字与封板容量主实验 ≠ 假设-D 成交时点开vs收与停牌假成交 ≠ 假设-C 股票池当时名单 ≠ 假设-M 盘后通道存在 ≠ 假设-H 退市整理退出期 ≠ 假设-CA/CB/CC 两融族）；选题自 `事实与坑`「按大宗成交价回放普通信号=假设你总能找到30万股对手盘；门槛30万股/200万；确认时点PIT；协议/成交申报≠盘后固定价格」+ 口径「执行鸿沟」+ 与 CD/CE/CF/CG/CH/CI/CJ 可成交性族正交、与 O 大宗假流动性正交；本页**假定板上容量层（A）/ 排队位次层（AR）/ 成交时点与停牌层（D）/ 超涨跌停价无效层（AG）/ 涨停可成交误开层（CD）/ 跌停可成交误开层（CE）/ 集合竞价可成交误开层（CF）/ 停牌复牌首日可成交误开层（CG）/ 盘后固定价格可成交误开层（CH）/ 新股上市首日可成交误开层（CI）/ 退市整理期可成交误开层（CJ）/ 大宗量价并进竞价与三通道混用层（O）/ 盘后通道存在层（M）诚实或显式旁路**，主病只在**发明「协议/成交申报大宗订单必能按目标价或谈妥价全额成交」这一误开默认**；**A 正文主测「涨停可成交性/板上枯竭」真数队列**（**双字母 CK ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 续篇；不抢 A 真数队列**），**O 正文主测「大宗假流动性」**（量价并进竞价/三通道混用 ≠ 协议大宗腿假全额可成；**双字母 CK ≠ 单字母假设-O；严禁复用 O 题面；尤其不改假设-O**），**CJ 正文主测「退市整理期可成交性误开」**（退市整理期 ≠ 协议大宗；**严禁改 CJ**），**CI/CH/CG/CF/CE/CD 正文主测上市首日/盘后固定价/复牌/集合/跌停/涨停可成交误开**（**严禁改 CI/CH/CG/CF/CE/CD**），**M 正文主测盘后通道存在**（通道存在 ≠ 大宗腿全额可成；**严禁改 M**），**C 正文主测「股票池当时名单」**（**双字母 CK ≠ 单字母假设-C；严禁复用 C**），**CA/CB/CC 正文主测两融族**（与本页正交；**严禁改 CA/CB/CC**）→ 自立；与假设 B/Z/BA–CJ/AG/AF/E/L/X/W/K/AB/N/H/AN 等**分列**；**严禁复用假设-K 融券名单**；**新建实验 CK**  
状态：**草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；禁止把「协议/成交申报大宗订单必能按目标价或谈妥价全额成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CJ 及其他 A/D–CJ 已交正文与冻结补丁；尤其不改假设-CJ；尤其不改假设-CI；尤其不改假设-CH；尤其不改假设-CG；尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-O；尤其不改假设-A；尤其不改假设-C；尤其不改假设-M；尤其不改假设-H；尤其不改假设-K；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；勿再改 CJ/CI/CH/CG/CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN/O/M/H/K**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CK（约 #94）。与假设 **CJ（退市整理期可成交性误开）** **硬分列（专节强调）**：CJ = 回测是否默认「**退市整理期**订单必能按目标价或开盘价/收盘价**全额**成交」；本页 = 回测是否默认「**协议/成交申报大宗**订单必能按目标价或谈妥价**全额**成交」；退市整理期 ≠ 协议大宗；**严禁复用 CJ 题面或 `invent_assume_delist_period_always_fillable`**；**尤其不改假设-CJ**。**CK≠CJ**。与假设 **CI（新股上市首日可成交性误开）** **硬分列**：上市首日 ≠ 协议大宗；**严禁复用 CI**；**尤其不改假设-CI**。**CK≠CI**。与假设 **CH（盘后固定价格可成交性误开）** **硬分列（专节强调）**：CH = 盘后固定价格全额可成误开；本页 = 协议大宗腿全额可成误开；盘后固定价 ≠ 协议大宗；**严禁复用 CH 题面或 `invent_assume_after_hours_fixed_price_always_fillable`**；**尤其不改假设-CH**。**CK≠CH**。与假设 **CG（停牌复牌首日可成交性误开）** **硬分列**：复牌首日 ≠ 协议大宗；**严禁复用 CG**；**尤其不改假设-CG**。**CK≠CG**。与假设 **CF（集合竞价可成交性误开）** **硬分列**：集合撮合 ≠ 协议大宗全额可成；**严禁复用 CF**；**尤其不改假设-CF**。**CK≠CF**。与假设 **CE（跌停板可成交性误开）** **硬分列**：连续竞价跌停侧 ≠ 协议大宗；**严禁复用 CE**；**尤其不改假设-CE**。**CK≠CE**。与假设 **CD（涨停板可成交性误开）** **硬分列**：连续竞价涨停侧 ≠ 协议大宗；**严禁复用 CD**；**尤其不改假设-CD**。**CK≠CD**。与假设 **O（大宗假流动性）** **硬分列（专节强调）**：O = 把**大宗量/价并进竞价**估冲击、或把**盘后固定价格/深市盘后定价大宗/沪市大宗固定价格申报**混成同一通道；本页 = 在 O 层诚实（或显式旁路交 O）的前提下，是否仍默认「协议/成交申报大宗订单必能按目标价或谈妥价全额成交」；量价并进竞价/三通道混用 ≠ 协议大宗腿假全额可成；**双字母 CK ≠ 单字母假设-O**；**严禁复用 O 题面**；**尤其不改假设-O**。**CK≠O**。与假设 **A（涨停可成交性/板上枯竭）** **硬分列（专节强调）**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成的**主实验与真数队列**；本页 = **纸面机制误开点**：回测/仿真是否默认发明「协议/成交申报大宗订单必能按目标价或谈妥价全额成交」并系统性高估大宗腿可实现成交、低估门槛未达、确认窗外失败与假对手盘；容量门槛 ≠ 协议大宗全额可成默认；**双字母 CK ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不占** A 的 A0/A1 主报与真数席位；**尤其不改假设-A**。**CK≠A**。与假设 **M（盘后补成交/通道）** **硬分列**：通道存在/自动滚入 ≠ 协议大宗腿全额可成；**严禁复用 M**；**尤其不改假设-M**。**CK≠M**。与假设 **C（股票池当时名单）** **硬分列**：股票池 ≠ 协议大宗全额可成；**双字母 CK ≠ 单字母假设-C**；**严禁复用 C**。**CK≠C**。与假设 **K（融券空头名单PIT）** **硬分列（专节强调）**：**双字母 CK ≠ 单字母假设-K**；**严禁复用假设-K 融券名单**；**尤其不改假设-K**。**CK≠K**。与假设 **CA/CB/CC** **硬分列**：两融公式/展期/调出了结时限 ≠ 协议大宗全额可成；**尤其不改 CA/CB/CC**。**CK≠CA≠CB≠CC**。与假设 **AR/AG/AN/BZ/BY/BX/BW…** 及两融审批/费用族 **硬分列**：假队首/超板无效/集合剩单/两融审批费用 ≠ 协议大宗全额可成默认。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A / 假设-C / 假设-O / 假设-K / 假设-M / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH / 假设-CI / 假设-CJ**。**严禁改写/续写假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-O / 假设-A / 假设-M / 假设-K / 假设-CA / 假设-CB / 假设-CC**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CK** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 K**（融券空头名单PIT；**严禁复用假设-K**）≠ **单字母实验 O**（大宗假流动性；**严禁复用假设-O**）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **单字母实验 M**（盘后通道；**严禁改写假设-M**）≠ **单字母实验 H**（退市整理退出期；**严禁改写假设-H**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **双字母实验 CB**（融资展期审批；**严禁改写假设-CB**）≠ **双字母实验 CC**（调出强制了结时点；**严禁改写假设-CC**）≠ **双字母实验 CD**（涨停板可成交性误开；**严禁改写假设-CD**）≠ **双字母实验 CE**（跌停板可成交性误开；**严禁改写假设-CE**）≠ **双字母实验 CF**（集合竞价可成交性误开；**严禁改写假设-CF**）≠ **双字母实验 CG**（停牌复牌首日可成交性误开；**严禁改写假设-CG**）≠ **双字母实验 CH**（盘后固定价格可成交性误开；**严禁改写假设-CH**）≠ **双字母实验 CI**（新股上市首日可成交性误开；**严禁改写假设-CI**）≠ **双字母实验 CJ**（退市整理期可成交性误开；**严禁改写假设-CJ**）≠ **单字母实验 B** ≠ **单字母实验 Z** ≠ **单字母实验 D** ≠ **单字母实验 I** ≠ **单字母实验 J** ≠ **单字母实验 N**。全文凡写「实验 CK / 假设-CK / hypothesis_id=CK / 组 CK0·CK1·CK2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CK 混读或互改；**尤其 params.Y ≠ 实验字母 CK ≠ 单字母假设-C ≠ 单字母假设-K ≠ 单字母假设-O ≠ 单字母假设-A ≠ 单字母假设-M ≠ 双字母假设-CA ≠ 双字母假设-CB ≠ 双字母假设-CC ≠ 双字母假设-CD ≠ 双字母假设-CE ≠ 双字母假设-CF ≠ 双字母假设-CG ≠ 双字母假设-CH ≠ 双字母假设-CI ≠ 双字母假设-CJ**。亦**禁止**把实验字母 CK 与单字母 **A/B/C/D/E/F/G/H/I/J/K/M/N/O/T/S/U/V/W/X/Y/Z**、双字母 **BA–CJ**、双字母 **CA/CB/CC/CD/CE/CF/CG/CH/CI/CJ/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ**、双字母 **AB**、双字母 **AI/AJ/AQ**、双字母 **AZ/AY/AX/AW**、或 params 键名 `ck0_*` 以外的实验页混读。**双字母 CK ≠ 单字母 C ≠ 单字母 K ≠ 单字母 O ≠ 单字母 A ≠ 单字母 M ≠ 单字母 H ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 D ≠ 单字母 I ≠ 单字母 J ≠ 单字母 N ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 CC ≠ 双字母 CD ≠ 双字母 CE ≠ 双字母 CF ≠ 双字母 CG ≠ 双字母 CH ≠ 双字母 CI ≠ 双字母 CJ ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 AN ≠ 双字母 AI ≠ 双字母 AJ ≠ 双字母 AQ ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BF ≠ 双字母 BQ ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB ≠ 双字母 BK**；**params.Y ≠ 实验字母 CK**；**params.G ≠ 实验字母 CK**；**params.N ≠ 实验字母 CK**。**带过：双字母 CJ ≠ C/J/H/CA–CI/A…；双字母 CI ≠ C/I/CA–CH/A/G/J…；双字母 CH ≠ C/H/CA–CG/A/M…；双字母 CG ≠ C/G/CA–CF/A/D…；双字母 CF ≠ C/F/CA–CE/A/Y…；双字母 CE ≠ C/E/CA/CB/CC/CD/AR…；双字母 CD ≠ A/C/D/CA/CB/CC/AR…；双字母 CC ≠ C/CA/CB/BQ/BY/BZ/BF…；双字母 CB ≠ B/C/CA/BF/BZ…；双字母 CA ≠ A/C/BZ/BY…；双字母 AR ≠ A/R/AQ…；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CK ≠ 单字母假设-A / 假设-C / 假设-O / 假设-K / 假设-M；且 ≠ 假设-CA / 假设-CB / 假设-CC / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH / 假设-CI / 假设-CJ；带过 CJ≠CI/CH/CG/CF/CE/CD/H/A、params.Y≠CK（硬）

| 维度 | 对照页 | 本页假设-CK（双字母） |
|------|--------|----------------------|
| 题面 CJ | **退市整理期可成交性误开**（`invent_assume_delist_period_always_fillable`） | **协议大宗可成交性误开**：默认「协议/成交申报大宗订单必能按目标价或谈妥价全额成交」vs 诚实大宗门槛/确认时点/对手盘约束；退市整理期 ≠ 协议大宗；**严禁复用 CJ 题面**；**CK≠CJ**；**不改 CJ** |
| 题面 CI | **新股上市首日可成交性误开**（`invent_assume_ipo_day1_always_fillable`） | 上市首日 ≠ 协议大宗；**严禁复用 CI 题面**；**CK≠CI**；**不改 CI** |
| 题面 CH | **盘后固定价格可成交性误开**（`invent_assume_after_hours_fixed_price_always_fillable`） | 盘后固定价 ≠ 协议大宗；**严禁复用 CH 题面**；**CK≠CH**；**不改 CH** |
| 题面 CG | **停牌复牌首日可成交性误开**（`invent_assume_resume_from_halt_always_fillable`） | 复牌首日 ≠ 协议大宗；**严禁复用 CG 题面**；**CK≠CG**；**不改 CG** |
| 题面 CF | **集合竞价可成交性误开**（`invent_assume_call_auction_always_fillable`） | 集合竞价 ≠ 协议大宗全额可成默认；**严禁复用 CF 题面**；**CK≠CF**；**不改 CF** |
| 题面 CE | **跌停板可成交性误开**（`invent_assume_limit_down_always_fillable`；连续竞价跌停侧） | 连续竞价跌停侧 ≠ 协议大宗全额可成；**严禁复用 CE 题面**；**CK≠CE**；**不改 CE** |
| 题面 CD | **涨停板可成交性误开**（`invent_assume_limit_up_always_fillable`；连续竞价涨停侧） | 连续竞价涨停侧 ≠ 协议大宗全额可成；**严禁复用 CD 题面**；**CK≠CD**；**不改 CD** |
| 题面 O | **大宗假流动性**（量价并进竞价/三通道混用；清单实验 O） | 量价并进竞价/三通道混用 ≠ 协议大宗腿假全额可成；**双字母 CK ≠ 单字母假设-O**；**严禁复用 O**；**CK≠O**；**不改 O** |
| 题面 A | **涨停可成交性/板上枯竭**（清单实验 A；真数队列） | 容量门槛 ≠ 协议大宗全额可成默认；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不抢 A 真数队列**；**CK≠A** |
| 题面 M | **盘后补成交/通道存在**（清单实验 M） | 通道存在 ≠ 协议大宗腿全额可成；**严禁复用 M 题面作主病**；**CK≠M**；**不改 M** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 股票池 ≠ 协议大宗全额可成；**严禁复用 C**；**CK≠C** |
| 题面 K | **融券空头名单PIT**（清单实验 K） | 融券名单 ≠ 协议大宗全额可成；**双字母 CK ≠ 单字母假设-K**；**严禁复用假设-K**；**CK≠K**；**不改 K** |
| 题面 CA | **维持担保比例分子分母口径** | 公式 ≠ 协议大宗全额可成；**CK≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批** | 展期审批 ≠ 协议大宗全额可成；**CK≠CB**；**不改 CB** |
| 题面 CC | **两融标的调出强制了结时点** | 调出了结时限 ≠ 协议大宗全额可成；**CK≠CC**；**不改 CC** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_assume_block_trade_always_fillable`（**写死冻结**单一主报；禁双挂 asof_leak；CK1不升格） |
| 文档 | 清单实验 A / C / O / K / M / `假设-CA-…` / `假设-CB-…` / `假设-CC-…` / `假设-CD-…` / `假设-CE-…` / `假设-CF-…` / `假设-CG-…` / `假设-CH-…` / `假设-CI-…` / `假设-CJ-…`（**只读；禁止改写**） | `假设-CK-协议大宗可成交性误开.md`（新建） |
| 预检键 | 实验字母 A / C / O / K / M / CA / CB / CC / CD / CE / CF / CG / CH / CI / CJ | 实验字母 **CK** / `ck0_primary_demo`；**不得**占用或改写预检 A/C/O/K/M/CA/CB/CC/CD/CE/CF/CG/CH/CI/CJ |

**禁止**：把 CK 写成「A/CJ/CI/CH/CG/CF/CE/CD/O/M/C/K/CA/CB/CC 的续篇」；把「板上容量已诚实（A）/ 退市整理期可成交已诚实（CJ）/ 上市首日可成交已诚实（CI）/ 盘后固定价可成交已诚实（CH）/ 复牌首日可成交已诚实（CG）/ 集合竞价可成交已诚实（CF）/ 跌停可成交已诚实（CE）/ 涨停可成交已诚实（CD）/ 大宗量价/通道已诚实（O）/ 盘后通道已诚实（M）/ 股票池已诚实（C）/ 融券名单已诚实（K）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「协议大宗可成交性已诚实」；覆盖或补丁改写假设-A / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-O / 假设-M / 假设-K / 假设-C / 假设-CA / 假设-CB / 假设-CC 正文；把 `params.Y/G/N` 与实验字母 CK 混读；**禁** `ck0_primary_demo` 与 `invent_asof_leak_block_trade_always_fillable` **双挂主报**；**禁** CK1 半泄露升格并列主报；**禁**复用假设-A / 假设-C / 假设-O / 假设-K / 假设-M / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH / 假设-CI / 假设-CJ 题面或口径键；**禁**复用 CJ/CI/CH/CG/CF/CE/CD/O/M/K/CA/CB/CC 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有路径、同一未复权价、同一 T+1、同一板上容量/排队位次/成交时点与停牌/涨跌停可成交/集合竞价可成交/复牌首日可成交/盘后固定价可成交/上市首日可成交/退市整理期可成交/大宗量价与三通道分列/盘后通道存在等输入（A/AR/D/CD/CE/CF/CG/CH/CI/CJ/O/M 层诚实或显式旁路声明「本页不重开板上容量门槛/假队首/开收时点与停牌期间假成交/连续竞价涨跌停全额可成/集合竞价全额可成/复牌首日全额可成/盘后固定价全额可成/上市首日全额可成/退市整理期全额可成/大宗量价并进竞价与三通道混用/盘后通道存在」）下，把「协议/成交申报大宗订单必能按目标价或谈妥价全额成交」或「全样本用核对日当天更宽『协议大宗一律全额可成』规则回放历史」当成默认，相对「每个交易日按当时有效协议大宗门槛/确认时点/对手盘约束 PIT（未达30万股或200万门槛记失败；确认窗外记未成/部分；无对手盘按事先写死规则或记未成；缺字段 skip/敏感性；不抢 A 真数席位；不把大宗腿并进竞价可成）」的诚实组，会**系统性发明假全额可成路径并高估大宗腿可实现成交、低估门槛未达、确认窗外失败与假对手盘**；差异应**集中在协议大宗可成交性误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、门槛失败差、确认窗外失败差/假对手盘冲击差在标定噪声带内可忽略，且「假全额可成 / 核对日泄露 / 协议大宗窗 / vs A·CJ·CI·CH·CG·CF·CE·CD·O·M·C·K·CA·CB·CC·AR·AG·AN·W·X·T·S·U·V」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 与 ck0 与锚 **三条已冻**）

```
# 配置写死键（见 §7；预检有条件通过 · 三条已冻 · 待复检；下列已写死冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CK；≠ 单字母假设-C；≠ 单字母假设-K；≠ 单字母假设-O；≠ 单字母假设-A；≠ 单字母假设-M；≠ 双字母假设-CA/CB/CC/CD/CE/CF/CG/CH/CI/CJ
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CK；≠ 单字母假设-G
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CK；≠ 单字母假设-N；亦≠实验字母 BN
# params.fill_time 写死冻结 next_open
# params.asof_check_date 写死冻结 2026-10-16
# params.px_basis 建议 unadj
# params.block_trade_fill_honest 写死冻结 pit_by_block_trade_fill_rule
# params.block_trade_fill_scope 写死冻结 assume_block_trade_always_fillable_at_target_or_negotiated
# params.block_trade_fill_over_policy 写死冻结 fail_or_partial_or_fail_missing_block_trade_rule
# params.block_threshold_shares 建议 300000
# params.block_threshold_notional 建议 2000000
# params.board_capacity_handoff 建议 a_page
# params.queue_handoff 建议 ar_page
# params.fill_time_suspend_handoff 建议 d_page
# params.beyond_limit_handoff 建议 ag_page
# params.limit_up_fill_handoff 建议 cd_page
# params.limit_down_fill_handoff 建议 ce_page
# params.call_auction_fill_handoff 建议 cf_page
# params.resume_halt_fill_handoff 建议 cg_page
# params.after_hours_fill_handoff 建议 ch_page
# params.ipo_day1_fill_handoff 建议 ci_page
# params.delist_period_fill_handoff 建议 cj_page
# params.block_liquidity_handoff 建议 o_page     # 大宗量价/三通道混用交 O；CK≠O；严禁复用假设-O
# params.aft_channel_handoff 建议 m_page
# params.exit_period_handoff 建议 h_page
# params.universe_pool_handoff 建议 c_page
# params.maint_ratio_formula_handoff 建议 ca_page
# params.financing_rollover_handoff 建议 cb_page
# params.delist_force_deadline_handoff 建议 cc_page
# params.block_trade_fill_handoff 建议 self
# params.shortable_list_handoff 建议 k_page
# params.ck0_primary_demo                写死冻结 invent_assume_block_trade_always_fillable
# params.ck0_invent_assume_block_trade_always_fillable 建议 True
# params.ck1_asof_leak_block_trade_always_fillable_only 建议 True
# params.ck2_pit_block_trade_fill 建议 True
# params.merge_with_A_fill 建议 False
# params.merge_with_AR_queue 建议 False
# params.merge_with_D_fill_time 建议 False
# params.merge_with_C_universe_pool 建议 False
# params.merge_with_O_block_liquidity 建议 False
# params.merge_with_M_aft_channel 建议 False
# params.merge_with_H_exit_period 建议 False
# params.merge_with_K_shortable_list 建议 False
# params.merge_with_CA_maint_ratio_formula 建议 False
# params.merge_with_CB_financing_rollover 建议 False
# params.merge_with_CC_delist_force_deadline 建议 False
# params.merge_with_CD_limit_up_fill 建议 False
# params.merge_with_CE_limit_down_fill 建议 False
# params.merge_with_CF_call_auction_fill 建议 False
# params.merge_with_CG_resume_halt_fill 建议 False
# params.merge_with_CH_after_hours_fill 建议 False
# params.merge_with_CI_ipo_day1_fill 建议 False
# params.merge_with_CJ_delist_period_fill 建议 False
# params.merge_with_AG_beyond_limit 建议 False
# params.missing_block_trade_fill_policy 建议 skip
# params.day_freq_proxy 建议 block_trade_fill_sensitivity
# params.universe_rule 建议 sse_szse_block_trade_fill_misopen_check
# params.fail_policy 写死冻结 skip
# params.redline_v0_exempt_scope 建议 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 CK；params.G≠实验字母 CK；params.N≠实验字母 CK；禁 null/holdout；勿改已冻他字母数值）
# params.date_start / date_end 建议 2019-01-01..2026-09-30
# params.oos_split.*                     建议四日期；禁 holdout 反调
# CK0：假全额可成——协议/成交申报大宗订单按目标价或谈妥价 100% 成交
# CK1：仅 asof 日更宽「协议大宗一律全额可成」规则泄露铺满
# CK2：每个交易日 d 按当时已生效协议大宗门槛/确认时点/对手盘约束 PIT
# 缺协议大宗可成交约束字段 → skip（params.missing_block_trade_fill_policy）
```

### 2.2 三组对照（CK0 / CK1 / CK2）

| 组 | 角色 | 规则 |
|----|------|------|
| CK0 | 天真 / 假全额可成 | 按 `ck0_primary_demo` **写死冻结**单一主报 `invent_assume_block_trade_always_fillable`：协议/成交申报大宗订单按目标价或谈妥价 100% 成交（**禁**与 `invent_asof_leak_block_trade_always_fillable` 双挂主报） |
| CK1 | 半泄露 | 仅核对日（asof）更宽「协议大宗一律全额可成」规则泄露铺满全历史；**不得升格并列主报**（已冻：CK1不升格） |
| CK2 | 诚实 PIT | `block_trade_fill_honest=pit_by_block_trade_fill_rule`（已冻结）：每个交易日按当时已生效协议大宗门槛/确认时点/对手盘约束；缺字段 skip |

### 2.3 额度窗内时频可落点（写明但不真跑）

主窗建议 `2019-01-01..2026-09-30`（额度窗内）；asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。本页**不开回测**；不拉真数；不做实盘。

### 3.1 oos_split（建议四日期；拉数前冻结；禁 holdout 反调）

建议四段日期写死于拉数前；**禁止** holdout 反调；具体四日期待预检与额度窗对齐后冻结。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（CK0）/ 半泄露组（CK1）相对诚实组（CK2）的假全额可成贡献差、可实现成交差、门槛失败差、确认窗外失败差/假对手盘冲击差**显著且集中在协议大宗可成交性误开桶**；分桶「假全额可成 / 核对日泄露 / 协议大宗窗 / vs A·CJ·CI·CH·CG·CF·CE·CD·O·M·C·K·CA·CB·CC…」不改变主结论方向。

### 3.2 失败（假设不成立 / 设计失效）

上述差异在标定噪声带内可忽略；或差异主要由 A/CJ/CI/CH/CG/CF/CE/CD/O/M/C 等旁路页解释而非本页主病；或缺字段过多导致有效样本不足；或 oos/holdout 反调污染。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CK0/CK1/CK2。报告假全额可成贡献差、可实现成交差、门槛失败差、确认窗外失败差/假对手盘冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前冻结；禁 holdout 改桶）

建议默认桶名（待预检冻结）：`invent_assume_block_trade_always_fillable` / `invent_asof_leak_block_trade_always_fillable` / `vs_A_board_capacity` / `vs_CJ_delist_period_fill` / `vs_CI_ipo_day1_fill` / `vs_CH_after_hours_fill` / `vs_CG_resume_halt_fill` / `vs_CF_call_auction_fill` / `vs_CE_limit_down_fill` / `vs_CD_limit_up_fill` / `vs_O_block_liquidity` / `vs_M_aft_channel` / `vs_C_universe_pool` / `vs_K_shortable` / `vs_CA_maint_ratio` / `vs_CB_rollover` / `vs_CC_delist_force` / `vs_AR_queue` / `vs_AG_beyond_limit` / `vs_AN_auction_leftover` / `vs_W_exright` / `vs_X_st_limit` / `vs_AB_short_px` / `vs_T_csrc_fee` / `vs_S_handling_fee` / `vs_U_transfer_fee` / `vs_V_stamp_tax`。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 缺协议大宗门槛/确认时点/对手盘约束字段，静默当假全额可成（应 skip）。
- 把 O「大宗量价并进竞价/三通道混用」已诚实误写成「协议大宗可成交性已诚实」。
- 把 CJ 退市整理期 / CI 上市首日 / CG 复牌首日 / CH 盘后 / CF 集合 / CD·CE 涨跌停可成交已诚实误写成协议大宗可成交已诚实。
- 把 A 真数队列或把 CK 做成 A/O/CJ 续篇。
- `ck0_primary_demo` 与 asof_leak 双挂主报；CK1 升格并列主报。
- 扩窗出额度、改已冻 Y/G/N/Y2、标纸面齐、开回测/真数/实盘。
- 实验字母 CK 与单字母 C/K/O/A/M 或双字母 CA–CJ 或 params.Y/G/N 混读。
- **复用假设-K 融券名单题面**。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 未复权 OHLC / 买卖方向 / T+1 信号日。
- 协议/成交申报大宗腿代理、谈妥价/目标价、门槛（股数/金额）、确认时点窗标签、对手盘有无代理。
- 当时有效协议大宗规则及生效日（门槛、确认窗、有板/无板价限）。
- A/AR/D/CD/CE/CF/CG/CH/CI/CJ/O/M/C/K/CA/CB/CC 旁路诚实标记或显式旁路声明。
- 交易日历；asof=2026-10-16 锚。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- hypothesis_id=`CK`；组 CK0/CK1/CK2。
- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`block_trade_fill_honest=pit_by_block_trade_fill_rule`；`block_trade_fill_scope=assume_block_trade_always_fillable_at_target_or_negotiated`；`block_trade_fill_over_policy=fail_or_partial_or_fail_missing_block_trade_rule`；`fail_policy=skip`；`ck0_primary_demo=invent_assume_block_trade_always_fillable`（**写死冻结**单一主报；禁双挂 asof_leak；CK1不升格）。
- 锚升格写死（不可再写「建议」）：`block_trade_fill_honest=pit_by_block_trade_fill_rule`；`block_trade_fill_scope=assume_block_trade_always_fillable_at_target_or_negotiated`；`block_trade_fill_over_policy=fail_or_partial_or_fail_missing_block_trade_rule`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CK**；**params.G≠实验字母 CK**；**params.N≠实验字母 CK**；禁 null/holdout；**勿改已冻他字母数值**）。
- 主窗建议 `2019-01-01..2026-09-30`；门槛建议 `300000` 股 / `2000000` 元；oos_split 四日期建议写死+禁 holdout 反调。
- 全部 `merge_with_*=False`（见 §2.1）。
- **本页不开回测**；不催 8765；不抢 A 真数。

---

## 8. 结论

（空；本页不开回测；不写买卖建议。）

---

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-04）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 CK**；**`params.G` ≠ 实验字母 CK**；**`params.N` ≠ 实验字母 CK**；**`params.Y` ≠ 单字母实验 C/K/O/A/M/Z**；尤重**双字母 CK ≠ 单字母假设-A**；**双字母 CK ≠ 单字母假设-C**；**双字母 CK ≠ 单字母假设-K**；**双字母 CK ≠ 单字母假设-O**；**双字母 CK ≠ 单字母假设-M**；**双字母 CK ≠ 双字母假设-CJ/CI/CH/CG/CF/CE/CD/CA/CB/CC**；禁 null/holdout/跑后改口；**勿改他字母已冻 Y/G/N/Y2**。  
2. **`params.ck0_primary_demo`**：**写死冻结** **`invent_assume_block_trade_always_fillable`**；禁与 **`invent_asof_leak_block_trade_always_fillable`** 双挂争主表（只挂一个 primary）；**CK1 半泄露不得升格并列主报**。  
3. **协议大宗可成交性锚升格写死（不可再写「建议」）**：`params.block_trade_fill_honest=pit_by_block_trade_fill_rule`；`params.block_trade_fill_scope=assume_block_trade_always_fillable_at_target_or_negotiated`；`params.block_trade_fill_over_policy=fail_or_partial_or_fail_missing_block_trade_rule`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。

**硬分列保留**：CK≠C/K/O/CA–CJ/A/M…；**尤其 CK≠O / CK≠CJ / CK≠CI / CK≠CH / CK≠CG / CK≠CF / CK≠CE / CK≠CD / CK≠A**；**双字母 CK ≠ 单字母假设-C / 假设-K / 假设-O / 假设-A / 假设-M**；**严禁复用假设-K / 假设-O / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-C / 假设-M**；**params.Y/G/N ≠ 实验字母 CK**。

**状态**：预检有条件通过 · 三条已冻 · 待复检；**禁止标任何纸面齐**；本页不开回测/真数/实盘；不改已冻 CJ/Y–CJ。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 风控预检补丁·冻结三条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CK**；**params.G≠实验字母 CK**；**params.N≠实验字母 CK**；亦≠单字母实验 C/K/O/A/M/Z；尤重**双字母 CK ≠ 单字母假设-A/C/K/O/M**；**双字母 CK ≠ 双字母假设-CJ/CI/CH/CG/CF/CE/CD/CA/CB/CC**；禁 null/holdout/跑后改口）；② `params.ck0_primary_demo=invent_assume_block_trade_always_fillable` 单一主报写死（禁与 `invent_asof_leak_block_trade_always_fillable` 双挂；CK1不升格）；③ 锚升格写死 `block_trade_fill_honest=pit_by_block_trade_fill_rule` / `scope=assume_block_trade_always_fillable_at_target_or_negotiated` / `over_policy=fail_or_partial_or_fail_missing_block_trade_rule` / `asof=2026-10-16` / `fill_time=next_open` / `fail=skip`；状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；不改已冻 CJ/Y–CJ；不开回测/真数/实盘。基线 tip=`270f9e8`（祖先 `294dd33`）。 |
| 2026-11-04 | 新建草稿·待入库预检（总管线：CJ 补丁 tip=`991e4cf` 已交后写 CK；选题协议大宗可成交性误开；ck0 建议 `invent_assume_block_trade_always_fillable`；清单约 #94；**禁止标任何纸面齐**）。 |

