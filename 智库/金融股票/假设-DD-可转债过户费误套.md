# 假设-DD · 可转债过户费误套/发明（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `20bf276` 上清单 #112=DC 已收口（**不改假设-DC 正文**，亦不改已齐 A–DC / 假设-DA / 假设-DB 及其他已存在假设页）后写下一纸面 DD；清单 #112=DC，下一未占号 **#113=DD**；选题自 `事实与坑` 2026-11-06「代收税费表印花税、证管费、过户费三栏都不写可转债，不发明 0」与「股票过户费 0.01‰ 不要套到转债腿」；**新建实验 DD**  
状态：**预检有条件通过 · 三条已冻 · 待复检**（结论栏空；禁止把「可转债腿静默套股票过户费 0.01‰、或发明免费=0 冒充诚实、或缺官方‰仍不 skip」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**未标纸面齐**；**禁止标纸面齐**；**不改已齐 A–DC / 假设-DA / 假设-DB / 假设-DC**；尤其不改假设-U / 假设-DA / 假设-DB / 假设-DC / 假设-V / 假设-Q / 假设-D）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 DD（#113）。一句话误开：回测对可转债腿误套/发明股票过户费档（例如静默套 0.01‰、或发明「免费=0」冒充诚实、或缺官方‰仍不 skip），系统性改写转债腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DD** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DD**；**勿把 `params.Y` 读成实验字母 DD**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，0.01‰ 是股票过户费率；**params.G ≠ 实验字母 DD**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DD**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DD ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DD ≠ 单字母假设-A**）≠ **单字母实验 U**（股票过户费；**双字母 DD ≠ 单字母假设-U；严禁复用假设-U**）≠ **单字母实验 V**（股票印花税；**双字母 DD ≠ 单字母假设-V**）≠ 双字母 **DC**（可转债印花税）≠ **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **S**（股票经手费）≠ **AX**（基金经手费）≠ **T**（证管费）≠ **Q**（可转债规则混用）。**DD≠U≠DA≠DB≠DC≠V≠S≠AX≠T≠Q≠A≠D**。**params.Y/G/N ≠ 实验字母 DD；亦 ≠ 单字母 D**。**勿把 `params.Y` 读成实验字母 DD，亦勿把单字母假设-D 读成双字母 DD**。**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰**。

### 专节 · 双字母 DD ≠ 单字母假设-D；且 ≠ 假设-U / 假设-DA / 假设-DB / 假设-DC（硬）

