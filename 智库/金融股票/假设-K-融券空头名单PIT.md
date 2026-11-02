# 假设 K · 默认多空对称 / 用今天的融券名单（空头名单 PIT）

更新：2026-11-02（风控补丁）  
来源：总管线 / I 补丁已交·J 已落盘后下一可离线纸面；清单实验 K  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「全 A 可空 / 今天的名单回放十年」当实盘预期；不抢实验 A 真数队列）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 K 对齐。与假设 C（股票池 PIT 幸存者）互补：本页专测**融券标的当时名单**被当成「全市场可空」或「核对日名单铺满历史」时，对空头腿可成交性与贡献收益的扭曲。**不主测市价通道（见 L）、不主测保证金杠杆切片（可另案）、不把名单写成一定借得到。**

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1（空头侧次日才还券）下，把「全 A 任意日任意量可空」或「全样本用核对日当天融券名单」当成空头可成交路径，相对「每个调仓日只用当日已生效名单（施行日对齐；ST/终止上市当日调出；2010-03-31 前不可空）」的 PIT 诚实组，**空头失败笔数与被今天名单事后借到的历史空头贡献收益会显著升高**；再叠加「2024-07-11 后转融券暂停、券源不保证」加严档，空头可成交量/失败率会进一步拉开。

证伪方向：若天真组 / 泄露组相对诚实组的空头失败差、名单外历史空头贡献差、多空净值差在标定噪声带内可忽略，且「施行日 vs 印发日」分桶不改变结论，则本假设在该样本与撮合设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融券标的当时名单（按调仓日已生效；未复权价仅用于价格限制自检，不主测）

```
# 配置写死（见 §7）
# params.asof_check_date              写死默认 2026-10-16  # 事实与坑融券核对日；泄露组「今天名单」锚点
# params.shortable_channel_start      写死默认 2010-03-31  # 此前不可空
# params.refinance_pause_start        写死默认 2024-07-11  # 转融券暂停起；≠标的消失
# params.refinance_stock_deadline     写死默认 2024-09-30  # 存量了结上限（事实窗）
# params.list_date_mode               写死默认 effective_date  # 禁 publish_date
# params.st_remove_same_day           写死默认 True
# params.delist_proc_remove_same_day  写死默认 True
# params.reg_ipo_shortable_day1       写死默认 True   # 仅注册制 IPO；禁铺到核准制主板新股
# params.approval_ipo_min_listed_days 写死默认 90     # 核准制「上市满约3个月」占位；非自动可空
# params.k3_borrow_tighten            写死默认 on     # K3 加严档：暂停后空头量/可得性加严
# params.k3_fill                      写死 skip（单一枚举仅 skip|cap|unchanged；禁 skip_or_cap；本页不用 unchanged；若改 cap 须同写 k3_cap_*）
# params.fill_time                     写死 next_open（不用 next_close；与 A/D 次日开对齐）
# params.list_notice_apply.same_day_order     写死 effective_then_publish_then_id
# params.list_notice_apply.full_replace_mode  写死 replace_then_later_incremental
# params.list_notice_apply.incremental_mode   写死 add_remove_on_current_set
# params.etf_price_exempt             写死默认 off    # 细则免价格限制款暂不实施；禁当已实施
# params.short_same_day_cover         写死默认 forbid # 禁当天开空当天平
# params.Y / G / N / Y2               拉数前写入具体数并冻结；禁 holdout 标定
# 拉数前冻结；禁 holdout / 事后改施行日锚点或名单源 / 禁跑后改 fill_time·k3_fill·list_notice_apply

fill_time = next_open
k3_fill = skip  # skip | cap | unchanged；本页默认 skip；禁 skip_or_cap；本页不用 unchanged
# list_notice_apply（写死；拉数前冻结）
#   same_day_order = effective_then_publish_then_id
#   full_replace_mode = replace_then_later_incremental
#   incremental_mode = add_remove_on_current_set

def is_before_channel(t):
    return t < params.shortable_channel_start

def list_effective_on(t, notices):
    # notices: 每条含 exchange, publish_date, effective_date, add[], remove[], full_replace?
    # 只取 effective_date <= t 的通知，按 same_day_order 排序后依次应用：
    #   full_replace → 覆盖该交易所当前集合；其后同序增量 add/remove 叠加在当前集合上
    #   同日多条：先按 effective_date，再 publish_date，再 notice_id 升序；禁并行合并、禁跑后改合并规则
    # **禁止**用 publish_date 当日当地生效
    ...

def is_shortable_pit(i, t, list_table, meta):
    if is_before_channel(t):
        return False
    if meta.is_st_on(i, t) and params.st_remove_same_day:
        return False
    if meta.in_delist_procedure_on(i, t) and params.delist_proc_remove_same_day:
        return False
    # 注册制 IPO 上市首日可做标的；核准制主板新股不走 day1
    if meta.is_reg_ipo_day1(i, t) and params.reg_ipo_shortable_day1:
        return True
    if meta.is_approval_ipo_within_min_days(i, t, params.approval_ipo_min_listed_days):
        return False  # 须进交易所选取名单，不是自动可空
    return list_table.get((i, t), False)  # 当日已生效名单

def short_open_allowed(i, t, qty, list_table, meta, k3=False):
    if not is_shortable_pit(i, t, list_table, meta):
        return False
    if k3 and t >= params.refinance_pause_start:
        # 名单内 ≠ 一定借得到；加严：券源不保证 → 默认记 fail/部分量（见 fail_policy / k3_fill）
        return "tighten"
    return True
```

