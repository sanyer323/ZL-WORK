# 假设-EB · 无板证券协议大宗价限误套（成交规则）

更新：2026-12-08  
来源：总管线 / 基 tip=`d462923` / 全长 `d4629238a86b70c7f66761d5e554d01d2e9e7d6d`（A/D–EA纸面齐已合）；**不改已冻 A–DQ / DA–EA**；**零改 EA**；**不改假设-EA 正文/预检/复检**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-DT / 假设-DU / 假设-DV / 假设-DW / 假设-DX / 假设-DY / 假设-DZ / 假设-EA / 假设-S / 假设-AX / 假设-AY / 假设-AW / 假设-T / 假设-U / 假设-V / 假设-W / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-E / 假设-F / 假设-J / 假设-G / 假设-CI / 假设-CK / 假设-Y / 假设-A / 假设-D / 假设-X / 假设-Z 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ / 假设-AI / 假设-I / 假设-AQ / 假设-AG）；**不改假设-B**（勿复用·无独立正文，亦不新建）；**不重开假设-R**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-O**；**不重开假设-CK**；**不重开假设-DZ**；**不重开假设-EA**；**不重开假设-AI**；**不重开假设-I**；**不重开假设-AQ**；**不重开假设-G**；**不重开假设-DY**；**不重开假设-AG**；**不重开假设-DI**；**不重开假设-E**；**不重开假设-B**；**不重开假设-Y**；**不重开假设-D**；**不重开假设-W**；**不重开假设-X**；**不重开假设-AY**）后写下一草稿 EB；清单 #136=EA，本页占用 **#137=EB**；选题是回测把 **无板证券协议大宗价限**套错（诚实方向：无板证券协议大宗价不得高于当日竞价实时成交均价 **120%** 与已成交最高价孰低，不得低于均价 **80%** 与已成交最低价孰高；上交所 3.6.10 / 深交所 3.5.4；缺实时均价 / 已成交最高最低价 / 是否有板标记则 skip；禁止无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报；禁止与有板主病半泄露双挂）；假设-AI 只收无板日集合竞价有效申报范围，假设-I 只收连续竞价价格笼子，假设-AQ 只收临停阶段误套连续笼子，假设-G 只收无板标签（无板日误套板块默认板），假设-AG 只收超涨跌停价无效申报，假设-DY 只收核准制主板新股首日申报带，假设-O 只收日量含大宗与三通道假流动性，假设-CK 只收协议大宗假全额可成，假设-DZ 只收创业板协议大宗确认钟，假设-EA 只收科创板大宗固定价格类型开关，假设-DI 只收股票大宗经手下浮，假设-R 只收股票 ETF 假 T+0，假设-V 只收股票印花税切日，假设-T 只收股票证管费切日，假设-U 只收股票过户切日，假设-E 只收整手与科创板 200 股，假设-B 无独立正文、勿复用，假设-Y 只收集合竞价量计入日线；**新建实验 EB**；不写下一字母；不预留 #138  
状态：**A/D–EB纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「无板证券协议大宗可以不看均价带」或「有板涨跌幅 / 竞价笼子」当诚实锚；禁止与有板主病半泄露双挂；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–EA**；**零改 EA**；**不改 #110–#136**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 EB（#137）。一句话误开：回测把无板证券的协议大宗价写成 **可以不管当日竞价实时成交均价的 120% 与已成交最高价孰低、也可以不管均价 80% 与已成交最低价孰高**，或拿核对日这道带倒灌到缺字段的日子、倒灌到有板证券，或把无价限、有板当日涨跌幅、竞价有效申报范围 / 连续笼子 / 临停笼子倒灌进主报，或与 AI无板日集合有效申报 / I连续竞价笼子 / AQ临停笼子 / G无板标签 / AG超涨跌停拒单 / DY核准制首日申报带 / O日量含大宗·三通道假流动性 / CK协议大宗假全额可成 / DZ创业板确认钟 / EA科创大宗固定价格类型开关 / DI大宗经手下浮 / R股票ETF假T+0 / V股票印花 / T股票证管费 / U股票过户 / E整手与科创板200股 混读，或缺实时均价 / 已成交最高最低价 / 是否有板标记仍不 skip，系统性改写这笔协议大宗**当时谈妥价能不能落在这道带里**。**禁把 AI/I/AQ/G/DY/O/CK/DZ/EA/DI/R/V/T/U/E 混读升格进 `eb0`**。**禁把 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 升格或与主报双挂**。**禁把 `invent_asof_leak_nolimit_nego_block_px` 与主报双挂**。**禁无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报**。**有板协议大宗价限仅诊断**。

> **字母消歧（硬）**：本页**实验字母 EB** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 EB**；**尤重：`params.Y/G/N` ≠ 实验字母 EB / 单字母 E/B**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**；**勿把 `params.Y` 读成实验字母 EB，亦勿读成单字母假设-E，亦勿读成单字母假设-B，亦勿读成假设-Y，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿读成假设-G**；**尤重：`params.Y` 的 0.02 ≠ 实验字母 EB ≠ 单字母 E/B ≠ 120% ≠ 80% ≠ 均价公式 ≠ 过户‰ ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**（**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**））≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 EB**；**params.G ≠ 假设-G**；**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 120% ≠ 80% ≠ 均价公式 ≠ 120%/80% 带宽**（**params.G=`0.01` ≠ 过户 0.01‰ ≠ 120%/80% 带宽**）——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是均价的 80%，不是均价的 120%，不是「有板」，不是「无板」，也不是过户费率）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 EB**；**params.N ≠ 单字母 E/B**）≠ **`params.Y2`**（写死冻结 0.015；不是 120%，不是 80%，不是均价公式）≠ **单字母实验 E**（整手与科创板 200 股；**双字母 EB ≠ 单字母假设-E；严禁复用假设-E**）≠ **单字母实验 B**（勿复用·无独立正文；**双字母 EB ≠ 单字母假设-B；严禁复用假设-B；不新建假设-B 正文**）≠ **单字母实验 Y**（集合竞价量计入日线；**双字母 EB ≠ 单字母假设-Y；严禁复用假设-Y**；**尤重 params.Y ≠ 实验字母 EB**）≠ **单字母实验 G**（无板标签 / 无板日默认板；**params.G ≠ 假设-G**；**G 无板标签 ≠ 本页谈妥价公式**）≠ **单字母实验 V**（股票印花税切日；**双字母 EB ≠ 单字母假设-V；严禁复用假设-V**；**不重开假设-V**）≠ **单字母实验 U**（股票过户费切日；**双字母 EB ≠ 单字母假设-U；严禁复用假设-U**；**不重开假设-U**）≠ **单字母实验 T**（股票证管费切日；**双字母 EB ≠ 单字母假设-T；严禁复用假设-T**；**不重开假设-T**）≠ **单字母实验 R**（股票 ETF 假 T+0；**双字母 EB ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `eb0`**）≠ **双字母 EA**（科创板大宗固定价格交易类型切日；**零改 EA**；**EB≠EA**；**EA 类型开关 ≠ 本页价限**）≠ **双字母 DZ**（创业板协议大宗确认时点切日；**EB≠DZ**；**DZ 确认钟 ≠ 本页**）≠ **双字母 DY**（核准制主板新股首日申报价格上下限；**EB≠DY**；**DY 申报带 ≠ 本页谈妥价公式**）≠ **双字母 AI**（无板日集合竞价有效申报范围；**竞价有效申报 ≠ 本页协议大宗价限**）≠ **单字母 I**（连续竞价价格笼子；**连续笼子 ≠ 本页协议大宗价限**）≠ **双字母 AQ**（临停阶段误套连续笼子；**临停笼子 ≠ 本页协议大宗价限**）≠ **双字母 AG**（超涨跌停价无效申报；**竞价拒单 ≠ 本页协议大宗价限**）≠ **双字母 O**（大宗日量 / 三通道假流动性；**O 假流动性 ≠ 本页价限**）≠ **双字母 CK**（协议大宗可成交性；**假全额可成 ≠ 本页价限**）≠ **双字母 DI**（股票大宗经手下浮；费率 ≠ 价限）≠ **DQ / DP / DO / DN / DM / DL / DK / DJ / DH / DG / DF / DE / DD / DC / DB / DA**（费用旁路；不并进 `eb0`）≠ **S**（股票经手费切日）≠ **AX**（基金经手费）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债回转/涨跌幅/收盘）≠ **CH / CL / CR / CQ**（可成交性旁路）≠ **F / J / W / AW / AY / X / CI**（取整、临停、除权、收盘集合失败回落、价位、ST 板幅、新股首日可成交）≠ **DW / DV / DU / DT / DS**（行权过户、现金选择权、转债首日临停、整手价位、转股印花）≠ **DX**（沪市基金收盘产生方式切日）≠ **单字母实验 D**（成交时点与停牌）≠ **单字母实验 Z**（融资保证金比例误铺）≠ **单字母实验 A**（涨停可成交性）。**EB≠EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠AI≠AQ≠I≠AG≠Y≠A≠D≠Z≠B**。**双字母 EB ≠ 单字母 E/B**。**双字母 EB ≠ 单字母假设-E / 假设-B**。**params.Y/G/N ≠ 实验字母 EB ≠ 单字母 E/B**。**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**。**禁把占位读成 120%/80%、均价公式、过户‰**。**params 相对门槛 ≠ 120% ≠ 80% ≠ 均价公式 ≠ 过户‰**。**无板证券协议大宗价限 ≠ AI/I/AQ竞价有效申报与笼子 ≠ G无板标签 ≠ DY核准制首日申报带 ≠ AG超涨跌停拒单 ≠ O日量含大宗/三通道假流动性 ≠ CK假全额可成 ≠ DZ创业板确认钟 ≠ EA科创大宗固定价格类型开关 ≠ DI大宗费率 ≠ R股票ETF假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ E整手与科创板200股 ≠ B旧位**。**尤重：实验 R 不抢；禁把 `vs_R_etf_t0` 升格进 `eb0`**。**尤重：不重开假设-V / 假设-T / 假设-U；禁把 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 升格进 `eb0`**。**尤重：有板协议大宗价限仅诊断；禁与无板主报半泄露双挂；禁把 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 升格或双挂**。**尤重：AI/I/AQ 竞价有效申报 / 笼子 ≠ 本页协议大宗价限；禁把 `vs_AI_call_valid_range` / `vs_I_continuous_cage` / `vs_AQ_halt_cage` 升格进 `eb0`**。**尤重：G/DY 无板标签 / 核准制首日申报带 ≠ 本页大宗谈妥价公式；禁把 `vs_G_nolimit_board` / `vs_DY_approval_ipo_band` 升格进 `eb0`**。**尤重：O/CK 假流动性 / 假全额 ≠ 本页价限；禁把 `vs_O_block_liquidity` / `vs_CK_block_fill` 升格进 `eb0`**。**尤重：DZ 确认钟 ≠ 本页；禁把 `vs_DZ_chinext_confirm` 升格进 `eb0`**。**尤重：EA 类型开关 ≠ 本页价限；禁把 `vs_EA_star_fixed_price_type` 升格进 `eb0`；零改 EA**。**尤重：双字母 EB ≠ 单字母假设-E（整手与科创板 200 股）/ 假设-B（勿复用·无独立正文）；禁把 `vs_E_lot_size` 升格进 `eb0`**。**尤重：禁无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报**。**零改 EA**。