| 维度 | 对照页 | 本页假设-DD（双字母） |
|------|--------|----------------------|
| 题面 U | **股票过户费**（主报股票：2015-08-01 起 0.02‰、2022-04-29 起 0.01‰ 双边；ETF/债券另表当时 skip） | U 主报股票过户。本页专测转债腿误套/发明过户费，不改 U 的股票切日、主报和 ETF/债券旁路。**DD≠U**；**严禁复用假设-U**；**不改 U**；不把「股票过户费已按切日切片」写成「转债过户费已诚实」；`stock_transfer_fee_handoff=u_page` |
| 题面 DA | **场内基金过户费**（中国结算；二级不套股票 0.01‰；申赎篮子与二级分列） | 场内基金过户费 ≠ 转债过户费。**DD≠DA**；**不改 DA**；不把「基金过户费已诚实」写成「转债过户费已诚实」；`etf_transfer_fee_handoff=da_page` 只旁路消费 |
| 题面 DB | **可转债经手费**（交易所；核对日 0.04‰；不是过户费） | 经手费 ≠ 过户费。**DD≠DB**；**不改 DB**；不把「转债经手费已诚实」写成「转债过户费已诚实」；**不升格 DB 的可交换债诊断桶**；`cb_handling_fee_handoff=db_page` |
| 题面 DC | **可转债印花税**（税目外；不是过户费） | 印花税 ≠ 过户费。**DD≠DC**；**不改 DC**；不把「转债印花税已诚实」写成「转债过户费已诚实」；`cb_stamp_handoff=dc_page` |
| 题面 V | **股票印花税** | 印花税 ≠ 过户费。**DD≠V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 S | **沪深 A 股经手费三切日** | 经手费 ≠ 过户费。**DD≠S**；**不改 S**；`fee_tier_handoff=s_page` |
| 题面 AX | **基金/ETF 经手费** | 基金经手费 ≠ 转债过户费。**DD≠AX**；**不改 AX**；`fund_fee_handoff=ax_page` |
| 题面 T | **证管费** | 证管费 ≠ 过户费。本页不展开转债证管费。**DD≠T**；**不改 T**；`csrc_fee_handoff=t_page` |
| 题面 Q | **可转债按股票规则回放**（回转、涨跌幅、收盘价、转股所得次日才可卖） | 规则混用 ≠ 过户费。**DD≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 转债腿过户费。**DD≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 过户费抽在哪一档。**双字母 DD ≠ 单字母假设-D**；**严禁复用假设-D**；**DD≠D**；**不改 D** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ashare_transfer_fee_on_convertible_bond`（**写死冻结**单一主报；禁与 `invent_asof_leak_cb_transfer_fee` 双挂；DD1 不升格；`invent_free_zero_cb_transfer` / `missing_official_bps_not_skip` / `vs_U_stock_transfer` / `vs_DA_etf_transfer` 只作诊断桶，不升格主报） |
| 文档 | 清单实验 U / DA / DB / DC / V / S / AX / T / Q / A / D（**只读；禁止改写**） | `假设-DD-可转债过户费误套.md`（新建） |
| 预检键 | 实验字母 U / DA / DB / DC / V / S / AX / T / Q / A / D / Y / G / N | 实验字母 **DD** / `dd0_primary_demo`；**不得**占用或改写预检 U/DA/DB/DC/V/S/AX/T/Q/A/D |

**禁止**：把 DD 写成「U / DA / DB / DC / V / S / AX / T / Q / A / D 的续篇」；把「股票过户已诚实（U）/ 基金过户已诚实（DA）/ 转债经手费已诚实（DB）/ 转债印花税已诚实（DC）」写成「转债过户费已诚实」；把实验字母 DD 与单字母 D 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-U 读成双字母 DD**；**尤重勿把 `params.Y` 读成实验字母 DD**；**尤重 `params.G` 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同）**；把 `invent_asof_leak_cb_transfer_fee` 升格进 `dd0`。本页主键只用 `dd0` / `dd1` / `dd2` 与 `cb_transfer_fee_*`。不写下一字母。

---

## 1. 一句话假设（可检验、可证伪）

同一转债信号、同一未复权成交金额、同一当日回转（规则交 Q，本页不重开）、同一股票过户费切片（U 只旁路）下，回测对可转债腿误套/发明股票过户费档（例如静默套 0.01‰、或发明「免费=0」冒充诚实、或缺官方‰仍不 skip），相对「可转债过户费按官方口径，勿发明；缺官方‰则 skip；禁静默 0.01‰；禁发明免费 0」的诚实组，会**系统性改写转债腿成本**——相对诚实锚偏误。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误套股票过户费截在标定噪声带内可忽略，且「静默套 0.01‰ / 核对日泄露 / 发明免费=0 / 缺官方‰仍不 skip / vs U·DA·DB·DC·V·S·AX·T·Q·A·D」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dd0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过 · 三条已冻 · 待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DD ≠ 单字母假设-D**；勿把 params.Y 读成实验字母 DD
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**尤重：params.G 的 0.01 ≠ 过户费 0.01‰**（量纲与语义不同：无量纲相对门槛 ≠ 过户费率‰）；**≠ 实验字母 DD ≠ 单字母 D**
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DD ≠ 单字母 D**
# params.Y2 写死冻结 0.015
# params.Y / G / N / Y2               写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误套股票过户费截 ΔFakeStockTransfer / 净收益差 / DD1−DD2；**params.Y/G/N ≠ 实验字母 DD ≠ 单字母假设-D**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）
# params.fill_time                    写死冻结 next_open
# params.asof_check_date              写死冻结 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  写死冻结 skip
# params.cb_transfer_fee_honest       写死冻结 pit_cb_official_transfer_not_stock_tier
#   诚实锚：可转债过户费按官方口径，勿发明
#   缺官方‰→skip；禁静默 0.01‰；禁发明免费 0
#   对照 DA 的 etf_transfer_fee_honest=pit_… 与 U 的股票过户 PIT 写法；枚举已写死冻结
#   不把「代收税费表没单列可转债」写成已经核死的 0‰
# params.cb_transfer_fee_scope        写死冻结 listed_cb_spot_apart_from_stock_and_etf
#   转债过户费 ≠ 股票过户（U）≠ 场内基金过户（DA）；不把 U 的 0.01‰ 或 DA 的二级口径写成转债已诚实
# params.cb_transfer_fee_over_policy  写死冻结 skip_if_official_cb_transfer_bps_missing
#   缺官方‰则 skip；禁静默 0.01‰；禁发明免费 0
# params.stock_transfer_fee_handoff   建议 u_page
#   消费 U 的股票过户费，或显式旁路；不在本页重开股票切日，也不改 U
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；基金过户费 ≠ 转债过户费；不改 DA
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的转债经手费，或显式旁路；经手费 ≠ 过户费；不升格 DB 可交换债诊断桶；不改 DB
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的转债印花税，或显式旁路；印花税 ≠ 过户费；不改 DC
# params.stock_stamp_handoff          建议 v_page
#   消费 V 的股票印花税，或显式旁路；不改 V
# params.cb_rule_handoff              建议 q_page
#   回转、涨跌幅、收盘价、转股所得何时可卖交 Q；本页只测过户费；不改 Q
# params.fee_tier_handoff             建议 s_page
# params.fund_fee_handoff             建议 ax_page
# params.csrc_fee_handoff             建议 t_page
#   证管费交 T；本页不展开转债证管费，也不写下一字母
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
# params.cb_transfer_fee_handoff      建议 self
# params.dd0_primary_demo             写死冻结 invent_ashare_transfer_fee_on_convertible_bond
#   单一主报写死，单挂；禁与 invent_asof_leak_cb_transfer_fee 双挂；DD1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_cb_transfer_fee 只作对照，不得升格进 dd0
# params.dd0_invent_ashare_transfer_fee_on_convertible_bond 建议 True
# params.dd1_asof_leak_cb_transfer_fee_only 建议 True
#   半泄露对照；DD1 不升格并列主报；不得把 invent_asof_leak_cb_transfer_fee 写进 dd0
# params.dd2_pit_cb_transfer_fee      建议 True
# params.merge_with_U                 建议 False
# params.merge_with_DA                建议 False
# params.merge_with_DB                建议 False
# params.merge_with_DC                建议 False
# params.merge_with_V                 建议 False
# params.merge_with_S                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_T                 建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.missing_cb_transfer_fee_policy 建议 skip
# params.day_freq_proxy               建议 cb_transfer_fee_sensitivity
# params.universe_rule                建议 cb_transfer_fee_mischarge_check
# params.redline_v0_exempt_scope      建议 position_industry_dd_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DD；勿把这个键读成实验 DD
```

