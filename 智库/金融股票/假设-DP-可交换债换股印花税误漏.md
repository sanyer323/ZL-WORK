# 假设-DP · 可交换债换股印花税误漏（成本诚信）

更新：2026-11-20  
来源：总管线 / 基 tip=`c786804e` / 全长 `c786804e28642c55521ac706825ffff78d728a47`（A/D–DO纸面齐已合）；**不改已冻 A–DO / DA–DN**；**不改假设-DO 正文**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-DN / 假设-S / 假设-AX / 假设-T / 假设-U / 假设-V / 假设-AC / 假设-Q / 假设-R / 假设-A / 假设-D / 假设-O / 假设-P / 假设-N 及其他已存在假设页；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DO**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**）后写下一草稿 DP；清单 #124=DO，本页占用 **#125=DP**；选题是回测漏记可交换债**换股**印花税（结算表列征税、出让方），或把 DC 现货不征抄成换股免费 0；假设-DC 只收可转债**现货**印花误抽（现货不征 ≠ 换股应交，方向相反），假设-V 只收股票二级印花税切日，假设-DK 只收场内基金印花税误抽，假设-DM 只收可交换债换股经手费，假设-DN 只收可交换债换股过户费，假设-DO 只收可转债回售经手费暂免；**新建实验 DP**；不写下一字母；不预留 #126  
状态：**草稿·待入库预检**（结论栏空；**三条尚未冻**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DP纸面齐**；禁止把「漏记换股印花、或把现货不征抄成换股免费 0」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改已冻 A–DO / DA–DN**；尤其不改假设-DC / 假设-V / 假设-DK / 假设-DM / 假设-DN / 假设-DO / 假设-DL / 假设-T / 假设-AC / 假设-R / 假设-U / 假设-O / 假设-DI / 假设-DF / 假设-DB / 假设-S / 假设-DD / 假设-DA / 假设-D / 假设-P；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DO**；**不重开假设-DC**；**不重开假设-DK**；**不重开假设-DA**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DP（#125）。一句话误开：回测漏记可交换债**换股**印花税（结算表列征税、出让方），或把 DC 现货不征抄成换股免费 0，或与 V股票印花 / DK基金印花 / DM换股经手 / DN换股过户 / DO回售经手 混读，或缺 venue/业务类型/官方‰仍不 skip，系统性改写换股腿印花成本。

> **字母消歧（硬）**：本页**实验字母 DP** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；占位 0.02；**尚未冻，不要写成已冻**；**params.Y ≠ 实验字母 DP**；**勿把 `params.Y` 读成实验字母 DP**）≠ **`params.G`**（同族门槛，占位 0.01；**尚未冻，不要写成已冻**；**params.G ≠ 实验字母 DP**；**尤重：`params.G` 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是印花税率；0.5‰ / 法定 1‰ 若被消费，只走 V 的股票印花切片，不是本页门槛，也不是换股免费 0；**禁把占位读成 1‰/0.5‰/免费 0**）≠ **`params.N`**（失败/废单率差门槛；占位 0.05；**尚未冻，不要写成已冻**；**params.N ≠ 实验字母 DP**；**params.N ≠ 单字母假设-N**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DP ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 P**（指数点位与停牌假成交权重；**双字母 DP ≠ 单字母假设-P；严禁复用假设-P**；组名 DP0/DP1/DP2 是本页三组对照，≠ 单字母实验 P）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DP ≠ 单字母假设-A**）≠ 双字母 **DO**（可转债回售经手费暂免误忽略）≠ **DN**（可交换债换股过户费误套）≠ **DM**（可交换债换股经手费误套现货）≠ **DL**（股票综合协议过户费下浮）≠ **DK**（场内基金印花税误抽）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债现货经手费沪深合成）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债现货印花税误抽）≠ **DB**（可转债现货经手费）≠ **DA**（场内基金过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费）≠ **T**（股票证管费）≠ **U**（股票过户费）≠ **V**（股票印花税切日）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）≠ **O**（大宗假流动性）。**DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D**。**双字母 DP ≠ 单字母 D/P**。**params.Y/G/N ≠ 实验字母 DP；亦 ≠ 单字母 D/P**。**勿把 `params.G` 读成实验字母 DP，亦勿把单字母假设-D / 假设-P 读成双字母 DP**。**尤重：`params.G` 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰**。**禁把占位读成 1‰/0.5‰/免费 0**。**可交换换股印花税误漏 ≠ DC转债现货印花 ≠ V股票印花切日 ≠ DM换股经手 ≠ DN换股过户**。**尤重：DC 可转债现货印花误抽 ≠ 本页可交换换股印花误漏（现货不征≠换股应交；方向相反）——禁止合成/混读升格进 `dp0`**。**尤重：V 股票二级印花切日 ≠ 本页换股业务类型——不重开假设-V、禁升格进 `dp0`**。**尤重：DK 场内基金印花误抽 ≠ 本页换股印花误漏——禁止合成/混读升格进 `dp0`**。**尤重：DM 换股经手 / DN 换股过户 ≠ 本页换股印花（经手≠过户≠印花三层分列）——禁止合成/混读升格进 `dp0`**。**尤重：DO 回售经手暂免 ≠ 本页换股印花——禁止合成/混读升格进 `dp0`**。

### 专节 · 双字母 DP ≠ 单字母假设-D / 假设-P；且 ≠ 假设-DC / 假设-V / 假设-DK / 假设-DM / 假设-DN / 假设-DO / 假设-DL（硬）

