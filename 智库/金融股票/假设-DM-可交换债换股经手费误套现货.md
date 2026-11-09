# 假设-DM · 可交换债换股经手费误套现货（成本诚信）

更新：2026-11-10  
来源：总管线 / 默认分支 HEAD `bc6df6d` 上清单 #121=DL 已收口（A/D–DL纸面齐已合入该 tip；全长 `bc6df6d2e52da183e8ef5eac9e5c44adba046a72`；**不改已冻 A–DL / DA–DK**；**不改假设-DL 正文**，亦不改已齐假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-DK / 假设-S / 假设-AX / 假设-T / 假设-U / 假设-V / 假设-AC / 假设-Q / 假设-R / 假设-A / 假设-D / 假设-M / 假设-O 及其他已存在假设页；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**）后写下一草稿 DM；清单 #121=DL，本页占用 **#122=DM**；选题是可交换债**换股**经手费被误套成**现货**档（或静默按现货暂免）；假设-DF 只收可交换债**现货**经手费沪深合成（现货沪深合成 ≠ 本页「换股≠现货」），假设-DB 只收可转债现货经手费，假设-S 只收股票经手费切日，假设-DD 只收可转债过户费；**新建实验 DM**；不写下一字母；不预留 #123  
状态：**预检有条件通过·三条已冻·待复检**（结论栏空；**三条已冻**；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DM纸面齐**；禁止把「可交换债换股经手费按现货档抽、或静默按现货暂免」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改已冻 A–DL / DA–DK**；尤其不改假设-DF / 假设-DB / 假设-S / 假设-DD / 假设-DL / 假设-DK / 假设-T / 假设-AC / 假设-R / 假设-U / 假设-O / 假设-DI / 假设-V / 假设-D / 假设-M；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DM（#122）。一句话误开：回测把可交换债**换股**经手费误套成**现货**档（或静默按现货暂免），或缺 venue/业务类型/官方‰仍不 skip，系统性改写换股腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DM** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DM**；**勿把 `params.Y` 读成实验字母 DM**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DM**；**尤重：`params.G` 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是换股经手费率，也不是现货暂免或 0.04‰；**禁把占位读成 0.00341%/0.04‰/暂免**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DM**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DM ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 M**（盘后补成交；**双字母 DM ≠ 单字母假设-M；严禁复用假设-M**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DM ≠ 单字母假设-A**）≠ 双字母 **DL**（股票综合协议过户费下浮）≠ **DK**（场内基金印花税）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债现货经手费沪深合成）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债现货经手费）≠ **DA**（场内基金过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费）≠ **T**（股票证管费）≠ **U**（股票过户费）≠ **V**（股票印花税）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）。**DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠A≠D**。**双字母 DM ≠ 单字母 D/M**。**params.Y/G/N ≠ 实验字母 DM；亦 ≠ 单字母 D/M**。**勿把 `params.G` 读成实验字母 DM，亦勿把单字母假设-D / 假设-M 读成双字母 DM**。**尤重：`params.G` 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档**。**禁把占位读成 0.00341%/0.04‰/暂免**。**可交换债换股经手费误套现货 ≠ DF可交换现货沪深合成 ≠ DB转债现货经手 ≠ S股票经手切日 ≠ DD转债过户**。**尤重：DF 可交换现货经手费沪深合成 ≠ 本页「换股≠现货」——禁止合成/混读升格进 `dm0`**。**尤重：DB 可转债现货经手费 ≠ 本页可交换换股经手费——禁止合成/混读升格进 `dm0`**。**尤重：S 股票经手费切日 ≠ 本页换股另档——禁止合成/混读升格进 `dm0`**。

### 专节 · 双字母 DM ≠ 单字母假设-D / 假设-M；且 ≠ 假设-DF / 假设-DB / 假设-S / 假设-DD（硬）

