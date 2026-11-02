# 假设 Y · 集合竞价量计入日线假连续流动性（执行鸿沟）

更新：2026-11-02  
来源：总管线 / R·S·T 补丁链齐、U–X 并行推进后写下一纸面 Y；清单原止于 X，选题自开跑前检查优先项「集合竞价量计入日线」+ `事实与坑`「9:15–9:25 开盘集合 / 9:30–11:30·13:00–14:57 连续 / 14:57–15:00 收盘集合；盘后成交计入当日总量，用日成交量估冲击时要知道含盘后」+ `口径`「大宗/盘后不是竞价可冲击」邻接层；**新建实验 Y**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「日总量=连续竞价可冲击量」当诚实流动性分母；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 W/X/V/U/A 及已交补丁正文**）

> **字母消歧（硬）**：本页**实验字母 Y** ≠ 费用/显著性参数 **`params.Y`**。全文凡写「实验 Y / 假设-Y / hypothesis_id=Y / 组 Y0·Y1·Y2」均指本实验；凡写 **`params.Y`** 均指相对门槛（与 G/N/Y2 同族），**禁止**把二者混读或互改。

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 开跑前检查对齐；清单原无 Y 节，本页自立实验 Y 标准件。与假设 O（大宗量价并进「竞价」日量）、假设 M（盘后固定价格通道）、假设 N（收盘价产生方式 / 假 GTC）**分列**：本页**主测**把**开盘/收盘集合竞价成交量**（以及未拆的盘后量）并进「连续竞价可冲击 / κ 分母 / 日频换手」——发明假连续流动性。**O 的 auction_only_ex_block = 竞价匹配剔大宗，仍可含集合竞价量，不是本页诚实组。** 板上可成交属 A；收盘机制属 N；盘后通道属 M；大宗属 O。本页主结论不混。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1、同一未复权价下，用**日成交量总量**（含开盘集合 + 收盘集合，并可再吞盘后/大宗）当连续竞价腿的冲击/κ/换手分母，相对「连续腿只用**连续竞价成交量**；开盘集合 / 收盘集合 / 盘后 / 大宗分列，且沪市股票收盘集合量窗按 **2018-08-20**、沪市基金按 **2026-07-06** 切片」的 PIT 诚实组，会**系统性高估连续时段可冲击流动性**；差异应**集中在高集合占比日**（开盘竞价放量、尾盘集合放量、涨跌停附近）、以及「沪市股票 <2018-08-20 仍发明收盘集合量桶」桶，而不是随机散开。

证伪方向：若天真组 / 泄露组相对诚实组的换手差、冲击差、κ 触顶率差在标定噪声带内可忽略，且「高开盘集合占比 / 高收盘集合占比 / 沪市股票切日前 / 对照低集合占比日」分桶不改变结论（差异不集中在集合相关桶），则本假设在该样本与分母设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 日总量 ≠ 连续可冲击量；集合 / 连续 / 盘后 / 大宗分列；收盘集合量窗 PIT

