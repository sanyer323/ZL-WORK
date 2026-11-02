# 假设 AM · 停牌期间假连续撮合（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AL 补丁已交后写下一纸面 AM；清单原止于 AL，无 AM 节 → 自立实验 AM；选题自 `事实与坑`「无涨跌幅日盘中临时停牌：停牌期间可申报也可撤单；复牌对已接受申报做集合竞价；跨越 14:57 且须当日复牌的，于 14:57 复牌（先复牌集合再收盘集合）（上交所 4.2.5；深交所 4.3.4 / 4.3.6）。核对日锚 2026-10-12」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AJ（临停复牌假连续）/ AK（集合竞价时段假连续）/ AL（午休与开盘空窗假连续）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价通道）/ G（无板日误套板块默认板）/ J（无板日临停触发）/ D（成交时点与停牌）/ N（收盘机制与假 GTC）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区误标）**分列**；**新建实验 AM**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「停牌钟点内仍连续撮合」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AL 及其他 A/D–AL 已交正文与冻结补丁；不改假设-H；不改假设-J；不改假设-AJ；不改假设-D；不改假设-M；不改假设-AL**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AL，本页自立实验 AM 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **停牌（含临停与其他停牌）钟点内是否被发明成连续可撮合**。双字母 **AM ≠ 单字母 A**。与假设 **M（盘后补成交）** **硬分列**：M = 盘后固定价格通道误套/竞价剩单自动进盘后；本页 = **竞价时段内停牌窗**假连续撮合，**不**开盘后 15:05 通道。双字母 **AM ≠ 单字母 M**。与假设 **J（无板日临停）** **分列**：J = 较开盘价 30%/60% **触发**与用最高/最低穿过临停窗当全日连续可成；本页 = 一旦已处停牌钟点，**窗内**是否仍记连续成交（不重开 30%/60% 触发主结论）。与假设 **AJ（临停复牌假连续）** **分列**：AJ = **复牌瞬间**跳过复牌集合、假连续；本页 = **停牌持续期间**假连续，不主测复牌撮合方式。与假设 **D（成交时点与停牌）** **分列**：D = 次日开/收成交时点与**全日**停牌/无成交当横盘可交易；本页 = **日内停牌钟点**撮合可否。与假设 **AL（午休与开盘空窗）** **分列**：AL = 日常非停牌的会话空窗；本页 = **停牌事件驱动**的不可连续撮合窗。与假设 A/H/X/E/M/O/R/Q/AC–AL/I/F/L/G/J/N/Y/AA/D/K **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AM** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AM / 假设-AM / hypothesis_id=AM / 组 AM0·AM1·AM2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AM 与单字母实验 **A**、单字母实验 **M**、或 params 键名 `am0_*` 以外的实验页混读。**双字母 AM ≠ 单字母 A ≠ 单字母 M**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，在**停牌期间**（含无板日盘中临停及其他已标停牌钟点）把本不应连续撮合的时段当成连续竞价可成交（或按停牌窗内高低/末笔发明冲击路径），相对「停牌期间可申报/可撤单、**不**连续撮合；复牌对已接受申报做集合竞价（复牌撮合方式另页 AJ）；连续仅在未停牌的连续竞价窗」的 PIT 诚实组，会**系统性发明停牌窗假连续路径并高估可成交名义 / 错价冲击**；差异应**集中在停牌窗假连续 / 临停窗假连续桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的停牌窗假连续贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在停牌钟点相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 停牌窗假连续 ≠ 临停触发；≠ 复牌撮合；≠ 全日停牌横盘；≠ 盘后；≠ 板上枯竭；≠ 会话空窗

