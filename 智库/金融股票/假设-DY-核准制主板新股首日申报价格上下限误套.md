# 假设-DY · 核准制主板新股首日申报价格上下限误套（成交规则）

更新：2026-12-05  
来源：总管线 / 基 tip=`845521f` / 全长 `845521f055106b1ea90db02793ab1521a362e15b`（A/D–DX纸面齐已合）；**不改已冻 A–DQ / DA–DX**；**零改 DX**；**不改假设-DX 正文/预检/复检**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-DT / 假设-DU / 假设-DV / 假设-DW / 假设-DX / 假设-S / 假设-AX / 假设-AY / 假设-AW / 假设-T / 假设-U / 假设-V / 假设-W / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-E / 假设-F / 假设-J / 假设-G / 假设-CI / 假设-CK / 假设-Y / 假设-A / 假设-D / 假设-X 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ）；**不重开假设-R**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-G**；**不重开假设-CI**；**不重开假设-J**；**不重开假设-DU**；**不重开假设-Y**；**不重开假设-D**；**不重开假设-DX**；**不重开假设-W**；**不重开假设-X**；**不重开假设-AY**；**不重开假设-O**；**不重开假设-CK**；**不重开假设-DW**；**不重开假设-DV**；**不重开假设-DT**；**不重开假设-DS**；**不重开假设-DR**）后写下一草稿 DY；清单 #133=DX，本页占用 **#134=DY**；选题是回测把 **核准制主板新股上市首日的申报价格上下限**套错（诚实方向：核准制主板首日**集合竞价申报带 = 发行价 80%–120%**、**连续竞价申报带 = 发行价 64%–144%**；注册制「前 5 日不设涨跌幅」自 **2023-04-10** 落地，禁止倒铺到核准制主板首日；缺上市制度 / 发行价 / 官方规则则 skip；禁止只测连续窗当半泄露主报）；假设-G 只收无板日误套板块默认板，假设-CI 只收新股上市首日可成交性，假设-J 只收股票无板日临停，假设-DU 只收可转债首日临停，假设-Y 只收集合竞价量计入日线，假设-D 只收成交时点与停牌，假设-DX 只收沪市基金收盘产生方式切日，假设-R 只收股票 ETF 假 T+0，假设-V 只收股票印花税切日，假设-T 只收股票证管费切日，假设-U 只收股票过户切日；**新建实验 DY**；不写下一字母；不预留 #135  
状态：**预检有条件通过·三条已冻·待复检**（结论栏空；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DY纸面齐**；禁止把「核准制主板新股首日无申报带 / 前 5 日无板」当诚实锚；禁止把注册制无板倒铺到 2023-04-10 之前；禁止只测连续竞价窗当半泄露主报；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–DX**；**零改 DX**；**不改 #110–#133**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DY（#134）。一句话误开：回测把核准制主板新股**上市首日**当成注册制「前 5 日不设涨跌幅、无申报价格上下限」，或只拿连续竞价 64%–144% 去代表全日、丢掉集合竞价 80%–120%，或把 2023-04-10 才落地的注册制无板倒铺到核准制样本，或与 G无板日误套板块默认板 / CI新股首日可成交性 / J无板日临停 / DU可转债首日临停 / Y集合竞价量计入日线 / D成交时点与停牌 / X主板ST涨跌幅 / W除权判板 / AY基金价位 / DX沪市基金收盘切日 / O大宗通道 / CK协议大宗可成交性 / R股票ETF假T+0 / V股票印花 / T股票证管费 / U股票过户 混读，或缺上市制度 / 发行价 / 官方规则仍不 skip，系统性改写这只新股首日**能不能按这个价申报**。**禁把 G/CI/J/DU/Y/D/R/V/T/U 混读升格进 `dy0`**。**禁把 DX/DW/DV/DT/DS/DR 混读升格进 `dy0`**。**禁把 `copy_registration_nolimit_onto_approval_ipo` / `invent_only_call_band_ignore_continuous` / `invent_only_continuous_band_on_approval_ipo` 升格进主报或双挂**。**禁把 `invent_asof_leak_approval_ipo_band` 与主报双挂**。

> **字母消歧（硬）**：本页**实验字母 DY** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DY**；**尤重：`params.Y` ≠ 实验字母 DY**；**params.Y/G/N ≠ 实验字母 DY ≠ 单字母 D/Y**；**尤重：`params.Y/G/N` ≠ 实验字母 DY / 假设-Y / 假设-G**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**；**勿把 `params.Y` 读成实验字母 DY，亦勿读成假设-Y，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿读成假设-G，亦勿读成假设-D**；**尤重：`params.Y` 的 0.02 ≠ 实验字母 DY ≠ 证管费 0.02‰ ≠ 发行价 20% ≠ 切日日期 ≠ 80% ≠ 120% ≠ 64% ≠ 144% ≠ 过户‰**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DY**；**params.G ≠ 假设-G**；**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 80% ≠ 120% ≠ 64% ≠ 144% ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是申报带，不是切日，也不是过户费率）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DY**；**params.N ≠ 假设-Y**；**params.N ≠ 假设-G**）≠ **`params.Y2`**（写死冻结 0.015；不是 80%/120%/64%/144%）≠ **单字母实验 D**（成交时点与停牌；**双字母 DY ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 Y**（集合竞价量计入日线；**双字母 DY ≠ 单字母假设-Y；严禁复用假设-Y**；**尤重 params.Y ≠ 实验字母 DY**）≠ **单字母实验 G**（无板日误套板块默认板；**本页核准制首日申报价格上下限 ≠ 假设-G**；**严禁复用假设-G**；**不重开假设-G**）≠ **单字母实验 V**（股票印花税切日；**双字母 DY ≠ 单字母假设-V；严禁复用假设-V**；**不重开假设-V**）≠ **单字母实验 U**（股票过户费切日；**双字母 DY ≠ 单字母假设-U；严禁复用假设-U**；**不重开假设-U**）≠ **单字母实验 T**（股票证管费切日；**双字母 DY ≠ 单字母假设-T；严禁复用假设-T**；**不重开假设-T**）≠ **单字母实验 R**（股票 ETF 假 T+0；**双字母 DY ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `dy0`**）≠ **双字母 DX**（沪市基金收盘产生方式切日；**零改 DX**；**DY≠DX**）≠ **双字母 CI**（新股上市首日可成交性；可成交 ≠ 申报价格闸门）≠ **双字母 DU**（可转债首日临停；临停 ≠ 申报带）≠ **双字母 CK**（协议大宗可成交性）≠ **双字母 AY**（基金/ETF 最小价位）≠ **双字母 DW**（权证/期权行权过户）≠ **双字母 DV**（现金选择权行权过户）≠ **DT**（可转债整手价位）≠ **DS**（转股印花）≠ **DR**（可转债盘后定价通道）≠ **DQ**（ETF 申赎篮子过户）≠ **DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA**（费用旁路；不并进 `dy0`）≠ **S**（股票经手费切日）≠ **AX**（基金经手费）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债回转/涨跌幅/收盘）≠ **O**（大宗通道）≠ **M**（盘后通道）≠ **CH / CL / CR / CQ**（可成交性旁路）≠ **E / F / J / W / AW / X**（整手、取整、无板日临停、除权判板、收盘集合失败回落、主板 ST 涨跌幅）≠ **单字母实验 A**（板上枯竭）。**DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D**。**双字母 DY ≠ 单字母 D/Y**。**双字母 DY ≠ 单字母假设-D / 假设-Y**。**params.Y/G/N ≠ 实验字母 DY ≠ 单字母 D/Y**。**尤重 params.Y ≠ 实验字母 DY**。**尤重 params.Y/G/N ≠ 实验字母 DY / 假设-Y / 假设-G**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**。**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**。**params 相对门槛 ≠ 申报带百分数 ≠ 切日日期 ≠ 过户费率 ≠ 证管费 ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**。**核准制主板首日申报价格上下限 ≠ G无板日误套板块默认板 ≠ CI新股首日可成交性 ≠ J/DU临停 ≠ Y集合竞价量计入日线 ≠ D成交时点 ≠ 注册制前5日无板（禁止倒铺）≠ R股票ETF假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ DX沪市基金收盘切日**。**尤重：实验 R 不抢；禁把 `vs_R_etf_t0` 升格进 `dy0`**。**尤重：不重开假设-V / 假设-T / 假设-U；禁把 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 升格进 `dy0`**。**尤重：G = 无板日误套板块默认板 ≠ 本页核准制首日申报价格上下限；禁把 `vs_G_nolimit_board_default` 升格进 `dy0`**。**尤重：CI 可成交性 ≠ 本页申报价格闸门；禁把 `vs_CI_ipo_fill` 升格进 `dy0`**。**尤重：J/DU 临停 ≠ 本页申报带；禁把 `vs_J_nolimit_halt` / `vs_DU_cb_ipo_halt` 升格进 `dy0`**。**尤重：双字母 DY ≠ 单字母假设-D / 假设-Y；禁把 `vs_Y_call_vol_in_bar` 升格进 `dy0`**。**尤重：禁 `copy_registration_nolimit_onto_approval_ipo` / `invent_only_call_band_ignore_continuous` / `invent_only_continuous_band_on_approval_ipo` 升格进主报或双挂**。**尤重：DX/DW/DV/DU/DT/DS/DR 旁路诊断禁升格进 `dy0`**。**零改 DX**。

