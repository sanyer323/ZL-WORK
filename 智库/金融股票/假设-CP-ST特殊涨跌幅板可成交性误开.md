# 假设 CP · ST特殊涨跌幅板可成交性误开 / 默认ST/*ST特殊涨跌幅板上订单必能按目标价或开盘价/收盘价全额成交（执行鸿沟）

更新：2026-11-04  
来源：总管线 / CO 补丁已交（tip=`f6668fb`；复检/入库另线并行后写下一纸面 CP）；清单撞题规则另选正交执行缺口（**回测默认「ST/*ST特殊涨跌幅板上订单必能按目标价或开盘价/收盘价全额成交」** ≠ 假设-CO 北交所连续竞价可成交性误开 ≠ 假设-CN 配股增发认购可成交性误开 ≠ 假设-CM ETF申赎可成交性误开 ≠ 假设-CL 可转债盘后定价可成交性误开 ≠ 假设-CK 协议大宗可成交性误开 ≠ 假设-CJ 退市整理期可成交性误开 ≠ 假设-CI 新股上市首日可成交性误开 ≠ 假设-CH 盘后固定价格可成交性误开 ≠ 假设-CG 停牌复牌首日可成交性误开 ≠ 假设-CF 集合竞价可成交性误开 ≠ 假设-CE 跌停板可成交性误开 ≠ 假设-CD 涨停板可成交性误开 ≠ 假设-X 主板ST涨跌幅PIT误切（**板幅5%→10%切日误标 ≠ 特殊涨跌幅板腿假全额可成**；X 明文主测板幅PIT → 本页自立） ≠ 假设-AD 风险警示买入50万上限（**买入额度上限 ≠ 特殊涨跌幅板假全额可成**；AD 明文主测当日累计买入股数上限 → 本页自立） ≠ 假设-P 指数点位停牌假成交权重（**双字母 CP ≠ 单字母假设-P；严禁复用假设-P**） ≠ 假设-O 大宗假流动性 ≠ 假设-A 板上枯竭/一字与封板容量主实验 ≠ 假设-C 股票池当时名单（**双字母 CP ≠ 单字母假设-C；严禁复用假设-C**） ≠ 假设-CA/CB/CC 两融族）；选题自 `事实与坑`/口径「执行鸿沟」+ 与 CA–CO 可成交性族正交、与 X 主板ST板幅PIT正交、与 AD 风险警示买入上限正交、与 P 指数点位权重正交；清单检索「ST特殊涨跌幅板可成交」「st special limit board fill」未占坑（X 仅占板幅PIT；AD 仅占买入上限；CD/CE 主测普通股涨跌停侧）；本页**假定板上容量层（A）/ 排队位次层（AR）/ 成交时点与停牌层（D）/ 超涨跌停价无效层（AG）/ 涨停可成交误开层（CD）/ 跌停可成交误开层（CE）/ 集合竞价可成交误开层（CF）/ 停牌复牌首日可成交误开层（CG）/ 盘后固定价格可成交误开层（CH）/ 新股上市首日可成交误开层（CI）/ 退市整理期可成交误开层（CJ）/ 协议大宗可成交误开层（CK）/ 可转债盘后定价可成交误开层（CL）/ ETF申赎可成交误开层（CM）/ 配股增发认购可成交误开层（CN）/ 北交所连续竞价可成交误开层（CO）/ 主板ST板幅PIT层（X）/ 风险警示买入上限层（AD）/ 指数点位权重层（P）/ 大宗假流动性层（O）诚实或显式旁路**，主病只在**发明「ST/*ST特殊涨跌幅板上订单必能按目标价或开盘价/收盘价全额成交」这一误开默认**；**A 正文主测「涨停可成交性/板上枯竭」真数队列**（**双字母 CP ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 续篇；不抢 A 真数队列**），**CO 正文主测「北交所连续竞价可成交性误开」**（北交所连续竞价 ≠ ST特殊涨跌幅板；**严禁改 CO**），**CN/CM/CL/CK/CJ/CI/CH/CG/CF/CE/CD 正文主测配股增发认购/ETF申赎/转债盘后定价/协议大宗/退市整理/上市首日/盘后固定价/复牌/集合/跌停/涨停可成交误开**（**严禁改 CN/CM/CL/CK/CJ/CI/CH/CG/CF/CE/CD**），**X 正文主测主板ST涨跌幅PIT误切**（板幅切日 ≠ 板上假全额可成；**严禁改 X**），**AD 正文主测风险警示买入50万上限**（买入额度 ≠ 板上假全额可成；**严禁改 AD**），**P 正文主测指数点位停牌假成交权重**（**双字母 CP ≠ 单字母假设-P；严禁复用假设-P；尤其不改假设-P**），**C 正文主测「股票池当时名单」**（**双字母 CP ≠ 单字母假设-C；严禁复用 C**），**CA/CB/CC 正文主测两融族**（与本页正交；**严禁改 CA/CB/CC**）→ 自立；与假设 B/Z/BA–CO/AG/AF/E/O/K/AB/H/AN/AC 等**分列**；**严禁复用假设-P / 假设-CO / 假设-CN / 假设-CM / 假设-CL / 假设-CK / 假设-CH / 假设-X / 假设-AD / 假设-C / 假设-A**；**新建实验 CP**  
状态：**草稿 · 预检有条件通过 · 三条已冻 · 待复检**（结论栏空；禁止把「ST/*ST特殊涨跌幅板上订单必能按目标价或开盘价/收盘价全额成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**不改 Y/Z/AA–CO 及其他 A/D–CO 已交正文与冻结补丁；尤其不改假设-CO；尤其不改假设-CN；尤其不改假设-CM；尤其不改假设-CL；尤其不改假设-CK；尤其不改假设-CJ；尤其不改假设-CI；尤其不改假设-CH；尤其不改假设-CG；尤其不改假设-CF；尤其不改假设-CE；尤其不改假设-CD；尤其不改假设-X；尤其不改假设-AD；尤其不改假设-P；尤其不改假设-A；尤其不改假设-C；尤其不改假设-O；尤其不改假设-CA；尤其不改假设-CB；尤其不改假设-CC；勿再改 CO/CN/CM/CL/CK/CJ/CI/CH/CG/CF/CE/CD/CC/CB/CA/BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW/AR/AG/AN/AC/AD/Q/M/L/O/H/K/R/W/X/N/P**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CP（约 #99）。与假设 **CO（北交所连续竞价可成交性误开）** **硬分列（专节强调）**：CO = 北交所连续竞价腿假全额可成；本页 = ST/*ST特殊涨跌幅板腿假全额可成；北交所连续竞价 ≠ ST特殊涨跌幅板；**严禁复用 CO 题面或 `invent_assume_bse_continuous_auction_always_fillable`**；**尤其不改假设-CO**。**CP≠CO**。与假设 **CN/CM/CL/CK/CJ/CI/CH/CG/CF/CE/CD** **硬分列**：配股增发认购/ETF申赎/转债盘后定价/协议大宗/退市整理/上市首日/盘后固定价/复牌/集合/跌停/涨停 ≠ ST特殊涨跌幅板；**严禁复用**；**尤其不改**。**CP≠CO≠CN≠CM≠CL≠CK≠CJ≠CI≠CH≠CG≠CF≠CE≠CD**。与假设 **X（主板ST涨跌幅PIT误切）** **硬分列（专节强调）**：X = 主板 ST/*ST 板幅 5%→10% 切日误标或创业/科创风险警示误套；本页 = 在 ST 板幅层诚实（或显式旁路交 X）的前提下，是否仍默认「ST/*ST特殊涨跌幅板上订单必能按目标价或开盘价/收盘价全额成交」；板幅PIT误切 ≠ 特殊涨跌幅板假全额可成；**严禁复用 X 题面**；**尤其不改假设-X**。**CP≠X**。与假设 **AD（风险警示买入50万上限）** **硬分列（专节强调）**：AD = 当日累计买入股数上限；本页 = 特殊涨跌幅板上假全额可成；买入额度上限 ≠ 板上假全额可成；**严禁复用 AD**；**尤其不改假设-AD**。**CP≠AD**。与假设 **P（指数点位停牌假成交权重）** **硬分列（专节强调）**：**双字母 CP ≠ 单字母假设-P**；指数点位/停牌假成交权重 ≠ ST特殊涨跌幅板假全额可成；**严禁复用假设-P**；**尤其不改假设-P**。**CP≠P**。与假设 **A（涨停可成交性/板上枯竭）** **硬分列（专节强调）**：容量门槛 ≠ ST特殊涨跌幅板全额可成默认；**双字母 CP ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不占** A 的 A0/A1 主报与真数席位；**尤其不改假设-A**。**CP≠A**。与假设 **C（股票池当时名单）** **硬分列**：**双字母 CP ≠ 单字母假设-C**；**严禁复用 C**。**CP≠C**。与假设 **O（大宗假流动性）** **硬分列**：大宗量价/三通道 ≠ ST特殊涨跌幅板全额可成；**严禁复用 O**。**CP≠O**。与假设 **CD/CE（普通股连续竞价涨跌停可成交）** **硬分列（专节强调）**：CD/CE 主测普通股（非风险警示特殊板幅语境下的）连续竞价涨跌停侧假全额可成；本页主测**ST/*ST特殊涨跌幅板**宇宙；普通涨跌停侧 ≠ ST特殊涨跌幅板；**严禁把 CD/CE 主结论抄成 ST 可成**；**尤其不改 CD/CE**。**CP≠CD≠CE**。与假设 **CA/CB/CC** **硬分列**：两融公式/展期/调出了结时限 ≠ ST特殊涨跌幅板全额可成；**尤其不改 CA/CB/CC**。**CP≠CA≠CB≠CC**。与假设 **AR/AG/AN/BZ/BY/BX/BW…** 及两融审批/费用族 **硬分列**。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A / 假设-C / 假设-P / 假设-CO / 假设-CN / 假设-CM / 假设-CL / 假设-CK / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-X / 假设-AD / 假设-O**。**严禁改写/续写假设-CO / 假设-CN / 假设-CM / 假设-CL / 假设-CK / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-X / 假设-AD / 假设-P / 假设-A / 假设-C / 假设-O / 假设-CA / 假设-CB / 假设-CC**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CP** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名；**尤重 params.N ≠ 实验字母 CP ≠ 单字母假设-N**）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 P**（指数点位停牌假成交权重；**严禁复用假设-P**）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **单字母实验 X**（主板ST涨跌幅PIT；**严禁复用假设-X**）≠ **单字母实验 O**（大宗假流动性；**严禁复用假设-O**）≠ **双字母实验 CO**（北交所连续竞价；**严禁改写假设-CO**）≠ **双字母实验 CN**（配股增发认购；**严禁改写假设-CN**）≠ **双字母实验 CM**（ETF申赎；**严禁改写假设-CM**）≠ **双字母实验 CL**（可转债盘后定价；**严禁改写假设-CL**）≠ **双字母实验 CK**（协议大宗；**严禁改写假设-CK**）≠ **双字母实验 CH**（盘后固定价；**严禁改写假设-CH**）≠ **双字母实验 AD**（风险警示买入上限；**严禁改写假设-AD**）≠ **双字母实验 CA/CB/CC/CD/CE/CF/CG/CI/CJ** ≠ **单字母实验 B/Z/K/D/I/J/H/M/N/W**。全文凡写「实验 CP / 假设-CP / hypothesis_id=CP / 组 CP0·CP1·CP2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CP 混读或互改；**尤其 params.Y ≠ 实验字母 CP ≠ 单字母假设-C ≠ 单字母假设-P ≠ 单字母假设-A ≠ 双字母假设-CO ≠ 双字母假设-CN ≠ 双字母假设-CM ≠ 双字母假设-CL ≠ 双字母假设-CK ≠ 双字母假设-CH ≠ 双字母假设-AD ≠ 双字母假设-CA/CB/CC/CD/CE/CF/CG/CI/CJ**；**尤其 params.N ≠ 实验字母 CP**。亦**禁止**把实验字母 CP 与单字母 **A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/Q/R/T/S/U/V/W/X/Y/Z/P**、双字母 **BA–CO**、双字母 **CA–CO/AR/AG/AN/AC/AD/AB/AI/AJ/AQ/AZ/AY/AX/AW**、或 params 键名 `cp0_*` 以外的实验页混读。**双字母 CP ≠ 单字母 C ≠ 单字母 P ≠ 单字母 A ≠ 单字母 X ≠ 单字母 O ≠ 双字母 CO ≠ 双字母 CN ≠ 双字母 CM ≠ 双字母 CL ≠ 双字母 CK ≠ 双字母 CH ≠ 双字母 AD ≠ 双字母 CA–CJ ≠ 双字母 AR ≠ 双字母 AG ≠ 双字母 AN ≠ 双字母 BA–BZ**；**params.Y ≠ 实验字母 CP**；**params.G ≠ 实验字母 CP**；**params.N ≠ 实验字母 CP**。**带过：双字母 CO ≠ C/O/AC/CA–CN/A…；双字母 CN ≠ C/N/W/BP/CA–CM/A…；双字母 CM ≠ C/M/R/CA–CL/A…；双字母 CL ≠ C/L/Q/CA–CK/A/M…；双字母 CK ≠ C/K/O/CA–CJ/A/M…；双字母 AD ≠ A/D/X/H…；双字母 BK ≠ 单字母假设-K**（本页只引用、不改写）。

### 专节 · 双字母 CP ≠ 单字母假设-A / 假设-C / 假设-P / 假设-X / 假设-O；且 ≠ 假设-CO / 假设-CN / 假设-CM / 假设-CL / 假设-CK / 假设-CH / 假设-CA–CJ / 假设-AD；带过 CO≠CN/CM/CL/CK/CH/O/A…、params.Y≠CP、params.N≠CP、尤重 CP≠P（硬）

| 维度 | 对照页 | 本页假设-CP（双字母） |
|------|--------|----------------------|
| 题面 CO | **北交所连续竞价可成交性误开**（`invent_assume_bse_continuous_auction_always_fillable`） | **ST特殊涨跌幅板可成交性误开**：默认「ST/*ST特殊涨跌幅板上订单必能按目标价或开盘价/收盘价全额成交」vs 诚实ST特殊涨跌幅板撮合/封板/对手盘约束；北交所连续竞价 ≠ ST特殊涨跌幅板；**严禁复用 CO 题面**；**CP≠CO**；**不改 CO** |
| 题面 CN | **配股增发认购可成交性误开**（`invent_assume_rights_seo_subscription_always_fillable`） | 认购缴款 ≠ ST特殊涨跌幅板；**严禁复用 CN**；**CP≠CN**；**不改 CN** |
| 题面 CM | **ETF申赎可成交性误开**（`invent_assume_etf_creation_redemption_always_fillable`） | ETF申赎 ≠ ST特殊涨跌幅板；**严禁复用 CM**；**CP≠CM**；**不改 CM** |
| 题面 CL | **可转债盘后定价可成交性误开**（`invent_assume_cb_after_hours_pricing_always_fillable`） | 转债盘后定价 ≠ ST特殊涨跌幅板；**严禁复用 CL**；**CP≠CL**；**不改 CL** |
| 题面 CK | **协议大宗可成交性误开**（`invent_assume_block_trade_always_fillable`） | 协议大宗 ≠ ST特殊涨跌幅板；**严禁复用 CK**；**CP≠CK**；**不改 CK** |
| 题面 CJ | **退市整理期可成交性误开**（`invent_assume_delist_period_always_fillable`） | 退市整理期 ≠ ST特殊涨跌幅板；**严禁复用 CJ**；**CP≠CJ**；**不改 CJ** |
| 题面 CI | **新股上市首日可成交性误开**（`invent_assume_ipo_day1_always_fillable`） | 上市首日 ≠ ST日常特殊涨跌幅板；**严禁复用 CI**；**CP≠CI**；**不改 CI** |
| 题面 CH | **盘后固定价格可成交性误开**（`invent_assume_after_hours_fixed_price_always_fillable`） | 盘后固定价 ≠ ST特殊涨跌幅板；**严禁复用 CH**；**CP≠CH**；**不改 CH** |
| 题面 CG | **停牌复牌首日可成交性误开**（`invent_assume_resume_from_halt_always_fillable`） | 复牌首日 ≠ ST特殊涨跌幅板；**严禁复用 CG**；**CP≠CG**；**不改 CG** |
| 题面 CF | **集合竞价可成交性误开**（`invent_assume_call_auction_always_fillable`） | 集合竞价 ≠ ST特殊涨跌幅板全额可成默认；**严禁复用 CF**；**CP≠CF**；**不改 CF** |
| 题面 CE | **跌停板可成交性误开**（`invent_assume_limit_down_always_fillable`） | 普通股连续竞价跌停侧 ≠ ST特殊涨跌幅板宇宙；**严禁复用 CE**；**CP≠CE**；**不改 CE** |
| 题面 CD | **涨停板可成交性误开**（`invent_assume_limit_up_always_fillable`） | 普通股连续竞价涨停侧 ≠ ST特殊涨跌幅板宇宙；**严禁复用 CD**；**CP≠CD**；**不改 CD** |
| 题面 X | **主板ST涨跌幅PIT误切**（清单实验 X；5%→10%切日） | 板幅PIT误切 ≠ 特殊涨跌幅板假全额可成；**严禁复用 X**；**CP≠X**；**不改 X** |
| 题面 AD | **风险警示买入50万上限**（清单实验 AD） | 买入额度上限 ≠ 特殊涨跌幅板全额可成；**严禁复用 AD**；**CP≠AD**；**不改 AD** |
| 题面 P | **指数点位停牌假成交权重**（清单实验 P） | 指数点位/停牌权重 ≠ ST特殊涨跌幅板全额可成；**双字母 CP ≠ 单字母假设-P**；**严禁复用假设-P**；**CP≠P**；**不改 P** |
| 题面 A | **涨停可成交性/板上枯竭**（清单实验 A；真数队列） | 容量门槛 ≠ ST特殊涨跌幅板全额可成默认；**严禁复用 A 题面**；**绝不可做成 A 续篇**；**不抢 A 真数队列**；**CP≠A** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 股票池 ≠ ST特殊涨跌幅板全额可成；**严禁复用 C**；**CP≠C** |
| 题面 O | **大宗假流动性**（清单实验 O） | 大宗量价/三通道 ≠ ST特殊涨跌幅板全额可成；**严禁复用 O**；**CP≠O**；**不改 O** |
| 题面 CA | **维持担保比例分子分母口径** | 公式 ≠ ST特殊涨跌幅板全额可成；**CP≠CA**；**不改 CA** |
| 题面 CB | **融资合约展期/续作审批** | 展期审批 ≠ ST特殊涨跌幅板全额可成；**CP≠CB**；**不改 CB** |
| 题面 CC | **两融标的调出强制了结时点** | 调出了结时限 ≠ ST特殊涨跌幅板全额可成；**CP≠CC**；**不改 CC** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_assume_st_special_limit_board_always_fillable`（**写死冻结**单一主报；禁双挂 asof_leak；CP1不升格） |
| 文档 | 清单实验 A / C / P / X / O / AD / `假设-CA-…` … / `假设-CO-…`（**只读；禁止改写**） | `假设-CP-ST特殊涨跌幅板可成交性误开.md`（新建） |
| 预检键 | 实验字母 A / C / P / X / O / AD / CA / CB / CC / CD / CE / CF / CG / CH / CI / CJ / CK / CL / CM / CN / CO | 实验字母 **CP** / `cp0_primary_demo`；**不得**占用或改写预检 A/C/P/X/O/AD/CA–CO |

**禁止**：把 CP 写成「A/CO/CN/CM/CL/CK/CJ/CI/CH/CG/CF/CE/CD/X/AD/P/C/O/CA/CB/CC 的续篇」；把「板上容量已诚实（A）/ 北交所连续竞价可成交已诚实（CO）/ 配股增发认购可成交已诚实（CN）/ ETF申赎可成交已诚实（CM）/ 可转债盘后定价可成交已诚实（CL）/ 协议大宗可成交已诚实（CK）/ 退市整理期可成交已诚实（CJ）/ 上市首日可成交已诚实（CI）/ 盘后固定价可成交已诚实（CH）/ 复牌首日可成交已诚实（CG）/ 集合竞价可成交已诚实（CF）/ 跌停可成交已诚实（CE）/ 涨停可成交已诚实（CD）/ ST板幅PIT已诚实（X）/ 风险警示买入上限已诚实（AD）/ 指数点位权重已诚实（P）/ 股票池已诚实（C）/ 大宗量价已诚实（O）/ 分子分母已诚实（CA）/ 展期审批已诚实（CB）/ 调出了结时限已诚实（CC）」静默写成「ST特殊涨跌幅板可成交性已诚实」；覆盖或补丁改写假设-A / 假设-CO / 假设-CN / 假设-CM / 假设-CL / 假设-CK / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-X / 假设-AD / 假设-P / 假设-C / 假设-O / 假设-CA / 假设-CB / 假设-CC 正文；把 `params.Y/G/N` 与实验字母 CP 混读；**禁** `cp0_primary_demo` 与 `invent_asof_leak_st_special_limit_board_always_fillable` **双挂主报**；**禁** CP1 半泄露升格并列主报；**禁**复用假设-A / 假设-C / 假设-P / 假设-CO / 假设-CN / 假设-CM / 假设-CL / 假设-CK / 假设-CJ / 假设-CI / 假设-CH / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-X / 假设-AD / 假设-O 题面或口径键；**禁**复用 CO/CN/CM/CL/CK/CJ/CI/CH/CG/CF/CE/CD/X/AD/P/CA/CB/CC 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有路径、同一未复权价、同一 T+1、同一板上容量/排队位次/成交时点与停牌/涨跌停可成交/集合竞价可成交/复牌首日可成交/盘后固定价可成交/上市首日可成交/退市整理期可成交/协议大宗可成交/可转债盘后定价可成交/ETF申赎可成交/配股增发认购可成交/北交所连续竞价可成交/ST板幅PIT/风险警示买入上限/指数点位权重/大宗假流动性等输入（A/AR/D/CD/CE/CF/CG/CH/CI/CJ/CK/CL/CM/CN/CO/X/AD/P/O 层诚实或显式旁路声明「本页不重开板上容量门槛/假队首/开收时点与停牌期间假成交/普通股连续竞价涨跌停全额可成/集合竞价全额可成/复牌首日全额可成/盘后固定价全额可成/上市首日全额可成/退市整理期全额可成/协议大宗全额可成/转债盘后定价全额可成/ETF申赎全额可成/配股增发认购全额可成/北交所连续竞价全额可成/ST板幅PIT/风险警示买入上限/指数点位权重/大宗量价」）下，把「ST/*ST特殊涨跌幅板上订单必能按目标价或开盘价/收盘价全额成交」或「全样本用核对日当天更宽『ST/*ST特殊涨跌幅板一律全额可成』规则回放历史」当成默认，相对「每个交易日按当时有效ST/*ST特殊涨跌幅板撮合/封板/对手盘约束 PIT（部分成交记截断；封板枯竭/对手盘不足记失败或 partial；停牌中该腿 skip；缺字段 skip/敏感性；不抢 A 真数席位；不把普通股 CD/CE 涨跌停全额可成静默抄成 ST 可成；不把 X 板幅层或 AD 买入上限层静默写成板上可成；不把 P 指数权重写成板上可成）」的诚实组，会**系统性发明假全额可成路径并高估ST/*ST特殊涨跌幅板腿可实现成交、低估封板枯竭、对手盘不足与部分成交截断**；差异应**集中在ST特殊涨跌幅板可成交性误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假全额可成贡献差、可实现成交差、封板枯竭失败差、部分成交截断差在标定噪声带内可忽略，且「假全额可成 / 核对日泄露 / ST特殊涨跌幅板窗 / vs A·CO·CN·CM·CL·CK·CJ·CI·CH·CG·CF·CE·CD·X·AD·P·C·O·CA·CB·CC·AR·AG·AN·T·S·U·V」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · cp0 与锚 **三条已冻**）

```
# 配置写死键（见 §7；预检有条件通过 · 三条已冻 · 待复检；下列已写死冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CP；≠ 单字母假设-C；≠ 单字母假设-P；≠ 单字母假设-A；≠ 双字母假设-CO/CN/CM/CL/CK/CH/AD/CA–CJ
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CP；≠ 单字母假设-G
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CP；≠ 单字母假设-N；亦≠实验字母 BN；**尤重 params.N ≠ 实验字母 CP**
# params.fill_time 写死冻结 next_open
# params.asof_check_date 写死冻结 2026-10-16
# params.px_basis 建议 unadj
# params.st_special_limit_fill_honest 写死冻结 pit_by_st_special_limit_board_fill_rule
# params.st_special_limit_fill_scope 写死冻结 assume_st_special_limit_board_always_fillable_at_target_or_open_or_close
# params.st_special_limit_fill_over_policy 写死冻结 fail_or_partial_or_fail_missing_st_special_limit_fill_rule
# params.st_special_limit_px_mode 建议 target_or_open_or_close   # ST特殊涨跌幅板；禁静默抄普通股 CD/CE 或盘后固定价/大宗/北交所连续竞价通道
# params.board_capacity_handoff 建议 a_page
# params.queue_handoff 建议 ar_page
# params.fill_time_suspend_handoff 建议 d_page
# params.beyond_limit_handoff 建议 ag_page
# params.limit_up_fill_handoff 建议 cd_page          # 普通股涨停侧交 CD；CP≠CD；严禁复用假设-CD
# params.limit_down_fill_handoff 建议 ce_page
# params.call_auction_fill_handoff 建议 cf_page
# params.resume_halt_fill_handoff 建议 cg_page
# params.after_hours_fill_handoff 建议 ch_page
# params.ipo_day1_fill_handoff 建议 ci_page
# params.delist_period_fill_handoff 建议 cj_page
# params.block_trade_fill_handoff 建议 ck_page
# params.cb_ah_pricing_fill_handoff 建议 cl_page
# params.etf_cr_fill_handoff 建议 cm_page
# params.rights_seo_fill_handoff 建议 cn_page
# params.bse_cont_fill_handoff 建议 co_page         # 北交所连续竞价交 CO；CP≠CO；严禁复用假设-CO
# params.st_limit_handoff 建议 x_page               # ST板幅PIT交 X；CP≠X；严禁复用假设-X
# params.risk_warn_buy_cap_handoff 建议 ad_page     # 买入上限交 AD；CP≠AD；严禁复用假设-AD
# params.index_weight_handoff 建议 p_page           # 指数点位权重交 P；CP≠P；严禁复用假设-P
# params.block_liquidity_handoff 建议 o_page
# params.universe_pool_handoff 建议 c_page
# params.maint_ratio_formula_handoff 建议 ca_page
# params.financing_rollover_handoff 建议 cb_page
# params.delist_force_deadline_handoff 建议 cc_page
# params.st_special_limit_fill_handoff 建议 self
# params.cp0_primary_demo                写死冻结 invent_assume_st_special_limit_board_always_fillable
# params.cp0_invent_assume_st_special_limit_board_always_fillable 建议 True
# params.cp1_asof_leak_st_special_limit_board_always_fillable_only 建议 True
# params.cp2_pit_st_special_limit_fill 建议 True
# params.merge_with_A_fill 建议 False
# params.merge_with_AR_queue 建议 False
# params.merge_with_D_fill_time 建议 False
# params.merge_with_C_universe_pool 建议 False
# params.merge_with_O_block_liquidity 建议 False
# params.merge_with_P_index_weight 建议 False
# params.merge_with_X_st_limit 建议 False
# params.merge_with_AD_risk_warn_buy_cap 建议 False
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
# params.merge_with_CM_etf_cr_fill 建议 False
# params.merge_with_CN_rights_seo_fill 建议 False
# params.merge_with_CO_bse_cont_fill 建议 False
# params.merge_with_AG_beyond_limit 建议 False
# params.missing_st_special_limit_fill_policy 建议 skip
# params.day_freq_proxy 建议 st_special_limit_fill_sensitivity
# params.universe_rule 建议 st_special_limit_board_fill_misopen_check
# params.fail_policy 写死冻结 skip
# params.redline_v0_exempt_scope 建议 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 CP；params.G≠实验字母 CP；params.N≠实验字母 CP；禁 null/holdout；勿改已冻他字母数值）
# params.date_start / date_end 建议 2019-01-01..2026-09-30
# params.oos_split.*                     建议四日期；禁 holdout 反调
# CP0：假全额可成——ST/*ST特殊涨跌幅板腿按目标价或开盘价/收盘价 100% 成交
# CP1：仅 asof 日更宽「ST/*ST特殊涨跌幅板一律全额可成」规则泄露铺满
# CP2：每个交易日 d 按当时已生效ST/*ST特殊涨跌幅板撮合/封板/对手盘规则 PIT
# 缺ST/*ST特殊涨跌幅板可成交约束字段 → skip（params.missing_st_special_limit_fill_policy）
# *0 禁 asof_leak 双挂；CP1不升格
```

### 2.2 三组对照（CP0 / CP1 / CP2）

| 组 | 角色 | 规则 |
|----|------|------|
| CP0 | 天真 / 假全额可成 | 按 `cp0_primary_demo` **写死冻结**单一主报 `invent_assume_st_special_limit_board_always_fillable`：ST/*ST特殊涨跌幅板腿按目标价或开盘价/收盘价 100% 成交（**禁**与 `invent_asof_leak_st_special_limit_board_always_fillable` 双挂主报） |
| CP1 | 半泄露 | 仅核对日（asof）更宽「ST/*ST特殊涨跌幅板一律全额可成」规则泄露铺满全历史；**不得升格并列主报**（建议：CP1不升格） |
| CP2 | 诚实 PIT | `st_special_limit_fill_honest=pit_by_st_special_limit_board_fill_rule`（写死冻结）：每个交易日按当时已生效ST/*ST特殊涨跌幅板撮合/封板/对手盘规则；缺字段 skip |

### 2.3 额度窗内时频可落点（写明但不真跑）

主窗建议 `2019-01-01..2026-09-30`（额度窗内）；asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。本页**不开回测**；不拉真数；不做实盘。

### 3.1 oos_split（建议四日期；拉数前冻结；禁 holdout 反调）

建议四段日期写死于拉数前；**禁止** holdout 反调；具体四日期待预检与额度窗对齐后冻结。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（CP0）/ 半泄露组（CP1）相对诚实组（CP2）的假全额可成贡献差、可实现成交差、封板枯竭失败差、部分成交截断差**显著且集中在ST特殊涨跌幅板可成交性误开桶**；分桶「假全额可成 / 核对日泄露 / ST特殊涨跌幅板窗 / vs A·CO·CN·CM·CL·CK·CJ·CI·CH·CG·CF·CE·CD·X·AD·P·C·O·CA·CB·CC…」不改变主结论方向。

### 3.2 失败（假设不成立 / 设计失效）

上述差异在标定噪声带内可忽略；或差异主要由 A/CO/CN/CM/CL/CK/CJ/CI/CH/CG/CF/CE/CD/X/AD/P/C 等旁路页解释而非本页主病；或缺字段过多导致有效样本不足；或 oos/holdout 反调污染。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CP0/CP1/CP2。报告假全额可成贡献差、可实现成交差、封板枯竭失败差、部分成交截断差。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前冻结；禁 holdout 改桶）

建议默认桶名（待预检冻结）：`invent_assume_st_special_limit_board_always_fillable` / `invent_asof_leak_st_special_limit_board_always_fillable` / `vs_A_board_capacity` / `vs_CO_bse_cont_fill` / `vs_CN_rights_seo_fill` / `vs_CM_etf_cr_fill` / `vs_CL_cb_ah_pricing_fill` / `vs_CK_block_trade_fill` / `vs_CJ_delist_period_fill` / `vs_CI_ipo_day1_fill` / `vs_CH_after_hours_fill` / `vs_CG_resume_halt_fill` / `vs_CF_call_auction_fill` / `vs_CE_limit_down_fill` / `vs_CD_limit_up_fill` / `vs_X_st_limit` / `vs_AD_risk_warn_buy_cap` / `vs_P_index_weight` / `vs_C_universe_pool` / `vs_O_block_liquidity` / `vs_CA_maint_ratio` / `vs_CB_rollover` / `vs_CC_delist_force` / `vs_AR_queue` / `vs_AG_beyond_limit` / `vs_AN_auction_leftover` / `vs_T_csrc_fee` / `vs_S_handling_fee` / `vs_U_transfer_fee` / `vs_V_stamp_tax`。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 缺ST/*ST特殊涨跌幅板撮合、封板、对手盘字段，静默当假全额可成（应 skip）。
- 把 X「ST板幅PIT」已诚实误写成「ST特殊涨跌幅板可成交性已诚实」。
- 把 AD「风险警示买入上限」已诚实误写成 ST特殊涨跌幅板可成交已诚实。
- 把 CD/CE「普通股涨跌停可成交」已诚实误写成 ST特殊涨跌幅板可成交已诚实。
- 把 CO「北交所连续竞价可成交」已诚实误写成 ST特殊涨跌幅板可成交已诚实。
- 把 CN/CM/CL/CK/CJ/CI/CH/CG/CF 可成交已诚实误写成 ST特殊涨跌幅板可成交已诚实。
- 把 A 真数队列或把 CP 做成 A/CO/X/AD/P 续篇。
- `cp0_primary_demo` 与 asof_leak 双挂主报；CP1 升格并列主报。
- 扩窗出额度、改已冻 Y/G/N/Y2、标纸面齐、开回测/真数/实盘。
- 实验字母 CP 与单字母 C/P/A/X 或双字母 CA–CO/AD 或 params.Y/G/N 混读。
- **复用假设-P 指数点位停牌假成交权重题面**；**复用假设-CO 北交所连续竞价题面**；**复用假设-X 主板ST涨跌幅PIT题面**；**复用假设-AD 风险警示买入上限题面**；**复用假设-CD/CE 普通股涨跌停可成交题面**。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 未复权 OHLC / 买卖方向 / T+1 信号日。
- ST/*ST特殊涨跌幅板腿代理、目标价/开盘价/收盘价、对手盘深度/成交量代理、封板状态/剩余量代理、停牌标记、风险警示股宇宙标签（含 *ST）。
- 当时有效ST/*ST特殊涨跌幅板撮合/封板/对手盘约束规则及生效日（特殊涨跌幅板；禁静默抄普通股 CD/CE 全额可成或盘后固定价/大宗/北交所连续竞价/认购通道）。
- A/AR/D/CD/CE/CF/CG/CH/CI/CJ/CK/CL/CM/CN/CO/X/AD/P/O/C/CA/CB/CC 旁路诚实标记或显式旁路声明。
- 交易日历；asof 建议=2026-10-16 锚。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- hypothesis_id=`CP`；组 CP0/CP1/CP2。
- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`st_special_limit_fill_honest=pit_by_st_special_limit_board_fill_rule`；`st_special_limit_fill_scope=assume_st_special_limit_board_always_fillable_at_target_or_open_or_close`；`st_special_limit_fill_over_policy=fail_or_partial_or_fail_missing_st_special_limit_fill_rule`；`fail_policy=skip`；`cp0_primary_demo=invent_assume_st_special_limit_board_always_fillable`（**写死冻结**单一主报；禁双挂 asof_leak；CP1不升格）。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CP**；**params.G≠实验字母 CP**；**params.N≠实验字母 CP**；禁 null/holdout；**勿改已冻他字母数值**）。
- 主窗建议 `2019-01-01..2026-09-30`；oos_split 四日期建议写死+禁 holdout 反调。
- 全部 `merge_with_*=False`（见 §2.1）。
- **本页不开回测**；不催 8765；不抢 A 真数。

---

## 8. 结论

（空；本页不开回测；不写买卖建议。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-04）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 CP**；**`params.G` ≠ 实验字母 CP**；**`params.N` ≠ 实验字母 CP**；**`params.Y` ≠ 单字母实验 C/P/A/X/Z**；尤其 **双字母 CP ≠ 单字母假设-A**；**双字母 CP ≠ 单字母假设-C**；**双字母 CP ≠ 单字母假设-P**；**双字母 CP ≠ 双字母假设-CO/CN/CM/CL/CK/CH/CG/CF/CE/CD/CA/CB/CC/AD/X**；禁 null/holdout/跑后改口；**勿改他字母已冻 Y/G/N/Y2**。 

2. **`params.cp0_primary_demo`**：**写死冻结** **`invent_assume_st_special_limit_board_always_fillable`**；禁止与 **`invent_asof_leak_st_special_limit_board_always_fillable`** 双挂争主表（只挂一个 primary）；**CP1 半泄露不得升格并列主报**。 

3. **ST特殊涨跌幅板可成交性锚升格写死（不可再写「建议」）**：`params.st_special_limit_fill_honest=pit_by_st_special_limit_board_fill_rule`；`params.st_special_limit_fill_scope=assume_st_special_limit_board_always_fillable_at_target_or_open_or_close`；`params.st_special_limit_fill_over_policy=fail_or_partial_or_fail_missing_st_special_limit_fill_rule`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。

**硬分列保留**：CP≠CO/CN/CM/CL/CK/CH/C/P/A/X/AD/CA–CO…；**尤其 CP≠CO / CP≠CN / CP≠CM / CP≠CL / CP≠CK / CP≠CH / CP≠P / CP≠X / CP≠AD / CP≠CJ / CP≠CI / CP≠CG / CP≠CF / CP≠CE / CP≠CD / CP≠A / CP≠O**；**双字母 CP ≠ 单字母假设-C / 假设-P / 假设-A**；**严禁复用假设-P / 假设-CO / 假设-CN / 假设-CM / 假设-CL / 假设-CK / 假设-CH / 假设-CJ / 假设-CI / 假设-CG / 假设-CF / 假设-CE / 假设-CD / 假设-X / 假设-AD / 假设-A / 假设-C / 假设-O**；不抢A；**params.Y/G/N ≠ 实验字母 CP**。

**状态**：预检有条件通过 · 三条已冻 · 待复检；**禁止标任何纸面齐**；本页不开回测/真数/实盘；不改已冻 A/D–CO…BK。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 风控预检补丁·冻结三条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CP**；**params.G≠实验字母 CP**；**params.N≠实验字母 CP**；亦≠单字母实验 C/P/A/X/Z；尤其 **双字母 CP ≠ 单字母假设-A/C/P**；**双字母 CP ≠ 双字母假设-CO/CN/CM/CL/CK/CH/CG/CF/CE/CD/CA/CB/CC/AD/X**；禁 null/holdout/跑后改口）；② `params.cp0_primary_demo=invent_assume_st_special_limit_board_always_fillable` 单一主报写死（禁与 `invent_asof_leak_st_special_limit_board_always_fillable` 双挂；CP1不升格）；③ 锚升格写死 `st_special_limit_fill_honest=pit_by_st_special_limit_board_fill_rule` / `scope=assume_st_special_limit_board_always_fillable_at_target_or_open_or_close` / `over_policy=fail_or_partial_or_fail_missing_st_special_limit_fill_rule` / `asof=2026-10-16` / `fill_time=next_open` / `fail=skip`；状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；不改已冻 A/D–CO…BK；不开回测/真数/实盘。基于 tip=`a0ab994`。 |
| 2026-11-04 | 新建草稿·待入库预检（总管线：CO 补丁 tip=`f6668fb` 已交后写 CP；选题ST特殊涨跌幅板可成交性误开；cp0 建议 `invent_assume_st_special_limit_board_always_fillable`；清单约 #99；硬分列 CP≠C/P/CA–CO…（尤≠CO/CN/CM/CL/CK/CH/P/A/X/AD）；**禁止标任何纸面齐**）。 |