| 维度 | 对照页 | 本页假设-DP（双字母） |
|------|--------|----------------------|
| 题面 DC | **可转债现货印花税误抽**（现货不在税目、不征；现货不征 ≠ 换股应交） | 现货印花误抽 ≠ 本页换股印花误漏。**现货不征≠换股应交**，方向相反。**DP≠DC**；**严禁复用假设-DC**；**不重开假设-DC**；**不改 DC**；**尤重：DC 可转债现货印花误抽 ≠ 本页可交换换股印花误漏（现货不征≠换股应交；方向相反）——禁止合成/混读升格进 `dp0`**；`cb_spot_stamp_handoff=dc_page`；诊断桶 `vs_DC_cb_spot_stamp` / `copy_DC_cb_spot_no_stamp_onto_conversion` / `invent_zero_stamp_on_exch_conversion` 不升格 |
| 题面 V | **股票二级印花税切日**（卖方、法定 1‰、2023-08-28 起减半 0.5‰；业务类型是股票二级，不是换股） | 股票二级印花切日 ≠ 本页换股业务类型。税率切片可以**消费** V 口径，**不重开假设-V**。**DP≠V**；**严禁复用假设-V**；**不改 V**；**尤重：V 股票二级印花切日 ≠ 本页换股业务类型——不重开假设-V、禁升格进 `dp0`**；`ashare_stamp_handoff=v_page`；诊断桶 `vs_V_ashare_stamp` / `confuse_with_stock_secondary_V` / `ignore_20230828_half_cut` 不升格 |
| 题面 DK | **场内基金印花税误抽**（基金不在股票税目） | 基金印花误抽 ≠ 本页换股印花误漏。**DP≠DK**；**严禁复用假设-DK**；**不重开假设-DK**；**不改 DK**；**尤重：DK 场内基金印花误抽 ≠ 本页换股印花误漏——禁止合成/混读升格进 `dp0`**；`fund_stamp_handoff=dk_page`；诊断桶 `vs_DK_fund_stamp` 不升格 |
| 题面 DM | **可交换债换股经手费误套现货**（经手 ≠ 印花） | 换股经手 ≠ 本页换股印花。**经手≠过户≠印花**。**DP≠DM**；**严禁复用假设-DM**；**不重开假设-DM**；**不改 DM**；**尤重：DM 换股经手 ≠ 本页换股印花——禁止合成/混读升格进 `dp0`**；`exch_conversion_handling_handoff=dm_page`；诊断桶 `vs_DM_exch_conversion_handling` 不升格 |
| 题面 DN | **可交换债换股过户费**（过户 ≠ 印花） | 换股过户 ≠ 本页换股印花。**经手≠过户≠印花三层分列**。**DP≠DN**；**严禁复用假设-DN**；**不重开假设-DN**；**不改 DN**；**尤重：DN 换股过户 ≠ 本页换股印花——禁止合成/混读升格进 `dp0`**；`exch_conversion_transfer_handoff=dn_page`；诊断桶 `vs_DN_exch_conversion_transfer` 不升格 |
| 题面 DO | **可转债回售经手费暂免**（回售经手 ≠ 换股印花） | 回售经手暂免 ≠ 本页换股印花。**DP≠DO**；**严禁复用假设-DO**；**不重开假设-DO**；**不改 DO**；**尤重：DO 回售经手暂免 ≠ 本页换股印花——禁止合成/混读升格进 `dp0`**；`cb_put_handling_handoff=do_page`；诊断桶 `vs_DO_cb_put_handling` 不升格 |
| 题面 DL | **股票综合协议过户费下浮**（过户下浮 ≠ 换股印花） | 综合协议过户下浮 ≠ 换股印花。**DP≠DL**；**严禁复用假设-DL**；**不重开假设-DL**；**不改 DL**；`agreement_transfer_handoff=dl_page` |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 本机制。**DP≠DJ**；**不改 DJ**；`fund_csrc_fee_handoff=dj_page` |
| 题面 DI | **股票大宗经手下浮** | 大宗经手下浮 ≠ 换股印花。**DP≠DI**；**严禁复用假设-DI**；**不重开假设-DI**；**不改 DI**；`stock_block_handling_handoff=di_page` |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 换股印花。**DP≠DH**；**不改 DH**；`commission_double_handoff=dh_page` |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 本机制。**DP≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DF | **可交换债现货经手费沪深合成** | 可交换现货经手 ≠ 换股印花。**DP≠DF**；**严禁复用假设-DF**；**不重开假设-DF**；**不改 DF**；`exch_spot_handling_handoff=df_page` |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 换股印花。**DP≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债现货过户费** | 转债过户 ≠ 换股印花。过户≠印花。**DP≠DD**；**严禁复用假设-DD**；**不重开假设-DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DB | **可转债现货经手费** | 转债现货经手 ≠ 换股印花。**DP≠DB**；**严禁复用假设-DB**；**不重开假设-DB**；**不改 DB**；`cb_handling_fee_handoff=db_page` |
| 题面 DA | **场内基金过户费** | 基金过户 ≠ 换股印花。**DP≠DA**；**严禁复用假设-DA**；**不重开假设-DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` |
| 题面 S | **沪深 A 股竞价经手费切日** | 股票经手切日 ≠ 换股印花。**DP≠S**；**严禁复用假设-S**；**不重开假设-S**；**不改 S**；`ashare_fee_handoff=s_page` |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 本机制。**DP≠AX**；**不改 AX**；`fund_handling_fee_handoff=ax_page` |
| 题面 T | **证管费主报股票** | 股票证管费 ≠ 换股印花。**DP≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日** | 股票过户切日 ≠ 换股印花。**DP≠U**；**严禁复用假设-U**；**不重开假设-U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 换股印花。**DP≠AC**；**不改 AC**；**不重开假设-AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 本机制。回转/涨跌幅 ≠ 换股印花。**DP≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 本机制。**DP≠R**；**不改 R**；**不重开假设-R**；`stock_etf_rotation_handoff=r_page` |
| 题面 O | **大宗通道 / 假流动性** | 大宗通道 ≠ 换股印花。**DP≠O**；**不重开假设-O**；**不改 O**；`block_channel_handoff=o_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 换股印花。**DP≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 换股印花抽在哪一腿。**双字母 DP ≠ 单字母假设-D**；**严禁复用假设-D**；**DP≠D**；**不改 D** |
| 题面 P | **指数点位 / 停牌样本假成交与权重** | 指数点位 ≠ 换股印花。**双字母 DP ≠ 单字母假设-P**；**严禁复用假设-P**；**DP≠P**；**不改 P** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_miss_stamp_on_exchangeable_conversion`（**建议**单一主报，单挂；**尚未冻，不要写成已冻**；禁与半泄露键 `invent_asof_leak_exchangeable_conversion_stamp` 双挂；DP1 不升格；`invent_zero_stamp_on_exch_conversion` / `copy_DC_cb_spot_no_stamp_onto_conversion` / `confuse_with_stock_secondary_V` / `bilateral_or_buyer_side_stamp` / `ignore_20230828_half_cut` / `vs_DC_cb_spot_stamp` / `vs_V_ashare_stamp` / `vs_DK_fund_stamp` / `vs_DM_exch_conversion_handling` / `vs_DN_exch_conversion_transfer` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip` 只作诊断对照，不升格主报；**尤重禁止把 DC 现货不征、V 股票二级印花切日、DK 基金印花、DM 换股经手、DN 换股过户、DO 回售经手合成进 `dp0`**） |
| 文档 | 清单实验 DC / V / DK / DM / DN / DO / DL / DJ / DI / DH / DG / DF / DE / DD / DB / DA / S / AX / T / U / AC / Q / R / O / A / D / P（**只读；禁止改写**） | `假设-DP-可交换债换股印花税误漏.md`（新建） |
| 预检键 | 实验字母 DC / V / DK / DM / DN / DO / DL / DJ / DI / DH / DG / DF / DE / DD / DB / DA / S / AX / T / U / AC / Q / R / O / A / D / P / Y / G / N | 实验字母 **DP** / `dp0_primary_demo`；**不得**占用或改写预检 DC/V/DK/DM/DN/DO/DL/DJ/DI/DH/DG/DF/DE/DD/DB/DA/S/AX/T/U/AC/Q/R/O/A/D/P/Y/G/N |

