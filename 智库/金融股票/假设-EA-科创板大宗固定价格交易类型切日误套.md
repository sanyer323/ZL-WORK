# 假设-EA · 科创板大宗固定价格交易类型切日误套（成交规则）

更新：2026-12-07  
来源：总管线 / 基 tip=`934e3cf` / 全长 `934e3cf4c065bf65fa192127131ed2659eebd762`（A/D–DZ纸面齐已合）；**不改已冻 A–DQ / DA–DZ**；**零改 DZ**；**不改假设-DZ 正文/预检/复检**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-DT / 假设-DU / 假设-DV / 假设-DW / 假设-DX / 假设-DY / 假设-DZ / 假设-S / 假设-AX / 假设-AY / 假设-AW / 假设-T / 假设-U / 假设-V / 假设-W / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-E / 假设-F / 假设-J / 假设-G / 假设-CI / 假设-CK / 假设-Y / 假设-A / 假设-D / 假设-X / 假设-Z 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ）；**不重开假设-R**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-O**；**不重开假设-M**；**不重开假设-CH**；**不重开假设-CK**；**不重开假设-DR**；**不重开假设-DZ**；**不重开假设-DX**；**不重开假设-DY**；**不重开假设-E**；**不重开假设-A**；**不重开假设-D**；**不重开假设-W**；**不重开假设-X**；**不重开假设-AY**）后写下一草稿 EA；清单 #135=DZ，本页占用 **#136=EA**；选题是回测把 **科创板大宗固定价格交易类型**按切日套错（诚实方向：该类型在上证发〔2019〕23 号下**不适用**，自 **2026-07** 技术实施指南起才增加；日期与假设-O 分桶参 `star_fixed_price_block_start=2026-07-06` **对齐复用**，**禁改语义进 `ea0`、禁并进 `o0`**；缺板块标记 / 官方规则则 skip；禁止「永远有 / 永远没有」半泄露双挂；禁止与 O0 量价 / 三通道合成一句）；假设-O 只收日量含大宗与三通道假流动性，假设-M 只收竞价盘后固定价格通道，假设-CH 只收盘后固定价格可成交性，假设-CK 只收协议大宗假全额可成，假设-DR 只收可转债盘后定价，假设-DZ 只收创业板协议大宗确认钟，假设-DX 只收沪市基金收盘产生方式切日，假设-DY 只收核准制主板新股首日申报带，假设-R 只收股票 ETF 假 T+0，假设-V 只收股票印花税切日，假设-T 只收股票证管费切日，假设-U 只收股票过户切日，假设-E 只收整手与科创板 200 股，假设-A 只收涨停可成交性；**新建实验 EA**；不写下一字母；不预留 #137  
状态：**草稿·待入库预检**（结论栏空；三条尚未冻；禁止把「科创板大宗固定价格类型永远有」或「永远没有」当诚实锚；禁止把竞价盘后固定价格当成大宗固定价格类型；禁止与 O0 量价 / 三通道合成一句；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–DZ**；**零改 DZ**；**不改 #110–#135**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–EA纸面齐**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 EA（#136）。一句话误开：回测把科创板大宗固定价格类型写成 **切日之前就已经有**，或写成 **切日之后仍然没有**，或拿核对日「已经增加」倒灌全历史，或把竞价侧的盘后固定价格（M/CH）当成这一种大宗类型，或与 O日量含大宗·三通道假流动性 / CK协议大宗假全额可成 / DR可转债盘后定价 / DZ创业板确认钟 / DX沪市基金收盘切日 / DY核准制首日申报带 / R股票ETF假T+0 / V股票印花 / T股票证管费 / U股票过户 / E整手与科创板200股 / A涨停可成交 混读，或缺板块标记 / 官方规则仍不 skip，系统性改写这笔申报**当时有没有「大宗固定价格」这一种类型**。**禁把 O/M/CH/CK/DR/DZ/DX/DY/R/V/T/U/E/A 混读升格进 `ea0`**。**禁把 `invent_star_fixed_price_block_type_always_off_post_cut` 升格进主报**。**禁把 `invent_asof_leak_star_fixed_price_block_on` 与主报双挂**。**禁与 O0 量价 / 三通道合成一句进 `ea0`**。**禁改 `star_fixed_price_block_start` 语义进 `ea0`，禁并进 `o0`**。

