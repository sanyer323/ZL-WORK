# 假设 DA · 场内基金过户费误套股票 0.01‰ / 把申赎篮子过户当二级成交过户（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `0b73994` 上 CZ 为「预检有条件通过 · 三条已冻 · 待复检」（未标纸面齐；**不改 CZ 正文**）后写下一纸面 DA；清单 #109=CZ，下一未占号 **#110=DA**（与 2026-11-06 预留一致）；DB=#111 留给转债经手费，**本轮不写 DB**；选题自 `事实与坑` 2026-11-06「场内基金过户费不是股票 0.01‰；二级成交 ≠ 申赎篮子过户」与清单预留段；**新建实验 DA**  
状态：**预检有条件通过 · 三条已冻 · 待复检**（结论栏空；禁止把「场内基金/ETF 二级腿抽股票过户费 0.01‰」或「申赎篮子面值过户当成二级成交过户」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**禁止标任何纸面齐**；**未标纸面齐**；**禁止标 A/D–DA 纸面齐**；**不改已冻 A–CZ**；尤其不改假设-U / 假设-AX / 假设-CM / 假设-A / 假设-D / 假设-S / 假设-CZ）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 DA（#110）。一句话误开：回测对场内基金/ETF 二级腿误抽股票过户费 0.01‰，或把申赎篮子成分股面值过户费当成二级成交过户，系统性改写基金腿成本。

> **字母消歧（硬）**：本页**实验字母 DA** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DA**；**勿把 `params.Y` 读成实验字母 DA**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**这个 0.01 不是过户费 0.01‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，过户费 0.01‰ 是费率；**params.G ≠ 实验字母 DA**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DA**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DA ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DA ≠ 单字母假设-A；严禁复用假设-A**）≠ **单字母实验 U**（股票过户费切日；**双字母 DA ≠ 单字母假设-U；严禁复用假设-U**）≠ 双字母 **AX**（基金经手费）≠ **CM**（ETF 申赎可成交）≠ **CZ**（存托凭证可成交）≠ **S**（股票经手费）≠ **CY**（优先股可成交；本页不引用其主键）。**DA≠U≠AX≠CM≠A≠D≠CZ≠CY**。**params.Y/G/N ≠ 实验字母 DA；亦 ≠ 单字母 D/A/U**。**勿把 `params.Y` 读成实验字母 DA，亦勿把单字母假设-D / 假设-A / 假设-U 读成双字母 DA**。

### 专节 · 双字母 DA ≠ 单字母假设-D / 假设-A / 假设-U；且 ≠ 假设-AX / 假设-CM / 假设-A / 假设-CZ / 假设-S（硬）

| 维度 | 对照页 | 本页假设-DA（双字母） |
|------|--------|----------------------|
| 题面 U | **股票过户费切日**（2015-08-01 起 0.02‰、2022-04-29 起 0.01‰ 双边；ETF 另表当时 skip） | 股票切日留在 U。本页不改切日，也不用股票 0.01‰ 填 U 的 ETF skip。**双字母 DA ≠ 单字母假设-U**；**严禁复用假设-U**；**DA≠U**；**不改 U**；不把「股票过户费已诚实」写成「场内基金过户费已诚实」 |
| 题面 AX | **基金/ETF 经手费**（基金竞价档；货币债基暂免） | 经手费是交易所，过户费是中国结算。**DA≠AX**；**不改 AX**；不把「基金经手费已诚实」写成「过户费已诚实」；`fund_brokerage_handoff=ax_page` |
| 题面 CM | **ETF 申赎可成交**（申购/赎回腿能否按净值或现金替代成交） | 申赎能否成交 ≠ 申赎篮子过户费。篮子过户按成分面值另计，与二级分列。**DA≠CM**；**不改 CM**；不把「ETF 申赎可成交已诚实」写成「篮子过户费已诚实」；`etf_cr_fill_handoff=cm_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 基金腿过户费。**双字母 DA ≠ 单字母假设-A**；**严禁复用假设-A**；**不抢 A 真数队列**；**DA≠A**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交、停牌能否成交 ≠ 过户费抽在哪一档。**双字母 DA ≠ 单字母假设-D**；**严禁复用假设-D**；**DA≠D**；**不改 D** |
| 题面 CZ | **存托凭证可成交性误开**（CZ 页；三条已冻 · 待复检） | 可成交误开 ≠ 过户费误套。**DA≠CZ**；**不改 CZ**；不把「存托凭证可成交已诚实」写成「基金过户费已诚实」 |
| 题面 S | **股票经手费现行档** | A 股经手费三切日 ≠ 中国结算过户费。**DA≠S**；**不改 S**；不把经手费档写成过户费依据 |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_etf_transfer_fee_as_stock_tier`（**写死冻结**单一主报；禁与 `invent_asof_leak_etf_transfer_fee` 双挂；DA1 不升格；篮子错捆只作诊断桶，不升格主报） |
| 文档 | 清单实验 U / AX / CM / A / D / CZ / S（**只读；禁止改写**） | `假设-DA-场内基金过户费误套股票.md`（新建） |
| 预检键 | 实验字母 U / AX / CM / A / D / CZ / S / Y / G / N | 实验字母 **DA** / `da0_primary_demo`；**不得**占用或改写预检 U/AX/CM/A/D/CZ/S |

