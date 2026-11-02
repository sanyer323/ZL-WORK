# 假设 AK · 开盘/收盘集合竞价时段假连续撮合（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AJ 补丁已交后写下一纸面 AK；清单原止于 AJ，无 AK 节 → 自立实验 AK；选题自 `事实与坑`「沪深现行竞价时段：**9:15–9:25** 开盘集合竞价，**9:30–11:30 / 13:00–14:57** 连续竞价，**14:57–15:00** 收盘集合竞价（上交所 2.4.2；深交所 2.3.2）。开盘价/收盘价由集合竞价产生（上交所 4.1.1–4.1.3；深交所 4.2.1–4.2.3）。核对日锚 2026-10-02」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AJ（临停复牌假连续）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价保护限价）/ G（无板日误套板块默认板）/ J（无板日临停触发）/ N（收盘机制与假 GTC）/ Y（集合量分母）/ D（成交时点与停牌）/ K（融券空头名单）**分列**；**新建实验 AK**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「集合竞价时段按连续竞价逐笔多价撮合」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AJ 及其他 A/D–AJ 已交正文与冻结补丁；不改假设-H；不改假设-K；不改假设-N；不改假设-AH**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AJ，本页自立实验 AK 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **开盘/收盘集合竞价钟点内**是否被改成连续竞价逐笔撮合。双字母 **AK ≠ 单字母 A**。与假设 **K（融券空头名单 PIT）** **硬分列**：K = 空头标的当时名单；本页 = 集合竞价**时段撮合方式**，不碰融券名单。双字母 **AK ≠ 单字母 K**。与假设 **AH（不可撤窗假撤改）** **分列**：AH = 9:20–9:25 / 14:57–15:00 **能否撤改**；本页 = 整段集合窗内**撮合机制**是否被发明成连续逐笔，不重开撤改权。与假设 **N（收盘机制与假 GTC）** **分列**：N = 沪市收盘价产生方式**历史切日**误套 + 限价**隔夜**假 GTC；本页 = 在**已适用收盘集合**的样本日，仍把 14:57–15:00（及开盘 9:15–9:25）当成连续撮合，不重开切日/隔夜有效。与假设 **AJ（临停复牌假连续）** **分列**：AJ = 无板日临停**复牌瞬间**跳过复牌集合；本页 = **日常开盘/收盘集合窗**假连续，不要求临停事件。与假设 **Y（集合量分母）** **分列**：Y = 冲击/κ 分母是否吞集合量；本页 = 集合窗内成交**路径**是否假连续。与假设 **D（开/收时点）** **分列**：D = 次日开 vs 收成交时点与停牌假成交；本页 = 集合窗内撮合方式。与假设 A/H/X/E/M/O/R/Q/AC–AJ/I/F/L/G/J **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AK** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AK / 假设-AK / hypothesis_id=AK / 组 AK0·AK1·AK2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AK 与单字母实验 **A**、单字母实验 **K**、或 params 键名 `ak0_*` 以外的实验页混读。**双字母 AK ≠ 单字母 A ≠ 单字母 K**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，在**开盘集合竞价 9:15–9:25** 或**收盘集合竞价 14:57–15:00** 时段，把集合竞价改成连续竞价逐笔多价撮合（或按窗内高低价/多笔冲击发明集合路径），相对「集合阶段对已接受申报做一次集中撮合、产生单一开盘价/收盘价（产生不了再按规则退回）；连续竞价仅在 9:30–11:30 / 13:00–14:57」的 PIT 诚实组，会**系统性发明集合时段假连续路径并高估可成交名义 / 错价冲击**；差异应**集中在开盘集合假连续 / 收盘集合假连续 / 多价冲击桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的集合假连续贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在集合时段撮合机制相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 集合竞价时段撮合 ≠ 不可撤窗；≠ 收盘切日/假 GTC；≠ 临停复牌；≠ 板上枯竭；≠ 融券名单

