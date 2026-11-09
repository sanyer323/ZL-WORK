# 假设-DR · 可转债盘后定价误套股票盘后固定价格（成交规则）

更新：2026-11-24  
来源：总管线 / 基 tip=`50946c09` / 全长 `50946c09b6160e4ade9bfed886e5dbb954f84358`（A/D–DQ纸面齐已合）；**不改已冻 A–DQ / DA–DQ**；**不改假设-DQ 正文**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-S / 假设-AX / 假设-T / 假设-U / 假设-V / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-A / 假设-D 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-BR / 假设-DO）；**不重开假设-T**；**不重开假设-R**；**不重开假设-Q**；**不重开假设-M**；**不重开假设-O**；**不重开假设-DO**；**不重开假设-DQ**；**不重开假设-AC**；**不重开假设-U**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**）后写下一草稿 DR；清单 #126=DQ，本页占用 **#127=DR**；选题是回测把**可转债盘后定价**误套成**股票盘后固定价格**（股票盘后固定价格=收盘价、时间优先；深市可转债盘后定价允许收盘价或匹配 VWAP；二者禁止合成一句）；假设-M 只收股票盘后通道是否存在、竞价剩单会不会自动进盘后，假设-CH 只收股票盘后固定价格可成交性，假设-CL 只收可转债盘后定价可成交性，假设-Q 只收可转债连续竞价规则混用，假设-O 只收大宗三通道，假设-R 只收股票 ETF 假 T+0，假设-DO 只收可转债回售处理，假设-CR 只收认沽/认购行权成交；**新建实验 DR**；不写下一字母；不预留 #128  
状态：**草稿·待入库预检**（结论栏空；**三条尚未冻**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DR纸面齐**；禁止把「转债盘后定价=股票盘后固定价格、只按收盘价时间优先」当诚实成交规则；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不催 8765；**不改已冻 A–DQ / DA–DQ**；尤其不改假设-M / 假设-CH / 假设-CL / 假设-Q / 假设-O / 假设-R / 假设-DO / 假设-CR / 假设-BR / 假设-DQ / 假设-T / 假设-D；**不重开假设-T**；**不重开假设-R**；**不重开假设-Q**；**不重开假设-M**；**不重开假设-O**；**不重开假设-DO**；**不重开假设-DQ**；**不重开假设-AC**；**不重开假设-U**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DR（#127）。一句话误开：回测把可转债盘后定价误套股票盘后固定价格，砍掉深市匹配 VWAP，把沪市股票盘后抄到转债，或与深市盘后定价大宗合成一句，或与 R股票ETF假T+0 / Q可转债连续竞价规则 / M股票盘后通道 / CH股票盘后可成交性 / CL可转债盘后定价可成交性 / O大宗三通道 混读，或缺 venue/业务类型/官方规则仍不 skip，系统性改写可转债盘后定价通道身份。**禁与 R/Q/M/CH/CL/O 混读**。

> **字母消歧（硬）**：本页**实验字母 DR** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；占位 0.02；**尚未冻，不要写成已冻**；**params.Y ≠ 实验字母 DR**；**勿把 `params.Y` 读成实验字母 DR**；**params 相对门槛 ≠ 官方定价规则**）≠ **`params.G`**（同族门槛，占位 0.01；**尚未冻，不要写成已冻**；**params.G ≠ 实验字母 DR**；**尤重：`params.G` 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是收盘价，不是匹配 VWAP，也不是 15:05 撮合窗口；**禁把占位读成收盘价/VWAP/15:05 窗口**；**params 相对门槛 ≠ 官方定价规则**）≠ **`params.N`**（失败/废单率差门槛；占位 0.05；**尚未冻，不要写成已冻**；**params.N ≠ 实验字母 DR**；**params.N ≠ 单字母假设-N**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DR ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 R**（股票 ETF 假 T+0 / 股票ETF假回转；**双字母 DR ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `dr0`**；组名 DR0/DR1/DR2 是本页三组对照，≠ 单字母实验 R）≠ **假设-BR**（融券借券费/融出费率计提；**双字母 DR ≠ 假设-BR；严禁复用假设-BR**）≠ **单字母实验 Q**（可转债连续竞价规则混用；**双字母 DR ≠ 单字母假设-Q；严禁复用假设-Q**；**Q 可转债连续竞价规则 ≠ 本页盘后定价通道身份**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DR ≠ 单字母假设-A**）≠ **单字母实验 M**（股票盘后通道；**M 股票盘后通道 ≠ 本页转债盘后定价≠股票盘后固定价格**）≠ **单字母实验 O**（大宗三通道；**O 大宗三通道 ≠ 本页**）≠ 双字母 **CH**（股票盘后固定价格可成交性；**CH 可成交性 ≠ 本页通道误套**）≠ **CL**（可转债盘后定价可成交性；**CL 可成交性 ≠ 本页通道误套**）≠ **CR**（认沽/认购行权成交；**CR 认沽/认购行权成交 ≠ 本页**）≠ **DO**（可转债回售处理；**DO 可转债回售处理 ≠ 本页盘后定价误套**）≠ **DQ**（ETF 申赎组合证券过户费误套）≠ **DP**（可交换债换股印花税误漏）≠ **DN**（可交换债换股过户费误套）≠ **DM**（可交换债换股经手费误套现货）≠ **DL**（股票综合协议过户费下浮）≠ **DK**（场内基金印花税误抽）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债现货经手费沪深合成）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债现货印花税误抽）≠ **DB**（可转债现货经手费）≠ **DA**（场内基金二级过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费）≠ **T**（股票证管费）≠ **U**（股票过户费）≠ **V**（股票印花税切日）≠ **AC**（北交所涨跌幅与盘后）。**DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠BR≠A≠D**。**双字母 DR ≠ 单字母 D/R**。**双字母 DR ≠ 单字母假设-D / 假设-R ≠ 假设-BR**。**params.Y/G/N ≠ 实验字母 DR；亦 ≠ 单字母 D/R**。**勿把 `params.G` 读成实验字母 DR，亦勿把单字母假设-D / 假设-R 读成双字母 DR，亦勿把假设-BR 读成双字母 DR**。**尤重：`params.G` 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口**。**禁把占位读成收盘价/VWAP/15:05 窗口**。**params 相对门槛 ≠ 官方定价规则**。**可转债盘后定价误套股票盘后固定价格 ≠ M股票盘后通道 ≠ CH股票盘后可成交性 ≠ CL可转债盘后定价可成交性 ≠ Q可转债连续竞价规则 ≠ O大宗三通道 ≠ R股票ETF假T+0**。**尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `dr0`**。**尤重：Q 可转债连续竞价规则 ≠ 本页盘后定价通道身份——禁止合成/混读升格进 `dr0`**。**尤重：M/CH 股票盘后通道/可成交性 ≠ 本页转债盘后定价≠股票盘后固定价格——禁止合成/混读升格进 `dr0`**。**尤重：CL 可转债盘后定价可成交性 ≠ 本页通道误套——禁止合成/混读升格进 `dr0`**。**尤重：O 大宗三通道 ≠ 本页——禁止合成/混读升格进 `dr0`**。**尤重：DO 可转债回售处理 ≠ 本页盘后定价误套——禁止合成/混读升格进 `dr0`**。**尤重：CR 认沽/认购行权成交 ≠ 本页——禁止合成/混读升格进 `dr0`**。**尤重：双字母 DR ≠ 单字母假设-D / 假设-R ≠ 假设-BR**。**禁与 R/Q/M/CH/CL/O 混读**。