### 专节 · 双字母 DY ≠ 单字母假设-D / 假设-Y；且 ≠ 假设-G / 假设-CI / 假设-J / 假设-R / 假设-V / 假设-T / 假设-U / 假设-DX（硬）

| 维度 | 对照页 | 本页假设-DY（双字母） |
|------|--------|----------------------|
| 题面 G | **无涨跌幅日误套板块默认板**（把「前 5 日无板」或板块默认 ±10%/±20% 贴错窗口；假设-G） | **G = 无板日被套上板块默认板**。本页问的是核准制主板上市首日**本来就有**的申报价格上下限（集合 80%–120%、连续 64%–144%）被抹成「无板、无带」，或被注册制无板倒铺。两件是反方向，禁止合成。**DY≠G**；**params.G ≠ 假设-G**；**严禁复用假设-G**；**不重开假设-G**；**不改 G**；**尤重：禁把 `vs_G_nolimit_board_default` 升格进 `dy0`**；`nolimit_board_handoff=g_page` |
| 题面 CI | **新股上市首日可成交性误开**（默认首日订单必能按目标价或开盘价/收盘价全额成交；假设-CI） | **CI = 价已经能挂之后，单子能不能打满**。本页 = 这个价**能不能申报**（上下限闸门）。闸门开了也不等于全额成交。**DY≠CI**；**严禁复用假设-CI**；**不重开假设-CI**；**不改 CI**；**尤重：禁把 `vs_CI_ipo_fill` 升格进 `dy0`**；`ipo_fill_handoff=ci_page` |
| 题面 J | **股票无板日临停**（开盘价 30%/60%、各 10 分钟；假设-J） | 临停是成交过程里的暂停，不是申报价格上下限。**DY≠J**；**严禁复用假设-J**；**不重开假设-J**；**不改 J**；**尤重：禁把 `vs_J_nolimit_halt` 升格进 `dy0`**；`nolimit_halt_handoff=j_page` |
| 题面 DU | **可转债首日临停**（假设-DU） | 转债首日临停 ≠ 股票核准制首日申报带。**DY≠DU**；**不重开假设-DU**；**不改 DU**；**尤重：禁把 `vs_DU_cb_ipo_halt` 升格进 `dy0`**；`cb_ipo_halt_handoff=du_page` |
| 题面 Y | **集合竞价量计入日线**（日总量里有多少是集合竞价，不能当连续可冲击量；假设-Y） | 集合竞价的**量**怎么进日线，和集合竞价的**申报价**有没有上下限，是两件事。**双字母 DY ≠ 单字母假设-Y**；**严禁复用假设-Y**；**DY≠Y**；**尤重：`params.Y` ≠ 实验字母 DY**；**尤重：`params.Y/G/N` ≠ 实验字母 DY / 假设-Y / 假设-G**；**不重开假设-Y**；**不改 Y**；**尤重：禁把 `vs_Y_call_vol_in_bar` 升格进 `dy0`**；`call_vol_bar_handoff=y_page` |
| 题面 D | **成交时点与停牌**（次日开还是次日收；停牌日记不可交易；假设-D） | 先问这个价首日能不能申报，再问信号腿在次日开盘还是次日收盘成交。两件事不合成。**双字母 DY ≠ 单字母假设-D**；**严禁复用假设-D**；**DY≠D**；**params 字母 ≠ 假设-D**；**不重开假设-D**；**不改 D**；`merge_with_D=False` |
| 题面 注册制无板 | **主板注册制前 5 日不设涨跌幅**自 **2023-04-10**（首只按注册办法发行的主板股票上市首日）落地，不是印发日 2023-02-17（`事实与坑` 2026-10-09） | 把这句倒铺到核准制主板首日，首日申报带会整段消失。**禁倒铺**；**尤重：禁 `copy_registration_nolimit_onto_approval_ipo` 进主报或双挂**；该键只作诊断桶，不升格 |
| 题面 只测连续窗 | 连续竞价带是发行价 **64%–144%**，集合竞价带是发行价 **80%–120%**（方向，已写死冻结） | 只测连续窗，会把集合竞价时段的申报带漏掉，也不能拿它当半泄露主报。**尤重：禁 `invent_only_continuous_band_on_approval_ipo` 升格进主报或双挂**；**禁止只测连续窗当半泄露主报**。只测集合、丢掉连续，同样不升格：`invent_only_call_band_ignore_continuous` 只作诊断桶 |
| 题面 半泄露 | 核对日已经是注册制，容易把「首日无板」或「有申报带」铺满全历史 | `invent_asof_leak_approval_ipo_band` 只作半泄露对照。**禁与 `dy0` 双挂**；不得升格并列主报 |
| 题面 R | **股票 ETF 假 T+0**（假设-R） | **实验 R 不抢**。ETF 能不能当日回转，和核准制主板新股首日申报带，是两件事。**DY≠R**；**严禁复用假设-R**；**不重开假设-R**；**不改 R**；**尤重：禁把 `vs_R_etf_t0` 升格进 `dy0`**；`etf_t0_handoff=r_page` |
| 题面 V | **股票印花税切日**（假设-V） | **不重开假设-V**。印花切日 ≠ 申报价格上下限。占位不是印花税率，也不是 80%。**DY≠V**；**params 字母 ≠ 假设-V**；**不改 V**；**尤重：禁把 `vs_V_stamp` 升格进 `dy0`**；`stamp_handoff=v_page` |
| 题面 T | **股票证管费切日**（假设-T） | **不重开假设-T**。`params.Y` 的 0.02 不是证管费，也不是实验字母 DY。**DY≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：禁把 `vs_T_csrc` 升格进 `dy0`**；`csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日**（假设-U） | **不重开假设-U**。`params.G` 的 0.01 不是过户 0.01‰。**DY≠U**；**params 字母 ≠ 假设-U**；**不改 U**；**尤重：禁把 `vs_U_transfer` 升格进 `dy0`**；`transfer_fee_handoff=u_page` |
| 题面 DX | **沪市基金收盘产生方式切日**（假设-DX 已纸面齐） | 基金收盘怎么产生 ≠ 核准制新股首日申报带。**零改 DX**。**DY≠DX**；**不重开假设-DX**；**不改 DX 正文/预检/复检**；**尤重：禁把 `vs_DX_sse_fund_close` 升格进 `dy0`**；`sse_fund_close_handoff=dx_page` |
| 题面 X | **主板 ST 涨跌幅 PIT**（假设-X） | ST 板幅切日 ≠ 核准制首日申报带。**DY≠X**；**不重开假设-X**；**不改 X**；**禁把 `vs_X_st_limit_pit` 升格进 `dy0`**；`st_limit_pit_handoff=x_page` |
| 题面 W | **除权日复权价误判板**（假设-W） | 除权判板 ≠ 首日申报价格上下限。**DY≠W**；**不重开假设-W**；**不改 W**；**禁把 `vs_W_ex_right_limit` 升格进 `dy0`**；`ex_right_limit_handoff=w_page` |
| 题面 AY | **基金/ETF 最小价位**（假设-AY） | 价位取整 ≠ 申报带。**DY≠AY**；**不重开假设-AY**；**不改 AY**；**禁把 `vs_AY_tick` 升格进 `dy0`**；`tick_handoff=ay_page` |
| 题面 O | **大宗三通道**（假设-O） | 大宗通道 ≠ 竞价申报价格上下限。**DY≠O**；**不重开假设-O**；**不改 O**；**禁把 `vs_O_block_channel` 升格进 `dy0`**；`block_channel_handoff=o_page` |
| 题面 CK | **协议大宗可成交性**（假设-CK） | 大宗能不能成交 ≠ 首日申报价闸门。**DY≠CK**；**不重开假设-CK**；**不改 CK**；**禁把 `vs_CK_block_fill` 升格进 `dy0`**；`block_fill_handoff=ck_page` |
| 题面 DW / DV / DT / DS / DR | 行权过户、现金选择权过户、整手价位、转股印花、盘后定价通道 | 费用和通道旁路不并进 `dy0`。**DY≠DW≠DV≠DT≠DS≠DR**；**不重开、不改这些页**；**尤重：DX/DW/DV/DU/DT/DS/DR 旁路诊断禁升格进 `dy0`** |
| 题面 DQ–DA / S / AX / AC / Q / M / CH / CL / CR / CQ / E / F / J / AW | 费用、整手、可成交性等旁路 | 全部不并进 `dy0`。**DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D**。不改这些页 |
| 题面 A | **涨停可成交 / 板上枯竭** | **DY≠A**；**不抢 A 真数队列**；**不改 A** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_approval_ipo_day_as_nolimit_no_band`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_approval_ipo_band` / `invent_only_continuous_band_on_approval_ipo` 双挂；DY1 不升格；诊断桶不升格） |
| 文档 | 清单实验 DX 及上表各页（**只读；禁止改写**） | `假设-DY-核准制主板新股首日申报价格上下限误套.md`（新建） |
| 预检键 | 实验字母 DX / DW / … / D / Y / G / V / T / U / R，以及已存在 CI / CK | 实验字母 **DY** / `dy0_primary_demo`；**不得**占用或改写上述预检键；**params.Y/G/N ≠ 实验字母 DY** |

**禁止**：把 DY 写成「G / CI / J / Y / D / R 的续篇」；把「注册制前 5 日无板已在 2023-04-10 落地 / 无板日临停已有页 / 新股首日可成交性已有页」写成「核准制首日申报带已诚实」；把实验字母 DY 与单字母 D/Y 或 params.Y/G/N 混读；**尤重 params.Y ≠ 实验字母 DY**；**尤重 params.Y/G/N ≠ 实验字母 DY / 假设-Y / 假设-G**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**；**禁把占位 `0.02/0.01/0.05/0.015` 读成 80%/120%/64%/144%、切日日期、过户‰**；**实验 R 不抢**；**不重开假设-V / 假设-T / 假设-U**；**G 无板日误套板块默认板 ≠ 本页申报带**；**CI 可成交性 ≠ 本页申报价格闸门**；**J/DU 临停 ≠ 本页申报带**；**禁 `copy_registration_nolimit_onto_approval_ipo` / `invent_only_call_band_ignore_continuous` / `invent_only_continuous_band_on_approval_ipo` 升格进主报或双挂**；**禁止只测连续窗当半泄露主报**；**零改 DX**；**禁把 DX/DW/DV/DU/DT/DS/DR 以及 G/CI/J/Y/R/V/T/U 的诊断升格进 `dy0`**；把 `invent_asof_leak_approval_ipo_band` 与主报双挂；缺上市制度 / 发行价 / 官方规则仍硬填。本页主键只用 `dy0` / `dy1` / `dy2` 与 `approval_ipo_band_*`。不写下一字母。不预留 #135。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–DX；勿再只改清单）。**当前禁止标纸面齐**。**不写 A/D–DY纸面齐**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测把 **核准制主板新股上市首日**当成 **没有申报价格上下限**（或当成注册制「前 5 日不设涨跌幅」），或只测连续竞价窗、或与 G 的无板日默认板、CI 的首日可成交性、J/DU 的临停、Y 的集合竞价量、D 的开收时点、R 的假 T+0、V/T/U 的费用切日、DX 的基金收盘切日混读，或缺上市制度 / 发行价 / 官方规则仍不 skip，相对「缺字段则 skip；核准制主板首日集合申报带 = 发行价 80%–120%、连续 = 发行价 64%–144%；注册制无板自 2023-04-10 落地，禁止倒铺」的诚实组，会**系统性改写这只新股首日能不能按这个价申报**——带外的单子被写成可挂，或带内的集合竞价单被连续窗误杀。方向是相对诚实锚偏误。

核对日方向（随锚写死；禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期）：`事实与坑` 2026-10-09 写明，核准制阶段沪深主板新股首日不是「前 5 日无板」。上交所《关于进一步加强新股上市初期交易监管的通知》对首日申报价格按发行价设上下限，集合竞价 **80%–120%**，连续竞价 **64%–144%**；2014-06-16 新闻稿仍保留该申报控制。第 2 个交易日起才是普通 ±10%，那一日的板块板不在本页主报里。主板注册制「前 5 日不设涨跌幅」要到按注册办法发行的**首只主板股票上市首日**才落地，该日是 **2023-04-10**，不是文件印发日 2023-02-17。科创板开市起、创业板 2020-08-24 起才是另一套「前 5 日无板」，不要把核准制主板这道申报带铺到那些板块，也不要把那些板块的无板倒贴回核准制主板首日。本页把核准制主板首日这一道收成已写死冻结的锚。方向随锚写死，不要把申报带铺成全历史唯一规则，也不要把占位读成申报带百分数。无板日默认板、首日能不能打满、临停、集合竞价量、费用切日、基金收盘切日都留在各自的页。缺上市制度、发行价或官方规则，整笔 skip。**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**。**尤重 params.Y ≠ 实验字母 DY**。

证伪方向：若天真组 / 半泄露组相对诚实组的申报带误套截在标定噪声带内可忽略，且「核准制首日被当成无带 / 注册制无板倒铺 / 只测连续窗 / 只测集合窗 / 核对日泄露 / vs G·CI·J·DU·Y·D·X·W·AY·DX·O·CK·R·V·T·U」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dy0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结；禁止标纸面齐；不写 A/D–DY纸面齐）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DY ≠ 单字母假设-D / 假设-Y**；勿把 params.Y 读成实验字母 DY，亦勿读成假设-Y，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿读成假设-G，亦勿读成假设-D
# 【消歧】尤重：params.Y ≠ 实验字母 DY
# 【消歧】尤重：params.Y/G/N ≠ 实验字母 DY / 假设-Y / 假设-G
# 【消歧】params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D
# 【消歧】尤重：params.Y 的 0.02 ≠ 实验字母 DY ≠ 证管费 0.02‰ ≠ 发行价 20% ≠ 切日日期 ≠ 80%/120%/64%/144% ≠ 过户‰
# 【消歧】尤重：params.G 的 0.01 ≠ 过户 0.01‰ ≠ 80% ≠ 120% ≠ 64% ≠ 144% ≠ 发行价 20%/30% ≠ 开盘价 30%/60%（无量纲相对门槛 ≠ 申报带 ≠ 过户费率 ≠ 证管费 ≠ 切日）
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DY ≠ 假设-Y ≠ 假设-G ≠ 单字母假设-N**
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期
# 【消歧】params 相对门槛 ≠ 申报带百分数 ≠ 切日日期 ≠ 过户费率 ≠ 证管费 ≠ 发行价 20%/30% ≠ 开盘价 30%/60%
# 【消歧】三条已冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值
# params.Y2                               写死冻结 0.015（不是 80%/120%/64%/144%，不是发行价 20%/30%，不是开盘价 30%/60%）
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：申报带误套截 ΔApprovalIpoBand / 净差异 / DY1−DY2；**params.Y/G/N ≠ 实验字母 DY ≠ 单字母 D/Y**；**尤重 params.Y ≠ 实验字母 DY**；**尤重 params.Y/G/N ≠ 实验字母 DY / 假设-Y / 假设-G**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 80%/120%/64%/144% ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价 20% ≠ 实验字母 DY ≠ 切日日期**；**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        写死冻结 next_open
# params.asof_check_date                  写死冻结 2026-10-09（这是核对日，不是切日，也不是占位，也不是 2023-04-10）
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.approval_ipo_band_honest         写死冻结 pit_call_80_120_cont_64_144_pre_20230410_not_registration_nolimit
#   诚实锚方向（已写死冻结）：
#   缺上市制度、发行价或官方规则 → skip
#   核准制主板上市首日：集合竞价申报带 = 发行价 80%–120%
#   连续竞价申报带 = 发行价 64%–144%
#   注册制无板自 2023-04-10 落地，禁止倒铺到核准制主板首日
#   禁止只测连续窗当半泄露主报
#   禁止把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期
#   枚举已写死冻结
#   锚名字里的百分数和日期是机制方向，不是 params.Y/G/N/Y2
# params.approval_ipo_band_scope          写死冻结 approval_mainboard_ipo_day1_order_price_band
#   只看核准制主板新股上市首日的申报价格上下限
#   不是无板日默认板，不是首日能不能打满，不是临停，不是集合竞价量，不是费用
# params.approval_ipo_band_over_policy    写死冻结 skip_if_listing_regime_or_issue_px_or_official_rule_missing
#   缺上市制度 / 发行价 / 官方规则则 skip
# params.nolimit_board_handoff            建议 g_page
#   无板日误套板块默认板交 G；G ≠ 本页申报带；不重开假设-G；不改 G
#   诊断桶 vs_G_nolimit_board_default 不得升格进 dy0
# params.ipo_fill_handoff                 建议 ci_page
#   新股首日可成交性交 CI；CI ≠ 本页申报价格闸门；不重开假设-CI；不改 CI
#   诊断桶 vs_CI_ipo_fill 不得升格进 dy0
# params.nolimit_halt_handoff             建议 j_page
#   股票无板日临停交 J；J ≠ 本页申报带；不重开假设-J；不改 J
#   诊断桶 vs_J_nolimit_halt 不得升格进 dy0
# params.cb_ipo_halt_handoff              建议 du_page
#   可转债首日临停交 DU；不重开假设-DU；不改 DU
#   诊断桶 vs_DU_cb_ipo_halt 不得升格进 dy0
# params.st_limit_pit_handoff             建议 x_page
#   主板 ST 涨跌幅交 X；不重开假设-X；不改 X
#   诊断桶 vs_X_st_limit_pit 不得升格进 dy0
# params.ex_right_limit_handoff           建议 w_page
#   除权判板交 W；不重开假设-W；不改 W
#   诊断桶 vs_W_ex_right_limit 不得升格进 dy0
# params.tick_handoff                     建议 ay_page
#   基金价位交 AY；不重开假设-AY；不改 AY
#   诊断桶 vs_AY_tick 不得升格进 dy0
# params.sse_fund_close_handoff           建议 dx_page
#   沪市基金收盘切日交 DX；零改 DX；不重开假设-DX；不改 DX 正文/预检/复检
#   诊断桶 vs_DX_sse_fund_close 不得升格进 dy0
# params.block_channel_handoff            建议 o_page
#   大宗通道交 O；不重开假设-O；不改 O
#   诊断桶 vs_O_block_channel 不得升格进 dy0
# params.block_fill_handoff               建议 ck_page
#   协议大宗可成交性交 CK；不重开假设-CK；不改 CK
#   诊断桶 vs_CK_block_fill 不得升格进 dy0
# params.call_vol_bar_handoff             建议 y_page
#   集合竞价量计入日线交 Y；双字母 DY ≠ 单字母假设-Y；不重开假设-Y；不改 Y
#   尤重 params.Y ≠ 实验字母 DY
#   诊断桶 vs_Y_call_vol_in_bar 不得升格进 dy0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 dy0；不改 R
#   诊断桶 vs_R_etf_t0 不得升格进 dy0
# params.stamp_handoff                    建议 v_page
#   股票印花切日交 V；不重开假设-V；params 字母 ≠ 假设-V；不改 V
#   诊断桶 vs_V_stamp 不得升格进 dy0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；params 字母 ≠ 假设-T；不改 T
#   诊断桶 vs_T_csrc 不得升格进 dy0
# params.transfer_fee_handoff             建议 u_page
#   股票过户切日交 U；不重开假设-U；params 字母 ≠ 假设-U；不改 U
#   诊断桶 vs_U_transfer 不得升格进 dy0
# params.dy0_primary_demo                 写死冻结 invent_approval_ipo_day_as_nolimit_no_band
#   单一主报写死，单挂
#   禁与 invent_asof_leak_approval_ipo_band 双挂
#   禁与 invent_only_continuous_band_on_approval_ipo 双挂
#   DY1 不升格；诊断桶不升格
#   半泄露名只作对照，不得升格进 dy0，不得双挂
#   禁止只测连续窗当半泄露主报
#   诊断桶 invent_only_call_band_ignore_continuous / copy_registration_nolimit_onto_approval_ipo / vs_G_nolimit_board_default / vs_CI_ipo_fill / vs_J_nolimit_halt / vs_DU_cb_ipo_halt / vs_X_st_limit_pit / vs_W_ex_right_limit / vs_AY_tick / vs_DX_sse_fund_close / vs_O_block_channel / vs_CK_block_fill / vs_R_etf_t0 / vs_V_stamp / vs_T_csrc / vs_U_transfer / vs_Y_call_vol_in_bar / missing_listing_regime_or_issue_px_or_official_rule_not_skip 不得升格进 dy0
#   尤重：禁 copy_registration_nolimit_onto_approval_ipo / invent_only_call_band_ignore_continuous / invent_only_continuous_band_on_approval_ipo 升格进主报或双挂
#   尤重：实验 R 不抢
#   尤重：不重开假设-V / 假设-T / 假设-U
#   尤重：G/CI/J/DU/Y/D 不升格
#   尤重：零改 DX；禁把 DX/DW/DV/DU/DT/DS/DR 升格进 dy0
#   禁把以下升格进 dy0：G无板日默认板 / CI可成交性 / J·DU临停 / DX沪市基金收盘 / Y集合竞价量 / D成交时点 / R假T+0 / V印花 / T证管费 / U过户 / Q·CQ / 注册制无板倒铺 / 只测连续窗半泄露
# params.dy0_invent_approval_ipo_day_as_nolimit_no_band 建议 True
# params.dy1_asof_leak_approval_ipo_band_only 建议 True
#   半泄露对照；DY1 不升格并列主报；不得把 invent_asof_leak_approval_ipo_band 写进 dy0
# params.dy1_only_continuous_band_on_approval_ipo 建议 True
#   只测连续窗的半泄露键；禁止把它当成半泄露主报；不得与 dy0 双挂；不得升格
# params.dy2_pit_call_80_120_cont_64_144_pre_20230410_not_registration_nolimit 建议 True
# params.merge_with_DX                    建议 False
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
# params.merge_with_X                     建议 False
# params.merge_with_G                     建议 False
# params.merge_with_CI                    建议 False
# params.merge_with_CK                    建议 False
# params.merge_with_Y                     建议 False
# params.merge_with_A                     建议 False
# params.merge_with_D                     建议 False
# params.missing_listing_regime_or_issue_px_or_official_rule_policy 建议 skip
# params.day_freq_proxy                   建议 approval_ipo_band_sensitivity
# params.universe_rule                    建议 approval_ipo_band_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dy_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DY；勿读成单字母 D/Y
#   不另挂主报，不预留 #135，不写下一字母
```

