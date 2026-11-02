# 假设 P · 指数点位当可交易组合（停牌价 + 总股本权重）

更新：2026-11-02  
来源：总管线 / O 四条风控补丁已交后恢复写 P；清单实验 P  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「指数日收益当可交易组合 / 停牌按前收盘成交 / 总股本权重」当实盘预期；不抢实验 A 真数队列；本页不开回测；O 不开回测）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 P 对齐。与假设 C（幸存者/名单 PIT）、D（停牌假成交时点）、O（大宗不进指数）、H（退市整理不进指数）互补：本页专测两件事——（1）把**指数点位/日收益**当成「按同样权重、同样价能交易的组合」，停牌腿按交易所收盘价（常是前收盘）假成交；（2）用**总股本或解禁当日流通盘**加权，对不上中证自由流通+分级靠档；再把大宗折价写进指数中性收益（大宗不进指数）。**名单泄露属实验 C，本页默认名单 PIT，禁止用今天的沪深300回放却标本页结论。**

---

## 1. 一句话假设（可检验、可证伪）

同一调仓日、同一持有期下，用指数日收益直接当组合收益（停牌日按收盘价/前收盘可交易，权实用总股本），相对「名单 PIT + 停牌/无成交记不可交易 + 权重用当时已生效自由流通+分级靠档（解禁未到 6/12 月第二个星期五下一交易日则不加流通盘）」的诚实组，会**显著抬高可交易覆盖、扭曲跟踪误差，并把停牌腿假成交与权重差贡献写进「指数中性」收益**；再把交易类强制退市停牌的 **0.00001** 剔除价当成竞价可成交，或把大宗折价写进指数中性，会进一步错标。

证伪方向：若天真组 / 半诚实组相对诚实组的跟踪误差差、停牌腿贡献差、权重差在标定噪声带内可忽略，且「连续停牌>25 日 / 交易类强制退市剔除价 / 解禁未生效」分桶不改变结论，则本假设在该样本与撮合设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 指数点位 ≠ 可交易组合；停牌价；自由流通+分级靠档（未复权）

