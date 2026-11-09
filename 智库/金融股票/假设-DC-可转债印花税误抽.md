# 假设 DC · 可转债印花税误抽股票档 / 把减半切日或买卖双边抄到转债（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `5680829` 上清单 #111=DB 已收口（**不改假设-DB 正文**，亦不改已存在的假设-DA 及其他已存在假设页）后写下一纸面 DC；清单 #111=DB，下一未占号 **#112=DC**；选题自 `事实与坑` 2026-11-06「代收税费表印花税、证管费、过户费三栏都不写可转债」与周一补题「可转债印花税不要套股票」；**新建实验 DC**  
状态：**草稿·待入库预检**（结论栏空；禁止把「可转债腿套股票印花税 1‰ / 减半后 0.5‰、买卖双边、或把 2023-08-28 股票减半抄成转债印花税切日」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**三条尚未冻**；**禁止标纸面齐**；**未标纸面齐**；**不改假设-DB / 假设-DA**；尤其不改假设-V / 假设-DB / 假设-Q / 假设-U / 假设-T / 假设-D）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 DC（#112）。一句话误开：回测对可转债腿误抽股票印花税（套1‰/减半后0.5‰、或买卖双边、或把2023-08-28股票减半抄成转债也有印花税切日），系统性改写转债腿成本（相对依法不征偏悲观）。

> **字母消歧（硬）**：本页**实验字母 DC** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；占位 0.02；**params.Y ≠ 实验字母 DC**；**勿把 `params.Y` 读成实验字母 DC**）≠ **`params.G`**（同族门槛，占位 0.01；**尤重：`params.G` ≠ 印花税 1‰ ≠ 减半后 0.5‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，1‰ / 0.5‰ 是股票印花税税率；**params.G ≠ 实验字母 DC**）≠ **`params.N`**（失败/废单率差门槛；占位 0.05；**params.N ≠ 实验字母 DC**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DC ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 C**（股票池当时名单；**双字母 DC ≠ 单字母实验 C；严禁复用实验 C**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DC ≠ 单字母假设-A**）≠ **单字母实验 V**（股票印花税；**双字母 DC ≠ 单字母假设-V；严禁复用假设-V**）≠ 双字母 **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **S**（股票经手费）≠ **U**（股票过户费）≠ **AX**（基金经手费）≠ **T**（证管费）≠ **Q**（可转债规则混用）≠ **CB**（融资展期；字母顺序不同，**DC≠CB**）。**DC≠V≠DB≠DA≠S≠U≠AX≠T≠Q≠A≠D**。**params.Y/G/N ≠ 实验字母 DC；亦 ≠ 单字母 D/C**。**勿把 `params.Y` 读成实验字母 DC，亦勿把单字母假设-D / 实验 C 读成双字母 DC**。**尤重：`params.G` ≠ 1‰ / 0.5‰**。

### 专节 · 双字母 DC ≠ 单字母假设-D / 实验 C；且 ≠ 假设-V / 假设-DB / 假设-DA（硬）

