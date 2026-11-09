# 假设-DT · 可转债整手价位误套股票（成交规则）

更新：2026-11-30  
来源：总管线 / 基 tip=`797e855b` / 全长 `797e855b5bb0a788e0339103de42cd27b9231c42`（A/D–DS纸面齐已合）；**不改已冻 A–DQ / DA–DS**；**不改假设-DS 正文**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-S / 假设-AX / 假设-T / 假设-U / 假设-V / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-E / 假设-F / 假设-A / 假设-D 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ / 假设-BR）；**不重开假设-T**；**不重开假设-R**；**不重开假设-E**；**不重开假设-F**；**不重开假设-Q**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-CQ**；**不重开假设-D**；**不重开假设-S**；**不重开假设-M**；**不重开假设-O**；**不重开假设-DO**；**不重开假设-DQ**；**不重开假设-AC**；**不重开假设-U**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**）后写下一草稿 DT；清单 #128=DS，本页占用 **#129=DT**；选题是回测把**可转债整手和最小价位**误套成**股票 100 股 / 0.01 元**（可转债申报按 1000 元面额整数倍、最小价位 0.001 元；禁止套股票 100 股/0.01；基金 0.001 价位只对照，禁止把基金档升格进主报）；假设-E 只收股票/科创整手（100 股或科创 200 股 ≠ 可转债 1000 元面额），假设-F 只收股票涨跌停取整（先乘比例再收到 0.01 ≠ 本页最小价位误套），假设-Q 只收可转债回转/涨跌幅/收盘，假设-DS 只收转股所得股票印花，假设-DR 只收可转债盘后定价通道，假设-CQ 只收转股可成交性，假设-R 只收股票 ETF 假 T+0，假设-T 只收股票证管费切日；**新建实验 DT**；不写下一字母；不预留 #130  
状态：**预检有条件通过·三条已冻·待复检**（结论栏空；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DT纸面齐**；禁止把「可转债按股票 100 股 / 0.01 元申报」当诚实成交规则；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–DS**；尤其不改假设-T / 假设-E / 假设-F / 假设-Q / 假设-DS / 假设-DR / 假设-CQ / 假设-R / 假设-D；**不重开假设-T**；**不重开假设-R**；**不重开假设-E**；**不重开假设-F**；**不重开假设-Q**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-CQ**；**不重开假设-D**；**不重开假设-S**；**不重开假设-M**；**不重开假设-O**；**不重开假设-DO**；**不重开假设-DQ**；**不重开假设-AC**；**不重开假设-U**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DT（#129）。一句话误开：回测把可转债整手价位误套股票，把 100 股或 0.01 元价位套到可转债申报，或只抄基金 0.001 价位而不带 1000 元面额整手，或与 T股票证管费 / E股票科创整手 / F涨跌停取整 / Q转债回转涨跌幅收盘 / DS转股印花 / DR盘后定价通道 / CQ转股可成交性 / R股票ETF假T+0 混读，或缺 venue/证券类别或官方整手/价位规则仍不 skip，系统性改写可转债申报的数量与价位闸门。**禁把 T/E/F/Q/DS/DR/CQ/R 混读升格进 `dt0`**。

> **字母消歧（硬）**：本页**实验字母 DT** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DT**；**params 字母 ≠ 假设-T**；**勿把 `params.Y` 读成实验字母 DT，亦勿读成假设-T**；**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**；**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DT**；**尤重：`params.G` 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是 0.01 元价位，也不是 0.001 元价位，更不是 1000 元面额；**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**；**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DT**；**params.N ≠ 单字母假设-N**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DT ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 T**（股票证管费切日；**双字母 DT ≠ 单字母假设-T；严禁复用假设-T**；**不重开假设-T**；组名 DT0/DT1/DT2 是本页三组对照，≠ 单字母实验 T，亦 ≠ 单字母实验 D）≠ **单字母实验 R**（股票 ETF 假 T+0 / 股票ETF假回转；**双字母 DT ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `dt0`**）≠ **单字母实验 E**（股票/科创整手；**E 股票/科创整手 ≠ 本页可转债 1000 元面额**；**严禁复用假设-E**）≠ **单字母实验 F**（涨跌停取整；**F 涨跌停取整 ≠ 本页最小价位误套**；**严禁复用假设-F**）≠ **单字母实验 Q**（可转债回转/涨跌幅/收盘；**Q 转债回转/涨跌幅/收盘 ≠ 本页整手价位**；**双字母 DT ≠ 单字母假设-Q；严禁复用假设-Q**）≠ **假设-BR**（融券借券费/融出费率计提；**双字母 DT ≠ 假设-BR；严禁复用假设-BR**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DT ≠ 单字母假设-A**）≠ 双字母 **DS**（可转债转股所得股票印花税误免；**DS 转股印花 ≠ 本页申报约束**）≠ **DR**（可转债盘后定价误套股票盘后固定价格；**DR 盘后定价通道 ≠ 本页整手价位**）≠ **CQ**（可转债转股可成交性误开；**CQ 转股可成交性 ≠ 本页订单数量/价位闸门**）≠ **DQ**（ETF 申赎组合证券过户费误套）≠ **DP**（可交换债换股印花税误漏）≠ **DO**（可转债回售处理）≠ **DN**（可交换债换股过户费误套）≠ **DM**（可交换债换股经手费误套现货）≠ **DL**（股票综合协议过户费下浮）≠ **DK**（场内基金印花税误抽）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债现货经手费沪深合成）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债现货印花税误抽）≠ **DB**（可转债现货经手费）≠ **DA**（场内基金二级过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费）≠ **U**（股票过户费）≠ **V**（股票印花税切日）≠ **AC**（北交所涨跌幅与盘后）≠ **O**（大宗三通道）≠ **M**（股票盘后通道）≠ **CH**（股票盘后固定价格可成交性）≠ **CL**（可转债盘后定价可成交性）≠ **CR**（认沽/认购行权成交）。**DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠BR≠A≠D**。**双字母 DT ≠ 单字母 D/T**。**双字母 DT ≠ 单字母假设-D / 假设-T**。**params.Y/G/N ≠ 实验字母 DT；亦 ≠ 单字母 D/T**。**params 字母 ≠ 假设-T**。**勿把 `params.Y` 或 `params.G` 读成实验字母 DT，亦勿把单字母假设-D / 假设-T 读成双字母 DT**。**尤重：`params.G` 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元；`params.Y` 的 0.02 ≠ 证管费 0.02‰；占位 ≠ 1000 元面额**。**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**。**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**。**可转债整手价位误套股票 ≠ T股票证管费 ≠ E股票/科创整手 ≠ F涨跌停取整 ≠ Q转债回转/涨跌幅/收盘 ≠ DS转股印花 ≠ DR盘后定价通道 ≠ CQ转股可成交性 ≠ R股票ETF假T+0**。**尤重：不重开假设-T（股票证管费切日）；禁把 `vs_T_csrc_fee` / 证管费升格进 `dt0`**。**尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `dt0`**。**尤重：E 股票/科创整手 ≠ 本页可转债 1000 元面额——禁止合成/混读升格进 `dt0`**。**尤重：F 涨跌停取整 ≠ 本页最小价位误套——禁止合成/混读升格进 `dt0`**。**尤重：Q 转债回转/涨跌幅/收盘 ≠ 本页整手价位——禁止合成/混读升格进 `dt0`**。**尤重：DS 转股印花 ≠ 本页申报约束——禁止合成/混读升格进 `dt0`**。**尤重：DR 盘后定价通道 ≠ 本页整手价位——禁止合成/混读升格进 `dt0`**。**尤重：CQ 转股可成交性 ≠ 本页订单数量/价位闸门——禁止合成/混读升格进 `dt0`**。**尤重：双字母 DT ≠ 单字母假设-D / 假设-T**。**禁把 T/E/F/Q/DS/DR/CQ/R 混读升格进 `dt0`**。

### 专节 · 双字母 DT ≠ 单字母假设-D / 假设-T；且 ≠ 假设-E / 假设-F / 假设-Q / 假设-DS / 假设-DR / 假设-CQ / 假设-R（硬）