**禁止**：把 DP 写成「DC / V / DK / DM / DN / DO / DL / DJ / DI / DH / DG / DF / DE / DD / DB / DA / S / AX / T / U / AC / Q / R / O / A / D / P 的续篇」；把「现货不征已诚实（DC）/ 股票印花切日已诚实（V）/ 基金印花已诚实（DK）/ 换股经手已分列（DM）/ 换股过户已分列（DN）/ 回售经手暂免已诚实（DO）」写成「可交换债换股印花已诚实」；把实验字母 DP 与单字母 D/P 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-P 读成双字母 DP**；**尤重勿把 `params.G` 读成实验字母 DP**；**尤重 `params.G` 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰（量纲与语义不同）**；**禁把占位读成 1‰/0.5‰/免费 0**；**尤重 DC 可转债现货印花误抽 ≠ 本页可交换换股印花误漏（现货不征≠换股应交；方向相反），禁止合成/混读升格进 `dp0`**；**尤重 V 股票二级印花切日 ≠ 本页换股业务类型，不重开假设-V，禁止合成/混读升格进 `dp0`**；**尤重 DK 场内基金印花误抽 ≠ 本页换股印花误漏，禁止合成/混读升格进 `dp0`**；**尤重 DM 换股经手 / DN 换股过户 ≠ 本页换股印花（经手≠过户≠印花三层分列），禁止合成/混读升格进 `dp0`**；**尤重 DO 回售经手暂免 ≠ 本页换股印花，禁止合成/混读升格进 `dp0`**；把 `invent_asof_leak_exchangeable_conversion_stamp` 升格进 `dp0` 或与主报双挂；把诊断桶 `invent_zero_stamp_on_exch_conversion` / `copy_DC_cb_spot_no_stamp_onto_conversion` / `confuse_with_stock_secondary_V` / `bilateral_or_buyer_side_stamp` / `ignore_20230828_half_cut` / `vs_DC_cb_spot_stamp` / `vs_V_ashare_stamp` / `vs_DK_fund_stamp` / `vs_DM_exch_conversion_handling` / `vs_DN_exch_conversion_transfer` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip` 升格进 `dp0`；把 DC 现货不征抄成换股免费 0；买卖双边或向受让方抽；把可转债转股在缺官方另档‰时仍硬填。本页主键只用 `dp0` / `dp1` / `dp2` 与 `exch_conversion_stamp_*`。不写下一字母。不预留 #126。**纸面齐惯例**：落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK/DL/DM/DN/DO；勿再只改清单）——**当前草稿阶段禁止标纸面齐**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权成交金额下，回测漏记可交换债**换股**印花税（结算表列征税、出让方），或把 DC 现货不征抄成换股免费 0，或与 V股票印花 / DK基金印花 / DM换股经手 / DN换股过户 / DO回售经手 混读，或缺 venue/业务类型/官方‰仍不 skip，相对「缺 venue/业务类型或官方‰则 skip；结算表列可交换公司债换股则征税、只向出让方；税率切片消费 V 口径但不重开 V；禁止把现货不征抄成换股免费 0；禁止买卖双边或向受让方抽；可转债转股缺官方另档‰则 skip」的诚实组，会**系统性改写换股腿印花成本**——相对诚实锚偏误。

核对日方向（随锚建议；**尚未冻，不要写成已冻**；禁止把 1‰ 或 0.5‰ 写成全历史唯一费率，也禁止把现货不征抄成换股免费 0，也禁止买卖双边或向受让方抽）：换股与现货分开，换股印花与换股经手、换股过户分开，换股与股票二级业务类型分开。结算代收表把可交换公司债换股列进印花税品种，向出让方征税。可转债现货不在这一栏，那是 DC 的「不征」，方向相反，不能抄成换股免费 0。税率切片消费 V 已有的出让方口径（法定 1‰，2023-08-28 起减半至 0.5‰），本页不重开 V，也不把这条切日升格成换股业务类型本身。可转债转股若没有官方另档‰，整腿 skip，不用换股行或股票二级行把转股腿填上。`事实与坑` 2026-11-09 已写：印花税品种含可交换公司债换股，没有可转债现货；换股/转股交割不要和现货捆成「都不抽」。那些现货「不征」留在 DC，股票切日留在 V，基金印花留在 DK，换股经手留在 DM，换股过户留在 DN，回售经手暂免留在 DO。**禁把占位读成 1‰/0.5‰/免费 0**。**`params.G` 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰**。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、漏记截在标定噪声带内可忽略，且「漏记换股印花 / 现货不征抄成免费 0 / 与股票二级混读 / 双边或向受让方抽 / 忽略减半切日 / 核对日泄露 / vs DC·V·DK·DM·DN·DO」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键占位（拉数前才冻结；本页不开跑；Y/G/N/Y2 · dp0 与锚 **三条尚未冻**）

```
# 配置写死键占位（见 §7；本页是草稿·待入库预检；下列三条尚未冻，不要写成已冻）
# 【消歧】params.Y = 显著性门槛；占位 0.02；尚未冻；**≠ 实验字母 DP ≠ 单字母假设-D / 假设-P**；勿把 params.Y 读成实验字母 DP
# 【消歧】params.G = 同族门槛；占位 0.01；尚未冻；**≠ 实验字母 DP ≠ 单字母 D/P**
# 【消歧】尤重：params.G 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰（量纲与语义不同：无量纲相对门槛 ≠ 印花税率）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成 1‰/0.5‰/免费 0（1‰ / 0.5‰ 若出现，只是消费 V 的切片，不是本页门槛；免费 0 是把 DC 现货不征抄错）
# 【消歧】params.N = 失败/废单率差门槛；占位 0.05；尚未冻；**≠ 实验字母 DP ≠ 单字母假设-N**
# params.Y2                               占位 0.015；尚未冻，不要写成已冻
# params.Y / G / N / Y2                   占位 0.02/0.01/0.05/0.015（相对门槛：成本差 / 漏记截 ΔExchConversionStamp / 净收益差 / DP1−DP2；**尚未冻，不要写成已冻**；**params.Y/G/N ≠ 实验字母 DP ≠ 单字母假设-D / 假设-P**；**尤重 params.G 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰**；**禁把占位读成 1‰/0.5‰/免费 0**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成印花税率或免费 0）
# params.fill_time                        建议 next_open；尚未冻，不要写成已冻
# params.asof_check_date                  建议 2026-10-16；尚未冻，不要写成已冻
# params.px_basis                         建议 unadj
# params.fail_policy                      建议 skip；尚未冻，不要写成已冻
# params.exch_conversion_stamp_honest     建议 pit_cs_table_lists_exch_conversion_charge_seller；尚未冻，不要写成已冻
#   诚实锚方向（建议，未冻；禁止把 1‰ 或 0.5‰ 写成全历史唯一费率；禁止把现货不征抄成换股免费 0）：
#   结算表列可交换公司债换股 → 征税、出让方
#   税率切片消费 V 口径，但不重开假设-V；换股业务类型 ≠ 股票二级
#   禁止把 DC/现货不征抄成换股免费 0（现货不征≠换股应交；方向相反）
#   禁止买卖双边或向受让方抽
#   可转债转股缺官方另档‰ → skip
#   缺 venue、业务类型或官方‰ → skip
#   枚举只是建议，尚未冻
#   不把 DC 的现货不征写成换股印花诚实锚
#   不把 V 的股票二级切日写成换股业务类型
#   不把 DK 的基金印花、DM 的换股经手、DN 的换股过户、DO 的回售经手写成换股印花
# params.exch_conversion_stamp_scope      建议 exchangeable_conversion_only_cb_spot_out_of_scope；尚未冻，不要写成已冻
#   方向名：只收可交换债换股；可转债现货不在本页范围
#   这不是把 1‰ / 0.5‰ 冻成全历史费率，也不是把现货不征冻成换股免费 0
#   可交换换股印花税误漏 ≠ DC转债现货印花 ≠ V股票印花切日 ≠ DM换股经手 ≠ DN换股过户
# params.exch_conversion_stamp_over_policy 建议 skip_if_venue_or_biz_type_or_official_bps_missing；尚未冻，不要写成已冻
#   缺 venue、业务类型或官方‰则 skip；禁在缺字段时仍按免费 0、双边、受让方或占位 0.01 把换股腿填上
# params.ashare_stamp_handoff             建议 v_page
#   消费 V 的股票印花税切日（出让方；法定 1‰；2023-08-28 起减半），或显式旁路；业务类型仍是换股，不是股票二级；不重开假设-V；不改 V
#   V 禁止合成/混读升格进 dp0；诊断桶 vs_V_ashare_stamp / confuse_with_stock_secondary_V / ignore_20230828_half_cut 不得升格进 dp0
# params.cb_spot_stamp_handoff            建议 dc_page
#   消费 DC 的可转债现货印花（现货不征），或显式旁路；现货不征 ≠ 换股应交；不重开假设-DC；不改 DC
#   DC 禁止合成/混读升格进 dp0；诊断桶 vs_DC_cb_spot_stamp / copy_DC_cb_spot_no_stamp_onto_conversion / invent_zero_stamp_on_exch_conversion 不得升格进 dp0
# params.fund_stamp_handoff               建议 dk_page
#   消费 DK 的场内基金印花税，或显式旁路；基金印花 ≠ 换股印花；不重开假设-DK；不改 DK
#   DK 禁止合成/混读升格进 dp0；诊断桶 vs_DK_fund_stamp 不得升格进 dp0
# params.exch_conversion_handling_handoff 建议 dm_page
#   消费 DM 的可交换债换股经手费，或显式旁路；经手 ≠ 印花；不重开假设-DM；不改 DM
#   DM 禁止合成/混读升格进 dp0；诊断桶 vs_DM_exch_conversion_handling 不得升格进 dp0
# params.exch_conversion_transfer_handoff 建议 dn_page
#   消费 DN 的可交换债换股过户费，或显式旁路；过户 ≠ 印花；不重开假设-DN；不改 DN
#   DN 禁止合成/混读升格进 dp0；诊断桶 vs_DN_exch_conversion_transfer 不得升格进 dp0
# params.cb_put_handling_handoff          建议 do_page
#   消费 DO 的可转债回售经手费暂免，或显式旁路；回售经手 ≠ 换股印花；不重开假设-DO；不改 DO
#   DO 禁止合成/混读升格进 dp0；诊断桶 vs_DO_cb_put_handling 不得升格进 dp0
# params.agreement_transfer_handoff       建议 dl_page
#   消费 DL 的股票综合协议过户费下浮，或显式旁路；不重开假设-DL；不改 DL
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
# params.cb_handling_fee_handoff          建议 db_page
#   消费 DB 的可转债现货经手费，或显式旁路；不重开假设-DB；不改 DB
# params.etf_transfer_fee_handoff         建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；不重开假设-DA；不改 DA
# params.ashare_fee_handoff               建议 s_page
#   消费 S 的沪深股票竞价经手费切日，或显式旁路；不重开假设-S；不改 S
# params.fund_handling_fee_handoff        建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；不改 AX
# params.stock_csrc_fee_handoff           建议 t_page
#   消费 T 的股票证管费，或显式旁路；不重开假设-T；不改 T
# params.stock_transfer_fee_handoff       建议 u_page
#   消费 U 的股票过户费切日，或显式旁路；不重开假设-U；不改 U
# params.bse_limit_aft_handoff            建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；不重开假设-AC；不改 AC
# params.cb_rule_handoff                  建议 q_page
#   可转债规则混用交 Q；回转/涨跌幅 ≠ 换股印花；不改 Q
# params.stock_etf_rotation_handoff       建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 换股印花；不重开假设-R；不改 R
# params.block_channel_handoff            建议 o_page
#   大宗通道交 O；不重开假设-O；不改 O
# params.board_capacity_handoff           建议 a_page
# params.fill_time_suspend_handoff        建议 d_page
#   成交时点与停牌交 D；双字母 DP ≠ 单字母假设-D；不改 D
# params.index_weight_handoff             建议 p_page
#   指数点位与权重交 P；双字母 DP ≠ 单字母假设-P；不改 P
# params.exch_conversion_stamp_handoff    建议 self
# params.dp0_primary_demo                 建议 invent_miss_stamp_on_exchangeable_conversion；尚未冻，不要写成已冻
#   单一主报，单挂；禁与 invent_asof_leak_exchangeable_conversion_stamp 双挂；DP1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_exchangeable_conversion_stamp 只作对照，不得升格进 dp0，不得双挂
#   诊断桶 invent_zero_stamp_on_exch_conversion / copy_DC_cb_spot_no_stamp_onto_conversion / confuse_with_stock_secondary_V / bilateral_or_buyer_side_stamp / ignore_20230828_half_cut / vs_DC_cb_spot_stamp / vs_V_ashare_stamp / vs_DK_fund_stamp / vs_DM_exch_conversion_handling / vs_DN_exch_conversion_transfer / vs_DO_cb_put_handling / missing_venue_or_biz_type_not_skip 不得升格进 dp0
#   尤重：禁止把 DC 现货不征与本页换股印花合成/混读后写进 dp0（现货不征≠换股应交；方向相反）
#   尤重：禁止把 V 股票二级印花切日与本页换股业务类型合成/混读后写进 dp0；不重开假设-V
#   尤重：禁止把 DK 基金印花与本页换股印花合成/混读后写进 dp0
#   尤重：禁止把 DM 换股经手、DN 换股过户与本页换股印花合成/混读后写进 dp0（经手≠过户≠印花）
#   尤重：禁止把 DO 回售经手暂免与本页换股印花合成/混读后写进 dp0
# params.dp0_invent_miss_stamp_on_exchangeable_conversion 建议 True
# params.dp1_asof_leak_exchangeable_conversion_stamp_only 建议 True
#   半泄露对照；DP1 不升格并列主报；不得把 invent_asof_leak_exchangeable_conversion_stamp 写进 dp0
# params.dp2_pit_cs_table_lists_exch_conversion_charge_seller 建议 True
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
# params.merge_with_P                     建议 False
# params.missing_venue_or_biz_type_or_official_bps_policy 建议 skip
# params.day_freq_proxy                   建议 exch_conversion_stamp_sensitivity
# params.universe_rule                    建议 exch_conversion_stamp_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dp_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DP；勿把这个键读成实验 DP，亦勿读成单字母 D/P
#   不另挂主报，不预留 #126，不写下一字母
```

### 2.2 三组对照（DP0 / DP1 / DP2）

组名 DP0 / DP1 / DP2 是本页三组，≠ 单字母实验 P（指数点位）。

| 组 | 角色 | 口径 |
|----|------|------|
| DP0 | 天真 / 换股印花误漏 | 按 `dp0_primary_demo` **建议**单一主报 `invent_miss_stamp_on_exchangeable_conversion`（单挂；**尚未冻，不要写成已冻**）：漏记可交换债换股印花（结算表本该征税、出让方）。**禁**与 `invent_asof_leak_exchangeable_conversion_stamp` 双挂主报。**禁把 DC 现货不征、V 股票二级印花切日、DK 基金印花、DM 换股经手、DN 换股过户、DO 回售经手合成进 `dp0`**（只作对照/旁路，不得升格进 `dp0` 或另挂主报） |
| DP1 | 半泄露 | 仅核对日把「换股征税、出让方、税率切片走 V」铺到全历史、铺到可转债现货、铺到可转债转股，或把现货不征抄成换股免费 0（`invent_asof_leak_exchangeable_conversion_stamp`）；**不得升格并列主报**，也不得写进 `dp0`（建议：DP1 不升格），不得双挂 |
| DP2 | 诚实 / 换股印花按结算表、出让方 | `exch_conversion_stamp_honest=pit_cs_table_lists_exch_conversion_charge_seller`（建议，**尚未冻**）：缺 venue/业务类型或官方‰则 skip；结算表列可交换公司债换股则征税、只向出让方；税率切片消费 V 口径但不重开 V；禁止把 DC 现货不征抄成换股免费 0；禁止买卖双边或向受让方抽；可转债转股缺官方另档‰则 skip。现货印花只消费 DC，股票印花切日只消费 V，基金印花只消费 DK，换股经手只消费 DM，换股过户只消费 DN，回售经手只消费 DO，或显式旁路 |

漏记换股印花、把现货不征抄成免费 0、把换股当成股票二级、买卖双边或向受让方抽、忽略 2023-08-28 减半、把 DC/V/DK/DM/DN/DO 混进换股印花，以及相对这些页的对照截（`invent_zero_stamp_on_exch_conversion` / `copy_DC_cb_spot_no_stamp_onto_conversion` / `confuse_with_stock_secondary_V` / `bilateral_or_buyer_side_stamp` / `ignore_20230828_half_cut` / `vs_DC_cb_spot_stamp` / `vs_V_ashare_stamp` / `vs_DK_fund_stamp` / `vs_DM_exch_conversion_handling` / `vs_DN_exch_conversion_transfer` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dp0_primary_demo`。`vs_DC_cb_spot_stamp` 只标记「有人把 DC 的现货不征和本页换股印花合成/混读」，**不得升格进 `dp0`**。`vs_V_ashare_stamp` 只标记股票二级对照，**不得升格进 `dp0`**。`vs_DK_fund_stamp` 只标记基金印花对照，**不得升格进 `dp0`**。`vs_DM_exch_conversion_handling` 只标记换股经手对照，**不得升格进 `dp0`**。`vs_DN_exch_conversion_transfer` 只标记换股过户对照，**不得升格进 `dp0`**。`vs_DO_cb_put_handling` 只标记回售经手对照，**不得升格进 `dp0`**。DC 的现货不征、V 的股票切日、DK 的基金印花、DM 的换股经手、DN 的换股过户、DO 的回售经手只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **建议** `2026-10-16`；fill_time **建议** `next_open`；fail **建议** `skip`。诚实锚六键与 Y/G/N/Y2、`dp0_primary_demo` 同属三条，**尚未冻，不要写成已冻**。机制红线只有一句：缺 venue/业务类型或官方‰则 skip；结算表列可交换公司债换股则征税、只向出让方；税率切片消费 V 口径但不重开 V；禁止把 DC 现货不征抄成换股免费 0；禁止买卖双边或向受让方抽；可转债转股缺官方另档‰则 skip。方向随锚建议：**不要把核对日税率铺满全历史，也不要把现货不征抄成换股免费 0，也不要双边或向受让方抽**。范围名 `exchangeable_conversion_only_cb_spot_out_of_scope` 只标方向：本页只看可交换债换股；可转债现货不在范围里，留给 DC。可转债转股没有官方另档‰就 skip，不升格进 `dp0`。`事实与坑` 2026-11-09 已写：结算表印花税品种含可交换公司债换股，没有可转债现货。1‰ 与 0.5‰ 是 V 的切片，本页不重开 V，也不把它们冻成自己的门槛。`params.G` 的 0.01 是无量纲相对门槛，不是印花 0.5‰，也不是法定 1‰。**禁把占位读成 1‰/0.5‰/免费 0**。缺 venue、业务类型或官方‰则 skip，不用免费 0、双边、受让方、自造‰或占位 0.01 把换股腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dp0_primary_demo` / `params.Y`·G·N·Y2 / 换股印花开关 / 桶 / 是否把税率或免费 0 铺到全历史、铺到现货或向受让方抽）。本页不开跑。三条都还没冻。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DP0）/ 半泄露组（DP1）相对诚实组（DP2）的成本差、漏记截**显著且集中在换股印花被漏记、或现货不征被抄成换股免费 0 的桶**；分桶「漏记 / 免费 0 / 与股票二级混读 / 双边或受让方 / 忽略减半 / 核对日泄露 / vs DC·V·DK·DM·DN·DO」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 1‰ 或 0.5‰ 冻成全历史唯一费率，也不把 `params.G` 的 0.01 读成印花税率。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 DC 的现货印花、V 的股票印花切日、DK 的基金印花、DM 的换股经手、DN 的换股过户、DO 的回售经手、DL 的综合协议过户、DJ 的基金证管费、DI 的大宗经手、DH 的佣金双计、DG 的北交所档、DF 的可交换现货经手、DE 的转债证管费、DD 的转债过户、DB 的转债现货经手、DA 的基金过户、S 的股票经手、AX 的基金经手费、T 的股票证管费、U 的股票过户、AC 的北交所涨跌幅与盘后、Q 的回转与涨跌幅、R 的股票 ETF 回转、O 的大宗通道、A 的板上容量、D 的成交时点、P 的指数权重解释；或 `dp0_primary_demo` 与 `invent_asof_leak_exchangeable_conversion_stamp` 双挂；或 DP1 升格并列主报；或 `invent_zero_stamp_on_exch_conversion` / `copy_DC_cb_spot_no_stamp_onto_conversion` / `confuse_with_stock_secondary_V` / `bilateral_or_buyer_side_stamp` / `ignore_20230828_half_cut` / `vs_DC_cb_spot_stamp` / `vs_V_ashare_stamp` / `vs_DK_fund_stamp` / `vs_DM_exch_conversion_handling` / `vs_DN_exch_conversion_transfer` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip` 诊断桶升格主报；或把 DC 现货不征、V 股票二级切日、DK 基金印花、DM 换股经手、DN 换股过户、DO 回售经手合成进 `dp0`；或实验字母 DP 与单字母 D/P 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成印花 0.5‰ 或法定 1‰；或把占位读成 1‰/0.5‰/免费 0；或把核对日税率写成已冻并铺满全历史；或缺 venue / 业务类型 / 官方‰仍不 skip；或买卖双边或向受让方抽；或重开假设-T / 假设-AC / 假设-R / 假设-U / 假设-O / 假设-DI / 假设-V / 假设-DF / 假设-DB / 假设-S / 假设-DD / 假设-DL / 假设-DM / 假设-DN / 假设-DO / 假设-DC / 假设-DK / 假设-DA；或标纸面齐；或写成 A/D–DP纸面齐；或把三条写成已冻。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DP0/DP1/DP2。现货印花走 DC 或显式旁路，不在本页改 DC，也不把 DC 的「不征」升成换股免费 0。股票印花切日走 V，基金印花走 DK，换股经手走 DM，换股过户走 DN，回售经手走 DO，都不改。报告成本差、漏记截。不把 1‰ 或 0.5‰ 标成已冻的全历史换股费率，也不把 `params.G` 的 0.01 读成印花税率。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_miss_stamp_on_exchangeable_conversion` / `invent_asof_leak_exchangeable_conversion_stamp` / `invent_zero_stamp_on_exch_conversion` / `copy_DC_cb_spot_no_stamp_onto_conversion` / `confuse_with_stock_secondary_V` / `bilateral_or_buyer_side_stamp` / `ignore_20230828_half_cut` / `vs_DC_cb_spot_stamp` / `vs_V_ashare_stamp` / `vs_DK_fund_stamp` / `vs_DM_exch_conversion_handling` / `vs_DN_exch_conversion_transfer` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip`

