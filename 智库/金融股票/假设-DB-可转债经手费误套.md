# 假设 DB · 可转债经手费误套 A 股 0.0341‰ / 把股票降档或债券暂免抄到转债（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `a54e96a` 上清单 #110=DA 已标 A/D–DA纸面齐（**不改 DA 正文**，亦不改已冻 A–CZ）后写下一纸面 DB；清单 #110=DA，下一未占号 **#111=DB**（与 2026-11-06 预留一致）；选题自 `事实与坑` 2026-11-06「可转债经手费是 0.04‰，不是 A 股 0.0341‰；切日沪深也不一样」与清单预留段；**新建实验 DB**  
状态：**草稿 · 待入库预检**（结论栏空；**三条尚未冻**；禁止把「可转债腿套 A 股经手费 0.0341‰」或「2023-08-28 股票降 30% / 普通债券暂免抄到上市公司转债现货」或「沪市切日前用 0.04‰」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**未标纸面齐**；**不改已冻 A–DA**；尤其不改假设-S / 假设-AX / 假设-DA / 假设-Q / 假设-A / 假设-U）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 DB（#111）。一句话误开：回测对可转债腿误套 A 股经手费 0.0341‰，或把 2023-08-28 股票降 30%/普通债券暂免抄到上市公司转债现货，或沪市切日前误用 0.04‰，系统性改写转债腿成本。

> **字母消歧（硬）**：本页**实验字母 DB** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；**params.Y ≠ 实验字母 DB**）≠ **`params.G`**（同族门槛占位，建议 0.01；**这个 0.01 不是费率**——不是转债 0.04‰，也不是 A 股 0.0341‰，更不是沪市切日前的 0.0001%；**params.G ≠ 实验字母 DB**）≠ **`params.N`**（失败/废单率差门槛；**params.N ≠ 实验字母 DB**）≠ **单字母实验 B**（除权日用复权价误判涨停，清单实验 B 旧位；**双字母 DB ≠ 单字母假设-B；严禁复用假设-B**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DB ≠ 单字母假设-A；严禁复用假设-A**）≠ **单字母实验 S**（沪深 A 股经手费三切日；**双字母 DB ≠ 单字母假设-S；严禁复用假设-S**）≠ 双字母 **AX**（基金经手费）≠ **DA**（场内基金过户费）≠ **Q**（可转债规则混用）≠ **U**（股票过户费）≠ **CZ**（存托凭证可成交；本页不引用其主键）。**DB≠S≠AX≠DA≠Q≠A≠B≠U≠CZ**。**params.Y/G/N ≠ 实验字母 DB；亦 ≠ 单字母 B/A/S**。

### 专节 · 双字母 DB ≠ 单字母假设-B / 假设-A / 假设-S；且 ≠ 假设-AX / 假设-DA / 假设-Q（硬）

| 维度 | 对照页 | 本页假设-DB（双字母） |
|------|--------|----------------------|
| 题面 S | **沪深 A 股竞价经手费三切日**（现行档 0.0341‰；2023-08-28 股票降 30%，不是减半） | 股票三切日留在 S。本页不改切日，也不用 0.0341‰ 当转债诚实档。**双字母 DB ≠ 单字母假设-S**；**严禁复用假设-S**；**DB≠S**；**不改 S**；不把「A 股经手费已诚实」写成「转债经手费已诚实」；`ashare_fee_handoff=s_page` |
| 题面 AX | **基金/ETF 经手费**（基金竞价档；核对日 0.04‰；切日 2021-07-19；2023-08-28 不改基金） | 数字同是 0.04‰ ≠ 同一档。AX 是基金，本页是上市公司可转债现货。**DB≠AX**；**不改 AX**；不把「基金经手费已诚实」写成「转债经手费已诚实」；`fund_fee_handoff=ax_page` |
| 题面 DA | **场内基金过户费**（中国结算；二级不套股票 0.01‰） | 过户费是中国结算，经手费是交易所。**DB≠DA**；**不改 DA**；不把「基金过户费已诚实」写成「转债经手费已诚实」；`etf_transfer_fee_handoff=da_page` 只旁路消费 |
| 题面 Q | **可转债按股票规则回放**（当日回转、涨跌幅、收盘价、转股所得次日才可卖） | 规则混用 ≠ 经手费。Q 的 2022-08-01 是次日 ±20% 板，本页的 2022-08-01 是沪市经手费切日，两件事不互相代替。**DB≠Q**；**不改 Q**；不把「转债规则已诚实」写成「转债经手费已诚实」；`cb_rule_handoff=q_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 转债腿经手费。**双字母 DB ≠ 单字母假设-A**；**严禁复用假设-A**；**不抢 A 真数队列**；**DB≠A**；**不改 A**；`board_capacity_handoff=a_page` |
| 题面 B | **除权日用复权价误判涨停**（清单实验 B 旧位） | 复权价判板 ≠ 经手费档。**双字母 DB ≠ 单字母假设-B**；**严禁复用假设-B**；**DB≠B**；**不改 B**；`ex_rights_limit_handoff=b_page` |
| 题面 U | **股票过户费切日** | 过户 ≠ 经手。**DB≠U**；**不改 U**；不把「股票过户已诚实」写成「转债经手费已诚实」 |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ashare_fee_on_convertible_bond`（**建议**单一主报；尚未冻；禁与 `invent_asof_leak_cb_handling_fee` 双挂；DB1 不升格） |
| 文档 | 清单实验 S / AX / DA / Q / A / B / U（**只读；禁止改写**） | `假设-DB-可转债经手费误套.md`（新建） |
| 预检键 | 实验字母 S / AX / DA / Q / A / B / U / Y / G / N | 实验字母 **DB** / `db0_primary_demo`；**不得**占用或改写预检 S/AX/DA/Q/A/B/U |

