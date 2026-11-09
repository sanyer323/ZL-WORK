# 假设-DE · 可转债证管费误套/发明（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `735e2f4` 上清单 #113=DD 已收口（**不改假设-DD 正文**，亦不改已齐 A–DD / 假设-DA / 假设-DB / 假设-DC / 假设-T 及其他已存在假设页；**不重开假设-T**）后写下一纸面 DE；清单 #113=DD，下一未占号 **#114=DE**；选题自 `事实与坑` 2026-11-06「代收税费表印花税、证管费、过户费三栏都不写可转债，留给以后，不发明 0」；**新建实验 DE**  
状态：**草稿·待入库预检**（结论栏空；禁止把「可转债腿静默套股票证管费 0.02‰、或发明免费=0 冒充诚实、或缺官方‰仍不 skip」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**三条尚未冻**；**禁止标纸面齐**；**未标纸面齐**；**不改已齐 A–DD / 假设-DA / 假设-DB / 假设-DC / 假设-DD**；尤其不改假设-T / 假设-DD / 假设-DA / 假设-DB / 假设-DC / 假设-U / 假设-V / 假设-Q / 假设-D / 假设-E；**不重开假设-T**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 DE（#114）。一句话误开：回测对可转债腿误套/发明股票证管费档（例如静默套 0.02‰、或发明「免费=0」冒充诚实、或缺官方‰仍不 skip），系统性改写转债腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DE** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；占位 0.02；**params.Y ≠ 实验字母 DE**；**勿把 `params.Y` 读成实验字母 DE**；**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**——量纲与语义都不同：`params.Y=0.02` 是无量纲相对门槛，0.02‰ 是股票证管费率）≠ **`params.G`**（同族门槛，占位 0.01；**params.G ≠ 实验字母 DE**）≠ **`params.N`**（失败/废单率差门槛；占位 0.05；**params.N ≠ 实验字母 DE**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DE ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 E**（整手与科创板 200 股；**双字母 DE ≠ 单字母假设-E；严禁复用假设-E**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DE ≠ 单字母假设-A**）≠ **单字母实验 T**（证管费主报股票；**双字母 DE ≠ 单字母假设-T；严禁复用假设-T；不重开假设-T**）≠ **单字母实验 U**（股票过户费）≠ **单字母实验 V**（股票印花税）≠ 双字母 **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **S**（股票经手费）≠ **AX**（基金经手费）≠ **Q**（可转债规则混用）。**DE≠T≠DA≠DB≠DC≠DD≠U≠V≠S≠AX≠Q≠A≠D**。**双字母 DE ≠ 单字母 D/E**。**params.Y/G/N ≠ 实验字母 DE；亦 ≠ 单字母 D/E**。**勿把 `params.Y` 读成实验字母 DE，亦勿把单字母假设-D / 假设-E 读成双字母 DE**。**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**。

### 专节 · 双字母 DE ≠ 单字母假设-D / 假设-E；且 ≠ 假设-T / 假设-DD / 假设-DA / 假设-DB / 假设-DC（硬）

