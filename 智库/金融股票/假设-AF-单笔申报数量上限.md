# 假设 AF · 单笔申报数量上限被忽略 / 误套板块（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AE 补丁已交后并行写下一纸面 AF；清单原止于 AE，无 AF 节 → 自立实验 AF；选题自 `事实与坑`「单笔上限默认 100 万股；创业板限价 ≤30 万 / 市价 ≤15 万；科创板限价 ≤10 万 / 市价 ≤5 万」+ `假设-E` 旁路「`chinext_order_cap=off`（创业板单笔上限不主测）」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手起买）/ M（盘后补成交）/ O（大宗门槛）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示累计买入 50 万）/ AE（普通股票假 T+0）**分列**；**新建实验 AF**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「任意大单可挂」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA/AB/AC/AD/AE 及其他 A/D–AE 已交正文与冻结补丁**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AE，本页自立实验 AF 标准件。与假设 E（整手与科创板 200 股起买）**分列**：E 主测**最小**手数/起买与零股卖出，并把创业板单笔上限旁路 `chinext_order_cap=off`；本页**主测**把该上限打开后的执行差——忽略单笔上限、或把主板默认 100 万误套到创业/科创（或订单类型限价/市价互抄）。与假设 AD（风险警示累计买入 50 万股）**分列**：AD 是**当日累计**买上限；本页是**单笔申报**上限，不重开 ST 累计。与假设 O（大宗门槛）**分列**：O 主测大宗**最低** 30 万股/200 万金额与通道混用；本页主测竞价（及声明桶内盘后）**最高**单笔。与假设 A（板上）/ H / X / M / R / Q / AC / AE **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AF** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AF / 假设-AF / hypothesis_id=AF / 组 AF0·AF1·AF2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AF 与 params 键名 `af0_*` 以外的单字母/双字母实验页混读。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一成交时点、同一 T+1 下，把竞价单笔申报数量上限**整段忽略**（任意大单当可进簿），或把**主板默认 100 万股**误套到创业板/科创板（或不分限价/市价互抄上限），相对「主板默认 ≤100 万；创业板限价 ≤30 万、市价 ≤15 万；科创板限价 ≤10 万、市价 ≤5 万；超限按 fail_policy 废单/截断写死」的 PIT 诚实组，会**系统性高估可挂名义并发明本应废单的超大单路径**；差异应**集中在忽略上限 / 误套板块·订单类型桶**，而不是随机散开。

证伪方向：若天真组 / 误套组相对诚实组的可挂名义差、超限废单率差、截断贡献差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在单笔上限相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 单笔上限 ≠ 整手起买；≠ 风险警示累计 50 万；≠ 大宗最低门槛

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AF
# params.asof_check_date                 写死默认 2026-10-05  # 事实与坑「整手/单笔上限」核对锚
# params.fill_time                        写死 next_open      # 成交腿与 A/D/E 对齐；本页主测单笔上限，不抢 A 板上真数
# params.main_limit_max_shares           写死 1000000        # 诚实：主板（及默认）限价/一般单笔上限 100 万股
# params.main_market_max_shares          写死 1000000        # 诚实默认：主板市价同档占位（若引擎分类型，按当时文本；禁发明更松）
# params.chinext_limit_max_shares        写死 300000         # 诚实：创业板限价 ≤30 万
# params.chinext_market_max_shares       写死 150000         # 诚实：创业板市价 ≤15 万
# params.star_limit_max_shares           写死 100000         # 诚实：科创限价 ≤10 万（与 E 同向；本页主测上限腿）
# params.star_market_max_shares          写死 50000          # 诚实：科创市价 ≤5 万
# params.star_aft_max_shares             写死 1000000        # 声明桶：科创盘后收盘定价 ≤100 万；默认不并进竞价主表
# params.aft_order_cap_in_main           写死 False          # 诚实：盘后数量条款不默认并进连续竞价主测
# params.af0_primary_demo                写死 ignore_max_order_shares  # 风控补丁冻结；主报：整段忽略单笔上限；禁与 misapply_board_caps 双挂争主表
# params.af0_ignore_max                  写死 True           # 天真主路径
# params.af1_misapply_main_1m            写死 True           # 半泄露：创业/科创也按主板 100 万
# params.af1_swap_limit_market           写死 False          # 可叠诊断：限价/市价上限互抄；主报仍以 af0_primary_demo 为准
# params.af2_apply_board_caps            写死 True           # PIT：按板块+订单类型切上限
# params.merge_with_E_lot                写死 False          # 整手/起买另页 E；本页承接 E 的 chinext_order_cap 旁路
# params.merge_with_AD_50w               写死 False          # 风险警示累计 50 万另页 AD
# params.merge_with_O_block              写死 False          # 大宗最低门槛另页 O
# params.merge_with_A_fill               写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_Q_cb_rotation        写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.universe_rule                   写死 sse_szse_common_stock  # 沪深普通 A 股；ETF/转债/北交所不进主宇宙
# params.missing_board_policy            写死 skip           # 缺板块 → skip（禁静默当主板 100 万）
# params.missing_order_type_policy       写死 assume_limit   # 缺订单类型默认按限价上限；须在报告声明
# params.over_cap_policy_honest          写死 reject         # 诚实：超限 → 废单（与 fail_policy=skip 同向）；禁静默全成
# params.px_basis                        写死 unadj
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AF；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-05"
main_limit_max_shares = 1_000_000
chinext_limit_max_shares = 300_000
chinext_market_max_shares = 150_000
star_limit_max_shares = 100_000
star_market_max_shares = 50_000
aft_order_cap_in_main = False
af0_primary_demo = "ignore_max_order_shares"  # 风控补丁冻结；禁双挂
af0_ignore_max = True
af1_misapply_main_1m = True
af2_apply_board_caps = True
merge_with_E_lot = False
merge_with_AD_50w = False
merge_with_O_block = False
merge_with_A_fill = False
merge_with_H_exit = False
merge_with_X_st_limit = False
merge_with_M_aft = False
merge_with_R_etf_rotation = False
merge_with_Q_cb_rotation = False
merge_with_AC_bse = False
merge_with_AE_stock_t0 = False
universe_rule = "sse_szse_common_stock"
missing_board_policy = "skip"
over_cap_policy_honest = "reject"
px_basis = "unadj"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 af0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AF
G = 0.01
N = 0.05
Y2 = 0.015