### 2.2 三组对照（DY0 / DY1 / DY2）

组名 DY0 / DY1 / DY2 是本页三组，≠ 单字母实验 D（成交时点与停牌），亦 ≠ 单字母实验 Y（集合竞价量计入日线）。**双字母 DY ≠ 单字母假设-D / 假设-Y**。**params.Y/G/N ≠ 实验字母 DY ≠ 单字母 D/Y**。**尤重 params.Y ≠ 实验字母 DY**。**尤重 params.Y/G/N ≠ 实验字母 DY / 假设-Y / 假设-G**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**。

| 组 | 角色 | 口径 |
|----|------|------|
| DY0 | 天真 / 核准制主板首日当成无申报带 | 按 `dy0_primary_demo` **写死冻结**单一主报 `invent_approval_ipo_day_as_nolimit_no_band`（单挂写死）：把核准制主板新股上市首日当成没有申报价格上下限。**禁**与 `invent_asof_leak_approval_ipo_band` 双挂。**禁**与 `invent_only_continuous_band_on_approval_ipo` 双挂。**禁把注册制无板倒铺、只测集合窗、只测连续窗、G/CI/J/DU/Y/R/V/T/U、DX/DW/DV/DT/DS/DR 合成进 `dy0`** |
| DY1 | 半泄露 | 仅用核对日「注册制首日已经无板 / 已经有另一套带」把规则铺到核准制主板首日（`invent_asof_leak_approval_ipo_band`），或只测连续竞价 64%–144%、不看集合 80%–120%（`invent_only_continuous_band_on_approval_ipo`）。两条都**不得升格并列主报**，不得写进 `dy0`，不得双挂。**禁止只测连续窗当半泄露主报** |
| DY2 | 诚实 / 核准制主板首日申报带 | `approval_ipo_band_honest=pit_call_80_120_cont_64_144_pre_20230410_not_registration_nolimit`（写死冻结）：缺上市制度/发行价/官方规则则 skip；核准制主板首日集合申报带=发行价 80%–120%、连续=发行价 64%–144%；注册制无板自 2023-04-10 落地，禁止倒铺。无板日默认板只消费 G，首日能不能打满只消费 CI，临停只消费 J 与 DU，集合竞价量只消费 Y，开收时点只消费 D，基金收盘切日只消费 DX，假 T+0 只消费 R，费用只消费 V/T/U，其余旁路只消费对应页，或显式旁路 |