| 维度 | 对照页 | 本页假设-DM（双字母） |
|------|--------|----------------------|
| 题面 DF | **可交换债现货经手费沪深合成**（沪市现货走债券现券暂免、深市现货 0.04‰，禁止合成一句；现货 ≠ 换股） | 现货沪深合成 ≠ 本页「换股≠现货」。本页专测：换股经手费被套成现货档，或静默按现货暂免。**DM≠DF**；**严禁复用假设-DF**；**不重开假设-DF**；**不改 DF**；**尤重：DF 可交换现货经手费沪深合成 ≠ 本页「换股≠现货」——禁止合成/混读升格进 `dm0`**；`exch_spot_handling_handoff=df_page`；诊断桶 `vs_DF_exch_spot_handling` / `confuse_DF_spot_merge_with_conversion` 不升格 |
| 题面 DB | **可转债现货经手费**（转债现货腿误套股票档） | 转债现货经手 ≠ 可交换债换股经手。**DM≠DB**；**严禁复用假设-DB**；**不重开假设-DB**；**不改 DB**；**尤重：DB 可转债现货经手费 ≠ 本页可交换换股经手费——禁止合成/混读升格进 `dm0`**；`cb_handling_fee_handoff=db_page`；诊断桶 `vs_DB_cb_handling` 不升格 |
| 题面 S | **沪深 A 股竞价经手费切日**（三切日；现行档留在 S） | 股票经手费切日 ≠ 换股另档。**DM≠S**；**严禁复用假设-S**；**不重开假设-S**；**不改 S**；**尤重：S 股票经手费切日 ≠ 本页换股另档——禁止合成/混读升格进 `dm0`**；`ashare_fee_handoff=s_page`；诊断桶 `vs_S_stock_handling` 不升格 |
| 题面 DD | **可转债过户费** | 转债过户 ≠ 可交换债换股经手。**DM≠DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page`；诊断桶 `vs_DD_cb_transfer` 不升格 |
| 题面 DL | **股票综合协议过户费下浮** | 综合协议过户下浮 ≠ 换股经手费。**DM≠DL**；**不改 DL**；`agreement_transfer_handoff=dl_page` |
| 题面 DK | **场内基金印花税** | 基金印花 ≠ 换股经手费。**DM≠DK**；**不改 DK**；`fund_stamp_handoff=dk_page` |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 本机制。**DM≠DJ**；**不改 DJ**；`fund_csrc_fee_handoff=dj_page` |
| 题面 DI | **股票大宗经手下浮** | 大宗经手下浮 ≠ 换股经手费。**DM≠DI**；**不重开假设-DI**；**不改 DI**；`stock_block_handling_handoff=di_page` |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 换股经手费。**DM≠DH**；**不改 DH**；`commission_double_handoff=dh_page` |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 本机制。**DM≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 换股经手费。**DM≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DC | **可转债印花税** | 转债印花税 ≠ 本机制。**DM≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 DA | **场内基金过户费** | 基金过户 ≠ 换股经手费。**DM≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 本机制。**DM≠AX**；**不改 AX**；`fund_handling_fee_handoff=ax_page` |
| 题面 T | **证管费主报股票** | 股票证管费 ≠ 换股经手费。**DM≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费切日** | 股票过户切日 ≠ 换股经手费。**DM≠U**；**严禁复用假设-U**；**不重开假设-U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 V | **股票印花税切日** | 印花税 ≠ 换股经手费。**DM≠V**；**严禁复用假设-V**；**不重开假设-V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 换股经手费。**DM≠AC**；**不改 AC**；**不重开假设-AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 本机制。**DM≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 本机制。**DM≠R**；**不改 R**；**不重开假设-R**；`stock_etf_rotation_handoff=r_page` |
| 题面 O | **大宗通道 / 假流动性** | 大宗通道 ≠ 换股经手费。**不重开假设-O**；**不改 O**；`block_channel_handoff=o_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 换股经手费。**DM≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 换股经手费抽在哪一档。**双字母 DM ≠ 单字母假设-D**；**严禁复用假设-D**；**DM≠D**；**不改 D** |
| 题面 M | **盘后补成交** | 盘后通道 ≠ 换股经手费。**双字母 DM ≠ 单字母假设-M**；**严禁复用假设-M**；**不改 M**；`aft_fixed_handoff=m_page` |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_spot_handling_on_exchangeable_conversion`（**写死冻结**单一主报，单挂写死；禁与半泄露键 `invent_asof_leak_exchangeable_conversion_handling` 双挂；DM1 不升格；`apply_spot_waiver_onto_conversion` / `copy_conversion_00341_onto_spot` / `confuse_DF_spot_merge_with_conversion` / `vs_DF_exch_spot_handling` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_DD_cb_transfer` / `missing_biz_type_not_skip` 只作诊断对照，不升格主报；**尤重禁止把 DF 现货沪深合成、DB 转债现货经手、S 股票经手切日合成进 `dm0`**） |
| 文档 | 清单实验 DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / T / U / V / AC / Q / R / A / D / M（**只读；禁止改写**） | `假设-DM-可交换债换股经手费误套现货.md`（新建） |
| 预检键 | 实验字母 DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / T / U / V / AC / Q / R / A / D / M / Y / G / N | 实验字母 **DM** / `dm0_primary_demo`；**不得**占用或改写预检 DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/A/D/M |

