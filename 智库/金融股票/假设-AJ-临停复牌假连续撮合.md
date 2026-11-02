# 假设 AJ · 临停复牌跳过复牌集合竞价假连续撮合（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AI 补丁已交后写下一纸面 AJ；清单原止于 AI，无 AJ 节 → 自立实验 AJ；选题自 `事实与坑`「无涨跌幅日盘中临停：停牌期间可申报也可撤单；**复牌对已接受申报做集合竞价**；跨越 **14:57** 且须当日复牌的，于 14:57 复牌（先复牌集合竞价，再收盘集合竞价）。上交所 4.2.5；深交所 4.3.4 / 4.3.6（核对日 2026-10-12）」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价保护限价）/ G（无板日误套板块默认板）/ J（无板日盘中临停 30%/60% 触发与窗内假连续）**分列**；**新建实验 AJ**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「临停复牌跳过复牌集合、直接按连续撮合/末笔价成交」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AI 及其他 A/D–AI 已交正文与冻结补丁；不改假设-H；不改假设-J**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AI，本页自立实验 AJ 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **无涨跌幅日临停结束后的复牌撮合方式**是否被跳过集合、发明假连续路径。双字母 **AJ ≠ 单字母 A**。与假设 **J（无板日临停）** **硬分列**：J = 较开盘价 **30%/60%** 临停**触发**与「窗内/穿过阈值后仍按最高最低连续可成交」；本页 = 临停**已结束后**，复牌是否仍须先走**复牌集合竞价**（跨越 14:57 则于 14:57 先复牌集合再收盘集合），不重开 30%/60% 触发阈值、不重开「窗内假连续」。双字母 **AJ ≠ 单字母 J**。与假设 **AI（无板日集合有效申报范围）** **分列**：AI = 临停/复牌集合阶段申报价是否超出最近成交 ±10% 仍进簿；本页 = 复牌**撮合机制**是否被跳过集合改成连续，不重开 ±10% 带宽。与假设 **AH（不可撤窗假撤改）** **分列**：AH = 9:20–9:25 / 14:57–15:00 能否撤改；本页 = 复牌集合是否被跳过。与假设 **D（成交时点与停牌）** **分列**：D = 停牌日/无成交日能否成交及次日开收时点；本页 = 盘中临停**复牌瞬间**的撮合方式。与假设 A/H/X/E/M/O/R/Q/AC/AD/AE/AF/AG/I/F/L/G/N **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AJ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AJ / 假设-AJ / hypothesis_id=AJ / 组 AJ0·AJ1·AJ2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AJ 与单字母实验 **A**、单字母实验 **J**、或 params 键名 `aj0_*` 以外的实验页混读。**双字母 AJ ≠ 单字母 A ≠ 单字母 J**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，在**无涨跌幅日盘中临停复牌**时，跳过法定的**复牌集合竞价**、把已接受申报直接按连续竞价撮合（或按临停前末笔/当日极值价发明复牌成交），或忽略「跨越 14:57 且须当日复牌 → 于 14:57 先复牌集合、再收盘集合」的时点，相对「复牌对已接受申报做集合竞价；跨越 14:57 且须当日复牌的于 14:57 复牌（先复牌集合竞价，再收盘集合竞价）；临停窗内可申报可撤单但不连续撮合（窗内假连续另页 J）」的 PIT 诚实组，会**系统性发明复牌假连续路径并高估可成交名义 / 错价冲击**；差异应**集中在复牌跳过集合 / 14:57 复牌时点被忽略 / 按末笔·极值发明复牌价桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的复牌假连续贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在复牌撮合机制相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 临停复牌集合 ≠ 临停触发；≠ 窗内假连续；≠ 集合有效申报范围；≠ 板上枯竭

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AJ；≠ 实验字母 A；≠ 实验字母 J
# params.asof_check_date                 写死默认 2026-10-12  # 事实与坑「临停复牌集合竞价」核对锚（与 J/AI 同批）
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；复牌冲击作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.halt_pct_1                      写死 0.30           # 复用 J：临停触发阈值；本页不重开触发主结论
# params.halt_pct_2                      写死 0.60
# params.halt_minutes                    写死 10
# params.halt_baseline                   写死 open           # 与 J 同向；禁 pre_close / issue_price
# params.resume_match_honest             写死 call_auction   # 诚实：复牌对已接受申报做集合竞价
# params.resume_at_1457_if_span          写死 True           # 跨越 14:57 且须当日复牌 → 于 14:57 复牌（先复牌集合再收盘集合）
# params.close_auction_start             写死 14:57
# params.aj0_primary_demo                写死 invent_resume_skip_call  # 风控补丁冻结；主报：复牌跳过集合、直接连续撮合；禁与 invent_resume_at_last_px 双挂争主表
# params.aj0_invent_resume_skip_call     写死 True           # 天真主路径（与建议主报同向）
# params.aj0_invent_resume_at_last_px    写死 False          # 诊断可叠；主报以 aj0_primary_demo 为准
# params.aj1_ignore_1457_resume_clock    写死 True           # 半泄露：忽略跨越 14:57 须于 14:57 复牌
# params.aj1_invent_resume_skip_call     写死 False          # AJ1 主病在时点，不在「完全跳过集合」双挂
# params.aj2_resume_match                写死 call_auction
# params.aj2_resume_at_1457_if_span      写死 True
# params.no_limit_day_source             写死 g_pit_table    # 无板日标签复用 G；临停窗标签可复用 J；本页不重开 G/J 主结论
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AJ≠A）
# params.merge_with_J_halt               写死 False          # 临停触发/窗内假连续另页 J（AJ≠J）
# params.merge_with_AI_call_band         写死 False          # 临停/复牌集合 ±10% 申报范围另页 AI
# params.merge_with_AH_nocancel          写死 False          # 不可撤窗另页 AH
# params.merge_with_D_halt_timing        写死 False          # 停牌日成交时点另页 D
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_L_mkt                写死 False
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
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_N_close_gtc          写死 False          # 收盘机制/假 GTC 另页 N；本页只碰复牌 vs 14:57 时点
# params.universe_rule                   写死 sse_szse_common_stock_nolimit_halt_resume  # 主宇宙=沪深普通 A 股无涨跌幅日且发生盘中临停并复牌的样本
# params.missing_halt_resume_policy      写死 skip           # 缺临停/复牌时点或公告 → skip（禁静默当连续可成）
# params.day_freq_proxy                  写死 resume_match_sensitivity  # 日频无 L2 时只报「复牌跳过集合」敏感性档；禁假装精确复盘簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AJ；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-12"
px_basis = "unadj"
tick = 0.01
halt_pct_1 = 0.30
halt_pct_2 = 0.60
halt_minutes = 10
halt_baseline = "open"
resume_match_honest = "call_auction"
resume_at_1457_if_span = True
close_auction_start = "14:57"
aj0_primary_demo = "invent_resume_skip_call"  # 风控补丁冻结；禁双挂
aj0_invent_resume_skip_call = True
aj0_invent_resume_at_last_px = False
aj1_ignore_1457_resume_clock = True
aj1_invent_resume_skip_call = False
aj2_resume_match = "call_auction"
aj2_resume_at_1457_if_span = True
no_limit_day_source = "g_pit_table"
universe_rule = "sse_szse_common_stock_nolimit_halt_resume"
missing_halt_resume_policy = "skip"
day_freq_proxy = "resume_match_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 aj0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AJ
G = 0.01
N = 0.05
Y2 = 0.015

