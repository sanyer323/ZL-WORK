# 假设 AL · 午休与开盘空窗假连续撮合（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AK 补丁已交后写下一纸面 AL；清单原止于 AK，无 AL 节 → 自立实验 AL；选题自 `事实与坑`「沪深现行竞价时段：**9:15–9:25** 开盘集合竞价，**9:30–11:30 / 13:00–14:57** 连续竞价，**14:57–15:00** 收盘集合竞价（上交所 2.4.2；深交所 2.3.2）。核对日锚 2026-10-02」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AJ（临停复牌假连续）/ AK（集合竞价时段假连续）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价通道）/ G（无板日误套板块默认板）/ J（无板日临停触发）/ N（收盘机制与假 GTC）/ Y（集合量分母）/ D（成交时点与停牌）/ K（融券空头名单）/ AA（分钟 bar 时区误标）**分列**；**新建实验 AL**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「9:25–9:30 开盘空窗 / 11:30–13:00 午休空窗」当连续可成；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AK 及其他 A/D–AK 已交正文与冻结补丁；不改假设-H；不改假设-L；不改假设-AK；不改假设-AA**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AK，本页自立实验 AL 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **非集合、非连续的空窗钟点**是否被发明成连续撮合。双字母 **AL ≠ 单字母 A**。与假设 **L（市价通道）** **硬分列**：L = 市价申报当「穿过整本档位的无限价」及保护限价/集合禁市价；本页 = **会话空窗是否可撮合**，不重开市价通道/保护限价。双字母 **AL ≠ 单字母 L**。与假设 **AK（集合竞价时段假连续）** **分列**：AK = 在 **开盘/收盘集合窗内**把集合改成连续；本页 = 在 **集合已结束、连续尚未开始** 的 **9:25–9:30** 与 **午休 11:30–13:00** 发明连续成交，**不**把集合窗当主病。与假设 **AA（分钟 bar 时区误标）** **分列**：AA = 分钟 bar 时区/标签把连续窗标错；本页 = 空窗钟点上**发明成交路径**，不主测 bar 标签。与假设 **AJ（临停复牌假连续）** **分列**：AJ = 无板日临停**复牌瞬间**跳过复牌集合；本页 = **日常午休/开盘空窗**假连续，不要求临停事件。与假设 **D（开/收时点）** **分列**：D = 次日开 vs 收成交时点与停牌假成交；本页 = 日内空窗钟点撮合可否。与假设 A/H/X/E/M/O/R/Q/AC–AK/I/F/L/G/J/N/Y/AA **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AL** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AL / 假设-AL / hypothesis_id=AL / 组 AL0·AL1·AL2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AL 与单字母实验 **A**、单字母实验 **L**、或 params 键名 `al0_*` 以外的实验页混读。**双字母 AL ≠ 单字母 A ≠ 单字母 L**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，在**开盘集合结束后至连续开始前的 9:25–9:30 空窗**或**午休 11:30–13:00 空窗**，把本不应撮合的时段当成连续竞价可成交（或按空窗内高低/末笔发明冲击路径），相对「连续竞价仅在 9:30–11:30 / 13:00–14:57；9:25–9:30 与 11:30–13:00 不产生竞价撮合成交；集合仅在 9:15–9:25 / 14:57–15:00」的 PIT 诚实组，会**系统性发明空窗假连续路径并高估可成交名义 / 错价冲击**；差异应**集中在开盘空窗假连续 / 午休空窗假连续桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的空窗假连续贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在空窗钟点相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 空窗假连续 ≠ 集合窗假连续；≠ 市价通道；≠ 板上枯竭；≠ 分钟 bar 时区

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AL；≠ 实验字母 A；≠ 实验字母 L
# params.asof_check_date                 写死默认 2026-10-02  # 事实与坑「竞价时段」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；空窗冲击作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.open_call_end                   写死 09:25          # 开盘集合结束
# params.continuous_am_start             写死 09:30
# params.continuous_am_end               写死 11:30
# params.continuous_pm_start             写死 13:00
# params.continuous_pm_end               写死 14:57
# params.open_gap_start                  写死 09:25          # 开盘空窗 [09:25, 09:30)
# params.open_gap_end                    写死 09:30
# params.lunch_gap_start                 写死 11:30          # 午休空窗 [11:30, 13:00)
# params.lunch_gap_end                   写死 13:00
# params.gap_match_honest                写死 no_match       # 诚实：空窗不撮合
# params.al0_primary_demo                写死 invent_noncontinuous_gap_fill  # 风控补丁冻结；主报：开盘空窗+午休空窗均假连续；禁与 invent_lunch_gap_only 双挂争主表
# params.al0_invent_open_gap             写死 True           # 天真主路径（随 primary_demo）
# params.al0_invent_lunch_gap            写死 True
# params.al1_lunch_only_fake             写死 True           # 半泄露：仅午休空窗发明连续，开盘空窗诚实
# params.al2_gap_match                   写死 no_match
# params.al2_apply_open_gap_skip         写死 True
# params.al2_apply_lunch_gap_skip        写死 True
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AL≠A）
# params.merge_with_L_mkt                写死 False          # 市价通道另页 L（AL≠L）
# params.merge_with_AK_call_cont         写死 False          # 集合窗假连续另页 AK
# params.merge_with_AA_bar_tz            写死 False          # 分钟 bar 时区另页 AA
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
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
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_K_short_list         写死 False
# params.universe_rule                   写死 sse_szse_common_stock_session_gaps  # 主宇宙=沪深普通 A 股；空窗主测
# params.missing_session_clock_policy    写死 skip           # 缺会话钟/时戳 → skip（禁静默当全日连续）
# params.day_freq_proxy                  写死 session_gap_match_sensitivity  # 日频无 L2 时只报「空窗假连续」敏感性档；禁假装精确复盘簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AL；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-02"
px_basis = "unadj"
tick = 0.01
open_call_end = "09:25"
continuous_am_start = "09:30"
continuous_am_end = "11:30"
continuous_pm_start = "13:00"
continuous_pm_end = "14:57"
open_gap_start = "09:25"
open_gap_end = "09:30"
lunch_gap_start = "11:30"
lunch_gap_end = "13:00"
gap_match_honest = "no_match"
al0_primary_demo = "invent_noncontinuous_gap_fill"  # 风控补丁冻结；禁双挂
al0_invent_open_gap = True
al0_invent_lunch_gap = True
al1_lunch_only_fake = True
al2_gap_match = "no_match"
al2_apply_open_gap_skip = True
al2_apply_lunch_gap_skip = True
universe_rule = "sse_szse_common_stock_session_gaps"
missing_session_clock_policy = "skip"
day_freq_proxy = "session_gap_match_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 al0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AL
G = 0.01
N = 0.05
Y2 = 0.015