| 维度 | 对照页 | 本页假设-DT（双字母） |
|------|--------|----------------------|
| 题面 T | **股票证管费切日**（假设-T；0.02‰ 双边是费率，不是本页门槛） | **不重开假设-T**。证管费切日 ≠ 可转债整手价位。`params.Y` 的 0.02 不是证管费 0.02‰。**双字母 DT ≠ 单字母假设-T**；**严禁复用假设-T**；**DT≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：不重开假设-T；禁把 `vs_T_csrc_fee` / 证管费升格进 `dt0`**；`csrc_fee_handoff=t_page`；诊断桶 `vs_T_csrc_fee` 不升格 |
| 题面 E | **股票/科创整手**（主板/创业板 100 股整数倍；科创板单笔至少 200 股） | E 股票/科创整手 ≠ 本页可转债 1000 元面额。股数整手 ≠ 面额整手。**DT≠E**；**严禁复用假设-E**；**不重开假设-E**；**不改 E**；**尤重：E 股票/科创整手 ≠ 本页可转债 1000 元面额——禁止合成/混读升格进 `dt0`**；`ashare_lot_handoff=e_page`；诊断桶 `vs_E_ashare_star_lot` / `invent_100share_on_cb` 不升格 |
| 题面 F | **涨跌停取整**（先乘比例，再四舍五入到股票最小价位 0.01） | F 涨跌停取整 ≠ 本页最小价位误套。限制价怎么收成价位 ≠ 申报最小价位被套成股票 0.01。**DT≠F**；**严禁复用假设-F**；**不重开假设-F**；**不改 F**；**尤重：F 涨跌停取整 ≠ 本页最小价位误套——禁止合成/混读升格进 `dt0`**；`limit_round_handoff=f_page`；诊断桶 `vs_F_limit_round` / `invent_001_tick_on_cb` 不升格 |
| 题面 Q | **可转债回转 / 涨跌幅 / 收盘**（按股票规则回放） | Q 转债回转/涨跌幅/收盘 ≠ 本页整手价位。当日回转、板幅、收盘怎么产生 ≠ 申报数量和最小价位。**双字母 DT ≠ 单字母假设-Q**；**严禁复用假设-Q**；**DT≠Q**；**不重开假设-Q**；**不改 Q**；**尤重：Q 转债回转/涨跌幅/收盘 ≠ 本页整手价位——禁止合成/混读升格进 `dt0`**；`cb_rules_handoff=q_page`；诊断桶 `vs_Q_cb_rules` 不升格 |
| 题面 DS | **转股所得股票印花**（误免成 0） | DS 转股印花 ≠ 本页申报约束。交割那笔股票交不交印花 ≠ 可转债订单的数量/价位闸门。**DT≠DS**；**严禁复用假设-DS**；**不重开假设-DS**；**不改 DS**；**尤重：DS 转股印花 ≠ 本页申报约束——禁止合成/混读升格进 `dt0`**；`cb_conversion_stamp_handoff=ds_page`；诊断桶 `vs_DS_conversion_stamp` 不升格 |
| 题面 DR | **可转债盘后定价通道**（误套股票盘后固定价格） | DR 盘后定价通道 ≠ 本页整手价位。盘后用哪条价格 ≠ 申报整手和最小价位。**DT≠DR**；**严禁复用假设-DR**；**不重开假设-DR**；**不改 DR**；**尤重：DR 盘后定价通道 ≠ 本页整手价位——禁止合成/混读升格进 `dt0`**；`aft_pricing_handoff=dr_page`；诊断桶 `vs_DR_aft_pricing` 不升格 |
| 题面 CQ | **可转债转股可成交性**（默认转股申报必能按转股价全额转成） | CQ 转股可成交性 ≠ 本页订单数量/价位闸门。能不能转成 ≠ 这笔可转债申报的股数/面额和价位合不合法。**DT≠CQ**；**严禁复用假设-CQ**；**不重开假设-CQ**；**不改 CQ**；**尤重：CQ 转股可成交性 ≠ 本页订单数量/价位闸门——禁止合成/混读升格进 `dt0`**；`cb_conversion_fill_handoff=cq_page`；诊断桶 `vs_CQ_conversion_fill` 不升格 |
| 题面 R | **股票 ETF 假 T+0**（假设-R 股票ETF假回转；回转名单 ≠ 整手价位） | 实验 R 不抢、不重开、不混读升格进 `dt0`。股票 ETF 假当日回转 ≠ 本页可转债整手价位被套成股票。**双字母 DT ≠ 单字母假设-R**；**严禁复用假设-R**；**DT≠R**；**不重开假设-R**；**不改 R**；**尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `dt0`**；`etf_t0_handoff=r_page`；诊断桶 `vs_R_etf_t0` 不升格 |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 申报数量和最小价位。**双字母 DT ≠ 单字母假设-D**；**严禁复用假设-D**；**DT≠D**；**不改 D** |
| 题面 DQ | **ETF 申赎组合证券过户费误套** | 篮子过户费 ≠ 整手价位。**DT≠DQ**；**不重开假设-DQ**；**不改 DQ** |
| 题面 DP | **可交换债换股印花税误漏** | 换股印花 ≠ 本页申报约束。**DT≠DP**；**不重开假设-DP**；**不改 DP** |
| 题面 DO | **可转债回售处理** | 回售经手 ≠ 整手价位。**DT≠DO**；**不重开假设-DO**；**不改 DO** |
| 题面 DN | **可交换债换股过户费** | 换股过户 ≠ 整手价位。**DT≠DN**；**不重开假设-DN**；**不改 DN** |
| 题面 DM | **可交换债换股经手费** | 换股经手 ≠ 整手价位。**DT≠DM**；**不重开假设-DM**；**不改 DM** |
| 题面 DL | **股票综合协议过户费下浮** | 综合协议过户下浮 ≠ 整手价位。**DT≠DL**；**不重开假设-DL**；**不改 DL** |
| 题面 DK | **场内基金印花税误抽** | 基金印花 ≠ 整手价位。**DT≠DK**；**不改 DK** |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 整手价位，亦 ≠ 股票证管费切日。**DT≠DJ**；**不改 DJ**；**不重开假设-T** |
| 题面 DI | **股票大宗经手下浮** | 大宗经手下浮 ≠ 整手价位。**DT≠DI**；**不重开假设-DI**；**不改 DI** |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 整手价位。**DT≠DH**；**不改 DH** |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 整手价位。**DT≠DG**；**不改 DG** |
| 题面 DF | **可交换债现货经手费沪深合成** | 可交换现货经手 ≠ 整手价位。**DT≠DF**；**不重开假设-DF**；**不改 DF** |
| 题面 DE | **可转债证管费** | 转债证管费误套 ≠ 本页整手价位，亦 ≠ 重开假设-T。**DT≠DE**；**不改 DE**；**不重开假设-T** |
| 题面 DD | **可转债现货过户费** | 转债现货过户 ≠ 整手价位。**DT≠DD**；**不重开假设-DD**；**不改 DD** |
| 题面 DC | **可转债现货印花税误抽** | 转债现货印花 ≠ 整手价位。**DT≠DC**；**不改 DC** |
| 题面 DB | **可转债现货经手费** | 转债现货经手 ≠ 整手价位。**DT≠DB**；**不重开假设-DB**；**不改 DB** |
| 题面 DA | **场内基金二级过户费** | 二级过户 ≠ 整手价位。**DT≠DA**；**不重开假设-DA**；**不改 DA** |
| 题面 S | **沪深 A 股竞价经手费切日** | 股票经手切日 ≠ 整手价位。**DT≠S**；**不重开假设-S**；**不改 S** |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 整手价位。基金 0.001 价位只对照，不把基金档升格进主报。**DT≠AX**；**不重开假设-AX**；**不改 AX** |
| 题面 U | **股票过户费切日** | 股票过户切日 ≠ 整手价位。**DT≠U**；**不重开假设-U**；**不改 U** |
| 题面 V | **股票印花税切日** | 股票印花切日 ≠ 整手价位。**DT≠V**；**不重开假设-V**；**不改 V** |
| 题面 AC | **北交所涨跌幅与盘后** | 北交所涨跌幅、盘后 ≠ 可转债整手价位。**DT≠AC**；**不重开假设-AC**；**不改 AC** |
| 题面 O | **大宗三通道** | 大宗通道 ≠ 整手价位。**DT≠O**；**不重开假设-O**；**不改 O** |
| 题面 M | **股票盘后通道** | 股票盘后通道 ≠ 整手价位。**DT≠M**；**不重开假设-M**；**不改 M** |
| 题面 CH | **股票盘后固定价格可成交性** | 盘后可成交 ≠ 整手价位。**DT≠CH**；**不重开假设-CH**；**不改 CH** |
| 题面 CL | **可转债盘后定价可成交性** | 转债盘后可成交 ≠ 整手价位。**DT≠CL**；**不重开假设-CL**；**不改 CL** |
| 题面 CR | **认沽/认购行权成交** | 行权兑付 ≠ 整手价位。**DT≠CR**；**不重开假设-CR**；**不改 CR** |
| 题面 BR | **融券借券费/融出费率** | 借券费计提 ≠ 整手价位。**双字母 DT ≠ 假设-BR**；**DT≠BR**；**不重开假设-BR**；**不改 BR** |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 整手价位。**DT≠A**；**不抢 A 真数队列**；**不改 A** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ashare_lot_tick_on_cb`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_cb_lot_tick` 双挂；DT1 不升格；`invent_100share_on_cb` / `invent_001_tick_on_cb` / `copy_fund_0001_tick_onto_cb_without_lot` / `vs_E_ashare_star_lot` / `vs_F_limit_round` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_R_etf_t0` / `vs_T_csrc_fee` / `missing_venue_or_sec_type_not_skip` 只作诊断对照，不升格主报；**尤重禁止把 T / E / F / Q / DS / DR / CQ / R 混读升格进 `dt0`**） |
| 文档 | 清单实验 T / E / F / Q / DS / DR / CQ / R / D / DQ / DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / U / V / AC / O / M / CH / CL / CR / BR / A（**只读；禁止改写**） | `假设-DT-可转债整手价位误套股票.md`（新建） |
| 预检键 | 实验字母 T / E / F / Q / DS / DR / CQ / R / D / DQ / DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / U / V / AC / O / M / A / Y / G / N，以及已存在 CH / CL / CR / BR | 实验字母 **DT** / `dt0_primary_demo`；**不得**占用或改写预检 T/E/F/Q/DS/DR/CQ/R/D/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/U/V/AC/O/M/A/Y/G/N，亦不得改写 CH/CL/CR/BR |

**禁止**：把 DT 写成「T / E / F / Q / DS / DR / CQ / R / D / A 的续篇」；把「股票整手已分列（E）/ 涨跌停取整已分列（F）/ 转债回转涨跌幅收盘已分列（Q）/ 转股印花已分列（DS）/ 盘后定价通道已分列（DR）/ 转股可成交已分列（CQ）/ 股票 ETF 回转已分列（R）/ 股票证管费已分列（T）」写成「可转债整手价位已诚实」；把实验字母 DT 与单字母 D/T 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-T 读成双字母 DT**；**尤重勿把 `params.Y` 读成假设-T**；**尤重勿把 `params.G` 读成实验字母 DT**；**尤重 `params.G` 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元；`params.Y` 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同）**；**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**；**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**；**params 字母 ≠ 假设-T**；**尤重不重开假设-T，禁把 `vs_T_csrc_fee` / 证管费升格进 `dt0`**；**尤重实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `dt0`**；**尤重 E 股票/科创整手 ≠ 本页可转债 1000 元面额，禁止合成/混读升格进 `dt0`**；**尤重 F 涨跌停取整 ≠ 本页最小价位误套，禁止合成/混读升格进 `dt0`**；**尤重 Q 转债回转/涨跌幅/收盘 ≠ 本页整手价位，禁止合成/混读升格进 `dt0`**；**尤重 DS 转股印花 ≠ 本页申报约束，禁止合成/混读升格进 `dt0`**；**尤重 DR 盘后定价通道 ≠ 本页整手价位，禁止合成/混读升格进 `dt0`**；**尤重 CQ 转股可成交性 ≠ 本页订单数量/价位闸门，禁止合成/混读升格进 `dt0`**；**禁把 T/E/F/Q/DS/DR/CQ/R 混读升格进 `dt0`**；把 `invent_asof_leak_cb_lot_tick` 升格进 `dt0` 或与主报双挂；把诊断桶 `invent_100share_on_cb` / `invent_001_tick_on_cb` / `copy_fund_0001_tick_onto_cb_without_lot` / `vs_E_ashare_star_lot` / `vs_F_limit_round` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_R_etf_t0` / `vs_T_csrc_fee` / `missing_venue_or_sec_type_not_skip` 升格进 `dt0`；把基金 0.001 价位升格进主报；用股票 100 股或 0.01 元去填可转债申报；缺 venue/证券类别或官方整手/价位规则仍硬填。本页主键只用 `dt0` / `dt1` / `dt2` 与 `cb_lot_tick_*`。不写下一字母。不预留 #130。**纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK–DS；勿再只改清单）。**当前禁止标纸面齐**。**不写 A/D–DT纸面齐**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权申报价下，回测把**可转债整手和最小价位**误套成**股票 100 股 / 0.01 元**，或只套 100 股、或只套 0.01 元价位、或只抄基金 0.001 价位而不带 1000 元面额整手，或与 T股票证管费 / E股票科创整手 / F涨跌停取整 / Q转债回转涨跌幅收盘 / DS转股印花 / DR盘后定价通道 / CQ转股可成交性 / R股票ETF假T+0 混读，或缺 venue/证券类别或官方整手/价位规则仍不 skip，相对「缺 venue/证券类别或官方整手/价位规则则 skip；可转债申报=1000 元面额整数倍、最小价位 0.001 元；禁止套股票 100 股/0.01；基金 0.001 价位仅对照、禁止把基金档升格进主报」的诚实组，会**系统性改写可转债申报的数量与价位闸门**——相对诚实锚偏误。套错整手会把能申报的数量写歪，套错价位会把合法报价收成错误的最小变动。