```
# 配置写死（见 §7）
# params.asof_check_date                 写死默认 2026-10-23  # 事实与坑指数/大宗核对日；泄露敏感仅作诊断锚，本页主对照禁名单泄露
# params.index_id                        写死默认 CSI300     # 主样本沪深300；中证500等另桶
# params.membership_mode                 写死 pit            # 本页默认名单 PIT；禁 asof_leak（那是实验 C）
# params.fill_time                        写死 next_open      # 组合调仓腿与 A/D 对齐；指数 TE 诊断可用同日 close 盯市但不改成交腿
# params.p0_use_index_return_as_portfolio 写死默认 True      # 天真：指数收益直接当组合收益
# params.p0_halt_tradable                 写死默认 True      # 天真：停牌按收盘价（前收盘）可交易
# params.p0_weight_basis                  写死 total_shares  # 天真：总股本加权
# params.p1_membership_pit                写死默认 True      # 半诚实：名单 PIT
# params.p1_halt_tradable                 写死默认 True      # 半诚实：停牌仍可按收盘成交
# params.p1_weight_basis                  写死 total_shares  # 半诚实：仍总股本
# params.p2_membership_pit                写死默认 True
# params.p2_halt_tradable                 写死默认 False     # 诚实：停牌/无成交记不可交易
# params.p2_weight_basis                  写死 free_float_graded  # 诚实：自由流通+分级靠档
# params.p3_long_halt_priority_exclude    写死默认 True      # 可选档：连续停牌>25 日且仍未复牌 → 优先剔除处理
# params.long_halt_days                   写死默认 25
# params.free_float_rebalance_rule        写死 jun_dec_2nd_friday_next  # 解禁当日一般不改；半年度与调样同生效日
# params.unlock_same_day_add_float        写死默认 False     # 解禁当日不加流通盘
# params.delist_halt_exclude_px           写死默认 0.00001
# params.treat_delist_halt_px_as_auction  写死默认 False     # 禁把 0.00001 写成竞价可成交
# params.block_into_index                 写死默认 False     # 大宗不进指数；与 O 分列
# params.exit_period_into_index           写死默认 False     # 退市整理不纳入指数（与 H 分列）
# params.missing_free_float_policy        写死 skip_weight_leg  # 无自由流通/靠档字段 → 跳过精确权重腿，禁静默总股本却标 P2
# params.missing_halt_flag_policy         写死 skip          # 缺停牌标记 → skip，禁静默当可交易
# params.diff_buckets                     写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                   写死具体数并冻结；禁 holdout 标定
# params.date_start / date_end            写死主窗并冻结
# params.oos_split.*                      写死四日期并冻结；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 fill_time·membership_mode·权重口径·停牌可成交开关·0.00001 政策·Y/G/N/Y2·主窗/oos

tick = 0.01  # A 股股票默认；本页主样本股票成分
fill_time = "next_open"
asof_check_date = "2026-10-23"
index_id = "CSI300"
membership_mode = "pit"
long_halt_days = 25
free_float_rebalance_rule = "jun_dec_2nd_friday_next"
unlock_same_day_add_float = False
delist_halt_exclude_px = 0.00001
treat_delist_halt_px_as_auction = False
block_into_index = False
exit_period_into_index = False
missing_free_float_policy = "skip_weight_leg"
missing_halt_flag_policy = "skip"

GRADE_BANDS = [
  (0.0, 0.15, "ceil_int_pct"),   # ≤15% 上调到最接近整数（按中证文本）
  (0.15, 0.20, 0.20),
  (0.20, 0.30, 0.30),
  (0.30, 0.40, 0.40),
  (0.40, 0.50, 0.50),
  (0.50, 0.60, 0.60),
  (0.60, 0.70, 0.70),
  (0.70, 0.80, 0.80),
  (0.80, 1.01, 1.00),            # >80% → 100%
]

def graded_free_float_ratio(ff_ratio):
    if ff_ratio is None:
        return None
    if ff_ratio <= 0.15:
        # ≤15%：上调到最接近整数百分点；实现细节拉数前写入 params.grade_le15_impl 并冻结
        return "ceil_int_pct"  # 占位标记；真实数在引擎按中证文本实现
    for lo, hi, band in GRADE_BANDS[1:]:
        if lo < ff_ratio <= hi or (lo == 0.80 and ff_ratio > 0.80):
            return band if isinstance(band, float) else band
    return None

def free_float_effective(asof_date, unlock_date, ff_pre, ff_post):
    # 解禁当日一般不改；生效日 = 每年 6/12 月第二个星期五的下一交易日
    if unlock_same_day_add_float:
        raise ValueError("unlock_same_day_add_float must stay False")
    if unlock_date is None or asof_date < next_ff_rebalance_on_or_after(unlock_date):
        return ff_pre
    return ff_post

def next_ff_rebalance_on_or_after(d):
    # 返回 d 当日或之后最近的「6/12 月第二个星期五下一交易日」
    # 具体日历拉数前固化；本页只锁规则名 jun_dec_2nd_friday_next
    return "calendar_lookup"

def is_halt_or_no_trade(suspend_flag, volume):
    if suspend_flag is None and missing_halt_flag_policy == "skip":
        return None  # 上层 skip
    if suspend_flag:
        return True
    if volume is not None and volume <= 0:
        return True
    return False

def tradable_px(group, close_px, prev_close, halt):
    if halt is None:
        return None  # skip
    if group in ("P0", "P1"):
        # 停牌仍按收盘价（常是前收盘）假成交
        if halt:
            return close_px if close_px is not None else prev_close
        return close_px
    # P2/P3 诚实：停牌/无成交不可交易
    if halt:
        return None
    return close_px

def weight_shares(group, total_shares, adj_free_float_shares):
    if group in ("P0", "P1"):
        return total_shares
    # P2/P3
    if adj_free_float_shares is None:
        if missing_free_float_policy == "skip_weight_leg":
            return None
        raise ValueError("missing free float")
    return adj_free_float_shares

def delist_halt_exclude_price_ok_as_fill(px):
    # 硬禁：0.00001 不得写成竞价可成交
    if treat_delist_halt_px_as_auction:
        raise ValueError("treat_delist_halt_px_as_auction must stay False")
    if px is not None and abs(px - delist_halt_exclude_px) < 1e-12:
        return False
    return True

def long_halt_priority_exclude(consec_halt_days, still_halted):
    if not p3_long_halt_priority_exclude:
        return False
    return still_halted and consec_halt_days is not None and consec_halt_days > long_halt_days
```