**禁止**：把 DA 写成「U / AX / CM / A / D / S / CZ 的续篇」；把「股票过户已诚实（U）/ 基金经手费已诚实（AX）/ ETF 申赎可成交已诚实（CM）/ 板上已诚实（A）/ 成交时点已诚实（D）/ 股票经手费已诚实（S）」写成「场内基金过户费已诚实」；把实验字母 DA 与单字母 D/A/U 或 params.Y/G/N 混读；**尤重勿把单字母假设-U / 假设-D / 假设-A 读成双字母 DA**；**尤重勿把 `params.Y` 读成实验字母 DA**；**尤重 `params.G` 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同）**。本页主键只用 `da0` / `da1` / `da2` 与 `etf_transfer_fee_*`。

---

## 1. 一句话假设（可检验、可证伪）

同一基金/ETF 信号、同一未复权成交金额、同一 T+1、同一经手费（AX）切片下，回测对场内基金/ETF 二级腿误抽股票过户费 0.01‰，或把申赎篮子成分股面值过户费当成二级成交过户，相对「二级不套股票档（缺官方二级‰则 skip，禁静默 0.01‰）；申赎腿按面值篮子规则与二级分列」的诚实组，会**系统性改写基金腿成本**——二级误抽发明收费、偏悲观；篮子与二级捆错会把申赎冲击算进买卖。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、二级误抽截、篮子错捆截在标定噪声带内可忽略，且「二级误套股票档 / 核对日泄露 / 篮子面值费按成交金额抽 / vs U·AX·CM·A·D·S·CZ」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · da0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过 · 三条已冻 · 待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DA ≠ 单字母假设-D ≠ 单字母假设-A ≠ 单字母假设-U**；勿把 params.Y 读成实验字母 DA
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**这个 0.01 不是股票过户费 0.01‰**（量纲与语义不同：无量纲相对门槛 ≠ 费率‰）；**≠ 实验字母 DA ≠ 单字母 D/A/U**
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DA ≠ 单字母 D/A/U**
# params.Y2 写死冻结 0.015
# params.Y / G / N / Y2               写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 二级误抽截 ΔFakeStockTier / 篮子错捆截 ΔBasketParAsSecondary / 净收益差 / DA1−DA2；**params.Y/G/N ≠ 实验字母 DA ≠ 单字母假设-D / 假设-A / 假设-U**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰**；禁 null；禁 holdout/OOS 标定；勿改已冻他字母数值）
# params.fill_time                    写死冻结 next_open
# params.asof_check_date              写死冻结 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  写死冻结 skip
# params.etf_transfer_fee_honest      写死冻结 pit_secondary_not_stock_tier
#   二级不套股票档；缺官方二级‰则 skip；禁静默 0.01‰
# params.etf_transfer_fee_scope       写死冻结 secondary_skip_and_basket_par_listed_apart
#   申赎腿按面值篮子规则，与二级分列；不得把篮子费写进二级成交金额
# params.etf_transfer_fee_over_policy 写死冻结 skip_if_official_secondary_bps_missing
# params.etf_secondary_official_bps   建议 missing→skip
#   核对日两所结算表没有「ETF/封闭式/LOF 二级成交按成交金额 0.01‰」这一栏；不发明沪市或深市二级精确‰
# params.etf_cr_basket_basis          建议 par_value
#   申赎篮子过户基数是成分股票面值，不是二级成交金额；债券成分免收（对照事实与坑 2026-11-06，建议占位，尚未冻）
# params.etf_cr_basket_stock_par_bps  建议 0.5
#   单位 ‰，只用于申赎腿；成立后暂减半见下一键；沪市只收所含沪市成分。禁止套进二级
# params.etf_cr_basket_stock_par_bps_halved 建议 0.25
# params.stock_transfer_fee_handoff   建议 u_page
#   消费 U 的股票过户 PIT，或显式旁路；不在本页重开 2015-08-01 / 2022-04-29
# params.fund_brokerage_handoff       建议 ax_page
#   消费 AX 的基金经手费诚实档，或显式旁路；过户 ≠ 经手
# params.etf_cr_fill_handoff          建议 cm_page
#   申赎能否成交交 CM；本页只测篮子过户费是否被当成二级成交过户
# params.fee_tier_handoff             建议 s_page
# params.fill_time_suspend_handoff    建议 d_page
# params.board_capacity_handoff       建议 a_page
# params.etf_transfer_fee_handoff     建议 self
# params.da0_primary_demo             写死冻结 invent_etf_transfer_fee_as_stock_tier
#   单一主报；禁与 invent_asof_leak_etf_transfer_fee 双挂；DA1 不升格；篮子错捆只作诊断桶，不升格主报
# params.da0_invent_etf_transfer_fee_as_stock_tier 建议 True
# params.da1_asof_leak_etf_transfer_fee_only 建议 True
#   半泄露对照；DA1 不升格并列主报
# params.da2_pit_etf_transfer_fee     建议 True
# params.merge_with_U                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_CM                建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_S                 建议 False
# params.merge_with_CZ                建议 False
# params.missing_etf_transfer_fee_policy 建议 skip
# params.day_freq_proxy               建议 etf_transfer_fee_sensitivity
# params.universe_rule                建议 etf_transfer_fee_mischarge_check
# params.redline_v0_exempt_scope      建议 position_industry_dd_only
```

### 2.2 三组对照（DA0 / DA1 / DA2）

| 组 | 角色 | 口径 |
|----|------|------|
| DA0 | 天真 / 误套股票档 | 按 `da0_primary_demo` **写死冻结**单一主报 `invent_etf_transfer_fee_as_stock_tier`：场内基金/ETF 二级腿按股票过户费 0.01‰ 抽（**禁**与 `invent_asof_leak_etf_transfer_fee` 双挂主报） |
| DA1 | 半泄露 | 仅核对日「用股票 0.01‰ 填二级」或核对日博客费率铺满全历史；**不得升格并列主报**（写死冻结：DA1 不升格） |
| DA2 | 诚实 / PIT | `etf_transfer_fee_honest=pit_secondary_not_stock_tier`（写死冻结）：二级不套股票档，缺官方二级‰则 skip，禁静默 0.01‰；申赎腿按面值篮子规则与二级分列。股票过户 PIT 只消费 U，基金经手费只消费 AX，或显式旁路 |

篮子错捆（把成分股票面值 0.5‰ / 成立后暂减半按二级成交金额抽）放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `da0_primary_demo`。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，不在本草稿写死起止日。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。收费表引用见 `事实与坑` 2026-11-06（中国结算 2026-01-01 更新表）：该日期是表的版本，不是 `asof_check_date`。本页**不开回测**；不拉真数；不做实盘。

### 3.1 oos_split（建议四日期；拉数前冻结；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DA0）/ 半泄露组（DA1）相对诚实组（DA2）的成本差、二级误抽截、篮子错捆截**显著且集中在场内基金过户费误套桶**；分桶「二级误套股票档 / 核对日泄露 / 篮子面值费按成交金额抽 / vs U·AX·CM·A·D·S·CZ」不改变主结论方向。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 U 的股票切日、AX 的基金经手费、CM 的申赎能否成交、S 的股票经手费、A 的板上容量解释；或 `da0_primary_demo` 与 `invent_asof_leak_etf_transfer_fee` 双挂；或 DA1 升格并列主报；或篮子错捆桶升格主报；或实验字母 DA 与单字母 D/A/U 或 params.Y/G/N 混读；或把 `params.G=0.01` 读成过户费 0.01‰。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额、同一 T+1，对照 DA0/DA1/DA2。经手费走 AX 的诚实档或显式旁路，不在本页重开基金经手费切日。报告成本差、二级误抽截、篮子错捆截。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前冻结；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_etf_transfer_fee_as_stock_tier` / `invent_asof_leak_etf_transfer_fee` / `basket_par_fee_as_secondary_notional` / `vs_U_stock_transfer_fee` / `vs_AX_fund_brokerage` / `vs_CM_etf_cr_fill` / `vs_A_board_capacity` / `vs_D_fill_time` / `vs_S_fee_tier` / `vs_CZ_fill`