- **施行日对齐**：季度定期调整用通知**施行日**（例：上证发〔2026〕101 号自 **2026-10-19** 生效，不要用 10-16 印发日）。不定期调整同理。  
- **通道起点**：`params.shortable_channel_start=2010-03-31`；此前样本**不可发明空头**。  
- **ST / 终止上市**：风险警示**当日**调出；进入终止上市程序自相关公告**当日**调出。  
- **注册制 vs 核准制**：注册制 IPO **上市首日**可做标的；**禁止**把该款铺到核准制主板新股（后者走上市满约 3 个月 + 条件选取）。  
- **转融券暂停**：自 **2024-07-11** 暂停转融券；暂停 ≠ 标的消失，但诚实/加严组**不得**假设名单内任意量可借。  
- **空头 T+1**：融券卖出后自**次一交易日**起才可还券；`short_same_day_cover=forbid`。  
- **价格限制（本页自检、不主测冲击）**：融券卖出不得低于最新成交（无成交则前收盘）；**不接受市价**；ETF 免价格限制款 **`etf_price_exempt=off`**（暂不实施）。精细市价通道见实验 L——**勿混主结论**。  
- **禁止**：用复权价判融券价格限制；把「1000 只」写成永恒数字；把标的名单写成一定借得到；结论写成选股/做空公式。

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺名单表、无法判定施行日、调仓日缺 ST/终止上市旗、或 K3 加严下券源不可得 → **跳过该空头腿**，不成交、不顺延用「全 A 可空」或核对日名单填假可借。  
- 允许拉数前改为 `long_only_fallback`（名单外只做多）或 `defer`，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。  
- **`params.k3_fill`（写死单一枚举；拉数前冻结）**：K3 在 `refinance_pause_start` 后，**必须**落成下列之一并冻结：
  - `skip`：该空头腿失败（跳过）；
  - `cap`：按事先写死的可借量上限成交（须同时写死 `params.k3_cap_rule` 与 `params.k3_cap_value`，禁「任意量」）；
  - `unchanged`：不加严券源（本页**不用**，否则加严档名存实亡）。
  **本页默认写死 `skip`**（对齐 `fail_policy=skip` +「名单≠一定借得到」）。**禁止**保留复合名 `skip_or_cap` 却不定义优先级；**禁止**跑后改口。若改选 `cap`，须拉数前同写 `k3_cap_rule`（如 `frac_prev_day_shortable_balance`）与 `k3_cap_value`（具体数）并冻结。