| 维度 | 对照页 | 本页假设-DC（双字母） |
|------|--------|----------------------|
| 题面 V | **股票印花税**（主报股票：卖方、2023-08-28 前 1‰ / 后 0.5‰；税目是转让股票及以股票为基础的存托凭证） | V 主报股票。本页专测转债腿被发明印花税，不改 V 的股票切日、主报和 ETF/债券旁路。**DC≠V**；**严禁复用假设-V**；**不改 V**；不把「股票印花税已按卖方切片」写成「转债印花税已诚实」；`stock_stamp_handoff=v_page` |
| 题面 DB | **可转债经手费**（交易所；核对日 0.04‰；不是印花税） | 经手费 ≠ 印花税。**DC≠DB**；**不改 DB**；不把「转债经手费已诚实」写成「转债印花税已诚实」；**不升格 DB 的可交换债诊断桶**（`sse_szse_exchangeable_merged` 留在 DB，本页不收成主报，也不另升一桶） |
| 题面 DA | **场内基金过户费**（中国结算；二级不套股票 0.01‰） | 过户费 ≠ 印花税。**DC≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` 只旁路消费 |
| 题面 S | **沪深 A 股经手费三切日** | 经手费降 30% ≠ 印花税减半。**DC≠S**；**不改 S**；不把 2023-08-28 股票经手费降档写成转债印花税切日 |
| 题面 U | **股票过户费切日** | 过户 ≠ 印花税。**DC≠U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 AX | **基金/ETF 经手费** | 基金经手费 ≠ 转债印花税。**DC≠AX**；**不改 AX** |
| 题面 T | **证管费** | 证管费 ≠ 印花税。本页不展开转债证管费。**DC≠T**；**不改 T**；`csrc_fee_handoff=t_page` |
| 题面 Q | **可转债按股票规则回放**（回转、涨跌幅、收盘价、转股所得次日才可卖） | 规则混用 ≠ 印花税。**DC≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 转债腿印花税。**DC≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 印花税抽在哪一档。**双字母 DC ≠ 单字母假设-D**；**严禁复用假设-D**；**DC≠D**；**不改 D** |
| 题面 C | **股票池当时名单**（清单实验 C） | 池子名单 ≠ 印花税税目。**双字母 DC ≠ 单字母实验 C**；**严禁复用实验 C**；**DC≠C** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_stamp_tax_on_convertible_bond`（**建议**单一主报，**尚未冻**；禁与 `invent_asof_leak_cb_stamp` 双挂；DC1 不升格；`bilateral_stamp_on_cb` / `stock_cut_20230828_copied_onto_cb_stamp` / `vs_V_stock_stamp` 只作诊断桶，不升格主报） |
| 文档 | 清单实验 V / DB / DA / S / U / AX / T / Q / A / D（**只读；禁止改写**） | `假设-DC-可转债印花税误抽.md`（新建） |
| 预检键 | 实验字母 V / DB / DA / S / U / AX / T / Q / A / D / Y / G / N | 实验字母 **DC** / `dc0_primary_demo`；**不得**占用或改写预检 V/DB/DA/S/U/AX/T/Q/A/D |

**禁止**：把 DC 写成「V / DB / DA / S / U / AX / T / Q / A / D 的续篇」；把「股票印花税已诚实（V）/ 转债经手费已诚实（DB）/ 基金过户费已诚实（DA）」写成「转债印花税已诚实」；把实验字母 DC 与单字母 D/C 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 实验 C / 假设-V 读成双字母 DC**；**尤重勿把 `params.Y` 读成实验字母 DC**；**尤重 `params.G` ≠ 1‰ / 0.5‰（量纲与语义不同）**；把 `invent_asof_leak_cb_stamp` 升格进 `dc0`。本页主键只用 `dc0` / `dc1` / `dc2` 与 `cb_stamp_*`。不写下一字母。

---

## 1. 一句话假设（可检验、可证伪）

同一转债信号、同一未复权成交金额、同一当日回转（规则交 Q，本页不重开）、同一股票印花税切片（V 只旁路）下，回测对可转债腿误抽股票印花税（套 1‰ / 减半后 0.5‰、或买卖双边、或把 2023-08-28 股票减半抄成转债也有印花税切日），相对「上市公司可转债现货不在印花税税目内：税目是转让股票及以股票为基础的存托凭证；转债现货不是股票、也不是股票存托凭证；依法不征；缺证券类别或买卖方向则 skip」的诚实组，会**系统性改写转债腿成本**——相对依法不征偏悲观。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误抽股票印花税截在标定噪声带内可忽略，且「套 1‰ 或 0.5‰ / 核对日泄露 / 买卖双边 / 2023-08-28 抄成转债印花税切日 / vs V·DB·DA·S·U·AX·T·Q·A·D」分桶不改变结论，则本假设在该样本与税率设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 建议键（拉数前再定；本页不开跑；Y/G/N/Y2 · dc0 与锚 **三条尚未冻**）

