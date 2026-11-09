# 假设-DX · 沪市基金收盘产生方式切日误套（成交规则）

更新：2026-12-04  
来源：总管线 / 基 tip=`d354b63f` / 全长 `d354b63fcba8a972c86d7f3ab1069b10b3db09b2`（A/D–DW纸面齐已合）；**不改已冻 A–DQ / DA–DW**；**零改 DW**；**不改假设-DW 正文/预检/复检**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-DT / 假设-DU / 假设-DV / 假设-DW / 假设-S / 假设-AX / 假设-AY / 假设-AW / 假设-T / 假设-U / 假设-V / 假设-W / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-N / 假设-E / 假设-F / 假设-J / 假设-A / 假设-D / 假设-X 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ）；**不重开假设-R**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-AW**；**不重开假设-D**；**不重开假设-X**；**不重开假设-AY**；**不重开假设-AX**；**不重开假设-DW**；**不重开假设-DV**；**不重开假设-DU**；**不重开假设-DT**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-N**；**不重开假设-Q**；**不重开假设-M**；**不重开假设-W**）后写下一草稿 DX；清单 #132=DW，本页占用 **#133=DX**；选题是回测把 **沪市基金/ETF 收盘产生方式**的切日套错（诚实方向：沪市基金/ETF **2026-07-06 起**收盘阶段改为收盘集合竞价，此前尾盘仍是连续竞价；禁止把沪市股票 **2018-08-20** 的收盘集合切日抄到基金；深市基金尾盘此前已是集合竞价，2026 修订不作变更，禁止发明深市基金 2026 切日；缺 venue / 证券类别 / 切日规则则 skip）；假设-AW 只收收盘集合**失败之后**假抄前收或假末笔（失败回落 ≠ 本页「何时改成集合」），假设-D 只收成交时点与停牌，假设-X 只收主板 ST 涨跌幅 PIT（同日 2026-07-06 不是同一件事），假设-N 只收收盘机制与假 GTC 的旧页方向（本页不改 N），假设-M 只收盘后通道落地，假设-R 只收股票 ETF 假 T+0，假设-AY 只收基金最小价位，假设-AX 只收基金经手费，假设-V 只收股票印花税切日，假设-T 只收股票证管费切日，假设-U 只收股票过户切日，假设-DW 只收权证/期权行权过户；**新建实验 DX**；不写下一字母；不预留 #134  
状态：**A/D–DX纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「沪市基金收盘一直是 14:57 集合竞价」或「基金跟股票一起从 2018-08-20 起改集合」当诚实切日；禁止发明深市基金 2026 切日；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–DW**；**零改 DW**；**不改 #110–#132**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DX（#133）。一句话误开：回测把沪市基金/ETF 在 **2026-07-06 之前**的收盘当成收盘集合竞价一次价，或把沪市股票 2018-08-20 的收盘集合切日抄到基金上，或给深市基金发明一个 2026-07-06 切日，或与 AW收盘集合失败回落 / D成交时点与停牌 / X主板ST涨跌幅 / AY基金价位 / AX基金经手费 / R股票ETF假T+0 / DW权证期权行权过户 / DV现金选择权行权过户 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后通道 / V股票印花 / T股票证管费 / U股票过户 混读，或缺 venue / 证券类别 / 切日规则仍不 skip，系统性改写沪市基金收盘是怎么来的。**禁把 AW/D/X/AY/AX/R/V/T/U 混读升格进 `dx0`**。**禁把 DW/DV/DU/DT/DS/DR 混读升格进 `dx0`**。**禁把 `copy_sse_stock_20180820_close_call_onto_fund` 抄套进主报**。**禁把 `invent_szse_fund_close_change_20260706` 升格进 `dx0`**。

> **字母消歧（硬）**：本页**实验字母 DX** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DX**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**；**勿把 `params.Y` 读成实验字母 DX，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿读成假设-X，亦勿读成假设-D**；**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DX**；**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰ ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户 0.01‰，也不是面值 0.5‰，也不是收盘价、匹配 VWAP 或 15:05 窗口，更不是 2018-08-20、2026-07-06 或深市切日）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DX**；**params.N ≠ 单字母假设-N**）≠ **`params.Y2`**（写死冻结 0.015）≠ **单字母实验 D**（成交时点与停牌；**双字母 DX ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 X**（主板 ST 涨跌幅 PIT；**双字母 DX ≠ 单字母假设-X；严禁复用假设-X**；同日 2026-07-06 是 ST 板幅切日，不是本页基金收盘阶段切日）≠ **单字母实验 V**（股票印花税切日；**双字母 DX ≠ 单字母假设-V；严禁复用假设-V**；**不重开假设-V**）≠ **单字母实验 U**（股票过户费切日；**双字母 DX ≠ 单字母假设-U；严禁复用假设-U**；**不重开假设-U**）≠ **单字母实验 T**（股票证管费切日；**双字母 DX ≠ 单字母假设-T；严禁复用假设-T**；**不重开假设-T**）≠ **单字母实验 R**（股票 ETF 假 T+0；**双字母 DX ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `dx0`**）≠ **双字母 AW**（收盘集合失败假抄前收或假末笔；**AW = 集合已经该产生价、却没产生时怎么回落**；**本页 = 沪市基金从哪一天起收盘阶段才改成集合**；**DX≠AW**；**不重开假设-AW**）≠ **双字母 AY**（基金/ETF 最小价位；价位 ≠ 收盘怎么产生）≠ **双字母 AX**（基金经手费；费用 ≠ 收盘阶段）≠ **双字母 DW**（权证/期权行权过户；**零改 DW**；**DX≠DW**）≠ **双字母 DV**（现金选择权行权过户）≠ **DU**（可转债首日临停）≠ **DT**（可转债整手价位）≠ **DS**（转股印花）≠ **DR**（可转债盘后定价通道）≠ **DQ**（ETF 申赎篮子过户）≠ **DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA**（费用旁路；不并进 `dx0`）≠ **S**（股票经手费切日）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债回转/涨跌幅/收盘）≠ **O**（大宗）≠ **M**（股票/ETF 盘后通道；**2026-07-06 盘后扩围 ≠ 本页收盘阶段切日**）≠ **CH / CL / CR / CQ**（可成交性旁路）≠ **E / F / J / W**（整手、取整、无板日临停、除权判板）≠ **单字母实验 A**（板上枯竭）。**DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠D≠X≠A**。**双字母 DX ≠ 单字母 D/X**。**双字母 DX ≠ 单字母假设-D / 假设-X**。**params.Y/G/N ≠ 实验字母 DX ≠ 单字母 D/X**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**。**禁把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**。**params 相对门槛 ≠ 切日日期 ≠ 过户费率 ≠ 印花税率 ≠ 证管费 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05**。**沪市基金收盘产生方式切日 ≠ 沪市股票 2018-08-20 切日 ≠ 深市基金 2026 变更（禁止发明）≠ AW收盘集合失败回落 ≠ D成交时点 ≠ X主板ST涨跌幅 ≠ R股票ETF假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ DW权证期权行权过户**。**尤重：实验 R 不抢；禁把 `vs_R_etf_t0` 升格进 `dx0`**。**尤重：不重开假设-V / 假设-T / 假设-U；禁把 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 升格进 `dx0`**。**尤重：AW 收盘集合失败假抄前收/末笔 ≠ 本页「何时改成集合」；禁把 `vs_AW_close_call_fail_fallback` 升格进 `dx0`**。**尤重：沪市股票 2018-08-20 ≠ 沪市基金 2026-07-06，禁抄套；禁 `copy_sse_stock_20180820_close_call_onto_fund` 进主报**。**尤重：深市基金尾盘已是集合、2026 不作变更，禁发明深市切日；禁 `invent_szse_fund_close_change_20260706` 升格进 `dx0`**。**尤重：双字母 DX ≠ 单字母假设-D / 假设-X；禁把 `vs_D_open_close_halt` / `vs_X_st_limit_pit` 升格进 `dx0`**。**尤重：DW/DV/DU/DT/DS/DR 旁路诊断禁升格进 `dx0`**。**零改 DW**。

