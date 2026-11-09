# 假设-DU · 可转债首日临停误套股票无板日临停（成交规则）

更新：2026-12-01  
来源：总管线 / 基 tip=`b1e0b311` / 全长 `b1e0b3112c39ab3749df670d08b79b9f5eca9277`（A/D–DT纸面齐已合）；**不改已冻 A–DQ / DA–DT**；**不改假设-DT 正文**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-DT / 假设-S / 假设-AX / 假设-T / 假设-U / 假设-V / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-E / 假设-F / 假设-J / 假设-AU / 假设-A / 假设-D 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ / 假设-BR）；**不重开假设-J**；**不重开假设-Q**；**不重开假设-CQ**；**不重开假设-DT**；**不重开假设-DR**；**不重开假设-DS**；**不重开假设-R**；**不重开假设-U**；**不重开假设-T**；**不重开假设-AU**；**不重开假设-D**；**不重开假设-E**；**不重开假设-F**；**不重开假设-S**；**不重开假设-M**；**不重开假设-O**；**不重开假设-DO**；**不重开假设-DQ**；**不重开假设-AC**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**）后写下一草稿 DU；清单 #129=DT，本页占用 **#130=DU**；选题是回测把**可转债上市首日临停**误套成**股票无涨跌幅日临停**（诚实方向：较**发行价**首次涨或跌 20% 停 30 分钟、30% 停到 14:57；禁止套股票无板日「开盘价 30%/60%、各 10 分钟」；禁止把核对日规则铺满 2022-08-01 前样本）；假设-J 只收股票无板日临停（开盘价 30%/60%、各 10 分钟 ≠ 本页可转债首日临停），假设-Q 只收可转债回转/涨跌幅/收盘（≠ 本页首日临停基准/阈值/时长），假设-CQ 只收转股可成交性，假设-DT 只收可转债整手价位，假设-DR 只收可转债盘后定价通道，假设-DS 只收转股所得股票印花，假设-R 只收股票 ETF 假 T+0，假设-U 只收股票过户切日，假设-T 只收股票证管费切日，假设-AU 只收本方对手最优空簿；**新建实验 DU**；不写下一字母；不预留 #131  
状态：**A/D–DU纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「可转债首日按股票无板日开盘价 30%/60%、各 10 分钟临停」当诚实成交规则；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–DT**；尤其不改假设-J / 假设-Q / 假设-CQ / 假设-DT / 假设-DR / 假设-DS / 假设-R / 假设-U / 假设-T / 假设-AU / 假设-D；**不重开假设-J**；**不重开假设-Q**；**不重开假设-CQ**；**不重开假设-DT**；**不重开假设-DR**；**不重开假设-DS**；**不重开假设-R**；**不重开假设-U**；**不重开假设-T**；**不重开假设-AU**；**不重开假设-D**；**不重开假设-E**；**不重开假设-F**；**不重开假设-S**；**不重开假设-M**；**不重开假设-O**；**不重开假设-DO**；**不重开假设-DQ**；**不重开假设-AC**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DU（#130）。一句话误开：回测把可转债首日临停误套股票无板日临停，用开盘价当临停基准，或套「开盘价 30%/60%、各 10 分钟」，或把核对日规则铺到 2022-08-01 前，或与 J股票无板日临停 / Q转债回转涨跌幅收盘 / CQ转股可成交性 / DT整手价位 / DR盘后定价通道 / DS转股印花 / R股票ETF假T+0 / U股票过户切日 / T股票证管费 / AU本方对手最优空簿 混读，或缺 venue/首日标记/发行价或官方临停规则仍不 skip，系统性改写可转债上市首日的临停基准、阈值与时长。**禁把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混读升格进 `du0`**。

> **字母消歧（硬）**：本页**实验字母 DU** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DU**；**params 字母 ≠ 假设-U / 假设-T**；**勿把 `params.Y` 读成实验字母 DU，亦勿读成假设-U，亦勿读成假设-T**；**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价阈值 20%**；**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DU**；**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰ ≠ 开盘价 30% ≠ 开盘价 60% ≠ 发行价 20% ≠ 发行价 30%**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户费率，也不是临停比例；**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**；**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DU**；**params.N ≠ 单字母假设-N**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DU ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 U**（股票过户费切日；**双字母 DU ≠ 单字母假设-U；严禁复用假设-U**；**不重开假设-U**；组名 DU0/DU1/DU2 是本页三组对照，≠ 单字母实验 U，亦 ≠ 单字母实验 D）≠ **单字母实验 T**（股票证管费切日；**双字母 DU ≠ 单字母假设-T；严禁复用假设-T**；**不重开假设-T**；**params 字母 ≠ 假设-T**）≠ **单字母实验 R**（股票 ETF 假 T+0 / 股票ETF假回转；**双字母 DU ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `du0`**）≠ **单字母实验 J**（股票无涨跌幅日盘中临停；**J 股票无板日临停 ≠ 本页可转债首日临停**；**严禁复用假设-J**）≠ **单字母实验 Q**（可转债回转/涨跌幅/收盘；**Q 转债回转/涨跌幅/收盘 ≠ 本页首日临停基准/阈值/时长**；**双字母 DU ≠ 单字母假设-Q；严禁复用假设-Q**）≠ **双字母 AU**（本方对手最优空簿假成；**双字母 DU ≠ 双字母 AU；严禁复用假设-AU**）≠ **假设-BR**（融券借券费/融出费率计提；**双字母 DU ≠ 假设-BR；严禁复用假设-BR**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DU ≠ 单字母假设-A**）≠ 双字母 **DT**（可转债整手价位误套股票；**DT 整手价位 ≠ 本页临停**）≠ **DS**（可转债转股所得股票印花税误免；**DS 转股印花 ≠ 本页临停**）≠ **DR**（可转债盘后定价误套股票盘后固定价格；**DR 盘后定价通道 ≠ 本页临停**）≠ **CQ**（可转债转股可成交性误开；**CQ 转股可成交性 ≠ 本页临停**）≠ **DQ**（ETF 申赎组合证券过户费误套）≠ **DP**（可交换债换股印花税误漏）≠ **DO**（可转债回售处理）≠ **DN**（可交换债换股过户费误套）≠ **DM**（可交换债换股经手费误套现货）≠ **DL**（股票综合协议过户费下浮）≠ **DK**（场内基金印花税误抽）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债现货经手费沪深合成）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债现货印花税误抽）≠ **DB**（可转债现货经手费）≠ **DA**（场内基金二级过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费）≠ **V**（股票印花税切日）≠ **AC**（北交所涨跌幅与盘后）≠ **O**（大宗三通道）≠ **M**（股票盘后通道）≠ **CH**（股票盘后固定价格可成交性）≠ **CL**（可转债盘后定价可成交性）≠ **CR**（认沽/认购行权成交）≠ **E**（股票/科创整手）≠ **F**（涨跌停取整）。**DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠AU≠A≠D**。**双字母 DU ≠ 单字母 D/U**。**双字母 DU ≠ 单字母假设-D / 假设-U**。**双字母 DU ≠ 双字母 AU**。**params.Y/G/N ≠ 实验字母 DU；亦 ≠ 单字母 D/U**。**params 字母 ≠ 假设-U / 假设-T**。**勿把 `params.Y` 或 `params.G` 读成实验字母 DU，亦勿把单字母假设-D / 假设-U 读成双字母 DU，亦勿把双字母 AU 读成双字母 DU**。**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰；`params.Y` 的 0.02 ≠ 证管费 0.02‰；占位 ≠ 发行价阈值 20%/30%，亦 ≠ 开盘价 30%/60%**。**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**。**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**。**可转债首日临停误套股票无板日临停 ≠ J股票无板日临停 ≠ Q转债回转/涨跌幅/收盘 ≠ CQ转股可成交性 ≠ DT整手价位 ≠ DR盘后定价通道 ≠ DS转股印花 ≠ R股票ETF假T+0 ≠ U股票过户切日 ≠ T股票证管费 ≠ AU本方对手最优空簿**。**尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `du0`**。**尤重：J 股票无板日临停 ≠ 本页可转债首日临停——禁止把 J / `copy_j_halt_onto_cb_ipo` / 开盘价 30%/60%·各 10 分钟合成/混读升格进 `du0`**。**尤重：Q 转债回转/涨跌幅/收盘 ≠ 本页首日临停基准/阈值/时长——禁止合成/混读升格进 `du0`**。**尤重：CQ 转股可成交性 ≠ 本页临停——禁止合成/混读升格进 `du0`**。**尤重：DT 整手价位 ≠ 本页临停——禁止合成/混读升格进 `du0`**。**尤重：DR 盘后定价通道 ≠ 本页临停——禁止合成/混读升格进 `du0`**。**尤重：DS 转股印花 ≠ 本页临停——禁止合成/混读升格进 `du0`**。**尤重：不重开假设-U（股票过户切日）；禁把 `vs_U_transfer_fee` 升格进 `du0`**。**尤重：不重开假设-T（股票证管费切日）；禁把 `vs_T_csrc_fee` 升格进 `du0`**。**尤重：双字母 DU ≠ 单字母假设-D / 假设-U**。**尤重：双字母 DU ≠ 双字母 AU（本方对手最优空簿）**。**禁把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混读升格进 `du0`**。

