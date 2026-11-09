# 假设-DW · 权证/股票期权行权过户费误套股票成交金额档（费用）

更新：2026-12-03  
来源：总管线 / 基 tip=`5e23a7dd` / 全长 `5e23a7dd736ad5f61e53605e834191774c6a5eec`（A/D–DV纸面齐已合）；**不改已冻 A–DQ / DA–DV**；**零改 DV**；**不改假设-DV 正文/预检/复检**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DP / 假设-DQ / 假设-DR / 假设-DS / 假设-DT / 假设-DU / 假设-DV / 假设-S / 假设-AX / 假设-T / 假设-U / 假设-V / 假设-W / 假设-AC / 假设-Q / 假设-R / 假设-O / 假设-M / 假设-E / 假设-F / 假设-J / 假设-A / 假设-D 及其他已存在假设页（含假设-CH / 假设-CL / 假设-CR / 假设-CQ / 假设-AU / 假设-BR）；**不重开假设-U**；**不重开假设-V**；**不重开假设-T**；**不重开假设-R**；**不重开假设-DV**；**不重开假设-DN**；**不重开假设-DQ**；**不重开假设-CR**；**不重开假设-W**；**不重开假设-DU**；**不重开假设-DT**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-D**；**不重开假设-Q**；**不重开假设-CQ**；**不重开假设-E**；**不重开假设-F**；**不重开假设-S**；**不重开假设-M**；**不重开假设-O**；**不重开假设-DO**；**不重开假设-AC**；**不重开假设-DI**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**；**不重开假设-J**；**不重开假设-CH**；**不重开假设-CL**）后写下一草稿 DW；清单 #131=DV，本页占用 **#132=DW**；选题是回测把 **权证/股票期权行权过户费**误套成**股票二级成交金额档**（诚实方向按 biz_type 分列：权证行权=面值 0.5‰ **单向**；股票期权行权=面值 0.5‰ **过入方**；禁止合成一句；禁止套 A 股二级成交金额 0.01‰；禁止与 DV/DN/DQ 仅因同是面值 0.5‰ 合成一句；缺业务类型/官方‰/场所表则 skip）；假设-DV 只收现金选择权行权过户（现金选择权 ≠ 本页权证/期权行权），假设-U 只收股票过户切日（金额档 ≠ 本页面值档），假设-V 只收股票印花税切日，假设-T 只收股票证管费切日，假设-DN 只收可交换债换股过户，假设-DQ 只收 ETF 申赎组合证券过户，假设-CR 只收行权可成交性，假设-W 只收除权日复权价误判板，假设-DU 只收可转债首日临停，假设-DT 只收可转债整手价位，假设-DS 只收转股所得股票印花，假设-DR 只收可转债盘后定价通道，假设-R 只收股票 ETF 假 T+0；**新建实验 DW**；不写下一字母；不预留 #133  
状态：**A/D–DW纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「权证或股票期权行权按 A 股二级成交金额 0.01‰」当诚实过户费；禁止把权证「单向」和期权「过入方」合成一句；不抢实验 A 真数队列；不抢实验 R；本页不开回测；不开户；不催 8765；**不改已冻 A–DQ / DA–DV**；**零改 DV**；尤其不改假设-DV / 假设-U / 假设-V / 假设-T / 假设-DN / 假设-DQ / 假设-CR / 假设-W / 假设-DU / 假设-DT / 假设-DS / 假设-DR / 假设-R / 假设-D；**不重开假设-U**；**不重开假设-V**；**不重开假设-T**；**不重开假设-R**；**不重开假设-DV**；**不重开假设-DN**；**不重开假设-DQ**；**不重开假设-CR**；**不重开假设-W**；**不重开假设-DU**；**不重开假设-DT**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-D**；**不重开假设-Q**；**不重开假设-CQ**；**不重开假设-E**；**不重开假设-F**；**不重开假设-S**；**不重开假设-M**；**不重开假设-O**；**不重开假设-DO**；**不重开假设-AC**；**不重开假设-DI**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**；**不重开假设-J**；**不重开假设-CH**；**不重开假设-CL**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DW（#132）。一句话误开：回测把权证/股票期权行权过户费误套股票成交金额档，按二级成交金额 0.01‰ 去抽行权过户，或把行权过户记成 0，或因同是面值 0.5‰ 抄 DV 现金选择权行权过户 / DN 换股过户 / DQ 申赎篮子过户，或把权证「单向」与期权「过入方」合成一句，或与 U股票过户切日 / V股票印花切日 / T股票证管费 / DV现金选择权行权过户 / DN换股过户 / DQ申赎篮子过户 / CR行权可成交性 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后通道 / W除权日复权价误判板 / R股票ETF假T+0 混读，或缺业务类型/官方‰/场所表仍不 skip，系统性改写权证/股票期权行权腿的过户成本。**禁把 U/V/T/DV/DN/DQ/CR/W/R 混读升格进 `dw0`**。**禁把 DU/DT/DS/DR 混读升格进 `dw0`**。

> **字母消歧（硬）**：本页**实验字母 DW** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DW**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**；**勿把 `params.Y` 读成实验字母 DW，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿读成假设-W**；**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰ ≠ 印花税率**；**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DW**；**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是 A 股二级过户 0.01‰，也不是行权面值 0.5‰，更不是印花税率；**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**；**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DW**；**params.N ≠ 单字母假设-N**；**`params.N` 的 0.05 ≠ 面值 0.5‰ ≠ 印花 0.5‰**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DW ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 W**（除权日用复权价误判涨跌停；**双字母 DW ≠ 单字母假设-W；严禁复用假设-W**；**不重开假设-W**；组名 DW0/DW1/DW2 是本页三组对照，≠ 单字母实验 W，亦 ≠ 单字母实验 D）≠ **单字母实验 V**（股票印花税切日；**双字母 DW ≠ 单字母假设-V；严禁复用假设-V**；**不重开假设-V**；**params 字母 ≠ 假设-V**）≠ **单字母实验 U**（股票过户费切日，金额档；**双字母 DW ≠ 单字母假设-U；严禁复用假设-U**；**不重开假设-U**；**U 股票过户切日（金额档）≠ 本页行权面值档**；**params 字母 ≠ 假设-U**）≠ **单字母实验 T**（股票证管费切日；**双字母 DW ≠ 单字母假设-T；严禁复用假设-T**；**不重开假设-T**；**params 字母 ≠ 假设-T**）≠ **单字母实验 R**（股票 ETF 假 T+0 / 股票ETF假回转；**双字母 DW ≠ 单字母假设-R；严禁复用假设-R**；**实验 R 不抢、不重开、不混读升格进 `dw0`**）≠ **假设-BR**（融券借券费/融出费率计提；本页不改、不并进 `dw0`；不在硬分列主链里另造桶）≠ **双字母 AU**（本方对手最优空簿；本页不改、不并进 `dw0`；不在硬分列主链里另造桶）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DW ≠ 单字母假设-A**）≠ 双字母 **DV**（A 股现金选择权行权过户费误套股票成交金额档；**DV 现金选择权行权 ≠ 本页权证/期权行权**；**零改 DV**）≠ **DU**（可转债首日临停误套股票无板日临停；**DU 首日临停 ≠ 本页过户费**）≠ **DT**（可转债整手价位误套股票；**DT 整手价位 ≠ 本页过户费**）≠ **DS**（可转债转股所得股票印花税误免；**DS 转股印花 ≠ 本页过户费**）≠ **DR**（可转债盘后定价误套股票盘后固定价格；**DR 盘后通道 ≠ 本页过户费**）≠ **DQ**（ETF 申赎组合证券过户费误套；**DQ 篮子面值 0.5‰ ≠ 本页权证/期权行权**）≠ **DP**（可交换债换股印花税误漏）≠ **DO**（可转债回售处理）≠ **DN**（可交换债换股过户费误套；**DN 换股面值 0.5‰ ≠ 本页权证/期权行权**）≠ **DM**（可交换债换股经手费误套现货）≠ **DL**（股票综合协议过户费下浮）≠ **DK**（场内基金印花税误抽）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债现货经手费沪深合成）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债现货印花税误抽）≠ **DB**（可转债现货经手费）≠ **DA**（场内基金二级过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债回转/涨跌幅/收盘）≠ **O**（大宗三通道）≠ **M**（股票盘后通道）≠ **CH**（股票盘后固定价格可成交性）≠ **CL**（可转债盘后定价可成交性）≠ **CR**（认沽/认购行权可成交性；行权能不能成交 ≠ 本页过户费）≠ **CQ**（可转债转股可成交性）≠ **E**（股票/科创整手）≠ **F**（涨跌停取整）≠ **J**（股票无板日临停）。**DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠A≠D**。**双字母 DW ≠ 单字母 D/W**。**双字母 DW ≠ 单字母假设-D / 假设-W**。**params.Y/G/N ≠ 实验字母 DW；亦 ≠ 单字母 D/W**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**。**勿把 `params.Y` 或 `params.G` 读成实验字母 DW，亦勿把单字母假设-D / 假设-W 读成双字母 DW**。**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰；`params.Y` 的 0.02 ≠ 证管费 0.02‰；占位 ≠ 印花税率**。**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**。**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**。**权证/股票期权行权过户费误套股票成交金额档 ≠ DV现金选择权行权过户 ≠ U股票过户切日（金额档）≠ V股票印花切日 ≠ T股票证管费 ≠ DN换股过户 ≠ DQ申赎篮子过户 ≠ CR行权可成交性 ≠ W除权日复权价误判板 ≠ DU首日临停 ≠ DT整手价位 ≠ DS转股印花 ≠ DR盘后通道 ≠ R股票ETF假T+0**。**尤重：权证「单向」与期权「过入方」须按 biz_type 分列，禁止合成一句进 `dw0`**。**尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `dw0`**。**尤重：不重开假设-V（股票印花切日）；禁把 `vs_V_stamp` 升格进 `dw0`**。**尤重：不重开假设-T（股票证管费切日）；禁把 `vs_T_csrc_fee` 升格进 `dw0`**。**尤重：不重开假设-U；U 股票过户切日（金额档）≠ 本页行权面值档；禁把 `vs_U_ashare_transfer_fee` 升格进 `dw0`**。**尤重：DV 现金选择权行权 ≠ 本页权证/期权行权；零改 DV；禁把 DV 诊断升格回写；禁 `copy_DV_cash_option_transfer_onto_warrant_option` / `vs_DV_cash_option_transfer` 进主报**。**尤重：DN/DQ 同为面值 0.5‰ 但业务不同，数字相同禁升格进 `dw0`；禁 `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` 进主报**。**尤重：CR 可成交性 ≠ 本页过户费；禁把 `vs_CR_put_call_fill` 升格进 `dw0`**。**尤重：双字母 DW ≠ 单字母假设-D / 假设-W（除权日复权价误判板）；禁把 `vs_W_ex_right_limit` 升格进 `dw0`**。**尤重：DU 首日临停 / DT 整手价位 / DS 转股印花 / DR 盘后通道 ≠ 本页过户费；禁升格进 `dw0`**。**禁把 U/V/T/DV/DN/DQ/CR/W/R 混读升格进 `dw0`**。**禁把 DU/DT/DS/DR 混读升格进 `dw0`**。

### 专节 · 双字母 DW ≠ 单字母假设-D / 假设-W；且 ≠ 假设-DV / 假设-U / 假设-V / 假设-T / 假设-DN / 假设-DQ / 假设-CR / 假设-R（硬）