### 专节 · 双字母 DX ≠ 单字母假设-D / 假设-X；且 ≠ 假设-AW / 假设-R / 假设-V / 假设-T / 假设-U / 假设-DW（硬）

| 维度 | 对照页 | 本页假设-DX（双字母） |
|------|--------|----------------------|
| 题面 AW | **收盘集合失败假抄前收或假末笔**（集合该产生价却没产生时，回落到最后一分钟加权；假设-AW） | **AW = 失败之后怎么填价**。本页问的是沪市基金**从哪一天起**收盘阶段才改成集合。集合还没启用的日子，不存在「集合失败回落」。**DX≠AW**；**严禁复用假设-AW**；**不重开假设-AW**；**不改 AW**；**尤重：禁把 `vs_AW_close_call_fail_fallback` 升格进 `dx0`**；`close_call_fail_handoff=aw_page`；诊断桶 `vs_AW_close_call_fail_fallback` 不升格 |
| 题面 股票切日 | **沪市股票 2018-08-20 起收盘集合**（`事实与坑`；债券、回购、基金当时不改） | **沪市股票 2018-08-20 ≠ 沪市基金 2026-07-06**。把股票切日抄到基金上，会把 2018 之后、2026-07-06 之前的基金尾盘连续竞价误写成集合一次价。**禁抄套**；**尤重：禁 `copy_sse_stock_20180820_close_call_onto_fund` 进主报**；该键只作诊断桶，不升格 |
| 题面 深市基金 | **深市基金尾盘此前已是集合竞价**（2026 修订说明：本次不作变更） | 禁止发明「深市基金也在 2026-07-06 改收盘阶段」。深市没有这道新切日。**尤重：禁 `invent_szse_fund_close_change_20260706` 升格进 `dx0`**；该键只作诊断桶 |
| 题面 D | **成交时点与停牌**（次日开还是次日收；停牌日记不可交易；假设-D） | 先问这根收盘价当时是怎么产生的，再问信号腿在次日开盘还是次日收盘成交。两件事不合成。**双字母 DX ≠ 单字母假设-D**；**严禁复用假设-D**；**DX≠D**；**params 字母 ≠ 假设-D**；**不重开假设-D**；**不改 D**；**尤重：禁把 `vs_D_open_close_halt` 升格进 `dx0`**；`open_close_halt_handoff=d_page` |
| 题面 X | **主板 ST 涨跌幅 PIT**（2026-07-06 前 5%、后 10%；假设-X） | 同一天可以既改 ST 板幅、又改沪市基金收盘阶段，规则不是一条。**双字母 DX ≠ 单字母假设-X**；**严禁复用假设-X**；**DX≠X**；**params 字母 ≠ 假设-X**；**不重开假设-X**；**不改 X**；**尤重：禁把 `vs_X_st_limit_pit` 升格进 `dx0`**；`st_limit_pit_handoff=x_page` |
| 题面 R | **股票 ETF 假 T+0**（假设-R；回转名单 ≠ 收盘阶段） | **实验 R 不抢**。股票 ETF 能不能当日回转，和收盘价是集合还是连续产生，是两件事。**DX≠R**；**严禁复用假设-R**；**不重开假设-R**；**不改 R**；**尤重：禁把 `vs_R_etf_t0` 升格进 `dx0`**；`etf_t0_handoff=r_page` |
| 题面 V | **股票印花税切日**（假设-V） | **不重开假设-V**。印花切日 ≠ 收盘产生方式。占位不是印花税率。**DX≠V**；**params 字母 ≠ 假设-V**；**不改 V**；**尤重：禁把 `vs_V_stamp` 升格进 `dx0`**；`stamp_handoff=v_page` |
| 题面 T | **股票证管费切日**（假设-T） | **不重开假设-T**。`params.Y` 的 0.02 不是证管费 0.02‰。**DX≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：禁把 `vs_T_csrc` 升格进 `dx0`**；`csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日**（假设-U） | **不重开假设-U**。`params.G` 的 0.01 不是过户 0.01‰。**DX≠U**；**params 字母 ≠ 假设-U**；**不改 U**；**尤重：禁把 `vs_U_transfer` 升格进 `dx0`**；`transfer_fee_handoff=u_page` |
| 题面 AY | **基金/ETF 最小价位**（0.001 ≠ 股票 0.01；假设-AY） | 价位取整 ≠ 收盘阶段切日。**DX≠AY**；**不重开假设-AY**；**不改 AY**；**禁把 `vs_AY_tick` 升格进 `dx0`**；`tick_handoff=ay_page` |
| 题面 AX | **基金/ETF 经手费**（假设-AX） | 经手费档 ≠ 收盘怎么产生。**DX≠AX**；**不重开假设-AX**；**不改 AX**；**禁把 `vs_AX_handling` 升格进 `dx0`**；`handling_handoff=ax_page` |
| 题面 DW | **权证/股票期权行权过户**（假设-DW 已纸面齐） | 行权过户 ≠ 基金收盘切日。**零改 DW**。**DX≠DW**；**不重开假设-DW**；**不改 DW 正文/预检/复检**；**尤重：禁把 `vs_DW_warrant_option_transfer` 升格进 `dx0`**；`warrant_option_transfer_handoff=dw_page` |
| 题面 DV | **现金选择权行权过户**（假设-DV） | **DX≠DV**；**不重开假设-DV**；**不改 DV**；**禁把 `vs_DV_cash_option_transfer` 升格进 `dx0`**；`cash_option_transfer_handoff=dv_page` |
| 题面 DU | **可转债首日临停** | **DX≠DU**；**不重开假设-DU**；**不改 DU**；**禁把 `vs_DU_cb_ipo_halt` 升格进 `dx0`**；`cb_ipo_halt_handoff=du_page` |
| 题面 DT | **可转债整手价位** | **DX≠DT**；**不重开假设-DT**；**不改 DT**；**禁把 `vs_DT_cb_lot_tick` 升格进 `dx0`**；`cb_lot_tick_handoff=dt_page` |
| 题面 DS | **转股所得股票印花** | **DX≠DS**；**不重开假设-DS**；**不改 DS**；**禁把 `vs_DS_conversion_stamp` 升格进 `dx0`**；`cb_conversion_stamp_handoff=ds_page` |
| 题面 DR | **可转债盘后定价通道** | 盘后通道 ≠ 收盘阶段切日。**DX≠DR**；**不重开假设-DR**；**不改 DR**；**禁把 `vs_DR_aft_pricing` 升格进 `dx0`**；`aft_pricing_handoff=dr_page` |
| 题面 M | **盘后固定价格通道**（ETF 盘后也在 2026-07-06 扩围；假设-M） | 同一天扩围的是盘后定价申报，不是「收盘价从连续竞价改成收盘集合」。两件事日期可以相同，禁止合成一句。**DX≠M**；**不重开假设-M**；**不改 M** |
| 题面 N | **收盘机制与假 GTC**（假设-N 已写沪市基金 2026-07-06 前不按股票收盘集合，并写限价不隔夜） | N 是旧页方向，含假 GTC。本页只收「沪市基金收盘产生方式切日被误套」这一腿，不改 N，不把假 GTC 升格进 `dx0`，不在硬分列主链里另造桶。**不重开假设-N**；**不改 N** |
| 题面 Q | **可转债回转 / 涨跌幅 / 收盘** | 转债收盘（沪市匹配成交没有 14:57 集合）≠ 沪市基金切日。**DX≠Q**；**不重开假设-Q**；**不改 Q** |
| 题面 W | **除权日复权价误判板** | 除权判板 ≠ 收盘阶段切日。**DX≠W**；**不重开假设-W**；**不改 W** |
| 题面 DQ–DA / S / AC / O / CH / CL / CR / CQ / E / F / J | 费用、整手、可成交性等旁路 | 全部不并进 `dx0`。**DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠D≠X≠A**。不改这些页 |
| 题面 A | **涨停可成交 / 板上枯竭** | **DX≠A**；**不抢 A 真数队列**；**不改 A** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_sse_fund_close_as_call_auction_pre_20260706`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_sse_fund_close_auction` 双挂；DX1 不升格；诊断桶不升格） |
| 文档 | 清单实验 DW 及上表各页（**只读；禁止改写**） | `假设-DX-沪市基金收盘产生方式切日误套.md`（新建） |
| 预检键 | 实验字母 DW / DV / … / D / X / Y / G / N，以及已存在 AW / AY / AX / R | 实验字母 **DX** / `dx0_primary_demo`；**不得**占用或改写上述预检键 |

**禁止**：把 DX 写成「AW / D / X / N / M / R 的续篇」；把「股票 2018-08-20 已改集合 / 深市基金本来就是集合 / ST 板幅已在 2026-07-06 切片 / 盘后已在 2026-07-06 扩围」写成「沪市基金收盘切日已诚实」；把实验字母 DX 与单字母 D/X 或 params.Y/G/N 混读；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**；**禁把占位 `0.02/0.01/0.05/0.015` 读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**；**实验 R 不抢**；**不重开假设-V / 假设-T / 假设-U**；**AW 失败回落 ≠ 本页切日**；**禁抄套股票 2018-08-20**；**禁发明深市基金 2026 切日**；**零改 DW**；**禁把 DW/DV/DU/DT/DS/DR 以及 AY/AX/R/V/T/U/D/X/AW 的诊断升格进 `dx0`**；把 `invent_asof_leak_sse_fund_close_auction` 与主报双挂；缺 venue / 证券类别 / 切日规则仍硬填。本页主键只用 `dx0` / `dx1` / `dx2` 与 `sse_fund_close_*`。不写下一字母。不预留 #134。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–DW；勿再只改清单）。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测把 **沪市基金/ETF 在 2026-07-06 之前的收盘**当成 **收盘集合竞价一次价**，或把沪市股票 2018-08-20 的切日抄到基金上，或给深市基金发明 2026-07-06 切日，或与 AW 的失败回落、D 的开收时点、X 的 ST 板幅、R 的假 T+0、V/T/U 的费用切日、DW/DV/DU/DT/DS/DR 的旁路混读，或缺 venue / 证券类别 / 切日规则仍不 skip，相对「缺字段则 skip；沪市基金/ETF 从 2026-07-06 起收盘阶段才是收盘集合，此前是连续竞价；不抄股票 2018-08-20；不发明深市基金 2026 切日」的诚实组，会**系统性改写这根收盘价当时是怎么来的**——尾盘连续竞价的冲击被写成集合一次价。方向是相对诚实锚偏误。

核对日方向（随锚写死；禁止把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日）：`事实与坑` 2026-10-19 写明，沪市股票自 2018-08-20 起收盘价改由 14:57–15:00 收盘集合产生，**基金当时不改**；沪市基金（含 ETF）要到 **2026-07-06** 才把尾盘从连续竞价改成收盘集合。深市基金尾盘此前已是集合，2026 修订说明本次不作变更。本页把这三句收成已写死冻结的锚。方向随锚写死，不要把切日铺成全历史唯一规则，也不要把占位读成切日。股票切日、ST 板幅、盘后扩围、费用切日都留在各自的页。缺 venue、证券类别或切日规则，整笔 skip。**禁把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**。

证伪方向：若天真组 / 半泄露组相对诚实组的收盘产生方式误套截在标定噪声带内可忽略，且「2026-07-06 前误当集合 / 抄股票 2018-08-20 / 发明深市 2026 切日 / 核对日泄露 / vs AW·D·X·AY·AX·R·DW·DV·DU·DT·DS·DR·V·T·U」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dx0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DX ≠ 单字母假设-D / 假设-X**；勿把 params.Y 读成实验字母 DX，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿读成假设-X，亦勿读成假设-D
# 【消歧】params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D
# 【消歧】尤重：params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期
# 【消歧】尤重：params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰ ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05（无量纲相对门槛 ≠ 过户费率 ≠ 面值档 ≠ 收盘价 ≠ 切日）
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DX ≠ 单字母假设-N**
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日
# 【消歧】params 相对门槛 ≠ 切日日期 ≠ 过户费率 ≠ 印花税率 ≠ 证管费 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05
# 【消歧】三条已冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值
# params.Y2                               写死冻结 0.015
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：收盘产生方式误套截 ΔSseFundClose / 净差异 / DX1−DX2；**params.Y/G/N ≠ 实验字母 DX ≠ 单字母 D/X**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰ ≠ 收盘价/VWAP/15:05**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期**；**禁把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        写死冻结 next_open
# params.asof_check_date                  写死冻结 2026-10-19（这是核对日，不是切日，也不是占位）
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.sse_fund_close_honest            写死冻结 pit_continuous_pre_20260706_call_from_20260706_not_stock_20180820
#   诚实锚方向（已写死冻结）：
#   缺 venue、证券类别或切日规则 → skip
#   沪市基金/ETF：2026-07-06 起，收盘阶段 = 收盘集合竞价
#   此前 = 连续竞价
#   禁止套沪市股票 2018-08-20
#   禁止发明深市基金 2026 切日（深市基金尾盘已是集合，2026 不作变更）
#   禁止把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20或深市切日
#   枚举已写死冻结
#   锚名字里的日期是机制方向，不是 params.Y/G/N/Y2
# params.sse_fund_close_scope             写死冻结 sse_fund_etf_close_generation_cutover
#   只看沪市基金/ETF 收盘价怎么产生的切日
#   不是股票切日，不是深市切日，不是盘后通道，不是费用
# params.sse_fund_close_over_policy       写死冻结 skip_if_venue_or_sec_type_or_cutover_rule_missing
#   缺 venue / 证券类别 / 切日规则则 skip
# params.close_call_fail_handoff          建议 aw_page
#   收盘集合失败回落交 AW；AW ≠ 本页切日；不重开假设-AW；不改 AW
#   诊断桶 vs_AW_close_call_fail_fallback 不得升格进 dx0
# params.open_close_halt_handoff          建议 d_page
#   成交时点与停牌交 D；双字母 DX ≠ 单字母假设-D；不重开假设-D；不改 D
#   诊断桶 vs_D_open_close_halt 不得升格进 dx0
# params.tick_handoff                     建议 ay_page
#   基金价位交 AY；不重开假设-AY；不改 AY；vs_AY_tick 不得升格进 dx0
# params.handling_handoff                 建议 ax_page
#   基金经手费交 AX；不重开假设-AX；不改 AX；vs_AX_handling 不得升格进 dx0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 dx0；不改 R
#   诊断桶 vs_R_etf_t0 不得升格进 dx0
# params.warrant_option_transfer_handoff  建议 dw_page
#   权证/期权行权过户交 DW；零改 DW；不重开假设-DW；不改 DW 正文/预检/复检
#   诊断桶 vs_DW_warrant_option_transfer 不得升格进 dx0
# params.cash_option_transfer_handoff     建议 dv_page
#   现金选择权行权过户交 DV；不重开假设-DV；不改 DV；vs_DV_cash_option_transfer 不得升格进 dx0
# params.cb_ipo_halt_handoff              建议 du_page
#   可转债首日临停交 DU；不重开假设-DU；不改 DU；vs_DU_cb_ipo_halt 不得升格进 dx0
# params.cb_lot_tick_handoff              建议 dt_page
#   整手价位交 DT；不重开假设-DT；不改 DT；vs_DT_cb_lot_tick 不得升格进 dx0
# params.cb_conversion_stamp_handoff      建议 ds_page
#   转股印花交 DS；不重开假设-DS；不改 DS；vs_DS_conversion_stamp 不得升格进 dx0
# params.aft_pricing_handoff              建议 dr_page
#   盘后定价通道交 DR；不重开假设-DR；不改 DR；vs_DR_aft_pricing 不得升格进 dx0
# params.st_limit_pit_handoff             建议 x_page
#   主板 ST 涨跌幅交 X；双字母 DX ≠ 单字母假设-X；params 字母 ≠ 假设-X；不重开假设-X；不改 X
#   诊断桶 vs_X_st_limit_pit 不得升格进 dx0
# params.stamp_handoff                    建议 v_page
#   股票印花切日交 V；不重开假设-V；params 字母 ≠ 假设-V；不改 V
#   诊断桶 vs_V_stamp 不得升格进 dx0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；params 字母 ≠ 假设-T；不改 T
#   诊断桶 vs_T_csrc 不得升格进 dx0
# params.transfer_fee_handoff             建议 u_page
#   股票过户切日交 U；不重开假设-U；params 字母 ≠ 假设-U；不改 U
#   诊断桶 vs_U_transfer 不得升格进 dx0
# params.dx0_primary_demo                 写死冻结 invent_sse_fund_close_as_call_auction_pre_20260706
#   单一主报写死，单挂；禁与 invent_asof_leak_sse_fund_close_auction 双挂
#   DX1 不升格；诊断桶不升格
#   半泄露名只作对照，不得升格进 dx0，不得双挂
#   诊断桶 copy_sse_stock_20180820_close_call_onto_fund / invent_szse_fund_close_change_20260706 / vs_AW_close_call_fail_fallback / vs_D_open_close_halt / vs_AY_tick / vs_AX_handling / vs_R_etf_t0 / vs_DW_warrant_option_transfer / vs_DV_cash_option_transfer / vs_DU_cb_ipo_halt / vs_DT_cb_lot_tick / vs_DS_conversion_stamp / vs_DR_aft_pricing / vs_X_st_limit_pit / vs_V_stamp / vs_T_csrc / vs_U_transfer / missing_venue_or_sec_type_or_cutover_rule_not_skip 不得升格进 dx0
#   尤重：实验 R 不抢
#   尤重：不重开假设-V / 假设-T / 假设-U
#   尤重：禁 copy_sse_stock_20180820_close_call_onto_fund 进主报
#   尤重：禁 invent_szse_fund_close_change_20260706 升格
#   尤重：零改 DW；禁把 DW/DV/DU/DT/DS/DR 升格进 dx0
# params.dx0_invent_sse_fund_close_as_call_auction_pre_20260706 建议 True
# params.dx1_asof_leak_sse_fund_close_auction_only 建议 True
#   半泄露对照；DX1 不升格并列主报；不得把 invent_asof_leak_sse_fund_close_auction 写进 dx0
# params.dx2_pit_continuous_pre_20260706_call_from_20260706_not_stock_20180820 建议 True
# params.merge_with_DW                    建议 False
# params.merge_with_DV                    建议 False
# params.merge_with_DU                    建议 False
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
# params.merge_with_W                     建议 False
# params.merge_with_AW                    建议 False
# params.merge_with_AY                    建议 False
# params.merge_with_D                     建议 False
# params.merge_with_X                     建议 False
# params.merge_with_A                     建议 False
# params.missing_venue_or_sec_type_or_cutover_rule_policy 建议 skip
# params.day_freq_proxy                   建议 sse_fund_close_sensitivity
# params.universe_rule                    建议 sse_fund_close_cutover_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dx_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DX；勿读成单字母 D/X
#   不另挂主报，不预留 #134，不写下一字母
```

