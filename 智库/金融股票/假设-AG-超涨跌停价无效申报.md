# 假设 AG · 超涨跌停价限价申报仍记成交（无效申报被忽略 / 执行鸿沟）

更新：2026-11-02  
来源：总管线 / AF 补丁已交后并行写下一纸面 AG；清单原止于 AF，无 AG 节 → 自立实验 AG；选题自 `事实与坑`「超过涨跌幅限制或有效申报价格范围的申报为无效（深交所 3.3.18；上交所 3.3.16 同类）」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价保护限价）**分列**；**新建实验 AG**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「超涨跌停价限价单仍可进簿/成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA/AB/AC/AD/AE/AF 及其他 A/D–AF 已交正文与冻结补丁**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AF，本页自立实验 AG 标准件。与假设 A（涨停可成交性）**分列**：A 主测触及板上时买卖枯竭能否按板上价成交；本页主测**限价申报价格本身是否已越过当日涨跌停价**——超板价在主机侧为无效申报，与「板上有没有对手盘」不是同一腿。与假设 I（价格笼子）**分列**：I 主测连续竞价限价相对买卖一/基准价能挂多远（2%/十个价位）；本页主测相对**当日涨跌停限制价**超限即拒单，不得把笼子当成唯一价格闸门而放过超板单。与假设 F（涨跌停价取整）**分列**：F 主测限制价四舍五入标签；本页承接取整后的限制价去做「超限拒单」执行差。与假设 L（市价保护限价）**分列**：L 主测市价通道；本页主测**限价**超板。与假设 AF（单笔数量上限）**分列**：AF=数量；AG=价格超板。与假设 H/X/E/M/O/R/Q/AC/AD/AE **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AG** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AG / 假设-AG / hypothesis_id=AG / 组 AG0·AG1·AG2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AG 与 params 键名 `ag0_*` 以外的单字母/双字母实验页混读。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一成交时点、同一 T+1 下，把「限价申报价格**越过当日涨跌停限制价**」的单仍记进簿/成交，或把**价格笼子**当成唯一价格闸门而放过超板单，相对「超涨跌停限制价 = 无效申报拒单；笼子另页 I；板上枯竭另页 A」的 PIT 诚实组，会**系统性发明本应废单的超板路径并高估可成交名义**；差异应**集中在超板假成交 / 混用笼子当唯一闸门桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的超板假成交贡献差、废单率差、可成交名义差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在超板无效申报相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 超板无效申报 ≠ 板上可成交；≠ 价格笼子；≠ 市价保护限价

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AG
# params.asof_check_date                 写死默认 2026-09-28  # 事实与坑「超涨跌幅/有效申报范围=无效」核对锚
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；本页主测超板拒单，不抢 A 板上真数
# params.px_basis                        写死 unadj          # 限制价与申报价均未复权
# params.limit_pct_source                写死 board_st_day_effective  # 与 F/G/X 同向；禁复权价算板
# params.tick                            写死 0.01           # A 股股票默认；禁基金 0.001 主宇宙
# params.tag_cmp                         写死 ge_le          # 限制价取整比较与 F/A 对齐
# params.beyond_limit_policy_honest      写死 reject         # 诚实：买入申报价 > 涨停价 或 卖出申报价 < 跌停价 → 废单
# params.no_limit_day_policy             写死 skip_separate_bucket  # 无涨跌幅日（G/J）不套 ±板拒单；另桶；禁发明
# params.ag0_primary_demo                写死 invent_beyond_limit_fill  # 风控补丁冻结；主报：超板仍记成交；禁与 treat_cage_as_only_gate 双挂争主表
# params.ag0_invent_beyond_limit_fill    写死 True           # 天真主路径
# params.ag1_treat_cage_as_only_gate     写死 True           # 半泄露/混口径：只套笼子、放过超板
# params.ag1_invent_beyond_limit_fill    写死 False          # AG1 主病不在「完全忽略」，而在「笼子当唯一闸门」
# params.ag2_beyond_limit_policy         写死 reject
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A
# params.merge_with_I_cage               写死 False          # 笼子另页 I
# params.merge_with_F_round              写死 False          # 取整另页 F；本页承接取整后限制价
# params.merge_with_L_mkt                写死 False          # 市价保护限价另页 L
# params.merge_with_AF_qty_cap           写死 False          # 单笔数量上限另页 AF
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_Q_cb_rotation        写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.universe_rule                   写死 sse_szse_common_stock  # 沪深普通 A 股；ETF/转债/北交所不进主宇宙
# params.missing_limit_px_policy         写死 skip           # 缺前收/板块/限制价 → skip（禁静默当可挂）
# params.order_side_required             写死 True           # 缺买卖方向 → skip
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AG；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-09-28"
px_basis = "unadj"
limit_pct_source = "board_st_day_effective"
tick = 0.01
tag_cmp = "ge_le"
beyond_limit_policy_honest = "reject"
no_limit_day_policy = "skip_separate_bucket"
ag0_primary_demo = "invent_beyond_limit_fill"  # 风控补丁冻结；禁双挂
ag0_invent_beyond_limit_fill = True
ag1_treat_cage_as_only_gate = True
ag1_invent_beyond_limit_fill = False
ag2_beyond_limit_policy = "reject"
merge_with_A_fill = False
merge_with_I_cage = False
merge_with_F_round = False
merge_with_L_mkt = False
merge_with_AF_qty_cap = False
universe_rule = "sse_szse_common_stock"
missing_limit_px_policy = "skip"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 ag0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AG
G = 0.01
N = 0.05
Y2 = 0.015