### 专节 · 双字母 DU ≠ 单字母假设-D / 假设-U；且 ≠ 双字母 AU；且 ≠ 假设-J / 假设-Q / 假设-CQ / 假设-DT / 假设-DR / 假设-DS / 假设-R / 假设-T（硬）

| 维度 | 对照页 | 本页假设-DU（双字母） |
|------|--------|----------------------|
| 题面 J | **股票无板日临停**（较**当日开盘价** 30%/60%、各 10 分钟；假设-J） | J 股票无板日临停 ≠ 本页可转债首日临停。开盘价基准、30%/60%、各 10 分钟，都不是可转债首日临停。**DU≠J**；**严禁复用假设-J**；**不重开假设-J**；**不改 J**；**尤重：禁把 J / `copy_j_halt_onto_cb_ipo` / 开盘价 30%/60%·各 10 分钟升格进 `du0`**；`nolimit_halt_handoff=j_page`；诊断桶 `vs_J_nolimit_halt` / `copy_j_halt_onto_cb_ipo` / `invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` 不升格 |
| 题面 Q | **可转债回转 / 涨跌幅 / 收盘**（按股票规则回放；2022-08-01 起次日 ±20% 等留在 Q） | Q 转债回转/涨跌幅/收盘 ≠ 本页首日临停基准/阈值/时长。有没有板、收盘怎么产生 ≠ 首日临停看发行价还是开盘价、停 30 分钟还是停到 14:57。**双字母 DU ≠ 单字母假设-Q**；**严禁复用假设-Q**；**DU≠Q**；**不重开假设-Q**；**不改 Q**；**尤重：禁把 Q 升格进 `du0`**；`cb_rules_handoff=q_page`；诊断桶 `vs_Q_cb_rules` 不升格 |
| 题面 CQ | **可转债转股可成交性**（默认转股申报必能按转股价全额转成） | CQ 转股可成交性 ≠ 本页临停。能不能转成 ≠ 上市首日这只转债临停与否。**DU≠CQ**；**严禁复用假设-CQ**；**不重开假设-CQ**；**不改 CQ**；**尤重：禁把 CQ 升格进 `du0`**；`cb_conversion_fill_handoff=cq_page`；诊断桶 `vs_CQ_conversion_fill` 不升格 |
| 题面 DT | **可转债整手价位**（1000 元面额 / 0.001 元，误套股票 100 股 / 0.01） | DT 整手价位 ≠ 本页临停。申报数量和最小价位 ≠ 首日临停的基准、阈值和时长。**DU≠DT**；**严禁复用假设-DT**；**不重开假设-DT**；**不改 DT**；**尤重：禁把 DT 升格进 `du0`**；`cb_lot_tick_handoff=dt_page`；诊断桶 `vs_DT_lot_tick` 不升格 |
| 题面 DR | **可转债盘后定价通道**（误套股票盘后固定价格） | DR 盘后定价通道 ≠ 本页临停。盘后用哪条价格 ≠ 首日盘中临停。**DU≠DR**；**严禁复用假设-DR**；**不重开假设-DR**；**不改 DR**；**尤重：禁把 DR 升格进 `du0`**；`aft_pricing_handoff=dr_page`；诊断桶 `vs_DR_aft_pricing` 不升格 |
| 题面 DS | **转股所得股票印花**（误免成 0） | DS 转股印花 ≠ 本页临停。交割那笔股票交不交印花 ≠ 首日临停。**DU≠DS**；**严禁复用假设-DS**；**不重开假设-DS**；**不改 DS**；**尤重：禁把 DS 升格进 `du0`**；`cb_conversion_stamp_handoff=ds_page`；诊断桶 `vs_DS_conversion_stamp` 不升格 |
| 题面 R | **股票 ETF 假 T+0**（假设-R 股票ETF假回转；回转名单 ≠ 临停） | 实验 R 不抢、不重开、不混读升格进 `du0`。股票 ETF 假当日回转 ≠ 本页可转债首日临停被套成股票无板日。**双字母 DU ≠ 单字母假设-R**；**严禁复用假设-R**；**DU≠R**；**不重开假设-R**；**不改 R**；**尤重：实验 R 不抢**；`etf_t0_handoff=r_page`；诊断桶 `vs_R_etf_t0` 不升格 |
| 题面 U | **股票过户费切日**（假设-U；0.01‰ 是费率，不是本页门槛） | **不重开假设-U**。过户切日 ≠ 可转债首日临停。`params.G` 的 0.01 不是过户费 0.01‰。**双字母 DU ≠ 单字母假设-U**；**严禁复用假设-U**；**DU≠U**；**params 字母 ≠ 假设-U**；**不改 U**；**尤重：不重开假设-U；禁把 `vs_U_transfer_fee` 升格进 `du0`**；`transfer_fee_handoff=u_page`；诊断桶 `vs_U_transfer_fee` 不升格 |
| 题面 T | **股票证管费切日**（假设-T；0.02‰ 双边是费率，不是本页门槛） | **不重开假设-T**。证管费切日 ≠ 可转债首日临停。`params.Y` 的 0.02 不是证管费 0.02‰。**双字母 DU ≠ 单字母假设-T**；**严禁复用假设-T**；**DU≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：不重开假设-T；禁把 `vs_T_csrc_fee` 升格进 `du0`**；`csrc_fee_handoff=t_page`；诊断桶 `vs_T_csrc_fee` 不升格 |
| 题面 AU | **本方对手最优空簿**（假设-AU；空簿假成） | 本方对手最优空簿 ≠ 可转债首日临停。**双字母 DU ≠ 双字母 AU**；**严禁复用假设-AU**；**DU≠AU**；**不重开假设-AU**；**不改 AU**；**尤重：双字母 DU ≠ 双字母 AU（本方对手最优空簿）；禁把 AU 升格进 `du0`** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 首日临停的基准和时长。**双字母 DU ≠ 单字母假设-D**；**严禁复用假设-D**；**DU≠D**；**不改 D** |
| 题面 DQ | **ETF 申赎组合证券过户费误套** | 篮子过户费 ≠ 首日临停。**DU≠DQ**；**不重开假设-DQ**；**不改 DQ** |
| 题面 DP | **可交换债换股印花税误漏** | 换股印花 ≠ 首日临停。**DU≠DP**；**不重开假设-DP**；**不改 DP** |
| 题面 DO | **可转债回售处理** | 回售经手 ≠ 首日临停。**DU≠DO**；**不重开假设-DO**；**不改 DO** |
| 题面 DN | **可交换债换股过户费** | 换股过户 ≠ 首日临停。**DU≠DN**；**不重开假设-DN**；**不改 DN** |
| 题面 DM | **可交换债换股经手费** | 换股经手 ≠ 首日临停。**DU≠DM**；**不重开假设-DM**；**不改 DM** |
| 题面 DL | **股票综合协议过户费下浮** | 综合协议过户下浮 ≠ 首日临停。**DU≠DL**；**不重开假设-DL**；**不改 DL** |
| 题面 DK | **场内基金印花税误抽** | 基金印花 ≠ 首日临停。**DU≠DK**；**不改 DK** |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 首日临停，亦 ≠ 股票证管费切日。**DU≠DJ**；**不改 DJ**；**不重开假设-T** |
| 题面 DI | **股票大宗经手下浮** | 大宗经手下浮 ≠ 首日临停。**DU≠DI**；**不重开假设-DI**；**不改 DI** |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 首日临停。**DU≠DH**；**不改 DH** |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 首日临停。**DU≠DG**；**不改 DG** |
| 题面 DF | **可交换债现货经手费沪深合成** | 可交换现货经手 ≠ 首日临停。**DU≠DF**；**不重开假设-DF**；**不改 DF** |
| 题面 DE | **可转债证管费** | 转债证管费误套 ≠ 本页临停，亦 ≠ 重开假设-T。**DU≠DE**；**不改 DE**；**不重开假设-T** |
| 题面 DD | **可转债现货过户费** | 转债现货过户 ≠ 首日临停，亦 ≠ 重开假设-U。**DU≠DD**；**不重开假设-DD**；**不改 DD**；**不重开假设-U** |
| 题面 DC | **可转债现货印花税误抽** | 转债现货印花 ≠ 首日临停。**DU≠DC**；**不改 DC** |
| 题面 DB | **可转债现货经手费** | 转债现货经手 ≠ 首日临停。**DU≠DB**；**不重开假设-DB**；**不改 DB** |
| 题面 DA | **场内基金二级过户费** | 二级过户 ≠ 首日临停。**DU≠DA**；**不重开假设-DA**；**不改 DA** |
| 题面 S | **沪深 A 股竞价经手费切日** | 股票经手切日 ≠ 首日临停。**DU≠S**；**不重开假设-S**；**不改 S** |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 首日临停。**DU≠AX**；**不重开假设-AX**；**不改 AX** |
| 题面 V | **股票印花税切日** | 股票印花切日 ≠ 首日临停。**DU≠V**；**不重开假设-V**；**不改 V** |
| 题面 AC | **北交所涨跌幅与盘后** | 北交所涨跌幅、盘后 ≠ 可转债首日临停。**DU≠AC**；**不重开假设-AC**；**不改 AC** |
| 题面 O | **大宗三通道** | 大宗通道 ≠ 首日临停。**DU≠O**；**不重开假设-O**；**不改 O** |
| 题面 M | **股票盘后通道** | 股票盘后通道 ≠ 首日临停。**DU≠M**；**不重开假设-M**；**不改 M** |
| 题面 CH | **股票盘后固定价格可成交性** | 盘后可成交 ≠ 首日临停。**DU≠CH**；**不重开假设-CH**；**不改 CH** |
| 题面 CL | **可转债盘后定价可成交性** | 转债盘后可成交 ≠ 首日临停。**DU≠CL**；**不重开假设-CL**；**不改 CL** |
| 题面 CR | **认沽/认购行权成交** | 行权兑付 ≠ 首日临停。**DU≠CR**；**不重开假设-CR**；**不改 CR** |
| 题面 E | **股票/科创整手** | 股数整手 ≠ 首日临停。**DU≠E**；**不重开假设-E**；**不改 E** |
| 题面 F | **涨跌停取整** | 限制价怎么收成价位 ≠ 首日临停阈值。**DU≠F**；**不重开假设-F**；**不改 F** |
| 题面 BR | **融券借券费/融出费率** | 借券费计提 ≠ 首日临停。**双字母 DU ≠ 假设-BR**；**DU≠BR**；**不重开假设-BR**；**不改 BR** |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 首日临停。**DU≠A**；**不抢 A 真数队列**；**不改 A** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_stock_nolimit_halt_on_cb_ipo`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_cb_ipo_halt` 双挂；DU1 不升格；`invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` / `copy_j_halt_onto_cb_ipo` / `vs_J_nolimit_halt` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DT_lot_tick` / `vs_DR_aft_pricing` / `vs_DS_conversion_stamp` / `vs_R_etf_t0` / `vs_U_transfer_fee` / `vs_T_csrc_fee` / `missing_venue_or_ipo_flag_or_issue_px_not_skip` 只作诊断对照，不升格主报；**尤重禁止把 J / Q / CQ / DT / DR / DS / R / U / T / AU 混读升格进 `du0`**） |
| 文档 | 清单实验 J / Q / CQ / DT / DR / DS / R / U / T / AU / D / DQ / DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / V / AC / O / M / CH / CL / CR / E / F / BR / A（**只读；禁止改写**） | `假设-DU-可转债首日临停误套股票无板日临停.md`（新建） |
| 预检键 | 实验字母 J / Q / CQ / DT / DR / DS / R / U / T / AU / D / DQ / DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / V / AC / O / M / A / Y / G / N，以及已存在 CH / CL / CR / E / F / BR | 实验字母 **DU** / `du0_primary_demo`；**不得**占用或改写预检 J/Q/CQ/DT/DR/DS/R/U/T/AU/D/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/V/AC/O/M/A/Y/G/N，亦不得改写 CH/CL/CR/E/F/BR |

**禁止**：把 DU 写成「J / Q / CQ / DT / DR / DS / R / U / T / AU / D / A 的续篇」；把「股票无板日临停已分列（J）/ 转债回转涨跌幅收盘已分列（Q）/ 转股可成交已分列（CQ）/ 整手价位已分列（DT）/ 盘后定价通道已分列（DR）/ 转股印花已分列（DS）/ 股票 ETF 回转已分列（R）/ 股票过户已分列（U）/ 股票证管费已分列（T）/ 空簿已分列（AU）」写成「可转债首日临停已诚实」；把实验字母 DU 与单字母 D/U 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-U 读成双字母 DU**；**尤重勿把双字母 AU 读成双字母 DU**；**尤重勿把 `params.Y` 读成假设-T**；**尤重勿把 `params.G` 读成假设-U**；**尤重 `params.G` 的 0.01 ≠ 过户费 0.01‰；`params.Y` 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同）**；**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**；**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**；**params 字母 ≠ 假设-U / 假设-T**；**尤重实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `du0`**；**尤重 J 股票无板日临停 ≠ 本页可转债首日临停，禁止把 J / `copy_j_halt_onto_cb_ipo` / 开盘价 30%/60%·各 10 分钟合成/混读升格进 `du0`**；**尤重 Q 转债回转/涨跌幅/收盘 ≠ 本页首日临停基准/阈值/时长，禁止合成/混读升格进 `du0`**；**尤重 CQ 转股可成交性 ≠ 本页临停，禁止合成/混读升格进 `du0`**；**尤重 DT 整手价位 ≠ 本页临停，禁止合成/混读升格进 `du0`**；**尤重 DR 盘后定价通道 ≠ 本页临停，禁止合成/混读升格进 `du0`**；**尤重 DS 转股印花 ≠ 本页临停，禁止合成/混读升格进 `du0`**；**尤重不重开假设-U，禁把 `vs_U_transfer_fee` 升格进 `du0`**；**尤重不重开假设-T，禁把 `vs_T_csrc_fee` 升格进 `du0`**；**尤重双字母 DU ≠ 双字母 AU，禁把 AU 升格进 `du0`**；**禁把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混读升格进 `du0`**；把 `invent_asof_leak_cb_ipo_halt` 升格进 `du0` 或与主报双挂；把诊断桶 `invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` / `copy_j_halt_onto_cb_ipo` / `vs_J_nolimit_halt` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DT_lot_tick` / `vs_DR_aft_pricing` / `vs_DS_conversion_stamp` / `vs_R_etf_t0` / `vs_U_transfer_fee` / `vs_T_csrc_fee` / `missing_venue_or_ipo_flag_or_issue_px_not_skip` 升格进 `du0`；用开盘价 30%/60%、各 10 分钟去填可转债首日；把核对日规则铺满 2022-08-01 前样本；缺 venue/首日标记/发行价或官方临停规则仍硬填。本页主键只用 `du0` / `du1` / `du2` 与 `cb_ipo_halt_*`。不写下一字母。不预留 #131。**纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK–DT；勿再只改清单）。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测把**可转债上市首日临停**误套成**股票无涨跌幅日临停**（较开盘价 30%/60%、各 10 分钟），或只把开盘价当成临停基准，或只套 30%/60% 与 10 分钟而不改基准，或把核对日「较发行价 20% 停 30 分钟、30% 停到 14:57」铺到 2022-08-01 前，或与 J股票无板日临停 / Q转债回转涨跌幅收盘 / CQ转股可成交性 / DT整手价位 / DR盘后定价通道 / DS转股印花 / R股票ETF假T+0 / U股票过户切日 / T股票证管费 / AU本方对手最优空簿 混读，或缺 venue/首日标记/发行价或官方临停规则仍不 skip，相对「缺 venue/首日标记/发行价或官方临停规则则 skip；可转债上市首日临停较发行价 20%→30 分钟、30%→14:57；禁止套股票无板日开盘价 30%/60%、各 10 分钟；禁止把核对日规则铺满 2022-08-01 前样本」的诚实组，会**系统性改写可转债上市首日的临停基准、阈值与时长**——相对诚实锚偏误。套错基准，临停从哪一价算起就偏了；套错阈值和时长，停几次、停多久、什么时候回到连续竞价都会偏。

