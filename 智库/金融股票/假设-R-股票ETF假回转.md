# 假设 R · 股票 ETF 当当日回转 / 全部 ETF 套 3.1.5（假 T+0）

更新：2026-11-02（风控补丁）  
来源：总管线 / Q 四条补丁已收后写下一纸面 R；清单实验 R  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「ETF 都能 T+0 / 股票 ETF 当日进出 / 盘后固定价格当 T+0」当实盘预期；不抢实验 A 真数队列；本页不开回测；Q/P 不开回测）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 R 对齐。与假设 Q（可转债当日回转写在转债细则、勿到 3.1.5 找）、B 类「股票 T+1」（普通 A 股不在 3.1.5）、M（盘后固定价格仍是当日成交、不改交收前不得卖出）互补：本页专测**股票 ETF / 跨境但书 / 商品期货 ETF 切日**上的假回转——把「ETF 都能 T+0」当默认，或把核对日现行 3.1.5 名单铺满却不剔除股票 ETF，或跨境不看底层是否本身可回转。**可转债回转属实验 Q；经手费/证管费对 ETF 误抽属实验 S/T；本页主结论不混。**

---

## 1. 一句话假设（可检验、可证伪）

同一套 ETF 信号与持有期下，把「全部 ETF 当日可买可卖」当默认（或把核对日现行 3.1.5 名单铺满全样本却不区分股票 ETF），相对「只有当日已在 3.1.5 且满足但书的品种记回转；股票 ETF 一律 T+1；商品期货 ETF 在 2020-01-20 前记失败；跨境须底层本身可回转」的 PIT 诚实组，会**虚增可交易次数、抹平股票 ETF 隔夜风险，并把不符合但书的跨境品种算成当天可平**。

证伪方向：若天真组 / 泄露组相对诚实组的「假 T+0」贡献差、失败笔数差、换手差在标定噪声带内可忽略，且「股票 ETF / 跨境但书失败 / 商品期货 2020-01-20 前」分桶不改变结论，则本假设在该样本与撮合设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 3.1.5 回转名单 ≠ 全部 ETF；股票 ETF = T+1；跨境但书；商品期货切日（未复权）

