# 假设-DF · 可交换债经手费沪深合成（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `e517506` 上清单 #114=DE 已收口（A/D–DE 已收口合入；**不改假设-DE 正文**，亦不改已齐 A–DE / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-T 及其他已存在假设页；**不重开假设-T**）后写下一草稿 DF；清单 #114=DE，本页占用 **#115=DF**；选题自 `事实与坑` 2026-11-06「沪市可交换债在债券现券暂免名单、深市可交换债与可转债同档 0.04‰，沪深可交换债不要合成一句」（DB 只把这件事留在诊断桶）；**新建实验 DF**  
状态：**草稿·待入库预检**（结论栏空；禁止把「沪市可交换债（债券现券暂免）与深市可交换债（0.04‰）合成一句/一个费率、或静默套 A 股经手费档、或缺 venue/sec_type 仍不 skip」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**三条尚未冻**；**禁止标纸面齐**；**未标纸面齐**；**不改已齐 A–DE / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE**；尤其不改假设-DB / 假设-S / 假设-AX / 假设-DE / 假设-DD / 假设-DC / 假设-T / 假设-D / 假设-F；**不重开假设-T**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DF（#115）。一句话误开：回测把沪市可交换债（债券现券暂免）与深市可交换债（0.04‰）合成一句/一个费率，或静默套 A 股经手费档、或缺 venue/sec_type 仍不 skip，系统性改写可交换债腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DF** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；占位 0.02；**params.Y ≠ 实验字母 DF**；**勿把 `params.Y` 读成实验字母 DF**）≠ **`params.G`**（同族门槛，占位 0.01；**params.G ≠ 实验字母 DF**；**尤重：`params.G` 的 0.01 ≠ 深市可交换 0.04‰ ≠ A股 0.0341‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，0.04‰ 是深市可交换债经手费率，0.0341‰ 是 A 股经手费率）≠ **`params.N`**（失败/废单率差门槛；占位 0.05；**params.N ≠ 实验字母 DF**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DF ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 F**（涨跌停价取整；**双字母 DF ≠ 单字母假设-F；严禁复用假设-F**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DF ≠ 单字母假设-A**）≠ **单字母实验 T**（证管费主报股票；**双字母 DF ≠ 单字母假设-T；严禁复用假设-T；不重开假设-T**）≠ 双字母 **DB**（可转债经手费）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DA**（场内基金过户费）≠ **S**（股票经手费）≠ **AX**（基金经手费）≠ **U**（股票过户费）≠ **V**（股票印花税）≠ **Q**（可转债规则混用）。**DF≠DB≠DE≠DD≠DC≠DA≠S≠AX≠T≠U≠V≠Q≠A≠D**。**双字母 DF ≠ 单字母 D/F**。**params.Y/G/N ≠ 实验字母 DF；亦 ≠ 单字母 D/F**。**勿把 `params.G` 读成实验字母 DF，亦勿把单字母假设-D / 假设-F 读成双字母 DF**。**尤重：`params.G` 的 0.01 ≠ 深市可交换 0.04‰ ≠ A股 0.0341‰**。

### 专节 · 双字母 DF ≠ 单字母假设-D / 假设-F；且 ≠ 假设-DB / 假设-S / 假设-AX / 假设-DE / 假设-DD / 假设-DC（硬）

