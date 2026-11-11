# 假设-EN · 现金选择权结算费误套行权过户或成交结算费或权证结算或沪深合成（费用层，不是行权过户，也不是 B 股二级成交结算费）

来源：总管线 / 基 tip=`5e0e4981` / 全长 `5e0e498165a3c0ff447a33e4f2fec6e6963e9e71`（A/D–EM纸面齐已合，已收讫）；分支起点 HEAD=`e88b7463e31322289d76c45e7fb187e9c5e1a58f`；开工核 origin/main 仍停在该提交，未比该基线前进；口径用「诚实锚」「收讫」「暂缓」（讫=U+8BAB）；**不改已冻 A–EM**；**零改 U**；**零改 DA**；**零改 DD**；**零改 DQ**；**零改 CZ**；**零改 V**；**零改 S**；**零改 AX**；**零改 DG**；**零改 CY**；**零改 T**；**零改 DF**；**零改 DI**；**零改 DW**；**零改 DL**；**零改 DN**；**零改 DV**；**零改 EH**；**零改 EG**；**零改 EF**；**零改 EE**；**零改 ED**；**零改 EC**；**零改 EB**；**零改 EI**；**零改 EJ**；**零改 EK**；**零改 EL**；**零改 EM**；**零改 O**；**零改 DO**；**零改 DB**；不改假设-U / 假设-DA / 假设-DD / 假设-DQ / 假设-CZ / 假设-V / 假设-S / 假设-AX / 假设-DG / 假设-CY / 假设-T / 假设-DF / 假设-DI / 假设-DW / 假设-DL / 假设-DN / 假设-DV / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EB / 假设-EI / 假设-EJ / 假设-EK / 假设-EL / 假设-EM / 假设-O / 假设-DO / 假设-DB / 假设-EA 正文/预检/复检，亦不改已齐 A–EM 其他已存在假设页；**不改假设-B**（勿复用·无独立正文，亦不新建）；**不重开假设-R**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-S**；**不重开假设-AX**；**不重开假设-DI**；**不重开假设-DB**；**不重开假设-DF**；**不重开假设-DO**；**不重开假设-DW**；**不重开假设-EH**；**不重开假设-EI**；**不重开假设-EJ**；**不重开假设-EK**；**不重开假设-EL**；**不重开假设-EM**；**不重开假设-DL**；**不重开假设-DV**；**不重开假设-O**）后写下一草稿 EN；清单 #148=EM，本页占用 **#149=EN**；选题是回测把 **现金选择权行权所涉中国结算结算费**套错（诚实方向：须沪深分列，并须 A 股 / B 股分列——深市中国结算结算费栏「A 股现金选择权」原文「按清算金额的 0.015‰向结算参与人单向收取。」；「B 股现金选择权」通过交易系统申报的行权业务，按照行权清算金额的 0.015‰向结算参与人单向收取行权结算费，不通过交易系统申报的手工行权业务不收取行权结算费；沪市结算费栏无「A 股现金选择权」「B 股现金选择权」专行，该腿费率细节 skip；收费对象栏为结算参与人，不得因此把投资者侧发明为 0；不得按假设-DV 的行权过户面值 0.5‰ 计，不得按已只补的 B 股二级成交结算费 0.02‰ 计，不得因同是 0.015‰ 抄权证交易/行权结算费，不得把沪市无专行写成与深市同档，不得把深市 A 股与 B 股合成一句，不得把系统申报档铺到手工行权，不得把手工行权不收取发明成全部为 0 或永久 0，不得把 params.Y2 的 0.015 读成 0.015‰；不得写成「沪深均为 0.015‰」；缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip；切日未钉的历史费率变更 skip，不发明切日；行权过户、B 股二级成交结算费、权证结算费、股票期权结算费、专项资产管理计划结算费、发行人侧派发登记费不进本页主键）；这是**费用层，不是行权过户，也不是 B 股二级成交结算费**。假设-DV 只收 A 股现金选择权行权过户，假设-DW 只收权证/股票期权行权过户，假设-EM 只收股票期权按张结算费，假设-EI 只收股票期权交易所经手费，假设-S 只收沪深 A 股竞价经手费，假设-U 只收普通股票二级过户；已只补的 B 股二级成交结算费、权证结算费、权证经手、沪市专项资产管理计划结算费都不进本页主报；**新建实验 EN**；不写下一字母；不预留 #150。

状态：**预检有条件通过·三条已冻·待复检**（结论栏空；禁止把「行权过户面值 0.5‰」或「B 股二级成交结算费 0.02‰」或「权证结算费 0.015‰」或「沪深均为 0.015‰」或「投资者侧发明为 0」或「手工行权不收取写成全部为 0」或「params.Y2 的 0.015」或「表更新日 2026年1月 / 2026-01-01」当现金选择权结算费切日或诚实锚；禁止与 DV 行权过户、DW 权证/期权行权过户、EM 股票期权结算费、已只补的 B 股成交结算费或权证结算费键双挂；诊断桶只进诊断、不升格主报；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–EM**；**零改 U**；**零改 DA**；**零改 DD**；**零改 DQ**；**零改 CZ**；**零改 V**；**零改 S**；**零改 AX**；**零改 DG**；**零改 CY**；**零改 T**；**零改 DF**；**零改 DI**；**零改 DW**；**零改 DL**；**零改 DN**；**零改 DV**；**零改 EH**；**零改 EG**；**零改 EF**；**零改 EE**；**零改 ED**；**零改 EC**；**零改 EB**；**零改 EI**；**零改 EJ**；**零改 EK**；**零改 EL**；**零改 EM**；**零改 O**；**零改 DO**；**零改 DB**；**不改 #110–#148**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–EN纸面齐**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 EN（#149）。一句话误开：回测对现金选择权行权所涉中国结算结算费，按假设-DV 的行权过户面值 0.5‰ 计，或按已只补的 B 股二级成交结算费 0.02‰ 计，或因同是 0.015‰ 抄权证交易/行权结算费（权证交易为双向、权证行权为向行权方单向），或把沪市结算费栏并无专行写成与深市同档（写成「沪深均为 0.015‰」），或把深市 A 股与 B 股两档合成一句，或把深市「通过交易系统申报」的 B 股行权结算费铺到「不通过交易系统申报的手工行权」（原文不收取），或因收费对象是结算参与人就把投资者侧发明为 0，或把 params.Y2 的 0.015 读成 0.015‰。按行权过户面值 0.5‰ 计，会把按清算金额的结算费收成过户；按 B 股二级成交结算费 0.02‰ 计，会把 0.015‰ 收成另一档，还会把收费对象从结算参与人换成投资者；因同是 0.015‰ 抄权证，会把现金选择权单向档抄成权证交易双向或权证行权向行权方单向；把沪市无专行写成与深市同档，会把该腿 skip 收成已核费率；把 A 股与 B 股合成一句，会抹掉手工行权不收取；把系统申报档铺到手工行权，会把原文不收取的腿收成 0.015‰；发明为 0，会抹掉深市表上已写下的结算费；把 params.Y2 的 0.015 读成 0.015‰，会把无量纲占位收成费率。**禁把 DV/DW/EM/EI/S/U/EL/EJ/EK/EH/EG/AX/V/T/O 混读升格进 `en0_primary_demo`**。**禁把沪深合成一句、把 A 股与 B 股互抄、把系统申报档铺到手工行权、把 0.015‰ 与 0.5‰ / 0.02‰ / params.Y2 的 0.015 混读、发明为 0，另挂第二主键**。这些只作同一误开的并列形态。**禁把切日发明键与主报双挂**。上述只进诊断、不升格主报。**禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格、不另挂主报、零改 O**。

> **字母消歧（硬）**：本页**实验字母 EN** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 EN**；**尤重：`params.Y/G/N` ≠ 实验字母 EN / 单字母 E / 假设-EM / 假设-EL / 假设-EI / 假设-DV**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-DV / 假设-DW**；**勿把 `params.Y` 读成实验字母 EN，亦勿读成单字母假设-E，亦勿读成假设-EM，亦勿读成假设-DV，亦勿读成假设-DW，亦勿读成假设-S，亦勿读成假设-U，亦勿读成假设-V，亦勿读成假设-T**；**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰ ≠ 实验字母 EN ≠ 单字母 E ≠ 假设-EM ≠ 假设-DV**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 EN**；**params.G ≠ 假设-G**；**尤重：`params.G` 的 0.01 ≠ 股票过户 0.01‰ ≠ 假设-G**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是股票过户费率，也不是结算费 0.015‰，也不是 0.01‰）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 EN**；**params.N ≠ 单字母 E**；**尤重：`params.N` 的 0.05 ≠ 面值 0.5‰**）≠ **`params.Y2`**（写死冻结 0.015；不是结算费千分比，不是面值档，不是切日；**尤重：`params.Y2` 的 0.015 ≠ 结算费 0.015‰**）≠ **单字母实验 E**（整手与科创板 200 股；**双字母 EN ≠ 单字母假设-E；严禁复用假设-E**）≠ **双字母 DV**（A 股现金选择权行权过户，深市交易过户栏按行权股票过户面值的 0.5‰向投资者单向收取；**零改 DV**；**EN≠DV**；**不重开假设-DV**；**0.5‰ ≠ 0.015‰**；这是中国结算结算费层，不是把 DV 行权过户改写）≠ **双字母 DW**（权证/股票期权行权过户，面值 0.5‰、过入方；**零改 DW**；**EN≠DW**；**不重开假设-DW**）≠ **双字母 EM**（股票期权按张结算费；**零改 EM**；**EN≠EM**；**不重开假设-EM**；这不是把 EM 股票期权结算费改写；锚前缀不要写成 `option_settlement_fee_*`）≠ **双字母 EI**（股票期权交易经手；**零改 EI**；**EN≠EI**；**不重开假设-EI**；两所收费表与上证发〔2023〕137 号指引规范的是交易所经手等项目，全文无「结算费」，不能替代中国结算结算费栏）≠ **单字母 S**（沪深 A 股竞价经手费；**零改 S**；**EN≠S**；**不重开假设-S**）≠ **单字母 U**（普通股票二级过户；**零改 U**；**EN≠U**；**不重开假设-U**；**尤重：`params.G` 的 0.01 ≠ 股票过户 0.01‰**）≠ **双字母 EL**（约定购回结算过户；**零改 EL**；**EN≠EL**；**不重开假设-EL**）≠ **双字母 EJ**（约定购回经手；**零改 EJ**；**EN≠EJ**；**不重开假设-EJ**）≠ **双字母 EK**（债券现券及资产支持证券经手费；**零改 EK**；**EN≠EK**；**不重开假设-EK**；深市债券结算费 0.0004‰ 不进本页主键；**0.015‰ ≠ 0.0004‰**）≠ **双字母 EH**（优先股经手；**零改 EH**；**EN≠EH**；**不重开假设-EH**；上证发〔2015〕67 号本选题不依赖）≠ **双字母 EG**（CDR 二级过户 0.02‰；**零改 EG**；**EN≠EG**；**尤重：`params.Y` 的 0.02 ≠ EG 过户 0.02‰**）≠ **双字母 AX**（场内基金经手费；**零改 AX**；**EN≠AX**；**不重开假设-AX**）≠ **单字母 V**（印花税；**零改 V**；**EN≠V**）≠ **单字母 T**（证管费；**零改 T**；**EN≠T**；**不重开假设-T**；**`params.Y` 的 0.02 ≠ 证管费 0.02‰**）≠ **双字母 O**（大宗日量 / 三通道假流动性；**零改 O**；**EN≠O**）≠ **单字母实验 R**（股票 ETF 假 T+0；**实验 R 不抢、不重开**）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（勿复用·无独立正文）≠ **双字母 DA**（场内基金二级过户；**零改 DA**；**EN≠DA**）≠ **双字母 DD**（可转债过户缺档；**零改 DD**；**EN≠DD**）≠ **双字母 DQ**（ETF 申赎篮子过户；**零改 DQ**；**EN≠DQ**）≠ **双字母 DL**（综合协议过户下浮；**零改 DL**；**EN≠DL**；**不重开假设-DL**）≠ **双字母 DN**（可交换换股过户；**零改 DN**；**EN≠DN**）≠ **双字母 DF**（可交换现货经手；**零改 DF**；**EN≠DF**）≠ **双字母 DI**（股票大宗经手下浮；**零改 DI**；**EN≠DI**）≠ **双字母 DO**（可转债回售经手暂免；**零改 DO**；**EN≠DO**）≠ **双字母 DB**（可转债现货经手；**零改 DB**；**EN≠DB**；118 号是可转债经手费通知，本选题不依赖）≠ **双字母 CZ**（CDR 可成交性；**零改 CZ**）≠ **双字母 DG**（北交所经手费；**零改 DG**）≠ **双字母 CY**（优先股可成交性；**零改 CY**）≠ **双字母 EF**（一季报/三季报可见日；**零改 EF**；**EN≠EF**）≠ **双字母 EE**（业绩预告/快报可见日；**零改 EE**；**EN≠EE**）≠ **双字母 ED**（正式年报/中报可见日；**零改 ED**；**EN≠ED**）≠ **双字母 EC**（沪市主板大宗停牌至 15:00 仍接受；**零改 EC**；**EN≠EC**）≠ **双字母 EB**（无板证券协议大宗价限；**零改 EB**；**EN≠EB**）≠ **双字母 EA**（科创板大宗固定价格交易类型切日；**EN≠EA**）。**硬分列：EN≠DV≠DW≠EM≠EI≠S≠U≠EL≠EJ≠EK≠EH≠EG≠AX≠V≠T≠DA≠DD≠DQ≠CZ≠DG≠CY≠DF≠DI≠DL≠DN≠EF≠EE≠ED≠EC≠EB≠O≠DO≠DB**。**双字母 EN ≠ 单字母 E**。**双字母 EN ≠ 单字母假设-E**。**双字母 EN ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB**。**params.Y/G/N ≠ 实验字母 EN ≠ 单字母 E ≠ 假设-EM ≠ 假设-DV**。**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰**。**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰**。**尤重 params.N 的 0.05 ≠ 面值 0.5‰**。**尤重 params.Y2 的 0.015 ≠ 结算费 0.015‰**。**尤重须沪深及 A 股 / B 股分列，禁止写成「沪深均为 0.015‰」**。**尤重 0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰；0.015‰ ≠ params.Y2 的 0.015**。**尤重：结算费 ≠ 行权过户 ≠ B 股二级成交结算费 ≠ 权证结算费 ≠ 股票期权按张结算费**。**尤重：零改 U / DA / DD / DQ / CZ / V / S / AX / DG / CY / T / DF / DI / DW / DL / DN / DV / EH / EG / EF / EE / ED / EC / EB / EI / EJ / EK / EL / EM / O / DO / DB**。**尤重：实验 R 不抢；不重开假设-V / T / U / S / AX / DI / DB / DF / DO / DW / EH / EI / EJ / EK / EL / EM / DL / DV**。**尤重：EN ≠ DV ≠ DW ≠ EM ≠ EI ≠ S ≠ U ≠ EL ≠ EJ ≠ EK ≠ EH ≠ EG ≠ AX ≠ V ≠ T**。这是中国结算结算费层，不是把 DV 行权过户改写，也不是把 EM 股票期权结算费改写。**尤重：两所收费表与上证发〔2023〕137 号通知页及附件指引无「结算费」专行，也无现金选择权结算费专行，不能替代中国结算结算费栏，也不得用经手表否定结算费栏。指引规范的是交易所经手等项目。零改 EI**。**尤重：表「更新」2026年1月 / 「2026 年 1 月 1 日更新」不是现金选择权结算费表定费率的首次生效日。切日未钉则历史变更 skip，不发明切日。深市现行表已写下的 0.015‰ 结算费、以及 B 股手工行权不收取，可冻为现行诚实锚。缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip**。**尤重：上证发〔2022〕118 号原件本轮总管未独立打开，正文不要把该件细节写成已核依据；废止句以 137 号通知页为准（自 2023年8月28日起废止）。该件是可转债经手费通知，本选题不依赖，零改 DB。失效规则目录页有同标题同日列表路径，本轮未打开该条目页，不视为 118 号已核**。**尤重：禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格；不另挂主报；零改 O；不改选 B2/B3**。诊断桶只作对照/旁路，不得升格进 `en0_primary_demo`。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–EM；勿再只改清单）。当前草稿阶段**禁止标纸面齐**，**不写 A/D–EN纸面齐**。

