# 假设-DZ · 创业板协议大宗确认时点切日误套（成交规则）

更新：2026-12-06  
来源：总管线 / 基 tip=`55056e0` / 全长 `55056e05d55f90b6a9029c56969795d733fab638`（A/D–DY纸面齐已合）；**不改已冻 A–DQ / DA–DY**；**零改 DY**；**不改假设-DY 正文/预检/复检**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-DT / 假设-DU / 假设-DV / 假设-DW / 假设-DX / 假设-DY / 假设-S / 假设-AX / 假设-AY / 假设-AW / 假设-T / 假设-U / 假设-V / 假设-W / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-E / 假设-F / 假设-J / 假设-G / 假设-CI / 假设-CK / 假设-Y / 假设-A / 假设-D / 假设-X / 假设-Z 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ）；**不重开假设-R**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-O**；**不重开假设-CK**；**不重开假设-DI**；**不重开假设-DL**；**不重开假设-DR**；**不重开假设-M**；**不重开假设-DY**；**不重开假设-DX**；**不重开假设-D**；**不重开假设-Z**；**不重开假设-W**；**不重开假设-X**；**不重开假设-AY**；**不重开假设-DW**；**不重开假设-DV**；**不重开假设-DT**；**不重开假设-DS**）后写下一草稿 DZ；清单 #134=DY，本页占用 **#135=DZ**；选题是回测把 **创业板协议大宗的确认时点**按切日套错（诚实方向：创业板协议大宗确认 **`<2026-07-06` → 15:00–15:30**，**`≥2026-07-06` → 9:30–11:30、13:00–15:30**；缺板块标记 / 官方规则则 skip；禁止倒铺沪主板 / 科创确认钟进主报；禁止与 O0 量价 / 三通道合成一句）；假设-O 只收日量含大宗与三通道假流动性，假设-CK 只收协议大宗假全额可成，假设-DI 只收股票大宗经手下浮，假设-DL 只收综合协议过户费下浮，假设-DR 只收可转债盘后定价，假设-M 只收盘后通道，假设-DY 只收核准制主板新股首日申报带，假设-DX 只收沪市基金收盘产生方式切日，假设-R 只收股票 ETF 假 T+0，假设-V 只收股票印花税切日，假设-T 只收股票证管费切日，假设-U 只收股票过户切日，假设-D 只收成交时点与停牌，假设-Z 只收融资保证金比例误铺；**新建实验 DZ**；不写下一字母；不预留 #136  
状态：**预检有条件通过·三条已冻·待复检**（结论栏空；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DZ纸面齐**；禁止把「创业板协议大宗一直盘中确认」或「沪主板 / 科创的确认钟」当诚实锚；禁止与 O0 量价 / 三通道合成一句；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–DY**；**零改 DY**；**不改 #110–#134**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DZ（#135）。一句话误开：回测把创业板协议大宗在 **2026-07-06 之前**的确认写成盘中 9:30–11:30、13:00–15:30，或把创业板切日之后的盘中确认钟抄到沪主板 / 科创，或把沪主板仍在用的 15:00–15:30、科创开市起的盘中确认钟倒铺进本页主报，或与 O日量含大宗·三通道假流动性 / CK协议大宗假全额可成 / DI大宗经手下浮 / DL综合协议过户费下浮 / DR可转债盘后定价 / M盘后通道 / DY核准制首日申报带 / DX沪市基金收盘切日 / R股票ETF假T+0 / V股票印花 / T股票证管费 / U股票过户 混读，或缺板块标记 / 官方规则仍不 skip，系统性改写这笔协议大宗**当时在哪个钟点才确认**。**禁把 O/CK/DI/DL/DR/M/DY/DX/R/V/T/U 混读升格进 `dz0`**。**禁把 `copy_chinext_intraday_confirm_onto_sh_main` 升格进主报**。**禁把 `invent_asof_leak_chinext_block_confirm_intraday` 与主报双挂**。**禁与 O0 量价 / 三通道合成一句进 `dz0`**。

> **字母消歧（硬）**：本页**实验字母 DZ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DZ**；**尤重：`params.Y/G/N` ≠ 实验字母 DZ / 单字母 D/Z**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**；**勿把 `params.Y` 读成实验字母 DZ，亦勿读成单字母假设-D，亦勿读成单字母假设-Z，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U**；**尤重：`params.Y` 的 0.02 ≠ 实验字母 DZ ≠ 单字母 D/Z ≠ 确认钟时刻 ≠ 切日日期 ≠ 核对日 ≠ 过户‰ ≠ 证管费 0.02‰**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DZ**；**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 确认钟时刻 ≠ 切日日期**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是 15:00，不是 9:30，不是 2026-07-06，也不是过户费率）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DZ**；**params.N ≠ 单字母 D/Z**）≠ **`params.Y2`**（写死冻结 0.015；不是确认钟，不是切日）≠ **单字母实验 D**（成交时点与停牌；**双字母 DZ ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 Z**（融资保证金比例误铺；**双字母 DZ ≠ 单字母假设-Z；严禁复用假设-Z**）≠ **单字母实验 V**（股票印花税切日；**双字母 DZ ≠ 单字母假设-V；严禁复用假设-V**；**不重开假设-V**）≠ **单字母实验 U**（股票过户费切日；**双字母 DZ ≠ 单字母假设-U；严禁复用假设-U**；**不重开假设-U**）≠ **单字母实验 T**（股票证管费切日；**双字母 DZ ≠ 单字母假设-T；严禁复用假设-T**；**不重开假设-T**）≠ **单字母实验 R**（股票 ETF 假 T+0；**双字母 DZ ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `dz0`**）≠ **双字母 DY**（核准制主板新股首日申报价格上下限；**零改 DY**；**DZ≠DY**）≠ **双字母 DX**（沪市基金收盘产生方式切日；**DZ≠DX**）≠ **双字母 O**（大宗日量 / 三通道假流动性；**O ≠ 本页确认窗**）≠ **双字母 CK**（协议大宗可成交性；假全额可成 ≠ 确认钟）≠ **双字母 DI**（股票大宗经手下浮；费率 ≠ 确认钟）≠ **双字母 DL**（综合协议过户费下浮；费率 ≠ 确认钟）≠ **双字母 DR**（可转债盘后定价；盘后定价 ≠ 协议大宗确认钟）≠ **单字母 M**（盘后通道；盘后通道 ≠ 协议大宗确认钟）≠ **DQ / DP / DO / DN / DM / DK / DJ / DH / DG / DF / DE / DD / DC / DB / DA**（费用旁路；不并进 `dz0`）≠ **S**（股票经手费切日）≠ **AX**（基金经手费）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债回转/涨跌幅/收盘）≠ **CH / CL / CR / CQ**（可成交性旁路）≠ **E / F / J / W / AW / AY / X / G / CI / Y**（整手、取整、临停、除权、收盘集合失败回落、价位、ST 板幅、无板日默认板、新股首日可成交、集合竞价量）≠ **DW / DV / DU / DT / DS**（行权过户、现金选择权、转债首日临停、整手价位、转股印花）≠ **单字母实验 A**（板上枯竭）。**DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z**。**双字母 DZ ≠ 单字母 D/Z**。**双字母 DZ ≠ 单字母假设-D / 假设-Z**。**params.Y/G/N ≠ 实验字母 DZ ≠ 单字母 D/Z**。**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**。**禁把占位读成确认钟时刻、切日日期、过户‰**。**params 相对门槛 ≠ 确认钟时刻 ≠ 切日日期 ≠ 过户‰**。**创业板协议大宗确认窗切日 ≠ O日量含大宗/三通道假流动性 ≠ CK假全额可成 ≠ DI/DL费率 ≠ DR盘后定价 ≠ M盘后通道 ≠ DY核准制首日申报带 ≠ DX沪市基金收盘切日 ≠ R股票ETF假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ D成交时点 ≠ Z融资保证金比例**。**尤重：实验 R 不抢；禁把 `vs_R_etf_t0` 升格进 `dz0`**。**尤重：不重开假设-V / 假设-T / 假设-U；禁把 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 升格进 `dz0`**。**尤重：O = 日量含大宗 / 三通道假流动性 ≠ 本页仅创业板确认窗切日；禁把 `vs_O_block_liquidity` 升格进 `dz0`；禁与 O0 量价 / 三通道合成一句进 `dz0`**。**尤重：CK 假全额可成 ≠ 本页确认钟；禁把 `vs_CK_block_fill` 升格进 `dz0`**。**尤重：DI/DL 费率 ≠ 本页确认钟；禁把 `vs_DI_block_fee` / `vs_DL_nego_transfer_fee` 升格进 `dz0`**。**尤重：DR/M 盘后定价 / 盘后通道 ≠ 本页协议大宗确认钟；禁把 `vs_DR_aft_pricing` / `vs_M_aft_channel` 升格进 `dz0`**。**尤重：禁 `copy_chinext_intraday_confirm_onto_sh_main` 倒铺沪主板 / 科创确认钟进主报**。**尤重：DY/DX 旁路诊断禁升格进 `dz0`**。**零改 DY**。

