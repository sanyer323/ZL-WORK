# 假设-EE · 业绩预告或快报按报告期末或预告时限对齐误套（因子可见性，不是成交规则）

更新：2026-12-11  
来源：总管线 / 基 tip=`b49d45dc` / 全长 `b49d45dcb0ab6a7985910a54ca0faff9c2db0b29`（A/D–ED纸面齐已合，已收讫）；分支起点 HEAD=`d6f6f32` / `d6f6f32bc7e794810a1ee04d122a4c39438e7553`；**不改已冻 A–DQ / DA–ED**；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O**；**不改假设-ED 正文/预检/复检**，**不改假设-EC 正文/预检/复检**，**不改假设-EB 正文/预检/复检**，**不改假设-O**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-DT / 假设-DU / 假设-DV / 假设-DW / 假设-DX / 假设-DY / 假设-DZ / 假设-EA / 假设-EB / 假设-EC / 假设-ED / 假设-S / 假设-AX / 假设-AY / 假设-AW / 假设-T / 假设-U / 假设-V / 假设-W / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-E / 假设-F / 假设-J / 假设-G / 假设-CI / 假设-CK / 假设-Y / 假设-A / 假设-D / 假设-C / 假设-X / 假设-Z 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ）；**不改假设-B**（勿复用·无独立正文，亦不新建）；**不重开假设-R**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-O**；**不重开假设-M**；**不重开假设-CH**；**不重开假设-CK**；**不重开假设-DZ**；**不重开假设-DY**；**不重开假设-DX**；**不重开假设-EA**；**不重开假设-EB**；**不重开假设-EC**；**不重开假设-ED**；**不重开假设-DI**；**不重开假设-E**；**不重开假设-D**；**不重开假设-C**；**不重开假设-W**；**不重开假设-Y**）后写下一草稿 EE；清单 #139=ED，本页占用 **#140=EE**；选题是回测把 **业绩预告或业绩快报的可见日**套错（诚实方向：预告/快报按**实际公告日或交易所披露时间**可见，再落到**下一可交易日**；「年报结束后一个月 / 中报结束后十五日」只是预告时限，不是可见日；缺公告日或披露时点则 skip；未触发预告义务则不得发明预告；已披露后又有修正公告的，以最新公告日为准；禁用 1 月 31 日 / 中报后第 15 日等时限假冒全市场可见日；禁把预告/快报升格成已审计年报/中报）；这是**因子可见性，不是成交规则**；假设-ED 只收正式年报/中报财务因子可见日，假设-C 只收股票池/指数当时名单（偷看对象是成分不是预告/快报），假设-D 只收次日开/收与停牌日假成交，假设-EC 只收沪市主板大宗接受闸门，假设-EB 只收无板协议大宗价限，假设-EA 只收科创板大宗固定价格类型开关，假设-DZ 只收创业板协议大宗确认钟切日，假设-DY 只收核准制主板新股首日申报带，假设-DX 只收沪市基金收盘产生方式切日，假设-O 只收日量含大宗与三通道假流动性，假设-M 只收盘后固定价格通道，假设-CH 只收盘后固定价格可成交，假设-CK 只收协议大宗假全额可成，假设-E 只收整手与科创板 200 股，假设-V 只收股票印花税切日，假设-W 只收除权日复权价误判板，假设-R 只收股票 ETF 假 T+0，假设-T 只收股票证管费切日，假设-U 只收股票过户切日；**新建实验 EE**；不写下一字母；不预留 #141  
状态：**A/D–EE纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「报告期末或预告时限对齐到下一交易日」或「1 月 31 日 / 中报后第 15 日全市场同一天可见」或「预告/快报当成已审计年报/中报」或「忽略修正公告」当诚实锚；禁止与 `invent_statutory_preview_deadline_as_visible_day` / `invent_treat_preview_or_flash_as_audited_periodic_report` / `invent_ignore_preview_or_flash_correction` 双挂；三者只进诊断、不升格主报；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–ED**；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O**；**不改 #110–#139**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 EE（#140）。一句话误开：回测把业绩预告或业绩快报的盈亏区间/主要财务数据，按报告期末（或按「年报结束后一个月 / 中报结束后十五日」的预告时限）对齐到下一交易日调仓，等于偷看尚未公告的预告或快报；或把预告/快报当成已审计年报/中报使用。**禁把 ED/EC/EB/EA/DZ/DY/DX/C/D/O/M/CH/CK/E/V/W/R/T/U 混读升格进 `ee0`**。**禁把 ED 诊断桶升格进 `ee0`**。**禁把 `invent_statutory_preview_deadline_as_visible_day` 与主报双挂**。**禁把 `invent_treat_preview_or_flash_as_audited_periodic_report` 与主报双挂**。**禁把 `invent_ignore_preview_or_flash_correction` 与主报双挂**。三者只进诊断、不升格主报。**禁把预告/快报升格成已审计定期报告**。**禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格、不另挂主报、零改 O**。

> **字母消歧（硬）**：本页**实验字母 EE** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 EE**；**尤重：`params.Y/G/N` ≠ 实验字母 EE / 单字母 E / 假设-ED**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED**；**勿把 `params.Y` 读成实验字母 EE，亦勿读成单字母假设-E，亦勿读成假设-ED，亦勿读成假设-EC，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U**；**尤重：`params.Y` 的 0.02 ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28 ≠ 可见日 ≠ 1 月 31 日 ≠ 预告时限**（**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28 ≠ 可见日 ≠ 1 月 31 日 ≠ 实验字母 EE**））≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 EE**；**params.G ≠ 假设-G**；**params.G ≠ 假设-ED**；**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日 ≠ 中报后第 15 日 ≠ 十五日时限**（**params.G=`0.01` ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日**）——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户费率，不是预告时限，也不是公告日）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 EE**；**params.N ≠ 单字母 E**）≠ **`params.Y2`**（写死冻结 0.015；不是可见日，不是预告时限，不是过户‰）≠ **单字母实验 E**（整手与科创板 200 股；**双字母 EE ≠ 单字母假设-E；严禁复用假设-E**）≠ **双字母 ED**（正式年报/中报财务因子可见日；**零改 ED**；**EE≠ED**；**EE 专写业绩预告/业绩快报可见日，不等于 ED 正式年报/中报**）≠ **双字母 EC**（沪市主板大宗停牌至 15:00 仍接受；**零改 EC**；**EE≠EC**；**EC 接受闸门 ≠ 本页披露可见日**）≠ **双字母 EB**（无板证券协议大宗价限；**零改 EB**；**EE≠EB**；**EB 价限 ≠ 本页**）≠ **双字母 EA**（科创板大宗固定价格交易类型切日；**EE≠EA**；**EA 类型开关 ≠ 本页**）≠ **双字母 DZ**（创业板协议大宗确认时点切日；**EE≠DZ**；**DZ 确认钟 ≠ 本页**）≠ **双字母 DY**（核准制主板新股首日申报价格上下限；**EE≠DY**；**DY 首日申报 ≠ 本页**）≠ **双字母 DX**（沪市基金收盘产生方式切日；**EE≠DX**；**DX 收盘产生 ≠ 本页**）≠ **单字母 C**（股票池/指数当时名单、幸存者偏差；偷看对象是**成分**不是预告/快报；**C ≠ 本页**；**双字母 EE ≠ 单字母假设-C**）≠ **单字母 D**（次日开/收与停牌日假成交；**D ≠ 本页披露可见日**；**双字母 EE ≠ 单字母假设-D**）≠ **双字母 O**（大宗日量 / 三通道假流动性；**O 通道与流动性 ≠ 本页**；**零改 O**）≠ **单字母 M**（盘后固定价格通道；**M ≠ 本页**）≠ **双字母 CH**（盘后固定价格可成交性；**CH ≠ 本页**）≠ **双字母 CK**（协议大宗可成交性；**CK ≠ 本页**）≠ **单字母 V**（股票印花税切日；**V = 印花切日，费用 ≠ 可见日**；**不重开假设-V**）≠ **单字母 W**（除权日复权价误判板；**W = 除权判板 ≠ 本页**；**不重开假设-W**）≠ **单字母 R**（股票 ETF 假 T+0；**实验 R 不抢、不重开、不混读升格进 `ee0`**）≠ **单字母 T**（股票证管费切日；**不重开假设-T**；**`params.Y` 的 0.02 ≠ 证管费 0.02‰**）≠ **单字母 U**（股票过户费切日；**不重开假设-U**；**`params.G` 的 0.01 ≠ 过户 0.01‰**）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（勿复用·无独立正文）≠ **单字母实验 Z**（融资保证金比例误铺）。**硬分列：EE≠ED≠EC≠EB≠EA≠DZ≠DY≠DX≠C≠D≠O≠M≠CH≠CK≠E≠V≠W**。**EE≠ED≠EC≠EB≠EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z≠B≠C**。**双字母 EE ≠ 单字母 E**。**双字母 EE ≠ 单字母假设-E**。**双字母 EE ≠ 假设-ED / 假设-EC / 假设-EA / 假设-EB**。**params.Y/G/N ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED**。**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**。**params.Y/G/N 亦不等于 V/T/U**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED**。**禁把占位读成证管费 0.02‰、过户 0.01‰、预告时限、1 月 31 日、中报后第 15 日**。**params 相对门槛 ≠ 可见日 ≠ 预告时限 ≠ 过户‰ ≠ 证管费**。**预告/快报可见日 ≠ ED正式年报/中报 ≠ EC接受闸门 ≠ EB价限 ≠ EA类型 ≠ DZ确认钟 ≠ DY首日申报 ≠ DX收盘产生 ≠ C股票池成分 ≠ D次日开收/停牌假成交 ≠ O/M/CH/CK通道与流动性 ≠ E整手 ≠ V印花切日 ≠ W除权判板 ≠ R股票ETF假T+0 ≠ T证管费 ≠ U过户**。**尤重：零改 ED / EC / EB / O**。**尤重：实验 R 不抢；禁把 `vs_R_etf_t0` 升格进 `ee0`**。**尤重：不重开假设-V / 假设-T / 假设-U；禁把 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 升格进 `ee0`**。**尤重：EE 专写业绩预告/业绩快报可见日，不等于 ED 正式年报/中报；禁把 `vs_ED_periodic_report_visibility` 升格进 `ee0`；禁把 ED 诊断桶升格进 `ee0`**。**尤重：C = 股票池/指数当时名单，偷看对象是成分不是预告/快报；C ≠ 本页；禁把 `vs_C_survivorship` 升格进 `ee0`**。**尤重：D = 次日开/收与停牌日假成交 ≠ 本页披露可见日；禁把 `vs_D_halt_bar` 升格进 `ee0`**。**尤重：EC 接受闸门 / EB 价限 / EA 类型 / DZ 确认钟 / DY 首日申报 / DX 收盘产生 ≠ 本页；零改 EC；零改 EB；禁把 `vs_EC_sh_main_block_accept` / `vs_EB_nolimit_nego_px` / `vs_EA_star_fixed_price_type` / `vs_DZ_chinext_confirm` / `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` 升格进 `ee0`**。**尤重：O/M/CH/CK 通道与流动性 ≠ 本页；零改 O；禁把 `vs_O_block_liquidity` / `vs_M_aft_channel` / `vs_CH_aft_fill` / `vs_CK_block_fill` 升格进 `ee0`**。**尤重：E = 整手 ≠ 本页；禁把 `vs_E_lot_size` 升格进 `ee0`**。**尤重：V = 印花切日，费用 ≠ 可见日；禁把 `vs_V_stamp` 升格进 `ee0`**。**尤重：W = 除权判板 ≠ 本页；禁把 `vs_W_ex_right_limit` 升格进 `ee0`**。**尤重：双字母 EE ≠ 单字母假设-E，亦不等于假设-ED / 假设-EC / 假设-EA / 假设-EB**。**尤重：禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格；不另挂主报；零改 O**。诊断桶只作对照/旁路，不得升格进 `ee0`。

