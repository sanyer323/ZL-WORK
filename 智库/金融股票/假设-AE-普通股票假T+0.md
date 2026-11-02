# 假设 AE · 普通 A 股当日买入当日卖出（假 T+0 / 执行鸿沟）

更新：2026-11-02  
来源：总管线 / AD 补丁已交后并行写下一纸面 AE；清单原止于 AD，无 AE 节 → 自立实验 AE；选题自 `事实与坑`「A 股股票默认不能当天买当天卖 / 3.1.4 交收前不得卖出、3.1.5 当日回转名单不含普通 A 股」+ `假设-R` 旁路「B 类股票 T+1（普通 A 股不在 3.1.5）」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债回转）/ AC（北交所）/ AD（风险警示 50 万买入上限）**分列**；**新建实验 AE**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「普通股票可当日买当日卖 / 盘后当绕开 T+1」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA/AB/AC/AD 及其他 A/D–AD 已交正文与冻结补丁**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AD，本页自立实验 AE 标准件。与假设 R（股票 ETF / 3.1.5 假回转）**分列**：R 主测 ETF 宇宙误开当日回转；本页主测**普通 A 股股票**被当成 T+0。与假设 Q（可转债）**分列**：可转债诚实可当日回转，勿把转债细则抄到股票，也勿把股票 T+1 罚到转债。与假设 M（盘后固定价格）**分列**：盘后仍是**当日**成交，**不改变**交收前不得卖出；本页禁止把盘后写成股票 T+0 逃生通道（M 同向禁止句，本页主测）。与假设 A（涨停可成交）**分列**：A 主测板上能否成交；本页在可成交前提下另测**当日新买仓可否当日卖**。与假设 E（整手）/ H（整理期）/ X（ST 涨跌幅）/ O（大宗）/ AC（北交所）/ AD（50 万买入上限）**分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AE** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AE / 假设-AE / hypothesis_id=AE / 组 AE0·AE1·AE2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AE 与 params 键名 `ae0_*` 以外的单字母/双字母实验页混读。

---

## 1. 一句话假设（可检验、可证伪）

同一普通 A 股股票宇宙、同一未复权价、同一成交时点下，把「当日新买入的股票仓」允许**当日再卖出**（假 T+0），或把**盘后固定价格**当成绕开交收前不得卖出的通道，相对「买入交收前不得卖出；当日新买仓计入不可卖库存；卖出所得资金当日可再买别的；盘后成交仍不改 T+1」的 PIT 诚实组，会**系统性虚增可交易次数与换手、抹平隔夜风险、高估可卖名义**；差异应**集中在「当日新买又卖 / 盘后当 T+0」桶**，而不是随机散开。

证伪方向：若天真组 / 误开组相对诚实组的当日回转腿贡献差、换手差、可卖名义差、（可选）净值差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在假 T+0 相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 普通股票 T+1 ≠ ETF 3.1.5；≠ 可转债回转；盘后 ≠ 绕开交收

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AE
# params.asof_check_date                 写死默认 2026-09-28  # 事实与坑「股票默认 T+1」核对锚（3.1.4/3.1.5）
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；本页主测库存可卖性，不抢 A 板上真数
# params.stock_rotation_honest           写死 t1             # 诚实：普通 A 股交收前不得卖出
# params.same_day_buy_sellable_honest    写死 False          # 诚实：当日新买仓不可卖
# params.cash_from_sell_reusable_same_day 写死 True          # 诚实：卖出资金当日可再买（与「股不能当日卖」分列）
# params.aft_as_t0_channel_honest        写死 False          # 诚实：盘后固定价格不改 T+1
# params.ae0_primary_demo                写死 invent_same_day_sell  # 风控补丁冻结；主报：允许当日新买仓当日卖；禁与 invent_aft_as_t0 双挂争主表
# params.ae0_allow_same_day_sell         写死 True           # 天真主路径：假 T+0
# params.ae0_aft_as_t0                   写死 False          # 天真可叠诊断；主报仍以 ae0_primary_demo 为准
# params.ae1_invent_aft_as_t0            写死 True           # 半泄露/误开：盘后当 T+0 逃生通道
# params.ae1_allow_same_day_sell         写死 False          # AE1 主病不在全日 T+0，而在盘后误开（可与 AE0 分桶对照）
# params.ae2_stock_rotation              写死 t1
# params.ae2_same_day_buy_sellable       写死 False
# params.ae2_aft_as_t0_channel           写死 False
# params.merge_with_R_etf_rotation       写死 False          # ETF 假回转另页 R
# params.merge_with_Q_cb_rotation        写死 False          # 可转债回转另页 Q
# params.merge_with_M_aft                写死 False          # 盘后通道另页 M；本页只测「盘后当绕开 T+1」
# params.merge_with_A_fill               写死 False          # 板上可成交另页 A
# params.merge_with_E_lot                写死 False          # 整手另页 E
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.universe_rule                   写死 sse_szse_common_stock  # 沪深普通 A 股股票；ETF/转债/北交所不进主宇宙
# params.missing_security_class_policy   写死 skip           # 缺证券类别 → skip（禁静默当可回转）
# params.inventory_lot_policy            写死 fifo_by_buy_date  # 可卖库存按买入日批次；当日批次 honest=不可卖
# params.px_basis                        写死 unadj
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AE；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-09-28"
stock_rotation_honest = "t1"
same_day_buy_sellable_honest = False
cash_from_sell_reusable_same_day = True
aft_as_t0_channel_honest = False
ae0_primary_demo = "invent_same_day_sell"  # 风控补丁冻结；禁双挂
ae0_allow_same_day_sell = True
ae0_aft_as_t0 = False
ae1_invent_aft_as_t0 = True
ae1_allow_same_day_sell = False
ae2_stock_rotation = "t1"
ae2_same_day_buy_sellable = False
ae2_aft_as_t0_channel = False
merge_with_R_etf_rotation = False
merge_with_Q_cb_rotation = False
merge_with_M_aft = False
merge_with_A_fill = False
merge_with_E_lot = False
merge_with_H_exit = False
merge_with_X_st_limit = False
merge_with_O_block = False
merge_with_AC_bse = False
merge_with_AD_50w = False
universe_rule = "sse_szse_common_stock"
missing_security_class_policy = "skip"
inventory_lot_policy = "fifo_by_buy_date"
px_basis = "unadj"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 ae0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AE
G = 0.01
N = 0.05
Y2 = 0.015

