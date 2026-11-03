# 假设 CM · ETF申赎可成交性误开 / 默认ETF申购赎回腿必能按NAV或IOPV或现金替代全额成交（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CL 补丁已交（tip=`287e2df`；复检/入库另线并行后写下一纸面 CM）；清单撞题规则另选正交执行缺口（**回测默认「ETF申购/赎回订单必能按NAV或IOPV或现金替代全额成交」** ≠ 假设-CL 可转债盘后定价可成交性误开 ≠ 假设-CK 协议大宗可成交性误开 ≠ 假设-CJ 退市整理期可成交性误开 ≠ 假设-CI 新股上市首日可成交性误开 ≠ 假设-CH 盘后固定价格可成交性误开 ≠ 假设-CG 停牌复牌首日可成交性误开 ≠ 假设-CF 集合竞价可成交性误开 ≠ 假设-CE 跌停板可成交性误开 ≠ 假设-CD 涨停板可成交性误开 ≠ 假设-R 股票ETF假回转（**回转/T+0 名单 ≠ 申赎腿假全额可成**；R 明文主测 3.1.5 假回转 → 本页自立） ≠ 假设-M 盘后通道存在（**双字母 CM ≠ 单字母假设-M；严禁复用假设-M**） ≠ 假设-O 大宗假流动性 ≠ 假设-A 板上枯竭/一字与封板容量主实验 ≠ 假设-L 市价通道 ≠ 假设-C 股票池当时名单（**双字母 CM ≠ 单字母假设-C；严禁复用假设-C**） ≠ 假设-Q 可转债规则混用 ≠ 假设-AX/AY ETF经手费/最小价位 ≠ 假设-CA/CB/CC 两融族）；选题自 `事实与坑`/口径「执行鸿沟」+ 与 CD–CL 可成交性族正交、与 R 假回转正交、与 M 通道存在正交；清单检索「申赎」未占坑；本页**假定板上容量层（A）/ 排队位次层（AR）/ 成交时点与停牌层（D）/ 超涨跌停价无效层（AG）/ 涨停可成交误开层（CD）/ 跌停可成交误开层（CE）/ 集合竞价可成交误开层（CF）/ 停牌复牌首日可成交误开层（CG）/ 盘后固定价格可成交误开层（CH）/ 新股上市首日可成交误开层（CI）/ 退市整理期可成交误开层（CJ）/ 协议大宗可成交误开层（CK）/ 可转债盘后定价可成交误开层（CL）/ ETF假回转层（R）/ 盘后通道存在层（M）/ 市价通道层（L）诚实或显式旁路**，主病只在**发明「ETF申购赎回腿必能按NAV或IOPV或现金替代全额成交」这一误开默认**；**A 正文主测「涨停可成交性/板上枯竭」真数队列**（**双字母 CM ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 续篇；不抢 A 真数队列**），**R 正文主测「股票ETF假回转」**（回转名单 ≠ 申赎全额可成；**严禁改 R**），**CL 正文主测「可转债盘后定价可成交性误开」**（转债盘后定价 ≠ ETF申赎；**严禁改 CL**），**CK/CJ/CI/CH/CG/CF/CE/CD 正文主测协议大宗/退市整理/上市首日/盘后固定价/复牌/集合/跌停/涨停可成交误开**（**严禁改 CK/CJ/CI/CH/CG/CF/CE/CD**），**M 正文主测盘后通道存在**（通道存在 ≠ 申赎腿全额可成；**双字母 CM ≠ 单字母假设-M；严禁复用假设-M；尤其不改假设-M**），**C 正文主测「股票池当时名单」**（**双字母 CM ≠ 单字母假设-C；严禁复用 C**），**CA/CB/CC 正文主测两融族**（与本页正交；**严禁改 CA/CB/CC**）→ 自立；与假设 B/Z/BA–CL/AG/AF/E/X/W/K/AB/N/H/AN/AX/AY 等**分列**；**严禁复用假设-M / 假设-R / 假设-CL / 假设-CK / 假设-C / 假设-A**；**新建实验 CM**  
状态：**草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；禁止把「ETF申购/赎回腿必能按NAV或IOPV或现金替代全额成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CL 及其他 A/D–CL 已交正文与冻结补丁；尤其不改假设-CL；尤其不改假设-CK；尤其不改假设-CJ；尤其不改假设-CI；尤其不改假设-CH；尤其不改假设-CG；尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-R；尤其不改假设-M；尤其不改假设-A；尤其不改假设-C；尤其不改假设-O；尤其不改假设-L；尤其不改假设-Q；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；勿再改 CL/CK/CJ/CI/CH/CG/CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN/Q/M/L/O/H/K/R**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CM（约 #96）。与假设 **CL（可转债盘后定价可成交性误开）** **硬分列（专节强调）**：CL = 可转债盘后定价腿假全额可成；本页 = ETF申购赎回腿假全额可成；转债盘后定价 ≠ ETF申赎；**严禁复用 CL 题面或 `invent_assume_cb_after_hours_pricing_always_fillable`**；**尤其不改假设-CL**。**CM≠CL**。与假设 **CK（协议大宗可成交性误开）** **硬分列**：协议大宗 ≠ ETF申赎；**严禁复用 CK**；**尤其不改假设-CK**。**CM≠CK**。与假设 **CJ/CI/CH/CG/CF/CE/CD** **硬分列**：退市整理/上市首日/盘后固定价/复牌/集合/跌停/涨停 ≠ ETF申赎；**严禁复用**；**尤其不改**。**CM≠CJ≠CI≠CH≠CG≠CF≠CE≠CD**。与假设 **R（股票ETF假回转）** **硬分列（专节强调）**：R = 把股票 ETF / 跨境但书 / 商品期货 ETF 切日上的假 T+0 回转当默认；本页 = 在回转层诚实（或显式旁路交 R）的前提下，是否仍默认「ETF申购/赎回腿必能按NAV或IOPV或现金替代全额成交」；回转名单 ≠ 申赎腿假全额可成；**严禁复用 R 题面**；**尤其不改假设-R**。**CM≠R**。与假设 **M（盘后补成交/通道）** **硬分列（专节强调）**：**双字母 CM ≠ 单字母假设-M**；通道存在/自动滚入 ≠ 申赎腿全额可成；**严禁复用假设-M**；**尤其不改假设-M**。**CM≠M**。与假设 **A（涨停可成交性/板上枯竭）** **硬分列（专节强调）**：容量门槛 ≠ 申赎全额可成默认；**双字母 CM ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不占** A 的 A0/A1 主报与真数席位；**尤其不改假设-A**。**CM≠A**。与假设 **C（股票池当时名单）** **硬分列**：**双字母 CM ≠ 单字母假设-C**；**严禁复用 C**。**CM≠C**。与假设 **O（大宗假流动性）** **硬分列**：大宗量价/三通道 ≠ 申赎全额可成；**严禁复用 O**。**CM≠O**。与假设 **L（市价通道）** **硬分列**：市价保护/废单 ≠ 申赎全额可成；**严禁复用 L**。**CM≠L**。与假设 **Q（可转债规则混用）** **硬分列**：转债规则混用 ≠ ETF申赎；**严禁复用 Q**。**CM≠Q**。与假设 **AX/AY（ETF经手费/最小价位）** **硬分列**：费用/价位 ≠ 申赎全额可成；**严禁改写 AX/AY 作主病**。与假设 **CA/CB/CC** **硬分列**：两融公式/展期/调出了结时限 ≠ 申赎全额可成；**尤其不改 CA/CB/CC**。**CM≠CA≠CB≠CC**。与假设 **AR/AG/AN/BZ/BY/BX/BW…** 及两融审批/费用族 **硬分列**。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A / 假设-C / 假设-M / 假设-R / 假设-CL / 假设-CK / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-O / 假设-L / 假设-Q**。**严禁改写/续写假设-CL / 假设-CK / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-R / 假设-M / 假设-A / 假设-C / 假设-O / 假设-L / 假设-Q / 假设-CA / 假设-CB / 假设-CC**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CM** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 M**（盘后通道；**严禁复用假设-M**）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **单字母实验 R**（股票ETF假回转；**严禁复用假设-R**）≠ **单字母实验 L**（市价通道；**严禁复用假设-L**）≠ **单字母实验 Q**（可转债规则混用；**严禁复用假设-Q**）≠ **单字母实验 O**（大宗假流动性；**严禁复用假设-O**）≠ **双字母实验 CA**（维持比分子分母；**严禁改写假设-CA**）≠ **双字母实验 CB**（融资展期审批；**严禁改写假设-CB**）≠ **双字母实验 CC**（调出强制了结时点；**严禁改写假设-CC**）≠ **双字母实验 CD**（涨停板可成交性误开；**严禁改写假设-CD**）≠ **双字母实验 CE**（跌停板可成交性误开；**严禁改写假设-CE**）≠ **双字母实验 CF**（集合竞价可成交性误开；**严禁改写假设-CF**）≠ **双字母实验 CG**（停牌复牌首日可成交性误开；**严禁改写假设-CG**）≠ **双字母实验 CH**（盘后固定价格可成交性误开；**严禁改写假设-CH**）≠ **双字母实验 CI**（新股上市首日可成交性误开；**严禁改写假设-CI**）≠ **双字母实验 CJ**（退市整理期可成交性误开；**严禁改写假设-CJ**）≠ **双字母实验 CK**（协议大宗可成交性误开；**严禁改写假设-CK**）≠ **双字母实验 CL**（可转债盘后定价可成交性误开；**严禁改写假设-CL**）≠ **单字母实验 B** ≠ **单字母实验 Z** ≠ **单字母实验 K** ≠ **单字母实验 D** ≠ **单字母实验 I** ≠ **单字母实验 J** ≠ **单字母实验 H** ≠ **单字母实验 N**。全文凡写「实验 CM / 假设-CM / hypothesis_id=CM / 组 CM0·CM1·CM2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CM 混读或互改；**尤其 params.Y ≠ 实验字母 CM ≠ 单字母假设-C ≠ 单字母假设-M ≠ 单字母假设-A ≠ 单字母假设-R ≠ 双字母假设-CA ≠ 双字母假设-CB ≠ 双字母假设-CC ≠ 双字母假设-CD ≠ 双字母假设-CE ≠ 双字母假设-CF ≠ 双字母假设-CG ≠ 双字母假设-CH ≠ 双字母假设-CI ≠ 双字母假设-CJ ≠ 双字母假设-CK ≠ 双字母假设-CL**。亦**禁止**把实验字母 CM 与单字母 **A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/Q/R/T/S/U/V/W/X/Y/Z**、双字母 **BA–CL**、双字母 **CA/CB/CC/CD/CE/CF/CG/CH/CI/CJ/CK/CL/AR/AG/AN/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/BF/BQ**、双字母 **AB**、双字母 **AI/AJ/AQ**、双字母 **AZ/AY/AX/AW**、或 params 键名 `cm0_*` 以外的实验页混读。**双字母 CM ≠ 单字母 C ≠ 单字母 M ≠ 单字母 A ≠ 单字母 R ≠ 单字母 L ≠ 单字母 Q ≠ 单字母 O ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 D ≠ 单字母 I ≠ 单字母 J ≠ 单字母 H ≠ 单字母 N ≠ 双字母 CA ≠ 双字母 CB ≠ 双字母 CC ≠ 双字母 CD ≠ 双字母 CE ≠ 双字母 CF ≠ 双字母 CG ≠ 双字母 CH ≠ 双字母 CI ≠ 双字母 CJ ≠ 双字母 CK ≠ 双字母 CL ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 AN ≠ 双字母 AI ≠ 双字母 AJ ≠ 双字母 AQ ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BY ≠ 双字母 BF ≠ 双字母 BQ ≠ 双字母 BC ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB ≠ 双字母 BK ≠ 双字母 AX ≠ 双字母 AY**；**params.Y ≠ 实验字母 CM**；**params.G ≠ 实验字母 CM**；**params.N ≠ 实验字母 CM**。**带过：双字母 CL ≠ C/L/Q/CA–CK/A/M…；双字母 CK ≠ C/K/O/CA–CJ/A/M…；双字母 CJ ≠ C/J/H/CA–CI/A…；双字母 CI ≠ C/I/CA–CH/A/G/J…；双字母 CH ≠ C/H/CA–CG/A/M…；双字母 CG ≠ C/G/CA–CF/A/D…；双字母 CF ≠ C/F/CA–CE/A/Y…；双字母 CE ≠ C/E/CA/CB/CC/CD/AR…；双字母 CD ≠ A/C/D/CA/CB/CC/AR…；双字母 CC ≠ C/CA/CB/BQ/BY/BZ/BF…；双字母 CB ≠ B/C/CA/BF/BZ…；双字母 CA ≠ A/C/BZ/BY…；双字母 AR ≠ A/R/AQ…；双字母 BK ≠ 单字母假设-K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CM ≠ 单字母假设-A / 假设-C / 假设-M / 假设-R / 假设-L / 假设-Q / 假设-O；且 ≠ 假设-CA / 假设-CB / 假设-CC / 假设-CD / 假设-CE / 假设-CF / 假设-CG / 假设-CH / 假设-CI / 假设-CJ / 假设-CK / 假设-CL；带过 CL≠CK/CH/Q/C/L/A、params.Y≠CM（硬）