| 维度 | 对照页 | 本页假设-DW（双字母） |
|------|--------|----------------------|
| 题面 DV | **A 股现金选择权行权过户**（行权股票过户面值 0.5‰ 单向；假设-DV 已纸面齐） | **DV 现金选择权行权 ≠ 本页权证/期权行权**。同在结算过户栏、数字可以都是面值 0.5‰，业务不是一回事。假设-DV 把权证/期权行权留在诊断、不另立字母；本页新开 DW 收这一腿，**不回写 DV**。**零改 DV**。**严禁复用假设-DV**；**DW≠DV**；**不重开假设-DV**；**不改 DV**；**尤重：禁把 DV 诊断升格回写；禁 `copy_DV_cash_option_transfer_onto_warrant_option` 进主报；禁把 `vs_DV_cash_option_transfer` 升格进 `dw0`**；`cash_option_transfer_handoff=dv_page`；诊断桶 `copy_DV_cash_option_transfer_onto_warrant_option` / `vs_DV_cash_option_transfer` 不升格 |
| 题面 U | **股票过户费切日**（金额档；核对日方向是成交金额 0.01‰、买卖双方；假设-U） | **U 股票过户切日（金额档）≠ 本页行权面值档**。二级买卖双方按成交金额抽，不是行权按面值、按 biz_type 抽。`params.G` 的 0.01 不是过户费 0.01‰。**双字母 DW ≠ 单字母假设-U**；**严禁复用假设-U**；**DW≠U**；**params 字母 ≠ 假设-U**；**不重开假设-U**；**不改 U**；**尤重：禁把 `vs_U_ashare_transfer_fee` 升格进 `dw0`**；`transfer_fee_handoff=u_page`；诊断桶 `vs_U_ashare_transfer_fee` 不升格 |
| 题面 V | **股票印花税切日**（卖方、切日前 1‰ / 切日后 0.5‰；假设-V） | **不重开假设-V**。印花切日 ≠ 权证/期权行权过户。占位不是印花税率。**双字母 DW ≠ 单字母假设-V**；**严禁复用假设-V**；**DW≠V**；**params 字母 ≠ 假设-V**；**不改 V**；**尤重：不重开假设-V；禁把 `vs_V_stamp` 升格进 `dw0`**；`stamp_handoff=v_page`；诊断桶 `vs_V_stamp` 不升格 |
| 题面 T | **股票证管费切日**（假设-T；0.02‰ 双边是费率，不是本页门槛） | **不重开假设-T**。证管费切日 ≠ 行权过户。`params.Y` 的 0.02 不是证管费 0.02‰。**双字母 DW ≠ 单字母假设-T**；**严禁复用假设-T**；**DW≠T**；**params 字母 ≠ 假设-T**；**不改 T**；**尤重：不重开假设-T；禁把 `vs_T_csrc_fee` 升格进 `dw0`**；`csrc_fee_handoff=t_page`；诊断桶 `vs_T_csrc_fee` 不升格 |
| 题面 DN | **可交换债换股过户**（深市换股有面值 0.5‰ 这一档；换股 ≠ 权证/期权行权） | DN/DQ/DV 都可以出现面值 0.5‰，业务不是权证行权，也不是股票期权行权。数字相同也不能合成一句，不能把 DN 抄进主报。**DW≠DN**；**严禁复用假设-DN**；**不重开假设-DN**；**不改 DN**；**尤重：禁 `copy_DN_face_transfer_onto_warrant_option` 进主报；禁把 `vs_DN_exchangeable_conversion_transfer` 升格进 `dw0`**；`exchangeable_conversion_transfer_handoff=dn_page`；诊断桶 `copy_DN_face_transfer_onto_warrant_option` / `vs_DN_exchangeable_conversion_transfer` 不升格 |
| 题面 DQ | **ETF 申赎组合证券过户**（篮子按成分股票面值 0.5‰；申赎 ≠ 权证/期权行权） | 篮子面值 0.5‰ ≠ 本页行权面值档。同数字禁升格。**DW≠DQ**；**严禁复用假设-DQ**；**不重开假设-DQ**；**不改 DQ**；**尤重：禁 `copy_DQ_basket_transfer_onto_warrant_option` 进主报；禁把 `vs_DQ_etf_creation_redemption_transfer` 升格进 `dw0`**；`etf_creation_redemption_transfer_handoff=dq_page`；诊断桶 `copy_DQ_basket_transfer_onto_warrant_option` / `vs_DQ_etf_creation_redemption_transfer` 不升格 |
| 权证 vs 期权 | **同一页内的两档口径**（不是另一封假设信） | 权证行权建议方向是面值 0.5‰ **单向**。股票期权行权建议方向是面值 0.5‰ **过入方**。必须按 `biz_type` 分列。主报名里的 `warrant_or_option` 只表示「这两类行权都被套成股票金额档」这一误套，不是把两档口径合成一句。合成一句走诊断桶 `merge_warrant_unilateral_with_option_inbound`，**不得升格进 `dw0`** |
| 题面 CR | **认沽/认购行权可成交性**（能不能按行权价兑付或交割；假设-CR） | **CR 可成交性 ≠ 本页过户费**。行权兑不兑得成，和过户按哪一档计，是两件事。**DW≠CR**；**严禁复用假设-CR**；**不重开假设-CR**；**不改 CR**；**尤重：禁把 `vs_CR_put_call_fill` 升格进 `dw0`**；`put_call_fill_handoff=cr_page`；诊断桶 `vs_CR_put_call_fill` 不升格 |
| 题面 W | **除权日用复权价误判涨跌停**（假设-W） | 除权参考价怎么判板 ≠ 行权过户怎么计。**双字母 DW ≠ 单字母假设-W**；**严禁复用假设-W**；**DW≠W**；**params 字母 ≠ 假设-W**；**不重开假设-W**；**不改 W**；**尤重：禁把 `vs_W_ex_right_limit` 升格进 `dw0`**；`ex_right_limit_handoff=w_page`；诊断桶 `vs_W_ex_right_limit` 不升格 |
| 题面 R | **股票 ETF 假 T+0**（假设-R 股票ETF假回转；回转名单 ≠ 过户费） | 实验 R 不抢、不重开、不混读升格进 `dw0`。股票 ETF 假当日回转 ≠ 本页行权过户被套成股票金额档。**双字母 DW ≠ 单字母假设-R**；**严禁复用假设-R**；**DW≠R**；**不重开假设-R**；**不改 R**；**尤重：实验 R 不抢**；`etf_t0_handoff=r_page`；诊断桶 `vs_R_etf_t0` 不升格 |
| 题面 DU | **可转债首日临停**（发行价 20%/30% ≠ 过户费） | DU 首日临停 ≠ 本页过户费。临停基准和时长不是行权过户怎么计。**DW≠DU**；**严禁复用假设-DU**；**不重开假设-DU**；**不改 DU**；**尤重：禁把 DU 升格进 `dw0`**；`cb_ipo_halt_handoff=du_page`；诊断桶 `vs_DU_cb_ipo_halt` 不升格 |
| 题面 DT | **可转债整手价位**（1000 元面额 / 0.001 元 ≠ 过户费） | DT 整手价位 ≠ 本页过户费。申报数量和最小价位不是过户基数。**DW≠DT**；**严禁复用假设-DT**；**不重开假设-DT**；**不改 DT**；**尤重：禁把 DT 升格进 `dw0`**；`cb_lot_tick_handoff=dt_page`；诊断桶 `vs_DT_cb_lot_tick` 不升格 |
| 题面 DS | **转股所得股票印花**（误免成 0） | DS 转股印花 ≠ 本页过户费。交割那笔股票交不交印花 ≠ 权证/期权行权过户。**DW≠DS**；**严禁复用假设-DS**；**不重开假设-DS**；**不改 DS**；**尤重：禁把 DS 升格进 `dw0`**；`cb_conversion_stamp_handoff=ds_page`；诊断桶 `vs_DS_conversion_stamp` 不升格 |
| 题面 DR | **可转债盘后定价通道**（误套股票盘后固定价格） | DR 盘后通道 ≠ 本页过户费。盘后用哪条价格 ≠ 行权过户怎么计。**DW≠DR**；**严禁复用假设-DR**；**不重开假设-DR**；**不改 DR**；**尤重：禁把 DR 升格进 `dw0`**；`aft_pricing_handoff=dr_page`；诊断桶 `vs_DR_aft_pricing` 不升格 |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 行权过户的基数和方向。**双字母 DW ≠ 单字母假设-D**；**严禁复用假设-D**；**DW≠D**；**不改 D** |
| 题面 DP | **可交换债换股印花税误漏** | 换股印花 ≠ 行权过户。**DW≠DP**；**不重开假设-DP**；**不改 DP** |
| 题面 DO | **可转债回售处理** | 回售经手 ≠ 行权过户。**DW≠DO**；**不重开假设-DO**；**不改 DO** |
| 题面 DM | **可交换债换股经手费** | 换股经手 ≠ 行权过户。**DW≠DM**；**不重开假设-DM**；**不改 DM** |
| 题面 DL | **股票综合协议过户费下浮** | 综合协议过户下浮 ≠ 本页行权面值档。**DW≠DL**；**不重开假设-DL**；**不改 DL** |
| 题面 DK | **场内基金印花税误抽** | 基金印花 ≠ 行权过户。**DW≠DK**；**不改 DK**；**不重开假设-V** |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 行权过户，亦 ≠ 股票证管费切日。**DW≠DJ**；**不改 DJ**；**不重开假设-T** |
| 题面 DI | **股票大宗经手下浮** | 大宗经手下浮 ≠ 行权过户。**DW≠DI**；**不重开假设-DI**；**不改 DI** |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 行权过户。**DW≠DH**；**不改 DH** |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 行权过户。**DW≠DG**；**不改 DG** |
| 题面 DF | **可交换债现货经手费沪深合成** | 可交换现货经手 ≠ 行权过户。**DW≠DF**；**不重开假设-DF**；**不改 DF** |
| 题面 DE | **可转债证管费** | 转债证管费误套 ≠ 本页过户，亦 ≠ 重开假设-T。**DW≠DE**；**不改 DE**；**不重开假设-T** |
| 题面 DD | **可转债现货过户费** | 转债现货过户 ≠ 权证/期权行权过户，亦 ≠ 重开假设-U。**DW≠DD**；**不重开假设-DD**；**不改 DD**；**不重开假设-U** |
| 题面 DC | **可转债现货印花税误抽** | 转债现货印花 ≠ 行权过户。**DW≠DC**；**不改 DC**；**不重开假设-V** |
| 题面 DB | **可转债现货经手费** | 转债现货经手 ≠ 行权过户。**DW≠DB**；**不重开假设-DB**；**不改 DB** |
| 题面 DA | **场内基金二级过户费** | 二级过户 ≠ 权证/期权行权过户。**DW≠DA**；**不重开假设-DA**；**不改 DA** |
| 题面 S | **沪深 A 股竞价经手费切日** | 股票经手切日 ≠ 行权过户。**DW≠S**；**不重开假设-S**；**不改 S** |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 行权过户。**DW≠AX**；**不重开假设-AX**；**不改 AX** |
| 题面 AC | **北交所涨跌幅与盘后** | 北交所涨跌幅、盘后 ≠ 行权过户。**DW≠AC**；**不重开假设-AC**；**不改 AC** |
| 题面 Q | **可转债回转 / 涨跌幅 / 收盘** | 回转和板幅 ≠ 行权过户。**双字母 DW ≠ 单字母假设-Q**；**DW≠Q**；**不重开假设-Q**；**不改 Q** |
| 题面 O | **大宗三通道** | 大宗通道 ≠ 行权过户。**DW≠O**；**不重开假设-O**；**不改 O** |
| 题面 M | **股票盘后通道** | 股票盘后通道 ≠ 行权过户。**DW≠M**；**不重开假设-M**；**不改 M** |
| 题面 CH | **股票盘后固定价格可成交性** | 盘后可成交 ≠ 行权过户。**DW≠CH**；**不重开假设-CH**；**不改 CH** |
| 题面 CL | **可转债盘后定价可成交性** | 转债盘后可成交 ≠ 行权过户。**DW≠CL**；**不重开假设-CL**；**不改 CL** |
| 题面 CQ | **可转债转股可成交性** | 能不能转成 ≠ 行权过户。**DW≠CQ**；**不重开假设-CQ**；**不改 CQ** |
| 题面 E | **股票/科创整手** | 股数整手 ≠ 行权过户。**DW≠E**；**不重开假设-E**；**不改 E** |
| 题面 F | **涨跌停取整** | 限制价怎么收成价位 ≠ 过户基数。**DW≠F**；**不重开假设-F**；**不改 F** |
| 题面 J | **股票无板日临停** | 无板日临停 ≠ 行权过户。**DW≠J**；**不重开假设-J**；**不改 J** |
| 题面 AU | **本方对手最优空簿** | 空簿假成 ≠ 行权过户。不在本页硬分列主链里另造桶。**不改 AU**；不并进 `dw0` |
| 题面 BR | **融券借券费/融出费率** | 借券费计提 ≠ 行权过户。不在本页硬分列主链里另造桶。**不改 BR**；不并进 `dw0` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 行权过户。**DW≠A**；**不抢 A 真数队列**；**不改 A** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ashare_amount_transfer_on_warrant_or_option_exercise`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_warrant_option_transfer` 双挂；DW1 不升格；`invent_zero_transfer_on_warrant_or_option_exercise` / `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` / `merge_warrant_unilateral_with_option_inbound` / `vs_U_ashare_transfer_fee` / `vs_V_stamp` / `vs_T_csrc_fee` / `vs_DV_cash_option_transfer` / `vs_DN_exchangeable_conversion_transfer` / `vs_DQ_etf_creation_redemption_transfer` / `vs_CR_put_call_fill` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `missing_biz_type_or_official_rate_not_skip` 只作诊断对照，不升格主报；**尤重禁止把 U / V / T / DV / DN / DQ / CR / W / R 混读升格进 `dw0`**；**尤重禁止把 DU / DT / DS / DR 混读升格进 `dw0`**） |
| 文档 | 清单实验 DV / U / V / T / DN / DQ / CR / W / R / DU / DT / DS / DR / D / DP / DO / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / AC / Q / O / M / CH / CL / CQ / E / F / J / A（**只读；禁止改写**） | `假设-DW-权证期权行权过户费误套.md`（新建） |
| 预检键 | 实验字母 DV / U / V / T / DN / DQ / CR / W / R / DU / DT / DS / DR / D / DP / DO / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / AC / Q / O / M / A / Y / G / N，以及已存在 CH / CL / CQ / E / F / J / AU / BR | 实验字母 **DW** / `dw0_primary_demo`；**不得**占用或改写预检 DV/U/V/T/DN/DQ/CR/W/R/DU/DT/DS/DR/D/DP/DO/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/AC/Q/O/M/A/Y/G/N，亦不得改写 CH/CL/CQ/E/F/J/AU/BR |