### 专节 · 双字母 EB ≠ 单字母假设-E / 假设-B；且 ≠ 假设-AI / 假设-I / 假设-AQ / 假设-G / 假设-DY / 假设-O / 假设-CK / 假设-DZ / 假设-EA / 假设-R / 假设-V / 假设-T / 假设-U（硬）

| 维度 | 对照页 | 本页假设-EB（双字母） |
|------|--------|----------------------|
| 题面 AI | **无涨跌幅日集合竞价有效申报范围**（开盘集合前收盘 900% 以内、上交所另写不低于前收盘 50%；临停与收盘集合是最近成交价上下 10%；假设-AI） | **AI = 竞价簿上这张单的有效申报范围**。本页问的是无板证券**协议大宗谈妥价**相对当日竞价实时均价与已成交最高最低的那道带。集合竞价能挂多远，不是大宗谈妥价公式。**EB≠AI**；**不重开假设-AI**；**不改 AI**；**尤重：禁把 `vs_AI_call_valid_range` 升格进 `eb0`**；`call_valid_range_handoff=ai_page` |
| 题面 I | **连续竞价价格笼子**（买入不超过基准价 102% 与十个价位孰高这一类；假设-I） | **I = 连续竞价限价能挂多远**。笼子基准是买卖一 / 最新成交，不是协议大宗的实时均价 120%/80%。**EB≠I**；**不重开假设-I**；**不改 I**；**尤重：禁把 `vs_I_continuous_cage` 升格进 `eb0`**；`continuous_cage_handoff=i_page` |
| 题面 AQ | **临停阶段误套连续价格笼子**（临停阶段不适用连续笼子两款；假设-AQ） | **AQ = 临停这段还套不套连续笼子**。临停笼子不是无板协议大宗价限。**EB≠AQ**；**不重开假设-AQ**；**不改 AQ**；**尤重：禁把 `vs_AQ_halt_cage` 升格进 `eb0`**；`halt_cage_handoff=aq_page` |
| 题面 G | **无涨跌幅日误套板块默认板**（无板标签被贴上 ±10%/±20%；假设-G） | **G = 这一天有没有板、板被贴错没有**。本页假定「是否有板」这个标记要先在册；标记说无板之后，协议大宗价才走均价带。无板标签本身不是谈妥价公式。`params.G` 的 0.01 也不是假设-G。**EB≠G**；**params.G ≠ 假设-G**；**不重开假设-G**；**不改 G**；**尤重：禁把 `vs_G_nolimit_board` 升格进 `eb0`**；`nolimit_board_handoff=g_page` |
| 题面 AG | **超涨跌停价限价申报仍记成交**（超过涨跌幅或有效申报范围 = 无效；假设-AG） | **AG = 竞价申报越过涨跌幅被记成成交**。有板的涨跌幅拒单不是无板协议大宗的均价带。**EB≠AG**；**不重开假设-AG**；**不改 AG**；**尤重：禁把 `vs_AG_over_limit_reject` 升格进 `eb0`**；`over_limit_reject_handoff=ag_page` |
| 题面 DY | **核准制主板新股首日申报价格上下限**（集合 80%–120%、连续 64%–144%；假设-DY） | 首日申报带是发行价的百分比，不是协议大宗的实时均价带。两套百分数禁止合成。**EB≠DY**；**不重开假设-DY**；**不改 DY**；**尤重：禁把 `vs_DY_approval_ipo_band` 升格进 `eb0`**；`approval_ipo_band_handoff=dy_page` |
| 题面 O | **大宗量价并进竞价 / 三条盘后通道混用**（日成交量含大宗结束后计入的那截；按大宗价回放竞价；三条通道合成一句；假设-O） | **O = 量、价、三通道假流动性**。本页只问无板证券协议大宗**谈妥价落不落在均价带里**。门槛 30 万股 / 200 万元、日量何时计入、三条通道怎么拆，都留在 O。两句禁止合成。**EB≠O**；**不重开假设-O**；**不改 O**；**尤重：禁把 `vs_O_block_liquidity` 升格进 `eb0`**；`block_liquidity_handoff=o_page` |
| 题面 CK | **协议大宗可成交性误开**（默认协议 / 成交申报大宗必能按目标价或谈妥价全额成交；假设-CK） | **CK = 价已经在带里之后，单子能不能打满**。假全额不是价限。带对了也不等于全额成交。**EB≠CK**；**不重开假设-CK**；**不改 CK**；**尤重：禁把 `vs_CK_block_fill` 升格进 `eb0`**；`block_fill_handoff=ck_page` |
| 题面 DZ | **创业板协议大宗确认时点切日**（假设-DZ 已纸面齐） | 确认钟问的是这笔在哪个钟点才确认。本页问的是无板证券谈妥价的上下限。同日落地也不合成一句。**EB≠DZ**；**不重开假设-DZ**；**不改 DZ**；**尤重：禁把 `vs_DZ_chinext_confirm` 升格进 `eb0`**；`chinext_confirm_handoff=dz_page` |
| 题面 EA | **科创板大宗固定价格交易类型切日**（假设-EA 已纸面齐） | EA 只问科创板大宗**有没有固定价格这一种类型**。类型开关不是无板协议大宗的均价带。**零改 EA**。**EB≠EA**；**不重开假设-EA**；**不改 EA 正文/预检/复检**；**尤重：禁把 `vs_EA_star_fixed_price_type` 升格进 `eb0`**；`star_fixed_price_type_handoff=ea_page` |
| 题面 DI | **股票大宗经手下浮误忽略**（假设-DI） | 经手费下浮是成本，不是价限。**EB≠DI**；**不重开假设-DI**；**不改 DI**；**尤重：禁把 `vs_DI_block_fee` 升格进 `eb0`**；`block_fee_handoff=di_page` |
| 题面 半泄露 | 核对日 2026-10-23 已经写着无板协议大宗按均价 120%/80% 与已成交最高最低孰紧 | `invent_asof_leak_nolimit_nego_block_px` 只作半泄露对照。**禁与 `eb0` 双挂**；不得升格并列主报 |
| 题面 有板价限 | **有板证券**的协议 / 成交申报价在**当日涨跌幅限制内**谈（`事实与坑` 2026-10-23），不是均价 120%/80% | 有板这道价限**仅诊断**。诊断桶 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 只标记把有板涨跌幅写成无板均价带，或把无板均价带写成有板涨跌幅。**禁升格进 `eb0`**，**禁与无板主报半泄露双挂** |
| 题面 R | **股票 ETF 假 T+0**（假设-R） | **实验 R 不抢**。ETF 能不能当日回转，和无板协议大宗价限，是两件事。**EB≠R**；**严禁复用假设-R**；**不重开假设-R**；**不改 R**；**尤重：禁把 `vs_R_etf_t0` 升格进 `eb0`**；`etf_t0_handoff=r_page` |
| 题面 V | **股票印花税切日**（假设-V） | **不重开假设-V**。印花切日 ≠ 价限。占位不是印花税率，也不是 120%。**EB≠V**；**params 字母 ≠ 假设-V**；**不改 V**；**尤重：禁把 `vs_V_stamp` 升格进 `eb0`**；`stamp_handoff=v_page` |
| 题面 T | **股票证管费切日**（假设-T） | **不重开假设-T**。`params.Y` 的 0.02 不是证管费 0.02‰，也不是实验字母 EB，也不是 120%。**EB≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：禁把 `vs_T_csrc` 升格进 `eb0`**；`csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日**（假设-U） | **不重开假设-U**。`params.G` 的 0.01 不是过户 0.01‰，也不是 80%。**EB≠U**；**params 字母 ≠ 假设-U**；**不改 U**；**尤重：禁把 `vs_U_transfer` 升格进 `eb0`**；`transfer_fee_handoff=u_page` |
| 题面 E | **整手与科创板 200 股**（假设-E） | 科创板买入至少 200 股，是数量闸门。本页问的是无板协议大宗**价限**。**双字母 EB ≠ 单字母假设-E**；**严禁复用假设-E**；**EB≠E**；**尤重：`params.Y/G/N` ≠ 单字母 E**；**不重开假设-E**；**不改 E**；**尤重：禁把 `vs_E_lot_size` 升格进 `eb0`**；`lot_size_handoff=e_page` |
| 题面 B | **单字母假设-B**（勿复用·无独立正文） | 没有一页独立正文可当本页的前身。**双字母 EB ≠ 单字母假设-B**；**严禁复用假设-B**；**EB≠B**；**尤重：`params.Y/G/N` ≠ 单字母 B**；**不重开假设-B**；**不改假设-B**；**不新建假设-B 正文** |
| 题面 Y | **集合竞价量计入日线**（假设-Y） | 集合竞价量进不进日线，不是谈妥价公式。`params.Y` 的 0.02 不是实验字母 EB，也不是假设-Y。**EB≠Y**；**params 字母 ≠ 假设-Y**；**不重开假设-Y**；**不改 Y** |
| 题面 DX / DW / DV / DU / DT / DS / DQ–DA / S / AX / AC / Q / M / CH / CL / CR / CQ / F / J / W / AW / AY / X / CI / A / D / Z | 费用、整手价位、可成交性、临停、开收时点、保证金比例、盘后通道等旁路 | 全部不并进 `eb0`。**EB≠EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠AI≠AQ≠I≠AG≠Y≠A≠D≠Z≠B**。不改这些页 |
| 题面 A | **涨停可成交 / 板上枯竭**（假设-A） | 板上能不能成交，不是无板协议大宗价限。**EB≠A**；**不抢 A 真数队列**；**不改 A** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_nolimit_nego_block_px_ignore_mean120_80_band`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_nolimit_nego_block_px` 双挂；禁与 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 双挂；EB1 不升格；诊断桶不升格） |
| 文档 | 清单实验 EA 及上表各页（**只读；禁止改写**） | `假设-EB-无板证券协议大宗价限误套.md`（新建） |
| 预检键 | 实验字母 EA / DZ / … / E / B / O / V / T / U / R / Y / G | 实验字母 **EB** / `eb0_primary_demo`；**不得**占用或改写上述预检键；**params.Y/G/N ≠ 实验字母 EB** |

**禁止**：把 EB 写成「AI / I / AQ / G / O / CK / EA / R / E / B 的续篇」；把「核对日无板协议大宗已经按均价 120%/80% 与最高最低孰紧 / 有板证券在涨跌幅内谈 / 竞价笼子已经写过」写成「本页价限已诚实」；把实验字母 EB 与单字母 E/B 或 params.Y/G/N 混读；**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**；**禁把占位 `0.02/0.01/0.05/0.015` 读成 120%/80%、均价公式、过户‰**；**实验 R 不抢**；**不重开假设-V / 假设-T / 假设-U**；**有板协议大宗价限仅诊断**；**禁与无板主报半泄露双挂**；**AI/I/AQ 竞价有效申报 / 笼子 ≠ 本页协议大宗价限**；**G/DY 无板标签 / 核准制首日申报带 ≠ 本页大宗谈妥价公式**；**O/CK 假流动性 / 假全额 ≠ 本页价限**；**DZ 确认钟 ≠ 本页**；**EA 类型开关 ≠ 本页价限**；**零改 EA**；**禁无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报**；**禁把 AI/I/AQ/G/DY/AG/O/CK/DZ/EA/DI/R/V/T/U/E 的诊断升格进 `eb0`**；把 `invent_asof_leak_nolimit_nego_block_px` 与主报双挂；把 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 升格或双挂；缺实时均价 / 已成交最高最低价 / 是否有板标记仍硬填。本页主键只用 `eb0` / `eb1` / `eb2` 与 `nolimit_nego_block_px_*`。不写下一字母。不预留 #138。**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–EA；勿再只改清单）。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测把 **无板证券的协议大宗价**写成 **可以不看当日竞价实时成交均价的 120% 与已成交最高价孰低、也可以不看均价 80% 与已成交最低价孰高**，或与 AI/I/AQ 的竞价有效申报和笼子、G 的无板标签、AG 的超涨跌停拒单、DY 的核准制首日申报带、O 的日量含大宗和三通道、CK 的假全额可成、DZ 的创业板确认钟、EA 的科创大宗类型开关、DI 的大宗费率、R 的假 T+0、V/T/U 的费用切日、E 的整手混读，或缺实时均价 / 已成交最高最低价 / 是否有板标记仍不 skip，相对「缺字段则 skip；无板证券协议大宗价不得高于均价 120% 与已成交最高价孰低，不得低于均价 80% 与已成交最低价孰高；上交所 3.6.10 / 深交所 3.5.4；不把无价限、有板涨跌幅、竞价笼子倒灌进主报；不与有板主病半泄露双挂」的诚实组，会**系统性改写这笔协议大宗当时谈妥价能不能落在这道带里**——带外的价被写成可报，或有板的涨跌幅被写成无板均价带。方向是相对诚实锚偏误。

核对日方向（随锚写死；禁把占位读成 120%/80%、均价公式、过户‰）：`事实与坑` 2026-10-23 写明，有板证券的协议 / 成交申报价由买卖双方在当日涨跌幅限制内谈；无板证券不得高于当日竞价实时成交均价的 120% 与已成交最高价孰低，不得低于均价 80% 与已成交最低价孰高。均价 = 已成交金额 / 已成交股数，四舍五入到最小价位。上交所 3.6.10；深交所 3.5.4。本页只收**无板**这一道。有板「在涨跌幅内谈」留在诊断桶，不进主报。竞价有效申报范围留在 AI，连续笼子留在 I，临停笼子留在 AQ，无板标签留在 G，超涨跌停拒单留在 AG，核准制首日申报带留在 DY。日量与三通道留在 O，能不能打满留在 CK，确认钟留在 DZ，科创固定价格类型开关留在 EA。缺实时均价、已成交最高最低价，或分不清有没有板，整笔 skip。**禁把占位读成 120%/80%、均价公式、过户‰**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**。**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**。

证伪方向：若天真组 / 半泄露组相对诚实组的价限误套截在标定噪声带内可忽略，且「有板价限误当无板均价带 / 核对日泄露 / vs AI·I·AQ·G·AG·DY·O·CK·DZ·EA·DI·R·V·T·U·E」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · eb0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 EB ≠ 单字母假设-E / 假设-B**；勿把 params.Y 读成实验字母 EB，亦勿读成单字母假设-E，亦勿读成单字母假设-B，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U
# 【消歧】尤重：params.Y/G/N ≠ 实验字母 EB / 单字母 E/B
# 【消歧】params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G
# 【消歧】尤重：params.Y 的 0.02 ≠ 实验字母 EB ≠ 单字母 E/B ≠ 120% ≠ 80% ≠ 均价公式 ≠ 过户‰ ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23；**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**
# 【消歧】尤重：params.G 的 0.01 ≠ 过户 0.01‰ ≠ 120% ≠ 80% ≠ 均价公式 ≠ 假设-G ≠ 120%/80% 带宽（无量纲相对门槛 ≠ 过户费率 ≠ 均价带 ≠ 120%/80% 带宽）；**params.G=`0.01` ≠ 过户 0.01‰ ≠ 120%/80% 带宽**
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 EB ≠ 单字母 E/B**
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成 120%/80%、均价公式、过户‰
# 【消歧】params 相对门槛 ≠ 120% ≠ 80% ≠ 均价公式 ≠ 过户‰
# 【消歧】三条已冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值
# params.Y2                               写死冻结 0.015（不是 120%，不是 80%，不是均价公式，不是过户‰，不是证管费 0.02‰，不是核对日）
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：价限误套截 ΔNolimitNegoBlockPx / 净差异 / EB1−EB2；**params.Y/G/N ≠ 实验字母 EB ≠ 单字母 E/B**；**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**；**尤重 params.G=`0.01` ≠ 过户 0.01‰ ≠ 120%/80% 带宽**；**尤重 params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 120% ≠ 80% ≠ 均价公式 ≠ 假设-G**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23 ≠ 实验字母 EB ≠ 单字母 E/B**；**禁把占位读成 120%/80%、均价公式、过户‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        写死冻结 next_open
#   这是信号腿的成交时点建议，不是协议大宗价限，也不是 120% 或 80%
#   双字母 EB ≠ 单字母假设-E / 假设-B
# params.asof_check_date                  写死冻结 2026-10-23（这是核对日，不是占位，也不是 120%，也不是均价带）
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.nolimit_nego_block_px_honest     写死冻结 pit_mean120_hi_lo_whichever_tighter
#   诚实锚方向（已写死冻结）：
#   缺实时均价 / 已成交最高最低价 / 是否有板标记 → skip
#   无板证券协议大宗价：不得高于当日竞价实时成交均价 120% 与已成交最高价孰低
#   不得低于均价 80% 与已成交最低价孰高
#   均价 = 已成交金额 / 已成交股数，四舍五入到最小价位
#   上交所 3.6.10 / 深交所 3.5.4
#   禁止无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报
#   禁止与有板主病半泄露双挂
#   禁止把占位读成 120%/80%、均价公式或过户‰
#   锚名字里的 120/80 是机制方向，不是 params.Y/G/N/Y2
#   枚举已写死冻结
# params.nolimit_nego_block_px_scope      写死冻结 nolimit_security_nego_block_price_band_only
#   只看无板证券协议大宗价限
#   不是竞价有效申报范围，不是连续笼子，不是临停笼子
#   不是无板标签本身，不是有板涨跌幅，不是能不能打满
# params.nolimit_nego_block_px_over_policy  写死冻结 skip_if_vwap_or_hi_lo_or_board_flag_missing
#   缺实时均价 / 已成交最高最低价 / 是否有板标记则 skip
# params.call_valid_range_handoff         建议 ai_page
#   无板日集合有效申报范围交 AI；AI ≠ 本页协议大宗价限；不重开假设-AI；不改 AI
#   诊断桶 vs_AI_call_valid_range 不得升格进 eb0
# params.continuous_cage_handoff          建议 i_page
#   连续竞价笼子交 I；I ≠ 本页协议大宗价限；不重开假设-I；不改 I
#   诊断桶 vs_I_continuous_cage 不得升格进 eb0
# params.halt_cage_handoff                建议 aq_page
#   临停笼子交 AQ；AQ ≠ 本页协议大宗价限；不重开假设-AQ；不改 AQ
#   诊断桶 vs_AQ_halt_cage 不得升格进 eb0
# params.nolimit_board_handoff            建议 g_page
#   无板标签交 G；G ≠ 本页谈妥价公式；params.G ≠ 假设-G；不重开假设-G；不改 G
#   诊断桶 vs_G_nolimit_board 不得升格进 eb0
# params.over_limit_reject_handoff        建议 ag_page
#   超涨跌停拒单交 AG；AG ≠ 本页协议大宗价限；不重开假设-AG；不改 AG
#   诊断桶 vs_AG_over_limit_reject 不得升格进 eb0
# params.approval_ipo_band_handoff        建议 dy_page
#   核准制首日申报带交 DY；DY ≠ 本页谈妥价公式；不重开假设-DY；不改 DY
#   诊断桶 vs_DY_approval_ipo_band 不得升格进 eb0
# params.block_liquidity_handoff          建议 o_page
#   日量含大宗 / 三通道交 O；O 假流动性 ≠ 本页价限；不重开假设-O；不改 O
#   诊断桶 vs_O_block_liquidity 不得升格进 eb0
# params.block_fill_handoff               建议 ck_page
#   协议大宗可成交性交 CK；CK 假全额 ≠ 本页价限；不重开假设-CK；不改 CK
#   诊断桶 vs_CK_block_fill 不得升格进 eb0
# params.chinext_confirm_handoff          建议 dz_page
#   创业板协议大宗确认钟交 DZ；DZ 确认钟 ≠ 本页；不重开假设-DZ；不改 DZ
#   诊断桶 vs_DZ_chinext_confirm 不得升格进 eb0
# params.star_fixed_price_type_handoff    建议 ea_page
#   科创大宗固定价格类型开关交 EA；零改 EA；不重开假设-EA；不改 EA 正文/预检/复检
#   诊断桶 vs_EA_star_fixed_price_type 不得升格进 eb0
# params.block_fee_handoff                建议 di_page
#   股票大宗经手下浮交 DI；费率 ≠ 价限；不重开假设-DI；不改 DI
#   诊断桶 vs_DI_block_fee 不得升格进 eb0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 eb0；不改 R
#   诊断桶 vs_R_etf_t0 不得升格进 eb0
# params.stamp_handoff                    建议 v_page
#   股票印花切日交 V；不重开假设-V；params 字母 ≠ 假设-V；不改 V
#   诊断桶 vs_V_stamp 不得升格进 eb0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；params 字母 ≠ 假设-T；不改 T
#   诊断桶 vs_T_csrc 不得升格进 eb0
# params.transfer_fee_handoff             建议 u_page
#   股票过户切日交 U；不重开假设-U；params 字母 ≠ 假设-U；不改 U
#   诊断桶 vs_U_transfer 不得升格进 eb0
# params.lot_size_handoff                 建议 e_page
#   整手与科创板 200 股交 E；双字母 EB ≠ 单字母假设-E；不重开假设-E；不改 E
#   诊断桶 vs_E_lot_size 不得升格进 eb0
# params.eb0_primary_demo                 写死冻结 invent_nolimit_nego_block_px_ignore_mean120_80_band
#   单一主报写死，单挂
#   禁与 invent_asof_leak_nolimit_nego_block_px 双挂
#   禁与 invent_limit_board_nego_block_px_as_nolimit_mean_band 双挂
#   EB1 不升格；诊断桶不升格
#   半泄露名只作对照，不得升格进 eb0，不得双挂
#   有板协议大宗价限仅诊断，不得升格，不得与无板主报半泄露双挂
#   禁止无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报
#   诊断桶 invent_limit_board_nego_block_px_as_nolimit_mean_band / vs_AI_call_valid_range / vs_I_continuous_cage / vs_AQ_halt_cage / vs_G_nolimit_board / vs_AG_over_limit_reject / vs_DY_approval_ipo_band / vs_O_block_liquidity / vs_CK_block_fill / vs_DZ_chinext_confirm / vs_EA_star_fixed_price_type / vs_DI_block_fee / vs_R_etf_t0 / vs_V_stamp / vs_T_csrc / vs_U_transfer / vs_E_lot_size / missing_vwap_or_hi_lo_or_board_flag_not_skip 不得升格进 eb0
#   禁把以下升格进 eb0：AI/I/AQ 竞价有效申报/笼子 / G无板标签 / DY核准制首日申报带 / O/CK 假流动性假全额 / DZ确认钟 / EA类型开关 / R假T+0 / V印花 / T证管费 / U过户 / 无价限/有板涨跌幅/竞价笼子倒灌
#   尤重：实验 R 不抢
#   尤重：不重开假设-V / 假设-T / 假设-U
#   尤重：有板价限不升格、不双挂
#   尤重：AI/I/AQ/G/DY/O/CK/DZ/EA 不升格
#   尤重：零改 EA
#   尤重：双字母 EB ≠ 单字母 E/B；禁把 E 升格进 eb0
# params.eb0_invent_nolimit_nego_block_px_ignore_mean120_80_band 建议 True
# params.eb1_asof_leak_nolimit_nego_block_px_only 建议 True
#   半泄露对照；EB1 不升格并列主报；不得把 invent_asof_leak_nolimit_nego_block_px 写进 eb0
# params.eb2_pit_mean120_hi_lo_whichever_tighter 建议 True
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
# params.merge_with_AI                    建议 False
# params.merge_with_AQ                    建议 False
# params.merge_with_I                     建议 False
# params.merge_with_AG                    建议 False
# params.merge_with_Y                     建议 False
# params.merge_with_A                     建议 False
# params.merge_with_D                     建议 False
# params.merge_with_Z                     建议 False
# params.merge_with_B                     建议 False
# params.missing_vwap_or_hi_lo_or_board_flag_policy 建议 skip
# params.day_freq_proxy                   建议 nolimit_nego_block_px_sensitivity
# params.universe_rule                    建议 nolimit_nego_block_px_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_eb_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 EB；勿读成单字母 E/B
#   不另挂主报，不预留 #138，不写下一字母
```