- **天真（P0）**：指数日收益直接当组合收益；停牌日按收盘价（前收盘）可交易；权实用总股本；不拆自由流通生效日。  
- **半诚实（P1）**：成分名单 **PIT**（可与实验 C 共用）；停牌仍按收盘价成交；权重仍用总股本。  
- **诚实（P2）**：名单 PIT；停牌/全日无成交记**不可交易**；权重用当时已生效自由流通+分级靠档；解禁未到半年度生效日不加流通盘；大宗不进指数；退市整理不纳入指数。  
- **可选诚实加严（P3）**：在 P2 上，连续停牌 `> long_halt_days(25)` 且仍未复牌 → 按优先剔除处理；交易类强制退市停牌剔除价 **0.00001** **不得**当成竞价成交价（只作指数剔除诊断）。  
- **禁止**：用今天的沪深300回放（实验 C）；把 0.00001 写成竞价可成交；把大宗折价写进指数中性；结论写成选股/指数增强公式；用复权价。

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺停牌标记、缺自由流通/靠档却要标 P2 精确权重、缺成分 PIT 名单、把 0.00001 当竞价成交、`membership_mode≠pit` 却进本页主结论 → **跳过该腿/该日该票**，不按前收盘假成、不静默总股本却标诚实。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 四组对照（本实验编码）

| 组 | 名单 | 停牌/无成交 | 权重 |
|----|------|-------------|------|
| P0 天真 | 可用指数点位/日收益直接替代组合（不拆腿）或总股本+停牌可成 | 按收盘价（前收盘）可交易 | 总股本 |
| P1 半诚实 | **PIT** | 仍按收盘价可交易 | 总股本 |
| P2 诚实 | **PIT** | **不可交易** | 自由流通+分级靠档（生效日规则） |
| P3 诚实+长停牌 | **PIT** | 不可交易；`>25` 日优先剔除诊断 | 同 P2；0.00001 禁当竞价成交 |

同一调仓日、同一成本开关（本页可先零成本只比 TE / 停牌腿 / 权重差）。**`params.fill_time=next_open` 写死**（调仓腿与 A/D 对齐；不抢 A 板上真数队列）。指数盯市可用同日 close 仅作 TE 诊断，**不得**把盯市价改口写成停牌可成交。

**`params.membership_mode=pit`（写死；拉数前冻结）**：本页主对照禁止 `asof_leak`；名单泄露对照归实验 C，不得与本页混报主结论却不标注。

**`params.missing_free_float_policy=skip_weight_leg`（写死）**：无自由流通/靠档字段时，跳过精确权重腿；**禁止**静默用总股本却标 P2/P3。

**`params.treat_delist_halt_px_as_auction=False`（写死）**：0.00001 只作指数剔除价诊断，禁止写成竞价可成交。

**`params.block_into_index=False` / `params.exit_period_into_index=False`（写死）**：与 O/H 分列；禁止把大宗折价或整理期成交写进指数中性主表。

---

## 3. 样本区间

- **宇宙（默认）**：沪深300 成分（`params.index_id=CSI300`）；中证500/全 A 指数另桶。主样本股票成分。  
- **排除（默认）**：调仓日未上市；缺未复权收盘；把今日成分回放历史却标本页；无自由流通却声称精确复制权重。  
- **股票池 PIT**：每个调仓日只用当日已生效成分（可与实验 C 共用生效日：6/12 月第二个星期五下一交易日；ST 月度剔除用每月第二个星期五下一交易日）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖多轮半年度调样、长停牌与交易类退市窗口；稳健分桶见 `params.diff_buckets`。  
- **PIT 切片原则**：该日该成分是否在指数、停牌是否可交易、自由流通是否已生效，一律按调仓日/成交日当时规则。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调停牌可成交定义、权重口径、显著性阈值或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **P0 − P2**：天真「指数收益当组合 + 停牌假成交 + 总股本」相对诚实——跟踪误差差、停牌腿贡献差、权重差、失败/跳过笔数差。  
2. **P1 − P2**：半诚实（名单已 PIT，价/权仍假）相对诚实——看「只修名单、不修停牌与权重」是否仍够吹胖。  
3. **P3 − P2**：长停牌优先剔除 / 0.00001 禁成交诊断相对 P2——看长停牌与退市类剔除价是否额外扭曲。  
4. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "halt_days",                 # 停牌/无成交日
  "long_halt_gt25",            # 连续停牌 >25 日且仍未复牌
  "delist_halt_px_1e-5",       # 交易类强制退市停牌剔除价 0.00001 诊断（禁当成交）
  "unlock_before_ff_rebal",    # 解禁未到 6/12 月第二个星期五下一交易日
  "ff_rebal_jun_dec",          # 半年度自由流通/调样生效窗
  "vs_C_membership",           # 与实验 C 名单对照分列（禁混主结论）
  "vs_O_block",                # 大宗不进指数诊断（禁把大宗折价写进指数中性）
  "vs_H_exit_period",          # 退市整理不纳入指数
  "weight_total_vs_ff",        # 总股本 vs 自由流通+靠档
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 跟踪误差差 ΔTE（P0/P1 相对 P2）；  
2. 停牌腿贡献差 ΔHalt（被「停牌按前收盘成交」吃到的那截）；  
3. 权重差 ΔW（总股本 vs 自由流通+靠档导致的收益/暴露差）；  
4. 失败/跳过笔数差 ΔFail（缺字段、0.00001 误成、无自由流通却标精确权重）。