| 维度 | 对照页 | 本页假设-CM（双字母） |
|------|--------|----------------------|
| 题面 CL | **可转债盘后定价可成交性误开**（`invent_assume_cb_after_hours_pricing_always_fillable`） | **ETF申赎可成交性误开**：默认「ETF申购/赎回腿必能按NAV或IOPV或现金替代全额成交」vs 诚实申赎撮合/篮子/现金替代/额度/截止时点约束；转债盘后定价 ≠ ETF申赎；**严禁复用 CL 题面**；**CM≠CL**；**不改 CL** |
| 题面 CK | **协议大宗可成交性误开**（`invent_assume_block_trade_always_fillable`） | 协议大宗 ≠ ETF申赎；**严禁复用 CK 题面**；**CM≠CK**；**不改 CK** |
| 题面 CJ | **退市整理期可成交性误开**（`invent_assume_delist_period_always_fillable`） | 退市整理期 ≠ ETF申赎；**严禁复用 CJ 题面**；**CM≠CJ**；**不改 CJ** |
| 题面 CI | **新股上市首日可成交性误开**（`invent_assume_ipo_day1_always_fillable`） | 上市首日 ≠ ETF申赎；**严禁复用 CI 题面**；**CM≠CI**；**不改 CI** |
| 题面 CH | **盘后固定价格可成交性误开**（`invent_assume_after_hours_fixed_price_always_fillable`） | 盘后固定价 ≠ ETF申赎；**严禁复用 CH 题面**；**CM≠CH**；**不改 CH** |
| 题面 CG | **停牌复牌首日可成交性误开**（`invent_assume_resume_from_halt_always_fillable`） | 复牌首日 ≠ ETF申赎；**严禁复用 CG 题面**；**CM≠CG**；**不改 CG** |
| 题面 CF | **集合竞价可成交性误开**（`invent_assume_call_auction_always_fillable`） | 集合竞价 ≠ ETF申赎全额可成默认；**严禁复用 CF 题面**；**CM≠CF**；**不改 CF** |
| 题面 CE | **跌停板可成交性误开**（`invent_assume_limit_down_always_fillable`） | 连续竞价跌停侧 ≠ ETF申赎；**严禁复用 CE 题面**；**CM≠CE**；**不改 CE** |
| 题面 CD | **涨停板可成交性误开**（`invent_assume_limit_up_always_fillable`） | 连续竞价涨停侧 ≠ ETF申赎；**严禁复用 CD 题面**；**CM≠CD**；**不改 CD** |
| 题面 R | **股票ETF假回转**（清单实验 R；3.1.5 假 T+0） | 回转名单 ≠ 申赎腿假全额可成；**严禁复用 R**；**CM≠R**；**不改 R** |
| 题面 M | **盘后补成交/通道存在**（清单实验 M） | 通道存在 ≠ 申赎腿全额可成；**双字母 CM ≠ 单字母假设-M**；**严禁复用假设-M**；**CM≠M**；**不改 M** |
| 题面 A | **涨停可成交性/板上枯竭**（清单实验 A；真数队列） | 容量门槛 ≠ 申赎全额可成默认；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不抢 A 真数队列**；**CM≠A** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 股票池 ≠ 申赎全额可成；**严禁复用 C**；**CM≠C** |
| 题面 L | **市价通道**（清单实验 L） | 市价保护/废单 ≠ 申赎全额可成；**严禁复用 L**；**CM≠L**；**不改 L** |
| 题面 Q | **可转债规则混用**（清单实验 Q） | 转债规则混用 ≠ ETF申赎；**严禁复用 Q**；**CM≠Q**；**不改 Q** |
| 题面 O | **大宗假流动性**（清单实验 O） | 大宗量价/三通道 ≠ 申赎全额可成；**严禁复用 O**；**CM≠O**；**不改 O** |
| 题面 CA | **维持担保比例分子分母口径** | 公式 ≠ 申赎全额可成；**CM≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批** | 展期审批 ≠ 申赎全额可成；**CM≠CB**；**不改 CB** |
| 题面 CC | **两融标的调出强制了结时点** | 调出了结时限 ≠ 申赎全额可成；**CM≠CC**；**不改 CC** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_assume_etf_creation_redemption_always_fillable`（**写死冻结**单一主报；禁双挂 asof_leak；CM1不升格） |
| 文档 | 清单实验 A / C / M / R / L / Q / O / `假设-CA-…` … / `假设-CL-…`（**只读；禁止改写**） | `假设-CM-ETF申赎可成交性误开.md`（新建） |
| 预检键 | 实验字母 A / C / M / R / L / Q / O / CA / CB / CC / CD / CE / CF / CG / CH / CI / CJ / CK / CL | 实验字母 **CM** / `cm0_primary_demo`；**不得**占用或改写预检 A/C/M/R/L/Q/O/CA/CB/CC/CD/CE/CF/CG/CH/CI/CJ/CK/CL |

**禁止**：把 CM 写成「A/CL/CK/CJ/CI/CH/CG/CF/CE/CD/R/M/C/L/Q/O/CA/CB/CC 的续篇」；把「板上容量已诚实（A）/ 可转债盘后定价可成交已诚实（CL）/ 协议大宗可成交已诚实（CK）/ 退市整理期可成交已诚实（CJ）/ 上市首日可成交已诚实（CI）/ 盘后固定价可成交已诚实（CH）/ 复牌首日可成交已诚实（CG）/ 集合竞价可成交已诚实（CF）/ 跌停可成交已诚实（CE）/ 涨停可成交已诚实（CD）/ ETF回转已诚实（R）/ 盘后通道已诚实（M）/ 市价通道已诚实（L）/ 股票池已诚实（C）/ 大宗量价已诚实（O）/ 转债规则混用已诚实（Q）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「ETF申赎可成交性已诚实」；覆盖或补丁改写假设-A / 假设-CL / 假设-CK / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-R / 假设-M / 假设-C / 假设-L / 假设-Q / 假设-O / 假设-CA / 假设-CB / 假设-CC 正文；把 `params.Y/G/N` 与实验字母 CM 混读；**禁** `cm0_primary_demo` 与 `invent_asof_leak_etf_creation_redemption_always_fillable` **双挂主报**；**禁** CM1 半泄露升格并列主报；**禁**复用假设-A / 假设-C / 假设-M / 假设-R / 假设-CL / 假设-CK / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-O / 假设-L / 假设-Q 题面或口径键；**禁**复用 CL/CK/CJ/CI/CH/CG/CF/CE/CD/R/M/CA/CB/CC 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有路径、同一未复权价、同一 T+1（或 ETF 当日回转腿另桶交 R）、同一板上容量/排队位次/成交时点与停牌/涨跌停可成交/集合竞价可成交/复牌首日可成交/盘后固定价可成交/上市首日可成交/退市整理期可成交/协议大宗可成交/可转债盘后定价可成交/ETF假回转/盘后通道存在/市价通道等输入（A/AR/D/CD/CE/CF/CG/CH/CI/CJ/CK/CL/R/M/L 层诚实或显式旁路声明「本页不重开板上容量门槛/假队首/开收时点与停牌期间假成交/连续竞价涨跌停全额可成/集合竞价全额可成/复牌首日全额可成/盘后固定价全额可成/上市首日全额可成/退市整理期全额可成/协议大宗全额可成/转债盘后定价全额可成/ETF假回转/盘后通道存在/市价保护废单」）下，把「ETF申购/赎回订单必能按NAV或IOPV或现金替代全额成交」或「全样本用核对日当天更宽『ETF申赎一律全额可成』规则回放历史」当成默认，相对「每个交易日按当时有效ETF申赎篮子/现金替代比例/最小申赎单位/申赎截止时点/暂停申赎标记 PIT（篮子成分停牌或缺券记部分或失败；现金替代超限记截断或失败；过截止时点记失败；暂停申赎日 skip；缺字段 skip/敏感性；不抢 A 真数席位；不把二级市场竞价成交写成一级申赎可成）」的诚实组，会**系统性发明假全额可成路径并高估申赎腿可实现成交、低估篮子失败、现金替代超限与暂停申赎**；差异应**集中在ETF申赎可成交性误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、篮子/现金替代失败差、暂停申赎冲击差在标定噪声带内可忽略，且「假全额可成 / 核对日泄露 / 申赎窗 / vs A·CL·CK·CJ·CI·CH·CG·CF·CE·CD·R·M·C·L·Q·O·CA·CB·CC·AR·AG·AN·AX·AY·W·X·T·S·U·V」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 与 cm0 与锚 **三条已冻**）

```
# 配置写死键（见 §7；预检有条件通过 · 三条已冻 · 待复检；下列已写死冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CM；≠ 单字母假设-C；≠ 单字母假设-M；≠ 单字母假设-A；≠ 单字母假设-R；≠ 双字母假设-CA/CB/CC/CD/CE/CF/CG/CH/CI/CJ/CK/CL
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CM；≠ 单字母假设-G
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CM；≠ 单字母假设-N；亦≠实验字母 BN
# params.fill_time 写死冻结 next_open
# params.asof_check_date 写死冻结 2026-10-16
# params.px_basis 建议 unadj
# params.etf_cr_fill_honest 写死冻结 pit_by_etf_creation_redemption_fill_rule
# params.etf_cr_fill_scope 写死冻结 assume_etf_creation_redemption_always_fillable_at_nav_or_iopv_or_cash
# params.etf_cr_fill_over_policy 写死冻结 fail_or_partial_or_fail_missing_etf_cr_rule
# params.etf_cr_px_mode 建议 nav_or_iopv_or_cash_sub   # 一级申赎；禁静默抄二级竞价全额可成
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
# params.block_trade_fill_handoff 建议 ck_page
# params.cb_ah_pricing_fill_handoff 建议 cl_page   # 转债盘后定价交 CL；CM≠CL；严禁复用假设-CL
# params.etf_rotation_handoff 建议 r_page          # ETF假回转交 R；CM≠R；严禁复用假设-R
# params.aft_channel_handoff 建议 m_page           # 盘后通道交 M；CM≠M；严禁复用假设-M
# params.mkt_order_handoff 建议 l_page
# params.block_liquidity_handoff 建议 o_page
# params.cb_rule_mix_handoff 建议 q_page
# params.universe_pool_handoff 建议 c_page
# params.maint_ratio_formula_handoff 建议 ca_page
# params.financing_rollover_handoff 建议 cb_page
# params.delist_force_deadline_handoff 建议 cc_page
# params.etf_cr_fill_handoff 建议 self
# params.cm0_primary_demo                写死冻结 invent_assume_etf_creation_redemption_always_fillable
# params.cm0_invent_assume_etf_creation_redemption_always_fillable 建议 True
# params.cm1_asof_leak_etf_creation_redemption_always_fillable_only 建议 True
# params.cm2_pit_etf_cr_fill 建议 True
# params.merge_with_A_fill 建议 False
# params.merge_with_AR_queue 建议 False
# params.merge_with_D_fill_time 建议 False
# params.merge_with_C_universe_pool 建议 False
# params.merge_with_L_mkt_order 建议 False
# params.merge_with_Q_cb_rule_mix 建议 False
# params.merge_with_M_aft_channel 建议 False
# params.merge_with_O_block_liquidity 建议 False
# params.merge_with_R_etf_rotation 建议 False
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
# params.merge_with_CK_block_trade_fill 建议 False
# params.merge_with_CL_cb_ah_pricing_fill 建议 False
# params.merge_with_AG_beyond_limit 建议 False
# params.missing_etf_cr_fill_policy 建议 skip
# params.day_freq_proxy 建议 etf_cr_fill_sensitivity
# params.universe_rule 建议 sse_szse_etf_cr_fill_misopen_check
# params.fail_policy 写死冻结 skip
# params.redline_v0_exempt_scope 建议 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 CM；params.G≠实验字母 CM；params.N≠实验字母 CM；禁 null/holdout；勿改已冻他字母数值）
# params.date_start / date_end 建议 2019-01-01..2026-09-30
# params.oos_split.*                     建议四日期；禁 holdout 反调
# CM0：假全额可成——ETF申购/赎回腿按NAV或IOPV或现金替代 100% 成交
# CM1：仅 asof 日更宽「ETF申赎一律全额可成」规则泄露铺满
# CM2：每个交易日 d 按当时已生效ETF申赎篮子/现金替代/截止时点/暂停标记 PIT
# 缺ETF申赎可成交约束字段 → skip（params.missing_etf_cr_fill_policy）
```

### 2.2 三组对照（CM0 / CM1 / CM2）

| 组 | 角色 | 规则 |
|----|------|------|
| CM0 | 天真 / 假全额可成 | 按 `cm0_primary_demo` **写死冻结**单一主报 `invent_assume_etf_creation_redemption_always_fillable`：ETF申购/赎回腿按NAV或IOPV或现金替代 100% 成交（**禁**与 `invent_asof_leak_etf_creation_redemption_always_fillable` 双挂主报） |
| CM1 | 半泄露 | 仅核对日（asof）更宽「ETF申赎一律全额可成」规则泄露铺满全历史；**不得升格并列主报**（已冻：CM1不升格） |
| CM2 | 诚实 PIT | `etf_cr_fill_honest=pit_by_etf_creation_redemption_fill_rule`（已冻结）：每个交易日按当时已生效ETF申赎篮子/现金替代/截止时点/暂停标记；缺字段 skip |

### 2.3 额度窗内时频可落点（写明但不真跑）

主窗建议 `2019-01-01..2026-09-30`（额度窗内）；asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。本页**不开回测**；不拉真数；不做实盘。

### 3.1 oos_split（建议四日期；拉数前冻结；禁 holdout 反调）

建议四段日期写死于拉数前；**禁止** holdout 反调；具体四日期待预检与额度窗对齐后冻结。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（CM0）/ 半泄露组（CM1）相对诚实组（CM2）的假全额可成贡献差、可实现成交差、篮子/现金替代失败差、暂停申赎冲击差**显著且集中在ETF申赎可成交性误开桶**；分桶「假全额可成 / 核对日泄露 / 申赎窗 / vs A·CL·CK·CJ·CI·CH·CG·CF·CE·CD·R·M·C·L·Q·O·CA·CB·CC…」不改变主结论方向。

### 3.2 失败（假设不成立 / 设计失效）

上述差异在标定噪声带内可忽略；或差异主要由 A/CL/CK/CJ/CI/CH/CG/CF/CE/CD/R/M/C 等旁路页解释而非本页主病；或缺字段过多导致有效样本不足；或 oos/holdout 反调污染。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1（或 ETF 当日回转腿另桶交 R），对照 CM0/CM1/CM2。报告假全额可成贡献差、可实现成交差、篮子/现金替代失败差、暂停申赎冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前冻结；禁 holdout 改桶）

建议默认桶名（待预检冻结）：`invent_assume_etf_creation_redemption_always_fillable` / `invent_asof_leak_etf_creation_redemption_always_fillable` / `vs_A_board_capacity` / `vs_CL_cb_ah_pricing_fill` / `vs_CK_block_trade_fill` / `vs_CJ_delist_period_fill` / `vs_CI_ipo_day1_fill` / `vs_CH_after_hours_fill` / `vs_CG_resume_halt_fill` / `vs_CF_call_auction_fill` / `vs_CE_limit_down_fill` / `vs_CD_limit_up_fill` / `vs_R_etf_rotation` / `vs_M_aft_channel` / `vs_L_mkt_order` / `vs_C_universe_pool` / `vs_O_block_liquidity` / `vs_Q_cb_rule_mix` / `vs_CA_maint_ratio` / `vs_CB_rollover` / `vs_CC_delist_force` / `vs_AR_queue` / `vs_AG_beyond_limit` / `vs_AN_auction_leftover` / `vs_AX_etf_fee` / `vs_AY_etf_tick` / `vs_W_exright` / `vs_X_st_limit` / `vs_AB_short_px` / `vs_T_csrc_fee` / `vs_S_handling_fee` / `vs_U_transfer_fee` / `vs_V_stamp_tax`。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 缺ETF申赎篮子/现金替代/截止时点/暂停字段，静默当假全额可成（应 skip）。
- 把 R「ETF假回转」已诚实误写成「ETF申赎可成交性已诚实」。
- 把 CL「可转债盘后定价可成交」已诚实误写成申赎可成交已诚实。
- 把 M「盘后通道存在」已诚实误写成申赎可成交已诚实。
- 把 CK/CJ/CI/CH/CG/CF/CD·CE 可成交已诚实误写成申赎可成交已诚实。
- 把 A 真数队列或把 CM 做成 A/CL/R/M 续篇。
- `cm0_primary_demo` 与 asof_leak 双挂主报；CM1 升格并列主报。
- 扩窗出额度、改已冻 Y/G/N/Y2、标纸面齐、开回测/真数/实盘。
- 实验字母 CM 与单字母 C/M/A/R/L/Q/O 或双字母 CA–CL 或 params.Y/G/N 混读。
- **复用假设-M 盘后通道存在题面**；**复用假设-R 股票ETF假回转题面**。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 未复权 OHLC / 买卖方向 / T+1 或 ETF 回转信号日（回转另桶交 R）。
- ETF申购/赎回腿代理、NAV/IOPV、现金替代比例与上限、最小申赎单位、申赎截止时点、暂停申赎标记、篮子成分停牌/缺券代理。
- 当时有效ETF申赎规则及生效日（一级申赎；禁静默抄二级竞价全额可成或盘后固定价通道）。
- A/AR/D/CD/CE/CF/CG/CH/CI/CJ/CK/CL/R/M/L/C/O/Q/CA/CB/CC 旁路诚实标记或显式旁路声明。
- 交易日历；asof=2026-10-16 锚。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- hypothesis_id=`CM`；组 CM0/CM1/CM2。
- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`etf_cr_fill_honest=pit_by_etf_creation_redemption_fill_rule`；`etf_cr_fill_scope=assume_etf_creation_redemption_always_fillable_at_nav_or_iopv_or_cash`；`etf_cr_fill_over_policy=fail_or_partial_or_fail_missing_etf_cr_rule`；`fail_policy=skip`；`cm0_primary_demo=invent_assume_etf_creation_redemption_always_fillable`（**写死冻结**单一主报；禁双挂 asof_leak；CM1不升格）。
- 锚升格写死（不可再写「建议」）：`etf_cr_fill_honest=pit_by_etf_creation_redemption_fill_rule`；`etf_cr_fill_scope=assume_etf_creation_redemption_always_fillable_at_nav_or_iopv_or_cash`；`etf_cr_fill_over_policy=fail_or_partial_or_fail_missing_etf_cr_rule`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CM**；**params.G≠实验字母 CM**；**params.N≠实验字母 CM**；禁 null/holdout；**勿改已冻他字母数值**）。
- 主窗建议 `2019-01-01..2026-09-30`；oos_split 四日期建议写死+禁 holdout 反调。
- 全部 `merge_with_*=False`（见 §2.1）。
- **本页不开回测**；不催 8765；不抢 A 真数。

---

## 8. 结论

（空；本页不开回测；不写买卖建议。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-04）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 CM**；**`params.G` ≠ 实验字母 CM**；**`params.N` ≠ 实验字母 CM**；**`params.Y` ≠ 单字母实验 C/M/A/R/Z**；尤重**双字母 CM ≠ 单字母假设-A**；**双字母 CM ≠ 单字母假设-C**；**双字母 CM ≠ 单字母假设-M**；**双字母 CM ≠ 单字母假设-R**；**双字母 CM ≠ 双字母假设-CL/CK/CH/CG/CF/CE/CD/CA/CB/CC**；禁 null/holdout/跑后改口；**勿改他字母已冻 Y/G/N/Y2**。  

2. **`params.cm0_primary_demo`**：**写死冻结** **`invent_assume_etf_creation_redemption_always_fillable`**；禁与 **`invent_asof_leak_etf_creation_redemption_always_fillable`** 双挂争主表（只挂一个 primary）；**CM1 半泄露不得升格并列主报**。  

3. **ETF申赎可成交性锚升格写死（不可再写「建议」）**：`params.etf_cr_fill_honest=pit_by_etf_creation_redemption_fill_rule`；`params.etf_cr_fill_scope=assume_etf_creation_redemption_always_fillable_at_nav_or_iopv_or_cash`；`params.etf_cr_fill_over_policy=fail_or_partial_or_fail_missing_etf_cr_rule`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。

**硬分列保持**：CM≠CL/CK/CH/R/C/M/A/CA–CL…；**尤其 CM≠CL / CM≠CK / CM≠CH / CM≠R / CM≠CJ / CM≠CI / CM≠CG / CM≠CF / CM≠CE / CM≠CD / CM≠A**；**双字母 CM ≠ 单字母假设-C / 假设-M / 假设-A / 假设-R**；**严禁复用假设-M / 假设-R / 假设-CL / 假设-CK / 假设-CH / 假设-CJ / 假设-CI / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-A / 假设-C**；**params.Y/G/N ≠ 实验字母 CM**。

**状态**：预检有条件通过 · 三条已冻 · 待复检；**禁止标任何纸面齐**；本页不开回测/真数/实盘；不改已冻 CL/Y–CL。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 风控预检补丁·冻结三条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CM**；**params.G≠实验字母 CM**；**params.N≠实验字母 CM**；亦≠单字母实验 C/M/A/R/Z；尤重**双字母 CM ≠ 单字母假设-A/C/M/R**；**双字母 CM ≠ 双字母假设-CL/CK/CH/CG/CF/CE/CD/CA/CB/CC**；禁 null/holdout/跑后改口）；② `params.cm0_primary_demo=invent_assume_etf_creation_redemption_always_fillable` 单一主报写死（禁与 `invent_asof_leak_etf_creation_redemption_always_fillable` 双挂；CM1不升格）；③ 锚升格写死 `etf_cr_fill_honest=pit_by_etf_creation_redemption_fill_rule` / `scope=assume_etf_creation_redemption_always_fillable_at_nav_or_iopv_or_cash` / `over_policy=fail_or_partial_or_fail_missing_etf_cr_rule` / `asof=2026-10-16` / `fill_time=next_open` / `fail=skip`；状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；不改已冻 CL/Y–CL；不开回测/真数/实盘。基线 tip=`58a1437`。 |
| 2026-11-04 | 新建草稿·待入库预检（总管线：CL 补丁 tip=`287e2df` 已交后写 CM；选题 ETF申赎可成交性误开；cm0 建议 `invent_assume_etf_creation_redemption_always_fillable`；清单约 #96；硬分列 CM≠C/M/CA–CL…（尤≠CL/CK/CH/R/M/A）；**禁止标任何纸面齐**）。 |