def round_limit_px(preclose, pct, side):
    """限制价：先乘比例再四舍五入到 tick；与假设 F 同向；本页不重开取整主测。"""
    raw = preclose * (1.0 + pct) if side == "up" else preclose * (1.0 - pct)
    # 引擎须实现 F 同款：差不到 1 个价位则 ±1 tick；低于 1 tick 则以 1 tick
    return round_to_tick(raw, tick)

def is_beyond_day_limit(order_px, side, limit_up, limit_down, is_no_limit_day, group):
    """超板判定。无板日另桶；AG0 发明成交；AG1 只当笼子过了就放过；AG2 reject。"""
    if is_no_limit_day:
        return False, "no_limit_day_skip"
    if group == "AG0" and ag0_invent_beyond_limit_fill:
        return False, "invent_fill_beyond"  # 假装未超板 / 仍可成
    # AG1：假定笼子已过，不再做涨跌停超限拒单
    if group == "AG1" and ag1_treat_cage_as_only_gate:
        return False, "cage_only_gate_pass"
    # AG2 诚实
    if side == "buy" and order_px > limit_up:
        return True, "reject_above_limit_up"
    if side == "sell" and order_px < limit_down:
        return True, "reject_below_limit_down"
    return False, "ok"

def apply_beyond_limit(order_px, side, preclose, board_pct, is_no_limit_day, group):
    limit_up = round_limit_px(preclose, board_pct, "up")
    limit_down = round_limit_px(preclose, board_pct, "down")
    beyond, reason = is_beyond_day_limit(order_px, side, limit_up, limit_down, is_no_limit_day, group)
    if beyond and beyond_limit_policy_honest == "reject" and group == "AG2":
        return 0, reason
    if group == "AG0" and reason == "invent_fill_beyond":
        return order_px, reason  # 假路径：仍按拟挂价/引擎成交假设
    if group == "AG1" and reason == "cage_only_gate_pass":
        return order_px, reason
    return order_px, reason
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺前收/板块/涨跌幅比例却硬判超板、把 A 板上枯竭 / I 笼子 / F 取整主测 / L 市价 / AF 数量上限混进本页主表、用复权价算限制价或申报价、无涨跌幅日却静默套 ±板拒单、超板却在诚实组静默全成 → **跳过该日该券该腿**，不静默记成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AG）