```
# 配置写死键（见 §7；两条待预检键见文末）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AM；≠ 实验字母 A；≠ 实验字母 M
# params.asof_check_date                 写死默认 2026-10-12  # 事实与坑「临停/停牌期间可申报撤单、复牌集合」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；停牌窗冲击作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.halt_match_honest               写死 no_continuous_match  # 诚实：停牌窗不连续撮合（可申报/撤单不记成交）
# params.halt_accept_orders_honest       写死 True           # 诚实：停牌窗可接受申报/撤单（不因此发明成交）
# params.resume_match_handoff            写死 aj_page        # 复牌撮合方式交 AJ；本页不重开
# params.am0_primary_demo                待预检（建议 invent_halt_window_continuous_fill）；禁与 invent_halt_as_flat_tradeable 双挂
# params.am0_invent_halt_continuous      写死 True           # 天真主路径（随 primary_demo）
# params.am1_intraday_temp_halt_only     写死 True           # 半泄露：仅临停窗发明连续；其他停牌诚实 no_match
# params.am2_halt_match                  写死 no_continuous_match
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AM≠A）
# params.merge_with_M_aft                写死 False          # 盘后通道另页 M（AM≠M）
# params.merge_with_J_halt               写死 False          # 临停 30%/60% 触发另页 J
# params.merge_with_AJ_resume            写死 False          # 复牌跳过集合另页 AJ
# params.merge_with_D_halt_timing        写死 False          # 开收时点/全日停牌另页 D
# params.merge_with_AL_session_gap       写死 False          # 午休/开盘空窗另页 AL
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_Q_cb_rotation        写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.universe_rule                   写死 sse_szse_common_stock_halt_windows  # 主宇宙=沪深普通 A 股；停牌窗主测
# params.missing_halt_clock_policy       写死 skip           # 缺停牌起止钟/时戳 → skip（禁静默当未停牌连续）
# params.day_freq_proxy                  写死 halt_window_match_sensitivity  # 日频无 L2 时只报「停牌窗假连续」敏感性档；禁假装精确复盘簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  键名稳、值待预检（建议 0.02/0.01/0.05/0.015）；params.Y≠实验字母 AM；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-12"
px_basis = "unadj"
tick = 0.01
halt_match_honest = "no_continuous_match"
halt_accept_orders_honest = True
resume_match_handoff = "aj_page"
# am0_primary_demo = 待预检（建议 "invent_halt_window_continuous_fill"）
am0_invent_halt_continuous = True
am1_intraday_temp_halt_only = True
am2_halt_match = "no_continuous_match"
universe_rule = "sse_szse_common_stock_halt_windows"
missing_halt_clock_policy = "skip"
day_freq_proxy = "halt_window_match_sensitivity"

# 拉数前须冻结（待预检；建议值如下；禁 holdout / 事后改口 / 禁跑后改 am0_primary_demo）
# Y = 0.02   # 建议；相对门槛 ≠ 实验字母 AM
# G = 0.01
# N = 0.05
# Y2 = 0.015

def in_halt_window(ts, halt_intervals):
    """halt_intervals: list of [start, end) in session clock; inclusive of temp halt and other suspensions."""
    for a, b in halt_intervals:
        if a <= ts < b:
            return True
    return False

def halt_match_mode(group, ts, halt_intervals, is_temp_halt_only_interval):
    """
    AM0：停牌窗假连续（按 am0_primary_demo）
    AM1：仅临停窗假连续；其他停牌诚实 no_match
    AM2：凡停牌窗均 no_continuous_match
    """
    if not in_halt_window(ts, halt_intervals):
        return "out_of_halt_scope"
    if group == "AM0" and am0_primary_demo == "invent_halt_window_continuous_fill":
        if am0_invent_halt_continuous:
            return "invent_continuous_in_halt"
    if group == "AM1" and am1_intraday_temp_halt_only and is_temp_halt_only_interval:
        return "invent_continuous_in_temp_halt_only"
    return "honest_halt_no_continuous_match"
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺停牌起止钟/时戳却硬判停牌窗连续可成、把 J 临停触发 / AJ 复牌 / D 全日停牌时点 / AL 会话空窗 / A 板上 / M 盘后混进本页主表、日频无代理声明却假装 L2 复盘停牌簿、诚实组停牌窗仍记连续成交 → **跳过该日该券该腿**，不静默记停牌窗假连续成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AM）

| 组 | 停牌窗撮合 | 说明 |
|----|------------|------|
| AM0 天真 | 停牌窗假连续（按 `am0_primary_demo` 单一主报） | 发明停牌窗假连续路径 |
| AM1 半泄露/混口径 | 仅临停窗假连续；其他停牌诚实 no_match | 混口径假路径 |
| AM2 PIT 诚实 | 凡停牌窗 `no_continuous_match`；可申报/撤单不记成交 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测停牌钟点内是否被发明成连续可撮合**，不主测临停 30%/60% 触发（见 J）、不主测复牌撮合方式（见 AJ）、不主测全日停牌横盘/开收时点（见 D）、不主测午休/开盘空窗（见 AL）、不主测盘后（见 M）、不主测板上枯竭（见 A）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/M/J/AJ/D/AL/AK/AH/AI/AG/I/F/L/H/X/E/O/R/Q/AC/AD/AE/AF/G/N/Y/K/AA）**。

**待预检两条（拉数前须写死冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            # 待预检；建议 0.02；可成交名义/冲击差显著门槛；≠实验字母 AM
params.G                            # 待预检；建议 0.01；停牌窗假连续桶相对对照差
params.N                            # 待预检；建议 0.05；失败/废单率差门槛
params.Y2                           # 待预检；建议 0.015；AM1（仅临停窗假连续）相对 AM2 专项门槛
params.am0_primary_demo             # 待预检；建议 invent_halt_window_continuous_fill；禁与 invent_halt_as_flat_tradeable 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_halt_windows`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺停牌起止钟/时戳；把 J/AJ/D/AL/A/M 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：停牌/临停规则按成交日当时交易规则文本；**禁止**用核对日规则铺满；临停触发交 J、复牌交 AJ，本页只测停牌窗内撮合可否。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `am0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AM0 − AM2**：停牌窗假连续相对诚实停牌不连续撮合——假路径 / 可成交名义吹胖。  
2. **AM1 − AM2**：仅临停窗假连续相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_halt_window_continuous",     # 停牌窗假连续（主病）
  "invent_temp_halt_only_continuous",  # 仅临停窗假连续（AM1）
  "honest_halt_no_continuous_match",   # 对照诚实停牌不连续撮合
  "vs_J_halt_trigger",                 # 对照声明：临停 30%/60% 触发另页 J
  "vs_AJ_resume",                      # 对照声明：复牌跳过集合另页 AJ
  "vs_D_halt_timing",                  # 对照声明：开收时点/全日停牌另页 D
  "vs_AL_session_gap",                 # 对照声明：午休/开盘空窗另页 AL
  "vs_A_fill",                         # 对照声明：板上枯竭另页 A（AM≠A）
  "vs_M_aft",                          # 对照声明：盘后另页 M（AM≠M）
  "vs_AK_call_cont",                   # 对照声明：集合窗假连续另页 AK
  "day_freq_proxy_only",               # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AM0/AM1 相对 AM2）；  
2. 停牌窗假连续腿贡献差 ΔFakeHaltCont；  
3. 废单/失败率差 ΔFail；  
4. （可选）停牌窗冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeHaltCont 桶贡献| **≥ params.G** 或 |ΔNotional_(AM1−AM2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「停牌窗撮合执行鸿沟显著」。

**params.Y / G / N / Y2（键名稳；值待预检；与实验字母 AM 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AM） | **待预检**（建议 `0.02`）；拉数前冻结；禁 null/holdout |
| params.G | 停牌窗假连续桶相对对照差 | **待预检**（建议 `0.01`） |
| params.N | 失败/废单率差门槛 | **待预检**（建议 `0.05`） |
| params.Y2 | AM1−AM2 专项门槛 | **待预检**（建议 `0.015`） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-12` |
| fill_time | 成交时点 | **写死** `next_open` |
| am0_primary_demo | 天真主报枚举 | **待预检**（建议 `invent_halt_window_continuous_fill`；禁双挂） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组停牌窗须 no_continuous_match；禁与 J/AJ/D/AL/A/M 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分停牌窗与连续窗成交，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把临停触发（J）、复牌撮合（AJ）、全日停牌时点（D）、会话空窗（AL）、板上枯竭（A）、盘后（M）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「停牌窗假连续」写成「复牌跳过集合」而不声明另页 AJ → 与 AJ 撞题，设计失效。  
4. 把「停牌窗假连续」写成「临停触发/极值可成」而不声明另页 J → 与 J 撞题，设计失效。  
5. holdout 反调 `am0_primary_demo` / Y·G·N·Y2 → 结论无效。  
6. 用复权价算停牌窗参考价或冲击 → 标签与执行双错，结论无效。  
7. 把实验字母 AM 与单字母 A 或单字母 M 或 `params.Y` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权 OHLC、交易所、买卖方向、拟挂限价；  
- 停牌/临停起止钟或公告时段（Asia/Shanghai）；是否落在停牌窗 / 连续 / 集合；  
- 交易日历。