def in_open_gap(ts):
    return open_gap_start <= ts < open_gap_end

def in_lunch_gap(ts):
    return lunch_gap_start <= ts < lunch_gap_end

def in_continuous(ts):
    return (continuous_am_start <= ts <= continuous_am_end) or (continuous_pm_start <= ts < continuous_pm_end)

def gap_match_mode(group, ts):
    """
    AL0：开盘空窗+午休空窗均假连续（按 al0_primary_demo）
    AL1：仅午休空窗假连续；开盘空窗诚实 skip
    AL2：两空窗均 no_match；连续窗才允许连续撮合
    """
    if group == "AL0" and al0_primary_demo == "invent_noncontinuous_gap_fill":
        if in_open_gap(ts) and al0_invent_open_gap:
            return "invent_continuous_in_open_gap"
        if in_lunch_gap(ts) and al0_invent_lunch_gap:
            return "invent_continuous_in_lunch_gap"
    if group == "AL1" and al1_lunch_only_fake and in_lunch_gap(ts):
        return "invent_continuous_in_lunch_gap_only"
    if in_open_gap(ts) or in_lunch_gap(ts):
        return "honest_gap_no_match"
    if in_continuous(ts):
        return "honest_continuous"
    return "out_of_scope_skip"
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺会话钟/时戳却硬判空窗连续可成、把 AK 集合窗假连续 / L 市价通道 / A 板上 / AA bar 时区 / AJ 复牌 / AH 不可撤窗混进本页主表、日频无代理声明却假装 L2 复盘空窗簿、诚实组空窗仍记连续成交 → **跳过该日该券该腿**，不静默记空窗假连续成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AL）