| 维度 | 对照页 | 本页假设-DF（双字母） |
|------|--------|----------------------|
| 题面 DB | **可转债经手费**（主报转债腿误套 A 股档；可交换债沪深合成只在 DB 的诊断桶） | DB 主报可转债经手费。本页专测**可交换债**沪深合成误开。**DF≠DB**；**不改 DB**；**禁把 DB 的 `sse_szse_exchangeable_merged` 升格作另挂主报**，也不得把它写进 `df0`；DB 侧该项只作对照/旁路；`cb_handling_fee_handoff=db_page` |
| 题面 S | **沪深 A 股经手费**（三切日；现行 0.0341‰） | 股票经手费族 ≠ 可交换债沪深分列。**DF≠S**；**不改 S**；不把 S 的 0.0341‰ 写成可交换债诚实档；`fee_tier_handoff=s_page` |
| 题面 AX | **基金/ETF 经手费** | 基金经手费 ≠ 可交换债沪深分列。**DF≠AX**；**不改 AX**；`fund_fee_handoff=ax_page` |
| 题面 DE | **可转债证管费**（证管费按官方口径，勿发明） | 证管费 ≠ 经手费合成。**DF≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债过户费** | 过户费 ≠ 经手费合成。**DF≠DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DC | **可转债印花税** | 印花税 ≠ 经手费合成。**DF≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 DA | **场内基金过户费** | 场内基金过户 ≠ 可交换债经手费。**DF≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` 只旁路消费 |
| 题面 T | **证管费主报股票** | 证管费 ≠ 可交换债经手费。**DF≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费** | 过户费 ≠ 可交换债经手费。**DF≠U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 V | **股票印花税** | 印花税 ≠ 可交换债经手费。**DF≠V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 Q | **可转债按股票规则回放**（回转、涨跌幅、收盘价、转股所得次日才可卖） | 规则混用 ≠ 可交换债经手费沪深分列。**DF≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 可交换债腿经手费。**DF≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 可交换债经手费抽在哪一档。**双字母 DF ≠ 单字母假设-D**；**严禁复用假设-D**；**DF≠D**；**不改 D** |
| 题面 F | **涨跌停价取整** | 取整到分 ≠ 可交换债经手费。**双字母 DF ≠ 单字母假设-F**；**严禁复用假设-F**；**DF≠F**；**不改 F** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_sse_szse_exchangeable_fee_merged`（**建议**单一主报，**尚未冻**；禁与 `invent_asof_leak_exchangeable_fee` 双挂；DF1 不升格；`vs_DB_cb_handling` / `vs_S_stock_handling` / `sse_szse_exchangeable_merged` 只作诊断对照，不升格主报；**禁把 DB 的 `sse_szse_exchangeable_merged` 升格进 `df0` 或作另挂主报**） |
| 文档 | 清单实验 DB / S / AX / DE / DD / DC / DA / T / U / V / Q / A / D / F（**只读；禁止改写**） | `假设-DF-可交换债经手费沪深合成.md`（新建） |
| 预检键 | 实验字母 DB / S / AX / DE / DD / DC / DA / T / U / V / Q / A / D / F / Y / G / N | 实验字母 **DF** / `df0_primary_demo`；**不得**占用或改写预检 DB/S/AX/DE/DD/DC/DA/T/U/V/Q/A/D/F |

**禁止**：把 DF 写成「DB / S / AX / DE / DD / DC / DA / T / U / V / Q / A / D / F 的续篇」；把「转债经手费已诚实（DB）/ 股票经手费已诚实（S）/ 基金经手费已诚实（AX）/ 转债证管费已诚实（DE）/ 转债过户费已诚实（DD）/ 转债印花税已诚实（DC）」写成「可交换债沪深分列已诚实」；把实验字母 DF 与单字母 D/F 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-F 读成双字母 DF**；**尤重勿把 `params.G` 读成实验字母 DF**；**尤重 `params.G` 的 0.01 ≠ 深市可交换 0.04‰ ≠ A股 0.0341‰（量纲与语义不同）**；把 `invent_asof_leak_exchangeable_fee` 升格进 `df0`；把 DB 的 `sse_szse_exchangeable_merged` 升格进 `df0` 或作另挂主报。本页主键只用 `df0` / `df1` / `df2` 与 `exch_handling_fee_*`。不写下一字母。

---

## 1. 一句话假设（可检验、可证伪）

同一可交换债信号、同一未复权成交金额、同一交易所 venue、同一证券类别下，回测把沪市可交换债（债券现券暂免）与深市可交换债（0.04‰）合成一句/一个费率，或静默套 A 股经手费档、或缺 venue/sec_type 仍不 skip，相对「沪深分列：沪市走债券现券暂免、深市 0.04‰，禁止合成一句；缺 venue 或 sec_type 则 skip；禁静默套 A 股经手费档」的诚实组，会**系统性改写可交换债腿成本**——相对诚实锚偏误。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、沪深合成截在标定噪声带内可忽略，且「沪深合成一句 / 核对日泄露 / 静默套 A 股档 / 缺 venue·sec_type 仍不 skip / vs DB·S·AX·DE·DD·DC」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 建议键（标准件占位；拉数前再定；本页不开跑；Y/G/N/Y2 · df0 与锚 **三条尚未冻**）

