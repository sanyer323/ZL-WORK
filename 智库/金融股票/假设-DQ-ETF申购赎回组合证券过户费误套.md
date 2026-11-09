# 假设-DQ · ETF申购赎回组合证券过户费误套（成本诚信）

更新：2026-11-23  
来源：总管线 / 基 tip=`08d5dfd0` / 全长 `08d5dfd0de59ddfa5d409713bb7b3d58e8469068`（A/D–DP纸面齐已合）；**不改已冻 A–DP / DA–DO**；**不改假设-DP 正文**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-S / 假设-AX / 假设-T / 假设-U / 假设-V / 假设-AC / 假设-Q / 假设-R / 假设-A / 假设-D / 假设-O / 假设-P / 假设-N 及其他已存在假设页；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DO**；**不重开假设-DP**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**；**不重开假设-AX**；**不重开假设-Q**）后写下一草稿 DQ；清单 #125=DP，本页占用 **#126=DQ**；选题是回测把 ETF **申购赎回组合证券过户**误套成股票过户成交金额 0.01‰、发明免费 0、忽略成立后暂减半、沪深合成一句、因同是 0.5‰ 抄 DN 换股面值、或把篮子费铺到二级腿；假设-DA 只收场内基金**二级**过户误套（二级成交 ≠ 申赎一级篮子），假设-DN 只收可交换债**换股**过户面值 0.5‰（换股 ≠ 申赎；数字相同禁止升格混读），假设-U 只收股票过户切日，假设-AX 只收基金经手费，假设-DP 只收可交换债换股印花税；**新建实验 DQ**；不写下一字母；不预留 #127  
状态：**A/D–DQ纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「按二级 0.01‰ 抽篮子、或发明免费 0、或把篮子费铺到二级腿」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改已冻 A–DP / DA–DO**；尤其不改假设-DA / 假设-DN / 假设-U / 假设-AX / 假设-DP / 假设-Q / 假设-DO / 假设-T / 假设-AC / 假设-R / 假设-O / 假设-DI / 假设-DF / 假设-DB / 假设-S / 假设-DD / 假设-D；**不重开假设-T**；**不重开假设-U**；**不重开假设-DA**；**不重开假设-DN**；**不重开假设-AX**；**不重开假设-DP**；**不重开假设-Q**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DO**；**不重开假设-DC**；**不重开假设-DK**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DQ（#126）。一句话误开：回测把 ETF申购赎回组合证券过户误套成股票过户 0.01‰、发明免费 0、忽略成立后暂减半、沪深合成、因同数字抄 DN 换股面值 0.5‰、或把篮子费铺到二级腿，或与 DA二级过户 / DN换股过户 / U股票过户 / AX基金经手 / DP换股印花 混读，或缺 venue/业务类型/官方‰仍不 skip，系统性改写申赎篮子过户成本。**禁与 DA/DN/U/AX/DP 混读**。

> **字母消歧（硬）**：本页**实验字母 DQ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DQ**；**勿把 `params.Y` 读成实验字母 DQ**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DQ**；**尤重：`params.G` 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是股票过户费率，也不是申赎篮子面值费率；0.01‰ 若被消费，只走 U 的股票过户切片或 DA 的二级旁路，不是本页门槛；0.5‰ / 0.25‰ 若出现，只是事实与坑里的篮子面值方向或 DN 的换股面值，不是本页门槛，也不是免费 0；**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DQ**；**params.N ≠ 单字母假设-N**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DQ ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 Q**（可转债按股票规则回放；**双字母 DQ ≠ 单字母假设-Q；严禁复用假设-Q**；组名 DQ0/DQ1/DQ2 是本页三组对照，≠ 单字母实验 Q）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DQ ≠ 单字母假设-A**）≠ 双字母 **DP**（可交换债换股印花税误漏）≠ **DO**（可转债回售经手费暂免误忽略）≠ **DN**（可交换债换股过户费误套）≠ **DM**（可交换债换股经手费误套现货）≠ **DL**（股票综合协议过户费下浮）≠ **DK**（场内基金印花税误抽）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债现货经手费沪深合成）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债现货印花税误抽）≠ **DB**（可转债现货经手费）≠ **DA**（场内基金二级过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费）≠ **T**（股票证管费）≠ **U**（股票过户费）≠ **V**（股票印花税切日）≠ **AC**（北交所涨跌幅与盘后）≠ **R**（股票 ETF 回转）≠ **O**（大宗假流动性）。**DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D**。**双字母 DQ ≠ 单字母 D/Q**。**params.Y/G/N ≠ 实验字母 DQ；亦 ≠ 单字母 D/Q**。**勿把 `params.G` 读成实验字母 DQ，亦勿把单字母假设-D / 假设-Q 读成双字母 DQ**。**尤重：`params.G` 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**。**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**。**ETF申购赎回组合证券过户误套 ≠ DA场内基金二级过户 ≠ DN可交换换股过户 ≠ U股票过户切日 ≠ AX基金经手费 ≠ DP换股印花**。**尤重：DA 场内基金二级过户误套 ≠ 本页 ETF 申赎组合证券过户（二级成交≠申赎一级篮子）——禁止合成/混读升格进 `dq0`**。**尤重：DN 可交换换股过户面值 0.5‰ ≠ 本页 ETF 篮子面值档（换股≠申赎；数字相同禁止升格混读）——禁止合成/混读升格进 `dq0`**。**尤重：U 股票过户切日 ≠ 本页申赎篮子另档——不重开假设-U、禁升格进 `dq0`**。**尤重：AX 基金经手费 ≠ 本页过户费——禁止合成/混读升格进 `dq0`**。**尤重：DP 换股印花 ≠ 本页申赎过户——禁止合成/混读升格进 `dq0`**。**尤重：双字母 DQ ≠ 单字母假设-Q**。

### 专节 · 双字母 DQ ≠ 单字母假设-D / 假设-Q；且 ≠ 假设-DA / 假设-DN / 假设-U / 假设-AX / 假设-DP（硬）