```
# 配置写死键（见 §7；风控补丁三条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 Y
# params.asof_check_date                 写死默认 2026-10-19  # 与 N/M 同批「收盘机制+盘后计入日总量」核对锚；本页不重开收盘价定义
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；本页主测流动性分母，不抢 A 板上真数
# params.sh_stock_close_auction_start    写死 2018-08-20     # 沪市股票收盘集合量窗起点（与 N 同切日；本页只切「量桶」）
# params.sh_fund_close_auction_start     写死 2026-07-06     # 沪市基金（含 ETF）收盘集合量窗
# params.sz_stock_close_auction_start    写死 None           # leave_unsliced；深市股票收盘集合更早切日未核死 → 不写死首日
# params.open_auction_window             写死 09:15-09:25    # 开盘集合；量进 open_call 桶
# params.continuous_windows              写死 [09:30-11:30,13:00-14:57]  # 连续；诚实连续分母
# params.close_auction_window            写死 14:57-15:00    # 收盘集合；量进 close_call 桶（PIT 见上切日）
# params.y0_vol_basis                    写死 day_total      # 天真：日总量当连续可冲击分母
# params.y1_vol_basis                    写死 matching_incl_call  # 半泄露：剔大宗后的「竞价匹配量」仍含集合（≈O 的 auction_only 层）
# params.y2_vol_basis                    写死 continuous_only  # PIT：仅连续窗成交量
# params.exclude_block_from_all          写死 True           # 各组估连续冲击前先剔大宗（大宗另页 O）；禁把 O0 假大宗流动性混进本页主表
# params.exclude_aft_from_continuous     写死 True           # 诚实组：盘后量不进连续分母（盘后另页 M）
# params.y0_swallow_aft                  写死 True           # 天真可吞盘后量进「日总量」分母（暴露含盘后估冲击）
# params.y0_swallow_block                写死 False          # 默认不在本页重演 O0；若 True 须进诊断桶且 merge_with_O 仍 False
# params.kappa                           写死 0.01           # 参与率上限示意；与 M 同量级；拉数前可冻结改值但禁 holdout 反调
# params.kappa_cap_round                 写死 floor
# params.vol_session_source              写死 vendor_session_fields_or_minute_sum  # 优先分列字段；否则分钟加总；禁门槛反推
# params.missing_session_vol_policy      写死 skip           # 缺开盘/收盘/连续分列且无分钟可加总 → skip 该腿
# params.minute_bar_tz                   写死 Asia/Shanghai  # 分钟加总时区；禁 UTC 错位把午休并进连续
# params.minute_bar_label                写死 bar_end        # 风控补丁冻结；分钟 bar 右端点；与 minute_bar_tz=Asia/Shanghai 配套
# params.merge_with_O_block              写死 False          # 大宗假流动性另页 O
# params.merge_with_M_aft                写死 False          # 盘后通道另页 M
# params.merge_with_N_close_mech         写死 False          # 收盘价产生方式另页 N；本页只切量桶
# params.merge_with_A_fill               写死 False
# params.merge_with_L_mkt                写死 False          # 市价通道另页 L（市价本就只走连续）
# params.merge_with_S_T_U_V_fee          写死 False
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=费用/冲击相对门槛键 ≠ 实验字母 Y；禁 holdout 标定；禁 null
# params.y0_primary_demo                 写死 day_total_as_continuous  # 风控补丁冻结；主报日总量当连续；禁与 matching_incl_call / swallow_aft 双挂
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改分母枚举、切日、κ、params.Y/G/N/Y2、主窗/oos、y0_primary_demo、minute_bar_label

fill_time = "next_open"
asof_check_date = "2026-10-19"
sh_stock_close_auction_start = "2018-08-20"
sh_fund_close_auction_start = "2026-07-06"
sz_stock_close_auction_start = None  # leave_unsliced
y0_vol_basis = "day_total"
y1_vol_basis = "matching_incl_call"
y2_vol_basis = "continuous_only"
exclude_block_from_all = True
exclude_aft_from_continuous = True
y0_swallow_aft = True
y0_swallow_block = False
kappa = 0.01
kappa_cap_round = "floor"
vol_session_source = "vendor_session_fields_or_minute_sum"
missing_session_vol_policy = "skip"
minute_bar_tz = "Asia/Shanghai"
minute_bar_label = "bar_end"  # 风控补丁冻结；分钟 bar 右端点
Y = 0.02   # params.Y：换手/冲击差门槛；≠实验字母 Y
G = 0.01
N = 0.05
Y2 = 0.015
y0_primary_demo = "day_total_as_continuous"  # 单一主报；禁双挂
merge_with_O_block = False
merge_with_M_aft = False
merge_with_N_close_mech = False
merge_with_A_fill = False
merge_with_L_mkt = False
merge_with_S_T_U_V_fee = False

def has_close_call_bucket(row):
    """PIT：该日该券是否存在收盘集合量桶（只切量，不定义收盘价）。"""
    board_like = row.get("sec_type")  # stock / fund_etf
    exch = row.get("exchange")  # SSE / SZSE
    d = row["trade_date"]
    if exch == "SSE" and board_like == "stock":
        return d >= sh_stock_close_auction_start
    if exch == "SSE" and board_like in ("fund", "etf", "fund_etf"):
        return d >= sh_fund_close_auction_start
    if exch == "SZSE":
        # 深市股票收盘集合更早切日未核死 → leave_unsliced：有分列字段则用，无则 skip 收盘集合差分诊断
        return True if row.get("vol_close_call") is not None else None
    return None

def split_volumes(row):
    """返回 open_call, continuous, close_call, aft, block；缺关键分列且无法分钟加总 → None（上层 skip）。"""
    block = float(row.get("vol_block") or 0.0)
    aft = float(row.get("vol_aft") or 0.0)
    open_c = row.get("vol_open_call")
    close_c = row.get("vol_close_call")
    cont = row.get("vol_continuous")
    day = row.get("vol_day_total")
    if cont is None or open_c is None or close_c is None:
        # 允许分钟加总回填（须 minute_bar_tz=Asia/Shanghai）
        if row.get("vols_from_minute") is True:
            open_c = row["vol_open_call"]
            close_c = row["vol_close_call"]
            cont = row["vol_continuous"]
        else:
            return None
    # 无收盘集合量窗的历史日：close_call 应记 0，不得把尾盘连续量标成集合
    hc = has_close_call_bucket(row)
    if hc is False:
        close_c = 0.0
    if hc is None and close_c is None:
        return None
    return {
        "open_call": float(open_c or 0.0),
        "continuous": float(cont or 0.0),
        "close_call": float(close_c or 0.0),
        "aft": aft,
        "block": block,
        "day_total": float(day) if day is not None else None,
    }

def continuous_basis(group, parts, row):
    if parts is None:
        return None
    cont = parts["continuous"]
    matching = cont + parts["open_call"] + parts["close_call"]  # 竞价匹配（可含集合），尚未加大宗/盘后
    if exclude_block_from_all:
        # 大宗一律不进本页连续分母主路径
        pass
    if group == "Y0":
        # 天真：日总量（默认可吞盘后；默认不吞大宗）
        if parts["day_total"] is not None:
            v = parts["day_total"]
            if not y0_swallow_block:
                v = max(v - parts["block"], 0.0)
            if not y0_swallow_aft:
                v = max(v - parts["aft"], 0.0)
            return v
        # 无日总量字段时退化：匹配量 + 可选盘后
        v = matching
        if y0_swallow_aft:
            v += parts["aft"]
        return v
    if group == "Y1":
        # 半泄露：剔大宗后的匹配量（含集合）当连续分母 —— 对齐「O 层 auction_only」仍假连续
        return matching
    # Y2 PIT
    return cont

def kappa_cap(basis, kappa=0.01):
    if basis is None:
        return None
    import math
    raw = basis * kappa
    if kappa_cap_round == "floor":
        return math.floor(raw)
    return raw
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺日量/会话分列且无法按 `Asia/Shanghai` 分钟加总、把大宗假流动性（O）/盘后通道主测（M）/收盘价机制（N）混进本页主结论、用 UTC 分钟把午休并进连续、在沪市股票 `<2018-08-20` 发明收盘集合量并标 Y2 → **跳过该日该券连续流动性腿**，不静默用日总量填假连续分母。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 Y）

| 组 | 连续腿流动性分母 | 说明 |
|----|------------------|------|
| Y0 天真-日总量 | `day_total`（默认可含盘后；默认剔大宗） | 「日线量就能打连续冲击」 |
| Y1 半泄露-匹配含集合 | `open_call+continuous+close_call` | 对齐 O 层「竞价剔大宗」仍含集合 |
| Y2 PIT 诚实 | **仅 `continuous`** | 集合/盘后/大宗分列；收盘集合量窗按切日 |

同一信号、同一 T+1、同一股票宇宙。本页**主测分母/κ/换手差**，不主测板上撮合（见 A）、不主测收盘价怎么来（见 N）、不主测盘后能否补成（见 M）、不主测大宗价腿（见 O）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_O_block=False` / `merge_with_M_aft=False` / `merge_with_N_close_mech=False` / `merge_with_A_fill=False` / `merge_with_L_mkt=False` / `merge_with_S_T_U_V_fee=False`（写死）**。

