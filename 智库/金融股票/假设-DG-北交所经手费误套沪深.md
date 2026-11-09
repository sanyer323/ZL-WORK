# 假设-DG · 北交所经手费误套沪深（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `0984c53` 上清单 #115=DF 已收口（A/D–DF 已在 `e995ae0` 收口合入；其后 main 只多了周一喂养对照段，未改假设页，本页不改该段；**不改假设-DF 正文**，亦不改已齐 A–DF / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-T / 假设-S / 假设-AX / 假设-AC 及其他已存在假设页；**不重开假设-T**）后写下一草稿 DG；清单 #115=DF，本页占用 **#116=DG**；选题自 `事实与坑` 2026-10-30「北交所不是同一档……不要和沪深 0.0341‰ 合成一句」（S 只禁把北交所费率抄到沪深；AC 只把经手费另档留在诊断）；**新建实验 DG**  
状态：**草稿·待入库预检**（结论栏空；禁止把「北交所股票经手费静默套沪深 A 股经手费档 0.0341‰、或与沪深合成/混用、或缺 venue/官方 bps 仍不 skip」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**三条尚未冻**；**禁止标纸面齐**；**未标纸面齐**；**不改已齐 A–DF / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE**；尤其不改假设-S / 假设-AX / 假设-DB / 假设-DF / 假设-AC / 假设-DE / 假设-DD / 假设-DC / 假设-T / 假设-D / 假设-G；**不重开假设-T**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DG（#116）。一句话误开：回测把北交所股票经手费静默套用沪深 A 股经手费档 0.0341‰（或合成/混用），而非诚实锚北交所 0.0125% 双边；或缺 venue/官方 bps 仍不 skip，系统性改写北交所腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DG** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；占位 0.02；**params.Y ≠ 实验字母 DG**；**勿把 `params.Y` 读成实验字母 DG**）≠ **`params.G`**（同族门槛，占位 0.01；**params.G ≠ 实验字母 DG**；**尤重：`params.G` 的 0.01 ≠ 北交所 0.0125% ≠ 沪深 0.0341‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，0.0125% 是北交所股票经手费双边费率，0.0341‰ 是沪深 A 股经手费率）≠ **`params.N`**（失败/废单率差门槛；占位 0.05；**params.N ≠ 实验字母 DG**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DG ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 G**（涨跌幅规则 PIT 新股窗；**双字母 DG ≠ 单字母假设-G；严禁复用假设-G**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DG ≠ 单字母假设-A**）≠ **单字母实验 T**（证管费主报股票；**双字母 DG ≠ 单字母假设-T；严禁复用假设-T；不重开假设-T**）≠ 双字母 **DF**（可交换债经手费沪深分列）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **S**（沪深股票经手费）≠ **AX**（基金经手费）≠ **AC**（北交所涨跌幅与盘后）≠ **U**（股票过户费）≠ **V**（股票印花税）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）。**DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠AC≠T≠U≠V≠Q≠R≠A≠D**。**双字母 DG ≠ 单字母 D/G**。**params.Y/G/N ≠ 实验字母 DG；亦 ≠ 单字母 D/G**。**勿把 `params.G` 读成实验字母 DG，亦勿把单字母假设-D / 假设-G 读成双字母 DG**。**尤重：`params.G` 的 0.01 ≠ 北交所 0.0125% ≠ 沪深 0.0341‰**。

### 专节 · 双字母 DG ≠ 单字母假设-D / 假设-G；且 ≠ 假设-S / 假设-AX / 假设-DB / 假设-DF / 假设-AC（硬）