### 专节 · 双字母 DZ ≠ 单字母假设-D / 假设-Z；且 ≠ 假设-O / 假设-CK / 假设-DI / 假设-DL / 假设-DR / 假设-M / 假设-R / 假设-V / 假设-T / 假设-U / 假设-DY（硬）

| 维度 | 对照页 | 本页假设-DZ（双字母） |
|------|--------|----------------------|
| 题面 O | **大宗量价并进竞价 / 三条盘后通道混用**（日成交量含大宗结束后计入的那截；按大宗价回放竞价；盘后固定价格、深市盘后定价大宗、沪市大宗固定价格申报合成一句；假设-O） | **O = 量、价、三通道假流动性**。本页只问创业板**协议大宗的确认窗**在切日前后是 15:00–15:30 还是盘中。门槛 30 万股 / 200 万元、日量何时计入、三条通道怎么拆，都留在 O。两句禁止合成。**DZ≠O**；**不重开假设-O**；**不改 O**；**尤重：禁把 `vs_O_block_liquidity` 升格进 `dz0`**；**禁与 O0 量价 / 三通道合成一句进 `dz0`**；`block_liquidity_handoff=o_page` |
| 题面 CK | **协议大宗可成交性误开**（默认协议 / 成交申报大宗必能按目标价或谈妥价全额成交；假设-CK） | **CK = 价已经在窗里之后，单子能不能打满**。本页 = 这笔确认**落在哪个钟点**。窗对了也不等于全额成交。**DZ≠CK**；**不重开假设-CK**；**不改 CK**；**尤重：禁把 `vs_CK_block_fill` 升格进 `dz0`**；`block_fill_handoff=ck_page` |
| 题面 DI | **股票大宗经手下浮误忽略**（假设-DI） | 经手费下浮是成本，不是确认钟。**DZ≠DI**；**不重开假设-DI**；**不改 DI**；**尤重：禁把 `vs_DI_block_fee` 升格进 `dz0`**；`block_fee_handoff=di_page` |
| 题面 DL | **股票综合协议过户费下浮误忽略**（假设-DL） | 协议过户费下浮是另一档费率。`params.G` 的 0.01 不是这档，也不是过户 0.01‰。**DZ≠DL**；**不重开假设-DL**；**不改 DL**；**尤重：禁把 `vs_DL_nego_transfer_fee` 升格进 `dz0`**；`nego_transfer_fee_handoff=dl_page` |
| 题面 DR | **可转债盘后定价误套股票盘后固定价格**（假设-DR） | 转债盘后定价通道 ≠ 创业板协议大宗确认钟。**DZ≠DR**；**不重开假设-DR**；**不改 DR**；**尤重：禁把 `vs_DR_aft_pricing` 升格进 `dz0`**；`aft_pricing_handoff=dr_page` |
| 题面 M | **盘后固定价格通道误套全历史**（假设-M） | 盘后固定价格是收盘后再按收盘价撮合的另一条通道。同一天 2026-07-06 可以既改创业板协议大宗确认窗、又扩盘后，两件事禁止合成。**DZ≠M**；**不重开假设-M**；**不改 M**；**尤重：禁把 `vs_M_aft_channel` 升格进 `dz0`**；`aft_channel_handoff=m_page` |
| 题面 倒铺确认钟 | **沪市主板**成交申报确认仍是 **15:00–15:30**；**科创板**开市起就是盘中 9:30–11:30、13:00–15:30（`事实与坑` 2026-10-23） | 这两口钟都不是创业板协议大宗的切日。把沪主板或科创的钟写进本页主报，或把创业板 `≥2026-07-06` 的盘中确认钟抄到沪主板，都算跨板块抄钟。诊断桶 `copy_chinext_intraday_confirm_onto_sh_main` 只标记这件事。**禁升格进 `dz0`**。**禁止倒铺沪主板 / 科创确认钟进主报** |
| 题面 半泄露 | 核对日 2026-10-23 已经在切日之后，创业板协议大宗确认已经是盘中 | `invent_asof_leak_chinext_block_confirm_intraday` 只作半泄露对照。**禁与 `dz0` 双挂**；不得升格并列主报 |
| 题面 DY | **核准制主板新股首日申报价格上下限**（假设-DY 已纸面齐） | 首日申报带 ≠ 大宗确认钟。**零改 DY**。**DZ≠DY**；**不重开假设-DY**；**不改 DY 正文/预检/复检**；**尤重：禁把 `vs_DY_approval_ipo_band` 升格进 `dz0`**；`approval_ipo_band_handoff=dy_page` |
| 题面 DX | **沪市基金收盘产生方式切日**（假设-DX） | 基金收盘怎么产生 ≠ 创业板协议大宗确认窗。同日 2026-07-06 不是同一件事。**DZ≠DX**；**不重开假设-DX**；**不改 DX**；**尤重：禁把 `vs_DX_sse_fund_close` 升格进 `dz0`**；`sse_fund_close_handoff=dx_page` |
| 题面 R | **股票 ETF 假 T+0**（假设-R） | **实验 R 不抢**。ETF 能不能当日回转，和协议大宗何时确认，是两件事。**DZ≠R**；**严禁复用假设-R**；**不重开假设-R**；**不改 R**；**尤重：禁把 `vs_R_etf_t0` 升格进 `dz0`**；`etf_t0_handoff=r_page` |
| 题面 V | **股票印花税切日**（假设-V） | **不重开假设-V**。印花切日 ≠ 确认钟。占位不是印花税率。**DZ≠V**；**params 字母 ≠ 假设-V**；**不改 V**；**尤重：禁把 `vs_V_stamp` 升格进 `dz0`**；`stamp_handoff=v_page` |
| 题面 T | **股票证管费切日**（假设-T） | **不重开假设-T**。`params.Y` 的 0.02 不是证管费 0.02‰，也不是实验字母 DZ。**DZ≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：禁把 `vs_T_csrc` 升格进 `dz0`**；`csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日**（假设-U） | **不重开假设-U**。`params.G` 的 0.01 不是过户 0.01‰。**DZ≠U**；**params 字母 ≠ 假设-U**；**不改 U**；**尤重：禁把 `vs_U_transfer` 升格进 `dz0`**；`transfer_fee_handoff=u_page` |
| 题面 D | **成交时点与停牌**（次日开还是次日收；停牌日记不可交易；假设-D） | 先问这笔协议大宗当时在哪个钟点确认，再问信号腿在次日开盘还是次日收盘成交。`fill_time=next_open` 是信号腿建议，不是确认钟。**双字母 DZ ≠ 单字母假设-D**；**严禁复用假设-D**；**DZ≠D**；**不重开假设-D**；**不改 D**；`merge_with_D=False` |
| 题面 Z | **融资保证金比例现行档误铺**（假设-Z） | 保证金比例不是大宗确认窗。**双字母 DZ ≠ 单字母假设-Z**；**严禁复用假设-Z**；**DZ≠Z**；**不重开假设-Z**；**不改 Z**；`merge_with_Z=False` |
| 题面 DW / DV / DU / DT / DS / DQ–DA / S / AX / AC / Q / CH / CL / CR / CQ / E / F / J / W / AW / AY / X / G / CI / Y | 费用、整手、可成交性、临停、价位等旁路 | 全部不并进 `dz0`。**DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z**。不改这些页 |
| 题面 A | **涨停可成交 / 板上枯竭** | **DZ≠A**；**不抢 A 真数队列**；**不改 A** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_chinext_nego_block_confirm_as_intraday_pre_20260706`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_chinext_block_confirm_intraday` 双挂；DZ1 不升格；诊断桶不升格） |
| 文档 | 清单实验 DY 及上表各页（**只读；禁止改写**） | `假设-DZ-创业板协议大宗确认时点切日误套.md`（新建） |
| 预检键 | 实验字母 DY / DX / … / D / Z / O / CK / V / T / U / R | 实验字母 **DZ** / `dz0_primary_demo`；**不得**占用或改写上述预检键；**params.Y/G/N ≠ 实验字母 DZ** |

**禁止**：把 DZ 写成「O / CK / DI / DL / DR / M / R 的续篇」；把「核对日创业板已经盘中确认 / 科创板开市起就盘中 / 沪主板一直 15:00–15:30 / 盘后通道也在 2026-07-06 扩围」写成「创业板协议大宗确认切日已诚实」；把实验字母 DZ 与单字母 D/Z 或 params.Y/G/N 混读；**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**；**禁把占位 `0.02/0.01/0.05/0.015` 读成确认钟时刻、切日日期、过户‰**；**实验 R 不抢**；**不重开假设-V / 假设-T / 假设-U**；**O 日量含大宗 / 三通道 ≠ 本页确认窗**；**CK 假全额可成 ≠ 本页确认钟**；**DI/DL 费率 ≠ 本页确认钟**；**DR/M 盘后 ≠ 本页协议大宗确认钟**；**禁 `copy_chinext_intraday_confirm_onto_sh_main` 倒铺沪主板 / 科创确认钟进主报**；**禁与 O0 量价 / 三通道合成一句进 `dz0`**；**零改 DY**；**禁把 O/CK/DI/DL/DR/M/DY/DX/R/V/T/U 的诊断升格进 `dz0`**；把 `invent_asof_leak_chinext_block_confirm_intraday` 与主报双挂；缺板块标记 / 官方规则仍硬填。本页主键只用 `dz0` / `dz1` / `dz2` 与 `chinext_block_confirm_*`。不写下一字母。不预留 #136。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–DY；勿再只改清单）。当前**禁止标纸面齐**，**不写 A/D–DZ纸面齐**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测把 **2026-07-06 之前的创业板协议大宗确认**写成 **已经是盘中**（9:30–11:30、13:00–15:30），或把沪主板 / 科创的确认钟倒铺进来，或与 O 的日量含大宗和三通道、CK 的假全额可成、DI/DL 的费率、DR/M 的盘后、DY 的申报带、DX 的基金收盘切日、R 的假 T+0、V/T/U 的费用切日混读，或缺板块标记 / 官方规则仍不 skip，相对「缺字段则 skip；创业板协议大宗确认 `<2026-07-06` 为 15:00–15:30，`≥2026-07-06` 为 9:30–11:30、13:00–15:30；不倒铺沪主板 / 科创确认钟；不与 O0 量价 / 三通道合成一句」的诚实组，会**系统性改写这笔协议大宗当时在哪个钟点才确认**——尾盘才确认的单被写成盘中已经落地，或盘中才该确认的单被写成仍要等到 15:00。方向是相对诚实锚偏误。

核对日方向（随锚写死；禁把占位读成确认钟时刻、切日日期、过户‰）：`事实与坑` 2026-10-23 写明，确认时点要按板块切片，不要用创业板现行「盘中确认」铺满全历史、全板块。创业板协议大宗的确认时间由 **15:00–15:30** 改成 **9:30–11:30、13:00–15:30**，与 **2026-07-06** 同日落地；来源是深交所《交易规则》修订说明。此前不要写成盘中实时确认。沪市主板成交申报确认仍是 15:00–15:30。科创板开市起就是盘中同一窗口。深市盘后定价大宗、盘后固定价格、沪市大宗固定价格申报是另外三条，不在本页主报里。本页把创业板协议大宗这一道确认窗收成已写死冻结的锚。方向随锚写死，不要把确认窗铺成全历史唯一规则。日量含不含大宗、谈妥价能不能当竞价价、三通道怎么拆，留在假设-O。能不能打满留在假设-CK。费率留在 DI / DL / V / T / U。盘后通道留在 DR / M。缺板块标记或官方规则，整笔 skip。**禁把占位读成确认钟时刻、切日日期、过户‰**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**。**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**。

证伪方向：若天真组 / 半泄露组相对诚实组的确认窗误套截在标定噪声带内可忽略，且「切日前误当盘中 / 倒铺沪主板或科创确认钟 / 核对日泄露 / vs O·CK·DI·DL·DR·M·DY·DX·R·V·T·U」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dz0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结；禁止标纸面齐；不写 A/D–DZ纸面齐）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DZ ≠ 单字母假设-D / 假设-Z**；勿把 params.Y 读成实验字母 DZ，亦勿读成单字母假设-D，亦勿读成单字母假设-Z，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U
# 【消歧】尤重：params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z
# 【消歧】params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D
# 【消歧】尤重：params.Y 的 0.02 ≠ 实验字母 DZ ≠ 单字母 D/Z ≠ 确认钟时刻 ≠ 切日日期 ≠ 核对日 ≠ 过户‰ ≠ 证管费 0.02‰
# 【消歧】尤重：params.G 的 0.01 ≠ 过户 0.01‰ ≠ 确认钟时刻 ≠ 切日日期（无量纲相对门槛 ≠ 过户费率 ≠ 15:00 ≠ 9:30 ≠ 2026-07-06）
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DZ ≠ 单字母 D/Z**
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成确认钟时刻、切日日期、过户‰
# 【消歧】params 相对门槛 ≠ 确认钟时刻 ≠ 切日日期 ≠ 过户‰
# 【消歧】三条已冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值
# params.Y2                               写死冻结 0.015（不是 15:00，不是 9:30，不是 2026-07-06，不是确认钟，不是过户‰）
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：确认窗误套截 ΔChinextBlockConfirm / 净差异 / DZ1−DZ2；**params.Y/G/N ≠ 实验字母 DZ ≠ 单字母 D/Z**；**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**；**尤重 params.G=`0.01` ≠ 过户‰ ≠ 确认钟**；**尤重 params.Y=`0.02` ≠ 证管费‰ ≠ 切日/核对日**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 确认钟时刻 ≠ 切日日期**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期 ≠ 核对日 ≠ 实验字母 DZ**；**禁把占位读成确认钟时刻、切日日期、过户‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        写死冻结 next_open
#   这是信号腿的成交时点建议，不是大宗确认钟
#   不要把 next_open 读成 9:30，也不要读成 15:00–15:30
#   双字母 DZ ≠ 单字母假设-D
# params.asof_check_date                  写死冻结 2026-10-23（这是核对日，不是切日，也不是占位，也不是 2026-07-06）
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.chinext_block_confirm_honest     写死冻结 pit_pre_20260706_1500_1530_else_intraday
#   诚实锚方向（已写死冻结）：
#   缺板块标记或官方规则 → skip
#   创业板协议大宗确认：<2026-07-06 → 15:00–15:30
#   ≥2026-07-06 → 9:30–11:30、13:00–15:30
#   禁止倒铺沪主板 / 科创确认钟进主报
#   禁止与 O0 量价 / 三通道合成一句
#   禁止把占位读成确认钟时刻、切日日期或过户‰
#   锚名字里的钟点和日期是机制方向，不是 params.Y/G/N/Y2
#   枚举已写死冻结
# params.chinext_block_confirm_scope      写死冻结 chinext_nego_block_confirm_window_only
#   只看创业板协议大宗的确认窗切日
#   不是日量含大宗，不是三通道，不是能不能打满，不是费率，不是盘后通道
# params.chinext_block_confirm_over_policy 写死冻结 skip_if_board_or_official_rule_missing
#   缺板块标记 / 官方规则则 skip
# params.block_liquidity_handoff          建议 o_page
#   日量含大宗 / 三通道交 O；O ≠ 本页确认窗；不重开假设-O；不改 O
#   诊断桶 vs_O_block_liquidity 不得升格进 dz0
#   禁与 O0 量价 / 三通道合成一句进 dz0
# params.block_fill_handoff               建议 ck_page
#   协议大宗可成交性交 CK；CK 假全额可成 ≠ 本页确认钟；不重开假设-CK；不改 CK
#   诊断桶 vs_CK_block_fill 不得升格进 dz0
# params.block_fee_handoff                建议 di_page
#   大宗经手下浮交 DI；费率 ≠ 确认钟；不重开假设-DI；不改 DI
#   诊断桶 vs_DI_block_fee 不得升格进 dz0
# params.nego_transfer_fee_handoff        建议 dl_page
#   综合协议过户费下浮交 DL；费率 ≠ 确认钟；不重开假设-DL；不改 DL
#   诊断桶 vs_DL_nego_transfer_fee 不得升格进 dz0
# params.aft_pricing_handoff              建议 dr_page
#   可转债盘后定价交 DR；不重开假设-DR；不改 DR
#   诊断桶 vs_DR_aft_pricing 不得升格进 dz0
# params.aft_channel_handoff              建议 m_page
#   盘后通道交 M；不重开假设-M；不改 M
#   诊断桶 vs_M_aft_channel 不得升格进 dz0
# params.approval_ipo_band_handoff        建议 dy_page
#   核准制首日申报带交 DY；零改 DY；不重开假设-DY；不改 DY 正文/预检/复检
#   诊断桶 vs_DY_approval_ipo_band 不得升格进 dz0
# params.sse_fund_close_handoff           建议 dx_page
#   沪市基金收盘切日交 DX；不重开假设-DX；不改 DX
#   诊断桶 vs_DX_sse_fund_close 不得升格进 dz0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 dz0；不改 R
#   诊断桶 vs_R_etf_t0 不得升格进 dz0
# params.stamp_handoff                    建议 v_page
#   股票印花切日交 V；不重开假设-V；params 字母 ≠ 假设-V；不改 V
#   诊断桶 vs_V_stamp 不得升格进 dz0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；params 字母 ≠ 假设-T；不改 T
#   诊断桶 vs_T_csrc 不得升格进 dz0
# params.transfer_fee_handoff             建议 u_page
#   股票过户切日交 U；不重开假设-U；params 字母 ≠ 假设-U；不改 U
#   诊断桶 vs_U_transfer 不得升格进 dz0
# params.dz0_primary_demo                 写死冻结 invent_chinext_nego_block_confirm_as_intraday_pre_20260706
#   单一主报写死，单挂
#   禁与 invent_asof_leak_chinext_block_confirm_intraday 双挂
#   DZ1 不升格；诊断桶不升格
#   半泄露名只作对照，不得升格进 dz0，不得双挂
#   禁止倒铺沪主板 / 科创确认钟进主报
#   禁止与 O0 量价 / 三通道合成一句进 dz0
#   诊断桶 copy_chinext_intraday_confirm_onto_sh_main / vs_O_block_liquidity / vs_CK_block_fill / vs_DI_block_fee / vs_DL_nego_transfer_fee / vs_DR_aft_pricing / vs_M_aft_channel / vs_DY_approval_ipo_band / vs_DX_sse_fund_close / vs_R_etf_t0 / vs_V_stamp / vs_T_csrc / vs_U_transfer / missing_board_or_official_rule_not_skip 不得升格进 dz0
#   禁把以下升格进 dz0：O日量含大宗/三通道假流动性 / CK假全额可成 / DI大宗费率 / DL协议过户费率 / DR盘后定价 / M盘后通道 / DY核准制申报带 / DX沪市基金收盘切日 / R假T+0 / V印花 / T证管费 / U过户 / 倒铺沪主板或科创确认钟 / 与 O0 量价三通道合成一句
#   尤重：实验 R 不抢
#   尤重：不重开假设-V / 假设-T / 假设-U
#   尤重：O/CK/DI/DL/DR/M 不升格
#   尤重：零改 DY；禁把 DY/DX 升格进 dz0
# params.dz0_invent_chinext_nego_block_confirm_as_intraday_pre_20260706 建议 True
# params.dz1_asof_leak_chinext_block_confirm_intraday_only 建议 True
#   半泄露对照；DZ1 不升格并列主报；不得把 invent_asof_leak_chinext_block_confirm_intraday 写进 dz0
# params.dz2_pit_pre_20260706_1500_1530_else_intraday 建议 True
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
# params.day_freq_proxy                   建议 chinext_block_confirm_sensitivity
# params.universe_rule                    建议 chinext_block_confirm_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dz_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DZ；勿读成单字母 D/Z
#   不另挂主报，不预留 #136，不写下一字母
```