```
# 配置写死（见 §7；风控四条已冻结）
# params.asof_check_date                 写死默认 2026-10-26  # 事实与坑「股票 ETF 仍 T+1」核对日；泄露组「现行」锚
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；不抢 A 板上真数
# params.rule_315_cut_date               写死 2026-07-06     # 《交易规则（2026年修订）》施行；名单文本锚
# params.commodity_etf_rotation_start    写死 2020-01-20     # 上证发〔2020〕1 号；商品期货 ETF 写入 3.1.5
# params.stock_etf_rotation              写死 t1             # 股票 ETF 一律 T+1；禁 same_day 进诚实组
# params.r0_all_etf_same_day             写死 True           # 天真：全部 ETF 当日可买可卖
# params.r1_asof_leak_315                写死 True           # 泄露：全样本用核对日现行 3.1.5，但不剔除股票 ETF
# params.r1_exclude_stock_etf            写死 False          # 泄露组故意不区分股票 ETF（暴露假回转）
# params.r2_pit                          写死 True           # 诚实 PIT
# params.r2_stock_etf_rotation           写死 t1
# params.r2_crossborder_require_underlying_rotatable 写死 True  # 跨境但书：底层本身须可回转
# params.r2_commodity_pre_cut_fail       写死 True           # 2020-01-20 前商品期货 ETF 记失败
# params.sse_315_includes_warrant        写死 True           # 沪市 3.1.5 含权证；深市无
# params.szse_315_includes_warrant       写死 False
# params.aft_fixed_as_t0_channel         写死 False          # 禁把盘后固定价格写成股票 ETF 的 T+0 通道
# params.etf_tick                        写死 0.001          # 基金最小价位；禁用股票 0.01 套主结论
# params.etf_lot_shares                  写死 100            # ETF 申报数量单位（份/手）；禁跑后改口；禁用股票手数冒充却不另标
# params.r0_unit_source                  写死 stock_share_tick  # 天真组混用股票 100 股/0.01，暴露与 etf_tick=0.001+etf_lot_shares 鸿沟；禁双挂 etf_native
# params.underlying_rotatable_source     写死 vendor_flag    # 跨境但书字段来源；缺 → skip；禁静默 True；枚举另有 rule_table_pit / manual_asof_map
# params.missing_etf_class_policy        写死 skip           # 缺 ETF 分类 → skip，禁静默当可回转
# params.missing_underlying_rot_flag_policy 写死 skip        # 跨境缺底层可回转标记 → skip，禁一律 T+0
# params.missing_exch_policy             写死 skip
# params.merge_with_Q_cb_rotation        写死 False          # 禁与可转债回转混进同一主表
# params.merge_with_S_T_fee              写死 False          # 经手费/证管费另页
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 相对门槛；禁 holdout 标定；禁 null
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 fill_time·stock_etf_rotation·commodity 切日·跨境但书·aft_fixed_as_t0·etf_lot_shares·r0_unit_source·underlying_rotatable_source·Y/G/N/Y2·主窗/oos

fill_time = "next_open"
asof_check_date = "2026-10-26"
rule_315_cut_date = "2026-07-06"
commodity_etf_rotation_start = "2020-01-20"
stock_etf_rotation = "t1"
aft_fixed_as_t0_channel = False
etf_tick = 0.001
sse_315_includes_warrant = True
szse_315_includes_warrant = False
missing_etf_class_policy = "skip"
missing_underlying_rot_flag_policy = "skip"
missing_exch_policy = "skip"
merge_with_Q_cb_rotation = False
merge_with_S_T_fee = False
etf_lot_shares = 100
r0_unit_source = "stock_share_tick"
underlying_rotatable_source = "vendor_flag"
Y, G, N, Y2 = 0.02, 0.01, 0.05, 0.015

# ETF 分类枚举（本页）
ETF_CLASS = [
  "stock",            # 股票 ETF → 诚实组一律 T+1
  "bond",             # 债券 ETF → 3.1.5 可回转（PIT）
  "money",            # 货币 / 交易型货币基金
  "gold",             # 黄金 ETF
  "crossborder",      # 跨境 ETF/LOF；须底层本身可回转
  "commodity_futures",# 商品期货 ETF；2020-01-20 起入 3.1.5
  "warrant",          # 权证（仅沪市名单；深市无）
  "other",            # 未列类 → skip / 不发明回转
]

def in_315_pit(d, etf_class, exch, underlying_rotatable):
    """当日已生效 3.1.5 + 但书；返回 True/False/None(None=skip)."""
    if etf_class is None:
        return None  # missing_etf_class_policy=skip
    if etf_class == "stock":
        return False  # 股票 ETF 永不进诚实回转
    if etf_class == "commodity_futures":
        if d < commodity_etf_rotation_start:
            return False  # 切日前记失败/不可回转
        return True
    if etf_class == "crossborder":
        if underlying_rotatable is None:
            return None  # skip
        return bool(underlying_rotatable)
    if etf_class == "warrant":
        if exch == "SSE":
            return True
        if exch == "SZSE":
            return False  # 深市名单无权限证
        return None
    if etf_class in ("bond", "money", "gold"):
        return True
    return False  # other → 不发明

def allow_same_day_sell(group, d, etf_class, exch, underlying_rotatable):
    if group == "R0":
        return True  # 天真：全部 ETF 当日可买可卖
    if group == "R1":
        # 泄露：用核对日现行 3.1.5 文本铺满，但不剔除股票 ETF
        if etf_class == "stock" and (not r1_exclude_stock_etf):
            return True  # 故意假回转
        # 其余按核对日名单（含商品期货已入、跨境不强制但书）— 本页简化：非 stock 一律 True
        return True
    # R2 PIT
    flag = in_315_pit(d, etf_class, exch, underlying_rotatable)
    if flag is None:
        return None
    return flag

def treat_aft_fixed_as_rotation(group):
    # 盘后固定价格仍是当日成交，不改变「交收前不得卖出」
    if aft_fixed_as_t0_channel:
        raise ValueError("aft_fixed_as_t0_channel must stay False")
    return False
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺 ETF 分类、跨境缺底层可回转标记、缺交易所却要做沪/深权证分列、把盘后固定价格当股票 ETF 的 T+0 通道、把可转债回转或 S/T 费用混进本页主结论 → **跳过该腿/该日该券**，不静默当可回转。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 三组对照（本实验编码）

| 组 | 回转默认 | 股票 ETF | 跨境但书 | 商品期货 ETF `<2020-01-20` |
|----|----------|----------|----------|------------------------------|
| R0 天真 | 全部 ETF 当日可买可卖 | 当日可平（假 T+0） | 不看底层，一律回转 | 仍当可回转 |
| R1 泄露 | 全样本用核对日现行 3.1.5 | **不剔除**股票 ETF（仍可当日） | 不强制底层可回转 | 按现行已入名单回放（泄露） |
| R2 PIT | 仅当日已在 3.1.5 且满足但书 | **一律 T+1** | 底层本身须可回转 | **记失败**（不可回转） |

同一信号、同一成本开关（本页可先零成本只比换手 / 假 T+0 贡献 / 失败笔数）。**`params.fill_time=next_open` 写死**（与 A/D 对齐；不抢 A 板上真数队列）。

**`params.stock_etf_rotation=t1`（写死）**：诚实组股票 ETF 不得标 same_day。

**`params.aft_fixed_as_t0_channel=False`（写死）**：盘后固定价格（2026-07-06 起 ETF 扩围）仍是当日成交，**不**把股票 ETF 改成 T+0。

**`params.merge_with_Q_cb_rotation=False` / `params.merge_with_S_T_fee=False`（写死）**：可转债回转、经手费/证管费不得混进本页主表。

**风控补丁四条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.etf_lot_shares               = 100                 # ETF 份/手；禁跑后因整手失败率改口；禁股票 100 股冒充却不另标
params.r0_unit_source               = stock_share_tick    # 天真组混用股票 100 股/0.01；枚举另有 etf_native（本页不选）；禁双挂；禁混进 R2/主结论
params.underlying_rotatable_source  = vendor_flag         # 跨境但书字段来源；缺 → missing_underlying_rot_flag_policy=skip；禁静默 True；枚举另有 rule_table_pit / manual_asof_map
params.Y                            = 0.02                # 换手差显著门槛 ≥ 2pp（同系列纸面占位；来源 L/M/N/O/P；禁 holdout 标定）
params.G                            = 0.01                # 回转标签差异率门槛 ≥ 1pp
params.N                            = 0.05                # 失败率差门槛 ≥ 5pp
params.Y2                           = 0.015               # 股票 ETF 假 T+0 贡献专项门槛 ≥ 1.5pp
```