```
# 配置建议键（见 §7；草稿·待入库预检；下列三条都是占位，尚未冻）
# 【消歧】params.Y = 显著性门槛；占位 0.02；**≠ 实验字母 DF ≠ 单字母假设-D / 假设-F**；勿把 params.Y 读成实验字母 DF
# 【消歧】params.G = 同族门槛；占位 0.01；**≠ 实验字母 DF ≠ 单字母 D/F**
# 【消歧】尤重：params.G 的 0.01 ≠ 深市可交换 0.04‰ ≠ A股 0.0341‰（量纲与语义不同：无量纲相对门槛 ≠ 经手费率‰）
# 【消歧】params.N = 失败/废单率差门槛；占位 0.05；**≠ 实验字母 DF ≠ 单字母 D/F**
# params.Y2 占位 0.015
# params.Y / G / N / Y2               占位 0.02/0.01/0.05/0.015（相对门槛：成本差 / 沪深合成截 ΔMergeExchFee / 净收益差 / DF1−DF2；**params.Y/G/N ≠ 实验字母 DF ≠ 单字母假设-D / 假设-F**；**尤重 params.G 的 0.01 ≠ 深市可交换 0.04‰ ≠ A股 0.0341‰**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                    建议 next_open
# params.asof_check_date              建议 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  建议 skip
# params.exch_handling_fee_honest     建议 pit_sse_szse_listed_apart
#   诚实锚方向：沪深分列，勿合成一句
#   沪市可交换债按债券现券暂免；深市可交换债 0.04‰
#   缺 venue 或 sec_type → skip；禁静默套 A 股经手费档
#   枚举是建议，尚未冻
#   不把 DB 的可转债经手费诚实档抄成可交换债诚实锚
#   不把 S 的 A 股 0.0341‰ 写成可交换债诚实档
# params.exch_handling_fee_scope      建议 sse_bond_waiver_vs_szse_004_not_merged
#   沪市可交换按债券现券暂免、深市 0.04‰，禁止合成一句
#   可交换债经手费 ≠ 可转债经手费（DB）≠ 股票经手费（S）≠ 基金经手费（AX）≠ 证管费（DE）≠ 过户费（DD）≠ 印花税（DC）
# params.exch_handling_fee_over_policy 建议 skip_if_venue_or_sec_type_missing
#   缺 venue 或 sec_type 则 skip；禁合成一句后照填；禁静默套 A 股档
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的可转债经手费，或显式旁路；DB 主报转债腿；本页专测可交换债
#   DB 的 sse_szse_exchangeable_merged 只作对照/旁路，不得升格进 df0，不得作另挂主报；不改 DB
# params.fee_tier_handoff             建议 s_page
#   消费 S 的股票经手费，或显式旁路；股票经手费族 ≠ 可交换债沪深分列；不改 S
# params.fund_fee_handoff             建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；不改 AX
# params.cb_rule_handoff              建议 q_page
#   回转、涨跌幅、收盘价交 Q；本页只测可交换债经手费沪深是否合成；不改 Q
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的转债印花税，或显式旁路；印花税 ≠ 经手费合成；不改 DC
# params.cb_transfer_fee_handoff      建议 dd_page
#   消费 DD 的转债过户费，或显式旁路；过户费 ≠ 经手费合成；不改 DD
# params.cb_csrc_fee_handoff          建议 de_page
#   消费 DE 的转债证管费，或显式旁路；证管费 ≠ 经手费合成；不改 DE
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；不改 DA
# params.stock_csrc_fee_handoff       建议 t_page
#   消费 T 的股票证管费，或显式旁路；不在本页重开假设-T，也不改 T
# params.stock_transfer_fee_handoff   建议 u_page
# params.stock_stamp_handoff          建议 v_page
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
#   成交时点与停牌交 D；双字母 DF ≠ 单字母假设-D；不改 D
# params.price_round_handoff          建议 f_page
#   涨跌停价取整交 F；双字母 DF ≠ 单字母假设-F；不改 F
# params.exch_handling_fee_handoff    建议 self
# params.df0_primary_demo             建议 invent_sse_szse_exchangeable_fee_merged
#   单一主报占位；禁与 invent_asof_leak_exchangeable_fee 双挂；DF1 不升格；诊断桶不升格；尚未冻
#   半泄露名 invent_asof_leak_exchangeable_fee 只作对照，不得升格进 df0
#   禁把 DB 的 sse_szse_exchangeable_merged 升格进 df0 或作另挂主报
# params.df0_invent_sse_szse_exchangeable_fee_merged 建议 True
# params.df1_asof_leak_exchangeable_fee_only 建议 True
#   半泄露对照；DF1 不升格并列主报；不得把 invent_asof_leak_exchangeable_fee 写进 df0
# params.df2_pit_exch_handling_fee    建议 True
# params.merge_with_DB                建议 False
# params.merge_with_S                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_DC                建议 False
# params.merge_with_DD                建议 False
# params.merge_with_DE                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_T                 建议 False
# params.merge_with_U                 建议 False
# params.merge_with_V                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_F                 建议 False
# params.missing_venue_or_sec_type_policy 建议 skip
# params.day_freq_proxy               建议 exch_handling_fee_sensitivity
# params.universe_rule                建议 exch_handling_fee_merge_check
# params.redline_v0_exempt_scope      建议 position_industry_df_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DF；勿把这个键读成实验 DF
```