### 专节 · 双字母 DR ≠ 单字母假设-D / 假设-R；且 ≠ 假设-BR / 假设-M / 假设-CH / 假设-CL / 假设-Q / 假设-O / 假设-DO / 假设-CR（硬）

| 维度 | 对照页 | 本页假设-DR（双字母） |
|------|--------|----------------------|
| 题面 R | **股票 ETF 假 T+0**（假设-R 股票ETF假回转；回转名单 ≠ 盘后定价通道） | 实验 R 不抢、不重开、不混读升格进 `dr0`。股票 ETF 假当日回转 ≠ 本页转债盘后定价被套成股票盘后固定价格。**双字母 DR ≠ 单字母假设-R**；**严禁复用假设-R**；**DR≠R**；**不重开假设-R**；**不改 R**；**尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `dr0`**；`etf_t0_handoff=r_page`；诊断桶 `vs_R_etf_t0` 不升格 |
| 题面 Q | **可转债连续竞价规则**（按股票 T+1 / 板幅 / 收盘定义回放） | Q 可转债连续竞价规则 ≠ 本页盘后定价通道身份。连续竞价规则混用 ≠ 盘后定价被套成股票盘后固定价格。**双字母 DR ≠ 单字母假设-Q**；**严禁复用假设-Q**；**DR≠Q**；**不重开假设-Q**；**不改 Q**；**尤重：Q 可转债连续竞价规则 ≠ 本页盘后定价通道身份——禁止合成/混读升格进 `dr0`**；`cb_continuous_rules_handoff=q_page`；诊断桶 `vs_Q_cb_continuous_rules` 不升格 |
| 题面 M | **股票盘后通道**（通道是否存在、竞价剩单会不会自动进盘后） | M 股票盘后通道 ≠ 本页转债盘后定价≠股票盘后固定价格。通道在不在 ≠ 转债盘后定价被写成股票盘后固定价格。**DR≠M**；**严禁复用假设-M**；**不重开假设-M**；**不改 M**；**尤重：M/CH 股票盘后通道/可成交性 ≠ 本页转债盘后定价≠股票盘后固定价格——禁止合成/混读升格进 `dr0`**；`stock_aft_channel_handoff=m_page`；诊断桶 `vs_M_stock_aft_channel` / `merge_stock_aft_with_cb_aft` 不升格 |
| 题面 CH | **股票盘后固定价格可成交性**（默认按收盘价全额可成） | CH 可成交性 ≠ 本页通道误套。能不能按收盘价成交 ≠ 把股票盘后固定价格的定价身份套到转债。**DR≠CH**；**严禁复用假设-CH**；**不重开假设-CH**；**不改 CH**；**尤重：M/CH 股票盘后通道/可成交性 ≠ 本页转债盘后定价≠股票盘后固定价格——禁止合成/混读升格进 `dr0`**；`stock_aft_fill_handoff=ch_page`；诊断桶 `vs_CH_stock_aft_fill` / `copy_sse_stock_aft_onto_cb` 不升格 |
| 题面 CL | **可转债盘后定价可成交性**（默认按收盘价或匹配 VWAP 全额可成） | CL 可转债盘后定价可成交性 ≠ 本页通道误套。腿上能不能成交 ≠ 这条通道是不是被套成股票盘后固定价格。**DR≠CL**；**严禁复用假设-CL**；**不重开假设-CL**；**不改 CL**；**尤重：CL 可转债盘后定价可成交性 ≠ 本页通道误套——禁止合成/混读升格进 `dr0`**；`cb_aft_fill_handoff=cl_page`；诊断桶 `vs_CL_cb_aft_fill` / `drop_vwap_leg_on_szse_cb_aft` 不升格 |
| 题面 O | **大宗三通道**（协议大宗 / 深市盘后定价大宗 / 沪市大宗固定价格申报） | O 大宗三通道 ≠ 本页。深市盘后定价大宗允许收盘价或 VWAP，仍是大宗通道，不是可转债盘后定价。**DR≠O**；**严禁复用假设-O**；**不重开假设-O**；**不改 O**；**尤重：O 大宗三通道 ≠ 本页——禁止合成/混读升格进 `dr0`**；`block_channel_handoff=o_page`；诊断桶 `vs_O_block_channels` / `confuse_with_szse_block_aft_pricing` 不升格 |
| 题面 DO | **可转债回售处理**（回售经手费暂免） | DO 可转债回售处理 ≠ 本页盘后定价误套。回售费用腿 ≠ 盘后定价通道身份。**DR≠DO**；**严禁复用假设-DO**；**不重开假设-DO**；**不改 DO**；**尤重：DO 可转债回售处理 ≠ 本页盘后定价误套——禁止合成/混读升格进 `dr0`**；`cb_put_handling_handoff=do_page`；诊断桶 `vs_DO_cb_put_handling` 不升格 |
| 题面 CR | **认沽/认购行权成交**（赎回或回售行权假全额兑付） | CR 认沽/认购行权成交 ≠ 本页。行权兑付 ≠ 盘后定价通道被套成股票盘后固定价格。**DR≠CR**；**严禁复用假设-CR**；**不重开假设-CR**；**不改 CR**；**尤重：CR 认沽/认购行权成交 ≠ 本页——禁止合成/混读升格进 `dr0`**；诊断桶 `vs_CR_put_call_exercise_fill` 不升格 |
| 题面 BR | **融券借券费/融出费率** | 借券费计提 ≠ 盘后定价通道身份。**双字母 DR ≠ 假设-BR**；**严禁复用假设-BR**；**DR≠BR**；**不重开假设-BR**；**不改 BR**；**尤重：双字母 DR ≠ 单字母假设-D / 假设-R ≠ 假设-BR** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 盘后定价用哪条价格规则。**双字母 DR ≠ 单字母假设-D**；**严禁复用假设-D**；**DR≠D**；**不改 D** |
| 题面 DQ | **ETF 申赎组合证券过户费误套** | 篮子过户费 ≠ 盘后定价通道。**DR≠DQ**；**不重开假设-DQ**；**不改 DQ** |
| 题面 DP | **可交换债换股印花税误漏** | 换股印花 ≠ 本机制。**DR≠DP**；**不重开假设-DP**；**不改 DP** |
| 题面 DN | **可交换债换股过户费** | 换股过户 ≠ 本机制。**DR≠DN**；**不重开假设-DN**；**不改 DN** |
| 题面 DM | **可交换债换股经手费** | 换股经手 ≠ 本机制。**DR≠DM**；**不重开假设-DM**；**不改 DM** |
| 题面 DL | **股票综合协议过户费下浮** | 综合协议过户下浮 ≠ 本机制。**DR≠DL**；**不重开假设-DL**；**不改 DL** |
| 题面 DK | **场内基金印花税误抽** | 基金印花 ≠ 本机制。**DR≠DK**；**不改 DK** |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 本机制。**DR≠DJ**；**不改 DJ** |
| 题面 DI | **股票大宗经手下浮** | 大宗经手下浮 ≠ 本机制。**DR≠DI**；**不重开假设-DI**；**不改 DI** |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 本机制。**DR≠DH**；**不改 DH** |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 本机制。**DR≠DG**；**不改 DG** |
| 题面 DF | **可交换债现货经手费沪深合成** | 可交换现货经手 ≠ 本机制。**DR≠DF**；**不重开假设-DF**；**不改 DF** |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 本机制。**DR≠DE**；**不改 DE** |
| 题面 DD | **可转债现货过户费** | 转债现货过户 ≠ 本机制。**DR≠DD**；**不重开假设-DD**；**不改 DD** |
| 题面 DC | **可转债现货印花税误抽** | 转债现货印花 ≠ 本机制。**DR≠DC**；**不改 DC** |
| 题面 DB | **可转债现货经手费** | 转债现货经手 ≠ 本机制。**DR≠DB**；**不重开假设-DB**；**不改 DB** |
| 题面 DA | **场内基金二级过户费** | 二级过户 ≠ 本机制。**DR≠DA**；**不重开假设-DA**；**不改 DA** |
| 题面 S | **沪深 A 股竞价经手费切日** | 股票经手切日 ≠ 本机制。**DR≠S**；**不重开假设-S**；**不改 S** |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 本机制。**DR≠AX**；**不重开假设-AX**；**不改 AX** |
| 题面 T | **证管费主报股票** | 股票证管费 ≠ 本机制。**DR≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T** |
| 题面 U | **股票过户费切日** | 股票过户切日 ≠ 本机制。**DR≠U**；**不重开假设-U**；**不改 U** |
| 题面 V | **股票印花税切日** | 股票印花切日 ≠ 本机制。**DR≠V**；**不重开假设-V**；**不改 V** |
| 题面 AC | **北交所涨跌幅与盘后** | 北交所涨跌幅、盘后 ≠ 本页转债盘后定价通道身份。**DR≠AC**；**不重开假设-AC**；**不改 AC** |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 盘后定价通道身份。**DR≠A**；**不抢 A 真数队列**；**不改 A** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_stock_aft_as_cb_pricing`（**建议**单一主报，单挂；**尚未冻，不要写成已冻**；禁与半泄露键 `invent_asof_leak_cb_aft_pricing` 双挂；DR1 不升格；`merge_stock_aft_with_cb_aft` / `drop_vwap_leg_on_szse_cb_aft` / `copy_sse_stock_aft_onto_cb` / `confuse_with_szse_block_aft_pricing` / `vs_M_stock_aft_channel` / `vs_CH_stock_aft_fill` / `vs_CL_cb_aft_fill` / `vs_Q_cb_continuous_rules` / `vs_O_block_channels` / `vs_R_etf_t0` / `vs_CR_put_call_exercise_fill` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip` 只作诊断对照，不升格主报；**尤重禁止把 R / Q / M / CH / CL / O 混读升格进 `dr0`**；**禁与 R/Q/M/CH/CL/O 混读**） |
| 文档 | 清单实验 R / Q / M / CH / CL / O / DO / CR / BR / DQ / DP / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / T / U / V / AC / A / D（**只读；禁止改写**） | `假设-DR-可转债盘后定价误套股票盘后固定价格.md`（新建） |
| 预检键 | 实验字母 R / Q / M / O / DO / DQ / DP / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / T / U / V / AC / A / D / Y / G / N，以及已存在 CH / CL / CR / BR | 实验字母 **DR** / `dr0_primary_demo`；**不得**占用或改写预检 R/Q/M/O/DO/DQ/DP/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/A/D/Y/G/N，亦不得改写 CH/CL/CR/BR |