**`params.etf_lot_shares`（写死；拉数前冻结）**：`100`。ETF 申报数量单位（份/手常见档）。**禁止**跑后因手数换算/整手失败率改口；**禁止**用股票 100 股规则冒充 ETF 手数却不另标（与 `r0_unit_source` 分列）。

**`params.r0_unit_source`（写死；拉数前冻结；禁双挂）**：`stock_share_tick`。天真组（R0）故意混用股票 100 股 / 0.01 价位，暴露与 `etf_tick=0.001` + `etf_lot_shares=100` 的执行鸿沟。枚举另有 `etf_native`（R0 仍用 ETF 份/0.001），本页不选。**禁止**双挂；**禁止**把股票价位/手数混进 R2/主结论。

**`params.underlying_rotatable_source`（写死；拉数前冻结）**：`vendor_flag`。跨境但书依赖 `underlying_rotatable` 字段，来源取供应商布尔旗；缺源或映射不明时按 `missing_underlying_rot_flag_policy=skip`，**禁止**静默 `True` 标 R2。枚举另有 `rule_table_pit` / `manual_asof_map`，本页不用。

---

## 3. 样本区间

- **宇宙（默认）**：样本内交易型开放式基金（ETF/相关 LOF 跨境档按分类表）；不扩成全 A 选股。  
- **排除（默认）**：缺未复权匹配成交 OHLC；缺 ETF 分类；把复权价当撮合；把盘后固定价格当 T+0 却声称 PIT。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖 2020-01-20 商品期货 ETF 切日、2026-07-06 规则修订锚；稳健分桶见 `params.diff_buckets`。  
- **PIT 切片原则**：回转资格、跨境但书、商品期货切日，一律按**成交日**当时已生效文本；名单按施行日不按印发日。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调回转定义、股票 ETF 口径、跨境但书、商品期货切日或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **R0 − R2**：天真「全部 ETF T+0」相对 PIT 诚实——换手差、假 T+0 贡献、失败/跳过笔数差。  
2. **R1 − R2**：泄露（现行 3.1.5 铺满且不剔除股票 ETF）相对 PIT——看股票 ETF / 跨境但书 / 商品期货切日前被「吹胖」的那截。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "stock_etf",                 # 股票 ETF（诚实组应 T+1）
  "crossborder_but_fail",      # 跨境但底层不可回转
  "commodity_pre_20200120",    # 商品期货 ETF 切日前
  "commodity_post_20200120",   # 商品期货 ETF 切日后
  "bond_money_gold",           # 债券/货币/黄金（名单内）
  "warrant_sse_only",          # 沪市权证 vs 深市无
  "fake_t0_contrib",           # 假 T+0 贡献主桶
  "aft_fixed_not_t0",          # 盘后固定价格≠T+0 自检
  "vs_Q_cb_rotation",          # 与实验 Q 分列
  "vs_S_T_fee",                # 与实验 S/T 分列
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 换手差 ΔTO（R0/R1 相对 R2）；  
2. 回转标签差异率 ΔRot；  
3. 假 T+0 贡献差 ΔFake（尤其股票 ETF 桶）；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔTO| **≥ Y** 或 |ΔRot| **≥ G** 或 |ΔFake| **≥ Y2** 或 |ΔFail| **≥ N**，记「股票 ETF / 3.1.5 假回转执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 换手差显著门槛 | **写死** `params.Y=0.02` 并冻结 |
| G | 回转标签差异率门槛 | **写死** `params.G=0.01` 并冻结 |
| N | 失败笔数率差门槛 | **写死** `params.N=0.05` 并冻结 |
| Y2 | 股票 ETF 假 T+0 贡献门槛 | **写死** `params.Y2=0.015` 并冻结 |
| asof_check_date | 核对日锚点（泄露诊断） | **写死默认** `2026-10-26`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| stock_etf_rotation | 股票 ETF 回转 | **写死** `t1` |
| commodity_etf_rotation_start | 商品期货切日 | **写死** `2020-01-20` |
| aft_fixed_as_t0_channel | 盘后当 T+0？ | **写死** `False` |
| etf_lot_shares | ETF 手数 | **写死** `100` |
| r0_unit_source | 天真组单位源 | **写死** `stock_share_tick` |
| underlying_rotatable_source | 跨境但书字段源 | **写死** `vendor_flag` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**`params.Y` / `params.G` / `params.N` / `params.Y2` 写入冻结（具体数已写入；禁继续 null；禁 holdout 标定）**：

