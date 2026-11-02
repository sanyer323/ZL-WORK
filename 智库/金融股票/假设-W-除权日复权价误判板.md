# 假设 W · 除权日用复权价误判涨跌停 / 自造除权参考价（执行鸿沟）

更新：2026-11-02  
来源：总管线 / U 补丁·V 预检并行写下一纸面 W；清单原止于 V，选题自清单早期「实验 B · 除权日用复权价误判涨停」+ `事实与坑`「复权价能算收益，不能判涨停」/「除权参考价有交易所公式」+ `口径`「涨跌停用不复权+除权参考价」；**新建实验 W**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「复权价判板 / 自造除权参考价」当诚实板上标签；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 U/V/R/S/T/A 及已交补丁正文**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 早期实验 B 对齐；清单原无 W 节，本页自立实验 W 标准件。与假设 A（涨停可成交性，假定板上价已诚实）、假设 F（涨跌停价取整；F2 复权判板仅作反例）**分列**：本页**主测**「数据商前/后复权收盘（及复权前收盘）套 ±10%/±20%」相对「未复权收盘 + 交易所前收盘（除权日=除权参考价）」的标签鸿沟，并附带「只减现金红利、忘送转/配股」的自造参考价臂。**取整属实验 F；板上可成交属实验 A；涨跌幅规则 PIT 属实验 G；费用四层属 S/T/U/V。本页主结论不混。**

---

## 1. 一句话假设（可检验、可证伪）

同一日、同一板块涨跌幅比例下，用数据商**前复权/后复权收盘（或复权前收盘）**去套「±10%/±20%」标涨跌停，相对「**未复权收盘** + **交易所前收盘（除权/息日=除权参考价）** + 同一比例」的诚实组，会**在除权（息）日系统性误标涨跌停**；若再自造「只减现金红利」的参考价，误标会再扩一层。差异率应**集中在除权（息）日**，而不是随机散开；错标会把后续「假成交 / 板上约束」实验（如假设 A）带偏。

证伪方向：若复权判板组 / 自造参考价组相对诚实组的标签差异率在标定噪声带内可忽略，且「除权日 / 非除权日 / 送转密集 / 配股日 / 低价股」分桶不改变结论（差异不集中在除权桶），则本假设在该样本与判板设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 判板基准三套；除权参考价用交易所公式；收益复权 ≠ 板上复权（未复权判板）