**禁止**：把 DB 写成「S / AX / DA / Q / A / B / U 的续篇」；把「A 股经手费已诚实（S）/ 基金经手费已诚实（AX）/ 基金过户费已诚实（DA）/ 转债规则已诚实（Q）/ 板上已诚实（A）/ 除权判板已诚实（B）/ 股票过户已诚实（U）」写成「转债经手费已诚实」；把实验字母 DB 与单字母 B/A/S 或 params.Y/G/N 混读；**尤重勿把单字母假设-S / 假设-B / 假设-A 读成双字母 DB**。本页主键只用 `db0` / `db1` / `db2` 与 `cb_handling_fee_*`。

---

## 1. 一句话假设（可检验、可证伪）

同一转债信号、同一未复权成交金额、同一当日回转（规则交 Q，本页不重开）、同一股票经手费切片（S 只旁路）下，回测对可转债腿误套 A 股经手费 0.0341‰，或把 2023-08-28 股票降 30%/普通债券暂免抄到上市公司转债现货，或沪市切日前误用 0.04‰，相对「上市公司可转债现货按当时档：沪深核对日 0.04‰ 双边；沪市 2022-08-01 才从 0.0001%+单笔帽 100 元改到 0.004% 无帽；深市不抄该切日；2023-08-28 不改转债；普通债券暂免不含上市公司可转债现货；回售与非上市公司转债按表暂免；可交换债沪深分列」的诚实组，会**系统性改写转债腿成本**——套 0.0341‰ 略低估；把暂免或股票降档抄到现货会发明免费或减档通道；沪市切日前用 0.04‰ 会高估早年成本。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误套 A 股档截、沪市切日前误用截在标定噪声带内可忽略，且「误套 0.0341‰ / 核对日泄露 / 2023-08-28 抄到转债 / 债券暂免铺到现货 / 沪深可交换债合成一句 / vs S·AX·DA·Q·A·B·U」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前才冻结；本草稿三条尚未冻；下列均为建议占位）