```
# 配置建议键（见 §7；草稿·待入库预检；下列三条都是占位，尚未冻）
# 【消歧】params.Y = 显著性门槛；占位 0.02；**≠ 实验字母 DC ≠ 单字母假设-D ≠ 单字母实验 C**；勿把 params.Y 读成实验字母 DC
# 【消歧】params.G = 同族门槛；占位 0.01；**尤重：params.G ≠ 印花税 1‰ ≠ 减半后 0.5‰**（量纲与语义不同：无量纲相对门槛 ≠ 税率‰）；**≠ 实验字母 DC ≠ 单字母 D/C**
# 【消歧】params.N = 失败/废单率差门槛；占位 0.05；**≠ 实验字母 DC ≠ 单字母 D/C**
# params.Y2 占位 0.015
# params.Y / G / N / Y2               占位 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误抽股票印花税截 ΔFakeStockStamp / 净收益差 / DC1−DC2；**params.Y/G/N ≠ 实验字母 DC ≠ 单字母假设-D / 实验 C**；**尤重 params.G ≠ 1‰/0.5‰**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                    建议 next_open
# params.asof_check_date              建议 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  建议 skip
# params.cb_stamp_honest              建议 pit_cb_out_of_stamp_tax_scope
#   上市公司可转债现货不在印花税税目内；不抽股票 1‰ / 0.5‰；尚未冻
# params.cb_stamp_scope               建议 listed_cb_spot_not_stock_cdr
#   转债现货不是股票，也不是以股票为基础的存托凭证；不把 CDR 税目套到转债
# params.cb_stamp_over_policy         建议 skip_if_sec_type_or_side_missing
#   缺证券类别或买卖方向则 skip；禁止用 1‰ / 0.5‰ 补齐
# params.stock_stamp_handoff          建议 v_page
#   消费 V 的股票印花税，或显式旁路；不在本页重开股票切日，也不改 V
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的转债经手费，或显式旁路；经手费 ≠ 印花税；不升格 DB 可交换债诊断桶
# params.cb_rule_handoff              建议 q_page
#   回转、涨跌幅、收盘价、转股所得何时可卖交 Q；本页只测印花税
# params.stock_transfer_fee_handoff   建议 u_page
# params.etf_transfer_fee_handoff     建议 da_page
# params.csrc_fee_handoff             建议 t_page
#   证管费交 T；本页不展开转债证管费，也不写下一字母
# params.fee_tier_handoff             建议 s_page
# params.fund_fee_handoff             建议 ax_page
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
# params.cb_stamp_handoff             建议 self
# params.dc0_primary_demo             建议 invent_stamp_tax_on_convertible_bond
#   单一主报占位；禁与 invent_asof_leak_cb_stamp 双挂；DC1 不升格；诊断桶不升格；尚未冻
# params.dc0_invent_stamp_tax_on_convertible_bond 建议 True
# params.dc1_asof_leak_cb_stamp_only  建议 True
#   半泄露对照；DC1 不升格并列主报；不得把 invent_asof_leak_cb_stamp 写进 dc0
# params.dc2_pit_cb_stamp             建议 True
# params.merge_with_V                 建议 False
# params.merge_with_DB                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_S                 建议 False
# params.merge_with_U                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_T                 建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.missing_sec_type_policy      建议 skip
# params.missing_side_policy          建议 skip
# params.day_freq_proxy               建议 cb_stamp_sensitivity
# params.universe_rule                建议 cb_stamp_mischarge_check
# params.redline_v0_exempt_scope      建议 position_industry_dd_only
```

### 2.2 三组对照（DC0 / DC1 / DC2）

| 组 | 角色 | 口径 |
|----|------|------|
| DC0 | 天真 / 发明印花税 | 按 `dc0_primary_demo` **建议**单一主报 `invent_stamp_tax_on_convertible_bond`（尚未冻）：可转债腿套股票印花税（1‰ 或减半后 0.5‰）。**禁**与 `invent_asof_leak_cb_stamp` 双挂主报 |
| DC1 | 半泄露 | 仅核对日把股票印花税现行档或 2023-08-28 切日铺到转债全历史（`invent_asof_leak_cb_stamp`）；**不得升格并列主报**，也不得写进 `dc0` |
| DC2 | 诚实 / 税目外 | `cb_stamp_honest=pit_cb_out_of_stamp_tax_scope`（建议，尚未冻）：上市公司可转债现货不在印花税税目内，依法不征。股票印花税只消费 V，转债经手费只消费 DB，转债规则只消费 Q，股票过户费只消费 U，基金过户费只消费 DA，证管费只消费 T，或显式旁路 |