| 维度 | 对照页 | 本页假设-DQ（双字母） |
|------|--------|----------------------|
| 题面 DA | **场内基金二级过户费误套**（二级不成交金额 0.01‰ 栏；二级成交 ≠ 申赎一级篮子） | 二级过户误套 ≠ 本页 ETF 申赎组合证券过户。**二级成交≠申赎一级篮子**。二级腿只消费 DA，篮子费禁止铺到二级。**DQ≠DA**；**严禁复用假设-DA**；**不重开假设-DA**；**不改 DA**；**尤重：DA 场内基金二级过户误套 ≠ 本页 ETF 申赎组合证券过户（二级成交≠申赎一级篮子）——禁止合成/混读升格进 `dq0`**；`fund_secondary_transfer_handoff=da_page`；诊断桶 `vs_DA_fund_secondary_transfer` / `apply_basket_fee_onto_secondary` / `copy_ashare_001_onto_etf_basket` 不升格 |
| 题面 DN | **可交换债换股过户费**（深市换股按股票过户面值 0.5‰；换股 ≠ 申赎） | 换股面值 0.5‰ ≠ 本页 ETF 篮子面值档。**换股≠申赎；数字相同禁止升格混读**。**DQ≠DN**；**严禁复用假设-DN**；**不重开假设-DN**；**不改 DN**；**尤重：DN 可交换换股过户面值 0.5‰ ≠ 本页 ETF 篮子面值档（换股≠申赎；数字相同禁止升格混读）——禁止合成/混读升格进 `dq0`**；`exch_conversion_transfer_handoff=dn_page`；诊断桶 `vs_DN_exch_conversion_transfer` / `copy_DN_05_face_onto_etf_basket` 不升格 |
| 题面 U | **股票过户费切日**（A 股成交金额 0.01‰；业务类型是股票二级，不是申赎篮子） | 股票过户切日 ≠ 本页申赎篮子另档。**不重开假设-U**。**DQ≠U**；**严禁复用假设-U**；**不改 U**；**尤重：U 股票过户切日 ≠ 本页申赎篮子另档——不重开假设-U、禁升格进 `dq0`**；`ashare_transfer_handoff=u_page`；诊断桶 `vs_U_ashare_transfer` / `copy_ashare_001_onto_etf_basket` 不升格 |
| 题面 AX | **基金/ETF 经手费档**（经手 ≠ 过户） | 基金经手费 ≠ 本页过户费。**DQ≠AX**；**严禁复用假设-AX**；**不重开假设-AX**；**不改 AX**；**尤重：AX 基金经手费 ≠ 本页过户费——禁止合成/混读升格进 `dq0`**；`fund_handling_handoff=ax_page`；诊断桶 `vs_AX_fund_handling` 不升格 |
| 题面 DP | **可交换债换股印花税误漏**（印花 ≠ 过户） | 换股印花 ≠ 本页申赎过户。**DQ≠DP**；**严禁复用假设-DP**；**不重开假设-DP**；**不改 DP**；**尤重：DP 换股印花 ≠ 本页申赎过户——禁止合成/混读升格进 `dq0`**；`exch_conversion_stamp_handoff=dp_page`；诊断桶 `vs_DP_exch_conversion_stamp` 不升格 |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 本机制。回转/涨跌幅 ≠ 申赎篮子过户。**双字母 DQ ≠ 单字母假设-Q**；**严禁复用假设-Q**；**DQ≠Q**；**不重开假设-Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 DO | **可转债回售经手费暂免** | 回售经手 ≠ 申赎篮子过户。**DQ≠DO**；**严禁复用假设-DO**；**不重开假设-DO**；**不改 DO**；`cb_put_handling_handoff=do_page` |
| 题面 DM | **可交换债换股经手费** | 换股经手 ≠ 申赎篮子过户。经手≠过户。**DQ≠DM**；**不重开假设-DM**；**不改 DM**；`exch_conversion_handling_handoff=dm_page` |
| 题面 DL | **股票综合协议过户费下浮** | 综合协议过户下浮 ≠ 申赎篮子过户。**DQ≠DL**；**不重开假设-DL**；**不改 DL**；`agreement_transfer_handoff=dl_page` |
| 题面 DK | **场内基金印花税误抽** | 基金印花 ≠ 本机制。**DQ≠DK**；**不改 DK**；`fund_stamp_handoff=dk_page` |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 本机制。**DQ≠DJ**；**不改 DJ**；`fund_csrc_fee_handoff=dj_page` |
| 题面 DI | **股票大宗经手下浮** | 大宗经手下浮 ≠ 申赎篮子过户。**DQ≠DI**；**不重开假设-DI**；**不改 DI**；`stock_block_handling_handoff=di_page` |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 申赎篮子过户。**DQ≠DH**；**不改 DH**；`commission_double_handoff=dh_page` |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 本机制。**DQ≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DF | **可交换债现货经手费沪深合成** | 可交换现货经手 ≠ 申赎篮子过户。**DQ≠DF**；**不重开假设-DF**；**不改 DF**；`exch_spot_handling_handoff=df_page` |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 申赎篮子过户。**DQ≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债现货过户费** | 转债现货过户 ≠ 申赎篮子过户。**DQ≠DD**；**不重开假设-DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DC | **可转债现货印花税误抽** | 转债现货印花 ≠ 申赎篮子过户。**DQ≠DC**；**不改 DC**；`cb_spot_stamp_handoff=dc_page` |
| 题面 DB | **可转债现货经手费** | 转债现货经手 ≠ 申赎篮子过户。**DQ≠DB**；**不重开假设-DB**；**不改 DB**；`cb_handling_fee_handoff=db_page` |
| 题面 S | **沪深 A 股竞价经手费切日** | 股票经手切日 ≠ 申赎篮子过户。**DQ≠S**；**不重开假设-S**；**不改 S**；`ashare_fee_handoff=s_page` |
| 题面 T | **证管费主报股票** | 股票证管费 ≠ 申赎篮子过户。**DQ≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 V | **股票印花税切日** | 股票印花切日 ≠ 申赎篮子过户。**DQ≠V**；**不重开假设-V**；**不改 V**；`ashare_stamp_handoff=v_page` |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 申赎篮子过户。**DQ≠AC**；**不重开假设-AC**；**不改 AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 篮子过户费。**DQ≠R**；**不重开假设-R**；**不改 R**；`stock_etf_rotation_handoff=r_page` |
| 题面 O | **大宗通道 / 假流动性** | 大宗通道 ≠ 申赎篮子过户。**DQ≠O**；**不重开假设-O**；**不改 O**；`block_channel_handoff=o_page` |
| 题面 CM | **ETF 申赎可成交**（能否按净值或现金替代成交） | 申赎能否成交 ≠ 篮子过户费。**不改 CM**；`etf_cr_fill_handoff=cm_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 申赎篮子过户。**DQ≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 篮子过户抽在哪一腿。**双字母 DQ ≠ 单字母假设-D**；**严禁复用假设-D**；**DQ≠D**；**不改 D** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_wrong_transfer_on_etf_creation_redemption`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_etf_creation_redemption_transfer` 双挂；DQ1 不升格；`copy_ashare_001_onto_etf_basket` / `invent_zero_on_etf_basket` / `ignore_post_establishment_half_cut` / `merge_sse_szse_basket_scope` / `copy_DN_05_face_onto_etf_basket` / `apply_basket_fee_onto_secondary` / `vs_DA_fund_secondary_transfer` / `vs_DN_exch_conversion_transfer` / `vs_U_ashare_transfer` / `vs_AX_fund_handling` / `vs_DP_exch_conversion_stamp` / `missing_venue_or_biz_type_not_skip` 只作诊断对照，不升格主报；**尤重禁止把 DA 二级过户、DN 换股面值 0.5‰、U 股票过户切日、AX 基金经手、DP 换股印花合成进 `dq0`**） |
| 文档 | 清单实验 DA / DN / U / AX / DP / DO / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / S / T / V / AC / Q / R / O / A / D（**只读；禁止改写**） | `假设-DQ-ETF申购赎回组合证券过户费误套.md`（新建） |
| 预检键 | 实验字母 DA / DN / U / AX / DP / DO / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / S / T / V / AC / Q / R / O / A / D / Y / G / N | 实验字母 **DQ** / `dq0_primary_demo`；**不得**占用或改写预检 DA/DN/U/AX/DP/DO/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/S/T/V/AC/Q/R/O/A/D/Y/G/N |

**禁止**：把 DQ 写成「DA / DN / U / AX / DP / DO / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / S / T / V / AC / Q / R / O / A / D 的续篇」；把「二级过户已分列（DA）/ 换股过户已分列（DN）/ 股票过户切日已诚实（U）/ 基金经手已诚实（AX）/ 换股印花已分列（DP）」写成「ETF 申赎组合证券过户已诚实」；把实验字母 DQ 与单字母 D/Q 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-Q 读成双字母 DQ**；**尤重勿把 `params.G` 读成实验字母 DQ**；**尤重 `params.G` 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰（量纲与语义不同）**；**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**；**尤重 DA 场内基金二级过户误套 ≠ 本页 ETF 申赎组合证券过户（二级成交≠申赎一级篮子），禁止合成/混读升格进 `dq0`**；**尤重 DN 可交换换股过户面值 0.5‰ ≠ 本页 ETF 篮子面值档（换股≠申赎；数字相同禁止升格混读），禁止合成/混读升格进 `dq0`**；**尤重 U 股票过户切日 ≠ 本页申赎篮子另档，不重开假设-U，禁止合成/混读升格进 `dq0`**；**尤重 AX 基金经手费 ≠ 本页过户费，禁止合成/混读升格进 `dq0`**；**尤重 DP 换股印花 ≠ 本页申赎过户，禁止合成/混读升格进 `dq0`**；**禁与 DA/DN/U/AX/DP 混读**；把 `invent_asof_leak_etf_creation_redemption_transfer` 升格进 `dq0` 或与主报双挂；把诊断桶 `copy_ashare_001_onto_etf_basket` / `invent_zero_on_etf_basket` / `ignore_post_establishment_half_cut` / `merge_sse_szse_basket_scope` / `copy_DN_05_face_onto_etf_basket` / `apply_basket_fee_onto_secondary` / `vs_DA_fund_secondary_transfer` / `vs_DN_exch_conversion_transfer` / `vs_U_ashare_transfer` / `vs_AX_fund_handling` / `vs_DP_exch_conversion_stamp` / `missing_venue_or_biz_type_not_skip` 升格进 `dq0`；按二级成交金额 0.01‰ 抽篮子；发明免费 0；把篮子费铺到二级腿；沪深合成一句。本页主键只用 `dq0` / `dq1` / `dq2` 与 `etf_basket_transfer_*`。不写下一字母。不预留 #127。**纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK/DL/DM/DN/DO/DP；勿再只改清单）。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权篮子面值（基数不是二级成交金额）下，回测把 ETF **申购赎回组合证券过户**误套成股票过户成交金额 0.01‰，或发明免费 0，或忽略成立后暂减半，或把沪深篮子范围合成一句，或因数字同是 0.5‰ 把 DN 换股面值档抄到申赎篮子，或把篮子费铺到二级腿，或与 DA场内基金二级过户 / DN可交换换股过户 / U股票过户切日 / AX基金经手费 / DP换股印花 混读，或缺 venue/业务类型/官方‰仍不 skip，相对「缺 venue/业务类型或官方‰则 skip；申赎篮子按组合证券股票面值档；深市成立后暂减半 0.25‰；沪市成立后暂减半且目前只收所含沪市成分；禁止按二级成交金额 0.01‰ 抽；禁止发明免费 0；禁止把篮子费铺到二级腿；沪深分列禁止合成；二级只消费 DA」的诚实组，会**系统性改写申赎篮子过户成本**——相对诚实锚偏误。

核对日方向（随锚写死；禁止把 0.5‰、0.25‰ 或 0.01‰ 写成全历史唯一费率，也禁止发明免费 0，也禁止把篮子费铺到二级腿，也禁止沪深合成一句）：申赎篮子与二级成交分开，篮子过户与基金经手、换股过户、换股印花、股票过户切日分开。`事实与坑` 2026-11-06 已写：深市组合证券里的股票按过户面值 0.5‰，债券免收；发售阶段用股票认购 ETF 免收，成立后暂减半到 0.25‰。沪市组合证券中股票按过户面值 0.5‰、存托凭证按过户份额 0.5‰；成立后暂按正常标准减半，且目前只收所含沪市成分股票/存托凭证。这是申赎腿，不是二级买卖 ETF 份额。表上没有「ETF 二级成交按 0.01‰」。那些二级「不要套股票 0.01‰」留在 DA，换股面值 0.5‰ 留在 DN，股票过户切日留在 U，基金经手留在 AX，换股印花留在 DP。债券成分免收、发售阶段股票认购免收是表内已写方向，不是缺字段时发明免费 0；缺 venue、业务类型或官方‰仍 skip。**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**。**`params.G` 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**。**禁与 DA/DN/U/AX/DP 混读**。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误套截在标定噪声带内可忽略，且「按二级 0.01‰ 抽篮子 / 发明免费 0 / 忽略成立后暂减半 / 沪深合成 / 抄 DN 面值 0.5‰ / 篮子费铺到二级 / 核对日泄露 / vs DA·DN·U·AX·DP」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dq0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DQ ≠ 单字母假设-D / 假设-Q**；勿把 params.Y 读成实验字母 DQ
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DQ ≠ 单字母 D/Q**
# 【消歧】尤重：params.G 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰（量纲与语义不同：无量纲相对门槛 ≠ 过户费率‰）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成 0.5‰/0.25‰/0.01‰/免费 0（0.01‰ 若出现，只是股票过户或被误套的二级口径，不是本页门槛；0.5‰ / 0.25‰ 是篮子面值方向或 DN 换股面值，不是本页门槛；免费 0 是缺字段时发明的假免费）
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DQ ≠ 单字母假设-N**
# params.Y2                               写死冻结 0.015
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误套截 ΔEtfBasketTransfer / 净收益差 / DQ1−DQ2；**params.Y/G/N ≠ 实验字母 DQ ≠ 单字母假设-D / 假设-Q**；**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**；**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成篮子过户费率或免费 0）
# params.fill_time                        写死冻结 next_open
# params.asof_check_date                  写死冻结 2026-10-16
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.etf_basket_transfer_honest       写死冻结 pit_cs_table_face_value_basket_not_secondary_amount
#   诚实锚方向（已写死冻结；禁止把 0.5‰、0.25‰ 或 0.01‰ 写成全历史唯一费率；禁止发明免费 0）：
#   申赎篮子按组合证券股票面值档，基数不是二级成交金额
#   深市成立后暂减半 0.25‰；沪市成立后暂减半且目前只收所含沪市成分
#   沪深分列，禁止合成一句
#   禁止按二级成交金额 0.01‰ 抽篮子
#   禁止发明免费 0（表内债券免收、发售阶段免收 ≠ 缺字段填 0）
#   禁止把篮子费铺到二级腿；二级只消费 DA
#   禁止把 DN 换股面值 0.5‰ 因数字相同抄到申赎篮子（换股≠申赎）
#   缺 venue、业务类型或官方‰ → skip
#   枚举已写死冻结
#   不把 DA 的二级过户、U 的股票过户切日、AX 的基金经手、DP 的换股印花写成篮子过户诚实锚
# params.etf_basket_transfer_scope        写死冻结 creation_redemption_only_secondary_out_of_scope
#   方向名：只收 ETF 申购/赎回组合证券过户；二级成交不在本页范围
#   这不是把 0.5‰ / 0.25‰ / 0.01‰ 冻成全历史费率，也不是把缺字段冻成免费 0
#   ETF申购赎回组合证券过户 ≠ DA二级过户 ≠ DN换股过户 ≠ U股票过户 ≠ AX基金经手 ≠ DP换股印花
# params.etf_basket_transfer_over_policy  写死冻结 skip_if_venue_or_biz_type_or_official_bps_missing
#   缺 venue、业务类型或官方‰则 skip；禁在缺字段时仍按 0.01‰、免费 0、占位 0.01 或 DN 的 0.5‰ 把篮子腿填上
# params.fund_secondary_transfer_handoff  建议 da_page
#   消费 DA 的场内基金二级过户，或显式旁路；二级成交 ≠ 申赎一级篮子；不重开假设-DA；不改 DA
#   DA 禁止合成/混读升格进 dq0；诊断桶 vs_DA_fund_secondary_transfer / apply_basket_fee_onto_secondary 不得升格进 dq0
# params.exch_conversion_transfer_handoff 建议 dn_page
#   消费 DN 的可交换债换股过户，或显式旁路；换股面值 0.5‰ ≠ 篮子面值档；不重开假设-DN；不改 DN
#   DN 禁止合成/混读升格进 dq0；诊断桶 vs_DN_exch_conversion_transfer / copy_DN_05_face_onto_etf_basket 不得升格进 dq0
# params.ashare_transfer_handoff          建议 u_page
#   消费 U 的股票过户费切日，或显式旁路；股票过户切日 ≠ 申赎篮子另档；不重开假设-U；不改 U
#   U 禁止合成/混读升格进 dq0；诊断桶 vs_U_ashare_transfer / copy_ashare_001_onto_etf_basket 不得升格进 dq0
# params.fund_handling_handoff            建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；经手 ≠ 过户；不重开假设-AX；不改 AX
#   AX 禁止合成/混读升格进 dq0；诊断桶 vs_AX_fund_handling 不得升格进 dq0
# params.exch_conversion_stamp_handoff    建议 dp_page
#   消费 DP 的可交换债换股印花，或显式旁路；印花 ≠ 过户；不重开假设-DP；不改 DP
#   DP 禁止合成/混读升格进 dq0；诊断桶 vs_DP_exch_conversion_stamp 不得升格进 dq0
# params.cb_put_handling_handoff          建议 do_page
#   消费 DO 的可转债回售经手费暂免，或显式旁路；不重开假设-DO；不改 DO
# params.exch_conversion_handling_handoff 建议 dm_page
#   消费 DM 的可交换债换股经手费，或显式旁路；不重开假设-DM；不改 DM
# params.agreement_transfer_handoff       建议 dl_page
#   消费 DL 的股票综合协议过户费下浮，或显式旁路；不重开假设-DL；不改 DL
# params.fund_stamp_handoff               建议 dk_page
#   消费 DK 的场内基金印花税，或显式旁路；不改 DK
# params.fund_csrc_fee_handoff            建议 dj_page
#   消费 DJ 的场内基金证管费，或显式旁路；不改 DJ
# params.stock_block_handling_handoff     建议 di_page
#   消费 DI 的股票大宗经手下浮，或显式旁路；不重开假设-DI；不改 DI
# params.commission_double_handoff        建议 dh_page
#   消费 DH 的佣金双计，或显式旁路；不改 DH
# params.bse_fee_handoff                  建议 dg_page
#   消费 DG 的北交所经手费档，或显式旁路；不改 DG
# params.exch_spot_handling_handoff       建议 df_page
#   消费 DF 的可交换现货经手费沪深分列，或显式旁路；不重开假设-DF；不改 DF
# params.cb_csrc_fee_handoff              建议 de_page
#   消费 DE 的转债证管费，或显式旁路；不改 DE
# params.cb_transfer_fee_handoff          建议 dd_page
#   消费 DD 的可转债现货过户费，或显式旁路；不重开假设-DD；不改 DD
# params.cb_spot_stamp_handoff            建议 dc_page
#   消费 DC 的可转债现货印花，或显式旁路；不改 DC
# params.cb_handling_fee_handoff          建议 db_page
#   消费 DB 的可转债现货经手费，或显式旁路；不重开假设-DB；不改 DB
# params.ashare_fee_handoff               建议 s_page
#   消费 S 的沪深股票竞价经手费切日，或显式旁路；不重开假设-S；不改 S
# params.stock_csrc_fee_handoff           建议 t_page
#   消费 T 的股票证管费，或显式旁路；不重开假设-T；不改 T
# params.ashare_stamp_handoff             建议 v_page
#   消费 V 的股票印花税切日，或显式旁路；不重开假设-V；不改 V
# params.bse_limit_aft_handoff            建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；不重开假设-AC；不改 AC
# params.cb_rule_handoff                  建议 q_page
#   可转债规则混用交 Q；双字母 DQ ≠ 单字母假设-Q；不重开假设-Q；不改 Q
# params.stock_etf_rotation_handoff       建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 篮子过户费；不重开假设-R；不改 R
# params.block_channel_handoff            建议 o_page
#   大宗通道交 O；不重开假设-O；不改 O
# params.etf_cr_fill_handoff              建议 cm_page
#   ETF 申赎能否成交交 CM；本页只看篮子过户费；不改 CM
# params.board_capacity_handoff           建议 a_page
# params.fill_time_suspend_handoff        建议 d_page
#   成交时点与停牌交 D；双字母 DQ ≠ 单字母假设-D；不改 D
# params.etf_basket_transfer_handoff      建议 self
# params.dq0_primary_demo                 写死冻结 invent_wrong_transfer_on_etf_creation_redemption
#   单一主报写死，单挂；禁与 invent_asof_leak_etf_creation_redemption_transfer 双挂；DQ1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_etf_creation_redemption_transfer 只作对照，不得升格进 dq0，不得双挂
#   诊断桶 copy_ashare_001_onto_etf_basket / invent_zero_on_etf_basket / ignore_post_establishment_half_cut / merge_sse_szse_basket_scope / copy_DN_05_face_onto_etf_basket / apply_basket_fee_onto_secondary / vs_DA_fund_secondary_transfer / vs_DN_exch_conversion_transfer / vs_U_ashare_transfer / vs_AX_fund_handling / vs_DP_exch_conversion_stamp / missing_venue_or_biz_type_not_skip 不得升格进 dq0
#   尤重：禁止把 DA 二级过户与本页申赎篮子合成/混读后写进 dq0（二级成交≠申赎一级篮子）
#   尤重：禁止把 DN 换股面值 0.5‰ 与本页篮子面值档合成/混读后写进 dq0（换股≠申赎；数字相同禁止升格）
#   尤重：禁止把 U 股票过户切日与本页申赎篮子另档合成/混读后写进 dq0；不重开假设-U
#   尤重：禁止把 AX 基金经手与本页过户费合成/混读后写进 dq0
#   尤重：禁止把 DP 换股印花与本页申赎过户合成/混读后写进 dq0
# params.dq0_invent_wrong_transfer_on_etf_creation_redemption 建议 True
# params.dq1_asof_leak_etf_creation_redemption_transfer_only 建议 True
#   半泄露对照；DQ1 不升格并列主报；不得把 invent_asof_leak_etf_creation_redemption_transfer 写进 dq0
# params.dq2_pit_cs_table_face_value_basket_not_secondary_amount 建议 True
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
# params.merge_with_A                     建议 False
# params.merge_with_D                     建议 False
# params.merge_with_CM                    建议 False
# params.missing_venue_or_biz_type_or_official_bps_policy 建议 skip
# params.day_freq_proxy                   建议 etf_basket_transfer_sensitivity
# params.universe_rule                    建议 etf_basket_transfer_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dq_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DQ；勿把这个键读成实验 DQ，亦勿读成单字母 D/Q
#   不另挂主报，不预留 #127，不写下一字母
```

