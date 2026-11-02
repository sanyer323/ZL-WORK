# 假设 AB · 融券卖出价限 / 禁市价 / 禁当日平（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AA 补丁已交后并行写下一纸面 AB；清单原止于 AA，无 AB 节 → 自立实验 AB；选题自总管候选旁路「执行缺口」+ `事实与坑` 2026-10-16「融券卖出不是最新价就能砸：有价格限制，也不能市价，也不能当天开当天平」+ 口径「拥挤着做空 = 没有券 / 低于最新价废单」；与假设 K（名单 PIT）/ L（市价通道）/ Z（保证金比例）**分列**；**新建实验 AB**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「可按任意低于最新价砸 / 融券可市价 / 当日开空当日平 / ETF 融券免价限已实施」当诚实空头执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA 及其他 A/D–AA 已交正文与冻结补丁**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AA，本页自立实验 AB 标准件。与假设 K（融券空头名单 PIT）**分列**：K 主测「当时可空名单」；本页**主测**名单内空头腿的**卖出价格下限、禁市价、禁当日平**，以及 ETF「免价限」条文**暂不实施**被误写成已开。与假设 L（市价通道）**分列**：L 主测多头/一般市价；本页专测**融券腿**误用市价。与假设 Z（保证金比例）**分列**：Z 主测杠杆占用；本页不重开保证金档。**转融券暂停/券源属 K 旁路；板上可成交属 A。本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AB** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AB / 假设-AB / hypothesis_id=AB / 组 AB0·AB1·AB2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AB 与 params 键名 `ab0_*` 以外的单字母/双字母实验页混读。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1、同一未复权价、同一融券名单（K 层诚实输入）下，把融券卖出当成「可按任意低于最新成交价（无成交则前收盘）的限价砸、可走市价、或当日开空当日平」，或把「ETF 等可不受价限」按细则正文写成已实施，相对「卖出价 ≥ 最新成交价（无成交 ≥ 前收盘）、禁市价、自次一交易日起才可还券、ETF 免价限暂不实施」的 PIT 诚实组，会**系统性高估空头可成交路径与日内对冲能力**；差异应**集中在「价限废单 / 融券市价废单 / 当日平失败 / ETF 误免价限」桶**，而不是随机散开。

证伪方向：若天真组 / 泄露组相对诚实组的空头失败率差、可平仓路径差、空头腿净值差在标定噪声带内可忽略，且「价限废单 / 市价废单 / 当日平 / ETF 误免 / 对照诚实价限」分桶不改变结论（差异不集中在价限·当日平相关桶），则本假设在该样本与空头执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融券卖出价限 ≠ 名单；≠ 市价通道；≠ 保证金；ETF 免价限暂不实施

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AB
# params.asof_check_date                 写死默认 2026-10-16  # 与 K/Z 同批「融券/保证金」核对锚；本页不重开名单/保证金
# params.fill_time                        写死 next_open      # 成交腿与 A/D/K 对齐；本页主测空头价限，不抢 A 板上真数
# params.short_channel_start             写死 2010-03-31     # 融资融券通道起点；此前不可空 → skip 空头腿
# params.short_price_floor_rule          写死 last_trade_else_preclose  # ≥最新成交；无成交 ≥前收盘
# params.short_mkt_allowed               写死 False          # 两所均不接受融券卖出市价
# params.short_same_day_cover            写死 forbid         # 自次一交易日起才可还券；禁当日开空当日平
# params.etf_short_price_exempt          写死 off            # 细则有免价限款，通知写明继续暂不实施
# params.ab0_primary_demo                写死 below_last_as_fill  # 风控补丁冻结；主报忽略价限按任意低于最新价可砸；禁与 same_day_cover 双挂
# params.ab0_ignore_price_floor          写死 True           # 天真主路径：忽略价限
# params.ab0_allow_short_mkt             写死 True           # 天真可叠加：融券走市价（诊断可拆）
# params.ab0_same_day_cover              写死 True           # 天真可叠加：当日开空当日平
# params.ab1_etf_exempt_as_on            写死 True           # 半泄露/诊断：ETF 免价限当已实施
# params.ab2_price_floor                 写死 last_trade_else_preclose
# params.ab2_short_mkt_allowed           写死 False
# params.ab2_same_day_cover              写死 forbid
# params.ab2_etf_short_price_exempt      写死 off
# params.merge_with_K_shortable_list     写死 False          # 名单另页 K；默认输入 K2 诚实名单或 long_only
# params.merge_with_L_mkt                写死 False          # 一般市价通道另页 L
# params.merge_with_Z_margin             写死 False          # 保证金比例另页 Z
# params.merge_with_A_fill               写死 False
# params.merge_with_Q_cb                 写死 False
# params.list_overlay                    写死 k2_honest_or_long_only
# params.missing_last_trade_policy       写死 use_preclose    # 无最新成交 → 价限退回前收盘（与条文同向）
# params.px_basis                        写死 unadj          # 价限用不复权；禁复权价
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AB；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-16"
short_channel_start = "2010-03-31"
short_price_floor_rule = "last_trade_else_preclose"
short_mkt_allowed = False
short_same_day_cover = "forbid"
etf_short_price_exempt = "off"
merge_with_K_shortable_list = False
merge_with_L_mkt = False
merge_with_Z_margin = False
merge_with_A_fill = False
merge_with_Q_cb = False
list_overlay = "k2_honest_or_long_only"
missing_last_trade_policy = "use_preclose"
px_basis = "unadj"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 ab0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AB
G = 0.01
N = 0.05
Y2 = 0.015
ab0_primary_demo = "below_last_as_fill"  # 风控补丁冻结；禁双挂