def spans_1457(halt_start_ts, scheduled_resume_ts, close_auction_start="14:57"):
    """临停窗是否跨越 14:57 且须当日复牌。"""
    # 纸面：若 scheduled_resume 落在 close_auction_start 之后或临停未在 14:57 前结束 → True
    return scheduled_resume_ts >= close_auction_start

def resume_match_mode(group, halt_start_ts, scheduled_resume_ts):
    """
    AJ0：复牌跳过集合、直接连续撮合（按 aj0_primary_demo）
    AJ1：忽略跨越 14:57 须于 14:57 复牌的时点（仍可按集合，但钟点错）
    AJ2：诚实 call_auction；若 spans_1457 → 于 14:57 先复牌集合再收盘集合
    """
    if group == "AJ0" and aj0_invent_resume_skip_call:
        return "invent_continuous_at_resume", scheduled_resume_ts
    if group == "AJ0" and aj0_invent_resume_at_last_px:
        return "invent_fill_at_last_px", scheduled_resume_ts
    if group == "AJ1" and aj1_ignore_1457_resume_clock and spans_1457(halt_start_ts, scheduled_resume_ts):
        return "ignore_1457_clock_resume_elsewhere", scheduled_resume_ts
    if spans_1457(halt_start_ts, scheduled_resume_ts) and aj2_resume_at_1457_if_span:
        return "honest_resume_call_at_1457_then_close_call", close_auction_start
    return "honest_resume_call_auction", scheduled_resume_ts
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺临停/复牌时点或无板日标签却硬判复牌连续可成、把 J 临停触发/窗内假连续 / AI 集合 ±10% / A 板上枯竭 / AH 不可撤窗 / D 停牌日时点混进本页主表、日频无代理声明却假装 L2 复盘复牌簿、诚实组复牌跳过集合仍静默成功 → **跳过该日该券该腿**，不静默记复牌假连续成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AJ）