| 维度 | 对照页 | 本页假设-DE（双字母） |
|------|--------|----------------------|
| 题面 T | **证管费主报股票**（股票证管费档在 T；基金/ETF/债券在 T 里另有免收口径） | T 若主报股票证管费。本页专测转债腿误套/发明证管费，不把 T 的股票 0.02‰ 或「免收=0」写成转债诚实档。**DE≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 DD | **可转债过户费**（过户费按官方口径，勿发明；不是证管费） | 过户费 ≠ 证管费。**DE≠DD**；**不改 DD**；不把「转债过户费已诚实」写成「转债证管费已诚实」；`cb_transfer_fee_handoff=dd_page` |
| 题面 DA | **场内基金过户费**（中国结算；二级不套股票档） | 场内基金过户 ≠ 证管费。**DE≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` 只旁路消费 |
| 题面 DB | **可转债经手费**（交易所经手费；不是证管费） | 经手费 ≠ 证管费。**DE≠DB**；**不改 DB**；不升格 DB 的可交换债诊断桶；`cb_handling_fee_handoff=db_page` |
| 题面 DC | **可转债印花税**（税目外；不是证管费） | 印花税 ≠ 证管费。**DE≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 U | **股票过户费** | 过户费 ≠ 证管费。**DE≠U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 V | **股票印花税** | 印花税 ≠ 证管费。**DE≠V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 S | **沪深 A 股经手费** | 经手费 ≠ 证管费。**DE≠S**；**不改 S**；`fee_tier_handoff=s_page` |
| 题面 AX | **基金/ETF 经手费** | 基金经手费 ≠ 转债证管费。**DE≠AX**；**不改 AX**；`fund_fee_handoff=ax_page` |
| 题面 Q | **可转债按股票规则回放**（回转、涨跌幅、收盘价、转股所得次日才可卖） | 规则混用 ≠ 证管费。**DE≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 转债腿证管费。**DE≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 证管费抽在哪一档。**双字母 DE ≠ 单字母假设-D**；**严禁复用假设-D**；**DE≠D**；**不改 D** |
| 题面 E | **整手与科创板 200 股** | 申报股数 ≠ 证管费。**双字母 DE ≠ 单字母假设-E**；**严禁复用假设-E**；**DE≠E**；**不改 E** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ashare_csrc_fee_on_convertible_bond`（**建议**单一主报，**尚未冻**；禁与 `invent_asof_leak_cb_csrc_fee` 双挂；DE1 不升格；`invent_free_zero_cb_csrc` / `missing_official_bps_not_skip` / `vs_T_stock_csrc` / `vs_DD_cb_transfer` 只作诊断桶，不升格主报） |
| 文档 | 清单实验 T / DD / DA / DB / DC / U / V / S / AX / Q / A / D / E（**只读；禁止改写**） | `假设-DE-可转债证管费误套.md`（新建） |
| 预检键 | 实验字母 T / DD / DA / DB / DC / U / V / S / AX / Q / A / D / E / Y / G / N | 实验字母 **DE** / `de0_primary_demo`；**不得**占用或改写预检 T/DD/DA/DB/DC/U/V/S/AX/Q/A/D/E |

**禁止**：把 DE 写成「T / DD / DA / DB / DC / U / V / S / AX / Q / A / D / E 的续篇」；把「股票证管费已诚实（T）/ 转债过户费已诚实（DD）/ 基金过户已诚实（DA）/ 转债经手费已诚实（DB）/ 转债印花税已诚实（DC）」写成「转债证管费已诚实」；把实验字母 DE 与单字母 D/E 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-E / 假设-T 读成双字母 DE**；**尤重勿把 `params.Y` 读成实验字母 DE**；**尤重 `params.Y` 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同）**；把 `invent_asof_leak_cb_csrc_fee` 升格进 `de0`。本页主键只用 `de0` / `de1` / `de2` 与 `cb_csrc_fee_*`。不写下一字母。

---

## 1. 一句话假设（可检验、可证伪）

同一转债信号、同一未复权成交金额、同一当日回转（规则交 Q，本页不重开）、同一股票证管费切片（T 只旁路，本页不重开假设-T）下，回测对可转债腿误套/发明股票证管费档（例如静默套 0.02‰、或发明「免费=0」冒充诚实、或缺官方‰仍不 skip），相对「可转债证管费按官方口径，勿发明；缺官方‰则 skip；禁静默 0.02‰；禁发明免费 0」的诚实组，会**系统性改写转债腿成本**——相对诚实锚偏误。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误套股票证管费截在标定噪声带内可忽略，且「静默套 0.02‰ / 核对日泄露 / 发明免费=0 / 缺官方‰仍不 skip / vs T·DD·DA·DB·DC·U·V·S·AX·Q·A·D」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 建议键（标准件占位；拉数前再定；本页不开跑；Y/G/N/Y2 · de0 与锚 **三条尚未冻**）