核对日方向（随锚写死；禁止把 1000 元面额、0.001 元价位或证管费 0.02‰ 写成占位门槛）：可转债申报和股票申报分开，价位和涨跌停取整分开，整手和费用分开。`事实与坑` 2026-10-26 已写：申报数量 1000 元面额整数倍（不是股票 100 股）；最小价位 **0.001** 元。来源留在该条（深交所《上市公司自律监管指引第 15 号——可转换公司债券》第七条 / 第九条 / 第十一条）。股票整手留在 E：主板/创业板买入 100 股整数倍，科创板单笔至少 200 股，不要把创业板写成 200 股起。股票涨跌停取整留在 F：先乘比例，再四舍五入到股票最小价位，A 股股票默认 0.01 元。那是限制价怎么收口，不是本页「申报最小价位被套错」。可转债回转、涨跌幅、收盘怎么产生留在 Q。转股印花留在 DS，盘后定价通道留在 DR，转股能不能转成留在 CQ，股票 ETF 假 T+0 留在 R。股票证管费切日留在 T，本页不重开 T。基金最小价位 0.001 元只作对照：看见数字相同，不能把基金档升格成可转债主报，也不能只抄价位、丢掉 1000 元面额整手。缺 venue、证券类别，或官方整手/价位规则对不上，整笔 skip，不用股票 100 股、股票 0.01、基金 0.001、占位 0.01 或证管费 0.02‰ 去填。**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**。**`params.G` 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元**。**`params.Y` 的 0.02 ≠ 证管费 0.02‰**。**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**。**params 字母 ≠ 假设-T**。**禁把 T/E/F/Q/DS/DR/CQ/R 混读升格进 `dt0`**。

