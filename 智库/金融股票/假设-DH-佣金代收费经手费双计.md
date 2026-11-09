# 假设-DH · 佣金已含代收费再外加经手费双计（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `48ffa7ee` 上清单 #116=DG 已收口（A/D–DG纸面齐已合入该 tip；**不改假设-DG 正文**，亦不改已齐 A–DG / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-T / 假设-S / 假设-AX / 假设-AC / 假设-R / 假设-H 及其他已存在假设页；**不重开假设-T**）后写下一草稿 DH；清单 #116=DG，本页占用 **#117=DH**；选题是佣金侧「已含代收费仍再外加经手费」的双计机制；假设-S 只收经手费切日，假设-T 只收证管费，假设-AX 只收基金档，假设-DG 只收北交所档；**新建实验 DH**；**方向2/3本轮不另立**  
状态：**草稿·待入库预检**（结论栏空；禁止把「佣金已含代收费/经手费时仍再外加经手费，或缺『佣金是否已含代收费』标志时仍硬加」当诚实成本；**禁止冻死具体佣金‰**（因券商而异）；不抢实验 A 真数队列；本页不开回测；不催 8765；**三条尚未冻**；**禁止标纸面齐**；**未标纸面齐**；**不改已齐 A–DG / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF**；尤其不改假设-S / 假设-T / 假设-AX / 假设-DG / 假设-DF / 假设-DE / 假设-DD / 假设-DC / 假设-DB / 假设-DA / 假设-AC / 假设-D / 假设-H；**不重开假设-T**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DH（#117）。一句话误开：回测在佣金已含代收费/经手费时仍再外加经手费（gross+handling 双计），或在缺「佣金是否已含代收费」标志时仍硬加，系统性改写成本（相对诚实锚偏误）；未含才可分列加。

> **字母消歧（硬）**：本页**实验字母 DH** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；占位 0.02；**params.Y ≠ 实验字母 DH**；**勿把 `params.Y` 读成实验字母 DH**）≠ **`params.G`**（同族门槛，占位 0.01；**params.G ≠ 实验字母 DH**；**尤重：`params.G` 的 0.01 ≠ 任何佣金‰ / 经手费‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是佣金费率，也不是经手费费率）≠ **`params.N`**（失败/废单率差门槛；占位 0.05；**params.N ≠ 实验字母 DH**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DH ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 H**（退市整理期；**双字母 DH ≠ 单字母假设-H；严禁复用假设-H**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DH ≠ 单字母假设-A**）≠ **单字母实验 T**（证管费主报股票；**双字母 DH ≠ 单字母假设-T；严禁复用假设-T；不重开假设-T**）≠ 双字母 **DG**（北交所经手费）≠ **DF**（可交换债经手费沪深分列）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **S**（沪深股票经手费切日）≠ **AX**（基金经手费）≠ **AC**（北交所涨跌幅与盘后）≠ **U**（股票过户费）≠ **V**（股票印花税）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）。**DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠AC≠T≠U≠V≠Q≠R≠A≠D**。**双字母 DH ≠ 单字母 D/H**。**params.Y/G/N ≠ 实验字母 DH；亦 ≠ 单字母 D/H**。**勿把 `params.G` 读成实验字母 DH，亦勿把单字母假设-D / 假设-H 读成双字母 DH**。**尤重：`params.G` 的 0.01 ≠ 任何佣金‰ / 经手费‰**。**双计机制 ≠ S 切日 ≠ DG 北交所档 ≠ T 证管费 ≠ AX 基金档**。

### 专节 · 双字母 DH ≠ 单字母假设-D / 假设-H；且 ≠ 假设-S / 假设-T / 假设-AX / 假设-DG（硬）