### 2.3 对照组（本实验编码）

| 组 | 空头可开条件 | 名单时点 | 转融券暂停后 |
|----|--------------|----------|--------------|
| K0 天真-全A可空 | 任意日任意量可空（通道起点可忽略） | 无名单约束 | 仍任意量 |
| K1 泄露-核对日名单 | 须在名单内 | **全样本**用 `asof_check_date` 当天名单 | 仍按泄露名单任意量（不反映暂停） |
| K2 PIT-施行日名单 | 须在当日已生效名单；ST/终止当日调出；2010-03-31 前不可空 | **每个调仓日**用当日已生效 | 名单仍 PIT，但**不**额外加严券源（与 K3 对照） |
| K3 PIT+券源加严 | 同 K2 | 同 K2 | `k3_borrow_tighten=on`：按 `k3_fill=skip` 加严（写死；禁 skip_or_cap） |

同一信号、同一 T+1（多头与空头还券）、同一成本开关（本页可先零成本只比名单处理差）。成交时点 **`fill_time=next_open` 写死**（与假设 A/D 次日开对齐；不用 next_close）。股票池 PIT 见 C；市价见 L；保证金切片可另案——**勿把 C/L/保证金主结论混进 K 主报告**；稳健性叠加须声明。

**成交时点（写死）**：`fill_time=next_open`（与假设 A/D 次日开对齐；**本页不用** `next_close`；若要收盘对照须另开页；拉数前冻结；禁跑后改口）。

**`params.list_notice_apply`（写死；拉数前冻结；禁跑后因净值改合并规则）**：须与「只取 `effective_date≤t` 的最新已生效集合」一致：

| 字段 | 写死默认 | 含义 |
|------|----------|------|
| `same_day_order` | `effective_then_publish_then_id` | 同日多条：先 `effective_date`，再 `publish_date`，再 `notice_id` 升序依次应用 |
| `full_replace_mode` | `replace_then_later_incremental` | 遇 `full_replace`：覆盖该交易所当前集合；**其后**同序通知的增量 add/remove 再叠加；同日若后到的 `full_replace` 再次覆盖此前同日结果 |
| `incremental_mode` | `add_remove_on_current_set` | 非 `full_replace`：在当前集合上 add∪、remove∖；禁并行合并、禁「取并集忽略顺序」 |

可选：`params.k0_respect_channel_start` 默认 **`off`**（K0 彻底天真）；若设 `on` 则 K0 仍尊重 2010-03-31 起点但无视名单——须拉数前写死。

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股股票；空头信号臂所覆盖标的。ETF 融券可作分桶诊断，**不进主样本结论**（且 `etf_price_exempt=off`）。不含可转债。  
- **排除（默认）**：调仓日未上市；缺名单/无法判定施行日却硬开空；核准制次新未满 `approval_ipo_min_listed_days` 却按注册制 day1 开空；用复权价。  
- **股票池 PIT**：每个调仓日只用当日已生效可交易名单（可与实验 C 共用）；本页空头另叠加融券名单 PIT。  
- **区间建议**：待数据接入后锁定起止。建议复现默认（可改，须写入配置）：  
  - 主窗：覆盖 `2010-03-31` 通道起点之后足够多空样本；至少跨过若干季度调样施行日；  
  - 稳健分桶：见 `params.diff_buckets`。  
- **PIT 切片原则**：是否可空、名单加减、ST/终止调出、注册制 day1 是否适用，一律按该调仓日当时已生效规则与通知。

### 3.1 oos_split 占位（拉数前冻结；禁 holdout 反调）

配置占位字段（数值待锁，先占位）：