### 专节 · 双字母 EN ≠ 单字母假设-E；且 ≠ DV / DW / EM / EI（硬）

| 维度 | 对照页 | 本页假设-EN（双字母） |
|------|--------|----------------------|
| 题面 DV | **现金选择权行权过户**（假设-DV 已纸面齐，已收讫） | **DV = 行权过户，不是结算费**。深市交易过户栏「A 股现金选择权行权」原文「按行权股票过户面值的 0.5‰向投资者单向收取。」「B 股现金选择权行权」原文「按行权股票过户面值的 0.5‰折算为外币，向投资者单向收取。」及「注：外币汇率以现金选择权行权清算当日中国人民银行发布的汇率中间价为准。」沪市非交易过户注：「2、要约收购及现金选择权的非交易过户费按股份过户面值的 1‰收取（双向收取）。」这些是过户层，不进本页主键。按面值 0.5‰ 或 1‰ 计结算费，正是本页误开的一种形态。**零改 DV**。**EN≠DV**；**不重开假设-DV**；**不改 DV**；**尤重：0.5‰ ≠ 0.015‰ ≠ 1‰**；**尤重：禁把 `vs_DV_cash_option_transfer` 升格进 `en0_primary_demo`**；`cash_option_transfer_handoff=dv_page` |
| 题面 DW | **权证/股票期权行权过户**（假设-DW 已纸面齐，已收讫） | **DW = 行权过户，面值 0.5‰、过入方**。不是现金选择权结算费。**零改 DW**。**EN≠DW**；**不重开假设-DW**；**不改 DW**；**尤重：禁把 `vs_DW_warrant_option_exercise_transfer` 升格进 `en0_primary_demo`**；`warrant_option_exercise_transfer_handoff=dw_page` |
| 题面 EM | **股票期权按张结算费**（假设-EM 已纸面齐，已收讫） | **EM = 股票期权交易/行权结算费，按张计**。不是现金选择权按清算金额的结算费。**零改 EM**。**EN≠EM**；**不重开假设-EM**；**不改 EM**；锚前缀不要写成 `option_settlement_fee_*`；**尤重：禁把 `vs_EM_option_settlement` 升格进 `en0_primary_demo`**；`option_settlement_handoff=em_page` |
| 题面 EI | **股票期权交易经手**（假设-EI 已纸面齐，已收讫） | **EI = 交易所经手费**。两所收费表与上证发〔2023〕137 号通知页及附件指引无「结算费」专行，也无现金选择权结算费专行。指引规范的是交易所经手等项目，全文无「结算费」。不得用经手表否定中国结算结算费栏。**零改 EI**。**EN≠EI**；**不重开假设-EI**；**不改 EI**；`option_handling_handoff=ei_page` |
| 题面 S | **沪深 A 股竞价经手费**（假设-S） | **S = A 股竞价经手**。不是现金选择权结算费。**零改 S**。**EN≠S**；**不重开假设-S**；**不改 S**；`ashare_handling_handoff=s_page` |
| 题面 U | **普通股票二级过户**（假设-U） | **U = 股票过户**。不是现金选择权结算费。**零改 U**。**EN≠U**；**不重开假设-U**；**不改 U**；**尤重：`params.G` 的 0.01 ≠ 股票过户 0.01‰**；`transfer_fee_handoff=u_page`；锚不要写成无前缀的 `settlement_fee_*` |
| 题面 EL / EJ / EK | **约定购回过户 / 约定购回经手 / 债券现券经手** | 都不是现金选择权结算费。深市债券结算费 0.0004‰ 不进本页主键。**零改 EL**。**零改 EJ**。**零改 EK**。**不重开假设-EL**。**不重开假设-EJ**。**不重开假设-EK**；`agreed_repurchase_transfer_handoff=el_page`；`agreed_repurchase_handling_handoff=ej_page`；`bond_cash_abs_handling_handoff=ek_page` |
| 题面 AX / EH | **场内基金经手 / 优先股经手** | 都不是现金选择权结算费。**零改 AX**。**零改 EH**。**不重开假设-AX**。**不重开假设-EH**；`fund_handling_handoff=ax_page`；`pref_handling_handoff=eh_page` |
| 题面 EG | **存托凭证结算过户**（假设-EG） | **EG = 二级过户 0.02‰**。不是现金选择权结算费。**零改 EG**。**EN≠EG**；**尤重：`params.Y` 的 0.02 ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰**；`cdr_transfer_handoff=eg_page` |
| 题面 V / T | **印花税 / 证管费** | 税和证管费不是结算费。**零改 V**。**零改 T**。**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page` |
| 题面 权证结算费 | 同栏按清算金额的 0.015‰，向结算参与人收取；权证交易为双向、权证行权为向行权方单向 | 不进本页主键。同是 0.015‰，不得抄到现金选择权腿。权证经手仍只补事实：深市官网已钉 0.045‰双边，上交所现行表与 137 号指引均无专行；不得写成「沪深均为 0.045‰」，不得发明沪市为 0。≠ DW。≠ 本页主键。`warrant_settlement_handoff=facts_only`；`warrant_handling_handoff=facts_only`。**尤重：`params.Y2` 的 0.015 ≠ 结算费 0.015‰** |
| 题面 B 股二级成交结算费 | 已只补：按成交金额的 0.02‰向买卖双方投资者收取 | 不进本页主键。0.02‰ ≠ 0.015‰。收费对象是投资者，不是本页结算参与人单向档。不得把 0.02‰ 套到现金选择权。**尤重：`params.Y` 的 0.02 ≠ B 股成交结算费 0.02‰**。`bshare_settlement_handoff=facts_only` |
| 题面 专项资产管理计划 | 沪市结算费栏原文「按清算金额的 0.015‰向结算参与人双向收取。」；深市结算费栏无此专行 | 只补事实，不升格。与已只补的资管计划份额转让经手不是同一项。同是 0.015‰，不得与权证结算费或现金选择权结算费合成一句。`am_plan_settlement_handoff=facts_only` |
| 题面 沪市无专行 | 结算费栏无「A 股现金选择权」「B 股现金选择权」专行 | 该腿费率细节 skip。禁止写成「沪深均为 0.015‰」，也不得因「表上没有」发明沪市为 0 或与深市同档。沪市若另有未打开专项通知，本轮未检索到，不写成已核无费 |
| 题面 A 股 / B 股合成 | 把深市两档收成一句 | `blend_ashare_and_bshare_cash_option` **只进诊断、不升格主报**。A 股按清算金额的 0.015‰单向；B 股还要再分系统申报与手工行权 |
| 题面 系统申报铺到手工 | 把 0.015‰ 铺到不通过交易系统申报的手工行权 | `spread_system_declared_fee_to_manual_exercise` **只进诊断、不升格主报**。手工行权原文不收取。不得因此把全部现金选择权发明成 0 或永久 0 |
| 题面 发明为 0 | 因收费对象是结算参与人就把投资者侧发明为 0 | `invent_investor_zero_from_participant` **只进诊断、不升格主报**。收费对象栏为结算参与人，不得因此把投资者侧发明为 0 |
| 题面 占位读成费率 | 把 params.Y2 的 0.015 读成 0.015‰ | `misread_params_y2_as_permille` **只进诊断、不升格主报**。**params.Y2 的 0.015 ≠ 结算费 0.015‰**。**params.N 的 0.05 ≠ 面值 0.5‰**。**params.G 的 0.01 ≠ 股票过户 0.01‰**。**params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰** |
| 题面 切日未钉 | 把表更新日或未打开的 118 号写成切日 | `invent_cash_option_settlement_cut_date` **只进诊断、不升格主报**。**禁止发明切日**。失效规则目录上未打开的列表条目不视为 118 号已核。零改 DB |
| 题面 B2 | **场内基金大宗门槛** | 成交规则族，不是结算费。诊断桶 `vs_B2_fund_block_threshold` 只作对照。**禁升格**。**不另挂主报**。**零改 O**。本页不改选 B2 |
| 题面 B3 | **16:00-17:00 / VWAP 暂缓窗** | 这道窗在事实稿里仍是**暂缓**，不是现行可成交，更不是结算费率。诊断桶 `vs_B3_deferred_vwap_window` 只作对照。**禁升格**。**不另挂主报**。**零改 O**。本页不改选 B3 |
| 题面 E / R | 整手页 / 股票 ETF 假 T+0 | **双字母 EN ≠ 单字母假设-E**。**实验 R 不抢**。`lot_size_handoff=e_page`；`etf_t0_handoff=r_page` |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend`（**写死冻结**单一主报，单挂写死；键名保持 `en0_primary_demo=`；值里的 `hs_blend` 只描述误套或沪深合成这一误开形态；诚实锚键名与键值禁止写成 hs_blend / both_same / 沪深均为 一类；禁与 DV 行权过户、DW 权证/期权行权过户、EM 股票期权结算费、已只补的 B 股成交结算费或权证结算费键双挂；诊断桶不升格；**零改 DV**；**零改 DW**；**零改 EM**） |
| 文档 | 清单实验 DV / DW / EM / EI / S / U 及上表各页（**只读；禁止改写**） | `假设-EN-现金选择权结算费误套过户或成交结算或权证结算或沪深合成.md`（新建） |
| 预检键 | 实验字母 DV / DW / EM / EI / S / U / V / T / O / E | 实验字母 **EN** / `en0_primary_demo`；**不得**占用或改写上述预检键；**params.Y/G/N ≠ 实验字母 EN**；不要只写裸 `en0=`；**零改 DV**；**零改 DW**；**零改 EM**；**零改 EI**；**零改 O** |

**禁止**：把 EN 写成「DV / DW / EM / EI 的续篇」；把诚实锚收成「沪深均为 0.015‰」一句；把深市 A 股与 B 股合成一句；把系统申报档铺到手工行权；把手工行权不收取发明成全部为 0 或永久 0；把 0.015‰ 读成过户 0.5‰ 或 B 股成交结算 0.02‰ 或 params.Y2 的 0.015；把 0.015‰ 与 0.0004‰ 或 1‰ 混读；因同是 0.015‰ 就把权证或沪市专项资产管理计划结算费抄到现金选择权腿；因收费对象是结算参与人就把投资者侧发明为 0；因「表上没有」发明沪市为 0 或与深市同档；把表更新日 2026年1月或 2026-01-01 写成现金选择权结算费的首次生效日；把未打开的上证发〔2022〕118 号细节写成已核依据；把失效规则目录上未打开的列表条目视为 118 号已核；把行权过户、B 股二级成交结算费、权证结算费、股票期权按张结算费、专项资产管理计划结算费捆进本页主键；用两所收费表或 137 号指引否定或替代中国结算结算费栏；把实验字母 EN 与单字母 E、假设-EM、假设-DV 或 params.Y/G/N 混读；**尤重 params.Y/G/N ≠ 实验字母 EN / 单字母 E / 假设-EM / 假设-DV**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰**；**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰**；**尤重 params.N 的 0.05 ≠ 面值 0.5‰**；**尤重 params.Y2 的 0.015 ≠ 结算费 0.015‰**；**尤重 0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰**；**禁把占位 `0.02/0.01/0.05/0.015` 读成千分比或面值档**；**实验 R 不抢**；**不重开假设-V / T / U / S / AX / DI / DB / DF / DO / DW / EH / EI / EJ / EK / EL / EM / DL / DV**；**零改 U**；**零改 DA**；**零改 DD**；**零改 DQ**；**零改 CZ**；**零改 V**；**零改 S**；**零改 AX**；**零改 DG**；**零改 CY**；**零改 T**；**零改 DF**；**零改 DI**；**零改 DW**；**零改 DL**；**零改 DN**；**零改 DV**；**零改 EH**；**零改 EG**；**零改 EF**；**零改 EE**；**零改 ED**；**零改 EC**；**零改 EB**；**零改 EI**；**零改 EJ**；**零改 EK**；**零改 EL**；**零改 EM**；**零改 O**；**零改 DO**；**零改 DB**；**现金选择权结算费 ≠ DV ≠ DW ≠ EM ≠ EI ≠ S ≠ U ≠ EL ≠ EJ ≠ EK ≠ EH ≠ EG ≠ AX ≠ V ≠ T**；**双字母 EN ≠ 单字母假设-E，亦 ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB**；**禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格**；**不另挂主报**；诊断桶只作对照/旁路，不得升格进 `en0_primary_demo`；缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额仍硬填；缺切日仍发明一个切日。本页主键只用 `en0_primary_demo` / `en1` / `en2` 与 `cash_option_settlement_fee_*`。不要只写裸 `en0=`。不写下一字母。不预留 #150。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–EM；勿再只改清单）。当前草稿阶段**禁止标纸面齐**，**不写 A/D–EN纸面齐**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测对现金选择权行权所涉中国结算结算费，按假设-DV 的行权过户面值 0.5‰ 计，或按已只补的 B 股二级成交结算费 0.02‰ 计，或因同是 0.015‰ 抄权证交易/行权结算费（权证交易为双向、权证行权为向行权方单向），或把沪市结算费栏并无专行写成与深市同档（写成「沪深均为 0.015‰」），或把深市 A 股与 B 股两档合成一句，或把深市「通过交易系统申报」的 B 股行权结算费铺到「不通过交易系统申报的手工行权」（原文不收取），或因收费对象是结算参与人就把投资者侧发明为 0，或把 params.Y2 的 0.015 读成 0.015‰，从而系统性改写现金选择权结算费腿的成本。相对「缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip；切日未钉的历史费率变更 skip，不发明切日；须沪深分列，并须 A 股 / B 股分列」的诚实组，会**系统性改写这条腿的成本**。按过户面值计，单位从清算金额换成面值；按 0.02‰ 计，档位和收费对象都换了；抄权证或抄专项资产管理计划，方向从单向换成双向或向行权方单向；发明为 0，漏掉深市表上已写下的 0.015‰。本题是**费用层，不是行权过户，也不是 B 股二级成交结算费**。