`basket_par_fee_as_secondary_notional` 只作诊断桶：二级不抽股票档，但把申赎篮子面值费按成交金额抽。它不是 `da0`，也不是 DA1，**不得升格主报**。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 缺官方场内基金二级过户费‰，却静默填股票 0.01‰。
- 把申赎篮子「按成分股票面值 0.5‰、成立后暂减半」写成二级成交过户。
- 用博客「沪市 ETF 收过户、深市免」填官方二级‰。
- 把「股票过户已诚实（U）/ 基金经手费已诚实（AX）/ ETF 申赎可成交已诚实（CM）」写成「场内基金过户费已诚实」。
- `da0_primary_demo` 与 `invent_asof_leak_etf_transfer_fee` 双挂主报；DA1 升格并列主报；篮子错捆桶升格主报。
- 实验字母 DA 与单字母 D/A/U 或 params.Y/G/N 混读；把 `params.G=0.01` 当成过户费 0.01‰。
- 改 U 的股票切日；改 AX / CM / A / D / S / CZ 正文；抢 A 真数队列；标纸面齐；开真数/回测/实盘；本轮顺手写 DB。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、证券类别（股票 / 场内基金或 ETF 二级 / ETF 申赎篮子）、交易所、未复权成交金额。
- 申赎腿另需：成分股票面值、是否成立后、成分属于沪市还是深市。二级腿没有这些字段时，不得用篮子规则填二级。
- 官方二级过户费‰：缺则 skip，禁止用 0.01‰ 补齐。
- 旁路消费：U 股票过户 PIT、AX 基金经手费、CM 申赎可成交、A 板上、D 成交时点、S 股票经手费、CZ 可成交约束的诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。**
- 未复权价；asof **写死冻结** `2026-10-16`。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`etf_transfer_fee_honest=pit_secondary_not_stock_tier`；`etf_transfer_fee_scope=secondary_skip_and_basket_par_listed_apart`；`etf_transfer_fee_over_policy=skip_if_official_secondary_bps_missing`；`da0_primary_demo=invent_etf_transfer_fee_as_stock_tier`（**写死冻结**单一主报；禁与 `invent_asof_leak_etf_transfer_fee` 双挂；DA1 不升格；篮子错捆只作诊断桶）；`stock_transfer_fee_handoff=u_page`；`fund_brokerage_handoff=ax_page`；`etf_cr_fill_handoff=cm_page`；`merge_with_U/AX/CM/A/D/S/CZ=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 二级误抽截 ΔFakeStockTier / 篮子错捆截 ΔBasketParAsSecondary / 净收益差 / DA1−DA2；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DA ≠ 单字母 D/A/U**；**勿把 params.Y 读成实验字母 DA，亦勿把单字母假设-D / 假设-A / 假设-U 读成双字母 DA**；禁 null；禁 holdout/OOS 标定；勿改已冻他字母数值）。
- oos_split 四日期建议占位；禁 holdout 反调。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。草稿行基 tip=`0b73994`；三冻补丁基 tip=`2454f5d`。

---

## 8. 结论

（空；预检有条件通过 · 三条已冻 · 待复检；复检通过前不得标纸面齐；本页作者不得标 A/D–DA 纸面齐。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-09）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DA-20261109.md`（原样落入，不改结论；SHA256=`01f40aeccecfa558b5fd0d1c2f368fad20b4238d17349852f479118a5d9d913e`；预检 2026-11-09；**结论：有条件通过**；tip基=`2454f5d` / `2454f5d2802e137fc02a6abc4a18cb1174f14a28`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、二级误抽截 ΔFakeStockTier、篮子错捆截 ΔBasketParAsSecondary、净收益差、DA1−DA2 专项。**`params.Y` ≠ 实验字母 DA**；**`params.G` ≠ 实验字母 DA**；**`params.N` ≠ 实验字母 DA**；亦 ≠ 单字母假设-D / 假设-A / 假设-U。**勿把 `params.Y` 读成实验字母 DA，亦勿把单字母假设-D / 假设-A / 假设-U 读成双字母 DA**。**尤重：`params.G` 的 `0.01` ≠ 过户费 `0.01‰`**。二者量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，过户费 `0.01‰` 是费率，禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.da0_primary_demo`**：**写死冻结** **`invent_etf_transfer_fee_as_stock_tier`**（单一主报）。**禁止**与 **`invent_asof_leak_etf_transfer_fee`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DA1 核对日「用股票 0.01‰ 填二级」或核对日博客费率只作半泄露对照，**不得升格与 da0 并列主报**。篮子错捆（`basket_par_fee_as_secondary_notional`：把申赎篮子面值费按二级成交金额抽）**只作诊断桶，不得升格主报**。

3. **场内基金过户费诚实锚六键升格写死（不可再写「建议」；键名前缀按本页既有 `etf_transfer_fee_*`，对照 CZ 的 `cdr_fill_*`）**：`params.etf_transfer_fee_honest=pit_secondary_not_stock_tier`；`params.etf_transfer_fee_scope=secondary_skip_and_basket_par_listed_apart`；`params.etf_transfer_fee_over_policy=skip_if_official_secondary_bps_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。禁止跑后改锚，或用股票过户费 0.01‰ / 核对日博客费率冒充诚实 PIT。