- `oos_split.is_start` / `oos_split.is_end`：样本内（IS）起止交易日  
- `oos_split.holdout_start` / `oos_split.holdout_end`：样本外 / holdout 起止  

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调名单源、施行日锚点、三/四组定义、`k3_fill`、显著性阈值或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **K0 − K2**：全 A 可空相对 PIT——空头失败笔数差、名单外历史空头贡献差、多空净值差。  
2. **K1 − K2**：核对日名单泄露相对 PIT——看被「今天名单」事后借到的历史空头贡献了多少。  
3. **K3 − K2**（`k3_borrow_tighten=on`）：转融券暂停后加严相对仅名单 PIT——失败/可借量差。  
4. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "pre_20100331",           # 通道前（应全失败/不可空）
  "st_same_day_remove",      # ST 当日调出窗
  "delist_proc_remove",      # 终止上市程序当日调出
  "reg_ipo_day1",            # 注册制 IPO 首日可空
  "approval_ipo_lt_90d",     # 核准制次新未满约3个月（禁 day1）
  "list_publish_vs_effective", # 印发日误当事施行日敏感
  "post_20240711_refinance", # 转融券暂停后（K3 敏感）
  "board_star_chinext",      # 科创/创业分列诊断
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 空头失败笔数/率差 ΔFail（名单外 / 通道前 / K3 加严导致 skip）；  
2. 泄露贡献差 ΔLeak（K1 相对 K2：被核对日名单事后纳入的历史空头腿贡献的那截）；  
3. 多空净值差 ΔNAV（K0−K2、K1−K2、K3−K2）——**可选**，有信号臂时才报，不得单独当「能空/该规避」证据。

**相对判据（草稿）**：若 |ΔFail| **≥ N** 或 |ΔLeak| **≥ G** 或 |ΔNAV| **≥ Y**，记「融券名单 PIT 鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 净值差显著门槛 | 拉数前写入 `params.Y` 并冻结 |
| G | 泄露贡献差门槛 | 拉数前写入 `params.G` 并冻结 |
| N | 失败笔数/率差门槛 | 拉数前写入 `params.N` 并冻结 |
| Y2 | 稳健子窗净值差门槛（可选） | 拉数前写入 `params.Y2` 并冻结 |
| asof_check_date | 泄露组核对日 | **写死默认** `params.asof_check_date=2026-10-16`；拉数前冻结 |
| shortable_channel_start | 通道起点 | **写死默认** `2010-03-31` |
| refinance_pause_start | 转融券暂停 | **写死默认** `2024-07-11` |
| list_date_mode | 名单生效锚点 | **写死默认** `effective_date` |
| k3_borrow_tighten / k3_fill | 加严档 | **写死默认** `on` / **`skip`**（单一枚举；**禁** `skip_or_cap`；本页不用 `unchanged`；改 `cap` 须同写 `k3_cap_*`） |
| fill_time | 成交时点 | **写死** `next_open`（不用 next_close）；拉数前冻结 |
| list_notice_apply | 同日多条 / full_replace 叠加 | **写死** `same_day_order=effective_then_publish_then_id`；`full_replace_mode=replace_then_later_incremental`；`incremental_mode=add_remove_on_current_set`；拉数前冻结 |
| etf_price_exempt | ETF 免价格限制 | **写死默认** `off` |
| short_same_day_cover | 当日平空 | **写死默认** `forbid` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**`params.Y` / `params.G` / `params.N` / `params.Y2` 写入冻结（本页占位槽已开；拉数前必须落入具体数）**：

```
# 拉数前在 IS 标定窗约定噪声带后写入具体数，一经写入即冻结
params.Y  = null   # 净值差显著门槛；拉数前替换为具体数并冻结
params.G  = null   # 泄露贡献差门槛；拉数前替换为具体数并冻结
params.N  = null   # 失败笔数/率差门槛；拉数前替换为具体数并冻结
params.Y2 = null   # 稳健子窗净值差门槛（可选）；拉数前替换为具体数并冻结
```