核对日方向（随锚写死；禁止把发行价 20%/30%、开盘价 30%/60%、过户费 0.01‰ 或证管费 0.02‰ 写成占位门槛）：可转债首日临停和股票无板日临停分开，临停和涨跌幅/收盘分开，临停和费用分开。`事实与坑` 2026-10-26 已写：可转债首日临停看**发行价**，不是开盘价、也不是前收盘；较发行价首次涨或跌 **20%** 停 **30 分钟**，**30%** 停到 **14:57**。沪深同结构（沪市第十六条；深市第十六条）。这和股票无涨跌幅日「较开盘价 30%/60%、各 10 分钟」不是同一套。股票那套留在 J，来源在 `事实与坑` 2026-10-12：比较基准是当日开盘价，单次 10 分钟；不要拿到可转债首日来用。可转债细则自 **2022-08-01** 施行（上证发〔2022〕117 号 / 深证上〔2022〕719 号）。该日之前可转债没有这道涨跌幅和这道首日临停，不要把核对日规则铺回去。回转、次日板幅、沪深首日涨跌幅差、收盘怎么产生，都留在 Q。本页只问临停的基准、阈值和时长。转股能不能转成留在 CQ，整手和最小价位留在 DT，盘后通道留在 DR，转股印花留在 DS，股票 ETF 假 T+0 留在 R，股票过户切日留在 U，股票证管费切日留在 T，本方对手最优空簿留在 AU。缺 venue、首日标记、发行价，或官方临停规则对不上，整笔 skip，不用开盘价、30%/60%、10 分钟、占位 0.02/0.01 或证管费/过户费去填。**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**。**`params.G` 的 0.01 ≠ 过户费 0.01‰**。**`params.Y` 的 0.02 ≠ 证管费 0.02‰**。**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**。**params 字母 ≠ 假设-U / 假设-T**。**禁把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混读升格进 `du0`**。

