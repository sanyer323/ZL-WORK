# 假设 AH · 集合竞价不可撤窗内假撤改单（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AG 补丁已交后并行写下一纸面 AH；清单原止于 AG，无 AH 节 → 自立实验 AH；选题自 `事实与坑`「9:20–9:25、14:57–15:00 不接受撤单（上交所 3.3.1；深交所同口径）」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理期）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价保护限价）/ N（收盘机制与假 GTC）/ Y（集合量计入日线）**分列**；**新建实验 AH**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「集合竞价不可撤窗内仍可撤单/改单并改写开收盘成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA/AB/AC/AD/AE/AF/AG 及其他 A/D–AG 已交正文与冻结补丁**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AG，本页自立实验 AH 标准件。与假设 **H（退市整理期）** **硬分列**：H = 摘牌前整理窗长度/首日无板/指数剔除；本页 = **当日**开盘集合 9:20–9:25 与收盘集合 14:57–15:00 **不可撤窗**内是否仍允许撤改。双字母 **AH ≠ 单字母 H**。与假设 **N（收盘机制与假 GTC）** **分列**：N 主测收盘价产生方式 PIT + **隔夜**限价假 GTC；本页主测**当日**不可撤窗内的假撤改，不重开隔夜有效、不重开沪市收盘切日。与假设 **Y（集合竞价量计入日线）** **分列**：Y 主测集合量是否进连续流动性分母；本页主测撤单合法性，不重开量分母。与假设 A/X/E/M/O/R/Q/AC/AD/AE/AF/AG/I/F/L **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AH** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AH / 假设-AH / hypothesis_id=AH / 组 AH0·AH1·AH2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AH 与单字母实验 **H**、或 params 键名 `ah0_*` 以外的实验页混读。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，允许在开盘集合 **9:20–9:25** 或收盘集合 **14:57–15:00** 的**不可撤窗**内撤单/改单，并据此改写开盘或收盘成交路径，相对「该两窗禁止撤单，只能按当时已接受申报撮合；窗内撤改记无效」的 PIT 诚实组，会**系统性发明改簿路径并高估可成交质量 / 低估废单与错价冲击**；差异应**集中在开盘不可撤窗假撤改 / 收盘不可撤窗假撤改桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假撤改贡献差、可成交名义/冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在不可撤窗相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 不可撤窗 ≠ 隔夜假 GTC；≠ 集合量分母；≠ 退市整理窗