**硬分列保住**：DA≠U≠AX≠CM≠A≠D≠CZ≠CY≠S；**双字母 DA ≠ 单字母假设-D / 假设-A / 假设-U**；**params.Y / params.G / params.N ≠ 实验字母 DA**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰**；不抢 A；不改已冻 A–CZ 正文。

**状态**：预检有条件通过 · 三条已冻 · 待复检；**禁止标任何纸面齐**；**未标 A/D–DA 纸面齐**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 风控预检补丁·冻结三条写死——依据 `预检-假设DA-20261109.md`（SHA256=`01f40aeccecfa558b5fd0d1c2f368fad20b4238d17349852f479118a5d9d913e`；结论=有条件通过；tip基=`2454f5d` / `2454f5d2802e137fc02a6abc4a18cb1174f14a28`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔFakeStockTier / ΔBasketParAsSecondary / 净收益差 / DA1−DA2；**params.Y/G/N ≠ 实验字母 DA ≠ 单字母假设-D / 假设-A / 假设-U**；**勿把 params.Y 读成实验字母 DA，亦勿把单字母假设-D / 假设-A / 假设-U 读成双字母 DA**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰（量纲与语义不同）**；禁 null；禁 holdout/OOS 标定）；② `params.da0_primary_demo=invent_etf_transfer_fee_as_stock_tier`（写死冻结单一主报；禁与 `invent_asof_leak_etf_transfer_fee` 双挂；DA1 不升格；篮子错捆只作诊断桶，不升格主报）；③ 锚六键写死 `etf_transfer_fee_honest=pit_secondary_not_stock_tier` / `etf_transfer_fee_scope=secondary_skip_and_basket_par_listed_apart` / `etf_transfer_fee_over_policy=skip_if_official_secondary_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标 A/D–DA 纸面齐**；不改已冻 A–CZ；不开回测/真数/实盘。基于 tip=`2454f5d`。 |
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；场内基金过户费误套股票；`da0_primary_demo` 建议 `invent_etf_transfer_fee_as_stock_tier`，单一主报，禁与 `invent_asof_leak_etf_transfer_fee` 双挂，DA1 不升格；Y/G/N/Y2 建议占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DA ≠ 单字母 D/A/U**，且 params.G 的 0.01 不是过户费 0.01‰；锚建议 `etf_transfer_fee_honest=pit_secondary_not_stock_tier` / scope=`secondary_skip_and_basket_par_listed_apart` / over_policy=`skip_if_official_secondary_bps_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；handoff：`stock_transfer_fee_handoff=u_page`，`fund_brokerage_handoff=ax_page`，`etf_cr_fill_handoff=cm_page`；`merge_with_U/AX/CM/A/D/S/CZ=False`；**DA≠U≠AX≠CM≠A≠D≠CZ≠CY**；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；不改已冻 A–CZ；不写 DB；不开真数/回测/实盘）。基 tip=`0b73994`（本次提交前 HEAD `0b739940d717f50fdea9de77f8e7bf0b4e8daf13`） |