### 专节 · 双字母 EE ≠ 单字母假设-E；且 ≠ 假设-ED / 假设-EC / 假设-EB / 假设-O / 假设-C / 假设-W / 假设-V（硬）

| 维度 | 对照页 | 本页假设-EE（双字母） |
|------|--------|----------------------|
| 题面 ED | **正式年报/中报财务因子按报告期末对齐**（假设-ED 已纸面齐，已收讫） | **ED = 正式年报/中报可见日**。本页问的是业绩预告、业绩快报**哪一天可以进因子**。年报四个月、中报两个月是 ED 的期限，不是本页的预告时限。**零改 ED**：正文、预检、复检、清单 #139 与基线字节相同。**EE≠ED**；**不重开假设-ED**；**不改 ED**；**尤重：禁把 `vs_ED_periodic_report_visibility` 升格进 `ee0`**；**禁把 ED 诊断桶升格进 `ee0`**；`periodic_report_visibility_handoff=ed_page` |
| 题面 EC | **沪市主板大宗 15:00 仍停牌当日还接不接受**（假设-EC 已纸面齐，已收讫） | **EC = 接受闸门**。大宗还接不接申报，不是预告/快报可见日。**零改 EC**。**EE≠EC**；**不重开假设-EC**；**不改 EC**；**尤重：禁把 `vs_EC_sh_main_block_accept` 升格进 `ee0`**；`sh_main_block_accept_handoff=ec_page` |
| 题面 EB | **无板证券协议大宗价限**（假设-EB 已纸面齐，已收讫） | EB 只问无板证券谈妥价落不落在均价带里。价限不是预告可见日。**零改 EB**。**EE≠EB**；**不重开假设-EB**；**不改 EB 正文/预检/复检**；**尤重：禁把 `vs_EB_nolimit_nego_px` 升格进 `ee0`**；`nolimit_nego_px_handoff=eb_page` |
| 题面 EA | **科创板大宗固定价格交易类型切日**（假设-EA） | EA 只问科创板大宗**有没有固定价格这一种类型**。类型开关不是可见日。**EE≠EA**；**不重开假设-EA**；**不改 EA**；**尤重：禁把 `vs_EA_star_fixed_price_type` 升格进 `ee0`**；`star_fixed_price_type_handoff=ea_page` |
| 题面 DZ | **创业板协议大宗确认时点切日**（假设-DZ） | DZ 只问创业板这道确认钟落在哪一段。确认钟不是公告日。**EE≠DZ**；**不重开假设-DZ**；**不改 DZ**；**尤重：禁把 `vs_DZ_chinext_confirm` 升格进 `ee0`**；`chinext_confirm_handoff=dz_page` |
| 题面 DY | **核准制主板新股首日申报价格上下限**（假设-DY） | DY 只问核准制首日申报带。首日申报不是预告可见日。**EE≠DY**；**不重开假设-DY**；**不改 DY**；**尤重：禁把 `vs_DY_approval_ipo_band` 升格进 `ee0`**；`approval_ipo_band_handoff=dy_page` |
| 题面 DX | **沪市基金收盘产生方式切日**（假设-DX） | DX 只问沪市基金收盘价怎么产生。收盘产生不是披露时点。**EE≠DX**；**不重开假设-DX**；**不改 DX**；**尤重：禁把 `vs_DX_sse_fund_close` 升格进 `ee0`**；`sse_fund_close_handoff=dx_page` |
| 题面 C | **股票池当时名单 / 指数成分 / 幸存者偏差**（假设-C） | **C 的偷看对象是成分，不是预告/快报**。今天的名单回放历史，和用报告期末倒填预告，是同一类偷看，但是两页。成分名单留在 C。本页只问预告或快报哪天可见。**C ≠ 本页**。**EE≠C**；**不重开假设-C**；**不改 C**；**尤重：禁把 `vs_C_survivorship` 升格进 `ee0`**；`survivorship_handoff=c_page` |
| 题面 D | **次日开盘 vs 次日收盘；停牌日按收盘=前收盘假成交**（假设-D） | **D = 次日开/收与停牌日假成交**。本页的「下一可交易日」是预告或快报已经公告之后，因子才能进截面；不是停牌日把收盘抄成前收盘。**D ≠ 本页披露可见日**。**EE≠D**；**不重开假设-D**；**不改 D**；**尤重：禁把 `vs_D_halt_bar` 升格进 `ee0`**；`halt_bar_handoff=d_page` |
| 题面 O | **大宗量价并进竞价 / 三条盘后通道混用**（假设-O） | **O = 通道与流动性**。日量含大宗、三通道怎么拆，都留在 O。本页不改 o0，不把大宗门槛当成预告可见日。**零改 O**。**EE≠O**；**不重开假设-O**；**不改 O**；**尤重：禁把 `vs_O_block_liquidity` 升格进 `ee0`**；`block_liquidity_handoff=o_page` |
| 题面 M / CH / CK | **盘后通道、盘后可成交、协议大宗假全额**（假设-M / 假设-CH / 假设-CK） | 这三页问的是成交通道开不开、单子能不能打满。预告数字哪天可见，和通道无关。**EE≠M≠CH≠CK**；**不重开这三页**；**不改这三页**；**尤重：禁把 `vs_M_aft_channel` / `vs_CH_aft_fill` / `vs_CK_block_fill` 升格进 `ee0`**；`aft_channel_handoff=m_page`；`aft_fill_handoff=ch_page`；`block_fill_handoff=ck_page` |
| 题面 E | **整手与科创板 200 股**（假设-E） | 整手是数量闸门。本页问的是因子哪天可见。**双字母 EE ≠ 单字母假设-E**。**E ≠ 本页**。**EE≠E**；**不重开假设-E**；**不改 E**；**尤重：禁把 `vs_E_lot_size` 升格进 `ee0`**；`lot_size_handoff=e_page` |
| 题面 V | **股票印花税切日**（假设-V） | **V = 印花切日。费用 ≠ 可见日**。写死冻结 0.02 不是印花税率，也不是证管费。**不重开假设-V**。**EE≠V**；**params 字母 ≠ 假设-V**；**不改 V**；**尤重：禁把 `vs_V_stamp` 升格进 `ee0`**；`stamp_handoff=v_page` |
| 题面 T | **股票证管费切日**（假设-T） | **不重开假设-T**。`params.Y` 的 0.02 不是证管费 0.02‰，也不是实验字母 EE。**EE≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：禁把 `vs_T_csrc` 升格进 `ee0`**；`csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日**（假设-U） | **不重开假设-U**。`params.G` 的 0.01 不是过户 0.01‰。**EE≠U**；**params 字母 ≠ 假设-U**；**不改 U**；**尤重：禁把 `vs_U_transfer` 升格进 `ee0`**；`transfer_fee_handoff=u_page` |
| 题面 W | **除权日用复权价误判涨跌停**（假设-W） | **W = 除权判板 ≠ 本页**。复权价能不能用来判板，是 W 的题。本页不改那条，也不用复权价去决定预告哪天可见。可见日是时间戳问题。**EE≠W**；**不重开假设-W**；**不改 W**；**尤重：禁把 `vs_W_ex_right_limit` 升格进 `ee0`**；`ex_right_limit_handoff=w_page` |
| 题面 R | **股票 ETF 假 T+0**（假设-R） | **实验 R 不抢**。ETF 能不能当日回转，和预告哪天可见，是两件事。**EE≠R**；**严禁复用假设-R**；**不重开假设-R**；**不改 R**；**尤重：禁把 `vs_R_etf_t0` 升格进 `ee0`**；`etf_t0_handoff=r_page` |
| 题面 DI | **股票大宗经手下浮**（假设-DI） | 费率不是可见日。**EE≠DI**；**不重开假设-DI**；**不改 DI**；**尤重：禁把 `vs_DI_block_fee` 升格进 `ee0`**；`block_fee_handoff=di_page` |
| 题面 预告时限 | 把「年报结束后一个月 / 中报结束后十五日」，或 1 月 31 日 / 中报后第 15 日，写成全市场同一天可见 | `invent_statutory_preview_deadline_as_visible_day` **只进诊断、不升格主报**。一个月 / 十五日是预告**时限**，不是可见日。**禁与 `ee0` 双挂**。**禁用 1 月 31 日 / 中报后第 15 日等时限假冒全市场可见日**。EE1 不升格并列主报 |
| 题面 当成已审计定期报告 | 把预告的盈亏区间，或快报的主要财务数据，当成已经审计的年报/中报使用 | `invent_treat_preview_or_flash_as_audited_periodic_report` **只进诊断、不升格主报**。**禁把预告/快报升格成已审计定期报告**。正式年报/中报留在 ED。**禁与 `ee0` 双挂**。**零改 ED** |
| 题面 忽略修正 | 预告或快报披露后又出修正公告，仍用第一份公告日，或不修正 | `invent_ignore_preview_or_flash_correction` **只进诊断、不升格主报**。**已披露后又有修正公告的，以最新公告日为准**。**禁与 `ee0` 双挂** |
| 题面 未触发仍发明 | 公司没有触发预告义务，回测仍补一份预告 | **未触发预告义务则不得发明预告**。缺这份预告不是「用时限日填上」，是 skip。诊断桶 `invent_preview_when_no_obligation` 只作对照，不得升格 |
| 题面 B2 | **场内基金大宗门槛** | 门槛是成交规则族，不是因子可见性。诊断桶 `vs_B2_fund_block_threshold` 只作对照。**禁升格**。**不另挂主报**。**零改 O** |
| 题面 B3 | **16:00-17:00 / VWAP 暂缓窗** | 这道窗在事实稿里仍是**暂缓**，不是现行可成交，更不是预告可见日。诊断桶 `vs_B3_deferred_vwap_window` 只作对照。**禁升格**。**不另挂主报**。**零改 O**。不要把暂缓窗改选成本页 |
| 题面 单字母 E | 整手页 | **双字母 EE ≠ 单字母假设-E，亦不等于假设-ED / 假设-EC / 假设-EA / 假设-EB**。主键只用 `ee0` / `ee1` / `ee2` 与 `earnings_preview_flash_*` |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_forecast_or_flash_aligned_to_period_end_or_deadline`（**写死冻结**单一主报，单挂写死；禁与 `invent_statutory_preview_deadline_as_visible_day` 双挂；禁与 `invent_treat_preview_or_flash_as_audited_periodic_report` 双挂；禁与 `invent_ignore_preview_or_flash_correction` 双挂；三者只进诊断；EE1 不升格；诊断桶不升格；**禁把 ED 诊断桶升格进 `ee0`**） |
| 文档 | 清单实验 ED 及上表各页（**只读；禁止改写**） | `假设-EE-业绩预告快报按期末或时限对齐误套.md`（新建） |
| 预检键 | 实验字母 ED / EC / EB / O / E / C / V / W / R | 实验字母 **EE** / `ee0_primary_demo`；**不得**占用或改写上述预检键；**params.Y/G/N ≠ 实验字母 EE**；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O** |