`invent_zero_stamp_on_exch_conversion`、`copy_DC_cb_spot_no_stamp_onto_conversion`、`confuse_with_stock_secondary_V`、`bilateral_or_buyer_side_stamp`、`ignore_20230828_half_cut`、`vs_DC_cb_spot_stamp`、`vs_V_ashare_stamp`、`vs_DK_fund_stamp`、`vs_DM_exch_conversion_handling`、`vs_DN_exch_conversion_transfer`、`vs_DO_cb_put_handling`、`missing_venue_or_biz_type_not_skip` 只作诊断桶：它们不是 `dp0`，也不是 DP1，**不得升格主报**。`vs_DC_cb_spot_stamp` 没有对应的「现货不征 + 换股免费 0」合成主报。DC 的现货不征只作诊断，**不得与换股印花合成后升格进 `dp0`**。V 的股票二级切日只作诊断，**不得升格进 `dp0`**。DK 的基金印花只作诊断，**不得升格进 `dp0`**。DM 的换股经手、DN 的换股过户只作诊断，**不得升格进 `dp0`**。DO 的回售经手只作诊断，**不得升格进 `dp0`**。写成免费 0、双边或向受让方抽、忽略减半切日、缺字段仍不 skip，都只作诊断，**不得升格进 `dp0`**。`invent_asof_leak_exchangeable_conversion_stamp` 只服务 DP1，**不得升格进 `dp0`，不得双挂**。`invent_miss_stamp_on_exchangeable_conversion` 才是建议的单一主报名，**尚未冻**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把漏记可交换债换股印花、或把现货不征抄成换股免费 0，并拿去当诚实锚。
- 把 `params.G` 的 0.01 当成印花 0.5‰ 或法定 1‰。**尤重：`params.G` 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 1‰/0.5‰/免费 0。**禁把占位读成 1‰/0.5‰/免费 0**。
- 缺 venue、业务类型或官方‰仍不 skip，并用免费 0、双边、受让方、自造‰或占位 0.01 把换股腿填上。
- 把核对日「换股征税、出让方」写成全历史唯一费率，并铺满全历史，或把现货不征抄成换股免费 0，或买卖双边，或向受让方抽。锚六键仍是建议，**尚未冻**。
- 可转债转股没有官方另档‰仍硬填一档（含把换股行或股票二级行抄成转股）。
- 把「现货不征已诚实（DC）/ 股票印花切日已诚实（V）/ 基金印花已诚实（DK）/ 换股经手已分列（DM）/ 换股过户已分列（DN）/ 回售经手暂免已诚实（DO）」写成「可交换债换股印花已诚实」。不改 DC / V / DK / DM / DN / DO。
- 把 DC 的现货不征和本页换股印花合成或混读后升格进 `dp0`。诊断桶 `vs_DC_cb_spot_stamp` / `copy_DC_cb_spot_no_stamp_onto_conversion` / `invent_zero_stamp_on_exch_conversion` 只作对照。现货不征≠换股应交，方向相反。
- 把 V 股票二级印花切日和本页换股业务类型合成或混读后升格进 `dp0`。诊断桶 `vs_V_ashare_stamp` / `confuse_with_stock_secondary_V` / `ignore_20230828_half_cut` 只作对照。不重开假设-V。
- 把 DK 基金印花和本页换股印花合成或混读后升格进 `dp0`。诊断桶 `vs_DK_fund_stamp` 只作对照。
- 把 DM 换股经手、DN 换股过户和本页换股印花合成或混读后升格进 `dp0`。诊断桶 `vs_DM_exch_conversion_handling` / `vs_DN_exch_conversion_transfer` 只作对照。经手≠过户≠印花。
- 把 DO 回售经手暂免和本页换股印花合成或混读后升格进 `dp0`。诊断桶 `vs_DO_cb_put_handling` 只作对照。
- 买卖双边或向受让方抽，并升格进 `dp0`。诊断桶 `bilateral_or_buyer_side_stamp` 只作对照。
- 缺 venue 或业务类型仍不 skip，并升格进 `dp0`。诊断桶 `missing_venue_or_biz_type_not_skip` 只作对照。
- `dp0_primary_demo` 与 `invent_asof_leak_exchangeable_conversion_stamp` 双挂主报；DP1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DP 与单字母 D/P 或 params.Y/G/N 混读。
- 改 DC / V / DK / DM / DN / DO / DL / DJ / DI / DH / DG / DF / DE / DD / DB / DA / S / AX / T / U / AC / Q / R / O / A / D / P 正文；重开假设-T；重开假设-AC；重开假设-R；重开假设-U；重开假设-O；重开假设-DI；重开假设-V；重开假设-DF；重开假设-DB；重开假设-S；重开假设-DD；重开假设-DL；重开假设-DM；重开假设-DN；重开假设-DO；重开假设-DC；重开假设-DK；重开假设-DA；抢 A 真数队列；标纸面齐；写成 A/D–DP纸面齐；把三条写成已冻；开真数/回测/实盘；用复权价当费用基数；结论写成「换股税更低所以能买」。
- **纸面齐惯例**：落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK/DL/DM/DN/DO；勿再只改清单）——**当前草稿阶段禁止标纸面齐**。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权成交金额、交易日、**交易所 venue**（沪/深）、**业务类型**（可交换债换股 / 可转债现货 / 可转债转股 / 股票二级 / 场内基金 / 可转债回售；仅用于把腿分回 DC、V、DK、DM、DN、DO 或本页）、**买卖方向或出让/受让**（只向出让方；受让方不抽）、**官方换股印花‰是否在册**（缺则 skip，不发明数，也不填免费 0）。
- 税率切片若要数字，只消费 V 已有口径，不在本页重开 V，也不把股票二级业务类型换成换股。
- 可转债转股若没有官方另档‰，整腿 skip。不拿换股行或股票二级行代替。
- 证券类别只用于把腿分回 DC / V / DK / DM / DN / DO 等旁路页，不在本页改那些页。
- 没有 venue、业务类型或官方‰时，按建议的 `exch_conversion_stamp_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing` skip，不得按免费 0 把换股腿填上，也不得双边或向受让方抽，或把占位 0.01 当成费率。
- 旁路消费：DC 的转债现货印花、V 的股票印花切日、DK 的基金印花、DM 的换股经手、DN 的换股过户、DO 的回售经手、DL 的综合协议过户下浮、DJ 的基金证管费、DI 的大宗经手、DH 的佣金双计、DG 的北交所经手费、DF 的可交换现货经手、DE 的转债证管费、DD 的转债过户、DB 的转债现货经手、DA 的基金过户、S 的股票经手切日、AX 的基金经手费、T 的股票证管费、U 的股票过户费、AC 的北交所涨跌幅与盘后、Q 的转债规则、R 的股票 ETF 回转、O 的大宗通道、D 的成交时点、P 的指数权重之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** DC 的现货不征、V 的股票切日、DK 的基金印花、DM 的换股经手、DN 的换股过户、DO 的回售经手不收到本页主报。
- 未复权价；asof **建议** `2026-10-16`，**尚未冻**。核对日方向「换股征税、出让方；现货不征不抄过来；转股缺官方‰则 skip」是建议的机制方向，不是已冻全历史费率。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **占位键摘要（三条尚未冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`exch_conversion_stamp_honest=pit_cs_table_lists_exch_conversion_charge_seller`（结算表列可交换公司债换股则征税、出让方；税率切片消费 V 口径但不重开 V；**禁止把 DC 现货不征抄成换股免费 0**；**禁止买卖双边或向受让方抽**；可转债转股缺官方另档‰则 skip；**禁止把 1‰ 或 0.5‰ 写成全历史唯一费率**；**尚未冻**）；`exch_conversion_stamp_scope=exchangeable_conversion_only_cb_spot_out_of_scope`（只收可交换债换股，可转债现货不在范围；方向名，不是已冻费率）；`exch_conversion_stamp_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing`（缺 venue/业务类型或官方‰则 skip）；`dp0_primary_demo=invent_miss_stamp_on_exchangeable_conversion`（**建议**单一主报，单挂；**尚未冻**；禁与 `invent_asof_leak_exchangeable_conversion_stamp` 双挂；DP1 不升格；诊断桶不升格主报；**禁把 DC 现货不征、V 股票二级印花切日、DK 基金印花、DM 换股经手、DN 换股过户、DO 回售经手合成进 `dp0`**，只作对照/旁路，不得升格进 `dp0` 或另挂主报）；`ashare_stamp_handoff=v_page`；`cb_spot_stamp_handoff=dc_page`；`fund_stamp_handoff=dk_page`；`exch_conversion_handling_handoff=dm_page`；`exch_conversion_transfer_handoff=dn_page`；`cb_put_handling_handoff=do_page`；`merge_with_DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/A/D/P=False`。
- `params.Y/G/N/Y2` **占位** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 漏记截 ΔExchConversionStamp / 净收益差 / DP1−DP2；**尚未冻，不要写成已冻**；**尤重 params.G 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰（量纲与语义不同）**；**禁把占位读成 1‰/0.5‰/免费 0**；**params.Y/G/N ≠ 实验字母 DP ≠ 单字母 D/P**；**勿把 params.G 读成实验字母 DP，亦勿把单字母假设-D / 假设-P 读成双字母 DP**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成印花税率或免费 0）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #126。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`c786804e`（A/D–DO纸面齐已合，全长 `c786804e28642c55521ac706825ffff78d728a47`）。**不改已冻 A–DO / DA–DN**。状态=**草稿·待入库预检**。**三条尚未冻**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DP纸面齐**。