### 2.2 三组对照（DZ0 / DZ1 / DZ2）

组名 DZ0 / DZ1 / DZ2 是本页三组，≠ 单字母实验 D（成交时点与停牌），亦 ≠ 单字母实验 Z（融资保证金比例误铺）。**双字母 DZ ≠ 单字母假设-D / 假设-Z**。**params.Y/G/N ≠ 实验字母 DZ ≠ 单字母 D/Z**。**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**。

| 组 | 角色 | 口径 |
|----|------|------|
| DZ0 | 天真 / 切日前的创业板协议大宗确认当成已经盘中 | 按 `dz0_primary_demo` **写死冻结**单一主报 `invent_chinext_nego_block_confirm_as_intraday_pre_20260706`（单挂写死）：把 2026-07-06 之前的创业板协议大宗确认写成 9:30–11:30、13:00–15:30。**禁**与 `invent_asof_leak_chinext_block_confirm_intraday` 双挂。**禁把倒铺沪主板/科创确认钟、O/CK/DI/DL/DR/M、DY/DX、R/V/T/U 合成进 `dz0`**。**禁与 O0 量价 / 三通道合成一句进 `dz0`** |
| DZ1 | 半泄露 | 仅用核对日「创业板协议大宗确认已经是盘中」把这条铺到全历史、铺到 2026-07-06 之前，或铺到沪主板 / 科创（`invent_asof_leak_chinext_block_confirm_intraday`）。**不得升格并列主报**，不得写进 `dz0`，不得双挂 |
| DZ2 | 诚实 / 按切日的创业板协议大宗确认窗 | `chinext_block_confirm_honest=pit_pre_20260706_1500_1530_else_intraday`（写死冻结）：缺板块标记/官方规则则 skip；`<2026-07-06` 确认窗=15:00–15:30，`≥2026-07-06` 确认窗=9:30–11:30、13:00–15:30。日量与三通道只消费 O，能不能打满只消费 CK，费率只消费 DI/DL 与 V/T/U，盘后只消费 DR 与 M，申报带只消费 DY，基金收盘切日只消费 DX，假 T+0 只消费 R，开收时点只消费 D，保证金比例只消费 Z，或显式旁路 |