def short_price_ok(order_px, last_trade, preclose, group, is_etf):
    """融券卖出价限：诚实组 order_px >= last_trade（无成交则 >= preclose）。"""
    if group == "AB0":
        return True  # 天真：忽略价限（或按 ab0_primary_demo 单一主报）
    floor = last_trade if last_trade is not None else preclose
    if group == "AB1" and is_etf and etf_short_price_exempt == "on_wrong":
        return True  # 误把 ETF 免价限当已实施
    # AB2 PIT；etf_short_price_exempt=off → ETF 同样受价限
    return order_px >= floor

def short_mkt_ok(group):
    if group == "AB0":
        return True  # 天真允许（诊断）
    return False     # AB1/AB2：禁融券市价

def short_cover_ok(open_date, cover_date, group):
    if group == "AB0":
        return True  # 天真：当日可平
    return cover_date > open_date  # AB2：次日起
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：无最新成交且无前收盘却硬标价限通过、把 K 名单 / L 市价 / Z 保证金 / A 板上混进本页主表、用复权价判价限、把 ETF 免价限当 AB2 诚实 → **跳过该日该券空头执行腿**，不静默记成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AB）

| 组 | 价限 / 市价 / 当日平 | 说明 |
|----|----------------------|------|
| AB0 天真 | 忽略价限（+可市价/+当日平，按 `ab0_primary_demo` 单一主报） | 把空头当美股式可砸可平 |
| AB1 半泄露 | 价限名义上开，但 ETF 免价限当已实施 | 细则正文误落地 |
| AB2 PIT 诚实 | ≥最新/前收盘；禁市价；禁当日平；ETF 免价限=off | 与事实与坑同向 |

同一信号、同一 T+1、同一股票宇宙。本页**主测空头执行价限/当日平**，不主测名单（见 K）、不主测一般市价（见 L）、不主测保证金档（见 Z）。**`params.fill_time=next_open` 写死**。名单默认叠加 **K2 诚实** 为对照声明，**`merge_with_K_shortable_list=False`**。