| 组 | 复牌撮合 | 说明 |
|----|----------|------|
| AJ0 天真 | 复牌跳过集合、直接连续撮合（按 `aj0_primary_demo` 单一主报） | 发明复牌假连续路径 |
| AJ1 半泄露/混口径 | 忽略跨越 14:57 须于 14:57 复牌；可诊断按末笔/极值发明复牌价 | 混口径假路径 |
| AJ2 PIT 诚实 | 复牌对已接受申报做集合竞价；跨越 14:57 且须当日复牌 → 于 14:57 先复牌集合再收盘集合 | 与事实与坑同向 |

同一信号、同一无涨跌幅日且发生盘中临停并复牌的沪深普通 A 股宇宙。本页**主测临停复牌撮合机制执行诚信**，不主测 30%/60% 触发（见 J）、不主测临停集合 ±10% 申报范围（见 AI）、不主测板上枯竭（见 A）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_A_fill=False` / `merge_with_J_halt=False` / `merge_with_AI_call_band=False` / `merge_with_AH_nocancel=False` / `merge_with_D_halt_timing=False` / `merge_with_G_nolimit_pct=False` / `merge_with_AG_beyond_limit=False` / `merge_with_I_cage=False` / `merge_with_F_round=False` / `merge_with_L_mkt=False` / `merge_with_H_exit=False` / `merge_with_X_st_limit=False` / `merge_with_E_lot=False` / `merge_with_M_aft=False` / `merge_with_O_block=False` / `merge_with_R_etf_rotation=False` / `merge_with_Q_cb_rotation=False` / `merge_with_AC_bse=False` / `merge_with_AD_50w=False` / `merge_with_AE_stock_t0=False` / `merge_with_AF_qty_cap=False` / `merge_with_N_close_gtc=False`（写死）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 可成交名义/冲击差显著门槛；≠实验字母 AJ
params.G                            = 0.01                      # 复牌假连续桶相对对照差
params.N                            = 0.05                      # 失败/废单率差门槛
params.Y2                           = 0.015                     # AJ1（忽略 14:57 复牌钟）相对 AJ2 专项门槛
params.aj0_primary_demo             = invent_resume_skip_call   # 主报：复牌跳过集合假连续；禁与 invent_resume_at_last_px 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股在**无涨跌幅日**且发生**盘中临停并复牌**的样本（`universe_rule=sse_szse_common_stock_nolimit_halt_resume`；无板日标签复用 G；临停触发可复用 J 的 PIT，本页不重开 J 主结论）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺临停/复牌时点；把 J/AI/A/AH/D 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：临停复牌撮合按成交日当时交易规则文本；**禁止**用核对日规则铺满；跨越 14:57 须于 14:57 复牌写死；临停触发阈值/时长切日交 J，本页只消费「已临停并复牌」事件。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `aj0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AJ0 ? AJ2**：复牌跳过集合假连续相对诚实复牌集合——假路径 / 可成交名义吹胖。  
2. **AJ1 ? AJ2**：忽略 14:57 复牌钟（及可选按末笔/极值发明复牌价）相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_resume_skip_call",       # 复牌跳过集合、直接连续
  "invent_resume_at_last_px",      # 按临停前末笔/极值发明复牌价
  "ignore_1457_resume_clock",      # AJ1：忽略跨越 14:57 须于 14:57 复牌
  "honest_resume_call_auction",    # 对照诚实复牌集合
  "vs_J_halt_30_60",               # 对照声明：临停触发/窗内假连续另页 J（AJ≠J）
  "vs_AI_call_band",               # 对照声明：临停/复牌集合 ±10% 另页 AI
  "vs_A_fill",                     # 对照声明：板上枯竭另页 A（AJ≠A）
  "vs_AH_nocancel",                # 对照声明：不可撤窗另页 AH
  "vs_D_halt_timing",              # 对照声明：停牌日成交时点另页 D
  "vs_N_close_mech",               # 对照声明：收盘机制另页 N
  "day_freq_proxy_only",           # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AJ0/AJ1 相对 AJ2）；  