把创业板盘中确认钟抄到沪主板、把沪主板或科创的钟倒铺进主报、把核对日规则铺满历史、以及相对 O/CK/DI/DL/DR/M/DY/DX/R/V/T/U 的对照，放进 §4.1 分桶，**只作诊断桶或半泄露对照，不得升格为第二个主报**。`copy_chinext_intraday_confirm_onto_sh_main` 只标记「有人把创业板盘中确认钟抄到沪主板，或把沪主板 / 科创确认钟倒铺进主报」，**不得进主报，不得双挂**。`invent_asof_leak_chinext_block_confirm_intraday` 只标记核对日泄露。`vs_O_block_liquidity` 只标记日量含大宗 / 三通道对照。`vs_CK_block_fill` 只标记假全额可成对照。`vs_DI_block_fee` / `vs_DL_nego_transfer_fee` 只标记费率对照。`vs_DR_aft_pricing` / `vs_M_aft_channel` 只标记盘后对照。`vs_DY_approval_ipo_band` 只标记核准制申报带，**零改 DY**。`vs_DX_sse_fund_close` 只标记基金收盘切日。`vs_R_etf_t0` 只标记假 T+0 对照。`vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只标记费用对照。`missing_board_or_official_rule_not_skip` 只标记缺字段仍不 skip。这些都**不得升格进 `dz0`**。

### 2.3 切日窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-23`；fill_time **写死冻结** `next_open`（这是信号腿，不是确认钟）；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dz0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺板块标记 / 官方规则则 skip；创业板协议大宗确认 `<2026-07-06` 为 15:00–15:30，`≥2026-07-06` 为 9:30–11:30、13:00–15:30；禁止倒铺沪主板 / 科创确认钟进主报；禁止与 O0 量价 / 三通道合成一句。`params.G` 的 0.01 不是过户费 0.01‰，也不是 15:00 或 9:30；`params.Y` 的 0.02 不是实验字母 DZ，也不是单字母 D 或 Z，也不是证管费 0.02‰，也不是切日；四个占位也不是 2026-07-06、2026-10-23 或确认钟上的时、分。**禁把占位读成确认钟时刻、切日日期、过户‰**。本页**不开回测**；不拉真数；不做实盘；不开户。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dz0_primary_demo` / `params.Y`·G·N·Y2 / 确认窗开关 / 桶 / 是否把盘中确认铺到 2026-07-06 之前、或倒铺沪主板/科创确认钟、或与 O0 合成一句、或把占位读成确认钟时刻）。本页不开跑。禁 null。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DZ0）/ 半泄露组（DZ1）相对诚实组（DZ2）的确认窗误套截**显著且集中在 2026-07-06 之前的创业板协议大宗被当成已经盘中确认**的桶；分桶「倒铺沪主板/科创确认钟 / 核对日泄露 / vs O·CK·DI·DL·DR·M·DY·DX·R·V·T·U」不改变主结论方向。成功不依赖把占位读成 15:00 或 2026-07-06，也不把 `params.Y` 读成实验字母 DZ，也不把 `params.G` 的 0.01 读成过户费。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 O 的日量与三通道、CK 的假全额可成、DI/DL 的费率、DR/M 的盘后、DY 的申报带、DX 的基金收盘切日、R 的假 T+0、V/T/U 的费用、D 的开收时点、Z 的保证金比例、或 A 的板上容量解释；或 `dz0_primary_demo` 与 `invent_asof_leak_chinext_block_confirm_intraday` 双挂；或 DZ1 升格并列主报；或诊断桶升格主报；或 `copy_chinext_intraday_confirm_onto_sh_main` 进主报；或与 O0 量价 / 三通道合成一句进 `dz0`；或实验字母 DZ 与单字母 D/Z 或 params.Y/G/N 混读；或把占位读成确认钟时刻、切日日期、过户‰；或缺板块标记 / 官方规则仍不 skip；或重开假设-R / 假设-V / 假设-T / 假设-U / 假设-O / 假设-CK / 假设-DI / 假设-DL / 假设-DR / 假设-M / 假设-DY / 假设-DX / 假设-D / 假设-Z；或改 DY 正文/预检/复检；或标纸面齐；或写成 A/D–DZ纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 DZ0/DZ1/DZ2。日量与三通道走 O，能不能打满走 CK，费率走 DI 与 DL，盘后走 DR 与 M，申报带走 DY，基金收盘切日走 DX，假 T+0 走 R，费用走 V/T/U，开收时点走 D，保证金比例走 Z，都不改。报告确认窗误套截。不把 15:00–15:30、9:30–11:30、13:00–15:30 或 2026-07-06 标成占位门槛，锚已写死冻结。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_chinext_nego_block_confirm_as_intraday_pre_20260706` / `invent_asof_leak_chinext_block_confirm_intraday` / `copy_chinext_intraday_confirm_onto_sh_main` / `vs_O_block_liquidity` / `vs_CK_block_fill` / `vs_DI_block_fee` / `vs_DL_nego_transfer_fee` / `vs_DR_aft_pricing` / `vs_M_aft_channel` / `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `missing_board_or_official_rule_not_skip`

`invent_chinext_nego_block_confirm_as_intraday_pre_20260706` 才是写死冻结的单一主报名（单挂）。`invent_asof_leak_chinext_block_confirm_intraday` 只服务半泄露对照，**不得升格进 `dz0`，不得双挂**。自 `copy_chinext_intraday_confirm_onto_sh_main` 起至 `missing_board_or_official_rule_not_skip` **只作诊断桶**：它们不是 `dz0`，也不是 DZ1 主报，**不得升格主报，不得双挂**。**禁把 `copy_chinext_intraday_confirm_onto_sh_main` 倒铺沪主板 / 科创确认钟进主报**。没有「O 日量 + 本页确认窗」合成主报，也没有「CK 可成交 + 本页确认钟」合成主报，也没有「DI/DL 费率 + 本页确认钟」合成主报，也没有「DR/M 盘后 + 本页确认钟」合成主报。**实验 R 不抢**。**不重开假设-V / 假设-T / 假设-U**。**零改 DY**。**禁把 O/CK/DI/DL/DR/M/DY/DX/R/V/T/U 升格进 `dz0`**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「创业板协议大宗一直盘中确认」或「全板块确认钟都是 15:00–15:30」拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成实验字母 DZ，或当成单字母 D/Z，或当成证管费 0.02‰，或当成切日，或当成 15:00。**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**。**params 字母 ≠ 假设-T**。**params 字母 ≠ 假设-D**。
- 把 `params.G` 的 0.01 当成过户 0.01‰，或当成 9:30，或当成确认钟上的分钟。**params 字母 ≠ 假设-U**。**params 字母 ≠ 假设-V**。
- 把 `params.N` 的 0.05 当成实验字母 DZ 或单字母 D/Z。**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**。
- 把占位 `0.02/0.01/0.05/0.015` 读成确认钟时刻、切日日期、过户‰。**禁把占位读成确认钟时刻、切日日期、过户‰**。**params 相对门槛 ≠ 确认钟时刻 ≠ 切日日期 ≠ 过户‰**。**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**。
- 缺板块标记或官方规则仍不 skip。诊断桶 `missing_board_or_official_rule_not_skip` 只作对照，不得升格。
- 把核对日「已经是盘中确认」写成全历史规则，或铺到 2026-07-06 之前。锚六键已写死冻结。半泄露键 `invent_asof_leak_chinext_block_confirm_intraday` 不得与主报双挂。
- 把创业板盘中确认钟抄到沪主板，或把沪主板 15:00–15:30、科创开市起的盘中确认钟倒铺进主报。诊断桶 `copy_chinext_intraday_confirm_onto_sh_main` 只作对照，**禁进主报，禁双挂**。**禁止倒铺沪主板 / 科创确认钟进主报**。
- 把假设-O 的日量含大宗、三通道假流动性和本页确认窗合成后升格。**不重开假设-O**。诊断桶 `vs_O_block_liquidity` 只作对照。**禁与 O0 量价 / 三通道合成一句进 `dz0`**。
- 把假设-CK 的假全额可成和本页确认钟合成后升格。**不重开假设-CK**。诊断桶 `vs_CK_block_fill` 只作对照。
- 把假设-DI / 假设-DL 的费率和本页确认钟合成后升格。诊断桶 `vs_DI_block_fee` / `vs_DL_nego_transfer_fee` 只作对照。**不重开假设-DI**；**不重开假设-DL**。
- 把假设-DR / 假设-M 的盘后定价、盘后通道和本页协议大宗确认钟合成后升格。诊断桶 `vs_DR_aft_pricing` / `vs_M_aft_channel` 只作对照。**不重开假设-DR**；**不重开假设-M**。
- 把假设-DY 的核准制首日申报带、假设-DX 的基金收盘切日和本页合成后升格。**零改 DY**。**不重开假设-DY**；**不重开假设-DX**。诊断桶 `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` 只作对照。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格。**实验 R 不抢**。诊断桶 `vs_R_etf_t0` 只作对照。
- 把假设-V / 假设-T / 假设-U 和本页合成或混读后升格。诊断桶 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只作对照。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。
- 把假设-D 的开收时点、停牌和本页确认钟合成后升格。**双字母 DZ ≠ 单字母假设-D**。`fill_time=next_open` 不是确认钟。
- 把假设-Z 的融资保证金比例和本页确认钟合成后升格。**双字母 DZ ≠ 单字母假设-Z**。
- `dz0_primary_demo` 与 `invent_asof_leak_chinext_block_confirm_intraday` 双挂；DZ1 升格并列主报。
- 实验字母 DZ 与单字母 D/Z 或 params.Y/G/N 混读。**双字母 DZ ≠ 单字母 D/Z**。
- 改 DY / DX / O / CK / DI / DL / DR / M / R / V / T / U / D / Z 及其他已冻页正文；改 #110–#134；禁止标纸面齐；禁止写成 A/D–DZ纸面齐；预留 #136；开真数/回测/开户/实盘；用复权价当确认钟的判据；结论写成「这类大宗更能成交所以能买」。
- **纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–DY；勿再只改清单）。当前禁止标纸面齐。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权路径、交易日、**板块标记**（创业板 / 沪市主板 / 科创板 / 其他）。板块分不清则 skip，不把创业板切日套到沪主板或科创，也不把沪主板、科创的确认钟套回创业板。
- 官方规则是否在册：创业板协议大宗确认窗的切日（建议方向：`<2026-07-06` 为 15:00–15:30，`≥2026-07-06` 为 9:30–11:30、13:00–15:30）。规则不在册则 skip，不用占位数字去填一个钟点或一个日期。
- 申报要能分清是**协议大宗的成交确认**，还是竞价、盘后固定价格、深市盘后定价大宗、沪市大宗固定价格申报。后四类不进本页主报；三通道的拆分走 O。
- 确认时刻字段：这笔在切日之前应落在 15:00–15:30，切日当天及之后应落在 9:30–11:30 或 13:00–15:30。只有一根日 K、没有确认钟，不要默认「按盘中放行」，也不要默认「全日都等到 15:00」。
- 旁路消费：O 的日量与三通道、CK 的可成交性、DI 的大宗经手、DL 的协议过户费、DR 的盘后定价、M 的盘后通道、DY 的核准制申报带、DX 的基金收盘切日、R 的假 T+0、V/T/U 的费用、D 的成交时点、Z 的保证金比例（见 §2.1 handoff）。**本页不改写这些页。零改 DY。**
- 未复权路径；asof **写死冻结** `2026-10-23`。核对日在切日之后，所以「核对日当天创业板协议大宗已经盘中确认」不能倒灌到 2026-07-06 之前。`事实与坑` 2026-10-23 是方向来源，不是已冻的全历史规则。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-23`；`fail_policy=skip`；`chinext_block_confirm_honest=pit_pre_20260706_1500_1530_else_intraday`；`chinext_block_confirm_scope=chinext_nego_block_confirm_window_only`；`chinext_block_confirm_over_policy=skip_if_board_or_official_rule_missing`；`dz0_primary_demo=invent_chinext_nego_block_confirm_as_intraday_pre_20260706`（**写死冻结**单一主报，单挂写死；禁与 `invent_asof_leak_chinext_block_confirm_intraday` 双挂；DZ1 不升格；诊断桶不升格；**禁止倒铺沪主板 / 科创确认钟进主报**；**禁与 O0 量价 / 三通道合成一句进 `dz0`**；**禁把 O/CK/DI/DL/DR/M/DY/DX/R/V/T/U 升格进 `dz0`**）；`block_liquidity_handoff=o_page`；`block_fill_handoff=ck_page`；`block_fee_handoff=di_page`；`nego_transfer_fee_handoff=dl_page`；`aft_pricing_handoff=dr_page`；`aft_channel_handoff=m_page`；`approval_ipo_band_handoff=dy_page`；`sse_fund_close_handoff=dx_page`；`etf_t0_handoff=r_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；`merge_with_DY/DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/Y/A/D/Z=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是确认钟时刻，不是切日日期，不是核对日，不是过户费率，不是证管费；**params.Y/G/N ≠ 实验字母 DZ ≠ 单字母 D/Z**；**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**；**尤重 params.Y 的 0.02 ≠ 实验字母 DZ ≠ 单字母 D/Z ≠ 确认钟时刻 ≠ 切日日期 ≠ 核对日 ≠ 证管费 0.02‰**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 确认钟时刻 ≠ 切日日期**；**禁把占位读成确认钟时刻、切日日期、过户‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #136。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`55056e0`（A/D–DY纸面齐已合，全长 `55056e05d55f90b6a9029c56969795d733fab638`）；三冻补丁基 tip=`4641b626` / `4641b626c7bc5c8b3c9ff61a26be962e29853f85`；分支起点 HEAD=`020c5f72` / `020c5f7243bf47a9eb3df998811a1188d73fd2c7`。**不改已冻 A–DQ / DA–DY**。**零改 DY**。**不改 #110–#134**。状态=**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DZ纸面齐**。