**禁止**：把 DM 写成「DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / T / U / V / AC / Q / R / A / D / M 的续篇」；把「可交换现货沪深已分列（DF）/ 转债现货经手已诚实（DB）/ 股票经手切日已诚实（S）/ 转债过户已诚实（DD）」写成「可交换债换股经手费已诚实」；把实验字母 DM 与单字母 D/M 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-M 读成双字母 DM**；**尤重勿把 `params.G` 读成实验字母 DM**；**尤重 `params.G` 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档（量纲与语义不同）**；**禁把占位读成 0.00341%/0.04‰/暂免**；**尤重 DF 可交换现货经手费沪深合成 ≠ 本页「换股≠现货」，禁止合成/混读升格进 `dm0`**；**尤重 DB 可转债现货经手费 ≠ 本页可交换换股经手费，禁止合成/混读升格进 `dm0`**；**尤重 S 股票经手费切日 ≠ 本页换股另档，禁止合成/混读升格进 `dm0`**；把 `invent_asof_leak_exchangeable_conversion_handling` 升格进 `dm0` 或与主报双挂；把诊断桶 `apply_spot_waiver_onto_conversion` / `copy_conversion_00341_onto_spot` / `confuse_DF_spot_merge_with_conversion` / `vs_DF_exch_spot_handling` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_DD_cb_transfer` / `missing_biz_type_not_skip` 升格进 `dm0`。本页主键只用 `dm0` / `dm1` / `dm2` 与 `exch_conversion_handling_*`。不写下一字母。不预留 #123。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权成交金额下，回测把可交换债**换股**经手费误套成**现货**档（或静默按现货暂免），或缺 venue/业务类型/官方‰仍不 skip，相对「缺 venue/业务类型或官方‰则 skip；换股与现货分开；沪市核对日换股 0.00341% 双向，禁止静默按现货暂免；深市缺官方换股另档‰则 skip」的诚实组，会**系统性改写换股腿成本**——相对诚实锚偏误。

核对日方向（随锚写死；禁止把 0.00341% 或现货暂免/0.04‰ 写成全历史唯一费率）：沪市换股与现货分开，核对日换股方向是 0.00341% 双向，禁止静默按现货暂免；深市没有官方换股另档‰就 skip，不把现货 0.04‰ 或沪市暂免抄过去。缺 venue、业务类型或官方‰则 skip。这不是把 0.00341%、0.04‰ 或「暂免」冻成全历史唯一费率，也不是把 `params.G` 的 0.01 读成换股经手费 0.00341%。**禁把占位读成 0.00341%/0.04‰/暂免**。**`params.G` 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档**。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误套截在标定噪声带内可忽略，且「现货暂免铺到换股 / 把换股 0.00341% 抄到现货 / 把 DF 现货沪深合成混进换股 / 核对日泄露 / vs DF·DB·S·DD」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dm0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DM ≠ 单字母假设-D / 假设-M**；勿把 params.Y 读成实验字母 DM
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DM ≠ 单字母 D/M**
# 【消歧】尤重：params.G 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档（量纲与语义不同：无量纲相对门槛 ≠ 换股经手费率，也 ≠ 现货暂免/0.04‰）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成 0.00341%/0.04‰/暂免（这些是会被误套的现货或换股口径，不是本页门槛，也不是本页要冻的费率）
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DM ≠ 单字母 D/M**
# params.Y2 写死冻结 0.015
# params.Y / G / N / Y2               写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误套截 ΔExchConversionHandling / 净收益差 / DM1−DM2；**params.Y/G/N ≠ 实验字母 DM ≠ 单字母假设-D / 假设-M**；**尤重 params.G 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档**；**禁把占位读成 0.00341%/0.04‰/暂免**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成换股或现货费率）
# params.fill_time                    写死冻结 next_open
# params.asof_check_date              写死冻结 2026-10-16
# params.px_basis                         建议 unadj
# params.fail_policy                  写死冻结 skip
# params.exch_conversion_handling_honest  写死冻结 pit_conversion_apart_from_spot
#   诚实锚方向（已写死冻结；禁止把 0.00341% 或现货暂免/0.04‰ 写成全历史唯一费率）：
#   换股与现货分开
#   沪市核对日换股 0.00341% 双向，禁止静默按现货暂免
#   深市缺官方换股另档‰ → skip（不发明深市换股档，不把现货 0.04‰ 抄成换股）
#   缺 venue、业务类型或官方‰ → skip
#   枚举已写死冻结
#   不把 DF 的可交换现货沪深合成写成换股诚实锚
#   不把 DB 的可转债现货经手费写成可交换换股诚实锚
#   不把 S 的股票经手费切日写成换股另档
# params.exch_conversion_handling_scope   写死冻结 sse_00341_conversion_not_spot_waiver
#   方向名：沪市换股按核对日 0.00341% 双向，不走现货暂免
#   这不是把 0.00341% 冻成全历史费率；深市缺官方换股另档‰仍 skip
#   可交换债换股经手费误套现货 ≠ DF可交换现货沪深合成 ≠ DB转债现货经手 ≠ S股票经手切日 ≠ DD转债过户
# params.exch_conversion_handling_over_policy 写死冻结 skip_if_venue_or_biz_type_or_official_bps_missing
#   缺 venue、业务类型或官方‰则 skip；禁在缺字段时仍按现货暂免或现货 0.04‰ 把换股腿填上
# params.exch_spot_handling_handoff       建议 df_page
#   消费 DF 的可交换现货经手费沪深分列，或显式旁路；现货沪深合成 ≠ 换股≠现货；不重开假设-DF；不改 DF
#   DF 禁止合成/混读升格进 dm0；诊断桶 vs_DF_exch_spot_handling / confuse_DF_spot_merge_with_conversion 不得升格进 dm0
# params.cb_handling_fee_handoff          建议 db_page
#   消费 DB 的可转债现货经手费，或显式旁路；转债现货经手 ≠ 可交换换股经手；不重开假设-DB；不改 DB
#   DB 禁止合成/混读升格进 dm0；诊断桶 vs_DB_cb_handling 不得升格进 dm0
# params.ashare_fee_handoff               建议 s_page
#   消费 S 的沪深股票竞价经手费切日，或显式旁路；股票经手费切日 ≠ 换股另档；不重开假设-S；不改 S
#   S 禁止合成/混读升格进 dm0；诊断桶 vs_S_stock_handling 不得升格进 dm0
# params.cb_transfer_fee_handoff          建议 dd_page
#   消费 DD 的可转债过户费，或显式旁路；转债过户 ≠ 换股经手；不改 DD
#   诊断桶 vs_DD_cb_transfer 不得升格进 dm0
# params.agreement_transfer_handoff       建议 dl_page
#   消费 DL 的股票综合协议过户费下浮，或显式旁路；不改 DL
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
# params.cb_csrc_fee_handoff              建议 de_page
#   消费 DE 的转债证管费，或显式旁路；不改 DE
# params.cb_stamp_handoff                 建议 dc_page
#   消费 DC 的可转债印花税，或显式旁路；不改 DC
# params.etf_transfer_fee_handoff         建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；不改 DA
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
# params.stock_etf_rotation_handoff       建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 换股经手费；不重开假设-R；不改 R
# params.block_channel_handoff            建议 o_page
#   大宗通道交 O；不重开假设-O；不改 O
# params.board_capacity_handoff           建议 a_page
# params.fill_time_suspend_handoff        建议 d_page
#   成交时点与停牌交 D；双字母 DM ≠ 单字母假设-D；不改 D
# params.aft_fixed_handoff                建议 m_page
#   盘后补成交交 M；双字母 DM ≠ 单字母假设-M；不改 M
# params.exch_conversion_handling_handoff 建议 self
# params.dm0_primary_demo             写死冻结 invent_spot_handling_on_exchangeable_conversion
#   单一主报写死，单挂；禁与 invent_asof_leak_exchangeable_conversion_handling 双挂；DM1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_exchangeable_conversion_handling 只作对照，不得升格进 dm0，不得双挂
#   诊断桶 apply_spot_waiver_onto_conversion / copy_conversion_00341_onto_spot / confuse_DF_spot_merge_with_conversion / vs_DF_exch_spot_handling / vs_DB_cb_handling / vs_S_stock_handling / vs_DD_cb_transfer / missing_biz_type_not_skip 不得升格进 dm0
#   尤重：禁止把 DF 可交换现货经手费沪深合成与本页「换股≠现货」合成/混读后写进 dm0
#   尤重：禁止把 DB 可转债现货经手费与本页可交换换股经手费合成/混读后写进 dm0
#   尤重：禁止把 S 股票经手费切日与本页换股另档合成/混读后写进 dm0
# params.dm0_invent_spot_handling_on_exchangeable_conversion 建议 True
# params.dm1_asof_leak_exchangeable_conversion_handling_only 建议 True
#   半泄露对照；DM1 不升格并列主报；不得把 invent_asof_leak_exchangeable_conversion_handling 写进 dm0
# params.dm2_pit_conversion_apart_from_spot 建议 True
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
# params.merge_with_M                     建议 False
# params.missing_venue_or_biz_type_or_official_bps_policy 建议 skip
# params.day_freq_proxy                   建议 exch_conversion_handling_sensitivity
# params.universe_rule                    建议 exch_conversion_handling_misapply_check
# params.redline_v0_exempt_scope          建议 position_industry_dm_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DM；勿把这个键读成实验 DM
#   不另挂主报，不预留 #123，不写下一字母
```