### 2.2 三组对照（DQ0 / DQ1 / DQ2）

组名 DQ0 / DQ1 / DQ2 是本页三组，≠ 单字母实验 Q（可转债规则混用）。

| 组 | 角色 | 口径 |
|----|------|------|
| DQ0 | 天真 / 申赎篮子过户误套 | 按 `dq0_primary_demo` **写死冻结**单一主报 `invent_wrong_transfer_on_etf_creation_redemption`（单挂写死）：把 ETF 申购赎回组合证券过户套错（按二级 0.01‰、免费 0、忽略减半、沪深合成、抄 DN 面值、或铺到二级）。**禁**与 `invent_asof_leak_etf_creation_redemption_transfer` 双挂主报。**禁把 DA 二级过户、DN 换股面值 0.5‰、U 股票过户切日、AX 基金经手、DP 换股印花合成进 `dq0`**（只作对照/旁路，不得升格进 `dq0` 或另挂主报） |
| DQ1 | 半泄露 | 仅核对日把「面值档、成立后暂减半、沪深分列、只收沪市成分」铺到全历史、铺到二级腿，或把 DN 的 0.5‰ 换成股抄过来，或把股票 0.01‰ 铺到篮子（`invent_asof_leak_etf_creation_redemption_transfer`）；**不得升格并列主报**，也不得写进 `dq0`（写死冻结：DQ1 不升格），不得双挂 |
| DQ2 | 诚实 / 申赎篮子按结算表面值档 | `etf_basket_transfer_honest=pit_cs_table_face_value_basket_not_secondary_amount`（写死冻结）：缺 venue/业务类型或官方‰则 skip；申赎篮子按组合证券股票面值档；深市成立后暂减半 0.25‰；沪市成立后暂减半且目前只收所含沪市成分；禁止按二级成交金额 0.01‰ 抽；禁止发明免费 0；禁止把篮子费铺到二级腿；沪深分列禁止合成；二级只消费 DA。换股过户只消费 DN，股票过户切日只消费 U，基金经手只消费 AX，换股印花只消费 DP，或显式旁路 |

