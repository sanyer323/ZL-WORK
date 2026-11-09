# 假设-DO · 可转债回售经手费暂免误忽略（成本诚信）

更新：2026-11-16  
来源：总管线 / 默认分支 HEAD `6d1a93d2` 上清单 #123=DN 已收口（A/D–DN纸面齐已合入该 tip；全长 `6d1a93d22d03dfeccb1807506904666b07d88b79`；**不改已冻 A–DN / DA–DM**；**不改假设-DN 正文**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-DL / 假设-DM / 假设-S / 假设-AX / 假设-T / 假设-U / 假设-V / 假设-AC / 假设-Q / 假设-R / 假设-A / 假设-D / 假设-O / 假设-N 及其他已存在假设页；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DA**）后写下一草稿 DO；清单 #123=DN，本页占用 **#124=DO**；选题是沪市可转债**回售**经手费暂免窗被忽略，把现货档 0.004% 铺到回售腿；假设-DB 只收可转债**现货**经手费（现货 ≠ 回售），假设-DF 只收可交换债现货经手费沪深分列，假设-DM 只收可交换债换股经手费，假设-S 只收股票经手费切日，假设-DI 只收股票大宗经手下浮，假设-DN 只收可交换债换股过户费；**新建实验 DO**；不写下一字母；不预留 #125  
状态：**预检有条件通过·三条已冻·待复检**（结论栏空；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DO纸面齐**；禁止把「忽略回售暂免、把现货档 0.004% 铺到回售」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改已冻 A–DN / DA–DM**；尤其不改假设-DB / 假设-DF / 假设-DM / 假设-S / 假设-DI / 假设-DN / 假设-DL / 假设-T / 假设-AC / 假设-R / 假设-U / 假设-O / 假设-V / 假设-DD / 假设-DA / 假设-D；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DA**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DO（#124）。一句话误开：回测忽略沪市可转债**回售**经手费暂免窗，把现货档 0.004% 铺到回售腿，或与 DB现货经手 / DF/DM可交换经手 / S股票经手 / DI大宗经手 混读，或缺 venue/业务类型/官方‰仍不 skip，系统性改写回售腿成本。

> **字母消歧（硬）**：本页**实验字母 DO** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DO**；**勿把 `params.Y` 读成实验字母 DO**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DO**；**尤重：`params.G` 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是转债现货经手费率，也不是回售暂免；现货档 0.004% = 0.04‰ 留在 DB，不是本页回售暂免；**禁把占位读成 0.004%/0.04‰/暂免**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DO**；**params.N ≠ 单字母假设-N**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DO ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 O**（大宗假流动性；**双字母 DO ≠ 单字母假设-O；严禁复用假设-O**；组名 DO0/DO1/DO2 是本页三组对照，≠ 单字母实验 O）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DO ≠ 单字母假设-A**）≠ 双字母 **DN**（可交换债换股过户费误套）≠ **DM**（可交换债换股经手费误套现货）≠ **DL**（股票综合协议过户费下浮）≠ **DK**（场内基金印花税）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债现货经手费沪深合成）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债现货经手费）≠ **DA**（场内基金过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费）≠ **T**（股票证管费）≠ **U**（股票过户费）≠ **V**（股票印花税）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）。**DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D**。**双字母 DO ≠ 单字母 D/O**。**params.Y/G/N ≠ 实验字母 DO；亦 ≠ 单字母 D/O**。**勿把 `params.G` 读成实验字母 DO，亦勿把单字母假设-D / 假设-O 读成双字母 DO**。**尤重：`params.G` 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免**。**禁把占位读成 0.004%/0.04‰/暂免**。**可转债回售经手费暂免误忽略 ≠ DB转债现货经手 ≠ DM换股经手 ≠ DN换股过户**。**尤重：DB 可转债现货经手费 ≠ 本页回售经手费暂免（现货≠回售）——禁止合成/混读升格进 `do0`**。**尤重：DF/DM 可交换现货/换股经手 ≠ 本页转债回售——禁止合成/混读升格进 `do0`**。**尤重：S 股票经手切日 ≠ 本页回售另档——禁止合成/混读升格进 `do0`**。**尤重：DI 大宗经手下浮 ≠ 本页回售暂免——禁止合成/混读升格进 `do0`**。

### 专节 · 双字母 DO ≠ 单字母假设-D / 假设-O；且 ≠ 假设-DB / 假设-DF / 假设-DM / 假设-S / 假设-DI / 假设-DN / 假设-DL（硬）