> **字母消歧（硬）**：本页**实验字母 EA** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；占位 0.02；**三条尚未冻**；**params.Y ≠ 实验字母 EA**；**尤重：`params.Y/G/N` ≠ 实验字母 EA / 单字母 E/A**；**params 字母 ≠ 假设-V / 假设-T / 假设-U**；**勿把 `params.Y` 读成实验字母 EA，亦勿读成单字母假设-E，亦勿读成单字母假设-A，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U**；**尤重：`params.Y` 的 0.02 ≠ 实验字母 EA ≠ 单字母 E/A ≠ 切日日期 ≠ 类型开关 ≠ 过户‰ ≠ 证管费 0.02‰**）≠ **`params.G`**（同族门槛，占位 0.01；**params.G ≠ 实验字母 EA**；**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 切日日期 ≠ 类型开关**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是「类型开」，不是「类型关」，不是 2026-07，不是 2026-07-06，也不是过户费率）≠ **`params.N`**（失败/废单率差门槛；占位 0.05；**params.N ≠ 实验字母 EA**；**params.N ≠ 单字母 E/A**）≠ **`params.Y2`**（占位 0.015；不是切日，不是类型开关）≠ **单字母实验 E**（整手与科创板 200 股；**双字母 EA ≠ 单字母假设-E；严禁复用假设-E**）≠ **单字母实验 A**（涨停可成交性；**双字母 EA ≠ 单字母假设-A；严禁复用假设-A**；**不抢 A 真数队列**）≠ **单字母实验 V**（股票印花税切日；**双字母 EA ≠ 单字母假设-V；严禁复用假设-V**；**不重开假设-V**）≠ **单字母实验 U**（股票过户费切日；**双字母 EA ≠ 单字母假设-U；严禁复用假设-U**；**不重开假设-U**）≠ **单字母实验 T**（股票证管费切日；**双字母 EA ≠ 单字母假设-T；严禁复用假设-T**；**不重开假设-T**）≠ **单字母实验 R**（股票 ETF 假 T+0；**双字母 EA ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `ea0`**）≠ **双字母 DZ**（创业板协议大宗确认时点切日；**零改 DZ**；**EA≠DZ**）≠ **双字母 DY**（核准制主板新股首日申报价格上下限；**EA≠DY**）≠ **双字母 DX**（沪市基金收盘产生方式切日；**EA≠DX**）≠ **双字母 O**（大宗日量 / 三通道假流动性；**O ≠ 本页类型可用性切日**）≠ **单字母 M**（竞价盘后固定价格通道；**盘后固定价格 ≠ 大宗固定价格类型**）≠ **双字母 CH**（盘后固定价格可成交性；**竞价盘后能不能打满 ≠ 类型开关**）≠ **双字母 CK**（协议大宗可成交性；**假全额可成 ≠ 类型开关**）≠ **双字母 DR**（可转债盘后定价；**转债盘后定价 ≠ 本页**）≠ **DQ / DP / DO / DN / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA**（费用旁路；不并进 `ea0`）≠ **S**（股票经手费切日）≠ **AX**（基金经手费）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债回转/涨跌幅/收盘）≠ **CL / CR / CQ**（可成交性旁路）≠ **F / J / W / AW / AY / X / G / CI / Y**（取整、临停、除权、收盘集合失败回落、价位、ST 板幅、无板日默认板、新股首日可成交、集合竞价量）≠ **DW / DV / DU / DT / DS**（行权过户、现金选择权、转债首日临停、整手价位、转股印花）≠ **单字母实验 D**（成交时点与停牌）≠ **单字母实验 Z**（融资保证金比例误铺）。**EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z**。**双字母 EA ≠ 单字母 E/A**。**双字母 EA ≠ 单字母假设-E / 假设-A**。**params.Y/G/N ≠ 实验字母 EA ≠ 单字母 E/A**。**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**。**params 字母 ≠ 假设-V / 假设-T / 假设-U**。**禁把占位读成切日日期、类型开关、过户‰**。**params 相对门槛 ≠ 切日日期 ≠ 类型开关 ≠ 过户‰**。**科创板大宗固定价格类型切日 ≠ O日量含大宗/三通道假流动性 ≠ M/CH竞价盘后固定价格 ≠ CK假全额可成 ≠ DR转债盘后定价 ≠ DZ创业板确认钟 ≠ DX沪市基金收盘切日 ≠ DY核准制首日申报带 ≠ R股票ETF假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ E整手与科创板200股 ≠ A涨停可成交**。**尤重：实验 R 不抢；禁把 `vs_R_etf_t0` 升格进 `ea0`**。**尤重：不重开假设-V / 假设-T / 假设-U；禁把 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 升格进 `ea0`**。**尤重：O = 日量含大宗 / 三通道假流动性 ≠ 本页只钉科创大宗固定价格类型可用性切日；参数 `star_fixed_price_block_start` 可复用，禁改语义进 `ea0`、禁并进 `o0`；禁把 `vs_O_block_liquidity` 升格进 `ea0`；禁与 O0 量价 / 三通道合成一句进 `ea0`**。**尤重：M/CH 竞价盘后固定价格 ≠ 大宗固定价格类型；禁把 `vs_M_aft_channel` / `vs_CH_aft_fill` 升格进 `ea0`**。**尤重：CK 假全额 ≠ 类型开关；禁把 `vs_CK_block_fill` 升格进 `ea0`**。**尤重：DR 转债盘后定价 ≠ 本页；禁把 `vs_DR_aft_pricing` 升格进 `ea0`**。**尤重：DZ 创业板确认钟 ≠ 本页；禁把 `vs_DZ_chinext_confirm` 升格进 `ea0`；零改 DZ**。**尤重：双字母 EA ≠ 单字母假设-E / 假设-A；禁把 `vs_E_lot_size` / `vs_A_limit_fill` 升格进 `ea0`**。**尤重：DX/DY/R/V/T/U/E/A 旁路诊断禁升格进 `ea0`**。**零改 DZ**。

### 专节 · 双字母 EA ≠ 单字母假设-E / 假设-A；且 ≠ 假设-O / 假设-M / 假设-CH / 假设-CK / 假设-DR / 假设-DZ / 假设-R / 假设-V / 假设-T / 假设-U（硬）

