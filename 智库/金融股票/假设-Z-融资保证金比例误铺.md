# 假设 Z · 融资融券保证金比例现行档误铺（杠杆诚信）

更新：2026-11-02  
来源：总管线 / Y 草稿已交、Y 预检补丁由他人负责后并行写下一纸面 Z；清单开跑前检查第 15 条「融资/融券保证金按当时通知切片」半句尚无独立实验（实验 K 只测融券名单 PIT，正文写明保证金杠杆可另案）；选题自 `事实与坑` 2026-10-16「保证金比例按当时通知切片」+ K「不主测保证金杠杆切片（可另案）」；**新建实验 Z**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「全样本 1 倍杠杆 / 用核对日 100% 铺满历史 / 融资 80% 窗抄成 100% 或反过来」当实盘杠杆预期；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/X/W/A 及已交补丁正文**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 开跑前检查第 15 条保证金半句对齐；清单原止于 Y，本页自立实验 Z 标准件。与假设 K（融券空头名单 PIT）**分列**：本页**主测**把融资/融券**保证金比例**按现行档铺满、或用错切日档，从而系统性改写多空可开杠杆与保证金占用；**名单可空性属 K，市价通道属 L，费用四层属 S/T/U/V。本页主结论不混。** 板上可成交属 A。本页主结论不混。

> **字母消歧（硬）**：本页**实验字母 Z** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 Z / 假设-Z / hypothesis_id=Z / 组 Z0·Z1·Z2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1、同一未复权价、同一融券名单（K 层诚实输入）下，把融资/融券保证金比例写成「全样本 1 倍杠杆（保证金≈0 占用）」或「全样本用核对日现行 100%（融资）/100%·私募 120%（融券）」铺满，相对「融资：2023-09-08 收市后起新开不得低于 80%、2026-01-19 起新开不得低于 100%（实施前未了结仍按原规定）；融券：2024-07-22 起不得低于 100%、私募 120%；券商可加码，本页以交易所下限为最宽杠杆」的 PIT 诚实组，会**系统性改写多空可开仓名义与保证金占用——漏计/过松偏乐观（吹胖杠杆收益），现行档误铺切日前偏悲观（罚重早年杠杆）**；差异应**集中在切日窗桶**（融资 80% 窗 / 融资 100% 窗 / 融券 2024-07-22 前后），而不是随机散开。

证伪方向：若天真组 / 泄露组相对诚实组的名义差、保证金占用差、杠杆贡献净值差在标定噪声带内可忽略，且「融资 2023-09-08～2026-01-18 / 2026-01-19 后 / 融券 2024-07-22 前 / 后 / 私募腿」分桶不改变结论（差异不集中在切日相关桶），则本假设在该样本与保证金设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 保证金比例 ≠ 标的名单；融资/融券分切日；交易所下限最宽（未复权名义）