### 2.2 三组对照（DD0 / DD1 / DD2）

| 组 | 角色 | 口径 |
|----|------|------|
| DD0 | 天真 / 误套股票过户档 | 按 `dd0_primary_demo` **写死冻结**单一主报 `invent_ashare_transfer_fee_on_convertible_bond`：可转债腿套股票过户费档（例如静默套 0.01‰）。**禁**与 `invent_asof_leak_cb_transfer_fee` 双挂主报 |
| DD1 | 半泄露 | 仅核对日把股票过户费现行档铺到转债全历史（`invent_asof_leak_cb_transfer_fee`）；**不得升格并列主报**，也不得写进 `dd0`（写死冻结：DD1 不升格） |
| DD2 | 诚实 / 官方口径 | `cb_transfer_fee_honest=pit_cb_official_transfer_not_stock_tier`（写死冻结）：可转债过户费按官方口径，勿发明。缺官方‰→skip；禁静默 0.01‰；禁发明免费 0。股票过户只消费 U，场内基金过户只消费 DA，转债经手费只消费 DB，转债印花税只消费 DC，股票印花税只消费 V，转债规则只消费 Q，或显式旁路 |

发明「免费=0」冒充诚实（`invent_free_zero_cb_transfer`）、缺官方‰仍不 skip（`missing_official_bps_not_skip`）、以及相对 U / DA 的对照截（`vs_U_stock_transfer` / `vs_DA_etf_transfer`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dd0_primary_demo`。DB 的可交换债诊断桶不收到本页。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dd0_primary_demo` 同属三条，**已写死冻结**。股票过户费的 0.02‰ / 0.01‰ 与 2022-04-29 是 U 已有的股票口径，本页只当作「被误套到转债腿」的对照，不改 U。场内基金过户费留在 DA，不改 DA。代收税费表版本日期不是 `asof_check_date`。核对日该表过户费栏不把可转债现货写成股票 0.01‰ 那一行；缺官方‰则 skip，不把「表上没单列」发明成免费 0，也不静默填 0.01‰。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dd0_primary_demo` / `params.Y`·G·N·Y2 / 混口径开关 / 桶）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DD0）/ 半泄露组（DD1）相对诚实组（DD2）的成本差、误套股票过户费截**显著且集中在转债腿误套/发明过户费桶**；分桶「静默套 0.01‰ / 核对日泄露 / 发明免费=0 / 缺官方‰仍不 skip / vs U·DA·DB·DC·V·S·AX·T·Q·A·D」不改变主结论方向。方向是相对诚实锚偏误。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 U 的股票过户切日、DA 的场内基金过户费、DB 的转债经手费、DC 的转债印花税、V 的股票印花税、Q 的回转与涨跌幅、T 的证管费、S/AX 的经手费、A 的板上容量、D 的成交时点解释；或 `dd0_primary_demo` 与 `invent_asof_leak_cb_transfer_fee` 双挂；或 DD1 升格并列主报；或 `invent_free_zero_cb_transfer` / `missing_official_bps_not_skip` / `vs_U_stock_transfer` / `vs_DA_etf_transfer` 诊断桶升格主报；或把 DB 的可交换债诊断桶升到本页；或实验字母 DD 与单字母 D 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成过户费 0.01‰。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额、同一当日回转（回转本身交 Q），对照 DD0/DD1/DD2。股票过户费走 U 的诚实档或显式旁路，不在本页重开股票切日。报告成本差、误套股票过户费截。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_ashare_transfer_fee_on_convertible_bond` / `invent_asof_leak_cb_transfer_fee` / `invent_free_zero_cb_transfer` / `missing_official_bps_not_skip` / `vs_U_stock_transfer` / `vs_DA_etf_transfer` / `vs_DB_cb_handling_fee` / `vs_DC_cb_stamp` / `vs_V_stock_stamp` / `vs_S_fee_tier` / `vs_AX_fund_fee` / `vs_T_csrc_fee` / `vs_Q_cb_rule` / `vs_A_board_capacity` / `vs_D_fill_time`