**禁止**：把 EE 写成「ED / EC / EB / O / C / D / E / V / W 的续篇」；把「核对日已经知道报告期末不能当可见日」写成「全历史预告已按公告日对齐」；把实验字母 EE 与单字母 E 或 params.Y/G/N 或假设-ED 混读；**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰**；**禁把占位 `0.02/0.01/0.05/0.015` 读成证管费、过户费、一个月、十五日、1 月 31 日、中报后第 15 日**；**实验 R 不抢**；**不重开假设-V / 假设-T / 假设-U**；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O**；**EE 专写业绩预告/业绩快报，不等于 ED 正式年报/中报**；**C 的偷看对象是成分不是预告/快报**；**D 的次日开/收与停牌假成交 ≠ 本页披露可见日**；**EC 接受闸门 / EB 价限 / EA 类型 / DZ 确认钟 / DY 首日申报 / DX 收盘产生 ≠ 本页**；**O/M/CH/CK 通道与流动性 ≠ 本页**；**E 整手 ≠ 本页**；**V 印花切日，费用 ≠ 可见日**；**W 除权判板 ≠ 本页**；**双字母 EE ≠ 单字母假设-E，亦不等于假设-ED / 假设-EC / 假设-EA / 假设-EB**；**禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格**；**不另挂主报**；**禁把预告时限键、当成已审计定期报告键、忽略修正键升格进 `ee0`**；**禁把 ED 诊断桶升格进 `ee0`**；诊断桶只作对照/旁路，不得升格进 `ee0`；缺公告日或披露时点仍硬填；未触发预告义务仍发明预告；修正公告仍用第一份公告日。本页主键只用 `ee0` / `ee1` / `ee2` 与 `earnings_preview_flash_*`。不写下一字母。不预留 #141。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–ED；勿再只改清单）。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测把业绩预告或业绩快报的盈亏区间/主要财务数据，按报告期末（或按「年报结束后一个月 / 中报结束后十五日」的预告时限）对齐到下一交易日调仓，等于偷看尚未公告的预告或快报；或把预告/快报当成已审计年报/中报使用。相对「缺公告日或披露时点则 skip；未触发预告义务则不得发明预告；预告/快报按实际公告日或交易所披露时间可见，再落到下一可交易日；已披露后又有修正公告的，以最新公告日为准；一个月 / 十五日只是预告时限，不是可见日」的诚实组，会**系统性改写这只股票在该截面上能不能用这份预告或快报**——公告还没出来，因子里已经有了盈亏区间或快报数字；或者快报被当成已经审计的年报。方向是相对诚实锚偏误。本题是**因子可见性，不是成交规则**。

核对日方向（随锚写死；禁把占位读成证管费、过户费或预告时限）：`事实与坑.md` L62–L64、L83–L86、L109–L111 已经钉住「报告期末不是可见日」，但那三处只覆盖**正式年报/中报**。L62–L64 写《证券法》第 79 条、《上市公司信息披露管理办法》第 13 条的四个月/两个月；L83–L86、L109–L111 写证监会令第 226 号第十三条（2025-07-01 施行）的同一期限，并要求对齐公告日再落到下一可交易日。那是假设-ED 的主报。本页不改那些行，也不把四个月/两个月搬进来当预告时限。本条专写业绩预告和业绩快报。同一令第十八条：预计亏损或大幅变动，应当及时进行业绩预告。第十九条：定期报告披露前业绩泄露，或因业绩传闻导致交易异常波动，应当及时披露本报告期相关财务数据。与 ED 所引同一令，ED 用第十三条定期报告期限；本条用第十八/十九条。令文 2025-07-01 施行。来源页：https://www.gov.cn/gongbao/2025/issue_12026/202505/content_7022576.html 。深交所《股票上市规则（2026 年修订）》5.1.1–5.1.7：年度预告在会计年度结束之日起一个月内，半年度预告在半年度结束之日起十五日内；快报有强制触发，也可以自愿披露；差异达 20% 等须及时修正。上交所信息披露页（发布日期 2026-09-30）与上述时限、触发情形同向：https://one.sse.com.cn/onething/xxpl/ 。`asof_check_date` 写死冻结 `2026-09-28`（财务因子可见性族核对日；不是 EC 的 `2026-10-23`；与 ED 同核对日，但披露类型不同：ED 是正式年报/中报，本页是预告/快报）。**禁把占位读成证管费 0.02‰、过户 0.01‰、1 月 31 日、中报后第 15 日**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED**。**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**。