买卖双边（`bilateral_stamp_on_cb`）、把 2023-08-28 股票减半抄成转债印花税切日（`stock_cut_20230828_copied_onto_cb_stamp`）、以及相对 V 股票印花税的对照截（`vs_V_stock_stamp`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dc0_primary_demo`。DB 的可交换债诊断桶不收到本页。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **建议** `2026-10-16`；fill_time **建议** `next_open`；fail **建议** `skip`。以上与诚实锚同属三条里的锚，**尚未冻**。股票印花税的 1‰ / 0.5‰ 与 2023-08-28 是 V 已有的股票口径，本页只当作「被误套到转债腿」的对照，不改 V。代收税费表版本日期不是 `asof_check_date`。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dc0_primary_demo` / `params.Y`·G·N·Y2 / 混口径开关 / 桶）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DC0）/ 半泄露组（DC1）相对诚实组（DC2）的成本差、误抽股票印花税截**显著且集中在转债腿发明印花税桶**；分桶「套 1‰ 或 0.5‰ / 核对日泄露 / 买卖双边 / 2023-08-28 抄成转债印花税切日 / vs V·DB·DA·S·U·AX·T·Q·A·D」不改变主结论方向。方向是相对依法不征偏悲观。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 V 的股票印花税切日、DB 的转债经手费、Q 的回转与涨跌幅、T 的证管费、U/DA 的过户费、S/AX 的经手费、A 的板上容量、D 的成交时点解释；或 `dc0_primary_demo` 与 `invent_asof_leak_cb_stamp` 双挂；或 DC1 升格并列主报；或 `bilateral_stamp_on_cb` / `stock_cut_20230828_copied_onto_cb_stamp` / `vs_V_stock_stamp` 诊断桶升格主报；或把 DB 的可交换债诊断桶升到本页；或实验字母 DC 与单字母 D/C 或 params.Y/G/N 混读；或把 `params.G` 读成 1‰ 或 0.5‰。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额、同一当日回转（回转本身交 Q），对照 DC0/DC1/DC2。股票印花税走 V 的诚实档或显式旁路，不在本页重开股票切日。报告成本差、误抽股票印花税截。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_stamp_tax_on_convertible_bond` / `invent_asof_leak_cb_stamp` / `bilateral_stamp_on_cb` / `stock_cut_20230828_copied_onto_cb_stamp` / `vs_V_stock_stamp` / `vs_DB_cb_handling_fee` / `vs_DA_fund_transfer` / `vs_S_fee_tier` / `vs_U_stock_transfer_fee` / `vs_AX_fund_fee` / `vs_T_csrc_fee` / `vs_Q_cb_rule` / `vs_A_board_capacity` / `vs_D_fill_time`

`bilateral_stamp_on_cb`、`stock_cut_20230828_copied_onto_cb_stamp`、`vs_V_stock_stamp` 只作诊断桶：它们不是 `dc0`，也不是 DC1，**不得升格主报**。`invent_asof_leak_cb_stamp` 只服务 DC1，**不得升格进 `dc0`**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 用股票印花税 1‰ 或减半后 0.5‰ 当转债诚实档，或把 `params.G` 当成 1‰ / 0.5‰。**尤重：`params.G` ≠ 1‰ / 0.5‰**。
- 买卖两边都抽印花税，并把这桶升成主报。
- 把 2023-08-28 股票减半抄成「转债也有印花税切日」。该日是股票印花税减半，不是转债开征日，也不是 DB 的经手费切日。
- 把「股票印花税已诚实（V）」写成「转债印花税已诚实」。V 主报股票；本页不改 V。
- 把「转债经手费已诚实（DB）」写成「转债印花税已诚实」。不升格 DB 的可交换债诊断桶。
- 把代收税费表「没写可转债」发明成一张已核死的 0‰ 费率行，拿去改 V 或冒充本页已完成的税率表。本页诚实锚是税目范围外（建议 `pit_cb_out_of_stamp_tax_scope`），缺证券类别或买卖方向则 skip。
- 把转债证管费、转债过户费在本页展开，或顺手写下一字母。
- `dc0_primary_demo` 与 `invent_asof_leak_cb_stamp` 双挂主报；DC1 升格并列主报；诊断桶（`bilateral_stamp_on_cb` / `stock_cut_20230828_copied_onto_cb_stamp` / `vs_V_stock_stamp`）升格为第二个主报。
- 实验字母 DC 与单字母 D/C 或 params.Y/G/N 混读。
- 改 V / DB / DA / S / U / AX / T / Q / A / D 正文；抢 A 真数队列；标纸面齐；开真数/回测/实盘；用复权价当印花税基数；结论写成「转债不征印花税所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、证券类别（股票 / 以股票为基础的存托凭证 / 上市公司可转债现货）、买卖方向、未复权成交金额、交易日。
- 没有证券类别或买卖方向时，按 `cb_stamp_over_policy` 建议 skip，不得用 1‰ / 0.5‰ 补上。
- 旁路消费：V 的股票印花税、DB 的转债经手费、Q 的转债规则、U 的股票过户费、DA 的场内基金过户费、T 的证管费之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。**
- 未复权价；asof **建议** `2026-10-16`（尚未冻）。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **建议键摘要（三条尚未冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`cb_stamp_honest=pit_cb_out_of_stamp_tax_scope`；`cb_stamp_scope=listed_cb_spot_not_stock_cdr`；`cb_stamp_over_policy=skip_if_sec_type_or_side_missing`；`dc0_primary_demo=invent_stamp_tax_on_convertible_bond`（**建议**单一主报；禁与 `invent_asof_leak_cb_stamp` 双挂；DC1 不升格；诊断桶不升格主报）；`stock_stamp_handoff=v_page`；`cb_handling_fee_handoff=db_page`；`cb_rule_handoff=q_page`；`stock_transfer_fee_handoff=u_page`；`etf_transfer_fee_handoff=da_page`；`csrc_fee_handoff=t_page`；`merge_with_V/DB/DA/S/U/AX/T/Q/A/D=False`。
- `params.Y/G/N/Y2` **占位** `0.02/0.01/0.05/0.015`（相对门槛，不是税率表：成本差 / 误抽股票印花税截 ΔFakeStockStamp / 净收益差 / DC1−DC2；**尤重 params.G ≠ 1‰/0.5‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DC ≠ 单字母 D/C**；**勿把 params.Y 读成实验字母 DC，亦勿把单字母假设-D / 实验 C 读成双字母 DC**；占位，尚未冻；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`5680829`。

---

## 8. 结论

（空；草稿·待入库预检；三条尚未冻；未标纸面齐。）

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；可转债印花税误抽；`dc0_primary_demo` 建议 `invent_stamp_tax_on_convertible_bond`，单一主报，禁与 `invent_asof_leak_cb_stamp` 双挂，DC1 不升格；诊断桶 `bilateral_stamp_on_cb` / `stock_cut_20230828_copied_onto_cb_stamp` / `vs_V_stock_stamp` 不升格；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DC ≠ 单字母 D/C**，且 **params.G ≠ 1‰/0.5‰**；锚建议 `cb_stamp_honest=pit_cb_out_of_stamp_tax_scope` / scope=`listed_cb_spot_not_stock_cdr` / over_policy=`skip_if_sec_type_or_side_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；handoff：`stock_stamp_handoff=v_page`，`cb_handling_fee_handoff=db_page`，`cb_rule_handoff=q_page`，`stock_transfer_fee_handoff=u_page`，`etf_transfer_fee_handoff=da_page`，`csrc_fee_handoff=t_page`；`merge_with_V/DB/DA/S/U/AX/T/Q/A/D=False`；**DC≠V≠DB≠DA≠S≠U≠AX≠T≠Q≠A≠D**；**双字母 DC ≠ 单字母假设-D / 实验 C**；vs V：V 主报股票，本页专测转债腿发明印花税，不改 V；vs DB：经手费≠印花税，不升格 DB 可交换债诊断桶；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；不改假设-DB / 假设-DA 及其他已存在假设页；不写下一字母；不开真数/回测/实盘）。基 tip=`5680829`（本次提交前 HEAD `5680829a2aa3825b6b41d8fa5fcd409129fa5929`） |