```
# 配置写死键（见 §7；风控补丁四条已冻结 2026-11-02；D_ex 与 G 合并）
# params.asof_check_date                 写死默认 2026-10-05  # 事实与坑「整手+取整+除权公式」核对日
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；本页主测标签，不抢 A 板上真数
# params.tick                            写死 0.01           # 仅 A 股股票；禁基金 0.001 混主结论
# params.tag_cmp                         写死 ge_le          # close >= limit_up / close <= limit_down；与 A/F 同向
# params.limit_pct_source                写死 board_st_day_effective  # 与 F/G 同向；本页不重开 ST/新股窗
# params.round_half_up_to_tick           写死 True           # 诚实组板上价先取整（对齐 F1）；本页不主测取整差
# params.w0_price_basis                  写死 adj_close      # 天真：数据商复权收盘判板
# params.w0_preclose_basis               写死 adj_preclose   # 天真：复权前收盘当涨跌幅基准
# params.w0_adj_flavor                   写死 dual_report_forward_and_backward  # 前/后复权分列报告；禁只跑一种却写「复权都一样」；禁双挂未声明
# params.w1_exref_formula                写死 cash_only      # 误切：只减现金红利，忘送转/配股
# params.w2_price_basis                  写死 raw_close      # PIT 诚实：未复权收盘
# params.w2_preclose_basis               写死 exchange_preclose_or_exref  # 除权日=交易所除权参考价
# params.exref_formula_source            写死 exchange_rule  # 上交所 4.3.2 / 深交所 4.4.2；禁数据商复权因子反推
# params.merge_with_A_fill               写死 False          # 板上可成交另页 A
# params.merge_with_F_rounding           写死 False          # 取整主测另页 F；本页诚实臂沿用 F1 取整但不报取整差为主结论
# params.merge_with_G_limit_pct_pit      写死 False          # 涨跌幅规则 PIT 另页 G
# params.merge_with_S_T_U_V_fee          写死 False          # 费用四层另页
# params.missing_ex_flag_policy          写死 skip           # 缺除权标记却要分除权桶 → skip
# params.missing_exref_policy            写死 skip           # 除权日缺交易所参考价 → skip，禁静默用昨收/复权前收
# params.missing_adj_policy              写死 skip           # 天真臂缺复权列 → skip，禁静默 raw
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；禁 holdout 标定；禁 null
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 price_basis、exref 公式、Y/G/N/Y2、主窗/oos、w0_adj_flavor、w1_primary_demo、D_ex

fill_time = "next_open"
asof_check_date = "2026-10-05"
tick = 0.01
tag_cmp = "ge_le"
limit_pct_source = "board_st_day_effective"
round_half_up_to_tick = True
w0_price_basis = "adj_close"
w0_preclose_basis = "adj_preclose"
w1_exref_formula = "cash_only"
w2_price_basis = "raw_close"
w2_preclose_basis = "exchange_preclose_or_exref"
exref_formula_source = "exchange_rule"
merge_with_A_fill = False
merge_with_F_rounding = False
merge_with_G_limit_pct_pit = False
merge_with_S_T_U_V_fee = False
missing_ex_flag_policy = "skip"
missing_exref_policy = "skip"
missing_adj_policy = "skip"
Y = 0.02
G = 0.01
N = 0.05
Y2 = 0.015
w0_adj_flavor = "dual_report_forward_and_backward"
w1_primary_demo = "cash_only_exref"
D_ex = 0.01  # 与 G 合并同槽；D_ex ≡ G
D_ex_merged_with_G = True

def round_half_up(x, tick=0.01):
    from math import floor
    return floor(x / tick + 0.5) * tick

def exchange_exref(pre_close, cash_div, rights_px, float_chg_ratio):
    """交易所除权（息）参考价（结构对齐上交所 4.3.2 / 深交所 4.4.2）。
    SSE 用流通股份变动比例；SZSE 用股份变动比例——本页键名 float_chg_ratio，
    拉数时按交易所字段映射；缺字段 → missing_exref_policy=skip。
    """
    return ((pre_close - cash_div) + rights_px * float_chg_ratio) / (1.0 + float_chg_ratio)

def cash_only_exref(pre_close, cash_div, rights_px, float_chg_ratio):
    """误切：只减现金红利，忽略送转/配股变动比例。"""
    return pre_close - cash_div

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

def tag_limit(close, pre_close, pct):
    if close is None or pre_close is None or pct is None:
        return None  # skip
    up, dn = board_limits(pre_close, pct)
    is_up = close >= up
    is_dn = close <= dn
    return is_up, is_dn

def tags_for_group(group, row):
    """row 须含：raw_close, exchange_preclose, ex_flag, adj_close, adj_preclose,
    cash_div, rights_px, float_chg_ratio, pct, exch。"""
    pct = row["pct"]  # 由 limit_pct_source 按日切片；无涨跌幅日 → skip
    if group == "W0":
        if row.get("adj_close") is None or row.get("adj_preclose") is None:
            return None
        return tag_limit(row["adj_close"], row["adj_preclose"], pct)
    if group == "W1":
        # 价格仍用未复权收盘，但基准自造 cash_only 参考价（除权日）；非除权日退回交易所前收盘
        if row.get("raw_close") is None:
            return None
        if row.get("ex_flag"):
            if any(row.get(k) is None for k in ("cash_div", "rights_px", "float_chg_ratio", "exchange_preclose")):
                return None
            # cash_only 忽略 rights/float；仍要求字段在以便对照
            pref = cash_only_exref(row["exchange_preclose"], row["cash_div"], row["rights_px"], row["float_chg_ratio"])
        else:
            pref = row.get("exchange_preclose")
        return tag_limit(row["raw_close"], pref, pct)
    # W2 PIT
    if row.get("raw_close") is None:
        return None
    if row.get("ex_flag"):
        pref = row.get("ex_ref_price")  # 行情前收盘=除权参考价；缺则用公式算
        if pref is None:
            if any(row.get(k) is None for k in ("cash_div", "rights_px", "float_chg_ratio", "exchange_preclose")):
                return None
            pref = exchange_exref(row["exchange_preclose"], row["cash_div"], row["rights_px"], row["float_chg_ratio"])
    else:
        pref = row.get("exchange_preclose")
    if pref is None:
        return None
    return tag_limit(row["raw_close"], pref, pct)
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺未复权收盘、缺交易所前收盘/除权参考价、缺复权列却跑 W0、缺除权标记却要分除权桶、无涨跌幅日硬套 ±10%/±20%、把取整主差（F）或费用层（S/T/U/V）混进本页主结论 → **跳过该日该券标签**，不静默用昨收/复权前收填假板。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 三组对照（本实验编码；自立实验 W）

| 组 | 收盘价列 | 涨跌幅基准 | 除权日处理 |
|----|----------|------------|------------|
| W0 天真-复权判板 | 前/后复权收盘 | 复权前收盘 | 整段平移后仍套 ±pct → **除权日易误标** |
| W1 误切-自造参考价 | 未复权收盘 | cash_only 参考价 | 只减红利、忘送转/配股 |
| W2 PIT 诚实 | 未复权收盘 | 交易所前收盘；除权日=除权参考价 | 交易所公式 / 行情前收盘字段 |

同一日、同一 `pct` 切片（`limit_pct_source=board_st_day_effective`）、同一股票宇宙。本页**主测标签差异**，不主测成交撮合（成交见 A；取整主测见 F；规则窗见 G）。**`params.fill_time=next_open` 写死**（与 A/D 对齐；不抢 A 板上真数队列）。

**`params.merge_with_A_fill=False` / `params.merge_with_F_rounding=False` / `params.merge_with_G_limit_pct_pit=False` / `params.merge_with_S_T_U_V_fee=False`（写死）**：A/F/G/费用层不得混进本页主表当主结论。

**风控补丁四条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                # 标签差异率显著门槛 ≥ 2pp（同系列纸面占位；来源 L/M/N/O/P/R/S/T/U/V；禁 holdout 标定）
params.G                            = 0.01                # 除权日相对非除权日差异率差门槛 ≥ 1pp（ΔTag_ex）
params.N                            = 0.05                # 失败/跳过率差门槛 ≥ 5pp
params.Y2                           = 0.015               # 送转/配股日或 W1 cash_only 专项差异门槛 ≥ 1.5pp
params.w0_adj_flavor                = dual_report_forward_and_backward  # 前/后复权分列报告；禁只跑一种却写「复权都一样」；禁双挂未声明
params.w1_primary_demo              = cash_only_exref     # 主报自造参考价；枚举另有 adj_forward_tag / adj_backward_tag；禁双挂争主表
params.D_ex                         = 0.01                # 与 params.G 合并同槽（除权日 δ_ex − 非除权 δ_nex）；D_ex ≡ G；不另立冲突门槛
params.D_ex_merged_with_G           = True                # 显式合并声明（预检条件④）；禁缺键静默自造
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股股票（不含可转债、不含股票 ETF 主样本）。须含足量**除权（息）日**（现金红利 / 送转 / 配股），否则分桶不可检。  
- **排除（默认）**：无涨跌幅日（见实验 G；纳入须另标）；退市整理期（见实验 H）；`raw_close` / 交易所前收盘缺失；无法识别板块/`pct`；缺除权标记却强行进除权桶。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2020-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖多个分红季与送转密集窗；除权日为差异主战场。  
- **PIT 切片原则**：板上标签一律按**成交日**未复权价 + 当日交易所前收盘/除权参考价；**收益复权列不得进入 W2 判板**。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2020-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 price_basis、exref 公式、显著性门槛或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **W0 − W2**：复权判板相对 PIT——「除权日误标」的那截标签差。  
2. **W1 − W2**：cash_only 自造参考价相对 PIT——忘送转/配股的那截。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "ex_div_day",                # 除权（息）日主战场
  "non_ex_day",                # 非除权对照；差异应显著更小
  "cash_div_only",             # 纯现金红利
  "stock_div_or_transfer",     # 送转
  "rights_issue",              # 配股
  "low_price_lt5",             # 未复权收盘 <5 元（与 F 低价桶对齐但不主测取整）
  "mid_price_5_20",
  "high_price_ge20",
  "adj_forward_vs_pit",
  "adj_backward_vs_pit",
  "cash_only_vs_pit",
  "vs_F_rounding",             # 对照声明：取整差另页 F，本页不抢主结论
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 标签差异率 ΔTag（W0/W1 相对 W2；涨停/跌停分列）；  
2. 除权日相对非除权日差异率差 ΔTag_ex（应显著为正）；  
3. 送转/配股日或 W1 专项差异 ΔTag_corp；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔTag| **≥ Y** 或 |ΔTag_ex| **≥ G** 或 |ΔTag_corp| **≥ Y2** 或 |ΔFail| **≥ N**，记「除权日复权价误判板 / 自造参考价执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 标签差异率显著门槛 | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| G | 除权日相对非除权差异率差门槛 | **写死冻结** `0.01`（与 D_ex 合并同槽） |
| N | 失败笔数率差门槛 | **写死冻结** `0.05` |
| Y2 | 送转/配股或 cash_only 专项门槛 | **写死冻结** `0.015` |
| D_ex | 除权日 δ_ex − 非除权 δ_nex | **与 G 合并**；`D_ex=0.01`；`D_ex_merged_with_G=True` |
| w0_adj_flavor | 复权口味 | **写死** `dual_report_forward_and_backward` |
| w1_primary_demo | 主报枚举 | **写死** `cash_only_exref`（禁双挂） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-05`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| tick | 最小价位 | **写死** 0.01（仅 A 股股票） |
| tag_cmp | 比较符 | **写死** `ge_le` |
| w2_preclose_basis | 诚实基准 | **写死** `exchange_preclose_or_exref` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已写入 params 并冻结（风控补丁 2026-11-02）；**禁止用 holdout / OOS 段标定或反调**。