| 组 | 空窗撮合 | 说明 |
|----|----------|------|
| AL0 天真 | 开盘空窗+午休空窗假连续（按 `al0_primary_demo` 单一主报） | 发明空窗假连续路径 |
| AL1 半泄露/混口径 | 仅午休空窗假连续；开盘空窗诚实 skip | 混口径假路径 |
| AL2 PIT 诚实 | 两空窗均 `no_match`；连续仅在连续窗 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测非集合非连续空窗是否被发明成可撮合**，不主测集合窗假连续（见 AK）、不主测市价通道（见 L）、不主测板上枯竭（见 A）、不主测分钟 bar 时区（见 AA）、不主测临停复牌（见 AJ）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_A_fill=False` / `merge_with_L_mkt=False` / `merge_with_AK_call_cont=False` / `merge_with_AA_bar_tz=False` / `merge_with_AJ_resume=False` / `merge_with_AH_nocancel=False` / `merge_with_N_close_gtc=False` / `merge_with_Y_call_volume=False` / `merge_with_D_halt_timing=False` / `merge_with_J_halt=False` / `merge_with_AI_call_band=False` / `merge_with_AG_beyond_limit=False` / `merge_with_I_cage=False` / `merge_with_F_round=False` / `merge_with_H_exit=False` / `merge_with_X_st_limit=False` / `merge_with_E_lot=False` / `merge_with_M_aft=False` / `merge_with_O_block=False` / `merge_with_R_etf_rotation=False` / `merge_with_Q_cb_rotation=False` / `merge_with_AC_bse=False` / `merge_with_AD_50w=False` / `merge_with_AE_stock_t0=False` / `merge_with_AF_qty_cap=False` / `merge_with_G_nolimit_pct=False` / `merge_with_K_short_list=False`（写死）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 可成交名义/冲击差显著门槛；≠实验字母 AL
params.G                            = 0.01                      # 空窗假连续桶相对对照差
params.N                            = 0.05                      # 失败/废单率差门槛
params.Y2                           = 0.015                     # AL1（仅午休假连续）相对 AL2 专项门槛
params.al0_primary_demo             = invent_noncontinuous_gap_fill  # 主报：开盘+午休空窗假连续；禁与 invent_lunch_gap_only 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_session_gaps`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺会话钟/时戳；把 AK/L/A/AA/AJ/AH 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：竞价时段按成交日当时交易规则文本；**禁止**用核对日规则铺满；集合窗假连续交 AK，本页只测空窗。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `al0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AL0 − AL2**：开盘+午休空窗假连续相对诚实空窗不撮合——假路径 / 可成交名义吹胖。  
2. **AL1 − AL2**：仅午休空窗假连续相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_open_gap_as_continuous",    # 9:25–9:30 开盘空窗假连续
  "invent_lunch_gap_as_continuous",   # 11:30–13:00 午休空窗假连续
  "honest_gap_no_match",              # 对照诚实空窗不撮合
  "vs_AK_call_cont",                  # 对照声明：集合窗假连续另页 AK
  "vs_L_mkt",                         # 对照声明：市价通道另页 L（AL≠L）
  "vs_A_fill",                        # 对照声明：板上枯竭另页 A（AL≠A）
  "vs_AA_bar_tz",                     # 对照声明：分钟 bar 时区另页 AA
  "vs_AJ_resume",                     # 对照声明：临停复牌另页 AJ
  "vs_AH_nocancel",                   # 对照声明：不可撤窗另页 AH
  "vs_D_halt_timing",                 # 对照声明：开收时点/停牌另页 D
  "vs_N_close_mech",                  # 对照声明：收盘机制另页 N
  "day_freq_proxy_only",              # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AL0/AL1 相对 AL2）；  
2. 空窗假连续腿贡献差 ΔFakeGapCont；  
3. 废单/失败率差 ΔFail；  
4. （可选）空窗冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeGapCont 桶贡献| **≥ params.G** 或 |ΔNotional_(AL1−AL2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「空窗撮合执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AL 无关；风控补丁 2026-11-02）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AL） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 空窗假连续桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛 | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AL1−AL2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-02` |
| fill_time | 成交时点 | **写死** `next_open` |
| al0_primary_demo | 天真主报枚举 | **写死冻结** `invent_noncontinuous_gap_fill`（禁双挂；风控补丁 2026-11-02） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组空窗须 no_match；禁与 AK/L/A/AA/AJ 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分空窗与连续窗成交，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把集合窗假连续（AK）、市价通道（L）、板上枯竭（A）、分钟 bar 时区（AA）、临停复牌（AJ）、不可撤窗（AH）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「空窗假连续」写成「集合窗假连续」而不声明另页 AK → 与 AK 撞题，设计失效。  
4. holdout 反调 `al0_primary_demo` / Y·G·N·Y2 → 结论无效。  
5. 用复权价算空窗参考价或冲击 → 标签与执行双错，结论无效。  
6. 把实验字母 AL 与单字母 A 或单字母 L 或 `params.Y` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权 OHLC、交易所、买卖方向、拟挂限价；  
- 会话钟/申报或成交时戳（Asia/Shanghai）；是否落在开盘空窗 / 连续 / 午休空窗 / 集合；  
- 交易日历。