**风控补丁三条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

> **消歧**：`params.Y` 是费用/冲击**相对门槛键**（与 G/N/Y2 同族），**不是**实验字母「假设 Y / hypothesis_id=Y」。

```
params.Y                            = 0.02                # 换手/冲击差显著门槛 ≥ 2pp（全样本或高集合占比桶）；≠实验字母 Y
params.G                            = 0.01                # 高集合占比桶相对低集合对照的差门槛 ≥ 1pp（ΔTO_call）
params.N                            = 0.05                # 失败/跳过率差门槛 ≥ 5pp
params.Y2                           = 0.015               # Y1（含集合匹配）相对 Y2 专项门槛 ≥ 1.5pp（ΔTO_(Y1−Y2)）
params.y0_primary_demo              = day_total_as_continuous  # 主报日总量当连续；枚举另有 matching_incl_call / swallow_aft；禁双挂争主表
params.minute_bar_label             = bar_end             # 分钟 bar 右端点；与 minute_bar_tz=Asia/Shanghai 配套；无分钟加总路径时本键不生效但仍冻结
params.vol_session_source           = vendor_session_fields_or_minute_sum  # 已写死；改枚举须冻结
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股股票为主；可另桶 ETF/基金（须用 `sh_fund_close_auction_start`）。不含可转债主样本（可转债收盘机制另见 Q）。  
- **排除（默认）**：缺 `vol_day_total` 且无会话分列/分钟可加总；停牌全日无成交；把实验 O/M/N 主结论并进本页主表。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2018-01-01`  
  - `params.date_end=2026-09-30`  
  - **必须跨过 2018-08-20**（沪市股票收盘集合量窗）；建议覆盖足量「开盘集合放量 / 尾盘集合放量」日。  