### 2.2 三组对照（DX0 / DX1 / DX2）

组名 DX0 / DX1 / DX2 是本页三组，≠ 单字母实验 D（成交时点与停牌），亦 ≠ 单字母实验 X（主板 ST 涨跌幅 PIT）。**双字母 DX ≠ 单字母假设-D / 假设-X**。**params.Y/G/N ≠ 实验字母 DX ≠ 单字母 D/X**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**。

| 组 | 角色 | 口径 |
|----|------|------|
| DX0 | 天真 / 沪市基金收盘提前当成集合 | 按 `dx0_primary_demo` **写死冻结**单一主报 `invent_sse_fund_close_as_call_auction_pre_20260706`（单挂写死）：把 2026-07-06 之前的沪市基金/ETF 收盘当成收盘集合竞价。**禁**与 `invent_asof_leak_sse_fund_close_auction` 双挂。**禁把抄股票 2018-08-20、发明深市 2026 切日、AW/D/X/AY/AX/R/V/T/U、DW/DV/DU/DT/DS/DR 合成进 `dx0`** |
| DX1 | 半泄露 | 仅用核对日「沪市基金收盘已经是集合」把这条铺到全历史、铺到 2026-07-06 之前、或铺到深市基金（`invent_asof_leak_sse_fund_close_auction`）；**不得升格并列主报**，不得写进 `dx0`，不得双挂 |
| DX2 | 诚实 / 按切日的收盘产生方式 | `sse_fund_close_honest=pit_continuous_pre_20260706_call_from_20260706_not_stock_20180820`（写死冻结）：缺 venue/证券类别/切日规则则 skip；沪市基金/ETF 2026-07-06 起收盘阶段=收盘集合，此前=连续竞价；禁止套股票 2018-08-20；禁止发明深市基金 2026 切日。失败回落只消费 AW，开收时点只消费 D，ST 板幅只消费 X，价位只消费 AY，经手费只消费 AX，假 T+0 只消费 R，行权过户只消费 DW，其余旁路只消费对应页，或显式旁路 |