| 维度 | 对照页 | 本页假设-DG（双字母） |
|------|--------|----------------------|
| 题面 S | **沪深 A 股经手费**（三切日；现行 0.0341‰；`copy_bse_fee_to_hs=False` 只禁把北交所费率抄到沪深） | 沪深经手费族 ≠ 北交所经手费。本页专测**反方向**：北交所腿被套成沪深 0.0341‰。**DG≠S**；**不改 S**；不把 S 的 0.0341‰ 写成北交所诚实档；**禁把 S 的 `copy_bse_fee_to_hs` 升格进 `dg0`**；`fee_tier_handoff=s_page` |
| 题面 AX | **基金/ETF 经手费** | 基金经手费 ≠ 北交所股票经手费。**DG≠AX**；**不改 AX**；`fund_fee_handoff=ax_page` |
| 题面 DB | **可转债经手费**（主报转债腿误套 A 股档） | 可转债经手费 ≠ 北交所股票经手费。**DG≠DB**；**不改 DB**；`cb_handling_fee_handoff=db_page` |
| 题面 DF | **可交换债经手费沪深分列**（沪市债券现券暂免 vs 深市 0.04‰） | 可交换债经手费 ≠ 北交所股票经手费。**DG≠DF**；**不改 DF**；`exch_handling_fee_handoff=df_page` |
| 题面 AC | **北交所涨跌幅与盘后**（30% / 2026-07-06 盘后暂不实施；经手费另档只在 AC 作诊断） | 涨跌幅、盘后 ≠ 经手费误套。**DG≠AC**；**不改 AC**；**禁把 AC 的经手费另档声明升格进 `dg0`**；`bse_limit_aft_handoff=ac_page` |
| 题面 DE | **可转债证管费** | 证管费 ≠ 经手费误套。**DG≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债过户费** | 过户费 ≠ 经手费误套。**DG≠DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DC | **可转债印花税** | 印花税 ≠ 经手费误套。**DG≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 DA | **场内基金过户费** | 场内基金过户 ≠ 北交所经手费。**DG≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` 只旁路消费 |
| 题面 T | **证管费主报股票** | 证管费 ≠ 北交所经手费。**DG≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费** | 过户费 ≠ 北交所经手费。**DG≠U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 V | **股票印花税** | 印花税 ≠ 北交所经手费。**DG≠V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 Q | **可转债按股票规则回放**（回转、涨跌幅、收盘价、转股所得次日才可卖） | 规则混用 ≠ 北交所经手费。**DG≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 北交所经手费。**DG≠R**；**不改 R**；`stock_etf_rotation_handoff=r_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 北交所腿经手费。**DG≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 北交所经手费抽在哪一档。**双字母 DG ≠ 单字母假设-D**；**严禁复用假设-D**；**DG≠D**；**不改 D** |
| 题面 G | **涨跌幅规则 PIT 新股窗** | 新股无板窗 ≠ 北交所经手费。**双字母 DG ≠ 单字母假设-G**；**严禁复用假设-G**；**DG≠G**；**不改 G** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_sse_szse_handling_fee_on_bse`（**建议**单一主报，**尚未冻**；禁与 `invent_asof_leak_bse_handling_fee` 双挂；DG1 不升格；`vs_S_stock_handling` / `vs_AX_fund_handling` / `vs_DB_cb_handling` / `vs_DF_exch_handling` / `vs_AC_bse_limit_aft` 只作诊断对照，不升格主报） |
| 文档 | 清单实验 S / AX / DB / DF / AC / DE / DD / DC / DA / T / U / V / Q / R / A / D / G（**只读；禁止改写**） | `假设-DG-北交所经手费误套沪深.md`（新建） |
| 预检键 | 实验字母 S / AX / DB / DF / AC / DE / DD / DC / DA / T / U / V / Q / R / A / D / G / Y / G / N | 实验字母 **DG** / `dg0_primary_demo`；**不得**占用或改写预检 S/AX/DB/DF/AC/DE/DD/DC/DA/T/U/V/Q/R/A/D/G |

**禁止**：把 DG 写成「S / AX / DB / DF / AC / DE / DD / DC / DA / T / U / V / Q / R / A / D / G 的续篇」；把「沪深经手费已诚实（S）/ 基金经手费已诚实（AX）/ 转债经手费已诚实（DB）/ 可交换债沪深分列已诚实（DF）/ 北交所涨跌幅与盘后已诚实（AC）」写成「北交所经手费已诚实」；把实验字母 DG 与单字母 D/G 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-G 读成双字母 DG**；**尤重勿把 `params.G` 读成实验字母 DG**；**尤重 `params.G` 的 0.01 ≠ 北交所 0.0125% ≠ 沪深 0.0341‰（量纲与语义不同）**；把 `invent_asof_leak_bse_handling_fee` 升格进 `dg0`；把 S 的 `copy_bse_fee_to_hs` 或 AC 的经手费另档声明升格进 `dg0`。本页主键只用 `dg0` / `dg1` / `dg2` 与 `bse_handling_fee_*`。不写下一字母。

---

## 1. 一句话假设（可检验、可证伪）

同一北交所股票信号、同一未复权成交金额、同一交易所 venue 下，回测把北交所股票经手费静默套用沪深 A 股经手费档 0.0341‰（或合成/混用），或缺 venue/官方 bps 仍不 skip，相对「北交所股票现货经手费按 0.0125% 双边，禁止套沪深 0.0341‰，禁止与沪深合成/混用；缺 venue 或官方 bps 则 skip」的诚实组，会**系统性改写北交所腿成本**——相对诚实锚偏误。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误套截在标定噪声带内可忽略，且「静默套沪深 0.0341‰ / 合成混用 / 核对日泄露 / 缺 venue·官方 bps 仍不 skip / vs S·AX·DB·DF·AC」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 建议键（标准件占位；拉数前再定；本页不开跑；Y/G/N/Y2 · dg0 与锚 **三条尚未冻**）

```
# 配置建议键（见 §7；草稿·待入库预检；下列三条都是占位，尚未冻）
# 【消歧】params.Y = 显著性门槛；占位 0.02；**≠ 实验字母 DG ≠ 单字母假设-D / 假设-G**；勿把 params.Y 读成实验字母 DG
# 【消歧】params.G = 同族门槛；占位 0.01；**≠ 实验字母 DG ≠ 单字母 D/G**
# 【消歧】尤重：params.G 的 0.01 ≠ 北交所 0.0125% ≠ 沪深 0.0341‰（量纲与语义不同：无量纲相对门槛 ≠ 北交所经手费率% ≠ 沪深经手费率‰）
# 【消歧】params.N = 失败/废单率差门槛；占位 0.05；**≠ 实验字母 DG ≠ 单字母 D/G**
# params.Y2 占位 0.015
# params.Y / G / N / Y2               占位 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误套截 ΔBseHandlingFee / 净收益差 / DG1−DG2；**params.Y/G/N ≠ 实验字母 DG ≠ 单字母假设-D / 假设-G**；**尤重 params.G 的 0.01 ≠ 北交所 0.0125% ≠ 沪深 0.0341‰**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                    建议 next_open
# params.asof_check_date              建议 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  建议 skip
# params.bse_handling_fee_honest      建议 pit_bse_0125_not_sse_szse_0341
#   诚实锚方向：北交所股票现货经手费 0.0125% 双边
#   禁止套沪深 A 股经手费档 0.0341‰；禁止与沪深合成/混用
#   缺 venue 或官方 bps → skip
#   枚举是建议，尚未冻
#   不把 S 的沪深 0.0341‰ 写成北交所诚实档
#   不把 DB 的可转债经手费、DF 的可交换债沪深分列抄成北交所诚实锚
# params.bse_handling_fee_scope       建议 bse_stock_spot_apart_from_sse_szse
#   北交所股票现货经手费与沪深分列
#   北交所经手费 ≠ 沪深股票经手费（S）≠ 基金经手费（AX）≠ 可转债经手费（DB）≠ 可交换债经手费（DF）≠ 证管费（DE）≠ 过户费（DD）≠ 印花税（DC）
# params.bse_handling_fee_over_policy 建议 skip_if_venue_or_official_bps_missing
#   缺 venue 或官方 bps 则 skip；禁静默套沪深 0.0341‰；禁合成/混用后照填
# params.fee_tier_handoff             建议 s_page
#   消费 S 的沪深股票经手费，或显式旁路；沪深经手费族 ≠ 北交所经手费；不改 S
#   S 的 copy_bse_fee_to_hs 只作对照/旁路（方向是禁把北交所费率抄到沪深），不得升格进 dg0；不改 S
# params.fund_fee_handoff             建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；不改 AX
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的可转债经手费，或显式旁路；可转债经手费 ≠ 北交所；不改 DB
# params.exch_handling_fee_handoff    建议 df_page
#   消费 DF 的可交换债经手费沪深分列，或显式旁路；可交换债经手费 ≠ 北交所；不改 DF
# params.bse_limit_aft_handoff        建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；涨跌幅/盘后 ≠ 经手费；不改 AC
#   AC 的经手费另档声明只作对照/旁路，不得升格进 dg0
# params.cb_rule_handoff              建议 q_page
#   回转、涨跌幅、收盘价交 Q；本页只测北交所股票经手费是否被套成沪深档；不改 Q
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的转债印花税，或显式旁路；印花税 ≠ 经手费误套；不改 DC
# params.cb_transfer_fee_handoff      建议 dd_page
#   消费 DD 的转债过户费，或显式旁路；过户费 ≠ 经手费误套；不改 DD
# params.cb_csrc_fee_handoff          建议 de_page
#   消费 DE 的转债证管费，或显式旁路；证管费 ≠ 经手费误套；不改 DE
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；不改 DA
# params.stock_csrc_fee_handoff       建议 t_page
#   消费 T 的股票证管费，或显式旁路；不在本页重开假设-T，也不改 T
# params.stock_transfer_fee_handoff   建议 u_page
# params.stock_stamp_handoff          建议 v_page
# params.stock_etf_rotation_handoff   建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 北交所经手费；不改 R
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
#   成交时点与停牌交 D；双字母 DG ≠ 单字母假设-D；不改 D
# params.ipo_limit_window_handoff     建议 g_page
#   涨跌幅规则新股窗交 G；双字母 DG ≠ 单字母假设-G；不改 G
# params.bse_handling_fee_handoff     建议 self
# params.dg0_primary_demo             建议 invent_sse_szse_handling_fee_on_bse
#   单一主报占位；禁与 invent_asof_leak_bse_handling_fee 双挂；DG1 不升格；诊断桶不升格；尚未冻
#   半泄露名 invent_asof_leak_bse_handling_fee 只作对照，不得升格进 dg0
# params.dg0_invent_sse_szse_handling_fee_on_bse 建议 True
# params.dg1_asof_leak_bse_handling_fee_only 建议 True
#   半泄露对照；DG1 不升格并列主报；不得把 invent_asof_leak_bse_handling_fee 写进 dg0
# params.dg2_pit_bse_handling_fee     建议 True
# params.merge_with_S                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_DB                建议 False
# params.merge_with_DF                建议 False
# params.merge_with_AC                建议 False
# params.merge_with_DE                建议 False
# params.merge_with_DD                建议 False
# params.merge_with_DC                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_T                 建议 False
# params.merge_with_U                 建议 False
# params.merge_with_V                 建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_R                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_G                 建议 False
# params.missing_venue_or_official_bps_policy 建议 skip
# params.day_freq_proxy               建议 bse_handling_fee_sensitivity
# params.universe_rule                建议 bse_handling_fee_misapply_check
# params.redline_v0_exempt_scope      建议 position_industry_dg_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DG；勿把这个键读成实验 DG
```

### 2.2 三组对照（DG0 / DG1 / DG2）

| 组 | 角色 | 口径 |
|----|------|------|
| DG0 | 天真 / 误套沪深档 | 按 `dg0_primary_demo` **建议**单一主报 `invent_sse_szse_handling_fee_on_bse`（尚未冻）：把北交所股票经手费静默套用沪深 A 股经手费档 0.0341‰，或与沪深合成/混用。**禁**与 `invent_asof_leak_bse_handling_fee` 双挂主报 |
| DG1 | 半泄露 | 仅核对日把北交所经手费现行口径铺到全历史（建议名 `invent_asof_leak_bse_handling_fee`，仅对照、不进 `dg0`）；**不得升格并列主报**，也不得写进 `dg0` |
| DG2 | 诚实 / 北交所分列 | `bse_handling_fee_honest=pit_bse_0125_not_sse_szse_0341`（建议，尚未冻）：北交所股票现货经手费 0.0125% 双边，禁止套沪深 0.0341‰，禁止合成/混用。缺 venue 或官方 bps → skip。沪深股票经手费只消费 S，基金经手费只消费 AX，转债经手费只消费 DB，可交换债经手费只消费 DF，北交所涨跌幅与盘后只消费 AC，或显式旁路 |

静默套沪深 0.0341‰、合成/混用、缺 venue/官方 bps 仍不 skip，以及相对 S / AX / DB / DF / AC 的对照截（`vs_S_stock_handling` / `vs_AX_fund_handling` / `vs_DB_cb_handling` / `vs_DF_exch_handling` / `vs_AC_bse_limit_aft`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dg0_primary_demo`。S 页上的 `copy_bse_fee_to_hs`、AC 页上的经手费另档声明只作对照/旁路：**不得升格进 `dg0`**。DE / DD / DC 的对照桶同样只作诊断。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **建议** `2026-10-16`；fill_time **建议** `next_open`；fail **建议** `skip`。以上与诚实锚同属三条里的锚，**尚未冻**。`事实与坑` 2026-10-30 已写下北交所经手费不是沪深 0.0341‰ 那一档、不要合成一句；假设-S 只把「北交所费率抄到沪深」留在禁项；假设-AC 只把经手费另档留在诊断。本页只收反方向：北交所腿被静默套成沪深 0.0341‰（或合成/混用）。诚实方向是北交所 0.0125% 双边。不改 S / AX / DB / DF / AC。证管费留在 DE，过户费留在 DD，印花税留在 DC，都不改。`params.G` 的 0.01 是无量纲相对门槛，不是 0.0125%，也不是 0.0341‰。缺 venue 或官方 bps 则 skip，不用沪深档、合成费率或 0 把腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dg0_primary_demo` / `params.Y`·G·N·Y2 / 混口径开关 / 桶）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DG0）/ 半泄露组（DG1）相对诚实组（DG2）的成本差、误套截**显著且集中在北交所腿误套沪深档桶**；分桶「静默套沪深 0.0341‰ / 合成混用 / 核对日泄露 / 缺 venue·官方 bps 仍不 skip / vs S·AX·DB·DF·AC」不改变主结论方向。方向是相对诚实锚偏误。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 S 的沪深股票经手费、AX 的基金经手费、DB 的可转债经手费、DF 的可交换债经手费、AC 的北交所涨跌幅与盘后、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、Q 的回转与涨跌幅、T 的股票证管费、U/V 的股票过户与印花税、DA 的场内基金过户、R 的股票 ETF 回转、A 的板上容量、D 的成交时点、G 的新股涨跌幅窗解释；或 `dg0_primary_demo` 与 `invent_asof_leak_bse_handling_fee` 双挂；或 DG1 升格并列主报；或 `vs_S_stock_handling` / `vs_AX_fund_handling` / `vs_DB_cb_handling` / `vs_DF_exch_handling` / `vs_AC_bse_limit_aft` 诊断桶升格主报；或把 S 的 `copy_bse_fee_to_hs`、AC 的经手费另档声明升格进 `dg0`；或实验字母 DG 与单字母 D/G 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成北交所 0.0125% 或沪深 0.0341‰；或把北交所诚实锚写成沪深 0.0341‰；或缺 venue/官方 bps 仍不 skip；或重开假设-T。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DG0/DG1/DG2。沪深股票经手费走 S 的诚实档或显式旁路，不在本页改 S，也不把 S 的 `copy_bse_fee_to_hs` 升成主报。报告成本差、误套截。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_sse_szse_handling_fee_on_bse` / `invent_asof_leak_bse_handling_fee` / `vs_S_stock_handling` / `vs_AX_fund_handling` / `vs_DB_cb_handling` / `vs_DF_exch_handling` / `vs_AC_bse_limit_aft` / `missing_venue_or_official_bps_not_skip` / `vs_DE_cb_csrc` / `vs_DD_cb_transfer` / `vs_DC_cb_stamp` / `vs_DA_etf_transfer` / `vs_T_stock_csrc` / `vs_U_stock_transfer` / `vs_V_stock_stamp` / `vs_Q_cb_rule` / `vs_R_stock_etf_rotation` / `vs_A_board_capacity` / `vs_D_fill_time` / `vs_G_ipo_limit_window`