### 2.2 三组对照（EB0 / EB1 / EB2）

组名 EB0 / EB1 / EB2 是本页三组，≠ 单字母实验 E（整手与科创板 200 股），亦 ≠ 单字母实验 B（勿复用·无独立正文）。**双字母 EB ≠ 单字母假设-E / 假设-B**。**params.Y/G/N ≠ 实验字母 EB ≠ 单字母 E/B**。**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**。

| 组 | 角色 | 口径 |
|----|------|------|
| EB0 | 天真 / 无板协议大宗价不看均价 120%/80% 与已成交最高最低孰紧 | 按 `eb0_primary_demo` **写死冻结**单一主报 `invent_nolimit_nego_block_px_ignore_mean120_80_band`（单挂写死）：把无板证券的协议大宗价写成可以不管这道带。**禁**与 `invent_asof_leak_nolimit_nego_block_px` 双挂。**禁**与 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 双挂。**禁把有板涨跌幅、AI/I/AQ 笼子、G/DY、O/CK、DZ、EA、R/V/T/U/E 合成进 `eb0`**。**禁无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报** |
| EB1 | 半泄露 | 仅用核对日「无板协议大宗已经按均价 120%/80% 与已成交最高最低孰紧」把这条铺到缺字段的日子、铺到有板证券、或铺成全历史无条件规则（`invent_asof_leak_nolimit_nego_block_px`）。**不得升格并列主报**，不得写进 `eb0`，不得双挂。**禁止与有板主病半泄露双挂** |
| EB2 | 诚实 / 无板协议大宗价取均价带与已成交最高最低孰紧 | `nolimit_nego_block_px_honest=pit_mean120_hi_lo_whichever_tighter`（写死冻结）：缺实时均价/已成交最高最低价/是否有板标记则 skip；无板证券协议大宗价不得高于均价 120% 与已成交最高价孰低，不得低于均价 80% 与已成交最低价孰高。竞价有效申报只消费 AI，连续笼子只消费 I，临停笼子只消费 AQ，无板标签只消费 G，超涨跌停拒单只消费 AG，核准制申报带只消费 DY，日量与三通道只消费 O，能不能打满只消费 CK，确认钟只消费 DZ，类型开关只消费 EA，费率只消费 DI，假 T+0 只消费 R，费用只消费 V/T/U，整手只消费 E，或显式旁路 |