按二级 0.01‰ 抽篮子、发明免费 0、忽略成立后暂减半、沪深合成、抄 DN 面值 0.5‰、把篮子费铺到二级、把 DA/DN/U/AX/DP 混进篮子过户，以及相对这些页的对照截（`copy_ashare_001_onto_etf_basket` / `invent_zero_on_etf_basket` / `ignore_post_establishment_half_cut` / `merge_sse_szse_basket_scope` / `copy_DN_05_face_onto_etf_basket` / `apply_basket_fee_onto_secondary` / `vs_DA_fund_secondary_transfer` / `vs_DN_exch_conversion_transfer` / `vs_U_ashare_transfer` / `vs_AX_fund_handling` / `vs_DP_exch_conversion_stamp` / `missing_venue_or_biz_type_not_skip`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dq0_primary_demo`。`vs_DA_fund_secondary_transfer` 只标记「有人把 DA 的二级过户和本页申赎篮子合成/混读」，**不得升格进 `dq0`**。`vs_DN_exch_conversion_transfer` 只标记换股过户对照，**不得升格进 `dq0`**。`vs_U_ashare_transfer` 只标记股票过户切日对照，**不得升格进 `dq0`**。`vs_AX_fund_handling` 只标记基金经手对照，**不得升格进 `dq0`**。`vs_DP_exch_conversion_stamp` 只标记换股印花对照，**不得升格进 `dq0`**。DA 的二级过户、DN 的换股面值、U 的股票切日、AX 的基金经手、DP 的换股印花只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dq0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺 venue/业务类型或官方‰则 skip；申赎篮子按组合证券股票面值档；深市成立后暂减半 0.25‰；沪市成立后暂减半且目前只收所含沪市成分；禁止按二级成交金额 0.01‰ 抽；禁止发明免费 0；禁止把篮子费铺到二级腿；沪深分列禁止合成；二级只消费 DA。方向随锚写死：**不要把核对日面值或减半铺满全历史，也不要按二级 0.01‰ 抽篮子，也不要发明免费 0，也不要把篮子费铺到二级腿，也不要沪深合成**。范围名 `creation_redemption_only_secondary_out_of_scope` 只标方向：本页只看 ETF 申购/赎回组合证券过户；二级成交不在范围里，留给 DA。`事实与坑` 2026-11-06 已写：二级成交 ≠ 申赎篮子过户；篮子基数是面值不是成交金额。0.5‰ 与 0.25‰ 是表上的篮子方向，0.01‰ 是股票过户或被误套的二级口径，本页不重开 U，也不把它们冻成自己的门槛。DN 的换股面值同是 0.5‰，数字相同也不升格。`params.G` 的 0.01 是无量纲相对门槛，不是股票过户 0.01‰，也不是篮子面值 0.5‰。**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**。缺 venue、业务类型或官方‰则 skip，不用免费 0、自造‰、占位 0.01 或 DN 的 0.5‰ 把篮子腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dq0_primary_demo` / `params.Y`·G·N·Y2 / 篮子过户开关 / 桶 / 是否把 0.5‰、0.25‰、0.01‰ 或免费 0 铺到全历史、铺到二级或合成沪深）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DQ0）/ 半泄露组（DQ1）相对诚实组（DQ2）的成本差、误套截**显著且集中在申赎篮子过户被套错的桶**（按二级 0.01‰、免费 0、忽略减半、沪深合成、抄 DN 面值、或铺到二级）；分桶「二级 0.01‰ / 免费 0 / 忽略减半 / 沪深合成 / 抄 DN / 铺到二级 / 核对日泄露 / vs DA·DN·U·AX·DP」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 0.5‰ 或 0.25‰ 冻成全历史唯一费率，也不把 `params.G` 的 0.01 读成过户费率。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 DA 的二级过户、DN 的换股过户、U 的股票过户切日、AX 的基金经手、DP 的换股印花、DO 的回售经手、DM 的换股经手、DL 的综合协议过户、DK 的基金印花、DJ 的基金证管费、DI 的大宗经手、DH 的佣金双计、DG 的北交所档、DF 的可交换现货经手、DE 的转债证管费、DD 的转债过户、DC 的转债印花、DB 的转债现货经手、S 的股票经手、T 的股票证管费、V 的股票印花、AC 的北交所涨跌幅与盘后、Q 的回转与涨跌幅、R 的股票 ETF 回转、O 的大宗通道、CM 的申赎可成交、A 的板上容量、D 的成交时点解释；或 `dq0_primary_demo` 与 `invent_asof_leak_etf_creation_redemption_transfer` 双挂；或 DQ1 升格并列主报；或 `copy_ashare_001_onto_etf_basket` / `invent_zero_on_etf_basket` / `ignore_post_establishment_half_cut` / `merge_sse_szse_basket_scope` / `copy_DN_05_face_onto_etf_basket` / `apply_basket_fee_onto_secondary` / `vs_DA_fund_secondary_transfer` / `vs_DN_exch_conversion_transfer` / `vs_U_ashare_transfer` / `vs_AX_fund_handling` / `vs_DP_exch_conversion_stamp` / `missing_venue_or_biz_type_not_skip` 诊断桶升格主报；或把 DA 二级过户、DN 换股面值、U 股票过户切日、AX 基金经手、DP 换股印花合成进 `dq0`；或实验字母 DQ 与单字母 D/Q 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成股票过户 0.01‰ 或篮子面值 0.5‰；或把占位读成 0.5‰/0.25‰/0.01‰/免费 0；或把核对日面值或减半写成已冻并铺满全历史；或缺 venue / 业务类型 / 官方‰仍不 skip；或按二级 0.01‰ 抽篮子；或发明免费 0；或把篮子费铺到二级腿；或沪深合成一句；或重开假设-T / 假设-U / 假设-DA / 假设-DN / 假设-AX / 假设-DP / 假设-Q / 假设-AC / 假设-R / 假设-O / 假设-DI / 假设-V / 假设-DF / 假设-DB / 假设-S / 假设-DD / 假设-DL / 假设-DM / 假设-DO / 假设-DC / 假设-DK；或标纸面齐；或写成 A/D–DQ纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权篮子面值，对照 DQ0/DQ1/DQ2。二级过户走 DA 或显式旁路，不在本页改 DA，也不把篮子费铺到二级腿。换股过户走 DN，股票过户切日走 U，基金经手走 AX，换股印花走 DP，都不改。报告成本差、误套截。不把 0.5‰ 或 0.25‰ 标成已冻的全历史篮子费率，也不把 `params.G` 的 0.01 读成过户费率。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_wrong_transfer_on_etf_creation_redemption` / `invent_asof_leak_etf_creation_redemption_transfer` / `copy_ashare_001_onto_etf_basket` / `invent_zero_on_etf_basket` / `ignore_post_establishment_half_cut` / `merge_sse_szse_basket_scope` / `copy_DN_05_face_onto_etf_basket` / `apply_basket_fee_onto_secondary` / `vs_DA_fund_secondary_transfer` / `vs_DN_exch_conversion_transfer` / `vs_U_ashare_transfer` / `vs_AX_fund_handling` / `vs_DP_exch_conversion_stamp` / `missing_venue_or_biz_type_not_skip`

`copy_ashare_001_onto_etf_basket`、`invent_zero_on_etf_basket`、`ignore_post_establishment_half_cut`、`merge_sse_szse_basket_scope`、`copy_DN_05_face_onto_etf_basket`、`apply_basket_fee_onto_secondary`、`vs_DA_fund_secondary_transfer`、`vs_DN_exch_conversion_transfer`、`vs_U_ashare_transfer`、`vs_AX_fund_handling`、`vs_DP_exch_conversion_stamp`、`missing_venue_or_biz_type_not_skip` 只作诊断桶：它们不是 `dq0`，也不是 DQ1，**不得升格主报**。`vs_DA_fund_secondary_transfer` 没有对应的「二级过户 + 篮子过户」合成主报。DA 的二级过户只作诊断，**不得与申赎篮子合成后升格进 `dq0`**。DN 的换股面值 0.5‰ 只作诊断，**不得因数字相同升格进 `dq0`**。U 的股票过户切日只作诊断，**不得升格进 `dq0`**。AX 的基金经手只作诊断，**不得升格进 `dq0`**。DP 的换股印花只作诊断，**不得升格进 `dq0`**。按 0.01‰ 抽、写成免费 0、忽略减半、沪深合成、篮子费铺到二级、缺字段仍不 skip，都只作诊断，**不得升格进 `dq0`**。`invent_asof_leak_etf_creation_redemption_transfer` 只服务 DQ1，**不得升格进 `dq0`，不得双挂**。`invent_wrong_transfer_on_etf_creation_redemption` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把按二级 0.01‰ 抽篮子、发明免费 0、或把篮子费铺到二级腿，并拿去当诚实锚。
- 把 `params.G` 的 0.01 当成股票过户 0.01‰ 或篮子面值 0.5‰。**尤重：`params.G` 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 0.5‰/0.25‰/0.01‰/免费 0。**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**。
- 缺 venue、业务类型或官方‰仍不 skip，并用 0.01‰、免费 0、自造‰或占位 0.01 把篮子腿填上。
- 把核对日「面值档、成立后暂减半」写成全历史唯一费率，并铺满全历史，或按二级 0.01‰ 抽，或发明免费 0，或把篮子费铺到二级腿，或沪深合成一句。锚六键已写死冻结。
- 把「二级过户已分列（DA）/ 换股过户已分列（DN）/ 股票过户切日已诚实（U）/ 基金经手已诚实（AX）/ 换股印花已分列（DP）」写成「ETF 申赎组合证券过户已诚实」。不改 DA / DN / U / AX / DP。
- 把 DA 的二级过户和本页申赎篮子合成或混读后升格进 `dq0`。诊断桶 `vs_DA_fund_secondary_transfer` / `apply_basket_fee_onto_secondary` 只作对照。二级成交≠申赎一级篮子。
- 把 DN 换股面值 0.5‰ 和本页篮子面值档合成或混读后升格进 `dq0`。诊断桶 `vs_DN_exch_conversion_transfer` / `copy_DN_05_face_onto_etf_basket` 只作对照。换股≠申赎；数字相同禁止升格混读。
- 把 U 股票过户切日和本页申赎篮子另档合成或混读后升格进 `dq0`。诊断桶 `vs_U_ashare_transfer` / `copy_ashare_001_onto_etf_basket` 只作对照。不重开假设-U。
- 把 AX 基金经手和本页过户费合成或混读后升格进 `dq0`。诊断桶 `vs_AX_fund_handling` 只作对照。
- 把 DP 换股印花和本页申赎过户合成或混读后升格进 `dq0`。诊断桶 `vs_DP_exch_conversion_stamp` 只作对照。
- 忽略成立后暂减半，并升格进 `dq0`。诊断桶 `ignore_post_establishment_half_cut` 只作对照。
- 沪深合成一句，并升格进 `dq0`。诊断桶 `merge_sse_szse_basket_scope` 只作对照。
- 发明免费 0，并升格进 `dq0`。诊断桶 `invent_zero_on_etf_basket` 只作对照。
- 缺 venue 或业务类型仍不 skip，并升格进 `dq0`。诊断桶 `missing_venue_or_biz_type_not_skip` 只作对照。
- `dq0_primary_demo` 与 `invent_asof_leak_etf_creation_redemption_transfer` 双挂主报；DQ1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DQ 与单字母 D/Q 或 params.Y/G/N 混读。**双字母 DQ ≠ 单字母假设-Q**。
- 改 DA / DN / U / AX / DP / DO / DM / DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / S / T / V / AC / Q / R / O / A / D 正文；重开假设-T；重开假设-U；重开假设-DA；重开假设-DN；重开假设-AX；重开假设-DP；重开假设-Q；重开假设-AC；重开假设-R；重开假设-O；重开假设-DI；重开假设-V；重开假设-DF；重开假设-DB；重开假设-S；重开假设-DD；重开假设-DL；重开假设-DM；重开假设-DO；重开假设-DC；重开假设-DK；抢 A 真数队列；标纸面齐；写成 A/D–DQ纸面齐；开真数/回测/实盘；用复权价当费用基数；结论写成「申赎费更低所以能买」。
- **纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK/DL/DM/DN/DO/DP；勿再只改清单）。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权篮子面值（不是二级成交金额）、交易日、**交易所 venue**（沪/深）、**业务类型**（ETF 申购赎回组合证券 / 场内基金二级 / 可交换债换股 / 股票二级 / 基金经手 / 换股印花；仅用于把腿分回 DA、DN、U、AX、DP 或本页）、**成分范围**（沪市目前只收所含沪市成分；深市按深市表分列）、**成立前/成立后**（成立后暂减半；发售阶段表内免收不另挂主报）、**官方篮子过户‰是否在册**（缺则 skip，不发明数，也不填免费 0）。
- 股票过户 0.01‰ 若要数字，只消费 U 已有口径，不在本页重开 U，也不把股票二级业务类型换成申赎篮子。
- 二级腿若要过户，只消费 DA，不把篮子面值档铺到二级成交金额。
- 证券类别只用于把腿分回 DA / DN / U / AX / DP 等旁路页，不在本页改那些页。
- 没有 venue、业务类型或官方‰时，按写死冻结的 `etf_basket_transfer_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing` skip，不得按免费 0 把篮子腿填上，也不得按 0.01‰ 或占位 0.01 或 DN 的 0.5‰ 把篮子腿填上。
- 旁路消费：DA 的场内基金二级过户、DN 的换股过户、U 的股票过户切日、AX 的基金经手、DP 的换股印花、DO 的回售经手、DM 的换股经手、DL 的综合协议过户下浮、DK 的基金印花、DJ 的基金证管费、DI 的大宗经手、DH 的佣金双计、DG 的北交所经手费、DF 的可交换现货经手、DE 的转债证管费、DD 的转债过户、DC 的转债印花、DB 的转债现货经手、S 的股票经手切日、T 的股票证管费、V 的股票印花、AC 的北交所涨跌幅与盘后、Q 的转债规则、R 的股票 ETF 回转、O 的大宗通道、CM 的申赎可成交、D 的成交时点之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** DA 的二级过户、DN 的换股面值、U 的股票切日、AX 的基金经手、DP 的换股印花不收到本页主报。
- 未复权价；asof **写死冻结** `2026-10-16`。核对日方向「篮子按面值、成立后暂减半、沪深分列、二级不抽本页」是写死冻结的机制方向，不是已冻全历史费率。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`etf_basket_transfer_honest=pit_cs_table_face_value_basket_not_secondary_amount`（申赎篮子按组合证券股票面值档；深市成立后暂减半 0.25‰；沪市成立后暂减半且目前只收所含沪市成分；**禁止按二级成交金额 0.01‰ 抽**；**禁止发明免费 0**；**禁止把篮子费铺到二级腿**；沪深分列禁止合成；二级只消费 DA；**禁止把 0.5‰、0.25‰ 或 0.01‰ 写成全历史唯一费率**）；`etf_basket_transfer_scope=creation_redemption_only_secondary_out_of_scope`（只收申赎组合证券过户，二级不在范围；方向名，不是已冻费率）；`etf_basket_transfer_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing`（缺 venue/业务类型或官方‰则 skip）；`dq0_primary_demo=invent_wrong_transfer_on_etf_creation_redemption`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_etf_creation_redemption_transfer` 双挂；DQ1 不升格；诊断桶不升格主报；**禁把 DA 二级过户、DN 换股面值 0.5‰、U 股票过户切日、AX 基金经手、DP 换股印花合成进 `dq0`**，只作对照/旁路，不得升格进 `dq0` 或另挂主报）；`fund_secondary_transfer_handoff=da_page`；`exch_conversion_transfer_handoff=dn_page`；`ashare_transfer_handoff=u_page`；`fund_handling_handoff=ax_page`；`exch_conversion_stamp_handoff=dp_page`；`merge_with_DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/A/D=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误套截 ΔEtfBasketTransfer / 净收益差 / DQ1−DQ2；**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰（量纲与语义不同）**；**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**；**params.Y/G/N ≠ 实验字母 DQ ≠ 单字母 D/Q**；**勿把 params.G 读成实验字母 DQ，亦勿把单字母假设-D / 假设-Q 读成双字母 DQ**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成篮子过户费率或免费 0）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #127。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`08d5dfd0`（A/D–DP纸面齐已合，全长 `08d5dfd0de59ddfa5d409713bb7b3d58e8469068`）；三冻补丁基 tip=`add50994` / `add5099439f048881a18b641281d01cbb2f9f645`；分支起点 HEAD=`01dfc9a7` / `01dfc9a76b809a977af2941637a68961c170a97d`。**不改已冻 A–DP / DA–DO**。状态=**A/D–DQ纸面齐（预检有条件通过·三条已冻）**。

---

## 8. 结论

（空；**A/D–DQ纸面齐（预检有条件通过·三条已冻）**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-23）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DQ-20261110.md`（原样落入，不改结论；SHA256=`48d58a74c9abe51adfc4b190d03a874487bacac130cddcd5f0bef928b9ffe445`；预检 2026-11-10；**结论：有条件通过**；tip基=`add50994` / `add5099439f048881a18b641281d01cbb2f9f645`；本补丁分支起点 HEAD=`01dfc9a7` / `01dfc9a76b809a977af2941637a68961c170a97d`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、误套截 ΔEtfBasketTransfer、净收益差、DQ1−DQ2 专项。**`params.Y` ≠ 实验字母 DQ**；**`params.G` ≠ 实验字母 DQ**；**`params.N` ≠ 实验字母 DQ**；亦 ≠ 单字母假设-D / 假设-Q。**勿把 `params.G` 读成实验字母 DQ，亦勿把单字母假设-D / 假设-Q 读成双字母 DQ**。**尤重：`params.G` 的 `0.01` ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**（**params.G 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**）。三者量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是股票过户费率，也不是申赎篮子面值费率，也不是免费 0；0.01‰ 若被消费，只走 U 的股票过户切片或 DA 的二级旁路；0.5‰ / 0.25‰ 若出现，只是篮子面值方向或 DN 的换股面值。**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**。禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dq0_primary_demo`**：**写死冻结** **`invent_wrong_transfer_on_etf_creation_redemption`**（单一主报，单挂写死）。**禁止**与 **`invent_asof_leak_etf_creation_redemption_transfer`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DQ1 仅核对日把「面值档、成立后暂减半、沪深分列、只收沪市成分」铺到全历史、铺到二级腿，或把 DN 的 0.5‰ 抄过来，或把股票 0.01‰ 铺到篮子只作半泄露对照，**不得升格与 dq0 并列主报**，也不得把 `invent_asof_leak_etf_creation_redemption_transfer` 写进 `dq0`。`copy_ashare_001_onto_etf_basket` / `invent_zero_on_etf_basket` / `ignore_post_establishment_half_cut` / `merge_sse_szse_basket_scope` / `copy_DN_05_face_onto_etf_basket` / `apply_basket_fee_onto_secondary` / `vs_DA_fund_secondary_transfer` / `vs_DN_exch_conversion_transfer` / `vs_U_ashare_transfer` / `vs_AX_fund_handling` / `vs_DP_exch_conversion_stamp` / `missing_venue_or_biz_type_not_skip` **只作诊断桶，不得升格主报**。DQ1 / 诊断桶 **不升格**。**禁把 DA场内基金二级过户 / DN换股过户面值 / U股票过户切日 / AX基金经手 / DP换股印花 合成/混读升格进 `dq0`**：这些只作对照/旁路，**不得升格进 `dq0`，不得另挂主报**。**不重开假设-U**；**不重开假设-Q**；**不重开假设-T**。二级成交≠申赎一级篮子。换股≠申赎；数字相同禁止升格混读。

3. **ETF 申购赎回组合证券过户诚实锚六键升格写死（不可再写「建议」）**：`params.etf_basket_transfer_honest=pit_cs_table_face_value_basket_not_secondary_amount`；`params.etf_basket_transfer_scope=creation_redemption_only_secondary_out_of_scope`；`params.etf_basket_transfer_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺 venue/业务类型或官方‰ → skip；申赎篮子按组合证券股票面值档；深市成立后暂减半 0.25‰；沪市成立后暂减半且目前只收所含沪市成分；禁止按二级成交金额 0.01‰ 抽；禁止发明免费 0；禁止把篮子费铺到二级腿；沪深分列禁止合成；二级只消费 DA。禁止把核对日 0.5‰、0.25‰ 或 0.01‰ 铺满全历史。禁止跑后改锚，或用免费 0 / 核对日费率铺满 / 0.01‰ 抽篮子 / 发明‰ / 缺 venue/业务类型或官方‰仍硬填 / 把 DA场内基金二级过户、DN换股过户面值、U股票过户切日、AX基金经手或 DP换股印花升格进 dq0 冒充诚实 PIT。**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**。**禁把 params.G 的 0.01 读成股票过户 0.01‰ 或篮子面值 0.5‰**。**不重开假设-U**；**不重开假设-Q**；**不重开假设-T**。

