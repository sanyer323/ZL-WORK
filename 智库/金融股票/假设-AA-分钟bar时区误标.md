# 假设 AA · 分钟 bar 时区 / 标签误标连续窗（执行鸿沟）

更新：2026-11-02  
来源：总管线 / Y·Z 补丁链暂齐后并行写下一纸面 AA；清单原止于 Z，无 AA 节 → 自立实验 AA；选题自总管候选「分钟 bar 对齐/时区」+ `事实与坑` 竞价时段（9:15–9:25 开盘集合 / 9:30–11:30·13:00–14:57 连续 / 14:57–15:00 收盘集合）+ 假设 Y 禁止项「用 UTC 分钟把午休并进连续」与已冻 `minute_bar_tz=Asia/Shanghai`·`minute_bar_label=bar_end`（Y 将其作诚实加总输入，不主测时区错位本身）；**新建实验 AA**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「UTC 分钟 / bar_start 反标」当诚实会话加总；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z 及其他 A/D–Z 已交正文与冻结补丁**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 Z，本页自立实验 AA 标准件。与假设 Y（集合竞价量计入日线假连续分母）**分列**：Y 在**已诚实时区/标签**前提下主测「日总量含集合 vs 仅连续量」；本页**主测**把分钟线用 **UTC（或非 Asia/Shanghai）**、或 **bar_start / bar_end 反标**，从而把 **11:30–13:00 午休并进连续**、或把开盘/收盘集合量窗错位。**盘后通道属 M；大宗属 O；收盘价产生方式属 N；板上可成交属 A。本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AA** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AA / 假设-AA / hypothesis_id=AA / 组 AA0·AA1·AA2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AA 与 params 键名 `aa0_*` 以外的单字母实验页混读。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1、同一未复权价、同一「仅连续量当分母」诚实规则下，用 **UTC（或非 Asia/Shanghai）分钟线**、或把分钟 bar 的 **右端点/左端点标签反标（bar_start 当 bar_end 或反之）** 去加总会话量，相对「**`minute_bar_tz=Asia/Shanghai` + `minute_bar_label=bar_end`**，严格按 09:15–09:25 / 09:30–11:30·13:00–14:57 / 14:57–15:00 分桶」的 PIT 诚实组，会**系统性把午休并进连续窗、或把开盘/收盘集合量错划进连续**，从而**改写连续可冲击流动性与会话腿归属**；差异应**集中在「UTC 错位 / 标签反标 / 高午休边界成交」桶**，而不是随机散开。

证伪方向：若天真组 / 泄露组相对诚实组的连续量差、κ 触顶差、会话错桶率在标定噪声带内可忽略，且「UTC 错位 / bar 标签反标 / 午休边界放量 / 对照正确 Asia/Shanghai·bar_end」分桶不改变结论（差异不集中在时区·标签相关桶），则本假设在该样本与分钟设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 会话窗按 Asia/Shanghai；分钟 bar 标签写死；UTC 错位 = 假连续