`invent_free_zero_cb_transfer`、`missing_official_bps_not_skip`、`vs_U_stock_transfer`、`vs_DA_etf_transfer` 只作诊断桶：它们不是 `dd0`，也不是 DD1，**不得升格主报**。`invent_asof_leak_cb_transfer_fee` 只服务 DD1，**不得升格进 `dd0`**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 用股票过户费 0.01‰ 当转债诚实档，或把 `params.G` 的 0.01 当成过户费 0.01‰。**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰**。
- 缺官方可转债过户费‰，却静默填股票 0.01‰。
- 把「代收税费表没写可转债」发明成免费=0，并拿去冒充诚实锚。诚实锚是官方口径；缺官方‰则 skip；禁静默 0.01‰；禁发明免费 0。
- 缺官方‰仍不 skip，并用 0 或 0.01‰ 把腿填上。
- 把「股票过户已诚实（U）」写成「转债过户费已诚实」。U 主报股票；本页不改 U。
- 把「场内基金过户费已诚实（DA）」写成「转债过户费已诚实」。不改 DA。
- 把「转债经手费已诚实（DB）/ 转债印花税已诚实（DC）」写成「转债过户费已诚实」。经手费、印花税 ≠ 过户费。不改 DB / DC。
- `dd0_primary_demo` 与 `invent_asof_leak_cb_transfer_fee` 双挂主报；DD1 升格并列主报；诊断桶（`invent_free_zero_cb_transfer` / `missing_official_bps_not_skip` / `vs_U_stock_transfer` / `vs_DA_etf_transfer`）升格为第二个主报。
- 实验字母 DD 与单字母 D 或 params.Y/G/N 混读。
- 改 U / DA / DB / DC / V / S / AX / T / Q / A / D 正文；抢 A 真数队列；标纸面齐；开真数/回测/实盘；用复权价当过户费基数；结论写成「转债过户费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、证券类别（股票 / 场内基金或 ETF / 上市公司可转债现货）、未复权成交金额、交易日。
- 没有证券类别，或没有官方可转债过户费‰时，按写死冻结的 `cb_transfer_fee_over_policy=skip_if_official_cb_transfer_bps_missing` skip，不得用 0.01‰ 补上，也不得发明免费 0。
- 旁路消费：U 的股票过户费、DA 的场内基金过户费、DB 的转债经手费、DC 的转债印花税、V 的股票印花税、Q 的转债规则之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。**
- 未复权价；asof **写死冻结** `2026-10-16`。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`cb_transfer_fee_honest=pit_cb_official_transfer_not_stock_tier`（缺官方‰→skip；禁静默 0.01‰；禁发明免费 0）；`cb_transfer_fee_scope=listed_cb_spot_apart_from_stock_and_etf`；`cb_transfer_fee_over_policy=skip_if_official_cb_transfer_bps_missing`；`dd0_primary_demo=invent_ashare_transfer_fee_on_convertible_bond`（**写死冻结**单一主报；禁与 `invent_asof_leak_cb_transfer_fee` 双挂；DD1 不升格；诊断桶不升格主报）；`stock_transfer_fee_handoff=u_page`；`etf_transfer_fee_handoff=da_page`；`cb_handling_fee_handoff=db_page`；`cb_stamp_handoff=dc_page`；`stock_stamp_handoff=v_page`；`cb_rule_handoff=q_page`；`merge_with_U/DA/DB/DC/V/S/AX/T/Q/A/D=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误套股票过户费截 ΔFakeStockTransfer / 净收益差 / DD1−DD2；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DD ≠ 单字母 D**；**勿把 params.Y 读成实验字母 DD，亦勿把单字母假设-D 读成双字母 DD**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值）。
- oos_split 四日期建议占位；禁 holdout 反调。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。草稿行基 tip=`20bf276`；三冻补丁基 tip=`b7ead20c`。

---

## 8. 结论

（空；预检有条件通过 · 三条已冻 · 待复检；复检通过前不得标纸面齐；**禁止标纸面齐**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-09）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DD-20261109.md`（原样落入，不改结论；SHA256=`1ca40e1d57cc5c166bc0e04c9ab6501e70efcffb40c6567eb6e1116dc1782030`；预检 2026-11-09；**结论：有条件通过**；tip基=`b7ead20c` / `b7ead20c86c9e0e082c6b525a26e106ce1cc5154`；本补丁分支起点 HEAD=`a0fdab2` / `a0fdab2fb53cfa2568fa53caf8bdc2885c69ff6a`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、误套股票过户费截 ΔFakeStockTransfer、净收益差、DD1−DD2 专项。**`params.Y` ≠ 实验字母 DD**；**`params.G` ≠ 实验字母 DD**；**`params.N` ≠ 实验字母 DD**；亦 ≠ 单字母假设-D。**勿把 `params.Y` 读成实验字母 DD，亦勿把单字母假设-D 读成双字母 DD**。**尤重：`params.G` 的 `0.01` ≠ 过户费 `0.01‰`**（**params.G 的 0.01 ≠ 过户费 0.01‰**）。二者量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，0.01‰ 是股票过户费率，禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dd0_primary_demo`**：**写死冻结** **`invent_ashare_transfer_fee_on_convertible_bond`**（单一主报，单挂写死）。**禁止**与 **`invent_asof_leak_cb_transfer_fee`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DD1 核对日把股票过户费现行档铺到转债全历史只作半泄露对照，**不得升格与 dd0 并列主报**，也不得把 `invent_asof_leak_cb_transfer_fee` 写进 `dd0`。`invent_free_zero_cb_transfer` / `missing_official_bps_not_skip` / `vs_U_stock_transfer` / `vs_DA_etf_transfer` **只作诊断桶，不得升格主报**。

3. **可转债过户费诚实锚六键升格写死（不可再写「建议」；键名前缀按本页既有 `cb_transfer_fee_*`，对照 DA 的 `etf_transfer_fee_*` 与 U 的股票过户 PIT）**：`params.cb_transfer_fee_honest=pit_cb_official_transfer_not_stock_tier`；`params.cb_transfer_fee_scope=listed_cb_spot_apart_from_stock_and_etf`；`params.cb_transfer_fee_over_policy=skip_if_official_cb_transfer_bps_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺官方‰→skip；禁静默 0.01‰；禁发明免费 0。禁止跑后改锚，或用股票过户费 0.01‰ / 核对日股票过户费现行档 / 发明免费 0 铺满转债全历史冒充诚实 PIT。