核对日方向（随锚写死；禁止把占位读成千分比或面值档）：工程于 2026-11-11 核对中国结算沪/深表「结算参与人业务收费 / 结算费」栏。两所官网收费表与上证发〔2023〕137 号通知页及附件指引无结算费专行，不能替代结算费栏，也不得用来否定结算费栏。沪深必须分列，A 股与 B 股必须分列，B 股还须把通过交易系统申报与手工行权分列，不得收成一句。`asof_check_date` 写死冻结 `2026-11-11`（本轮总管独立重抓日；不是切日；派单所记中国结算深市表重抓窗为 2026-11-11 09:27:30–09:28:06 Asia/Shanghai；稿内 09:27:30–09:28:06 与风控再下 10:03:30–10:04:06 不得以时刻否决；日期同为 2026-11-11 且官方八件哈希须保持已核 MATCH；不要写成短要点里较早的 09:18 窗口，也不要写成研究原稿或其它页可能出现的 2026-11-10 / 2026-01-01 / 2026年1月）。**禁把占位读成证管费 0.02‰、EG 过户 0.02‰、B 股成交结算费 0.02‰、股票过户 0.01‰、面值 0.5‰，也禁把占位读成结算费 0.015‰**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-DV / 假设-DW**。**尤重 params.Y/G/N ≠ 实验字母 EN / 单字母 E / 假设-EM / 假设-DV**。**尤重须沪深分列**。

证伪方向：若天真组（按行权过户 0.5‰ 计，或按 B 股二级成交结算费 0.02‰ 计，或抄权证 0.015‰，或收成「沪深均为 0.015‰」，或 A 股与 B 股合成一句，或把系统申报档铺到手工行权，或发明为 0，或把 params.Y2 的 0.015 读成 0.015‰）相对诚实组的成本差截在标定噪声带内可忽略，且「发明切日 / 用经手表替代结算费栏 / vs DV·DW·EM·EI / B2 / B3」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · en0 与锚 **三条已冻**）