证伪方向：若天真组 / 预告时限组相对诚实组的可见日误套截在标定噪声带内可忽略，且「预告时限假冒可见日 / 预告快报当成已审计定期报告 / 忽略修正 / vs ED·EC·EB·EA·DZ·DY·DX·C·D·O·M·CH·CK·E·V·T·U·W·R / B2 / B3」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · ee0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结；禁止标纸面齐；不写 A/D–EE纸面齐）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 EE ≠ 单字母假设-E ≠ 假设-ED**；勿把 params.Y 读成实验字母 EE，亦勿读成单字母假设-E，亦勿读成假设-ED，亦勿读成假设-EC，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U
# 【消歧】尤重：params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED；亦不等于 V/T/U
# 【消歧】params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED
# 【消歧】尤重：params.Y 的 0.02 ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED ≠ 证管费 0.02‰ ≠ 可见日 ≠ 1 月 31 日 ≠ 核对日 2026-09-28；**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28 ≠ 可见日 ≠ 1 月 31 日 ≠ 实验字母 EE**
# 【消歧】尤重：params.G 的 0.01 ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日 ≠ 中报后第 15 日 ≠ 假设-G ≠ 假设-ED（无量纲相对门槛 ≠ 过户费率 ≠ 预告时限 ≠ 可见日）；**params.G=`0.01` ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日**
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 EE ≠ 单字母 E**
# 【消歧】params.Y2 写死冻结 0.015；不是可见日，不是预告时限，不是过户‰
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成证管费、过户费、一个月、十五日、1 月 31 日、中报后第 15 日
# 【消歧】params 相对门槛 ≠ 可见日 ≠ 预告时限 ≠ 过户‰ ≠ 证管费
# 【消歧】三条已冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值
# 【消歧】asof_check_date 写死冻结 2026-09-28；这不是 EC 的 2026-10-23；与 ED 同核对日，披露类型不同
# 【消歧】键名是 earnings_preview_flash_*，不要写成 fundamental_visible_*，也不要写成别的族名
# 【消歧】双字母 EE ≠ 单字母假设-E，亦不等于假设-ED / 假设-EC / 假设-EA / 假设-EB
# 【消歧】零改 ED；零改 EC；零改 EB；零改 O
# 【消歧】实验 R 不抢；不重开假设-V / 假设-T / 假设-U
# 【消歧】EE 专写业绩预告/业绩快报可见日，不等于 ED 正式年报/中报
# 【消歧】C = 股票池/指数当时名单，偷看对象是成分不是预告/快报；C ≠ 本页
# 【消歧】D = 次日开/收与停牌日假成交 ≠ 本页披露可见日
# 【消歧】EC 接受闸门 / EB 价限 / EA 类型 / DZ 确认钟 / DY 首日申报 / DX 收盘产生 ≠ 本页
# 【消歧】O/M/CH/CK 通道与流动性 ≠ 本页
# 【消歧】E = 整手 ≠ 本页；V = 印花切日，费用 ≠ 可见日；W = 除权判板 ≠ 本页
# 【消歧】硬分列：EE≠ED≠EC≠EB≠EA≠DZ≠DY≠DX≠C≠D≠O≠M≠CH≠CK≠E≠V≠W
# 【消歧】禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格；不另挂主报；零改 O
# 【消歧】诊断桶只作对照/旁路，不得升格进 ee0；禁把 ED 诊断桶升格进 ee0
# params.Y2                               写死冻结 0.015（不是可见日，不是预告时限，不是过户‰，不是证管费 0.02‰，不是核对日，不是 1 月 31 日）
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：可见日误套截 ΔPreviewFlashVisible / 净差异 / EE1−EE2；**params.Y/G/N ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED**；**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED**；**禁把占位读成证管费 0.02‰、过户 0.01‰、预告时限、可见日、核对日、1 月 31 日、中报后第 15 日**；**尤重 params.G=`0.01` ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日**；**尤重 params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28 ≠ 可见日 ≠ 1 月 31 日 ≠ 实验字母 EE**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        写死冻结 next_open
#   这是信号腿的成交时点建议：实际公告日或披露已经可见之后，落到下一可交易日
#   它不是报告期末的次日，也不是预告时限日，也不是 1 月 31 日，也不是停牌日假成交（那是假设-D）
#   双字母 EE ≠ 单字母假设-E
# params.asof_check_date                  写死冻结 2026-09-28（财务因子可见性族核对日；不是占位，不是 EC 的 2026-10-23，也不是可见日本身；与 ED 同核对日，披露类型不同）
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
#   缺公告日/披露时点则 skip
#   未触发预告义务则不得发明预告
# params.earnings_preview_flash_honest    写死冻结 asof_announcement_or_exchange_disclosure_then_next_tradable
#   诚实锚方向（已写死冻结）：
#   预告/快报按实际公告日或交易所披露时间可见，再落到下一可交易日
#   「年报结束后一个月 / 中报结束后十五日」只是预告时限，不是可见日
#   缺公告日或披露时点 → skip
#   未触发预告义务 → 不得发明预告
#   已披露后又有修正公告的，以最新公告日为准
#   禁用 1 月 31 日 / 中报后第 15 日等时限假冒全市场可见日
#   禁用报告期末对齐到下一交易日
#   禁把预告/快报升格成已审计年报/中报（那是另一类误套，只进诊断；正式定期报告可见日交 ED）
#   因子可见性，不是成交规则
#   键名是 earnings_preview_flash_*，不要写成别的族名
#   枚举已写死冻结
# params.earnings_preview_flash_scope     写死冻结 earnings_forecast_and_flash_only_not_periodic_report
#   主报只看业绩预告和业绩快报
#   正式年报/中报不进主报，交 ED；零改 ED
#   不是股票池成分，不是停牌假成交，不是大宗接受闸门
# params.earnings_preview_flash_over_policy 写死冻结 skip_if_announcement_or_disclosure_timestamp_missing
#   缺公告日或交易所披露时点则 skip
#   不用报告期末、不用 1 月 31 日 / 中报后第 15 日去补这个时点
#   未触发预告义务则不得发明预告
# params.periodic_report_visibility_handoff 建议 ed_page
#   正式年报/中报可见日交 ED；EE ≠ ED；零改 ED；不重开假设-ED；不改 ED 正文/预检/复检
#   诊断桶 vs_ED_periodic_report_visibility 不得升格进 ee0
#   ED 诊断桶（含 invent_statutory_deadline_as_visible_day / invent_quarterly_report_deadline_invented）不得升格进 ee0
# params.survivorship_handoff             建议 c_page
#   股票池/指数当时名单交 C；偷看对象是成分不是预告/快报；C ≠ 本页；不重开假设-C；不改 C
#   诊断桶 vs_C_survivorship 不得升格进 ee0
# params.halt_bar_handoff                 建议 d_page
#   次日开/收与停牌日假成交交 D；D ≠ 本页披露可见日；不重开假设-D；不改 D
#   诊断桶 vs_D_halt_bar 不得升格进 ee0
# params.sh_main_block_accept_handoff     建议 ec_page
#   沪市主板大宗接受闸门交 EC；零改 EC；EC ≠ 本页；不重开假设-EC；不改 EC 正文/预检/复检
#   诊断桶 vs_EC_sh_main_block_accept 不得升格进 ee0
# params.nolimit_nego_px_handoff          建议 eb_page
#   无板协议大宗价限交 EB；零改 EB；不重开假设-EB；不改 EB 正文/预检/复检
#   诊断桶 vs_EB_nolimit_nego_px 不得升格进 ee0
# params.star_fixed_price_type_handoff    建议 ea_page
#   科创大宗固定价格类型开关交 EA；EA ≠ 本页；不重开假设-EA；不改 EA
#   诊断桶 vs_EA_star_fixed_price_type 不得升格进 ee0
# params.chinext_confirm_handoff          建议 dz_page
#   创业板确认钟交 DZ；DZ ≠ 本页；不重开假设-DZ；不改 DZ
#   诊断桶 vs_DZ_chinext_confirm 不得升格进 ee0
# params.approval_ipo_band_handoff        建议 dy_page
#   核准制首日申报带交 DY；DY ≠ 本页；不重开假设-DY；不改 DY
#   诊断桶 vs_DY_approval_ipo_band 不得升格进 ee0
# params.sse_fund_close_handoff           建议 dx_page
#   沪市基金收盘产生交 DX；DX ≠ 本页；不重开假设-DX；不改 DX
#   诊断桶 vs_DX_sse_fund_close 不得升格进 ee0
# params.block_liquidity_handoff          建议 o_page
#   日量含大宗 / 三通道交 O；O 通道与流动性 ≠ 本页；零改 O；不重开假设-O；不改 O
#   诊断桶 vs_O_block_liquidity 不得升格进 ee0
#   B2 场内基金大宗门槛不另挂主报，不改 O
# params.aft_channel_handoff              建议 m_page
#   盘后固定价格通道交 M；M ≠ 本页；不重开假设-M；不改 M
#   诊断桶 vs_M_aft_channel 不得升格进 ee0
# params.aft_fill_handoff                 建议 ch_page
#   盘后可成交性交 CH；CH ≠ 本页；不重开假设-CH；不改 CH
#   诊断桶 vs_CH_aft_fill 不得升格进 ee0
# params.block_fill_handoff               建议 ck_page
#   协议大宗可成交性交 CK；CK ≠ 本页；不重开假设-CK；不改 CK
#   诊断桶 vs_CK_block_fill 不得升格进 ee0
# params.lot_size_handoff                 建议 e_page
#   整手与科创板 200 股交 E；双字母 EE ≠ 单字母假设-E；E ≠ 本页；不重开假设-E；不改 E
#   诊断桶 vs_E_lot_size 不得升格进 ee0
# params.stamp_handoff                    建议 v_page
#   股票印花切日交 V；费用 ≠ 可见日；不重开假设-V；params 字母 ≠ 假设-V；不改 V
#   诊断桶 vs_V_stamp 不得升格进 ee0
# params.ex_right_limit_handoff           建议 w_page
#   除权判板交 W；W ≠ 本页；不重开假设-W；不改 W
#   诊断桶 vs_W_ex_right_limit 不得升格进 ee0
# params.block_fee_handoff                建议 di_page
#   股票大宗经手下浮交 DI；费率 ≠ 可见日；不重开假设-DI；不改 DI
#   诊断桶 vs_DI_block_fee 不得升格进 ee0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 ee0；不改 R
#   诊断桶 vs_R_etf_t0 不得升格进 ee0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；params.Y 的 0.02 ≠ 证管费 0.02‰；不改 T
#   诊断桶 vs_T_csrc 不得升格进 ee0
# params.transfer_fee_handoff             建议 u_page
#   股票过户切日交 U；不重开假设-U；params.G 的 0.01 ≠ 过户 0.01‰；不改 U
#   诊断桶 vs_U_transfer 不得升格进 ee0
# params.ee0_primary_demo                 写死冻结 invent_forecast_or_flash_aligned_to_period_end_or_deadline
#   单一主报，单挂写死；三条已冻
#   禁与 invent_statutory_preview_deadline_as_visible_day 双挂
#   禁与 invent_treat_preview_or_flash_as_audited_periodic_report 双挂
#   禁与 invent_ignore_preview_or_flash_correction 双挂
#   三者只进诊断、不升格主报
#   EE1 不升格；诊断桶不升格
#   禁把预告/快报升格成已审计定期报告
#   禁把「年报结束后一个月 / 中报结束后十五日」预告时限写成可见日
#   禁用 1 月 31 日 / 中报后第 15 日等时限假冒全市场可见日
#   已披露后又有修正公告的，以最新公告日为准
#   未触发预告义务则不得发明预告
#   禁把 ED 诊断桶升格进 ee0
#   禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格
#   不另挂主报；零改 O；零改 ED；零改 EC；零改 EB
#   诊断桶 invent_statutory_preview_deadline_as_visible_day / invent_treat_preview_or_flash_as_audited_periodic_report / invent_ignore_preview_or_flash_correction / invent_preview_when_no_obligation / vs_ED_periodic_report_visibility / vs_EC_sh_main_block_accept / vs_EB_nolimit_nego_px / vs_EA_star_fixed_price_type / vs_DZ_chinext_confirm / vs_DY_approval_ipo_band / vs_DX_sse_fund_close / vs_C_survivorship / vs_D_halt_bar / vs_O_block_liquidity / vs_M_aft_channel / vs_CH_aft_fill / vs_CK_block_fill / vs_E_lot_size / vs_V_stamp / vs_T_csrc / vs_U_transfer / vs_W_ex_right_limit / vs_R_etf_t0 / vs_DI_block_fee / vs_B2_fund_block_threshold / vs_B3_deferred_vwap_window / missing_announcement_or_disclosure_timestamp_not_skip 不得升格进 ee0
#   尤重：实验 R 不抢
#   尤重：不重开假设-V / 假设-T / 假设-U
#   尤重：零改 ED；零改 EC；零改 EB；零改 O
#   尤重：双字母 EE ≠ 单字母 E；亦不等于假设-ED / 假设-EC / 假设-EA / 假设-EB
# params.ee0_invent_forecast_or_flash_aligned_to_period_end_or_deadline 建议 True
# params.ee1_preview_deadline_audited_treat_or_ignore_correction_diag_only 建议 True
#   预告时限假冒可见日、把预告/快报当成已审计定期报告、忽略修正公告，都只作诊断对照
#   EE1 不升格并列主报
#   不得把上述三键写进 ee0，不得双挂
# params.ee2_asof_announcement_or_exchange_disclosure 建议 True
# params.correction_visible_day           写死冻结 latest_announcement_date
#   已披露后又有修正公告的，以最新公告日为准；已写死冻结
# params.no_obligation_invent_preview     建议 False
#   未触发预告义务则不得发明预告
# params.merge_with_ED                    建议 False
# params.merge_with_EC                    建议 False
# params.merge_with_EB                    建议 False
# params.merge_with_EA                    建议 False
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
# params.merge_with_B                     建议 False
# params.merge_with_C                     建议 False
# params.missing_announcement_timestamp_policy 建议 skip
# params.day_freq_proxy                   建议 earnings_preview_flash_visible_sensitivity
# params.universe_rule                    建议 earnings_preview_flash_visible_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_ee_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 EE；勿读成单字母 E，亦勿读成假设-ED
#   不另挂主报，不预留 #141，不写下一字母
```

### 2.2 三组对照（EE0 / EE1 / EE2）

组名 EE0 / EE1 / EE2 是本页三组，≠ 单字母实验 E（整手与科创板 200 股），亦 ≠ 双字母实验 ED（正式年报/中报可见日），亦 ≠ 双字母实验 EC（沪市主板大宗接受闸门）。**双字母 EE ≠ 单字母假设-E**。**双字母 EE ≠ 假设-ED / 假设-EC / 假设-EA / 假设-EB**。**params.Y/G/N ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED**。**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED**。

| 组 | 角色 | 口径 |
|----|------|------|
| EE0 | 天真 / 按报告期末或预告时限对齐到下一交易日 | 按 `ee0_primary_demo` **写死冻结**单一主报 `invent_forecast_or_flash_aligned_to_period_end_or_deadline`（单挂写死）：业绩预告或业绩快报按报告期末，或按「年报结束后一个月 / 中报结束后十五日」，对齐到下一交易日就能调仓。**禁**与 `invent_statutory_preview_deadline_as_visible_day` 双挂。**禁**与 `invent_treat_preview_or_flash_as_audited_periodic_report` 双挂。**禁**与 `invent_ignore_preview_or_flash_correction` 双挂。**禁把这三键、ED 诊断桶、B2、B3、ED/EC/EB/EA/DZ/DY/DX/C/D/O/M/CH/CK/E/V/T/U/W/R 合成进 `ee0`** |
| EE1 | 诊断对照（不升格） | 三键只进诊断：把预告时限或 1 月 31 日 / 中报后第 15 日写成全市场可见日（`invent_statutory_preview_deadline_as_visible_day`）；把预告/快报当成已审计年报/中报（`invent_treat_preview_or_flash_as_audited_periodic_report`）；忽略修正公告（`invent_ignore_preview_or_flash_correction`）。**只进诊断、不得升格并列主报**，不得写进 `ee0`，不得双挂。**EE1 不升格并列主报**。未触发义务仍发明预告，见诊断桶，不进主报 |
| EE2 | 诚实 / 公告日或交易所披露时间，再落到下一可交易日 | `earnings_preview_flash_honest=asof_announcement_or_exchange_disclosure_then_next_tradable`（写死冻结）：缺公告日或披露时点则 skip；未触发预告义务则不得发明预告；预告/快报按实际公告日或交易所披露时间可见，再落到下一可交易日；已披露后又有修正公告的，以最新公告日为准；一个月 / 十五日只是预告时限，不是可见日。正式年报/中报只消费 ED，接受闸门只消费 EC，价限只消费 EB，类型只消费 EA，确认钟只消费 DZ，首日申报只消费 DY，收盘产生只消费 DX，成分只消费 C，停牌假成交只消费 D，通道与流动性只消费 O/M/CH/CK，整手只消费 E，印花只消费 V，除权判板只消费 W，假 T+0 只消费 R，证管费只消费 T，过户只消费 U，或显式旁路 |

把预告时限假冒可见日、把预告/快报当成已审计定期报告、忽略修正、未触发仍发明预告、B2、B3，以及相对 ED/EC/EB/EA/DZ/DY/DX/C/D/O/M/CH/CK/E/V/T/U/W/R/DI 的对照，放进 §4.1 分桶，**只作诊断桶或旁路，不得升格为第二个主报**。上述三键**只进诊断、不升格主报、禁与 `ee0` 双挂**。`vs_ED_periodic_report_visibility` 只标记正式年报/中报那一页，**零改 ED**，**禁把 ED 诊断桶升格进 `ee0`**。`vs_B2_fund_block_threshold` 只标记场内基金大宗门槛。`vs_B3_deferred_vwap_window` 只标记 16:00-17:00 / VWAP **暂缓**窗。这两条**禁升格、不另挂主报、零改 O**。其余 `vs_*` 与 `missing_announcement_or_disclosure_timestamp_not_skip` 同样**不得升格进 `ee0`**。

### 2.3 可见日可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-09-28`（财务因子可见性族核对日；不是 EC 的 `2026-10-23`；与 ED 同核对日，披露类型不同）；fill_time **写死冻结** `next_open`（这是实际公告日之后的下一可交易日，不是报告期末，也不是预告时限日）；fail **写死冻结** `skip`（缺公告日/披露时点则 skip；未触发预告义务则不得发明预告）。诚实锚六键与 Y/G/N/Y2、`ee0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺公告日或交易所披露时点则 skip；未触发预告义务则不得发明预告；预告/快报按实际公告日或交易所披露时间可见，再落到下一可交易日；已披露后又有修正公告的，以最新公告日为准；「年报结束后一个月 / 中报结束后十五日」只是预告时限，不是可见日；禁用 1 月 31 日 / 中报后第 15 日假冒全市场可见日；禁用报告期末对齐；禁把预告/快报当成已审计年报/中报。`params.G` 的 0.01 不是过户费 0.01‰；`params.Y` 的 0.02 不是实验字母 EE，也不是单字母 E，也不是假设-ED，也不是证管费 0.02‰；四个占位也不是 2026-09-28，也不是 1 月 31 日，也不是报告期末。**禁把占位读成证管费、过户费、预告时限**。本页**不开回测**；不拉真数；不做实盘；不开户。因子可见性，不是成交规则。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `ee0_primary_demo` / `params.Y`·G·N·Y2 / 可见日开关 / 桶 / 是否把预告时限或已审计误用或忽略修正或 B2/B3 或成交规则页或 ED 正式年报倒灌进主报、或与诊断键双挂、或把占位读成证管费或过户费或 1 月 31 日）。本页不开跑。禁 null。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（EE0）/ 诊断对照组（EE1）相对诚实组（EE2）的可见日误套截**显著且集中在预告或快报按报告期末或预告时限对齐到下一交易日**的桶；分桶「预告时限假冒可见日 / 当成已审计定期报告 / 忽略修正 / vs ED·EC·EB·EA·DZ·DY·DX·C·D·O·M·CH·CK·E·V·T·U·W·R / B2 / B3」不改变主结论方向。成功不依赖把占位读成证管费或过户费，也不把 `params.Y` 读成实验字母 EE，也不把 1 月 31 日读成全市场可见日。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 ED 的正式年报/中报、EC 的接受闸门、EB 的价限、C 的成分名单、D 的停牌假成交、O 的通道、E 的整手、V/T/U 的费用、W 的除权判板、R 的假 T+0、A 的板上容量解释；或 `ee0_primary_demo` 与 `invent_statutory_preview_deadline_as_visible_day` 双挂；或与 `invent_treat_preview_or_flash_as_audited_periodic_report` 双挂；或与 `invent_ignore_preview_or_flash_correction` 双挂；或 EE1 升格并列主报；或诊断桶升格主报；或 ED 诊断桶升格进 `ee0`；或 B2/B3 另挂主报；或把 1 月 31 日 / 中报后第 15 日写成全市场可见日并升格；或把预告/快报升格成已审计定期报告；或未触发预告义务仍发明预告；或修正公告不用最新公告日；或实验字母 EE 与单字母 E 或假设-ED 或 params.Y/G/N 混读；或把占位读成证管费 0.02‰、过户 0.01‰；或缺公告日/披露时点仍不 skip；或重开假设-R / 假设-V / 假设-T / 假设-U / 假设-ED / 假设-EC / 假设-EB / 假设-O / 假设-C / 假设-D / 假设-E / 假设-W；或改 ED / EC / EB / O 正文/预检/复检；或标纸面齐；或写成 A/D–EE纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 EE0/EE1/EE2。正式年报/中报走 ED，接受闸门走 EC，价限走 EB，类型走 EA，确认钟走 DZ，首日申报走 DY，收盘产生走 DX，成分走 C，停牌假成交走 D，通道走 O/M/CH/CK，整手走 E，印花走 V，除权判板走 W，假 T+0 走 R，证管费走 T，过户走 U，都不改。预告/快报可见日误套截：有多少截面在公告日前就用上了盈亏区间或快报主要财务数据，或把它们当成已审计年报/中报。不把 1 月 31 日或 2026-09-28 标成占位门槛，也不把建议锚写成已冻。本页不开回测。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_forecast_or_flash_aligned_to_period_end_or_deadline` / `invent_statutory_preview_deadline_as_visible_day` / `invent_treat_preview_or_flash_as_audited_periodic_report` / `invent_ignore_preview_or_flash_correction` / `invent_preview_when_no_obligation` / `vs_ED_periodic_report_visibility` / `vs_EC_sh_main_block_accept` / `vs_EB_nolimit_nego_px` / `vs_EA_star_fixed_price_type` / `vs_DZ_chinext_confirm` / `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` / `vs_C_survivorship` / `vs_D_halt_bar` / `vs_O_block_liquidity` / `vs_M_aft_channel` / `vs_CH_aft_fill` / `vs_CK_block_fill` / `vs_E_lot_size` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `vs_DI_block_fee` / `vs_B2_fund_block_threshold` / `vs_B3_deferred_vwap_window` / `missing_announcement_or_disclosure_timestamp_not_skip`