把股票 2018-08-20 抄到基金、发明深市基金 2026 切日、把核对日规则铺满历史、以及相对 AW/D/X/AY/AX/R/DW/DV/DU/DT/DS/DR/V/T/U 的对照，放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**。`copy_sse_stock_20180820_close_call_onto_fund` 只标记「有人抄了股票切日」，**不得进主报**。`invent_szse_fund_close_change_20260706` 只标记「有人发明了深市切日」，**不得升格进 `dx0`**。`vs_AW_close_call_fail_fallback` 只标记失败回落对照。`vs_D_open_close_halt` 只标记开收时点对照。`vs_X_st_limit_pit` 只标记 ST 板幅对照。`vs_R_etf_t0` 只标记假 T+0 对照。`vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只标记费用对照。`vs_DW_warrant_option_transfer` / `vs_DV_cash_option_transfer` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` 只标记旁路，**零改 DW**。`vs_AY_tick` / `vs_AX_handling` 只标记价位和经手费。`missing_venue_or_sec_type_or_cutover_rule_not_skip` 只标记缺字段仍不 skip。这些都**不得升格进 `dx0`**。

### 2.3 切日窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-19`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dx0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺 venue / 证券类别 / 切日规则则 skip；沪市基金/ETF 从 2026-07-06 起收盘阶段才是收盘集合，此前是连续竞价；禁止套股票 2018-08-20；禁止发明深市基金 2026 切日。`params.G` 的 0.01 不是过户费 0.01‰，也不是面值 0.5‰，也不是收盘价、VWAP 或 15:05；`params.Y` 的 0.02 不是证管费 0.02‰，也不是切日日期；四个占位也不是 2018-08-20、2026-07-06、深市切日或核对日。**禁把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**。本页**不开回测**；不拉真数；不做实盘；不开户。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dx0_primary_demo` / `params.Y`·G·N·Y2 / 切日开关 / 桶 / 是否把 2026-07-06 的集合规则铺到此前、或抄到股票切日、或发明深市切日、或把占位读成切日日期）。本页不开跑。禁 null。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DX0）/ 半泄露组（DX1）相对诚实组（DX2）的收盘产生方式误套截**显著且集中在 2026-07-06 之前的沪市基金/ETF 被当成收盘集合**的桶；分桶「抄股票 2018-08-20 / 发明深市 2026 切日 / 核对日泄露 / vs AW·D·X·AY·AX·R·DW·DV·DU·DT·DS·DR·V·T·U」不改变主结论方向。成功不依赖把占位读成切日，也不把 `params.Y` 的 0.02 读成证管费，也不把 `params.G` 的 0.01 读成过户费。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 AW 的失败回落、D 的开收时点、X 的 ST 板幅、N 的假 GTC、M 的盘后扩围、Q 的转债收盘、R 的假 T+0、AY 的价位、AX 的经手费、V/T/U 的费用、DW/DV/DU/DT/DS/DR 的旁路、或 A 的板上容量解释；或 `dx0_primary_demo` 与 `invent_asof_leak_sse_fund_close_auction` 双挂；或 DX1 升格并列主报；或诊断桶升格主报；或把股票 2018-08-20 抄进主报；或发明深市基金 2026 切日并升格；或实验字母 DX 与单字母 D/X 或 params.Y/G/N 混读；或把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日；或缺 venue / 证券类别 / 切日规则仍不 skip；或重开假设-R / 假设-V / 假设-T / 假设-U / 假设-AW / 假设-D / 假设-X / 假设-DW；或改 DW 正文/预检/复检；或标纸面齐；或写成 A/D–DX纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 DX0/DX1/DX2。失败回落走 AW，开收时点走 D，ST 板幅走 X，价位走 AY，经手费走 AX，假 T+0 走 R，行权过户走 DW，其余旁路走对应页，都不改。报告收盘产生方式误套截。不把 2026-07-06 或 2018-08-20 标成已冻门槛。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_sse_fund_close_as_call_auction_pre_20260706` / `invent_asof_leak_sse_fund_close_auction` / `copy_sse_stock_20180820_close_call_onto_fund` / `invent_szse_fund_close_change_20260706` / `vs_AW_close_call_fail_fallback` / `vs_D_open_close_halt` / `vs_AY_tick` / `vs_AX_handling` / `vs_R_etf_t0` / `vs_DW_warrant_option_transfer` / `vs_DV_cash_option_transfer` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_X_st_limit_pit` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `missing_venue_or_sec_type_or_cutover_rule_not_skip`