```
# 纸面冻结默认（机制实验相对门槛；一经写入即冻结）
# 单位：Y = abs(ΔTO) 换手差；G = abs(ΔRot) 回转标签差异率；N = abs(ΔFail) 失败率；Y2 = abs(ΔFake) 股票ETF假T+0贡献
# 来源：预检禁 holdout 标定且未给推荐数 → 与同系列 L/M/N/O/P 纸面占位一致
params.Y  = 0.02    # 换手差显著门槛 ≥ 2pp
params.G  = 0.01    # 回转标签差异率门槛 ≥ 1pp
params.N  = 0.05    # 失败率差门槛 ≥ 5pp
params.Y2 = 0.015   # 股票 ETF 假 T+0 贡献专项门槛 ≥ 1.5pp
```

门槛已在纸面写入并冻结；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、股票 ETF 口径、跨境但书、商品期货切日、`aft_fixed_as_t0_channel`、`etf_lot_shares` / `r0_unit_source` / `underlying_rotatable_source`、主窗/`oos_split` 开工拉数前必须保持冻结；**禁止跑后改口**。

**风控补丁四条（2026-11-02；拉数前冻结）**：

```
params.Y / G / N / Y2                 = 0.02 / 0.01 / 0.05 / 0.015   # 相对门槛写死；禁 holdout 标定；禁 null
params.etf_lot_shares                 = 100                          # ETF 份/手
params.r0_unit_source                 = stock_share_tick             # 天真混用股票单位；禁双挂
params.underlying_rotatable_source    = vendor_flag                  # 跨境但书字段源；缺→skip
```

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「ETF 都按 T+0 差不多」或「这类 ETF 能买」。