**相对判据（草稿）**：若 |ΔTE| **≥ Y** 或 |ΔHalt| **≥ G** 或 |ΔW| **≥ Y2** 或 |ΔFail| **≥ N**，记「指数点位假可交易 / 权重口径执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 跟踪误差差显著门槛 | **写死** `params.Y=0.02` 并冻结 |
| G | 停牌腿贡献差门槛 | **写死** `params.G=0.01` 并冻结 |
| N | 失败笔数率差门槛 | **写死** `params.N=0.05` 并冻结 |
| Y2 | 权重差 / 稳健子窗门槛 | **写死** `params.Y2=0.015` 并冻结 |
| asof_check_date | 核对日锚点（诊断） | **写死默认** `2026-10-23`；拉数前冻结 |
| fill_time | 调仓成交时点 | **写死** `next_open` |
| membership_mode | 名单模式 | **写死** `pit` |
| long_halt_days | 长停牌阈值 | **写死** `25` |
| treat_delist_halt_px_as_auction | 0.00001 是否可成 | **写死** `False` |
| block_into_index | 大宗是否进指数 | **写死** `False` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**`params.Y` / `params.G` / `params.N` / `params.Y2` 写入冻结（具体数已写入；禁继续 null；禁 holdout 标定）**：

```
# 纸面冻结默认（机制实验相对门槛；一经写入即冻结）
# 单位：Y/Y2 = abs(ΔTE) 或 abs(ΔW) 相对；G = abs(ΔHalt) 相对；N = abs(ΔFail) 失败率（小数）
params.Y  = 0.02    # TE 差显著门槛 ≥ 2pp
params.G  = 0.01    # 停牌腿贡献差门槛 ≥ 1pp
params.N  = 0.05    # 失败率差门槛 ≥ 5pp
params.Y2 = 0.015   # 权重差/稳健子窗门槛 ≥ 1.5pp
```

门槛已在纸面写入并冻结；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、停牌可成交开关、权重口径、0.00001 政策、主窗/`oos_split` 开工拉数前必须保持冻结；**禁止跑后改口**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「指数点位可以当组合」或「总股本权重差不多」。

结论栏：空。跑完只写「该假设下差多少」，不写「这类票/这类指数增强能买」。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验指数点位假可交易（停牌价）+ 权重口径（总股本 vs 自由流通靠档）**，**不为组合策略/指数增强放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权、名单 PIT、停牌不可假成、禁 0.00001 当竞价成交、禁大宗进指数、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用指数日收益直接当可交易组合收益却标诚实（P2/P3）**：发明停牌假成交与权重对齐；仅允许出现在 P0 叙事。  
2. **停牌/无成交按收盘价（前收盘）成交却标 P2/P3**。  
3. **权实用总股本或解禁当日流通盘却标自由流通+靠档诚实**。  
4. **解禁当日即改自由流通量（违反 `unlock_same_day_add_float=False` / `free_float_rebalance_rule`）**。  
5. **把 0.00001 剔除价写成竞价可成交**。  
6. **用今天的沪深300/今日成分回放（实验 C；违反 `membership_mode=pit`）**。  
7. **把大宗折价写进指数中性收益（违反 `block_into_index=False`；与 O 分列）**。  
8. **退市整理期成交算进指数（违反 `exit_period_into_index=False`；与 H 分列）**。  
9. **无自由流通字段却静默总股本并标 P2（违反 `missing_free_float_policy`）**。  
10. **用复权价撮合或算权重市值**。  
11. **宇宙泄露 / holdout 反调**：看完 OOS 再改停牌定义、权重口径或显著性门槛。  
12. **把差异写成选股/指数增强公式**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | |
| index_id / 成分 PIT 名单 | 当日已生效成分 | **必填**；可与实验 C 共用；禁今日名单 |
| open/high/low/close（未复权） | 价腿 / TE | **禁复权**；停牌日 close 常=前收盘 |
| prev_close | 停牌假价对照 | |
| suspend_flag / volume | 停牌/无成交 | 缺 → skip |
| consec_halt_days | P3 长停牌 | 有则更好 |
| total_shares | P0/P1 权重 | |
| free_float_ratio 或 adj_free_float_shares | P2/P3 权重 | 缺 → skip_weight_leg |
| graded band 或可靠算靠档 | P2/P3 | 可用本页 §2.1 编码 |
| unlock_date（可选） | 解禁未生效桶 | |
| delist_halt_exclude_px 标记 | 0.00001 诊断 | 禁当成交 |
| 指数日收益（官方） | P0 对照锚 | |
| 调样/自由流通生效日历 | 6/12 月第二个星期五下一交易日 | 不必新开数据商 |