```
# 配置写死键（见文末变更；草稿·待入库预检；值均建议占位，尚未冻）
# 【消歧】params.Y = 显著性门槛；建议占位 0.02；**≠ 实验字母 DB ≠ 单字母假设-B ≠ 单字母假设-A ≠ 单字母假设-S**
# 【消歧】params.G = 同族门槛占位；建议占位 0.01；**这个 0.01 不是费率**（不是 0.04‰，不是 0.0341‰，不是 0.0001%）；**≠ 实验字母 DB ≠ 单字母 B/A/S**
# 【消歧】params.N = 失败/废单率差门槛；建议占位 0.05；**≠ 实验字母 DB ≠ 单字母 B/A/S**
# params.Y2 建议占位 0.015
# params.Y / G / N / Y2               建议占位 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误套 A 股档截 / 沪市切日前误用截 / DB1−DB2；禁 null；禁 holdout/OOS 标定；勿改已冻他字母数值；**尚未冻**）
# params.fill_time                    建议 next_open
# params.asof_check_date              建议 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  建议 skip
# params.cb_handling_fee_honest       建议 pit_listed_cb_spot_not_ashare_tier
#   上市公司可转债现货不套 A 股 0.0341‰；2023-08-28 不改转债；普通债券暂免不含该现货
# params.cb_handling_fee_scope        建议 sse_20220801_cut_szse_keep_listed_spot_not_waived
#   沪市 2022-08-01 前：0.0001% 双向 + 单笔帽 100 元；该日及之后：0.004% 双向、无这笔帽
#   深市不抄沪市切日，继续按 0.04‰；不发明深市更早首次生效日
# params.cb_handling_fee_exchangeable 建议 sse_szse_listed_apart
#   沪市可交换债与转债分列（核对日可走债券暂免档）；深市可交换与可转债同 0.04‰
#   沪深可交换债勿合成一句
# params.cb_handling_fee_over_policy  建议 skip_if_official_cb_handling_bps_missing
# params.cb_handling_fee_spot_bps     建议 0.04
#   单位 ‰，双边；0.04‰ = 0.004%。沪深上市公司可转债现货竞价核对日档。建议占位，尚未冻
# params.cb_handling_fee_sse_pre_cut_pct 建议 0.0001
#   单位是 %，不是 ‰。0.0001% = 0.001‰，不要写成 0.0001‰，也不要写成 0.04‰
# params.cb_handling_fee_sse_pre_cut_cap_cny 建议 100
#   单笔最高 100 元；2022-08-01 起沪市这笔帽取消
# params.cb_handling_fee_sse_cut_date 建议 2022-08-01
#   只切沪市经手费。不是 Q 的涨跌幅切日，不是 S 的股票降档日
# params.cb_handling_fee_szse_copy_sse_cut 建议 False
# params.cb_handling_fee_stock_cut_20230828_applies 建议 False
# params.cb_handling_fee_ashare_misapply_bps 建议 0.0341
#   天真组误套用的 A 股档，不是诚实档
# params.ordinary_bond_waiver_start   建议 2022-07-01
# params.ordinary_bond_waiver_end     建议 2026-12-31
# params.ordinary_bond_waiver_covers_listed_cb_spot 建议 False
# params.cb_handling_fee_put_and_nonlisted 建议 table_waiver
#   上市公司可转债回售、以及除上市公司可转债以外的转债，按表暂免；现货竞价仍收费
# params.ashare_fee_handoff           建议 s_page
#   消费 S 的 A 股经手费 PIT，或显式旁路；不在本页重开 2012-09-01 / 2015-08-01 / 2023-08-28
# params.fund_fee_handoff             建议 ax_page
#   消费 AX 的基金经手费诚实档，或显式旁路；基金 0.04‰ ≠ 转债 0.04‰
# params.cb_rule_handoff              建议 q_page
#   回转、涨跌幅、收盘价、转股所得何时可卖交 Q；本页只测经手费
# params.etf_transfer_fee_handoff     建议 da_page
#   只旁路消费 DA 的场内基金过户费诚实结果；本页不重开过户费，也不改 DA
# params.board_capacity_handoff       建议 a_page
# params.ex_rights_limit_handoff      建议 b_page
# params.cb_handling_fee_handoff      建议 self
# params.db0_primary_demo             建议 invent_ashare_fee_on_convertible_bond
#   单一主报；禁与 invent_asof_leak_cb_handling_fee 双挂；尚未冻
# params.db0_invent_ashare_fee_on_convertible_bond 建议 True
# params.db1_asof_leak_cb_handling_fee_only 建议 True
#   半泄露对照；DB1 不升格并列主报
# params.db2_pit_cb_handling_fee      建议 True
# params.merge_with_S                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_B                 建议 False
# params.merge_with_U                 建议 False
# params.merge_with_CZ                建议 False
# params.missing_cb_handling_fee_policy 建议 skip
# params.day_freq_proxy               建议 cb_handling_fee_sensitivity
# params.universe_rule                建议 cb_handling_fee_mischarge_check
# params.redline_v0_exempt_scope      建议 position_industry_dd_only
```

### 2.2 三组对照（DB0 / DB1 / DB2）