def max_shares(board, order_type, group):
    """单笔上限（股）。AF0 忽略；AF1 创业/科创误套主板 100 万；AF2 按板块+类型。"""
    if group == "AF0" and af0_ignore_max:
        return None  # 无上限
    if group == "AF1" and af1_misapply_main_1m and board in ("chinext", "star"):
        return main_limit_max_shares
    # AF2 / 主板诚实
    if board == "chinext":
        return chinext_market_max_shares if order_type == "market" else chinext_limit_max_shares
    if board == "star":
        return star_market_max_shares if order_type == "market" else star_limit_max_shares
    return main_limit_max_shares

def apply_cap(qty, board, order_type, group):
    cap = max_shares(board, order_type, group)
    if cap is None:
        return qty, "ok_no_cap"
    if qty <= cap:
        return qty, "ok"
    if over_cap_policy_honest == "reject" and group == "AF2":
        return 0, "reject_over_cap"
    if group == "AF0":
        return qty, "invent_over_cap_fill"
    # AF1 误套后仍可能超真实上限 → 记假路径
    return qty, "misapply_then_over_true_cap"
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺板块却硬套主板 100 万、把 E 整手起买 / AD 累计 50 万 / O 大宗最低门槛混进本页主表、用复权价、超限却静默全成（诚实组）、把盘后科创 100 万上限并进连续竞价主表却不声明 → **跳过该日该券该腿**，不静默记成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AF）

| 组 | 单笔上限 | 说明 |
|----|----------|------|
| AF0 天真 | 整段忽略上限（按 `af0_primary_demo` 单一主报） | 任意大单可挂 |
| AF1 半泄露/误套 | 创业/科创也按主板 100 万（可叠限价/市价互抄诊断） | 误套板块或订单类型 |
| AF2 PIT 诚实 | 主板 100 万；创业限价 30 万/市价 15 万；科创限价 10 万/市价 5 万；超限 reject | 与事实与坑同向；承接 E 旁路 |