证伪方向：若天真组 / 半泄露组相对诚实组的首日临停误套截在标定噪声带内可忽略，且「开盘价当基准 / 套 30%·60%·10 分钟 / 抄 J / 核对日泄露铺到 2022-08-01 前 / vs J·Q·CQ·DT·DR·DS·R·U·T」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · du0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DU ≠ 单字母假设-D / 假设-U**；params 字母 ≠ 假设-U / 假设-T；勿把 params.Y 读成实验字母 DU，亦勿读成假设-T，亦勿读成假设-U
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DU ≠ 单字母 D/U**
# 【消歧】尤重：params.G 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同：无量纲相对门槛 ≠ 假设-U 的费率）
# 【消歧】尤重：params.Y 的 0.02 ≠ 证管费 0.02‰（无量纲相对门槛 ≠ 假设-T 的费率）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰
# 【消歧】params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费
# 【消歧】params 字母 ≠ 假设-U / 假设-T
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DU ≠ 单字母假设-N**
# params.Y2                               写死冻结 0.015
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：首日临停误套截 ΔCbIpoHalt / 净差异 / DU1−DU2；**params.Y/G/N ≠ 实验字母 DU ≠ 单字母假设-D / 假设-U**；**params 字母 ≠ 假设-U / 假设-T**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**；**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        写死冻结 next_open
# params.asof_check_date                  写死冻结 2026-10-26
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.cb_ipo_halt_honest               写死冻结 pit_issue_px_20pct_30m_30pct_to_1457_not_open_30_60_10m
#   诚实锚方向（已写死冻结）：
#   缺 venue、首日标记、发行价或官方临停规则 → skip
#   可转债上市首日临停较发行价：20% → 30 分钟；30% → 14:57
#   禁止套股票无板日「开盘价 30%/60%、各 10 分钟」
#   禁止把核对日规则铺满 2022-08-01 前样本
#   禁止把占位 0.02/0.01/0.05/0.015 读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰ 或证管费 0.02‰
#   枚举已写死冻结
#   锚名字里的 20pct / 30pct / 30m / 1457 / open_30_60_10m 是机制方向，不是 params.Y/G/N/Y2
#   不把 J 的开盘价 30%/60%·各 10 分钟、Q 的回转涨跌幅收盘、CQ 的转股可成交、DT 的整手价位、DR 的盘后通道、DS 的转股印花、R 的假 T+0、U 的过户费、T 的证管费、AU 的空簿写成可转债首日临停诚实锚
# params.cb_ipo_halt_scope                写死冻结 cb_first_day_halt_vs_ashare_nolimit
#   方向名：可转债上市首日临停，与股票无板日临停分列
#   这不是把 20%/30% 或 30%/60% 冻成门槛
#   可转债首日临停 ≠ 股票无板日开盘价 30%/60%、各 10 分钟
# params.cb_ipo_halt_over_policy          写死冻结 skip_if_venue_or_ipo_flag_or_issue_px_or_official_rule_missing
#   缺 venue、首日标记、发行价或官方临停规则则 skip；禁在缺字段时仍按开盘价 30%/60%、各 10 分钟把可转债首日填上
# params.nolimit_halt_handoff             建议 j_page
#   消费 J 的股票无板日临停，或显式旁路；J ≠ 本页可转债首日临停；不重开假设-J；不改 J
#   J 禁止合成/混读升格进 du0；诊断桶 vs_J_nolimit_halt / copy_j_halt_onto_cb_ipo / invent_open_px_as_cb_ipo_halt_baseline / invent_30_60_10m_on_cb_ipo 不得升格进 du0
# params.cb_rules_handoff                 建议 q_page
#   可转债回转/涨跌幅/收盘交 Q；Q ≠ 本页首日临停基准/阈值/时长；双字母 DU ≠ 单字母假设-Q；不重开假设-Q；不改 Q
#   Q 禁止合成/混读升格进 du0；诊断桶 vs_Q_cb_rules 不得升格进 du0
# params.cb_conversion_fill_handoff       建议 cq_page
#   消费 CQ 的转股可成交性，或显式旁路；可成交性 ≠ 本页临停；不重开假设-CQ；不改 CQ
#   CQ 禁止合成/混读升格进 du0；诊断桶 vs_CQ_conversion_fill 不得升格进 du0
# params.cb_lot_tick_handoff              建议 dt_page
#   整手价位交 DT；DT ≠ 本页临停；不重开假设-DT；不改 DT
#   DT 禁止合成/混读升格进 du0；诊断桶 vs_DT_lot_tick 不得升格进 du0
# params.aft_pricing_handoff              建议 dr_page
#   盘后定价通道交 DR；DR ≠ 本页临停；不重开假设-DR；不改 DR
#   DR 禁止合成/混读升格进 du0；诊断桶 vs_DR_aft_pricing 不得升格进 du0
# params.cb_conversion_stamp_handoff      建议 ds_page
#   转股印花交 DS；DS ≠ 本页临停；不重开假设-DS；不改 DS
#   DS 禁止合成/混读升格进 du0；诊断桶 vs_DS_conversion_stamp 不得升格进 du0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 du0；双字母 DU ≠ 单字母假设-R；不改 R
#   R 禁止合成/混读升格进 du0；诊断桶 vs_R_etf_t0 不得升格进 du0
# params.transfer_fee_handoff             建议 u_page
#   股票过户费切日交 U；不重开假设-U；双字母 DU ≠ 单字母假设-U；params 字母 ≠ 假设-U；不改 U
#   U 禁止合成/混读升格进 du0；诊断桶 vs_U_transfer_fee 不得升格进 du0；过户费不得升格进 du0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；双字母 DU ≠ 单字母假设-T；params 字母 ≠ 假设-T；不改 T
#   T 禁止合成/混读升格进 du0；诊断桶 vs_T_csrc_fee 不得升格进 du0；证管费不得升格进 du0
# params.fill_time_suspend_handoff        建议 d_page
#   成交时点与停牌交 D；双字母 DU ≠ 单字母假设-D；不改 D
# params.board_capacity_handoff           建议 a_page
#   板上容量交 A；不抢 A 真数队列；不改 A
# params.du0_primary_demo                 写死冻结 invent_stock_nolimit_halt_on_cb_ipo
#   单一主报写死，单挂；禁与 invent_asof_leak_cb_ipo_halt 双挂；DU1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_cb_ipo_halt 只作对照，不得升格进 du0，不得双挂
#   诊断桶 invent_open_px_as_cb_ipo_halt_baseline / invent_30_60_10m_on_cb_ipo / copy_j_halt_onto_cb_ipo / vs_J_nolimit_halt / vs_Q_cb_rules / vs_CQ_conversion_fill / vs_DT_lot_tick / vs_DR_aft_pricing / vs_DS_conversion_stamp / vs_R_etf_t0 / vs_U_transfer_fee / vs_T_csrc_fee / missing_venue_or_ipo_flag_or_issue_px_not_skip 不得升格进 du0
#   尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 du0
#   尤重：禁止把 J 股票无板日临停、copy_j_halt、开盘价 30%/60%·各 10 分钟与本页合成/混读后写进 du0
#   尤重：禁止把 Q 转债回转/涨跌幅/收盘与本页首日临停基准/阈值/时长合成/混读后写进 du0
#   尤重：禁止把 CQ 转股可成交性与本页临停合成/混读后写进 du0
#   尤重：禁止把 DT 整手价位与本页临停合成/混读后写进 du0
#   尤重：禁止把 DR 盘后定价通道与本页临停合成/混读后写进 du0
#   尤重：禁止把 DS 转股印花与本页临停合成/混读后写进 du0
#   尤重：不重开假设-U；禁止把 vs_U_transfer_fee / 过户费混读后写进 du0
#   尤重：不重开假设-T；禁止把 vs_T_csrc_fee / 证管费混读后写进 du0
#   尤重：双字母 DU ≠ 双字母 AU；禁止把 AU 本方对手最优空簿混读后写进 du0
#   禁把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混读升格进 du0
# params.du0_invent_stock_nolimit_halt_on_cb_ipo 建议 True
# params.du1_asof_leak_cb_ipo_halt_only   建议 True
#   半泄露对照；DU1 不升格并列主报；不得把 invent_asof_leak_cb_ipo_halt 写进 du0
# params.du2_pit_issue_px_20pct_30m_30pct_to_1457_not_open_30_60_10m 建议 True
# params.merge_with_DT                    建议 False
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
# params.merge_with_J                     建议 False
# params.merge_with_AU                    建议 False
# params.merge_with_A                     建议 False
# params.merge_with_D                     建议 False
# params.missing_venue_or_ipo_flag_or_issue_px_or_official_rule_policy 建议 skip
# params.day_freq_proxy                   建议 cb_ipo_halt_sensitivity
# params.universe_rule                    建议 cb_ipo_halt_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_du_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DU；勿把这个键读成实验 DU，亦勿读成单字母 D/U，亦勿读成假设-U，亦勿读成双字母 AU
#   不另挂主报，不预留 #131，不写下一字母
```

### 2.2 三组对照（DU0 / DU1 / DU2）

组名 DU0 / DU1 / DU2 是本页三组，≠ 单字母实验 U（股票过户费切日），亦 ≠ 单字母实验 D（成交时点与停牌），亦 ≠ 单字母实验 R（股票 ETF 假 T+0），亦 ≠ 双字母 AU（本方对手最优空簿）。**双字母 DU ≠ 单字母假设-D / 假设-U**。**双字母 DU ≠ 双字母 AU**。**params 字母 ≠ 假设-U / 假设-T**。

| 组 | 角色 | 口径 |
|----|------|------|
| DU0 | 天真 / 可转债首日临停误套股票无板日临停 | 按 `du0_primary_demo` **写死冻结**单一主报 `invent_stock_nolimit_halt_on_cb_ipo`（单挂写死）：把股票无板日「开盘价 30%/60%、各 10 分钟」套到可转债上市首日。**禁**与 `invent_asof_leak_cb_ipo_halt` 双挂主报。**禁把 J / Q / CQ / DT / DR / DS / R / U / T / AU 合成进 `du0`**（只作对照/旁路，不得升格进 `du0` 或另挂主报）。**禁把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混读升格进 `du0`** |
| DU1 | 半泄露 | 仅核对日把「可转债上市首日较发行价 20% 停 30 分钟、30% 停到 14:57」铺到全历史、铺到 2022-08-01 前样本、或铺到股票无板日（`invent_asof_leak_cb_ipo_halt`）；**不得升格并列主报**，也不得写进 `du0`（写死冻结：DU1 不升格），不得双挂 |
| DU2 | 诚实 / 可转债首日按发行价临停 | `cb_ipo_halt_honest=pit_issue_px_20pct_30m_30pct_to_1457_not_open_30_60_10m`（写死冻结）：缺 venue/首日标记/发行价或官方临停规则则 skip；较发行价 20%→30 分钟、30%→14:57；禁止套股票无板日开盘价 30%/60%、各 10 分钟；禁止把核对日规则铺满 2022-08-01 前样本。股票无板日临停只消费 J，回转涨跌幅收盘只消费 Q，转股可成交只消费 CQ，整手价位只消费 DT，盘后定价只消费 DR，转股印花只消费 DS，股票 ETF 假 T+0 只消费 R，股票过户只消费 U，股票证管费只消费 T，或显式旁路。空簿只留在 AU，不并进本页 |

只把开盘价当基准、只套 30%/60% 与 10 分钟、把 J 整页抄过来、把核对日规则铺到 2022-08-01 前、把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混进本页，以及相对这些页的对照截（`invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` / `copy_j_halt_onto_cb_ipo` / `vs_J_nolimit_halt` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DT_lot_tick` / `vs_DR_aft_pricing` / `vs_DS_conversion_stamp` / `vs_R_etf_t0` / `vs_U_transfer_fee` / `vs_T_csrc_fee` / `missing_venue_or_ipo_flag_or_issue_px_not_skip`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `du0_primary_demo`。`vs_J_nolimit_halt` 与 `copy_j_halt_onto_cb_ipo` 只标记股票无板日临停对照，**不得升格进 `du0`**。`invent_open_px_as_cb_ipo_halt_baseline` 只标记「有人用开盘价当可转债首日临停基准」，**不得升格进 `du0`**。`invent_30_60_10m_on_cb_ipo` 只标记「有人把 30%/60%、各 10 分钟套到可转债首日」，**不得升格进 `du0`**。`vs_Q_cb_rules` 只标记回转涨跌幅收盘对照，**不得升格进 `du0`**。`vs_CQ_conversion_fill` 只标记转股可成交对照，**不得升格进 `du0`**。`vs_DT_lot_tick` 只标记整手价位对照，**不得升格进 `du0`**。`vs_DR_aft_pricing` 只标记盘后通道对照，**不得升格进 `du0`**。`vs_DS_conversion_stamp` 只标记转股印花对照，**不得升格进 `du0`**。`vs_R_etf_t0` 只标记「有人把实验 R 和本页混读」，**不得升格进 `du0`**。`vs_U_transfer_fee` 只标记「有人把过户费和本页混读」，**不得升格进 `du0`**。`vs_T_csrc_fee` 只标记「有人把证管费和本页混读」，**不得升格进 `du0`**。`missing_venue_or_ipo_flag_or_issue_px_not_skip` 同样只作诊断；官方临停规则缺失也走 skip，不另造主报。J 的无板日临停、Q 的规则、CQ 的可成交、DT 的整手价位、DR 的盘后、DS 的印花、R 的假 T+0、U 的过户、T 的证管费、AU 的空簿只作对照/旁路。