def sellable_qty(code, trade_date, group, lots):
    """可卖股数：诚实组剔除当日买入批次；天真组可含当日批次。"""
    if group == "AE0" and ae0_allow_same_day_sell:
        return sum(q for _, q in lots)
    if group == "AE1" and ae1_allow_same_day_sell:
        return sum(q for _, q in lots)
    # AE2 / AE1 默认：仅 buy_date < trade_date
    return sum(q for d, q in lots if d < trade_date)

def aft_sell_ok_same_day_buy(group, is_aft_session):
    """盘后是否允许卖当日新买仓。诚实=否；AE1 误开=是。"""
    if not is_aft_session:
        return False
    if group == "AE2":
        return False
    if group == "AE1" and ae1_invent_aft_as_t0:
        return True
    if group == "AE0" and ae0_aft_as_t0:
        return True
    return False
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺证券类别却硬判可回转、把 R 的 ETF 回转 / Q 的转债回转 / M 的盘后主通道 / A 板上混进本页主表、用复权价、把盘后写成 AE2 诚实可绕开 T+1、把普通股票写成 3.1.5 名单成员却不改表述 → **跳过该日该券卖出执行腿**，不静默记成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AE）

| 组 | 当日新买仓可否卖 / 盘后 | 说明 |
|----|-------------------------|------|
| AE0 天真 | 允许当日新买仓当日卖（按 `ae0_primary_demo` 单一主报；可叠盘后诊断） | 普通股票假 T+0 |
| AE1 半泄露/误开 | 竞价仍 T+1，但把盘后固定价格当成可卖当日新买仓的逃生通道 | 盘后绕开交收 |
| AE2 PIT 诚实 | 当日新买仓不可卖；盘后不改 T+1；卖出资金当日可再买 | 与事实与坑 3.1.4 同向 |