证伪方向：若天真组 / 半泄露组相对诚实组的整手价位误套截在标定噪声带内可忽略，且「套 100 股 / 套 0.01 价位 / 只抄基金 0.001 / 核对日泄露 / vs T·E·F·Q·DS·DR·CQ·R」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dt0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结；禁止标纸面齐；不写 A/D–DT纸面齐）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DT ≠ 单字母假设-D / 假设-T**；params 字母 ≠ 假设-T；勿把 params.Y 读成实验字母 DT，亦勿读成假设-T
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DT ≠ 单字母 D/T**
# 【消歧】尤重：params.G 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元（量纲与语义不同：无量纲相对门槛 ≠ 价位）
# 【消歧】尤重：params.Y 的 0.02 ≠ 证管费 0.02‰（无量纲相对门槛 ≠ 假设-T 的费率）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰
# 【消歧】params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费
# 【消歧】params 字母 ≠ 假设-T
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DT ≠ 单字母假设-N**
# params.Y2                               写死冻结 0.015
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：整手价位误套截 ΔCbLotTick / 净差异 / DT1−DT2；**params.Y/G/N ≠ 实验字母 DT ≠ 单字母假设-D / 假设-T**；**params 字母 ≠ 假设-T**；**尤重 params.G 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**；**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        写死冻结 next_open
# params.asof_check_date                  写死冻结 2026-10-26
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.cb_lot_tick_honest               写死冻结 pit_cb_lot_1000_par_tick_0_001_not_ashare_100_0_01
#   诚实锚方向（已写死冻结）：
#   缺 venue、证券类别或官方整手/价位规则 → skip
#   可转债申报 = 1000 元面额整数倍
#   最小价位 = 0.001 元
#   禁止套股票 100 股 / 0.01 元
#   基金 0.001 价位仅对照，禁止把基金档升格进主报
#   禁止把占位 0.02/0.01/0.05/0.015 读成 1000 元面额、0.001 元价位或证管费 0.02‰
#   枚举已写死冻结
#   不把 E 的股票/科创整手、F 的涨跌停取整、Q 的回转涨跌幅收盘、DS 的转股印花、DR 的盘后通道、CQ 的转股可成交、R 的假 T+0、T 的证管费写成可转债整手价位诚实锚
# params.cb_lot_tick_scope                写死冻结 cb_order_lot_tick_vs_ashare_and_fund
#   方向名：可转债申报整手/价位，与股票整手价位、基金价位分列
#   这不是把 1000 元面额或 0.001 元价位冻成门槛
#   可转债整手价位 ≠ 股票 100 股/0.01 ≠ 基金 0.001 价位
# params.cb_lot_tick_over_policy          写死冻结 skip_if_venue_or_sec_type_or_official_rule_missing
#   缺 venue、证券类别或官方整手/价位规则则 skip；禁在缺字段时仍按股票 100 股/0.01 或基金 0.001 把可转债申报填上
# params.ashare_lot_handoff               建议 e_page
#   消费 E 的股票/科创整手，或显式旁路；股票整手 ≠ 本页可转债 1000 元面额；不重开假设-E；不改 E
#   E 禁止合成/混读升格进 dt0；诊断桶 vs_E_ashare_star_lot / invent_100share_on_cb 不得升格进 dt0
# params.limit_round_handoff              建议 f_page
#   消费 F 的涨跌停取整，或显式旁路；涨跌停取整 ≠ 本页最小价位误套；不重开假设-F；不改 F
#   F 禁止合成/混读升格进 dt0；诊断桶 vs_F_limit_round / invent_001_tick_on_cb 不得升格进 dt0
# params.cb_rules_handoff                 建议 q_page
#   可转债回转/涨跌幅/收盘交 Q；Q ≠ 本页整手价位；双字母 DT ≠ 单字母假设-Q；不重开假设-Q；不改 Q
#   Q 禁止合成/混读升格进 dt0；诊断桶 vs_Q_cb_rules 不得升格进 dt0
# params.cb_conversion_fill_handoff       建议 cq_page
#   消费 CQ 的转股可成交性，或显式旁路；可成交性 ≠ 本页订单数量/价位闸门；不重开假设-CQ；不改 CQ
#   CQ 禁止合成/混读升格进 dt0；诊断桶 vs_CQ_conversion_fill 不得升格进 dt0
# params.cb_conversion_stamp_handoff      建议 ds_page
#   转股印花交 DS；DS ≠ 本页申报约束；不重开假设-DS；不改 DS
#   DS 禁止合成/混读升格进 dt0；诊断桶 vs_DS_conversion_stamp 不得升格进 dt0
# params.aft_pricing_handoff              建议 dr_page
#   盘后定价通道交 DR；DR ≠ 本页整手价位；不重开假设-DR；不改 DR
#   DR 禁止合成/混读升格进 dt0；诊断桶 vs_DR_aft_pricing 不得升格进 dt0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 dt0；双字母 DT ≠ 单字母假设-R；不改 R
#   R 禁止合成/混读升格进 dt0；诊断桶 vs_R_etf_t0 不得升格进 dt0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；双字母 DT ≠ 单字母假设-T；params 字母 ≠ 假设-T；不改 T
#   T 禁止合成/混读升格进 dt0；诊断桶 vs_T_csrc_fee 不得升格进 dt0；证管费不得升格进 dt0
# params.fill_time_suspend_handoff        建议 d_page
#   成交时点与停牌交 D；双字母 DT ≠ 单字母假设-D；不改 D
# params.board_capacity_handoff           建议 a_page
#   板上容量交 A；不抢 A 真数队列；不改 A
# params.dt0_primary_demo                 写死冻结 invent_ashare_lot_tick_on_cb
#   单一主报写死，单挂；禁与 invent_asof_leak_cb_lot_tick 双挂；DT1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_cb_lot_tick 只作对照，不得升格进 dt0，不得双挂
#   诊断桶 invent_100share_on_cb / invent_001_tick_on_cb / copy_fund_0001_tick_onto_cb_without_lot / vs_E_ashare_star_lot / vs_F_limit_round / vs_Q_cb_rules / vs_CQ_conversion_fill / vs_DS_conversion_stamp / vs_DR_aft_pricing / vs_R_etf_t0 / vs_T_csrc_fee / missing_venue_or_sec_type_not_skip 不得升格进 dt0
#   尤重：不重开假设-T；禁止把 vs_T_csrc_fee / 证管费混读后写进 dt0
#   尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 dt0
#   尤重：禁止把 E 股票/科创整手与本页可转债 1000 元面额合成/混读后写进 dt0
#   尤重：禁止把 F 涨跌停取整与本页最小价位误套合成/混读后写进 dt0
#   尤重：禁止把 Q 转债回转/涨跌幅/收盘与本页整手价位合成/混读后写进 dt0
#   尤重：禁止把 DS 转股印花与本页申报约束合成/混读后写进 dt0
#   尤重：禁止把 DR 盘后定价通道与本页整手价位合成/混读后写进 dt0
#   尤重：禁止把 CQ 转股可成交性与本页订单数量/价位闸门合成/混读后写进 dt0
#   禁把 T/E/F/Q/DS/DR/CQ/R 混读升格进 dt0
#   基金 0.001 价位仅对照；copy_fund_0001_tick_onto_cb_without_lot 不得升格进 dt0
# params.dt0_invent_ashare_lot_tick_on_cb 建议 True
# params.dt1_asof_leak_cb_lot_tick_only   建议 True
#   半泄露对照；DT1 不升格并列主报；不得把 invent_asof_leak_cb_lot_tick 写进 dt0
# params.dt2_pit_cb_lot_1000_par_tick_0_001_not_ashare_100_0_01 建议 True
# params.merge_with_DS                    建议 False
# params.merge_with_DR                    建议 False
# params.merge_with_DQ                    建议 False
# params.merge_with_DP                    建议 False
# params.merge_with_DO                    建议 False
# params.merge_with_DN                    建议 False
# params.merge_with_DM                    建议 False
# params.merge_with_DL                    建议 False
# params.merge_with_DK                    建议 False
# params.merge_with_DJ                    建议 False
# params.merge_with_DI                    建议 False
# params.merge_with_DH                    建议 False
# params.merge_with_DG                    建议 False
# params.merge_with_DF                    建议 False
# params.merge_with_DE                    建议 False
# params.merge_with_DD                    建议 False
# params.merge_with_DC                    建议 False
# params.merge_with_DB                    建议 False
# params.merge_with_DA                    建议 False
# params.merge_with_S                     建议 False
# params.merge_with_AX                    建议 False
# params.merge_with_T                     建议 False
# params.merge_with_U                     建议 False
# params.merge_with_V                     建议 False
# params.merge_with_AC                    建议 False
# params.merge_with_Q                     建议 False
# params.merge_with_R                     建议 False
# params.merge_with_O                     建议 False
# params.merge_with_M                     建议 False
# params.merge_with_CH                    建议 False
# params.merge_with_CL                    建议 False
# params.merge_with_CR                    建议 False
# params.merge_with_CQ                    建议 False
# params.merge_with_E                     建议 False
# params.merge_with_F                     建议 False
# params.merge_with_BR                    建议 False
# params.merge_with_A                     建议 False
# params.merge_with_D                     建议 False
# params.missing_venue_or_sec_type_or_official_rule_policy 建议 skip
# params.day_freq_proxy                   建议 cb_lot_tick_sensitivity
# params.universe_rule                    建议 cb_lot_tick_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dt_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DT；勿把这个键读成实验 DT，亦勿读成单字母 D/T，亦勿读成假设-T
#   不另挂主报，不预留 #130，不写下一字母
```

### 2.2 三组对照（DT0 / DT1 / DT2）

组名 DT0 / DT1 / DT2 是本页三组，≠ 单字母实验 T（股票证管费切日），亦 ≠ 单字母实验 D（成交时点与停牌），亦 ≠ 单字母实验 R（股票 ETF 假 T+0）。**双字母 DT ≠ 单字母假设-D / 假设-T**。**params 字母 ≠ 假设-T**。

| 组 | 角色 | 口径 |
|----|------|------|
| DT0 | 天真 / 可转债整手价位误套股票 | 按 `dt0_primary_demo` **写死冻结**单一主报 `invent_ashare_lot_tick_on_cb`（单挂写死）：把股票 100 股整手和 0.01 元价位一起套到可转债申报。**禁**与 `invent_asof_leak_cb_lot_tick` 双挂主报。**禁把 T / E / F / Q / DS / DR / CQ / R 合成进 `dt0`**（只作对照/旁路，不得升格进 `dt0` 或另挂主报）。**禁把 T/E/F/Q/DS/DR/CQ/R 混读升格进 `dt0`** |
| DT1 | 半泄露 | 仅核对日把「可转债 1000 元面额整数倍、最小价位 0.001 元」铺到全历史、铺到股票腿、铺到基金腿，或把基金 0.001 写成可转债唯一价位（`invent_asof_leak_cb_lot_tick`）；**不得升格并列主报**，也不得写进 `dt0`（写死冻结：DT1 不升格），不得双挂 |
| DT2 | 诚实 / 可转债按面额整手和 0.001 元价位 | `cb_lot_tick_honest=pit_cb_lot_1000_par_tick_0_001_not_ashare_100_0_01`（写死冻结）：缺 venue/证券类别或官方整手/价位规则则 skip；可转债申报=1000 元面额整数倍、最小价位 0.001 元；禁止套股票 100 股/0.01；基金 0.001 价位仅对照、禁止把基金档升格进主报。股票/科创整手只消费 E，涨跌停取整只消费 F，回转涨跌幅收盘只消费 Q，转股印花只消费 DS，盘后定价只消费 DR，转股可成交只消费 CQ，股票 ETF 假 T+0 只消费 R，股票证管费只消费 T，或显式旁路 |

只套 100 股、只套 0.01 元价位、只抄基金 0.001 而不带整手、把 T/E/F/Q/DS/DR/CQ/R 混进本页，以及相对这些页的对照截（`invent_100share_on_cb` / `invent_001_tick_on_cb` / `copy_fund_0001_tick_onto_cb_without_lot` / `vs_E_ashare_star_lot` / `vs_F_limit_round` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_R_etf_t0` / `vs_T_csrc_fee` / `missing_venue_or_sec_type_not_skip`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dt0_primary_demo`。`vs_T_csrc_fee` 只标记「有人把证管费和本页混读」，**不得升格进 `dt0`**。`vs_E_ashare_star_lot` 与 `invent_100share_on_cb` 只标记股票整手对照，**不得升格进 `dt0`**。`vs_F_limit_round` 与 `invent_001_tick_on_cb` 只标记涨跌停取整/股票价位对照，**不得升格进 `dt0`**。`vs_Q_cb_rules` 只标记回转涨跌幅收盘对照，**不得升格进 `dt0`**。`vs_DS_conversion_stamp` 只标记转股印花对照，**不得升格进 `dt0`**。`vs_DR_aft_pricing` 只标记盘后通道对照，**不得升格进 `dt0`**。`vs_CQ_conversion_fill` 只标记转股可成交对照，**不得升格进 `dt0`**。`vs_R_etf_t0` 只标记「有人把实验 R 和本页混读」，**不得升格进 `dt0`**。`copy_fund_0001_tick_onto_cb_without_lot` 只标记基金价位对照，**不得升格进 `dt0`**。`missing_venue_or_sec_type_not_skip` 同样只作诊断；官方整手/价位规则缺失也走 skip，不另造主报。E 的整手、F 的取整、Q 的规则、DS 的印花、DR 的盘后、CQ 的可成交、R 的假 T+0、T 的证管费只作对照/旁路。

### 2.3 成交规则窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-26`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dt0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺 venue/证券类别或官方整手/价位规则则 skip；可转债申报=1000 元面额整数倍、最小价位 0.001 元；禁止套股票 100 股/0.01；基金 0.001 价位仅对照、禁止把基金档升格进主报。方向随锚写死：**不要把核对日规则铺满全历史，也不要把股票 100 股/0.01 写成可转债唯一规则，也不要把基金 0.001 升格进主报**。范围名 `cb_order_lot_tick_vs_ashare_and_fund` 只标方向：本页只看可转债申报的整手和最小价位有没有被套成股票。股票/科创整手留给 E，涨跌停取整留给 F，回转涨跌幅收盘留给 Q，转股印花留给 DS，盘后通道留给 DR，转股可成交留给 CQ，股票 ETF 假 T+0 留给 R，证管费留给 T。`params.G` 的 0.01 是无量纲相对门槛，不是股票 0.01 元价位，也不是可转债 0.001 元价位。`params.Y` 的 0.02 不是证管费 0.02‰。**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**。**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**。**params 字母 ≠ 假设-T**。缺 venue、证券类别或官方规则则 skip，不用股票 100 股、0.01 元、基金 0.001 或占位 0.01 把可转债申报填上。本页**不开回测**；不拉真数；不做实盘；不开户。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dt0_primary_demo` / `params.Y`·G·N·Y2 / 整手价位开关 / 桶 / 是否把 1000 元面额、0.001 元价位或证管费 0.02‰ 铺到全历史、或把占位读成面额/价位/证管费）。本页不开跑。禁 null。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DT0）/ 半泄露组（DT1）相对诚实组（DT2）的整手价位误套截**显著且集中在可转债申报被套成股票 100 股 / 0.01 元价位的桶**；分桶「套 100 股 / 套 0.01 / 只抄基金 0.001 / 核对日泄露 / vs T·E·F·Q·DS·DR·CQ·R」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 1000 元面额或 0.001 元价位冻成门槛，也不把 `params.G` 的 0.01 读成价位，也不把 `params.Y` 的 0.02 读成证管费。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 E 的股票/科创整手、F 的涨跌停取整、Q 的回转涨跌幅收盘、DS 的转股印花、DR 的盘后定价、CQ 的转股可成交、R 的股票 ETF 假 T+0、T 的股票证管费、BR 的借券费、DQ 的篮子过户、DP 的换股印花、DO 的回售处理、DN 的换股过户、DM 的换股经手、DL 的综合协议过户、DK 的基金印花、DJ 的基金证管费、DI 的大宗经手、DH 的佣金双计、DG 的北交所档、DF 的可交换现货经手、DE 的转债证管费、DD 的转债过户、DC 的转债印花、DB 的转债现货经手、DA 的二级过户、S 的股票经手、AX 的基金经手、U 的股票过户、V 的股票印花、AC 的北交所涨跌幅与盘后、O 的大宗、M 的股票盘后、CH/CL 的盘后可成交、CR 的行权成交、A 的板上容量、D 的成交时点解释；或 `dt0_primary_demo` 与 `invent_asof_leak_cb_lot_tick` 双挂；或 DT1 升格并列主报；或 `invent_100share_on_cb` / `invent_001_tick_on_cb` / `copy_fund_0001_tick_onto_cb_without_lot` / `vs_E_ashare_star_lot` / `vs_F_limit_round` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_R_etf_t0` / `vs_T_csrc_fee` / `missing_venue_or_sec_type_not_skip` 诊断桶升格主报；或把 T / E / F / Q / DS / DR / CQ / R 合成进 `dt0`；或实验字母 DT 与单字母 D/T 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成股票 0.01 元价位或可转债 0.001 元价位；或把 `params.Y` 的 0.02 读成证管费 0.02‰；或把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰；或把 params 字母读成假设-T；或把核对日规则写成已冻并铺满全历史；或缺 venue / 证券类别 / 官方整手价位规则仍不 skip；或把基金 0.001 升格进主报；或重开假设-T / 假设-E / 假设-F / 假设-Q / 假设-DS / 假设-DR / 假设-CQ / 假设-R；或标纸面齐；或写成 A/D–DT纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权申报价，对照 DT0/DT1/DT2。股票/科创整手走 E 或显式旁路，不在本页改 E。涨跌停取整走 F，回转涨跌幅收盘走 Q，转股印花走 DS，盘后定价走 DR，转股可成交走 CQ，股票 ETF 假 T+0 走 R，股票证管费走 T，都不改。报告整手价位误套截。不把 1000 元面额或 0.001 元价位标成已冻门槛，也不把 `params.G` 的 0.01 读成价位，也不把 `params.Y` 的 0.02 读成证管费。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_ashare_lot_tick_on_cb` / `invent_asof_leak_cb_lot_tick` / `invent_100share_on_cb` / `invent_001_tick_on_cb` / `copy_fund_0001_tick_onto_cb_without_lot` / `vs_E_ashare_star_lot` / `vs_F_limit_round` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_R_etf_t0` / `vs_T_csrc_fee` / `missing_venue_or_sec_type_not_skip`

