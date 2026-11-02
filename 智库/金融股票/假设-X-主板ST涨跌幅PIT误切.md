# 假设 X · 主板 ST/*ST 涨跌幅按现行/历史一刀切误标板（执行鸿沟）

更新：2026-11-02  
来源：总管线 / V 补丁·W 预检并行写下一纸面 X；清单原止于 W，选题自清单开跑前检查「涨跌停按交易日×板块×是否风险警示取当时限制；主板 ST 是否在 2026-07-06 处分段」+ `事实与坑`「主板 ST/*ST：2026-07-06 起与主板普通股同为 10%（此前 5%）；创业板/科创板风险警示股仍 20%」+ `口径`「主板 ST 涨跌幅以 2026-07-06 为界」；**新建实验 X**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「ST 永远 ±5% / 永远 ±10% / 全市场 ST 都 10%」当诚实板上区间；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 V/W/U/A 及已交补丁正文**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 开跑前检查对齐；清单原无 X 节，本页自立实验 X 标准件。与假设 G（涨跌幅规则 PIT·新股/无板窗；G0 附带 `g0_st_mode=use_current_10pct` 仅作泄露臂的 ST 侧写）**分列**：本页**主测**主板风险警示股 **5%→10% 切日** 与「创业/科创风险警示误套主板 10%」；G 的主战场仍是 IPO 前 5 日无板 / 创业板 20% 切日 / 无板日误套 ±10%/±20%。**取整属实验 F；板上可成交属实验 A；除权复权判板属实验 W；退市整理属实验 H；费用四层属 S/T/U/V。本页主结论不混。**

---

## 1. 一句话假设（可检验、可证伪）

同一批主板风险警示股（ST/*ST）、同一未复权 OHLC 与同一交易所前收下，把涨跌幅限制**全历史按 ±5%**、或**全历史按核对日现行 ±10%**、或把**创业板/科创板风险警示也按主板 10%** 去标涨跌停，相对「**2026-07-06 前主板 ST ±5%、之后 ±10%；创业板/科创板风险警示仍 ±20%**」的 PIT 诚实组，会**系统性误标板上区间**；差异率应**集中在主板 ST 且交易日跨 2026-07-06 切日**，以及「创业/科创风险警示被误套 10%」桶，而不是随机散开。错标会把后续「假成交 / 板上约束」实验（如假设 A）带偏。

证伪方向：若天真组 / 泄露组 / 误套组相对诚实组的标签差异率在标定噪声带内可忽略，且「主板 ST 切日前 / 切日后 / 非 ST 主板对照 / 创业·科创风险警示」分桶不改变结论（差异不集中在切日相关桶），则本假设在该样本与判板设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 主板 ST 5%→10% 切日写死；创业/科创风险警示 ≠ 主板 10%；未复权判板

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# params.asof_check_date                 写死默认 2026-10-09  # 与清单/事实「ST 5%→10%」同批核对日（G 同锚；本页不重开新股窗）
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；本页主测标签，不抢 A 板上真数
# params.tick                            写死 0.01           # 仅 A 股股票；禁基金 0.001 混主结论
# params.tag_cmp                         写死 ge_le          # close >= limit_up / close <= limit_down；与 A/F 同向
# params.round_half_up_to_tick           写死 True           # 诚实组板上价先取整（对齐 F1）；本页不主测取整差
# params.st_limit_cut_date               写死 2026-07-06     # 主板 ST/*ST：此前 5%、之后 10%
# params.st_limit_pct_pre                写死 0.05
# params.st_limit_pct_post               写死 0.10
# params.main_non_st_pct                 写死 0.10           # 主板非风险警示对照
# params.chinext_star_risk_warn_pct      写死 0.20           # 创业板/科创板风险警示仍 20%；禁抄主板 10%
# params.bse_risk_warn_pct               写死 0.30           # 北交所风险警示；默认另桶/不进主跑
# params.x0_mode                         写死 flat_5pct      # 天真：主板 ST 全历史 ±5%
# params.x1_mode                         写死 flat_10pct     # 泄露：主板 ST 全历史 ±10%（=核对日现行）
# params.x1b_copy_main10_to_chinext_star 写死 True           # 误套臂开关：创业/科创风险警示也按 10%
# params.x2_mode                         写死 pit_st_cut     # PIT：按切日+板块
# params.st_flag_source                  写死 day_effective_risk_warn  # 按日有效风险警示标记；禁用核对日 ST 名单回放
# params.include_star_st                 写死 True           # 科创风险警示进误套桶对照；板上比例仍 20%
# params.include_chinext_st              写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_F_rounding           写死 False
# params.merge_with_G_limit_pct_pit      写死 False          # 新股/无板窗另页 G；本页不重开 IPO 窗
# params.merge_with_H_exit_period        写死 False          # 退市整理另页 H
# params.merge_with_W_exref              写死 False          # 除权复权判板另页 W
# params.merge_with_S_T_U_V_fee          写死 False
# params.missing_st_flag_policy          写死 skip           # 缺风险警示日标记 → skip
# params.missing_board_policy            写死 skip
# params.no_limit_day_policy             写死 skip           # 无涨跌幅日（见 G）不硬套 ±5%/±10%/±20%
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；禁 holdout 标定；禁 null
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.x0_primary_demo                 写死 flat_5pct     # 风控补丁冻结；主报永远 5%；禁与 flat_10pct / copy_10_to_chinext_star 双挂
# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改切日、5%/10%/20%、Y/G/N/Y2、主窗/oos、x0_primary_demo

fill_time = "next_open"
asof_check_date = "2026-10-09"
tick = 0.01
tag_cmp = "ge_le"
round_half_up_to_tick = True
st_limit_cut_date = "2026-07-06"
st_limit_pct_pre = 0.05
st_limit_pct_post = 0.10
main_non_st_pct = 0.10
chinext_star_risk_warn_pct = 0.20
x0_mode = "flat_5pct"
x1_mode = "flat_10pct"
x1b_copy_main10_to_chinext_star = True
x2_mode = "pit_st_cut"
st_flag_source = "day_effective_risk_warn"
merge_with_A_fill = False
merge_with_F_rounding = False
merge_with_G_limit_pct_pit = False
merge_with_H_exit_period = False
merge_with_W_exref = False
merge_with_S_T_U_V_fee = False
missing_st_flag_policy = "skip"
missing_board_policy = "skip"
no_limit_day_policy = "skip"

def round_half_up(x, tick=0.01):
    from math import floor
    return floor(x / tick + 0.5) * tick

def board_limits(pre_close, pct):
    raw_up = pre_close * (1.0 + pct)
    raw_dn = pre_close * (1.0 - pct)
    if not round_half_up_to_tick:
        return raw_up, raw_dn
    up = round_half_up(raw_up, tick)
    dn = round_half_up(raw_dn, tick)
    if abs(up - pre_close) < tick:
        up = pre_close + tick
    if abs(dn - pre_close) < tick:
        dn = pre_close - tick
    if up < tick:
        up = tick
    if dn < tick:
        dn = tick
    return up, dn

def pit_limit_pct(row):
    """按日有效：主板 ST 切 2026-07-06；创业/科创风险警示 20%；无板日 → None。"""
    if row.get("is_no_limit"):
        return None
    board = row.get("board")  # main / chinext / star / bse
    is_st = bool(row.get("is_risk_warn"))
    d = row["trade_date"]
    if board == "main":
        if is_st:
            return st_limit_pct_pre if d < st_limit_cut_date else st_limit_pct_post
        return main_non_st_pct
    if board in ("chinext", "star"):
        if is_st:
            return chinext_star_risk_warn_pct
        return 0.20
    return None  # bse/其他 → missing_board_policy

def naive_limit_pct(group, row):
    board = row.get("board")
    is_st = bool(row.get("is_risk_warn"))
    if row.get("is_no_limit"):
        return None
    if group == "X0":
        # 天真：主板 ST 全历史 5%；非 ST / 创业科创走对照默认
        if board == "main" and is_st:
            return st_limit_pct_pre
        if board == "main":
            return main_non_st_pct
        if board in ("chinext", "star"):
            return chinext_star_risk_warn_pct if is_st else 0.20
        return None
    if group == "X1":
        # 泄露：主板 ST 全历史 10%
        if board == "main" and is_st:
            return st_limit_pct_post
        if board == "main":
            return main_non_st_pct
        if board in ("chinext", "star"):
            return chinext_star_risk_warn_pct if is_st else 0.20
        return None
    if group == "X1b":
        # 误套：创业/科创风险警示也按主板 10%
        if board in ("chinext", "star") and is_st and x1b_copy_main10_to_chinext_star:
            return st_limit_pct_post
        return pit_limit_pct(row)
    # X2
    return pit_limit_pct(row)

def tag_limit(close, pre_close, pct):
    if close is None or pre_close is None or pct is None:
        return None
    up, dn = board_limits(pre_close, pct)
    return close >= up, close <= dn

def tags_for_group(group, row):
    if row.get("raw_close") is None or row.get("exchange_preclose") is None:
        return None
    if row.get("is_risk_warn") is None:
        return None  # 缺 ST 日标记 → skip（非 ST 对照须显式 False）
    pct = naive_limit_pct(group, row)
    if pct is None:
        return None
    return tag_limit(row["raw_close"], row["exchange_preclose"], pct)
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺未复权收盘/交易所前收、缺按日风险警示标记、缺板块、无涨跌幅日硬套 ±5%/±10%/±20%、把新股窗（G）/整理期（H）/除权复权（W）/取整主差（F）/费用层混进本页主结论 → **跳过该日该券标签**，不静默用核对日 ST 名单或板块默认 10% 填假板。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 X）

| 组 | 主板 ST 比例 | 创业/科创风险警示 | 说明 |
|----|--------------|-------------------|------|
| X0 天真-永远 5% | 全历史 5% | 仍 20%（本臂不测误套） | 券商通页「ST ±5%」铺满 |
| X1 泄露-永远 10% | 全历史 10% | 仍 20% | 用核对日现行铺满历史 |
| X1b 误套-创业科创也 10% | PIT 切日 | **误套 10%** | 「全市场 ST 都 10%」 |
| X2 PIT 诚实 | 切日前 5%、后 10% | **20%** | `pit_st_cut` |

同一日、同一未复权收盘与交易所前收、同一股票宇宙。本页**主测标签差异**，不主测成交撮合（成交见 A；取整主测见 F；新股/无板窗见 G；整理期见 H；除权复权见 W）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_A_fill=False` / `merge_with_F_rounding=False` / `merge_with_G_limit_pct_pit=False` / `merge_with_H_exit_period=False` / `merge_with_W_exref=False` / `merge_with_S_T_U_V_fee=False`（写死）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                # 标签差异率显著门槛 ≥ 2pp（主板 ST 全样本或切日前桶；同系列纸面占位；禁 holdout 标定）
params.G                            = 0.01                # 切日前相对切日后（或相对非 ST 对照）差异率差门槛 ≥ 1pp（ΔTag_cut）
params.N                            = 0.05                # 失败/跳过率差门槛 ≥ 5pp
params.Y2                           = 0.015               # 创业/科创风险警示误套 10% 专项门槛 ≥ 1.5pp（ΔTag_copy）
params.x0_primary_demo              = flat_5pct           # 主报永远 5%；枚举另有 flat_10pct / copy_10_to_chinext_star；禁双挂争主表
params.st_flag_source               = day_effective_risk_warn  # 已写死；禁核对日名单回放
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股股票；**必须含足量主板 ST/*ST 日**（切日前后皆有），并含创业板/科创板风险警示日作 X1b 对照。不含可转债、不含股票 ETF 主样本。  
- **排除（默认）**：无涨跌幅日（见实验 G；纳入须另标）；退市整理期（见实验 H）；`raw_close` / 交易所前收缺失；无法识别板块；缺按日 `is_risk_warn`。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2022-01-01`  
  - `params.date_end=2026-09-30`  
  - **必须跨过 2026-07-06**；切日前须有足够主板 ST 日，否则分桶不可检。  
- **PIT 切片原则**：板上比例一律按**成交日**已生效文本；**禁止用核对日 ST 名单或现行 10% 回放切日前**。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2022-01-01
params.oos_split.is_end         = 2025-06-30
params.oos_split.holdout_start  = 2025-07-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**（holdout 刻意跨过 2026-07-06 以便报告切日后段，**禁止**用 holdout 反调切日、5%/10%、显著性门槛）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **X0 − X2**：永远 5% 相对 PIT——切日后主板 ST 被收窄板上区间的那截标签差。  
2. **X1 − X2**：永远 10% 相对 PIT——切日前主板 ST 被放宽板上区间的那截。  
3. **X1b − X2**：创业/科创风险警示误套 10% 相对诚实 20%。  
4. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "main_st_pre_20260706",      # 主板 ST，切日前（X1 主战场）
  "main_st_post_20260706",     # 主板 ST，切日后（X0 主战场）
  "main_non_st_control",       # 主板非 ST 对照；差异应接近 0
  "chinext_star_risk_warn",    # 创业/科创风险警示（X1b 主战场）
  "st_enter_exit_month",       # 进出风险警示当月（名单 PIT 敏感）
  "vs_G_ipo_window",           # 对照声明：新股/无板窗另页 G，本页不抢主结论
  "vs_H_exit_period",          # 对照声明：整理期另页 H
  "vs_A_fill",                 # 对照声明：板上可成交另页 A
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 标签差异率 ΔTag（X0/X1/X1b 相对 X2；涨停/跌停分列）；  
2. 切日前相对切日后（或相对非 ST）差异率差 ΔTag_cut；  
3. 创业/科创风险警示误套专项 ΔTag_copy；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔTag| **≥ Y** 或 |ΔTag_cut| **≥ G** 或 |ΔTag_copy| **≥ Y2** 或 |ΔFail| **≥ N**，记「主板 ST 涨跌幅 PIT 误切 / 创业科创误套执行鸿沟显著」。

**Y / G / N / Y2（已写入 params 并冻结；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 标签差异率显著门槛 | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| G | 切日相关差异率差门槛 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| N | 失败笔数率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| Y2 | 创业/科创误套 10% 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-09`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| st_limit_cut_date | 主板 ST 切日 | **写死** `2026-07-06` |
| st_limit_pct_pre / post | 5% / 10% | **写死** `0.05` / `0.10` |
| chinext_star_risk_warn_pct | 创业/科创风险警示 | **写死** `0.20` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已写入 params 并冻结（风控补丁 2026-11-02）；**禁止用 holdout / OOS 段标定或反调**。

**失败/不显著**：差异落在噪声带内或均匀散在非 ST / 非切日桶——结论栏写明，不得改口称「ST 5% 和 10% 差不多」或「这类 ST 能买」。

结论栏：空。跑完只写「该假设下标签差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验主板 ST 涨跌幅 PIT / 创业科创误套**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（未复权判板、按日风险警示、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **主板 ST 全历史套 5% 或全历史套 10% 却标 X2 诚实**。  
2. **把创业板/科创板风险警示写成 10% 却标 PIT**。  
3. **用核对日 ST 名单回放历史进出警示日**。  
4. **无涨跌幅日硬套 ±5%/±10%/±20%**（见实验 G）。  
5. **把新股窗/无板窗（G）、整理期（H）、除权复权（W）、取整（F）、板上可成交（A）重开混进本页主结论**。  
6. **把费用四层（S/T/U/V）混进本页主表**。  
7. **宇宙泄露 / holdout 反调**：看完 OOS 再改切日或显著性门槛。  
8. **差异不集中在切日/误套桶却仍写「ST PIT 系统性误标」而不改表述**。  
9. **把差异写成「这类 ST 能买」或选股公式**。  
10. **把 50 万股买入上限（风险警示板）当本页主测却不另开配置**——本页默认不主测该上限（见实验 H 声明）；纳入须另页/另键。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股股票 |
| exchange (SSE/SZSE) | 沪深 | 北交所默认另桶/不进主跑 |
| raw_close / exchange_preclose（未复权） | 判板 | **禁复权**；缺 → skip |
| board (main/chinext/star) | 比例切片 | 缺 → skip |
| is_risk_warn（按日有效） | ST/*ST 标记 | **禁核对日名单回放**；缺 → skip |
| is_no_limit（可选，复用 G 表） | 无板日跳过 | 有则 skip 硬套 |
| in_exit_period（可选） | 与 H 衔接 | 整理期默认排除 |
| st_enter_date / st_exit_date（可选） | 进出警示月桶 | 可有则报 |

**明确**：不依赖聚宽；**不要求新开 Level-2 / 新数据商**——日频未复权行情 + 按日风险警示标记 + 板块 + 本页切日表即可起步。主窗自 2022-01-01，必须跨 2026-07-06。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=X`，`groups=[X0,X1,X1b,X2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-09`**，**`params.fill_time=next_open`（写死）**，**`params.tick=0.01`**，**`params.tag_cmp=ge_le`**，**`params.round_half_up_to_tick=True`**，**`params.st_limit_cut_date=2026-07-06`**，**`params.st_limit_pct_pre=0.05`**，**`params.st_limit_pct_post=0.10`**，**`params.main_non_st_pct=0.10`**，**`params.chinext_star_risk_warn_pct=0.20`**，**`params.x0_mode=flat_5pct`**，**`params.x1_mode=flat_10pct`**，**`params.x1b_copy_main10_to_chinext_star=True`**，**`params.x2_mode=pit_st_cut`**，**`params.st_flag_source=day_effective_risk_warn`**，**`params.missing_st_flag_policy=skip`**，**`params.missing_board_policy=skip`**，**`params.no_limit_day_policy=skip`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_F_rounding=False`**，**`params.merge_with_G_limit_pct_pit=False`**，**`params.merge_with_H_exit_period=False`**，**`params.merge_with_W_exref=False`**，**`params.merge_with_S_T_U_V_fee=False`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015`（写死冻结；禁 holdout 标定；禁 null）**，**`params.x0_primary_demo=flat_5pct`（写死；禁双挂）**，`universe_rule`，**`params.date_start=2022-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2022-01-01,is_end=2025-06-30,holdout_start=2025-07-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_F=off`，`overlay_G=off`，`overlay_H=off`，`overlay_W=off`，`overlay_S=off`，`overlay_T=off`，`overlay_U=off`，`overlay_V=off`。  
- 行情与 ST 日标记：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- X0/X1/X1b/X2 涨跌停标签一致率、ΔTag、ΔTag_cut、误套专项、失败笔数；分桶（切日前/后、非 ST 对照、创业科创风险警示、进出警示月、vs G/H/A）。  
- 自检布尔：X2 主板 ST 是否切 2026-07-06；创业/科创风险警示是否仍 20%；是否未复权；是否未用核对日 ST 名单；是否未与 A/F/G/H/W/费用层混主结论；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把永远 5%/永远 10% 当诚实板上区间；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 V/W/U/A 已冻结正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：涨跌停按交易日 × 板块 × 是否风险警示取当时限制；主板 ST/*ST 以 **2026-07-06** 为界（前 5%、后 10%）；创业板/科创板风险警示维持 20%，不要合成「全市场 ST 都 10%」。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 W，本页**新增实验 X** 收成标准件，**不改口径主线**，**不改假设 A–W 正文**。与实验 G 分工：**G 主测新股/无板窗（ST 仅作 G0 泄露臂附带）；X 主测主板 ST 5%→10% 切日与创业/科创误套 10%**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权行情 + 按日风险警示 + 板块即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2022-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-09；**fill_time=next_open 写死**；**st_limit_cut_date=2026-07-06 / pre=0.05 / post=0.10 / chinext_star=0.20 写死**；diff_buckets 八桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死冻结**；**x0_primary_demo=flat_5pct 写死（禁双挂）** |

---

## 变更

- 2026-11-02：新建标准件（总管线：V 补丁/W 预检并行写 X；清单止于 W → 自开跑前检查 + `事实与坑` 主板 ST 5%→10% 坑选题，**与 A–W 不撞主结论**；近邻 G=新股/无板窗（ST 仅附带）、H=整理期、W=除权复权，本页主测主板 ST 切日+创业科创误套；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 V/W/U/A 正文**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设X-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写入具体数并冻结（预检禁 holdout 标定且建议 0.02/0.01/0.05/0.015；与同系列 R/S/T/U/V/W 纸面占位一致；禁 null）；② `params.x0_primary_demo=flat_5pct`（主报永远 5%；禁与 flat_10pct / copy_10_to_chinext_star 双挂争主表）。**不抢实验 A**；**X 不开回测**；未动 Y/W/V/U/A。