`vs_S_stock_handling`、`vs_AX_fund_handling`、`vs_DB_cb_handling`、`vs_DF_exch_handling`、`vs_AC_bse_limit_aft`、`missing_venue_or_official_bps_not_skip` 只作诊断桶：它们不是 `dg0`，也不是 DG1，**不得升格主报**。S 的 `copy_bse_fee_to_hs` 是「禁把北交所费率抄到沪深」，方向与本页主报相反，本页只引用作诊断，**不得升格进 `dg0`**。AC 的经手费另档声明同样只作诊断。`vs_DE_cb_csrc` / `vs_DD_cb_transfer` / `vs_DC_cb_stamp` 同样只作诊断。`invent_asof_leak_bse_handling_fee` 只服务 DG1，**不得升格进 `dg0`**。`invent_sse_szse_handling_fee_on_bse` 才是建议中的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把北交所股票经手费套成沪深 A 股 0.0341‰，或与沪深合成/混用，并拿去当诚实锚。
- 把 `params.G` 的 0.01 当成北交所 0.0125% 或沪深 0.0341‰。**尤重：`params.G` 的 0.01 ≠ 北交所 0.0125% ≠ 沪深 0.0341‰**。
- 缺 venue 或官方 bps 仍不 skip，并用沪深档、合成费率或 0 把腿填上。
- 把「沪深经手费已诚实（S）/ 基金经手费已诚实（AX）」写成「北交所经手费已诚实」。不改 S / AX。
- 把 S 的 `copy_bse_fee_to_hs` 升格进 `dg0`。该键只作对照/旁路，方向是禁把北交所费率抄到沪深。
- 把「转债经手费已诚实（DB）/ 可交换债沪深分列已诚实（DF）」写成「北交所经手费已诚实」。可转债 / 可交换债经手费 ≠ 北交所。不改 DB / DF。
- 把「北交所涨跌幅与盘后已诚实（AC）」写成「北交所经手费已诚实」。不改 AC。AC 的经手费另档声明不得升格进 `dg0`。
- 把「转债证管费已诚实（DE）/ 转债过户费已诚实（DD）/ 转债印花税已诚实（DC）」写成「北交所经手费已诚实」。证管费 / 过户费 / 印花税 ≠ 经手费误套。不改 DE / DD / DC。
- `dg0_primary_demo` 与 `invent_asof_leak_bse_handling_fee` 双挂主报；DG1 升格并列主报；诊断桶（`vs_S_stock_handling` / `vs_AX_fund_handling` / `vs_DB_cb_handling` / `vs_DF_exch_handling` / `vs_AC_bse_limit_aft`）升格为第二个主报。
- 实验字母 DG 与单字母 D/G 或 params.Y/G/N 混读。
- 改 S / AX / DB / DF / AC / DE / DD / DC / DA / T / U / V / Q / R / A / D / G 正文；重开假设-T；抢 A 真数队列；标纸面齐；开真数/回测/实盘；用复权价当经手费基数；结论写成「北交所费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、venue（北交所 / 沪 / 深）、证券类别（北交所股票现货 / 沪深股票 / 可转债 / 可交换债 / 场内基金）、未复权成交金额、交易日、官方经手费 bps（若已核到）。
- 没有 venue，或没有官方 bps 时，按 `bse_handling_fee_over_policy` 建议 skip，不得套沪深 0.0341‰，也不得合成/混用后照填。
- 旁路消费：S 的沪深股票经手费、AX 的基金经手费、DB 的转债经手费、DF 的可交换债经手费、AC 的北交所涨跌幅与盘后、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、DA 的场内基金过户费、T 的股票证管费、U 的股票过户费、V 的股票印花税、Q 的转债规则、R 的股票 ETF 回转之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** S 的 `copy_bse_fee_to_hs` 与 AC 的经手费另档声明不收到本页主报。
- 未复权价；asof **建议** `2026-10-16`（尚未冻）。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **建议键摘要（三条尚未冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`bse_handling_fee_honest=pit_bse_0125_not_sse_szse_0341`（北交所 0.0125% 双边，禁止套沪深 0.0341‰）；`bse_handling_fee_scope=bse_stock_spot_apart_from_sse_szse`（北交所股票现货经手费与沪深分列）；`bse_handling_fee_over_policy=skip_if_venue_or_official_bps_missing`（缺 venue/官方 bps 则 skip）；`dg0_primary_demo=invent_sse_szse_handling_fee_on_bse`（**建议**单一主报；禁与 `invent_asof_leak_bse_handling_fee` 双挂；DG1 不升格；诊断桶不升格主报）；`fee_tier_handoff=s_page`；`fund_fee_handoff=ax_page`；`cb_handling_fee_handoff=db_page`；`exch_handling_fee_handoff=df_page`；`bse_limit_aft_handoff=ac_page`；`merge_with_S/AX/DB/DF/AC/DE/DD/DC/DA/T/U/V/Q/R/A/D=False`（另 `merge_with_G=False`）。
- `params.Y/G/N/Y2` **占位** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误套截 ΔBseHandlingFee / 净收益差 / DG1−DG2；**尤重 params.G 的 0.01 ≠ 北交所 0.0125% ≠ 沪深 0.0341‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DG ≠ 单字母 D/G**；**勿把 params.G 读成实验字母 DG，亦勿把单字母假设-D / 假设-G 读成双字母 DG**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`0984c53`（A/D–DF 收口点 `e995ae0`）。