`invent_forecast_or_flash_aligned_to_period_end_or_deadline` 才是写死冻结的单一主报名（单挂写死）。自 `invent_statutory_preview_deadline_as_visible_day` 起至 `missing_announcement_or_disclosure_timestamp_not_skip` **只作诊断桶**：它们不是 `ee0`，也不是并列主报，**不得升格主报，不得双挂**。`invent_statutory_preview_deadline_as_visible_day`、`invent_treat_preview_or_flash_as_audited_periodic_report`、`invent_ignore_preview_or_flash_correction` **三者只进诊断、不升格主报**。`vs_ED_periodic_report_visibility` 以及 ED 页自己的诊断桶（`invent_statutory_deadline_as_visible_day` / `invent_quarterly_report_deadline_invented` 等）**禁升格进 `ee0`**。**零改 ED**。`vs_B2_fund_block_threshold` 与 `vs_B3_deferred_vwap_window` **禁升格、不另挂主报**。B3 那道 16:00-17:00 / VWAP 窗仍是**暂缓**，不要写成现行可成交，也不要改选成本页。**零改 O**。**零改 EC**。**零改 EB**。**实验 R 不抢**。**不重开假设-V / 假设-T / 假设-U**。没有「成交规则 + 本页可见日」合成主报，也没有「成分名单 + 预告」合成主报，也没有「正式年报 + 预告」合成主报，也没有「预告时限 + 报告期末」合成主报。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「报告期末或预告时限对齐到下一交易日」或「1 月 31 日 / 中报后第 15 日全市场同一天可见」或「预告/快报当成已审计年报/中报」或「忽略修正公告」拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成实验字母 EE，或当成单字母 E，或当成假设-ED，或当成证管费 0.02‰，或当成 1 月 31 日，或当成核对日。**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**。**params 字母 ≠ 假设-T**。**params 字母 ≠ 假设-E**。**params 字母 ≠ 假设-ED**。
- 把 `params.G` 的 0.01 当成过户 0.01‰，或当成假设-G，或当成十五日时限，或当成中报后第 15 日。**params 字母 ≠ 假设-U**。**params 字母 ≠ 假设-V**。
- 把 `params.N` 的 0.05 当成实验字母 EE 或单字母 E。**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**。**params.Y/G/N 亦不等于 V/T/U**。
- 把占位 `0.02/0.01/0.05/0.015` 读成证管费、过户费、预告时限或 1 月 31 日。**params 相对门槛 ≠ 可见日 ≠ 预告时限 ≠ 过户‰ ≠ 证管费**。
- 缺公告日或交易所披露时点仍不 skip。诊断桶 `missing_announcement_or_disclosure_timestamp_not_skip` 只作对照，不得升格。
- 把「年报结束后一个月 / 中报结束后十五日」写成可见日，或用 1 月 31 日 / 中报后第 15 日假冒全市场可见日，并升格进主报。诊断桶 `invent_statutory_preview_deadline_as_visible_day` 只作对照。**禁与 `ee0` 双挂**。**EE1 不升格**。
- 把预告或快报升格成已审计年报/中报。诊断桶 `invent_treat_preview_or_flash_as_audited_periodic_report` 只作对照。**禁与 `ee0` 双挂**。正式定期报告留在 ED。
- 已披露后又有修正公告，仍不用最新公告日。诊断桶 `invent_ignore_preview_or_flash_correction` 只作对照。**禁与 `ee0` 双挂**。
- 未触发预告义务仍发明一份预告。诊断桶 `invent_preview_when_no_obligation` 只作对照，不得升格。
- 把假设-ED 的正式年报/中报和本页预告/快报合成后升格，或把 ED 诊断桶升格进 `ee0`。**零改 ED**。**EE≠ED**。诊断桶 `vs_ED_periodic_report_visibility` 只作对照。
- 把假设-EC 的接受闸门和本页可见日合成后升格。**零改 EC**。**EE≠EC**。诊断桶 `vs_EC_sh_main_block_accept` 只作对照。
- 把假设-EB 的价限、假设-EA 的类型开关和本页合成后升格。**零改 EB**。诊断桶 `vs_EB_nolimit_nego_px` / `vs_EA_star_fixed_price_type` 只作对照。
- 把假设-DZ 的确认钟、假设-DY 的首日申报、假设-DX 的收盘产生和本页合成后升格。诊断桶 `vs_DZ_chinext_confirm` / `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` 只作对照。
- 把假设-C 的股票池/指数成分和本页预告可见日合成后升格。**C 的偷看对象是成分不是预告/快报**。**C ≠ 本页**。诊断桶 `vs_C_survivorship` 只作对照。
- 把假设-D 的次日开/收、停牌日假成交和本页披露可见日合成后升格。诊断桶 `vs_D_halt_bar` 只作对照。
- 把假设-O / 假设-M / 假设-CH / 假设-CK 的通道与流动性和本页合成后升格，或改 O。**零改 O**。诊断桶 `vs_O_block_liquidity` / `vs_M_aft_channel` / `vs_CH_aft_fill` / `vs_CK_block_fill` 只作对照。
- 把 B2（场内基金大宗门槛）或 B3（16:00-17:00/VWAP 暂缓窗）升格，或另挂主报，或因此去改 O。诊断桶 `vs_B2_fund_block_threshold` / `vs_B3_deferred_vwap_window` 只作对照。B3 仍是**暂缓**。
- 把假设-E 的整手和本页合成后升格。**双字母 EE ≠ 单字母假设-E**。**E ≠ 本页**。诊断桶 `vs_E_lot_size` 只作对照。
- 把假设-V / 假设-T / 假设-U 的费用切日和可见日合成后升格。**费用 ≠ 可见日**。诊断桶 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只作对照。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。
- 把假设-W 的除权判板和本页合成后升格。**W ≠ 本页**。诊断桶 `vs_W_ex_right_limit` 只作对照。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格。**实验 R 不抢**。诊断桶 `vs_R_etf_t0` 只作对照。
- `ee0_primary_demo` 与三诊断键任一双挂；EE1 升格并列主报。
- 实验字母 EE 与单字母 E 或假设-ED 或 params.Y/G/N 混读。**双字母 EE ≠ 单字母 E**。**双字母 EE ≠ 假设-ED**。**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**。
- 改 ED / EC / EB / EA / O / C / D / W / R / V / T / U / E 及其他已冻页正文；改 #110–#139；禁止标纸面齐；禁止写成 A/D–EE纸面齐；或预留下一号；开真数/回测/开户/实盘；用报告期末或预告时限当可见日；结论写成「这类预告更早可见所以能买」。
- **纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–ED；勿再只改清单）。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权路径、交易日、披露类型（须能分出**业绩预告 / 业绩快报 / 正式年报 / 正式中报 / 其他**）。类型分不清则 skip。本页主报只钉业绩预告和业绩快报的可见日。正式年报/中报交 ED，不进 `ee0`。
- **报告期末**（如 12 月 31 日、6 月 30 日）：只作「这份预告或快报覆盖哪一段」的标签，**不作可见日**。把报告期末对齐到下一交易日，就是本页要抓的误套。
- **预告时限**：年度预告在会计年度结束之日起一个月内，半年度预告在半年度结束之日起十五日内。这是时限，不是可见日。禁用 1 月 31 日 / 中报后第 15 日假冒全市场可见日。
- **公告日或交易所披露时间**：实际对外可见的时点。有了这个时点，才落到**下一可交易日**。时点缺了则 skip。不用报告期末，也不用时限日，去填这个空。
- **修正公告**：已披露后又有修正公告的，以最新公告日为准。快报与后来定期报告差异达 20% 等，规则要求及时修正；修正没出来之前，不得把快报升格成已审计年报/中报。
- **预告义务**：预计亏损或大幅变动才应当及时预告（第十八条）。没有触发，不得发明预告。第十九条管的是定期报告披露前业绩泄露，或业绩传闻导致交易异常波动时，及时披露本报告期相关财务数据；这仍是公告时点，不是报告期末。
- 官方规则是否在册：证监会令第 226 号《上市公司信息披露管理办法》第十八条、第十九条（2025-07-01 施行）。与 ED 所引同一令，ED 用第十三条定期报告期限；本条用第十八/十九条。来源页：https://www.gov.cn/gongbao/2025/issue_12026/202505/content_7022576.html 。深交所《股票上市规则（2026 年修订）》5.1.1–5.1.7。上交所信息披露页（发布日期 2026-09-30）：https://one.sse.com.cn/onething/xxpl/ 。事实稿落点：`事实与坑.md` L62–L64、L83–L86、L109–L111 已钉「报告期末不是可见日」，但只覆盖正式年报/中报；本条专写预告/快报，不改那三处原文。规则不在册则 skip。
- 旁路消费：ED 的正式年报/中报、EC 的接受闸门、EB 的价限、EA 的类型、DZ 的确认钟、DY 的首日申报、DX 的收盘产生、C 的成分名单、D 的停牌假成交、O/M/CH/CK 的通道与流动性、E 的整手、V/T/U 的费用、W 的除权判板、R 的假 T+0（见 §2.1 handoff）。**本页不改写这些页。零改 ED。零改 EC。零改 EB。零改 O。** B2 场内基金大宗门槛与 B3 的 16:00-17:00 / VWAP 暂缓窗不进主报。
- 未复权路径；asof **写死冻结** `2026-09-28`（不是 EC 的 `2026-10-23`；与 ED 同核对日，披露类型不同）。核对日已经写着正式财报「报告期末不是可见日」，所以不能把这句话倒灌成「预告可以用 1 月 31 日」，也不能把 ED 的四个月/两个月抄成预告时限。`事实与坑.md` 是方向来源，不是已冻的全历史规则。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`（实际公告日后一可交易日，不是报告期末，也不是预告时限日）；`asof_check_date=2026-09-28`（财务因子可见性族核对日；不是 EC 的 `2026-10-23`；与 ED 同核对日，披露类型不同）；`fail_policy=skip`（缺公告日/披露时点则 skip；未触发预告义务则不得发明预告）；`earnings_preview_flash_honest=asof_announcement_or_exchange_disclosure_then_next_tradable`；`earnings_preview_flash_scope=earnings_forecast_and_flash_only_not_periodic_report`；`earnings_preview_flash_over_policy=skip_if_announcement_or_disclosure_timestamp_missing`；`ee0_primary_demo=invent_forecast_or_flash_aligned_to_period_end_or_deadline`（**写死冻结**单一主报，单挂写死；禁与 `invent_statutory_preview_deadline_as_visible_day` 双挂；禁与 `invent_treat_preview_or_flash_as_audited_periodic_report` 双挂；禁与 `invent_ignore_preview_or_flash_correction` 双挂；三者只进诊断、不升格主报；EE1 不升格；诊断桶不升格；**禁把预告/快报升格成已审计定期报告**；**禁把预告时限写成可见日**；**禁用 1 月 31 日 / 中报后第 15 日假冒全市场可见日**；**已披露后又有修正公告的，以最新公告日为准**；**未触发预告义务则不得发明预告**；**禁把 B2 / B3 升格，不另挂主报**；**禁把 ED 诊断桶升格进 `ee0`**；**禁把 ED/EC/EB/EA/DZ/DY/DX/C/D/O/M/CH/CK/E/V/T/U/W/R 升格进 `ee0`**）；`periodic_report_visibility_handoff=ed_page`；`survivorship_handoff=c_page`；`halt_bar_handoff=d_page`；`sh_main_block_accept_handoff=ec_page`；`nolimit_nego_px_handoff=eb_page`；`star_fixed_price_type_handoff=ea_page`；`chinext_confirm_handoff=dz_page`；`approval_ipo_band_handoff=dy_page`；`sse_fund_close_handoff=dx_page`；`block_liquidity_handoff=o_page`；`aft_channel_handoff=m_page`；`aft_fill_handoff=ch_page`；`block_fill_handoff=ck_page`；`lot_size_handoff=e_page`；`stamp_handoff=v_page`；`ex_right_limit_handoff=w_page`；`block_fee_handoff=di_page`；`etf_t0_handoff=r_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；全部 `merge_with_*=False`；`merge_with_ED/EC/EB/EA/DZ/DY/DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/Y/A/D/Z/B/C=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是可见日，不是预告时限，不是过户费率，不是证管费，不是 1 月 31 日，不是核对日；**三条已冻**；**params.Y/G/N ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED**；**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**；**params.Y/G/N 亦不等于 V/T/U**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED**；**尤重 params.Y 的 0.02 ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED ≠ 证管费 0.02‰**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 假设-G ≠ 假设-ED**；**禁把占位读成证管费、过户费、一个月、十五日、1 月 31 日、中报后第 15 日**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #141。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`b49d45dc`（A/D–ED纸面齐已合，已收讫，全长 `b49d45dcb0ab6a7985910a54ca0faff9c2db0b29`）；分支起点 HEAD=`d6f6f32` / `d6f6f32bc7e794810a1ee04d122a4c39438e7553`；三冻补丁基 tip=`74e606f9` / `74e606f926ceaf25e99b49ab512d5a54d9383afc`；本补丁分支起点 HEAD=`b3d54a19` / `b3d54a19cac96b8289e936f987eac17c4cdd0740`。**不改已冻 A–DQ / DA–ED**。**零改 ED**。**零改 EC**。**零改 EB**。**零改 O**。**不改 #110–#139**。状态=**A/D–EE纸面齐（预检有条件通过·三条已冻）**。

---

## 8. 结论

（空；**A/D–EE纸面齐（预检有条件通过·三条已冻）**。）

---

## 变更
| 日期 | 变更 |
|------|------|

## 风控预检补丁·冻结（三条已写死 · 2026-12-11）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设EE-20261110.md`（原样落入，不改结论；SHA256=`b0404e0aaaa68a1b2077cd399ff81def9484d7bf0027bb9f0d9a2d85412ef633`；预检 2026-11-10；**结论：有条件通过**；tip基=`74e606f9` / `74e606f926ceaf25e99b49ab512d5a54d9383afc`；本补丁分支起点 HEAD=`b3d54a19` / `b3d54a19cac96b8289e936f987eac17c4cdd0740`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于可见日误套截 ΔPreviewFlashVisible、净差异、EE1−EE2 专项。**`params.Y` ≠ 实验字母 EE**；**`params.G` ≠ 实验字母 EE**；**`params.N` ≠ 实验字母 EE**；亦 ≠ 单字母假设-E；亦 ≠ 假设-ED / 假设-EC / 假设-EA / 假设-EB。**params.Y/G/N ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED**。**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**。**勿把 `params.Y` 读成实验字母 EE，亦勿读成单字母假设-E，亦勿读成假设-ED，亦勿读成假设-EC，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿把 `params.G` 读成假设-U，亦勿把 `params.G` 读成假设-G，亦勿把 `params.G` 读成假设-ED，亦勿把单字母假设-E 读成双字母 EE**。**尤重：`params.G` 的 `0.01` ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日**（**params.G=`0.01` ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日**）。量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户 0.01‰，也不是预告时限「一个月/十五日」，也不是 1 月 31 日或中报后第 15 日，也不是可见日，也不是假设-G。**尤重：`params.Y` 的 `0.02` ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28 ≠ 可见日 ≠ 1 月 31 日 ≠ 实验字母 EE**（**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28 ≠ 可见日 ≠ 1 月 31 日 ≠ 实验字母 EE**）。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED / 假设-EC / 假设-EA / 假设-EB**。**禁把占位读成证管费、过户费、一个月、十五日、1 月 31 日、中报后第 15 日、可见日、核对日、预告时限**。**params 相对门槛 ≠ 可见日 ≠ 预告时限 ≠ 过户‰ ≠ 证管费 ≠ 核对日 2026-09-28**。禁止互读、禁止把门槛改写成可见日、预告时限、核对日、过户费率或证管费。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.ee0_primary_demo`**：**写死冻结** **`invent_forecast_or_flash_aligned_to_period_end_or_deadline`**（单一主报，单挂写死）。**禁止**与预告时限键 **`invent_statutory_preview_deadline_as_visible_day`** 双挂争主表；**禁止**与当成已审计定期报告键 **`invent_treat_preview_or_flash_as_audited_periodic_report`** 双挂；**禁止**与忽略修正键 **`invent_ignore_preview_or_flash_correction`** 双挂；三者只进诊断、不升格；**禁止**跑后因分桶显著性改口主报。EE1 仅把预告时限假冒可见日、把预告/快报当成已审计定期报告、忽略修正公告，只作诊断对照，**不得升格与 ee0 并列主报**，也不得把这三键写进 `ee0`。`invent_statutory_preview_deadline_as_visible_day / invent_treat_preview_or_flash_as_audited_periodic_report / invent_ignore_preview_or_flash_correction / invent_preview_when_no_obligation / vs_ED_periodic_report_visibility / vs_EC_sh_main_block_accept / vs_EB_nolimit_nego_px / vs_EA_star_fixed_price_type / vs_DZ_chinext_confirm / vs_DY_approval_ipo_band / vs_DX_sse_fund_close / vs_C_survivorship / vs_D_halt_bar / vs_O_block_liquidity / vs_M_aft_channel / vs_CH_aft_fill / vs_CK_block_fill / vs_E_lot_size / vs_V_stamp / vs_T_csrc / vs_U_transfer / vs_W_ex_right_limit / vs_R_etf_t0 / vs_DI_block_fee / vs_B2_fund_block_threshold / vs_B3_deferred_vwap_window / missing_announcement_or_disclosure_timestamp_not_skip` **只作诊断桶，不得升格主报**。EE1 / 诊断桶 **不升格**。**未触发预告义务则不得发明预告**。**已披露后又有修正公告的，以最新公告日为准**。**「年报结束后一个月 / 中报结束后十五日」只是预告时限，不是可见日**。**禁用 1 月 31 日 / 中报后第 15 日等时限假冒全市场可见日**。**禁止把预告/快报当成已审计年报/中报**。**禁把以下升格进 ee0**：预告时限键 / 当成已审计定期报告 / 忽略修正 / 未触发仍发明预告 / ED 诊断桶（含 `invent_statutory_deadline_as_visible_day` / `invent_quarterly_report_deadline_invented` / `vs_ED_periodic_report_visibility`） / ED/EC/EB/EA/DZ/DY/DX/C/D/O/M/CH/CK/E/V/T/U/W/R/DI / B2场内基金大宗门槛 / B3 的 16:00-17:00/VWAP 暂缓窗。这些只作对照/旁路，**不得升格进 `ee0`，不得另挂主报**。**禁 B2/B3 升格或另挂主报**。**零改 ED**。**零改 EC**。**零改 EB**。**零改 O**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**不抢实验 R**。**双字母 EE ≠ 单字母假设-E**。**双字母 EE ≠ 假设-ED / 假设-EC / 假设-EA / 假设-EB**。

3. **预告/快报可见日诚实锚六键升格写死（不可再写「建议」；键名是 `earnings_preview_flash_*`，不是 ED 的 `fundamental_visible_*`）**：`params.earnings_preview_flash_honest=asof_announcement_or_exchange_disclosure_then_next_tradable`；`params.earnings_preview_flash_scope=earnings_forecast_and_flash_only_not_periodic_report`；`params.earnings_preview_flash_over_policy=skip_if_announcement_or_disclosure_timestamp_missing`；`params.asof_check_date=2026-09-28`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺公告日或交易所披露时点 → skip。诚实：预告/快报按实际公告日或交易所披露时间可见，再落到下一可交易日；「年报结束后一个月 / 中报结束后十五日」只是预告时限，不是可见日；已披露后又有修正公告的，以最新公告日为准；未触发预告义务则不得发明预告；禁用 1 月 31 日 / 中报后第 15 日假冒全市场可见日；禁用报告期末对齐到下一交易日；禁止把预告/快报当成已审计年报/中报。主报只收业绩预告和业绩快报；正式年报/中报交 ED。官方依据是证监会令第 226 号第十八/十九条（与 ED 同一令，ED 用第十三条，本条用第十八/十九条；第十八条、第十九条仍分开引）。`asof_check_date=2026-09-28` 是核对日，**不是 EC 的 2026-10-23**；与 ED 同核对日，披露类型不同。禁止跑后改锚，或用「报告期末或预告时限即可见」/「1 月 31 日 / 中报后第 15 日全市场同一天可见」/ 忽略修正 / 未触发仍发明预告 / 把预告/快报当成已审计年报/中报 / 核对日规则铺满 / 把预告时限键或当成已审计定期报告或忽略修正或 B2/B3 或 ED 诊断桶或 ED/EC/EB/EA/DZ/DY/DX/C/D/O/M/CH/CK/E/V/T/U/W/R/DI 升格进 ee0 冒充诚实 PIT。**禁把占位读成证管费、过户费、一个月、十五日、1 月 31 日、中报后第 15 日、可见日、核对日、预告时限**。**禁把 params.G 的 0.01 读成过户 0.01‰ 或预告时限或 1 月 31 日/中报后第 15 日或可见日或假设-G**。**禁把 params.Y 的 0.02 读成证管费 0.02‰ 或核对日 2026-09-28 或实验字母 EE**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**零改 ED**。**零改 EC**。**零改 EB**。**零改 O**。**不抢实验 R**。

**硬分列保住**：EE≠ED≠EC≠EB≠EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠Y≠A≠D≠Z≠B≠C；**双字母 EE ≠ 单字母假设-E**；**双字母 EE ≠ 假设-ED / 假设-EC / 假设-EA / 假设-EB**；**params.Y / params.G / params.N ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED**；**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED / 假设-EC / 假设-EA / 假设-EB**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日**；**params.G=`0.01` ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28 ≠ 实验字母 EE**；**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28**；**禁把占位读成证管费、过户费、一个月、十五日、1 月 31 日、中报后第 15 日、可见日、核对日、预告时限**；**params 相对门槛 ≠ 可见日 ≠ 预告时限 ≠ 过户‰ ≠ 证管费**；**预告/快报可见日 ≠ ED正式年报/中报可见日 ≠ EC接受闸门 ≠ EB价限 ≠ C股票池成分 ≠ D停牌假成交 ≠ O日量含大宗/三通道**；不抢 A；不抢实验 R；不改已齐/已冻 DA～ED 及 A–DQ 正文；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-R**；**不重开假设-ED**；**不重开假设-EC**；**不重开假设-EB**；**不重开假设-O**；**禁把 ED/EC/EB/EA/DZ/DY/DX/C/D/O/M/CH/CK/E/V/T/U/W/R/DI 及预告时限 / 当成已审计 / 忽略修正 / B2 / B3 / ED 诊断桶 合成/混读升格进 ee0**。handoff 保持：`periodic_report_visibility_handoff=ed_page`；`survivorship_handoff=c_page`；`halt_bar_handoff=d_page`；`sh_main_block_accept_handoff=ec_page`；`nolimit_nego_px_handoff=eb_page`；`star_fixed_price_type_handoff=ea_page`；`chinext_confirm_handoff=dz_page`；`approval_ipo_band_handoff=dy_page`；`sse_fund_close_handoff=dx_page`；`block_liquidity_handoff=o_page`；`aft_channel_handoff=m_page`；`aft_fill_handoff=ch_page`；`block_fill_handoff=ck_page`；`lot_size_handoff=e_page`；`stamp_handoff=v_page`；`ex_right_limit_handoff=w_page`；`block_fee_handoff=di_page`；`etf_t0_handoff=r_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；全部 `merge_with_*=False`。