| 维度 | 对照页 | 本页假设-DO（双字母） |
|------|--------|----------------------|
| 题面 DB | **可转债现货经手费**（现货竞价等；核对日现货仍收 0.004% = 0.04‰；现货 ≠ 回售） | 现货经手费 ≠ 本页回售经手费暂免。**现货≠回售**。**DO≠DB**；**严禁复用假设-DB**；**不重开假设-DB**；**不改 DB**；**尤重：DB 可转债现货经手费 ≠ 本页回售经手费暂免（现货≠回售）——禁止合成/混读升格进 `do0`**；`cb_handling_fee_handoff=db_page`；诊断桶 `vs_DB_cb_spot_handling` / `confuse_DB_spot_with_put` / `copy_spot_004_onto_put` 不升格 |
| 题面 DF | **可交换债现货经手费沪深合成**（沪市现货暂免与深市 0.04‰ 分列；可交换现货 ≠ 转债回售） | 可交换现货经手 ≠ 本页转债回售。**DO≠DF**；**严禁复用假设-DF**；**不重开假设-DF**；**不改 DF**；**尤重：DF 可交换现货经手 ≠ 本页转债回售——禁止合成/混读升格进 `do0`**；`exch_spot_handling_handoff=df_page`；诊断桶 `vs_DF_exch_spot_handling` 不升格 |
| 题面 DM | **可交换债换股经手费误套现货**（换股经手与现货分开） | 换股经手 ≠ 本页转债回售。**DO≠DM**；**严禁复用假设-DM**；**不重开假设-DM**；**不改 DM**；**尤重：DM 换股经手 ≠ 本页转债回售——禁止合成/混读升格进 `do0`**；`exch_conversion_handling_handoff=dm_page`；诊断桶 `vs_DM_exch_conversion_handling` 不升格 |
| 题面 S | **沪深 A 股竞价经手费切日**（股票三切日；不是回售另档） | 股票经手切日 ≠ 回售另档。**DO≠S**；**严禁复用假设-S**；**不重开假设-S**；**不改 S**；**尤重：S 股票经手切日 ≠ 本页回售另档——禁止合成/混读升格进 `do0`**；`ashare_fee_handoff=s_page`；诊断桶 `vs_S_stock_handling` 不升格 |
| 题面 DI | **股票大宗经手下浮**（相对竞价经手再下浮；经手下浮 ≠ 回售暂免） | 大宗经手下浮 ≠ 回售暂免。**DO≠DI**；**严禁复用假设-DI**；**不重开假设-DI**；**不改 DI**；**尤重：DI 大宗经手下浮 ≠ 本页回售暂免——禁止合成/混读升格进 `do0`**；`stock_block_handling_handoff=di_page`；诊断桶 `vs_DI_block_handling` 不升格 |
| 题面 DN | **可交换债换股过户费**（过户 ≠ 经手；换股过户 ≠ 转债回售） | 换股过户 ≠ 回售经手暂免。**经手≠过户**。**DO≠DN**；**严禁复用假设-DN**；**不重开假设-DN**；**不改 DN**；`exch_conversion_transfer_handoff=dn_page` |
| 题面 DL | **股票综合协议过户费下浮**（过户下浮 ≠ 回售经手暂免） | 综合协议过户下浮 ≠ 回售经手。**DO≠DL**；**严禁复用假设-DL**；**不重开假设-DL**；**不改 DL**；`agreement_transfer_handoff=dl_page` |
| 题面 DK | **场内基金印花税** | 基金印花 ≠ 回售经手费。**DO≠DK**；**不改 DK**；`fund_stamp_handoff=dk_page` |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 本机制。**DO≠DJ**；**不改 DJ**；`fund_csrc_fee_handoff=dj_page` |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 回售经手暂免。**DO≠DH**；**不改 DH**；`commission_double_handoff=dh_page` |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 本机制。**DO≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 回售经手费。**DO≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债现货过户费** | 转债过户 ≠ 回售经手。过户≠经手。**DO≠DD**；**严禁复用假设-DD**；**不重开假设-DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DC | **可转债印花税** | 转债印花税 ≠ 本机制。**DO≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 DA | **场内基金过户费** | 基金过户 ≠ 回售经手。**DO≠DA**；**严禁复用假设-DA**；**不重开假设-DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 本机制。**DO≠AX**；**不改 AX**；`fund_handling_fee_handoff=ax_page` |
| 题面 T | **证管费主报股票** | 股票证管费 ≠ 回售经手费。**DO≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日** | 股票过户切日 ≠ 回售经手。**DO≠U**；**严禁复用假设-U**；**不重开假设-U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 V | **股票印花税切日** | 印花税 ≠ 回售经手费。**DO≠V**；**严禁复用假设-V**；**不重开假设-V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 回售经手费。**DO≠AC**；**不改 AC**；**不重开假设-AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 本机制。回转/涨跌幅 ≠ 回售经手暂免。**DO≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 本机制。**DO≠R**；**不改 R**；**不重开假设-R**；`stock_etf_rotation_handoff=r_page` |
| 题面 O | **大宗通道 / 假流动性** | 大宗通道 ≠ 回售经手暂免。**双字母 DO ≠ 单字母假设-O**；**不重开假设-O**；**不改 O**；`block_channel_handoff=o_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 回售经手费。**DO≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 回售经手费抽在哪一档。**双字母 DO ≠ 单字母假设-D**；**严禁复用假设-D**；**DO≠D**；**不改 D** |
| 题面 CR | **可转债赎回/回售行权可成交性**（能不能按行权价兑付；不是经手费） | 回售能不能成交 ≠ 回售经手费暂免。**DO≠CR**；**不改 CR**；`cb_call_put_fill_handoff=cr_page`；可成交性不升格进 `do0` |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_full_handling_fee_on_cb_put`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_cb_put_handling` 双挂；DO1 不升格；`ignore_sse_put_waiver_window` / `copy_spot_004_onto_put` / `merge_sse_szse_put_handling` / `confuse_DB_spot_with_put` / `vs_DB_cb_spot_handling` / `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` / `vs_S_stock_handling` / `vs_DI_block_handling` / `missing_venue_or_biz_type_not_skip` 只作诊断对照，不升格主报；**尤重禁止把 DB 现货经手、DF 可交换现货经手、DM 换股经手、S 股票经手切日、DI 大宗经手下浮合成进 `do0`**） |
| 文档 | 清单实验 DB / DF / DM / S / DI / DN / DL / DK / DJ / DH / DG / DE / DD / DC / DA / AX / T / U / V / AC / Q / R / O / A / D（**只读；禁止改写**） | `假设-DO-可转债回售经手费暂免误忽略.md`（新建） |
| 预检键 | 实验字母 DB / DF / DM / S / DI / DN / DL / DK / DJ / DH / DG / DE / DD / DC / DA / AX / T / U / V / AC / Q / R / O / A / D / Y / G / N | 实验字母 **DO** / `do0_primary_demo`；**不得**占用或改写预检 DB/DF/DM/S/DI/DN/DL/DK/DJ/DH/DG/DE/DD/DC/DA/AX/T/U/V/AC/Q/R/O/A/D/Y/G/N |

**禁止**：把 DO 写成「DB / DF / DM / S / DI / DN / DL / DK / DJ / DH / DG / DE / DD / DC / DA / AX / T / U / V / AC / Q / R / O / A / D 的续篇」；把「现货经手已诚实（DB）/ 可交换现货经手已分列（DF）/ 换股经手已分列（DM）/ 股票经手切日已诚实（S）/ 大宗经手下浮已诚实（DI）/ 换股过户已分列（DN）」写成「可转债回售经手费暂免已诚实」；把实验字母 DO 与单字母 D/O 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-O 读成双字母 DO**；**尤重勿把 `params.G` 读成实验字母 DO**；**尤重 `params.G` 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免（量纲与语义不同）**；**禁把占位读成 0.004%/0.04‰/暂免**；**尤重 DB 可转债现货经手费 ≠ 本页回售经手费暂免（现货≠回售），禁止合成/混读升格进 `do0`**；**尤重 DF/DM 可交换现货/换股经手 ≠ 本页转债回售，禁止合成/混读升格进 `do0`**；**尤重 S 股票经手切日 ≠ 本页回售另档，禁止合成/混读升格进 `do0`**；**尤重 DI 大宗经手下浮 ≠ 本页回售暂免，禁止合成/混读升格进 `do0`**；把 `invent_asof_leak_cb_put_handling` 升格进 `do0` 或与主报双挂；把诊断桶 `ignore_sse_put_waiver_window` / `copy_spot_004_onto_put` / `merge_sse_szse_put_handling` / `confuse_DB_spot_with_put` / `vs_DB_cb_spot_handling` / `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` / `vs_S_stock_handling` / `vs_DI_block_handling` / `missing_venue_or_biz_type_not_skip` 升格进 `do0`；把现货档 0.004% 铺到回售；沪深回售经手合成一句。本页主键只用 `do0` / `do1` / `do2` 与 `cb_put_handling_*`。不写下一字母。不预留 #125。**纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK/DL/DM/DN；勿再只改清单）。**当前禁止标纸面齐**。**不写 A/D–DO纸面齐**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权成交金额下，回测忽略沪市可转债**回售**经手费暂免窗，把现货档 0.004% 铺到回售腿，或与 DB现货经手 / DF/DM可交换经手 / S股票经手 / DI大宗经手 混读，或缺 venue/业务类型/官方‰仍不 skip，相对「缺 venue/业务类型或官方‰则 skip；沪市核对日回售在暂免窗内按表暂免、现货仍收 0.004%，禁止把现货档铺到回售；深市缺官方回售另档‰则 skip」的诚实组，会**系统性改写回售腿成本**——相对诚实锚偏误。

核对日方向（随锚写死；禁止把暂免或 0.004% 写成全历史唯一费率，也禁止把现货档铺到回售，也禁止沪深合成一句）：沪市回售与现货分开，沪市与深市分开。核对日方向是沪市上市公司可转债回售经手费在 2022-07-01 至 2026-12-31 暂免窗内按表暂免，现货竞价仍收 0.004%（= 0.04‰）。这不是把现货档铺到回售腿。深市没有官方回售另档‰，缺了就 skip，不拿现货 0.04‰ 或沪市暂免把深市回售腿填上。`事实与坑` 2026-11-06 已写这张表：回售在暂免栏，现货不在。那些现货数字留在 DB，本页不重开 DB。**禁把占位读成 0.004%/0.04‰/暂免**。**`params.G` 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免**。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误套截在标定噪声带内可忽略，且「忽略暂免窗 / 现货 0.004% 铺到回售 / 沪深回售合成一句 / DB 现货混进回售 / 核对日泄露 / vs DB·DF·DM·S·DI」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · do0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结；禁止标纸面齐；不写 A/D–DO纸面齐）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DO ≠ 单字母假设-D / 假设-O**；勿把 params.Y 读成实验字母 DO
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DO ≠ 单字母 D/O**
# 【消歧】尤重：params.G 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免（量纲与语义不同：无量纲相对门槛 ≠ 现货经手费率‰ ≠ 回售暂免）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成 0.004%/0.04‰/暂免（0.004% = 0.04‰ 是 DB 现货档，暂免是回售窗，都不是本页门槛）
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DO ≠ 单字母假设-N**
# params.Y2                               写死冻结 0.015
# params.Y / G / N / Y2                   写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误套截 ΔCbPutHandling / 净收益差 / DO1−DO2；**params.Y/G/N ≠ 实验字母 DO ≠ 单字母假设-D / 假设-O**；**尤重 params.G 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免**；**禁把占位读成 0.004%/0.04‰/暂免**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成回售经手费率或现货档）
# params.fill_time                        写死冻结 next_open
# params.asof_check_date                  写死冻结 2026-10-16
# params.px_basis                         建议 unadj
# params.fail_policy                      写死冻结 skip
# params.cb_put_handling_honest           写死冻结 pit_sse_put_waived_spot_still_charged
#   诚实锚方向（已写死冻结；禁止把暂免或 0.004% 写成全历史唯一费率；禁止把现货档铺到回售）：
#   沪市回售与现货分列；沪市与深市分列
#   沪市核对日：上市公司可转债回售在暂免窗 2022-07-01 至 2026-12-31 内按表暂免
#   现货仍收 0.004%（= 0.04‰），禁止把现货档铺到回售
#   深市缺官方回售另档‰ → skip
#   缺 venue、业务类型或官方‰ → skip
#   枚举已写死冻结
#   不把 DB 的现货经手写成回售暂免诚实锚（现货≠回售）
#   不把 DF 的可交换现货经手、DM 的换股经手写成转债回售
#   不把 S 的股票经手切日写成回售另档
#   不把 DI 的大宗经手下浮写成回售暂免
# params.cb_put_handling_scope            写死冻结 sse_put_waiver_20220701_20261231_szse_listed_apart
#   方向名：沪市回售暂免窗与深市分列，不合成一句
#   这不是把暂免或 0.004% 冻成全历史费率
#   可转债回售经手费暂免误忽略 ≠ DB转债现货经手 ≠ DM换股经手 ≠ DN换股过户
# params.cb_put_handling_over_policy      写死冻结 skip_if_venue_or_biz_type_or_official_bps_missing
#   缺 venue、业务类型或官方‰则 skip；禁在缺字段时仍按现货档 0.004% 或沪深合成一句把回售腿填上
# params.cb_handling_fee_handoff          建议 db_page
#   消费 DB 的可转债现货经手费，或显式旁路；现货 ≠ 回售；不重开假设-DB；不改 DB
#   DB 禁止合成/混读升格进 do0；诊断桶 vs_DB_cb_spot_handling / confuse_DB_spot_with_put / copy_spot_004_onto_put 不得升格进 do0
# params.exch_spot_handling_handoff       建议 df_page
#   消费 DF 的可交换现货经手费沪深分列，或显式旁路；可交换现货 ≠ 转债回售；不重开假设-DF；不改 DF
#   DF 禁止合成/混读升格进 do0；诊断桶 vs_DF_exch_spot_handling 不得升格进 do0
# params.exch_conversion_handling_handoff 建议 dm_page
#   消费 DM 的可交换债换股经手费，或显式旁路；换股经手 ≠ 转债回售；不重开假设-DM；不改 DM
#   DM 禁止合成/混读升格进 do0；诊断桶 vs_DM_exch_conversion_handling 不得升格进 do0
# params.ashare_fee_handoff               建议 s_page
#   消费 S 的沪深股票竞价经手费切日，或显式旁路；股票经手切日 ≠ 回售另档；不重开假设-S；不改 S
#   S 禁止合成/混读升格进 do0；诊断桶 vs_S_stock_handling 不得升格进 do0
# params.stock_block_handling_handoff     建议 di_page
#   消费 DI 的股票大宗经手下浮，或显式旁路；大宗经手下浮 ≠ 回售暂免；不重开假设-DI；不改 DI
#   DI 禁止合成/混读升格进 do0；诊断桶 vs_DI_block_handling 不得升格进 do0
# params.exch_conversion_transfer_handoff 建议 dn_page
#   消费 DN 的可交换债换股过户费，或显式旁路；换股过户 ≠ 回售经手；经手≠过户；不重开假设-DN；不改 DN
# params.agreement_transfer_handoff       建议 dl_page
#   消费 DL 的股票综合协议过户费下浮，或显式旁路；不重开假设-DL；不改 DL
# params.fund_stamp_handoff               建议 dk_page
#   消费 DK 的场内基金印花税，或显式旁路；不改 DK
# params.fund_csrc_fee_handoff            建议 dj_page
#   消费 DJ 的场内基金证管费，或显式旁路；不改 DJ
# params.commission_double_handoff        建议 dh_page
#   消费 DH 的佣金双计，或显式旁路；不改 DH
# params.bse_fee_handoff                  建议 dg_page
#   消费 DG 的北交所经手费档，或显式旁路；不改 DG
# params.cb_csrc_fee_handoff              建议 de_page
#   消费 DE 的转债证管费，或显式旁路；不改 DE
# params.cb_transfer_fee_handoff          建议 dd_page
#   消费 DD 的可转债现货过户费，或显式旁路；过户 ≠ 回售经手；不重开假设-DD；不改 DD
# params.cb_stamp_handoff                 建议 dc_page
#   消费 DC 的可转债印花税，或显式旁路；不改 DC
# params.etf_transfer_fee_handoff         建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；不重开假设-DA；不改 DA
# params.fund_handling_fee_handoff        建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；不改 AX
# params.stock_csrc_fee_handoff           建议 t_page
#   消费 T 的股票证管费，或显式旁路；不重开假设-T；不改 T
# params.stock_transfer_fee_handoff       建议 u_page
#   消费 U 的股票过户费切日，或显式旁路；不重开假设-U；不改 U
# params.stock_stamp_handoff              建议 v_page
#   消费 V 的股票印花税切日，或显式旁路；不重开假设-V；不改 V
# params.bse_limit_aft_handoff            建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；不重开假设-AC；不改 AC
# params.cb_rule_handoff                  建议 q_page
#   可转债规则混用交 Q；回转/涨跌幅 ≠ 回售经手暂免；不改 Q
# params.stock_etf_rotation_handoff       建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 回售经手费；不重开假设-R；不改 R
# params.block_channel_handoff            建议 o_page
#   大宗通道交 O；双字母 DO ≠ 单字母假设-O；不重开假设-O；不改 O
# params.board_capacity_handoff           建议 a_page
# params.fill_time_suspend_handoff        建议 d_page
#   成交时点与停牌交 D；双字母 DO ≠ 单字母假设-D；不改 D
# params.cb_call_put_fill_handoff         建议 cr_page
#   赎回/回售能不能成交交 CR；可成交性 ≠ 回售经手费；不改 CR；不升格进 do0
# params.cb_put_handling_handoff          建议 self
# params.do0_primary_demo                 写死冻结 invent_full_handling_fee_on_cb_put
#   单一主报写死，单挂；禁与 invent_asof_leak_cb_put_handling 双挂；DO1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_cb_put_handling 只作对照，不得升格进 do0，不得双挂
#   诊断桶 ignore_sse_put_waiver_window / copy_spot_004_onto_put / merge_sse_szse_put_handling / confuse_DB_spot_with_put / vs_DB_cb_spot_handling / vs_DF_exch_spot_handling / vs_DM_exch_conversion_handling / vs_S_stock_handling / vs_DI_block_handling / missing_venue_or_biz_type_not_skip 不得升格进 do0
#   尤重：禁止把 DB 现货经手费与本页回售暂免合成/混读后写进 do0（现货≠回售）
#   尤重：禁止把 DF 可交换现货经手、DM 换股经手与本页转债回售合成/混读后写进 do0
#   尤重：禁止把 S 股票经手切日与本页回售另档合成/混读后写进 do0
#   尤重：禁止把 DI 大宗经手下浮与本页回售暂免合成/混读后写进 do0
# params.do0_invent_full_handling_fee_on_cb_put 建议 True
# params.do1_asof_leak_cb_put_handling_only 建议 True
#   半泄露对照；DO1 不升格并列主报；不得把 invent_asof_leak_cb_put_handling 写进 do0
# params.do2_pit_sse_put_waived_spot_still_charged 建议 True
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
# params.missing_venue_or_biz_type_or_official_bps_policy 建议 skip
# params.day_freq_proxy                   建议 cb_put_handling_sensitivity
# params.universe_rule                    建议 cb_put_handling_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_do_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DO；勿把这个键读成实验 DO，亦勿读成单字母 D/O
#   不另挂主报，不预留 #125，不写下一字母
```