`invent_100share_on_cb`、`invent_001_tick_on_cb`、`copy_fund_0001_tick_onto_cb_without_lot`、`vs_E_ashare_star_lot`、`vs_F_limit_round`、`vs_Q_cb_rules`、`vs_CQ_conversion_fill`、`vs_DS_conversion_stamp`、`vs_DR_aft_pricing`、`vs_R_etf_t0`、`vs_T_csrc_fee`、`missing_venue_or_sec_type_not_skip` 只作诊断桶：它们不是 `dt0`，也不是 DT1，**不得升格主报**。`vs_T_csrc_fee` 没有对应的「证管费 + 整手价位误套」合成主报。假设-T 只作诊断，**不得升格进 `dt0`**，**不重开假设-T**。`vs_R_etf_t0` 没有对应的「假 T+0 + 整手价位误套」合成主报。实验 R 只作诊断，**不得升格进 `dt0`**。E 的股票/科创整手只作诊断，**不得升格进 `dt0`**。F 的涨跌停取整只作诊断，**不得升格进 `dt0`**。Q 的回转涨跌幅收盘只作诊断，**不得升格进 `dt0`**。DS 的转股印花只作诊断，**不得升格进 `dt0`**。DR 的盘后通道只作诊断，**不得升格进 `dt0`**。CQ 的转股可成交只作诊断，**不得升格进 `dt0`**。只套 100 股、只套 0.01 元价位、只抄基金 0.001、缺字段仍不 skip，都只作诊断，**不得升格进 `dt0`**。`invent_asof_leak_cb_lot_tick` 只服务 DT1，**不得升格进 `dt0`，不得双挂**。`invent_ashare_lot_tick_on_cb` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「可转债按股票 100 股 / 0.01 元申报」拿去当诚实锚。
- 把 `params.G` 的 0.01 当成股票最小价位 0.01 元，或当成可转债最小价位 0.001 元。**尤重：`params.G` 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元**。
- 把 `params.Y` 的 0.02 当成证管费 0.02‰。**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**。**params 字母 ≠ 假设-T**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰。**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**。**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**。
- 缺 venue、证券类别或官方整手/价位规则仍不 skip，并用股票 100 股、0.01 元、基金 0.001 或占位 0.01 把可转债申报填上。
- 把核对日「1000 元面额、0.001 元」写成全历史唯一规则，并铺满全历史，或把股票 100 股/0.01 写成可转债唯一规则。锚六键已写死冻结。
- 把「股票整手已分列（E）/ 涨跌停取整已分列（F）/ 回转涨跌幅收盘已分列（Q）/ 转股印花已分列（DS）/ 盘后通道已分列（DR）/ 转股可成交已分列（CQ）/ 股票 ETF 回转已分列（R）/ 证管费已分列（T）」写成「可转债整手价位已诚实」。不改 E / F / Q / DS / DR / CQ / R / T。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格进 `dt0`。诊断桶 `vs_R_etf_t0` 只作对照。不抢、不重开假设-R。
- 把假设-T 的证管费和本页合成或混读后升格进 `dt0`。诊断桶 `vs_T_csrc_fee` 只作对照。**不重开假设-T**。
- 把 E 股票/科创整手和本页可转债 1000 元面额合成或混读后升格进 `dt0`。诊断桶 `vs_E_ashare_star_lot` / `invent_100share_on_cb` 只作对照。
- 把 F 涨跌停取整和本页最小价位误套合成或混读后升格进 `dt0`。诊断桶 `vs_F_limit_round` / `invent_001_tick_on_cb` 只作对照。
- 把 Q 转债回转/涨跌幅/收盘和本页整手价位合成或混读后升格进 `dt0`。诊断桶 `vs_Q_cb_rules` 只作对照。
- 把 DS 转股印花和本页申报约束合成或混读后升格进 `dt0`。诊断桶 `vs_DS_conversion_stamp` 只作对照。
- 把 DR 盘后定价通道和本页整手价位合成或混读后升格进 `dt0`。诊断桶 `vs_DR_aft_pricing` 只作对照。
- 把 CQ 转股可成交性和本页订单数量/价位闸门合成或混读后升格进 `dt0`。诊断桶 `vs_CQ_conversion_fill` 只作对照。
- 把基金 0.001 价位升格进主报。诊断桶 `copy_fund_0001_tick_onto_cb_without_lot` 只作对照。
- 缺 venue 或证券类别仍不 skip，并升格进 `dt0`。诊断桶 `missing_venue_or_sec_type_not_skip` 只作对照。
- `dt0_primary_demo` 与 `invent_asof_leak_cb_lot_tick` 双挂主报；DT1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DT 与单字母 D/T 或 params.Y/G/N 混读。**双字母 DT ≠ 单字母假设-D / 假设-T**。
- 改 T / E / F / Q / DS / DR / CQ / R / D / DQ / DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / U / V / AC / O / M / CH / CL / CR / BR / A 正文；重开假设-T；重开假设-E；重开假设-F；重开假设-Q；重开假设-DS；重开假设-DR；重开假设-CQ；重开假设-R；抢 A 真数队列；抢实验 R；标纸面齐；写成 A/D–DT纸面齐；开真数/回测/开户/实盘；用复权价当价位基准；结论写成「转债价位更细所以能买」。
- **纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK–DS；勿再只改清单）。**当前禁止标纸面齐**。**不写 A/D–DT纸面齐**。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权申报价、交易日、**交易所 venue**（沪/深）、**证券类别**（可转债 / 股票 / 基金或 ETF；仅用于把腿分回 E、F、Q、DS、DR、CQ、R、T 或本页）、**官方整手与最小价位规则是否在册**（缺则 skip，不发明沪市另档，也不拿股票 100 股/0.01 或基金 0.001 去填）。
- 申报数量的单位要能分清「股」和「元面额」。可转债按 1000 元面额整数倍，不是按 100 股。股票整手只消费 E，不在本页改 E。
- 最小价位：可转债建议方向是 0.001 元；股票默认 0.01 元留在 F 的取整口径旁边作对照，不把 F 的涨跌停取整收进本页主报。
- 基金/ETF 最小价位 0.001 元只作对照。数字和可转债价位相同，仍禁止把基金档升格进 `dt0`。
- 没有 venue、证券类别或官方整手/价位规则时，按写死冻结的 `cb_lot_tick_over_policy=skip_if_venue_or_sec_type_or_official_rule_missing` skip，不得按股票 100 股、0.01 元、基金 0.001 或占位 0.01 把可转债申报填上。
- 旁路消费：E 的股票/科创整手、F 的涨跌停取整、Q 的回转涨跌幅收盘、DS 的转股印花、DR 的盘后定价、CQ 的转股可成交、R 的股票 ETF 假 T+0、T 的股票证管费、D 的成交时点之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** 这些页的主报不收到本页 `dt0`。
- 未复权申报价；asof **写死冻结** `2026-10-26`。核对日方向「可转债 1000 元面额整数倍、最小价位 0.001 元、禁止套股票 100 股/0.01、基金 0.001 仅对照」是写死冻结的机制方向，不是已冻的全历史规则，也不是占位门槛。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-26`；`fail_policy=skip`；`cb_lot_tick_honest=pit_cb_lot_1000_par_tick_0_001_not_ashare_100_0_01`（缺 venue/证券类别或官方整手/价位规则则 skip；可转债申报=1000 元面额整数倍、最小价位 0.001 元；禁止套股票 100 股/0.01；基金 0.001 价位仅对照、禁止把基金档升格进主报）；`cb_lot_tick_scope=cb_order_lot_tick_vs_ashare_and_fund`（可转债申报整手/价位与股票、基金分列；方向名，不是已冻规则）；`cb_lot_tick_over_policy=skip_if_venue_or_sec_type_or_official_rule_missing`（缺 venue/证券类别或官方整手/价位规则则 skip）；`dt0_primary_demo=invent_ashare_lot_tick_on_cb`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_cb_lot_tick` 双挂；DT1 不升格；诊断桶不升格主报；**禁把 T / E / F / Q / DS / DR / CQ / R 合成进 `dt0`**，只作对照/旁路，不得升格进 `dt0` 或另挂主报；**禁把 T/E/F/Q/DS/DR/CQ/R 混读升格进 `dt0`**）；`ashare_lot_handoff=e_page`；`limit_round_handoff=f_page`；`cb_rules_handoff=q_page`；`cb_conversion_fill_handoff=cq_page`；`cb_conversion_stamp_handoff=ds_page`；`aft_pricing_handoff=dr_page`；`etf_t0_handoff=r_page`；`csrc_fee_handoff=t_page`；`merge_with_DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/BR/A/D=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是整手、不是价位、不是证管费：整手价位误套截 ΔCbLotTick / 净差异 / DT1−DT2；**尤重 params.G 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元（量纲与语义不同）**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**；**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**；**params.Y/G/N ≠ 实验字母 DT ≠ 单字母 D/T**；**params 字母 ≠ 假设-T**；**勿把 params.Y 读成假设-T，亦勿把 params.G 读成实验字母 DT，亦勿把单字母假设-D / 假设-T 读成双字母 DT**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #130。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`797e855b`（A/D–DS纸面齐已合，全长 `797e855b5bb0a788e0339103de42cd27b9231c42`）；三冻补丁基 tip=`fc7a4336` / `fc7a43365516cbb79e744dc79266a69234711c59`；分支起点 HEAD=`a25ecd10` / `a25ecd10f7f6d8433f82a378a272a5649159fa58`。**不改已冻 A–DQ / DA–DS**。状态=**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DT纸面齐**。

---

## 8. 结论

（空；**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DT纸面齐**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-30）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DT-20261110.md`（原样落入，不改结论；SHA256=`746c841921e693e69474dc4f095b02823ce77b91233bfff5ac196754ce3d720a`；预检 2026-11-10；**结论：有条件通过**；tip基=`fc7a4336` / `fc7a43365516cbb79e744dc79266a69234711c59`；本补丁分支起点 HEAD=`a25ecd10` / `a25ecd10f7f6d8433f82a378a272a5649159fa58`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于整手价位误套截 ΔCbLotTick、净差异、DT1−DT2 专项。**`params.Y` ≠ 实验字母 DT**；**`params.G` ≠ 实验字母 DT**；**`params.N` ≠ 实验字母 DT**；亦 ≠ 单字母假设-D / 假设-T。**勿把 `params.Y` 读成假设-T，亦勿把 `params.G` 读成实验字母 DT，亦勿把单字母假设-D / 假设-T 读成双字母 DT**。**尤重：`params.G` 的 `0.01` ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元**（**params.G 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元**）。三者量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是股票 0.01 元价位，也不是可转债 0.001 元价位。**尤重：`params.Y` 的 `0.02` ≠ 证管费 0.02‰**（**params.Y 的 0.02 ≠ 证管费 0.02‰**）。**params 字母 ≠ 假设-T**。**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**。**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**。禁止互读、禁止把门槛改写成整手、价位或证管费。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dt0_primary_demo`**：**写死冻结** **`invent_ashare_lot_tick_on_cb`**（单一主报，单挂写死）。**禁止**与半泄露键 **`invent_asof_leak_cb_lot_tick`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DT1 仅核对日把「可转债 1000 元面额整数倍、最小价位 0.001 元」铺到全历史、铺到股票腿、铺到基金腿，或把基金 0.001 写成可转债唯一价位只作半泄露对照，**不得升格与 dt0 并列主报**，也不得把 `invent_asof_leak_cb_lot_tick` 写进 `dt0`。`invent_100share_on_cb` / `invent_001_tick_on_cb` / `copy_fund_0001_tick_onto_cb_without_lot` / `vs_E_ashare_star_lot` / `vs_F_limit_round` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_R_etf_t0` / `vs_T_csrc_fee` / `missing_venue_or_sec_type_not_skip` **只作诊断桶，不得升格主报**。DT1 / 诊断桶 **不升格**。**禁把以下升格进 dt0**：E股票整手 / F涨跌停取整 / Q转债规则 / CQ转股可成交 / DS转股印花 / DR盘后定价 / T证管费切日 / R假T+0。这些只作对照/旁路，**不得升格进 `dt0`，不得另挂主报**。**不重开假设-T**；**不重开假设-R**；**不重开假设-Q**；**不重开假设-E**；**不重开假设-F**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-CQ**。**不抢实验 R**。