上列自 `copy_sse_stock_20180820_close_call_onto_fund` 起至 `missing_venue_or_sec_type_or_cutover_rule_not_skip` **只作诊断桶**：它们不是 `dx0`，也不是 DX1，**不得升格主报**。`invent_asof_leak_sse_fund_close_auction` 只服务 DX1，**不得升格进 `dx0`，不得双挂**。`invent_sse_fund_close_as_call_auction_pre_20260706` 才是写死冻结的单一主报名。没有「股票 2018-08-20 + 基金 2026-07-06」合成主报，也没有「深市基金 2026 切日」主报，也没有「AW 失败回落 + 本页切日」合成主报。**实验 R 不抢**。**不重开假设-V / 假设-T / 假设-U**。**零改 DW**。**禁把 DW/DV/DU/DT/DS/DR 升格进 `dx0`**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「沪市基金收盘一直是集合竞价」或「基金从 2018-08-20 起跟股票一起改集合」拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成证管费 0.02‰，或当成切日。**params 字母 ≠ 假设-T**。**params 字母 ≠ 假设-X**。**params 字母 ≠ 假设-D**。
- 把 `params.G` 的 0.01 当成过户 0.01‰。**params 字母 ≠ 假设-U**。**params 字母 ≠ 假设-V**。
- 把占位 `0.02/0.01/0.05/0.015` 读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日。**禁把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**。**params 相对门槛 ≠ 切日日期 ≠ 过户费率 ≠ 印花税率 ≠ 证管费 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05**。**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**。
- 缺 venue、证券类别或切日规则仍不 skip。诊断桶 `missing_venue_or_sec_type_or_cutover_rule_not_skip` 只作对照，不得升格。
- 把核对日「已经是收盘集合」写成全历史规则，或铺到 2026-07-06 之前，或铺到深市基金。锚六键已写死冻结。
- 把沪市股票 2018-08-20 抄到基金。诊断桶 `copy_sse_stock_20180820_close_call_onto_fund` 只作对照，**禁进主报**。
- 发明深市基金 2026-07-06 切日。深市基金尾盘已是集合，2026 不作变更。诊断桶 `invent_szse_fund_close_change_20260706` 只作对照，**禁升格**。
- 把 AW 的「集合失败假抄前收/末笔」和本页「何时改成集合」合成后升格进 `dx0`。**不重开假设-AW**。
- 把假设-D 的开收时点、停牌和本页切日合成后升格。**双字母 DX ≠ 单字母假设-D**。诊断桶 `vs_D_open_close_halt` 只作对照。
- 把假设-X 的主板 ST 涨跌幅（同日 2026-07-06）和本页基金收盘阶段合成后升格。**双字母 DX ≠ 单字母假设-X**。诊断桶 `vs_X_st_limit_pit` 只作对照。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格。**实验 R 不抢**。诊断桶 `vs_R_etf_t0` 只作对照。
- 把假设-V / 假设-T / 假设-U 和本页合成或混读后升格。诊断桶 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只作对照。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。
- 把 AY 价位、AX 经手费和本页合成后升格。诊断桶 `vs_AY_tick` / `vs_AX_handling` 只作对照。
- 把 DW/DV/DU/DT/DS/DR 旁路诊断升格进 `dx0`。**零改 DW**。**不重开假设-DW**。
- `dx0_primary_demo` 与 `invent_asof_leak_sse_fund_close_auction` 双挂；DX1 升格并列主报。
- 实验字母 DX 与单字母 D/X 或 params.Y/G/N 混读。**双字母 DX ≠ 单字母 D/X**。
- 改 DW / DV / DU / DT / DS / DR / AW / AY / AX / R / V / T / U / D / X / N / M / Q 及其他已冻页正文；改 #110–#132；标纸面齐；写成 A/D–DX纸面齐；开真数/回测/开户/实盘；用复权价当收盘产生方式的判据；结论写成「这类基金尾盘更好成交所以能买」。
- **纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–DW；勿再只改清单）。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权路径、交易日、**交易所 venue**、**证券类别**（沪市股票 / 沪市基金或 ETF / 深市基金或 ETF / 其他）。类别分不清则 skip，不把股票切日套到基金，也不把沪市切日套到深市。
- 切日规则是否在册：沪市基金/ETF 的收盘阶段切日（建议方向 2026-07-06）、沪市股票的收盘集合切日（2018-08-20，只作对照，不抄）。规则不在册则 skip，不用占位数字去填一个日期。
- 深市基金：只需要知道「本次修订不作收盘阶段变更」。不要另造一个 2026-07-06 切日字段去回放。
- 收盘价字段要能分清「这根价当时由连续竞价尾盘产生」还是「由收盘集合产生」。本页不改写价，只标产生方式有没有被套错。
- 旁路消费：AW 的失败回落、D 的成交时点、X 的 ST 板幅、AY 的价位、AX 的经手费、R 的假 T+0、DW 的权证/期权行权过户、DV/DU/DT/DS/DR 的旁路、V/T/U 的费用（见 §2.1 handoff）。**本页不改写这些页。零改 DW。**
- 未复权路径；asof **写死冻结** `2026-10-19`。核对日在切日之后，所以「核对日当天沪市基金收盘已经是集合」不能倒灌到 2026-07-06 之前。`事实与坑` 2026-10-19 是方向来源，不是已冻的全历史规则。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-19`；`fail_policy=skip`；`sse_fund_close_honest=pit_continuous_pre_20260706_call_from_20260706_not_stock_20180820`；`sse_fund_close_scope=sse_fund_etf_close_generation_cutover`；`sse_fund_close_over_policy=skip_if_venue_or_sec_type_or_cutover_rule_missing`；`dx0_primary_demo=invent_sse_fund_close_as_call_auction_pre_20260706`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_sse_fund_close_auction` 双挂；DX1 不升格；诊断桶不升格；**禁抄股票 2018-08-20 进主报**；**禁发明深市切日并升格**；**禁把 AW/D/X/AY/AX/R/V/T/U 与 DW/DV/DU/DT/DS/DR 升格进 `dx0`**）；`close_call_fail_handoff=aw_page`；`open_close_halt_handoff=d_page`；`tick_handoff=ay_page`；`handling_handoff=ax_page`；`etf_t0_handoff=r_page`；`warrant_option_transfer_handoff=dw_page`；`cash_option_transfer_handoff=dv_page`；`cb_ipo_halt_handoff=du_page`；`cb_lot_tick_handoff=dt_page`；`cb_conversion_stamp_handoff=ds_page`；`aft_pricing_handoff=dr_page`；`st_limit_pit_handoff=x_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；`merge_with_DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/D/X/A=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是切日日期、不是过户费率、不是印花税率、不是证管费、不是收盘价、不是 VWAP、不是 15:05；**params.Y/G/N ≠ 实验字母 DX ≠ 单字母 D/X**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰ ≠ 收盘价/VWAP/15:05**；**禁把占位读成切日日期、过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #134。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`d354b63f`（A/D–DW纸面齐已合，全长 `d354b63fcba8a972c86d7f3ab1069b10b3db09b2`）；三冻补丁基 tip=`9afeb6a8` / `9afeb6a81dd13036b9288725b51b04ae3de11ef6`；分支起点 HEAD=`c4e7985e` / `c4e7985eb6c0ca3ca54412969e241c83f7ae2522`。**不改已冻 A–DQ / DA–DW**。**零改 DW**。**不改 #110–#132**。状态=**A/D–DX纸面齐（预检有条件通过·三条已冻）**。