### 2.2 三组对照（DO0 / DO1 / DO2）

组名 DO0 / DO1 / DO2 是本页三组，≠ 单字母实验 O（大宗）。

| 组 | 角色 | 口径 |
|----|------|------|
| DO0 | 天真 / 回售经手费暂免误忽略 | 按 `do0_primary_demo` **写死冻结**单一主报 `invent_full_handling_fee_on_cb_put`（单挂写死）：忽略沪市回售暂免窗，把现货档 0.004% 铺到回售腿。**禁**与 `invent_asof_leak_cb_put_handling` 双挂主报。**禁把 DB 现货经手、DF 可交换现货经手、DM 换股经手、S 股票经手切日、DI 大宗经手下浮合成进 `do0`**（只作对照/旁路，不得升格进 `do0` 或另挂主报） |
| DO1 | 半泄露 | 仅核对日把「沪市回售暂免」铺到全历史、铺到现货、铺到深市，或把沪深回售合成一句（`invent_asof_leak_cb_put_handling`）；**不得升格并列主报**，也不得写进 `do0`（写死冻结：DO1 不升格），不得双挂 |
| DO2 | 诚实 / 回售暂免与现货分列 | `cb_put_handling_honest=pit_sse_put_waived_spot_still_charged`（写死冻结）：缺 venue/业务类型或官方‰则 skip；沪市核对日回售在暂免窗内按表暂免、现货仍收 0.004%，禁止把现货档铺到回售；深市缺官方回售另档‰则 skip。现货经手只消费 DB，可交换现货经手只消费 DF，换股经手只消费 DM，股票经手切日只消费 S，大宗经手下浮只消费 DI，或显式旁路 |