---

## 8. 结论

（空；**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DZ纸面齐**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-12-06）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DZ-20261110.md`（原样落入，不改结论；SHA256=`cb5fdce13c7c09634cc20f41bfaf9ece92f438d01a40cabe709fa93171cab9c6`；预检 2026-11-10；**结论：有条件通过**；tip基=`4641b626` / `4641b626c7bc5c8b3c9ff61a26be962e29853f85`；本补丁分支起点 HEAD=`020c5f72` / `020c5f7243bf47a9eb3df998811a1188d73fd2c7`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于确认窗误套截 ΔChinextBlockConfirm、净差异、DZ1−DZ2 专项。**`params.Y` ≠ 实验字母 DZ**；**`params.G` ≠ 实验字母 DZ**；**`params.N` ≠ 实验字母 DZ**；亦 ≠ 单字母假设-D / 假设-Z。**params.Y/G/N ≠ 实验字母 DZ ≠ 单字母 D/Z**。**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**。**勿把 `params.Y` 读成实验字母 DZ，亦勿读成单字母假设-D，亦勿读成单字母假设-Z，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿把 `params.G` 读成假设-U，亦勿把单字母假设-D / 假设-Z 读成双字母 DZ**。**尤重：`params.G` 的 `0.01` ≠ 过户 0.01‰ ≠ 确认钟时刻 ≠ 切日日期**（**params.G=`0.01` ≠ 过户‰ ≠ 确认钟**）。量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户 0.01‰，也不是 15:00，也不是 9:30，也不是 2026-07-06。**尤重：`params.Y` 的 `0.02` ≠ 证管费 0.02‰ ≠ 切日日期 ≠ 核对日 ≠ 实验字母 DZ**（**params.Y=`0.02` ≠ 证管费‰ ≠ 切日/核对日**）。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**。**禁把占位读成确认钟时刻、切日日期、过户‰**。**params 相对门槛 ≠ 确认钟时刻 ≠ 切日日期 ≠ 过户‰**。禁止互读、禁止把门槛改写成确认钟时刻、切日日期、核对日、过户费率或证管费。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dz0_primary_demo`**：**写死冻结** **`invent_chinext_nego_block_confirm_as_intraday_pre_20260706`**（单一主报，单挂写死）。**禁止**与半泄露键 **`invent_asof_leak_chinext_block_confirm_intraday`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DZ1 仅核对日把「创业板协议大宗确认已经是盘中」铺到全历史、铺到 2026-07-06 之前、或铺到沪主板 / 科创，只作半泄露对照，**不得升格与 dz0 并列主报**，也不得把 `invent_asof_leak_chinext_block_confirm_intraday` 写进 `dz0`。`copy_chinext_intraday_confirm_onto_sh_main` / `vs_O_block_liquidity` / `vs_CK_block_fill` / `vs_DI_block_fee` / `vs_DL_nego_transfer_fee` / `vs_DR_aft_pricing` / `vs_M_aft_channel` / `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `missing_board_or_official_rule_not_skip` **只作诊断桶，不得升格主报**。DZ1 / 诊断桶 **不升格**。**禁把以下升格进 dz0**：O日量含大宗/三通道假流动性 / CK假全额可成 / DI大宗费率 / DL协议过户费率 / DR盘后定价 / M盘后通道 / DY核准制申报带 / DX沪市基金收盘切日 / R假T+0 / V印花 / T证管费 / U过户 / 倒铺沪主板或科创确认钟 / 与 O0 量价三通道合成一句。这些只作对照/旁路，**不得升格进 `dz0`，不得另挂主报**。**零改 DY**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**不抢实验 R**。**双字母 DZ ≠ 单字母假设-D / 假设-Z**。**双字母 DZ ≠ 单字母 D/Z**。

3. **创业板协议大宗确认窗诚实锚六键升格写死（不可再写「建议」）**：`params.chinext_block_confirm_honest=pit_pre_20260706_1500_1530_else_intraday`；`params.chinext_block_confirm_scope=chinext_nego_block_confirm_window_only`；`params.chinext_block_confirm_over_policy=skip_if_board_or_official_rule_missing`；`params.asof_check_date=2026-10-23`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺板块标记 / 官方规则 → skip；创业板协议大宗确认 `<2026-07-06` → 15:00–15:30，`≥2026-07-06` → 9:30–11:30、13:00–15:30。禁止倒铺沪主板 / 科创确认钟进主报。禁止与 O0 量价 / 三通道合成一句。禁止跑后改锚，或用盘中 / 核对日规则铺满 / 倒铺沪主板或科创确认钟 / 与 O0 合成一句 / 缺板块标记或官方规则仍硬填 / 把 O/CK/DI/DL/DR/M/DY/DX/R/V/T/U 升格进 dz0 冒充诚实 PIT。**禁把占位读成确认钟时刻、切日日期、过户‰**。**禁把 params.G 的 0.01 读成过户 0.01‰ 或确认钟**。**禁把 params.Y 的 0.02 读成证管费 0.02‰ 或切日日期或核对日或实验字母 DZ**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**零改 DY**。**不抢实验 R**。

**硬分列保住**：DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z；**双字母 DZ ≠ 单字母假设-D / 假设-Z**；**双字母 DZ ≠ 单字母 D/Z**；**params.Y / params.G / params.N ≠ 实验字母 DZ ≠ 单字母 D/Z**；**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 确认钟时刻 ≠ 切日日期**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期 ≠ 核对日**；**禁把占位读成确认钟时刻、切日日期、过户‰**；**params 相对门槛 ≠ 确认钟时刻 ≠ 切日日期 ≠ 过户‰**；**创业板协议大宗确认窗切日 ≠ O日量含大宗/三通道假流动性 ≠ CK假全额可成 ≠ DI/DL费率 ≠ DR盘后定价 ≠ M盘后通道 ≠ DY核准制申报带 ≠ DX沪市基金收盘切日 ≠ R假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ D成交时点 ≠ Z融资保证金比例**；不抢 A；不抢实验 R；不改已齐/已冻 DA～DY 及 A–DQ 正文；**零改 DY**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-O**；**不重开假设-CK**；**不重开假设-DI**；**不重开假设-DL**；**不重开假设-DR**；**不重开假设-M**；**不重开假设-DY**；**不重开假设-DX**；**不重开假设-D**；**不重开假设-Z**；**不重开假设-R**；**禁把 O日量含大宗/三通道假流动性 / CK假全额可成 / DI大宗费率 / DL协议过户费率 / DR盘后定价 / M盘后通道 / DY核准制申报带 / DX沪市基金收盘切日 / R假T+0 / V印花 / T证管费 / U过户 / 倒铺沪主板或科创确认钟 / 与 O0 量价三通道合成一句 合成/混读升格进 dz0**。handoff 保持：`block_liquidity_handoff=o_page`；`block_fill_handoff=ck_page`；`block_fee_handoff=di_page`；`nego_transfer_fee_handoff=dl_page`；`aft_pricing_handoff=dr_page`；`aft_channel_handoff=m_page`；`approval_ipo_band_handoff=dy_page`；`sse_fund_close_handoff=dx_page`；`etf_t0_handoff=r_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；全部 `merge_with_*=False`。