把注册制无板倒铺、只测集合窗、只测连续窗、把核对日规则铺满历史、以及相对 G/CI/J/DU/X/W/AY/DX/O/CK/R/V/T/U/Y 的对照，放进 §4.1 分桶，**只作诊断桶或半泄露对照，不得升格为第二个主报**。`copy_registration_nolimit_onto_approval_ipo` 只标记「有人把注册制无板抄到核准制首日」，**不得进主报，不得双挂**。`invent_only_call_band_ignore_continuous` 只标记「只测了集合带、丢掉连续带」，**不得升格**。`invent_only_continuous_band_on_approval_ipo` 只标记「只测了连续窗」，**不得当半泄露主报，不得双挂**。`invent_asof_leak_approval_ipo_band` 只标记核对日泄露。`vs_G_nolimit_board_default` 只标记无板日默认板对照。`vs_CI_ipo_fill` 只标记首日可成交性对照。`vs_J_nolimit_halt` / `vs_DU_cb_ipo_halt` 只标记临停对照。`vs_Y_call_vol_in_bar` 只标记集合竞价量对照。`vs_R_etf_t0` 只标记假 T+0 对照。`vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只标记费用对照。`vs_DX_sse_fund_close` 只标记基金收盘切日，**零改 DX**。`vs_X_st_limit_pit` / `vs_W_ex_right_limit` / `vs_AY_tick` / `vs_O_block_channel` / `vs_CK_block_fill` 只标记旁路。`missing_listing_regime_or_issue_px_or_official_rule_not_skip` 只标记缺字段仍不 skip。这些都**不得升格进 `dy0`**。DW/DV/DT/DS/DR 的旁路诊断同样**不得升格进 `dy0`**。

### 2.3 切日窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-09`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dy0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺上市制度 / 发行价 / 官方规则则 skip；核准制主板首日集合申报带 = 发行价 80%–120%，连续 = 发行价 64%–144%；注册制无板自 2023-04-10 落地，禁止倒铺；禁止只测连续窗当半泄露主报。`params.G` 的 0.01 不是过户费 0.01‰，也不是 80%/120%/64%/144%，也不是发行价 20%/30%，也不是开盘价 30%/60%；`params.Y` 的 0.02 不是实验字母 DY，也不是证管费 0.02‰，也不是发行价 20%，也不是切日，也不是 64% 或 144%；四个占位也不是 2023-04-10、2023-02-17 或核对日。**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**。本页**不开回测**；不拉真数；不做实盘；不开户。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dy0_primary_demo` / `params.Y`·G·N·Y2 / 申报带开关 / 桶 / 是否把注册制无板倒铺、或只测连续窗、或把占位读成 80%/120%/64%/144%）。本页不开跑。禁 null。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DY0）/ 半泄露组（DY1）相对诚实组（DY2）的申报带误套截**显著且集中在核准制主板新股上市首日被当成无申报带**的桶；分桶「注册制无板倒铺 / 只测连续窗 / 只测集合窗 / 核对日泄露 / vs G·CI·J·DU·Y·X·W·AY·DX·O·CK·R·V·T·U」不改变主结论方向。成功不依赖把占位读成 80%/120%/64%/144%，也不把 `params.Y` 读成实验字母 DY，也不把 `params.G` 的 0.01 读成过户费或读成假设-G。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 G 的无板日默认板、CI 的首日可成交性、J/DU 的临停、Y 的集合竞价量、D 的开收时点、X 的 ST 板幅、W 的除权判板、R 的假 T+0、V/T/U 的费用、DX 的基金收盘切日、O/CK 的大宗、DW/DV/DT/DS/DR 的旁路、或 A 的板上容量解释；或 `dy0_primary_demo` 与 `invent_asof_leak_approval_ipo_band` 双挂；或与 `invent_only_continuous_band_on_approval_ipo` 双挂；或 DY1 升格并列主报；或只测连续窗被当成半泄露主报；或诊断桶升格主报；或 `copy_registration_nolimit_onto_approval_ipo` / `invent_only_call_band_ignore_continuous` 进主报；或实验字母 DY 与单字母 D/Y 或 params.Y/G/N 混读；或把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期；或缺上市制度 / 发行价 / 官方规则仍不 skip；或重开假设-R / 假设-V / 假设-T / 假设-U / 假设-G / 假设-CI / 假设-J / 假设-Y / 假设-D / 假设-DX；或改 DX 正文/预检/复检；或标纸面齐；或写成 A/D–DY纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 DY0/DY1/DY2。无板日默认板走 G，首日能不能打满走 CI，临停走 J 与 DU，集合竞价量走 Y，开收时点走 D，ST 板幅走 X，除权判板走 W，价位走 AY，基金收盘切日走 DX，大宗走 O 与 CK，假 T+0 走 R，费用走 V/T/U，都不改。报告申报带误套截。不把 80%/120%/64%/144% 或 2023-04-10 标成已冻门槛。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_approval_ipo_day_as_nolimit_no_band` / `invent_asof_leak_approval_ipo_band` / `invent_only_continuous_band_on_approval_ipo` / `invent_only_call_band_ignore_continuous` / `copy_registration_nolimit_onto_approval_ipo` / `vs_G_nolimit_board_default` / `vs_CI_ipo_fill` / `vs_J_nolimit_halt` / `vs_DU_cb_ipo_halt` / `vs_X_st_limit_pit` / `vs_W_ex_right_limit` / `vs_AY_tick` / `vs_DX_sse_fund_close` / `vs_O_block_channel` / `vs_CK_block_fill` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_Y_call_vol_in_bar` / `missing_listing_regime_or_issue_px_or_official_rule_not_skip`

`invent_approval_ipo_day_as_nolimit_no_band` 才是写死冻结的单一主报名（单挂）。`invent_asof_leak_approval_ipo_band` 与 `invent_only_continuous_band_on_approval_ipo` 只服务半泄露对照，**不得升格进 `dy0`，不得双挂**。**禁止只测连续窗当半泄露主报**。自 `invent_only_call_band_ignore_continuous` 起至 `missing_listing_regime_or_issue_px_or_official_rule_not_skip` **只作诊断桶**：它们不是 `dy0`，也不是 DY1 主报，**不得升格主报，不得双挂**。**禁把 `copy_registration_nolimit_onto_approval_ipo` / `invent_only_call_band_ignore_continuous` / `invent_only_continuous_band_on_approval_ipo` 升格进主报或双挂**。没有「G 无板日默认板 + 本页申报带」合成主报，也没有「CI 可成交 + 本页闸门」合成主报，也没有「只测连续窗」主报。**实验 R 不抢**。**不重开假设-V / 假设-T / 假设-U**。**零改 DX**。**禁把 DX/DW/DV/DU/DT/DS/DR 升格进 `dy0`**。**禁把 G/CI/J/DU/Y/D 升格进 `dy0`**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「核准制主板新股首日无申报带」或「前 5 日不设涨跌幅铺满注册制之前」拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成实验字母 DY，或当成证管费 0.02‰，或当成发行价 20%，或当成切日，或当成 80%。**尤重 params.Y ≠ 实验字母 DY**。**params 字母 ≠ 假设-Y**。**params 字母 ≠ 假设-T**。**params 字母 ≠ 假设-D**。
- 把 `params.G` 的 0.01 当成过户 0.01‰，或当成假设-G，或当成 80%/120%/64%/144%，或当成发行价 20%/30%，或当成开盘价 30%/60%，或当成 120%。**尤重 params.G ≠ 假设-G**。**params 字母 ≠ 假设-U**。**params 字母 ≠ 假设-G**。**params 字母 ≠ 假设-V**。
- 把 `params.N` 的 0.05 当成实验字母 DY 或假设-Y / 假设-G。**尤重 params.Y/G/N ≠ 实验字母 DY / 假设-Y / 假设-G**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 80%/120%/64%/144%、切日日期、过户‰。**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**。**params 相对门槛 ≠ 申报带百分数 ≠ 切日日期 ≠ 过户费率 ≠ 证管费 ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**。**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**。
- 缺上市制度、发行价或官方规则仍不 skip。诊断桶 `missing_listing_regime_or_issue_px_or_official_rule_not_skip` 只作对照，不得升格。
- 把核对日「已经是注册制前 5 日无板」写成全历史规则，或铺到 2023-04-10 之前的核准制主板首日。锚六键已写死冻结。半泄露键 `invent_asof_leak_approval_ipo_band` 不得与主报双挂。
- 把注册制无板抄到核准制首日。诊断桶 `copy_registration_nolimit_onto_approval_ipo` 只作对照，**禁进主报，禁双挂**。
- 只测集合竞价 80%–120%、丢掉连续 64%–144%。诊断桶 `invent_only_call_band_ignore_continuous` 只作对照，**禁升格，禁双挂**。
- 只测连续竞价窗，并把它当成半泄露主报。`invent_only_continuous_band_on_approval_ipo` 只作对照，**禁升格进主报，禁双挂**。**禁止只测连续窗当半泄露主报**。
- 把假设-G 的「无板日误套板块默认板」和本页申报带合成后升格。**不重开假设-G**。诊断桶 `vs_G_nolimit_board_default` 只作对照。
- 把假设-CI 的新股首日可成交性和本页申报价格闸门合成后升格。**不重开假设-CI**。诊断桶 `vs_CI_ipo_fill` 只作对照。
- 把假设-J / 假设-DU 的临停和本页申报带合成后升格。诊断桶 `vs_J_nolimit_halt` / `vs_DU_cb_ipo_halt` 只作对照。**不重开假设-J**；**不重开假设-DU**。
- 把假设-Y 的集合竞价量计入日线和本页合成后升格。**双字母 DY ≠ 单字母假设-Y**。**尤重 params.Y ≠ 实验字母 DY**。诊断桶 `vs_Y_call_vol_in_bar` 只作对照。
- 把假设-D 的开收时点、停牌和本页申报带合成后升格。**双字母 DY ≠ 单字母假设-D**。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格。**实验 R 不抢**。诊断桶 `vs_R_etf_t0` 只作对照。
- 把假设-V / 假设-T / 假设-U 和本页合成或混读后升格。诊断桶 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只作对照。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。
- 把 X 的 ST 板幅、W 的除权判板、AY 的价位、O 的大宗通道、CK 的大宗可成交性和本页合成后升格。诊断桶 `vs_X_st_limit_pit` / `vs_W_ex_right_limit` / `vs_AY_tick` / `vs_O_block_channel` / `vs_CK_block_fill` 只作对照。
- 把 DX/DW/DV/DU/DT/DS/DR 旁路诊断升格进 `dy0`。**零改 DX**。**不重开假设-DX**。
- `dy0_primary_demo` 与 `invent_asof_leak_approval_ipo_band` 或 `invent_only_continuous_band_on_approval_ipo` 双挂；DY1 升格并列主报。
- 实验字母 DY 与单字母 D/Y 或 params.Y/G/N 混读。**双字母 DY ≠ 单字母 D/Y**。
- 改 DX / DW / DV / DU / DT / DS / DR / G / CI / J / Y / D / R / V / T / U 及其他已冻页正文；改 #110–#133；标纸面齐；写成 A/D–DY纸面齐；预留 #135；开真数/回测/开户/实盘；用复权价当申报带的判据；结论写成「这类新股首日更好成交所以能买」。
- **纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–DX；勿再只改清单）。当前禁止标纸面齐。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权路径、交易日、**交易所 venue**、**上市制度**（核准制主板 / 注册制主板 / 科创板 / 创业板 / 其他）、**是不是上市首日**。制度或首日标记分不清则 skip，不把注册制无板套到核准制，也不把核准制申报带套到科创板或创业板。
- **发行价**。没有发行价就没法标 80%–120% 和 64%–144%，整笔 skip，不用占位数字去填一个价。
- 官方规则是否在册：核准制主板首日申报价格上下限（建议方向：集合竞价按发行价 80%–120%，连续竞价按发行价 64%–144%），以及注册制无板的落地日（建议方向 2023-04-10，不是印发日 2023-02-17）。规则不在册则 skip。
- 申报时段要能分清集合竞价和连续竞价。只拿到全日一根 K 线、分不清时段，不要默认「按连续窗放行」，也不要默认「全日无带」。
- 第 2 个交易日起的普通 ±10% 不在本页主报。需要板块默认板的，走 G 的无板日对照，不在这里另挂。
- 旁路消费：G 的无板日默认板、CI 的首日可成交性、J 的无板日临停、DU 的转债首日临停、Y 的集合竞价量、D 的成交时点、X 的 ST 板幅、W 的除权判板、AY 的价位、DX 的基金收盘切日、O/CK 的大宗、R 的假 T+0、V/T/U 的费用（见 §2.1 handoff）。**本页不改写这些页。零改 DX。**
- 未复权路径；asof **写死冻结** `2026-10-09`。核对日在 2023-04-10 之后，所以「核对日当天主板新股前 5 日已经无板」不能倒灌到核准制主板首日。`事实与坑` 2026-10-09 是方向来源，不是已冻的全历史规则。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-09`；`fail_policy=skip`；`approval_ipo_band_honest=pit_call_80_120_cont_64_144_pre_20230410_not_registration_nolimit`；`approval_ipo_band_scope=approval_mainboard_ipo_day1_order_price_band`；`approval_ipo_band_over_policy=skip_if_listing_regime_or_issue_px_or_official_rule_missing`；`dy0_primary_demo=invent_approval_ipo_day_as_nolimit_no_band`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_approval_ipo_band` / `invent_only_continuous_band_on_approval_ipo` 双挂；DY1 不升格；诊断桶不升格；**禁止只测连续窗当半泄露主报**；**禁把注册制无板倒铺、只测集合窗、G/CI/J/DU/Y/R/V/T/U 与 DX/DW/DV/DT/DS/DR 升格进 `dy0`**）；`nolimit_board_handoff=g_page`；`ipo_fill_handoff=ci_page`；`nolimit_halt_handoff=j_page`；`cb_ipo_halt_handoff=du_page`；`st_limit_pit_handoff=x_page`；`ex_right_limit_handoff=w_page`；`tick_handoff=ay_page`；`sse_fund_close_handoff=dx_page`；`block_channel_handoff=o_page`；`block_fill_handoff=ck_page`；`call_vol_bar_handoff=y_page`；`etf_t0_handoff=r_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；`merge_with_DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/Y/A/D=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是 80%/120%/64%/144%，不是切日日期，不是过户费率，不是证管费，不是发行价 20%/30%，不是开盘价 30%/60%；**params.Y/G/N ≠ 实验字母 DY ≠ 单字母 D/Y**；**尤重 params.Y ≠ 实验字母 DY**；**尤重 params.Y/G/N ≠ 实验字母 DY / 假设-Y / 假设-G**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价 20% ≠ 实验字母 DY ≠ 切日日期**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 80%/120%/64%/144% ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**；**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #135。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`845521f`（A/D–DX纸面齐已合，全长 `845521f055106b1ea90db02793ab1521a362e15b`）；三冻补丁基 tip=`e5b3e812` / `e5b3e81221a7e17eb3c95d7c8bce2aaf7645bf03`；分支起点 HEAD=`d2bbca50` / `d2bbca503a0a5edd5e3b14204855d1980bdd0651`。**不改已冻 A–DQ / DA–DX**。**零改 DX**。**不改 #110–#133**。状态=**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DY纸面齐**。

---

## 8. 结论

（空；**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DY纸面齐**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-12-05）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DY-20261110.md`（原样落入，不改结论；SHA256=`d28c6a91a20822edeabd814f146a40bf88ae6f819491e49d747a06754078718a`；预检 2026-11-10；**结论：有条件通过**；tip基=`e5b3e812` / `e5b3e81221a7e17eb3c95d7c8bce2aaf7645bf03`；本补丁分支起点 HEAD=`d2bbca50` / `d2bbca503a0a5edd5e3b14204855d1980bdd0651`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于申报带误套截 ΔApprovalIpoBand、净差异、DY1−DY2 专项。**`params.Y` ≠ 实验字母 DY**；**`params.G` ≠ 实验字母 DY**；**`params.N` ≠ 实验字母 DY**；亦 ≠ 单字母假设-D / 假设-Y。**params.Y/G/N ≠ 实验字母 DY ≠ 单字母 D/Y**。**勿把 `params.Y` 读成实验字母 DY，亦勿读成假设-Y，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿读成假设-G，亦勿读成假设-D，亦勿把 `params.G` 读成假设-G，亦勿把 `params.G` 读成假设-U，亦勿把单字母假设-D / 假设-Y 读成双字母 DY**。**尤重：`params.Y` ≠ 实验字母 DY**。**尤重：`params.G` 的 `0.01` ≠ 过户 0.01‰ ≠ 80% ≠ 120% ≠ 64% ≠ 144% ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**（**params.G 的 0.01 ≠ 过户 0.01‰ ≠ 80%/120%/64%/144% ≠ 发行价 20%/30%**）。量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户 0.01‰，也不是 80%/120%/64%/144%，也不是发行价 20%/30%，也不是开盘价 30%/60%，更不是假设-G。**尤重：`params.Y` 的 `0.02` ≠ 证管费 0.02‰ ≠ 发行价 20% ≠ 实验字母 DY ≠ 切日日期**（**params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价 20% ≠ 切日日期**）。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**。**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**。**params 相对门槛 ≠ 申报带百分数 ≠ 切日日期 ≠ 过户费率 ≠ 证管费 ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**。禁止互读、禁止把门槛改写成申报带百分数、切日日期、过户费率、证管费、发行价 20%/30% 或开盘价 30%/60%。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dy0_primary_demo`**：**写死冻结** **`invent_approval_ipo_day_as_nolimit_no_band`**（单一主报，单挂写死）。**禁止**与半泄露键 **`invent_asof_leak_approval_ipo_band`** / **`invent_only_continuous_band_on_approval_ipo`** 双挂争主表；**禁止只测连续窗当半泄露主报**；**禁止**跑后因分桶显著性改口主报。DY1 仅核对日把「注册制首日已经无板」铺到核准制主板首日，或只测连续竞价 64%–144%、不看集合 80%–120%，只作半泄露对照，**不得升格与 dy0 并列主报**，也不得把 `invent_asof_leak_approval_ipo_band` 或 `invent_only_continuous_band_on_approval_ipo` 写进 `dy0`。`invent_only_call_band_ignore_continuous` / `copy_registration_nolimit_onto_approval_ipo` / `vs_G_nolimit_board_default` / `vs_CI_ipo_fill` / `vs_J_nolimit_halt` / `vs_DU_cb_ipo_halt` / `vs_X_st_limit_pit` / `vs_W_ex_right_limit` / `vs_AY_tick` / `vs_DX_sse_fund_close` / `vs_O_block_channel` / `vs_CK_block_fill` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_Y_call_vol_in_bar` / `missing_listing_regime_or_issue_px_or_official_rule_not_skip` **只作诊断桶，不得升格主报**。草稿页已列的其他诊断桶同样不升格。DY1 / 诊断桶 **不升格**。**禁把以下升格进 dy0**：G无板日默认板 / CI可成交性 / J·DU临停 / DX沪市基金收盘 / Y集合竞价量 / D成交时点 / R假T+0 / V印花 / T证管费 / U过户 / Q·CQ / 注册制无板倒铺 / 只测连续窗半泄露。这些只作对照/旁路，**不得升格进 `dy0`，不得另挂主报**。**零改 DX**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-G**；**不重开假设-CI**；**不重开假设-J**；**不重开假设-DU**；**不重开假设-Y**；**不重开假设-D**；**不重开假设-DX**；**不重开假设-R**。**不抢实验 R**。**双字母 DY ≠ 单字母假设-D / 假设-Y**。**双字母 DY ≠ 单字母 D/Y**。