```
# 配置写死键（见 §7；待预检键见文末；拉数前冻结；禁 holdout 反调）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AA
# params.asof_check_date                 写死默认 2026-10-19  # 与 Y/N/M 同批「竞价时段+盘后计入日总量」核对锚；本页不重开收盘价定义
# params.fill_time                        写死 next_open      # 成交腿与 A/D/Y 对齐；本页主测分钟对齐，不抢 A 板上真数
# params.session_tz_honest               写死 Asia/Shanghai  # 诚实组唯一合法时区
# params.minute_bar_label_honest         写死 bar_end        # 诚实组：分钟 bar 右端点归属该窗（与 Y 冻结同向；本页主测其被反标的后果）
# params.open_auction_window             写死 09:15-09:25
# params.continuous_windows              写死 [09:30-11:30,13:00-14:57]
# params.close_auction_window            写死 14:57-15:00
# params.lunch_gap                       写死 11:30-13:00    # 午休；诚实组不得并进连续
# params.aa0_primary_demo                键名稳值待预检     # 建议 utc_tz_as_local；单一主报；禁与 bar_start_flip 双挂
# params.aa0_wrong_tz                    写死 UTC            # 天真主路径时区（当 UTC 墙钟当上海墙钟）
# params.aa1_label_flip                  写死 bar_start      # 半泄露/诊断：标签反标（诚实为 bar_end）
# params.aa2_tz                          写死 Asia/Shanghai
# params.aa2_label                       写死 bar_end
# params.merge_with_Y_vol_denominators   写死 False          # 集合量分母另页 Y；本页默认输入「Y2 仅连续」规则为对照声明
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_N_close              写死 False
# params.merge_with_A_fill               写死 False
# params.missing_minute_policy           写死 skip           # 无分钟线 → skip 本页主测腿（不静默退回日总量）
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  键名稳值待预检     # 建议 0.02/0.01/0.05/0.015；params.Y≠实验字母 AA；禁 null/holdout 标定
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-19"
session_tz_honest = "Asia/Shanghai"
minute_bar_label_honest = "bar_end"
open_auction_window = ("09:15", "09:25")
continuous_windows = [("09:30", "11:30"), ("13:00", "14:57")]
close_auction_window = ("14:57", "15:00")
lunch_gap = ("11:30", "13:00")
merge_with_Y_vol_denominators = False
merge_with_M_aft = False
merge_with_O_block = False
merge_with_N_close = False
merge_with_A_fill = False
missing_minute_policy = "skip"

def wall_clock_in_tz(ts_utc, tz_name):
    """把时间戳投到指定时区墙钟；本页禁把 UTC 墙钟直接当上海会话钟。"""
    ...

def bar_belongs_to(ts, label, window_start, window_end):
    """label=bar_end：右端点落入 [start,end) 则归属；label=bar_start：左端点。"""
    ...

def session_bucket(ts, tz_name, label):
    local = wall_clock_in_tz(ts, tz_name)
    if bar_belongs_to(local, label, *open_auction_window):
        return "open_call"
    if any(bar_belongs_to(local, label, *w) for w in continuous_windows):
        return "continuous"
    if bar_belongs_to(local, label, *close_auction_window):
        return "close_call"
    if bar_belongs_to(local, label, *lunch_gap):
        return "lunch_gap"  # 诚实组不得并进 continuous
    return "other"

def continuous_volume(group, bars):
    if group == "AA0":
        # 天真：UTC 墙钟当会话钟（或 aa0_primary_demo 写死的单一主报）
        tz, label = "UTC", minute_bar_label_honest
    elif group == "AA1":
        # 标签反标：时区诚实，label=bar_start
        tz, label = session_tz_honest, "bar_start"
    else:
        # AA2 PIT
        tz, label = session_tz_honest, minute_bar_label_honest
    vol = 0.0
    for b in bars:
        if session_bucket(b.ts, tz, label) == "continuous":
            vol += b.volume
    return vol
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：无可用分钟线却硬标 AA2、把 Y 集合分母主结论 / M 盘后 / O 大宗 / N 收盘机制混进本页主表、用 UTC 却标 AA2 诚实、把午休成交静默并进连续却不报错桶 → **跳过该日该券分钟对齐腿**，不静默用日总量填假连续。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AA）

| 组 | 时区 / 标签 | 说明 |
|----|-------------|------|
| AA0 天真 | UTC（或 `aa0_primary_demo` 单一主报）+ 诚实 label | 把 UTC 墙钟当上海会话钟 → 午休/集合窗错位 |
| AA1 标签反标 | Asia/Shanghai + bar_start | 时区对、归属端点反 → 边界 bar 错桶 |
| AA2 PIT 诚实 | Asia/Shanghai + bar_end | 与 Y 冻结输入同向；本页只验其对齐本身 |

同一信号、同一 T+1、同一股票宇宙。本页**主测时区/标签对齐**，不主测集合量是否应进分母（见 Y）、不主测盘后通道（见 M）。**`params.fill_time=next_open` 写死**。分母规则默认叠加 **Y2 仅连续** 为对照声明，**`merge_with_Y_vol_denominators=False`**（不重开集合分母实验）。

**`params.merge_with_Y_vol_denominators=False` / `merge_with_M_aft=False` / `merge_with_O_block=False` / `merge_with_N_close=False` / `merge_with_A_fill=False`（写死）**。

**待预检（键名稳；值建议如下；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                 # 连续量/κ差显著门槛；≠实验字母 AA
params.G                            = 0.01                 # 错桶/午休边界桶相对对照差门槛
params.N                            = 0.05                 # 失败/跳过率差门槛
params.Y2                           = 0.015                # AA1（标签反标）相对 AA2 专项门槛
params.aa0_primary_demo             = utc_tz_as_local      # 主报 UTC 当本地；禁与 bar_start_flip 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股日频/分钟可复原会话量的股票为主；ETF 可进诊断桶但不改主结论。不含可转债主样本（见 Q）。  
- **排除（默认）**：无分钟线且 `missing_minute_policy=skip`；把 Y/M/O/N/A 主结论并进本页主表；用复权价。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2018-01-01`  
  - `params.date_end=2026-09-30`  
  - **覆盖沪市股票收盘集合 2018-08-20 切日前后**（与 Y 同向，便于对照声明；本页不重开量窗切日本体）。  