忽略暂免窗、把现货 0.004% 铺到回售、沪深回售合成一句、把 DB 的现货经手混进回售、把 DF 的可交换现货或 DM 的换股经手混进回售、把 S 的股票切日混进回售、把 DI 的大宗下浮混进回售，以及相对这些页的对照截（`ignore_sse_put_waiver_window` / `copy_spot_004_onto_put` / `merge_sse_szse_put_handling` / `confuse_DB_spot_with_put` / `vs_DB_cb_spot_handling` / `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` / `vs_S_stock_handling` / `vs_DI_block_handling` / `missing_venue_or_biz_type_not_skip`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `do0_primary_demo`。`vs_DB_cb_spot_handling` 只标记「有人把 DB 的现货经手和本页回售暂免合成/混读」，**不得升格进 `do0`**。`vs_DF_exch_spot_handling` 只标记可交换现货对照，**不得升格进 `do0`**。`vs_DM_exch_conversion_handling` 只标记换股经手对照，**不得升格进 `do0`**。`vs_S_stock_handling` 只标记股票经手切日对照，**不得升格进 `do0`**。`vs_DI_block_handling` 只标记大宗经手下浮对照，**不得升格进 `do0`**。DB 的现货、DF 的可交换现货、DM 的换股、S 的股票切日、DI 的大宗下浮只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`do0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺 venue/业务类型或官方‰则 skip；沪市核对日回售在暂免窗内按表暂免、现货仍收 0.004%，禁止把现货档铺到回售；深市缺官方回售另档‰则 skip。方向随锚写死：**不要把核对日暂免铺满全历史或铺到现货，也不要把现货 0.004% 铺到回售，也不要沪深合成一句**。窗名 `sse_put_waiver_20220701_20261231_szse_listed_apart` 只标方向：沪市上市公司可转债回售经手费暂免是 2022-07-01 至 2026-12-31 这一段，核对日 2026-10-16 落在窗内；窗外出了这段不要继续当暂免。现货不进这个窗。深市另列，缺官方回售另档‰就 skip。`事实与坑` 2026-11-06 已写：沪市表阶段性调整里，上市公司可转债回售同期暂免，现货竞价仍收 0.004%。「除上市公司可转债以外的转债暂免」是另一行，不是本页回售腿，不升格进 `do0`。那些现货数字留在 DB，可交换现货留在 DF，换股经手留在 DM。`params.G` 的 0.01 是无量纲相对门槛，不是转债现货经手 0.04‰，也不是回售暂免。**禁把占位读成 0.004%/0.04‰/暂免**。缺 venue、业务类型或官方‰则 skip，不用现货档、沪市暂免、自造‰或把占位 0.01 当成费率把回售腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `do0_primary_demo` / `params.Y`·G·N·Y2 / 回售暂免开关 / 桶 / 是否把暂免或 0.004% 铺到全历史、铺到现货或合成一句）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DO0）/ 半泄露组（DO1）相对诚实组（DO2）的成本差、误套截**显著且集中在回售经手费暂免被忽略、现货档 0.004% 被铺到回售腿的桶**；分桶「忽略暂免窗 / 现货铺到回售 / 沪深合成 / DB 现货混进回售 / 核对日泄露 / vs DB·DF·DM·S·DI」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把暂免或 0.004% 冻成全历史唯一费率，也不把 `params.G` 的 0.01 读成转债现货经手或回售暂免。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 DB 的现货经手、DF 的可交换现货经手、DM 的换股经手、S 的股票经手切日、DI 的大宗经手下浮、DN 的换股过户、DL 的综合协议过户、DK 的基金印花税、DJ 的基金证管费、DH 的佣金双计、DG 的北交所档、DE 的转债证管费、DD 的转债过户、DC 的转债印花税、DA 的基金过户、AX 的基金经手费、T 的股票证管费、U 的股票过户、V 的股票印花税、AC 的北交所涨跌幅与盘后、Q 的回转与涨跌幅、R 的股票 ETF 回转、O 的大宗通道、A 的板上容量、D 的成交时点、CR 的回售可成交性解释；或 `do0_primary_demo` 与 `invent_asof_leak_cb_put_handling` 双挂；或 DO1 升格并列主报；或 `ignore_sse_put_waiver_window` / `copy_spot_004_onto_put` / `merge_sse_szse_put_handling` / `confuse_DB_spot_with_put` / `vs_DB_cb_spot_handling` / `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` / `vs_S_stock_handling` / `vs_DI_block_handling` / `missing_venue_or_biz_type_not_skip` 诊断桶升格主报；或把 DB 现货、DF 可交换现货、DM 换股、S 股票切日、DI 大宗下浮合成进 `do0`；或实验字母 DO 与单字母 D/O 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成转债现货经手 0.04‰ 或回售暂免；或把占位读成 0.004%/0.04‰/暂免；或把核对日暂免 / 现货 0.004% 写成已冻并铺满全历史或铺到回售；或缺 venue / 业务类型 / 官方‰仍按现货档把回售腿填上；或重开假设-T / 假设-AC / 假设-R / 假设-U / 假设-O / 假设-DI / 假设-V / 假设-DF / 假设-DB / 假设-S / 假设-DD / 假设-DL / 假设-DM / 假设-DN / 假设-DA；或标纸面齐；或写成 A/D–DO纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DO0/DO1/DO2。现货经手走 DB 或显式旁路，不在本页改 DB，也不把 DB 的现货升成主报。可交换现货走 DF，换股经手走 DM，股票经手切日走 S，大宗经手下浮走 DI，换股过户走 DN，都不改。报告成本差、误套截。不把 0.004% 或暂免标成已冻的全历史回售费率，也不把 `params.G` 的 0.01 读成转债现货经手。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_full_handling_fee_on_cb_put` / `invent_asof_leak_cb_put_handling` / `ignore_sse_put_waiver_window` / `copy_spot_004_onto_put` / `merge_sse_szse_put_handling` / `confuse_DB_spot_with_put` / `vs_DB_cb_spot_handling` / `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` / `vs_S_stock_handling` / `vs_DI_block_handling` / `missing_venue_or_biz_type_not_skip`