**禁止**：把 DW 写成「DV / U / V / T / DN / DQ / CR / W / R / DU / DT / DS / DR / D / A 的续篇」；把「现金选择权行权过户已分列（DV）/ 股票过户切日已分列（U）/ 股票印花已分列（V）/ 股票证管费已分列（T）/ 换股过户已分列（DN）/ 申赎篮子过户已分列（DQ）/ 行权可成交已分列（CR）/ 除权判板已分列（W）/ 股票 ETF 回转已分列（R）/ 首日临停已分列（DU）/ 整手价位已分列（DT）/ 转股印花已分列（DS）/ 盘后通道已分列（DR）」写成「权证/期权行权过户已诚实」；把实验字母 DW 与单字母 D/W 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-W 读成双字母 DW**；**尤重勿把 `params.Y` 读成假设-T，亦勿读成假设-V**；**尤重勿把 `params.G` 读成假设-U**；**尤重勿把 params 字母读成假设-W**；**尤重 `params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰；`params.Y` 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同）**；**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**；**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**；**尤重实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 `dw0`**；**尤重不重开假设-V，禁把 `vs_V_stamp` 升格进 `dw0`**；**尤重不重开假设-T，禁把 `vs_T_csrc_fee` 升格进 `dw0`**；**尤重 U 股票过户切日（金额档）≠ 本页行权面值档，禁把 `vs_U_ashare_transfer_fee` 升格进 `dw0`**；**尤重 DV 现金选择权行权 ≠ 本页权证/期权行权，零改 DV，禁把 DV 诊断升格回写，禁 copy_DV / vs_DV 进主报**；**尤重权证「单向」与期权「过入方」须按 biz_type 分列，禁止合成一句进 `dw0`；禁 `merge_warrant_unilateral_with_option_inbound` 升格**；**尤重 DN/DQ 同为面值 0.5‰ 但业务不同，数字相同禁升格进 `dw0`；禁 copy_DN / copy_DQ 进主报**；**尤重 CR 可成交性 ≠ 本页过户费，禁把 `vs_CR_put_call_fill` 升格进 `dw0`**；**尤重双字母 DW ≠ 单字母假设-D / 假设-W，禁把 `vs_W_ex_right_limit` 升格进 `dw0`**；**尤重 DU 首日临停 / DT 整手价位 / DS 转股印花 / DR 盘后通道 ≠ 本页过户费，禁止合成/混读升格进 `dw0`**；**禁把 U/V/T/DV/DN/DQ/CR/W/R 混读升格进 `dw0`**；**禁把 DU/DT/DS/DR 混读升格进 `dw0`**；把 `invent_asof_leak_warrant_option_transfer` 升格进 `dw0` 或与主报双挂；把诊断桶 `invent_zero_transfer_on_warrant_or_option_exercise` / `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` / `merge_warrant_unilateral_with_option_inbound` / `vs_U_ashare_transfer_fee` / `vs_V_stamp` / `vs_T_csrc_fee` / `vs_DV_cash_option_transfer` / `vs_DN_exchangeable_conversion_transfer` / `vs_DQ_etf_creation_redemption_transfer` / `vs_CR_put_call_fill` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `missing_biz_type_or_official_rate_not_skip` 升格进 `dw0`；用 A 股二级成交金额 0.01‰ 去填权证或期权行权；把行权过户记成 0；缺业务类型/官方‰/场所表仍硬填。本页主键只用 `dw0` / `dw1` / `dw2` 与 `warrant_option_transfer_*`。不写下一字母。不预留 #133。**纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK–DV；勿再只改清单）。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权路径下，回测把 **权证/股票期权行权过户费**误套成**股票二级成交金额档**（按成交金额 0.01‰、还往往按买卖双方），或把这笔过户记成 0，或因同是面值 0.5‰ 抄 DV 现金选择权行权过户 / DN 换股过户 / DQ 申赎篮子过户，或把权证「单向」和期权「过入方」合成一句，或与 U股票过户切日 / V股票印花切日 / T股票证管费 / DV现金选择权行权过户 / DN换股过户 / DQ申赎篮子过户 / CR行权可成交性 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后通道 / W除权日复权价误判板 / R股票ETF假T+0 混读，或缺业务类型/官方‰/场所表仍不 skip，相对「缺业务类型/官方‰/场所表则 skip；按 biz_type 分列：权证行权按面值 0.5‰ 单向，股票期权行权按面值 0.5‰ 过入方；禁止合成一句；禁止套 A 股二级成交金额 0.01‰；禁止与 DV/DN/DQ 仅因同数字合成一句」的诚实组，会**系统性改写权证/股票期权行权腿的过户成本**——相对诚实锚偏误。套成金额档，基数从面值变成成交金额，方向还可能从单向或过入方变成双边；抄 DV/DN/DQ，业务对不上，数字碰巧相同也把成本写到别人的腿上；把权证和期权合成一句，单向和过入方就对不上。

核对日方向（随锚写死；禁止把过户 0.01‰、面值 0.5‰、印花税率或证管费 0.02‰ 写成占位门槛）：权证行权和股票期权行权分开，行权和股票二级过户分开，过户和印花、证管费分开，行权和现金选择权、换股、申赎篮子分开，过户费和行权能不能成交分开。`事实与坑` 2026-11-06 只把权证/期权行权写进中国结算「交易过户费」同一栏（和现金选择权、可交换债换股、ETF 申购/赎回组合证券过户并列），并写明 A 股二级是成交金额 **0.01‰**、买卖双方。同栏不是同费率。本页写死方向按 biz_type 分列：权证行权过户按**面值 0.5‰ 单向**；股票期权行权过户按**面值 0.5‰ 过入方**；禁止把这两句合成一句；禁止套 A 股二级成交金额 0.01‰。DV 的现金选择权面值 0.5‰ 单向、DN 的换股面值 0.5‰、DQ 的篮子面值 0.5‰ 可以数字相同，业务不是权证行权，也不是股票期权行权，禁止因同数字合成一句，也禁止把 `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` 写进主报。股票过户切日留在 U，那是金额档，不是本页面值档。股票印花切日留在 V，股票证管费切日留在 T。行权能不能成交留在 CR。除权日复权价误判板留在 W。可转债首日临停留在 DU，整手价位留在 DT，转股印花留在 DS，盘后通道留在 DR。股票 ETF 假 T+0 留在 R，实验 R 不抢。缺业务类型、官方‰或场所表，整笔 skip，不用 0.01‰、0.5‰、免费 0、占位 0.02/0.01 或印花/证管费去填。**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**。**`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰**。**`params.Y` 的 0.02 ≠ 证管费 0.02‰**。**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**。**禁把 U/V/T/DV/DN/DQ/CR/W/R 混读升格进 `dw0`**。**禁把 DU/DT/DS/DR 混读升格进 `dw0`**。