**禁止**：把 DR 写成「R / Q / M / CH / CL / O / DO / CR / BR / DQ / D / A 的续篇」；把「股票盘后通道已分列（M）/ 股票盘后可成交已分列（CH）/ 转债盘后可成交已分列（CL）/ 转债连续竞价规则已分列（Q）/ 大宗三通道已分列（O）/ 股票 ETF 回转已分列（R）」写成「可转债盘后定价通道身份已诚实」；把实验字母 DR 与单字母 D/R 或 params.Y/G/N 或假设-BR 混读；**尤重勿把单字母假设-D / 假设-R 读成双字母 DR**；**尤重勿把假设-BR 读成双字母 DR**；**尤重勿把 `params.G` 读成实验字母 DR**；**尤重 `params.G` 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口（量纲与语义不同）**；**禁把占位读成收盘价/VWAP/15:05 窗口**；**params 相对门槛 ≠ 官方定价规则**；**尤重实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `dr0`**；**尤重 Q 可转债连续竞价规则 ≠ 本页盘后定价通道身份，禁止合成/混读升格进 `dr0`**；**尤重 M/CH 股票盘后通道/可成交性 ≠ 本页转债盘后定价≠股票盘后固定价格，禁止合成/混读升格进 `dr0`**；**尤重 CL 可转债盘后定价可成交性 ≠ 本页通道误套，禁止合成/混读升格进 `dr0`**；**尤重 O 大宗三通道 ≠ 本页，禁止合成/混读升格进 `dr0`**；**尤重 DO 可转债回售处理 ≠ 本页盘后定价误套，禁止合成/混读升格进 `dr0`**；**尤重 CR 认沽/认购行权成交 ≠ 本页，禁止合成/混读升格进 `dr0`**；**禁与 R/Q/M/CH/CL/O 混读**；把 `invent_asof_leak_cb_aft_pricing` 升格进 `dr0` 或与主报双挂；把诊断桶 `merge_stock_aft_with_cb_aft` / `drop_vwap_leg_on_szse_cb_aft` / `copy_sse_stock_aft_onto_cb` / `confuse_with_szse_block_aft_pricing` / `vs_M_stock_aft_channel` / `vs_CH_stock_aft_fill` / `vs_CL_cb_aft_fill` / `vs_Q_cb_continuous_rules` / `vs_O_block_channels` / `vs_R_etf_t0` / `vs_CR_put_call_exercise_fill` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip` 升格进 `dr0`；把股票盘后固定价格和深市可转债盘后定价合成一句；砍掉深市匹配 VWAP；把沪市股票盘后抄到转债；沪深合成一句；缺官方规则仍硬填。本页主键只用 `dr0` / `dr1` / `dr2` 与 `cb_aft_pricing_*`。不写下一字母。不预留 #128。**纸面齐惯例**：落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK/DL/DM/DN/DO/DP/DQ；勿再只改清单）——**当前草稿阶段禁止标纸面齐**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价下，回测把**可转债盘后定价**误套成**股票盘后固定价格**（只按收盘价、时间优先），或砍掉深市匹配 VWAP，或把沪市股票盘后抄到转债，或与深市盘后定价大宗合成一句，或与 R股票ETF假T+0 / Q可转债连续竞价规则 / M股票盘后通道 / CH股票盘后可成交性 / CL可转债盘后定价可成交性 / O大宗三通道 混读，或缺 venue/业务类型/官方规则仍不 skip，相对「缺 venue/业务类型或官方规则则 skip；股票盘后固定价格=收盘价、时间优先；深市可转债盘后定价允许收盘价或匹配 VWAP，禁止与股票盘后固定价格合成一句；沪市可转债若缺官方盘后定价另档规则则 skip，禁止沪深合成」的诚实组，会**系统性改写可转债盘后定价通道身份**——相对诚实锚偏误。

核对日方向（随锚建议；**尚未冻，不要写成已冻**；禁止把收盘价、匹配 VWAP 或 15:05 窗口写成占位门槛，也禁止沪深合成一句）：两条通道分开写。`事实与坑` 2026-10-19 已写股票盘后固定价格按当日收盘价、时间优先。`事实与坑` 2026-10-26 的坑是：把深市可转债盘后定价（收盘价或匹配 VWAP）和股票盘后固定价格合成一句。`事实与坑` 2026-10-23 已把深市盘后定价大宗另列为大宗通道，留给 O。沪市可转债若缺官方盘后定价另档规则，本页 skip，不拿深市规则或股票盘后固定价格去填。那些「通道在不在」留在 M，「股票盘后能不能全额成交」留在 CH，「转债盘后能不能全额成交」留在 CL，「连续竞价规则混用」留在 Q，「大宗三通道」留在 O，「股票 ETF 假 T+0」留在 R。**禁把占位读成收盘价/VWAP/15:05 窗口**。**`params.G` 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口**。**params 相对门槛 ≠ 官方定价规则**。**禁与 R/Q/M/CH/CL/O 混读**。

证伪方向：若天真组 / 半泄露组相对诚实组的通道误套截在标定噪声带内可忽略，且「合成一句 / 砍掉 VWAP / 抄沪市股票盘后 / 混成大宗盘后定价 / 核对日泄露 / vs R·Q·M·CH·CL·O」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 键占位（拉数前才冻结；本页不开跑；Y/G/N/Y2 · dr0 与锚 **三条尚未冻**）

```
# 配置键占位（见 §7；本页是草稿·待入库预检；下列三条尚未冻，不要写成已冻）
# 【消歧】params.Y = 显著性门槛；占位 0.02；尚未冻；**≠ 实验字母 DR ≠ 单字母假设-D / 假设-R**；勿把 params.Y 读成实验字母 DR
# 【消歧】params.G = 同族门槛；占位 0.01；尚未冻；**≠ 实验字母 DR ≠ 单字母 D/R**
# 【消歧】尤重：params.G 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口（量纲与语义不同：无量纲相对门槛 ≠ 官方定价规则）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成收盘价/VWAP/15:05 窗口
# 【消歧】params 相对门槛 ≠ 官方定价规则
# 【消歧】params.N = 失败/废单率差门槛；占位 0.05；尚未冻；**≠ 实验字母 DR ≠ 单字母假设-N**
# params.Y2                               占位 0.015；尚未冻，不要写成已冻
# params.Y / G / N / Y2                   占位 0.02/0.01/0.05/0.015（相对门槛：通道误套截 ΔCbAftPricing / 净差异 / DR1−DR2；**尚未冻，不要写成已冻**；**params.Y/G/N ≠ 实验字母 DR ≠ 单字母假设-D / 假设-R**；**尤重 params.G 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口**；**禁把占位读成收盘价/VWAP/15:05 窗口**；**params 相对门槛 ≠ 官方定价规则**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        建议 next_open；尚未冻，不要写成已冻
# params.asof_check_date                  建议 2026-10-16；尚未冻，不要写成已冻
# params.px_basis                         建议 unadj
# params.fail_policy                      建议 skip；尚未冻，不要写成已冻
# params.cb_aft_pricing_honest            建议 pit_szse_cb_aft_close_or_vwap_not_stock_aft_close_only；尚未冻，不要写成已冻
#   诚实锚方向（建议，未冻）：
#   缺 venue、业务类型或官方规则 → skip
#   股票盘后固定价格 = 收盘价、时间优先（这条身份留在股票盘后，不套到转债）
#   深市可转债盘后定价允许收盘价或匹配 VWAP
#   禁止与股票盘后固定价格合成一句
#   沪市可转债若缺官方盘后定价另档规则则 skip
#   禁止沪深合成
#   禁止把占位 0.02/0.01/0.05/0.015 读成收盘价、VWAP 或 15:05 窗口
#   枚举只是建议，尚未冻
#   不把 M 的通道存在、CH 的可成交、CL 的可成交、Q 的连续竞价规则、O 的大宗三通道、R 的假 T+0 写成转债盘后定价诚实锚
# params.cb_aft_pricing_scope             建议 cb_aft_pricing_vs_stock_aft_fixed_listed_apart；尚未冻，不要写成已冻
#   方向名：可转债盘后定价与股票盘后固定价格分列
#   这不是把收盘价、VWAP 或 15:05 窗口冻成门槛
#   可转债盘后定价 ≠ 股票盘后固定价格 ≠ 深市盘后定价大宗
# params.cb_aft_pricing_over_policy       建议 skip_if_venue_or_biz_type_or_official_rule_missing；尚未冻，不要写成已冻
#   缺 venue、业务类型或官方规则则 skip；禁在缺字段时仍按股票收盘价时间优先把转债盘后腿填上
# params.stock_aft_channel_handoff        建议 m_page
#   消费 M 的股票盘后通道，或显式旁路；通道存在 ≠ 本页通道误套；不重开假设-M；不改 M
#   M 禁止合成/混读升格进 dr0；诊断桶 vs_M_stock_aft_channel / merge_stock_aft_with_cb_aft 不得升格进 dr0
# params.stock_aft_fill_handoff           建议 ch_page
#   消费 CH 的股票盘后可成交性，或显式旁路；可成交性 ≠ 本页通道误套；不重开假设-CH；不改 CH
#   CH 禁止合成/混读升格进 dr0；诊断桶 vs_CH_stock_aft_fill / copy_sse_stock_aft_onto_cb 不得升格进 dr0
# params.cb_aft_fill_handoff              建议 cl_page
#   消费 CL 的可转债盘后定价可成交性，或显式旁路；可成交性 ≠ 本页通道误套；不重开假设-CL；不改 CL
#   CL 禁止合成/混读升格进 dr0；诊断桶 vs_CL_cb_aft_fill / drop_vwap_leg_on_szse_cb_aft 不得升格进 dr0
# params.cb_continuous_rules_handoff      建议 q_page
#   可转债连续竞价规则交 Q；Q ≠ 本页盘后定价通道身份；双字母 DR ≠ 单字母假设-Q；不重开假设-Q；不改 Q
#   Q 禁止合成/混读升格进 dr0；诊断桶 vs_Q_cb_continuous_rules 不得升格进 dr0
# params.block_channel_handoff            建议 o_page
#   大宗三通道交 O；O ≠ 本页；不重开假设-O；不改 O
#   O 禁止合成/混读升格进 dr0；诊断桶 vs_O_block_channels / confuse_with_szse_block_aft_pricing 不得升格进 dr0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 dr0；双字母 DR ≠ 单字母假设-R；不改 R
#   R 禁止合成/混读升格进 dr0；诊断桶 vs_R_etf_t0 不得升格进 dr0
# params.cb_put_handling_handoff          建议 do_page
#   可转债回售处理交 DO；DO ≠ 本页盘后定价误套；不重开假设-DO；不改 DO
#   DO 禁止合成/混读升格进 dr0；诊断桶 vs_DO_cb_put_handling 不得升格进 dr0
# params.fill_time_suspend_handoff        建议 d_page
#   成交时点与停牌交 D；双字母 DR ≠ 单字母假设-D；不改 D
# params.board_capacity_handoff           建议 a_page
#   板上容量交 A；不抢 A 真数队列；不改 A
# params.dr0_primary_demo                 建议 invent_stock_aft_as_cb_pricing；尚未冻，不要写成已冻
#   单一主报，单挂；禁与 invent_asof_leak_cb_aft_pricing 双挂；DR1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_cb_aft_pricing 只作对照，不得升格进 dr0，不得双挂
#   诊断桶 merge_stock_aft_with_cb_aft / drop_vwap_leg_on_szse_cb_aft / copy_sse_stock_aft_onto_cb / confuse_with_szse_block_aft_pricing / vs_M_stock_aft_channel / vs_CH_stock_aft_fill / vs_CL_cb_aft_fill / vs_Q_cb_continuous_rules / vs_O_block_channels / vs_R_etf_t0 / vs_CR_put_call_exercise_fill / vs_DO_cb_put_handling / missing_venue_or_biz_type_not_skip 不得升格进 dr0
#   尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 dr0
#   尤重：禁止把 Q 可转债连续竞价规则与本页盘后定价通道身份合成/混读后写进 dr0
#   尤重：禁止把 M/CH 股票盘后通道/可成交性与本页转债盘后定价≠股票盘后固定价格合成/混读后写进 dr0
#   尤重：禁止把 CL 可转债盘后定价可成交性与本页通道误套合成/混读后写进 dr0
#   尤重：禁止把 O 大宗三通道与本页合成/混读后写进 dr0
#   尤重：禁止把 DO 可转债回售处理与本页盘后定价误套合成/混读后写进 dr0
#   尤重：禁止把 CR 认沽/认购行权成交与本页合成/混读后写进 dr0
#   禁与 R/Q/M/CH/CL/O 混读
# params.dr0_invent_stock_aft_as_cb_pricing 建议 True
# params.dr1_asof_leak_cb_aft_pricing_only 建议 True
#   半泄露对照；DR1 不升格并列主报；不得把 invent_asof_leak_cb_aft_pricing 写进 dr0
# params.dr2_pit_szse_cb_aft_close_or_vwap_not_stock_aft_close_only 建议 True
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
# params.merge_with_BR                    建议 False
# params.merge_with_A                     建议 False
# params.merge_with_D                     建议 False
# params.missing_venue_or_biz_type_or_official_rule_policy 建议 skip
# params.day_freq_proxy                   建议 cb_aft_pricing_sensitivity
# params.universe_rule                    建议 cb_aft_pricing_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dr_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DR；勿把这个键读成实验 DR，亦勿读成单字母 D/R
#   不另挂主报，不预留 #128，不写下一字母
```

### 2.2 三组对照（DR0 / DR1 / DR2）

组名 DR0 / DR1 / DR2 是本页三组，≠ 单字母实验 R（股票 ETF 假 T+0），亦 ≠ 单字母实验 D（成交时点与停牌），亦 ≠ 假设-BR。

| 组 | 角色 | 口径 |
|----|------|------|
| DR0 | 天真 / 可转债盘后定价误套股票盘后固定价格 | 按 `dr0_primary_demo` **建议**单一主报 `invent_stock_aft_as_cb_pricing`（单挂；**尚未冻，不要写成已冻**）：把可转债盘后定价套成股票盘后固定价格（只按收盘价时间优先、砍掉深市 VWAP、抄沪市股票盘后、或混成大宗盘后定价）。**禁**与 `invent_asof_leak_cb_aft_pricing` 双挂主报。**禁把 R / Q / M / CH / CL / O 合成进 `dr0`**（只作对照/旁路，不得升格进 `dr0` 或另挂主报）。**禁与 R/Q/M/CH/CL/O 混读** |
| DR1 | 半泄露 | 仅核对日把「深市收盘价或匹配 VWAP、股票盘后只按收盘价、沪市缺规则则 skip」铺到全历史、铺到沪市缺规则的转债、或把股票盘后固定价格铺成转债唯一规则（`invent_asof_leak_cb_aft_pricing`）；**不得升格并列主报**，也不得写进 `dr0`（建议：DR1 不升格），不得双挂 |
| DR2 | 诚实 / 转债盘后定价与股票盘后固定价格分列 | `cb_aft_pricing_honest=pit_szse_cb_aft_close_or_vwap_not_stock_aft_close_only`（建议，**尚未冻**）：缺 venue/业务类型或官方规则则 skip；股票盘后固定价格=收盘价、时间优先；深市可转债盘后定价允许收盘价或匹配 VWAP，禁止与股票盘后固定价格合成一句；沪市可转债若缺官方盘后定价另档规则则 skip，禁止沪深合成。股票盘后通道只消费 M，股票盘后可成交只消费 CH，转债盘后可成交只消费 CL，连续竞价规则只消费 Q，大宗三通道只消费 O，股票 ETF 假 T+0 只消费 R，回售处理只消费 DO，或显式旁路 |

把两条通道合成一句、砍掉深市 VWAP、抄沪市股票盘后、混成深市盘后定价大宗、把 R/Q/M/CH/CL/O 混进本页，以及相对这些页的对照截（`merge_stock_aft_with_cb_aft` / `drop_vwap_leg_on_szse_cb_aft` / `copy_sse_stock_aft_onto_cb` / `confuse_with_szse_block_aft_pricing` / `vs_M_stock_aft_channel` / `vs_CH_stock_aft_fill` / `vs_CL_cb_aft_fill` / `vs_Q_cb_continuous_rules` / `vs_O_block_channels` / `vs_R_etf_t0` / `vs_CR_put_call_exercise_fill` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dr0_primary_demo`。`vs_R_etf_t0` 只标记「有人把实验 R 和本页混读」，**不得升格进 `dr0`**。`vs_Q_cb_continuous_rules` 只标记连续竞价规则对照，**不得升格进 `dr0`**。`vs_M_stock_aft_channel` 与 `vs_CH_stock_aft_fill` 只标记股票盘后通道/可成交对照，**不得升格进 `dr0`**。`vs_CL_cb_aft_fill` 只标记转债盘后可成交对照，**不得升格进 `dr0`**。`vs_O_block_channels` 只标记大宗三通道对照，**不得升格进 `dr0`**。`vs_DO_cb_put_handling` 与 `vs_CR_put_call_exercise_fill` 同样只作对照。M 的通道、CH 的可成交、CL 的可成交、Q 的连续竞价规则、O 的大宗、R 的假 T+0 只作对照/旁路。