- **PIT 切片原则**：会话归属按 **Asia/Shanghai 墙钟 + bar_end**；**禁止**用 UTC 墙钟回放 A 股竞价窗。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2018-01-01
params.oos_split.is_end         = 2023-12-31
params.oos_split.holdout_start  = 2024-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调时区、标签枚举、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AA0 ? AA2**：UTC 错位相对 PIT——被并进连续的午休量 / 错划的集合量。  
2. **AA1 ? AA2**：bar_start 反标相对 PIT——边界 bar 错桶。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "utc_misalign",               # UTC 墙钟错位
  "label_flip_bar_start",       # 标签反标
  "lunch_boundary",             # 11:30 / 13:00 边界放量
  "open_call_spill",            # 开盘集合量被划进连续
  "close_call_spill",           # 收盘集合量被划进连续
  "vs_Y_continuous_only",       # 对照声明：分母规则另页 Y
  "vs_M_aft",                   # 对照声明：盘后另页 M
  "vs_O_block",                 # 对照声明：大宗另页 O
  "vs_N_close",                 # 对照声明：收盘机制另页 N
  "vs_A_fill",                  # 对照声明：板上可成交另页 A
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 连续量差 ΔContVol（AA0/AA1 相对 AA2）；  
2. κ/冲击触顶差 ΔKappa；  
3. 会话错桶率差 ΔMisbucket；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔContVol| 或 |ΔKappa| **≥ params.Y** 或 |ΔMisbucket| **≥ params.G** 或 |ΔContVol_(AA1−AA2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「分钟 bar 时区/标签误标连续窗鸿沟显著」。

**params.Y / G / N / Y2（拉数前写入；禁 holdout 标定；与实验字母 AA 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 连续量/κ差显著门槛（≠实验字母 AA） | **键名稳；值待预检**（建议 `0.02`） |
| params.G | 错桶/午休边界桶相对对照差门槛 | **键名稳；值待预检**（建议 `0.01`） |
| params.N | 失败笔数率差门槛 | **键名稳；值待预检**（建议 `0.05`） |
| params.Y2 | AA1 标签反标专项门槛 | **键名稳；值待预检**（建议 `0.015`） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| session_tz_honest | 诚实时区 | **写死** `Asia/Shanghai` |
| minute_bar_label_honest | 诚实标签 | **写死** `bar_end` |
| aa0_primary_demo | 天真主报枚举 | **键名稳；值待预检**（建议 `utc_tz_as_local`；禁双挂） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**失败/不显著**：差异落在噪声带内或均匀散在非时区·标签对照桶——结论栏写明，不得改口称「时区差不多」或「这类票更能买」。

结论栏：空。跑完只写「该假设下连续量/错桶差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验分钟对齐诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（PIT 时区/标签、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用 UTC 却标 AA2 诚实**。  
2. **把 bar_start 当诚实标签却不写 `aa1` 诊断组**。  
3. **无分钟线却静默退回日总量并声称验了时区**。  
4. **把 Y 集合分母、M 盘后、O 大宗、N 收盘、A 板上重开混进本页主结论**。  
5. **用复权价**。  
6. **宇宙泄露 / holdout 反调**：看完 OOS 再改时区枚举或 **`params.Y` 等门槛**。  
7. **差异不集中在时区·标签桶却仍写「系统性对齐鸿沟」而不改表述**。  
8. **把差异写成「这类票能买」或选股公式**。  
9. **把实验字母 AA 与 `params.Y` 混改**；或改写 Y 已冻 `minute_bar_tz` / `minute_bar_label` 正文。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股为主 |
| minute_ts（带时区或可还原 UTC） | 对齐 | 缺 → skip |
| minute_volume（未复权） | 加总 | 禁复权量 |
| exchange (SSE/SZSE) | 分桶 | 北交所默认另桶 |
| session 分列日量（可选） | 对照 | 有则与分钟加总交叉核 |

**明确**：不依赖聚宽；**不要求新开 Level-2 盘口**——有 Asia/Shanghai 可还原的分钟量即可起步；缺分钟 → `missing_minute_policy=skip`。主窗自 2018-01-01，覆盖 2018-08-20 前后。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=AA`（**实验字母**），`groups=[AA0,AA1,AA2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-19`**，**`params.fill_time=next_open`（写死）**，**`params.session_tz_honest=Asia/Shanghai`**，**`params.minute_bar_label_honest=bar_end`**，**`params.open_auction_window=09:15-09:25`**，**`params.continuous_windows=[09:30-11:30,13:00-14:57]`**，**`params.close_auction_window=14:57-15:00`**，**`params.lunch_gap=11:30-13:00`**，**`params.merge_with_Y_vol_denominators=False`**，**`params.merge_with_M_aft=False`**，**`params.merge_with_O_block=False`**，**`params.merge_with_N_close=False`**，**`params.merge_with_A_fill=False`**，**`params.missing_minute_policy=skip`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y` / `G` / `N` / `Y2`（键名稳值待预检；建议 0.02/0.01/0.05/0.015；禁 holdout 标定；禁 null；params.Y≠实验字母 AA）**，**`params.aa0_primary_demo`（键名稳值待预检；建议 utc_tz_as_local；禁双挂）**，`universe_rule`，**`params.date_start=2018-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2018-01-01,is_end=2023-12-31,holdout_start=2024-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_Y=off`，`overlay_M=off`，`overlay_A=off`。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AA0/AA1/AA2 连续量、ΔContVol、ΔKappa、ΔMisbucket、失败笔数；分桶（UTC 错位 / 标签反标 / 午休边界 / 开收盘溢出 / vs Y·M·O·N·A）。  
- 自检布尔：AA2 是否 Asia/Shanghai+bar_end；AA0 是否 UTC 主报；AA1 是否仅标签反标；是否未与 Y/M/O/N/A 混主结论；holdout 是否未反调；**是否未把实验字母 AA 与 params.Y 混用**；**是否未改 Y 冻结补丁正文**。  
- **禁止输出**：具体买卖标的列表当「建议」；把 UTC 当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z 及其他 A/D–Z 已交正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：A 股竞价时段按交易所规则墙钟（Asia/Shanghai）；午休 11:30–13:00 不属连续竞价；开盘/收盘集合与连续分列。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 Z，本页**新增实验 AA** 收成标准件，**不改口径主线**，**不改假设 A–Z 正文**。与实验 Y 分工：**Y=在诚实时区/标签下测集合量是否应进连续分母；AA=测时区/标签本身被写错时的错桶与假连续**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；可还原 Asia/Shanghai 的分钟量即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2018-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**session_tz_honest=Asia/Shanghai / minute_bar_label_honest=bar_end 写死**；diff_buckets 十桶写死冻结；**Y/G/N/Y2 与 aa0_primary_demo 键名稳值待预检**（params.Y≠实验字母 AA） |

---

## 变更

- 2026-11-02：新建标准件（总管线：并行写下一纸面 AA；Y/Z 补丁已交不改；清单止于 Z → 自候选「分钟 bar 对齐/时区」+ `事实与坑` 竞价时段 + Y「禁 UTC 并午休」选题，**与 A/D–Z 不撞主结论**；近邻 Y=集合分母、M=盘后通道、N=收盘机制，本页主测时区/标签误标；**实验字母 AA ≠ params.Y**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/A/D–X 正文**）。

### 待预检键（交总管入库预检）

| 键 | 建议值 | 备注 |
|----|--------|------|
| params.Y | 0.02 | 相对门槛；**≠实验字母 AA**；禁 null/holdout |
| params.G | 0.01 | 错桶/午休边界桶 |
| params.N | 0.05 | 失败/跳过率差 |
| params.Y2 | 0.015 | AA1−AA2 专项 |
| params.aa0_primary_demo | utc_tz_as_local | 单一主报；禁与 bar_start_flip 双挂 |