```
# 配置写死键（见 §7；待预检建议值如下，拉数前须冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AK；≠ 实验字母 A；≠ 实验字母 K
# params.asof_check_date                 写死默认 2026-10-02  # 事实与坑「竞价时段 / 开收盘价产生」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；集合窗冲击作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.open_call_start                 写死 09:15
# params.open_call_end                   写死 09:25
# params.close_call_start                写死 14:57
# params.close_call_end                  写死 15:00
# params.continuous_am_start             写死 09:30
# params.continuous_am_end               写死 11:30
# params.continuous_pm_start             写死 13:00
# params.continuous_pm_end               写死 14:57
# params.call_match_honest               写死 single_clearing # 诚实：集合窗一次集中撮合 → 单一开/收盘价
# params.ak0_primary_demo                待预检建议 invent_call_as_continuous  # 主报：集合窗假连续逐笔；禁与 invent_multi_px_in_call 双挂争主表
# params.ak0_invent_call_as_continuous   写死 True           # 天真主路径（与建议主报同向）
# params.ak0_invent_multi_px_in_call     写死 False          # 诊断可叠；主报以 ak0_primary_demo 为准
# params.ak1_close_call_only_fake        写死 True           # 半泄露：仅收盘集合窗发明连续，开盘集合诚实
# params.ak1_invent_call_as_continuous   写死 False          # AK1 主病在收盘窗，不与 AK0 双挂主报
# params.ak2_call_match                  写死 single_clearing
# params.ak2_apply_open_call             写死 True
# params.ak2_apply_close_call            写死 True           # 诚实组：开+收集合均一次集中撮合；收盘切日另页 N
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AK≠A）
# params.merge_with_K_short_list         写死 False          # 融券名单另页 K（AK≠K）
# params.merge_with_AH_nocancel          写死 False          # 不可撤窗另页 AH
# params.merge_with_N_close_gtc          写死 False          # 收盘切日/假 GTC 另页 N
# params.merge_with_AJ_resume            写死 False          # 临停复牌另页 AJ
# params.merge_with_Y_call_volume        写死 False          # 集合量分母另页 Y
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_AI_call_band         写死 False
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
# params.merge_with_G_nolimit_pct        写死 False
# params.universe_rule                   写死 sse_szse_common_stock_call_sessions  # 主宇宙=沪深普通 A 股；集合窗主测
# params.missing_session_clock_policy    写死 skip           # 缺会话钟/时戳 → skip（禁静默当全日连续）
# params.day_freq_proxy                  写死 call_session_match_sensitivity  # 日频无 L2 时只报「集合窗假连续」敏感性档；禁假装精确复盘簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  待预检建议 0.02/0.01/0.05/0.015  # params.Y=相对门槛键 ≠ 实验字母 AK；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-02"
px_basis = "unadj"
tick = 0.01
open_call_start = "09:15"
open_call_end = "09:25"
close_call_start = "14:57"
close_call_end = "15:00"
continuous_am_start = "09:30"
continuous_am_end = "11:30"
continuous_pm_start = "13:00"
continuous_pm_end = "14:57"
call_match_honest = "single_clearing"
ak0_primary_demo = "invent_call_as_continuous"  # 待预检建议；禁双挂
ak0_invent_call_as_continuous = True
ak0_invent_multi_px_in_call = False
ak1_close_call_only_fake = True
ak1_invent_call_as_continuous = False
ak2_call_match = "single_clearing"
ak2_apply_open_call = True
ak2_apply_close_call = True
universe_rule = "sse_szse_common_stock_call_sessions"
missing_session_clock_policy = "skip"
day_freq_proxy = "call_session_match_sensitivity"

# 待预检建议（拉数前须写死冻结）；禁 holdout / 事后改口 / 禁跑后改 ak0_primary_demo
Y = 0.02   # 相对门槛 ≠ 实验字母 AK
G = 0.01
N = 0.05
Y2 = 0.015

def in_open_call(ts):
    return open_call_start <= ts < open_call_end

def in_close_call(ts):
    return close_call_start <= ts <= close_call_end

def in_continuous(ts):
    return (continuous_am_start <= ts <= continuous_am_end) or (continuous_pm_start <= ts < continuous_pm_end)

def call_match_mode(group, ts):
    """
    AK0：开+收集合窗均假连续（按 ak0_primary_demo）
    AK1：仅收盘集合窗假连续；开盘集合诚实
    AK2：开+收集合均 single_clearing；连续窗才允许连续撮合
    """
    if group == "AK0" and (in_open_call(ts) or in_close_call(ts)) and ak0_invent_call_as_continuous:
        return "invent_continuous_in_call"
    if group == "AK0" and (in_open_call(ts) or in_close_call(ts)) and ak0_invent_multi_px_in_call:
        return "invent_multi_px_in_call"
    if group == "AK1" and ak1_close_call_only_fake and in_close_call(ts):
        return "invent_continuous_in_close_call_only"
    if in_open_call(ts) or in_close_call(ts):
        return "honest_single_clearing"
    if in_continuous(ts):
        return "honest_continuous"
    return "out_of_auction_skip"
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺会话钟/时戳却硬判集合窗连续可成、把 AH 撤改权 / N 收盘切日·假 GTC / AJ 复牌 / Y 集合量分母 / A 板上 / K 融券名单混进本页主表、日频无代理声明却假装 L2 复盘集合簿、诚实组集合窗仍记多价连续成交 → **跳过该日该券该腿**，不静默记集合假连续成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AK）

| 组 | 集合窗撮合 | 说明 |
|----|------------|------|
| AK0 天真 | 开+收集合窗假连续（按 `ak0_primary_demo` 单一主报） | 发明集合时段假连续路径 |
| AK1 半泄露/混口径 | 仅收盘集合窗假连续；开盘集合诚实 | 混口径假路径 |
| AK2 PIT 诚实 | 开+收集合均一次集中撮合（`single_clearing`）；连续仅在连续窗 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测集合竞价时段撮合方式执行诚信**，不主测不可撤窗（见 AH）、不主测收盘切日/隔夜 GTC（见 N）、不主测临停复牌（见 AJ）、不主测集合量分母（见 Y）、不主测板上枯竭（见 A）、不主测融券名单（见 K）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_A_fill=False` / `merge_with_K_short_list=False` / `merge_with_AH_nocancel=False` / `merge_with_N_close_gtc=False` / `merge_with_AJ_resume=False` / `merge_with_Y_call_volume=False` / `merge_with_D_halt_timing=False` / `merge_with_J_halt=False` / `merge_with_AI_call_band=False` / `merge_with_AG_beyond_limit=False` / `merge_with_I_cage=False` / `merge_with_F_round=False` / `merge_with_L_mkt=False` / `merge_with_H_exit=False` / `merge_with_X_st_limit=False` / `merge_with_E_lot=False` / `merge_with_M_aft=False` / `merge_with_O_block=False` / `merge_with_R_etf_rotation=False` / `merge_with_Q_cb_rotation=False` / `merge_with_AC_bse=False` / `merge_with_AD_50w=False` / `merge_with_AE_stock_t0=False` / `merge_with_AF_qty_cap=False` / `merge_with_G_nolimit_pct=False`（写死）**。