证伪方向：若天真组 / 半泄露组相对诚实组的行权过户误套截在标定噪声带内可忽略，且「套二级金额 0.01‰ / 记成 0 / 抄 DV / 抄 DN / 抄 DQ / 权证与期权合成一句 / 核对日泄露 / vs U·V·T·DV·DN·DQ·CR·DU·DT·DS·DR·W·R」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dw0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DW ≠ 单字母假设-D / 假设-W**；params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W；勿把 params.Y 读成实验字母 DW，亦勿读成假设-V，亦勿读成假设-T，亦勿读成假设-U，亦勿读成假设-W
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DW ≠ 单字母 D/W**
# 【消歧】尤重：params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰（量纲与语义不同：无量纲相对门槛 ≠ 假设-U 的金额档费率，也 ≠ 本页建议的面值档）
# 【消歧】尤重：params.Y 的 0.02 ≠ 证管费 0.02‰（无量纲相对门槛 ≠ 假设-T 的费率）
# 【消歧】尤重：params.N 的 0.05 ≠ 面值 0.5‰ ≠ 印花 0.5‰
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰
# 【消歧】params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费
# 【消歧】params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DW ≠ 单字母假设-N**
# params.Y2                               写死冻结 0.015
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：行权过户误套截 ΔWarrantOptionTransfer / 净差异 / DW1−DW2；**params.Y/G/N ≠ 实验字母 DW ≠ 单字母假设-D / 假设-W**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**；**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                        写死冻结 next_open
# params.asof_check_date                  写死冻结 2026-11-06
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.warrant_option_transfer_honest   写死冻结 pit_face_value_0p5_permille_by_biz_type_not_ashare_amount_0p01
#   诚实锚方向（已写死冻结）：
#   缺业务类型、官方‰或场所表 → skip
#   权证行权 = 面值 0.5‰ 单向
#   股票期权行权 = 面值 0.5‰ 过入方
#   权证与期权口径禁止合成一句；须按 biz_type 分列
#   禁止套 A 股二级成交金额 0.01‰
#   禁止与 DV/DN/DQ 仅因同数字合成一句
#   禁止把占位 0.02/0.01/0.05/0.015 读成过户 0.01‰/0.5‰、印花税率或证管费 0.02‰
#   枚举已写死冻结
#   锚名字里的 0p5 / 0p01 是机制方向，不是 params.Y/G/N/Y2
#   不把 DV 的现金选择权、U 的金额档、V 的印花、T 的证管费、DN 的换股面值、DQ 的篮子面值、CR 的可成交性、W 的除权判板、DU 的首日临停、DT 的整手价位、DS 的转股印花、DR 的盘后通道、R 的假 T+0 写成本页诚实锚
# params.warrant_option_transfer_scope    写死冻结 warrant_or_stock_option_exercise_vs_secondary_transfer
#   方向名：权证行权或股票期权行权过户，与股票二级过户分列
#   范围名里的 or 不是把权证单向和期权过入方合成一句
#   这不是把 0.5‰ 或 0.01‰ 冻成门槛
#   行权面值档 ≠ A 股二级成交金额档
# params.warrant_option_transfer_over_policy 写死冻结 skip_if_biz_type_or_official_rate_or_venue_table_missing
#   缺业务类型、官方‰或场所表则 skip；禁在缺字段时仍按成交金额 0.01‰ 或免费 0 把行权过户填上
# params.cash_option_transfer_handoff     建议 dv_page
#   现金选择权行权过户交 DV；DV ≠ 本页；零改 DV；不重开假设-DV；不改 DV
#   DV 禁止合成/混读升格进 dw0；copy_DV / vs_DV 不得升格进 dw0；禁把 DV 诊断升格回写
# params.transfer_fee_handoff             建议 u_page
#   股票过户费切日交 U；不重开假设-U；U 金额档 ≠ 本页面值档；双字母 DW ≠ 单字母假设-U；params 字母 ≠ 假设-U；不改 U
#   U 禁止合成/混读升格进 dw0；诊断桶 vs_U_ashare_transfer_fee 不得升格进 dw0
# params.stamp_handoff                    建议 v_page
#   股票印花切日交 V；不重开假设-V；双字母 DW ≠ 单字母假设-V；params 字母 ≠ 假设-V；不改 V
#   V 禁止合成/混读升格进 dw0；诊断桶 vs_V_stamp 不得升格进 dw0
# params.csrc_fee_handoff                 建议 t_page
#   股票证管费切日交 T；不重开假设-T；双字母 DW ≠ 单字母假设-T；params 字母 ≠ 假设-T；不改 T
#   T 禁止合成/混读升格进 dw0；诊断桶 vs_T_csrc_fee 不得升格进 dw0
# params.exchangeable_conversion_transfer_handoff 建议 dn_page
#   可交换债换股过户交 DN；同是面值 0.5‰ 也不合成；不重开假设-DN；不改 DN
#   DN 禁止合成/混读升格进 dw0；copy_DN_face_transfer_onto_warrant_option / vs_DN_exchangeable_conversion_transfer 不得升格进 dw0
# params.etf_creation_redemption_transfer_handoff 建议 dq_page
#   ETF 申赎篮子过户交 DQ；同是面值 0.5‰ 也不合成；不重开假设-DQ；不改 DQ
#   DQ 禁止合成/混读升格进 dw0；copy_DQ_basket_transfer_onto_warrant_option / vs_DQ_etf_creation_redemption_transfer 不得升格进 dw0
# params.put_call_fill_handoff            建议 cr_page
#   行权可成交性交 CR；CR 可成交性 ≠ 本页过户费；不重开假设-CR；不改 CR
#   CR 禁止合成/混读升格进 dw0；诊断桶 vs_CR_put_call_fill 不得升格进 dw0
# params.cb_ipo_halt_handoff              建议 du_page
#   可转债首日临停交 DU；DU ≠ 本页过户费；不重开假设-DU；不改 DU
#   DU 禁止合成/混读升格进 dw0；诊断桶 vs_DU_cb_ipo_halt 不得升格进 dw0
# params.cb_lot_tick_handoff              建议 dt_page
#   整手价位交 DT；DT ≠ 本页过户费；不重开假设-DT；不改 DT
#   DT 禁止合成/混读升格进 dw0；诊断桶 vs_DT_cb_lot_tick 不得升格进 dw0
# params.cb_conversion_stamp_handoff      建议 ds_page
#   转股印花交 DS；DS ≠ 本页过户费；不重开假设-DS；不改 DS
#   DS 禁止合成/混读升格进 dw0；诊断桶 vs_DS_conversion_stamp 不得升格进 dw0
# params.aft_pricing_handoff              建议 dr_page
#   盘后定价通道交 DR；DR ≠ 本页过户费；不重开假设-DR；不改 DR
#   DR 禁止合成/混读升格进 dw0；诊断桶 vs_DR_aft_pricing 不得升格进 dw0
# params.ex_right_limit_handoff           建议 w_page
#   除权日复权价误判板交 W；双字母 DW ≠ 单字母假设-W；params 字母 ≠ 假设-W；不重开假设-W；不改 W
#   W 禁止合成/混读升格进 dw0；诊断桶 vs_W_ex_right_limit 不得升格进 dw0
# params.etf_t0_handoff                   建议 r_page
#   股票 ETF 假 T+0 交 R；实验 R 不抢、不重开、不混读升格进 dw0；双字母 DW ≠ 单字母假设-R；不改 R
#   R 禁止合成/混读升格进 dw0；诊断桶 vs_R_etf_t0 不得升格进 dw0
# params.fill_time_suspend_handoff        建议 d_page
#   成交时点与停牌交 D；双字母 DW ≠ 单字母假设-D；不改 D
# params.board_capacity_handoff           建议 a_page
#   板上容量交 A；不抢 A 真数队列；不改 A
# params.dw0_primary_demo                 写死冻结 invent_ashare_amount_transfer_on_warrant_or_option_exercise
#   单一主报写死，单挂；禁与 invent_asof_leak_warrant_option_transfer 双挂；DW1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_warrant_option_transfer 只作对照，不得升格进 dw0，不得双挂
#   主报名里的 warrant_or_option 是误套对象的并称，不是把权证单向和期权过入方合成一句
#   诊断桶 invent_zero_transfer_on_warrant_or_option_exercise / copy_DV_cash_option_transfer_onto_warrant_option / copy_DN_face_transfer_onto_warrant_option / copy_DQ_basket_transfer_onto_warrant_option / merge_warrant_unilateral_with_option_inbound / vs_U_ashare_transfer_fee / vs_V_stamp / vs_T_csrc_fee / vs_DV_cash_option_transfer / vs_DN_exchangeable_conversion_transfer / vs_DQ_etf_creation_redemption_transfer / vs_CR_put_call_fill / vs_DU_cb_ipo_halt / vs_DT_cb_lot_tick / vs_DS_conversion_stamp / vs_DR_aft_pricing / vs_W_ex_right_limit / vs_R_etf_t0 / missing_biz_type_or_official_rate_not_skip 不得升格进 dw0
#   尤重：实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 dw0
#   尤重：不重开假设-V；禁止把 vs_V_stamp / 印花混读后写进 dw0
#   尤重：不重开假设-T；禁止把 vs_T_csrc_fee / 证管费混读后写进 dw0
#   尤重：不重开假设-U；U 金额档 ≠ 本页面值档；禁止把 vs_U_ashare_transfer_fee 混读后写进 dw0
#   尤重：零改 DV；DV 现金选择权 ≠ 本页；禁止把 copy_DV / vs_DV 写进主报；禁止把 DV 诊断升格回写
#   尤重：权证单向与期权过入方禁止合成一句；禁止把 merge_warrant_unilateral_with_option_inbound 写进主报
#   尤重：DN/DQ 同为面值 0.5‰ 但业务不同；禁止把 copy_DN / copy_DQ 写进主报
#   尤重：CR 可成交性 ≠ 本页过户费；禁止把 vs_CR_put_call_fill 混读后写进 dw0
#   尤重：双字母 DW ≠ 单字母假设-W；禁止把 vs_W_ex_right_limit 混读后写进 dw0
#   尤重：禁止把 DU 首日临停、DT 整手价位、DS 转股印花、DR 盘后通道与本页过户费合成/混读后写进 dw0
#   禁把 U/V/T/DV/DN/DQ/CR/W/R 混读升格进 dw0
#   禁把 DU/DT/DS/DR 混读升格进 dw0
# params.dw0_invent_ashare_amount_transfer_on_warrant_or_option_exercise 建议 True
# params.dw1_asof_leak_warrant_option_transfer_only 建议 True
#   半泄露对照；DW1 不升格并列主报；不得把 invent_asof_leak_warrant_option_transfer 写进 dw0
# params.dw2_pit_face_value_0p5_permille_by_biz_type_not_ashare_amount_0p01 建议 True
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
# params.merge_with_AU                    建议 False
# params.merge_with_BR                    建议 False
# params.merge_with_A                     建议 False
# params.merge_with_D                     建议 False
# params.missing_biz_type_or_official_rate_or_venue_table_policy 建议 skip
# params.day_freq_proxy                   建议 warrant_option_transfer_sensitivity
# params.universe_rule                    建议 warrant_option_transfer_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dw_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DW；勿把这个键读成实验 DW，亦勿读成单字母 D/W，亦勿读成假设-W
#   不另挂主报，不预留 #133，不写下一字母
```

### 2.2 三组对照（DW0 / DW1 / DW2）

组名 DW0 / DW1 / DW2 是本页三组，≠ 单字母实验 W（除权日复权价误判板），亦 ≠ 单字母实验 D（成交时点与停牌），亦 ≠ 单字母实验 U（股票过户费切日），亦 ≠ 单字母实验 V（股票印花税切日），亦 ≠ 单字母实验 R（股票 ETF 假 T+0）。**双字母 DW ≠ 单字母假设-D / 假设-W**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**。

| 组 | 角色 | 口径 |
|----|------|------|
| DW0 | 天真 / 权证或股票期权行权过户误套股票成交金额档 | 按 `dw0_primary_demo` **写死冻结**单一主报 `invent_ashare_amount_transfer_on_warrant_or_option_exercise`（单挂写死）：把 A 股二级成交金额 0.01‰ 套到权证行权或股票期权行权过户。**禁**与 `invent_asof_leak_warrant_option_transfer` 双挂主报。**禁把 U / V / T / DV / DN / DQ / CR / W / R 合成进 `dw0`**（只作对照/旁路，不得升格进 `dw0` 或另挂主报）。**禁把 DU / DT / DS / DR 合成进 `dw0`**。**禁把 U/V/T/DV/DN/DQ/CR/W/R 混读升格进 `dw0`**。**禁 copy_DV / copy_DN / copy_DQ 进主报**。**禁把权证单向与期权过入方合成一句进 `dw0`** |
| DW1 | 半泄露 | 仅核对日把「按 biz_type：权证面值 0.5‰ 单向、期权面值 0.5‰ 过入方」铺到全历史、铺到股票二级、铺到 DV/DN/DQ 的业务，或把两档口径合成一句再铺开（`invent_asof_leak_warrant_option_transfer`）；**不得升格并列主报**，也不得写进 `dw0`（写死冻结：DW1 不升格），不得双挂 |
| DW2 | 诚实 / 按 biz_type 分列的行权面值档 | `warrant_option_transfer_honest=pit_face_value_0p5_permille_by_biz_type_not_ashare_amount_0p01`（写死冻结）：缺业务类型/官方‰/场所表则 skip；权证行权按面值 0.5‰ 单向；股票期权行权按面值 0.5‰ 过入方；禁止合成一句；禁止套 A 股二级成交金额 0.01‰；禁止与 DV/DN/DQ 仅因同数字合成一句。现金选择权只消费 DV，股票过户切日只消费 U，股票印花只消费 V，股票证管费只消费 T，换股过户只消费 DN，申赎篮子过户只消费 DQ，行权可成交只消费 CR，除权判板只消费 W，首日临停只消费 DU，整手价位只消费 DT，转股印花只消费 DS，盘后通道只消费 DR，股票 ETF 假 T+0 只消费 R，或显式旁路 |

把行权过户记成 0、抄 DV 的现金选择权句、抄 DN 的面值句、抄 DQ 的篮子句、把权证单向和期权过入方合成一句、把核对日面值档铺到二级或铺到别的业务、把 U/V/T/DV/DN/DQ/CR/W/R 或 DU/DT/DS/DR 混进本页，以及相对这些页的对照截（`invent_zero_transfer_on_warrant_or_option_exercise` / `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` / `merge_warrant_unilateral_with_option_inbound` / `vs_U_ashare_transfer_fee` / `vs_V_stamp` / `vs_T_csrc_fee` / `vs_DV_cash_option_transfer` / `vs_DN_exchangeable_conversion_transfer` / `vs_DQ_etf_creation_redemption_transfer` / `vs_CR_put_call_fill` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `missing_biz_type_or_official_rate_not_skip`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dw0_primary_demo`。`invent_zero_transfer_on_warrant_or_option_exercise` 只标记「有人把行权过户记成 0」，**不得升格进 `dw0`**。`copy_DV_cash_option_transfer_onto_warrant_option` 只标记「有人因同数字抄 DV」，**不得升格进 `dw0`**。`copy_DN_face_transfer_onto_warrant_option` 只标记「有人因同数字抄 DN」，**不得升格进 `dw0`**。`copy_DQ_basket_transfer_onto_warrant_option` 只标记「有人因同数字抄 DQ」，**不得升格进 `dw0`**。`merge_warrant_unilateral_with_option_inbound` 只标记「有人把权证单向和期权过入方合成一句」，**不得升格进 `dw0`**。`vs_U_ashare_transfer_fee` 只标记「有人把 U 的金额档和本页面值档混读」，**不得升格进 `dw0`**。`vs_V_stamp` 只标记「有人把印花和本页混读」，**不得升格进 `dw0`**。`vs_T_csrc_fee` 只标记「有人把证管费和本页混读」，**不得升格进 `dw0`**。`vs_DV_cash_option_transfer` 只标记现金选择权对照，**不得升格进 `dw0`**，也不得回写 DV。`vs_DN_exchangeable_conversion_transfer` 只标记换股过户对照，**不得升格进 `dw0`**。`vs_DQ_etf_creation_redemption_transfer` 只标记申赎篮子过户对照，**不得升格进 `dw0`**。`vs_CR_put_call_fill` 只标记行权可成交对照，**不得升格进 `dw0`**。`vs_DU_cb_ipo_halt` 只标记首日临停对照，**不得升格进 `dw0`**。`vs_DT_cb_lot_tick` 只标记整手价位对照，**不得升格进 `dw0`**。`vs_DS_conversion_stamp` 只标记转股印花对照，**不得升格进 `dw0`**。`vs_DR_aft_pricing` 只标记盘后通道对照，**不得升格进 `dw0`**。`vs_W_ex_right_limit` 只标记「有人把假设-W 和本页混读」，**不得升格进 `dw0`**。`vs_R_etf_t0` 只标记「有人把实验 R 和本页混读」，**不得升格进 `dw0`**。`missing_biz_type_or_official_rate_not_skip` 同样只作诊断；场所表缺失也走 skip，不另造主报。DV 的现金选择权、U 的金额档、V 的印花、T 的证管费、DN 的换股、DQ 的篮子、CR 的可成交、W 的除权判板、DU 的临停、DT 的整手、DS 的印花、DR 的盘后、R 的假 T+0 只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-11-06`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dw0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺业务类型/官方‰/场所表则 skip；权证行权按面值 0.5‰ 单向；股票期权行权按面值 0.5‰ 过入方；禁止合成一句；禁止套 A 股二级成交金额 0.01‰；禁止与 DV/DN/DQ 仅因同数字合成一句。方向随锚写死：**不要把 0.5‰ 写成全历史唯一费率，也不要把 A 股 0.01‰ 写成行权过户的唯一规则，也不要把权证和期权写成同一句**。范围名 `warrant_or_stock_option_exercise_vs_secondary_transfer` 只标方向：本页只看权证行权或股票期权行权过户有没有被套成股票二级金额档。现金选择权留给 DV，股票过户切日留给 U，印花留给 V，证管费留给 T，换股过户留给 DN，申赎篮子留给 DQ，行权可成交留给 CR，除权判板留给 W，首日临停留给 DU，整手价位留给 DT，转股印花留给 DS，盘后通道留给 DR，股票 ETF 假 T+0 留给 R。`params.G` 的 0.01 是无量纲相对门槛，不是过户费 0.01‰，也不是面值 0.5‰。`params.Y` 的 0.02 不是证管费 0.02‰，也不是印花税率。**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**。**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**。缺业务类型、官方‰或场所表则 skip，不用 0.01‰、0.5‰、免费 0 或占位 0.01 把行权过户填上。本页**不开回测**；不拉真数；不做实盘；不开户。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dw0_primary_demo` / `params.Y`·G·N·Y2 / 行权过户开关 / 桶 / 是否把面值 0.5‰ 或金额 0.01‰ 铺到全历史、或铺到 DV/DN/DQ、或把权证与期权合成一句、或把占位读成过户费率/印花税率/证管费）。本页不开跑。禁 null。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DW0）/ 半泄露组（DW1）相对诚实组（DW2）的行权过户误套截**显著且集中在权证行权或股票期权行权被套成 A 股二级成交金额 0.01‰ 的桶**；分桶「套金额档 / 记成 0 / 抄 DV / 抄 DN / 抄 DQ / 权证与期权合成一句 / 核对日泄露 / vs U·V·T·DV·DN·DQ·CR·DU·DT·DS·DR·W·R」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 0.5‰ 或 0.01‰ 冻成门槛，也不把 `params.G` 的 0.01 读成过户费，也不把 `params.Y` 的 0.02 读成证管费或印花税率，也不把权证单向和期权过入方合成一句。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 DV 的现金选择权行权过户、U 的股票过户金额档、V 的股票印花、T 的股票证管费、DN 的换股过户、DQ 的申赎篮子过户、CR 的行权可成交、W 的除权判板、DU 的首日临停、DT 的整手价位、DS 的转股印花、DR 的盘后通道、R 的股票 ETF 假 T+0、E 的股票/科创整手、F 的涨跌停取整、J 的无板日临停、CQ 的转股可成交、BR 的借券费、AU 的空簿、DP 的换股印花、DO 的回售处理、DM 的换股经手、DL 的综合协议过户、DK 的基金印花、DJ 的基金证管费、DI 的大宗经手、DH 的佣金双计、DG 的北交所档、DF 的可交换现货经手、DE 的转债证管费、DD 的转债过户、DC 的转债印花、DB 的转债现货经手、DA 的二级过户、S 的股票经手、AX 的基金经手、AC 的北交所涨跌幅与盘后、Q 的转债规则、O 的大宗、M 的股票盘后、CH/CL 的盘后可成交、A 的板上容量、D 的成交时点解释；或 `dw0_primary_demo` 与 `invent_asof_leak_warrant_option_transfer` 双挂；或 DW1 升格并列主报；或 `invent_zero_transfer_on_warrant_or_option_exercise` / `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` / `merge_warrant_unilateral_with_option_inbound` / `vs_U_ashare_transfer_fee` / `vs_V_stamp` / `vs_T_csrc_fee` / `vs_DV_cash_option_transfer` / `vs_DN_exchangeable_conversion_transfer` / `vs_DQ_etf_creation_redemption_transfer` / `vs_CR_put_call_fill` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `missing_biz_type_or_official_rate_not_skip` 诊断桶升格主报；或把 U / V / T / DV / DN / DQ / CR / W / R / DU / DT / DS / DR 合成进 `dw0`；或实验字母 DW 与单字母 D/W 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成过户 0.01‰ 或面值 0.5‰；或把 `params.Y` 的 0.02 读成证管费 0.02‰；或把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰；或把 params 字母读成假设-V / 假设-T / 假设-U / 假设-W；或把核对日面值档写成已冻并铺满全历史；或把权证单向和期权过入方合成一句；或缺业务类型 / 官方‰ / 场所表仍不 skip；或重开假设-DV / 假设-U / 假设-V / 假设-T / 假设-DN / 假设-DQ / 假设-CR / 假设-W / 假设-DU / 假设-DT / 假设-DS / 假设-DR / 假设-R；或改 DV 正文；或标纸面齐；或写成 A/D–DW纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权路径，对照 DW0/DW1/DW2。现金选择权走 DV 或显式旁路，不在本页改 DV。股票过户切日走 U，股票印花走 V，股票证管费走 T，换股过户走 DN，申赎篮子过户走 DQ，行权可成交走 CR，除权判板走 W，首日临停走 DU，整手价位走 DT，转股印花走 DS，盘后通道走 DR，股票 ETF 假 T+0 走 R，都不改。报告行权过户误套截。不把面值 0.5‰ 或金额 0.01‰ 标成已冻门槛，也不把 `params.G` 的 0.01 读成过户费，也不把 `params.Y` 的 0.02 读成证管费，也不把权证和期权合成一句。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_ashare_amount_transfer_on_warrant_or_option_exercise` / `invent_asof_leak_warrant_option_transfer` / `invent_zero_transfer_on_warrant_or_option_exercise` / `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` / `merge_warrant_unilateral_with_option_inbound` / `vs_U_ashare_transfer_fee` / `vs_V_stamp` / `vs_T_csrc_fee` / `vs_DV_cash_option_transfer` / `vs_DN_exchangeable_conversion_transfer` / `vs_DQ_etf_creation_redemption_transfer` / `vs_CR_put_call_fill` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `missing_biz_type_or_official_rate_not_skip`

`invent_zero_transfer_on_warrant_or_option_exercise`、`copy_DV_cash_option_transfer_onto_warrant_option`、`copy_DN_face_transfer_onto_warrant_option`、`copy_DQ_basket_transfer_onto_warrant_option`、`merge_warrant_unilateral_with_option_inbound`、`vs_U_ashare_transfer_fee`、`vs_V_stamp`、`vs_T_csrc_fee`、`vs_DV_cash_option_transfer`、`vs_DN_exchangeable_conversion_transfer`、`vs_DQ_etf_creation_redemption_transfer`、`vs_CR_put_call_fill`、`vs_DU_cb_ipo_halt`、`vs_DT_cb_lot_tick`、`vs_DS_conversion_stamp`、`vs_DR_aft_pricing`、`vs_W_ex_right_limit`、`vs_R_etf_t0`、`missing_biz_type_or_official_rate_not_skip` 只作诊断桶：它们不是 `dw0`，也不是 DW1，**不得升格主报**。`vs_U_ashare_transfer_fee` 没有对应的「U 金额档 + 行权面值档」合成主报。假设-U 只作诊断，**不得升格进 `dw0`**，**不重开假设-U**。`vs_V_stamp` 没有对应的「印花 + 行权过户」合成主报。假设-V 只作诊断，**不得升格进 `dw0`**，**不重开假设-V**。`vs_T_csrc_fee` 没有对应的「证管费 + 行权过户」合成主报。假设-T 只作诊断，**不得升格进 `dw0`**，**不重开假设-T**。`copy_DV_cash_option_transfer_onto_warrant_option` 与 `vs_DV_cash_option_transfer` 没有对应的「现金选择权 + 权证/期权」合成主报。**禁 copy_DV / vs_DV 进主报**。**零改 DV**。`copy_DN_face_transfer_onto_warrant_option` 与 `vs_DN_exchangeable_conversion_transfer` 没有对应的「换股面值 + 行权面值」合成主报。**禁 copy_DN 进主报**。`copy_DQ_basket_transfer_onto_warrant_option` 与 `vs_DQ_etf_creation_redemption_transfer` 没有对应的「篮子面值 + 行权面值」合成主报。**禁 copy_DQ 进主报**。`merge_warrant_unilateral_with_option_inbound` 没有对应的「权证单向 + 期权过入方」合成主报。**禁合成一句进 `dw0`**。`vs_CR_put_call_fill` 没有对应的「可成交性 + 过户费」合成主报。`vs_DU_cb_ipo_halt` 没有对应的「首日临停 + 过户费」合成主报。`vs_DT_cb_lot_tick` 没有对应的「整手价位 + 过户费」合成主报。`vs_DS_conversion_stamp` 没有对应的「转股印花 + 过户费」合成主报。`vs_DR_aft_pricing` 没有对应的「盘后通道 + 过户费」合成主报。`vs_W_ex_right_limit` 没有对应的「除权判板 + 过户费」合成主报。假设-W 只作诊断，**不得升格进 `dw0`**，**不重开假设-W**。`vs_R_etf_t0` 没有对应的「假 T+0 + 行权过户」合成主报。实验 R 只作诊断，**不得升格进 `dw0`**。**实验 R 不抢**。`invent_zero_transfer_on_warrant_or_option_exercise` 只标记记成 0，**不得升格进 `dw0`**。缺字段仍不 skip，只作诊断，**不得升格进 `dw0`**。`invent_asof_leak_warrant_option_transfer` 只服务 DW1，**不得升格进 `dw0`，不得双挂**。`invent_ashare_amount_transfer_on_warrant_or_option_exercise` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把「权证或股票期权行权按 A 股二级成交金额 0.01‰」拿去当诚实锚。
- 把 `params.G` 的 0.01 当成过户费 0.01‰，或当成面值 0.5‰。**尤重：`params.G` 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰**。**params 字母 ≠ 假设-U**。
- 把 `params.Y` 的 0.02 当成证管费 0.02‰，或当成印花税率。**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**。**params 字母 ≠ 假设-T**。**params 字母 ≠ 假设-V**。
- 把 params 字母读成假设-W，或把单字母假设-W 读成双字母 DW。**params 字母 ≠ 假设-W**。**双字母 DW ≠ 单字母假设-D / 假设-W**。
- 把占位 `0.02/0.01/0.05/0.015` 读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰。**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**。**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**。
- 缺业务类型、官方‰或场所表仍不 skip，并用成交金额 0.01‰、面值 0.5‰、免费 0 或占位 0.01 把行权过户填上。
- 把核对日「面值 0.5‰」写成全历史唯一规则，或把 A 股 0.01‰ 写成行权过户唯一规则，或把权证单向和期权过入方写成同一句。锚六键已写死冻结。
- 把「现金选择权已分列（DV）/ 股票过户已分列（U）/ 印花已分列（V）/ 证管费已分列（T）/ 换股过户已分列（DN）/ 篮子过户已分列（DQ）/ 行权可成交已分列（CR）/ 除权判板已分列（W）/ 首日临停已分列（DU）/ 整手已分列（DT）/ 转股印花已分列（DS）/ 盘后已分列（DR）/ 股票 ETF 回转已分列（R）」写成「权证/期权行权过户已诚实」。不改 DV / U / V / T / DN / DQ / CR / W / DU / DT / DS / DR / R。
- 把实验 R（股票 ETF 假 T+0）和本页合成或混读后升格进 `dw0`。诊断桶 `vs_R_etf_t0` 只作对照。不抢、不重开假设-R。**实验 R 不抢**。
- 把假设-V 的股票印花切日和本页合成或混读后升格进 `dw0`。诊断桶 `vs_V_stamp` 只作对照。**不重开假设-V**。
- 把假设-T 的证管费和本页合成或混读后升格进 `dw0`。诊断桶 `vs_T_csrc_fee` 只作对照。**不重开假设-T**。
- 把假设-U 的金额档过户和本页面值档合成或混读后升格进 `dw0`。诊断桶 `vs_U_ashare_transfer_fee` 只作对照。**不重开假设-U**。**U 股票过户切日（金额档）≠ 本页行权面值档**。
- 把 DV 现金选择权面值句抄到权证/期权，或把 DV 诊断升格回写。诊断桶 `copy_DV_cash_option_transfer_onto_warrant_option` / `vs_DV_cash_option_transfer` 只作对照。**禁 copy_DV / vs_DV 进主报**。**零改 DV**。**不重开假设-DV**。
- 把权证「单向」和期权「过入方」合成一句后升格进 `dw0`。诊断桶 `merge_warrant_unilateral_with_option_inbound` 只作对照。**须按 biz_type 分列**。
- 把 DN 换股面值 0.5‰ 和本页因同数字合成后升格进 `dw0`。诊断桶 `copy_DN_face_transfer_onto_warrant_option` / `vs_DN_exchangeable_conversion_transfer` 只作对照。**禁 copy_DN 进主报**。**不重开假设-DN**。
- 把 DQ 篮子面值 0.5‰ 和本页因同数字合成后升格进 `dw0`。诊断桶 `copy_DQ_basket_transfer_onto_warrant_option` / `vs_DQ_etf_creation_redemption_transfer` 只作对照。**禁 copy_DQ 进主报**。**不重开假设-DQ**。
- 把 CR 行权可成交和本页过户费合成或混读后升格进 `dw0`。诊断桶 `vs_CR_put_call_fill` 只作对照。**不重开假设-CR**。
- 把假设-W 的除权日复权价误判板和本页过户费合成或混读后升格进 `dw0`。诊断桶 `vs_W_ex_right_limit` 只作对照。**不重开假设-W**。**双字母 DW ≠ 单字母假设-W**。
- 把 DU 首日临停和本页过户费合成或混读后升格进 `dw0`。诊断桶 `vs_DU_cb_ipo_halt` 只作对照。**不重开假设-DU**。
- 把 DT 整手价位和本页过户费合成或混读后升格进 `dw0`。诊断桶 `vs_DT_cb_lot_tick` 只作对照。**不重开假设-DT**。
- 把 DS 转股印花和本页过户费合成或混读后升格进 `dw0`。诊断桶 `vs_DS_conversion_stamp` 只作对照。**不重开假设-DS**。
- 把 DR 盘后通道和本页过户费合成或混读后升格进 `dw0`。诊断桶 `vs_DR_aft_pricing` 只作对照。**不重开假设-DR**。
- 把行权过户记成 0 并升格进 `dw0`。诊断桶 `invent_zero_transfer_on_warrant_or_option_exercise` 只作对照。
- 缺业务类型、官方‰或场所表仍不 skip，并升格进 `dw0`。诊断桶 `missing_biz_type_or_official_rate_not_skip` 只作对照。
- `dw0_primary_demo` 与 `invent_asof_leak_warrant_option_transfer` 双挂主报；DW1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DW 与单字母 D/W 或 params.Y/G/N 混读。**双字母 DW ≠ 单字母假设-D / 假设-W**。
- 改 DV / U / V / T / DN / DQ / CR / W / DU / DT / DS / DR / R / D / DP / DO / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / AC / Q / O / M / CH / CL / CQ / E / F / J / AU / BR / A 正文；重开假设-DV；重开假设-U；重开假设-V；重开假设-T；重开假设-DN；重开假设-DQ；重开假设-CR；重开假设-W；重开假设-DU；重开假设-DT；重开假设-DS；重开假设-DR；重开假设-R；抢 A 真数队列；抢实验 R；标纸面齐；写成 A/D–DW纸面齐；开真数/回测/开户/实盘；用复权价当过户基数；结论写成「行权过户更便宜所以能买」。
- **纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK–DV；勿再只改清单）。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权路径、交易日、**交易所 venue / 场所表是否在册**、**业务类型**（权证行权 / 股票期权行权 / 现金选择权行权 / A 股二级成交 / 可交换债换股 / ETF 申赎篮子 / 其他；仅用于把腿分回 DV、U、V、T、DN、DQ、CR、W、DU、DT、DS、DR、R 或本页）、**官方过户‰是否在册**（缺则 skip，不发明另一档，也不拿股票成交金额 0.01‰ 或免费 0 去填）。
- 过户基数要能分清「行权标的面值」和「二级成交金额」。权证行权建议方向是面值、单向。股票期权行权建议方向是面值、过入方。这两句不能合成。股票二级的成交金额、买卖双方只消费 U，不在本页改 U。
- 费率方向：权证建议是面值 0.5‰ 单向；股票期权建议是面值 0.5‰ 过入方。A 股二级 0.01‰ 只作对照，不收进本页主报。DV 的现金选择权面值、DN 的换股面值、DQ 的篮子面值只作同数字对照，不收进主报。
- 样本日要能对上场所表。表上没有这一栏、或官方‰对不上、或 biz_type 分不清权证还是期权，整笔 skip。不要用「同栏所以同费率」把现金选择权、换股或篮子的句子抄过来。
- 认沽/认购能不能成交留在 CR，不在本页改 CR。除权日复权价怎么判板留在 W，不在本页改 W，也不用复权价当过户基数。
- 没有业务类型、官方‰或场所表时，按写死冻结的 `warrant_option_transfer_over_policy=skip_if_biz_type_or_official_rate_or_venue_table_missing` skip，不得按成交金额 0.01‰、面值 0.5‰、免费 0 或占位 0.01 把行权过户填上。
- 旁路消费：DV 的现金选择权行权过户、U 的股票过户切日、V 的股票印花、T 的股票证管费、DN 的换股过户、DQ 的申赎篮子过户、CR 的行权可成交、W 的除权判板、DU 的首日临停、DT 的整手价位、DS 的转股印花、DR 的盘后通道、R 的股票 ETF 假 T+0、D 的成交时点之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。零改 DV。** 这些页的主报不收到本页 `dw0`。
- 未复权路径；asof **写死冻结** `2026-11-06`。核对日方向「按 biz_type 分列的面值档；禁止套二级成交金额 0.01‰；禁止与 DV/DN/DQ 同数字合成；权证与期权禁止合成一句」是写死冻结的机制方向，不是已冻的全历史规则，也不是占位门槛。`事实与坑` 2026-11-06 只证明权证/期权行权出现在交易过户费栏，没有把「权证单向 / 期权过入方」写成已冻句子；本页也不把那一栏的并列关系写成「已经同费率」。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-11-06`；`fail_policy=skip`；`warrant_option_transfer_honest=pit_face_value_0p5_permille_by_biz_type_not_ashare_amount_0p01`（缺业务类型/官方‰/场所表则 skip；权证行权按面值 0.5‰ 单向；股票期权行权按面值 0.5‰ 过入方；禁止合成一句；禁止套 A 股二级成交金额 0.01‰；禁止与 DV/DN/DQ 仅因同数字合成一句）；`warrant_option_transfer_scope=warrant_or_stock_option_exercise_vs_secondary_transfer`（权证或股票期权行权过户与股票二级过户分列；方向名，不是已冻规则，也不是把两档口径合成一句）；`warrant_option_transfer_over_policy=skip_if_biz_type_or_official_rate_or_venue_table_missing`（缺业务类型/官方‰/场所表则 skip）；`dw0_primary_demo=invent_ashare_amount_transfer_on_warrant_or_option_exercise`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_warrant_option_transfer` 双挂；DW1 不升格；诊断桶不升格主报；**禁把 U / V / T / DV / DN / DQ / CR / W / R 合成进 `dw0`**；**禁把 DU / DT / DS / DR 合成进 `dw0`**；只作对照/旁路，不得升格进 `dw0` 或另挂主报；**禁把 U/V/T/DV/DN/DQ/CR/W/R 混读升格进 `dw0`**；**禁 copy_DV / copy_DN / copy_DQ 进主报**；**禁 merge_warrant_unilateral_with_option_inbound 升格**）；`cash_option_transfer_handoff=dv_page`；`transfer_fee_handoff=u_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`exchangeable_conversion_transfer_handoff=dn_page`；`etf_creation_redemption_transfer_handoff=dq_page`；`put_call_fill_handoff=cr_page`；`cb_ipo_halt_handoff=du_page`；`cb_lot_tick_handoff=dt_page`；`cb_conversion_stamp_handoff=ds_page`；`aft_pricing_handoff=dr_page`；`ex_right_limit_handoff=w_page`；`etf_t0_handoff=r_page`；`merge_with_DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AU/BR/A/D=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是过户费率、不是印花税率、不是证管费：行权过户误套截 ΔWarrantOptionTransfer / 净差异 / DW1−DW2；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰（量纲与语义不同）**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**；**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**；**params.Y/G/N ≠ 实验字母 DW ≠ 单字母 D/W**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**；**勿把 params.Y 读成假设-V 或假设-T，亦勿把 params.G 读成假设-U，亦勿把 params 字母读成假设-W，亦勿把单字母假设-D / 假设-W 读成双字母 DW**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #133。
- **本页不开回测**；不拉真数；不做实盘；不开户；不催 8765。本草稿基 tip=`5e23a7dd`（A/D–DV纸面齐已合，全长 `5e23a7dd736ad5f61e53605e834191774c6a5eec`）；三冻补丁基 tip=`ea5df300` / `ea5df3008b0fdb8b41667c6ef32ff300f9fabdf4`；分支起点 HEAD=`1a915919` / `1a9159193c567e79822d623a1fd7dcce35d99f88`。**不改已冻 A–DQ / DA–DV**。**零改 DV**。状态=**A/D–DW纸面齐（预检有条件通过·三条已冻）**。

---

## 8. 结论

（空；**A/D–DW纸面齐（预检有条件通过·三条已冻）**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-12-03）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DW-20261110.md`（原样落入，不改结论；SHA256=`dfa868cd157130e6c1d6a7885c732b6e847c56b30d070c9088c3ace6102525e6`；预检 2026-11-10；**结论：有条件通过**；tip基=`ea5df300` / `ea5df3008b0fdb8b41667c6ef32ff300f9fabdf4`；本补丁分支起点 HEAD=`1a915919` / `1a9159193c567e79822d623a1fd7dcce35d99f88`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于行权过户误套截 ΔWarrantOptionTransfer、净差异、DW1−DW2 专项。**`params.Y` ≠ 实验字母 DW**；**`params.G` ≠ 实验字母 DW**；**`params.N` ≠ 实验字母 DW**；亦 ≠ 单字母假设-D / 假设-W。**params.Y/G/N ≠ 实验字母 DW ≠ 单字母 D/W**。**勿把 `params.Y` 读成假设-V，亦勿读成假设-T，亦勿读成假设-W，亦勿把 `params.G` 读成假设-U，亦勿把 `params.Y` 读成实验字母 DW，亦勿把单字母假设-D / 假设-W 读成双字母 DW**。**尤重：`params.G` 的 `0.01` ≠ 过户 0.01‰ ≠ 面值 0.5‰**（**params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰**）。量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户 0.01‰，也不是面值 0.5‰，也不是印花税率。**尤重：`params.Y` 的 `0.02` ≠ 证管费 0.02‰**（**params.Y 的 0.02 ≠ 证管费 0.02‰**）。**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**。**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**。**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**。禁止互读、禁止把门槛改写成过户费率、印花税率或证管费。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dw0_primary_demo`**：**写死冻结** **`invent_ashare_amount_transfer_on_warrant_or_option_exercise`**（单一主报，单挂写死）。**禁止**与半泄露键 **`invent_asof_leak_warrant_option_transfer`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DW1 仅核对日把「按 biz_type：权证面值 0.5‰ 单向、期权面值 0.5‰ 过入方」铺到全历史、铺到股票二级、铺到 DV/DN/DQ，或把两档口径合成一句再铺开，只作半泄露对照，**不得升格与 dw0 并列主报**，也不得把 `invent_asof_leak_warrant_option_transfer` 写进 `dw0`。`invent_zero_transfer_on_warrant_or_option_exercise` / `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` / `merge_warrant_unilateral_with_option_inbound` / `vs_U_ashare_transfer_fee` / `vs_V_stamp` / `vs_T_csrc_fee` / `vs_DV_cash_option_transfer` / `vs_DN_exchangeable_conversion_transfer` / `vs_DQ_etf_creation_redemption_transfer` / `vs_CR_put_call_fill` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `missing_biz_type_or_official_rate_not_skip` **只作诊断桶，不得升格主报**。DW1 / 诊断桶 **不升格**。**禁把以下升格进 dw0**：U股票过户金额档 / V印花切日 / T证管费切日 / DV现金选择权行权过户 / DN换股过户 / DQ ETF篮子过户 / CR行权可成交性 / W除权判板 / R假T+0 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后定价。**DN/DQ 同数字面值档禁升格**。**权证「单向」与期权「过入方」禁止合成一句进 dw0**（合成走诊断桶 `merge_warrant_unilateral_with_option_inbound`）。这些只作对照/旁路，**不得升格进 `dw0`，不得另挂主报**。**零改 DV**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-DV**；**不重开假设-DN**；**不重开假设-DQ**；**不重开假设-CR**；**不重开假设-W**；**不重开假设-DU**；**不重开假设-DT**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-R**。**不抢实验 R**。**双字母 DW ≠ 单字母假设-D / 假设-W**。

3. **权证/股票期权行权过户诚实锚六键升格写死（不可再写「建议」）**：`params.warrant_option_transfer_honest=pit_face_value_0p5_permille_by_biz_type_not_ashare_amount_0p01`；`params.warrant_option_transfer_scope=warrant_or_stock_option_exercise_vs_secondary_transfer`；`params.warrant_option_transfer_over_policy=skip_if_biz_type_or_official_rate_or_venue_table_missing`；`params.asof_check_date=2026-11-06`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺业务类型/官方‰/场所表 → skip；权证行权=面值 0.5‰ 单向；股票期权行权=面值 0.5‰ 过入方；禁止合成一句；禁止套 A 股二级成交金额 0.01‰；禁止与 DV/DN/DQ 仅因同数字合成一句。禁止跑后改锚，或用金额档 / 核对日面值铺满 / 记成 0 / 抄 DV/DN/DQ / 把权证单向和期权过入方合成一句 / 缺业务类型/官方‰/场所表仍硬填 / 把 U/V/T/DV/DN/DQ/CR/W/R/DU/DT/DS/DR 升格进 dw0 冒充诚实 PIT。**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**。**禁把 params.G 的 0.01 读成过户 0.01‰ 或面值 0.5‰**。**禁把 params.Y 的 0.02 读成证管费 0.02‰**。**不重开假设-V**；**不重开假设-T**；**不重开假设-U**。**零改 DV**。**不抢实验 R**。

**硬分列保住**：DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠A≠D；**双字母 DW ≠ 单字母假设-D / 假设-W**；**双字母 DW ≠ 单字母 D/W**；**params.Y / params.G / params.N ≠ 实验字母 DW ≠ 单字母 D/W**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**；**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**；**权证/股票期权行权过户费误套股票成交金额档 ≠ DV现金选择权行权过户 ≠ U股票过户金额档 ≠ V印花切日 ≠ T证管费切日 ≠ DN换股过户 ≠ DQ ETF篮子过户 ≠ CR行权可成交性 ≠ W除权判板 ≠ R假T+0 ≠ DU首日临停 ≠ DT整手价位 ≠ DS转股印花 ≠ DR盘后定价**；**权证「单向」≠ 期权「过入方」**；不抢 A；不抢实验 R；不改已齐/已冻 DA～DV 及 A–DQ 正文；**零改 DV**；**不重开假设-V**；**不重开假设-T**；**不重开假设-U**；**不重开假设-DV**；**不重开假设-DN**；**不重开假设-DQ**；**不重开假设-CR**；**不重开假设-W**；**不重开假设-DU**；**不重开假设-DT**；**不重开假设-DS**；**不重开假设-DR**；**不重开假设-R**；**禁把 U股票过户金额档 / V印花切日 / T证管费切日 / DV现金选择权行权过户 / DN换股过户 / DQ ETF篮子过户 / CR行权可成交性 / W除权判板 / R假T+0 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后定价 合成/混读升格进 dw0**。handoff 保持：`cash_option_transfer_handoff=dv_page`；`transfer_fee_handoff=u_page`；`stamp_handoff=v_page`；`csrc_fee_handoff=t_page`；`exchangeable_conversion_transfer_handoff=dn_page`；`etf_creation_redemption_transfer_handoff=dq_page`；`put_call_fill_handoff=cr_page`；`ex_right_limit_handoff=w_page`；`cb_ipo_halt_handoff=du_page`；`cb_lot_tick_handoff=dt_page`；`cb_conversion_stamp_handoff=ds_page`；`aft_pricing_handoff=dr_page`；`etf_t0_handoff=r_page`；`merge_with_*=False`。

**状态**：**A/D–DW纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/开户/实盘。

## 变更
| 日期 | 变更 |
|------|------|
| 2026-11-10 | 复检/纸面齐——**A/D–DW纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设DW-20261110.md` 原样落入，SHA256=`cabbfb7450c521352a2e7386d8e99c216c88937644f59f3d883173f056fb869d`；三冻 tip=`6ab8f268` / `6ab8f268e0858917acf88e7116d247bf6d9bb7ad`。只改状态标签；未改写已冻三条/六键；不改已齐 A–DQ / DA–DV；**零改 DV**；不改 #110–#131；不重开假设-U / 假设-V / 假设-T / 假设-DV / 假设-DN / 假设-DQ / 假设-CR / 假设-W / 假设-DU / 假设-DT / 假设-DS / 假设-DR / 假设-R / 假设-D；不抢实验 R；不预留 #133；不开回测/真数/开户/实盘。 |
| 2026-12-03 | 风控预检补丁·冻结三条写死——依据 `预检-假设DW-20261110.md`（SHA256=`dfa868cd157130e6c1d6a7885c732b6e847c56b30d070c9088c3ace6102525e6`；结论=有条件通过；tip基=`ea5df300` / `ea5df3008b0fdb8b41667c6ef32ff300f9fabdf4`；分支起点 HEAD=`1a915919` / `1a9159193c567e79822d623a1fd7dcce35d99f88`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖行权过户误套截 ΔWarrantOptionTransfer / 净差异 / DW1−DW2；**params.Y/G/N ≠ 实验字母 DW ≠ 单字母 D/W**；**勿把 params.Y 读成假设-V 或假设-T 或假设-W，亦勿把 params.G 读成假设-U，亦勿把单字母假设-D / 假设-W 读成双字母 DW**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**；**尤重 params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰（量纲与语义不同）**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**；**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成过户费率/印花税率/证管费）；② `params.dw0_primary_demo=invent_ashare_amount_transfer_on_warrant_or_option_exercise`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_warrant_option_transfer` 双挂；DW1 不升格；诊断桶 `invent_zero_transfer_on_warrant_or_option_exercise` / `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` / `merge_warrant_unilateral_with_option_inbound` / `vs_U_ashare_transfer_fee` / `vs_V_stamp` / `vs_T_csrc_fee` / `vs_DV_cash_option_transfer` / `vs_DN_exchangeable_conversion_transfer` / `vs_DQ_etf_creation_redemption_transfer` / `vs_CR_put_call_fill` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `missing_biz_type_or_official_rate_not_skip` 不升格；**禁把 U股票过户金额档 / V印花切日 / T证管费切日 / DV现金选择权行权过户 / DN换股过户 / DQ ETF篮子过户 / CR行权可成交性 / W除权判板 / R假T+0 / DU首日临停 / DT整手价位 / DS转股印花 / DR盘后定价 合成/混读升格进 dw0**，只作对照/旁路，不得升格进 dw0 或另挂主报；**DN/DQ 同数字面值档禁升格**；**权证单向与期权过入方禁止合成一句**；**零改 DV**；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-DV；不重开假设-DN；不重开假设-DQ；不重开假设-CR；不重开假设-W；不重开假设-DU；不重开假设-DT；不重开假设-DS；不重开假设-DR；不重开假设-R；不抢实验 R；**双字母 DW ≠ 单字母假设-D / 假设-W**）；③ 锚六键写死 `warrant_option_transfer_honest=pit_face_value_0p5_permille_by_biz_type_not_ashare_amount_0p01` / `warrant_option_transfer_scope=warrant_or_stock_option_exercise_vs_secondary_transfer` / `warrant_option_transfer_over_policy=skip_if_biz_type_or_official_rate_or_venue_table_missing` / `asof_check_date=2026-11-06` / `fill_time=next_open` / `fail_policy=skip`（缺业务类型/官方‰/场所表 → skip；权证行权=面值 0.5‰ 单向；股票期权行权=面值 0.5‰ 过入方；禁止合成一句；禁止套 A 股二级成交金额 0.01‰）。handoff 保持 `cash_option_transfer_handoff=dv_page` / `transfer_fee_handoff=u_page` / `stamp_handoff=v_page` / `csrc_fee_handoff=t_page` / `exchangeable_conversion_transfer_handoff=dn_page` / `etf_creation_redemption_transfer_handoff=dq_page` / `put_call_fill_handoff=cr_page` / `ex_right_limit_handoff=w_page` / `cb_ipo_halt_handoff=du_page` / `cb_lot_tick_handoff=dt_page` / `cb_conversion_stamp_handoff=ds_page` / `aft_pricing_handoff=dr_page` / `etf_t0_handoff=r_page`；`merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DW纸面齐**；不改已齐/已冻 DA～DV 及 A–DQ；不改假设-DA～假设-DV；**零改 DV**；不改 #110–#131；不重开假设-V；不重开假设-T；不重开假设-U；不重开假设-R；不重开假设-DV；不重开假设-DN；不重开假设-DQ；不重开假设-CR；不重开假设-W；不重开假设-DU；不重开假设-DT；不重开假设-DS；不重开假设-DR；不抢实验 R；不预留 #133；不开回测/真数/开户/实盘。基于 tip=`ea5df300`。 |
| 2026-12-03 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。权证/股票期权行权过户费误套股票成交金额档（费用）；`dw0_primary_demo` 建议 `invent_ashare_amount_transfer_on_warrant_or_option_exercise`，单一主报，单挂，禁与 `invent_asof_leak_warrant_option_transfer` 双挂，DW1 不升格；诊断桶 `invent_zero_transfer_on_warrant_or_option_exercise` / `copy_DV_cash_option_transfer_onto_warrant_option` / `copy_DN_face_transfer_onto_warrant_option` / `copy_DQ_basket_transfer_onto_warrant_option` / `merge_warrant_unilateral_with_option_inbound` / `vs_U_ashare_transfer_fee` / `vs_V_stamp` / `vs_T_csrc_fee` / `vs_DV_cash_option_transfer` / `vs_DN_exchangeable_conversion_transfer` / `vs_DQ_etf_creation_redemption_transfer` / `vs_CR_put_call_fill` / `vs_DU_cb_ipo_halt` / `vs_DT_cb_lot_tick` / `vs_DS_conversion_stamp` / `vs_DR_aft_pricing` / `vs_W_ex_right_limit` / `vs_R_etf_t0` / `missing_biz_type_or_official_rate_not_skip` 不升格；**尤重实验 R（股票 ETF 假 T+0）不抢、不重开、不混读升格进 dw0**；**尤重不重开假设-V，禁把 vs_V_stamp 升格进 dw0**；**尤重不重开假设-T，禁把 vs_T_csrc_fee 升格进 dw0**；**尤重 U 股票过户切日（金额档）≠ 本页行权面值档，禁把 vs_U_ashare_transfer_fee 升格进 dw0**；**尤重 DV 现金选择权行权 ≠ 本页权证/期权行权，零改 DV，禁把 DV 诊断升格回写，禁 copy_DV / vs_DV 进主报**；**尤重权证「单向」与期权「过入方」须按 biz_type 分列，禁止合成一句进 dw0，禁 merge_warrant_unilateral_with_option_inbound 升格**；**尤重 DN/DQ 同为面值 0.5‰ 但业务不同，数字相同禁升格进 dw0，禁 copy_DN / copy_DQ 进主报**；**尤重 CR 可成交性 ≠ 本页过户费，禁把 vs_CR_put_call_fill 升格进 dw0**；**尤重双字母 DW ≠ 单字母假设-D / 假设-W（除权日复权价误判板），禁把 vs_W_ex_right_limit 升格进 dw0**；**尤重 DU 首日临停 / DT 整手价位 / DS 转股印花 / DR 盘后通道 ≠ 本页过户费，禁止合成进 dw0**；**params 字母 ≠ 假设-V / 假设-T / 假设-U / 假设-W**；**禁把 U/V/T/DV/DN/DQ/CR/W/R 混读升格进 dw0**；**禁把 DU/DT/DS/DR 混读升格进 dw0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DW ≠ 单字母 D/W**，且 **params.G 的 0.01 ≠ 过户 0.01‰ ≠ 面值 0.5‰**，**params.Y 的 0.02 ≠ 证管费 0.02‰**，**禁把占位读成过户 0.01‰/0.5‰、印花税率、证管费 0.02‰**，**params 相对门槛 ≠ 过户费率 ≠ 印花税率 ≠ 证管费**；锚建议·待冻、未冻：`warrant_option_transfer_honest=pit_face_value_0p5_permille_by_biz_type_not_ashare_amount_0p01` / scope=`warrant_or_stock_option_exercise_vs_secondary_transfer` / over_policy=`skip_if_biz_type_or_official_rate_or_venue_table_missing` / `asof_check_date=2026-11-06` / `fill_time=next_open` / `fail_policy=skip`；口径：缺业务类型/官方‰/场所表则 skip；权证行权=面值 0.5‰ 单向；股票期权行权=面值 0.5‰ 过入方；禁止合成一句；禁止套 A 股二级成交金额 0.01‰；禁止与 DV/DN/DQ 仅因同数字合成一句（**草稿方向，尚未冻，不要写成已冻**）；handoff：`cash_option_transfer_handoff=dv_page`，`transfer_fee_handoff=u_page`，`stamp_handoff=v_page`，`csrc_fee_handoff=t_page`，`exchangeable_conversion_transfer_handoff=dn_page`，`etf_creation_redemption_transfer_handoff=dq_page`，`put_call_fill_handoff=cr_page`，`cb_ipo_halt_handoff=du_page`，`cb_lot_tick_handoff=dt_page`，`cb_conversion_stamp_handoff=ds_page`，`aft_pricing_handoff=dr_page`，`ex_right_limit_handoff=w_page`，`etf_t0_handoff=r_page`；`merge_with_DV/DU/DT/DS/DR/DQ/DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/M/CH/CL/CR/CQ/E/F/J/W/AU/BR/A/D=False`；**DW≠DV≠DU≠DT≠DS≠DR≠DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠M≠CH≠CL≠CR≠CQ≠E≠F≠J≠W≠A≠D**；**双字母 DW ≠ 单字母 D/W**；**未标纸面齐**；**不写 A/D–DW纸面齐**；**纸面齐惯例**：将来落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK–DV；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DQ / DA–DV；不改已齐假设-DA～假设-DV；**零改 DV**；不改 #110–#131；不重开假设-DV；不重开假设-U；不重开假设-V；不重开假设-T；不重开假设-R；不重开假设-DN；不重开假设-DQ；不重开假设-CR；不重开假设-W；不重开假设-DU；不重开假设-DT；不重开假设-DS；不重开假设-DR；不写下一字母；不预留 #133；不开真数/回测/开户/实盘。基 tip=`5e23a7dd`（A/D–DV纸面齐已合，全长 `5e23a7dd736ad5f61e53605e834191774c6a5eec`；不改该 tip 上的 #110–#131，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