### 2.2 三组对照（DM0 / DM1 / DM2）

| 组 | 角色 | 口径 |
|----|------|------|
| DM0 | 天真 / 换股经手费误套现货 | 按 `dm0_primary_demo` **写死冻结**单一主报 `invent_spot_handling_on_exchangeable_conversion`（单挂写死）：可交换债换股经手费按现货档抽，或静默按现货暂免。**禁**与 `invent_asof_leak_exchangeable_conversion_handling` 双挂主报。**禁把 DF 现货沪深合成、DB 转债现货经手、S 股票经手切日合成进 `dm0`**（只作对照/旁路，不得升格进 `dm0` 或另挂主报） |
| DM1 | 半泄露 | 仅核对日把「沪市换股 0.00341%」或现货暂免/现货 0.04‰ 铺到全历史、铺到全部 venue、或把换股和现货合成一条（`invent_asof_leak_exchangeable_conversion_handling`）；**不得升格并列主报**，也不得写进 `dm0`（写死冻结：DM1 不升格），不得双挂 |
| DM2 | 诚实 / 换股与现货分开 | `exch_conversion_handling_honest=pit_conversion_apart_from_spot`（写死冻结）：缺 venue/业务类型或官方‰则 skip；沪市核对日换股 0.00341% 双向，禁止静默按现货暂免；深市缺官方换股另档‰则 skip。可交换现货只消费 DF，转债现货经手只消费 DB，股票经手切日只消费 S，转债过户只消费 DD，或显式旁路 |