| 组 | 超板无效申报 | 说明 |
|----|--------------|------|
| AG0 天真 | 超板仍记进簿/成交（按 `ag0_primary_demo` 单一主报） | 发明超板路径 |
| AG1 半泄露/混口径 | 只把价格笼子当闸门，放过超涨跌停价单 | 把 I 当成唯一价格有效性 |
| AG2 PIT 诚实 | 买入价 > 涨停价或卖出价 < 跌停价 → reject；无板日另桶 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测超板无效申报执行诚信**，不主测板上枯竭（见 A）、不主测笼子远近（见 I）、不主测限制价取整（见 F）、不主测市价保护限价（见 L）、不主测单笔数量上限（见 AF）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_A_fill=False` / `merge_with_I_cage=False` / `merge_with_F_round=False` / `merge_with_L_mkt=False` / `merge_with_AF_qty_cap=False` / `merge_with_H_exit=False` / `merge_with_X_st_limit=False` / `merge_with_E_lot=False` / `merge_with_M_aft=False` / `merge_with_O_block=False` / `merge_with_R_etf_rotation=False` / `merge_with_Q_cb_rotation=False` / `merge_with_AC_bse=False` / `merge_with_AD_50w=False` / `merge_with_AE_stock_t0=False`（写死）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 可成交名义/净值差显著门槛；≠实验字母 AG
params.G                            = 0.01                      # 超板假成交桶相对对照差
params.N                            = 0.05                      # 失败/废单率差门槛
params.Y2                           = 0.015                     # AG1（笼子当唯一闸门）相对 AG2 专项门槛
params.ag0_primary_demo             = invent_beyond_limit_fill  # 主报超板仍成交；禁与 treat_cage_as_only_gate 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股股票（`universe_rule=sse_szse_common_stock`），须含板块涨跌幅比例与交易所前收盘。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺前收/板块；用复权价；无涨跌幅日硬套 ±板拒单进主表；把 A/I/F/L/AF 主结论并进本页主表。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - **覆盖主板 ST 2026-07-06 切日**（涨跌幅比例另页 X；本页只要求限制价 PIT 后做超板拒单，不重开 5%→10% 主测）。  
- **PIT 切片原则**：限制比例、前收盘/除权参考价、是否无板日，一律按成交日当时；**禁止**用核对日规则铺满；限制价取整与 F 同向，**本页不另开取整实验**。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ag0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AG0 − AG2**：超板仍成交相对诚实拒单——假路径 / 可成交名义吹胖。  
2. **AG1 − AG2**：只套笼子放过超板相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_beyond_limit_up",    # 买入超涨停仍成
  "invent_beyond_limit_down",  # 卖出超跌停仍成
  "cage_only_gate",            # 混用笼子当唯一闸门
  "no_limit_day_miscategorized", # 无板日误套 ±板拒单（诊断）
  "honest_reject_beyond",      # 对照诚实废单
  "vs_A_fill",                 # 对照声明：板上枯竭另页 A
  "vs_I_cage",                 # 对照声明：笼子另页 I
  "vs_F_round",                # 对照声明：取整另页 F
  "vs_L_mkt",                  # 对照声明：市价保护限价另页 L
  "vs_AF_qty_cap",             # 对照声明：数量上限另页 AF
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义差 ΔNotional（AG0/AG1 相对 AG2）；  
2. 超板假成交腿贡献差 ΔBeyond；  
3. 废单/失败率差 ΔFail；  
4. （可选）腿净值差 ΔPnL。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔPnL| **≥ params.Y** 或 |ΔBeyond 桶贡献| **≥ params.G** 或 |ΔNotional_(AG1−AG2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「超板无效申报执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AG 无关；风控补丁 2026-11-02）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/净值差显著门槛（≠实验字母 AG） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 超板假成交桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AG1−AG2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-09-28` |
| fill_time | 成交时点 | **写死** `next_open` |
| beyond_limit_policy_honest | 诚实超板处理 | **写死** `reject` |
| ag0_primary_demo | 天真主报枚举 | **写死冻结** `invent_beyond_limit_fill`（风控补丁 2026-11-02；禁双挂） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已写入 params 并冻结（风控补丁 2026-11-02；**`params.Y`≠实验字母 AG**）；**禁止用 holdout / 事后显著性改口**；**`ag0_primary_demo=invent_beyond_limit_fill` 单一主报，禁与 treat_cage_as_only_gate 双挂争主表**。

**失败/不显著**：差异落在噪声带内或均匀散在非超板对照桶——结论栏写明，不得改口称「超板申报差不多可忽略」或「这类票更能挂远价」。

结论栏：空。跑完只写「该假设下超板假成交/废单率差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验超板无效申报执行诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（PIT 限制价、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价算限制价或申报价**。  
2. **把 A 板上枯竭、I 笼子远近、F 取整主测、L 市价保护限价、AF 数量上限混进本页主结论**。  
3. **无涨跌幅日静默套 ±板拒单进主表**（须 `no_limit_day_policy` 另桶或 skip）。  
4. **诚实组超板仍静默全成**（须 reject/skip）。  
5. **缺前收/板块却静默当可挂任意远价**。  
6. **宇宙泄露 / holdout 反调**：看完 OOS 再改 `ag0_primary_demo` 或 **`params.Y` 等门槛**。  
7. **差异不集中在超板/混口径桶却仍写「系统性超板执行鸿沟」而不改表述**。  
8. **把差异写成「这类票能挂远价」或选股公式**。  
9. **把实验字母 AG 与 `params.Y` 混改**；或改写 Y/Z/AA/AB/AC/AD/AE/AF 及其他 A/D–AF 已冻正文。  
10. **把有效申报价格范围（笼子/无板日 900% 等）整段并进本页主结论却不声明另页 I/J**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | 沪深普通股为主 |
| board / list_board | 主板/创业/科创 | 切涨跌幅比例；缺 → skip |
| exchange_preclose / 除权参考价 | 算限制价 | 未复权；缺 → skip |
| board_limit_pct（按日 PIT） | ±比例 | 可与 G/X 表复用；禁复权 |
| is_no_limit_day | 无涨跌幅日 | 另桶；禁主表硬套 |
| order_side | 买/卖 | 缺 → skip |
| order_px / intended_limit_px | 拟挂限价 | 主测超板 |
| fill_qty / fill_notional（可选） | 成交对照 | 禁复权主结论 |
| unadj_ohlc（可选） | 旁路核对 | 禁用复权判板 |