把有板价限误当无板均价带、把核对日规则铺满、以及相对 AI/I/AQ/G/AG/DY/O/CK/DZ/EA/DI/R/V/T/U/E 的对照，放进 §4.1 分桶，**只作诊断桶或半泄露对照，不得升格为第二个主报**。`invent_limit_board_nego_block_px_as_nolimit_mean_band` 只标记有板价限与无板均价带互套，**不得进主报，不得双挂**。`invent_asof_leak_nolimit_nego_block_px` 只标记核对日泄露。`vs_AI_call_valid_range` 只标记集合有效申报范围。`vs_I_continuous_cage` 只标记连续笼子。`vs_AQ_halt_cage` 只标记临停笼子。`vs_G_nolimit_board` 只标记无板标签。`vs_AG_over_limit_reject` 只标记超涨跌停拒单。`vs_DY_approval_ipo_band` 只标记核准制申报带。`vs_O_block_liquidity` 只标记日量含大宗 / 三通道。`vs_CK_block_fill` 只标记假全额可成。`vs_DZ_chinext_confirm` 只标记创业板确认钟。`vs_EA_star_fixed_price_type` 只标记科创类型开关，**零改 EA**。`vs_DI_block_fee` 只标记大宗费率。`vs_R_etf_t0` 只标记假 T+0。`vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只标记费用。`vs_E_lot_size` 只标记整手。`missing_vwap_or_hi_lo_or_board_flag_not_skip` 只标记缺字段仍不 skip。这些都**不得升格进 `eb0`**。

### 2.3 价限可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-23`；fill_time **写死冻结** `next_open`（这是信号腿，不是价限）；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`eb0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺实时均价 / 已成交最高最低价 / 是否有板标记则 skip；无板证券协议大宗价不得高于当日竞价实时成交均价 120% 与已成交最高价孰低，不得低于均价 80% 与已成交最低价孰高；上交所 3.6.10 / 深交所 3.5.4；禁止无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报；禁止与有板主病半泄露双挂。`params.G` 的 0.01 不是过户费 0.01‰，也不是 80%，也不是假设-G；`params.Y` 的 0.02 不是实验字母 EB，也不是单字母 E 或 B，也不是证管费 0.02‰，也不是 120%；四个占位也不是均价公式，也不是核对日。**禁把占位读成 120%/80%、均价公式、过户‰**。本页**不开回测**；不拉真数；不做实盘；不开户。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `eb0_primary_demo` / `params.Y`·G·N·Y2 / 价限开关 / 桶 / 是否把无价限或有板涨跌幅或竞价笼子倒灌进主报、或与有板主病双挂、或把占位读成 120%/80% 或均价公式）。本页不开跑。禁 null。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（EB0）/ 半泄露组（EB1）相对诚实组（EB2）的价限误套截**显著且集中在无板证券协议大宗价被写成可以不管均价 120%/80% 与已成交最高最低孰紧**的桶；分桶「有板价限误套 / 核对日泄露 / vs AI·I·AQ·G·AG·DY·O·CK·DZ·EA·DI·R·V·T·U·E」不改变主结论方向。成功不依赖把占位读成 120% 或 80%，也不把 `params.Y` 读成实验字母 EB，也不把 `params.G` 的 0.01 读成过户费或读成假设-G。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 AI/I/AQ 的竞价申报与笼子、G 的无板标签、AG 的超涨跌停拒单、DY 的申报带、O 的日量与三通道、CK 的假全额、DZ 的确认钟、EA 的类型开关、DI 的费率、R 的假 T+0、V/T/U 的费用、E 的整手、A 的板上容量解释；或 `eb0_primary_demo` 与 `invent_asof_leak_nolimit_nego_block_px` 双挂；或与 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 双挂；或 EB1 升格并列主报；或诊断桶升格主报；或有板价限进主报；或无价限 / 有板涨跌幅 / 竞价笼子倒灌进 `eb0`；或实验字母 EB 与单字母 E/B 或 params.Y/G/N 混读；或把占位读成 120%/80%、均价公式、过户‰；或缺实时均价 / 已成交最高最低价 / 是否有板标记仍不 skip；或重开假设-R / 假设-V / 假设-T / 假设-U / 假设-AI / 假设-I / 假设-AQ / 假设-G / 假设-DY / 假设-O / 假设-CK / 假设-DZ / 假设-EA / 假设-E / 假设-B / 假设-Y；或改 EA 正文/预检/复检；或标纸面齐；或写成 A/D–EB纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 EB0/EB1/EB2。集合有效申报走 AI，连续笼子走 I，临停笼子走 AQ，无板标签走 G，超涨跌停拒单走 AG，核准制申报带走 DY，日量与三通道走 O，能不能打满走 CK，确认钟走 DZ，类型开关走 EA，费率走 DI，假 T+0 走 R，费用走 V/T/U，整手走 E，都不改。报告价限误套截。不把 120%、80% 或均价公式标成占位门槛，锚已写死冻结。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_nolimit_nego_block_px_ignore_mean120_80_band` / `invent_asof_leak_nolimit_nego_block_px` / `invent_limit_board_nego_block_px_as_nolimit_mean_band` / `vs_AI_call_valid_range` / `vs_I_continuous_cage` / `vs_AQ_halt_cage` / `vs_G_nolimit_board` / `vs_AG_over_limit_reject` / `vs_DY_approval_ipo_band` / `vs_O_block_liquidity` / `vs_CK_block_fill` / `vs_DZ_chinext_confirm` / `vs_EA_star_fixed_price_type` / `vs_DI_block_fee` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_E_lot_size` / `missing_vwap_or_hi_lo_or_board_flag_not_skip`

`invent_nolimit_nego_block_px_ignore_mean120_80_band` 才是写死冻结的单一主报名（单挂）。`invent_asof_leak_nolimit_nego_block_px` 只服务半泄露对照，**不得升格进 `eb0`，不得双挂**。自 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 起至 `missing_vwap_or_hi_lo_or_board_flag_not_skip` **只作诊断桶**：它们不是 `eb0`，也不是 EB1 主报，**不得升格主报，不得双挂**。**有板协议大宗价限仅诊断**。**禁止与有板主病半泄露双挂**。没有「竞价笼子 + 本页价限」合成主报，也没有「有板涨跌幅 + 本页均价带」合成主报，也没有「O 日量 + 本页价限」合成主报。**实验 R 不抢**。**不重开假设-V / 假设-T / 假设-U**。**零改 EA**。**禁把 AI/I/AQ/G/DY/AG/O/CK/DZ/EA/DI/R/V/T/U/E 升格进 `eb0`**。**禁无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「无板证券协议大宗可以不看均价带」或「有板涨跌幅 / 竞价笼子」拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成实验字母 EB，或当成单字母 E/B，或当成假设-Y，或当成证管费 0.02‰，或当成 120%，或当成均价公式。**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**。**params 字母 ≠ 假设-T**。**params 字母 ≠ 假设-Y**。
- 把 `params.G` 的 0.01 当成过户 0.01‰，或当成假设-G，或当成 80%，或当成 120%。**params 字母 ≠ 假设-U**。**params 字母 ≠ 假设-G**。**params 字母 ≠ 假设-V**。
- 把 `params.N` 的 0.05 当成实验字母 EB 或单字母 E/B。**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 120%/80%、均价公式、过户‰。**禁把占位读成 120%/80%、均价公式、过户‰**。**params 相对门槛 ≠ 120% ≠ 80% ≠ 均价公式 ≠ 过户‰**。**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**。**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**。
- 缺实时均价、已成交最高最低价或是否有板标记仍不 skip。诊断桶 `missing_vwap_or_hi_lo_or_board_flag_not_skip` 只作对照，不得升格。
- 把核对日「已经按均价 120%/80% 与最高最低孰紧」写成全历史规则，或铺到有板证券、铺到缺字段的日子。锚六键已写死冻结。半泄露键 `invent_asof_leak_nolimit_nego_block_px` 不得与主报双挂。
- 把有板证券「在当日涨跌幅内谈」写成无板均价带，或把无板均价带写成有板涨跌幅，并升格进主报。诊断桶 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 只作对照，**禁进主报，禁双挂**。**有板协议大宗价限仅诊断**。**禁止与有板主病半泄露双挂**。
- 把无价限、有板涨跌幅、竞价笼子倒灌进主报。**禁无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报**。
- 把假设-AI / 假设-I / 假设-AQ 的竞价有效申报、连续笼子、临停笼子和本页价限合成后升格。诊断桶 `vs_AI_call_valid_range` / `vs_I_continuous_cage` / `vs_AQ_halt_cage` 只作对照。**不重开假设-AI**；**不重开假设-I**；**不重开假设-AQ**。
- 把假设-G 的无板标签、假设-DY 的核准制首日申报带和本页谈妥价公式合成后升格。**不重开假设-G**；**不重开假设-DY**。诊断桶 `vs_G_nolimit_board` / `vs_DY_approval_ipo_band` 只作对照。
- 把假设-AG 的超涨跌停拒单和本页合成后升格。**不重开假设-AG**。诊断桶 `vs_AG_over_limit_reject` 只作对照。
- 把假设-O 的日量含大宗、三通道假流动性和本页价限合成后升格。**不重开假设-O**。诊断桶 `vs_O_block_liquidity` 只作对照。
- 把假设-CK 的假全额可成和本页价限合成后升格。**不重开假设-CK**。诊断桶 `vs_CK_block_fill` 只作对照。
- 把假设-DZ 的创业板确认钟和本页合成后升格。**不重开假设-DZ**。诊断桶 `vs_DZ_chinext_confirm` 只作对照。
- 把假设-EA 的科创大宗固定价格类型开关和本页价限合成后升格。**零改 EA**。**不重开假设-EA**。诊断桶 `vs_EA_star_fixed_price_type` 只作对照。
- 把假设-DI 的大宗费率和本页价限合成后升格。**不重开假设-DI**。诊断桶 `vs_DI_block_fee` 只作对照。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格。**实验 R 不抢**。诊断桶 `vs_R_etf_t0` 只作对照。
- 把假设-V / 假设-T / 假设-U 和本页合成或混读后升格。诊断桶 `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` 只作对照。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。
- 把假设-E 的整手、科创板 200 股和本页价限合成后升格。**双字母 EB ≠ 单字母假设-E**。诊断桶 `vs_E_lot_size` 只作对照。
- 把单字母假设-B 读成双字母 EB，或给假设-B 新写独立正文来顶本页。**双字母 EB ≠ 单字母假设-B**。**假设-B 勿复用·无独立正文**。
- `eb0_primary_demo` 与 `invent_asof_leak_nolimit_nego_block_px` 双挂；或与 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 双挂；EB1 升格并列主报。
- 实验字母 EB 与单字母 E/B 或 params.Y/G/N 混读。**双字母 EB ≠ 单字母 E/B**。**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**。
- 改 EA / DZ / DY / O / CK / AI / I / AQ / G / AG / R / V / T / U / E / Y 及其他已冻页正文；改 #110–#136；禁止标纸面齐；禁止写成 A/D–EB纸面齐；预留 #138；开真数/回测/开户/实盘；用复权价当价限的判据；结论写成「这类大宗更能成交所以能买」。
- **纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头、结论、尾状态（对照 DK–EA；勿再只改清单）。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权路径、交易日、**是否有板标记**（无板 / 有板）。标记分不清则 skip。本页只钉无板证券的协议大宗价限，不把有板「在当日涨跌幅内谈」套进来当主报，也不把无板标签本身当成谈妥价公式。
- 当日竞价**实时成交均价**，以及**已成交最高价、已成交最低价**。均价 = 已成交金额 / 已成交股数，四舍五入到最小价位（`事实与坑` 2026-10-23）。这三样缺一则 skip，不用占位数字去填 120% 或 80%。
- 官方规则是否在册：无板证券协议大宗价不得高于均价 120% 与已成交最高价孰低，不得低于均价 80% 与已成交最低价孰高。上交所 3.6.10；深交所 3.5.4。规则不在册则 skip。
- 申报要能分清是**无板证券的协议 / 成交申报大宗**，还是竞价限价、集合竞价、连续竞价笼子、临停阶段、盘后固定价格、有板证券的协议大宗。后几类不进本页主报。
- 价限字段：无板这笔的谈妥价要能对照「均价 120% 与已成交最高价孰低」和「均价 80% 与已成交最低价孰高」。只有一根日 K、没有实时均价和已成交最高最低，不要默认「无板就没有价限」，也不要默认「按有板涨跌幅谈」。
- 旁路消费：AI 的集合有效申报、I 的连续笼子、AQ 的临停笼子、G 的无板标签、AG 的超涨跌停拒单、DY 的核准制申报带、O 的日量与三通道、CK 的协议大宗可成交、DZ 的创业板确认钟、EA 的科创类型开关、DI 的大宗费率、R 的假 T+0、V/T/U 的费用、E 的整手（见 §2.1 handoff）。**本页不改写这些页。零改 EA。**
- 未复权路径；asof **写死冻结** `2026-10-23`。核对日已经写着这道带，所以「核对日当天无板协议大宗按这道带」不能倒灌到缺字段的日子，也不能倒灌到有板证券。`事实与坑` 2026-10-23 是方向来源，不是已冻的全历史规则。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-23`；`fail_policy=skip`；`nolimit_nego_block_px_honest=pit_mean120_hi_lo_whichever_tighter`；`nolimit_nego_block_px_scope=nolimit_security_nego_block_price_band_only`；`nolimit_nego_block_px_over_policy=skip_if_vwap_or_hi_lo_or_board_flag_missing`；`eb0_primary_demo=invent_nolimit_nego_block_px_ignore_mean120_80_band`（**写死冻结**单一主报，单挂写死；禁与 `invent_asof_leak_nolimit_nego_block_px` 双挂；禁与 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 双挂；EB1 不升格；诊断桶不升格；**有板协议大宗价限仅诊断**；**禁无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报**；**禁把 AI/I/AQ/G/DY/AG/O/CK/DZ/EA/DI/R/V/T/U/E 升格进 `eb0`**）；`call_valid_range_handoff=ai_page`；`continuous_cage_handoff=i_page`；`halt_cage_handoff=aq_page`；`nolimit_board_handoff=g_page`；`over_limit_reject_handoff=ag_page`；`approval_ipo_band_handoff=dy_page`；`block_liquidity_handoff=o_page`；`block_fill_handoff=ck_page`；`chinext_confirm_handoff=dz_page`；`star_fixed_price_type_handoff=ea_page`；`block_fee_handoff=di_page`；`etf_t0_handoff=r_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；`lot_size_handoff=e_page`；`merge_with_EA/DZ/DY/DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/AI/AQ/I/AG/Y/A/D/Z/B=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是 120%，不是 80%，不是均价公式，不是过户费率，不是证管费，不是核对日；**params.G=`0.01` ≠ 过户 0.01‰ ≠ 120%/80% 带宽**；**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**；**params.Y/G/N ≠ 实验字母 EB ≠ 单字母 E/B**；**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**；**尤重 params.Y 的 0.02 ≠ 实验字母 EB ≠ 单字母 E/B ≠ 120% ≠ 80% ≠ 均价公式 ≠ 证管费 0.02‰**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 120% ≠ 80% ≠ 均价公式 ≠ 假设-G**；**禁把占位读成 120%/80%、均价公式、过户‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #138。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`d462923`（A/D–EA纸面齐已合，全长 `d4629238a86b70c7f66761d5e554d01d2e9e7d6d`）；三冻补丁基 tip=`84cb2cdd` / `84cb2cddd83dad33c1b646758f9e6d4f0bb2c1b8`；分支起点 HEAD=`a4ef8dce` / `a4ef8dce68b50490a344d656c84840bade388267`。**不改已冻 A–DQ / DA–EA**。**零改 EA**。**不改 #110–#136**。状态=**A/D–EB纸面齐（预检有条件通过·三条已冻）**。