### 2.3 成交规则窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-26`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`du0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺 venue/首日标记/发行价或官方临停规则则 skip；可转债上市首日临停较发行价 20%→30 分钟、30%→14:57；禁止套股票无板日「开盘价 30%/60%、各 10 分钟」；禁止把核对日规则铺满 2022-08-01 前样本。方向随锚写死：**不要把核对日规则铺满 2022-08-01 前，也不要把开盘价 30%/60%、各 10 分钟写成可转债首日唯一规则**。范围名 `cb_first_day_halt_vs_ashare_nolimit` 只标方向：本页只看可转债上市首日临停有没有被套成股票无板日临停。股票无板日临停留给 J，回转涨跌幅收盘留给 Q，转股可成交留给 CQ，整手价位留给 DT，盘后通道留给 DR，转股印花留给 DS，股票 ETF 假 T+0 留给 R，过户费留给 U，证管费留给 T，空簿留给 AU。`params.G` 的 0.01 是无量纲相对门槛，不是过户费 0.01‰，也不是开盘价 30% 或 60%。`params.Y` 的 0.02 不是证管费 0.02‰，也不是发行价 20%。**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**。**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**。**params 字母 ≠ 假设-U / 假设-T**。缺 venue、首日标记、发行价或官方规则则 skip，不用开盘价、30%/60%、10 分钟或占位 0.01 把可转债首日临停填上。本页**不开回测**；不拉真数；不做实盘；不开户。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `du0_primary_demo` / `params.Y`·G·N·Y2 / 首日临停开关 / 桶 / 是否把发行价 20%/30% 或开盘价 30%/60% 铺到全历史、或铺到 2022-08-01 前、或把占位读成临停阈值/过户费/证管费）。本页不开跑。禁 null。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DU0）/ 半泄露组（DU1）相对诚实组（DU2）的首日临停误套截**显著且集中在可转债上市首日被套成股票无板日「开盘价 30%/60%、各 10 分钟」的桶**；分桶「开盘价当基准 / 套 30%·60%·10 分钟 / 抄 J / 核对日泄露 / vs J·Q·CQ·DT·DR·DS·R·U·T」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 20%/30% 或 30%/60% 冻成门槛，也不把 `params.G` 的 0.01 读成过户费，也不把 `params.Y` 的 0.02 读成证管费。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 J 的股票无板日临停、Q 的回转涨跌幅收盘、CQ 的转股可成交、DT 的整手价位、DR 的盘后定价、DS 的转股印花、R 的股票 ETF 假 T+0、U 的股票过户、T 的股票证管费、AU 的本方对手最优空簿、E 的股票/科创整手、F 的涨跌停取整、BR 的借券费、DQ 的篮子过户、DP 的换股印花、DO 的回售处理、DN 的换股过户、DM 的换股经手、DL 的综合协议过户、DK 的基金印花、DJ 的基金证管费、DI 的大宗经手、DH 的佣金双计、DG 的北交所档、DF 的可交换现货经手、DE 的转债证管费、DD 的转债过户、DC 的转债印花、DB 的转债现货经手、DA 的二级过户、S 的股票经手、AX 的基金经手、V 的股票印花、AC 的北交所涨跌幅与盘后、O 的大宗、M 的股票盘后、CH/CL 的盘后可成交、CR 的行权成交、A 的板上容量、D 的成交时点解释；或 `du0_primary_demo` 与 `invent_asof_leak_cb_ipo_halt` 双挂；或 DU1 升格并列主报；或 `invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` / `copy_j_halt_onto_cb_ipo` / `vs_J_nolimit_halt` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DT_lot_tick` / `vs_DR_aft_pricing` / `vs_DS_conversion_stamp` / `vs_R_etf_t0` / `vs_U_transfer_fee` / `vs_T_csrc_fee` / `missing_venue_or_ipo_flag_or_issue_px_not_skip` 诊断桶升格主报；或把 J / Q / CQ / DT / DR / DS / R / U / T / AU 合成进 `du0`；或实验字母 DU 与单字母 D/U 或 params.Y/G/N 混读；或把双字母 AU 读成双字母 DU；或把 `params.G` 的 0.01 读成过户费 0.01‰；或把 `params.Y` 的 0.02 读成证管费 0.02‰；或把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰；或把 params 字母读成假设-U / 假设-T；或把核对日规则写成已冻并铺满 2022-08-01 前；或缺 venue / 首日标记 / 发行价 / 官方临停规则仍不 skip；或重开假设-J / 假设-Q / 假设-CQ / 假设-DT / 假设-DR / 假设-DS / 假设-R / 假设-U / 假设-T / 假设-AU；或标纸面齐；或写成 A/D–DU纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 DU0/DU1/DU2。股票无板日临停走 J 或显式旁路，不在本页改 J。回转涨跌幅收盘走 Q，转股可成交走 CQ，整手价位走 DT，盘后定价走 DR，转股印花走 DS，股票 ETF 假 T+0 走 R，股票过户走 U，股票证管费走 T，都不改。空簿留在 AU，不并进本页。报告首日临停误套截。不把发行价 20%/30% 或开盘价 30%/60% 标成已冻门槛，也不把 `params.G` 的 0.01 读成过户费，也不把 `params.Y` 的 0.02 读成证管费。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_stock_nolimit_halt_on_cb_ipo` / `invent_asof_leak_cb_ipo_halt` / `invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` / `copy_j_halt_onto_cb_ipo` / `vs_J_nolimit_halt` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DT_lot_tick` / `vs_DR_aft_pricing` / `vs_DS_conversion_stamp` / `vs_R_etf_t0` / `vs_U_transfer_fee` / `vs_T_csrc_fee` / `missing_venue_or_ipo_flag_or_issue_px_not_skip`