```
# 配置写死键（见 §7；值待预检项见 §4.2 / 待预检键）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AH；≠ 实验字母 H
# params.asof_check_date                 写死默认 2026-10-19  # 事实与坑会话/撤单核对锚（与 N 同批会话规则）
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；收盘窗冲击作旁路指标；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.open_nocancel_window            写死 09:20-09:25    # 开盘集合不可撤窗（上交所 3.3.1）
# params.close_nocancel_window           写死 14:57-15:00    # 收盘集合不可撤窗
# params.nocancel_policy_honest          写死 reject_cancel_replace  # 诚实：窗内撤/改 → 无效
# params.ah0_primary_demo                待预检（建议 invent_cancel_in_nocancel_window）  # 主报：窗内仍允许撤单并改写成交；禁与 invent_replace_improve_fill 双挂
# params.ah0_invent_cancel_in_nocancel   写死 True           # 天真主路径
# params.ah0_invent_replace_improve_fill 写死 False          # 诊断可叠；主报以 ah0_primary_demo 为准
# params.ah1_open_only_invent            写死 True           # 半泄露：只在开盘不可撤窗发明撤改，收盘窗按诚实
# params.ah1_close_honest                写死 True
# params.ah2_nocancel_policy             写死 reject_cancel_replace
# params.merge_with_N_close_gtc          写死 False          # 隔夜假 GTC / 收盘价机制另页 N
# params.merge_with_Y_call_vol           写死 False          # 集合量分母另页 Y
# params.merge_with_H_exit               写死 False          # 退市整理另页 H（AH≠H）
# params.merge_with_A_fill               写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_Q_cb_rotation        写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_L_mkt                写死 False
# params.universe_rule                   写死 sse_szse_common_stock  # 沪深普通 A 股；ETF/转债/北交所不进主宇宙
# params.missing_session_clock_policy    写死 skip           # 缺会话钟/申报时戳 → skip（禁静默当可撤）
# params.day_freq_proxy                  写死 open_close_path_sensitivity  # 日频无 L2 时只报「不可撤窗假撤改」敏感性档；禁假装精确复盘簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  待预检（建议 0.02/0.01/0.05/0.015）；params.Y≠实验字母 AH；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-19"
px_basis = "unadj"
open_nocancel_window = "09:20-09:25"
close_nocancel_window = "14:57-15:00"
nocancel_policy_honest = "reject_cancel_replace"
ah0_primary_demo = "invent_cancel_in_nocancel_window"  # 建议值；待预检写死
ah0_invent_cancel_in_nocancel = True
ah0_invent_replace_improve_fill = False
ah1_open_only_invent = True
ah1_close_honest = True
ah2_nocancel_policy = "reject_cancel_replace"
merge_with_N_close_gtc = False
merge_with_Y_call_vol = False
merge_with_H_exit = False
universe_rule = "sse_szse_common_stock"
missing_session_clock_policy = "skip"
day_freq_proxy = "open_close_path_sensitivity"

# 拉数前冻结建议（待预检）；禁 holdout / 事后改口 / 禁跑后改 ah0_primary_demo
Y = 0.02   # 建议；相对门槛 ≠ 实验字母 AH
G = 0.01
N = 0.05
Y2 = 0.015

def in_nocancel_window(ts, which):
    """which in {open, close}；按 Asia/Shanghai 会话钟。"""
    # 实现侧用 exchange session clock；缺时戳 → missing_session_clock_policy
    pass

def apply_cancel_replace(order, action, ts, group):
    """窗内撤/改：AH0 发明成功；AH1 仅开盘窗发明；AH2 reject。"""
    open_hit = in_nocancel_window(ts, "open")
    close_hit = in_nocancel_window(ts, "close")
    if group == "AH0" and ah0_invent_cancel_in_nocancel and (open_hit or close_hit):
        return "invent_cancel_ok", order  # 假路径：改簿成功
    if group == "AH1" and ah1_open_only_invent and open_hit:
        return "invent_open_cancel_ok", order
    if group == "AH1" and ah1_close_honest and close_hit:
        return "reject_close_nocancel", None
    if (open_hit or close_hit) and group == "AH2":
        return "reject_nocancel", None
    return "ok_outside_window", order
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺会话钟/申报时戳却硬判可撤、把 N 隔夜假 GTC / Y 集合量分母 / H 整理窗混进本页主表、日频无时戳却假装精确复盘簿内撤改、诚实组窗内撤改仍静默成功 → **跳过该日该券该腿**，不静默记改簿成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AH）

| 组 | 不可撤窗撤改 | 说明 |
|----|--------------|------|
| AH0 天真 | 开盘+收盘不可撤窗内仍允许撤/改并改写成交（按 `ah0_primary_demo` 单一主报） | 发明改簿路径 |
| AH1 半泄露/混口径 | 只在开盘 9:20–9:25 发明撤改；收盘 14:57–15:00 按诚实拒撤 | 混口径假路径 |
| AH2 PIT 诚实 | 两窗内撤/改 = 无效；窗外按普通规则 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测集合竞价不可撤窗执行诚信**，不主测隔夜假 GTC（见 N）、不主测集合量分母（见 Y）、不主测退市整理（见 H）、不主测板上枯竭（见 A）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_N_close_gtc=False` / `merge_with_Y_call_vol=False` / `merge_with_H_exit=False` / `merge_with_A_fill=False` / `merge_with_M_aft=False` / `merge_with_O_block=False` / `merge_with_X_st_limit=False` / `merge_with_E_lot=False` / `merge_with_R_etf_rotation=False` / `merge_with_Q_cb_rotation=False` / `merge_with_AC_bse=False` / `merge_with_AD_50w=False` / `merge_with_AE_stock_t0=False` / `merge_with_AF_qty_cap=False` / `merge_with_AG_beyond_limit=False` / `merge_with_I_cage=False` / `merge_with_F_round=False` / `merge_with_L_mkt=False`（写死）**。

**待预检键（纸面占位；拉数前须写死冻结；禁 null；禁 holdout 标定；禁双挂）**：