同一信号、同一沪深普通 A 股宇宙。本页**主测单笔上限执行诚信**，不主测整手起买（见 E）、不主测风险警示累计买（见 AD）、不主测大宗最低门槛（见 O）、不主测板上可成交（见 A）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_E_lot=False` / `merge_with_AD_50w=False` / `merge_with_O_block=False` / `merge_with_A_fill=False` / `merge_with_H_exit=False` / `merge_with_X_st_limit=False` / `merge_with_M_aft=False` / `merge_with_R_etf_rotation=False` / `merge_with_Q_cb_rotation=False` / `merge_with_AC_bse=False` / `merge_with_AE_stock_t0=False`（写死）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 可挂名义/净值差显著门槛；≠实验字母 AF
params.G                            = 0.01                      # 忽略/误套桶相对对照差
params.N                            = 0.05                      # 失败/废单率差门槛
params.Y2                           = 0.015                     # AF1（误套主板 100 万）相对 AF2 专项门槛
params.af0_primary_demo             = ignore_max_order_shares   # 主报忽略上限；禁与 misapply_board_caps 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股股票（`universe_rule=sse_szse_common_stock`），须含主板 / 创业板 / 科创板标记。ETF、可转债、北交所、大宗只进「对照声明」桶，不进主跑。  
- **排除（默认）**：缺板块；用复权价；把 E/AD/O/A 主结论并进本页主表；盘后数量条款静默并进竞价。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - **覆盖科创开市起 / 创业板注册制后**（单笔上限条款以当时文本为准；不得用核对日规则铺满更早样本若条文有变——变日未核到则 skip 该切日前误用现行句）。  
- **PIT 切片原则**：板块、订单类型、单笔上限，一律按申报/成交日当时；**禁止**用核对日「某券商拆单习惯」回放；**禁止**把创业板上限写成与主板同档却不改表述。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `af0_primary_demo`、误套开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AF0 − AF2**：忽略单笔上限相对诚实——可挂名义吹胖 / 超限假成交。  
2. **AF1 − AF2**：创业·科创误套主板 100 万相对诚实——假路径 / 假废单漏检。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "ignore_max_cap",            # 忽略上限
  "misapply_main_1m",          # 创业/科创误套主板 100 万
  "limit_vs_market_swap",      # 限价/市价上限互抄（诊断）
  "star_over_100k_or_50k",     # 科创超限价 10 万 / 市价 5 万
  "chinext_over_300k_or_150k", # 创业超限价 30 万 / 市价 15 万
  "honest_reject_over_cap",    # 对照诚实废单
  "vs_E_lot_floor",            # 对照声明：整手起买另页 E
  "vs_AD_50w_cum",             # 对照声明：累计 50 万另页 AD
  "vs_O_block_floor",          # 对照声明：大宗最低门槛另页 O
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可挂名义差 ΔNotional（AF0/AF1 相对 AF2）；  
2. 超限腿贡献差 ΔOverCap；  
3. 废单/失败率差 ΔFail；  
4. （可选）腿净值差 ΔPnL；  
5. 截断贡献差 ΔClip（若引擎用截断而非 reject）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔPnL| **≥ params.Y** 或 |ΔOverCap 桶贡献| **≥ params.G** 或 |ΔNotional_(AF1−AF2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「单笔上限执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；禁 holdout 标定；与实验字母 AF 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 可挂名义/净值差显著门槛（≠实验字母 AF） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 忽略/误套桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AF1−AF2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-05` |
| fill_time | 成交时点 | **写死** `next_open` |
| main/chinext/star_*_max_shares | 诚实上限表 | **写死**见 §2.1 |
| af0_primary_demo | 天真主报枚举 | **写死冻结** `ignore_max_order_shares`（风控补丁 2026-11-02；禁双挂） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已写入 params 并冻结（风控补丁 2026-11-02；**`params.Y`≠实验字母 AF**）；**禁止用 holdout / 事后显著性改口**；**`af0_primary_demo=ignore_max_order_shares` 单一主报，禁与 misapply_board_caps 双挂争主表**。

**失败/不显著**：差异落在噪声带内或均匀散在非单笔上限对照桶——结论栏写明，不得改口称「单笔上限差不多可忽略」或「这类票更能挂大单」。

结论栏：空。跑完只写「该假设下可挂名义/废单率差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验单笔上限执行诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（PIT 上限表、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价做名义金额**。  
2. **把 E 的整手起买、AD 的累计 50 万、O 的大宗最低门槛混进本页主结论**。  
3. **缺板块却静默当主板 100 万可挂**。  
4. **诚实组超限仍静默全成**（须 reject/skip 或事先写死拆单/截断并计桶）。  
5. **把科创盘后 200～100 万默认并进连续竞价主表**。  
6. **宇宙泄露 / holdout 反调**：看完 OOS 再改 `af0_primary_demo` 或 **`params.Y` 等门槛**。  
7. **差异不集中在忽略/误套桶却仍写「系统性单笔上限鸿沟」而不改表述**。  
8. **把差异写成「这类票能挂大单」或选股公式**。  
9. **把实验字母 AF 与 `params.Y` 混改**；或改写 Y/Z/AA/AB/AC/AD/AE 及其他 A/D–AE 已冻正文。  
10. **把 ETF/可转债数量条款用股票上限回放却不改宇宙**（另页或不进主宇宙）。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | 沪深普通股为主 |
| board / list_board | 主板/创业/科创 | 缺 → skip |
| order_type（限价/市价） | 切上限 | 缺 → assume_limit 并声明 |
| intended_qty / order_shares | 拟挂股数 | 主测超限路径 |
| fill_qty / fill_notional（可选） | 成交对照 | 禁复权主结论 |
| is_aft_session（可选） | 盘后数量声明桶 | 默认不并进主表 |
| unadj_px（可选） | 名义金额 | 禁复权 |