**明确**：不依赖聚宽；**不要求新开 Level-2 数据商**——日频未复权 OHLC + 停牌标记 + 成分 PIT + 总股本/自由流通（有则）+ 本页生效日规则即可起步。无自由流通时只做停牌假成交对照 + skip 精确权重腿，不声称精确复制沪深300权重。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=P`，`groups=[P0,P1,P2,P3]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-23`**，**`params.index_id=CSI300`**，**`params.membership_mode=pit`（写死；禁 asof_leak 进本页主结论）**，**`params.fill_time=next_open`（写死）**，**`params.p0_use_index_return_as_portfolio=True`**，**`params.p0_halt_tradable=True`**，**`params.p0_weight_basis=total_shares`**，**`params.p1_membership_pit=True`**，**`params.p1_halt_tradable=True`**，**`params.p1_weight_basis=total_shares`**，**`params.p2_halt_tradable=False`**，**`params.p2_weight_basis=free_float_graded`**，**`params.p3_long_halt_priority_exclude=True`**，**`params.long_halt_days=25`**，**`params.free_float_rebalance_rule=jun_dec_2nd_friday_next`**，**`params.unlock_same_day_add_float=False`**，**`params.delist_halt_exclude_px=0.00001`**，**`params.treat_delist_halt_px_as_auction=False`**，**`params.block_into_index=False`**，**`params.exit_period_into_index=False`**，**`params.missing_free_float_policy=skip_weight_leg`**，**`params.missing_halt_flag_policy=skip`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[halt_days,long_halt_gt25,delist_halt_px_1e-5,unlock_before_ff_rebal,ff_rebal_jun_dec,vs_C_membership,vs_O_block,vs_H_exit_period,weight_total_vs_ff]`（写死默认；拉数前冻结）**，**`params.Y=0.02` / `params.G=0.01` / `params.N=0.05` / `params.Y2=0.015`（写死具体数并冻结；禁 holdout 标定；禁 null）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_C=off`（默认 off；名单对照分表），`overlay_O=off`，`overlay_H=off`，`overlay_A=off`，`cost_switch=off`（P 主跑）。  
- 行情与规则表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- P0/P1/P2/P3 跟踪误差、停牌腿贡献、权重差、失败笔数；分桶（停牌日、长停牌>25、0.00001 诊断、解禁未生效、半年度生效窗、vs C/O/H、总股本 vs 自由流通）。  
- 自检布尔：是否未复权；名单是否 PIT；P2/P3 停牌是否不可交易；是否未把 0.00001 当成交；是否未把大宗/整理期写进指数；无自由流通是否 skip 权重腿；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把天真指数点位/停牌假成当实盘预期；催跑抢 A 真数队列。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**O 不开回测**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` 一致：指数点位不是成分股可成交价；停牌样本继续用交易所收盘价往下算（常是前收盘）；权重用自由流通+分级靠档，解禁当日一般不改；大宗不进指数。与 `事实与坑.md` 2026-10-23 条一致：长停牌>25 日优先剔除规则、剔除价 0.00001、靠档表、半年度生效日。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 P 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A/D–O 正文**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权 OHLC + 停牌 + 成分 PIT + 总股本/自由流通（有则）即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测；**O 不开回测**） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-23；index_id=CSI300；**membership_mode=pit**；**fill_time=next_open 写死**；P0 指数当组合+停牌可成+总股本 / P1 名单PIT仍假价权 / P2 停牌不可成+自由流通靠档 / P3 长停牌>25+0.00001禁成交；unlock_same_day_add_float=False；block_into_index=False；exit_period_into_index=False；missing_free_float_policy=skip_weight_leg；diff_buckets 九桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死具体数并冻结、禁 holdout 标定、禁 null** |

---

## 变更

- 2026-11-02：新建标准件（总管线：O 四条风控补丁已交后恢复写 P；选型对齐清单实验 P；机制类预埋 fail_policy/oos/红线豁免/params 冻结；**不抢实验 A**；**不派回测**；**本页不开回测**；**O 不开回测**）。