### 2.2 三组对照（DF0 / DF1 / DF2）

| 组 | 角色 | 口径 |
|----|------|------|
| DF0 | 天真 / 沪深合成一句 | 按 `df0_primary_demo` **建议**单一主报 `invent_sse_szse_exchangeable_fee_merged`（尚未冻）：把沪市可交换债（债券现券暂免）与深市可交换债（0.04‰）合成一句/一个费率。**禁**与 `invent_asof_leak_exchangeable_fee` 双挂主报。**禁**把 DB 的 `sse_szse_exchangeable_merged` 升格作另挂主报或写进 `df0` |
| DF1 | 半泄露 | 仅核对日把可交换债经手费现行口径铺到全历史（建议名 `invent_asof_leak_exchangeable_fee`，仅对照、不进 `df0`）；**不得升格并列主报**，也不得写进 `df0` |
| DF2 | 诚实 / 沪深分列 | `exch_handling_fee_honest=pit_sse_szse_listed_apart`（建议，尚未冻）：沪市可交换按债券现券暂免、深市 0.04‰，禁止合成一句。缺 venue 或 sec_type → skip。禁静默套 A 股经手费档。转债经手费只消费 DB，股票经手费只消费 S，基金经手费只消费 AX，转债规则只消费 Q，转债印花税只消费 DC，转债过户费只消费 DD，转债证管费只消费 DE，或显式旁路 |