```text
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结；禁止标纸面齐；不写 A/D–EN纸面齐）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 EN ≠ 单字母假设-E ≠ 假设-EM ≠ 假设-DV**
# 【消歧】尤重：params.Y/G/N ≠ 实验字母 EN / 单字母 E / 假设-EM / 假设-DV
# 【消歧】params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-DV / 假设-DW
# 【消歧】尤重：params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰ ≠ 实验字母 EN ≠ 单字母 E
# 【消歧】尤重：params.G 的 0.01 ≠ 股票过户 0.01‰ ≠ 假设-G
# 【消歧】尤重：params.N 的 0.05 ≠ 面值 0.5‰
# 【消歧】尤重：params.Y2 的 0.015 ≠ 结算费 0.015‰
# 【消歧】尤重：0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰
# 【消歧】结算费 ≠ 行权过户 ≠ B 股二级成交结算费 ≠ 权证结算费 ≠ 股票期权按张结算费
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 EN ≠ 单字母 E ≠ 面值 0.5‰**
# 【消歧】params.Y2 写死冻结 0.015；不是结算费千分比，不是面值档，不是切日
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成千分比或面值档，也禁读成证管费、过户费或经手费
# 【消歧】三条已冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值
# 【消歧】口径注释：讫=U+8BAB。正文「收讫」的讫是这个字，不要写成别的字
# 【消歧】asof_check_date 写死冻结 2026-11-11；这是本轮总管独立重抓日，不是切日；中国结算深市表重抓窗为 2026-11-11 09:27:30–09:28:06 Asia/Shanghai；稿内 09:27:30–09:28:06 与风控再下 10:03:30–10:04:06 不得以时刻否决；日期同为 2026-11-11 且官方八件哈希须保持已核 MATCH；不要写成短要点里较早的 09:18 窗口，也不要写成研究原稿或其它页可能出现的 2026-11-10 / 2026-01-01 / 2026年1月
# 【消歧】锚键名是 cash_option_settlement_fee_*，不要写成 option_settlement_fee_*，也不要写成无前缀的 settlement_fee_*
# 【消歧】诚实锚键名与键值禁止写成 hs_blend / both_same / 沪深均为 一类。en0_primary_demo 值里的 hs_blend 只描述误开形态
# 【消歧】正文键名是 en0_primary_demo=，不要只写裸 en0=
# 【消歧】双字母 EN ≠ 单字母假设-E，亦 ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB
# 【消歧】零改 U；零改 DA；零改 DD；零改 DQ；零改 CZ；零改 V；零改 S；零改 AX；零改 DG；零改 CY；零改 T；零改 DF；零改 DI；零改 DW；零改 DL；零改 DN；零改 DV；零改 EH；零改 EG；零改 EF；零改 EE；零改 ED；零改 EC；零改 EB；零改 EI；零改 EJ；零改 EK；零改 EL；零改 EM；零改 O；零改 DO；零改 DB
# 【消歧】实验 R 不抢；不重开假设-V / T / U / S / AX / DI / DB / DF / DO / DW / EH / EI / EJ / EK / EL / EM / DL / DV
# 【消歧】现金选择权结算费 ≠ DV 行权过户 ≠ DW 权证/期权行权过户 ≠ EM 股票期权按张结算费 ≠ EI 股票期权经手 ≠ S A 股经手 ≠ U 股票过户 ≠ EL 约定购回过户 ≠ EJ 约定购回经手 ≠ EK 债券现券经手 ≠ EH 优先股经手 ≠ EG CDR 过户 ≠ AX 基金经手
# 【消歧】须沪深及 A 股 / B 股分列；禁止把诚实锚写成「沪深均为 0.015‰」
# 【消歧】深市 A 股现金选择权：按清算金额的 0.015‰向结算参与人单向收取
# 【消歧】深市 B 股现金选择权：通过交易系统申报的，按照行权清算金额的 0.015‰向结算参与人单向收取行权结算费；不通过交易系统申报的手工行权业务，不收取行权结算费
# 【消歧】原件在「不通过交」与「易系统」处换行、中间无 U+0020；连写时不要另加空格
# 【消歧】沪市结算费栏无「A 股现金选择权」「B 股现金选择权」专行。该腿费率细节 skip。不得发明沪市为 0，也不得写成与深市同档
# 【消歧】收费对象栏为结算参与人；不得因此把投资者侧发明为 0
# 【消歧】不得把系统申报档铺到手工行权；不得把手工行权不收取发明成全部为 0 或永久 0
# 【消歧】不得因同是 0.015‰ 就把权证（交易双向、行权向行权方单向）或沪市专项资产管理计划（双向）抄到现金选择权腿
# 【消歧】行权过户不进主键：深市 A 股「按行权股票过户面值的 0.5‰向投资者单向收取。」；深市 B 股「按行权股票过户面值的 0.5‰折算为外币，向投资者单向收取。」及汇率中间价注；沪市非交易过户注「2、要约收购及现金选择权的非交易过户费按股份过户面值的 1‰收取（双向收取）。」零改 DV
# 【消歧】禁止发明切日；表「更新」2026年1月 / 「2026 年 1 月 1 日更新」不是首次生效日
# 【消歧】118 号原件本轮未独立打开，不得把未核细节写成已核依据；废止句以 137 号通知页为准（自 2023年8月28日起废止）；本选题不依赖该件；零改 DB；失效规则目录页未打开的列表条目不视为 118 号已核
# 【消歧】两所收费表与 137 号通知页及附件指引无结算费专行，不能替代中国结算结算费栏，也不得用经手表否定结算费栏。零改 EI
# 【消歧】硬分列：EN≠DV≠DW≠EM≠EI≠S≠U≠EL≠EJ≠EK≠EH≠EG≠AX≠V≠T≠DA≠DD≠DQ≠CZ≠DG≠CY≠DF≠DI≠DL≠DN≠EF≠EE≠ED≠EC≠EB≠O≠DO≠DB
# 【消歧】不改已冻 A–EM
# 【消歧】禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格；不另挂主报；零改 O；不改选 B2/B3
# 【消歧】诊断桶只作对照/旁路，不得升格进 en0_primary_demo；禁与 DV 行权过户、DW 权证/期权行权过户、EM 股票期权结算费、已只补的 B 股成交结算费或权证结算费键双挂
# 【消歧】把沪深合成一句、把 A 股与 B 股互抄、把系统申报档铺到手工行权、把 0.015‰ 与 0.5‰ / 0.02‰ / params.Y2 的 0.015 混读、发明为 0，只作同一误开的并列形态，不另挂第二主键
# params.Y2                               写死冻结 0.015（不是结算费千分比，不是面值档，不是切日；≠ 结算费 0.015‰）
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：现金选择权结算费腿成本差 ΔCashOptionSettlement / 净差异 / EN1−EN2；**params.Y/G/N ≠ 实验字母 EN ≠ 单字母 E ≠ 假设-EM ≠ 假设-DV**；**禁把占位读成千分比或面值档，也禁读成证管费 0.02‰、EG 过户 0.02‰、B 股成交结算费 0.02‰、股票过户 0.01‰、面值 0.5‰、结算费 0.015‰**）
# params.fill_time                        写死冻结 next_open
#   这是信号腿的成交时点建议，不是结算费切日，也不是表更新日
#   双字母 EN ≠ 单字母假设-E
# params.asof_check_date                  写死冻结 2026-11-11（本轮总管独立重抓日；不是切日，不是占位门槛；不是研究原稿或其它页可能出现的 2026-11-10；稿内 09:27:30–09:28:06 与风控再下 10:03:30–10:04:06 不得以时刻否决；日期同为 2026-11-11 且官方八件哈希须保持已核 MATCH）
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
#   缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip
#   切日未钉的历史费率变更 skip，不发明切日
#   沪市结算费栏无专行则该腿费率细节 skip
#   不得收成一句，也不得发明为 0，也不得把手工行权不收取发明成全部为 0
# params.cash_option_settlement_fee_honest 写死冻结 szse_ashare_cash_option_0p015_unidirectional_bshare_system_declared_0p015_unidirectional_manual_exercise_exempt_sse_no_dedicated_row_skip
#   诚实锚方向（已写死冻结）：
#   深市「A 股现金选择权」按清算金额的 0.015‰向结算参与人单向收取
#   深市「B 股现金选择权」通过交易系统申报的按行权清算金额的 0.015‰向结算参与人单向收取
#   手工行权不收取
#   沪市结算费栏无对应专行，该腿费率细节 skip
#   不得写成与深市同档，也不得发明为 0
#   收费对象是结算参与人，不得因此把投资者侧发明为 0
#   键值禁止写成 hs_blend / both_same / 沪深均为
# params.cash_option_settlement_fee_scope 写死冻结 cash_option_csdc_settlement_fee_only
#   只覆盖现金选择权在中国结算结算费栏已写下的费率
#   行权过户、B 股二级成交结算费、权证结算费、股票期权结算费、专项资产管理计划结算费、发行人侧派发登记费不进本页范围
#   行权过户交 DV；零改 DV
#   权证/期权行权过户交 DW；零改 DW
#   股票期权结算费交 EM；零改 EM
#   股票期权经手交 EI；零改 EI
#   A 股经手费交 S；零改 S
#   股票过户交 U；零改 U
#   B 股二级成交结算费只补事实
#   权证结算费与权证经手只补事实
#   专项资产管理计划结算费只补事实
# params.cash_option_settlement_fee_over_policy 写死冻结 skip_if_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_missing
#   缺 venue / A 股或 B 股标志 / 是否通过交易系统申报（B 股）/ 清算金额则 skip
#   禁止沪深合成、A 股与 B 股互抄、把系统申报档铺到手工行权
#   禁止把 0.015‰ 读成过户 0.5‰ 或 B 股成交结算 0.02‰ 或 params.Y2 的 0.015
#   禁止把经手费或行权过户当成结算费
#   禁止因结算参与人就把投资者侧发明为 0
#   禁止把手工行权不收取发明成全部为 0
#   禁止把已只补项或 DV 诊断桶升格进主键
#   表更新日不是切日
# params.cash_option_transfer_handoff     写死 dv_page
#   现金选择权行权过户交 DV；EN ≠ DV；零改 DV；不重开假设-DV；不改 DV
#   诊断桶 vs_DV_cash_option_transfer 不得升格进 en0_primary_demo
#   0.5‰ 与 1‰ 不得当成结算费
#   merge_with_DV=False
# params.warrant_option_exercise_transfer_handoff 写死 dw_page
#   权证/股票期权行权过户交 DW；EN ≠ DW；零改 DW；不重开假设-DW；不改 DW
#   merge_with_DW=False
# params.option_settlement_handoff        写死 em_page
#   股票期权按张结算费交 EM；键名是 handoff，不是本页锚前缀 option_settlement_fee_*
#   EN ≠ EM；零改 EM；不重开假设-EM；不改 EM
#   merge_with_EM=False
# params.option_handling_handoff          写死 ei_page
#   股票期权交易经手交 EI；EN ≠ EI；零改 EI；不重开假设-EI；不改 EI
#   merge_with_EI=False
# params.ashare_handling_handoff          写死 s_page
#   A 股经手费交 S；EN ≠ S；零改 S；不重开假设-S；不改 S
#   merge_with_S=False
# params.transfer_fee_handoff             写死 u_page
#   股票过户交 U；EN ≠ U；零改 U；不重开假设-U；不改 U
#   params.G 的 0.01 ≠ 股票过户 0.01‰
#   merge_with_U=False
# params.fund_handling_handoff            写死 ax_page
#   场内基金经手费交 AX；零改 AX；不重开假设-AX；不改 AX
#   merge_with_AX=False
# params.pref_handling_handoff            写死 eh_page
#   优先股经手费交 EH；零改 EH；不重开假设-EH；不改 EH
#   merge_with_EH=False
# params.cdr_transfer_handoff             写死 eg_page
#   存托凭证结算过户交 EG；EN ≠ EG；零改 EG；不改 EG
#   params.Y 的 0.02 ≠ EG 过户 0.02‰
#   merge_with_EG=False
# params.agreed_repurchase_handling_handoff 写死 ej_page
#   约定购回经手交 EJ；EN ≠ EJ；零改 EJ；不重开假设-EJ；不改 EJ
#   merge_with_EJ=False
# params.agreed_repurchase_transfer_handoff 写死 el_page
#   约定购回结算过户交 EL；EN ≠ EL；零改 EL；不重开假设-EL；不改 EL
#   merge_with_EL=False
# params.bond_cash_abs_handling_handoff   写死 ek_page
#   债券现券及资产支持证券经手交 EK；EN ≠ EK；零改 EK；不重开假设-EK；不改 EK
#   深市债券结算费 0.0004‰ 不进本页主键
#   merge_with_EK=False
# params.stamp_handoff                    写死 v_page
#   印花税交 V；零改 V；不重开假设-V；不改 V
#   merge_with_V=False
# params.csrc_fee_handoff                 写死 t_page
#   证管费交 T；不重开假设-T；params.Y 的 0.02 ≠ 证管费 0.02‰；不改 T
#   merge_with_T=False
# params.bshare_settlement_handoff        写死 facts_only
#   B 股二级成交结算费只补事实，不另立第二专页，不升格进 en0_primary_demo
#   0.02‰ ≠ 0.015‰
# params.warrant_settlement_handoff       写死 facts_only
#   权证交易/行权结算费只补事实，不另立第二专页；同是 0.015‰ 不得抄到现金选择权
#   权证交易为双向、权证行权为向行权方单向
# params.warrant_handling_handoff         写死 facts_only
#   权证经手只补事实；深市 0.045‰双边；不得写成「沪深均为 0.045‰」；不得发明沪市为 0；≠ DW
# params.am_plan_settlement_handoff       写死 facts_only
#   沪市专项资产管理计划结算费只补事实；深市无此专行；不得与现金选择权或权证结算费合成一句
# params.stock_block_handling_handoff     写死 di_page
#   股票大宗经手下浮交 DI；零改 DI；不改 DI
# params.block_fee_handoff                写死 di_page
#   与 EM 草稿同模板的大宗下浮 handoff，同样指向 DI，merge_with_DI=False，不升格
# params.fund_transfer_handoff            写死 da_page
#   场内基金二级过户交 DA；零改 DA；不改 DA
# params.etf_basket_transfer_handoff      写死 dq_page
#   ETF 篮子过户交 DQ；零改 DQ；不改 DQ
# params.etf_basket_handoff               写死 dq_page
#   与 EM 草稿同模板的篮子过户 handoff，同样指向 DQ，不升格
# params.cbond_transfer_handoff           写死 dd_page
#   转债过户交 DD；零改 DD；不改 DD
# params.cbond_handling_handoff           写死 db_page
#   转债现货经手费交 DB；零改 DB；不改 DB
#   118 号是可转债经手费通知，本选题不依赖；零改 DB
# params.bse_handling_handoff             写死 dg_page
#   北交所经手费交 DG；零改 DG；不改 DG
# params.exchangeable_handling_handoff    写死 df_page
#   可交换现货经手费交 DF；零改 DF；不改 DF
# params.cbond_put_handling_handoff       写死 do_page
#   可转债回售经手交 DO；零改 DO；不改 DO
# params.protocol_block_transfer_handoff  写死 dl_page
#   综合协议过户下浮交 DL；零改 DL；不重开假设-DL；不改 DL
# params.exchangeable_conversion_transfer_handoff 写死 dn_page
#   可交换换股过户交 DN；零改 DN；不改 DN
# params.agreed_repurchase_handoff        写死 ej_page
#   与 EM 草稿同模板的约定购回 handoff，同样指向 EJ，不升格；本页指定键名仍是 agreed_repurchase_handling_handoff
# params.exchangeable_conversion_handling_handoff 写死 dm_page
#   可交换换股经手费交 DM；与换股过户 handoff（DN）分列，不升格
# params.cdr_tradability_handoff          写死 cz_page
#   CDR 可成交性交 CZ；零改 CZ；不改 CZ
# params.pref_tradability_handoff         写死 cy_page
#   优先股可成交性交 CY；零改 CY；不改 CY
# params.periodic_report_visibility_handoff 写死 ed_page
#   正式年报/中报可见日交 ED；零改 ED；不改 ED
# params.earnings_preview_flash_handoff   写死 ee_page
#   业绩预告/快报可见日交 EE；零改 EE；不改 EE
# params.survivorship_handoff             写死 c_page
#   股票池/指数当时名单交 C；不改 C
# params.halt_bar_handoff                 写死 d_page
#   次日开/收与停牌日假成交交 D；不改 D
# params.sh_main_block_accept_handoff     写死 ec_page
#   沪市主板大宗接受闸门交 EC；零改 EC；不改 EC
# params.nolimit_nego_px_handoff          写死 eb_page
#   无板协议大宗价限交 EB；零改 EB；不改 EB
# params.star_fixed_price_type_handoff    写死 ea_page
#   科创大宗固定价格类型开关交 EA；不改 EA
# params.chinext_confirm_handoff          写死 dz_page
#   创业板确认钟交 DZ；不改 DZ
# params.approval_ipo_band_handoff        写死 dy_page
#   核准制首日申报带交 DY；不改 DY
# params.sse_fund_close_handoff           写死 dx_page
#   沪市基金收盘产生交 DX；不改 DX
# params.block_liquidity_handoff          写死 o_page
#   日量含大宗 / 三通道交 O；零改 O；不改 O
#   B2 场内基金大宗门槛不另挂主报，不改 O，不改选 B2
# params.aft_channel_handoff              写死 m_page
#   盘后固定价格通道交 M；不改 M
# params.aft_fill_handoff                 写死 ch_page
#   盘后可成交性交 CH；不改 CH
# params.block_fill_handoff               写死 ck_page
#   协议大宗可成交性交 CK；不改 CK
# params.lot_size_handoff                 写死 e_page
#   整手与科创板 200 股交 E；双字母 EN ≠ 单字母假设-E；不改 E
# params.ex_right_limit_handoff           写死 w_page
#   除权判板交 W；不改 W
# params.etf_t0_handoff                   写死 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 en0_primary_demo；不改 R
# params.en0_primary_demo                 写死冻结 invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend
#   单一主报，单挂写死；三条已冻
#   不要只写裸 en0=
#   禁与 DV 行权过户、DW 权证/期权行权过户、EM 股票期权结算费、已只补的 B 股成交结算费或权证结算费键双挂
#   诊断桶不升格
#   EN1 不升格并列主报
#   把沪深合成一句、把 A 股与 B 股互抄、把系统申报档铺到手工行权、把 0.015‰ 与 0.5‰ / 0.02‰ / params.Y2 的 0.015 混读、发明为 0，都在这一个主键里
#   上述只作同一误开的并列形态，不另挂第二主键
#   禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格
#   不另挂主报；零改 O；零改 DV；零改 DW；零改 EM
#   诊断桶 use_dv_face_permille_as_settlement / use_bshare_trade_settlement_as_cash_option / copy_warrant_015_onto_cash_option / copy_am_plan_015_onto_cash_option / merge_sh_sz_cash_option_settlement_sentence / blend_ashare_and_bshare_cash_option / spread_system_declared_fee_to_manual_exercise / invent_investor_zero_from_participant / misread_params_y2_as_permille / invent_all_zero_from_manual_exempt / invent_sse_zero_or_same_tier / bundle_transfer_or_handling_as_settlement / invent_cash_option_settlement_cut_date / vs_DV_cash_option_transfer / vs_DW_warrant_option_exercise_transfer / vs_EM_option_settlement / vs_EI_option_handling / vs_S_ashare_handling / vs_U_transfer / vs_EL_agreed_repurchase_transfer / vs_EJ_agreed_repurchase_handling / vs_EK_bond_cash_abs_handling / vs_AX_fund_handling / vs_EH_pref_handling / vs_EG_cdr_transfer / vs_V_stamp / vs_T_csrc / vs_O_block_liquidity / vs_R_etf_t0 / vs_E_lot_size / vs_B2_fund_block_threshold / vs_B3_deferred_vwap_window / missing_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_not_skip 不得升格进 en0_primary_demo
#   尤重：实验 R 不抢
#   尤重：不重开假设-V / T / U / S / AX / DI / DB / DF / DO / DW / EH / EI / EJ / EK / EL / EM / DL / DV
#   尤重：零改 U；零改 DA；零改 DD；零改 DQ；零改 CZ；零改 V；零改 S；零改 AX；零改 DG；零改 CY；零改 T；零改 DF；零改 DI；零改 DW；零改 DL；零改 DN；零改 DV；零改 EH；零改 EG；零改 EF；零改 EE；零改 ED；零改 EC；零改 EB；零改 EI；零改 EJ；零改 EK；零改 EL；零改 EM；零改 O；零改 DO；零改 DB
#   尤重：双字母 EN ≠ 单字母 E；亦 ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB
# params.en0_invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend 建议 True
# params.en1_unit_blend_or_transfer_as_settlement_diag_only 建议 True
#   把 0.015‰ 读成 0.5‰ / 0.02‰ / params.Y2 的 0.015、发明切日、把两所合成一句、把手工行权不收取发明成全部为 0、用经手表替代结算费栏，都只作诊断对照
#   EN1 不升格并列主报
#   不得把上述键写进 en0_primary_demo，不得双挂
# params.en2_sse_szse_ab_share_listed_separately 建议 True
# params.use_dv_face_permille_as_settlement 建议 False
#   禁止按行权过户面值 0.5‰ 或沪市非交易过户 1‰ 计结算费
# params.use_bshare_trade_settlement_as_cash_option 建议 False
#   禁止按 B 股二级成交结算费 0.02‰ 计现金选择权结算费
# params.copy_warrant_015_onto_cash_option 建议 False
#   禁止因同是 0.015‰ 抄权证交易/行权结算费
# params.copy_am_plan_015_onto_cash_option 建议 False
#   禁止把沪市专项资产管理计划双向 0.015‰ 抄到现金选择权
# params.merge_sh_sz_cash_option_settlement_sentence 建议 False
#   禁止写成「沪深均为 0.015‰」
# params.blend_ashare_and_bshare_cash_option 建议 False
#   禁止把深市 A 股与 B 股两档合成一句
# params.spread_system_declared_fee_to_manual_exercise 建议 False
#   禁止把系统申报档铺到手工行权
# params.invent_investor_zero_from_participant 建议 False
#   禁止因收费对象是结算参与人就把投资者侧发明为 0
# params.misread_params_y2_as_permille    建议 False
#   禁止把 params.Y2 的 0.015 读成 0.015‰
# params.invent_all_zero_from_manual_exempt 建议 False
#   禁止把手工行权不收取发明成全部为 0 或永久 0
# params.invent_sse_zero_or_same_tier     建议 False
#   禁止因表上没有就把沪市发明为 0 或与深市同档
# params.bundle_transfer_or_handling_as_settlement 建议 False
#   禁止把行权过户或经手费当成结算费
# params.invent_cash_option_settlement_cut_date 建议 False
#   禁止发明切日；2026年1月、2026-01-01、未打开的 118 号都不是首次生效日
# params.replace_csdc_settlement_with_exchange_handling_table 建议 False
#   禁止用两所收费表或 137 号指引否定或替代中国结算结算费栏
# params.merge_with_S                     写死 False
# params.merge_with_AX                    写死 False
# params.merge_with_DB                    写死 False
# params.merge_with_DO                    写死 False
# params.merge_with_DF                    写死 False
# params.merge_with_DI                    写死 False
# params.merge_with_EJ                    写死 False
# params.merge_with_EI                    写死 False
# params.merge_with_EH                    写死 False
# params.merge_with_EG                    写死 False
# params.merge_with_DQ                    写死 False
# params.merge_with_DW                    写死 False
# params.merge_with_U                     写死 False
# params.merge_with_V                     写死 False
# params.merge_with_T                     写死 False
# params.merge_with_DG                    写死 False
# params.merge_with_CY                    写死 False
# params.merge_with_O                     写死 False
# params.merge_with_E                     写死 False
# params.merge_with_DL                    写死 False
# params.merge_with_DN                    写死 False
# params.merge_with_DV                    写死 False
# params.merge_with_DD                    写死 False
# params.merge_with_DA                    写死 False
# params.merge_with_EK                    写死 False
# params.merge_with_EL                    写死 False
# params.merge_with_EM                    写死 False
# params.merge_with_EF                    写死 False
# params.merge_with_EE                    写死 False
# params.merge_with_ED                    写死 False
# params.merge_with_EC                    写死 False
# params.merge_with_EB                    写死 False
# params.merge_with_EA                    写死 False
# params.merge_with_CZ                    写死 False
# params.merge_with_DM                    写死 False
# params.merge_with_DZ                    写死 False
# params.merge_with_DY                    写死 False
# params.merge_with_DX                    写死 False
# params.merge_with_DU                    写死 False
# params.merge_with_DT                    写死 False
# params.merge_with_DS                    写死 False
# params.merge_with_DR                    写死 False
# params.merge_with_DP                    写死 False
# params.merge_with_DK                    写死 False
# params.merge_with_DJ                    写死 False
# params.merge_with_DH                    写死 False
# params.merge_with_DE                    写死 False
# params.merge_with_DC                    写死 False
# params.merge_with_AC                    写死 False
# params.merge_with_Q                     写死 False
# params.merge_with_R                     写死 False
# params.merge_with_M                     写死 False
# params.merge_with_CH                    写死 False
# params.merge_with_CL                    写死 False
# params.merge_with_CR                    写死 False
# params.merge_with_CQ                    写死 False
# params.merge_with_F                     写死 False
# params.merge_with_J                     写死 False
# params.merge_with_W                     写死 False
# params.merge_with_AW                    写死 False
# params.merge_with_AY                    写死 False
# params.merge_with_X                     写死 False
# params.merge_with_G                     写死 False
# params.merge_with_CI                    写死 False
# params.merge_with_CK                    写死 False
# params.merge_with_Y                     写死 False
# params.merge_with_A                     写死 False
# params.merge_with_D                     写死 False
# params.merge_with_Z                     写死 False
# params.merge_with_B                     写死 False
# params.merge_with_C                     写死 False
# params.missing_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_policy 建议 skip
# params.day_freq_proxy                   建议 cash_option_settlement_fee_sensitivity
# params.universe_rule                    建议 cash_option_settlement_fee_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_en_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 EN；勿读成单字母 E，亦勿读成假设-EM，亦勿读成假设-DV
#   不另挂主报，不预留 #150，不写下一字母
```