```
params.Y                            = 0.02                      # 建议；可成交名义/冲击差显著门槛；≠实验字母 AH
params.G                            = 0.01                      # 建议；假撤改桶相对对照差
params.N                            = 0.05                      # 建议；失败/废单率差门槛
params.Y2                           = 0.015                     # 建议；AH1（仅开盘窗发明）相对 AH2 专项门槛
params.ah0_primary_demo             = invent_cancel_in_nocancel_window  # 建议；主报窗内假撤；禁与 invent_replace_improve_fill 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股股票（`universe_rule=sse_szse_common_stock`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺会话钟/时戳；把 N/Y/H 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：不可撤窗按成交日当时交易规则文本；**禁止**用核对日规则铺满；沪深两窗同向（9:20–9:25 / 14:57–15:00）；若核出历史切日差异须改 params 冻结，禁默覆盖。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ah0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AH0 − AH2**：两窗假撤改相对诚实拒撤——假改簿 / 可成交质量吹胖。  
2. **AH1 − AH2**：仅开盘窗发明相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_open_nocancel_cancel",   # 9:20–9:25 假撤改
  "invent_close_nocancel_cancel",  # 14:57–15:00 假撤改
  "open_only_miscategorized",      # AH1 混口径
  "honest_reject_nocancel",        # 对照诚实废单
  "vs_N_gtc",                      # 对照声明：隔夜假 GTC 另页 N
  "vs_Y_call_vol",                 # 对照声明：集合量分母另页 Y
  "vs_H_exit",                     # 对照声明：退市整理另页 H（AH≠H）
  "vs_A_fill",                     # 对照声明：板上枯竭另页 A
  "day_freq_proxy_only",           # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AH0/AH1 相对 AH2）；  
2. 假撤改腿贡献差 ΔFakeCancel；  
3. 废单/失败率差 ΔFail；  
4. （可选）开/收盘冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeCancel 桶贡献| **≥ params.G** 或 |ΔNotional_(AH1−AH2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「集合竞价不可撤窗执行鸿沟显著」。

**params.Y / G / N / Y2（待预检；与实验字母 AH 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AH） | **待预检**建议 `0.02`；拉数前写死冻结 |
| params.G | 假撤改桶相对对照差 | **待预检**建议 `0.01`；拉数前写死冻结 |
| params.N | 失败/废单率差门槛 | **待预检**建议 `0.05`；拉数前写死冻结 |
| params.Y2 | AH1−AH2 专项门槛 | **待预检**建议 `0.015`；拉数前写死冻结 |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19` |
| fill_time | 成交时点 | **写死** `next_open` |
| nocancel_policy_honest | 诚实窗内处理 | **写死** `reject_cancel_replace` |
| ah0_primary_demo | 天真主报枚举 | **待预检**建议 `invent_cancel_in_nocancel_window`（禁双挂） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与建议值见上；**禁止用 holdout / 事后显著性改口**；**`ah0_primary_demo` 单一主报，禁与 invent_replace_improve_fill 双挂争主表**。

**失败/不显著**：差异落在噪声带内或均匀散在非不可撤窗对照桶——结论栏写明，不得改口称「集合竞价撤单差不多可忽略」或「这类票更能改单」。

结论栏：空。跑完只写「该假设下假撤改/废单率差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验集合竞价不可撤窗执行诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（PIT 会话钟、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **缺会话钟/申报时戳却静默当窗外可撤或窗内可撤**。  
2. **把 N 隔夜假 GTC、Y 集合量分母、H 退市整理混进本页主结论**。  
3. **日频无代理声明却假装 L2 簿内精确撤改复盘**。  
4. **诚实组窗内撤改仍静默成功**（须 reject/skip）。  
5. **把实验字母 AH 与单字母 H 或 `params.Y` 混改**；或改写 Y/Z/AA/AB/AC/AD/AE/AF/AG 及其他 A/D–AG 已冻正文。  
6. **宇宙泄露 / holdout 反调**：看完 OOS 再改 `ah0_primary_demo` 或 **`params.Y` 等门槛**。  
7. **差异不集中在不可撤窗桶却仍写「系统性不可撤窗执行鸿沟」而不改表述**。  
8. **把差异写成「这类票更能改单」或选股公式**。  
9. **把开盘集合有效申报价格范围（900%/50%）、连续竞价笼子整段并进本页主结论却不声明另页 I/J/G**。  
10. **核出历史不可撤窗切日与现行两窗不同却默用现行铺满**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | 沪深普通股为主 |
| order_ts / session_clock | 是否落入不可撤窗 | Asia/Shanghai；缺 → skip |
| action | 撤/改/新报 | 主测撤改 |
| order_side / order_px（可选） | 改单后拟挂 | 日频可降级为路径敏感性 |
| open_px / close_px（未复权） | 开收盘路径对照 | 禁复权主结论 |
| is_call_auction_leg（可选） | 分桶 | 与 Y 字段可复用但不并表 |