可选：L2/逐笔（精确复盘空窗是否出现假撮合标记）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日现行规则铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 AK 的「集合窗假连续」或 L 的「市价无限价」或 AA 的「bar 时区误标」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AL`  
- **组**：AL0 / AL1 / AL2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-02`；`open_gap=09:25-09:30`；`lunch_gap=11:30-13:00`；`continuous=09:30-11:30|13:00-14:57`；`gap_match_honest=no_match`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_session_gaps`；`missing_session_clock_policy=skip`；`day_freq_proxy=session_gap_match_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2=0.02/0.01/0.05/0.015` 写死冻结**（params.Y≠实验字母 AL；禁 null/holdout）；**`params.al0_primary_demo=invent_noncontinuous_gap_fill` 写死冻结**（禁与 invent_lunch_gap_only 双挂；风控补丁 2026-11-02）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AL0/AL1/AL2 可成交名义/路径质量、ΔFakeGapCont、ΔFail；分桶（开盘空窗假连续 / 午休空窗假连续 / vs AK·L·A·AA·AJ·AH·D·N）。  
- 自检布尔：AL2 是否空窗 no_match；AL0 是否单一主报；AL1 是否仅午休假连续；是否未与 AK/L/A/AA/AJ 混主结论；holdout 是否未反调；**是否未把实验字母 AL 与 A 或 L 或 params.Y 混用**；**是否未改 Y/Z/AA–AK 冻结补丁正文**；**是否未改假设-H / 假设-L / 假设-AK / 假设-AA**。  
- **禁止输出**：具体买卖标的列表当「建议」；把空窗假连续当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AK 及其他 A/D–AK 已交正文**；**不改假设-H**；**不改假设-L**；**不改假设-AK**；**不改假设-AA**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：沪深现行 **9:15–9:25** 开盘集合、**9:30–11:30 / 13:00–14:57** 连续、**14:57–15:00** 收盘集合；**9:25–9:30** 与 **11:30–13:00** 不在连续竞价窗内，诚实组不得记竞价撮合成交。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AK，本页**新增实验 AL** 收成标准件，**不改口径主线**，**不改假设 A–AK 正文**。与实验 AK/L/A/AA/AJ/D 分工：**AK=开盘/收盘集合窗假连续；L=市价通道；A=板上枯竭；AA=分钟 bar 时区误标；AJ=临停复牌跳过集合；D=开收时点/停牌；AL=午休与开盘空窗假连续撮合（AL≠A≠L）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；会话钟或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-02；**fill_time=next_open 写死**；**gap_match_honest=no_match + 开盘/午休空窗钟点写死**；diff_buckets 写死待冻结；**Y/G/N/Y2=0.02/0.01/0.05/0.015 写死冻结（params.Y≠实验字母 AL）**；**al0_primary_demo=invent_noncontinuous_gap_fill 写死冻结（禁双挂）**；**风控补丁两条 2026-11-02 已写死待复检** |

---

## 已冻结键（风控补丁 2026-11-02；已写死待复检）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AL**；禁 null / holdout 标定。  
2. **`params.al0_primary_demo`**：**写死冻结** **`invent_noncontinuous_gap_fill`**；禁与 **`invent_lunch_gap_only`** 双挂争主表。

---

## 变更

- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AL-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写死冻结（**params.Y≠实验字母 AL**；禁 null/holdout 标定）；② `params.al0_primary_demo=invent_noncontinuous_gap_fill` 写死冻结（禁与 `invent_lunch_gap_only` 双挂争主表）。**已写死待复检**；**不抢实验 A**；**不开回测**；**不改假设-H**；**不改假设-L**；**不改假设-AK**；**不改假设-AA**；**不改 Y/Z/AA–AK 及其他 A/D–AK 正文**。
- 2026-11-02：新建标准件（总管线：AK 补丁已交后写下一纸面 AL；Y/Z/AA–AK 补丁已交不改；清单止于 AK → 自 `事实与坑`「竞价时段：连续仅 9:30–11:30 / 13:00–14:57」选题，**与 A/H/X/E/M/O/AC–AK/R/Q/I/F/L/J/G/D/N/Y/AA 不撞主结论**；**明确双字母 AL ≠ 单字母 A ≠ 单字母 L**；近邻 AK=集合窗假连续、L=市价通道、A=板上、AA=bar 时区、AJ=复牌，本页主测午休与开盘空窗假连续；**实验字母 AL ≠ params.Y ≠ 实验字母 A ≠ 实验字母 L**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA–AK/A/D–AK 正文**；**不改假设-H**；**不改假设-L**；**不改假设-AK**；**不改假设-AA**）。