- **PIT 切片原则**：是否存在收盘集合**量桶**按成交日已生效文本；**禁止**用核对日现行时段回放沪市股票切日前。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2018-01-01
params.oos_split.is_end         = 2023-12-31
params.oos_split.holdout_start  = 2024-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调分母枚举、κ、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **Y0 − Y2**：日总量分母相对仅连续——被集合（及可选盘后）灌胖的连续可冲击量。  
2. **Y1 − Y2**：匹配含集合相对仅连续——证明「剔大宗后的竞价量」仍不是连续可冲击量。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "high_open_call_share",       # 开盘集合量/日量高占比
  "high_close_call_share",      # 收盘集合量/日量高占比
  "low_call_share_control",     # 低集合占比对照；差异应更小
  "sse_stock_pre_20180820",     # 沪市股票收盘集合量窗切日前（Y0/Y1 发明集合桶）
  "sse_stock_post_20180820",    # 切日后
  "limit_near_day",             # 近涨跌停日（集合占比常抬升）
  "vs_O_block",                 # 对照声明：大宗另页 O
  "vs_M_aft",                   # 对照声明：盘后另页 M
  "vs_N_close_mech",            # 对照声明：收盘价机制另页 N
  "vs_A_fill",                  # 对照声明：板上可成交另页 A
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 换手差 ΔTO（Y0/Y1 相对 Y2；连续腿）；  
2. 冲击/κ 触顶率差 ΔImpact / ΔκHit；  
3. 高集合占比桶相对低集合对照的差 ΔTO_call；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔTO| 或 |ΔImpact| **≥ params.Y** 或 |ΔTO_call| **≥ params.G** 或 |ΔTO_(Y1−Y2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「集合竞价量计入日线假连续流动性执行鸿沟显著」。

**params.Y / G / N / Y2（拉数前写入；禁 holdout 标定；与实验字母 Y 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 换手/冲击差显著门槛（≠实验字母 Y） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 高集合桶相对对照差门槛 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败笔数率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | Y1 含集合匹配专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| sh_stock_close_auction_start | 沪市股票收盘集合量窗 | **写死** `2018-08-20` |
| sh_fund_close_auction_start | 沪市基金收盘集合量窗 | **写死** `2026-07-06` |
| y2_vol_basis | 诚实分母 | **写死** `continuous_only` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已写入 params 并冻结（风控补丁 2026-11-02；**`params.Y`≠实验字母 Y**）；**禁止用 holdout / OOS 段标定或反调**。

**失败/不显著**：差异落在噪声带内或均匀散在低集合对照桶——结论栏写明，不得改口称「日量当连续分母差不多」或「这类票更能打」。

结论栏：空。跑完只写「该假设下分母差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验集合/连续量分母诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（会话分列、PIT 量窗、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做；若沿用流动性≤前日量 5% 类红线，分母须与 Y2 同向用**连续量**（或显式声明另键），**禁止**用日总量当分母却标诚实。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用日总量当连续可冲击分母却标 Y2 诚实**。  
2. **把 O 的 auction_only_ex_block（匹配剔大宗、仍含集合）写成 Y2**。  
3. **沪市股票 <2018-08-20 发明收盘集合量桶并标 PIT**。  
4. **把盘后量（M）或大宗量（O）并进连续分母却不标注、并进主结论**。  
5. **用 UTC / 错时区分钟线把 11:30–13:00 午休并进连续量**。  
6. **把收盘价产生方式（N）、市价通道（L）、板上可成交（A）、费用四层（S/T/U/V）重开混进本页主结论**。  
7. **宇宙泄露 / holdout 反调**：看完 OOS 再改分母枚举或 **`params.Y` 等门槛**。  
8. **差异不集中在高集合占比 / 切日桶却仍写「系统性假连续流动性」而不改表述**。  
9. **把差异写成「这类票能买」或选股公式**。  
10. **把实验字母 Y 与 `params.Y` 混改**（改门槛却动实验编号，或反之）。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股股票为主 |
| exchange (SSE/SZSE) | 切日 | 北交所默认另桶/不进主跑 |
| sec_type (stock/fund_etf) | 沪市基金切日 | 缺 → 按 stock 或 skip |
| vol_day_total | Y0 分母 | 未复权成交量 |
| vol_open_call / vol_continuous / vol_close_call | Y1/Y2 | **优先供应商会话分列** |
| vol_block（可选） | 剔大宗 | 与 O 衔接；缺则按 0 并声明 |
| vol_aft（可选） | 盘后量 | 与 M 衔接；Y0 可吞；Y2 不进连续 |
| minute bars（可选） | 无分列时加总 | **`minute_bar_tz=Asia/Shanghai`**；按窗加总 09:15–09:25 / 连续窗 / 14:57–15:00 |
| raw OHLC（未复权，可选） | 近板日分桶 | 禁复权判板 |
| is_limit_near（可选） | 分桶 | 可有则报 |

**明确**：不依赖聚宽；**不要求新开 Level-2**——有会话分列日量即可起步；否则用分钟加总（时区写死）起步；两者皆无 → `missing_session_vol_policy=skip`，不声称精确连续冲击复盘。主窗自 2018-01-01，必须跨 2018-08-20。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=Y`（**实验字母**），`groups=[Y0,Y1,Y2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-19`**，**`params.fill_time=next_open`（写死）**，**`params.sh_stock_close_auction_start=2018-08-20`**，**`params.sh_fund_close_auction_start=2026-07-06`**，**`params.sz_stock_close_auction_start=None(leave_unsliced)`**，**`params.y0_vol_basis=day_total`**，**`params.y1_vol_basis=matching_incl_call`**，**`params.y2_vol_basis=continuous_only`**，**`params.exclude_block_from_all=True`**，**`params.exclude_aft_from_continuous=True`**，**`params.y0_swallow_aft=True`**，**`params.y0_swallow_block=False`**，**`params.kappa=0.01`**，**`params.kappa_cap_round=floor`**，**`params.vol_session_source=vendor_session_fields_or_minute_sum`**，**`params.missing_session_vol_policy=skip`**，**`params.minute_bar_tz=Asia/Shanghai`**，**`params.merge_with_O_block=False`**，**`params.merge_with_M_aft=False`**，**`params.merge_with_N_close_mech=False`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_L_mkt=False`**，**`params.merge_with_S_T_U_V_fee=False`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015`（写死冻结；禁 holdout 标定；禁 null；params.Y≠实验字母 Y）**，**`params.y0_primary_demo=day_total_as_continuous`（写死；禁双挂）**，**`params.minute_bar_label=bar_end`（写死冻结）**，`universe_rule`，**`params.date_start=2018-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2018-01-01,is_end=2023-12-31,holdout_start=2024-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_O=off`，`overlay_M=off`，`overlay_N=off`，`overlay_A=off`，`overlay_L=off`。  
- 行情与分量：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- Y0/Y1/Y2 连续腿换手、冲击/κ 触顶、ΔTO、ΔImpact、Y1 专项、失败笔数；分桶（高开盘集合/高收盘集合/低集合对照/沪市切日前售后、近板、vs O/M/N/A）。  
- 自检布尔：Y2 是否仅连续量；Y0 是否日总量；Y1 是否仍含集合；沪市股票切日前是否未发明收盘集合量；是否未与 O/M/N/A 混主结论；holdout 是否未反调；**是否未把实验字母 Y 与 params.Y 混用**。  
- **禁止输出**：具体买卖标的列表当「建议」；把日总量当诚实连续分母；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 W/X/V/U/A 已冻结正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：开盘集合 / 连续 / 收盘集合分时段；盘后与大宗成交计入日总量时，用日量估冲击必须知道成分；沪市股票收盘集合自 **2018-08-20**、沪市基金自 **2026-07-06**。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 X，本页**新增实验 Y** 收成标准件，**不改口径主线**，**不改假设 A–X 正文**。与实验 O/M/N 分工：**O=大宗并进匹配量；M=盘后通道；N=收盘价怎么来；Y=集合量并进连续流动性分母**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；会话分列日量或 Asia/Shanghai 分钟加总即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2018-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**sh_stock_close_auction_start=2018-08-20 / sh_fund_close_auction_start=2026-07-06 写死**；y0=day_total / y1=matching_incl_call / y2=continuous_only；diff_buckets 十桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死冻结**（params.Y≠实验字母 Y）；**y0_primary_demo=day_total_as_continuous 写死（禁双挂）**；**minute_bar_label=bar_end 写死** |

---

## 变更

- 2026-11-02：新建标准件（总管线：并行写下一纸面 Y；W 补丁/X 预检由他人负责；清单止于 X → 自开跑前优先项「集合竞价量计入日线」+ `事实与坑` 时段/日量估冲击坑选题，**与 A–X 不撞主结论**；近邻 O=大宗、M=盘后、N=收盘机制，本页主测集合量假连续分母；**实验字母 Y ≠ params.Y**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 W/X/V/U/A 正文**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设Y-20261102.md` 有条件通过补三条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写入具体数并冻结（预检禁 holdout 标定且建议 0.02/0.01/0.05/0.015；**params.Y≠实验字母 Y**，页内注明为费用/冲击相对门槛键；禁 null）；② `params.y0_primary_demo=day_total_as_continuous`（主报日总量当连续；禁与 matching_incl_call / swallow_aft 双挂争主表）；③ `params.minute_bar_label=bar_end`（分钟 bar 右端点；与 `minute_bar_tz=Asia/Shanghai` 配套；写死冻结）。**不抢实验 A**；**Y 不开回测**；未动 Z/X/A。

### 增量补丁段 · 2026-11-02（风控三条冻结）

| 键 | 冻结值 | 备注 |
|----|--------|------|
| params.Y | 0.02 | 费用/冲击相对门槛键；**≠实验字母 Y** |
| params.G | 0.01 | 高集合桶相对对照差 |
| params.N | 0.05 | 失败/跳过率差 |
| params.Y2 | 0.015 | Y1−Y2 专项 |
| params.y0_primary_demo | day_total_as_continuous | 单一主报；禁双挂 |
| params.minute_bar_label | bar_end | 与 Asia/Shanghai 配套 |

预检稿：`experiments/backtest/A_limit_up_fill/risk_notes/预检-假设Y-20261102.md`。