**明确**：不依赖聚宽；**不要求新开 Level-2**——有会话钟（或日频 `day_freq_proxy` 声明）+ 拟撤改动作即可起步；缺关键字段 → `fail_policy=skip`。主窗 2019-01-01..2026-09-30。盘口深度**不**作为本页主跑必需。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=AH`（**实验字母**；**≠H**），`groups=[AH0,AH1,AH2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-19`**，**`params.fill_time=next_open`（写死）**，**`params.px_basis=unadj`**，**`params.open_nocancel_window=09:20-09:25`**，**`params.close_nocancel_window=14:57-15:00`**，**`params.nocancel_policy_honest=reject_cancel_replace`**，**`params.merge_with_N_close_gtc=False`**，**`params.merge_with_Y_call_vol=False`**，**`params.merge_with_H_exit=False`**，**`params.merge_with_A_fill=False`**，**`params.merge_with_M_aft=False`**，**`params.merge_with_O_block=False`**，**`params.merge_with_X_st_limit=False`**，**`params.merge_with_E_lot=False`**，**`params.merge_with_R_etf_rotation=False`**，**`params.merge_with_Q_cb_rotation=False`**，**`params.merge_with_AC_bse=False`**，**`params.merge_with_AD_50w=False`**，**`params.merge_with_AE_stock_t0=False`**，**`params.merge_with_AF_qty_cap=False`**，**`params.merge_with_AG_beyond_limit=False`**，**`params.merge_with_I_cage=False`**，**`params.merge_with_F_round=False`**，**`params.merge_with_L_mkt=False`**，**`params.universe_rule=sse_szse_common_stock`**，**`params.missing_session_clock_policy=skip`**，**`params.day_freq_proxy=open_close_path_sensitivity`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y/G/N/Y2` 待预检建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AH；禁 null/holdout）**，**`params.ah0_primary_demo` 待预检建议 invent_cancel_in_nocancel_window（禁双挂）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_N=off`，`overlay_Y=off`，`overlay_H=off`，`overlay_A=off`。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AH0/AH1/AH2 可成交名义/路径质量、ΔFakeCancel、ΔFail；分桶（开盘窗/收盘窗/混口径 / vs N·Y·H·A）。  
- 自检布尔：AH2 是否窗内拒撤；AH0 是否单一主报；AH1 是否仅开盘窗发明；是否未与 N/Y/H 混主结论；holdout 是否未反调；**是否未把实验字母 AH 与 H 或 params.Y 混用**；**是否未改 Y/Z/AA/AB/AC/AD/AE/AF/AG 冻结补丁正文**。  
- **禁止输出**：具体买卖标的列表当「建议」；把窗内可撤当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA/AB/AC/AD/AE/AF/AG 及其他 A/D–AG 已交正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：9:20–9:25、14:57–15:00 不接受撤单；隔夜假 GTC 另页 N；集合量分母另页 Y；退市整理另页 H。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AG，本页**新增实验 AH** 收成标准件，**不改口径主线**，**不改假设 A–AG 正文**。与实验 N/Y/H 分工：**N=收盘机制+隔夜假 GTC；Y=集合量分母；H=退市整理窗；AH=当日集合竞价不可撤窗假撤改（AH≠H）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；会话钟或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**nocancel_policy_honest=reject_cancel_replace / 两窗写死**；diff_buckets 九桶写死冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015 待预检（params.Y≠实验字母 AH）**；**ah0_primary_demo 建议 invent_cancel_in_nocancel_window 待预检（禁双挂）** |

---

## 变更

- 2026-11-02：新建标准件（总管线：AG 补丁已交后写下一纸面 AH；Y/Z/AA/AB/AC/AD/AE/AF/AG 补丁已交不改；清单止于 AG → 自 `事实与坑`「9:20–9:25 / 14:57–15:00 不接受撤单」选题，**与 A/H/X/E/M/O/AC/AD/AE/AF/AG/R/Q 及 I/F/L 及 N/Y 不撞主结论**；**明确与假设-H 分列：AH≠H**；近邻 N=隔夜假 GTC/收盘机制、Y=集合量分母、H=退市整理，本页主测当日不可撤窗假撤改；**实验字母 AH ≠ params.Y ≠ 实验字母 H**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA/AB/AC/AD/AE/AF/AG/A/D–AG 正文**）。