**明确**：不依赖聚宽；**不要求新开 Level-2**——有未复权前收 + 板块涨跌幅 PIT + 拟挂限价 + 买卖方向即可起步；缺关键字段 → `fail_policy=skip`。主窗 2019-01-01..2026-09-30。笼子/盘口字段**不**作为本页主跑必需（笼子另页 I）。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=AG`（**实验字母**），`groups=[AG0,AG1,AG2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-09-28`**，**`params.fill_time=next_open`（写死）**，**`params.px_basis=unadj`**，**`params.limit_pct_source=board_st_day_effective`**，**`params.tick=0.01`**，**`params.tag_cmp=ge_le`**，**`params.beyond_limit_policy_honest=reject`**，**`params.no_limit_day_policy=skip_separate_bucket`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_I_cage=False`**，**`params.merge_with_F_round=False`**，**`params.merge_with_L_mkt=False`**，**`params.merge_with_AF_qty_cap=False`**，**`params.merge_with_H_exit=False`**，**`params.merge_with_X_st_limit=False`**，**`params.merge_with_E_lot=False`**，**`params.merge_with_M_aft=False`**，**`params.merge_with_O_block=False`**，**`params.merge_with_R_etf_rotation=False`**，**`params.merge_with_Q_cb_rotation=False`**，**`params.merge_with_AC_bse=False`**，**`params.merge_with_AD_50w=False`**，**`params.merge_with_AE_stock_t0=False`**，**`params.universe_rule=sse_szse_common_stock`**，**`params.missing_limit_px_policy=skip`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015`（写死冻结；禁 holdout；禁 null；params.Y≠实验字母 AG）**，**`params.ag0_primary_demo=invent_beyond_limit_fill`（写死冻结；禁双挂）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_I=off`，`overlay_F=off`，`overlay_L=off`，`overlay_AF=off`。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AG0/AG1/AG2 可成交名义、ΔBeyond、ΔFail；分桶（超板上/下 / 笼子混口径 / 无板日误套 / vs A·I·F·L·AF）。  
- 自检布尔：AG2 是否超板 reject；AG0 是否单一主报；AG1 是否笼子当唯一闸门；是否未与 A/I/F/L/AF 混主结论；holdout 是否未反调；**是否未把实验字母 AG 与 params.Y 混用**；**是否未改 Y/Z/AA/AB/AC/AD/AE/AF 冻结补丁正文**。  
- **禁止输出**：具体买卖标的列表当「建议」；把超板可成当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA/AB/AC/AD/AE/AF 及其他 A/D–AF 已交正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：超过涨跌幅限制或有效申报价格范围的申报为无效；笼子管挂多远、板上枯竭管能不能成交，不得合成一句却放过超板单。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AF，本页**新增实验 AG** 收成标准件，**不改口径主线**，**不改假设 A–AF 正文**。与实验 A/I/F/L/AF 分工：**A=板上枯竭可成交；I=笼子远近；F=限制价取整；L=市价保护限价；AF=单笔数量上限；AG=超涨跌停价限价申报无效拒单**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；未复权前收 + 涨跌幅 PIT + 拟挂限价即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-09-28；**fill_time=next_open 写死**；**beyond_limit_policy_honest=reject / no_limit_day_policy=skip_separate_bucket 写死**；diff_buckets 十桶写死冻结；**Y/G/N/Y2=0.02/0.01/0.05/0.015 写死冻结（params.Y≠实验字母 AG）**；**ag0_primary_demo=invent_beyond_limit_fill 写死冻结（禁双挂）**；**风控补丁两条 2026-11-02 已写死待复检** |

---

## 变更

- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AG-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写死冻结（**params.Y≠实验字母 AG**；禁 null/holdout 标定）；② `params.ag0_primary_demo=invent_beyond_limit_fill` 写死冻结（禁与 `treat_cage_as_only_gate` 双挂争主表）。**已写死待复检**；**不抢实验 A**；**不开回测**；**不改 Y/Z/AA/AB/AC/AD/AE/AF 及其他 A/D–AF 正文**。
- 2026-11-02：新建标准件（总管线：AF 补丁已交后写下一纸面 AG；Y/Z/AA/AB/AC/AD/AE/AF 补丁已交不改；清单止于 AF → 自 `事实与坑`「超涨跌幅/有效申报范围=无效申报」选题，**与 A/H/X/E/M/O/AC/AD/AE/AF/R/Q 及 I/F/L 不撞主结论**；近邻 A=板上枯竭、I=笼子、F=取整、L=市价保护、AF=数量上限，本页主测超板限价无效拒单；**实验字母 AG ≠ params.Y**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA/AB/AC/AD/AE/AF/A/D–AF 正文**）。