结论栏：空。跑完只写「该假设下差多少」，不写「这类基金能买」或选基公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验 ETF 回转 / 3.1.5 假 T+0（股票 ETF、跨境但书、商品期货切日）**，**不为 ETF 交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权、PIT 切日、禁股票 ETF same_day 标诚实、禁盘后当 T+0、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价撮合**。  
2. **把股票 ETF 写成当日回转却标 R2 诚实**。  
3. **2020-01-20 前发明商品期货 ETF 回转通道却标 PIT**。  
4. **跨境 ETF 不看底层是否本身可回转就一律 T+0 却标诚实**。  
5. **把盘后固定价格写成股票 ETF 的 T+0 通道**（违反 `aft_fixed_as_t0_channel=False`）。  
6. **用股票 0.01 价位 / 100 股去套 ETF 整手却不另标，并混进主结论**（价位应 `etf_tick=0.001`；手数 `etf_lot_shares=100` 已冻结；天真组混用仅限 R0 且 `r0_unit_source=stock_share_tick`）。  
7. **把可转债回转（实验 Q）或经手费/证管费（实验 S/T）混进本页主表**。  
8. **宇宙泄露 / holdout 反调**：看完 OOS 再改回转定义、但书或显著性门槛。  
9. **把差异写成「这类 ETF 能买」或选基公式**。  
10. **把沪市权证名单抄到深市**（违反 `szse_315_includes_warrant=False`）。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | ETF/相关 LOF 代码 |
| exchange (SSE/SZSE) | 沪深分列（权证） | 缺 → skip |
| etf_class | 分类枚举见 §2.1 | 缺 → skip；禁静默 stock→same_day |
| open/high/low/close（未复权匹配成交） | 价腿 | **禁复权** |
| volume | 换手/失败诊断 | 可选 |
| underlying_rotatable | 跨境但书 | 来源 `params.underlying_rotatable_source=vendor_flag`；跨境缺 → skip |
| is_stock_etf | 冗余布尔（可与 etf_class 互校） | 有则更好 |
| 3.1.5 回转表（PIT） | 名单+切日 | 本页 §2.1 已锁默认；商品期货自 2020-01-20 |
| aft_fixed_eligible（可选） | 盘后≠T+0 自检 | 与 M 分列；本页只禁当回转通道 |