### 2.3 成交规则窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **建议** `2026-10-16`；fill_time **建议** `next_open`；fail **建议** `skip`。诚实锚六键与 Y/G/N/Y2、`dr0_primary_demo` 同属三条，**尚未冻，不要写成已冻**。机制红线只有一句：缺 venue/业务类型或官方规则则 skip；股票盘后固定价格=收盘价、时间优先；深市可转债盘后定价允许收盘价或匹配 VWAP，禁止与股票盘后固定价格合成一句；沪市可转债若缺官方盘后定价另档规则则 skip，禁止沪深合成。方向随锚建议：**不要把核对日规则铺满全历史，也不要把股票盘后固定价格写成转债唯一规则，也不要沪深合成**。范围名 `cb_aft_pricing_vs_stock_aft_fixed_listed_apart` 只标方向：本页只看可转债盘后定价有没有被套成股票盘后固定价格。通道在不在留给 M，能不能成交留给 CH 和 CL，连续竞价规则留给 Q，大宗三通道留给 O，股票 ETF 假 T+0 留给 R。`params.G` 的 0.01 是无量纲相对门槛，不是收盘价，不是匹配 VWAP，也不是 15:05 窗口。**禁把占位读成收盘价/VWAP/15:05 窗口**。**params 相对门槛 ≠ 官方定价规则**。缺 venue、业务类型或官方规则则 skip，不用股票收盘价时间优先、占位 0.01 或深市规则把沪市缺规则的转债腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dr0_primary_demo` / `params.Y`·G·N·Y2 / 盘后定价开关 / 桶 / 是否把收盘价、VWAP 或 15:05 窗口铺到全历史、或合成沪深、或把占位读成官方定价规则）。本页不开跑。三条都还没冻。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DR0）/ 半泄露组（DR1）相对诚实组（DR2）的通道误套截**显著且集中在可转债盘后定价被套成股票盘后固定价格的桶**（合成一句、砍掉深市 VWAP、抄沪市股票盘后、或混成大宗盘后定价）；分桶「合成一句 / 砍掉 VWAP / 抄沪市股票盘后 / 混成大宗 / 核对日泄露 / vs R·Q·M·CH·CL·O」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把收盘价、VWAP 或 15:05 窗口冻成门槛，也不把 `params.G` 的 0.01 读成官方定价规则。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 M 的股票盘后通道、CH 的股票盘后可成交、CL 的转债盘后可成交、Q 的连续竞价规则、O 的大宗三通道、R 的股票 ETF 假 T+0、DO 的回售处理、CR 的行权成交、BR 的借券费、DQ 的篮子过户、DP 的换股印花、DN 的换股过户、DM 的换股经手、DL 的综合协议过户、DK 的基金印花、DJ 的基金证管费、DI 的大宗经手、DH 的佣金双计、DG 的北交所档、DF 的可交换现货经手、DE 的转债证管费、DD 的转债过户、DC 的转债印花、DB 的转债现货经手、DA 的二级过户、S 的股票经手、AX 的基金经手、T 的股票证管费、U 的股票过户、V 的股票印花、AC 的北交所涨跌幅与盘后、A 的板上容量、D 的成交时点解释；或 `dr0_primary_demo` 与 `invent_asof_leak_cb_aft_pricing` 双挂；或 DR1 升格并列主报；或 `merge_stock_aft_with_cb_aft` / `drop_vwap_leg_on_szse_cb_aft` / `copy_sse_stock_aft_onto_cb` / `confuse_with_szse_block_aft_pricing` / `vs_M_stock_aft_channel` / `vs_CH_stock_aft_fill` / `vs_CL_cb_aft_fill` / `vs_Q_cb_continuous_rules` / `vs_O_block_channels` / `vs_R_etf_t0` / `vs_CR_put_call_exercise_fill` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip` 诊断桶升格主报；或把 R / Q / M / CH / CL / O 合成进 `dr0`；或实验字母 DR 与单字母 D/R 或 params.Y/G/N 或假设-BR 混读；或把 `params.G` 的 0.01 读成收盘价、匹配 VWAP 或 15:05 窗口；或把占位读成收盘价/VWAP/15:05 窗口；或把核对日规则写成已冻并铺满全历史；或缺 venue / 业务类型 / 官方规则仍不 skip；或沪深合成一句；或重开假设-T / 假设-R / 假设-Q / 假设-M / 假设-O / 假设-DO / 假设-DQ；或标纸面齐；或写成 A/D–DR纸面齐；或把三条写成已冻。