---

## 8. 结论

（空；**A/D–EB纸面齐（预检有条件通过·三条已冻）**。）

---

## 变更
| 日期 | 变更 |
|------|------|

## 风控预检补丁·冻结（三条已写死 · 2026-12-08）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设EB-20261110.md`（原样落入，不改结论；SHA256=`c7c47980b5bb14b59835761e5d53ebaacdc4de32844fbacf697195d73f379be9`；预检 2026-11-10；**结论：有条件通过**；tip基=`84cb2cdd` / `84cb2cddd83dad33c1b646758f9e6d4f0bb2c1b8`；本补丁分支起点 HEAD=`a4ef8dce` / `a4ef8dce68b50490a344d656c84840bade388267`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于价限误套截 ΔNolimitNegoBlockPx、净差异、EB1−EB2 专项。**`params.Y` ≠ 实验字母 EB**；**`params.G` ≠ 实验字母 EB**；**`params.N` ≠ 实验字母 EB**；亦 ≠ 单字母假设-E / 假设-B。**params.Y/G/N ≠ 实验字母 EB ≠ 单字母 E/B**。**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**。**勿把 `params.Y` 读成实验字母 EB，亦勿读成单字母假设-E，亦勿读成单字母假设-B，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿把 `params.G` 读成假设-U，亦勿把 `params.G` 读成假设-G，亦勿把单字母假设-E / 假设-B 读成双字母 EB**。**尤重：`params.G` 的 `0.01` ≠ 过户 0.01‰ ≠ 120%/80% 带宽 ≠ 均价公式**（**params.G=`0.01` ≠ 过户 0.01‰ ≠ 120%/80% 带宽**）。量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户 0.01‰，也不是均价的 80%，也不是均价的 120%，也不是假设-G。**尤重：`params.Y` 的 `0.02` ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23 ≠ 实验字母 EB**（**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**）。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B**。**禁把占位读成 120%/80%、均价公式、过户‰**。**params 相对门槛 ≠ 120% ≠ 80% ≠ 均价公式 ≠ 过户‰**。禁止互读、禁止把门槛改写成 120%、80%、均价公式、核对日、过户费率或证管费。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.eb0_primary_demo`**：**写死冻结** **`invent_nolimit_nego_block_px_ignore_mean120_80_band`**（单一主报，单挂写死）。**禁止**与半泄露键 **`invent_asof_leak_nolimit_nego_block_px`** 双挂争主表；**禁止**与有板对照键 **`invent_limit_board_nego_block_px_as_nolimit_mean_band`** 双挂；**禁止**跑后因分桶显著性改口主报。EB1 仅核对日把「无板协议大宗已经按均价 120%/80% 与已成交最高最低孰紧」铺到缺字段的日子、铺到有板证券、或铺成全历史无条件规则，只作半泄露对照，**不得升格与 eb0 并列主报**，也不得把 `invent_asof_leak_nolimit_nego_block_px` 写进 `eb0`。有板对照只进诊断桶，不升格。`invent_limit_board_nego_block_px_as_nolimit_mean_band` / `vs_AI_call_valid_range` / `vs_I_continuous_cage` / `vs_AQ_halt_cage` / `vs_G_nolimit_board` / `vs_AG_over_limit_reject` / `vs_DY_approval_ipo_band` / `vs_O_block_liquidity` / `vs_CK_block_fill` / `vs_DZ_chinext_confirm` / `vs_EA_star_fixed_price_type` / `vs_DI_block_fee` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_E_lot_size` / `missing_vwap_or_hi_lo_or_board_flag_not_skip` **只作诊断桶，不得升格主报**。EB1 / 诊断桶 **不升格**。**禁把以下升格进 eb0**：AI/I/AQ 竞价有效申报/笼子 / G无板标签 / DY核准制首日申报带 / O/CK 假流动性假全额 / DZ确认钟 / EA类型开关 / R假T+0 / V印花 / T证管费 / U过户 / 无价限/有板涨跌幅/竞价笼子倒灌。这些只作对照/旁路，**不得升格进 `eb0`，不得另挂主报**。**零改 EA**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**不抢实验 R**。**不重开假设-V/T/U**。**双字母 EB ≠ 单字母假设-E / 假设-B**。**双字母 EB ≠ 单字母 E/B**。