同一信号、同一普通 A 股宇宙。本页**主测股票 T+1 执行诚信**，不主测 ETF 回转名单（见 R）、不主测可转债回转（见 Q）、不主测盘后通道落地（见 M）、不主测板上可成交（见 A）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_R_etf_rotation=False` / `merge_with_Q_cb_rotation=False` / `merge_with_M_aft=False` / `merge_with_A_fill=False` / `merge_with_E_lot=False` / `merge_with_H_exit=False` / `merge_with_X_st_limit=False` / `merge_with_O_block=False` / `merge_with_AC_bse=False` / `merge_with_AD_50w=False`（写死）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                 # 换手/净值/可卖名义差显著门槛；≠实验字母 AE
params.G                            = 0.01                 # 假 T+0 腿贡献 / 盘后误开桶相对对照差
params.N                            = 0.05                 # 失败/跳过率差门槛
params.Y2                           = 0.015                # AE1（盘后当 T+0）相对 AE2 专项门槛
params.ae0_primary_demo             = invent_same_day_sell # 主报允许当日新买仓当日卖；禁与 invent_aft_as_t0 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股股票（`universe_rule=sse_szse_common_stock`）。ETF、可转债、北交所只进「对照声明」桶，不进主跑。  
- **排除（默认）**：非普通股票；缺证券类别；用复权价；把 R/Q/M/A 主结论并进本页主表。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - **覆盖 2026-07-06**（规则修订施行日；盘后扩围仍不改股票 T+1——本页主测点之一）。  
- **PIT 切片原则**：是否普通股票、买入批次日期，一律按成交日当时；**禁止**把 3.1.5 回转名单扩到普通股票；**禁止**用核对日「某券商误开 T+0」回放。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ae0_primary_demo`、盘后误开开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AE0 − AE2**：假 T+0（当日新买又卖）相对诚实 T+1——换手吹胖 / 隔夜风险被抹平。  
2. **AE1 − AE2**：盘后当 T+0 逃生通道相对诚实——假可卖名义 / 假盘后平仓。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "same_day_buy_then_sell",   # 当日新买又卖
  "aft_as_t0_escape",         # 盘后当绕开 T+1
  "honest_t1_blocked",        # 对照诚实：当日批次不可卖
  "cash_reuse_ok",            # 对照声明：卖出资金当日可再买（非本页病）
  "vs_R_etf_rotation",        # 对照声明：ETF 假回转另页 R
  "vs_Q_cb_rotation",         # 对照声明：可转债另页 Q
  "vs_M_aft_channel",         # 对照声明：盘后通道另页 M
  "vs_A_fill",                # 对照声明：板上可成交另页 A
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 当日回转腿贡献差 ΔRoundTrip（AE0/AE1 相对 AE2）；  
2. 换手差 ΔTurnover；  
3. 可卖名义差 ΔSellableNotional；  
4. （可选）腿净值差 ΔPnL；  
5. 失败/跳过率差 ΔFail。