```
# 配置建议键（见 §7；草稿·待入库预检；下列三条都是占位，尚未冻）
# 【消歧】params.Y = 显著性门槛；占位 0.02；**≠ 实验字母 DE ≠ 单字母假设-D / 假设-E**；勿把 params.Y 读成实验字母 DE
# 【消歧】尤重：params.Y 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同：无量纲相对门槛 ≠ 证管费率‰）
# 【消歧】params.G = 同族门槛；占位 0.01；**≠ 实验字母 DE ≠ 单字母 D/E**
# 【消歧】params.N = 失败/废单率差门槛；占位 0.05；**≠ 实验字母 DE ≠ 单字母 D/E**
# params.Y2 占位 0.015
# params.Y / G / N / Y2               占位 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误套股票证管费截 ΔFakeStockCsrc / 净收益差 / DE1−DE2；**params.Y/G/N ≠ 实验字母 DE ≠ 单字母假设-D / 假设-E**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                    建议 next_open
# params.asof_check_date              建议 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  建议 skip
# params.cb_csrc_fee_honest           建议 pit_cb_official_csrc_not_stock_tier
#   诚实锚方向：可转债证管费按官方口径，勿发明
#   缺官方‰→skip；禁静默 0.02‰；禁发明免费 0
#   对照假设-DD 的 cb_transfer_fee_honest=pit_… 与假设-T / 假设-U 的 pit_ 写法；枚举是建议，尚未冻
#   不把「代收税费表没单列可转债」写成已经核死的 0‰
#   不把 T 的股票证管费 0.02‰、或 T 里基金/债券免收，写成转债诚实锚
# params.cb_csrc_fee_scope            建议 listed_cb_spot_apart_from_stock_csrc
#   转债证管费 ≠ 股票证管费（T）≠ 转债过户费（DD）≠ 场内基金过户（DA）≠ 转债经手费（DB）≠ 转债印花税（DC）
# params.cb_csrc_fee_over_policy      建议 skip_if_official_cb_csrc_bps_missing
#   缺官方‰则 skip；禁静默 0.02‰；禁发明免费 0
# params.stock_csrc_fee_handoff       建议 t_page
#   消费 T 的股票证管费，或显式旁路；不在本页重开假设-T，也不改 T；不把 T 的 0.02‰ 写成转债诚实档
# params.cb_transfer_fee_handoff      建议 dd_page
#   消费 DD 的转债过户费，或显式旁路；过户费 ≠ 证管费；不改 DD
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的转债印花税，或显式旁路；印花税 ≠ 证管费；不改 DC
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的转债经手费，或显式旁路；经手费 ≠ 证管费；不升格 DB 可交换债诊断桶；不改 DB
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；场内基金过户 ≠ 证管费；不改 DA
# params.stock_transfer_fee_handoff   建议 u_page
#   消费 U 的股票过户费，或显式旁路；不改 U
# params.stock_stamp_handoff          建议 v_page
#   消费 V 的股票印花税，或显式旁路；不改 V
# params.cb_rule_handoff              建议 q_page
#   回转、涨跌幅、收盘价、转股所得何时可卖交 Q；本页只测证管费；不改 Q
# params.fee_tier_handoff             建议 s_page
# params.fund_fee_handoff             建议 ax_page
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
# params.lot_size_handoff             建议 e_page
#   整手与科创板门槛交 E；双字母 DE ≠ 单字母假设-E；不改 E
# params.cb_csrc_fee_handoff          建议 self
# params.de0_primary_demo             建议 invent_ashare_csrc_fee_on_convertible_bond
#   单一主报占位；禁与 invent_asof_leak_cb_csrc_fee 双挂；DE1 不升格；诊断桶不升格；尚未冻
#   半泄露名 invent_asof_leak_cb_csrc_fee 只作对照，不得升格进 de0
# params.de0_invent_ashare_csrc_fee_on_convertible_bond 建议 True
# params.de1_asof_leak_cb_csrc_fee_only 建议 True
#   半泄露对照；DE1 不升格并列主报；不得把 invent_asof_leak_cb_csrc_fee 写进 de0
# params.de2_pit_cb_csrc_fee          建议 True
# params.merge_with_T                 建议 False
# params.merge_with_DD                建议 False
# params.merge_with_DC                建议 False
# params.merge_with_DB                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_U                 建议 False
# params.merge_with_V                 建议 False
# params.merge_with_S                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_E                 建议 False
# params.missing_cb_csrc_fee_policy   建议 skip
# params.day_freq_proxy               建议 cb_csrc_fee_sensitivity
# params.universe_rule                建议 cb_csrc_fee_mischarge_check
# params.redline_v0_exempt_scope      建议 position_industry_de_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DE；勿把这个键读成实验 DE
```