**状态**：**预检有条件通过·三条已冻·待复检**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DZ纸面齐**；本页不开回测/真数/开户/实盘。

## 变更
| 日期 | 变更 |
|------|------|
| 2026-12-06 | 风控预检补丁·冻结三条写死——依据 `预检-假设DZ-20261110.md`（SHA256=`cb5fdce13c7c09634cc20f41bfaf9ece92f438d01a40cabe709fa93171cab9c6`；结论=有条件通过；tip基=`4641b626` / `4641b626c7bc5c8b3c9ff61a26be962e29853f85`；分支起点 HEAD=`020c5f72` / `020c5f7243bf47a9eb3df998811a1188d73fd2c7`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖确认窗误套截 ΔChinextBlockConfirm / 净差异 / DZ1−DZ2；**params.Y/G/N ≠ 实验字母 DZ ≠ 单字母 D/Z**；**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**；**勿把 params.Y 读成实验字母 DZ 或单字母假设-D 或单字母假设-Z 或假设-V 或假设-T 或假设-U，亦勿把 params.G 读成假设-U，亦勿把单字母假设-D / 假设-Z 读成双字母 DZ**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-Z / 假设-D**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 确认钟时刻 ≠ 切日日期（量纲与语义不同）**；**params.G=`0.01` ≠ 过户‰ ≠ 确认钟**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 切日日期 ≠ 核对日 ≠ 实验字母 DZ**；**params.Y=`0.02` ≠ 证管费‰ ≠ 切日/核对日**；**禁把占位读成确认钟时刻、切日日期、过户‰**；**params 相对门槛 ≠ 确认钟时刻 ≠ 切日日期 ≠ 过户‰**；禁 null；禁 holdout/OOS 标定）；② `params.dz0_primary_demo=invent_chinext_nego_block_confirm_as_intraday_pre_20260706`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_chinext_block_confirm_intraday` 双挂；DZ1 不升格；诊断桶 `copy_chinext_intraday_confirm_onto_sh_main` / `vs_O_block_liquidity` / `vs_CK_block_fill` / `vs_DI_block_fee` / `vs_DL_nego_transfer_fee` / `vs_DR_aft_pricing` / `vs_M_aft_channel` / `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `missing_board_or_official_rule_not_skip` 不升格；**禁把 O日量含大宗/三通道假流动性 / CK假全额可成 / DI大宗费率 / DL协议过户费率 / DR盘后定价 / M盘后通道 / DY核准制申报带 / DX沪市基金收盘切日 / R假T+0 / V印花 / T证管费 / U过户 / 倒铺沪主板或科创确认钟 / 与 O0 量价三通道合成一句 合成/混读升格进 dz0**，只作对照/旁路，不得升格进 dz0 或另挂主报；**零改 DY**；不重开假设-V；不重开假设-T；不重开假设-U；不抢实验 R；**双字母 DZ ≠ 单字母假设-D / 假设-Z**）；③ 锚六键写死 `chinext_block_confirm_honest=pit_pre_20260706_1500_1530_else_intraday` / `chinext_block_confirm_scope=chinext_nego_block_confirm_window_only` / `chinext_block_confirm_over_policy=skip_if_board_or_official_rule_missing` / `asof_check_date=2026-10-23` / `fill_time=next_open` / `fail_policy=skip`（缺板块标记/官方规则 → skip；创业板协议大宗确认 `<2026-07-06`→15:00–15:30，`≥2026-07-06`→9:30–11:30、13:00–15:30；禁止倒铺沪主板/科创确认钟进主报；禁止与 O0 量价/三通道合成一句）。handoff 保持 `block_liquidity_handoff=o_page` / `block_fill_handoff=ck_page` / `block_fee_handoff=di_page` / `nego_transfer_fee_handoff=dl_page` / `aft_pricing_handoff=dr_page` / `aft_channel_handoff=m_page` / `approval_ipo_band_handoff=dy_page` / `sse_fund_close_handoff=dx_page` / `etf_t0_handoff=r_page` / `stamp_handoff=v_page` / `csrc_fee_handoff=t_page` / `transfer_fee_handoff=u_page`；全部 `merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DZ纸面齐**；不改已齐/已冻 DA～DY 及 A–DQ；**零改 DY**；不改 #110–#134；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-R；不重开假设-O；不重开假设-CK；不重开假设-DI；不重开假设-DL；不重开假设-DR；不重开假设-M；不重开假设-DY；不重开假设-DX；不重开假设-D；不重开假设-Z；不抢实验 R；不预留 #136；不开回测/真数/开户/实盘。基于 tip=`4641b626`。 |
| 2026-12-06 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。创业板协议大宗确认时点切日误套（成交规则）；`dz0_primary_demo` 建议 `invent_chinext_nego_block_confirm_as_intraday_pre_20260706`，单一主报，单挂，禁与 `invent_asof_leak_chinext_block_confirm_intraday` 双挂，DZ1 不升格；诊断桶 `copy_chinext_intraday_confirm_onto_sh_main` / `vs_O_block_liquidity` / `vs_CK_block_fill` / `vs_DI_block_fee` / `vs_DL_nego_transfer_fee` / `vs_DR_aft_pricing` / `vs_M_aft_channel` / `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `missing_board_or_official_rule_not_skip` 不升格；**尤重实验 R 不抢，禁把 vs_R_etf_t0 升格进 dz0**；**尤重不重开假设-V / 假设-T / 假设-U，禁把 vs_V_stamp / vs_T_csrc / vs_U_transfer 升格进 dz0**；**尤重 O=日量含大宗/三通道假流动性 ≠ 本页仅创业板确认窗切日，禁把 vs_O_block_liquidity 升格，禁与 O0 量价/三通道合成一句进 dz0**；**尤重 CK 假全额可成 ≠ 本页确认钟，禁把 vs_CK_block_fill 升格**；**尤重 DI/DL 费率 ≠ 本页确认钟，禁把 vs_DI_block_fee / vs_DL_nego_transfer_fee 升格**；**尤重 DR/M 盘后定价/盘后通道 ≠ 本页协议大宗确认钟，禁把 vs_DR_aft_pricing / vs_M_aft_channel 升格**；**尤重双字母 DZ ≠ 单字母假设-D / 假设-Z**；**尤重 params.Y/G/N ≠ 实验字母 DZ / 单字母 D/Z**；**尤重禁 copy_chinext_intraday_confirm_onto_sh_main 倒铺沪主板/科创确认钟进主报**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U**；**禁把占位读成确认钟时刻、切日日期、过户‰**；**禁把 DY/DX 升格进 dz0**；**零改 DY**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DZ ≠ 单字母 D/Z**；锚建议·待冻、未冻：`chinext_block_confirm_honest=pit_pre_20260706_1500_1530_else_intraday` / scope=`chinext_nego_block_confirm_window_only` / over_policy=`skip_if_board_or_official_rule_missing` / `asof_check_date=2026-10-23` / `fill_time=next_open` / `fail_policy=skip`；口径：缺板块标记/官方规则则 skip；创业板协议大宗确认 `<2026-07-06`→15:00–15:30，`≥2026-07-06`→9:30–11:30、13:00–15:30；禁止倒铺沪主板/科创确认钟进主报；禁止与 O0 量价/三通道合成一句（**草稿方向，尚未冻，不要写成已冻**）；handoff：`block_liquidity_handoff=o_page`，`block_fill_handoff=ck_page`，`block_fee_handoff=di_page`，`nego_transfer_fee_handoff=dl_page`，`aft_pricing_handoff=dr_page`，`aft_channel_handoff=m_page`，`approval_ipo_band_handoff=dy_page`，`sse_fund_close_handoff=dx_page`，`etf_t0_handoff=r_page`，`stamp_handoff=v_page`，`csrc_fee_handoff=t_page`，`transfer_fee_handoff=u_page`；`merge_with_DY/DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/Y/A/D/Z=False`；**DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z**；**双字母 DZ ≠ 单字母 D/Z**；**未标纸面齐**；**不写 A/D–DZ纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–DY；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–DY；**零改 DY**；不改 #110–#134；不重开假设-R；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-O；不重开假设-CK；不重开假设-DI；不重开假设-DL；不重开假设-DR；不重开假设-M；不重开假设-DY；不重开假设-DX；不重开假设-D；不重开假设-Z；不写下一字母；不预留 #136；不开真数/回测/开户/实盘。基 tip=`55056e0`（A/D–DY纸面齐已合，全长 `55056e05d55f90b6a9029c56969795d733fab638`；不改该 tip 上的 #110–#134，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