| 维度 | 对照页 | 本页假设-DH（双字母） |
|------|--------|----------------------|
| 题面 S | **沪深 A 股经手费切日**（当时有效档；佣金分层在 S 只作切日旁路） | 经手费切日 ≠ 佣金双计机制。本页专测：佣金已含代收费时仍再外加经手费。**DH≠S**；**不改 S**；**禁把 S 的切日或演示键升格进 `dh0`**；`ashare_fee_handoff=s_page`；诊断桶 `vs_S_handling_tier` 不升格 |
| 题面 T | **证管费主报股票**（代收进佣金口径在 T） | 证管费 ≠ 佣金双计机制。**DH≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`csrc_fee_handoff=t_page`；诊断桶 `vs_T_csrc_in_commission` 不升格 |
| 题面 AX | **基金/ETF 经手费档** | 基金档 ≠ 佣金双计机制。**DH≠AX**；**不改 AX**；`fund_fee_handoff=ax_page` |
| 题面 DG | **北交所经手费档**（与沪深分列） | 北交所档 ≠ 佣金双计机制。**DH≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DF | **可交换债经手费沪深分列** | 可交换债经手费 ≠ 本机制。**DH≠DF**；**不改 DF**；`exch_handling_fee_handoff=df_page` |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 本机制。**DH≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债过户费** | 转债过户费 ≠ 本机制。**DH≠DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DC | **可转债印花税** | 转债印花税 ≠ 本机制。**DH≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 DB | **可转债经手费** | 转债经手费 ≠ 本机制。**DH≠DB**；**不改 DB**；`cb_handling_fee_handoff=db_page` |
| 题面 DA | **场内基金过户费** | 场内基金过户 ≠ 本机制。**DH≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` 只旁路消费 |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 佣金双计。**DH≠AC**；**不改 AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 U | **股票过户费** | 过户费 ≠ 佣金双计。**DH≠U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 V | **股票印花税** | 印花税 ≠ 佣金双计。**DH≠V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 佣金双计。**DH≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 佣金双计。**DH≠R**；**不改 R**；`stock_etf_rotation_handoff=r_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 佣金双计。**DH≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 佣金是否再外加经手费。**双字母 DH ≠ 单字母假设-D**；**严禁复用假设-D**；**DH≠D**；**不改 D** |
| 题面 H | **退市整理期** | 整理期窗口 ≠ 佣金双计。**双字母 DH ≠ 单字母假设-H**；**严禁复用假设-H**；**DH≠H**；**不改 H** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_double_count_handling_on_gross_commission`（**建议**单一主报，**尚未冻**；禁与 `invent_asof_leak_commission_handling_double` 双挂；DH1 不升格；`gross_plus_handling` / `net_commission_switch_inverted` / `vs_S_handling_tier` / `vs_T_csrc_in_commission` / `freeze_commission_bps_forbidden` 只作诊断对照，不升格主报） |
| 文档 | 清单实验 S / T / AX / DG / DF / DE / DD / DC / DB / DA / AC / U / V / Q / R / A / D / H（**只读；禁止改写**） | `假设-DH-佣金代收费经手费双计.md`（新建） |
| 预检键 | 实验字母 S / T / AX / DG / DF / DE / DD / DC / DB / DA / AC / U / V / Q / R / A / D / H / Y / G / N | 实验字母 **DH** / `dh0_primary_demo`；**不得**占用或改写预检 S/T/AX/DG/DF/DE/DD/DC/DB/DA/AC/U/V/Q/R/A/D/H |

**禁止**：把 DH 写成「S / T / AX / DG / DF / DE / DD / DC / DB / DA / AC / U / V / Q / R / A / D / H 的续篇」；把「经手费切日已诚实（S）/ 证管费已诚实（T）/ 基金档已诚实（AX）/ 北交所档已诚实（DG）」写成「佣金双计已诚实」；把实验字母 DH 与单字母 D/H 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-H 读成双字母 DH**；**尤重勿把 `params.G` 读成实验字母 DH**；**尤重 `params.G` 的 0.01 ≠ 任何佣金‰ / 经手费‰（量纲与语义不同）**；**禁止冻死具体佣金‰**；把 `invent_asof_leak_commission_handling_double` 升格进 `dh0`；把诊断桶 `gross_plus_handling` / `net_commission_switch_inverted` / `vs_S_handling_tier` / `vs_T_csrc_in_commission` / `freeze_commission_bps_forbidden` 升格进 `dh0`。本页主键只用 `dh0` / `dh1` / `dh2` 与 `commission_handling_*`。**方向2/3本轮不另立**。不写下一字母。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权成交金额下，回测在佣金已含代收费/经手费时仍再外加经手费（gross+handling 双计），或在缺「佣金是否已含代收费」标志时仍硬加，相对「缺标志则 skip；已含则不得再加经手费；未含才可分列加；不冻死具体佣金‰」的诚实组，会**系统性改写成本**——相对诚实锚偏误。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、双计截在标定噪声带内可忽略，且「已含仍再加 / 缺标志仍硬加 / 核对日泄露 / 净佣金开关反接 / vs S·T·AX·DG」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 建议键（标准件占位；拉数前再定；本页不开跑；Y/G/N/Y2 · dh0 与锚 **三条尚未冻**）

```
# 配置建议键（见 §7；草稿·待入库预检；下列三条都是占位，尚未冻）
# 【消歧】params.Y = 显著性门槛；占位 0.02；**≠ 实验字母 DH ≠ 单字母假设-D / 假设-H**；勿把 params.Y 读成实验字母 DH
# 【消歧】params.G = 同族门槛；占位 0.01；**≠ 实验字母 DH ≠ 单字母 D/H**
# 【消歧】尤重：params.G 的 0.01 ≠ 任何佣金‰ / 经手费‰（量纲与语义不同：无量纲相对门槛 ≠ 佣金费率‰ ≠ 经手费费率‰）
# 【消歧】params.N = 失败/废单率差门槛；占位 0.05；**≠ 实验字母 DH ≠ 单字母 D/H**
# params.Y2 占位 0.015
# params.Y / G / N / Y2               占位 0.02/0.01/0.05/0.015（相对门槛：成本差 / 双计截 ΔCommissionHandling / 净收益差 / DH1−DH2；**params.Y/G/N ≠ 实验字母 DH ≠ 单字母假设-D / 假设-H**；**尤重 params.G 的 0.01 ≠ 任何佣金‰ / 经手费‰**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成佣金‰）
# params.fill_time                    建议 next_open
# params.asof_check_date              建议 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  建议 skip
# params.commission_handling_honest   建议 pit_no_double_count_gross_plus_handling
#   诚实锚方向：已含代收费/经手费则不得再外加经手费
#   未含才可分列加
#   缺「佣金是否已含代收费」标志 → skip
#   禁止冻死具体佣金‰（因券商而异）；本键不携带佣金‰
#   枚举是建议，尚未冻
#   不把 S 的经手费切日、T 的证管费、AX 的基金档、DG 的北交所档写成佣金双计诚实锚
# params.commission_handling_scope    建议 gross_includes_exchange_fee_no_readd
#   佣金已含交易所代收经手费时，不得再加一遍
#   双计机制 ≠ 经手费切日（S）≠ 证管费（T）≠ 基金档（AX）≠ 北交所档（DG）≠ 可交换债经手费（DF）≠ 转债证管费（DE）≠ 转债过户费（DD）≠ 转债印花税（DC）≠ 转债经手费（DB）≠ 场内基金过户（DA）
# params.commission_handling_over_policy 建议 skip_if_commission_inclusion_flag_missing
#   缺「佣金是否已含代收费」标志则 skip；禁在缺标志时仍硬加；禁已含再外加
# params.ashare_fee_handoff           建议 s_page
#   消费 S 的沪深股票经手费切日，或显式旁路；经手费切日 ≠ 佣金双计；不改 S
#   S 的切日与「已含仍再叠」演示只作对照/旁路，不得升格进 dh0；不改 S
# params.csrc_fee_handoff             建议 t_page
#   消费 T 的股票证管费，或显式旁路；不在本页重开假设-T，也不改 T
#   诊断桶 vs_T_csrc_in_commission 不得升格进 dh0
# params.fund_fee_handoff             建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；基金档 ≠ 佣金双计；不改 AX
# params.bse_fee_handoff              建议 dg_page
#   消费 DG 的北交所经手费档，或显式旁路；北交所档 ≠ 佣金双计；不改 DG
# params.exch_handling_fee_handoff    建议 df_page
#   消费 DF 的可交换债经手费沪深分列，或显式旁路；不改 DF
# params.cb_csrc_fee_handoff          建议 de_page
#   消费 DE 的转债证管费，或显式旁路；不改 DE
# params.cb_transfer_fee_handoff      建议 dd_page
#   消费 DD 的转债过户费，或显式旁路；不改 DD
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的转债印花税，或显式旁路；不改 DC
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的可转债经手费，或显式旁路；不改 DB
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；不改 DA
# params.bse_limit_aft_handoff        建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；不改 AC
# params.cb_rule_handoff              建议 q_page
#   回转、涨跌幅、收盘价交 Q；本页只测佣金双计；不改 Q
# params.stock_transfer_fee_handoff   建议 u_page
# params.stock_stamp_handoff          建议 v_page
# params.stock_etf_rotation_handoff   建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 佣金双计；不改 R
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
#   成交时点与停牌交 D；双字母 DH ≠ 单字母假设-D；不改 D
# params.delist_window_handoff        建议 h_page
#   退市整理期交 H；双字母 DH ≠ 单字母假设-H；不改 H
# params.commission_handling_handoff  建议 self
# params.dh0_primary_demo             建议 invent_double_count_handling_on_gross_commission
#   单一主报占位；禁与 invent_asof_leak_commission_handling_double 双挂；DH1 不升格；诊断桶不升格；尚未冻
#   半泄露名 invent_asof_leak_commission_handling_double 只作对照，不得升格进 dh0
#   诊断桶 gross_plus_handling / net_commission_switch_inverted / vs_S_handling_tier / vs_T_csrc_in_commission / freeze_commission_bps_forbidden 不得升格进 dh0
# params.dh0_invent_double_count_handling_on_gross_commission 建议 True
# params.dh1_asof_leak_commission_handling_double_only 建议 True
#   半泄露对照；DH1 不升格并列主报；不得把 invent_asof_leak_commission_handling_double 写进 dh0
# params.dh2_pit_no_double_count      建议 True
# params.merge_with_S                 建议 False
# params.merge_with_T                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_DG                建议 False
# params.merge_with_DF                建议 False
# params.merge_with_DE                建议 False
# params.merge_with_DD                建议 False
# params.merge_with_DC                建议 False
# params.merge_with_DB                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_AC                建议 False
# params.merge_with_U                 建议 False
# params.merge_with_V                 建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_R                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_H                 建议 False
# params.missing_commission_inclusion_flag_policy 建议 skip
# params.day_freq_proxy               建议 commission_handling_double_count_sensitivity
# params.universe_rule                建议 commission_handling_double_count_check
# params.redline_v0_exempt_scope      建议 position_industry_dh_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DH；勿把这个键读成实验 DH
#   方向2/3本轮不另立：不另挂主报，不预留下一号
```

### 2.2 三组对照（DH0 / DH1 / DH2）

| 组 | 角色 | 口径 |
|----|------|------|
| DH0 | 天真 / 已含仍再加 | 按 `dh0_primary_demo` **建议**单一主报 `invent_double_count_handling_on_gross_commission`（尚未冻）：佣金已含代收费/经手费时仍再外加经手费（gross+handling 双计）。**禁**与 `invent_asof_leak_commission_handling_double` 双挂主报 |
| DH1 | 半泄露 | 仅核对日把「佣金是否已含代收费」的现行开关铺到全历史（建议名 `invent_asof_leak_commission_handling_double`，仅对照、不进 `dh0`）；**不得升格并列主报**，也不得写进 `dh0` |
| DH2 | 诚实 / 不得双计 | `commission_handling_honest=pit_no_double_count_gross_plus_handling`（建议，尚未冻）：缺「佣金是否已含代收费」标志则 skip；已含则不得再加经手费；未含才可分列加。不冻死具体佣金‰。经手费切日只消费 S，证管费只消费 T，基金档只消费 AX，北交所档只消费 DG，或显式旁路 |

已含仍再加、缺标志仍硬加、净佣金开关反接、以及相对 S / T 的对照截（`gross_plus_handling` / `net_commission_switch_inverted` / `vs_S_handling_tier` / `vs_T_csrc_in_commission` / `freeze_commission_bps_forbidden`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dh0_primary_demo`。`freeze_commission_bps_forbidden` 只标记「有人把具体佣金‰冻进本页」这一类失效，**本页不给出、也不占位任何具体佣金‰**。S 的切日、T 的证管费、AX 的基金档、DG 的北交所档只作对照/旁路：**不得升格进 `dh0`**。**方向2/3本轮不另立。**