| 维度 | 对照页 | 本页假设-EA（双字母） |
|------|--------|----------------------|
| 题面 O | **大宗量价并进竞价 / 三条盘后通道混用**（日成交量含大宗结束后计入的那截；按大宗价回放竞价；盘后固定价格、深市盘后定价大宗、沪市大宗固定价格申报合成一句；假设-O）。O 自己的分桶参 `star_fixed_price_block_start=2026-07-06` 只用来对齐「科创板大宗固定价格类型从哪天起算」 | **O = 量、价、三通道假流动性**。本页只问科创板**大宗固定价格这一种类型**在切日之前有没有。门槛 30 万股 / 200 万元、日量何时计入、三条通道怎么拆，都留在 O。日期对齐可以复用那颗参，**语义不改、不写进 `ea0`、不并进 `o0`**。两句禁止合成。**EA≠O**；**不重开假设-O**；**不改 O**；**尤重：禁把 `vs_O_block_liquidity` 升格进 `ea0`**；**禁与 O0 量价 / 三通道合成一句进 `ea0`**；`block_liquidity_handoff=o_page` |
| 题面 M | **盘后固定价格通道误套全历史**（收盘后再按收盘价撮合；假设-M） | 科创板**开市起**就把盘后固定价格列为交易方式。那是竞价侧的盘后通道，不是大宗申报里的固定价格类型。同一天 2026-07-06 可以既扩盘后、又给科创增加大宗固定价格类型，两件事禁止合成。**EA≠M**；**不重开假设-M**；**不改 M**；**尤重：禁把 `vs_M_aft_channel` 升格进 `ea0`**；`aft_channel_handoff=m_page` |
| 题面 CH | **盘后固定价格可成交性误开**（默认盘后单必能按收盘价打满；假设-CH） | **CH = 价已经走在竞价盘后通道里之后，单子能不能打满**。本页 = 大宗申报里**有没有这一种类型**。类型开了也不等于盘后能打满。**EA≠CH**；**不重开假设-CH**；**不改 CH**；**尤重：禁把 `vs_CH_aft_fill` 升格进 `ea0`**；`aft_fill_handoff=ch_page` |
| 题面 CK | **协议大宗可成交性误开**（默认协议 / 成交申报大宗必能按目标价或谈妥价全额成交；假设-CK） | **CK = 类型已经可用之后，单子能不能打满**。假全额不是类型开关。**EA≠CK**；**不重开假设-CK**；**不改 CK**；**尤重：禁把 `vs_CK_block_fill` 升格进 `ea0`**；`block_fill_handoff=ck_page` |
| 题面 DR | **可转债盘后定价误套股票盘后固定价格**（假设-DR） | 转债盘后定价通道 ≠ 科创板大宗固定价格类型。**EA≠DR**；**不重开假设-DR**；**不改 DR**；**尤重：禁把 `vs_DR_aft_pricing` 升格进 `ea0`**；`aft_pricing_handoff=dr_page` |
| 题面 DZ | **创业板协议大宗确认时点切日**（假设-DZ 已纸面齐） | 创业板协议大宗的确认钟，和科创板大宗固定价格类型从哪天起才有，是两件事。同日落地也不合成一句。**零改 DZ**。**EA≠DZ**；**不重开假设-DZ**；**不改 DZ 正文/预检/复检**；**尤重：禁把 `vs_DZ_chinext_confirm` 升格进 `ea0`**；`chinext_confirm_handoff=dz_page` |
| 题面 半泄露 | 核对日 2026-10-23 已经在技术实施指南之后，科创板大宗固定价格类型已经增加 | `invent_asof_leak_star_fixed_price_block_on` 只作半泄露对照。**禁与 `ea0` 双挂**；不得升格并列主报。**禁止「永远有 / 永远没有」半泄露双挂** |
| 题面 永远没有 | 把「2019 号下不适用」铺到 2026-07 技术实施指南之后，写成这个类型永远没有 | 诊断桶 `invent_star_fixed_price_block_type_always_off_post_cut` 只标记切日之后仍当成没有。**禁升格进 `ea0`**，不得与主报双挂 |
| 题面 DY | **核准制主板新股首日申报价格上下限**（假设-DY） | 首日申报带 ≠ 大宗固定价格类型切日。**EA≠DY**；**不重开假设-DY**；**不改 DY**；**尤重：禁把 `vs_DY_approval_ipo_band` 升格进 `ea0`**；`approval_ipo_band_handoff=dy_page` |
| 题面 DX | **沪市基金收盘产生方式切日**（假设-DX） | 基金收盘怎么产生 ≠ 科创大宗固定价格类型。同日 2026-07-06 不是同一件事。**EA≠DX**；**不重开假设-DX**；**不改 DX**；**尤重：禁把 `vs_DX_sse_fund_close` 升格进 `ea0`**；`sse_fund_close_handoff=dx_page` |
| 题面 R | **股票 ETF 假 T+0**（假设-R） | **实验 R 不抢**。ETF 能不能当日回转，和科创大宗有没有固定价格这一种类型，是两件事。**EA≠R**；**严禁复用假设-R**；**不重开假设-R**；**不改 R**；**尤重：禁把 `vs_R_etf_t0` 升格进 `ea0`**；`etf_t0_handoff=r_page` |
| 题面 V | **股票印花税切日**（假设-V） | **不重开假设-V**。印花切日 ≠ 类型开关。占位不是印花税率。**EA≠V**；**params 字母 ≠ 假设-V**；**不改 V**；**尤重：禁把 `vs_V_stamp` 升格进 `ea0`**；`stamp_handoff=v_page` |
| 题面 T | **股票证管费切日**（假设-T） | **不重开假设-T**。`params.Y` 的 0.02 不是证管费 0.02‰，也不是实验字母 EA。**EA≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：禁把 `vs_T_csrc` 升格进 `ea0`**；`csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日**（假设-U） | **不重开假设-U**。`params.G` 的 0.01 不是过户 0.01‰，也不是类型开关。**EA≠U**；**params 字母 ≠ 假设-U**；**不改 U**；**尤重：禁把 `vs_U_transfer` 升格进 `ea0`**；`transfer_fee_handoff=u_page` |
| 题面 E | **整手与科创板 200 股**（假设-E） | 科创板买入至少 200 股，是数量闸门。本页问的是大宗固定价格**类型有没有**。**双字母 EA ≠ 单字母假设-E**；**严禁复用假设-E**；**EA≠E**；**尤重：`params.Y/G/N` ≠ 单字母 E**；**不重开假设-E**；**不改 E**；**尤重：禁把 `vs_E_lot_size` 升格进 `ea0`**；`lot_size_handoff=e_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（假设-A） | 板上能不能成交，不是大宗类型开关。**双字母 EA ≠ 单字母假设-A**；**严禁复用假设-A**；**EA≠A**；**尤重：`params.Y/G/N` ≠ 单字母 A**；**不抢 A 真数队列**；**不重开假设-A**；**不改 A**；**尤重：禁把 `vs_A_limit_fill` 升格进 `ea0`**；`limit_fill_handoff=a_page` |
| 题面 DW / DV / DU / DT / DS / DQ–DA / S / AX / AC / Q / CL / CR / CQ / F / J / W / AW / AY / X / G / CI / Y / D / Z | 费用、整手价位、可成交性、临停、开收时点、保证金比例等旁路 | 全部不并进 `ea0`。**EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z**。不改这些页 |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_star_fixed_price_block_type_always_on_pre_cut`（**建议**单一主报，单挂；**三条尚未冻**；禁与半泄露键 `invent_asof_leak_star_fixed_price_block_on` 双挂；EA1 不升格；诊断桶不升格） |
| 文档 | 清单实验 DZ 及上表各页（**只读；禁止改写**） | `假设-EA-科创板大宗固定价格交易类型切日误套.md`（新建） |
| 预检键 | 实验字母 DZ / DY / … / E / A / O / M / V / T / U / R | 实验字母 **EA** / `ea0_primary_demo`；**不得**占用或改写上述预检键；**params.Y/G/N ≠ 实验字母 EA** |

**禁止**：把 EA 写成「O / M / CH / CK / DZ / R / E / A 的续篇」；把「核对日科创板已经增加大宗固定价格类型 / 科创板开市起就有盘后固定价格 / O 的分桶参已经写了 2026-07-06」写成「本页类型切日已诚实」；把实验字母 EA 与单字母 E/A 或 params.Y/G/N 混读；**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U**；**禁把占位 `0.02/0.01/0.05/0.015` 读成切日日期、类型开关、过户‰**；**实验 R 不抢**；**不重开假设-V / 假设-T / 假设-U**；**O 日量含大宗 / 三通道 ≠ 本页类型可用性**；**`star_fixed_price_block_start` 只对齐复用，禁改语义进 `ea0`、禁并进 `o0`**；**M/CH 竞价盘后固定价格 ≠ 大宗固定价格类型**；**CK 假全额 ≠ 类型开关**；**DR 转债盘后定价 ≠ 本页**；**DZ 创业板确认钟 ≠ 本页**；**零改 DZ**；**禁「永远有 / 永远没有」半泄露双挂**；**禁与 O0 量价 / 三通道合成一句进 `ea0`**；**禁把 O/M/CH/CK/DR/DZ/DX/DY/R/V/T/U/E/A 的诊断升格进 `ea0`**；把 `invent_asof_leak_star_fixed_price_block_on` 与主报双挂；缺板块标记 / 官方规则仍硬填。本页主键只用 `ea0` / `ea1` / `ea2` 与 `star_fixed_price_block_type_*`。不写下一字母。不预留 #137。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–DZ；勿再只改清单）。当前草稿阶段**禁止标纸面齐**，**不写 A/D–EA纸面齐**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测把 **2026-07 技术实施指南之前的科创板大宗**写成 **已经有固定价格这一种类型**，或把指南之后仍写成没有，或与 O 的日量含大宗和三通道、M/CH 的竞价盘后固定价格、CK 的假全额可成、DR 的转债盘后定价、DZ 的创业板确认钟、DX 的基金收盘切日、DY 的申报带、R 的假 T+0、V/T/U 的费用切日、E 的整手、A 的板上可成交混读，或缺板块标记 / 官方规则仍不 skip，相对「缺字段则 skip；上证发〔2019〕23 号下科创板大宗不适用固定价格申报，自 2026-07 技术实施指南起才增加该类型；日期与 O 的 `star_fixed_price_block_start=2026-07-06` 对齐复用，不改语义、不并进 o0；不与 O0 量价 / 三通道合成一句」的诚实组，会**系统性改写这笔申报当时有没有大宗固定价格这一种类型**——指南之前不该有的类型被写成可报，或指南之后已经增加的类型被写成仍然没有。方向是相对诚实锚偏误。

核对日方向（建议·待冻；**三条尚未冻**；禁止把占位读成切日日期、类型开关、过户‰）：`事实与坑` 2026-10-23 写明，2019 通知同时写科创板大宗**不适用**固定价格申报；2026-07 技术实施指南才写「增加科创板股票大宗交易固定价格交易类型」。不要把「科创板永远没有固定价格大宗」铺到指南之后，也不要把「永远有」铺到指南之前。科创板开市起就有的，是**盘后固定价格**这一种竞价交易方式，那一页在假设-M / 假设-CH，不在这里。假设-O 用 `star_fixed_price_block_start=2026-07-06` 给自己的量价分桶对齐同一天，本页只复用这个对齐，**不改那颗参的语义，不把它写进 `ea0`，不并进 `o0`**。日量含不含大宗、三通道怎么拆，留在假设-O。盘后通道留在 M，盘后能不能打满留在 CH，协议大宗能不能打满留在 CK，转债盘后留在 DR，创业板确认钟留在 DZ。缺板块标记或官方规则，整笔 skip。**禁把占位读成切日日期、类型开关、过户‰**。**params 字母 ≠ 假设-V / 假设-T / 假设-U**。**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**。

证伪方向：若天真组 / 半泄露组相对诚实组的类型误套截在标定噪声带内可忽略，且「切日前误当已有 / 切日后误当仍无 / 核对日泄露 / vs O·M·CH·CK·DR·DZ·DX·DY·R·V·T·U·E·A」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 建议键（拉数前待预检；本页不开跑；Y/G/N/Y2 · ea0 与锚 **三条尚未冻**）

```
# 配置建议键（见 §7；草稿·待入库预检；下列三条都还没冻，不要写成已冻）
# 【消歧】params.Y = 显著性门槛；占位 0.02；**≠ 实验字母 EA ≠ 单字母假设-E / 假设-A**
# 【消歧】尤重：params.Y/G/N ≠ 实验字母 EA / 单字母 E/A
# 【消歧】params 字母 ≠ 假设-V / 假设-T / 假设-U
# 【消歧】尤重：params.Y 的 0.02 ≠ 实验字母 EA ≠ 单字母 E/A ≠ 切日日期 ≠ 类型开关 ≠ 过户‰ ≠ 证管费 0.02‰
# 【消歧】尤重：params.G 的 0.01 ≠ 过户 0.01‰ ≠ 切日日期 ≠ 类型开关（无量纲相对门槛 ≠ 过户费率 ≠ 2026-07 ≠ 2026-07-06 ≠ 开/关）
# 【消歧】params.N = 失败/废单率差门槛；占位 0.05；**≠ 实验字母 EA ≠ 单字母 E/A**
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成切日日期、类型开关、过户‰
# 【消歧】params 相对门槛 ≠ 切日日期 ≠ 类型开关 ≠ 过户‰
# 【消歧】三条尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值
# params.Y2                               占位 0.015（尚未冻；不是切日，不是类型开关，不是 2026-07-06）
# params.Y / G / N / Y2                   占位 0.02/0.01/0.05/0.015（相对门槛：类型误套截 ΔStarFixedPriceBlockType / 净差异 / EA1−EA2；**params.Y/G/N ≠ 实验字母 EA ≠ 单字母 E/A**；**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**；**三条尚未冻**）
# params.fill_time                        建议 next_open（尚未冻）
#   这是信号腿的成交时点建议，不是类型开关，也不是切日
#   双字母 EA ≠ 单字母假设-E / 假设-A
# params.asof_check_date                  建议 2026-10-23（尚未冻；这是核对日，不是切日，也不是占位，也不是 2026-07-06）
# params.px_basis                         建议 unadj
# params.fail_policy                      建议 skip（尚未冻）
# params.star_fixed_price_block_type_honest  建议 pit_unavailable_pre_202607_tech_guide_else_available
#   诚实锚方向（建议·待冻，三条尚未冻，不要写成已冻）：
#   缺板块标记或官方规则 → skip
#   科创板大宗固定价格类型：上证发〔2019〕23 号下不适用
#   自 2026-07 技术实施指南起增加该类型
#   日期与 O 分桶参 star_fixed_price_block_start=2026-07-06 对齐复用
#   禁改这颗参的语义进 ea0；禁并进 o0
#   禁止「永远有 / 永远没有」半泄露双挂
#   禁止与 O0 量价 / 三通道合成一句
#   禁止把占位读成切日日期、类型开关或过户‰
#   锚名字里的月份是机制方向，不是 params.Y/G/N/Y2
# params.star_fixed_price_block_type_scope  建议 star_block_fixed_price_type_availability_only
#   只看科创板大宗固定价格类型在不在
#   不是日量含大宗，不是三通道，不是竞价盘后固定价格，不是能不能打满
# params.star_fixed_price_block_type_over_policy  建议 skip_if_board_or_official_rule_missing
#   缺板块标记 / 官方规则则 skip
# params.block_liquidity_handoff          建议 o_page
#   日量含大宗 / 三通道交 O；O ≠ 本页类型切日；不重开假设-O；不改 O
#   star_fixed_price_block_start 只对齐复用，禁改语义进 ea0，禁并进 o0
#   诊断桶 vs_O_block_liquidity 不得升格进 ea0
#   禁与 O0 量价 / 三通道合成一句进 ea0
# params.aft_channel_handoff              建议 m_page
#   竞价盘后固定价格通道交 M；M ≠ 大宗固定价格类型；不重开假设-M；不改 M
#   诊断桶 vs_M_aft_channel 不得升格进 ea0
# params.aft_fill_handoff                 建议 ch_page
#   盘后固定价格可成交性交 CH；不重开假设-CH；不改 CH
#   诊断桶 vs_CH_aft_fill 不得升格进 ea0
# params.block_fill_handoff               建议 ck_page
#   协议大宗可成交性交 CK；CK 假全额 ≠ 类型开关；不重开假设-CK；不改 CK
#   诊断桶 vs_CK_block_fill 不得升格进 ea0
# params.aft_pricing_handoff              建议 dr_page
#   可转债盘后定价交 DR；不重开假设-DR；不改 DR
#   诊断桶 vs_DR_aft_pricing 不得升格进 ea0
# params.chinext_confirm_handoff          建议 dz_page
#   创业板协议大宗确认钟交 DZ；零改 DZ；不重开假设-DZ；不改 DZ 正文/预检/复检
#   诊断桶 vs_DZ_chinext_confirm 不得升格进 ea0
# params.sse_fund_close_handoff           建议 dx_page
#   沪市基金收盘切日交 DX；不重开假设-DX；不改 DX
#   诊断桶 vs_DX_sse_fund_close 不得升格进 ea0
# params.approval_ipo_band_handoff        建议 dy_page
#   核准制首日申报带交 DY；不重开假设-DY；不改 DY
#   诊断桶 vs_DY_approval_ipo_band 不得升格进 ea0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 ea0；不改 R
#   诊断桶 vs_R_etf_t0 不得升格进 ea0
# params.stamp_handoff                    建议 v_page
#   股票印花切日交 V；不重开假设-V；params 字母 ≠ 假设-V；不改 V
#   诊断桶 vs_V_stamp 不得升格进 ea0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；params 字母 ≠ 假设-T；不改 T
#   诊断桶 vs_T_csrc 不得升格进 ea0
# params.transfer_fee_handoff             建议 u_page
#   股票过户切日交 U；不重开假设-U；params 字母 ≠ 假设-U；不改 U
#   诊断桶 vs_U_transfer 不得升格进 ea0
# params.lot_size_handoff                 建议 e_page
#   整手与科创板 200 股交 E；双字母 EA ≠ 单字母假设-E；不重开假设-E；不改 E
#   诊断桶 vs_E_lot_size 不得升格进 ea0
# params.limit_fill_handoff               建议 a_page
#   涨停可成交性交 A；双字母 EA ≠ 单字母假设-A；不抢 A；不重开假设-A；不改 A
#   诊断桶 vs_A_limit_fill 不得升格进 ea0
# params.ea0_primary_demo                 建议 invent_star_fixed_price_block_type_always_on_pre_cut
#   单一主报，单挂；三条尚未冻
#   禁与 invent_asof_leak_star_fixed_price_block_on 双挂
#   EA1 不升格；诊断桶不升格
#   半泄露名只作对照，不得升格进 ea0，不得双挂
#   禁止「永远有 / 永远没有」半泄露双挂
#   禁止与 O0 量价 / 三通道合成一句进 ea0
#   禁改 star_fixed_price_block_start 语义进 ea0；禁并进 o0
#   诊断桶 invent_star_fixed_price_block_type_always_off_post_cut / vs_O_block_liquidity / vs_M_aft_channel / vs_CH_aft_fill / vs_CK_block_fill / vs_DR_aft_pricing / vs_DZ_chinext_confirm / vs_DX_sse_fund_close / vs_DY_approval_ipo_band / vs_R_etf_t0 / vs_V_stamp / vs_T_csrc / vs_U_transfer / vs_E_lot_size / vs_A_limit_fill / missing_board_or_official_rule_not_skip 不得升格进 ea0
#   尤重：实验 R 不抢
#   尤重：不重开假设-V / 假设-T / 假设-U
#   尤重：O/M/CH/CK/DR/DZ 不升格
#   尤重：零改 DZ；禁把 DZ/DX/DY 升格进 ea0
#   尤重：双字母 EA ≠ 单字母 E/A；禁把 E/A 升格进 ea0
# params.ea0_invent_star_fixed_price_block_type_always_on_pre_cut 建议 True
# params.ea1_asof_leak_star_fixed_price_block_on_only 建议 True
#   半泄露对照；EA1 不升格并列主报；不得把 invent_asof_leak_star_fixed_price_block_on 写进 ea0
# params.ea2_pit_unavailable_pre_202607_tech_guide_else_available 建议 True
# params.merge_with_DZ                    建议 False
# params.merge_with_DY                    建议 False
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
# params.merge_with_Z                     建议 False
# params.missing_board_or_official_rule_policy 建议 skip
# params.day_freq_proxy                   建议 star_fixed_price_block_type_sensitivity
# params.universe_rule                    建议 star_fixed_price_block_type_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_ea_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 EA；勿读成单字母 E/A
#   不另挂主报，不预留 #137，不写下一字母
```

### 2.2 三组对照（EA0 / EA1 / EA2）

组名 EA0 / EA1 / EA2 是本页三组，≠ 单字母实验 E（整手与科创板 200 股），亦 ≠ 单字母实验 A（涨停可成交性）。**双字母 EA ≠ 单字母假设-E / 假设-A**。**params.Y/G/N ≠ 实验字母 EA ≠ 单字母 E/A**。**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**。**params 字母 ≠ 假设-V / 假设-T / 假设-U**。三条尚未冻。

| 组 | 角色 | 口径 |
|----|------|------|
| EA0 | 天真 / 切日前的科创板大宗固定价格类型当成已经有 | 按 `ea0_primary_demo` **建议**单一主报 `invent_star_fixed_price_block_type_always_on_pre_cut`（单挂；**尚未冻**）：把 2026-07 技术实施指南之前的科创板大宗写成已经可以报固定价格类型。**禁**与 `invent_asof_leak_star_fixed_price_block_on` 双挂。**禁把永远没有、O/M/CH/CK/DR/DZ、DX/DY、R/V/T/U/E/A 合成进 `ea0`**。**禁与 O0 量价 / 三通道合成一句进 `ea0`**。**禁改 `star_fixed_price_block_start` 语义进 `ea0`** |
| EA1 | 半泄露 | 仅用核对日「科创板大宗固定价格类型已经增加」把这条铺到全历史、铺到 2026-07 技术实施指南之前（`invent_asof_leak_star_fixed_price_block_on`）。**不得升格并列主报**，不得写进 `ea0`，不得双挂。**禁止「永远有 / 永远没有」半泄露双挂** |
| EA2 | 诚实 / 按切日的类型可用性 | `star_fixed_price_block_type_honest=pit_unavailable_pre_202607_tech_guide_else_available`（建议·待冻）：缺板块标记/官方规则则 skip；上证发〔2019〕23 号下不适用，自 2026-07 技术实施指南起才有该类型。日期对齐复用 O 的 `star_fixed_price_block_start=2026-07-06`，不改语义、不并进 o0。日量与三通道只消费 O，竞价盘后通道只消费 M，盘后可成交只消费 CH，能不能打满只消费 CK，转债盘后只消费 DR，创业板确认钟只消费 DZ，基金收盘切日只消费 DX，申报带只消费 DY，假 T+0 只消费 R，费用只消费 V/T/U，整手只消费 E，板上可成交只消费 A，或显式旁路 |

把切日后仍当成没有、把核对日规则铺满历史、以及相对 O/M/CH/CK/DR/DZ/DX/DY/R/V/T/U/E/A 的对照，放进 §4.1 分桶，**只作诊断桶或半泄露对照，不得升格为第二个主报**。`invent_star_fixed_price_block_type_always_off_post_cut` 只标记「指南之后仍写成这个类型没有」，**不得进主报，不得双挂**。`invent_asof_leak_star_fixed_price_block_on` 只标记核对日泄露。`vs_O_block_liquidity` 只标记日量含大宗 / 三通道对照。`vs_M_aft_channel` / `vs_CH_aft_fill` 只标记竞价盘后固定价格。`vs_CK_block_fill` 只标记假全额可成。`vs_DR_aft_pricing` 只标记转债盘后定价。`vs_DZ_chinext_confirm` 只标记创业板确认钟，**零改 DZ**。`vs_DX_sse_fund_close` 只标记基金收盘切日。`vs_DY_approval_ipo_band` 只标记核准制申报带。`vs_R_etf_t0` 只标记假 T+0。`vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只标记费用。`vs_E_lot_size` 只标记整手。`vs_A_limit_fill` 只标记板上可成交。`missing_board_or_official_rule_not_skip` 只标记缺字段仍不 skip。这些都**不得升格进 `ea0`**。