---

## 8. 结论

（空）

---

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-20 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。可交换债换股印花税误漏；`dp0_primary_demo` 建议 `invent_miss_stamp_on_exchangeable_conversion`，单一主报，单挂，禁与 `invent_asof_leak_exchangeable_conversion_stamp` 双挂，DP1 不升格；诊断桶 `invent_zero_stamp_on_exch_conversion` / `copy_DC_cb_spot_no_stamp_onto_conversion` / `confuse_with_stock_secondary_V` / `bilateral_or_buyer_side_stamp` / `ignore_20230828_half_cut` / `vs_DC_cb_spot_stamp` / `vs_V_ashare_stamp` / `vs_DK_fund_stamp` / `vs_DM_exch_conversion_handling` / `vs_DN_exch_conversion_transfer` / `vs_DO_cb_put_handling` / `missing_venue_or_biz_type_not_skip` 不升格；**尤重 DC 可转债现货印花误抽 ≠ 本页可交换换股印花误漏（现货不征≠换股应交；方向相反），禁止合成/混读升格进 dp0**；**尤重 V 股票二级印花切日 ≠ 本页换股业务类型，不重开假设-V，禁止合成进 dp0**；**尤重 DK 场内基金印花误抽 ≠ 本页换股印花误漏，禁止合成进 dp0**；**尤重 DM 换股经手 / DN 换股过户 ≠ 本页换股印花（经手≠过户≠印花三层分列），禁止合成进 dp0**；**尤重 DO 回售经手暂免 ≠ 本页换股印花，禁止合成进 dp0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DP ≠ 单字母 D/P**，且 **params.G 的 0.01 ≠ 印花 0.5‰ ≠ 法定 1‰**，**禁把占位读成 1‰/0.5‰/免费 0**；锚建议、未冻：`exch_conversion_stamp_honest=pit_cs_table_lists_exch_conversion_charge_seller` / scope=`exchangeable_conversion_only_cb_spot_out_of_scope` / over_policy=`skip_if_venue_or_biz_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`；口径：缺 venue/业务类型或官方‰则 skip；结算表列可交换公司债换股→征税、出让方；税率切片消费 V 口径但不重开 V；禁止把 DC/现货不征抄成换股免费 0；禁止买卖双边或向受让方抽；可转债转股缺官方另档‰则 skip（**草稿方向，尚未冻，不要写成已冻**）；handoff：`ashare_stamp_handoff=v_page`，`cb_spot_stamp_handoff=dc_page`，`fund_stamp_handoff=dk_page`，`exch_conversion_handling_handoff=dm_page`，`exch_conversion_transfer_handoff=dn_page`，`cb_put_handling_handoff=do_page`；`merge_with_DO/DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/A/D/P=False`；**DP≠DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D**；**双字母 DP ≠ 单字母假设-D / 假设-P**；**可交换换股印花税误漏 ≠ DC转债现货印花 ≠ V股票印花切日 ≠ DM换股经手 ≠ DN换股过户**；**未标纸面齐**；**不写 A/D–DP纸面齐**；**纸面齐惯例**：落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK/DL/DM/DN/DO；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DO / DA–DN；不改已齐假设-DA～假设-DO；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-U；不重开假设-O；不重开假设-DI；不重开假设-V；不重开假设-DF；不重开假设-DB；不重开假设-S；不重开假设-DD；不重开假设-DL；不重开假设-DM；不重开假设-DN；不重开假设-DO；不重开假设-DC；不重开假设-DK；不重开假设-DA；不写下一字母；不预留 #126；不开真数/回测/实盘。基 tip=`c786804e`（A/D–DO纸面齐已合，全长 `c786804e28642c55521ac706825ffff78d728a47`；不改该 tip 上的 #110–#124，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