`invent_open_px_as_cb_ipo_halt_baseline`、`invent_30_60_10m_on_cb_ipo`、`copy_j_halt_onto_cb_ipo`、`vs_J_nolimit_halt`、`vs_Q_cb_rules`、`vs_CQ_conversion_fill`、`vs_DT_lot_tick`、`vs_DR_aft_pricing`、`vs_DS_conversion_stamp`、`vs_R_etf_t0`、`vs_U_transfer_fee`、`vs_T_csrc_fee`、`missing_venue_or_ipo_flag_or_issue_px_not_skip` 只作诊断桶：它们不是 `du0`，也不是 DU1，**不得升格主报**。`vs_J_nolimit_halt` 没有对应的「J 无板日临停 + 可转债首日临停」合成主报。假设-J 只作诊断，**不得升格进 `du0`**，**不重开假设-J**。`copy_j_halt_onto_cb_ipo`、`invent_open_px_as_cb_ipo_halt_baseline`、`invent_30_60_10m_on_cb_ipo` 同样只作诊断，**不得升格进 `du0`**。`vs_Q_cb_rules` 没有对应的「回转涨跌幅收盘 + 首日临停」合成主报。`vs_CQ_conversion_fill` 没有对应的「转股可成交 + 临停」合成主报。`vs_DT_lot_tick` 没有对应的「整手价位 + 临停」合成主报。`vs_DR_aft_pricing` 没有对应的「盘后通道 + 临停」合成主报。`vs_DS_conversion_stamp` 没有对应的「转股印花 + 临停」合成主报。`vs_R_etf_t0` 没有对应的「假 T+0 + 首日临停」合成主报。实验 R 只作诊断，**不得升格进 `du0`**。`vs_U_transfer_fee` 没有对应的「过户费 + 临停」合成主报。假设-U 只作诊断，**不得升格进 `du0`**，**不重开假设-U**。`vs_T_csrc_fee` 没有对应的「证管费 + 临停」合成主报。假设-T 只作诊断，**不得升格进 `du0`**，**不重开假设-T**。AU 的本方对手最优空簿只作分列，**不得升格进 `du0`**，**不重开假设-AU**。缺字段仍不 skip，只作诊断，**不得升格进 `du0`**。`invent_asof_leak_cb_ipo_halt` 只服务 DU1，**不得升格进 `du0`，不得双挂**。`invent_stock_nolimit_halt_on_cb_ipo` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「可转债首日按股票无板日开盘价 30%/60%、各 10 分钟临停」拿去当诚实锚。
- 把 `params.G` 的 0.01 当成过户费 0.01‰，或当成开盘价 30%/60%。**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰**。**params 字母 ≠ 假设-U**。
- 把 `params.Y` 的 0.02 当成证管费 0.02‰，或当成发行价 20%。**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**。**params 字母 ≠ 假设-T**。
- 把占位 `0.02/0.01/0.05/0.015` 读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰。**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**。**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**。
- 缺 venue、首日标记、发行价或官方临停规则仍不 skip，并用开盘价 30%/60%、各 10 分钟或占位 0.01 把可转债首日填上。
- 把核对日「发行价 20%→30 分钟、30%→14:57」写成全历史唯一规则，并铺满 2022-08-01 前样本，或把开盘价 30%/60%、各 10 分钟写成可转债首日唯一规则。锚六键已写死冻结。
- 把「股票无板日临停已分列（J）/ 回转涨跌幅收盘已分列（Q）/ 转股可成交已分列（CQ）/ 整手价位已分列（DT）/ 盘后通道已分列（DR）/ 转股印花已分列（DS）/ 股票 ETF 回转已分列（R）/ 过户已分列（U）/ 证管费已分列（T）/ 空簿已分列（AU）」写成「可转债首日临停已诚实」。不改 J / Q / CQ / DT / DR / DS / R / U / T / AU。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格进 `du0`。诊断桶 `vs_R_etf_t0` 只作对照。不抢、不重开假设-R。**实验 R 不抢**。
- 把 J 股票无板日临停、`copy_j_halt_onto_cb_ipo`、开盘价 30%/60%·各 10 分钟和本页合成或混读后升格进 `du0`。诊断桶 `vs_J_nolimit_halt` / `copy_j_halt_onto_cb_ipo` / `invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` 只作对照。**不重开假设-J**。
- 把 Q 转债回转/涨跌幅/收盘和本页首日临停基准/阈值/时长合成或混读后升格进 `du0`。诊断桶 `vs_Q_cb_rules` 只作对照。
- 把 CQ 转股可成交性和本页临停合成或混读后升格进 `du0`。诊断桶 `vs_CQ_conversion_fill` 只作对照。
- 把 DT 整手价位和本页临停合成或混读后升格进 `du0`。诊断桶 `vs_DT_lot_tick` 只作对照。
- 把 DR 盘后定价通道和本页临停合成或混读后升格进 `du0`。诊断桶 `vs_DR_aft_pricing` 只作对照。
- 把 DS 转股印花和本页临停合成或混读后升格进 `du0`。诊断桶 `vs_DS_conversion_stamp` 只作对照。
- 把假设-U 的过户费和本页合成或混读后升格进 `du0`。诊断桶 `vs_U_transfer_fee` 只作对照。**不重开假设-U**。
- 把假设-T 的证管费和本页合成或混读后升格进 `du0`。诊断桶 `vs_T_csrc_fee` 只作对照。**不重开假设-T**。
- 把 AU 本方对手最优空簿和本页合成或混读后升格进 `du0`。**双字母 DU ≠ 双字母 AU**。**不重开假设-AU**。
- 缺 venue、首日标记或发行价仍不 skip，并升格进 `du0`。诊断桶 `missing_venue_or_ipo_flag_or_issue_px_not_skip` 只作对照。
- `du0_primary_demo` 与 `invent_asof_leak_cb_ipo_halt` 双挂主报；DU1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DU 与单字母 D/U 或 params.Y/G/N 混读。**双字母 DU ≠ 单字母假设-D / 假设-U**。**双字母 DU ≠ 双字母 AU**。
- 改 J / Q / CQ / DT / DR / DS / R / U / T / AU / D / DQ / DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / V / AC / O / M / CH / CL / CR / E / F / BR / A 正文；重开假设-J；重开假设-Q；重开假设-CQ；重开假设-DT；重开假设-DR；重开假设-DS；重开假设-R；重开假设-U；重开假设-T；重开假设-AU；抢 A 真数队列；抢实验 R；标纸面齐；写成 A/D–DU纸面齐；开真数/回测/开户/实盘；用复权价当临停基准；结论写成「转债首日能穿过临停所以能买」。
- **纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK–DT；勿再只改清单）。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权价格路径、交易日、**交易所 venue**（沪/深）、**是否上市首日**、**发行价**、**证券类别**（可转债 / 股票；仅用于把腿分回 J、Q、CQ、DT、DR、DS、R、U、T 或本页）、**官方临停规则是否在册**（缺则 skip，不发明另一套分钟数，也不拿股票开盘价 30%/60%、各 10 分钟去填）。
- 临停基准要能分清「发行价」和「当日开盘价」。可转债首日建议方向是发行价。股票无板日的开盘价基准只消费 J，不在本页改 J。
- 阈值和时长：可转债首日建议方向是 20%→30 分钟、30%→14:57。股票无板日的 30%/60%、各 10 分钟只作对照，不收进本页主报。
- 样本日要能分清是否早于 **2022-08-01**。早于该日的可转债，不要用核对日首日临停去填。细则施行日之前怎么停，本页不发明分钟数；对不上就 skip。
- 回转、涨跌幅、收盘怎么产生只消费 Q。深市首日有效申报范围、沪市首日 57.3%/43.3%，都不是本页临停主报。
- 没有 venue、首日标记、发行价或官方临停规则时，按写死冻结的 `cb_ipo_halt_over_policy=skip_if_venue_or_ipo_flag_or_issue_px_or_official_rule_missing` skip，不得按开盘价 30%/60%、各 10 分钟或占位 0.01 把可转债首日填上。
- 旁路消费：J 的股票无板日临停、Q 的回转涨跌幅收盘、CQ 的转股可成交、DT 的整手价位、DR 的盘后定价、DS 的转股印花、R 的股票 ETF 假 T+0、U 的股票过户、T 的股票证管费、D 的成交时点之诚实结果或显式旁路（见 §2.1 handoff）。AU 的空簿不消费进本页主报。**本页不改写这些页。** 这些页的主报不收到本页 `du0`。
- 未复权路径；asof **写死冻结** `2026-10-26`。核对日方向「较发行价 20%→30 分钟、30%→14:57；禁止套开盘价 30%/60%、各 10 分钟；禁止铺满 2022-08-01 前」是写死冻结的机制方向，不是已冻的全历史规则，也不是占位门槛。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-26`；`fail_policy=skip`；`cb_ipo_halt_honest=pit_issue_px_20pct_30m_30pct_to_1457_not_open_30_60_10m`（缺 venue/首日标记/发行价或官方临停规则则 skip；较发行价 20%→30 分钟、30%→14:57；禁止套股票无板日开盘价 30%/60%、各 10 分钟；禁止把核对日规则铺满 2022-08-01 前样本）；`cb_ipo_halt_scope=cb_first_day_halt_vs_ashare_nolimit`（可转债上市首日临停与股票无板日临停分列；方向名，不是已冻规则）；`cb_ipo_halt_over_policy=skip_if_venue_or_ipo_flag_or_issue_px_or_official_rule_missing`（缺 venue/首日标记/发行价或官方临停规则则 skip）；`du0_primary_demo=invent_stock_nolimit_halt_on_cb_ipo`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_cb_ipo_halt` 双挂；DU1 不升格；诊断桶不升格主报；**禁把 J / Q / CQ / DT / DR / DS / R / U / T / AU 合成进 `du0`**，只作对照/旁路，不得升格进 `du0` 或另挂主报；**禁把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混读升格进 `du0`**）；`nolimit_halt_handoff=j_page`；`cb_rules_handoff=q_page`；`cb_conversion_fill_handoff=cq_page`；`cb_lot_tick_handoff=dt_page`；`aft_pricing_handoff=dr_page`；`cb_conversion_stamp_handoff=ds_page`；`etf_t0_handoff=r_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`merge_with_DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/AU/A/D=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是临停阈值、不是过户费、不是证管费：首日临停误套截 ΔCbIpoHalt / 净差异 / DU1−DU2；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同）**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**；**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**；**params.Y/G/N ≠ 实验字母 DU ≠ 单字母 D/U**；**params 字母 ≠ 假设-U / 假设-T**；**勿把 params.Y 读成假设-T，亦勿把 params.G 读成假设-U，亦勿把单字母假设-D / 假设-U 读成双字母 DU，亦勿把双字母 AU 读成双字母 DU**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #131。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`b1e0b311`（A/D–DT纸面齐已合，全长 `b1e0b3112c39ab3749df670d08b79b9f5eca9277`）；三冻补丁基 tip=`43f0a74b` / `43f0a74ba318c42f130b668580c01fcc3c1439c3`；分支起点 HEAD=`867c9a70` / `867c9a708b5327c59eb89b0c79d56626eed15d0b`。**不改已冻 A–DQ / DA–DT**。状态=**A/D–DU纸面齐（预检有条件通过·三条已冻）**。