门槛可在 **IS 标定窗**（非 holdout）内事先约定噪声带后写入；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、`fill_time`、`k3_fill`、`list_notice_apply` 开工拉数前必须落进 params 并冻结；**禁止跑后改口**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「名单 PIT 无关」。

结论栏：空。跑完只写「该假设下差多少」，不写「这类票因可空/不可空能买或该做空」。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验融券标的名单 PIT / 空头可开机制**，**不为组合策略放行实盘**。

- **显式豁免**：数值红线 v0（单票仓位、行业集中、回撤熔断等组合约束）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权、施行日对齐、PIT 名单、禁 holdout 反调、禁荐股/禁当实盘预期、名单≠一定借得到）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用印发日当事施行日**：`list_date_mode` 必须为 `effective_date`（例：101 号 10-19 而非 10-16）。  
2. **2010-03-31 前发明空头**：诚实组必须失败/不可空。  
3. **注册制 day1 铺到核准制主板新股**：核准制走选取条件，不是上市当天自动可空。  
4. **ST / 终止上市未当日调出**：与事实与坑冲突。  
5. **把标的名单写成一定借得到**：K2 只答「当时是否在名单」；券源加严看 K3，且 K3 不得变回任意量。  
6. **ETF 免价格限制当已实施**：`etf_price_exempt` 必须 `off`。  
7. **当天开空当天平**：`short_same_day_cover=forbid`。  
8. **用复权价判融券价格限制**。  
9. **宇宙泄露 / holdout 反调**：看完 OOS 再改核对日、施行日锚点、`k3_fill`、`list_notice_apply`、`fill_time` 或阈值。  
10. **保留复合名 `skip_or_cap` / 未写死 `list_notice_apply`**：K3 必须单一枚举；同日多条与 `full_replace` 叠加顺序必须写死。  
11. **与 L（市价）/保证金切片混报主结论**：市价与保证金另案；本页主测名单 PIT。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先公开名单规则）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | |
| 沪/深融券标的名单历史（含加减与施行日） | PIT 可空判定 | **公开交易所通知即可起步**；不必新开数据商 |
| publish_date / effective_date | 印发 vs 施行 | 生效锚点用 effective |
| is_st / risk_warn_flag（按日） | 当日调出 | |
| in_delist_procedure_flag（按日） | 当日调出 | |
| board / ipo_regime / list_date | 注册制 day1 vs 核准制 | |
| 未复权 OHLC（可选） | 价格限制自检 | 本页不主测冲击 |
| 信号表（多空臂） | 对照净值 | 无信号可先跑「调仓日 × 可空标签」差 |
| 转融券暂停旗 | K3 | 可用本页切日常量，不必新商 |