**相对判据（草稿）**：若 |ΔRoundTrip| 或 |ΔTurnover| 或 |ΔPnL| **≥ params.Y** 或 |ΔSellableNotional 桶贡献| **≥ params.G** 或 |ΔRoundTrip_(AE1−AE2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「普通股票假 T+0 执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；禁 holdout 标定；与实验字母 AE 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 换手/净值/回转腿差显著门槛（≠实验字母 AE） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 假 T+0 / 盘后误开桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败笔数率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AE1−AE2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-09-28` |
| fill_time | 成交时点 | **写死** `next_open` |
| stock_rotation_honest | 诚实回转属性 | **写死** `t1` |
| same_day_buy_sellable_honest | 当日新买可卖 | **写死** `False` |
| aft_as_t0_channel_honest | 盘后绕开 T+1 | **写死** `False` |
| ae0_primary_demo | 天真主报枚举 | **写死冻结** `invent_same_day_sell`（风控补丁 2026-11-02；禁双挂） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已写入 params 并冻结（风控补丁 2026-11-02；**`params.Y`≠实验字母 AE**）；**禁止用 holdout / 事后显著性改口**；**`ae0_primary_demo=invent_same_day_sell` 单一主报，禁与 invent_aft_as_t0 双挂争主表**。

**失败/不显著**：差异落在噪声带内或均匀散在非假 T+0 对照桶——结论栏写明，不得改口称「普通股票差不多能按 T+0 回放」或「这类票更能做日内」。

结论栏：空。跑完只写「该假设下当日回转腿/换手差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验普通股票 T+1 执行诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（PIT T+1、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价做库存/成交金额**。  
2. **把 R 的 ETF 回转、Q 的可转债回转、M 的盘后主通道落地混进本页主结论**。  
3. **把盘后固定价格写成 AE2 诚实可卖当日新买仓**。  
4. **把普通 A 股写成 3.1.5 当日回转名单成员却不改表述**。  
5. **缺证券类别却静默当可回转**。  
6. **宇宙泄露 / holdout 反调**：看完 OOS 再改 `ae0_primary_demo` 或 **`params.Y` 等门槛**。  
7. **差异不集中在假 T+0 / 盘后误开桶却仍写「系统性股票 T+0 鸿沟」而不改表述**。  
8. **把差异写成「这类票能做日内」或选股公式**。  
9. **把实验字母 AE 与 `params.Y` 混改**；或改写 Y/Z/AA/AB/AC/AD 及其他 A/D–AD 已冻正文。  
10. **把「卖出资金当日可再买」误判成本页失败条件**（该条诚实为 True，与「股不能当日卖」分列）。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | 沪深普通股为主 |
| security_class / asset_type | 过滤普通股票 | 缺 → skip；禁静默当 ETF/转债 |
| exchange | 沪/深 | 北交所不进主宇宙 |
| buy_lots / position_by_buy_date | 库存批次 | 至少能区分「当日买入批次」vs「昨日及更早」 |
| sell_qty / sell_notional | 卖出腿 | 用于算当日回转 |
| is_aft_session（可选） | 盘后误开诊断 | 无字段→只报通道可用性差 |
| unadj_px（可选） | 名义金额 | 禁复权主结论 |

**明确**：不依赖聚宽；**不要求新开 Level-2**——有日频买卖腿 + 证券类别 +（最好）按买入日分批库存即可起步；缺证券类别 → `fail_policy=skip`。主窗 2019-01-01..2026-09-30。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=AE`（**实验字母**），`groups=[AE0,AE1,AE2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-09-28`**，**`params.fill_time=next_open`（写死）**，**`params.stock_rotation_honest=t1`**，**`params.same_day_buy_sellable_honest=False`**，**`params.cash_from_sell_reusable_same_day=True`**，**`params.aft_as_t0_channel_honest=False`**，**`params.merge_with_R_etf_rotation=False`**，**`params.merge_with_Q_cb_rotation=False`**，**`params.merge_with_M_aft=False`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_E_lot=False`**，**`params.merge_with_H_exit=False`**，**`params.merge_with_X_st_limit=False`**，**`params.merge_with_O_block=False`**，**`params.merge_with_AC_bse=False`**，**`params.merge_with_AD_50w=False`**，**`params.universe_rule=sse_szse_common_stock`**，**`params.missing_security_class_policy=skip`**，**`params.inventory_lot_policy=fifo_by_buy_date`**，**`params.px_basis=unadj`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015`（写死冻结；禁 holdout；禁 null；params.Y≠实验字母 AE）**，**`params.ae0_primary_demo=invent_same_day_sell`（写死冻结；禁双挂）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_R=off`，`overlay_Q=off`，`overlay_M=off`，`overlay_A=off`。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AE0/AE1/AE2 当日回转腿贡献、ΔTurnover、ΔSellableNotional、ΔFail；分桶（当日新买又卖 / 盘后当 T+0 / vs R·Q·M·A）。  
- 自检布尔：AE2 是否 T+1+盘后不改；AE0 是否单一主报；AE1 是否盘后误开；是否未与 R/Q/M/A 混主结论；holdout 是否未反调；**是否未把实验字母 AE 与 params.Y 混用**；**是否未改 Y/Z/AA/AB/AC/AD 冻结补丁正文**。  
- **禁止输出**：具体买卖标的列表当「建议」；把普通股票 T+0 当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA/AB/AC/AD 及其他 A/D–AD 已交正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：普通 A 股交收前不得卖出；3.1.5 当日回转名单不含普通股票；盘后固定价格仍是当日成交、不改 T+1；卖出资金当日可再买与「股不能当日卖」分列。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AD，本页**新增实验 AE** 收成标准件，**不改口径主线**，**不改假设 A–AD 正文**。与实验 R/Q/M 分工：**R=ETF 假回转；Q=可转债回转；M=盘后通道落地；AE=普通股票假 T+0 / 盘后当绕开 T+1**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频买卖腿 + 证券类别 + 买入日批次即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-09-28；**fill_time=next_open 写死**；**stock_rotation_honest=t1 / same_day_buy_sellable_honest=False / aft_as_t0_channel_honest=False 写死**；diff_buckets 八桶写死冻结；**Y/G/N/Y2=0.02/0.01/0.05/0.015 写死冻结（params.Y≠实验字母 AE）**；**ae0_primary_demo=invent_same_day_sell 写死冻结（禁双挂）**；**风控补丁两条 2026-11-02 已写死待复检** |

---

## 变更

- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AE-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写死冻结（**params.Y≠实验字母 AE**；禁 null/holdout 标定）；② `params.ae0_primary_demo=invent_same_day_sell` 写死冻结（禁与 `invent_aft_as_t0` 双挂争主表）。**已写死待复检**；**不抢实验 A**；**不开回测**；**不改 Y/Z/AA/AB/AC/AD 及其他 A/D–AD 正文**。
- 2026-11-02：新建标准件（总管线：AD 补丁已交后写下一纸面 AE；Y/Z/AA/AB/AC/AD 补丁已交不改；清单止于 AD → 自 `事实与坑`「普通 A 股 T+1 / 3.1.4–3.1.5」+ R 旁路「B 类股票 T+1」选题，**与 A/H/X/E/M/O/AC/AD/R/Q 不撞主结论**；近邻 R=ETF 假回转、Q=转债回转、M=盘后通道，本页主测普通股票假 T+0；**实验字母 AE ≠ params.Y**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA/AB/AC/AD/A/D–AD 正文**）。