---

## 8. 结论

（空；草稿·待入库预检；三条尚未冻；未标纸面齐；禁止标纸面齐。）

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；北交所经手费误套沪深；`dg0_primary_demo` 建议 `invent_sse_szse_handling_fee_on_bse`，单一主报，禁与 `invent_asof_leak_bse_handling_fee` 双挂，DG1 不升格；诊断桶 `vs_S_stock_handling` / `vs_AX_fund_handling` / `vs_DB_cb_handling` / `vs_DF_exch_handling` / `vs_AC_bse_limit_aft` 不升格；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DG ≠ 单字母 D/G**，且 **params.G 的 0.01 ≠ 北交所 0.0125% ≠ 沪深 0.0341‰**；锚建议 `bse_handling_fee_honest=pit_bse_0125_not_sse_szse_0341` / scope=`bse_stock_spot_apart_from_sse_szse` / over_policy=`skip_if_venue_or_official_bps_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；handoff：`fee_tier_handoff=s_page`，`fund_fee_handoff=ax_page`，`cb_handling_fee_handoff=db_page`，`exch_handling_fee_handoff=df_page`，`bse_limit_aft_handoff=ac_page`；`merge_with_S/AX/DB/DF/AC/DE/DD/DC/DA/T/U/V/Q/R/A/D=False`；**DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠AC≠T≠U≠V≠Q≠R≠A≠D**；**双字母 DG ≠ 单字母假设-D / 假设-G**；vs S/AX：沪深/其他经手费族 ≠ 北交所经手费，不改 S/AX；vs DF/DB：可交换/可转债经手费 ≠ 北交所，不改 DF/DB；vs AC：北交所涨跌幅与盘后 ≠ 经手费，不改 AC；vs DE/DD/DC：证管费/过户费/印花税 ≠ 经手费误套，不改 DE/DD/DC；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；不改已齐 A–DF / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE 及其他已存在假设页；不重开假设-T；不写下一字母；不开真数/回测/实盘）。基 tip=`0984c53`（A/D–DF 收口点 `e995ae0745a377679eebaf2f0cbbbb72856be509`；本次提交前 HEAD `0984c53b447b822611da864ce2ff1cd3934f842f`；不改该 tip 上的周一喂养对照段） |