**硬分列保住**：DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D；**双字母 DQ ≠ 单字母假设-D / 假设-Q**；**params.Y / params.G / params.N ≠ 实验字母 DQ ≠ 单字母 D/Q**；**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**；**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**；**ETF申购赎回组合证券过户误套 ≠ DA场内基金二级过户 ≠ DN换股过户面值 ≠ U股票过户切日 ≠ AX基金经手 ≠ DP换股印花**；不抢 A；不改已齐/已冻 DA～DP 及 A–DP 正文；**不重开假设-T**；**不重开假设-U**；**不重开假设-Q**；**不重开假设-DA**；**不重开假设-DN**；**不重开假设-AX**；**不重开假设-DP**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DO**；**不重开假设-DC**；**不重开假设-DK**；**禁把 DA场内基金二级过户 / DN换股过户面值 / U股票过户切日 / AX基金经手 / DP换股印花 合成/混读升格进 dq0**。handoff 保持：`fund_secondary_transfer_handoff=da_page`；`exch_conversion_transfer_handoff=dn_page`；`ashare_transfer_handoff=u_page`；`fund_handling_handoff=ax_page`；`exch_conversion_stamp_handoff=dp_page`；`merge_with_*=False`。

**状态**：**A/D–DQ纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-10 | 复检/纸面齐——**A/D–DQ纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设DQ-20261110.md` 原样落入，SHA256=`f4b86f99e660e5e2fbcdf39880e2a8a3d8880f424b87416e29ab2659c57ea023`；三冻 tip=`227a1f26` / `227a1f26cda838b4183163d26360d468c70db7c1`。只改状态标签；未改写已冻三条/六键；不改已齐 A–DP / DA–DO；不改 #110–#125；不重开假设-DA / 假设-DN / 假设-U / 假设-AX / 假设-DP / 假设-T / 假设-Q；不开回测/真数/实盘。 |
| 2026-11-23 | 风控预检补丁·冻结三条写死——依据 `预检-假设DQ-20261110.md`（SHA256=`48d58a74c9abe51adfc4b190d03a874487bacac130cddcd5f0bef928b9ffe445`；结论=有条件通过；tip基=`add50994` / `add5099439f048881a18b641281d01cbb2f9f645`；分支起点 HEAD=`01dfc9a7` / `01dfc9a76b809a977af2941637a68961c170a97d`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔEtfBasketTransfer / 净收益差 / DQ1−DQ2；**params.Y/G/N ≠ 实验字母 DQ ≠ 单字母 D/Q**；**勿把 params.G 读成实验字母 DQ，亦勿把单字母假设-D / 假设-Q 读成双字母 DQ**；**尤重 params.G 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰（量纲与语义不同）**；**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成篮子过户费率或免费 0）；② `params.dq0_primary_demo=invent_wrong_transfer_on_etf_creation_redemption`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_etf_creation_redemption_transfer` 双挂；DQ1 不升格；诊断桶 `copy_ashare_001_onto_etf_basket` / `invent_zero_on_etf_basket` / `ignore_post_establishment_half_cut` / `merge_sse_szse_basket_scope` / `copy_DN_05_face_onto_etf_basket` / `apply_basket_fee_onto_secondary` / `vs_DA_fund_secondary_transfer` / `vs_DN_exch_conversion_transfer` / `vs_U_ashare_transfer` / `vs_AX_fund_handling` / `vs_DP_exch_conversion_stamp` / `missing_venue_or_biz_type_not_skip` 不升格；**禁把 DA场内基金二级过户 / DN换股过户面值 / U股票过户切日 / AX基金经手 / DP换股印花 合成/混读升格进 dq0**，只作对照/旁路，不得升格进 dq0 或另挂主报；不重开假设-U；不重开假设-Q；不重开假设-T；二级成交≠申赎一级篮子；换股≠申赎）；③ 锚六键写死 `etf_basket_transfer_honest=pit_cs_table_face_value_basket_not_secondary_amount` / `etf_basket_transfer_scope=creation_redemption_only_secondary_out_of_scope` / `etf_basket_transfer_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`（缺 venue/业务类型或官方‰ → skip；申赎篮子按组合证券股票面值档；深市成立后暂减半 0.25‰；沪市成立后暂减半且目前只收所含沪市成分；禁止按二级成交金额 0.01‰ 抽；禁止发明免费 0；禁止把篮子费铺到二级腿；沪深分列禁止合成；二级只消费 DA）。handoff 保持 `fund_secondary_transfer_handoff=da_page` / `exch_conversion_transfer_handoff=dn_page` / `ashare_transfer_handoff=u_page` / `fund_handling_handoff=ax_page` / `exch_conversion_stamp_handoff=dp_page`；`merge_with_*=False`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DQ纸面齐**；不改已齐/已冻 DA～DP 及 A–DP；不改假设-DA～假设-DP；不重开假设-T；不重开假设-U；不重开假设-Q；不重开假设-DA；不重开假设-DN；不重开假设-AX；不重开假设-DP；不开回测/真数/实盘。基于 tip=`add50994`。 |
| 2026-11-23 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。ETF申购赎回组合证券过户费误套；`dq0_primary_demo` 建议 `invent_wrong_transfer_on_etf_creation_redemption`，单一主报，单挂，禁与 `invent_asof_leak_etf_creation_redemption_transfer` 双挂，DQ1 不升格；诊断桶 `copy_ashare_001_onto_etf_basket` / `invent_zero_on_etf_basket` / `ignore_post_establishment_half_cut` / `merge_sse_szse_basket_scope` / `copy_DN_05_face_onto_etf_basket` / `apply_basket_fee_onto_secondary` / `vs_DA_fund_secondary_transfer` / `vs_DN_exch_conversion_transfer` / `vs_U_ashare_transfer` / `vs_AX_fund_handling` / `vs_DP_exch_conversion_stamp` / `missing_venue_or_biz_type_not_skip` 不升格；**尤重 DA 场内基金二级过户误套 ≠ 本页 ETF 申赎组合证券过户（二级成交≠申赎一级篮子），禁止合成/混读升格进 dq0**；**尤重 DN 可交换换股过户面值 0.5‰ ≠ 本页 ETF 篮子面值档（换股≠申赎；数字相同禁止升格混读），禁止合成进 dq0**；**尤重 U 股票过户切日 ≠ 本页申赎篮子另档，不重开假设-U，禁止合成进 dq0**；**尤重 AX 基金经手费 ≠ 本页过户费，禁止合成进 dq0**；**尤重 DP 换股印花 ≠ 本页申赎过户，禁止合成进 dq0**；**禁与 DA/DN/U/AX/DP 混读**；**双字母 DQ ≠ 单字母假设-Q**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DQ ≠ 单字母 D/Q**，且 **params.G 的 0.01 ≠ 股票过户 0.01‰ ≠ 篮子面值 0.5‰**，**禁把占位读成 0.5‰/0.25‰/0.01‰/免费 0**；锚建议、未冻：`etf_basket_transfer_honest=pit_cs_table_face_value_basket_not_secondary_amount` / scope=`creation_redemption_only_secondary_out_of_scope` / over_policy=`skip_if_venue_or_biz_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`；口径：缺 venue/业务类型或官方‰则 skip；申赎篮子按组合证券股票面值档；深市成立后暂减半 0.25‰；沪市成立后暂减半且目前只收所含沪市成分；禁止按二级成交金额 0.01‰ 抽；禁止发明免费 0；禁止把篮子费铺到二级腿；沪深分列禁止合成；二级只消费 DA（**草稿方向，尚未冻，不要写成已冻**）；handoff：`fund_secondary_transfer_handoff=da_page`，`exch_conversion_transfer_handoff=dn_page`，`ashare_transfer_handoff=u_page`，`fund_handling_handoff=ax_page`，`exch_conversion_stamp_handoff=dp_page`；`merge_with_DP/DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/A/D=False`；**DQ≠DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D**；**双字母 DQ ≠ 单字母假设-D / 假设-Q**；**未标纸面齐**；**不写 A/D–DQ纸面齐**；**纸面齐惯例**：落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK/DL/DM/DN/DO/DP；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DP / DA–DO；不改已齐假设-DA～假设-DP；不重开假设-T；不重开假设-U；不重开假设-DA；不重开假设-DN；不重开假设-AX；不重开假设-DP；不重开假设-Q；不写下一字母；不预留 #127；不开真数/回测/实盘。基 tip=`08d5dfd0`（A/D–DP纸面齐已合，全长 `08d5dfd0de59ddfa5d409713bb7b3d58e8469068`；不改该 tip 上的 #110–#125，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