3. **核准制主板首日申报价格上下限诚实锚六键升格写死（不可再写「建议」）**：`params.approval_ipo_band_honest=pit_call_80_120_cont_64_144_pre_20230410_not_registration_nolimit`；`params.approval_ipo_band_scope=approval_mainboard_ipo_day1_order_price_band`；`params.approval_ipo_band_over_policy=skip_if_listing_regime_or_issue_px_or_official_rule_missing`；`params.asof_check_date=2026-10-09`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺上市制度 / 发行价 / 官方规则 → skip；核准制主板首日集合竞价申报带 = 发行价 80%–120%，连续竞价申报带 = 发行价 64%–144%；注册制无板自 2023-04-10 落地，禁止倒铺。G 无板日默认板 ≠ 本页；CI 可成交性 ≠ 本页。禁止跑后改锚，或用无板 / 核对日规则铺满 / 注册制无板倒铺 / 只测连续窗 / 缺上市制度/发行价/官方规则仍硬填 / 把 G/CI/J/DU/DX/Y/D/R/V/T/U/Q/CQ 升格进 dy0 冒充诚实 PIT。**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**。**禁把 params.G 的 0.01 读成过户 0.01‰ 或 80%/120%/64%/144% 或发行价 20%/30%**。**禁把 params.Y 的 0.02 读成证管费 0.02‰ 或发行价 20% 或实验字母 DY 或切日日期**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**零改 DX**。**不抢实验 R**。**不重开假设-G**；**不重开假设-CI**。