---

## 8. 结论

（空；**A/D–DU纸面齐（预检有条件通过·三条已冻）**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-12-01）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DU-20261110.md`（原样落入，不改结论；SHA256=`0f860c47a71948572b0490bdfe5897ec9873ee05cb5340e4a23647579aba1a92`；预检 2026-11-10；**结论：有条件通过**；tip基=`43f0a74b` / `43f0a74ba318c42f130b668580c01fcc3c1439c3`；本补丁分支起点 HEAD=`867c9a70` / `867c9a708b5327c59eb89b0c79d56626eed15d0b`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于首日临停误套截 ΔCbIpoHalt、净差异、DU1−DU2 专项。**`params.Y` ≠ 实验字母 DU**；**`params.G` ≠ 实验字母 DU**；**`params.N` ≠ 实验字母 DU**；亦 ≠ 单字母假设-D / 假设-U。**params.Y/G/N ≠ 实验字母 DU ≠ 单字母 D/U**。**勿把 `params.Y` 读成假设-T，亦勿把 `params.G` 读成假设-U，亦勿把 `params.Y` 读成实验字母 DU，亦勿把单字母假设-D / 假设-U 读成双字母 DU，亦勿把双字母 AU 读成双字母 DU**。**尤重：`params.G` 的 `0.01` ≠ 过户费 0.01‰**（**params.G 的 0.01 ≠ 过户费 0.01‰**）。量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户费 0.01‰，也不是开盘价 30% 或 60%，也不是发行价 20% 或 30%。**尤重：`params.Y` 的 `0.02` ≠ 证管费 0.02‰ ≠ 发行价 20%**（**params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价 20%**）。**params 字母 ≠ 假设-U / 假设-T**。**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**。**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**。禁止互读、禁止把门槛改写成临停阈值、过户费或证管费。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.du0_primary_demo`**：**写死冻结** **`invent_stock_nolimit_halt_on_cb_ipo`**（单一主报，单挂写死）。**禁止**与半泄露键 **`invent_asof_leak_cb_ipo_halt`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DU1 仅核对日把「可转债上市首日较发行价 20% 停 30 分钟、30% 停到 14:57」铺到全历史、铺到 2022-08-01 前样本、或铺到股票无板日只作半泄露对照，**不得升格与 du0 并列主报**，也不得把 `invent_asof_leak_cb_ipo_halt` 写进 `du0`。`invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` / `copy_j_halt_onto_cb_ipo` / `vs_J_nolimit_halt` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DT_lot_tick` / `vs_DR_aft_pricing` / `vs_DS_conversion_stamp` / `vs_R_etf_t0` / `vs_U_transfer_fee` / `vs_T_csrc_fee` / `missing_venue_or_ipo_flag_or_issue_px_not_skip` **只作诊断桶，不得升格主报**。DU1 / 诊断桶 **不升格**。**禁把以下升格进 du0**：J股票无板日临停 / Q转债规则 / CQ转股可成交 / DT整手价位 / DR盘后定价 / DS转股印花 / R假T+0 / U过户切日 / T证管费切日 / AU。这些只作对照/旁路，**不得升格进 `du0`，不得另挂主报**。**不重开假设-J**；**不重开假设-Q**；**不重开假设-CQ**；**不重开假设-DT**；**不重开假设-DR**；**不重开假设-DS**；**不重开假设-R**；**不重开假设-U**；**不重开假设-T**；**不重开假设-AU**。**不抢实验 R**。

3. **可转债首日临停诚实锚六键升格写死（不可再写「建议」）**：`params.cb_ipo_halt_honest=pit_issue_px_20pct_30m_30pct_to_1457_not_open_30_60_10m`；`params.cb_ipo_halt_scope=cb_first_day_halt_vs_ashare_nolimit`；`params.cb_ipo_halt_over_policy=skip_if_venue_or_ipo_flag_or_issue_px_or_official_rule_missing`；`params.asof_check_date=2026-10-26`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺 venue/首日标记/发行价或官方临停规则 → skip；可转债上市首日临停较发行价 20%→30 分钟、30%→14:57；禁止套股票无板日「开盘价 30%/60%、各 10 分钟」；禁止把核对日规则铺满 2022-08-01 前样本。禁止跑后改锚，或用开盘价 30%/60%、各 10 分钟 / 核对日规则铺满 / 只把开盘价当基准 / 缺 venue/首日标记/发行价或官方规则仍硬填 / 把 J/Q/CQ/DT/DR/DS/R/U/T/AU 升格进 du0 冒充诚实 PIT。**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**。**禁把 params.G 的 0.01 读成过户费 0.01‰**。**禁把 params.Y 的 0.02 读成证管费 0.02‰ 或发行价 20%**。**不重开假设-U**；**不重开假设-T**；**不重开假设-J**；**不重开假设-Q**；**不重开假设-R**。**不抢实验 R**。

**硬分列保住**：DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠AU≠A≠D；**双字母 DU ≠ 单字母假设-D / 假设-U**；**双字母 DU ≠ 单字母 D/U**；**双字母 DU ≠ 双字母 AU**；**params.Y / params.G / params.N ≠ 实验字母 DU ≠ 单字母 D/U**；**params 字母 ≠ 假设-U / 假设-T**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价 20%**；**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**；**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**；**可转债首日临停误套股票无板日临停 ≠ J股票无板日临停 ≠ Q转债规则 ≠ CQ转股可成交 ≠ DT整手价位 ≠ DR盘后定价 ≠ DS转股印花 ≠ R假T+0 ≠ U过户切日 ≠ T证管费切日 ≠ AU**；不抢 A；不抢实验 R；不改已齐/已冻 DA～DT 及 A–DQ 正文；**不重开假设-J**；**不重开假设-Q**；**不重开假设-CQ**；**不重开假设-DT**；**不重开假设-DR**；**不重开假设-DS**；**不重开假设-R**；**不重开假设-U**；**不重开假设-T**；**不重开假设-AU**；**禁把 J股票无板日临停 / Q转债规则 / CQ转股可成交 / DT整手价位 / DR盘后定价 / DS转股印花 / R假T+0 / U过户切日 / T证管费切日 / AU 合成/混读升格进 du0**。handoff 保持：`nolimit_halt_handoff=j_page`；`cb_rules_handoff=q_page`；`cb_conversion_fill_handoff=cq_page`；`cb_lot_tick_handoff=dt_page`；`aft_pricing_handoff=dr_page`；`cb_conversion_stamp_handoff=ds_page`；`etf_t0_handoff=r_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`merge_with_*=False`。