把现货暂免铺到换股、把换股 0.00341% 抄到现货、把 DF 的现货沪深合成混进换股、把 DB 的转债现货经手混进换股、把 S 的股票经手切日混进换股另档，以及相对 DF / DB / S / DD 的对照截（`apply_spot_waiver_onto_conversion` / `copy_conversion_00341_onto_spot` / `confuse_DF_spot_merge_with_conversion` / `vs_DF_exch_spot_handling` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_DD_cb_transfer` / `missing_biz_type_not_skip`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dm0_primary_demo`。`vs_DF_exch_spot_handling` 只标记「有人把 DF 的可交换现货沪深合成和本页换股≠现货合成/混读」，**不得升格进 `dm0`**。`vs_DB_cb_handling` 只标记「有人把 DB 转债现货经手和本页可交换换股经手合成/混读」，**不得升格进 `dm0`**。`vs_S_stock_handling` 只标记「有人把 S 股票经手切日和本页换股另档合成/混读」，**不得升格进 `dm0`**。`vs_DD_cb_transfer` 只标记转债过户对照，**不得升格进 `dm0`**。DF 的现货、DB 的转债现货、S 的股票切日、DD 的转债过户只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dm0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺 venue/业务类型或官方‰则 skip；沪市核对日换股 0.00341% 双向，禁止静默按现货暂免；深市缺官方换股另档‰则 skip。方向随锚写死：**不要把核对日 0.00341% 或现货暂免/0.04‰ 铺满全历史**。`事实与坑` 2026-11-09 已写沪市「可交换公司债券换股交易」经手费与现货分列、深市现货与转债同档不要合成一句；换股另档不在 DF 的现货主报里，本页不重开 DF。转债现货经手留在 DB，股票经手切日留在 S，转债过户留在 DD，都不改。`params.G` 的 0.01 是无量纲相对门槛，不是换股经手费 0.00341%，也不是现货任何档。**禁把占位读成 0.00341%/0.04‰/暂免**。缺 venue、业务类型或官方‰则 skip，不用现货暂免、现货 0.04‰、自造‰或把占位 0.01 当成费率把换股腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dm0_primary_demo` / `params.Y`·G·N·Y2 / 换股与现货开关 / 桶 / 是否把 0.00341% 或现货暂免铺到全历史）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DM0）/ 半泄露组（DM1）相对诚实组（DM2）的成本差、误套截**显著且集中在换股经手费被套成现货档的桶**；分桶「现货暂免铺到换股 / 换股 0.00341% 抄到现货 / DF 现货合成混进换股 / 核对日泄露 / vs DF·DB·S·DD」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 0.00341% 或现货暂免冻成全历史唯一费率，也不把 `params.G` 的 0.01 读成换股经手费。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 DF 的可交换现货沪深合成、DB 的转债现货经手、S 的股票经手切日、DD 的转债过户、DL 的综合协议过户下浮、DK 的基金印花税、DJ 的基金证管费、DI 的大宗经手下浮、DH 的佣金双计、DG 的北交所档、DE 的转债证管费、DC 的转债印花税、DA 的基金过户、AX 的基金经手费、T 的股票证管费、U 的股票过户、V 的股票印花税、AC 的北交所涨跌幅与盘后、Q 的回转与涨跌幅、R 的股票 ETF 回转、O 的大宗通道、A 的板上容量、D 的成交时点、M 的盘后通道解释；或 `dm0_primary_demo` 与 `invent_asof_leak_exchangeable_conversion_handling` 双挂；或 DM1 升格并列主报；或 `apply_spot_waiver_onto_conversion` / `copy_conversion_00341_onto_spot` / `confuse_DF_spot_merge_with_conversion` / `vs_DF_exch_spot_handling` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_DD_cb_transfer` / `missing_biz_type_not_skip` 诊断桶升格主报；或把 DF 现货沪深合成、DB 转债现货经手、S 股票经手切日合成进 `dm0`；或实验字母 DM 与单字母 D/M 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成换股经手费 0.00341%；或把占位读成 0.00341%/0.04‰/暂免；或把核对日 0.00341% 写成已冻并铺满全历史；或缺 venue / 业务类型 / 官方‰仍按现货暂免把换股腿填上；或重开假设-T / 假设-AC / 假设-R / 假设-U / 假设-O / 假设-DI / 假设-V / 假设-DF / 假设-DB / 假设-S；或标纸面齐；或写成 A/D–DM纸面齐。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DM0/DM1/DM2。可交换现货走 DF 的沪深分列或显式旁路，不在本页改 DF，也不把 DF 的现货合成升成主报。转债现货经手走 DB，股票经手切日走 S，转债过户走 DD，都不改。报告成本差、误套截。不把 0.00341% 或现货暂免标成已冻的换股费率，也不把 `params.G` 的 0.01 读成换股经手费。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_spot_handling_on_exchangeable_conversion` / `invent_asof_leak_exchangeable_conversion_handling` / `apply_spot_waiver_onto_conversion` / `copy_conversion_00341_onto_spot` / `confuse_DF_spot_merge_with_conversion` / `vs_DF_exch_spot_handling` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_DD_cb_transfer` / `missing_biz_type_not_skip`

