# 假设 CI · 新股上市首日可成交性误开 / 默认新股/次新上市首日订单必能按目标价或开盘价/收盘价全额成交（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CH 补丁已交（tip=`13a2363`；复检/入库另线并行后写下一纸面 CI）；清单撞题规则另选正交执行缺口（**回测默认「新股/次新上市首日订单必能按目标价或开盘价/收盘价全额成交」** ≠ 假设-CH 盘后固定价格可成交性误开 ≠ 假设-CG 停牌复牌首日可成交性误开 ≠ 假设-CF 集合竞价可成交性误开 ≠ 假设-CE 跌停板可成交性误开 ≠ 假设-CD 涨停板可成交性误开 ≠ 假设-A 板上枯竭/一字与封板容量主实验 ≠ 假设-G 涨跌幅规则PIT新股窗 ≠ 假设-J 无板日临停 ≠ 假设-I 价格笼子远限价（**双字母 CI ≠ 单字母假设-I**） ≠ 假设-D 成交时点开vs收与停牌假成交 ≠ 假设-C 股票池当时名单 ≠ 假设-CA/CB/CC 两融族）；选题自 `事实与坑`「新股上市首日开盘大幅偏离、临停与流动性枯竭；回测用目标价/开盘价/收盘价一律全额成交等于假设永远可成」+ 口径「执行鸿沟」+ 与 CD/CE/CF/CG/CH 可成交性族正交、与 G 新股涨跌幅窗正交、与 J 临停触发正交；本页**假定板上容量层（A）/ 排队位次层（AR）/ 成交时点与停牌层（D）/ 超涨跌停价无效层（AG）/ 涨停可成交误开层（CD）/ 跌停可成交误开层（CE）/ 集合竞价可成交误开层（CF）/ 停牌复牌首日可成交误开层（CG）/ 盘后固定价格可成交误开层（CH）/ 涨跌幅规则新股窗层（G）/ 无板日临停层（J）/ 价格笼子层（I）诚实或显式旁路**，主病只在**发明「新股/次新上市首日订单必能按目标价或开盘价/收盘价全额成交」这一误开默认**；**A 正文主测「涨停可成交性/板上枯竭」真数队列**（**双字母 CI ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 续篇；不抢 A 真数队列**），**G 正文主测「涨跌幅规则PIT新股窗」**（涨跌幅标签切日 ≠ 上市首日全额可成；**严禁改 G**），**J 正文主测「无板日临停」**（临停触发标签 ≠ 上市首日全额可成；**严禁改 J**），**I 正文主测「价格笼子远限价」**（**双字母 CI ≠ 单字母假设-I；严禁复用 I**），**CH 正文主测「盘后固定价格可成交性误开」**（`invent_assume_after_hours_fixed_price_always_fillable`；盘后固定价 ≠ 上市首日；**严禁改 CH**），**CG 正文主测「停牌复牌首日可成交性误开」**（`invent_assume_resume_from_halt_always_fillable`；复牌首日 ≠ 上市首日；**严禁改 CG**），**CF/CE/CD 正文主测集合/跌停/涨停可成交误开**（**严禁改 CF/CE/CD**），**C 正文主测「股票池当时名单」**（**双字母 CI ≠ 单字母假设-C；严禁复用 C**），**CA/CB/CC 正文主测两融族**（与本页正交；**严禁改 CA/CB/CC**）→ 自立；与假设 B/Z/BA–CH/AG/AF/E/L/X/W/K/AB/N/O/AN 等**分列**；**新建实验 CI**  
状态：**草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；禁止把「新股/次新上市首日订单必能按目标价或开盘价/收盘价全额成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CH 及其他 A/D–CH 已交正文与冻结补丁；尤其不改假设-CH；尤其不改假设-CG；尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-A；尤其不改假设-C；尤其不改假设-G；尤其不改假设-J；尤其不改假设-I；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；勿再改 CH/CG/CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN/M/N/O/G/J/I**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CI（约 #92）。与假设 **CH（盘后固定价格可成交性误开）** **硬分列（专节强调）**：CH = 回测是否默认「**盘后固定价格交易时段**订单必能按收盘价/固定价**全额**成交」；本页 = 回测是否默认「**新股/次新上市首日**订单必能按目标价或开盘价/收盘价**全额**成交」；盘后固定价 ≠ 上市首日；**严禁复用 CH 题面或 `invent_assume_after_hours_fixed_price_always_fillable`**；**尤其不改假设-CH**。**CI≠CH**。与假设 **CG（停牌复牌首日可成交性误开）** **硬分列（专节强调）**：CG = 停牌复牌首日全额可成误开；本页 = 新股上市首日全额可成误开；复牌首日 ≠ 上市首日；**严禁复用 CG 题面或 `invent_assume_resume_from_halt_always_fillable`**；**尤其不改假设-CG**。**CI≠CG**。与假设 **CF（集合竞价可成交性误开）** **硬分列（专节强调）**：CF = 开盘/收盘集合竞价全额可成误开；本页 = 上市首日全额可成误开；集合撮合 ≠ 上市首日可成交默认；**严禁复用 CF 题面或 `invent_assume_call_auction_always_fillable`**；**尤其不改假设-CF**。**CI≠CF**。与假设 **CE（跌停板可成交性误开）** **硬分列（专节强调）**：CE = 连续竞价跌停侧全额可卖出误开；本页 = 上市首日全额可成误开；**严禁复用 CE 题面或 `invent_assume_limit_down_always_fillable`**；**尤其不改假设-CE**。**CI≠CE**。与假设 **CD（涨停板可成交性误开）** **硬分列（专节强调）**：CD = 连续竞价涨停侧全额可成误开；本页 = 上市首日全额可成误开；**严禁复用 CD 题面或 `invent_assume_limit_up_always_fillable`**；**尤其不改假设-CD**。**CI≠CD**。与假设 **A（涨停可成交性/板上枯竭）** **硬分列（专节强调）**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成的**主实验与真数队列**；本页 = **纸面机制误开点**：回测/仿真是否默认发明「新股/次新上市首日订单必能按目标价或开盘价/收盘价全额成交」并系统性高估上市首日可实现成交、低估开盘大幅偏离、临停与流动性枯竭；容量门槛 ≠ 上市首日全额可成默认；**双字母 CI ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不占** A 的 A0/A1 主报与真数席位；**尤其不改假设-A**。**CI≠A**。与假设 **G（涨跌幅规则PIT新股窗）** **硬分列**：G = 新股窗涨跌幅标签切日；本页 = 上市首日全额可成误开；标签规则 ≠ 可成交默认；**尤其不改假设-G**。**CI≠G**。与假设 **J（无板日临停）** **硬分列**：J = 无板日 30%/60% 临停触发；本页 = 上市首日全额可成误开；临停触发 ≠ 全额可成默认；**尤其不改假设-J**。**CI≠J**。与假设 **I（价格笼子远限价）** **硬分列（专节强调）**：I = 连续竞价价格笼子远限价；本页 = 上市首日全额可成误开；**双字母 CI ≠ 单字母假设-I**；**严禁复用 I**；**尤其不改假设-I**。**CI≠I**。与假设 **C（股票池当时名单）** **硬分列**：C = 成分/股票池 PIT；本页 = 上市首日全额可成误开；**双字母 CI ≠ 单字母假设-C**；**严禁复用 C**。**CI≠C**。与假设 **CA/CB/CC** **硬分列**：两融公式/展期/调出了结时限 ≠ 上市首日全额可成；**尤其不改 CA/CB/CC**。**CI≠CA≠CB≠CC**。与假设 **AR/AG/AN/BZ/BY/BX/BW…** 及两融审批/费用族 **硬分列**：假队首/超板无效/集合剩单/两融审批费用 ≠ 上市首日全额可成默认。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A / 假设-C / 假设-I / 假设-G / 假设-J / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH**。**严禁改写/续写假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-G / 假设-J / 假设-I / 假设-CA / 假设-CB / 假设-CC**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CI** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 I**（价格笼子远限价；**严禁复用假设-I**）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **单字母实验 G**（涨跌幅规则PIT新股窗；**严禁改写假设-G**）≠ **单字母实验 J**（无板日临停；**严禁改写假设-J**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **双字母实验 CB**（融资展期审批；**严禁改写假设-CB**）≠ **双字母实验 CC**（调出强制了结时点；**严禁改写假设-CC**）≠ **双字母实验 CD**（涨停板可成交性误开；**严禁改写假设-CD**）≠ **双字母实验 CE**（跌停板可成交性误开；**严禁改写假设-CE**）≠ **双字母实验 CF**（集合竞价可成交性误开；**严禁改写假设-CF**）≠ **双字母实验 CG**（停牌复牌首日可成交性误开；**严禁改写假设-CG**）≠ **双字母实验 CH**（盘后固定价格可成交性误开；**严禁改写假设-CH**）≠ **单字母实验 B** ≠ **单字母实验 Z** ≠ **单字母实验 K** ≠ **单字母实验 D** ≠ **单字母实验 H** ≠ **单字母实验 M**。全文凡写「实验 CI / 假设-CI / hypothesis_id=CI / 组 CI0·CI1·CI2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CI 混读或互改；**尤其 params.Y ≠ 实验字母 CI ≠ 单字母假设-C ≠ 单字母假设-I ≠ 单字母假设-A ≠ 单字母假设-G ≠ 单字母假设-J ≠ 双字母假设-CA ≠ 双字母假设-CB ≠ 双字母假设-CC ≠ 双字母假设-CD ≠ 双字母假设-CE ≠ 双字母假设-CF ≠ 双字母假设-CG ≠ 双字母假设-CH**。亦**禁止**把实验字母 CI 与单字母 **A/B/C/D/E/F/G/H/I/J/K/M/N/O/T/S/U/V/W/X/Y/Z**、双字母 **BA–CH**、双字母 **CA/CB/CC/CD/CE/CF/CG/CH/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ**、双字母 **AB**、双字母 **AI/AJ/AQ**、双字母 **AZ/AY/AX/AW**、或 params 键名 `ci0_*` 以外的实验页混读。**双字母 CI ≠ 单字母 C ≠ 单字母 I ≠ 单字母 A ≠ 单字母 G ≠ 单字母 J ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 D ≠ 单字母 H ≠ 单字母 M ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 CC ≠ 双字母 CD ≠ 双字母 CE ≠ 双字母 CF ≠ 双字母 CG ≠ 双字母 CH ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 AN ≠ 双字母 AI ≠ 双字母 AJ ≠ 双字母 AQ ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BF ≠ 双字母 BQ ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB**；**params.Y ≠ 实验字母 CI**；**params.G ≠ 实验字母 CI**；**params.N ≠ 实验字母 CI**。**带过：双字母 CH ≠ C/H/CA–CG/A/M…；双字母 CG ≠ C/G/CA–CF/A/D…；双字母 CF ≠ C/F/CA–CE/A/Y…；双字母 CE ≠ C/E/CA/CB/CC/CD/AR…；双字母 CD ≠ A/C/D/CA/CB/CC/AR…；双字母 CC ≠ C/CA/CB/BQ/BY/BZ/BF…；双字母 CB ≠ B/C/CA/BF/BZ…；双字母 CA ≠ A/C/BZ/BY…；双字母 AR ≠ A/R/AQ…；双字母 AI ≠ A/I…；双字母 AJ ≠ A/J…；双字母 AQ ≠ A/Q/I/AI…；双字母 BZ ≠ Z/BY/BX…；双字母 BY ≠ Y/BX/BW…；双字母 BX ≠ X/BW…；双字母 BW ≠ W/BV…；双字母 BV ≠ V/BU/BT…；双字母 BU ≠ U/BB/BT/K…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BP ≠ P/BO/W；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CI ≠ 单字母假设-A / 假设-C / 假设-I / 假设-G / 假设-J；且 ≠ 假设-CA / 假设-CB / 假设-CC / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH；带过 CH≠CG/CF/CE/CD、params.Y≠CI（硬）