```
# 配置写死键（见 §7；风控补丁四条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 Z
# params.asof_check_date                 写死默认 2026-10-16  # 事实与坑「融券/保证金」核对日；与 K 同周五复盘锚
# params.fill_time                        写死 next_open      # 成交腿与 A/D/K 对齐；不抢 A 板上真数
# params.margin_channel_start            写死 2010-03-31     # 融资融券通道起点；此前不可融资/融券 → skip 杠杆腿
# params.fin_margin_cut_20230908         写死 2023-09-08     # 融资不得低于 80%；自该日收市后实施
# params.fin_margin_cut_20260119         写死 2026-01-19     # 融资新开不得低于 100%；实施前未了结仍按原规定
# params.fin_margin_pct_mid              写死 0.80           # 2023-09-08 收市后～2026-01-18 新开窗
# params.fin_margin_pct_post             写死 1.00           # 2026-01-19 起新开
# params.fin_legacy_keep_pre_cut         写死 True           # 2026-01-19 前未了结融资合约及其展期仍按原规定（事实窗）
# params.short_margin_cut_20240722       写死 2024-07-22     # 融券不得低于 100%（私募 120%）
# params.short_margin_pct_post           写死 1.00
# params.short_margin_pct_pe_post        写死 1.20           # 私募证券投资基金
# params.short_margin_pct_pre_cut        写死 leave_unsliced # 2024-07-22 前细则正文曾写 50% 等，已被通知覆盖；主窗若含切日前须显式冻结或 skip
# params.pre_20240722_short_window       写死 skip_or_out_of_scope  # 风控补丁冻结；主测不依赖未核死旧档；禁静默用 0.50 标 Z2
# params.broker_may_tighten              写死 True           # 券商可在交易所下限之上加码；本页只用交易所下限当最宽杠杆
# params.z0_primary_demo                 写死 flat_one_times  # 风控补丁冻结；主报全样本 1 倍/零占用；禁与 asof_leak_flat_100 双挂
# params.fin_dayfreq_20230908_rule        写死 next_day_mid80  # 风控补丁冻结；日频把 2023-09-08 收市后近似到次日起 80%
# params.z0_margin_pct                   写死 0.0            # 天真主路径：保证金占用≈0 → 名义杠杆无穷/1 倍现金当满仓融资（见编码注释）
# params.z1_margin_pct_fin               写死 1.00           # 泄露：融资全样本用核对日 100%
# params.z1_margin_pct_short             写死 1.00           # 泄露：融券全样本 100%（私募诊断桶可另用 1.20）
# params.z2_pit                          写死 True
# params.apply_fin_rules_to_short        写死 False          # 禁把融资切日抄到融券腿
# params.apply_short_rules_to_fin        写死 False          # 禁把融券 100%/120% 抄到融资腿
# params.merge_with_K_shortable_list     写死 False          # 名单另页 K；本页默认输入「K2 诚实名单」或显式声明 list_overlay
# params.merge_with_L_mkt                写死 False          # 市价通道另页 L
# params.merge_with_S_T_U_V_fee          写死 False          # 费用四层另页
# params.merge_with_A_fill               写死 False
# params.merge_with_Q_cb                 写死 False          # 可转债另页 Q
# params.list_overlay                    写死 k2_honest_or_long_only  # 空头腿须有名单；缺名单 → skip 空头杠杆腿
# params.missing_margin_leg_policy       写死 skip
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 Z；禁 holdout 标定；禁 null
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改切日、比例档、z0_primary_demo、pre_20240722_short_window、fin_dayfreq_20230908_rule、params.Y/G/N/Y2、主窗/oos

fill_time = "next_open"
asof_check_date = "2026-10-16"
margin_channel_start = "2010-03-31"
fin_margin_cut_20230908 = "2023-09-08"
fin_margin_cut_20260119 = "2026-01-19"
fin_margin_pct_mid = 0.80
fin_margin_pct_post = 1.00
fin_legacy_keep_pre_cut = True
short_margin_cut_20240722 = "2024-07-22"
short_margin_pct_post = 1.00
short_margin_pct_pe_post = 1.20
broker_may_tighten = True
apply_fin_rules_to_short = False
apply_short_rules_to_fin = False
merge_with_K_shortable_list = False
merge_with_L_mkt = False
merge_with_S_T_U_V_fee = False
merge_with_A_fill = False
merge_with_Q_cb = False
missing_margin_leg_policy = "skip"
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 Z
G = 0.01
N = 0.05
Y2 = 0.015
z0_primary_demo = "flat_one_times"  # 单一主报；禁与 asof_leak_flat_100 双挂
pre_20240722_short_window = "skip_or_out_of_scope"  # 风控补丁冻结
fin_dayfreq_20230908_rule = "next_day_mid80"  # 风控补丁冻结

def pit_fin_margin_pct(open_date, is_new_open, legacy_open_date=None):
    """融资保证金下限（交易所）。返回 None → 上层 skip。"""
    if open_date < margin_channel_start:
        return None
    # 新开：按开仓日已生效档
    if is_new_open:
        if open_date >= fin_margin_cut_20260119:
            return fin_margin_pct_post
        if open_date > fin_margin_cut_20230908 or (
            open_date == fin_margin_cut_20230908
        ):
            # 通知：自 2023-09-08 收市后实施 → 该日收市后新开用 0.80；日频近似：>= 次日 或 显式 after_close
            # 日频默认：trade_date > 2023-09-08 用 0.80；==2023-09-08 记 after_close_only 桶
            return fin_margin_pct_mid if open_date > fin_margin_cut_20230908 else None
        # 2023-09-08 前融资下限未在本页核死 → skip 或另键
        return None
    # 未了结展期：2026-01-19 前开立者可保留原规定
    if fin_legacy_keep_pre_cut and legacy_open_date is not None:
        if legacy_open_date < fin_margin_cut_20260119:
            if legacy_open_date > fin_margin_cut_20230908:
                return fin_margin_pct_mid
            return None
    return fin_margin_pct_post

def pit_short_margin_pct(open_date, is_pe_fund=False):
    """融券保证金下限（交易所）。切日前主窗默认 skip_or_out_of_scope。"""
    if open_date < margin_channel_start:
        return None
    if open_date >= short_margin_cut_20240722:
        return short_margin_pct_pe_post if is_pe_fund else short_margin_pct_post
    # pre_20240722_short_window = skip_or_out_of_scope
    return None

def margin_pct_for_group(group, leg, open_date, is_new_open=True, is_pe_fund=False, legacy_open_date=None):
    if group == "Z0":
        # 天真：全样本 1 倍现金当满仓、保证金占用≈0（或等价「不写保证金约束」）
        return 0.0
    if group == "Z1":
        # 泄露：全样本用核对日现行档
        if leg == "financing":
            return 1.00
        return 1.20 if is_pe_fund else 1.00
    # Z2 PIT
    if leg == "financing":
        return pit_fin_margin_pct(open_date, is_new_open, legacy_open_date)
    return pit_short_margin_pct(open_date, is_pe_fund)

def max_notional(equity, margin_pct):
    """最宽名义 = 保证金资金 / 比例；比例<=0 视为无约束（Z0 诊断）。"""
    if margin_pct is None:
        return None
    if margin_pct <= 0:
        return float("inf")  # 上层用现金全仓名义并打 z0_unconstrained 标记
    return equity / margin_pct
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：通道日 `<2010-03-31`、融资 `<2023-09-08` 未核死旧档却要标 Z2、融券 `<2024-07-22` 却静默用 50% 标诚实、把 K 名单主结论/L 市价/S–V 费用混进本页主表、空头腿无名单却发明可空杠杆 → **跳过该日该腿保证金/杠杆计量**，不静默用现行 100% 填假 PIT。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 Z）

| 组 | 保证金比例 | 说明 |
|----|------------|------|
| Z0 天真-无约束/1 倍 | 占用≈0 或「不写保证金」 | 「全样本 1 倍杠杆/现金满仓当融资」 |
| Z1 泄露-现行档铺满 | 融资 100%；融券 100%（私募 120%） | 用核对日现行档回放历史 |
| Z2 PIT 诚实 | 融资 80% 窗 / 100% 窗按切日；融券 2024-07-22 起 100%/私募 120%；切日前 skip 或窗外 | 交易所下限最宽；券商加码不发明更松 |

同一信号、同一 T+1、同一股票宇宙。本页**主测保证金比例/可开名义/占用差**，不主测名单可空（见 K）、不主测市价（见 L）、不主测板上撮合（见 A）。**`params.fill_time=next_open` 写死**。空头腿默认叠加 **K2 诚实名单** 为输入，**`merge_with_K_shortable_list=False`**（不重开名单实验）。

**`params.merge_with_K_shortable_list=False` / `merge_with_L_mkt=False` / `merge_with_S_T_U_V_fee=False` / `merge_with_A_fill=False` / `merge_with_Q_cb=False`（写死）**。

**风控补丁四条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                 # 名义/占用差显著门槛；≠实验字母 Z
params.G                            = 0.01                 # 切日窗桶相对对照差门槛
params.N                            = 0.05                 # 失败/跳过率差门槛
params.Y2                           = 0.015                # Z1（现行铺满）相对 Z2 专项门槛
params.z0_primary_demo              = flat_one_times       # 主报全样本 1 倍/零占用；禁与 asof_leak_flat_100 双挂
params.pre_20240722_short_window    = skip_or_out_of_scope # 切日前融券窗；禁静默用旧 50% 标 Z2
params.fin_dayfreq_20230908_rule    = next_day_mid80       # 日频把 2023-09-08 收市后近似到次日起 80%
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股可融资/可融券股票为主（空头腿须当日在 K 诚实名单内）；ETF 融券价格限制免责款本页不实施（与 K 同向 `etf_price_exempt=off` 仅作输入声明，不重开）。不含可转债主样本（见 Q）。  
- **排除（默认）**：`<2010-03-31`；融资 `<2023-09-08` 未核死却要硬标 Z2；融券 `<2024-07-22` 且 `pre_20240722_short_window=skip`；把 K/L/A/S–V 主结论并进本页主表。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2023-01-01`  
  - `params.date_end=2026-09-30`  
  - **必须跨过 2023-09-08、2024-07-22、2026-01-19**。  