**硬分列保住**：DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D；**双字母 DY ≠ 单字母假设-D / 假设-Y**；**双字母 DY ≠ 单字母 D/Y**；**params.Y / params.G / params.N ≠ 实验字母 DY ≠ 单字母 D/Y**；**尤重 params.Y ≠ 实验字母 DY**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 80%/120%/64%/144% ≠ 发行价 20%/30%**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价 20% ≠ 切日日期**；**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**；**params 相对门槛 ≠ 申报带百分数 ≠ 切日日期 ≠ 过户费率 ≠ 证管费 ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**；**核准制主板首日申报价格上下限 ≠ G无板日误套板块默认板 ≠ CI新股首日可成交性 ≠ J/DU临停 ≠ Y集合竞价量计入日线 ≠ D成交时点 ≠ 注册制前5日无板（禁止倒铺）≠ R股票ETF假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ DX沪市基金收盘切日 ≠ Q·CQ**；不抢 A；不抢实验 R；不改已齐/已冻 DA～DX 及 A–DQ 正文；**零改 DX**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-G**；**不重开假设-CI**；**不重开假设-J**；**不重开假设-DU**；**不重开假设-Y**；**不重开假设-D**；**不重开假设-DX**；**不重开假设-R**；**禁把 G无板日默认板 / CI可成交性 / J·DU临停 / DX沪市基金收盘 / Y集合竞价量 / D成交时点 / R假T+0 / V印花 / T证管费 / U过户 / Q·CQ / 注册制无板倒铺 / 只测连续窗半泄露 合成/混读升格进 dy0**。handoff 保持：`nolimit_board_handoff=g_page`；`ipo_fill_handoff=ci_page`；`nolimit_halt_handoff=j_page`；`cb_ipo_halt_handoff=du_page`；`st_limit_pit_handoff=x_page`；`ex_right_limit_handoff=w_page`；`tick_handoff=ay_page`；`sse_fund_close_handoff=dx_page`；`block_channel_handoff=o_page`；`block_fill_handoff=ck_page`；`call_vol_bar_handoff=y_page`；`etf_t0_handoff=r_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；`merge_with_*=False`。

**状态**：**预检有条件通过·三条已冻·待复检**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DY纸面齐**；本页不开回测/真数/开户/实盘。

## 变更
| 日期 | 变更 |
|------|------|
| 2026-12-05 | 风控预检补丁·冻结三条写死——依据 `预检-假设DY-20261110.md`（SHA256=`d28c6a91a20822edeabd814f146a40bf88ae6f819491e49d747a06754078718a`；结论=有条件通过；tip基=`e5b3e812` / `e5b3e81221a7e17eb3c95d7c8bce2aaf7645bf03`；分支起点 HEAD=`d2bbca50` / `d2bbca503a0a5edd5e3b14204855d1980bdd0651`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖申报带误套截 ΔApprovalIpoBand / 净差异 / DY1−DY2；**params.Y/G/N ≠ 实验字母 DY ≠ 单字母 D/Y**；**尤重 params.Y ≠ 实验字母 DY**；**勿把 params.Y 读成实验字母 DY 或假设-Y 或假设-V 或假设-T 或假设-U 或假设-G 或假设-D，亦勿把 params.G 读成假设-G 或假设-U，亦勿把单字母假设-D / 假设-Y 读成双字母 DY**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 80%/120%/64%/144% ≠ 发行价 20%/30% ≠ 开盘价 30%/60%（量纲与语义不同）**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 发行价 20% ≠ 实验字母 DY ≠ 切日日期**；**禁把占位读成发行价20%/30%、开盘价30%/60%、过户0.01‰、证管费0.02‰、申报带百分数（80%/120%/64%/144%）、切日日期**；**params 相对门槛 ≠ 申报带百分数 ≠ 切日日期 ≠ 过户费率 ≠ 证管费 ≠ 发行价 20%/30% ≠ 开盘价 30%/60%**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成申报带百分数/切日日期/过户费率/证管费/发行价20%/30%/开盘价30%/60%）；② `params.dy0_primary_demo=invent_approval_ipo_day_as_nolimit_no_band`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_approval_ipo_band` / `invent_only_continuous_band_on_approval_ipo` 双挂；禁止只测连续窗当半泄露主报；DY1 不升格；诊断桶 `invent_only_call_band_ignore_continuous` / `copy_registration_nolimit_onto_approval_ipo` / `vs_G_nolimit_board_default` / `vs_CI_ipo_fill` / `vs_J_nolimit_halt` / `vs_DU_cb_ipo_halt` / `vs_X_st_limit_pit` / `vs_W_ex_right_limit` / `vs_AY_tick` / `vs_DX_sse_fund_close` / `vs_O_block_channel` / `vs_CK_block_fill` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_Y_call_vol_in_bar` / `missing_listing_regime_or_issue_px_or_official_rule_not_skip` 不升格；**禁把 G无板日默认板 / CI可成交性 / J·DU临停 / DX沪市基金收盘 / Y集合竞价量 / D成交时点 / R假T+0 / V印花 / T证管费 / U过户 / Q·CQ / 注册制无板倒铺 / 只测连续窗半泄露 合成/混读升格进 dy0**，只作对照/旁路，不得升格进 dy0 或另挂主报；**零改 DX**；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-G；不重开假设-CI；不重开假设-J；不重开假设-DU；不重开假设-Y；不重开假设-D；不重开假设-DX；不重开假设-R；不抢实验 R；**双字母 DY ≠ 单字母假设-D / 假设-Y**）；③ 锚六键写死 `approval_ipo_band_honest=pit_call_80_120_cont_64_144_pre_20230410_not_registration_nolimit` / `approval_ipo_band_scope=approval_mainboard_ipo_day1_order_price_band` / `approval_ipo_band_over_policy=skip_if_listing_regime_or_issue_px_or_official_rule_missing` / `asof_check_date=2026-10-09` / `fill_time=next_open` / `fail_policy=skip`（缺上市制度/发行价/官方规则 → skip；核准制主板首日集合申报带=发行价 80%–120%、连续=发行价 64%–144%；注册制无板自 2023-04-10 落地，禁止倒铺；G/CI ≠ 本页）。handoff 保持 `nolimit_board_handoff=g_page` / `ipo_fill_handoff=ci_page` / `nolimit_halt_handoff=j_page` / `cb_ipo_halt_handoff=du_page` / `st_limit_pit_handoff=x_page` / `ex_right_limit_handoff=w_page` / `tick_handoff=ay_page` / `sse_fund_close_handoff=dx_page` / `block_channel_handoff=o_page` / `block_fill_handoff=ck_page` / `call_vol_bar_handoff=y_page` / `etf_t0_handoff=r_page` / `stamp_handoff=v_page` / `csrc_fee_handoff=t_page` / `transfer_fee_handoff=u_page`；`merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DY纸面齐**；不改已齐/已冻 DA～DX 及 A–DQ；**零改 DX**；不改 #110–#133；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-R；不重开假设-G；不重开假设-CI；不重开假设-J；不重开假设-Y；不重开假设-D；不重开假设-DX；不抢实验 R；不预留 #135；不开回测/真数/开户/实盘。基于 tip=`e5b3e812`。 |
| 2026-12-05 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。核准制主板新股首日申报价格上下限误套（成交规则）；`dy0_primary_demo` 建议 `invent_approval_ipo_day_as_nolimit_no_band`，单一主报，单挂，禁与 `invent_asof_leak_approval_ipo_band` / `invent_only_continuous_band_on_approval_ipo` 双挂，DY1 不升格；诊断桶 `invent_only_call_band_ignore_continuous` / `copy_registration_nolimit_onto_approval_ipo` / `vs_G_nolimit_board_default` / `vs_CI_ipo_fill` / `vs_J_nolimit_halt` / `vs_DU_cb_ipo_halt` / `vs_X_st_limit_pit` / `vs_W_ex_right_limit` / `vs_AY_tick` / `vs_DX_sse_fund_close` / `vs_O_block_channel` / `vs_CK_block_fill` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_Y_call_vol_in_bar` / `missing_listing_regime_or_issue_px_or_official_rule_not_skip` 不升格；**尤重实验 R 不抢，禁把 vs_R_etf_t0 升格进 dy0**；**尤重不重开假设-V / 假设-T / 假设-U，禁把 vs_V_stamp / vs_T_csrc / vs_U_transfer 升格进 dy0**；**尤重 G=无板日误套板块默认板 ≠ 本页核准制首日申报价格上下限，禁把 vs_G_nolimit_board_default 升格**；**尤重 CI 可成交性 ≠ 本页申报价格闸门，禁把 vs_CI_ipo_fill 升格**；**尤重 J/DU 临停 ≠ 本页申报带，禁把 vs_J_nolimit_halt / vs_DU_cb_ipo_halt 升格**；**尤重双字母 DY ≠ 单字母假设-D / 假设-Y，禁把 vs_Y_call_vol_in_bar 升格**；**尤重 params.Y ≠ 实验字母 DY**；**尤重 params.Y/G/N ≠ 实验字母 DY / 假设-Y / 假设-G**；**尤重禁 copy_registration_nolimit_onto_approval_ipo / invent_only_call_band_ignore_continuous / invent_only_continuous_band_on_approval_ipo 升格进主报或双挂**；**禁止只测连续窗当半泄露主报**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Y / 假设-G / 假设-D**；**禁把占位读成 80%/120%/64%/144%、切日日期、过户‰**；**禁把 DX/DW/DV/DU/DT/DS/DR 升格进 dy0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DY ≠ 单字母 D/Y**；锚建议·待冻、未冻：`approval_ipo_band_honest=pit_call_80_120_cont_64_144_pre_20230410_not_registration_nolimit` / scope=`approval_mainboard_ipo_day1_order_price_band` / over_policy=`skip_if_listing_regime_or_issue_px_or_official_rule_missing` / `asof_check_date=2026-10-09` / `fill_time=next_open` / `fail_policy=skip`；口径：缺上市制度/发行价/官方规则则 skip；核准制主板首日集合申报带=发行价 80%–120%、连续=发行价 64%–144%；注册制无板自 2023-04-10 落地，禁止倒铺（**草稿方向，尚未冻，不要写成已冻**）；handoff：`nolimit_board_handoff=g_page`，`ipo_fill_handoff=ci_page`，`nolimit_halt_handoff=j_page`，`cb_ipo_halt_handoff=du_page`，`st_limit_pit_handoff=x_page`，`ex_right_limit_handoff=w_page`，`tick_handoff=ay_page`，`sse_fund_close_handoff=dx_page`，`block_channel_handoff=o_page`，`block_fill_handoff=ck_page`，`call_vol_bar_handoff=y_page`，`etf_t0_handoff=r_page`，`stamp_handoff=v_page`，`csrc_fee_handoff=t_page`，`transfer_fee_handoff=u_page`；`merge_with_DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/Y/A/D=False`；**DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D**；**双字母 DY ≠ 单字母 D/Y**；**未标纸面齐**；**不写 A/D–DY纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–DX；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–DX；**零改 DX**；不改 #110–#133；不重开假设-R；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-G；不重开假设-CI；不重开假设-J；不重开假设-DU；不重开假设-Y；不重开假设-D；不重开假设-DX；不写下一字母；不预留 #135；不开真数/回测/开户/实盘。基 tip=`845521f`（A/D–DX纸面齐已合，全长 `845521f055106b1ea90db02793ab1521a362e15b`；不改该 tip 上的 #110–#133，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