### 2.2 三组对照（EN0 / EN1 / EN2）

组名 EN0 / EN1 / EN2 是本页三组，≠ 单字母实验 E（整手与科创板 200 股），亦 ≠ 双字母实验 EM（股票期权结算费），亦 ≠ 双字母实验 DV（现金选择权行权过户），亦 ≠ 双字母实验 EI / EL / EK / EJ / EH / EG / EF / EE / ED。**双字母 EN ≠ 单字母假设-E**。**双字母 EN ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB**。**params.Y/G/N ≠ 实验字母 EN ≠ 单字母 E ≠ 假设-EM ≠ 假设-DV**。**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰**。**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰**。**尤重 params.N 的 0.05 ≠ 面值 0.5‰**。**尤重 params.Y2 的 0.015 ≠ 结算费 0.015‰**。**尤重须沪深分列**。**尤重 0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰**。三条已冻。

| 组 | 角色 | 口径 |
|----|------|------|
| EN0 | 天真 / 按过户、成交结算、权证或沪深合成 | 按 `en0_primary_demo` **写死冻结**单一主报 `invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend`（单挂写死）：现金选择权结算费按 DV 行权过户面值 0.5‰ 计，或按 B 股二级成交结算费 0.02‰ 计，或因同是 0.015‰ 抄权证，或收成「沪深均为 0.015‰」，或把深市 A 股与 B 股合成一句，或把系统申报档铺到手工行权。发明为 0、把 params.Y2 的 0.015 读成 0.015‰、把手工行权不收取发明成全部为 0，是同一误开的并列形态，不另挂第二主键。**禁**与 DV / DW / EM 键双挂，也禁与已只补的 B 股成交结算费或权证结算费键双挂。**禁把诊断桶、B2、B3 合成进 `en0_primary_demo`** |
| EN1 | 诊断对照（不升格） | 把 0.015‰ 与 0.5‰ / 0.02‰ / 0.0004‰ / 1‰ / params.Y2 的 0.015 混读、发明切日（含把 2026年1月、2026-01-01 或未打开的 118 号当成切日）、用两所收费表或 137 号指引替代中国结算结算费栏，以及相对 DV/DW/EM/EI/S/U 等的对照。**只进诊断、不得升格并列主报**，不得写进 `en0_primary_demo`，不得双挂。**EN1 不升格并列主报** |
| EN2 | 诚实 / 沪深及 A/B 股分列，缺了就 skip | `cash_option_settlement_fee_honest=szse_ashare_cash_option_0p015_unidirectional_bshare_system_declared_0p015_unidirectional_manual_exercise_exempt_sse_no_dedicated_row_skip`（写死冻结）：深市 A 股现金选择权按清算金额的 0.015‰向结算参与人单向收取；深市 B 股通过交易系统申报的按行权清算金额的 0.015‰向结算参与人单向收取，手工行权不收取；沪市结算费栏无专行，该腿 skip。收费对象是结算参与人，不得因此把投资者侧发明为 0。缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip；切日未钉的历史费率变更 skip，不发明切日。不得收成一句，不得发明为 0。行权过户只消费 DV，股票期权结算费只消费 EM，股票期权经手只消费 EI，或显式旁路 |

把单位写错、发明切日、两所合成一句、A 股与 B 股互抄、系统申报铺到手工行权、永久 0、经手表替代结算费栏、B2、B3，以及相对 DV/DW/EM/EI/S/U/V/T/O/R/E 的对照，放进 §4.1 分桶，**只作诊断桶或旁路，不得升格为第二个主报**。`vs_B2_fund_block_threshold` 只标记场内基金大宗门槛。`vs_B3_deferred_vwap_window` 只标记 16:00-17:00 / VWAP **暂缓**窗。这两条**禁升格、不另挂主报、零改 O**。`vs_DV_cash_option_transfer` 不得升格进主键。其余 `vs_*` 与 `missing_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_not_skip` 同样**不得升格进 `en0_primary_demo`**。

### 2.3 费率可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-11-11`（本轮总管独立重抓日；不是切日；中国结算深市表重抓窗为 2026-11-11 09:27:30–09:28:06 Asia/Shanghai；稿内 09:27:30–09:28:06 与风控再下 10:03:30–10:04:06 不得以时刻否决；日期同为 2026-11-11 且官方八件哈希须保持已核 MATCH；不要写成短要点里较早的 09:18 窗口，也不要写成研究原稿或其它页可能出现的 2026-11-10 / 2026-09-28 / 2026-10-23 / 2026-01-01 / 2026年1月）；fill_time **写死冻结** `next_open`（信号腿时点，不是结算费切日）；fail **写死冻结** `skip`（缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip；切日未钉则 skip，不发明切日）。诚实锚六键与 Y/G/N/Y2、`en0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：现金选择权结算费须沪深分列，并须 A 股 / B 股分列——深市 A 股按清算金额 0.015‰向结算参与人单向收取；深市 B 股系统申报按行权清算金额 0.015‰向结算参与人单向收取，手工行权不收取；沪市结算费栏无专行则该腿 skip。不得把系统申报档铺到手工行权，也不得把手工行权不收取发明成全部为 0。缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额，或缺切日的历史费率变更，则 skip。`params.Y` 的 0.02 不是证管费 0.02‰，也不是 EG 过户 0.02‰，也不是 B 股成交结算费 0.02‰，也不是实验字母 EN；`params.G` 的 0.01 不是股票过户 0.01‰；`params.N` 的 0.05 不是面值 0.5‰；`params.Y2` 的 0.015 不是结算费 0.015‰；四个占位也不是 2026-11-11，也不是 2026-01-01。**禁把占位读成千分比或面值档**。本页**不开回测**；不拉真数；不做实盘；不开户。真数仍停。费用层，不是行权过户，也不是 B 股二级成交结算费。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `en0_primary_demo` / `params.Y`·G·N·Y2 / 费率开关 / 桶 / 是否把发明切日或单位误写或两所合成句或 A/B 股互抄或经手表替代结算费栏或 B2/B3 或成交规则页倒灌进主报、或与诊断键双挂、或把占位读成千分比或面值档）。本页不开跑。禁 null。三条已冻。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（EN0）/ 诊断对照组（EN1）相对诚实组（EN2）的现金选择权结算费腿成本差**显著且集中在按行权过户 0.5‰ 计、或按 B 股二级成交结算费 0.02‰ 计、或抄权证 0.015‰、或收成「沪深均为 0.015‰」、或 A 股与 B 股合成一句、或把系统申报档铺到手工行权、或发明为 0**的桶；分桶「占位读成费率 / 发明切日 / 经手表替代结算费栏 / vs DV·DW·EM·EI / B2 / B3」不改变主结论方向。成功不依赖把占位读成 0.015‰ 或 0.5‰，也不把 `params.Y` 读成实验字母 EN，也不把 2026年1月读成首次生效日。按过户计的方向是把清算金额结算费换成面值；发明 0 的方向是漏掉深市表上已写下的结算费；把系统申报档铺到手工行权的方向是把原文不收取的腿收成 0.015‰。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 DV 的行权过户、DW 的权证/期权行权过户、EM 的股票期权结算费、EI 的股票期权经手、S 的 A 股经手、U 的股票过户、V 的印花税、T 的证管费、O 的大宗通道、R 的假 T+0、A 的板上容量解释；或 `en0_primary_demo` 与 DV / DW / EM 键双挂；或 EN1 升格并列主报；或诊断桶升格主报；或 B2/B3 另挂主报；或把 2026年1月 / 2026-01-01 / 未打开的 118 号写成切日并升格；或把诚实锚收成一句；或把 0.015‰ 写成 params.Y2 的 0.015；或把手工行权不收取写成全部为 0 并另挂第二主键；或把行权过户写进结算费主键；或实验字母 EN 与单字母 E、假设-EM、假设-DV 或 params.Y/G/N 混读；或把占位读成证管费 0.02‰、EG 过户 0.02‰、B 股成交结算费 0.02‰、股票过户 0.01‰、面值 0.5‰或结算费 0.015‰；或缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）、清算金额或切日仍不 skip；或重开假设-R / 假设-V / 假设-T / 假设-U / 假设-S / 假设-AX / 假设-DI / 假设-DB / 假设-DF / 假设-DO / 假设-DW / 假设-EH / 假设-EI / 假设-EJ / 假设-EK / 假设-EL / 假设-EM / 假设-DL / 假设-DV / 假设-O；或改 U / DA / DD / DQ / CZ / V / S / AX / DG / CY / T / DF / DI / DW / DL / DN / DV / EH / EG / EF / EE / ED / EC / EB / EI / EJ / EK / EL / EM / O / DO / DB 正文/预检/复检；或标纸面齐；或写成 A/D–EN纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 EN0/EN1/EN2。行权过户走 DV，权证/期权行权过户走 DW，股票期权结算费走 EM，股票期权经手走 EI，A 股经手走 S，股票过户走 U，印花走 V，证管走 T，都不改。成本差：现金选择权行权上，天真档相对诚实档少计或多计的中国结算结算费。不把 2026年1月、2026-01-01 或 2026-11-11 标成占位门槛。本页不开回测。真数仍停。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend` / `use_dv_face_permille_as_settlement` / `use_bshare_trade_settlement_as_cash_option` / `copy_warrant_015_onto_cash_option` / `copy_am_plan_015_onto_cash_option` / `merge_sh_sz_cash_option_settlement_sentence` / `blend_ashare_and_bshare_cash_option` / `spread_system_declared_fee_to_manual_exercise` / `invent_investor_zero_from_participant` / `misread_params_y2_as_permille` / `invent_all_zero_from_manual_exempt` / `invent_sse_zero_or_same_tier` / `bundle_transfer_or_handling_as_settlement` / `invent_cash_option_settlement_cut_date` / `vs_DV_cash_option_transfer` / `vs_DW_warrant_option_exercise_transfer` / `vs_EM_option_settlement` / `vs_EI_option_handling` / `vs_S_ashare_handling` / `vs_U_transfer` / `vs_EL_agreed_repurchase_transfer` / `vs_EJ_agreed_repurchase_handling` / `vs_EK_bond_cash_abs_handling` / `vs_AX_fund_handling` / `vs_EH_pref_handling` / `vs_EG_cdr_transfer` / `vs_V_stamp` / `vs_T_csrc` / `vs_O_block_liquidity` / `vs_R_etf_t0` / `vs_E_lot_size` / `vs_B2_fund_block_threshold` / `vs_B3_deferred_vwap_window` / `missing_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_not_skip`

`invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend` 才是写死冻结的单一主报名（单挂写死）。自 `use_dv_face_permille_as_settlement` 起至 `missing_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_not_skip` **只作诊断桶**：它们不是 `en0_primary_demo`，也不是并列主报，**不得升格主报，不得双挂**。沪深合成、A 股与 B 股互抄、系统申报铺到手工行权、把 0.015‰ 与 0.5‰ / 0.02‰ / params.Y2 的 0.015 混读、发明为 0，只作同一误开的并列形态，不另挂第二主键。`vs_B2_fund_block_threshold` 与 `vs_B3_deferred_vwap_window` **禁升格、不另挂主报**。B3 那道 16:00-17:00 / VWAP 窗仍是**暂缓**，不要写成现行可成交，也不要改选成本页。**零改 O**。**零改 DV**。**零改 DW**。**零改 EM**。**零改 EI**。**实验 R 不抢**。**不重开假设-V / T / U / S / AX / DI / DB / DF / DO / DW / EH / EI / EJ / EK / EL / EM / DL / DV**。没有「沪深均为 0.015‰」合成主报，也没有「过户 + 结算费」合成主报，也没有「0.02‰ 即现金选择权结算费」合成主报。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「行权过户面值 0.5‰」或「沪深均为 0.015‰」或「B 股二级成交结算费 0.02‰」或「发明为 0」或「2026年1月 / 2026-01-01 / 未打开的 118 号当切日」拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成证管费 0.02‰，或当成 EG 过户 0.02‰，或当成 B 股成交结算费 0.02‰，或当成实验字母 EN，或当成单字母 E，或当成假设-EM，或当成假设-DV，或当成核对日。**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰**。**尤重 params.Y/G/N ≠ 实验字母 EN / 单字母 E / 假设-EM / 假设-DV**。
- 把 `params.G` 的 0.01 当成股票过户 0.01‰，或当成假设-G。**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰**。
- 把 `params.N` 的 0.05 当成面值 0.5‰，或当成实验字母 EN，或当成单字母 E。**尤重 params.N 的 0.05 ≠ 面值 0.5‰**。
- 把 `params.Y2` 的 0.015 当成结算费 0.015‰。**尤重 params.Y2 的 0.015 ≠ 结算费 0.015‰**。
- 把 0.015‰ 与 0.02‰、0.5‰、0.0004‰、1‰ 混读。**尤重 0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰**。
- 把占位 `0.02/0.01/0.05/0.015` 读成千分比或面值档。
- 缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额仍不 skip。诊断桶 `missing_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_not_skip` 只作对照，不得升格。
- 缺切日仍发明切日，或把表「更新」日、或未打开的上证发〔2022〕118 号细节写成现金选择权结算费切日。诊断桶 `invent_cash_option_settlement_cut_date` 只作对照。**禁与 `en0_primary_demo` 双挂**。118 号是可转债经手费通知，本选题不依赖，零改 DB。废止句以 137 号通知页为准（自 2023年8月28日起废止）。失效规则目录页有同标题同日列表路径，本轮未打开该条目页，不视为 118 号已核。
- 把沪市原文和深市原文收成一句写死。诊断桶 `merge_sh_sz_cash_option_settlement_sentence` 只作对照。不得写成「沪深均为 0.015‰」。须沪深分列。
- 把深市 A 股与 B 股互抄。诊断桶 `blend_ashare_and_bshare_cash_option` 只作对照。
- 把系统申报档铺到手工行权。诊断桶 `spread_system_declared_fee_to_manual_exercise` 只作对照。
- 因收费对象是结算参与人就把投资者侧发明为 0。诊断桶 `invent_investor_zero_from_participant` 只作对照。
- 把手工行权不收取写成全部为 0 或永久 0。诊断桶 `invent_all_zero_from_manual_exempt` 只作对照。手工行权不收取只覆盖「不通过交易系统申报的手工行权业务」。
- 因表上没有就把沪市发明为 0 或与深市同档。诊断桶 `invent_sse_zero_or_same_tier` 只作对照。沪市该腿 skip。不写成已核无费。
- 因同是 0.015‰ 抄权证或沪市专项资产管理计划。诊断桶 `copy_warrant_015_onto_cash_option` / `copy_am_plan_015_onto_cash_option` 只作对照。权证交易为双向、权证行权为向行权方单向；专项资产管理计划为双向。
- 把行权过户或经手费捆进主键。诊断桶 `bundle_transfer_or_handling_as_settlement` 只作对照。**零改 DV**。**零改 EI**。**零改 EM**。
- 用两所收费表或 137 号指引否定或替代中国结算结算费栏。指引规范的是交易所经手等项目，全文无「结算费」。零改 EI。
- 把假设-DV 的行权过户和本页合成后升格。**零改 DV**。**不重开假设-DV**。
- 把假设-DW 的行权过户和本页合成后升格。**零改 DW**。**不重开假设-DW**。
- 把假设-EM 的股票期权结算费和本页合成后升格。**零改 EM**。**不重开假设-EM**。
- 把假设-EI 的股票期权经手和本页合成后升格。**零改 EI**。**不重开假设-EI**。
- 把假设-S 的 A 股经手和本页合成后升格。**零改 S**。**不重开假设-S**。
- 把假设-U 的股票过户和本页合成后升格。**零改 U**。**不重开假设-U**。
- 把假设-EL / EJ / EK / EH / EG / AX 的经手或过户页和本页合成后升格。**零改 EL**。**零改 EJ**。**零改 EK**。**零改 EH**。**零改 EG**。**零改 AX**。
- 把假设-V 的印花税、假设-T 的证管费和结算费合成后升格。**零改 V**。**零改 T**。
- 把假设-O 的成交规则和本页合成后升格，或改选 B2/B3。**零改 O**。B3 仍是**暂缓**。
- 把假设-E 的整手和本页合成后升格。**双字母 EN ≠ 单字母假设-E**。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格。**实验 R 不抢**。
- `en0_primary_demo` 与行权过户键、权证/期权行权过户键、股票期权结算费键、已只补的 B 股成交结算费键、权证结算费键或任一诊断键双挂；EN1 升格并列主报；发明为 0 另挂第二主键。
- 实验字母 EN 与单字母 E、假设-EM、假设-DV 或 params.Y/G/N 混读。**双字母 EN ≠ 单字母 E**。**双字母 EN ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB**。
- 改 U / DA / DD / DQ / CZ / V / S / AX / DG / CY / T / DF / DI / DW / DL / DN / DV / EH / EG / EF / EE / ED / EC / EB / EI / EJ / EK / EL / EM / EA / O / DO / DB 及其他已冻页正文；改 #110–#148；禁止标纸面齐；禁止写成 A/D–EN纸面齐；或预留 #150；开真数/回测/开户/实盘；用过户面值或 0 当现金选择权结算费；结论写成「这笔现金选择权该做」。
- **纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–EM；勿再只改清单）。当前禁止标纸面齐。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 证券代码、交易日、交易所（沪 / 深）、A 股或 B 股标志、是否通过交易系统申报（B 股）、清算金额。交易所、A 股或 B 股标志、B 股是否通过交易系统申报、或清算金额分不清则 skip。本页主报只钉现金选择权在中国结算结算费栏已写下的费率。
- **清算金额**：深市 A 股按清算金额，深市 B 股系统申报按行权清算金额。清算金额缺了则 skip，不填 0，也不用面值 0.5‰ 或成交结算 0.02‰ 去补。0.015‰ 是清算金额的费率，不是 params.Y2 的 0.015。
- **交易所与 A/B 股**：两所必须分列，A 股与 B 股必须分列。缺 venue 或 A/B 标志则 skip，不许收成一句。沪市结算费栏无专行，该腿 skip，不得抄深市 0.015‰。
- **B 股申报方式**：通过交易系统申报的才按 0.015‰单向收取行权结算费。不通过交易系统申报的手工行权不收取。只看到一条，不要把另一条填成同一档，也不要把手工行权的「不收取」铺成全部为 0。
- **切日**：今天不钉现金选择权结算费表定费率的首次生效日。表「更新」2026年1月、封面「2026 年 1 月 1 日更新」都不是首次生效日。上证发〔2022〕118 号原件本轮未独立打开，废止句仍以 137 号通知页为准，不得把未核细节写成已核依据。该件是可转债经手费通知，本选题不依赖，零改 DB。失效规则目录页未打开的列表条目不视为 118 号已核。缺现行有效文本重述则 skip，不发明。深市现行表已写下的 0.015‰、以及 B 股手工行权不收取，可冻为现行诚实锚；三条已写死冻结。
- 旁路消费：DV 的行权过户、DW 的权证/期权行权过户、EM 的股票期权结算费、EI 的股票期权经手、S 的 A 股经手、U 的股票过户、EL 的约定购回过户、EJ 的约定购回经手、EK 的债券现券经手、AX 的基金经手、EH 的优先股经手、EG 的存托过户、V 的印花税、T 的证管费、O 的大宗通道、R 的假 T+0（见 §2.1 handoff）。**本页不改写这些页。零改 U。零改 DA。零改 DD。零改 DQ。零改 CZ。零改 V。零改 S。零改 AX。零改 DG。零改 CY。零改 T。零改 DF。零改 DI。零改 DW。零改 DL。零改 DN。零改 DV。零改 EH。零改 EG。零改 EF。零改 EE。零改 ED。零改 EC。零改 EB。零改 EI。零改 EJ。零改 EK。零改 EL。零改 EM。零改 O。零改 DO。零改 DB。** B2 与 B3 不进主报，不改选。B 股二级成交结算费不进主报。权证经手与权证结算费不进主报。专项资产管理计划结算费不进主报。发行人侧现金选择权派发登记费不进主报。
- 未复权路径；asof **写死冻结** `2026-11-11`（本轮总管独立重抓日；不是切日；不是研究原稿或其它页可能出现的 2026-11-10；稿内 09:27:30–09:28:06 与风控再下 10:03:30–10:04:06 不得以时刻否决；日期同为 2026-11-11 且官方八件哈希须保持已核 MATCH）。核对日只钉「结算费这一栏怎么写」，不钉「这档费率从哪一天首次开始」。权证、B 股二级成交结算费、专项资产管理计划、深市 B 股现金选择权行权过户、发行人侧派发登记费，都写在《事实与坑》2026-11-11 本轮条，只补事实，不进本页主键。

### 6.1 官方依据（沪深分列；不扩切日；现金选择权结算费以中国结算结算费栏为准）

工程已于 2026-11-11 按派单已核原件核对中国结算沪/深 PDF、两所官网收费页、上证发〔2023〕137 号通知页与附件指引、以及失效规则目录页。现金选择权结算费以中国结算沪/深表「结算参与人业务收费 / 结算费」栏为准。两所收费表与 137 号通知页及附件指引无「结算费」专行，也无现金选择权结算费专行，不能替代结算费栏，也不得用来否定结算费栏。下面分列写，不收成一句。深市 B 股原文在「不通过交」与「易系统」处换行、中间无 U+0020，剥行断后连写，不要另加空格。中国结算深市表重抓窗为 2026-11-11 09:27:30–09:28:06 Asia/Shanghai。不要写成短要点里较早的 09:18 窗口。

1. **深市中国结算原件**（单独一句，不得与沪市合成，A 股与 B 股也不得合成）：《深圳市场证券登记结算业务收费及代收税费一览表（2026 年 1 月 1 日更新）》，https://www.chinaclear.cn/zdjs/fbzyls/202512/a59388fbfa714c5fa546784891a42e30/files/深圳市场证券登记结算业务收费及代收税费一览表.pdf 。工程核 SHA256=`dff4a06ce20e180f4a85ddae138211dcf7dd3246fb84775453cfd21cbaec6573`（114722B；本轮总管 2026-11-11 09:27:30–09:28:06 Asia/Shanghai 重抓）。目录 UUID 为 `a59388fb…`，必须与沪市 `922adc26…` 分列完整直链。结算费栏「A 股现金选择权」原文：「按清算金额的 0.015‰向结算参与人单向收取。」「B 股现金选择权」剥行断后原文：「通过交易系统申报的行权业务，按照行权清算金额的 0.015‰向结算参与人单向收取行权结算费；不通过交易系统申报的手工行权业务，不收取行权结算费。」收费对象栏为结算参与人；不得因此把投资者侧发明为 0。手工行权不收取不得铺成全部为 0，也不得把系统申报档铺过去。同栏权证交易/行权结算费（按清算金额的 0.015‰，向结算参与人收取；权证交易为双向、权证行权为向行权方单向）不进本页主键。交易过户栏「A 股现金选择权行权」「B 股现金选择权行权」是过户层，零改 DV，不进主键。封面「2026 年 1 月 1 日更新」不是首次生效日。

2. **沪市中国结算原件**（单独一句，不与深市合并）：《上海市场证券登记结算业务收费及代收税费一览表（2026 年 1 月 1 日更新）》，https://www.chinaclear.cn/zdjs/fbzyls/202512/922adc26c2ff4865930c7fb77688bb8a/files/上海市场证券登记结算业务收费及代收税费一览表.pdf 。工程核 SHA256=`84a99e563cb8e84e264c88e3bea2df5f4ac50b1e95330417ec30e2b2566d862f`（139671B）。目录 UUID 为 `922adc26…`，必须与深市 `a59388fb…` 分列完整直链。结算费栏无「A 股现金选择权」「B 股现金选择权」专行。该腿费率细节 skip。禁止写成「沪深均为 0.015‰」，也不得因「表上没有」发明沪市为 0 或与深市同档。沪市现金选择权结算费若另有未打开专项通知，本轮未检索到，不写成已核无费。同栏可见「专项资产管理计划」原文「按清算金额的 0.015‰向结算参与人双向收取。」，深市结算费栏无此专行；只补事实，不进本页主键。非交易过户注：「2、要约收购及现金选择权的非交易过户费按股份过户面值的 1‰收取（双向收取）。」这是过户层，不是结算费，零改 DV。1‰ ≠ 0.015‰ ≠ 0.5‰。

3. **上交所收费页**（经手费对照，不是结算费依据）：《上海证券交易所收费一览表》，更新时间：2026年1月，https://www.sse.com.cn/services/tradingservice/charge/ssecharge/ 。工程核 SHA256=`a28de66ea31037ffa240a2212a8599a06f1f1513f4c4a424976f3a193ae1eb7a`（40445B）。同日条目页 https://www.sse.com.cn/services/tradingservice/charge/ssecharge/c/c_20251231_10803655.shtml ，工程核 SHA256=`af521f20b42a238fbd1b14f1e8793d9ecf1a5bb933d3daa88d26805762053bdd`（41076B）。两页均无「结算费」专行，也无现金选择权结算费专行。不得用经手表否定中国结算结算费栏。更新时间「2026年1月」不是现金选择权结算费的首次生效日。零改 EI。

4. **深交所收费页**（经手费对照，不是结算费依据）：《深交所收费及代收税费标准（2026年1月）》，https://www.szse.cn/marketServices/deal/payFees/ 。工程核 SHA256=`fbd7df3dfa07778b1318564563d22992f19d06bde415144fef248f27674f03c7`（90980B）。页内无结算费专行，亦无现金选择权结算费专行。不得用该页替代中国结算结算费栏。零改 EI。权证交易经手仍只补事实：深市官网已钉 0.045‰双边；不得写成「沪深均为 0.045‰」，不得发明沪市为 0。≠ DW。≠ 本页主键。

5. **现行有效指引**（只规范经手等项目，不是结算费依据）：上证发〔2023〕137 号通知页 https://www.sse.com.cn/lawandrules/sselawsrules2025/charge/c/c_20250610_10781461.shtml （34190B，SHA256=`4e0e6964e3688dce18a484ca9bbd3a5927633f17842524baf62b4d11bb159fe1`；发布 2023-08-18，施行 2023-08-28；文号括号为 U+3014/U+3015；时效性现行有效）写明上证发〔2022〕118 号自 2023年8月28日起废止。附件指引 docx https://www.sse.com.cn/lawandrules/sselawsrules2025/charge/c/10781461/files/6ead9e7d60e14272a19cd75b622dd2ef.docx （31017B，SHA256=`b42cb6ad16be71f59618e2150ec31af57e8cf8874bc83973934ca8237fd56e84`）全文无「结算费」，也无现金选择权结算费专行，不是结算费依据，零改 EI。118 号原件本轮未独立打开，不得把未核细节写成已核依据。该件是可转债经手费通知，本选题不依赖，零改 DB。

6. **失效规则目录页**（不视为 118 号已核）：https://www.sse.com.cn/lawandrules/sselawsrules2025/repeal/rules/ （139710B，SHA256=`f22747a4cbbe684ed3be4e85fcd044a0df3d743bb96d5e53a46bde3855b64d78`）。有同标题同日列表路径，本轮未打开该条目页，不视为 118 号已核。

未打开、不得写成已核依据：上证发〔2022〕118 号原件；深市 2019 年期权试点初期收费通知官方直链（零改 EI/EM）；沪市约定购回过户「超过 500 元的部分暂时免于收取」的首次生效通知（零改 EL）；债券现券/ABS 暂免窗或表定费率的 2022 年（或更早）原始通知（零改 EK）；债券通专表；转股/换股次日流通专项费率；港股通揭示书附件（不重开 CT）。上证发〔2015〕67 号本选题不依赖，零改 EH。沪市现金选择权结算费若另有未打开专项通知，本轮未检索到，不写成已核无费，只写结算费栏无专行则该腿 skip。