- **PIT 切片原则**：保证金比例按**开仓日已生效通知**；融资 2026-01-19 前未了结可保留原规定；**禁止**用核对日 100% 回放 80% 窗。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2023-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调比例档、切日、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **Z0 − Z2**：无保证金约束相对 PIT——被吹胖的可开名义 / 杠杆贡献。  
2. **Z1 − Z2**：现行 100% 铺满相对 PIT——80% 窗被罚重、或切日前被误用现行档。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "fin_mid80_window",           # 融资 2023-09-09～2026-01-18 新开（80% 窗）
  "fin_post100_window",         # 融资 2026-01-19 后新开
  "fin_legacy_pre_20260119",    # 未了结仍按原规定桶
  "short_pre_20240722",         # 融券切日前（默认 skip 对照声明）
  "short_post_20240722",        # 融券切日后 100%
  "short_pe_120",               # 私募 120% 腿
  "vs_K_list",                  # 对照声明：名单另页 K
  "vs_L_mkt",                   # 对照声明：市价另页 L
  "vs_A_fill",                  # 对照声明：板上可成交另页 A
  "vs_S_T_U_V_fee",             # 对照声明：费用另页
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可开名义差 ΔNotional（Z0/Z1 相对 Z2）；  
2. 保证金占用差 ΔMargin；  
3. 切日窗桶相对对照的差 ΔNotional_cut；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔMargin| **≥ params.Y** 或 |ΔNotional_cut| **≥ params.G** 或 |ΔNotional_(Z1−Z2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「融资融券保证金比例现行档误铺杠杆诚信鸿沟显著」。

**params.Y / G / N / Y2（拉数前写入；禁 holdout 标定；与实验字母 Z 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/占用差显著门槛（≠实验字母 Z） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 切日窗桶相对对照差门槛 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败笔数率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | Z1 现行铺满专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-16`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| fin_margin_cut_20230908 | 融资 80% 切日 | **写死** `2023-09-08` |
| fin_margin_cut_20260119 | 融资 100% 切日 | **写死** `2026-01-19` |
| short_margin_cut_20240722 | 融券 100% 切日 | **写死** `2024-07-22` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已写入 params 并冻结（风控补丁 2026-11-02；**`params.Y`≠实验字母 Z**）；**禁止用 holdout / OOS 段标定或反调**。

**失败/不显著**：差异落在噪声带内或均匀散在非切日对照桶——结论栏写明，不得改口称「保证金档差不多」或「这类票更能加杠杆」。

结论栏：空。跑完只写「该假设下名义/占用差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验保证金比例诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（PIT 切日、禁 holdout 反调、禁荐股/禁当实盘预期、禁发明比交易所下限更松的杠杆）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用核对日 100% 铺满融资 80% 窗却标 Z2 诚实**。  
2. **把融资切日/比例抄到融券腿，或把融券 100%/120% 抄到融资腿**。  
3. **融券 `<2024-07-22` 静默用细则旧 50% 标 PIT，却不写 `pre_20240722_short_window` 冻结**。  
4. **把 K 名单可空、L 市价、A 板上、S/T/U/V 费用重开混进本页主结论**。  
5. **发明比交易所下限更松的杠杆（忽略券商可加码事实却写成更松）**。  
6. **`<2010-03-31` 发明融资融券通道**。  
7. **宇宙泄露 / holdout 反调**：看完 OOS 再改比例档或 **`params.Y` 等门槛**。  
8. **差异不集中在切日窗桶却仍写「系统性杠杆诚信鸿沟」而不改表述**。  
9. **把差异写成「这类票能买 / 能加杠杆」或选股公式**。  
10. **把实验字母 Z 与 `params.Y` 混改**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股为主 |
| exchange (SSE/SZSE) | 分桶 | 北交所默认另桶/不进主跑 |
| leg (financing/short) | 分腿 | 缺 → skip |
| is_new_open / legacy_open_date | 融资未了结规则 | 缺则按新开近似并声明 |
| is_pe_fund（可选） | 融券私募 120% | 缺则按非私募 100% |
| equity / margin_cash | 保证金资金 | 未复权名义计量 |
| shortable_flag_k2（可选） | 空头腿输入 | 来自 K 诚实名单；缺 → skip 空头 |
| raw OHLC（未复权，可选） | 诊断 | 禁复权判板 |

**明确**：不依赖聚宽；**不要求新开 Level-2**——有日频开平仓腿 + 切日表即可起步；缺腿 → `missing_margin_leg_policy=skip`。主窗自 2023-01-01，必须跨 2023-09-08 / 2024-07-22 / 2026-01-19。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=Z`（**实验字母**），`groups=[Z0,Z1,Z2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-16`**，**`params.fill_time=next_open`（写死）**，**`params.margin_channel_start=2010-03-31`**，**`params.fin_margin_cut_20230908=2023-09-08`**，**`params.fin_margin_cut_20260119=2026-01-19`**，**`params.fin_margin_pct_mid=0.80`**，**`params.fin_margin_pct_post=1.00`**，**`params.fin_legacy_keep_pre_cut=True`**，**`params.short_margin_cut_20240722=2024-07-22`**，**`params.short_margin_pct_post=1.00`**，**`params.short_margin_pct_pe_post=1.20`**，**`params.broker_may_tighten=True`**，**`params.apply_fin_rules_to_short=False`**，**`params.apply_short_rules_to_fin=False`**，**`params.merge_with_K_shortable_list=False`**，**`params.merge_with_L_mkt=False`**，**`params.merge_with_S_T_U_V_fee=False`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_Q_cb=False`**，**`params.list_overlay=k2_honest_or_long_only`**，**`params.missing_margin_leg_policy=skip`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015`（写死冻结；禁 holdout 标定；禁 null；params.Y≠实验字母 Z）**，**`params.z0_primary_demo=flat_one_times`（写死；禁与 asof_leak_flat_100 双挂）**，**`params.pre_20240722_short_window=skip_or_out_of_scope`（写死冻结）**，**`params.fin_dayfreq_20230908_rule=next_day_mid80`（写死冻结）**，`universe_rule`，**`params.date_start=2023-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2023-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_K=off`，`overlay_L=off`，`overlay_A=off`。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- Z0/Z1/Z2 可开名义、保证金占用、ΔNotional、ΔMargin、Z1 专项、失败笔数；分桶（融资 80% 窗 / 100% 窗 / 未了结、融券切日前售后、私募 120%、vs K/L/A/S–V）。  
- 自检布尔：Z2 是否按切日；Z0 是否无约束；Z1 是否现行铺满；是否未把融资/融券规则互抄；是否未与 K/L/A/S–V 混主结论；holdout 是否未反调；**是否未把实验字母 Z 与 params.Y 混用**。  
- **禁止输出**：具体买卖标的列表当「建议」；把现行 100% 当诚实 PIT 铺满 80% 窗；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/X/W/A 已交正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：融资保证金 2023-09-08 收市后 80%、2026-01-19 新开 100%（未了结可按原规定）；融券 2024-07-22 起 100%/私募 120%；券商可加码；通道自 2010-03-31。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 Y，本页**新增实验 Z** 收成标准件，**不改口径主线**，**不改假设 A–Y 正文**。与实验 K 分工：**K=融券标的当时名单；Z=融资/融券保证金比例 PIT**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频开平仓腿 + 切日表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2023-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**三切日 2023-09-08·2024-07-22·2026-01-19 写死**；融资 0.80/1.00、融券 1.00/私募 1.20；diff_buckets 十桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死冻结**（params.Y≠实验字母 Z）；**z0_primary_demo=flat_one_times 写死（禁双挂）**；**pre_20240722_short_window=skip_or_out_of_scope 写死**；**fin_dayfreq_20230908_rule=next_day_mid80 写死** |

---

## 变更

- 2026-11-02：新建标准件（总管线：并行写下一纸面 Z；Y 预检补丁由他人负责；清单止于 Y → 自开跑前检查第 15 条保证金半句 + `事实与坑` 保证金切片 + K「杠杆可另案」选题，**与 A–Y 不撞主结论**；近邻 K=名单、L=市价，本页主测保证金比例误铺；**实验字母 Z ≠ params.Y**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/X/W/A 正文**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设Z-20261102.md` 有条件通过补四条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写入具体数并冻结（预检禁 holdout 标定且建议 0.02/0.01/0.05/0.015；**params.Y≠实验字母 Z**；禁 null）；② `params.z0_primary_demo=flat_one_times`（主报全样本 1 倍/零占用；禁与 asof_leak_flat_100 双挂争主表）；③ `params.pre_20240722_short_window=skip_or_out_of_scope`（切日前融券窗；禁静默用旧 50% 标 Z2）；④ `params.fin_dayfreq_20230908_rule=next_day_mid80`（日频把 2023-09-08 收市后近似到次日起 80%）。**不抢实验 A**；**Z 不开回测**；未动 Y/X/A。

### 增量补丁段 · 2026-11-02（风控四条冻结）

| 键 | 冻结值 | 备注 |
|----|--------|------|
| params.Y | 0.02 | 相对门槛键；**≠实验字母 Z** |
| params.G | 0.01 | 切日窗桶相对对照差 |
| params.N | 0.05 | 失败/跳过率差 |
| params.Y2 | 0.015 | Z1−Z2 专项 |
| params.z0_primary_demo | flat_one_times | 单一主报；禁双挂 |
| params.pre_20240722_short_window | skip_or_out_of_scope | 禁静默旧 50% |
| params.fin_dayfreq_20230908_rule | next_day_mid80 | 日频对齐 09-08 收市后 |

预检稿：`experiments/backtest/A_limit_up_fill/risk_notes/预检-假设Z-20261102.md`。