`apply_spot_waiver_onto_conversion`、`copy_conversion_00341_onto_spot`、`confuse_DF_spot_merge_with_conversion`、`vs_DF_exch_spot_handling`、`vs_DB_cb_handling`、`vs_S_stock_handling`、`vs_DD_cb_transfer`、`missing_biz_type_not_skip` 只作诊断桶：它们不是 `dm0`，也不是 DM1，**不得升格主报**。`vs_DF_exch_spot_handling` 没有对应的「DF 现货沪深合成 + 换股」合成主报。DF 的现货沪深合成只作诊断，**不得与换股≠现货合成后升格进 `dm0`**。DB 的转债现货经手只作诊断，**不得升格进 `dm0`**。S 的股票经手切日只作诊断，**不得升格进 `dm0`**。DD 的转债过户只作诊断，**不得升格进 `dm0`**。`invent_asof_leak_exchangeable_conversion_handling` 只服务 DM1，**不得升格进 `dm0`，不得双挂**。`invent_spot_handling_on_exchangeable_conversion` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把可交换债换股经手费按现货档抽，或静默按现货暂免，并拿去当诚实锚。
- 把 `params.G` 的 0.01 当成换股经手费 0.00341%。**尤重：`params.G` 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 0.00341%/0.04‰/暂免。**禁把占位读成 0.00341%/0.04‰/暂免**。
- 缺 venue、业务类型或官方‰仍不 skip，并用现货暂免、现货 0.04‰、自造‰或占位 0.01 把换股腿填上。
- 把核对日「沪市换股 0.00341% 双向」写成全历史唯一费率，并铺满全历史、铺到深市。方向是核对日换股与现货分开，不是全历史已冻费率。锚六键已写死冻结。
- 深市没有官方换股另档‰仍硬填一档（含把现货 0.04‰ 或沪市暂免抄成深市换股）。
- 把「可交换现货沪深已分列（DF）/ 转债现货经手已诚实（DB）/ 股票经手切日已诚实（S）/ 转债过户已诚实（DD）」写成「可交换债换股经手费已诚实」。不改 DF / DB / S / DD。
- 把 DF 的可交换现货经手费沪深合成和本页「换股≠现货」合成或混读后升格进 `dm0`。诊断桶 `vs_DF_exch_spot_handling` / `confuse_DF_spot_merge_with_conversion` 只作对照。
- 把 DB 可转债现货经手费和本页可交换换股经手费合成或混读后升格进 `dm0`。诊断桶 `vs_DB_cb_handling` 只作对照。
- 把 S 股票经手费切日和本页换股另档合成或混读后升格进 `dm0`。诊断桶 `vs_S_stock_handling` 只作对照。
- 把换股 0.00341% 抄到现货，或把现货暂免铺到换股，并升格进 `dm0`。诊断桶 `copy_conversion_00341_onto_spot` / `apply_spot_waiver_onto_conversion` 只作对照。不改 DF。
- 把 DD 转债过户和本页换股经手费合成后升格进 `dm0`。诊断桶 `vs_DD_cb_transfer` 只作对照。
- 缺业务类型仍不 skip，并升格进 `dm0`。诊断桶 `missing_biz_type_not_skip` 只作对照。
- `dm0_primary_demo` 与 `invent_asof_leak_exchangeable_conversion_handling` 双挂主报；DM1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DM 与单字母 D/M 或 params.Y/G/N 混读。
- 改 DL / DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / S / AX / T / U / V / AC / Q / R / A / D / M 正文；重开假设-T；重开假设-AC；重开假设-R；重开假设-U；重开假设-O；重开假设-DI；重开假设-V；重开假设-DF；重开假设-DB；重开假设-S；抢 A 真数队列；标纸面齐；写 A/D–DM纸面齐；开真数/回测/实盘；用复权价当费用基数；结论写成「换股费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权成交金额、交易日、**交易所 venue**（沪/深）、**业务类型**（可交换债换股 / 可交换债现货 / 可转债现货 / 股票；仅用于把腿分回 DF、DB、S 或本页）、**官方换股经手费‰是否在册**（缺则 skip，不发明数）。
- 证券类别只用于把腿分回 DF / DB / S / DD 等旁路页，不在本页改那些页。
- 没有 venue、业务类型或官方‰时，按写死冻结的 `exch_conversion_handling_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing` skip，不得按现货暂免或现货 0.04‰ 把换股腿填上，也不得用核对日 0.00341% 把腿填满全历史或填到深市缺档的日子。深市缺官方换股另档‰ → skip。
- 旁路消费：DF 的可交换现货经手费沪深分列、DB 的可转债现货经手费、S 的沪深股票竞价经手费切日、DD 的转债过户费、DL 的综合协议过户下浮、DK 的基金印花税、DJ 的基金证管费、DI 的大宗经手下浮、DH 的佣金双计、DG 的北交所经手费、DE 的转债证管费、DC 的转债印花税、DA 的场内基金过户费、AX 的基金经手费、T 的股票证管费、U 的股票过户费、V 的股票印花税、AC 的北交所涨跌幅与盘后、Q 的转债规则、R 的股票 ETF 回转、O 的大宗通道、M 的盘后通道之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** DF 的现货沪深合成、DB 的转债现货经手、S 的股票经手切日不收到本页主报。
- 未复权价；asof **写死冻结** `2026-10-16`。核对日方向「沪市换股 0.00341% 双向、禁止静默按现货暂免」是写死冻结的机制方向，不是已冻全历史费率。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`exch_conversion_handling_honest=pit_conversion_apart_from_spot`（换股与现货分开；沪市核对日换股 0.00341% 双向，禁止静默按现货暂免；深市缺官方换股另档‰则 skip；**禁止把 0.00341% 或现货暂免/0.04‰ 写成全历史唯一费率**）；`exch_conversion_handling_scope=sse_00341_conversion_not_spot_waiver`（沪市换股不走现货暂免；方向名，不是已冻费率）；`exch_conversion_handling_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing`（缺 venue/业务类型或官方‰则 skip）；`dm0_primary_demo=invent_spot_handling_on_exchangeable_conversion`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_exchangeable_conversion_handling` 双挂；DM1 不升格；诊断桶不升格主报；**禁把 DF 现货沪深合成、DB 转债现货经手、S 股票经手切日合成进 `dm0`**，只作对照/旁路，不得升格进 `dm0` 或另挂主报）；`exch_spot_handling_handoff=df_page`；`cb_handling_fee_handoff=db_page`；`ashare_fee_handoff=s_page`；`cb_transfer_fee_handoff=dd_page`；`merge_with_DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/A/D/M=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误套截 ΔExchConversionHandling / 净收益差 / DM1−DM2；**尤重 params.G 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档（量纲与语义不同）**；**禁把占位读成 0.00341%/0.04‰/暂免**；**params.Y/G/N ≠ 实验字母 DM ≠ 单字母 D/M**；**勿把 params.G 读成实验字母 DM，亦勿把单字母假设-D / 假设-M 读成双字母 DM**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成换股或现货费率）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #123。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`bc6df6d`（A/D–DL纸面齐已合，全长 `bc6df6d2e52da183e8ef5eac9e5c44adba046a72`）；三冻补丁基 tip=`6f7dc4ad` / `6f7dc4adea6e1787bfc44d6b68199312bba54961`；分支起点 HEAD=`6da664fc` / `6da664fc0a09ad8ba5fd531d595eb91ba6da4d2d`。**不改已冻 A–DL / DA–DK**。状态=预检有条件通过·三条已冻·待复检。三条已冻。禁止标纸面齐。未标纸面齐。不写 A/D–DM纸面齐。