### 2.3 切日窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **建议** `2026-10-23`（尚未冻）；fill_time **建议** `next_open`（尚未冻；这是信号腿，不是类型开关）；fail **建议** `skip`（尚未冻）。诚实锚六键与 Y/G/N/Y2、`ea0_primary_demo` 同属三条，**都尚未冻**。机制红线只有一句：缺板块标记 / 官方规则则 skip；科创板大宗固定价格类型在上证发〔2019〕23 号下不适用，自 2026-07 技术实施指南起才增加；与 O 的 `star_fixed_price_block_start=2026-07-06` 对齐复用，禁改语义进 `ea0`、禁并进 `o0`；禁止「永远有 / 永远没有」半泄露双挂；禁止与 O0 量价 / 三通道合成一句。`params.G` 的 0.01 不是过户费 0.01‰，也不是类型开或类型关；`params.Y` 的 0.02 不是实验字母 EA，也不是单字母 E 或 A，也不是证管费 0.02‰，也不是切日；四个占位也不是 2026-07、2026-07-06 或 2026-10-23。**禁把占位读成切日日期、类型开关、过户‰**。本页**不开回测**；不拉真数；不做实盘；不开户。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `ea0_primary_demo` / `params.Y`·G·N·Y2 / 类型开关 / 桶 / 是否把类型铺成永远有或永远没有、或与 O0 合成一句、或把占位读成切日日期或类型开关）。本页不开跑。禁 null。三条尚未冻。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（EA0）/ 半泄露组（EA1）相对诚实组（EA2）的类型误套截**显著且集中在 2026-07 技术实施指南之前的科创板大宗被当成已经有固定价格类型**的桶；分桶「切日后仍无 / 核对日泄露 / vs O·M·CH·CK·DR·DZ·DX·DY·R·V·T·U·E·A」不改变主结论方向。成功不依赖把占位读成 2026-07-06 或读成开/关，也不把 `params.Y` 读成实验字母 EA，也不把 `params.G` 的 0.01 读成过户费。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 O 的日量与三通道、M/CH 的竞价盘后、CK 的假全额、DR 的转债盘后、DZ 的确认钟、DX 的基金收盘切日、DY 的申报带、R 的假 T+0、V/T/U 的费用、E 的整手、A 的板上容量解释；或 `ea0_primary_demo` 与 `invent_asof_leak_star_fixed_price_block_on` 双挂；或 EA1 升格并列主报；或诊断桶升格主报；或 `invent_star_fixed_price_block_type_always_off_post_cut` 进主报；或与 O0 量价 / 三通道合成一句进 `ea0`；或把 `star_fixed_price_block_start` 的语义改写进 `ea0` 或并进 `o0`；或实验字母 EA 与单字母 E/A 或 params.Y/G/N 混读；或把占位读成切日日期、类型开关、过户‰；或缺板块标记 / 官方规则仍不 skip；或重开假设-R / 假设-V / 假设-T / 假设-U / 假设-O / 假设-M / 假设-CH / 假设-CK / 假设-DR / 假设-DZ / 假设-DX / 假设-DY / 假设-E / 假设-A；或改 DZ 正文/预检/复检；或标纸面齐；或写成 A/D–EA纸面齐；或把三条建议写成已冻。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 EA0/EA1/EA2。日量与三通道走 O，竞价盘后通道走 M，盘后可成交走 CH，能不能打满走 CK，转债盘后走 DR，创业板确认钟走 DZ，基金收盘切日走 DX，申报带走 DY，假 T+0 走 R，费用走 V/T/U，整手走 E，板上可成交走 A，都不改。报告类型误套截。不把 2026-07、2026-07-06 或开/关标成占位门槛，也不把建议锚写成已冻。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_star_fixed_price_block_type_always_on_pre_cut` / `invent_asof_leak_star_fixed_price_block_on` / `invent_star_fixed_price_block_type_always_off_post_cut` / `vs_O_block_liquidity` / `vs_M_aft_channel` / `vs_CH_aft_fill` / `vs_CK_block_fill` / `vs_DR_aft_pricing` / `vs_DZ_chinext_confirm` / `vs_DX_sse_fund_close` / `vs_DY_approval_ipo_band` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_E_lot_size` / `vs_A_limit_fill` / `missing_board_or_official_rule_not_skip`