3. **可转债整手价位诚实锚六键升格写死（不可再写「建议」）**：`params.cb_lot_tick_honest=pit_cb_lot_1000_par_tick_0_001_not_ashare_100_0_01`；`params.cb_lot_tick_scope=cb_order_lot_tick_vs_ashare_and_fund`；`params.cb_lot_tick_over_policy=skip_if_venue_or_sec_type_or_official_rule_missing`；`params.asof_check_date=2026-10-26`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺 venue/证券类别或官方整手/价位规则 → skip；可转债申报=1000 元面额整数倍、最小价位 0.001 元；禁止套股票 100 股/0.01；基金 0.001 价位仅对照、禁止把基金档升格进主报。禁止把核对日 1000 元面额或 0.001 元价位铺满全历史。禁止跑后改锚，或用股票 100 股/0.01 / 核对日规则铺满 / 只抄基金 0.001 / 缺 venue/证券类别或官方规则仍硬填 / 把 E/F/Q/CQ/DS/DR/T/R 升格进 dt0 冒充诚实 PIT。**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**。**禁把 params.G 的 0.01 读成股票 0.01 元价位或可转债 0.001 元价位**。**禁把 params.Y 的 0.02 读成证管费 0.02‰**。**不重开假设-T**；**不重开假设-R**；**不重开假设-Q**；**不重开假设-E**；**不重开假设-F**。**不抢实验 R**。