**硬分列保住**：DD≠U≠DA≠DB≠DC≠V≠S≠AX≠T≠Q≠A≠D；**双字母 DD ≠ 单字母假设-D / 假设-U**；**params.Y / params.G / params.N ≠ 实验字母 DD ≠ 单字母 D**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰**；不抢 A；不改已齐 A–DC / 假设-DA / 假设-DB / 假设-DC 正文。

**状态**：预检有条件通过 · 三条已冻 · 待复检；**禁止标任何纸面齐**；**未标纸面齐**；**禁止标纸面齐**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 风控预检补丁·冻结三条写死——依据 `预检-假设DD-20261109.md`（SHA256=`1ca40e1d57cc5c166bc0e04c9ab6501e70efcffb40c6567eb6e1116dc1782030`；结论=有条件通过；tip基=`b7ead20c` / `b7ead20c86c9e0e082c6b525a26e106ce1cc5154`；分支起点 HEAD=`a0fdab2` / `a0fdab2fb53cfa2568fa53caf8bdc2885c69ff6a`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔFakeStockTransfer / 净收益差 / DD1−DD2；**params.Y/G/N ≠ 实验字母 DD ≠ 单字母 D**；**勿把 params.Y 读成实验字母 DD，亦勿把单字母假设-D 读成双字母 DD**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同）**；禁 null；禁 holdout/OOS 标定）；② `params.dd0_primary_demo=invent_ashare_transfer_fee_on_convertible_bond`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_cb_transfer_fee` 双挂；DD1 不升格；诊断桶 `invent_free_zero_cb_transfer` / `missing_official_bps_not_skip` / `vs_U_stock_transfer` / `vs_DA_etf_transfer` 不升格）；③ 锚六键写死 `cb_transfer_fee_honest=pit_cb_official_transfer_not_stock_tier` / `cb_transfer_fee_scope=listed_cb_spot_apart_from_stock_and_etf` / `cb_transfer_fee_over_policy=skip_if_official_cb_transfer_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`（缺官方‰→skip；禁静默 0.01‰；禁发明免费 0）。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；不改已齐 A–DC / 假设-DA / 假设-DB / 假设-DC；不开回测/真数/实盘。基于 tip=`b7ead20c`。 |
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；可转债过户费误套/发明；`dd0_primary_demo` 建议 `invent_ashare_transfer_fee_on_convertible_bond`，单一主报，禁与 `invent_asof_leak_cb_transfer_fee` 双挂，DD1 不升格；诊断桶 `invent_free_zero_cb_transfer` / `missing_official_bps_not_skip` / `vs_U_stock_transfer` / `vs_DA_etf_transfer` 不升格；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DD ≠ 单字母 D**，且 **params.G 的 0.01 ≠ 过户费 0.01‰**；锚建议 `cb_transfer_fee_honest=pit_cb_official_transfer_not_stock_tier`（缺官方‰→skip；禁静默 0.01‰；禁发明免费 0）/ scope=`listed_cb_spot_apart_from_stock_and_etf` / over_policy=`skip_if_official_cb_transfer_bps_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；handoff：`stock_transfer_fee_handoff=u_page`，`etf_transfer_fee_handoff=da_page`，`cb_handling_fee_handoff=db_page`，`cb_stamp_handoff=dc_page`，`stock_stamp_handoff=v_page`，`cb_rule_handoff=q_page`；`merge_with_U/DA/DB/DC/V/S/AX/T/Q/A/D=False`；**DD≠U≠DA≠DB≠DC≠V≠S≠AX≠T≠Q≠A≠D**；**双字母 DD ≠ 单字母假设-D**；vs U：U 主报股票过户，本页专测转债腿误套/发明过户费，不改 U；vs DA：场内基金过户费 ≠ 转债过户费，不改 DA；vs DB/DC：经手费/印花税 ≠ 过户费，不改 DB/DC；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；不改已齐 A–DC / 假设-DA / 假设-DB / 假设-DC 及其他已存在假设页；不写下一字母；不开真数/回测/实盘）。基 tip=`20bf276`（本次提交前 HEAD `20bf276efe3cbd18aa897ff765f6d710e7e85654`） |