`invent_star_fixed_price_block_type_always_on_pre_cut` 才是建议的单一主报名（尚未冻，单挂）。`invent_asof_leak_star_fixed_price_block_on` 只服务半泄露对照，**不得升格进 `ea0`，不得双挂**。自 `invent_star_fixed_price_block_type_always_off_post_cut` 起至 `missing_board_or_official_rule_not_skip` **只作诊断桶**：它们不是 `ea0`，也不是 EA1 主报，**不得升格主报，不得双挂**。**禁止「永远有 / 永远没有」半泄露双挂**。没有「O 日量 + 本页类型开关」合成主报，也没有「M/CH 盘后 + 本页类型」合成主报，也没有「CK 可成交 + 本页类型」合成主报。**实验 R 不抢**。**不重开假设-V / 假设-T / 假设-U**。**零改 DZ**。**禁把 O/M/CH/CK/DR/DZ/DX/DY/R/V/T/U/E/A 升格进 `ea0`**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「科创板大宗固定价格类型永远有」或「永远没有」拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成实验字母 EA，或当成单字母 E/A，或当成证管费 0.02‰，或当成切日，或当成类型开。**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**。**params 字母 ≠ 假设-T**。
- 把 `params.G` 的 0.01 当成过户 0.01‰，或当成类型关，或当成切日。**params 字母 ≠ 假设-U**。**params 字母 ≠ 假设-V**。
- 把 `params.N` 的 0.05 当成实验字母 EA 或单字母 E/A。**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**。
- 把占位 `0.02/0.01/0.05/0.015` 读成切日日期、类型开关、过户‰。**禁把占位读成切日日期、类型开关、过户‰**。**params 相对门槛 ≠ 切日日期 ≠ 类型开关 ≠ 过户‰**。**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U**。**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**。
- 缺板块标记或官方规则仍不 skip。诊断桶 `missing_board_or_official_rule_not_skip` 只作对照，不得升格。
- 把核对日「已经增加该类型」写成全历史规则，或铺到 2026-07 技术实施指南之前。锚六键仍是建议·待冻。半泄露键 `invent_asof_leak_star_fixed_price_block_on` 不得与主报双挂。**禁止「永远有 / 永远没有」半泄露双挂**。
- 把指南之后仍写成这个类型没有，并升格进主报。诊断桶 `invent_star_fixed_price_block_type_always_off_post_cut` 只作对照，**禁进主报，禁双挂**。
- 把假设-O 的日量含大宗、三通道假流动性和本页类型切日合成后升格。**不重开假设-O**。诊断桶 `vs_O_block_liquidity` 只作对照。**禁与 O0 量价 / 三通道合成一句进 `ea0`**。`star_fixed_price_block_start=2026-07-06` 只对齐复用，**禁改语义进 `ea0`，禁并进 `o0`**。
- 把假设-M / 假设-CH 的竞价盘后固定价格和本页大宗固定价格类型合成后升格。诊断桶 `vs_M_aft_channel` / `vs_CH_aft_fill` 只作对照。**不重开假设-M**；**不重开假设-CH**。
- 把假设-CK 的假全额可成和本页类型开关合成后升格。**不重开假设-CK**。诊断桶 `vs_CK_block_fill` 只作对照。
- 把假设-DR 的转债盘后定价和本页合成后升格。**不重开假设-DR**。诊断桶 `vs_DR_aft_pricing` 只作对照。
- 把假设-DZ 的创业板确认钟和本页合成后升格。**零改 DZ**。**不重开假设-DZ**。诊断桶 `vs_DZ_chinext_confirm` 只作对照。
- 把假设-DX / 假设-DY 和本页合成后升格。**不重开假设-DX**；**不重开假设-DY**。诊断桶 `vs_DX_sse_fund_close` / `vs_DY_approval_ipo_band` 只作对照。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格。**实验 R 不抢**。诊断桶 `vs_R_etf_t0` 只作对照。
- 把假设-V / 假设-T / 假设-U 和本页合成或混读后升格。诊断桶 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只作对照。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。
- 把假设-E 的整手、科创板 200 股和本页类型开关合成后升格。**双字母 EA ≠ 单字母假设-E**。诊断桶 `vs_E_lot_size` 只作对照。
- 把假设-A 的涨停可成交和本页类型开关合成后升格。**双字母 EA ≠ 单字母假设-A**。**不抢 A 真数队列**。诊断桶 `vs_A_limit_fill` 只作对照。
- `ea0_primary_demo` 与 `invent_asof_leak_star_fixed_price_block_on` 双挂；EA1 升格并列主报。
- 实验字母 EA 与单字母 E/A 或 params.Y/G/N 混读。**双字母 EA ≠ 单字母 E/A**。
- 改 DZ / DX / DY / O / M / CH / CK / DR / R / V / T / U / E / A 及其他已冻页正文；改 #110–#135；禁止标纸面齐；禁止写成 A/D–EA纸面齐；把三条建议写成已冻；预留 #137；开真数/回测/开户/实盘；用复权价当类型开关的判据；结论写成「这类大宗更能成交所以能买」。
- **纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–DZ；勿再只改清单）。当前禁止标纸面齐。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权路径、交易日、**板块标记**（科创板 / 沪市主板 / 创业板 / 其他）。板块分不清则 skip。本页只钉科创板大宗固定价格类型，不把这道切日套到沪主板或创业板，也不把科创板开市起的盘后固定价格套回来当大宗类型。
- 官方规则是否在册：上证发〔2019〕23 号下科创板大宗不适用固定价格申报；2026-07 技术实施指南起增加该类型。规则不在册则 skip，不用占位数字去填一个日期或一个开/关。
- 申报要能分清是**科创板大宗固定价格类型**，还是竞价、盘后固定价格、协议大宗、深市盘后定价大宗、沪市主板大宗固定价格申报。后几类不进本页主报；三通道的拆分走 O，竞价盘后走 M/CH。
- 类型可用性字段：指南之前这笔不该出现「大宗固定价格」类型，指南起才可以有。只有一根日 K、没有类型字段，不要默认「科创板一直有」，也不要默认「永远没有」。
- 对齐参 `star_fixed_price_block_start=2026-07-06` 只从假设-O **读**来对日期，不在本页改写，不并进 O0 的量价主报。
- 旁路消费：O 的日量与三通道、M 的盘后通道、CH 的盘后可成交、CK 的协议大宗可成交、DR 的转债盘后、DZ 的创业板确认钟、DX 的基金收盘切日、DY 的核准制申报带、R 的假 T+0、V/T/U 的费用、E 的整手、A 的板上可成交（见 §2.1 handoff）。**本页不改写这些页。零改 DZ。**
- 未复权路径；asof **建议** `2026-10-23`（尚未冻）。核对日在技术实施指南之后，所以「核对日当天这个类型已经有」不能倒灌到指南之前。`事实与坑` 2026-10-23 是方向来源，不是已冻的全历史规则。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **建议键摘要（三条尚未冻，不要写成已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-23`；`fail_policy=skip`；`star_fixed_price_block_type_honest=pit_unavailable_pre_202607_tech_guide_else_available`；`star_fixed_price_block_type_scope=star_block_fixed_price_type_availability_only`；`star_fixed_price_block_type_over_policy=skip_if_board_or_official_rule_missing`；`ea0_primary_demo=invent_star_fixed_price_block_type_always_on_pre_cut`（**建议**单一主报，单挂；禁与 `invent_asof_leak_star_fixed_price_block_on` 双挂；EA1 不升格；诊断桶不升格；**禁止「永远有 / 永远没有」半泄露双挂**；**禁与 O0 量价 / 三通道合成一句进 `ea0`**；**禁改 `star_fixed_price_block_start` 语义进 `ea0`、禁并进 `o0`**；**禁把 O/M/CH/CK/DR/DZ/DX/DY/R/V/T/U/E/A 升格进 `ea0`**）；`block_liquidity_handoff=o_page`；`aft_channel_handoff=m_page`；`aft_fill_handoff=ch_page`；`block_fill_handoff=ck_page`；`aft_pricing_handoff=dr_page`；`chinext_confirm_handoff=dz_page`；`sse_fund_close_handoff=dx_page`；`approval_ipo_band_handoff=dy_page`；`etf_t0_handoff=r_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；`lot_size_handoff=e_page`；`limit_fill_handoff=a_page`；`merge_with_DZ/DY/DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/Y/A/D/Z=False`。
- `params.Y/G/N/Y2` **占位** `0.02/0.01/0.05/0.015`（相对门槛，不是切日日期，不是类型开关，不是过户费率；**三条尚未冻**；**params.Y/G/N ≠ 实验字母 EA ≠ 单字母 E/A**；**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**；**params 字母 ≠ 假设-V / 假设-T / 假设-U**；**尤重 params.Y 的 0.02 ≠ 实验字母 EA ≠ 单字母 E/A ≠ 切日日期 ≠ 类型开关 ≠ 证管费 0.02‰**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 切日日期 ≠ 类型开关**；**禁把占位读成切日日期、类型开关、过户‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #137。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`934e3cf`（A/D–DZ纸面齐已合，全长 `934e3cf4c065bf65fa192127131ed2659eebd762`）。**不改已冻 A–DQ / DA–DZ**。**零改 DZ**。**不改 #110–#135**。状态=**草稿·待入库预检**。**三条尚未冻**。**禁止标纸面齐**。