3. **无板证券协议大宗价限诚实锚六键升格写死（不可再写「建议」）**：`params.nolimit_nego_block_px_honest=pit_mean120_hi_lo_whichever_tighter`；`params.nolimit_nego_block_px_scope=nolimit_security_nego_block_price_band_only`；`params.nolimit_nego_block_px_over_policy=skip_if_vwap_or_hi_lo_or_board_flag_missing`；`params.asof_check_date=2026-10-23`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺实时均价 / 已成交最高最低价 / 是否有板标记 → skip。诚实：无板证券协议大宗价不得高于当日竞价实时成交均价 120% 与已成交最高价孰低、不得低于均价 80% 与已成交最低价孰高；上交所 3.6.10 / 深交所 3.5.4。禁止无价限 / 有板涨跌幅 / 竞价笼子倒灌进主报。禁止与有板主病半泄露双挂。禁止跑后改锚，或用无价限 / 有板涨跌幅 / 竞价笼子 / 核对日规则铺满 / 与有板主病半泄露双挂 / 缺 vwap 或高低价或有板标记仍硬填 / 把 AI/I/AQ/G/DY/O/CK/DZ/EA/R/V/T/U 升格进 eb0 冒充诚实 PIT。**禁把占位读成 120%/80%、均价公式、过户‰**。**禁把 params.G 的 0.01 读成过户 0.01‰ 或 120%/80% 带宽**。**禁把 params.Y 的 0.02 读成证管费 0.02‰ 或均价带或核对日 2026-10-23 或实验字母 EB**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**零改 EA**。**不抢实验 R**。