**硬分列保住**：DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠BR≠A≠D；**双字母 DT ≠ 单字母假设-D / 假设-T**；**双字母 DT ≠ 单字母 D/T**；**params.Y / params.G / params.N ≠ 实验字母 DT ≠ 单字母 D/T**；**params 字母 ≠ 假设-T**；**尤重 params.G 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**；**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**；**可转债整手价位误套股票 ≠ E股票整手 ≠ F涨跌停取整 ≠ Q转债规则 ≠ CQ转股可成交 ≠ DS转股印花 ≠ DR盘后定价 ≠ T证管费切日 ≠ R假T+0**；不抢 A；不抢实验 R；不改已齐/已冻 DA～DS 及 A–DQ 正文；**不重开假设-T**；**不重开假设-R**；**不重开假设-Q**；**不重开假设-E**；**不重开假设-F**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-CQ**；**禁把 E股票整手 / F涨跌停取整 / Q转债规则 / CQ转股可成交 / DS转股印花 / DR盘后定价 / T证管费切日 / R假T+0 合成/混读升格进 dt0**。handoff 保持：`ashare_lot_handoff=e_page`；`limit_round_handoff=f_page`；`cb_rules_handoff=q_page`；`cb_conversion_fill_handoff=cq_page`；`cb_conversion_stamp_handoff=ds_page`；`aft_pricing_handoff=dr_page`；`etf_t0_handoff=r_page`；`csrc_fee_handoff=t_page`；`merge_with_*=False`。