### 2.3 费用窗可落点（写明但不真跑）

本页不设佣金‰切日。佣金因券商而异，**禁止冻死具体佣金‰**。主窗建议占位、待预检，起止日仍空着。asof **建议** `2026-10-16`；fill_time **建议** `next_open`；fail **建议** `skip`。以上与诚实锚同属三条里的锚，**尚未冻**。机制红线只有一句：缺「佣金是否已含代收费」标志则 skip；已含则不得再加经手费；未含才可分列加。经手费切日留在 S，证管费留在 T，基金档留在 AX，北交所档留在 DG，都不改。可交换债经手费留在 DF，转债证管费留在 DE，转债过户费留在 DD，转债印花税留在 DC，转债经手费留在 DB，场内基金过户留在 DA，都不改。`params.G` 的 0.01 是无量纲相对门槛，不是任何佣金‰，也不是任何经手费‰。缺标志则 skip，不用「再加一遍」或自造佣金‰把腿填上。**方向2/3本轮不另立。** 本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dh0_primary_demo` / `params.Y`·G·N·Y2 / 含代收标志开关 / 桶 / 任何佣金‰）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DH0）/ 半泄露组（DH1）相对诚实组（DH2）的成本差、双计截**显著且集中在已含仍再加的桶**；分桶「已含仍再加 / 缺标志仍硬加 / 核对日泄露 / 净佣金开关反接 / vs S·T·AX·DG」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖、也不产出一个具体佣金‰。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 S 的经手费切日、T 的证管费、AX 的基金档、DG 的北交所档、DF 的可交换债经手费、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、DA 的场内基金过户、AC 的北交所涨跌幅与盘后、Q 的回转与涨跌幅、U/V 的股票过户与印花税、R 的股票 ETF 回转、A 的板上容量、D 的成交时点、H 的退市整理期解释；或 `dh0_primary_demo` 与 `invent_asof_leak_commission_handling_double` 双挂；或 DH1 升格并列主报；或 `gross_plus_handling` / `net_commission_switch_inverted` / `vs_S_handling_tier` / `vs_T_csrc_in_commission` / `freeze_commission_bps_forbidden` 诊断桶升格主报；或实验字母 DH 与单字母 D/H 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成任何佣金‰或经手费‰；或冻死具体佣金‰；或缺「佣金是否已含代收费」标志仍硬加；或重开假设-T；或本轮另立方向2/3。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DH0/DH1/DH2。沪深股票经手费走 S 的诚实切日或显式旁路，不在本页改 S，也不把 S 的切日升成主报。报告成本差、双计截。不报告、不标定具体佣金‰。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_double_count_handling_on_gross_commission` / `invent_asof_leak_commission_handling_double` / `gross_plus_handling` / `net_commission_switch_inverted` / `vs_S_handling_tier` / `vs_T_csrc_in_commission` / `freeze_commission_bps_forbidden` / `missing_commission_inclusion_flag_not_skip` / `vs_AX_fund_handling` / `vs_DG_bse_handling` / `vs_DF_exch_handling` / `vs_DE_cb_csrc` / `vs_DD_cb_transfer` / `vs_DC_cb_stamp` / `vs_DB_cb_handling` / `vs_DA_etf_transfer` / `vs_AC_bse_limit_aft` / `vs_U_stock_transfer` / `vs_V_stock_stamp` / `vs_Q_cb_rule` / `vs_R_stock_etf_rotation` / `vs_A_board_capacity` / `vs_D_fill_time` / `vs_H_delist_window`