**硬分列保住**：EB≠EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠AI≠AQ≠I≠AG≠Y≠A≠D≠Z≠B；**双字母 EB ≠ 单字母假设-E / 假设-B**；**双字母 EB ≠ 单字母 E/B**；**params.Y / params.G / params.N ≠ 实验字母 EB ≠ 单字母 E/B**；**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 120%/80% 带宽**；**params.G=`0.01` ≠ 过户 0.01‰ ≠ 120%/80% 带宽**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**；**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**；**禁把占位读成 120%/80%、均价公式、过户‰**；**params 相对门槛 ≠ 120% ≠ 80% ≠ 均价公式 ≠ 过户‰**；**无板证券协议大宗价限 ≠ AI/I/AQ竞价有效申报与笼子 ≠ G无板标签 ≠ DY核准制首日申报带 ≠ O/CK假流动性假全额 ≠ DZ确认钟 ≠ EA类型开关 ≠ R假T+0 ≠ V印花 ≠ T证管费 ≠ U过户 ≠ E整手 ≠ B旧位**；不抢 A；不抢实验 R；不改已齐/已冻 DA～EA 及 A–DQ 正文；**零改 EA**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-R**；**不重开假设-AI**；**不重开假设-I**；**不重开假设-AQ**；**不重开假设-G**；**不重开假设-DY**；**不重开假设-O**；**不重开假设-CK**；**不重开假设-DZ**；**不重开假设-EA**；**不重开假设-E**；**不重开假设-B**；**禁把 AI/I/AQ 竞价有效申报/笼子 / G无板标签 / DY核准制首日申报带 / O/CK 假流动性假全额 / DZ确认钟 / EA类型开关 / R假T+0 / V印花 / T证管费 / U过户 / 无价限/有板涨跌幅/竞价笼子倒灌 合成/混读升格进 eb0**。handoff 保持：`call_valid_range_handoff=ai_page`；`continuous_cage_handoff=i_page`；`halt_cage_handoff=aq_page`；`nolimit_board_handoff=g_page`；`over_limit_reject_handoff=ag_page`；`approval_ipo_band_handoff=dy_page`；`block_liquidity_handoff=o_page`；`block_fill_handoff=ck_page`；`chinext_confirm_handoff=dz_page`；`star_fixed_price_type_handoff=ea_page`；`block_fee_handoff=di_page`；`etf_t0_handoff=r_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`transfer_fee_handoff=u_page`；`lot_size_handoff=e_page`；全部 `merge_with_*=False`。

**状态**：**A/D–EB纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/开户/实盘。

| 2026-11-10 | 复检/纸面齐——**A/D–EB纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设EB-20261110.md` 原样落入，SHA256=`3554a1b41544f9529b0f64dbdeaaf7826bb09b6f19839fa57b6e30657b14fe72`；三冻 tip=`5e871ae9` / `5e871ae96d7c4412f4618b6c3eac9d126de5f8f3`。只改状态标签；未改写已冻三条/六键；不改已齐 A–DQ / DA–EA；**零改 EA**；不改 #110–#136；不重开假设-V / 假设-T / 假设-U / 假设-R / 假设-AI / 假设-I / 假设-AQ / 假设-G / 假设-DY / 假设-O / 假设-CK / 假设-DZ / 假设-EA / 假设-E / 假设-B；不抢实验 R；不预留 #138；不开回测/真数/开户/实盘。 |
| 2026-12-08 | 风控预检补丁·冻结三条写死——依据 `预检-假设EB-20261110.md`（SHA256=`c7c47980b5bb14b59835761e5d53ebaacdc4de32844fbacf697195d73f379be9`；结论=有条件通过；tip基=`84cb2cdd` / `84cb2cddd83dad33c1b646758f9e6d4f0bb2c1b8`；分支起点 HEAD=`a4ef8dce` / `a4ef8dce68b50490a344d656c84840bade388267`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖价限误套截 ΔNolimitNegoBlockPx / 净差异 / EB1−EB2；**params.Y/G/N ≠ 实验字母 EB ≠ 单字母 E/B**；**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**；**勿把 params.Y 读成实验字母 EB 或单字母假设-E 或单字母假设-B 或假设-V 或假设-T 或假设-U，亦勿把 params.G 读成假设-U 或假设-G，亦勿把单字母假设-E / 假设-B 读成双字母 EB**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 120%/80% 带宽 ≠ 均价公式（量纲与语义不同）**；**params.G=`0.01` ≠ 过户 0.01‰ ≠ 120%/80% 带宽**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23 ≠ 实验字母 EB**；**params.Y=`0.02` ≠ 证管费 0.02‰ ≠ 均价带 ≠ 核对日 2026-10-23**；**禁把占位读成 120%/80%、均价公式、过户‰**；**params 相对门槛 ≠ 120% ≠ 80% ≠ 均价公式 ≠ 过户‰**；禁 null；禁 holdout/OOS 标定）；② `params.eb0_primary_demo=invent_nolimit_nego_block_px_ignore_mean120_80_band`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_nolimit_nego_block_px` 双挂；禁与 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 双挂；EB1 不升格；诊断桶 `invent_limit_board_nego_block_px_as_nolimit_mean_band` / `vs_AI_call_valid_range` / `vs_I_continuous_cage` / `vs_AQ_halt_cage` / `vs_G_nolimit_board` / `vs_AG_over_limit_reject` / `vs_DY_approval_ipo_band` / `vs_O_block_liquidity` / `vs_CK_block_fill` / `vs_DZ_chinext_confirm` / `vs_EA_star_fixed_price_type` / `vs_DI_block_fee` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_E_lot_size` / `missing_vwap_or_hi_lo_or_board_flag_not_skip` 不升格；**禁把 AI/I/AQ 竞价有效申报/笼子 / G无板标签 / DY核准制首日申报带 / O/CK 假流动性假全额 / DZ确认钟 / EA类型开关 / R假T+0 / V印花 / T证管费 / U过户 / 无价限/有板涨跌幅/竞价笼子倒灌 合成/混读升格进 eb0**，只作对照/旁路，不得升格进 eb0 或另挂主报；**零改 EA**；不重开假设-V；不重开假设-T；不重开假设-U；不抢实验 R；**双字母 EB ≠ 单字母假设-E / 假设-B**）；③ 锚六键写死 `nolimit_nego_block_px_honest=pit_mean120_hi_lo_whichever_tighter` / `nolimit_nego_block_px_scope=nolimit_security_nego_block_price_band_only` / `nolimit_nego_block_px_over_policy=skip_if_vwap_or_hi_lo_or_board_flag_missing` / `asof_check_date=2026-10-23` / `fill_time=next_open` / `fail_policy=skip`（缺实时均价/已成交最高最低价/是否有板标记 → skip；无板证券协议大宗价不得高于当日竞价实时成交均价 120% 与已成交最高价孰低、不得低于均价 80% 与已成交最低价孰高；上交所 3.6.10 / 深交所 3.5.4；禁止无价限/有板涨跌幅/竞价笼子倒灌进主报；禁止与有板主病半泄露双挂）。handoff 保持 `call_valid_range_handoff=ai_page` / `continuous_cage_handoff=i_page` / `halt_cage_handoff=aq_page` / `nolimit_board_handoff=g_page` / `over_limit_reject_handoff=ag_page` / `approval_ipo_band_handoff=dy_page` / `block_liquidity_handoff=o_page` / `block_fill_handoff=ck_page` / `chinext_confirm_handoff=dz_page` / `star_fixed_price_type_handoff=ea_page` / `block_fee_handoff=di_page` / `etf_t0_handoff=r_page` / `stamp_handoff=v_page` / `csrc_fee_handoff=t_page` / `transfer_fee_handoff=u_page` / `lot_size_handoff=e_page`；全部 `merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–EB纸面齐**；不改已齐/已冻 DA～EA 及 A–DQ；**零改 EA**；不改 #110–#136；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-R；不重开假设-AI；不重开假设-I；不重开假设-AQ；不重开假设-G；不重开假设-DY；不重开假设-O；不重开假设-CK；不重开假设-DZ；不重开假设-EA；不重开假设-E；不重开假设-B；不抢实验 R；不预留 #138；不开回测/真数/开户/实盘。基于 tip=`84cb2cdd`。
| 2026-12-08 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。无板证券协议大宗价限误套（成交规则）；`eb0_primary_demo` 建议 `invent_nolimit_nego_block_px_ignore_mean120_80_band`，单一主报，单挂，禁与 `invent_asof_leak_nolimit_nego_block_px` 双挂，禁与 `invent_limit_board_nego_block_px_as_nolimit_mean_band` 双挂，EB1 不升格；诊断桶 `invent_limit_board_nego_block_px_as_nolimit_mean_band` / `vs_AI_call_valid_range` / `vs_I_continuous_cage` / `vs_AQ_halt_cage` / `vs_G_nolimit_board` / `vs_AG_over_limit_reject` / `vs_DY_approval_ipo_band` / `vs_O_block_liquidity` / `vs_CK_block_fill` / `vs_DZ_chinext_confirm` / `vs_EA_star_fixed_price_type` / `vs_DI_block_fee` / `vs_R_etf_t0` / `vs_V_stamp` / `vs_T_csrc` / `vs_U_transfer` / `vs_E_lot_size` / `missing_vwap_or_hi_lo_or_board_flag_not_skip` 不升格；**尤重实验 R 不抢，禁把 vs_R_etf_t0 升格进 eb0**；**尤重不重开假设-V / 假设-T / 假设-U，禁把 vs_V_stamp / vs_T_csrc / vs_U_transfer 升格进 eb0**；**尤重有板协议大宗价限仅诊断，禁与无板主报半泄露双挂，禁把 invent_limit_board_nego_block_px_as_nolimit_mean_band 升格或双挂**；**尤重 AI/I/AQ 竞价有效申报/笼子 ≠ 本页协议大宗价限，禁把 vs_AI_call_valid_range / vs_I_continuous_cage / vs_AQ_halt_cage 升格**；**尤重 G/DY 无板标签/核准制首日申报带 ≠ 本页大宗谈妥价公式，禁把 vs_G_nolimit_board / vs_DY_approval_ipo_band 升格**；**尤重 O/CK 假流动性/假全额 ≠ 本页价限，禁把 vs_O_block_liquidity / vs_CK_block_fill 升格**；**尤重 DZ 确认钟 ≠ 本页，禁把 vs_DZ_chinext_confirm 升格**；**尤重 EA 类型开关 ≠ 本页价限，禁把 vs_EA_star_fixed_price_type 升格，零改 EA**；**尤重双字母 EB ≠ 单字母假设-E（整手与科创板 200 股）/ 假设-B（勿复用·无独立正文），禁把 vs_E_lot_size 升格**；**尤重 params.Y/G/N ≠ 实验字母 EB / 单字母 E/B**；**尤重 params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-E / 假设-B / 假设-Y / 假设-G**；**禁把占位读成 120%/80%、均价公式、过户‰**；**禁无价限/有板涨跌幅/竞价笼子倒灌进主报**；**零改 EA**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 EB ≠ 单字母 E/B**；锚建议·待冻、未冻：`nolimit_nego_block_px_honest=pit_mean120_hi_lo_whichever_tighter` / scope=`nolimit_security_nego_block_price_band_only` / over_policy=`skip_if_vwap_or_hi_lo_or_board_flag_missing` / `asof_check_date=2026-10-23` / `fill_time=next_open` / `fail_policy=skip`；口径：缺实时均价/已成交最高最低价/是否有板标记则 skip；无板证券协议大宗价不得高于当日竞价实时成交均价 120% 与已成交最高价孰低、不得低于均价 80% 与已成交最低价孰高；上交所 3.6.10 / 深交所 3.5.4；禁止无价限/有板涨跌幅/竞价笼子倒灌进主报；禁止与有板主病半泄露双挂（**草稿方向，尚未冻，不要写成已冻**）；handoff：`call_valid_range_handoff=ai_page`，`continuous_cage_handoff=i_page`，`halt_cage_handoff=aq_page`，`nolimit_board_handoff=g_page`，`over_limit_reject_handoff=ag_page`，`approval_ipo_band_handoff=dy_page`，`block_liquidity_handoff=o_page`，`block_fill_handoff=ck_page`，`chinext_confirm_handoff=dz_page`，`star_fixed_price_type_handoff=ea_page`，`block_fee_handoff=di_page`，`etf_t0_handoff=r_page`，`stamp_handoff=v_page`，`csrc_fee_handoff=t_page`，`transfer_fee_handoff=u_page`，`lot_size_handoff=e_page`；全部 `merge_with_*=False`；`merge_with_EA/DZ/DY/DX/DW/DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AW/AY/X/G/CI/CK/AI/AQ/I/AG/Y/A/D/Z/B=False`；**EB≠EA≠DZ≠DY≠DX≠DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠AW≠AY≠X≠G≠CI≠CK≠AI≠AQ≠I≠AG≠Y≠A≠D≠Z≠B**；**双字母 EB ≠ 单字母 E/B**；**未标纸面齐**；**不写 A/D–EB纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–EA；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–EA；**零改 EA**；不改 #110–#136；不重开假设-R；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-AI；不重开假设-I；不重开假设-AQ；不重开假设-G；不重开假设-DY；不重开假设-AG；不重开假设-O；不重开假设-CK；不重开假设-DZ；不重开假设-EA；不重开假设-DI；不重开假设-E；不重开假设-B；不重开假设-Y；不写下一字母；不预留 #138；不开真数/回测/开户/实盘。基 tip=`d462923`（A/D–EA纸面齐已合，全长 `d4629238a86b70c7f66761d5e554d01d2e9e7d6d`；不改该 tip 上的 #110–#136，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