可选：L2/逐笔（精确复盘停牌窗是否出现假撮合标记）；分钟 bar（若做敏感性，须声明与 AA 分列）；临停触发事件（可复用 J，不重开 J 主结论）。

**禁止**：用核对日现行规则铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 J 的「临停触发/极值」或 AJ 的「复牌跳过集合」或 D 的「全日停牌横盘」或 AL 的「会话空窗」或 M 的「盘后」或 A 的「板上枯竭」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AM`  
- **组**：AM0 / AM1 / AM2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-12`；`halt_match_honest=no_continuous_match`；`halt_accept_orders_honest=True`；`resume_match_handoff=aj_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_halt_windows`；`missing_halt_clock_policy=skip`；`day_freq_proxy=halt_window_match_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 键名稳、值待预检（建议 0.02/0.01/0.05/0.015；params.Y≠实验字母 AM；禁 null/holdout）**；**`params.am0_primary_demo` 待预检（建议 invent_halt_window_continuous_fill；禁与 invent_halt_as_flat_tradeable 双挂）**；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AM0/AM1/AM2 可成交名义/路径质量、ΔFakeHaltCont、ΔFail；分桶（停牌窗假连续 / 仅临停窗 / vs J·AJ·D·AL·A·M·AK）。  
- 自检布尔：AM2 是否停牌窗 no_continuous_match；AM0 是否单一主报；AM1 是否仅临停窗假连续；是否未与 J/AJ/D/AL/A/M 混主结论；holdout 是否未反调；**是否未把实验字母 AM 与 A 或 M 或 params.Y 混用**；**是否未改 Y/Z/AA–AL 冻结补丁正文**；**是否未改假设-H / 假设-J / 假设-AJ / 假设-D / 假设-M / 假设-AL**。  
- **禁止输出**：具体买卖标的列表当「建议」；把停牌窗假连续当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AL 及其他 A/D–AL 已交正文**；**不改假设-H**；**不改假设-J**；**不改假设-AJ**；**不改假设-D**；**不改假设-M**；**不改假设-AL**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：停牌期间可申报也可撤单；**不**在停牌钟点内连续撮合；复牌对已接受申报做集合竞价（复牌方式另页 AJ）。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AL，本页**新增实验 AM** 收成标准件，**不改口径主线**，**不改假设 A–AL 正文**。与实验 J/AJ/D/AL/A/M 分工：**J=临停触发与极值；AJ=复牌跳过集合；D=开收时点/全日停牌；AL=会话空窗；A=板上枯竭；M=盘后；AM=停牌期间假连续撮合（AM≠A≠M）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；停牌钟或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-12；**fill_time=next_open 写死**；**halt_match_honest=no_continuous_match 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 键名稳、值待预检（建议 0.02/0.01/0.05/0.015；params.Y≠实验字母 AM）**；**am0_primary_demo 待预检（建议 invent_halt_window_continuous_fill；禁双挂）** |

---

## 待预检键（拉数前不补则打回）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：键名稳；值**待预检**（建议 `0.02` / `0.01` / `0.05` / `0.015`）；**`params.Y` ≠ 实验字母 AM**；须写死冻结；禁 null / holdout 标定。  
2. **`params.am0_primary_demo`**：**待预检**（建议 **`invent_halt_window_continuous_fill`**）；禁与 **`invent_halt_as_flat_tradeable`** 双挂争主表。

---

## 变更

- 2026-11-02：新建标准件（总管线：AL 补丁已交后写下一纸面 AM；Y/Z/AA–AL 补丁已交不改；清单止于 AL → 自 `事实与坑`「停牌期间可申报/撤单、不连续撮合；复牌集合另页」选题，**与 A/H/X/E/M/O/AC–AL/R/Q/I/F/L/J/G/D/N/Y/AA/K 不撞主结论**；**明确双字母 AM ≠ 单字母 A ≠ 单字母 M**；近邻 J=临停触发、AJ=复牌假连续、D=全日停牌时点、AL=会话空窗、A=板上、M=盘后，本页主测停牌期间假连续；**实验字母 AM ≠ params.Y ≠ 实验字母 A ≠ 实验字母 M**；机制类预埋 fail_policy/oos/红线豁免/params 键；**待预检两条**见上；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA–AL/A/D–AL 正文**；**不改假设-H**；**不改假设-J**；**不改假设-AJ**；**不改假设-D**；**不改假设-M**；**不改假设-AL**）。