切日不要扩写。表「更新」2026年1月 / 「2026 年 1 月 1 日更新」不是现金选择权结算费表定费率的首次生效日。深市现行表已写下的 0.015‰ 结算费、以及 B 股手工行权不收取，可冻为现行诚实锚。缺切日则历史变更 skip，不发明。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`（信号腿时点，不是结算费切日）；`asof_check_date=2026-11-11`（本轮总管独立重抓日；不是切日；中国结算深市表重抓窗为 2026-11-11 09:27:30–09:28:06 Asia/Shanghai；稿内 09:27:30–09:28:06 与风控再下 10:03:30–10:04:06 不得以时刻否决；日期同为 2026-11-11 且官方八件哈希须保持已核 MATCH；不要写成短要点里较早的 09:18 窗口，也不要写成研究原稿或其它页可能出现的 2026-11-10 / 2026-01-01 / 2026年1月）；`fail_policy=skip`（缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip；切日未钉的历史费率变更 skip，不发明切日）；`cash_option_settlement_fee_honest=szse_ashare_cash_option_0p015_unidirectional_bshare_system_declared_0p015_unidirectional_manual_exercise_exempt_sse_no_dedicated_row_skip`；`cash_option_settlement_fee_scope=cash_option_csdc_settlement_fee_only`；`cash_option_settlement_fee_over_policy=skip_if_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_missing`；`en0_primary_demo=invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend`（**写死冻结**单一主报，单挂写死；不要只写裸 `en0=`；禁与 DV 行权过户、DW 权证/期权行权过户、EM 股票期权结算费、已只补的 B 股成交结算费或权证结算费键双挂；诊断桶不升格；EN1 不升格；把沪深合成一句、把 A 股与 B 股互抄、把系统申报档铺到手工行权、把 0.015‰ 与 0.5‰ / 0.02‰ / params.Y2 的 0.015 混读、发明为 0，只作同一误开的并列形态，不另挂第二主键；**不得把诚实锚写成「沪深均为」**；**须沪深分列**；**须 A 股 / B 股分列**；**须把 B 股系统申报与手工行权分列**；**禁把 B2 / B3 升格，不另挂主报**）；`cash_option_transfer_handoff=dv_page`；`warrant_option_exercise_transfer_handoff=dw_page`；`option_settlement_handoff=em_page`；`option_handling_handoff=ei_page`；`ashare_handling_handoff=s_page`；`transfer_fee_handoff=u_page`；`fund_handling_handoff=ax_page`；`pref_handling_handoff=eh_page`；`cdr_transfer_handoff=eg_page`；`agreed_repurchase_handling_handoff=ej_page`；`agreed_repurchase_transfer_handoff=el_page`；`bond_cash_abs_handling_handoff=ek_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`bshare_settlement_handoff=facts_only`；`warrant_settlement_handoff=facts_only`；`warrant_handling_handoff=facts_only`；`am_plan_settlement_handoff=facts_only`；并保留同模板旁路 `stock_block_handling_handoff=di_page`；`block_fee_handoff=di_page`；`fund_transfer_handoff=da_page`；`etf_basket_transfer_handoff=dq_page`；`etf_basket_handoff=dq_page`；`cbond_transfer_handoff=dd_page`；`cbond_handling_handoff=db_page`；`bse_handling_handoff=dg_page`；`exchangeable_handling_handoff=df_page`；`cbond_put_handling_handoff=do_page`；`protocol_block_transfer_handoff=dl_page`；`exchangeable_conversion_transfer_handoff=dn_page`；`agreed_repurchase_handoff=ej_page`；`exchangeable_conversion_handling_handoff=dm_page`；`cdr_tradability_handoff=cz_page`；`pref_tradability_handoff=cy_page`；`periodic_report_visibility_handoff=ed_page`；`earnings_preview_flash_handoff=ee_page`；`survivorship_handoff=c_page`；`halt_bar_handoff=d_page`；`sh_main_block_accept_handoff=ec_page`；`nolimit_nego_px_handoff=eb_page`；`star_fixed_price_type_handoff=ea_page`；`chinext_confirm_handoff=dz_page`；`approval_ipo_band_handoff=dy_page`；`sse_fund_close_handoff=dx_page`；`block_liquidity_handoff=o_page`；`aft_channel_handoff=m_page`；`aft_fill_handoff=ch_page`；`block_fill_handoff=ck_page`；`lot_size_handoff=e_page`；`ex_right_limit_handoff=w_page`；`etf_t0_handoff=r_page`；全部 `merge_with_*=False`；`merge_with_S/AX/DB/DO/DF/DI/EJ/EI/EH/EG/DQ/DW/U/V/T/DG/CY/O/E/DL/DN/DV/DD/DA/EK/EL/EM=False`；`merge_with_EM=False`；`merge_with_DV=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是证管费，不是过户费，不是经手费，不是结算费千分比，不是面值档，不是核对日，不是切日；**三条已冻**；**params.Y/G/N ≠ 实验字母 EN ≠ 单字母 E ≠ 假设-EM ≠ 假设-DV**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰**；**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰**；**尤重 params.N 的 0.05 ≠ 面值 0.5‰**；**尤重 params.Y2 的 0.015 ≠ 结算费 0.015‰**；**尤重 0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰**；**禁把占位读成千分比或面值档**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #150。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。真数仍停。本草稿基 tip=`5e0e4981`（A/D–EM纸面齐已合，已收讫，讫=U+8BAB，全长 `5e0e498165a3c0ff447a33e4f2fec6e6963e9e71`）；分支起点 HEAD=`e88b7463e31322289d76c45e7fb187e9c5e1a58f`；开工核 origin/main 仍停在该提交。三冻补丁基 tip=`50e23cb1` / `50e23cb133eb2c6990c604bf455d022daa5b4c15`；本补丁分支起点 HEAD=`1acf8cec` / `1acf8cec2d84c798a4ead8d0b47aa806b624955c`；开工核 origin/main 仍停在 starting_ref `1acf8cec2d84c798a4ead8d0b47aa806b624955c`，未比该基线更前。**不改已冻 A–EM**。**零改 U**。**零改 DA**。**零改 DD**。**零改 DQ**。**零改 CZ**。**零改 V**。**零改 S**。**零改 AX**。**零改 DG**。**零改 CY**。**零改 T**。**零改 DF**。**零改 DI**。**零改 DW**。**零改 DL**。**零改 DN**。**零改 DV**。**零改 EH**。**零改 EG**。**零改 EF**。**零改 EE**。**零改 ED**。**零改 EC**。**零改 EB**。**零改 EI**。**零改 EJ**。**零改 EK**。**零改 EL**。**零改 EM**。**零改 O**。**零改 DO**。**零改 DB**。**不改 #110–#148**。状态=**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–EN纸面齐**。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–EM；勿再只改清单）。
- 诚实锚：现金选择权结算费须沪深分列，并须 A 股 / B 股分列。深市现行结算费栏，「A 股现金选择权」按清算金额的 0.015‰向结算参与人单向收取；「B 股现金选择权」通过交易系统申报的按行权清算金额的 0.015‰向结算参与人单向收取，不通过交易系统申报的手工行权不收取。沪市结算费栏无对应专行，该腿费率细节 skip。收费对象是结算参与人，不得因此把投资者侧发明为 0。不得写成「沪深均为 0.015‰」。缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip。

---

## 8. 结论

（空；**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–EN纸面齐**。）

---

## 变更
| 日期 | 变更 |
|------|------|
## 风控预检补丁·冻结（三条已写死 · 2026-12-20）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设EN-20261111.md`（原样落入，不改结论；SHA256=`77504fa4dc4a69b69de70db75d1d2b527ceec6573e7403d3401b799fb6042237`；预检 2026-11-11；**结论：有条件通过**；tip基=`50e23cb1` / `50e23cb133eb2c6990c604bf455d022daa5b4c15`；本补丁分支起点 HEAD=`1acf8cec` / `1acf8cec2d84c798a4ead8d0b47aa806b624955c`）。按该稿条件 1–3 升格，不标纸面齐。开工核 origin/main 仍停在派单 starting_ref `1acf8cec2d84c798a4ead8d0b47aa806b624955c`，未比该基线更前，本页以该提交为基线。稿内 09:27:30–09:28:06 与风控再下 10:03:30–10:04:06 不得以时刻否决；日期同为 2026-11-11 且官方八件哈希须保持已核 MATCH。上证发〔2022〕118 号原件未独立打开，本冻不把它升成现金选择权结算费切日，也不拿它当切日（废止句以 137 号通知页为准，自 2023-08-28 起废止）。失效规则目录页的同标题同日列表路径不视为 118 号已核。切日未钉则 skip，不发明切日。表「更新」2026年1月 / 「2026 年 1 月 1 日更新」不是现金选择权结算费切日。口径用「收讫」（讫=U+8BAB）。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于现金选择权结算费腿成本差 ΔCashOptionSettlement、净差异、EN1−EN2 专项。**`params.Y` ≠ 实验字母 EN**；**`params.G` ≠ 实验字母 EN**；**`params.N` ≠ 实验字母 EN**；亦 ≠ 单字母假设-E；亦 ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-V / 假设-T / 假设-U / 假设-S / 假设-EC / 假设-EA / 假设-EB / 假设-DW / 假设-DI / 假设-AX / 假设-DB / 假设-DF / 假设-DO / 假设-DL / 假设-DN / 假设-DV。**params.Y/G/N ≠ 实验字母 EN ≠ 单字母 E ≠ 假设-EM ≠ 假设-DV**。**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰ ≠ 核对日 2026-11-11**。**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰**。**尤重 params.N 的 0.05 ≠ 面值 0.5‰**。**尤重 params.Y2 的 0.015 ≠ 结算费 0.015‰**。**尤重 0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰**。量纲与语义都不同：四个数是无量纲相对门槛，不是结算费千分比，也不是过户面值，也不是证管费，也不是核对日。**禁把占位读成证管费 0.02‰、EG 过户 0.02‰、B 股成交结算费 0.02‰、股票过户 0.01‰、面值 0.5‰、结算费 0.015‰**。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.en0_primary_demo`**：**写死冻结** **`invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend`**（单一主报，单挂写死；键名保持 `en0_primary_demo=`，不要只写裸 `en0=`；值里的 `hs_blend` 只描述误开形态，诚实锚键名与键值禁止写成 hs_blend / both_same / 沪深均为 一类）。**禁止**与 DV 行权过户、DW 权证/期权行权过户、EM 股票期权结算费、已只补的 B 股成交结算费或权证结算费键双挂。诊断桶不升格；**不得把诊断桶 `vs_DV_cash_option_transfer` / `vs_DW_warrant_option_exercise_transfer` / `vs_EM_option_settlement` 升格进 `en0_primary_demo`**。把沪深合成一句、把 A 股与 B 股互抄、把系统申报档铺到手工行权、把 0.015‰ 与 0.5‰ / 0.02‰ / params.Y2 的 0.015 混读、发明为 0，只作同一误开的并列形态，不另挂第二主键。EN1 不升格并列主报。禁 B2/B3 升格或另挂主报。**零改 U**。**零改 DA**。**零改 DD**。**零改 DQ**。**零改 CZ**。**零改 V**。**零改 S**。**零改 AX**。**零改 DG**。**零改 CY**。**零改 T**。**零改 DF**。**零改 DI**。**零改 DW**。**零改 DL**。**零改 DN**。**零改 DV**。**零改 EH**。**零改 EG**。**零改 EF**。**零改 EE**。**零改 ED**。**零改 EC**。**零改 EB**。**零改 EI**。**零改 EJ**。**零改 EK**。**零改 EL**。**零改 EM**。**零改 O**。**零改 DO**。**零改 DB**。不重开假设-V / T / U / S / AX / DI / DB / DF / DO / DW / EH / EI / EJ / EK / EL / EM / DL / DV。不抢实验 R。切日未钉则 skip，不发明切日。禁止把「更新」2026年1月 / 「2026 年 1 月 1 日更新」写成现金选择权结算费切日。禁止把上证发〔2022〕118 号未核细节写成已核依据，也不得拿它当切日。禁止把失效规则目录页的同标题同日列表路径写成 118 号已核。禁止把沪深合成一句写死。禁止把 A 股与 B 股互抄。禁止把系统申报档铺到手工行权，或把手工行权不收取写成全部为 0 或永久 0。禁止把投资者侧发明为 0。禁止把沪市无专行写成与深市同档或发明沪市为 0。禁止因同是 0.015‰ 抄权证或专项资产管理计划结算费。禁止用经手表或上证发〔2023〕137 号第 3.4 条、第 5.4 条（六）否定或替代中国结算结算费栏。**双字母 EN ≠ 单字母假设-E**；**双字母 EN ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB**。诚实锚须沪深分列，并须 A 股 / B 股分列，B 股还须把系统申报与手工行权分列，不得写成「沪深均为」。

3. **现金选择权结算费诚实锚六键升格写死（不可再写「建议」；键名是 `cash_option_settlement_fee_*`，不是 `option_settlement_fee_*`，亦不是无前缀 `settlement_fee_*`，亦不是 `option_handling_fee_*`，亦不是 `agreed_repurchase_transfer_fee_*`，亦不是 `bond_cash_abs_handling_fee_*`，亦不是 `pref_handling_fee_*`，亦不是 `cdr_transfer_fee_*`）**：`params.cash_option_settlement_fee_honest=szse_ashare_cash_option_0p015_unidirectional_bshare_system_declared_0p015_unidirectional_manual_exercise_exempt_sse_no_dedicated_row_skip`；`params.cash_option_settlement_fee_scope=cash_option_csdc_settlement_fee_only`；`params.cash_option_settlement_fee_over_policy=skip_if_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_missing`；`params.asof_check_date=2026-11-11`（核对日/总管独立重抓日，不是切日；稿内 09:27:30–09:28:06 与风控再下 10:03:30–10:04:06 不得以时刻否决；日期同为 2026-11-11 且官方八件哈希须保持已核 MATCH；不是研究原稿或其它页可能出现的 2026-11-10，不是 ED/EE/EF 的 2026-09-28，不是 EC 的 2026-10-23，不是表「更新」2026年1月 / 2026-01-01）；`params.fill_time=next_open`；`params.fail_policy=skip`（缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额则 skip；切日未钉的历史费率变更 skip，不发明）。须沪深分列，并须 A 股 / B 股分列，B 股还须把系统申报与手工行权分列。层次是中国结算「结算参与人业务收费 / 结算费」，不是行权过户（归 DV），也不是 B 股二级成交结算费，也不是权证结算费，也不是股票期权结算费（归 EM），也不是经手费（归 EI）。深市已核原文：「A 股现金选择权」按清算金额的 0.015‰向结算参与人单向收取；「B 股现金选择权」通过交易系统申报的按行权清算金额的 0.015‰向结算参与人单向收取，不通过交易系统申报的手工行权业务不收取行权结算费。两品种必须分列。收费对象是结算参与人，不得因此把投资者侧发明为 0。不得把系统申报档铺到手工行权，也不得把手工行权不收取发明成全部为 0 或永久 0。沪市结算费栏无「A 股现金选择权」「B 股现金选择权」专行，该腿费率细节 skip，不得写成与深市同档，也不得发明沪市为 0。过户层归 DV，零改 DV。不得因同是 0.015‰ 抄权证或沪市专项资产管理计划结算费。handoff 十八键：`cash_option_transfer_handoff=dv_page`；`warrant_option_exercise_transfer_handoff=dw_page`；`option_settlement_handoff=em_page`；`option_handling_handoff=ei_page`；`ashare_handling_handoff=s_page`；`transfer_fee_handoff=u_page`；`fund_handling_handoff=ax_page`；`pref_handling_handoff=eh_page`；`cdr_transfer_handoff=eg_page`；`agreed_repurchase_handling_handoff=ej_page`；`agreed_repurchase_transfer_handoff=el_page`；`bond_cash_abs_handling_handoff=ek_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`bshare_settlement_handoff=facts_only`；`warrant_settlement_handoff=facts_only`；`warrant_handling_handoff=facts_only`；`am_plan_settlement_handoff=facts_only`。全部 `merge_with_*=False`。勿误抄 EM 的 `option_exercise_transfer_handoff`。**零改 U**。**零改 DA**。**零改 DD**。**零改 DQ**。**零改 CZ**。**零改 V**。**零改 S**。**零改 AX**。**零改 DG**。**零改 CY**。**零改 T**。**零改 DF**。**零改 DI**。**零改 DW**。**零改 DL**。**零改 DN**。**零改 DV**。**零改 EH**。**零改 EG**。**零改 EF**。**零改 EE**。**零改 ED**。**零改 EC**。**零改 EB**。**零改 EI**。**零改 EJ**。**零改 EK**。**零改 EL**。**零改 EM**。**零改 O**。**零改 DO**。**零改 DB**。**不抢实验 R**。