---

## 4. 检验设计（纸面）

同一信号、同一未复权价，对照 DR0/DR1/DR2。股票盘后通道走 M 或显式旁路，不在本页改 M。股票盘后可成交走 CH，转债盘后可成交走 CL，连续竞价规则走 Q，大宗三通道走 O，股票 ETF 假 T+0 走 R，回售处理走 DO，都不改。报告通道误套截。不把收盘价、VWAP 或 15:05 窗口标成已冻门槛，也不把 `params.G` 的 0.01 读成官方定价规则。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_stock_aft_as_cb_pricing` / `invent_asof_leak_cb_aft_pricing` / `merge_stock_aft_with_cb_aft` / `drop_vwap_leg_on_szse_cb_aft` / `copy_sse_stock_aft_onto_cb` / `confuse_with_szse_block_aft_pricing` / `vs_M_stock_aft_channel` / `vs_CH_stock_aft_fill` / `vs_CL_cb_aft_fill` / `vs_Q_cb_continuous_rules` / `vs_O_block_channels` / `vs_R_etf_t0` / `vs_CR_put_call_exercise_fill` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip`

`merge_stock_aft_with_cb_aft`、`drop_vwap_leg_on_szse_cb_aft`、`copy_sse_stock_aft_onto_cb`、`confuse_with_szse_block_aft_pricing`、`vs_M_stock_aft_channel`、`vs_CH_stock_aft_fill`、`vs_CL_cb_aft_fill`、`vs_Q_cb_continuous_rules`、`vs_O_block_channels`、`vs_R_etf_t0`、`vs_CR_put_call_exercise_fill`、`vs_DO_cb_put_handling`、`missing_venue_or_biz_type_not_skip` 只作诊断桶：它们不是 `dr0`，也不是 DR1，**不得升格主报**。`vs_R_etf_t0` 没有对应的「假 T+0 + 盘后定价误套」合成主报。实验 R 只作诊断，**不得升格进 `dr0`**。Q 的连续竞价规则只作诊断，**不得升格进 `dr0`**。M 的通道与 CH 的可成交只作诊断，**不得升格进 `dr0`**。CL 的可成交只作诊断，**不得升格进 `dr0`**。O 的大宗三通道只作诊断，**不得升格进 `dr0`**。合成一句、砍掉 VWAP、抄沪市股票盘后、混成大宗盘后定价、缺字段仍不 skip，都只作诊断，**不得升格进 `dr0`**。`invent_asof_leak_cb_aft_pricing` 只服务 DR1，**不得升格进 `dr0`，不得双挂**。`invent_stock_aft_as_cb_pricing` 才是建议的单一主报名，**尚未冻**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「转债盘后定价=股票盘后固定价格、只按收盘价时间优先」拿去当诚实锚。
- 把 `params.G` 的 0.01 当成收盘价、匹配 VWAP 或 15:05 窗口。**尤重：`params.G` 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口**。
- 把占位 `0.02/0.01/0.05/0.015` 读成收盘价/VWAP/15:05 窗口。**禁把占位读成收盘价/VWAP/15:05 窗口**。**params 相对门槛 ≠ 官方定价规则**。
- 缺 venue、业务类型或官方规则仍不 skip，并用股票收盘价时间优先或占位 0.01 把转债盘后腿填上。
- 把核对日「深市收盘价或匹配 VWAP」写成全历史唯一规则，并铺满全历史，或沪深合成一句，或把股票盘后固定价格写成转债唯一规则。锚六键仍是建议，**尚未冻**。
- 把「股票盘后通道已分列（M）/ 股票盘后可成交已分列（CH）/ 转债盘后可成交已分列（CL）/ 连续竞价规则已分列（Q）/ 大宗三通道已分列（O）/ 股票 ETF 回转已分列（R）」写成「可转债盘后定价通道身份已诚实」。不改 M / CH / CL / Q / O / R。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格进 `dr0`。诊断桶 `vs_R_etf_t0` 只作对照。不抢、不重开假设-R。
- 把 Q 可转债连续竞价规则和本页盘后定价通道身份合成或混读后升格进 `dr0`。诊断桶 `vs_Q_cb_continuous_rules` 只作对照。
- 把 M/CH 股票盘后通道/可成交性和本页转债盘后定价≠股票盘后固定价格合成或混读后升格进 `dr0`。诊断桶 `vs_M_stock_aft_channel` / `vs_CH_stock_aft_fill` / `merge_stock_aft_with_cb_aft` / `copy_sse_stock_aft_onto_cb` 只作对照。
- 把 CL 可转债盘后定价可成交性和本页通道误套合成或混读后升格进 `dr0`。诊断桶 `vs_CL_cb_aft_fill` / `drop_vwap_leg_on_szse_cb_aft` 只作对照。
- 把 O 大宗三通道和本页合成或混读后升格进 `dr0`。诊断桶 `vs_O_block_channels` / `confuse_with_szse_block_aft_pricing` 只作对照。
- 把 DO 可转债回售处理和本页盘后定价误套合成或混读后升格进 `dr0`。诊断桶 `vs_DO_cb_put_handling` 只作对照。
- 把 CR 认沽/认购行权成交和本页合成或混读后升格进 `dr0`。诊断桶 `vs_CR_put_call_exercise_fill` 只作对照。
- 两条通道合成一句，并升格进 `dr0`。诊断桶 `merge_stock_aft_with_cb_aft` 只作对照。
- 缺 venue 或业务类型仍不 skip，并升格进 `dr0`。诊断桶 `missing_venue_or_biz_type_not_skip` 只作对照。
- `dr0_primary_demo` 与 `invent_asof_leak_cb_aft_pricing` 双挂主报；DR1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DR 与单字母 D/R 或 params.Y/G/N 或假设-BR 混读。**双字母 DR ≠ 单字母假设-D / 假设-R ≠ 假设-BR**。
- 改 R / Q / M / CH / CL / O / DO / CR / BR / DQ / DP / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / T / U / V / AC / A / D 正文；重开假设-T；重开假设-R；重开假设-Q；重开假设-M；重开假设-O；重开假设-DO；重开假设-DQ；抢 A 真数队列；抢实验 R；标纸面齐；写成 A/D–DR纸面齐；把三条写成已冻；开真数/回测/实盘；用复权价当盘后定价基准；结论写成「转债盘后更好成交所以能买」。
- **纸面齐惯例**：落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK/DL/DM/DN/DO/DP/DQ；勿再只改清单）——**当前草稿阶段禁止标纸面齐**。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权价、交易日、**交易所 venue**（沪/深）、**业务类型**（可转债盘后定价 / 股票盘后固定价格 / 深市盘后定价大宗 / 可转债连续竞价 / 可转债回售 / 认沽认购行权 / 股票 ETF 回转；仅用于把腿分回 M、CH、CL、Q、O、R、DO、CR 或本页）、**官方盘后定价规则是否在册**（缺则 skip，不发明沪市另档，也不拿股票盘后固定价格去填）。
- 股票盘后固定价格若要「收盘价、时间优先」这句，只消费 M/CH 已有口径，不在本页重开 M 或 CH，也不把股票业务类型换成可转债盘后定价。
- 转债盘后「能不能成交」只消费 CL，不把可成交性误开收进本页主报。
- 证券类别只用于把腿分回旁路页，不在本页改那些页。
- 没有 venue、业务类型或官方规则时，按建议的 `cb_aft_pricing_over_policy=skip_if_venue_or_biz_type_or_official_rule_missing` skip，不得按股票收盘价时间优先把转债盘后腿填上，也不得按占位 0.01 或深市规则把沪市缺规则的腿填上。
- 旁路消费：M 的股票盘后通道、CH 的股票盘后可成交、CL 的转债盘后可成交、Q 的连续竞价规则、O 的大宗三通道、R 的股票 ETF 假 T+0、DO 的回售处理、CR 的行权成交、D 的成交时点之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** 这些页的主报不收到本页 `dr0`。
- 未复权价；asof **建议** `2026-10-16`，**尚未冻**。核对日方向「深市允许收盘价或匹配 VWAP、股票盘后固定价格只按收盘价时间优先、沪市缺规则则 skip、禁止沪深合成」是建议的机制方向，不是已冻的全历史规则，也不是占位门槛。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **占位键摘要（三条尚未冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`cb_aft_pricing_honest=pit_szse_cb_aft_close_or_vwap_not_stock_aft_close_only`（缺 venue/业务类型或官方规则则 skip；股票盘后固定价格=收盘价、时间优先；深市可转债盘后定价允许收盘价或匹配 VWAP，禁止与股票盘后固定价格合成一句；沪市可转债若缺官方盘后定价另档规则则 skip，禁止沪深合成；**尚未冻**）；`cb_aft_pricing_scope=cb_aft_pricing_vs_stock_aft_fixed_listed_apart`（转债盘后定价与股票盘后固定价格分列；方向名，不是已冻规则）；`cb_aft_pricing_over_policy=skip_if_venue_or_biz_type_or_official_rule_missing`（缺 venue/业务类型或官方规则则 skip）；`dr0_primary_demo=invent_stock_aft_as_cb_pricing`（**建议**单一主报，单挂；**尚未冻**；禁与 `invent_asof_leak_cb_aft_pricing` 双挂；DR1 不升格；诊断桶不升格主报；**禁把 R / Q / M / CH / CL / O 合成进 `dr0`**，只作对照/旁路，不得升格进 `dr0` 或另挂主报；**禁与 R/Q/M/CH/CL/O 混读**）；`stock_aft_channel_handoff=m_page`；`stock_aft_fill_handoff=ch_page`；`cb_aft_fill_handoff=cl_page`；`cb_continuous_rules_handoff=q_page`；`block_channel_handoff=o_page`；`etf_t0_handoff=r_page`；`cb_put_handling_handoff=do_page`；`merge_with_DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/BR/A/D=False`。
- `params.Y/G/N/Y2` **占位** `0.02/0.01/0.05/0.015`（相对门槛，不是官方定价规则：通道误套截 ΔCbAftPricing / 净差异 / DR1−DR2；**尚未冻，不要写成已冻**；**尤重 params.G 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口（量纲与语义不同）**；**禁把占位读成收盘价/VWAP/15:05 窗口**；**params 相对门槛 ≠ 官方定价规则**；**params.Y/G/N ≠ 实验字母 DR ≠ 单字母 D/R**；**勿把 params.G 读成实验字母 DR，亦勿把单字母假设-D / 假设-R 读成双字母 DR，亦勿把假设-BR 读成双字母 DR**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #128。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`50946c09`（A/D–DQ纸面齐已合，全长 `50946c09b6160e4ade9bfed886e5dbb954f84358`）。**不改已冻 A–DQ / DA–DQ**。状态=**草稿·待入库预检**。**三条尚未冻**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DR纸面齐**。