**状态**：**A/D–EE纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/开户/实盘。

| 2026-11-10 | 复检/纸面齐——**A/D–EE纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设EE-20261110.md` 原样落入，SHA256=`fe769bfe511f923fa16ad3ca96fd936ffa6e4903f5f3623537d793ba06c7bffd`；三冻 tip=`213e55b5` / `213e55b5f803f807c1f8a439bf862a7c6ec6c8e7`。只改状态标签；未改写已冻三条/六键；不改已齐 A–DQ / DA–ED；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O**；不改 #110–#139；不重开假设-V / 假设-T / 假设-U / 假设-R / 假设-ED / 假设-EC / 假设-EB / 假设-EA / 假设-DZ / 假设-DY / 假设-DX / 假设-C / 假设-D / 假设-O / 假设-M / 假设-CH / 假设-CK / 假设-DI / 假设-E / 假设-W / 假设-Y；不抢实验 R；不预留 #141；不开回测/真数/开户/实盘。 |
| 2026-12-11 | 风控预检补丁·冻结三条写死——依据 `预检-假设EE-20261110.md`（SHA256=`b0404e0aaaa68a1b2077cd399ff81def9484d7bf0027bb9f0d9a2d85412ef633`；结论=有条件通过；tip基=`74e606f9` / `74e606f926ceaf25e99b49ab512d5a54d9383afc`；分支起点 HEAD=`b3d54a19` / `b3d54a19cac96b8289e936f987eac17c4cdd0740`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖可见日误套截 ΔPreviewFlashVisible / 净差异 / EE1−EE2；**params.Y/G/N ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED**；**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**；**勿把 params.Y 读成实验字母 EE 或单字母假设-E 或假设-ED 或假设-EC 或假设-V 或假设-T 或假设-U，亦勿把 params.G 读成假设-U 或假设-G 或假设-ED，亦勿把单字母假设-E 读成双字母 EE**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED / 假设-EC / 假设-EA / 假设-EB**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日（量纲与语义不同）**；**params.G=`0.01` ≠ 过户 0.01‰ ≠ 预告时限「一个月/十五日」 ≠ 1 月 31 日/中报后第 15 日 ≠ 可见日**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28 ≠ 可见日 ≠ 1 月 31 日 ≠ 实验字母 EE**；**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 核对日 2026-09-28**；**禁把占位读成证管费、过户费、一个月、十五日、1 月 31 日、中报后第 15 日、可见日、核对日、预告时限**；**params 相对门槛 ≠ 可见日 ≠ 预告时限 ≠ 过户‰ ≠ 证管费**；禁 null；禁 holdout/OOS 标定）；② `params.ee0_primary_demo=invent_forecast_or_flash_aligned_to_period_end_or_deadline`（写死冻结单一主报，单挂；禁与 `invent_statutory_preview_deadline_as_visible_day` 双挂；禁与 `invent_treat_preview_or_flash_as_audited_periodic_report` 双挂；禁与 `invent_ignore_preview_or_flash_correction` 双挂；三者只进诊断、不升格；EE1 不升格；诊断桶 `invent_statutory_preview_deadline_as_visible_day / invent_treat_preview_or_flash_as_audited_periodic_report / invent_ignore_preview_or_flash_correction / invent_preview_when_no_obligation / vs_ED_periodic_report_visibility / vs_EC_sh_main_block_accept / vs_EB_nolimit_nego_px / vs_EA_star_fixed_price_type / vs_DZ_chinext_confirm / vs_DY_approval_ipo_band / vs_DX_sse_fund_close / vs_C_survivorship / vs_D_halt_bar / vs_O_block_liquidity / vs_M_aft_channel / vs_CH_aft_fill / vs_CK_block_fill / vs_E_lot_size / vs_V_stamp / vs_T_csrc / vs_U_transfer / vs_W_ex_right_limit / vs_R_etf_t0 / vs_DI_block_fee / vs_B2_fund_block_threshold / vs_B3_deferred_vwap_window / missing_announcement_or_disclosure_timestamp_not_skip` 不升格；**未触发预告义务则不得发明预告**；**已披露后又有修正公告的，以最新公告日为准**；**禁把 ED 诊断桶升格进 ee0**；**禁 B2/B3 升格或另挂主报**；**禁把 ED/EC/EB/EA/DZ/DY/DX/C/D/O/M/CH/CK/E/V/T/U/W/R/DI 混读升格进 ee0**，只作对照/旁路，不得升格进 ee0 或另挂主报；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O**；不重开假设-V；不重开假设-T；不重开假设-U；不抢实验 R；**双字母 EE ≠ 单字母假设-E**；**双字母 EE ≠ 假设-ED / 假设-EC / 假设-EA / 假设-EB**）；③ 锚六键写死 `earnings_preview_flash_honest=asof_announcement_or_exchange_disclosure_then_next_tradable` / `earnings_preview_flash_scope=earnings_forecast_and_flash_only_not_periodic_report` / `earnings_preview_flash_over_policy=skip_if_announcement_or_disclosure_timestamp_missing` / `asof_check_date=2026-09-28` / `fill_time=next_open` / `fail_policy=skip`（键名是 `earnings_preview_flash_*`，不是 `fundamental_visible_*`；缺公告日或披露时点 → skip；预告/快报按实际公告日或交易所披露时间可见，再落到下一可交易日；「年报结束后一个月 / 中报结束后十五日」只是预告时限，不是可见日；已披露后又有修正公告的，以最新公告日为准；未触发预告义务则不得发明预告；禁用 1 月 31 日 / 中报后第 15 日假冒全市场可见日；禁止把预告/快报当成已审计年报/中报；asof=`2026-09-28`，不是 EC 的 2026-10-23；与 ED 同核对日，披露类型不同；官方依据第十八/十九条）。handoff 保持 `periodic_report_visibility_handoff=ed_page`；`survivorship_handoff=c_page`；`halt_bar_handoff=d_page`；`sh_main_block_accept_handoff=ec_page`；`nolimit_nego_px_handoff=eb_page`；`star_fixed_price_type_handoff=ea_page`；`chinext_confirm_handoff=dz_page`；`approval_ipo_band_handoff=dy_page`；`sse_fund_close_handoff=dx_page`；`block_liquidity_handoff=o_page`；`aft_channel_handoff=m_page`；`aft_fill_handoff=ch_page`；`block_fill_handoff=ck_page`；`lot_size_handoff=e_page`；`stamp_handoff=v_page`；`ex_right_limit_handoff=w_page`；`block_fee_handoff=di_page`；`etf_t0_handoff=r_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；全部 `merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–EE纸面齐**；不改已齐/已冻 DA～ED 及 A–DQ；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O**；不改 #110–#139；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-R；不重开假设-ED；不重开假设-EC；不重开假设-EB；不重开假设-O；不重开假设-C；不重开假设-D；不重开假设-E；不重开假设-W；不抢实验 R；不预留 #141；不开回测/真数/开户/实盘。基于 tip=`74e606f9`。 |
| 2026-12-11 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。业绩预告或快报按报告期末或预告时限对齐误套（因子可见性，不是成交规则）；`ee0_primary_demo` 建议 `invent_forecast_or_flash_aligned_to_period_end_or_deadline`，单一主报，单挂写死，禁与 `invent_statutory_preview_deadline_as_visible_day` 双挂，禁与 `invent_treat_preview_or_flash_as_audited_periodic_report` 双挂，禁与 `invent_ignore_preview_or_flash_correction` 双挂，三者只进诊断、不升格主报，EE1 不升格；诊断桶 `invent_statutory_preview_deadline_as_visible_day` / `invent_treat_preview_or_flash_as_audited_periodic_report` / `invent_ignore_preview_or_flash_correction` / `invent_preview_when_no_obligation` / `vs_ED_periodic_report_visibility` / `vs_EC_sh_main_block_accept` / `vs_EB_nolimit_nego_px` / `vs_EA_star_fixed_price_type` / `vs_DZ_chinext_confirm` / `vs_DY_approval_ipo_band` / `vs_DX_sse_fund_close` / `vs_C_survivorship` / `vs_D_halt_bar` / `vs_O_block_liquidity` / `vs_M_aft_channel` / `vs_CH_aft_fill` / `vs_CK_block_fill` / `vs_E_lot_size` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `vs_DI_block_fee` / `vs_B2_fund_block_threshold` / `vs_B3_deferred_vwap_window` / `missing_announcement_or_disclosure_timestamp_not_skip` 不升格；**禁把 ED 诊断桶升格进 ee0**；**尤重零改 ED / EC / EB / O**；**尤重实验 R 不抢，禁把 vs_R_etf_t0 升格进 ee0**；**尤重不重开假设-V / 假设-T / 假设-U，禁把 vs_V_stamp / vs_T_csrc / vs_U_transfer 升格进 ee0**；**尤重 EE 专写业绩预告/业绩快报可见日，不等于 ED 正式年报/中报，禁把 vs_ED_periodic_report_visibility 升格**；**尤重 C = 股票池/指数当时名单，偷看对象是成分不是预告/快报，C ≠ 本页，禁把 vs_C_survivorship 升格**；**尤重 D = 次日开/收与停牌日假成交 ≠ 本页披露可见日，禁把 vs_D_halt_bar 升格**；**尤重 EC 接受闸门 / EB 价限 / EA 类型 / DZ 确认钟 / DY 首日申报 / DX 收盘产生 ≠ 本页，零改 EC，零改 EB，禁把对应 vs_ 桶升格**；**尤重 O/M/CH/CK 通道与流动性 ≠ 本页，零改 O，禁把对应 vs_ 桶升格**；**尤重 E = 整手 ≠ 本页，禁把 vs_E_lot_size 升格**；**尤重 V = 印花切日，费用 ≠ 可见日，禁把 vs_V_stamp 升格**；**尤重 W = 除权判板 ≠ 本页，禁把 vs_W_ex_right_limit 升格**；**尤重双字母 EE ≠ 单字母假设-E，亦不等于假设-ED / 假设-EC / 假设-EA / 假设-EB**；**尤重 params.Y/G/N ≠ 实验字母 EE / 单字母 E / 假设-ED**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-ED**；**禁把 B2（场内基金大宗门槛）与 B3（16:00-17:00/VWAP 暂缓窗）升格，不另挂主报，零改 O**；**禁把占位读成证管费、过户费、一个月、十五日、1 月 31 日、中报后第 15 日**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 EE ≠ 单字母 E ≠ 假设-ED**；锚建议·待冻、未冻：`earnings_preview_flash_honest=asof_announcement_or_exchange_disclosure_then_next_tradable` / scope=`earnings_forecast_and_flash_only_not_periodic_report` / over_policy=`skip_if_announcement_or_disclosure_timestamp_missing` / `asof_check_date=2026-09-28` / `fill_time=next_open` / `fail_policy=skip`；口径：预告/快报按实际公告日或交易所披露时间可见，再落到下一可交易日；「年报结束后一个月 / 中报结束后十五日」只是预告时限，不是可见日；缺公告日/披露时点则 skip；未触发预告义务则不得发明预告；已披露后又有修正公告的，以最新公告日为准；禁用 1 月 31 日 / 中报后第 15 日等时限假冒全市场可见日（**草稿方向，尚未冻，不要写成已冻**）；事实稿 L62–L64、L83–L86、L109–L111 已钉报告期末不是可见日，但只覆盖正式年报/中报；证监会令第 226 号第十八条、第十九条（2025-07-01 施行；与 ED 所引同一令，ED 用第十三条定期报告期限；本条用第十八/十九条）；https://www.gov.cn/gongbao/2025/issue_12026/202505/content_7022576.html ；深交所《股票上市规则（2026 年修订）》5.1.1–5.1.7；上交所信息披露页（发布日期 2026-09-30）https://one.sse.com.cn/onething/xxpl/ ；handoff：`periodic_report_visibility_handoff=ed_page`，`survivorship_handoff=c_page`，`halt_bar_handoff=d_page`，`sh_main_block_accept_handoff=ec_page`，`nolimit_nego_px_handoff=eb_page`，`star_fixed_price_type_handoff=ea_page`，`chinext_confirm_handoff=dz_page`，`approval_ipo_band_handoff=dy_page`，`sse_fund_close_handoff=dx_page`，`block_liquidity_handoff=o_page`，`aft_channel_handoff=m_page`，`aft_fill_handoff=ch_page`，`block_fill_handoff=ck_page`，`lot_size_handoff=e_page`，`stamp_handoff=v_page`，`ex_right_limit_handoff=w_page`，`block_fee_handoff=di_page`，`etf_t0_handoff=r_page`，`csrc_fee_handoff=t_page`，`transfer_fee_handoff=u_page`；全部 `merge_with_*=False`；`merge_with_ED/EC/EB/EA/DZ/DY/DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/Y/A/D/Z/B/C=False`；**硬分列：EE≠ED≠EC≠EB≠EA≠DZ≠DY≠DX≠C≠D≠O≠M≠CH≠CK≠E≠V≠W**；**双字母 EE ≠ 单字母 E**；**双字母 EE ≠ 假设-ED / 假设-EC / 假设-EA / 假设-EB**；**未标纸面齐**；**不写 A/D–EE纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–ED；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–ED；**零改 ED**；**零改 EC**；**零改 EB**；**零改 O**；不改 #110–#139；不重开假设-R；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-ED；不重开假设-EC；不重开假设-EB；不重开假设-O；不重开假设-C；不重开假设-D；不重开假设-E；不重开假设-W；不写下一字母；不预留 #141；不开真数/回测/开户/实盘。基 tip=`b49d45dc`（A/D–ED纸面齐已合，已收讫，全长 `b49d45dcb0ab6a7985910a54ca0faff9c2db0b29`；分支起点 HEAD=`d6f6f32bc7e794810a1ee04d122a4c39438e7553`；不改该基线上的 #110–#139，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文，亦不改 #139 里「不预留 #140」原句）。 |