**待预检键（建议值；拉数前须冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 可成交名义/冲击差显著门槛；≠实验字母 AK
params.G                            = 0.01                      # 集合假连续桶相对对照差
params.N                            = 0.05                      # 失败/废单率差门槛
params.Y2                           = 0.015                     # AK1（仅收盘窗假连续）相对 AK2 专项门槛
params.ak0_primary_demo             = invent_call_as_continuous # 主报：集合窗假连续；禁与 invent_multi_px_in_call 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_call_sessions`）。ETF、可转债、北交所不进主宇宙。沪市股票 `<2018-08-20` 收盘集合是否适用交 N 切日消费：本页诚实组对「当日规则已是收盘集合」的样本才测收盘窗；切日前样本收盘窗主对比可 skip 或单列桶，**不重开 N 主结论**。  
- **排除（默认）**：缺会话钟/时戳；把 AH/N/AJ/Y/A/K 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：集合/连续时段按成交日当时交易规则文本；**禁止**用核对日规则铺满；收盘集合历史切日交 N，本页只消费「当日已适用开/收集合」事件。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ak0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AK0 − AK2**：开+收集合窗假连续相对诚实一次集中撮合——假路径 / 可成交名义吹胖。  
2. **AK1 − AK2**：仅收盘集合窗假连续相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_open_call_as_continuous",   # 开盘集合窗假连续
  "invent_close_call_as_continuous",  # 收盘集合窗假连续
  "invent_multi_px_in_call",          # 集合窗内多价冲击
  "honest_single_clearing",           # 对照诚实一次集中撮合
  "vs_AH_nocancel",                   # 对照声明：不可撤窗另页 AH
  "vs_N_close_mech",                  # 对照声明：收盘切日/假 GTC 另页 N
  "vs_AJ_resume",                     # 对照声明：临停复牌另页 AJ
  "vs_Y_call_volume",                 # 对照声明：集合量分母另页 Y
  "vs_A_fill",                        # 对照声明：板上枯竭另页 A（AK≠A）
  "vs_K_short_list",                  # 对照声明：融券名单另页 K（AK≠K）
  "vs_D_halt_timing",                 # 对照声明：开收时点/停牌另页 D
  "day_freq_proxy_only",              # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AK0/AK1 相对 AK2）；  