**明确**：不依赖聚宽；**不要求新开 Level-2 / 新数据商**——日频未复权匹配成交 OHLC + ETF 分类 + 交易所 + 跨境底层可回转标记 + 本页 3.1.5 规则表即可起步。无分类字段时 **`params.missing_etf_class_policy=skip`**，不得静默当可回转。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=R`，`groups=[R0,R1,R2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-26`**，**`params.fill_time=next_open`（写死）**，**`params.rule_315_cut_date=2026-07-06`**，**`params.commodity_etf_rotation_start=2020-01-20`**，**`params.stock_etf_rotation=t1`**，**`params.r0_all_etf_same_day=True`**，**`params.r1_asof_leak_315=True`**，**`params.r1_exclude_stock_etf=False`**，**`params.r2_pit=True`**，**`params.r2_stock_etf_rotation=t1`**，**`params.r2_crossborder_require_underlying_rotatable=True`**，**`params.r2_commodity_pre_cut_fail=True`**，**`params.sse_315_includes_warrant=True`**，**`params.szse_315_includes_warrant=False`**，**`params.aft_fixed_as_t0_channel=False`**，**`params.etf_tick=0.001`**，**`params.etf_lot_shares=100`（写死冻结）**，**`params.r0_unit_source=stock_share_tick`（写死冻结；禁双挂）**，**`params.underlying_rotatable_source=vendor_flag`（写死冻结）**，**`params.missing_etf_class_policy=skip`**，**`params.missing_underlying_rot_flag_policy=skip`**，**`params.missing_exch_policy=skip`**，**`params.merge_with_Q_cb_rotation=False`**，**`params.merge_with_S_T_fee=False`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[stock_etf,crossborder_but_fail,commodity_pre_20200120,commodity_post_20200120,bond_money_gold,warrant_sse_only,fake_t0_contrib,aft_fixed_not_t0,vs_Q_cb_rotation,vs_S_T_fee]`（写死默认；拉数前冻结）**，**`params.Y=0.02` / `params.G=0.01` / `params.N=0.05` / `params.Y2=0.015`（写死具体数并冻结；禁 holdout 标定；禁 null）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_Q=off`，`overlay_M=off`，`overlay_S=off`，`overlay_T=off`，`cost_switch=off`（R 主跑）。  
- 行情与规则表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- R0/R1/R2 换手、回转标签一致率、假 T+0 贡献、失败笔数；分桶（股票 ETF、跨境但书失败、商品期货切日前后、债/货/金、权证沪深、假 T+0、盘后≠T+0、vs Q/S/T）。  
- 自检布尔：是否未复权；R2 股票 ETF 是否 T+1；2020-01-20 前商品期货是否失败；跨境是否强制但书；盘后是否未当 T+0；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把天真「ETF 都能 T+0」当实盘预期；催跑抢 A 真数队列。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**Q/P 不开回测**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：股票 ETF 仍是 T+1；3.1.5 回转名单不要扩成「所有 ETF」；跨境须底层本身可回转；商品期货 ETF 自 2020-01-20 入名单；盘后固定价格不把股票 ETF 改成 T+0。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 R 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A/D–Q 正文**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权匹配成交 OHLC + ETF 分类 + 交易所 + 跨境但书标记 + 本页 3.1.5 规则表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测；**Q/P 不开回测**） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-26；**fill_time=next_open 写死**；**stock_etf_rotation=t1**；**commodity_etf_rotation_start=2020-01-20**；**aft_fixed_as_t0_channel=False**；跨境但书强制；沪深权证分列；diff_buckets 十桶写死冻结；**`etf_lot_shares=100`**；**`r0_unit_source=stock_share_tick`（禁双挂）**；**`underlying_rotatable_source=vendor_flag`**；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死具体数并冻结、禁 holdout 标定、禁 null** |

---

## 变更

- 2026-11-02：新建标准件（总管线：Q 四条补丁已收后写 R；选型严格对齐清单实验 R「股票 ETF 当当日回转 / 全部 ETF 套 3.1.5」；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设R-20261102.md` 有条件通过补四条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写入具体数并冻结（预检禁 holdout 标定且未给推荐数；与同系列 L/M/N/O/P 纸面占位一致；禁 null）；② `params.etf_lot_shares=100`；③ `params.r0_unit_source=stock_share_tick`（禁双挂 `etf_native`）；④ `params.underlying_rotatable_source=vendor_flag`（缺→skip；禁静默 True）。**不抢实验 A**；**R 不开回测**；未动 S/P/Q/A。