`gross_plus_handling`、`net_commission_switch_inverted`、`vs_S_handling_tier`、`vs_T_csrc_in_commission`、`freeze_commission_bps_forbidden`、`missing_commission_inclusion_flag_not_skip` 只作诊断桶：它们不是 `dh0`，也不是 DH1，**不得升格主报**。`freeze_commission_bps_forbidden` 没有对应的佣金‰数值。S 的经手费切日、T 的证管费只作诊断，**不得升格进 `dh0`**。`invent_asof_leak_commission_handling_double` 只服务 DH1，**不得升格进 `dh0`**。`invent_double_count_handling_on_gross_commission` 才是建议中的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 在佣金已含代收费/经手费时仍再外加经手费，并拿去当诚实锚。
- 把 `params.G` 的 0.01 当成任何佣金‰或经手费‰。**尤重：`params.G` 的 0.01 ≠ 任何佣金‰ / 经手费‰**。
- 缺「佣金是否已含代收费」标志仍不 skip，并用再加一遍或自造佣金‰把腿填上。
- 冻死具体佣金‰。佣金因券商而异，本页只守「不得双计」。
- 把「经手费切日已诚实（S）/ 证管费已诚实（T）/ 基金档已诚实（AX）/ 北交所档已诚实（DG）」写成「佣金双计已诚实」。不改 S / T / AX / DG。
- 把 S 的切日或 T 的证管费升格进 `dh0`。诊断桶 `vs_S_handling_tier` / `vs_T_csrc_in_commission` 只作对照。
- 把「可交换债经手费已诚实（DF）/ 转债证管费已诚实（DE）/ 转债过户费已诚实（DD）/ 转债印花税已诚实（DC）/ 转债经手费已诚实（DB）/ 场内基金过户已诚实（DA）」写成「佣金双计已诚实」。不改 DF / DE / DD / DC / DB / DA。
- `dh0_primary_demo` 与 `invent_asof_leak_commission_handling_double` 双挂主报；DH1 升格并列主报；诊断桶（`gross_plus_handling` / `net_commission_switch_inverted` / `vs_S_handling_tier` / `vs_T_csrc_in_commission` / `freeze_commission_bps_forbidden`）升格为第二个主报。
- 实验字母 DH 与单字母 D/H 或 params.Y/G/N 混读。
- 改 S / T / AX / DG / DF / DE / DD / DC / DB / DA / AC / U / V / Q / R / A / D / H 正文；重开假设-T；另立方向2/3；抢 A 真数队列；标纸面齐；开真数/回测/实盘；用复权价当费用基数；结论写成「佣金更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权成交金额、交易日、证券类别（仅用于把腿交回 S/T/AX/DG 等旁路）、**佣金是否已含代收费**标志。
- 没有该标志时，按 `commission_handling_over_policy` 建议 skip，不得再外加经手费，也不得补一个具体佣金‰。
- 旁路消费：S 的沪深股票经手费切日、T 的股票证管费、AX 的基金经手费、DG 的北交所经手费、DF 的可交换债经手费、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、DA 的场内基金过户费、AC 的北交所涨跌幅与盘后、U 的股票过户费、V 的股票印花税、Q 的转债规则、R 的股票 ETF 回转之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** S 的切日与 T 的证管费不收到本页主报。
- 未复权价；asof **建议** `2026-10-16`（尚未冻）。本页不要求、也不接收一份「标准佣金‰」。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **建议键摘要（三条尚未冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`commission_handling_honest=pit_no_double_count_gross_plus_handling`（已含则不得再加经手费；未含才可分列加；禁止冻死具体佣金‰）；`commission_handling_scope=gross_includes_exchange_fee_no_readd`（已含代收则不再外加）；`commission_handling_over_policy=skip_if_commission_inclusion_flag_missing`（缺标志则 skip）；`dh0_primary_demo=invent_double_count_handling_on_gross_commission`（**建议**单一主报；禁与 `invent_asof_leak_commission_handling_double` 双挂；DH1 不升格；诊断桶不升格主报）；`ashare_fee_handoff=s_page`；`csrc_fee_handoff=t_page`；`fund_fee_handoff=ax_page`；`bse_fee_handoff=dg_page`；`merge_with_S/T/AX/DG/DF/DE/DD/DC/DB/DA/AC/U/V/Q/R/A/D=False`（另 `merge_with_H=False`）。
- `params.Y/G/N/Y2` **占位** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 双计截 ΔCommissionHandling / 净收益差 / DH1−DH2；**尤重 params.G 的 0.01 ≠ 任何佣金‰ / 经手费‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DH ≠ 单字母 D/H**；**勿把 params.G 读成实验字母 DH，亦勿把单字母假设-D / 假设-H 读成双字母 DH**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。**方向2/3本轮不另立。**
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`48ffa7ee`（A/D–DG纸面齐已合）。