---

## 8. 结论

（空；**预检有条件通过·三条已冻·待复检**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-10）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DM-20261110.md`（原样落入，不改结论；SHA256=`bc465789b4b81a403c45a361de00b9a13735d1eef0cf02dd8ac9c97785cd0537`；预检 2026-11-10；**结论：有条件通过**；tip基=`6f7dc4ad` / `6f7dc4adea6e1787bfc44d6b68199312bba54961`；本补丁分支起点 HEAD=`6da664fc` / `6da664fc0a09ad8ba5fd531d595eb91ba6da4d2d`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、误套截 ΔExchConversionHandling、净收益差、DM1−DM2 专项。**`params.Y` ≠ 实验字母 DM**；**`params.G` ≠ 实验字母 DM**；**`params.N` ≠ 实验字母 DM**；亦 ≠ 单字母假设-D / 假设-M。**勿把 `params.G` 读成实验字母 DM，亦勿把单字母假设-D / 假设-M 读成双字母 DM**。**尤重：`params.G` 的 `0.01` ≠ 换股经手费 0.00341% ≠ 现货任何档**（**params.G 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档**）。二者量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是换股经手费率，也不是现货暂免或 0.04‰。**禁把占位读成 0.00341%/0.04‰/暂免**。禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dm0_primary_demo`**：**写死冻结** **`invent_spot_handling_on_exchangeable_conversion`**（单一主报，单挂写死）。**禁止**与 **`invent_asof_leak_exchangeable_conversion_handling`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DM1 核对日把「沪市换股 0.00341%」或现货暂免/现货 0.04‰ 铺到全历史、铺到全部 venue、或把换股和现货合成一条只作半泄露对照，**不得升格与 dm0 并列主报**，也不得把 `invent_asof_leak_exchangeable_conversion_handling` 写进 `dm0`。`apply_spot_waiver_onto_conversion` / `copy_conversion_00341_onto_spot` / `confuse_DF_spot_merge_with_conversion` / `vs_DF_exch_spot_handling` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_DD_cb_transfer` / `missing_biz_type_not_skip` **只作诊断桶，不得升格主报**。DM1 / 诊断桶 **不升格**。**禁把 DF 可交换现货沪深合成 / DB 转债现货经手 / S 股票经手切日 合成/混读升格进 `dm0`**：这些只作对照/旁路，**不得升格进 `dm0`，不得另挂主报**。换股≠现货。

3. **可交换债换股经手费诚实锚六键升格写死（不可再写「建议」）**：`params.exch_conversion_handling_honest=pit_conversion_apart_from_spot`；`params.exch_conversion_handling_scope=sse_00341_conversion_not_spot_waiver`；`params.exch_conversion_handling_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺 venue/业务类型或官方‰ → skip；沪市核对日换股 0.00341% 双向，禁止静默按现货暂免；深市缺官方换股另档‰ → skip。禁止把核对日 0.00341% 或现货暂免/0.04‰ 铺满全历史。禁止跑后改锚，或用现货档 / 核对日现行费率 / 发明‰ / 缺 venue/业务类型或官方‰仍硬填 / 把 DF 可交换现货沪深合成、DB 转债现货经手或 S 股票经手切日升格进 dm0 冒充诚实 PIT。**禁把占位读成 0.00341%/0.04‰/暂免**。**禁把 params.G 的 0.01 读成换股经手费 0.00341%**。**换股≠现货**。

**硬分列保住**：DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠O≠A≠D≠M；**双字母 DM ≠ 单字母假设-D / 假设-M**；**params.Y / params.G / params.N ≠ 实验字母 DM ≠ 单字母 D/M**；**尤重 params.G 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档**；**禁把占位读成 0.00341%/0.04‰/暂免**；**可交换债换股经手费误套现货 ≠ DF可交换现货沪深合成 ≠ DB转债现货经手 ≠ S股票经手切日 ≠ DD转债过户**；不抢 A；不改已齐/已冻 DA～DL 及 A–DL 正文；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**不重开假设-DF**；**不重开假设-DB**；**不重开假设-S**；**禁把 DF 可交换现货沪深合成 / DB 转债现货经手 / S 股票经手切日 合成/混读升格进 dm0**。