| 维度 | 对照页 | 本页假设-CI（双字母） |
|------|--------|----------------------|
| 题面 CH | **盘后固定价格可成交性误开**（`invent_assume_after_hours_fixed_price_always_fillable`） | **新股上市首日可成交性误开**：默认「新股/次新上市首日订单必能按目标价或开盘价/收盘价全额成交」vs 诚实上市首日撮合/临停/流动性约束；盘后固定价 ≠ 上市首日；**严禁复用 CH 题面**；**CI≠CH**；**不改 CH** |
| 题面 CG | **停牌复牌首日可成交性误开**（`invent_assume_resume_from_halt_always_fillable`） | 复牌首日 ≠ 上市首日；**严禁复用 CG 题面**；**CI≠CG**；**不改 CG** |
| 题面 CF | **集合竞价可成交性误开**（`invent_assume_call_auction_always_fillable`） | 集合竞价 ≠ 上市首日全额可成默认；**严禁复用 CF 题面**；**CI≠CF**；**不改 CF** |
| 题面 CE | **跌停板可成交性误开**（`invent_assume_limit_down_always_fillable`；连续竞价跌停侧） | 连续竞价跌停侧 ≠ 上市首日全额可成；**严禁复用 CE 题面**；**CI≠CE**；**不改 CE** |
| 题面 CD | **涨停板可成交性误开**（`invent_assume_limit_up_always_fillable`；连续竞价涨停侧） | 连续竞价涨停侧 ≠ 上市首日全额可成；**严禁复用 CD 题面**；**CI≠CD**；**不改 CD** |
| 题面 A | **涨停可成交性/板上枯竭**（清单实验 A；真数队列） | 容量门槛 ≠ 上市首日全额可成默认；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不抢 A 真数队列**；**CI≠A** |
| 题面 G | **涨跌幅规则PIT新股窗**（清单实验 G） | 涨跌幅标签切日 ≠ 上市首日全额可成；**严禁复用 G 题面作主病**；**CI≠G**；**不改 G** |
| 题面 J | **无板日临停**（清单实验 J） | 临停触发标签 ≠ 上市首日全额可成默认；**严禁复用 J 题面作主病**；**CI≠J**；**不改 J** |
| 题面 I | **价格笼子远限价**（清单实验 I） | 连续笼子 ≠ 上市首日全额可成；**双字母 CI ≠ 单字母假设-I**；**严禁复用 I**；**CI≠I**；**不改 I** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 股票池 ≠ 上市首日全额可成；**严禁复用 C**；**CI≠C** |
| 题面 CA | **维持担保比例分子分母口径** | 公式 ≠ 上市首日全额可成；**CI≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批** | 展期审批 ≠ 上市首日全额可成；**CI≠CB**；**不改 CB** |
| 题面 CC | **两融标的调出强制了结时点** | 调出了结时限 ≠ 上市首日全额可成；**CI≠CC**；**不改 CC** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_assume_ipo_day1_always_fillable`（**写死冻结**单一主报；禁双挂 asof_leak；CI1不升格） |
| 文档 | 清单实验 A / C / I / G / J / `假设-CA-…` / `假设-CB-…` / `假设-CC-…` / `假设-CD-…` / `假设-CE-…` / `假设-CF-…` / `假设-CG-…` / `假设-CH-…`（**只读；禁止改写**） | `假设-CI-新股上市首日可成交性误开.md`（新建） |
| 预检键 | 实验字母 A / C / I / G / J / CA / CB / CC / CD / CE / CF / CG / CH | 实验字母 **CI** / `ci0_primary_demo`；**不得**占用或改写预检 A/C/I/G/J/CA/CB/CC/CD/CE/CF/CG/CH |

**禁止**：把 CI 写成「A/CH/CG/CF/CE/CD/G/J/I/C/CA/CB/CC 的续篇」；把「板上容量已诚实（A）/ 盘后固定价可成交已诚实（CH）/ 复牌首日可成交已诚实（CG）/ 集合竞价可成交已诚实（CF）/ 跌停可成交已诚实（CE）/ 涨停可成交已诚实（CD）/ 新股涨跌幅窗已诚实（G）/ 临停触发已诚实（J）/ 价格笼子已诚实（I）/ 股票池已诚实（C）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「新股上市首日可成交性已诚实」；覆盖或补丁改写假设-A / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-G / 假设-J / 假设-I / 假设-C / 假设-CA / 假设-CB / 假设-CC 正文；把 `params.Y/G/N` 与实验字母 CI 混读；**禁** `ci0_primary_demo` 与 `invent_asof_leak_ipo_day1_always_fillable` **双挂主报**；**禁** CI1 半泄露升格并列主报；**禁**复用假设-A / 假设-C / 假设-I / 假设-G / 假设-J / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH 题面或口径键；**禁**复用 CH/CG/CF/CE/CD/G/J/I/CA/CB/CC 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有路径、同一未复权价、同一 T+1、同一板上容量/排队位次/成交时点与停牌/涨跌停可成交/集合竞价可成交/复牌首日可成交/盘后固定价可成交/新股涨跌幅窗/临停触发/价格笼子等输入（A/AR/D/CD/CE/CF/CG/CH/G/J/I 层诚实或显式旁路声明「本页不重开板上容量门槛/假队首/开收时点与停牌期间假成交/连续竞价涨跌停全额可成/集合竞价全额可成/复牌首日全额可成/盘后固定价全额可成/新股涨跌幅标签/临停触发标签/价格笼子」）下，把「新股/次新上市首日订单必能按目标价或开盘价/收盘价全额成交」或「全样本用核对日当天更宽『上市首日一律全额可成』规则回放历史」当成默认，相对「每个交易日按当时有效上市首日撮合/临停/流动性约束 PIT（开盘大幅偏离记冲击；临停窗记未成/部分；流动性枯竭按事先写死规则或记未成；缺字段 skip/敏感性；不抢 A 真数席位）」的诚实组，会**系统性发明假全额可成路径并高估上市首日可实现成交、低估开盘大幅偏离、临停与流动性枯竭**；差异应**集中在新股上市首日可成交性误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、开盘偏离冲击差、临停/枯竭失败差在标定噪声带内可忽略，且「假全额可成 / 核对日泄露 / 上市首日窗 / vs A·CH·CG·CF·CE·CD·G·J·I·C·CA·CB·CC·AR·AG·AN·W·X·K·AB·T·S·U·V」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 与 ci0 与锚 **三条已冻**）

```
# 配置写死键（见 §7；预检有条件通过 · 三条已冻 · 待复检；下列已写死冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CI；≠ 单字母假设-C；≠ 单字母假设-I；≠ 单字母假设-A；≠ 单字母假设-G；≠ 单字母假设-J；≠ 双字母假设-CA/CB/CC/CD/CE/CF/CG/CH
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CI；≠ 单字母假设-G
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CI；≠ 单字母假设-N；亦≠实验字母 BN
# params.fill_time 写死冻结 next_open
# params.asof_check_date 写死冻结 2026-10-16
# params.px_basis 建议 unadj
# params.ipo_day1_fill_honest 写死冻结 pit_by_ipo_day1_fill_rule
# params.ipo_day1_fill_scope 写死冻结 assume_ipo_day1_always_fillable_at_target_or_open_or_close
# params.ipo_day1_fill_over_policy 写死冻结 fail_or_partial_or_fail_missing_ipo_day1_rule
# params.board_capacity_handoff 建议 a_page
# params.queue_handoff 建议 ar_page
# params.fill_time_suspend_handoff 建议 d_page
# params.beyond_limit_handoff 建议 ag_page
# params.limit_up_fill_handoff 建议 cd_page
# params.limit_down_fill_handoff 建议 ce_page
# params.call_auction_fill_handoff 建议 cf_page
# params.resume_halt_fill_handoff 建议 cg_page
# params.after_hours_fill_handoff 建议 ch_page
# params.limit_rule_ipo_window_handoff 建议 g_page
# params.nolimit_halt_handoff 建议 j_page
# params.price_cage_handoff 建议 i_page
# params.auction_vol_handoff 建议 y_page
# params.auction_leftover_handoff 建议 an_page
# params.lot_size_handoff 建议 e_page
# params.limit_round_handoff 建议 f_page
# params.universe_pool_handoff 建议 c_page
# params.maint_ratio_formula_handoff 建议 ca_page
# params.financing_rollover_handoff 建议 cb_page
# params.delist_force_deadline_handoff 建议 cc_page
# params.ipo_day1_fill_handoff 建议 self
# params.exright_board_handoff 建议 w_page
# params.st_limit_handoff 建议 x_page
# params.shortable_list_handoff 建议 k_page
# params.short_px_handoff 建议 ab_page
# params.stamp_tax_handoff 建议 v_page
# params.transfer_fee_handoff 建议 u_page
# params.csrc_fee_handoff 建议 t_page
# params.handling_fee_handoff 建议 s_page
# params.ci0_primary_demo                写死冻结 invent_assume_ipo_day1_always_fillable
# params.ci0_invent_assume_ipo_day1_always_fillable 建议 True
# params.ci1_asof_leak_ipo_day1_always_fillable_only 建议 True
# params.ci2_pit_ipo_day1_fill 建议 True
# params.merge_with_A_fill 建议 False
# params.merge_with_AR_queue 建议 False
# params.merge_with_D_fill_time 建议 False
# params.merge_with_C_universe_pool 建议 False
# params.merge_with_I_price_cage 建议 False
# params.merge_with_G_limit_rule_ipo 建议 False
# params.merge_with_J_nolimit_halt 建议 False
# params.merge_with_CA_maint_ratio_formula 建议 False
# params.merge_with_CB_financing_rollover 建议 False
# params.merge_with_CC_delist_force_deadline 建议 False
# params.merge_with_CD_limit_up_fill 建议 False
# params.merge_with_CE_limit_down_fill 建议 False
# params.merge_with_CF_call_auction_fill 建议 False
# params.merge_with_CG_resume_halt_fill 建议 False
# params.merge_with_CH_after_hours_fill 建议 False
# params.merge_with_AG_beyond_limit 建议 False
# params.merge_with_B_legacy 建议 False
# params.merge_with_Z_margin_ratio 建议 False
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
# params.missing_ipo_day1_fill_policy 建议 skip
# params.day_freq_proxy 建议 ipo_day1_fill_sensitivity
# params.universe_rule 建议 sse_szse_ipo_day1_fill_misopen_check
# params.fail_policy 写死冻结 skip
# params.redline_v0_exempt_scope 建议 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015
# params.date_start / date_end 建议 2019-01-01..2026-09-30
# params.oos_split.*                     建议四日期；禁 holdout 反调
```

可编码摘要（伪代码，不开跑）：

```
asof = params.asof_check_date  # 写死冻结 2026-10-16
# CI0：假全额可成——新股/次新上市首日订单按目标价或开盘价/收盘价 100% 成交
# CI1：仅 asof 日更宽「上市首日一律全额可成」规则泄露铺满
# CI2：每个交易日 d 按当日已生效上市首日撮合/临停/流动性约束 PIT
# 缺上市首日可成交约束字段 → skip（params.missing_ipo_day1_fill_policy）
```

```
fill_time = "next_open"  # 写死冻结
asof_check_date = "2026-10-16"  # 写死冻结
px_basis = "unadj"
ipo_day1_fill_honest = "pit_by_ipo_day1_fill_rule"  # 写死冻结
ipo_day1_fill_scope = "assume_ipo_day1_always_fillable_at_target_or_open_or_close"  # 写死冻结
ipo_day1_fill_over_policy = "fail_or_partial_or_fail_missing_ipo_day1_rule"  # 写死冻结
ci0_primary_demo = "invent_assume_ipo_day1_always_fillable"  # 写死冻结单一主报；禁与 invent_asof_leak_ipo_day1_always_fillable 双挂
ci0_invent_assume_ipo_day1_always_fillable = True
ci1_asof_leak_ipo_day1_always_fillable_only = True
ci2_pit_ipo_day1_fill = True
merge_with_A_fill = False
merge_with_AR_queue = False
merge_with_D_fill_time = False
merge_with_C_universe_pool = False
merge_with_I_price_cage = False
merge_with_G_limit_rule_ipo = False
merge_with_J_nolimit_halt = False
merge_with_CA_maint_ratio_formula = False
merge_with_CB_financing_rollover = False
merge_with_CC_delist_force_deadline = False
merge_with_CD_limit_up_fill = False
merge_with_CE_limit_down_fill = False
merge_with_CF_call_auction_fill = False
merge_with_CG_resume_halt_fill = False
merge_with_CH_after_hours_fill = False
fail_policy = "skip"
```

### 2.2 三组对照（CI0 / CI1 / CI2）

| 组 | 口径 | 说明 |
|----|------|------|
| CI0 天真 | `invent_assume_ipo_day1_always_fillable`（建议单一主报） | 发明假全额可成路径；禁与 invent_asof_leak_ipo_day1_always_fillable 双挂 |
| CI1 半泄露·混口径 | 全样本用 `asof_check_date` 当天更宽「上市首日一律全额可成」规则铺满历史 | 仅上市首日全额可成 asof 泄露；不升格并列主报 |
| CI2 PIT | `ipo_day1_fill_honest=pit_by_ipo_day1_fill_rule`（已冻结） | 每个交易日按当时已生效上市首日撮合/临停/流动性约束 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：上市首日窗标签代理 + 目标价/开盘价/收盘价全额成交默认 vs 诚实开盘偏离/临停/枯竭 → 当日可实现成交与失败笔；缺字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有未复权 OHLC + 上市日期/首日标签代理 + 成交意图代理即可纸面起步；**本页不开回测、不拉真数、不派回测岗、不抢 A 真数队列**。

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

天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、开盘偏离冲击差、临停/枯竭失败差超出标定噪声带，且差异集中在「新股上市首日可成交性误开」桶，不被 A 板上容量、CH 盘后固定价、CG 复牌首日、CF 集合竞价、CE 跌停可成交、CD 涨停可成交、G 新股涨跌幅窗、J 临停触发、I 价格笼子、C 股票池、CA/CB/CC 两融族等他页桶吞并。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 A/CH/CG/CF/CE/CD/G/J/I/C/CA/CB/CC/AR/AG/AN/T 等他页桶吞并；或 holdout 反调 `ci0_primary_demo` / Y·G·N·Y2；或 CI0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CI0 / CI1 / CI2。报告可实现成交差、假全额可成贡献差、开盘偏离冲击差、临停/枯竭失败差。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_assume_ipo_day1_always_fillable",
  "invent_asof_leak_ipo_day1_always_fillable",
  "ipo_day1_window",
  "open_gap_shock_window",
  "temp_halt_liquidity_window",
  "vs_A_limit_up_fill",
  "vs_CH_after_hours_fill",
  "vs_CG_resume_halt_fill",
  "vs_CF_call_auction_fill",
  "vs_CE_limit_down_fill",
  "vs_CD_limit_up_fill",
  "vs_G_limit_rule_ipo",
  "vs_J_nolimit_halt",
  "vs_I_price_cage",
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

1. 样本无足够上市首日窗/撮合与临停/流动性约束字段；缺字段却静默当假全额可成 → 设计失效。  
2. 把「板上容量已诚实（A）」静默写成「新股上市首日可成交性已诚实」且不声明另页 A → **与 A 撞题**（**尤其 CI≠A**；**严禁复用假设-A**；**绝不可做成 A 续篇**；**不抢 A 真数队列**）。  
3. 把「盘后固定价可成交已诚实（CH）」静默写成「新股上市首日可成交性已诚实」 → **与 CH 撞题**（盘后固定价 ≠ 上市首日；**尤其 CI≠CH**；**不改 CH**）。  
4. 把「复牌首日可成交已诚实（CG）」静默写成「新股上市首日可成交性已诚实」 → **与 CG 撞题**（复牌首日 ≠ 上市首日；**尤其 CI≠CG**；**不改 CG**）。  
5. 把「集合竞价可成交已诚实（CF）」静默写成「新股上市首日可成交性已诚实」 → **与 CF 撞题**（**尤其 CI≠CF**；**不改 CF**）。  
6. 把「跌停可成交已诚实（CE）」静默写成「新股上市首日可成交性已诚实」 → **与 CE 撞题**（**尤其 CI≠CE**；**不改 CE**）。  
7. 把「涨停可成交已诚实（CD）」静默写成「新股上市首日可成交性已诚实」 → **与 CD 撞题**（**尤其 CI≠CD**；**不改 CD**）。  
8. 把「新股涨跌幅窗已诚实（G）」静默写成「新股上市首日可成交性已诚实」 → **与 G 撞题**（标签规则 ≠ 全额可成默认；**尤其 CI≠G**；**不改 G**）。  
9. 把「临停触发已诚实（J）」静默写成「新股上市首日可成交性已诚实」 → **与 J 撞题**（临停触发 ≠ 全额可成默认；**尤其 CI≠J**；**不改 J**）。  
10. 把「价格笼子已诚实（I）」静默写成「新股上市首日可成交性已诚实」 → **与 I 撞题**（**尤其 CI≠I**；**双字母 CI ≠ 单字母假设-I**；**严禁复用假设-I**）。  
11. 把「股票池已诚实（C）」静默写成「新股上市首日可成交性已诚实」 → **与 C 撞题**（**尤其 CI≠C**；**严禁复用假设-C**）。  
12. 把「分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「新股上市首日可成交性已诚实」 → **与 CA/CB/CC 撞题**（与两融审批/费用类正交；**尤其 CI≠CA / CI≠CB / CI≠CC**；**不改 CA/CB/CC**）。  
13. 把「集合剩单/超板无效/整手/单笔上限/集合量分母已诚实」写成主病或不声明另页 → 与 AN/AG/E/AF/Y 撞题。  
14. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「新股上市首日可成交性已诚实」→ 与交易所费用族撞题（**明确避开预检T**）。  
15. 把实验字母 CI 与单字母 A/B/C/D/E/F/G/H/I/J/K/M/N/O/T/S/U/V/W/X/Y/Z 或双字母 BA–CH/CA/CB/CC/CD/CE/CF/CG/CH/AR/AG/AN/AI/AJ/AQ/BZ/BY/BF/BQ/BC/BT/BD/BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
16. holdout 反调 `ci0_primary_demo` / Y·G·N·Y2 → 结论无效。  
17. 用复权价代理上市首日可成交路径 → 标签与执行双错，结论无效。  
18. 用核对日更宽「假全额可成」当诚实 PIT、或把临时宽口径铺满历史 → 设计失效。  
19. **`ci0_primary_demo` 与 `invent_asof_leak_ipo_day1_always_fillable` 双挂主报**；或 CI1 升格并列主报 → 设计失效。  
20. **改写或覆盖 `假设-A` / `假设-CH` / `假设-CG` / `假设-CF` / `假设-CE` / `假设-CD` / `假设-G` / `假设-J` / `假设-I` / `假设-C` / `假设-CA` / `假设-CB` / `假设-CC` / 已冻 AA–CH** → 硬边界违约，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块、上市日期/首日标签代理；  
- 成交意图量、目标价/开盘价/收盘价全额成交默认 vs 诚实开盘偏离/临停/枯竭规则及生效日；  
- 板上容量 / 排队位次 / 开收时点与停牌 / 涨跌停可成交误开 / 集合竞价可成交误开 / 复牌首日可成交误开 / 盘后固定价可成交误开 / 新股涨跌幅窗 / 临停触发 / 价格笼子输入（消费 A/AR/D/CD/CE/CF/CG/CH/G/J/I 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历。

可选：注册制前后分段；与 A 容量窗、CH 盘后窗、CG 复牌窗、CF 集合竞价窗、CE/CD 涨跌停窗、G 新股涨跌幅窗、J 临停窗对照但不混主结论；缺上市首日约束原因码敏感性（主报仍在新股上市首日可成交性误开）。

**禁止**：用核对日「今天上市首日一律全额可成」铺满当唯一诚实组；用复权价；把板上容量已诚实/盘后固定价可成交已诚实/复牌首日可成交已诚实/集合竞价可成交已诚实/跌停可成交已诚实/涨停可成交已诚实/新股涨跌幅窗已诚实/临停触发已诚实/价格笼子已诚实/股票池已诚实/两融审批费用已诚实当成「新股上市首日可成交性正确」依据；把 A/CH/CG/CF/CE/CD/G/J/I/C/CA/CB/CC/AR/AG/AN/Z/BA–CH/K/AB/W/X/V/U/T/S 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`CI`  
- **组**：CI0 / CI1 / CI2  
- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`ipo_day1_fill_honest=pit_by_ipo_day1_fill_rule`；`ipo_day1_fill_scope=assume_ipo_day1_always_fillable_at_target_or_open_or_close`；`ipo_day1_fill_over_policy=fail_or_partial_or_fail_missing_ipo_day1_rule`；`board_capacity_handoff=a_page`；`queue_handoff=ar_page`；`fill_time_suspend_handoff=d_page`；`beyond_limit_handoff=ag_page`；`limit_up_fill_handoff=cd_page`；`limit_down_fill_handoff=ce_page`；`call_auction_fill_handoff=cf_page`；`resume_halt_fill_handoff=cg_page`；`after_hours_fill_handoff=ch_page`；`limit_rule_ipo_window_handoff=g_page`；`nolimit_halt_handoff=j_page`；`price_cage_handoff=i_page`；`universe_pool_handoff=c_page`；`maint_ratio_formula_handoff=ca_page`；`financing_rollover_handoff=cb_page`；`delist_force_deadline_handoff=cc_page`；其余 handoff 见 §2.1；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_ipo_day1_fill_misopen_check`；`missing_ipo_day1_fill_policy=skip`；`day_freq_proxy=ipo_day1_fill_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 CI**；**params.G≠实验字母 CI**；**params.N≠实验字母 CI**；亦≠单字母实验 C/I/A/G/J/Z；禁 null/holdout/跑后改口；**勿改他字母已冻 Y/G/N/Y2**）；**`params.ci0_primary_demo` 写死冻结 `invent_assume_ipo_day1_always_fillable`**（禁与 invent_asof_leak_ipo_day1_always_fillable 双挂；CI1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期建议写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- CI0/CI1/CI2 净收益/成本质量、ΔFakeAlwaysFillable、ΔRealizableFill、ΔOpenGapShock、ΔTempHaltOrLiquidityFail；分桶（新股上市首日可成交性误开 / 核对日泄露 / 上市首日窗 / 开盘偏离窗 / 临停枯竭窗 / vs A·CH·CG·CF·CE·CD·G·J·I·C·CA·CB·CC·AR·AG·AN·Z·BA–CH·K·AB·W·X·V·U·T·S）。  
- 自检气泡：CI2 是否 pit_by_ipo_day1_fill_rule；CI0 是否单一主报；CI1 是否仅核对日泄露；是否未与 A/CH/CG/CF/CE/CD/G/J/I/C/CA/CB/CC/AR/AG/AN/Z/BA–CH/K/AB/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 CI 与 C 或 I 或 A 或 G 或 J 或 CH 或 CG 或 CF 或 CE 或 CD 或 CA 或 CB 或 CC 或 B 或 Z 或 K 或 BA–CH 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 CI≠单字母假设-A；CI≠单字母假设-C；CI≠单字母假设-I；CI≠单字母假设-G；CI≠单字母假设-J；CI≠双字母假设-CH；CI≠双字母假设-CG；CI≠双字母假设-CF；CI≠双字母假设-CE；CI≠双字母假设-CD；CI≠双字母假设-CA；CI≠双字母假设-CB；CI≠双字母假设-CC；params.Y≠实验字母 CI**；**是否未改 Y/Z/AA–CH 冻结补丁正文**；**是否未改假设-A / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-G / 假设-J / 假设-I / 假设-C / 假设-CA / 假设-CB / 假设-CC**；**是否未重做预检T**；**是否未复用假设-A / 假设-C / 假设-I / 假设-G / 假设-J / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH**；**是否未与 invent_asof_leak_ipo_day1_always_fillable 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假全额可成或核对日泄露吹成诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不占本机 8765 席位；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–CH 及其他 A/D–CH 已交正文**；**尤其不改假设-CH；尤其不改假设-CG；尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-A；尤其不改假设-C；尤其不改假设-G；尤其不改假设-J；尤其不改假设-I；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC**；**勿再改 CH/CG/CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN/M/N/O/G/J/I**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 执行鸿沟同向：板上枯竭（A）、板上排队（AR）、成交时点与停牌（D）、超涨跌停价无效（AG）、涨停板可成交性误开（CD）、跌停板可成交性误开（CE）、集合竞价可成交性误开（CF）、停牌复牌首日可成交性误开（CG）、盘后固定价格可成交性误开（CH）、新股涨跌幅窗（G）、无板日临停（J）、价格笼子（I）之外，**回测不得默认「新股/次新上市首日订单必能按目标价或开盘价/收盘价全额成交」**；须按当时有效上市首日撮合/临停/流动性约束 PIT。与两融审批/费用族（Z/BA–CC 等）正交，本页不主测两融。与 CD 连续竞价涨停侧、CE 连续竞价跌停侧、CF 集合竞价时段、CG 复牌首日、CH 盘后固定价、G 涨跌幅标签、J 临停触发**正交分列**，本页专测新股/次新上市首日可成交误开。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 CI** 标准件，**不改口径主线**，**不改假设 A–CH 正文**，**尤其不改假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-C / 假设-G / 假设-J / 假设-I / 假设-CA / 假设-CB / 假设-CC**。与实验 A/CH/CG/CF/CE/CD/G/J/I/C/CA/CB/CC/AR/AG/AN/Z/BA–CH/K/AB/W/X/V/U/T/S 分工：**A=板上枯竭主实验（严禁复用；不抢真数）；CH=盘后固定价格可成交性误开（严禁改）；CG=停牌复牌首日可成交性误开（严禁改）；CF=集合竞价可成交性误开（严禁改）；CE=跌停板可成交性误开（严禁改）；CD=涨停板可成交性误开（严禁改）；G=涨跌幅规则PIT新股窗（严禁改）；J=无板日临停（严禁改）；I=价格笼子远限价（严禁复用）；C=股票池；CA=维持比分子分母；CB=展期审批；CC=调出了结时限；CI=新股上市首日可成交性误开（CI≠A≠CH≠CG≠CF≠CE≠CD≠G≠J≠I≠C≠CA≠CB≠CC≠B≠Z≠K≠BA≠…≠BZ≠BY≠BF≠BQ≠BC≠BT≠BD≠BL≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AR≠AG≠AN≠AI≠AJ≠AQ≠AB≠W≠T≠S≠U≠V≠X）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；**禁止标任何纸面齐**） |
| 标准件路径 | `假设-CI-新股上市首日可成交性误开.md` |
| 清单序号 | 约 #92 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死冻结**；**ipo_day1_fill_honest=pit_by_ipo_day1_fill_rule 写死冻结**；diff_buckets 默认名待预检；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 CI；params.G≠实验字母 CI；params.N≠实验字母 CI；亦≠单字母实验 C/I/A/G/J/Z；禁 null/holdout/跑后改口；勿改他字母已冻）**；**ci0_primary_demo 写死冻结 invent_assume_ipo_day1_always_fillable（禁双挂 invent_asof_leak_ipo_day1_always_fillable；CI1半泄露不得升格并列主报）**；锚升格写死 ipo_day1_fill_honest=pit_by_ipo_day1_fill_rule / ipo_day1_fill_scope=assume_ipo_day1_always_fillable_at_target_or_open_or_close / ipo_day1_fill_over_policy=fail_or_partial_or_fail_missing_ipo_day1_rule / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **CI≠C/I/CA/CB/CC/CD/CE/CF/CG/CH/A/G/J/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ/Z/B**（及 ≠BA–CH/K/AB/W/T/S/U/V/X/Y/F/E/D/H/M/AI/AJ/AQ），**严禁复用假设-A / 假设-C / 假设-I / 假设-G / 假设-J / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH**；**尤其 CI≠CH（勿撞盘后固定价格可成交性）**；**尤其 CI≠CG（勿撞停牌复牌首日可成交性）**；**尤其 CI≠CF（勿撞集合竞价可成交性）**；**尤其 CI≠CE（勿撞跌停可成交性）**；**尤其 CI≠CD（勿撞涨停可成交性）**；**尤其 CI≠A（不抢实验A真数队列）**；**尤其 CI≠I（双字母 CI ≠ 单字母假设-I）**；**尤其 CI≠G / CI≠J / CI≠C**；**尤其不改假设-CH/CG/CF/CE/CD/A/C/G/J/I/CA/CB/CC**；**params.Y≠实验字母 CI**；**params.G≠实验字母 CI**；与两融审批/费用类正交 |
| 结论栏 | 空 |

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-04）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 CI**；**`params.G` ≠ 实验字母 CI**；**`params.N` ≠ 实验字母 CI**；**`params.Y` ≠ 单字母实验 C/I/A/G/J/Z**；尤重**双字母 CI ≠ 单字母假设-A**；**双字母 CI ≠ 单字母假设-C**；**双字母 CI ≠ 单字母假设-I**；**双字母 CI ≠ 单字母假设-G**；**双字母 CI ≠ 单字母假设-J**；**双字母 CI ≠ 双字母假设-CH/CG/CF/CE/CD/CA/CB/CC**；禁 null/holdout/跑后改口；**勿改他字母已冻 Y/G/N/Y2**。  
2. **`params.ci0_primary_demo`**：**写死冻结** **`invent_assume_ipo_day1_always_fillable`**；禁与 **`invent_asof_leak_ipo_day1_always_fillable`** 双挂争主表（只挂一个 primary）；**CI1 半泄露不得升格并列主报**。  
3. **新股上市首日可成交性锚升格写死（不可再写「建议」）**：`params.ipo_day1_fill_honest=pit_by_ipo_day1_fill_rule`；`params.ipo_day1_fill_scope=assume_ipo_day1_always_fillable_at_target_or_open_or_close`；`params.ipo_day1_fill_over_policy=fail_or_partial_or_fail_missing_ipo_day1_rule`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。

**硬分列保留**：CI≠C/I/CA/CB/CC/CD/CE/CF/CG/CH/A/G/J/AR/AG…；**尤其 CI≠CH / CI≠CG / CI≠CF / CI≠CE / CI≠CD / CI≠A / CI≠I**；**双字母 CI ≠ 单字母假设-I**；**严禁复用假设-C / 假设-I / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-G / 假设-J**；**params.Y/G/N ≠ 实验字母 CI**。

**状态**：预检有条件通过 · 三条已冻 · 待复检；**禁止标任何纸面齐**；本页不开回测/真数/实盘；不改已冻 Y/Z/AA–CH。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 风控预检补丁·冻结三条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CI**；**params.G≠实验字母 CI**；**params.N≠实验字母 CI**；亦≠单字母实验 C/I/A/G/J/Z；尤重**双字母 CI ≠ 单字母假设-A/C/I/G/J**；**双字母 CI ≠ 双字母假设-CH/CG/CF/CE/CD/CA/CB/CC**；禁 null/holdout/跑后改口）；② `params.ci0_primary_demo=invent_assume_ipo_day1_always_fillable` 单一主报写死（禁与 `invent_asof_leak_ipo_day1_always_fillable` 双挂；CI1不升格）；③ 锚升格写死 `ipo_day1_fill_honest=pit_by_ipo_day1_fill_rule` / `scope=assume_ipo_day1_always_fillable_at_target_or_open_or_close` / `over_policy=fail_or_partial_or_fail_missing_ipo_day1_rule` / `asof=2026-10-16` / `fill_time=next_open` / `fail=skip`；状态「预检有条件通过 · 三条已冻 · 待复检」；清单 #92→已冻结·待复检；**未标纸面齐**；不改 CH/Y–CH 及其他已齐字母；不开回测/真数/实盘。 |
| 2026-11-04 | 新建草稿·待入库预检（总管线：CH 补丁 tip=`13a2363` 已交后写 CI；选题新股上市首日可成交性误开；**CI≠C/I/CA/CB/CC/CD/CE/CF/CG/CH/A/G/J…**；尤其 **CI≠CH（勿撞盘后固定价格可成交性）**、**CI≠CG（勿撞停牌复牌首日可成交性）**、**CI≠CF（勿撞集合竞价可成交性）**、**CI≠CE（勿撞跌停可成交性）**、**CI≠CD（勿撞涨停可成交性）**、**CI≠A（不抢实验A真数队列）**、**CI≠I（双字母 CI ≠ 单字母假设-I）**、**CI≠G / CI≠J / CI≠C**；primary_demo 建议=`invent_assume_ipo_day1_always_fillable`；Y/G/N/Y2 建议占位 `0.02/0.01/0.05/0.015` 待预检；不开回测；未改 CH/CG/CF/CE/CD/A/C/G/J/I/CA/CB/CC 及其他已齐字母；**未标纸面齐**）。 |