2. 复牌假连续腿贡献差 ΔFakeResume；  
3. 废单/失败率差 ΔFail；  
4. （可选）复牌冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeResume 桶贡献| **≥ params.G** 或 |ΔNotional_(AJ1?AJ2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「临停复牌撮合执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AJ 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AJ） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 复牌假连续桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AJ1?AJ2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-12` |
| fill_time | 成交时点 | **写死** `next_open` |
| aj0_primary_demo | 天真主报枚举 | **写死冻结** `invent_resume_skip_call`（禁双挂；风控补丁 2026-11-02） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组复牌须走集合；禁与 J/AI/A/AH/D 混主结论）。

---

## 5. 失效条件

1. 样本几乎无临停复牌事件，或日频无法区分复牌集合与连续成交，且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把临停触发/窗内假连续（J）、临停集合 ±10%（AI）、板上枯竭（A）、停牌日时点（D）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「复牌跳过集合」写成「临停窗内仍可连续成交」而不声明另页 J → 与 J 撞题，设计失效。  
4. holdout 反调 `aj0_primary_demo` / Y·G·N·Y2 → 结论无效。  
5. 用复权价算复牌参考价或临停边界 → 标签与执行双错，结论无效。  
6. 把实验字母 AJ 与单字母 A 或单字母 J 或 `params.Y` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权 OHLC、是否无涨跌幅日（G PIT）、是否触发盘中临停及复牌时点（可用公告；无公告则日频 `day_freq_proxy` 敏感性档并声明）；  
- 交易所、板块、买卖方向、拟挂限价；  
- 临停开始/计划复牌墙钟（Asia/Shanghai）；是否跨越 14:57；  
- 交易日历。

可选：L2/逐笔（精确复盘复牌集合簿）；临停公告全文。

**禁止**：用核对日现行规则铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 J 的「窗内假连续」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AJ`  
- **组**：AJ0 / AJ1 / AJ2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-12`；`resume_match_honest=call_auction`；`resume_at_1457_if_span=True`；`close_auction_start=14:57`；`halt_pct_1/2=0.30/0.60`（消费 J，不重开）；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_nolimit_halt_resume`；`missing_halt_resume_policy=skip`；`day_freq_proxy=resume_match_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2=0.02/0.01/0.05/0.015` 写死冻结**（params.Y≠实验字母 AJ；禁 null/holdout）；**`params.aj0_primary_demo=invent_resume_skip_call` 写死冻结**（禁与 invent_resume_at_last_px 双挂）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AJ0/AJ1/AJ2 可成交名义/路径质量、ΔFakeResume、ΔFail；分桶（复牌跳过集合 / 末笔发明复牌价 / 忽略 14:57 / vs J·AI·A·AH·D·N）。  
- 自检布尔：AJ2 是否复牌走集合；AJ0 是否单一主报；AJ1 是否忽略 14:57 钟；是否未与 J/AI/A/AH/D 混主结论；holdout 是否未反调；**是否未把实验字母 AJ 与 A 或 J 或 params.Y 混用**；**是否未改 Y/Z/AA–AI 冻结补丁正文**；**是否未改假设-H / 假设-J**。  
- **禁止输出**：具体买卖标的列表当「建议」；把复牌跳过集合当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AI 及其他 A/D–AI 已交正文**；**不改假设-H**；**不改假设-J**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：无涨跌幅日盘中临停期间可申报可撤单；**复牌对已接受申报做集合竞价**；跨越 14:57 且须当日复牌的于 14:57 复牌（先复牌集合，再收盘集合）。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AI，本页**新增实验 AJ** 收成标准件，**不改口径主线**，**不改假设 A–AI 正文**。与实验 J/AI/A/AH/D 分工：**J=无板日 30%/60% 临停触发与窗内假连续；AI=临停/复牌集合有效申报范围 ±10%；A=板上枯竭；AH=不可撤窗假撤改；D=停牌日成交时点；AJ=临停复牌跳过复牌集合假连续撮合（AJ≠A≠J）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；无板日+临停复牌事件或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-12；**fill_time=next_open 写死**；**resume_match_honest=call_auction + resume_at_1457_if_span=True 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2=0.02/0.01/0.05/0.015 写死冻结（params.Y≠实验字母 AJ）**；**aj0_primary_demo=invent_resume_skip_call 写死冻结（禁双挂）**；**风控补丁两条 2026-11-02 已写死待复检** |

---

## 已冻结键（风控补丁 2026-11-02；已写死待复检）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AJ**；禁 null / holdout 标定。  
2. **`params.aj0_primary_demo`**：**写死冻结** **`invent_resume_skip_call`**；禁与 **`invent_resume_at_last_px`** 双挂争主表。

---

## 变更

- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AJ-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写死冻结（**params.Y≠实验字母 AJ**；禁 null/holdout 标定）；② `params.aj0_primary_demo=invent_resume_skip_call` 写死冻结（禁与 `invent_resume_at_last_px` 双挂争主表）。**已写死待复检**；**不抢实验 A**；**不开回测**；**不改假设-H**；**不改假设-J**；**不改 Y/Z/AA–AI 及其他 A/D–AI 正文**。
- 2026-11-02：新建标准件（总管线：AI 补丁已交后写下一纸面 AJ；Y/Z/AA–AI 补丁已交不改；清单止于 AI → 自 `事实与坑`「临停复牌对已接受申报做集合竞价；跨越 14:57 于 14:57 复牌」选题，**与 A/H/X/E/M/O/AC–AI/R/Q/I/F/L/J/G/D/N 不撞主结论**；**明确双字母 AJ ≠ 单字母 A ≠ 单字母 J**；近邻 J=临停触发/窗内假连续、AI=集合 ±10%、A=板上、AH=不可撤窗、D=停牌时点，本页主测复牌跳过集合假连续；**实验字母 AJ ≠ params.Y ≠ 实验字母 A ≠ 实验字母 J**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA–AI/A/D–AI 正文**；**不改假设-H**；**不改假设-J**）。