`ignore_sse_put_waiver_window`、`copy_spot_004_onto_put`、`merge_sse_szse_put_handling`、`confuse_DB_spot_with_put`、`vs_DB_cb_spot_handling`、`vs_DF_exch_spot_handling`、`vs_DM_exch_conversion_handling`、`vs_S_stock_handling`、`vs_DI_block_handling`、`missing_venue_or_biz_type_not_skip` 只作诊断桶：它们不是 `do0`，也不是 DO1，**不得升格主报**。`vs_DB_cb_spot_handling` 没有对应的「DB 现货经手 + 回售暂免」合成主报。DB 的现货经手只作诊断，**不得与回售暂免合成后升格进 `do0`**。DF 的可交换现货、DM 的换股经手只作诊断，**不得升格进 `do0`**。S 的股票经手切日只作诊断，**不得升格进 `do0`**。DI 的大宗经手下浮只作诊断，**不得升格进 `do0`**。忽略暂免窗、把现货 0.004% 铺到回售、沪深合成一句，都只作诊断，**不得升格进 `do0`**。`invent_asof_leak_cb_put_handling` 只服务 DO1，**不得升格进 `do0`，不得双挂**。`invent_full_handling_fee_on_cb_put` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把忽略沪市回售暂免、把现货档 0.004% 铺到回售，并拿去当诚实锚。
- 把 `params.G` 的 0.01 当成转债现货经手 0.04‰ 或回售暂免。**尤重：`params.G` 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 0.004%/0.04‰/暂免。**禁把占位读成 0.004%/0.04‰/暂免**。
- 缺 venue、业务类型或官方‰仍不 skip，并用现货档、沪市暂免、自造‰或占位 0.01 把回售腿填上。
- 把核对日「沪市回售暂免、现货仍收 0.004%」写成全历史唯一费率，并铺满全历史，或把现货档铺到回售，或沪深合成一句。方向是窗内暂免、现货另档、深市缺档则 skip，不是全历史已冻费率。锚六键已写死冻结。
- 深市回售没有官方另档‰仍硬填一档（含把现货 0.04‰ 或沪市暂免抄成深市回售）。
- 把「现货经手已诚实（DB）/ 可交换现货已分列（DF）/ 换股经手已分列（DM）/ 股票经手切日已诚实（S）/ 大宗经手下浮已诚实（DI）」写成「可转债回售经手费暂免已诚实」。不改 DB / DF / DM / S / DI。
- 把 DB 的现货经手费和本页回售暂免合成或混读后升格进 `do0`。诊断桶 `vs_DB_cb_spot_handling` / `confuse_DB_spot_with_put` / `copy_spot_004_onto_put` 只作对照。现货≠回售。
- 把 DF 可交换现货经手、DM 换股经手和本页转债回售合成或混读后升格进 `do0`。诊断桶 `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` 只作对照。
- 把 S 股票经手切日和本页回售另档合成或混读后升格进 `do0`。诊断桶 `vs_S_stock_handling` 只作对照。
- 把 DI 大宗经手下浮和本页回售暂免合成或混读后升格进 `do0`。诊断桶 `vs_DI_block_handling` 只作对照。
- 忽略暂免窗，并升格进 `do0`。诊断桶 `ignore_sse_put_waiver_window` 只作对照。
- 沪深回售经手合成一句，并升格进 `do0`。诊断桶 `merge_sse_szse_put_handling` 只作对照。
- 缺 venue 或业务类型仍不 skip，并升格进 `do0`。诊断桶 `missing_venue_or_biz_type_not_skip` 只作对照。
- `do0_primary_demo` 与 `invent_asof_leak_cb_put_handling` 双挂主报；DO1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DO 与单字母 D/O 或 params.Y/G/N 混读。
- 把回售能不能成交（CR）写成回售经手费已经诚实。
- 改 DB / DF / DM / S / DI / DN / DL / DK / DJ / DH / DG / DE / DD / DC / DA / AX / T / U / V / AC / Q / R / O / A / D 正文；重开假设-T；重开假设-AC；重开假设-R；重开假设-U；重开假设-O；重开假设-DI；重开假设-V；重开假设-DF；重开假设-DB；重开假设-S；重开假设-DD；重开假设-DL；重开假设-DM；重开假设-DN；重开假设-DA；抢 A 真数队列；标纸面齐；写成 A/D–DO纸面齐；开真数/回测/实盘；用复权价当费用基数；结论写成「回售费更低所以能买」。
- **纸面齐惯例**：以后若落复检稿要标纸面齐，须同步升假设正文页头、结论、尾状态（对照 DK/DL/DM/DN；勿再只改清单）。**当前禁止标纸面齐**。**不写 A/D–DO纸面齐**。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权成交金额、交易日、**交易所 venue**（沪/深）、**业务类型**（可转债回售 / 可转债现货 / 可交换债现货 / 可交换债换股 / 股票竞价 / 股票大宗；仅用于把腿分回 DB、DF、DM、S、DI 或本页）、**官方回售经手‰或暂免是否在册**（缺则 skip，不发明数，也不把现货档填上）。
- 沪市回售还要知道成交日是否落在 2022-07-01 至 2026-12-31 暂免窗内。窗外不把窗内暂免往回铺。现货腿不进这个窗。
- 深市回售若没有官方另档‰，整腿 skip。不拿现货 0.04‰ 或沪市暂免代替。
- 证券类别只用于把腿分回 DB / DF / DM / S / DI 等旁路页，不在本页改那些页。
- 没有 venue、业务类型或官方‰时，按写死冻结的 `cb_put_handling_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing` skip，不得按现货档 0.004% 把回售腿填上，也不得用核对日暂免把腿填满全历史或填到现货，或把两所合成一句。
- 旁路消费：DB 的转债现货经手费、DF 的可交换现货经手费、DM 的换股经手费、S 的股票经手切日、DI 的大宗经手下浮、DN 的换股过户费、DL 的综合协议过户费下浮、DK 的基金印花税、DJ 的基金证管费、DH 的佣金双计、DG 的北交所经手费、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、DA 的基金过户费、AX 的基金经手费、T 的股票证管费、U 的股票过户费、V 的股票印花税、AC 的北交所涨跌幅与盘后、Q 的转债规则、R 的股票 ETF 回转、O 的大宗通道、D 的成交时点、CR 的回售可成交性之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** DB 的现货经手、DF/DM 的可交换经手、S 的股票切日、DI 的大宗下浮不收到本页主报。
- 未复权价；asof **写死冻结** `2026-10-16`。核对日方向「沪市回售窗内暂免、现货仍收 0.004%、深市缺官方回售另档‰则 skip」是写死冻结的机制方向，不是已冻全历史费率。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`cb_put_handling_honest=pit_sse_put_waived_spot_still_charged`（沪市核对日回售在暂免窗内按表暂免、现货仍收 0.004%，禁止把现货档铺到回售；深市缺官方回售另档‰则 skip；**禁止把暂免或 0.004% 写成全历史唯一费率**）；`cb_put_handling_scope=sse_put_waiver_20220701_20261231_szse_listed_apart`（沪市回售暂免窗与深市分列；方向名，不是已冻费率）；`cb_put_handling_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing`（缺 venue/业务类型或官方‰则 skip）；`do0_primary_demo=invent_full_handling_fee_on_cb_put`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_cb_put_handling` 双挂；DO1 不升格；诊断桶不升格主报；**禁把 DB 现货经手、DF 可交换现货经手、DM 换股经手、S 股票经手切日、DI 大宗经手下浮合成进 `do0`**，只作对照/旁路，不得升格进 `do0` 或另挂主报）；`cb_handling_fee_handoff=db_page`；`exch_spot_handling_handoff=df_page`；`exch_conversion_handling_handoff=dm_page`；`ashare_fee_handoff=s_page`；`stock_block_handling_handoff=di_page`；`merge_with_DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/A/D=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误套截 ΔCbPutHandling / 净收益差 / DO1−DO2；**尤重 params.G 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免（量纲与语义不同）**；**禁把占位读成 0.004%/0.04‰/暂免**；**params.Y/G/N ≠ 实验字母 DO ≠ 单字母 D/O**；**勿把 params.G 读成实验字母 DO，亦勿把单字母假设-D / 假设-O 读成双字母 DO**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成回售经手费率或现货档）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #125。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`6d1a93d2`（A/D–DN纸面齐已合，全长 `6d1a93d22d03dfeccb1807506904666b07d88b79`）；三冻补丁基 tip=`875ba8be` / `875ba8be8bde4768257475f09246d141b1dbc662`；分支起点 HEAD=`3470b2d6` / `3470b2d6cb9064bc3fbeb84c45e4de26d6f59de6`。**不改已冻 A–DN / DA–DM**。状态=**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DO纸面齐**。