**失败/不显著**：差异落在噪声带内或均匀散在非除权日——结论栏写明，不得改口称「复权判板差不多」或「这类除权票能买」。

结论栏：空。跑完只写「该假设下标签差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验除权日复权判板 / 自造参考价**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（未复权判板、交易所除权参考价、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权收盘/复权前收盘标涨跌停却标 W2 诚实**。  
2. **除权日不用交易所除权参考价（或行情前收盘字段）却标 PIT**。  
3. **只减现金红利、忘送转/配股却标交易所公式**。  
4. **用数据商复权因子反推涨跌停价**。  
5. **无涨跌幅日硬套 ±10%/±20%**（见实验 G）。  
6. **把取整差（F）或板上可成交（A）重开混进本页主结论**。  
7. **把费用四层（S/T/U/V）混进本页主表**。  
8. **宇宙泄露 / holdout 反调**：看完 OOS 再改 price_basis 或显著性门槛。  
9. **差异不集中在除权桶却仍写「除权日系统性误标」而不改表述**。  
10. **把差异写成「这类除权票能买」或选股公式**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股股票 |
| exchange (SSE/SZSE) | 沪深公式字段映射 | 北交所默认另桶/不进主跑 |
| raw_close / raw OHLC（未复权） | W1/W2 判板 | **禁复权**；缺 → skip |
| exchange_preclose | 非除权日基准；除权公式输入 | 行情前收盘 |
| ex_ref_price 或除权参考价 | 除权日基准 | 可与行情前收盘同列；缺则公式算或 skip |
| ex_flag / ex_div_date | 除权（息）标记 | 分桶核心；缺 → skip 除权桶 |
| cash_div, rights_px, float_chg_ratio | 交易所公式 / W1 cash_only | SSE 流通股份变动比例 / SZSE 股份变动比例 |
| adj_close, adj_preclose（前/后复权） | W0 天真臂 | 前/后复权分列报告；缺 → skip W0 |
| board / st_flag / limit_pct | 比例切片 | 与 F/G 同向；本页不重开切日实验 |
| 未复权收盘价分桶 | 低价/中价/高价 | 与 F 桶边对齐声明，不主测取整 |