**状态**：**预检有条件通过·三条已冻·待复检**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DM纸面齐**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-10 | 风控预检补丁·冻结三条写死——依据 `预检-假设DM-20261110.md`（SHA256=`bc465789b4b81a403c45a361de00b9a13735d1eef0cf02dd8ac9c97785cd0537`；结论=有条件通过；tip基=`6f7dc4ad` / `6f7dc4adea6e1787bfc44d6b68199312bba54961`；分支起点 HEAD=`6da664fc` / `6da664fc0a09ad8ba5fd531d595eb91ba6da4d2d`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔExchConversionHandling / 净收益差 / DM1−DM2；**params.Y/G/N ≠ 实验字母 DM ≠ 单字母 D/M**；**勿把 params.G 读成实验字母 DM，亦勿把单字母假设-D / 假设-M 读成双字母 DM**；**尤重 params.G 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档（量纲与语义不同）**；**禁把占位读成 0.00341%/0.04‰/暂免**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成换股或现货费率）；② `params.dm0_primary_demo=invent_spot_handling_on_exchangeable_conversion`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_exchangeable_conversion_handling` 双挂；DM1 不升格；诊断桶 `apply_spot_waiver_onto_conversion` / `copy_conversion_00341_onto_spot` / `confuse_DF_spot_merge_with_conversion` / `vs_DF_exch_spot_handling` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_DD_cb_transfer` / `missing_biz_type_not_skip` 不升格；**禁把 DF 可交换现货沪深合成 / DB 转债现货经手 / S 股票经手切日 合成/混读升格进 dm0**，只作对照/旁路，不得升格进 dm0 或另挂主报；换股≠现货）；③ 锚六键写死 `exch_conversion_handling_honest=pit_conversion_apart_from_spot` / `exch_conversion_handling_scope=sse_00341_conversion_not_spot_waiver` / `exch_conversion_handling_over_policy=skip_if_venue_or_biz_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`（缺 venue/业务类型或官方‰ → skip；沪市核对日换股 0.00341% 双向，禁止静默按现货暂免；深市缺官方换股另档‰ → skip；禁止把核对日 0.00341% 或现货暂免/0.04‰ 铺满全历史）。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DM纸面齐**；不改已齐/已冻 DA～DL 及 A–DL；不改假设-DA～假设-DL；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-U；不重开假设-O；不重开假设-DI；不重开假设-V；不重开假设-DF；不重开假设-DB；不重开假设-S；不开回测/真数/实盘。基于 tip=`6f7dc4ad`。 |
| 2026-11-09 | 新建纸面草稿（首次入库）；状态=草稿·待入库预检；三条尚未冻；禁止标纸面齐。可交换债换股经手费误套现货；`dm0_primary_demo` 建议 `invent_spot_handling_on_exchangeable_conversion`，单一主报，单挂，禁与 `invent_asof_leak_exchangeable_conversion_handling` 双挂，DM1 不升格；诊断桶 `apply_spot_waiver_onto_conversion` / `copy_conversion_00341_onto_spot` / `confuse_DF_spot_merge_with_conversion` / `vs_DF_exch_spot_handling` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_DD_cb_transfer` / `missing_biz_type_not_skip` 不升格；**尤重 DF 可交换现货经手费沪深合成 ≠ 本页「换股≠现货」，禁止合成/混读升格进 dm0**；**尤重 DB 可转债现货经手费 ≠ 本页可交换换股经手费，禁止合成进 dm0**；**尤重 S 股票经手费切日 ≠ 本页换股另档，禁止合成进 dm0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**尚未冻，不要写成已冻**，**params.Y/G/N ≠ 实验字母 DM ≠ 单字母 D/M**，且 **params.G 的 0.01 ≠ 换股经手费 0.00341% ≠ 现货任何档**，**禁把占位读成 0.00341%/0.04‰/暂免**；锚建议、未冻：`exch_conversion_handling_honest=pit_conversion_apart_from_spot` / scope=`sse_00341_conversion_not_spot_waiver` / over_policy=`skip_if_venue_or_biz_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`；口径：缺 venue/业务类型或官方‰则 skip；沪市核对日换股 0.00341% 双向，禁止静默按现货暂免；深市缺官方换股另档‰则 skip（**草稿方向，尚未冻，不要写成已冻**）；handoff：`exch_spot_handling_handoff=df_page`，`cb_handling_fee_handoff=db_page`，`ashare_fee_handoff=s_page`，`cb_transfer_fee_handoff=dd_page`；`merge_with_DL/DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/S/AX/T/U/V/AC/Q/R/O/A/D/M=False`；**DM≠DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠T≠U≠V≠AC≠Q≠R≠A≠D**；**双字母 DM ≠ 单字母假设-D / 假设-M**；**可交换债换股经手费误套现货 ≠ DF可交换现货沪深合成 ≠ DB转债现货经手 ≠ S股票经手切日 ≠ DD转债过户**；**未标纸面齐**；**不写 A/D–DM纸面齐**；结论栏空；不改已冻 A–DL / DA–DK；不改已齐假设-DA～假设-DL；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-U；不重开假设-O；不重开假设-DI；不重开假设-V；不重开假设-DF；不重开假设-DB；不重开假设-S；不写下一字母；不预留 #123；不开真数/回测/实盘。基 tip=`bc6df6d`（A/D–DL纸面齐已合，全长 `bc6df6d2e52da183e8ef5eac9e5c44adba046a72`；不改该 tip 上的 #110–#121，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文）。 |