---

## 8. 结论

（空；**A/D–DX纸面齐（预检有条件通过·三条已冻）**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-12-04）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DX-20261110.md`（原样落入，不改结论；SHA256=`4ef2991fdfd90bab56a2ab06bc6aeeaca5fc579430b35d8d5ab33ee9c8ecf69e`；预检 2026-11-10；**结论：有条件通过**；tip基=`9afeb6a8` / `9afeb6a81dd13036b9288725b51b04ae3de11ef6`；本补丁分支起点 HEAD=`c4e7985e` / `c4e7985eb6c0ca3ca54412969e241c83f7ae2522`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于收盘产生方式误套截 ΔSseFundClose、净差异、DX1−DX2 专项。**`params.Y` ≠ 实验字母 DX**；**`params.G` ≠ 实验字母 DX**；**`params.N` ≠ 实验字母 DX**；亦 ≠ 单字母假设-D / 假设-X。**params.Y/G/N ≠ 实验字母 DX ≠ 单字母 D/X**。**勿把 `params.Y` 读成假设-V，亦勿读成假设-T，亦勿读成假设-X，亦勿读成假设-D，亦勿把 `params.G` 读成假设-U，亦勿把 `params.Y` 读成实验字母 DX，亦勿把单字母假设-D / 假设-X 读成双字母 DX**。**尤重：`params.G` 的 `0.01` ≠ 过户 0.01‰ ≠ 面值 0.5‰ ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05**（**params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰ ≠ 收盘价/VWAP/15:05**）。量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户 0.01‰，也不是面值 0.5‰，也不是收盘价、匹配 VWAP 或 15:05，也不是印花税率，更不是股票 2018-08-20 或深市切日。**尤重：`params.Y` 的 `0.02` ≠ 证管费 0.02‰ ≠ 切日日期**（**params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期**）。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**。**禁把占位读成过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**。**params 相对门槛 ≠ 切日日期 ≠ 过户费率 ≠ 印花税率 ≠ 证管费 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05**。禁止互读、禁止把门槛改写成过户费率、印花税率、证管费、收盘价、VWAP 或 15:05。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dx0_primary_demo`**：**写死冻结** **`invent_sse_fund_close_as_call_auction_pre_20260706`**（单一主报，单挂写死）。**禁止**与半泄露键 **`invent_asof_leak_sse_fund_close_auction`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DX1 仅核对日把「沪市基金收盘已经是集合」铺到全历史、铺到 2026-07-06 之前、或铺到深市基金，只作半泄露对照，**不得升格与 dx0 并列主报**，也不得把 `invent_asof_leak_sse_fund_close_auction` 写进 `dx0`。`copy_sse_stock_20180820_close_call_onto_fund` / `invent_szse_fund_close_change_20260706` / `vs_AW_close_call_fail_fallback` / `vs_D_open_close_halt` / `vs_AY_tick` / `vs_AX_handling` / `vs_R_etf_t0` / `vs_DW_warrant_option_transfer` / `vs_DV_cash_option_transfer` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_X_st_limit_pit` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `missing_venue_or_sec_type_or_cutover_rule_not_skip` **只作诊断桶，不得升格主报**。DX1 / 诊断桶 **不升格**。**禁把以下升格进 dx0**：股票2018-08-20抄套 / 发明深市基金2026切日 / AW失败回落 / D成交时点停牌 / X主板ST涨跌幅 / R假T+0 / V印花 / T证管费 / U过户 / AY价位 / AX经手费 / DW权证期权行权过户 / DV现金选择权 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后定价。这些只作对照/旁路，**不得升格进 `dx0`，不得另挂主报**。**零改 DW**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-AW**；**不重开假设-D**；**不重开假设-X**；**不重开假设-DW**；**不重开假设-DV**；**不重开假设-DU**；**不重开假设-DT**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-R**；**不重开假设-AY**；**不重开假设-AX**。**不抢实验 R**。**双字母 DX ≠ 单字母假设-D / 假设-X**。**双字母 DX ≠ 单字母 D/X**。

3. **沪市基金收盘产生方式诚实锚六键升格写死（不可再写「建议」）**：`params.sse_fund_close_honest=pit_continuous_pre_20260706_call_from_20260706_not_stock_20180820`；`params.sse_fund_close_scope=sse_fund_etf_close_generation_cutover`；`params.sse_fund_close_over_policy=skip_if_venue_or_sec_type_or_cutover_rule_missing`；`params.asof_check_date=2026-10-19`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺 venue / 证券类别 / 切日规则 → skip；沪市基金/ETF 2026-07-06 起收盘阶段=收盘集合，此前=连续竞价；禁止套股票 2018-08-20；禁止发明深市基金 2026 切日。AW ≠ 本页切日。禁止跑后改锚，或用集合 / 核对日规则铺满 / 抄股票 2018-08-20 / 发明深市切日 / 缺 venue/证券类别/切日规则仍硬填 / 把 AW/D/X/R/V/T/U/AY/AX/DW/DV/DU/DT/DS/DR 升格进 dx0 冒充诚实 PIT。**禁把占位读成过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**。**禁把 params.G 的 0.01 读成过户 0.01‰ 或面值 0.5‰ 或收盘价/VWAP/15:05**。**禁把 params.Y 的 0.02 读成证管费 0.02‰ 或切日日期**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**零改 DW**。**不抢实验 R**。**不重开假设-AW**；**不重开假设-D**；**不重开假设-X**。

**硬分列保住**：DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠D≠X≠A；**双字母 DX ≠ 单字母假设-D / 假设-X**；**双字母 DX ≠ 单字母 D/X**；**params.Y / params.G / params.N ≠ 实验字母 DX ≠ 单字母 D/X**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰ ≠ 收盘价/VWAP/15:05**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期**；**禁把占位读成过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**；**params 相对门槛 ≠ 切日日期 ≠ 过户费率 ≠ 印花税率 ≠ 证管费 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05**；**沪市基金收盘产生方式切日 ≠ 沪市股票 2018-08-20 切日 ≠ 深市基金 2026 变更（禁止发明）≠ AW收盘集合失败回落 ≠ D成交时点停牌 ≠ X主板ST涨跌幅 ≠ R假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ AY价位 ≠ AX经手费 ≠ DW权证期权行权过户 ≠ DV现金选择权 ≠ DU首日临停 ≠ DT整手价位 ≠ DS转股印花 ≠ DR盘后定价**；不抢 A；不抢实验 R；不改已齐/已冻 DA～DW 及 A–DQ 正文；**零改 DW**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-AW**；**不重开假设-D**；**不重开假设-X**；**不重开假设-DW**；**不重开假设-DV**；**不重开假设-DU**；**不重开假设-DT**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-R**；**不重开假设-AY**；**不重开假设-AX**；**禁把股票2018-08-20抄套 / 发明深市基金2026切日 / AW失败回落 / D成交时点停牌 / X主板ST涨跌幅 / R假T+0 / V印花 / T证管费 / U过户 / AY价位 / AX经手费 / DW权证期权行权过户 / DV现金选择权 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后定价 合成/混读升格进 dx0**。handoff 保持：`close_call_fail_handoff=aw_page`；`open_close_halt_handoff=d_page`；`tick_handoff=ay_page`；`handling_handoff=ax_page`；`etf_t0_handoff=r_page`；`warrant_option_transfer_handoff=dw_page`；`cash_option_transfer_handoff=dv_page`；`cb_ipo_halt_handoff=du_page`；`cb_lot_tick_handoff=dt_page`；`cb_conversion_stamp_handoff=ds_page`；`aft_pricing_handoff=dr_page`；`st_limit_pit_handoff=x_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；`merge_with_*=False`。