| 组 | 角色 | 口径 |
|----|------|------|
| DB0 | 天真 / 误套 A 股档 | 按 `db0_primary_demo` **建议**单一主报 `invent_ashare_fee_on_convertible_bond`：可转债腿按 A 股经手费 0.0341‰ 抽（**禁**与 `invent_asof_leak_cb_handling_fee` 双挂主报） |
| DB1 | 半泄露 | 仅核对日 0.04‰ 铺满全历史，含沪市 2022-08-01 前；**不得升格并列主报** |
| DB2 | 诚实 / PIT | `cb_handling_fee_honest=pit_listed_cb_spot_not_ashare_tier`（建议）：上市公司可转债现货按当时档；沪市 2022-08-01 切片；深市不抄该切日；2023-08-28 不改转债；普通债券暂免不含现货；回售与非上市公司转债按表暂免；可交换债沪深分列。A 股经手费只消费 S，基金经手费只消费 AX，转债规则只消费 Q，基金过户费只消费 DA，或显式旁路 |

把 2023-08-28 股票降 30% 抄到转债、或把普通债券暂免铺到上市公司转债现货，放进 §4.1 分桶，**不得升格为第二个主报**，也不得改写 `db0_primary_demo`。清单预留段里的四组叙述保留在旧行，本页不改那两行；误切不另升主报，泄露就是 DB1。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，不在本草稿写死起止日。asof **建议** `2026-10-16`；fill_time **建议** `next_open`；fail **建议** `skip`。收费表引用见 `事实与坑` 2026-11-06（两所 2026 年 1 月表；沪市切日文本是上证发〔2022〕118 号）。表的版本日期不是 `asof_check_date`。118 号自 2023-08-28 废止，是并进收费指引，不是改回 0.0001%，也不是转债跟着股票降 30%。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前冻结；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DB0）/ 半泄露组（DB1）相对诚实组（DB2）的成本差、误套 A 股档截、沪市切日前误用截**显著且集中在转债经手费误套桶**；分桶「误套 0.0341‰ / 核对日泄露 / 2023-08-28 抄到转债 / 债券暂免铺到现货 / 沪深可交换债合成一句 / vs S·AX·DA·Q·A·B·U」不改变主结论方向。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 S 的 A 股三切日、AX 的基金经手费、DA 的基金过户费、Q 的回转与涨跌幅、A 的板上容量、B 的除权判板解释；或 `db0_primary_demo` 与 `invent_asof_leak_cb_handling_fee` 双挂；或 DB1 升格并列主报；或实验字母 DB 与单字母 B/A/S 或 params.Y/G/N 混读。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额、同一当日回转（回转本身交 Q），对照 DB0/DB1/DB2。A 股经手费走 S 的诚实档或显式旁路，不在本页重开股票三切日。报告成本差、误套 A 股档截、沪市切日前误用截。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前冻结；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_ashare_fee_on_convertible_bond` / `invent_asof_leak_cb_handling_fee` / `stock_cut_20230828_copied_onto_cb` / `ordinary_bond_waiver_on_listed_cb_spot` / `sse_szse_exchangeable_merged` / `vs_S_ashare_fee` / `vs_AX_fund_fee` / `vs_DA_fund_transfer` / `vs_Q_cb_rule` / `vs_A_board_capacity` / `vs_B_ex_rights_limit` / `vs_U_stock_transfer_fee`

`stock_cut_20230828_copied_onto_cb` 与 `ordinary_bond_waiver_on_listed_cb_spot` 只作诊断桶：现货仍不套 0.0341‰，但把股票降档或普通债券暂免抄到上市公司转债现货。它们不是 `db0`，也不是 DB1。`sse_szse_exchangeable_merged` 只诊断「沪深可交换债被合成一句」，不升格主报。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 用 A 股 0.0341‰ 当转债诚实档，或把 `params.G=0.01` 当成 0.04‰ / 0.0341‰ / 0.0001%。
- 把 0.0001% 写成 0.0001‰，或把 0.004% 与 0.04‰ 当成两个不同的数。
- 把 2023-08-28 股票降 30% 写成转债也降了档；把 118 号废止理解成改回 0.0001%。
- 把普通债券暂免（2022-07-01～2026-12-31）铺到上市公司可转债现货。回售、非上市公司转债按表暂免，不能反过来证明现货免费。
- 沪市 2022-08-01 前也按 0.04‰；或把该切日抄到深市。深市 2022-07-29 通知写的是继续按现行 0.04‰。更早的深市首次生效日未核死，缺则 skip，不发明。
- 把沪市可交换债（与转债分列，核对日可暂免档）和深市可交换债（与可转债同 0.04‰）合成一句。
- 把北交所转债套成沪深 0.04‰（本页未核，缺则 skip，不发明 0）。
- 把转债过户费、证管费、印花税发明成 0 或套股票档。代收税费表这三栏都不写可转债；本页不展开，也不派下一字母。
- 把「A 股经手费已诚实（S）/ 基金经手费已诚实（AX）/ 基金过户费已诚实（DA）/ 转债规则已诚实（Q）」写成「转债经手费已诚实」。Q 的 2022-08-01 板幅切日不能代替本页经手费切日。
- `db0_primary_demo` 与 `invent_asof_leak_cb_handling_fee` 双挂主报；DB1 升格并列主报；诊断桶升格为第二个主报。
- 实验字母 DB 与单字母 B/A/S 或 params.Y/G/N 混读。
- 改 S / AX / DA / Q / A / B / U 正文；抢 A 真数队列；标纸面齐；开真数/回测/实盘；用复权价当经手费基数；结论写成「这类转债费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、交易所（沪/深；北交所缺官方档则 skip）、未复权成交金额、交易日。
- 品种：上市公司可转债现货 / 上市公司可转债回售 / 非上市公司转债 / 可交换债。没有这列时，不得把暂免或现货档互相填上。
- 官方经手费档与切日：缺则 skip，禁止用 0.0341‰ 或静默 0 补齐。
- 旁路消费：S 的 A 股经手费、AX 的基金经手费、Q 的转债规则、DA 的场内基金过户费、A 的板上、B 的除权判板、U 的股票过户之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。**

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **建议键摘要（三条尚未冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`cb_handling_fee_honest=pit_listed_cb_spot_not_ashare_tier`；`cb_handling_fee_scope=sse_20220801_cut_szse_keep_listed_spot_not_waived`；`cb_handling_fee_exchangeable=sse_szse_listed_apart`；`cb_handling_fee_over_policy=skip_if_official_cb_handling_bps_missing`；`db0_primary_demo=invent_ashare_fee_on_convertible_bond`（建议单一主报；禁与 `invent_asof_leak_cb_handling_fee` 双挂；DB1 不升格）；`ashare_fee_handoff=s_page`；`fund_fee_handoff=ax_page`；`cb_rule_handoff=q_page`；`etf_transfer_fee_handoff=da_page`；`merge_with_S/AX/DA/Q/A/B/U/CZ=False`。
- `params.Y/G/N/Y2` **建议占位** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表；**params.G 的 0.01 ≠ 0.04‰ ≠ 0.0341‰**；**params.Y/G/N ≠ 实验字母 DB ≠ 单字母 B/A/S**；禁 null；禁 holdout；勿改已冻他字母数值）。
- oos_split 四日期建议占位；禁 holdout 反调。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。变更基 tip 见文末，用本次提交前 HEAD `a54e96a`。

---

## 8. 结论

（空。状态=草稿 · 待入库预检；三条尚未冻；入库预检通过前不得把建议占位改写成已冻，也不得标纸面齐。）

---

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；可转债经手费误套；`db0_primary_demo` 建议 `invent_ashare_fee_on_convertible_bond`，单一主报，禁与 `invent_asof_leak_cb_handling_fee` 双挂，DB1 不升格；Y/G/N/Y2 建议占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DB ≠ 单字母 B/A/S**，且 params.G 的 0.01 不是 0.04‰ 也不是 0.0341‰；锚建议 `cb_handling_fee_honest=pit_listed_cb_spot_not_ashare_tier` / scope=`sse_20220801_cut_szse_keep_listed_spot_not_waived` / exchangeable=`sse_szse_listed_apart` / over_policy=`skip_if_official_cb_handling_bps_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；handoff：`ashare_fee_handoff=s_page`，`fund_fee_handoff=ax_page`，`cb_rule_handoff=q_page`，`etf_transfer_fee_handoff=da_page`；`merge_with_S/AX/DA/Q/A/B/U/CZ=False`；**DB≠S≠AX≠DA≠Q≠A≠B≠U≠CZ**；**双字母 DB ≠ 单字母假设-B / 假设-A / 假设-S；严禁复用假设-S**；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；不改已冻 A–DA；不写下一字母；不开真数/回测/实盘）。基 tip=`a54e96a`（本次提交前 HEAD `a54e96a91df7f1a7eafc41af8972ded8659cde0a`） |