---

## 8. 结论

（空；草稿·待入库预检；三条尚未冻；未标纸面齐；禁止标纸面齐；禁止冻死具体佣金‰。）

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；佣金已含代收费再外加经手费双计；`dh0_primary_demo` 建议 `invent_double_count_handling_on_gross_commission`，单一主报，禁与 `invent_asof_leak_commission_handling_double` 双挂，DH1 不升格；诊断桶 `gross_plus_handling` / `net_commission_switch_inverted` / `vs_S_handling_tier` / `vs_T_csrc_in_commission` / `freeze_commission_bps_forbidden` 不升格；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DH ≠ 单字母 D/H**，且 **params.G 的 0.01 ≠ 任何佣金‰ / 经手费‰**；锚建议 `commission_handling_honest=pit_no_double_count_gross_plus_handling` / scope=`gross_includes_exchange_fee_no_readd` / over_policy=`skip_if_commission_inclusion_flag_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；口径：缺标志则 skip，已含则不得再加经手费，未含才可分列加；**禁止冻死具体佣金‰**；handoff：`ashare_fee_handoff=s_page`，`csrc_fee_handoff=t_page`，`fund_fee_handoff=ax_page`，`bse_fee_handoff=dg_page`；`merge_with_S/T/AX/DG/DF/DE/DD/DC/DB/DA/AC/U/V/Q/R/A/D=False`；**DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠AC≠T≠U≠V≠Q≠R≠A≠D**；**双字母 DH ≠ 单字母假设-D / 假设-H**；双计机制 ≠ S 切日 ≠ DG 北交所档 ≠ T 证管费 ≠ AX 基金档，不改 S/T/AX/DG；可交换/证管/过户/印花/经手/场内基金过户 ≠ 本机制，不改 DF/DE/DD/DC/DB/DA；**方向2/3本轮不另立**；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；不改已齐 A–DG / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF 及其他已存在假设页；不重开假设-T；不写下一字母；不开真数/回测/实盘）。基 tip=`48ffa7ee`（A/D–DG纸面齐已合，全长 `48ffa7ee45f82fb36b597f2ea898e6bbea790c71`；不改该 tip 上的 #110–#116，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文） |