**状态**：**A/D–DX纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/开户/实盘。

## 变更
| 日期 | 变更 |
|------|------|
| 2026-11-10 | 复检/纸面齐——**A/D–DX纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设DX-20261110.md` 原样落入，SHA256=`866b260265e070e9b14c5ce91d8888c8ae2385868e39a833a61591c9533a5807`；三冻 tip=`68f6db58` / `68f6db589344e29f58c6fbc248909b0b201d050c`。只改状态标签；未改写已冻三条/六键；不改已齐 A–DQ / DA–DW；**零改 DW**；不改 #110–#132；不重开假设-V / 假设-T / 假设-U / 假设-AW / 假设-D / 假设-X / 假设-DW / 假设-DV / 假设-DU / 假设-DT / 假设-DS / 假设-DR / 假设-R；不抢实验 R；不预留 #134；不开回测/真数/开户/实盘。 |
| 2026-12-04 | 风控预检补丁·冻结三条写死——依据 `预检-假设DX-20261110.md`（SHA256=`4ef2991fdfd90bab56a2ab06bc6aeeaca5fc579430b35d8d5ab33ee9c8ecf69e`；结论=有条件通过；tip基=`9afeb6a8` / `9afeb6a81dd13036b9288725b51b04ae3de11ef6`；分支起点 HEAD=`c4e7985e` / `c4e7985eb6c0ca3ca54412969e241c83f7ae2522`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖收盘产生方式误套截 ΔSseFundClose / 净差异 / DX1−DX2；**params.Y/G/N ≠ 实验字母 DX ≠ 单字母 D/X**；**勿把 params.Y 读成假设-V 或假设-T 或假设-X 或假设-D，亦勿把 params.G 读成假设-U，亦勿把单字母假设-D / 假设-X 读成双字母 DX**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰ ≠ 收盘价/VWAP/15:05（量纲与语义不同）**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期**；**禁把占位读成过户‰、印花税率、证管费、收盘价、VWAP、15:05、股票2018-08-20、深市切日**；**params 相对门槛 ≠ 切日日期 ≠ 过户费率 ≠ 印花税率 ≠ 证管费 ≠ 收盘价 ≠ 匹配 VWAP ≠ 15:05**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成过户费率/印花税率/证管费/收盘价/VWAP/15:05/切日日期）；② `params.dx0_primary_demo=invent_sse_fund_close_as_call_auction_pre_20260706`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_sse_fund_close_auction` 双挂；DX1 不升格；诊断桶 `copy_sse_stock_20180820_close_call_onto_fund` / `invent_szse_fund_close_change_20260706` / `vs_AW_close_call_fail_fallback` / `vs_D_open_close_halt` / `vs_AY_tick` / `vs_AX_handling` / `vs_R_etf_t0` / `vs_DW_warrant_option_transfer` / `vs_DV_cash_option_transfer` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_X_st_limit_pit` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `missing_venue_or_sec_type_or_cutover_rule_not_skip` 不升格；**禁把股票2018-08-20抄套 / 发明深市基金2026切日 / AW失败回落 / D成交时点停牌 / X主板ST涨跌幅 / R假T+0 / V印花 / T证管费 / U过户 / AY价位 / AX经手费 / DW权证期权行权过户 / DV现金选择权 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后定价 合成/混读升格进 dx0**，只作对照/旁路，不得升格进 dx0 或另挂主报；**零改 DW**；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-AW；不重开假设-D；不重开假设-X；不重开假设-DW；不重开假设-DV；不重开假设-DU；不重开假设-DT；不重开假设-DS；不重开假设-DR；不重开假设-R；不重开假设-AY；不重开假设-AX；不抢实验 R；**双字母 DX ≠ 单字母假设-D / 假设-X**）；③ 锚六键写死 `sse_fund_close_honest=pit_continuous_pre_20260706_call_from_20260706_not_stock_20180820` / `sse_fund_close_scope=sse_fund_etf_close_generation_cutover` / `sse_fund_close_over_policy=skip_if_venue_or_sec_type_or_cutover_rule_missing` / `asof_check_date=2026-10-19` / `fill_time=next_open` / `fail_policy=skip`（缺 venue/证券类别/切日规则 → skip；沪市基金/ETF 2026-07-06 起收盘阶段=收盘集合，此前=连续竞价；禁止套股票 2018-08-20；禁止发明深市基金 2026 切日；AW ≠ 本页切日）。handoff 保持 `close_call_fail_handoff=aw_page` / `open_close_halt_handoff=d_page` / `tick_handoff=ay_page` / `handling_handoff=ax_page` / `etf_t0_handoff=r_page` / `warrant_option_transfer_handoff=dw_page` / `cash_option_transfer_handoff=dv_page` / `cb_ipo_halt_handoff=du_page` / `cb_lot_tick_handoff=dt_page` / `cb_conversion_stamp_handoff=ds_page` / `aft_pricing_handoff=dr_page` / `st_limit_pit_handoff=x_page` / `stamp_handoff=v_page` / `csrc_fee_handoff=t_page` / `transfer_fee_handoff=u_page`；`merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DX纸面齐**；不改已齐/已冻 DA～DW 及 A–DQ；**零改 DW**；不改 #110–#132；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-R；不重开假设-AW；不重开假设-D；不重开假设-X；不重开假设-DW；不抢实验 R；不预留 #134；不开回测/真数/开户/实盘。基于 tip=`9afeb6a8`。 |
| 2026-12-04 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。沪市基金收盘产生方式切日误套（成交规则）；`dx0_primary_demo` 建议 `invent_sse_fund_close_as_call_auction_pre_20260706`，单一主报，单挂，禁与 `invent_asof_leak_sse_fund_close_auction` 双挂，DX1 不升格；诊断桶 `copy_sse_stock_20180820_close_call_onto_fund` / `invent_szse_fund_close_change_20260706` / `vs_AW_close_call_fail_fallback` / `vs_D_open_close_halt` / `vs_AY_tick` / `vs_AX_handling` / `vs_R_etf_t0` / `vs_DW_warrant_option_transfer` / `vs_DV_cash_option_transfer` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_X_st_limit_pit` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `missing_venue_or_sec_type_or_cutover_rule_not_skip` 不升格；**尤重实验 R 不抢，禁把 vs_R_etf_t0 升格进 dx0**；**尤重不重开假设-V / 假设-T / 假设-U，禁把 vs_V_stamp / vs_T_csrc / vs_U_transfer 升格进 dx0**；**尤重 AW 收盘集合失败假抄前收/末笔 ≠ 本页何时改成集合，禁把 vs_AW_close_call_fail_fallback 升格**；**尤重沪市股票 2018-08-20 ≠ 沪市基金 2026-07-06，禁 copy_sse_stock_20180820_close_call_onto_fund 进主报**；**尤重深市基金尾盘已是集合、不作 2026 变更，禁 invent_szse_fund_close_change_20260706 升格**；**尤重双字母 DX ≠ 单字母假设-D / 假设-X，禁把 vs_D_open_close_halt / vs_X_st_limit_pit 升格**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-X / 假设-D**；**禁把占位读成切日日期、过户‰、印花税率、证管费**；**禁把 DW/DV/DU/DT/DS/DR 升格进 dx0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DX ≠ 单字母 D/X**；锚建议·待冻、未冻：`sse_fund_close_honest=pit_continuous_pre_20260706_call_from_20260706_not_stock_20180820` / scope=`sse_fund_etf_close_generation_cutover` / over_policy=`skip_if_venue_or_sec_type_or_cutover_rule_missing` / `asof_check_date=2026-10-19` / `fill_time=next_open` / `fail_policy=skip`；口径：缺 venue/证券类别/切日规则则 skip；沪市基金/ETF 2026-07-06 起收盘阶段=收盘集合，此前=连续竞价；禁止套股票 2018-08-20；禁止发明深市基金 2026 切日（**草稿方向，尚未冻，不要写成已冻**）；handoff：`close_call_fail_handoff=aw_page`，`open_close_halt_handoff=d_page`，`tick_handoff=ay_page`，`handling_handoff=ax_page`，`etf_t0_handoff=r_page`，`warrant_option_transfer_handoff=dw_page`，`cash_option_transfer_handoff=dv_page`，`cb_ipo_halt_handoff=du_page`，`cb_lot_tick_handoff=dt_page`，`cb_conversion_stamp_handoff=ds_page`，`aft_pricing_handoff=dr_page`，`st_limit_pit_handoff=x_page`，`stamp_handoff=v_page`，`csrc_fee_handoff=t_page`，`transfer_fee_handoff=u_page`；`merge_with_DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/D/X/A=False`；**DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠D≠X≠A**；**双字母 DX ≠ 单字母 D/X**；**未标纸面齐**；**不写 A/D–DX纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–DW；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–DW；**零改 DW**；不改 #110–#132；不重开假设-R；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-AW；不重开假设-D；不重开假设-X；不重开假设-DW；不写下一字母；不预留 #134；不开真数/回测/开户/实盘。基 tip=`d354b63f`（A/D–DW纸面齐已合，全长 `d354b63fcba8a972c86d7f3ab1069b10b3db09b2`；不改该 tip 上的 #110–#132，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