静默套 A 股经手费档、缺 venue/sec_type 仍不 skip，以及相对 DB / S 的对照截（`vs_DB_cb_handling` / `vs_S_stock_handling`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `df0_primary_demo`。DB 页上的 `sse_szse_exchangeable_merged` 只作对照/旁路：**不得升格进 `df0`，不得作另挂主报**。AX / DE / DD / DC 的对照桶同样只作诊断。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **建议** `2026-10-16`；fill_time **建议** `next_open`；fail **建议** `skip`。以上与诚实锚同属三条里的锚，**尚未冻**。深市可交换债 0.04‰、沪市可交换债走债券现券暂免，是 `事实与坑` 2026-11-06 已写下、并由假设-DB 留在诊断桶的方向；本页只把它收成可交换债专测，不改 DB，也不把两档合成一句当诚实锚。A 股 0.0341‰ 留在 S，只当作「被静默套到可交换债腿」的对照，不改 S。转债经手费留在 DB，证管费留在 DE，过户费留在 DD，印花税留在 DC，基金经手费留在 AX，都不改。`params.G` 的 0.01 是无量纲相对门槛，不是 0.04‰，也不是 0.0341‰。缺 venue 或 sec_type 则 skip，不用合成费率、A 股档或 0 把腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `df0_primary_demo` / `params.Y`·G·N·Y2 / 混口径开关 / 桶）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DF0）/ 半泄露组（DF1）相对诚实组（DF2）的成本差、沪深合成截**显著且集中在可交换债腿沪深合成桶**；分桶「沪深合成一句 / 核对日泄露 / 静默套 A 股档 / 缺 venue·sec_type 仍不 skip / vs DB·S·AX·DE·DD·DC」不改变主结论方向。方向是相对诚实锚偏误。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 DB 的可转债经手费、S 的股票经手费、AX 的基金经手费、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、Q 的回转与涨跌幅、T 的股票证管费、U/V 的股票过户与印花税、DA 的场内基金过户、A 的板上容量、D 的成交时点、F 的涨跌停价取整解释；或 `df0_primary_demo` 与 `invent_asof_leak_exchangeable_fee` 双挂；或 DF1 升格并列主报；或 `vs_DB_cb_handling` / `vs_S_stock_handling` / `sse_szse_exchangeable_merged` 诊断桶升格主报；或把 DB 的 `sse_szse_exchangeable_merged` 升格进 `df0` 或作另挂主报；或实验字母 DF 与单字母 D/F 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成深市可交换 0.04‰ 或 A 股 0.0341‰；或重开假设-T。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DF0/DF1/DF2。可转债经手费走 DB 的诚实档或显式旁路，不在本页改 DB，也不把 DB 的可交换债诊断桶升成主报。报告成本差、沪深合成截。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_sse_szse_exchangeable_fee_merged` / `invent_asof_leak_exchangeable_fee` / `sse_szse_exchangeable_merged` / `vs_DB_cb_handling` / `vs_S_stock_handling` / `vs_AX_fund_handling` / `vs_DE_cb_csrc` / `vs_DD_cb_transfer` / `vs_DC_cb_stamp` / `silent_ashare_handling_on_exchangeable` / `missing_venue_or_sec_type_not_skip` / `vs_DA_etf_transfer` / `vs_T_stock_csrc` / `vs_U_stock_transfer` / `vs_V_stock_stamp` / `vs_Q_cb_rule` / `vs_A_board_capacity` / `vs_D_fill_time` / `vs_F_price_round`

`vs_DB_cb_handling`、`vs_S_stock_handling`、`sse_szse_exchangeable_merged`、`silent_ashare_handling_on_exchangeable`、`missing_venue_or_sec_type_not_skip` 只作诊断桶：它们不是 `df0`，也不是 DF1，**不得升格主报**。`sse_szse_exchangeable_merged` 是 DB 侧已有对照名，本页只引用作诊断，**不得升格进 `df0`，不得作另挂主报**。`vs_AX_fund_handling` / `vs_DE_cb_csrc` / `vs_DD_cb_transfer` / `vs_DC_cb_stamp` 同样只作诊断。`invent_asof_leak_exchangeable_fee` 只服务 DF1，**不得升格进 `df0`**。`invent_sse_szse_exchangeable_fee_merged` 才是建议中的单一主报名，与 DB 的短名不是同一个键。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把沪市可交换债（债券现券暂免）和深市可交换债（0.04‰）合成一句/一个费率，并拿去当诚实锚。
- 静默套 A 股经手费档（0.0341‰）。或把 `params.G` 的 0.01 当成 0.04‰ 或 0.0341‰。**尤重：`params.G` 的 0.01 ≠ 深市可交换 0.04‰ ≠ A股 0.0341‰**。
- 缺 venue 或 sec_type 仍不 skip，并用合成费率、A 股档或 0 把腿填上。
- 把「转债经手费已诚实（DB）」写成「可交换债沪深分列已诚实」。DB 主报可转债经手费；本页不改 DB。
- 把 DB 的 `sse_szse_exchangeable_merged` 升格作另挂主报，或写进 `df0`。该名只作对照/旁路。
- 把「股票经手费已诚实（S）/ 基金经手费已诚实（AX）」写成「可交换债沪深分列已诚实」。不改 S / AX。
- 把「转债证管费已诚实（DE）/ 转债过户费已诚实（DD）/ 转债印花税已诚实（DC）」写成「可交换债经手费已诚实」。证管费 / 过户费 / 印花税 ≠ 经手费合成。不改 DE / DD / DC。
- `df0_primary_demo` 与 `invent_asof_leak_exchangeable_fee` 双挂主报；DF1 升格并列主报；诊断桶（`vs_DB_cb_handling` / `vs_S_stock_handling` / `sse_szse_exchangeable_merged`）升格为第二个主报。
- 实验字母 DF 与单字母 D/F 或 params.Y/G/N 混读。
- 改 DB / S / AX / DE / DD / DC / DA / T / U / V / Q / A / D / F 正文；重开假设-T；抢 A 真数队列；标纸面齐；开真数/回测/实盘；用复权价当经手费基数；结论写成「可交换债费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、venue（沪/深）、证券类别（可交换债 / 可转债现货 / 股票 / 场内基金）、未复权成交金额、交易日。
- 没有 venue，或没有 sec_type 时，按 `exch_handling_fee_over_policy` 建议 skip，不得合成一句费率，也不得套 A 股 0.0341‰。
- 旁路消费：DB 的转债经手费、S 的股票经手费、AX 的基金经手费、Q 的转债规则、DC 的转债印花税、DD 的转债过户费、DE 的转债证管费、DA 的场内基金过户费、T 的股票证管费、U 的股票过户费、V 的股票印花税之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** DB 的 `sse_szse_exchangeable_merged` 不收到本页主报。
- 未复权价；asof **建议** `2026-10-16`（尚未冻）。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **建议键摘要（三条尚未冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`exch_handling_fee_honest=pit_sse_szse_listed_apart`（沪深分列，勿合成一句）；`exch_handling_fee_scope=sse_bond_waiver_vs_szse_004_not_merged`（沪市可交换按债券现券暂免、深市 0.04‰，禁止合成一句）；`exch_handling_fee_over_policy=skip_if_venue_or_sec_type_missing`（缺 venue/sec_type 则 skip）；`df0_primary_demo=invent_sse_szse_exchangeable_fee_merged`（**建议**单一主报；禁与 `invent_asof_leak_exchangeable_fee` 双挂；DF1 不升格；诊断桶不升格主报；禁把 DB 的 `sse_szse_exchangeable_merged` 升格进 `df0` 或作另挂主报）；`cb_handling_fee_handoff=db_page`；`fee_tier_handoff=s_page`；`fund_fee_handoff=ax_page`；`cb_rule_handoff=q_page`；`cb_stamp_handoff=dc_page`；`cb_transfer_fee_handoff=dd_page`；`cb_csrc_fee_handoff=de_page`；`merge_with_DB/S/AX/Q/DC/DD/DE/DA/T/U/V/A/D=False`（另 `merge_with_F=False`）。
- `params.Y/G/N/Y2` **占位** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 沪深合成截 ΔMergeExchFee / 净收益差 / DF1−DF2；**尤重 params.G 的 0.01 ≠ 深市可交换 0.04‰ ≠ A股 0.0341‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DF ≠ 单字母 D/F**；**勿把 params.G 读成实验字母 DF，亦勿把单字母假设-D / 假设-F 读成双字母 DF**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`e517506`。

---

## 8. 结论

（空；草稿·待入库预检；三条尚未冻；未标纸面齐；禁止标纸面齐。）

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；可交换债经手费沪深合成；`df0_primary_demo` 建议 `invent_sse_szse_exchangeable_fee_merged`，单一主报，禁与 `invent_asof_leak_exchangeable_fee` 双挂，DF1 不升格；诊断桶 `vs_DB_cb_handling` / `vs_S_stock_handling` / `sse_szse_exchangeable_merged` 不升格；**禁把 DB 的 `sse_szse_exchangeable_merged` 升格进 df0 或作另挂主报**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DF ≠ 单字母 D/F**，且 **params.G 的 0.01 ≠ 深市可交换 0.04‰ ≠ A股 0.0341‰**；锚建议 `exch_handling_fee_honest=pit_sse_szse_listed_apart` / scope=`sse_bond_waiver_vs_szse_004_not_merged` / over_policy=`skip_if_venue_or_sec_type_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；handoff：`cb_handling_fee_handoff=db_page`，`fee_tier_handoff=s_page`，`fund_fee_handoff=ax_page`，`cb_rule_handoff=q_page`，`cb_stamp_handoff=dc_page`，`cb_transfer_fee_handoff=dd_page`，`cb_csrc_fee_handoff=de_page`；`merge_with_DB/S/AX/Q/DC/DD/DE/DA/T/U/V/A/D=False`；**DF≠DB≠DE≠DD≠DC≠DA≠S≠AX≠T≠U≠V≠Q≠A≠D**；**双字母 DF ≠ 单字母假设-D / 假设-F**；vs DB：DB 主报可转债经手费，本页专测可交换债沪深合成误开，不改 DB；vs S/AX：股票/基金经手费族 ≠ 可交换债沪深分列，不改 S/AX；vs DE/DD/DC：证管费/过户费/印花税 ≠ 经手费合成，不改 DE/DD/DC；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；不改已齐 A–DE / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE 及其他已存在假设页；不重开假设-T；不写下一字母；不开真数/回测/实盘）。基 tip=`e517506`（本次提交前 HEAD `e517506173c3561f3af5c0c24db83b35eb548ff1`） |