### 2.2 三组对照（DE0 / DE1 / DE2）

| 组 | 角色 | 口径 |
|----|------|------|
| DE0 | 天真 / 误套股票证管费档 | 按 `de0_primary_demo` **建议**单一主报 `invent_ashare_csrc_fee_on_convertible_bond`（尚未冻）：可转债腿套股票证管费档（例如静默套 0.02‰）。**禁**与 `invent_asof_leak_cb_csrc_fee` 双挂主报 |
| DE1 | 半泄露 | 仅核对日把股票证管费现行档铺到转债全历史（建议名 `invent_asof_leak_cb_csrc_fee`，仅对照）；**不得升格并列主报**，也不得写进 `de0` |
| DE2 | 诚实 / 官方口径 | `cb_csrc_fee_honest=pit_cb_official_csrc_not_stock_tier`（建议，尚未冻）：可转债证管费按官方口径，勿发明。缺官方‰→skip；禁静默 0.02‰；禁发明免费 0。股票证管费只消费 T，转债过户费只消费 DD，转债印花税只消费 DC，转债经手费只消费 DB，场内基金过户只消费 DA，股票过户只消费 U，股票印花税只消费 V，转债规则只消费 Q，或显式旁路 |

发明「免费=0」冒充诚实（`invent_free_zero_cb_csrc`）、缺官方‰仍不 skip（`missing_official_bps_not_skip`）、以及相对 T / DD 的对照截（`vs_T_stock_csrc` / `vs_DD_cb_transfer`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `de0_primary_demo`。DB 的可交换债诊断桶不收到本页。U / DA / DB / DC / V 的对照桶同样只作诊断。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **建议** `2026-10-16`；fill_time **建议** `next_open`；fail **建议** `skip`。以上与诚实锚同属三条里的锚，**尚未冻**。股票证管费 0.02‰ 是假设-T 已有的股票口径，本页只当作「被误套到转债腿」的对照，不改 T，也不把 0.02‰ 写成转债诚实档。T 里基金/ETF/债券免收，不得抄成转债诚实锚=0。转债过户费留在 DD，场内基金过户费留在 DA，转债经手费留在 DB，转债印花税留在 DC，都不改。代收税费表版本日期不是 `asof_check_date`。核对日该表证管费栏不把可转债现货写成股票 0.02‰ 那一行；缺官方‰则 skip，不把「表上没单列」发明成免费 0，也不静默填 0.02‰。`params.Y` 的 0.02 是无量纲相对门槛，不是这道‰。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `de0_primary_demo` / `params.Y`·G·N·Y2 / 混口径开关 / 桶）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DE0）/ 半泄露组（DE1）相对诚实组（DE2）的成本差、误套股票证管费截**显著且集中在转债腿误套/发明证管费桶**；分桶「静默套 0.02‰ / 核对日泄露 / 发明免费=0 / 缺官方‰仍不 skip / vs T·DD·DA·DB·DC·U·V·S·AX·Q·A·D」不改变主结论方向。方向是相对诚实锚偏误。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 T 的股票证管费、DD 的转债过户费、DA 的场内基金过户费、DB 的转债经手费、DC 的转债印花税、U 的股票过户费、V 的股票印花税、Q 的回转与涨跌幅、S/AX 的经手费、A 的板上容量、D 的成交时点、E 的整手门槛解释；或 `de0_primary_demo` 与 `invent_asof_leak_cb_csrc_fee` 双挂；或 DE1 升格并列主报；或 `invent_free_zero_cb_csrc` / `missing_official_bps_not_skip` / `vs_T_stock_csrc` / `vs_DD_cb_transfer` 诊断桶升格主报；或把 DB 的可交换债诊断桶升到本页；或实验字母 DE 与单字母 D/E 或 params.Y/G/N 混读；或把 `params.Y` 的 0.02 读成证管费 0.02‰；或重开假设-T。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额、同一当日回转（回转本身交 Q），对照 DE0/DE1/DE2。股票证管费走 T 的诚实档或显式旁路，不在本页重开假设-T。报告成本差、误套股票证管费截。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_ashare_csrc_fee_on_convertible_bond` / `invent_asof_leak_cb_csrc_fee` / `invent_free_zero_cb_csrc` / `missing_official_bps_not_skip` / `vs_T_stock_csrc` / `vs_DD_cb_transfer` / `vs_U_stock_transfer` / `vs_DA_etf_transfer` / `vs_DB_cb_handling_fee` / `vs_DC_cb_stamp` / `vs_V_stock_stamp` / `vs_S_fee_tier` / `vs_AX_fund_fee` / `vs_Q_cb_rule` / `vs_A_board_capacity` / `vs_D_fill_time` / `vs_E_lot_size`

`invent_free_zero_cb_csrc`、`missing_official_bps_not_skip`、`vs_T_stock_csrc`、`vs_DD_cb_transfer` 只作诊断桶：它们不是 `de0`，也不是 DE1，**不得升格主报**。`vs_U_stock_transfer` / `vs_DA_etf_transfer` / `vs_DB_cb_handling_fee` / `vs_DC_cb_stamp` / `vs_V_stock_stamp` 同样只作诊断。`invent_asof_leak_cb_csrc_fee` 只服务 DE1，**不得升格进 `de0`**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 用股票证管费 0.02‰ 当转债诚实档，或把 `params.Y` 的 0.02 当成证管费 0.02‰。**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**。
- 缺官方可转债证管费‰，却静默填股票 0.02‰。
- 把「代收税费表没写可转债」或 T 里「基金/债券免收」发明成免费=0，并拿去冒充诚实锚。诚实锚是官方口径；缺官方‰则 skip；禁静默 0.02‰；禁发明免费 0。
- 缺官方‰仍不 skip，并用 0 或 0.02‰ 把腿填上。
- 把「股票证管费已诚实（T）」写成「转债证管费已诚实」。T 若主报股票；本页不重开假设-T，不改 T。
- 把「转债过户费已诚实（DD）」写成「转债证管费已诚实」。过户费 ≠ 证管费。不改 DD。
- 把「场内基金过户已诚实（DA）/ 转债经手费已诚实（DB）/ 转债印花税已诚实（DC）」写成「转债证管费已诚实」。不改 DA / DB / DC。
- `de0_primary_demo` 与 `invent_asof_leak_cb_csrc_fee` 双挂主报；DE1 升格并列主报；诊断桶（`invent_free_zero_cb_csrc` / `missing_official_bps_not_skip` / `vs_T_stock_csrc` / `vs_DD_cb_transfer`）升格为第二个主报。
- 实验字母 DE 与单字母 D/E 或 params.Y/G/N 混读。
- 改 T / DD / DA / DB / DC / U / V / S / AX / Q / A / D / E 正文；抢 A 真数队列；标纸面齐；开真数/回测/实盘；用复权价当证管费基数；结论写成「转债证管费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、证券类别（股票 / 场内基金或 ETF / 上市公司可转债现货）、未复权成交金额、交易日。
- 没有证券类别，或没有官方可转债证管费‰时，按 `cb_csrc_fee_over_policy` 建议 skip，不得用 0.02‰ 补上，也不得发明免费 0。
- 旁路消费：T 的股票证管费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、DA 的场内基金过户费、U 的股票过户费、V 的股票印花税、Q 的转债规则之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。**
- 未复权价；asof **建议** `2026-10-16`（尚未冻）。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **建议键摘要（三条尚未冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`cb_csrc_fee_honest=pit_cb_official_csrc_not_stock_tier`（缺官方‰→skip；禁静默 0.02‰；禁发明免费 0）；`cb_csrc_fee_scope=listed_cb_spot_apart_from_stock_csrc`；`cb_csrc_fee_over_policy=skip_if_official_cb_csrc_bps_missing`；`de0_primary_demo=invent_ashare_csrc_fee_on_convertible_bond`（**建议**单一主报；禁与 `invent_asof_leak_cb_csrc_fee` 双挂；DE1 不升格；诊断桶不升格主报）；`stock_csrc_fee_handoff=t_page`；`cb_transfer_fee_handoff=dd_page`；`cb_stamp_handoff=dc_page`；`cb_handling_fee_handoff=db_page`；`etf_transfer_fee_handoff=da_page`；`stock_transfer_fee_handoff=u_page`；`stock_stamp_handoff=v_page`；`cb_rule_handoff=q_page`；`merge_with_T/DD/DC/DB/DA/U/V/S/AX/Q/A/D=False`（另 `merge_with_E=False`）。
- `params.Y/G/N/Y2` **占位** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误套股票证管费截 ΔFakeStockCsrc / 净收益差 / DE1−DE2；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DE ≠ 单字母 D/E**；**勿把 params.Y 读成实验字母 DE，亦勿把单字母假设-D / 假设-E 读成双字母 DE**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`735e2f4`。

---

## 8. 结论

（空；草稿·待入库预检；三条尚未冻；未标纸面齐。）

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；可转债证管费误套/发明；`de0_primary_demo` 建议 `invent_ashare_csrc_fee_on_convertible_bond`，单一主报，禁与 `invent_asof_leak_cb_csrc_fee` 双挂，DE1 不升格；诊断桶 `invent_free_zero_cb_csrc` / `missing_official_bps_not_skip` / `vs_T_stock_csrc` / `vs_DD_cb_transfer` 不升格；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DE ≠ 单字母 D/E**，且 **params.Y 的 0.02 ≠ 证管费 0.02‰**；锚建议 `cb_csrc_fee_honest=pit_cb_official_csrc_not_stock_tier`（缺官方‰→skip；禁静默 0.02‰；禁发明免费 0）/ scope=`listed_cb_spot_apart_from_stock_csrc` / over_policy=`skip_if_official_cb_csrc_bps_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；handoff：`stock_csrc_fee_handoff=t_page`，`cb_transfer_fee_handoff=dd_page`，`cb_stamp_handoff=dc_page`，`cb_handling_fee_handoff=db_page`，`etf_transfer_fee_handoff=da_page`，`stock_transfer_fee_handoff=u_page`，`stock_stamp_handoff=v_page`，`cb_rule_handoff=q_page`；`merge_with_T/DD/DC/DB/DA/U/V/S/AX/Q/A/D=False`；**DE≠T≠DA≠DB≠DC≠DD≠U≠V≠S≠AX≠Q≠A≠D**；**双字母 DE ≠ 单字母假设-D / 假设-E**；vs T：T 若主报股票证管费，本页专测转债腿误套/发明证管费，不重开假设-T，不改 T；vs DD：过户费 ≠ 证管费，不改 DD；vs DA/DB/DC：场内基金过户 / 经手费 / 印花税 ≠ 证管费，不改 DA/DB/DC；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；不改已齐 A–DD / 假设-DA / 假设-DB / 假设-DC / 假设-DD 及其他已存在假设页；不写下一字母；不开真数/回测/实盘）。基 tip=`735e2f4`（本次提交前 HEAD `735e2f4ca8e44a9ad43a0e6fd041184e7525ac91`） |