---

## 8. 结论

（空；**草稿·待入库预检**；三条尚未冻；禁止标纸面齐。）

---

## 变更
| 日期 | 变更 |
|------|------|
| 2026-12-07 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。科创板大宗固定价格交易类型切日误套（成交规则）；`ea0_primary_demo` 建议 `invent_star_fixed_price_block_type_always_on_pre_cut`，单一主报，单挂，禁与 `invent_asof_leak_star_fixed_price_block_on` 双挂，EA1 不升格；诊断桶 `invent_star_fixed_price_block_type_always_off_post_cut` / `vs_O_block_liquidity` / `vs_M_aft_channel` / `vs_CH_aft_fill` / `vs_CK_block_fill` / `vs_DR_aft_pricing` / `vs_DZ_chinext_confirm` / `vs_DX_sse_fund_close` / `vs_DY_approval_ipo_band` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_E_lot_size` / `vs_A_limit_fill` / `missing_board_or_official_rule_not_skip` 不升格；**尤重实验 R 不抢，禁把 vs_R_etf_t0 升格进 ea0**；**尤重不重开假设-V / 假设-T / 假设-U，禁把 vs_V_stamp / vs_T_csrc / vs_U_transfer 升格进 ea0**；**尤重 O=日量含大宗/三通道假流动性 ≠ 本页只钉科创大宗固定价格类型可用性切日，`star_fixed_price_block_start` 可复用，禁改语义进 ea0、禁并进 o0，禁把 vs_O_block_liquidity 升格，禁与 O0 量价/三通道合成一句进 ea0**；**尤重 M/CH 竞价盘后固定价格 ≠ 大宗固定价格类型，禁把 vs_M_aft_channel / vs_CH_aft_fill 升格**；**尤重 CK 假全额 ≠ 类型开关，禁把 vs_CK_block_fill 升格**；**尤重 DR 转债盘后定价 ≠ 本页，禁把 vs_DR_aft_pricing 升格**；**尤重 DZ 创业板确认钟 ≠ 本页，禁把 vs_DZ_chinext_confirm 升格，零改 DZ**；**尤重双字母 EA ≠ 单字母假设-E / 假设-A，禁把 vs_E_lot_size / vs_A_limit_fill 升格**；**尤重 params.Y/G/N ≠ 实验字母 EA / 单字母 E/A**；**尤重禁止「永远有/永远没有」半泄露双挂**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U**；**禁把占位读成切日日期、类型开关、过户‰**；**禁把 DX/DY 升格进 ea0**；**零改 DZ**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 EA ≠ 单字母 E/A**；锚建议·待冻、未冻：`star_fixed_price_block_type_honest=pit_unavailable_pre_202607_tech_guide_else_available` / scope=`star_block_fixed_price_type_availability_only` / over_policy=`skip_if_board_or_official_rule_missing` / `asof_check_date=2026-10-23` / `fill_time=next_open` / `fail_policy=skip`；口径：缺板块标记/官方规则则 skip；上证发〔2019〕23 号下不适用，自 2026-07 技术实施指南起增加该类型；与 O 分桶参 `star_fixed_price_block_start=2026-07-06` 对齐复用，禁改语义进 ea0、禁并进 o0；禁止「永远有/永远没有」半泄露双挂；禁止与 O0 量价/三通道合成一句（**草稿方向，尚未冻，不要写成已冻**）；handoff：`block_liquidity_handoff=o_page`，`aft_channel_handoff=m_page`，`aft_fill_handoff=ch_page`，`block_fill_handoff=ck_page`，`aft_pricing_handoff=dr_page`，`chinext_confirm_handoff=dz_page`，`sse_fund_close_handoff=dx_page`，`approval_ipo_band_handoff=dy_page`，`etf_t0_handoff=r_page`，`stamp_handoff=v_page`，`csrc_fee_handoff=t_page`，`transfer_fee_handoff=u_page`，`lot_size_handoff=e_page`，`limit_fill_handoff=a_page`；全部 `merge_with_*=False`；`merge_with_DZ/DY/DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/Y/A/D/Z=False`；**EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z**；**双字母 EA ≠ 单字母 E/A**；**未标纸面齐**；**不写 A/D–EA纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–DZ；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–DZ；**零改 DZ**；不改 #110–#135；不重开假设-R；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-O；不重开假设-M；不重开假设-CH；不重开假设-CK；不重开假设-DR；不重开假设-DZ；不重开假设-DX；不重开假设-DY；不重开假设-E；不重开假设-A；不写下一字母；不预留 #137；不开真数/回测/开户/实盘。基 tip=`934e3cf`（A/D–DZ纸面齐已合，全长 `934e3cf4c065bf65fa192127131ed2659eebd762`；不改该 tip 上的 #110–#135，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