**明确**：不依赖聚宽；**不要求新开 Level-2 / 新数据商**——日频未复权行情 + 交易所前收盘/除权字段 + 数据商复权列 + 本页规则即可起步。主窗自 2020-01-01。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=W`，`groups=[W0,W1,W2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-05`**，**`params.fill_time=next_open`（写死）**，**`params.tick=0.01`**，**`params.tag_cmp=ge_le`**，**`params.limit_pct_source=board_st_day_effective`**，**`params.round_half_up_to_tick=True`**，**`params.w0_price_basis=adj_close`**，**`params.w0_preclose_basis=adj_preclose`**，**`params.w1_exref_formula=cash_only`**，**`params.w2_price_basis=raw_close`**，**`params.w2_preclose_basis=exchange_preclose_or_exref`**，**`params.exref_formula_source=exchange_rule`**，**`params.missing_ex_flag_policy=skip`**，**`params.missing_exref_policy=skip`**，**`params.missing_adj_policy=skip`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_F_rounding=False`**，**`params.merge_with_G_limit_pct_pit=False`**，**`params.merge_with_S_T_U_V_fee=False`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015`（写死冻结；禁 holdout 标定；禁 null）**，**`params.w0_adj_flavor=dual_report_forward_and_backward`（写死；禁双挂未声明）**，**`params.w1_primary_demo=cash_only_exref`（写死；禁双挂）**，**`params.D_ex=0.01` / `params.D_ex_merged_with_G=True`（与 G 合并冻结）**，`universe_rule`，**`params.date_start=2020-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2020-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_F=off`，`overlay_G=off`，`overlay_S=off`，`overlay_T=off`，`overlay_U=off`，`overlay_V=off`。  
- 行情与除权字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- W0/W1/W2 涨跌停标签一致率、ΔTag、ΔTag_ex、送转/配股专项、失败笔数；分桶（除权/非除权、现金/送转/配股、价位、前/后复权、vs F）。  
- 自检布尔：W2 是否未复权；除权日是否用交易所参考价；是否未用复权因子反推；是否未与 A/F/G/费用层混主结论；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把复权判板当诚实板上标签；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 U/V/R/S/T/A 已冻结正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：复权价只用来算收益；涨跌停/一字/可否成交必须用不复权价；除权（息）日用交易所除权参考价当行情前收盘；除权参考价按交易所公式，不要用数据商复权因子反推。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 V，本页**新增实验 W** 收成标准件（对齐早期「实验 B · 除权日用复权价误判涨停」），**不改口径主线**，**不改假设 A–V 正文**。与实验 A/F/G 分工：**A 只动板上可成交，F 只动取整，G 只动涨跌幅规则窗，W 只动复权判板 / 除权参考价基准**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权行情 + 交易所前收盘/除权字段 + 复权列即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2020-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-05；**fill_time=next_open 写死**；**tick=0.01 / tag_cmp=ge_le / w2_preclose_basis=exchange_preclose_or_exref 写死**；diff_buckets 十二桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死冻结**；**w0_adj_flavor=dual_report_forward_and_backward 写死（禁双挂未声明）**；**w1_primary_demo=cash_only_exref 写死（禁双挂）**；**D_ex=0.01 与 G 合并（D_ex_merged_with_G=True）** |

---

## 变更

- 2026-11-02：新建标准件（总管线：U 补丁/V 预检并行写 W；清单止于 V → 自清单早期实验 B + `事实与坑` 除权/复权坑选题，**与 A–V 不撞主结论**；近邻 A=可成交、F=取整（F2 仅反例）、G=规则窗，本页主测复权判板+自造参考价；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 U/V/R/S/T/A 正文**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设W-20261102.md` 有条件通过补四条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写入具体数并冻结（预检禁 holdout 标定且建议 0.02/0.01/0.05/0.015；与同系列 R/S/T/U/V 纸面占位一致；禁 null）；② `params.w0_adj_flavor=dual_report_forward_and_backward`（前/后复权分列报告；禁双挂未声明）；③ `params.w1_primary_demo=cash_only_exref`（主报自造参考价；禁双挂 adj_forward_tag / adj_backward_tag）；④ `params.D_ex=0.01` 与 `params.G` 合并同槽（`D_ex_merged_with_G=True`；不另立冲突门槛）。**不抢实验 A**；**W 不开回测**；未动 X/V/U/R/S/T/A。