---

## 8. 结论

（空；**预检有条件通过·三条已冻·待复检**。**禁止标纸面齐**。**未标纸面齐**。**不写 A/D–DO纸面齐**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-16）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DO-20261110.md`（原样落入，不改结论；SHA256=`04e93a04782af8e25bdbff0b7d7e71d761116cd0fe0ade9d99d3a95f96d1bb37`；预检 2026-11-10；**结论：有条件通过**；tip基=`875ba8be` / `875ba8be8bde4768257475f09246d141b1dbc662`；本补丁分支起点 HEAD=`3470b2d6` / `3470b2d6cb9064bc3fbeb84c45e4de26d6f59de6`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、误套截 ΔCbPutHandling、净收益差、DO1−DO2 专项。**`params.Y` ≠ 实验字母 DO**；**`params.G` ≠ 实验字母 DO**；**`params.N` ≠ 实验字母 DO**；亦 ≠ 单字母假设-D / 假设-O。**勿把 `params.G` 读成实验字母 DO，亦勿把单字母假设-D / 假设-O 读成双字母 DO**。**尤重：`params.G` 的 `0.01` ≠ 转债现货经手 0.04‰ ≠ 回售暂免**（**params.G 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免**）。二者量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是转债现货经手费率，也不是回售暂免；现货档 0.004% = 0.04‰ 留在 DB。**禁把占位读成 0.004%/0.04‰/暂免**。禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.do0_primary_demo`**：**写死冻结** **`invent_full_handling_fee_on_cb_put`**（单一主报，单挂写死）。**禁止**与 **`invent_asof_leak_cb_put_handling`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DO1 仅核对日把「沪市回售暂免」铺到全历史、铺到现货、铺到深市，或把沪深回售合成一句只作半泄露对照，**不得升格与 do0 并列主报**，也不得把 `invent_asof_leak_cb_put_handling` 写进 `do0`。`ignore_sse_put_waiver_window` / `copy_spot_004_onto_put` / `merge_sse_szse_put_handling` / `confuse_DB_spot_with_put` / `vs_DB_cb_spot_handling` / `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` / `vs_S_stock_handling` / `vs_DI_block_handling` / `missing_venue_or_biz_type_not_skip` **只作诊断桶，不得升格主报**。DO1 / 诊断桶 **不升格**。**禁把 DB转债现货经手 / DF可交换现货经手 / DM换股经手 / S股票经手切日 / DI大宗经手下浮 合成/混读升格进 `do0`**：这些只作对照/旁路，**不得升格进 `do0`，不得另挂主报**。现货≠回售。