**状态**：**预检有条件通过·三条已冻·待复检**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DT纸面齐**；本页不开回测/真数/开户/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-30 | 风控预检补丁·冻结三条写死——依据 `预检-假设DT-20261110.md`（SHA256=`746c841921e693e69474dc4f095b02823ce77b91233bfff5ac196754ce3d720a`；结论=有条件通过；tip基=`fc7a4336` / `fc7a43365516cbb79e744dc79266a69234711c59`；分支起点 HEAD=`a25ecd10` / `a25ecd10f7f6d8433f82a378a272a5649159fa58`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖整手价位误套截 ΔCbLotTick / 净差异 / DT1−DT2；**params.Y/G/N ≠ 实验字母 DT ≠ 单字母 D/T**；**勿把 params.Y 读成假设-T，亦勿把 params.G 读成实验字母 DT，亦勿把单字母假设-D / 假设-T 读成双字母 DT**；**params 字母 ≠ 假设-T**；**尤重 params.G 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元（量纲与语义不同）**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**；**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成整手/价位/证管费）；② `params.dt0_primary_demo=invent_ashare_lot_tick_on_cb`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_cb_lot_tick` 双挂；DT1 不升格；诊断桶 `invent_100share_on_cb` / `invent_001_tick_on_cb` / `copy_fund_0001_tick_onto_cb_without_lot` / `vs_E_ashare_star_lot` / `vs_F_limit_round` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_R_etf_t0` / `vs_T_csrc_fee` / `missing_venue_or_sec_type_not_skip` 不升格；**禁把 E股票整手 / F涨跌停取整 / Q转债规则 / CQ转股可成交 / DS转股印花 / DR盘后定价 / T证管费切日 / R假T+0 合成/混读升格进 dt0**，只作对照/旁路，不得升格进 dt0 或另挂主报；不重开假设-T；不重开假设-E；不重开假设-F；不重开假设-Q；不重开假设-DS；不重开假设-DR；不重开假设-CQ；不重开假设-R；不抢实验 R）；③ 锚六键写死 `cb_lot_tick_honest=pit_cb_lot_1000_par_tick_0_001_not_ashare_100_0_01` / `cb_lot_tick_scope=cb_order_lot_tick_vs_ashare_and_fund` / `cb_lot_tick_over_policy=skip_if_venue_or_sec_type_or_official_rule_missing` / `asof_check_date=2026-10-26` / `fill_time=next_open` / `fail_policy=skip`（缺 venue/证券类别或官方整手/价位规则 → skip；可转债申报=1000 元面额整数倍、最小价位 0.001 元；禁止套股票 100 股/0.01；基金 0.001 价位仅对照、禁止把基金档升格进主报）。handoff 保持 `ashare_lot_handoff=e_page` / `limit_round_handoff=f_page` / `cb_rules_handoff=q_page` / `cb_conversion_fill_handoff=cq_page` / `cb_conversion_stamp_handoff=ds_page` / `aft_pricing_handoff=dr_page` / `etf_t0_handoff=r_page` / `csrc_fee_handoff=t_page`；`merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DT纸面齐**；不改已齐/已冻 DA～DS 及 A–DQ；不改假设-DA～假设-DS；不改 #110–#128；不重开假设-T；不重开假设-E；不重开假设-F；不重开假设-Q；不重开假设-DS；不重开假设-DR；不重开假设-CQ；不重开假设-R；不抢实验 R；不预留 #130；不开回测/真数/开户/实盘。基于 tip=`fc7a4336`。 |
| 2026-11-30 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。可转债整手价位误套股票（成交规则）；`dt0_primary_demo` 建议 `invent_ashare_lot_tick_on_cb`，单一主报，单挂，禁与 `invent_asof_leak_cb_lot_tick` 双挂，DT1 不升格；诊断桶 `invent_100share_on_cb` / `invent_001_tick_on_cb` / `copy_fund_0001_tick_onto_cb_without_lot` / `vs_E_ashare_star_lot` / `vs_F_limit_round` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_R_etf_t0` / `vs_T_csrc_fee` / `missing_venue_or_sec_type_not_skip` 不升格；**尤重不重开假设-T，禁把 vs_T_csrc_fee / 证管费升格进 dt0**；**尤重实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 dt0**；**尤重 E 股票/科创整手 ≠ 本页可转债 1000 元面额，禁止合成进 dt0**；**尤重 F 涨跌停取整 ≠ 本页最小价位误套，禁止合成进 dt0**；**尤重 Q 转债回转/涨跌幅/收盘 ≠ 本页整手价位，禁止合成进 dt0**；**尤重 DS 转股印花 ≠ 本页申报约束，禁止合成进 dt0**；**尤重 DR 盘后定价通道 ≠ 本页整手价位，禁止合成进 dt0**；**尤重 CQ 转股可成交性 ≠ 本页订单数量/价位闸门，禁止合成进 dt0**；**双字母 DT ≠ 单字母假设-D / 假设-T**；**params 字母 ≠ 假设-T**；**禁把 T/E/F/Q/DS/DR/CQ/R 混读升格进 dt0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DT ≠ 单字母 D/T**，且 **params.G 的 0.01 ≠ 股票最小价位 0.01 元 ≠ 可转债最小价位 0.001 元**，**params.Y 的 0.02 ≠ 证管费 0.02‰**，**禁把占位读成 1000 元面额 / 0.001 元价位 / 证管费 0.02‰**，**params 相对门槛 ≠ 整手 ≠ 价位 ≠ 证管费**；锚建议·待冻、未冻：`cb_lot_tick_honest=pit_cb_lot_1000_par_tick_0_001_not_ashare_100_0_01` / scope=`cb_order_lot_tick_vs_ashare_and_fund` / over_policy=`skip_if_venue_or_sec_type_or_official_rule_missing` / `asof_check_date=2026-10-26` / `fill_time=next_open` / `fail_policy=skip`；口径：缺 venue/证券类别或官方整手/价位规则则 skip；可转债申报=1000 元面额整数倍、最小价位 0.001 元；禁止套股票 100 股/0.01；基金 0.001 价位仅对照、禁止把基金档升格进主报（**草稿方向，尚未冻，不要写成已冻**）；handoff：`ashare_lot_handoff=e_page`，`limit_round_handoff=f_page`，`cb_rules_handoff=q_page`，`cb_conversion_fill_handoff=cq_page`，`cb_conversion_stamp_handoff=ds_page`，`aft_pricing_handoff=dr_page`，`etf_t0_handoff=r_page`，`csrc_fee_handoff=t_page`；`merge_with_DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/BR/A/D=False`；**DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠BR≠A≠D**；**双字母 DT ≠ 单字母 D/T**；**未标纸面齐**；**不写 A/D–DT纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–DS；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–DS；不改已齐假设-DA～假设-DS；不改 #110–#128；不重开假设-T；不重开假设-E；不重开假设-F；不重开假设-Q；不重开假设-DS；不重开假设-DR；不重开假设-CQ；不重开假设-R；不写下一字母；不预留 #130；不开真数/回测/开户/实盘。基 tip=`797e855b`（A/D–DS纸面齐已合，全长 `797e855b5bb0a788e0339103de42cd27b9231c42`；不改该 tip 上的 #110–#128，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