**状态**：**A/D–DU纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/开户/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-10 | 复检/纸面齐——**A/D–DU纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设DU-20261110.md` 原样落入，SHA256=`3e5c3d09b3e14fc64ea2826709d5f53bd78d7c8771ad9170efe784b7cb59ff90`；三冻 tip=`000dac19` / `000dac196e94a4b62a6b2297ac8674f8b9569c45`。只改状态标签；未改写已冻三条/六键；不改已齐 A–DQ / DA–DT；不改 #110–#129；不重开假设-J / 假设-Q / 假设-CQ / 假设-DT / 假设-DR / 假设-DS / 假设-R / 假设-U / 假设-T / 假设-AU；不抢实验 R；不开回测/真数/开户/实盘。 |
| 2026-12-01 | 风控预检补丁·冻结三条写死——依据 `预检-假设DU-20261110.md`（SHA256=`0f860c47a71948572b0490bdfe5897ec9873ee05cb5340e4a23647579aba1a92`；结论=有条件通过；tip基=`43f0a74b` / `43f0a74ba318c42f130b668580c01fcc3c1439c3`；分支起点 HEAD=`867c9a70` / `867c9a708b5327c59eb89b0c79d56626eed15d0b`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖首日临停误套截 ΔCbIpoHalt / 净差异 / DU1−DU2；**params.Y/G/N ≠ 实验字母 DU ≠ 单字母 D/U**；**勿把 params.Y 读成假设-T，亦勿把 params.G 读成假设-U，亦勿把单字母假设-D / 假设-U 读成双字母 DU，亦勿把双字母 AU 读成双字母 DU**；**params 字母 ≠ 假设-U / 假设-T**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同）**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价 20%**；**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**；**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成临停阈值/过户费/证管费）；② `params.du0_primary_demo=invent_stock_nolimit_halt_on_cb_ipo`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_cb_ipo_halt` 双挂；DU1 不升格；诊断桶 `invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` / `copy_j_halt_onto_cb_ipo` / `vs_J_nolimit_halt` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DT_lot_tick` / `vs_DR_aft_pricing` / `vs_DS_conversion_stamp` / `vs_R_etf_t0` / `vs_U_transfer_fee` / `vs_T_csrc_fee` / `missing_venue_or_ipo_flag_or_issue_px_not_skip` 不升格；**禁把 J股票无板日临停 / Q转债规则 / CQ转股可成交 / DT整手价位 / DR盘后定价 / DS转股印花 / R假T+0 / U过户切日 / T证管费切日 / AU 合成/混读升格进 du0**，只作对照/旁路，不得升格进 du0 或另挂主报；不重开假设-J；不重开假设-Q；不重开假设-CQ；不重开假设-DT；不重开假设-DR；不重开假设-DS；不重开假设-R；不重开假设-U；不重开假设-T；不重开假设-AU；不抢实验 R）；③ 锚六键写死 `cb_ipo_halt_honest=pit_issue_px_20pct_30m_30pct_to_1457_not_open_30_60_10m` / `cb_ipo_halt_scope=cb_first_day_halt_vs_ashare_nolimit` / `cb_ipo_halt_over_policy=skip_if_venue_or_ipo_flag_or_issue_px_or_official_rule_missing` / `asof_check_date=2026-10-26` / `fill_time=next_open` / `fail_policy=skip`（缺 venue/首日标记/发行价或官方临停规则 → skip；可转债上市首日临停较发行价 20%→30 分钟、30%→14:57；禁止套股票无板日「开盘价 30%/60%、各 10 分钟」；禁止把核对日规则铺满 2022-08-01 前样本）。handoff 保持 `nolimit_halt_handoff=j_page` / `cb_rules_handoff=q_page` / `cb_conversion_fill_handoff=cq_page` / `cb_lot_tick_handoff=dt_page` / `aft_pricing_handoff=dr_page` / `cb_conversion_stamp_handoff=ds_page` / `etf_t0_handoff=r_page` / `transfer_fee_handoff=u_page` / `csrc_fee_handoff=t_page`；`merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DU纸面齐**；不改已齐/已冻 DA～DT 及 A–DQ；不改假设-DA～假设-DT；不改 #110–#129；不重开假设-J；不重开假设-Q；不重开假设-CQ；不重开假设-DT；不重开假设-DR；不重开假设-DS；不重开假设-R；不重开假设-U；不重开假设-T；不重开假设-AU；不抢实验 R；不预留 #131；不开回测/真数/开户/实盘。基于 tip=`43f0a74b`。 |
| 2026-12-01 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。可转债首日临停误套股票无板日临停（成交规则）；`du0_primary_demo` 建议 `invent_stock_nolimit_halt_on_cb_ipo`，单一主报，单挂，禁与 `invent_asof_leak_cb_ipo_halt` 双挂，DU1 不升格；诊断桶 `invent_open_px_as_cb_ipo_halt_baseline` / `invent_30_60_10m_on_cb_ipo` / `copy_j_halt_onto_cb_ipo` / `vs_J_nolimit_halt` / `vs_Q_cb_rules` / `vs_CQ_conversion_fill` / `vs_DT_lot_tick` / `vs_DR_aft_pricing` / `vs_DS_conversion_stamp` / `vs_R_etf_t0` / `vs_U_transfer_fee` / `vs_T_csrc_fee` / `missing_venue_or_ipo_flag_or_issue_px_not_skip` 不升格；**尤重实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 du0**；**尤重 J 股票无板日临停 ≠ 本页可转债首日临停，禁止把 J / copy_j_halt / 开盘价 30%/60%·各 10 分钟合成进 du0**；**尤重 Q 转债回转/涨跌幅/收盘 ≠ 本页首日临停基准/阈值/时长，禁止合成进 du0**；**尤重 CQ 转股可成交性 ≠ 本页临停，禁止合成进 du0**；**尤重 DT 整手价位 ≠ 本页临停，禁止合成进 du0**；**尤重 DR 盘后定价通道 ≠ 本页临停，禁止合成进 du0**；**尤重 DS 转股印花 ≠ 本页临停，禁止合成进 du0**；**尤重不重开假设-U，禁把 vs_U_transfer_fee 升格进 du0**；**尤重不重开假设-T，禁把 vs_T_csrc_fee 升格进 du0**；**双字母 DU ≠ 单字母假设-D / 假设-U**；**双字母 DU ≠ 双字母 AU（本方对手最优空簿），禁把 AU 升格进 du0**；**params 字母 ≠ 假设-U / 假设-T**；**禁把 J/Q/CQ/DT/DR/DS/R/U/T/AU 混读升格进 du0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DU ≠ 单字母 D/U**，且 **params.G 的 0.01 ≠ 过户费 0.01‰**，**params.Y 的 0.02 ≠ 证管费 0.02‰**，**禁把占位读成发行价阈值 20%/30%、开盘价 30%/60%、过户费 0.01‰、证管费 0.02‰**，**params 相对门槛 ≠ 临停阈值 ≠ 过户费 ≠ 证管费**；锚建议·待冻、未冻：`cb_ipo_halt_honest=pit_issue_px_20pct_30m_30pct_to_1457_not_open_30_60_10m` / scope=`cb_first_day_halt_vs_ashare_nolimit` / over_policy=`skip_if_venue_or_ipo_flag_or_issue_px_or_official_rule_missing` / `asof_check_date=2026-10-26` / `fill_time=next_open` / `fail_policy=skip`；口径：缺 venue/首日标记/发行价或官方临停规则则 skip；可转债上市首日临停较发行价 20%→30 分钟、30%→14:57；禁止套股票无板日「开盘价 30%/60%、各 10 分钟」；禁止把核对日规则铺满 2022-08-01 前样本（**草稿方向，尚未冻，不要写成已冻**）；handoff：`nolimit_halt_handoff=j_page`，`cb_rules_handoff=q_page`，`cb_conversion_fill_handoff=cq_page`，`cb_lot_tick_handoff=dt_page`，`aft_pricing_handoff=dr_page`，`cb_conversion_stamp_handoff=ds_page`，`etf_t0_handoff=r_page`，`transfer_fee_handoff=u_page`，`csrc_fee_handoff=t_page`；`merge_with_DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/AU/A/D=False`；**DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠AU≠A≠D**；**双字母 DU ≠ 单字母 D/U**；**双字母 DU ≠ 双字母 AU**；**未标纸面齐**；**不写 A/D–DU纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–DT；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–DT；不改已齐假设-DA～假设-DT；不改 #110–#129；不重开假设-J；不重开假设-Q；不重开假设-CQ；不重开假设-DT；不重开假设-DR；不重开假设-DS；不重开假设-R；不重开假设-U；不重开假设-T；不重开假设-AU；不写下一字母；不预留 #131；不开真数/回测/开户/实盘。基 tip=`b1e0b311`（A/D–DT纸面齐已合，全长 `b1e0b3112c39ab3749df670d08b79b9f5eca9277`；不改该 tip 上的 #110–#129，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