**明确**：不依赖聚宽；**优先仅用公开名单规则纸面化**——交易所融券标的调整通知（施行日）+ ST/终止上市旗 + 注册制/核准制上市属性即可起步。券源/可借量明细为增强项，非纸面最小集（K3 用 `k3_fill=skip` 写死；改 cap 才需可借量上限字段）。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=K`，`groups=[K0,K1,K2,K3]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-16`**，**`params.shortable_channel_start=2010-03-31`**，**`params.refinance_pause_start=2024-07-11`**，**`params.refinance_stock_deadline=2024-09-30`**，**`params.list_date_mode=effective_date`**，**`params.st_remove_same_day=True`**，**`params.delist_proc_remove_same_day=True`**，**`params.reg_ipo_shortable_day1=True`**，**`params.approval_ipo_min_listed_days=90`**，**`params.k3_borrow_tighten=on`**，**`params.k3_fill=skip`（写死；枚举仅 skip|cap|unchanged；禁 skip_or_cap；本页不用 unchanged；改 cap 须同写 k3_cap_rule/k3_cap_value）**，**`params.etf_price_exempt=off`**，**`params.short_same_day_cover=forbid`**，**`fill_time=next_open`（写死；不用 next_close）**，**`params.list_notice_apply.same_day_order=effective_then_publish_then_id`**，**`params.list_notice_apply.full_replace_mode=replace_then_later_incremental`**，**`params.list_notice_apply.incremental_mode=add_remove_on_current_set`**，**`params.diff_buckets=[pre_20100331,st_same_day_remove,delist_proc_remove,reg_ipo_day1,approval_ipo_lt_90d,list_publish_vs_effective,post_20240711_refinance,board_star_chinext]`（写死默认；拉数前冻结）**，**`params.Y` / `params.G` / `params.N` / `params.Y2`（占位槽已开；拉数前写入具体数并冻结；禁 holdout 标定）**，`universe_rule`，`date_start/date_end`（可空=待锁），`oos_split.{is_start,is_end,holdout_start,holdout_end}`（占位，禁 holdout 反调），`redline_v0_exempt=true`（仅本机制实验；见 §4.3），`overlay_C=on|off`（建议 on：股票池 PIT 共用），`overlay_L=off`（默认 off；市价另案）。  
- 名单与规则表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- K0/K1/K2/K3 空头失败笔数、泄露贡献、（可选）多空净值；分桶（通道前 / ST 当日 / 注册制 day1 / 核准制次新 / 印发vs施行 / 暂停后）。  
- 自检布尔：是否施行日对齐；2010-03-31 前是否不可空；ST/终止是否当日调出；是否未把注册制 day1 铺到核准制；`etf_price_exempt` 是否 off；是否未当天平空；`fill_time` 是否 `next_open`；`k3_fill` 是否为三枚举之一且非 `skip_or_cap`；`list_notice_apply` 三字段是否已写死；Y/G/N/Y2 与切日是否已冻结；holdout 是否未反调；是否未声称名单=一定借得到。  
- **禁止输出**：具体做空标的列表当「建议」；把天真全 A 可空当实盘预期；催跑抢 A 真数队列。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` 一致：默认不能按美股全市场多空对称；融券只覆盖当时交易所公布标的；2010-03-31 前无此通道。与 `事实与坑.md` 2026-10-16 条一致：施行日对齐、ST/终止当日调出、注册制首日≠核准制次新、转融券 2024-07-11 暂停≠标的消失、名单≠一定借得到、融券禁市价与当日平、ETF 免价格限制暂不实施。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 K 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A/D/E/F/G/H/I/J 正文**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；公开融券名单通知+ST/上市属性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；oos_split 占位+禁 holdout 反调；红线 v0 机制豁免；asof_check_date=2026-10-16 / shortable_channel_start=2010-03-31 / refinance_pause_start=2024-07-11 / list_date_mode=effective_date；**fill_time=next_open 写死**；**k3_fill=skip 写死**（禁 skip_or_cap；本页不用 unchanged）；**list_notice_apply 三字段写死**（same_day_order / full_replace_mode / incremental_mode）；etf_price_exempt=off / short_same_day_cover=forbid / diff_buckets 八桶写死+拉数前冻结；**Y/G/N/Y2 占位槽已开、拉数前写入具体数并冻结、禁 holdout 标定** |

---

## 变更

- 2026-11-02：新建标准件（总管线：I 补丁已交、J 已落盘后继续可离线下一纸面；选型 K；优先公开名单规则纸面；机制类预埋 fail_policy/oos/红线豁免/params 冻结；**不抢实验 A**）。
- 2026-11-02：风控有条件通过四条补齐——① `fill_time=next_open` 写死；② `k3_fill=skip` 单一枚举写死（禁 `skip_or_cap`；本页不用 `unchanged`；改 `cap` 须同写 `k3_cap_*`）；③ `params.Y/G/N/Y2` 占位槽写入、拉数前落入具体数并冻结、禁 holdout 标定；④ `params.list_notice_apply` 写死同日多条顺序与 `full_replace`/增量叠加（`effective_then_publish_then_id` / `replace_then_later_incremental` / `add_remove_on_current_set`）。顺修 §9 标题乱码→「状态」。参考 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设K-20261102.md`。