**明确**：不依赖聚宽；**不要求新开 Level-2**——有日频拟挂股数 + 板块 +（最好）订单类型即可起步；缺板块 → `fail_policy=skip`。主窗 2019-01-01..2026-09-30。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=AF`（**实验字母**），`groups=[AF0,AF1,AF2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-05`**，**`params.fill_time=next_open`（写死）**，**`params.main_limit_max_shares=1000000`**，**`params.chinext_limit_max_shares=300000`**，**`params.chinext_market_max_shares=150000`**，**`params.star_limit_max_shares=100000`**，**`params.star_market_max_shares=50000`**，**`params.aft_order_cap_in_main=False`**，**`params.over_cap_policy_honest=reject`**，**`params.merge_with_E_lot=False`**，**`params.merge_with_AD_50w=False`**，**`params.merge_with_O_block=False`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_H_exit=False`**，**`params.merge_with_X_st_limit=False`**，**`params.merge_with_M_aft=False`**，**`params.merge_with_R_etf_rotation=False`**，**`params.merge_with_Q_cb_rotation=False`**，**`params.merge_with_AC_bse=False`**，**`params.merge_with_AE_stock_t0=False`**，**`params.universe_rule=sse_szse_common_stock`**，**`params.missing_board_policy=skip`**，**`params.px_basis=unadj`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015`（写死冻结；禁 holdout；禁 null；params.Y≠实验字母 AF）**，**`params.af0_primary_demo=ignore_max_order_shares`（写死冻结；禁双挂）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_E=off`，`overlay_AD=off`，`overlay_O=off`，`overlay_A=off`。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AF0/AF1/AF2 可挂名义、ΔOverCap、ΔFail；分桶（忽略上限 / 误套主板 100 万 / 创业·科创超限 / vs E·AD·O）。  
- 自检布尔：AF2 是否按板块+类型切上限；AF0 是否单一主报；AF1 是否误套；是否未与 E/AD/O/A 混主结论；holdout 是否未反调；**是否未把实验字母 AF 与 params.Y 混用**；**是否未改 Y/Z/AA/AB/AC/AD/AE 冻结补丁正文**。  
- **禁止输出**：具体买卖标的列表当「建议」；把无上限当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA/AB/AC/AD/AE 及其他 A/D–AE 已交正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：主板单笔默认 ≤100 万股；创业板限价 ≤30 万、市价 ≤15 万；科创板限价 ≤10 万、市价 ≤5 万；整手起买另页 E；风险警示累计 50 万另页 AD；大宗最低门槛另页 O。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AE，本页**新增实验 AF** 收成标准件，**不改口径主线**，**不改假设 A–AE 正文**。与实验 E/AD/O 分工：**E=整手起买（旁路单笔上限）；AD=风险警示累计买；O=大宗最低门槛；AF=竞价单笔上限忽略/误套**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；拟挂股数 + 板块 + 订单类型即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-05；**fill_time=next_open 写死**；诚实上限表写死；diff_buckets 九桶写死冻结；**Y/G/N/Y2=0.02/0.01/0.05/0.015 写死冻结（params.Y≠实验字母 AF）**；**af0_primary_demo=ignore_max_order_shares 写死冻结（禁双挂）**；**风控补丁两条 2026-11-02 已写死待复检** |

---

## 变更

- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AF-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写死冻结（**params.Y≠实验字母 AF**；禁 null/holdout 标定）；② `params.af0_primary_demo=ignore_max_order_shares` 写死冻结（禁与 `misapply_board_caps` 双挂争主表）。**已写死待复检**；**不抢实验 A**；**不开回测**；**不改 Y/Z/AA/AB/AC/AD/AE 及其他 A/D–AE 正文**。
- 2026-11-02：新建标准件（总管线：AE 补丁已交后写下一纸面 AF；Y/Z/AA/AB/AC/AD/AE 补丁已交不改；清单止于 AE → 自 `事实与坑`「单笔上限 100 万 / 创业 30·15 万 / 科创 10·5 万」+ E 旁路 `chinext_order_cap=off` 选题，**与 A/H/X/E/M/O/AC/AD/AE/R/Q 不撞主结论**；近邻 E=整手起买、AD=累计 50 万、O=大宗最低门槛，本页主测单笔上限忽略/误套；**实验字母 AF ≠ params.Y**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA/AB/AC/AD/AE/A/D–AE 正文**）。