**`params.merge_with_K_shortable_list=False` / `merge_with_L_mkt=False` / `merge_with_Z_margin=False` / `merge_with_A_fill=False` / `merge_with_Q_cb=False`（写死）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                 # 空头失败/净值差显著门槛；≠实验字母 AB
params.G                            = 0.01                 # 价限废单桶相对对照差
params.N                            = 0.05                 # 失败/跳过率差门槛
params.Y2                           = 0.015                # AB1（ETF 误免）相对 AB2 专项门槛
params.ab0_primary_demo             = below_last_as_fill   # 主报忽略价限按任意低于最新价可砸；禁与 same_day_cover 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股可进融券通道的股票为主；ETF 进「误免价限」诊断桶，不改主结论股票腿。不含可转债主样本（见 Q）。  
- **排除（默认）**：`trade_date < 2010-03-31`；无诚实名单且 `list_overlay` 要求空头 → skip；用复权价；把 K/L/Z/A 主结论并进本页主表。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - **覆盖转融券暂停 2024-07-11 前后**（券源另页 K；本页只作分桶对照声明，不重开券源主测）。  
- **PIT 切片原则**：价限、禁市价、禁当日平按当时已生效细则；**ETF 免价限以「暂不实施」通知为准**，禁止按细则正文回放为已开。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2023-12-31
params.oos_split.holdout_start  = 2024-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调价限枚举、`ab0_primary_demo`、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AB0 ? AB2**：忽略价限/可市价/当日平 相对 PIT——空头假成交与日内假对冲。  
2. **AB1 ? AB2**：ETF 免价限误开 相对 PIT——ETF 空头腿假砸。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "price_floor_reject",         # 低于最新/前收盘被拒
  "short_mkt_reject",           # 融券市价废单
  "same_day_cover_fail",        # 当日开空当日平失败
  "etf_exempt_false_on",        # ETF 免价限误实施
  "no_trade_use_preclose",      # 无成交退回前收盘
  "vs_K_list",                  # 对照声明：名单另页 K
  "vs_L_mkt",                   # 对照声明：一般市价另页 L
  "vs_Z_margin",                # 对照声明：保证金另页 Z
  "vs_A_fill",                  # 对照声明：板上可成交另页 A
  "post_refinance_pause",       # 对照声明：2024-07-11 后券源另页 K
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 空头失败率差 ΔShortFail（AB0/AB1 相对 AB2）；  
2. 可平仓路径差 ΔCoverPath（当日平被吹胖的那截）；  
3. 空头腿净值差 ΔShortPnL；  
4. 跳过/废单笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔShortFail| 或 |ΔShortPnL| **≥ params.Y** 或 |ΔCoverPath| **≥ params.G** 或 |ΔShortFail_(AB1−AB2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「融券价限/当日平执行鸿沟显著」。

**params.Y / G / N / Y2（键名稳；值已冻结 2026-11-02；禁 holdout 标定；与实验字母 AB 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 空头失败/净值差显著门槛（≠实验字母 AB） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 价限废单/当日平路径桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败笔数率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AB1 ETF 误免专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-16`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| short_price_floor_rule | 诚实价限 | **写死** `last_trade_else_preclose` |
| short_mkt_allowed | 融券市价 | **写死** `False` |
| short_same_day_cover | 当日平 | **写死** `forbid` |
| etf_short_price_exempt | ETF 免价限 | **写死** `off` |
| ab0_primary_demo | 天真主报枚举 | **写死冻结** `below_last_as_fill`（风控补丁 2026-11-02；禁双挂） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已写入 params 并冻结（风控补丁 2026-11-02；**`params.Y`≠实验字母 AB**）；**禁止用 holdout / 事后显著性改口**；**`ab0_primary_demo=below_last_as_fill` 单一主报，禁与 same_day_cover 双挂争主表**。

**失败/不显著**：差异落在噪声带内或均匀散在非价限·当日平对照桶——结论栏写明，不得改口称「空头差不多能砸」或「这类票更能空」。

结论栏：空。跑完只写「该假设下空头失败/路径差多少」，不写选股/做空公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验空头执行诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（PIT 价限/禁市价/禁当日平、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价判价限**。  
2. **把 K 名单、L 市价、Z 保证金、A 板上重开混进本页主结论**。  
3. **把 ETF 免价限按细则正文写成 AB2 诚实已实施**。  
4. **把当日开空当日平写成 AB2 合法**。  
5. **无最新成交却不用前收盘、静默放行任意低价**。  
6. **宇宙泄露 / holdout 反调**：看完 OOS 再改 `ab0_primary_demo` 或 **`params.Y` 等门槛**。  
7. **差异不集中在价限·当日平桶却仍写「系统性空头执行鸿沟」而不改表述**。  
8. **把差异写成「这类票能空」或选股/做空公式**。  
9. **把实验字母 AB 与 `params.Y` 混改**；或改写 Y/Z/AA 及其他 A/D–AA 已冻正文。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股为主 |
| unadj_last_trade / unadj_preclose | 价限基准 | 禁复权 |
| short_order_px（未复权） | 申报价 | 诊断用 |
| is_market_order | 市价标记 | 融券腿须 False |
| short_open_date, short_cover_date | 当日平检验 | |
| is_etf | ETF 误免桶 | |
| shortable_flag（可选，K2） | 名单叠加 | 缺 → skip 或 long_only |
| exchange (SSE/SZSE) | 分桶 | 北交所默认另桶 |

**明确**：不依赖聚宽；**不要求新开 Level-2 全档**——有未复权最新价/前收盘 + 开平仓日即可起步；缺价限字段 → `fail_policy=skip`。主窗自 2019-01-01。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=AB`（**实验字母**），`groups=[AB0,AB1,AB2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-16`**，**`params.fill_time=next_open`（写死）**，**`params.short_channel_start=2010-03-31`**，**`params.short_price_floor_rule=last_trade_else_preclose`**，**`params.short_mkt_allowed=False`**，**`params.short_same_day_cover=forbid`**，**`params.etf_short_price_exempt=off`**，**`params.merge_with_K_shortable_list=False`**，**`params.merge_with_L_mkt=False`**，**`params.merge_with_Z_margin=False`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_Q_cb=False`**，**`params.list_overlay=k2_honest_or_long_only`**，**`params.missing_last_trade_policy=use_preclose`**，**`params.px_basis=unadj`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015`（写死冻结；禁 holdout 标定；禁 null；params.Y≠实验字母 AB）**，**`params.ab0_primary_demo=below_last_as_fill`（写死冻结；禁双挂）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2023-12-31,holdout_start=2024-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_K=off`，`overlay_L=off`，`overlay_Z=off`，`overlay_A=off`。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AB0/AB1/AB2 空头失败率、ΔShortFail、ΔCoverPath、ΔShortPnL、失败笔数；分桶（价限废单 / 市价废单 / 当日平 / ETF 误免 / vs K·L·Z·A）。  
- 自检布尔：AB2 是否价限+禁市价+禁当日平+ETF 免=off；AB0 是否单一主报；AB1 是否仅 ETF 误免；是否未与 K/L/Z/A 混主结论；holdout 是否未反调；**是否未把实验字母 AB 与 params.Y 混用**；**是否未改 Y/Z/AA 冻结补丁正文**。  
- **禁止输出**：具体买卖/做空标的列表当「建议」；把忽略价限当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA 及其他 A/D–AA 已交正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：融券卖出不得低于最新成交价（无成交则前收盘）；不接受融券市价；自次一交易日起才可还券；ETF 免价限继续暂不实施。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AA，本页**新增实验 AB** 收成标准件，**不改口径主线**，**不改假设 A–AA 正文**。与实验 K/L/Z 分工：**K=名单可空；L=一般市价通道；Z=保证金比例；AB=名单内空头的价限 / 禁市价 / 禁当日平 / ETF 免价限未实施**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；未复权最新价/前收盘 + 开平仓日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**short_price_floor_rule / short_mkt_allowed=False / short_same_day_cover=forbid / etf_short_price_exempt=off 写死**；diff_buckets 十桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死冻结**（params.Y≠实验字母 AB）；**ab0_primary_demo=below_last_as_fill 写死（禁双挂）** |

---

## 变更

- 2026-11-02：新建标准件（总管线：并行写下一纸面 AB；Y/Z/AA 补丁已交不改；清单止于 AA → 自 `事实与坑`「融券卖出不是最新价就能砸」+ 口径「低于最新价废单」选题，**与 A/D–AA 不撞主结论**；近邻 K=名单、L=市价、Z=保证金，本页主测价限/禁市价/禁当日平；**实验字母 AB ≠ params.Y**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA/A/D–X 正文**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AB-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写入具体数并冻结（预检禁 holdout 标定且建议 0.02/0.01/0.05/0.015；**params.Y≠实验字母 AB**；禁 null）；② `params.ab0_primary_demo=below_last_as_fill`（主报忽略价限按任意低于最新价可砸；禁与 same_day_cover 双挂争主表）。**不抢实验 A**；**AB 不开回测**；未动 Y/Z/AA/A。

### 增量补丁段 · 2026-11-02（风控两条冻结）

| 键 | 冻结值 | 备注 |
|----|--------|------|
| params.Y | 0.02 | 相对门槛键；**≠实验字母 AB** |
| params.G | 0.01 | 价限废单/当日平路径桶相对对照差 |
| params.N | 0.05 | 失败/跳过率差 |
| params.Y2 | 0.015 | AB1−AB2 专项 |
| params.ab0_primary_demo | below_last_as_fill | 单一主报；禁与 same_day_cover 双挂 |

预检稿：`experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AB-20261102.md`。