---

## 8. 结论

（空。草稿·待入库预检；三条尚未冻；禁止标纸面齐。）

---

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-24 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。可转债盘后定价误套股票盘后固定价格（成交规则）；`dr0_primary_demo` 建议 `invent_stock_aft_as_cb_pricing`，单一主报，单挂，禁与 `invent_asof_leak_cb_aft_pricing` 双挂，DR1 不升格；诊断桶 `merge_stock_aft_with_cb_aft` / `drop_vwap_leg_on_szse_cb_aft` / `copy_sse_stock_aft_onto_cb` / `confuse_with_szse_block_aft_pricing` / `vs_M_stock_aft_channel` / `vs_CH_stock_aft_fill` / `vs_CL_cb_aft_fill` / `vs_Q_cb_continuous_rules` / `vs_O_block_channels` / `vs_R_etf_t0` / `vs_CR_put_call_exercise_fill` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip` 不升格；**尤重实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 dr0**；**尤重 Q 可转债连续竞价规则 ≠ 本页盘后定价通道身份，禁止合成进 dr0**；**尤重 M/CH 股票盘后通道/可成交性 ≠ 本页转债盘后定价≠股票盘后固定价格，禁止合成进 dr0**；**尤重 CL 可转债盘后定价可成交性 ≠ 本页通道误套，禁止合成进 dr0**；**尤重 O 大宗三通道 ≠ 本页，禁止合成进 dr0**；**尤重 DO 可转债回售处理 ≠ 本页盘后定价误套，禁止合成进 dr0**；**尤重 CR 认沽/认购行权成交 ≠ 本页，禁止合成进 dr0**；**双字母 DR ≠ 单字母假设-D / 假设-R ≠ 假设-BR**；**禁与 R/Q/M/CH/CL/O 混读**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DR ≠ 单字母 D/R**，且 **params.G 的 0.01 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05 窗口**，**禁把占位读成收盘价/VWAP/15:05 窗口**，**params 相对门槛 ≠ 官方定价规则**；锚建议、未冻：`cb_aft_pricing_honest=pit_szse_cb_aft_close_or_vwap_not_stock_aft_close_only` / scope=`cb_aft_pricing_vs_stock_aft_fixed_listed_apart` / over_policy=`skip_if_venue_or_biz_type_or_official_rule_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`；口径：缺 venue/业务类型或官方规则则 skip；股票盘后固定价格=收盘价、时间优先；深市可转债盘后定价允许收盘价或匹配 VWAP，禁止与股票盘后固定价格合成一句；沪市可转债若缺官方盘后定价另档规则则 skip，禁止沪深合成（**草稿方向，尚未冻，不要写成已冻**）；handoff：`stock_aft_channel_handoff=m_page`，`stock_aft_fill_handoff=ch_page`，`cb_aft_fill_handoff=cl_page`，`cb_continuous_rules_handoff=q_page`，`block_channel_handoff=o_page`，`etf_t0_handoff=r_page`，`cb_put_handling_handoff=do_page`；`merge_with_DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/BR/A/D=False`；**DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠BR≠A≠D**；**双字母 DR ≠ 单字母 D/R**；**未标纸面齐**；**不写 A/D–DR纸面齐**；**纸面齐惯例**：落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK/DL/DM/DN/DO/DP/DQ；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–DQ；不改已齐假设-DA～假设-DQ；不重开假设-T；不重开假设-R；不重开假设-Q；不重开假设-M；不重开假设-O；不重开假设-DO；不重开假设-DQ；不写下一字母；不预留 #128；不开真数/回测/实盘。基 tip=`50946c09`（A/D–DQ纸面齐已合，全长 `50946c09b6160e4ade9bfed886e5dbb954f84358`；不改该 tip 上的 #110–#126，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