3. **可转债回售经手费诚实锚六键升格写死（不可再写「建议」）**：`params.cb_put_handling_honest=pit_sse_put_waived_spot_still_charged`；`params.cb_put_handling_scope=sse_put_waiver_20220701_20261231_szse_listed_apart`；`params.cb_put_handling_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺 venue/业务类型或官方‰ → skip；沪市核对日回售在暂免窗内按表暂免、现货仍收 0.004%，禁止把现货档铺到回售；深市缺官方回售另档‰ → skip。禁止把核对日暂免或现货 0.004% 铺满全历史。禁止跑后改锚，或用现货档 / 核对日暂免铺满 / 沪深合成一句 / 发明‰ / 缺 venue/业务类型或官方‰仍硬填 / 把 DB转债现货经手、DF可交换现货经手、DM换股经手、S股票经手切日或 DI大宗经手下浮升格进 do0 冒充诚实 PIT。**禁把占位读成 0.004%/0.04‰/暂免**。**禁把 params.G 的 0.01 读成转债现货经手 0.04‰ 或回售暂免**。**现货≠回售**。

**硬分列保住**：DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D；**双字母 DO ≠ 单字母假设-D / 假设-O**；**params.Y / params.G / params.N ≠ 实验字母 DO ≠ 单字母 D/O**；**尤重 params.G 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免**；**禁把占位读成 0.004%/0.04‰/暂免**；**可转债回售经手费暂免误忽略 ≠ DB转债现货经手 ≠ DF可交换现货经手 ≠ DM换股经手 ≠ S股票经手切日 ≠ DI大宗经手下浮 ≠ DN换股过户**；不抢 A；不改已齐/已冻 DA～DN 及 A–DN 正文；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**不重开假设-DD**；**不重开假设-DL**；**不重开假设-DM**；**不重开假设-DN**；**不重开假设-DA**；**禁把 DB转债现货经手 / DF可交换现货经手 / DM换股经手 / S股票经手切日 / DI大宗经手下浮 合成/混读升格进 do0**。

**状态**：**预检有条件通过·三条已冻·待复检**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DO纸面齐**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-16 | 风控预检补丁·冻结三条写死——依据 `预检-假设DO-20261110.md`（SHA256=`04e93a04782af8e25bdbff0b7d7e71d761116cd0fe0ade9d99d3a95f96d1bb37`；结论=有条件通过；tip基=`875ba8be` / `875ba8be8bde4768257475f09246d141b1dbc662`；分支起点 HEAD=`3470b2d6` / `3470b2d6cb9064bc3fbeb84c45e4de26d6f59de6`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔCbPutHandling / 净收益差 / DO1−DO2；**params.Y/G/N ≠ 实验字母 DO ≠ 单字母 D/O**；**勿把 params.G 读成实验字母 DO，亦勿把单字母假设-D / 假设-O 读成双字母 DO**；**尤重 params.G 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免（量纲与语义不同）**；**禁把占位读成 0.004%/0.04‰/暂免**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成回售经手费率或现货档）；② `params.do0_primary_demo=invent_full_handling_fee_on_cb_put`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_cb_put_handling` 双挂；DO1 不升格；诊断桶 `ignore_sse_put_waiver_window` / `copy_spot_004_onto_put` / `merge_sse_szse_put_handling` / `confuse_DB_spot_with_put` / `vs_DB_cb_spot_handling` / `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` / `vs_S_stock_handling` / `vs_DI_block_handling` / `missing_venue_or_biz_type_not_skip` 不升格；**禁把 DB转债现货经手 / DF可交换现货经手 / DM换股经手 / S股票经手切日 / DI大宗经手下浮 合成/混读升格进 do0**，只作对照/旁路，不得升格进 do0 或另挂主报；现货≠回售）；③ 锚六键写死 `cb_put_handling_honest=pit_sse_put_waived_spot_still_charged` / `cb_put_handling_scope=sse_put_waiver_20220701_20261231_szse_listed_apart` / `cb_put_handling_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`（缺 venue/业务类型或官方‰ → skip；沪市核对日回售在暂免窗内按表暂免、现货仍收 0.004%，禁止把现货档铺到回售；深市缺官方回售另档‰ → skip）。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DO纸面齐**；不改已齐/已冻 DA～DN 及 A–DN；不改假设-DA～假设-DN；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-U；不重开假设-O；不重开假设-DI；不重开假设-V；不重开假设-DF；不重开假设-DB；不重开假设-S；不重开假设-DD；不重开假设-DL；不重开假设-DM；不重开假设-DN；不重开假设-DA；不开回测/真数/实盘。基于 tip=`875ba8be`。 |
| 2026-11-16 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。可转债回售经手费暂免误忽略；`do0_primary_demo` 建议 `invent_full_handling_fee_on_cb_put`，单一主报，单挂，禁与 `invent_asof_leak_cb_put_handling` 双挂，DO1 不升格；诊断桶 `ignore_sse_put_waiver_window` / `copy_spot_004_onto_put` / `merge_sse_szse_put_handling` / `confuse_DB_spot_with_put` / `vs_DB_cb_spot_handling` / `vs_DF_exch_spot_handling` / `vs_DM_exch_conversion_handling` / `vs_S_stock_handling` / `vs_DI_block_handling` / `missing_venue_or_biz_type_not_skip` 不升格；**尤重 DB 可转债现货经手费 ≠ 本页回售经手费暂免（现货≠回售），禁止合成/混读升格进 do0**；**尤重 DF/DM 可交换现货/换股经手 ≠ 本页转债回售，禁止合成进 do0**；**尤重 S 股票经手切日 ≠ 本页回售另档，禁止合成进 do0**；**尤重 DI 大宗经手下浮 ≠ 本页回售暂免，禁止合成进 do0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DO ≠ 单字母 D/O**，且 **params.G 的 0.01 ≠ 转债现货经手 0.04‰ ≠ 回售暂免**，**禁把占位读成 0.004%/0.04‰/暂免**；锚建议、未冻：`cb_put_handling_honest=pit_sse_put_waived_spot_still_charged` / scope=`sse_put_waiver_20220701_20261231_szse_listed_apart` / over_policy=`skip_if_venue_or_biz_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`；口径：缺 venue/业务类型或官方‰则 skip；沪市核对日回售在暂免窗内按表暂免、现货仍收 0.004%，禁止把现货档铺到回售；深市缺官方回售另档‰则 skip（**草稿方向，尚未冻，不要写成已冻**）；handoff：`cb_handling_fee_handoff=db_page`，`exch_spot_handling_handoff=df_page`，`exch_conversion_handling_handoff=dm_page`，`ashare_fee_handoff=s_page`，`stock_block_handling_handoff=di_page`；`merge_with_DN/DM/DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/A/D=False`；**DO≠DN≠DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D**；**双字母 DO ≠ 单字母假设-D / 假设-O**；**可转债回售经手费暂免误忽略 ≠ DB转债现货经手 ≠ DM换股经手 ≠ DN换股过户**；**未标纸面齐**；**不写 A/D–DO纸面齐**；**纸面齐惯例**：落复检稿标纸面齐时须同步升假设正文页头/结论/尾状态（对照 DK/DL/DM/DN；勿再只改清单）——当前草稿阶段禁止标纸面齐；结论栏空；不改已冻 A–DN / DA–DM；不改已齐假设-DA～假设-DN；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-U；不重开假设-O；不重开假设-DI；不重开假设-V；不重开假设-DF；不重开假设-DB；不重开假设-S；不重开假设-DD；不重开假设-DL；不重开假设-DM；不重开假设-DN；不重开假设-DA；不写下一字母；不预留 #125；不开真数/回测/实盘。基 tip=`6d1a93d2`（A/D–DN纸面齐已合，全长 `6d1a93d22d03dfeccb1807506904666b07d88b79`；不改该 tip 上的 #110–#123，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