**硬分列保住**：EN≠DV≠DW≠EM≠EI≠S≠U≠EL≠EJ≠EK≠EH≠EG≠AX≠V≠T；**双字母 EN ≠ 单字母假设-E**；**双字母 EN ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB**；**params.Y / params.G / params.N ≠ 实验字母 EN ≠ 单字母 E**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰ ≠ 核对日 2026-11-11**；**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰**；**尤重 params.N 的 0.05 ≠ 面值 0.5‰**；**尤重 params.Y2 的 0.015 ≠ 结算费 0.015‰**；**尤重 0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰**；**须沪深分列**；**须 A 股 / B 股分列**；**须把 B 股系统申报与手工行权分列**；**零改 U**。**零改 DA**。**零改 DD**。**零改 DQ**。**零改 CZ**。**零改 V**。**零改 S**。**零改 AX**。**零改 DG**。**零改 CY**。**零改 T**。**零改 DF**。**零改 DI**。**零改 DW**。**零改 DL**。**零改 DN**。**零改 DV**。**零改 EH**。**零改 EG**。**零改 EF**。**零改 EE**。**零改 ED**。**零改 EC**。**零改 EB**。**零改 EI**。**零改 EJ**。**零改 EK**。**零改 EL**。**零改 EM**。**零改 O**。**零改 DO**。**零改 DB**；不预留 #150；不写下一字母；本页不开回测/真数/开户/实盘。

**状态**：**预检有条件通过·三条已冻·待复检**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–EN纸面齐**；本页不开回测/真数/开户/实盘。口径「收讫」（讫=U+8BAB）。

| 2026-12-20 | 风控预检补丁·冻结三条写死——依据 `预检-假设EN-20261111.md`（SHA256=`77504fa4dc4a69b69de70db75d1d2b527ceec6573e7403d3401b799fb6042237`；结论=有条件通过；tip基=`50e23cb1` / `50e23cb133eb2c6990c604bf455d022daa5b4c15`；分支起点 HEAD=`1acf8cec` / `1acf8cec2d84c798a4ead8d0b47aa806b624955c`；开工核 origin/main 仍停在 starting_ref `1acf8cec2d84c798a4ead8d0b47aa806b624955c`，未更前，以该提交为基线）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛；**params.Y/G/N ≠ 实验字母 EN ≠ 单字母 E ≠ 假设-EM ≠ 假设-DV**；**params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰ ≠ 核对日 2026-11-11**；**params.G 的 0.01 ≠ 股票过户 0.01‰**；**params.N 的 0.05 ≠ 面值 0.5‰**；**params.Y2 的 0.015 ≠ 结算费 0.015‰**；**0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰**；禁 null；禁 holdout/OOS 标定）。② `en0_primary_demo=invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend`（单挂写死；键名保持 `en0_primary_demo=`；不要只写裸 `en0=`；不得把诊断桶 `vs_DV_cash_option_transfer` / `vs_DW_warrant_option_exercise_transfer` / `vs_EM_option_settlement` 升格进主键；把沪深合成一句、把 A 股与 B 股互抄、把系统申报档铺到手工行权、把 0.015‰ 与 0.5‰ / 0.02‰ / params.Y2 的 0.015 混读、发明为 0，只作同一误开的并列形态，不另挂第二主键）。③ 锚六键写死 `cash_option_settlement_fee_honest=szse_ashare_cash_option_0p015_unidirectional_bshare_system_declared_0p015_unidirectional_manual_exercise_exempt_sse_no_dedicated_row_skip` / `cash_option_settlement_fee_scope=cash_option_csdc_settlement_fee_only` / `cash_option_settlement_fee_over_policy=skip_if_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_missing` / `asof_check_date=2026-11-11` / `fill_time=next_open` / `fail_policy=skip`。须沪深分列，并须 A 股 / B 股分列，B 股还须把系统申报与手工行权分列。handoff 十八键保持原值，全部 `merge_with_*=False`。状态=**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–EN纸面齐**。**不改 #110–#148**。**不改 #148 里「不预留 #149」原句**。不预留 #150。不写下一字母。零改 U/DA/DD/DQ/CZ/V/S/AX/DG/CY/T/DF/DI/DW/DL/DN/DV/EH/EG/EF/EE/ED/EC/EB/EI/EJ/EK/EL/EM/O/DO/DB。不开回测/真数/开户/实盘。真数仍停。基于 tip=`50e23cb1`。 |
| 2026-12-20 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。现金选择权结算费误套行权过户或成交结算费或权证结算或沪深合成（费用层，不是行权过户，也不是 B 股二级成交结算费）；`en0_primary_demo` 建议 `invent_cash_option_settlement_fee_as_transfer_bshare_trade_warrant_or_hs_blend`，单一主报，单挂写死，不要只写裸 `en0=`，禁与 DV 行权过户、DW 权证/期权行权过户、EM 股票期权结算费、已只补的 B 股成交结算费或权证结算费键双挂，诊断桶不升格，EN1 不升格，把沪深合成一句、把 A 股与 B 股互抄、把系统申报档铺到手工行权、把 0.015‰ 与 0.5‰ / 0.02‰ / params.Y2 的 0.015 混读、发明为 0 只作同一误开的并列形态、不另挂第二主键；**尤重零改 U / DA / DD / DQ / CZ / V / S / AX / DG / CY / T / DF / DI / DW / DL / DN / DV / EH / EG / EF / EE / ED / EC / EB / EI / EJ / EK / EL / EM / O / DO / DB**；**尤重实验 R 不抢**；**尤重不重开假设-V / T / U / S / AX / DI / DB / DF / DO / DW / EH / EI / EJ / EK / EL / EM / DL / DV**；**尤重 EN ≠ DV ≠ DW ≠ EM ≠ EI ≠ S ≠ U ≠ EL ≠ EJ ≠ EK ≠ EH ≠ EG ≠ AX ≠ V ≠ T**；**尤重须沪深及 A 股 / B 股分列，禁止把诚实锚写成「沪深均为 0.015‰」；B 股还须把通过交易系统申报与手工行权分列**；**尤重 0.015‰ ≠ 0.02‰ ≠ 0.5‰ ≠ 0.0004‰ ≠ 1‰；0.015‰ ≠ params.Y2 的 0.015；结算费 ≠ 行权过户 ≠ B 股二级成交结算费 ≠ 权证结算费 ≠ 股票期权按张结算费**；**尤重不得因同是 0.015‰ 就把权证或沪市专项资产管理计划结算费抄到现金选择权腿；不得因收费对象是结算参与人就把投资者侧发明为 0；不得把系统申报档铺到手工行权，也不得把手工行权不收取发明成全部为 0 或永久 0**；**尤重禁止发明切日；表「更新」2026年1月 / 「2026 年 1 月 1 日更新」不是首次生效日；118 号原件未打开，不得把未核细节写成已核依据；废止句以 137 号通知页为准（自 2023年8月28日起废止）；失效规则目录上未打开的列表条目不视为 118 号已核；该件是可转债经手费通知，本选题不依赖，零改 DB**；**尤重两所收费表与 137 号通知页及附件指引无「结算费」专行，不能替代中国结算结算费栏，也不得用经手表否定结算费栏，零改 EI**；**尤重双字母 EN ≠ 单字母假设-E，亦 ≠ 假设-EM / 假设-EL / 假设-EK / 假设-EJ / 假设-EI / 假设-EH / 假设-EG / 假设-EF / 假设-EE / 假设-ED / 假设-EC / 假设-EA / 假设-EB**；**尤重 params.Y/G/N ≠ 实验字母 EN / 单字母 E / 假设-EM / 假设-DV**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ EG 过户 0.02‰ ≠ B 股成交结算费 0.02‰**；**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰**；**尤重 params.N 的 0.05 ≠ 面值 0.5‰**；**尤重 params.Y2 的 0.015 ≠ 结算费 0.015‰**；**禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格，不另挂主报，零改 O，不改选 B2/B3**；**禁把占位读成千分比或面值档**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**；锚建议·待冻、未冻：`cash_option_settlement_fee_honest=szse_ashare_cash_option_0p015_unidirectional_bshare_system_declared_0p015_unidirectional_manual_exercise_exempt_sse_no_dedicated_row_skip` / scope=`cash_option_csdc_settlement_fee_only` / over_policy=`skip_if_venue_or_ab_share_or_bshare_system_flag_or_clearing_amount_missing` / `asof_check_date=2026-11-11` / `fill_time=next_open` / `fail_policy=skip`；口径：深市 A 股现金选择权按清算金额的 0.015‰向结算参与人单向收取；深市 B 股通过交易系统申报的按行权清算金额的 0.015‰向结算参与人单向收取，手工行权不收取；沪市结算费栏无专行，该腿 skip；收费对象为结算参与人，不得发明投资者侧为 0；缺交易所、A 股或 B 股标志、是否通过交易系统申报（B 股）或清算金额、或缺切日则 skip（**草稿方向，尚未冻，不要写成已冻**）；口径注释讫=U+8BAB；深市中国结算 sha256=`dff4a06ce20e180f4a85ddae138211dcf7dd3246fb84775453cfd21cbaec6573`（114722B，目录 `a59388fb…`）；沪市中国结算 sha256=`84a99e563cb8e84e264c88e3bea2df5f4ac50b1e95330417ec30e2b2566d862f`（139671B，目录 `922adc26…`）；上交所收费一览表 sha256=`a28de66ea31037ffa240a2212a8599a06f1f1513f4c4a424976f3a193ae1eb7a`（40445B）；上交所条目页 sha256=`af521f20b42a238fbd1b14f1e8793d9ecf1a5bb933d3daa88d26805762053bdd`（41076B）；深交所收费页 sha256=`fbd7df3dfa07778b1318564563d22992f19d06bde415144fef248f27674f03c7`（90980B）；上证发〔2023〕137 号通知页 sha256=`4e0e6964e3688dce18a484ca9bbd3a5927633f17842524baf62b4d11bb159fe1`（34190B）；137 号附件指引 docx SHA256=`b42cb6ad16be71f59618e2150ec31af57e8cf8874bc83973934ca8237fd56e84`（31017B），全文无「结算费」，不是结算费依据；失效规则目录页 SHA256=`f22747a4cbbe684ed3be4e85fcd044a0df3d743bb96d5e53a46bde3855b64d78`（139710B），未打开条目页，不视为 118 号已核；经手表只作对照，不替代结算费栏；handoff：`cash_option_transfer_handoff=dv_page`，`warrant_option_exercise_transfer_handoff=dw_page`，`option_settlement_handoff=em_page`，`option_handling_handoff=ei_page`，`ashare_handling_handoff=s_page`，`transfer_fee_handoff=u_page`，`fund_handling_handoff=ax_page`，`pref_handling_handoff=eh_page`，`cdr_transfer_handoff=eg_page`，`agreed_repurchase_handling_handoff=ej_page`，`agreed_repurchase_transfer_handoff=el_page`，`bond_cash_abs_handling_handoff=ek_page`，`stamp_handoff=v_page`，`csrc_fee_handoff=t_page`，`bshare_settlement_handoff=facts_only`，`warrant_settlement_handoff=facts_only`，`warrant_handling_handoff=facts_only`，`am_plan_settlement_handoff=facts_only`，并保留同模板其余旁路 handoff；全部 `merge_with_*=False`；`merge_with_S/AX/DB/DO/DF/DI/EJ/EI/EH/EG/DQ/DW/U/V/T/DG/CY/O/E/DL/DN/DV/DD/DA/EK/EL/EM=False`；**硬分列：EN≠DV≠DW≠EM≠EI≠S≠U≠EL≠EJ≠EK≠EH≠EG≠AX≠V≠T≠DA≠DD≠DQ≠CZ≠DG≠CY≠DF≠DI≠DL≠DN≠EF≠EE≠ED≠EC≠EB≠O≠DO≠DB**；**双字母 EN ≠ 单字母 E**；**未标纸面齐**；**不写 A/D–EN纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–EM；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–EM；**零改 U**；**零改 DA**；**零改 DD**；**零改 DQ**；**零改 CZ**；**零改 V**；**零改 S**；**零改 AX**；**零改 DG**；**零改 CY**；**零改 T**；**零改 DF**；**零改 DI**；**零改 DW**；**零改 DL**；**零改 DN**；**零改 DV**；**零改 EH**；**零改 EG**；**零改 EF**；**零改 EE**；**零改 ED**；**零改 EC**；**零改 EB**；**零改 EI**；**零改 EJ**；**零改 EK**；**零改 EL**；**零改 EM**；**零改 O**；**零改 DO**；**零改 DB**；不改 #110–#148；不重开假设-R；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-S；不重开假设-AX；不重开假设-DI；不重开假设-DB；不重开假设-DF；不重开假设-DO；不重开假设-DW；不重开假设-EH；不重开假设-EI；不重开假设-EJ；不重开假设-EK；不重开假设-EL；不重开假设-EM；不重开假设-DL；不重开假设-DV；不写下一字母；不预留 #150；不开真数/回测/开户/实盘。基 tip=`5e0e4981`（A/D–EM纸面齐已合，已收讫，讫=U+8BAB，全长 `5e0e498165a3c0ff447a33e4f2fec6e6963e9e71`；分支起点 HEAD=`e88b7463e31322289d76c45e7fb187e9c5e1a58f`；开工核 origin/main 未比该基线前进；不改该基线上的 #110–#148，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文，亦不改 #148 里「不预留 #149」原句，亦不改 #147 里「不预留 #148」原句，亦不改 #146 里「不预留 #147」原句）。 |