2. 集合假连续腿贡献差 ΔFakeCallCont；  
3. 废单/失败率差 ΔFail；  
4. （可选）集合窗冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeCallCont 桶贡献| **≥ params.G** 或 |ΔNotional_(AK1−AK2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「集合竞价时段撮合执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AK 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AK） | **待预检建议** `0.02`；拉数前须写死冻结 |
| params.G | 集合假连续桶相对对照差 | **待预检建议** `0.01`；拉数前须写死冻结 |
| params.N | 失败/废单率差门槛 | **待预检建议** `0.05`；拉数前须写死冻结 |
| params.Y2 | AK1−AK2 专项门槛 | **待预检建议** `0.015`；拉数前须写死冻结 |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-02` |
| fill_time | 成交时点 | **写死** `next_open` |
| ak0_primary_demo | 天真主报枚举 | **待预检建议** `invent_call_as_continuous`（禁双挂） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组集合窗须一次集中撮合；禁与 AH/N/AJ/Y/A/K 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分集合窗与连续窗成交，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把不可撤窗（AH）、收盘切日/假 GTC（N）、临停复牌（AJ）、集合量分母（Y）、板上枯竭（A）、融券名单（K）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「集合窗假连续」写成「临停复牌跳过集合」而不声明另页 AJ → 与 AJ 撞题，设计失效。  
4. holdout 反调 `ak0_primary_demo` / Y·G·N·Y2 → 结论无效。  
5. 用复权价算集合参考价或冲击 → 标签与执行双错，结论无效。  
6. 把实验字母 AK 与单字母 A 或单字母 K 或 `params.Y` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权 OHLC、交易所、买卖方向、拟挂限价；  
- 会话钟/申报或成交时戳（Asia/Shanghai）；是否落在开盘集合 / 连续 / 收盘集合；  
- （可选）沪市股票是否 ≥2018-08-20 才测收盘集合窗（切日消费 N，不重开）；  
- 交易日历。

可选：L2/逐笔（精确复盘集合簿与连续簿）；开盘价/收盘价产生方式标记。

**禁止**：用核对日现行规则铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 AH 的「假撤改」或 N 的「假 GTC」当成本页主病；把 AJ 复牌事件当成本页日常集合窗。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AK`  
- **组**：AK0 / AK1 / AK2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-02`；`open_call=09:15-09:25`；`close_call=14:57-15:00`；`continuous=09:30-11:30|13:00-14:57`；`call_match_honest=single_clearing`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_call_sessions`；`missing_session_clock_policy=skip`；`day_freq_proxy=call_session_match_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 待预检建议 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AK；禁 null/holdout）；**`params.ak0_primary_demo` 待预检建议 `invent_call_as_continuous`**（禁与 invent_multi_px_in_call 双挂）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AK0/AK1/AK2 可成交名义/路径质量、ΔFakeCallCont、ΔFail；分桶（开盘集合假连续 / 收盘集合假连续 / 多价冲击 / vs AH·N·AJ·Y·A·K·D）。  
- 自检布尔：AK2 是否集合窗一次集中撮合；AK0 是否单一主报；AK1 是否仅收盘窗假连续；是否未与 AH/N/AJ/Y/A/K 混主结论；holdout 是否未反调；**是否未把实验字母 AK 与 A 或 K 或 params.Y 混用**；**是否未改 Y/Z/AA–AJ 冻结补丁正文**；**是否未改假设-H / 假设-K / 假设-N / 假设-AH**。  
- **禁止输出**：具体买卖标的列表当「建议」；把集合窗假连续当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AJ 及其他 A/D–AJ 已交正文**；**不改假设-H**；**不改假设-K**；**不改假设-N**；**不改假设-AH**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：沪深现行 **9:15–9:25** 开盘集合、**9:30–11:30 / 13:00–14:57** 连续、**14:57–15:00** 收盘集合；开盘价/收盘价由集合竞价产生（产生不了再按规则退回）。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AJ，本页**新增实验 AK** 收成标准件，**不改口径主线**，**不改假设 A–AJ 正文**。与实验 AH/N/AJ/Y/A/K/D 分工：**AH=不可撤窗假撤改；N=收盘切日+隔夜假 GTC；AJ=临停复牌跳过集合；Y=集合量分母；A=板上枯竭；K=融券名单；D=开收时点/停牌；AK=开盘/收盘集合竞价时段假连续撮合（AK≠A≠K）**。

---

## 9. ״̬

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；会话钟或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-02；**fill_time=next_open 写死**；**call_match_honest=single_clearing + 开/收集合钟点写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 待预检建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AK）**；**ak0_primary_demo 待预检建议 invent_call_as_continuous（禁双挂）** |

---

## 待预检键（纸面占位；拉数前须冻结）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：建议 **`0.02` / `0.01` / `0.05` / `0.015`**；**`params.Y` ≠ 实验字母 AK**；禁 null / holdout 标定。  
2. **`params.ak0_primary_demo`**：建议 **`invent_call_as_continuous`**；禁与 **`invent_multi_px_in_call`** 双挂争主表。

---

## 变更

- 2026-11-02：新建标准件（总管线：AJ 补丁已交后写下一纸面 AK；Y/Z/AA–AJ 补丁已交不改；清单止于 AJ → 自 `事实与坑`「开盘集合 9:15–9:25 / 连续 9:30–11:30·13:00–14:57 / 收盘集合 14:57–15:00；开收盘价由集合产生」选题，**与 A/H/X/E/M/O/AC–AJ/R/Q/I/F/L/J/G/D/N/Y/K 不撞主结论**；**明确双字母 AK ≠ 单字母 A ≠ 单字母 K**；近邻 AH=不可撤窗、N=收盘切日/假 GTC、AJ=复牌跳过集合、Y=集合量分母、A=板上、K=融券名单，本页主测集合竞价时段假连续撮合；**实验字母 AK ≠ params.Y ≠ 实验字母 A ≠ 实验字母 K**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA–AJ/A/D–AJ 正文**；**不改假设-H**；**不改假设-K**；**不改假设-N**；**不改假设-AH**）。