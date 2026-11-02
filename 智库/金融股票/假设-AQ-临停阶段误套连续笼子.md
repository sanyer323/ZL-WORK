# 假设 AQ · 临停阶段误套连续价格笼子（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AP 补丁已交后写下一纸面 AQ；清单原止于 AP，无 AQ 节 → 自立实验 AQ；选题自 `事实与坑`「开市期间**临时停牌**阶段的限价**不适用**连续竞价有效申报价格范围两款（买入≤基准价102%与十价位孰高、卖出≥基准价98%与十价位孰低）；超过涨跌幅或有效申报范围=无效申报。上交所 3.3.14/3.3.16；深交所 3.3.16/3.3.18；核对日锚 2026-10-12」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合/临停 ±10% 有效申报范围）/ AJ（临停复牌假连续）/ AK（集合竞价时段假连续）/ AL（午休与开盘空窗假连续）/ AM（停牌期间假连续）/ AN（开盘集合剩单假即时成）/ AO（收盘集合剩单假即时成）/ AP（盘后错侧限价假有效）/ I（连续竞价价格笼子远限价）/ F（涨跌停价取整）/ L（市价通道）/ G（无板日误套板块默认板）/ J（无板日临停触发）/ D（成交时点与停牌）/ N（收盘机制与假 GTC）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区误标）/ P（指数点位停牌假成交权重）**分列**；**新建实验 AQ**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「临停阶段仍套连续笼子拒远限价」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AP 及其他 A/D–AP 已交正文与冻结补丁；不改假设-H；不改假设-I；不改假设-J；不改假设-AI；不改假设-AJ；不改假设-AM；不改假设-A**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AP，本页自立实验 AQ 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **临时停牌阶段**是否仍被发明套上**连续竞价价格笼子**而拒远限价。双字母 **AQ ≠ 单字母 A**。与假设 **Q（可转债规则混用）** **硬分列**：Q = 可转债按股票规则回放（回转/涨跌幅/收盘）；本页 = 普通 A 股**临停窗内连续笼子是否适用**，不主测转债。双字母 **AQ ≠ 单字母 Q**。与假设 **I（价格笼子远限价）** **硬分列**：I = **连续竞价未停牌时段**远限价能否进簿（笼子带宽/切日/科创无十价位）；本页**默认连续时段笼子规则另页 I**，主测**临停阶段误套该连续笼子**（诚实=临停阶段连续笼子两款不适用）。与假设 **AI（无板日集合有效申报范围）** **分列**：AI = 无板日开盘集合 900%/50%、临停/收盘集合 ±10%；本页不重开 ±10% 主测，半泄露仅诊断「无板日临停仍套连续笼子」时对照声明交 AI。与假设 **J（无板日临停）** **分列**：J = 30%/60% 临停**触发**与窗内假连续路径；本页不主测触发阈值，主测触发后/临停窗内**限价进簿是否误套连续笼子**。与假设 **AJ（临停复牌假连续）** **分列**：AJ = 复牌撮合跳过集合；本页 = 临停窗内申报有效性，不重开复牌撮合。与假设 **AM（停牌期间假连续）** **分列**：AM = 停牌窗内假连续**成交**；本页 = 临停窗内假**拒单/假进簿**（笼子误套），不发明连续成交。与假设 A/H/X/E/M/O/R/Q/AC–AP/I/F/L/G/J/N/Y/AA/D/K/P **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AQ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AQ / 假设-AQ / hypothesis_id=AQ / 组 AQ0·AQ1·AQ2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AQ 混读或互改。亦**禁止**把实验字母 AQ 与单字母实验 **A**、单字母实验 **Q**、双字母实验 **AP**、或 params 键名 `aq0_*` 以外的实验页混读。**双字母 AQ ≠ 单字母 A ≠ 单字母 Q ≠ 双字母 AP**；**params.Y ≠ 实验字母 AQ**；**params.N ≠ 实验字母 AQ**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，在**开市期间临时停牌**阶段仍按**连续竞价价格笼子**（买入 ≤ 基准价 102% 与十个最小价位孰高；卖出 ≥ 基准价 98% 与十个最小价位孰低；科创板无十价位另桶）拒远限价进簿，相对「临时停牌阶段连续竞价笼子两款**不适用**；无板日临停有效申报范围另页 AI（±10%）；连续未停牌时段笼子另页 I」的 PIT 诚实组，会**系统性发明临停窗假拒单（或假进簿口径错位）并低估复牌可成交簿 / 可成交名义**；差异应**集中在临停误套连续笼子桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假拒单贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在临停阶段笼子适用性相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 临停误套连续笼子 ≠ 连续时段笼子；≠ 无板日临停 ±10%；≠ 临停触发；≠ 复牌撮合；≠ 停牌窗假连续成交；≠ 板上枯竭

```
# 配置写死键（见 §7；Y/G/N/Y2 与 aq0_primary_demo 待预检建议值）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AQ；≠ 实验字母 A；≠ 实验字母 Q
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AQ
# params.asof_check_date                 写死默认 2026-10-12  # 事实与坑「临停阶段笼子不适用」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；临停窗进簿有效性作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.halt_cage_honest                写死 no_continuous_cage  # 诚实：临停阶段连续笼子两款不适用
# params.continuous_cage_handoff         写死 i_page          # 连续未停牌时段笼子交 I，不重开切日/科创十价位主测
# params.nolimit_halt_band_handoff       写死 ai_page         # 无板日临停 ±10% 交 AI，不重开主测
# params.aq0_primary_demo                待预检建议 invent_halt_apply_continuous_cage  # 主报：临停仍套连续笼子拒远限价；禁与 invent_halt_as_always_accept_far 双挂
# params.aq0_invent_halt_cage_reject     写死 True           # 天真主路径（随 primary_demo）
# params.aq1_nolimit_halt_cage_only     写死 True           # 半泄露：仅无板日临停仍套连续笼子（±10% 诚实可诊断；对照交 AI）
# params.aq2_halt_cage_policy            写死 no_continuous_cage
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AQ≠A）
# params.merge_with_Q_cb                 写死 False          # 可转债另页 Q（AQ≠Q）
# params.merge_with_I_cage               写死 False          # 连续时段笼子另页 I
# params.merge_with_AI_call_band         写死 False          # 无板日集合/临停 ±10% 另页 AI
# params.merge_with_J_halt               写死 False          # 临停触发另页 J
# params.merge_with_AJ_resume            写死 False          # 复牌撮合另页 AJ
# params.merge_with_AM_halt              写死 False          # 停牌窗假连续成交另页 AM
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_AL_session_gap       写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_P_index_halt         写死 False
# params.universe_rule                   写死 sse_szse_common_stock_halt_cage_check
# params.missing_halt_cage_policy        写死 skip           # 缺临停钟/拟挂限价/基准价标记 → skip（禁静默当连续笼子可拒）
# params.day_freq_proxy                  写死 halt_cage_sensitivity  # 日频无 L2 时只报敏感性档；禁假装精确复盘临停簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  待预检建议 0.02/0.01/0.05/0.015  # params.Y=相对门槛键 ≠ 实验字母 AQ；params.N≠实验字母 AQ；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-12"
px_basis = "unadj"
tick = 0.01
halt_cage_honest = "no_continuous_cage"
continuous_cage_handoff = "i_page"
nolimit_halt_band_handoff = "ai_page"
aq0_primary_demo = "invent_halt_apply_continuous_cage"  # 待预检建议；禁双挂
aq0_invent_halt_cage_reject = True
aq1_nolimit_halt_cage_only = True
aq2_halt_cage_policy = "no_continuous_cage"
universe_rule = "sse_szse_common_stock_halt_cage_check"
missing_halt_cage_policy = "skip"
day_freq_proxy = "halt_cage_sensitivity"

# 拉数前待预检建议；禁 holdout / 事后改口 / 禁跑后改 aq0_primary_demo
Y = 0.02   # 待预检建议；相对门槛 ≠ 实验字母 AQ
G = 0.01
N = 0.05   # 待预检建议；失败率门槛键 params.N ≠ 实验字母 AQ
Y2 = 0.015

def in_temp_halt(ts, halt_windows):
    """Asia/Shanghai 会话钟是否落在临时停牌窗（含无板日临停与其他开市临停）。"""
    return any(w.start <= ts < w.end for w in halt_windows)

def would_reject_by_continuous_cage(side, limit_px, baseline_px, board, cage_impl):
    """连续竞价笼子判定代理；切日/科创无十价位细节交 I，本页只消费「若套连续笼子会否拒」。"""
    return cage_impl.would_reject(side, limit_px, baseline_px, board)

def halt_cage_policy(group, side, limit_px, baseline_px, board, in_halt, is_nolimit_day, cage_impl):
    """
    AQ0：按 aq0_primary_demo 单一主报（建议 invent_halt_apply_continuous_cage）
    AQ1：仅无板日临停仍套连续笼子；有板日临停可按诚实 no_continuous_cage（对照交 AI）
    AQ2：凡临停窗 no_continuous_cage（不发明连续笼子拒单）
    """
    if not in_halt:
        return "not_in_halt_handoff_I"  # 连续未停牌交 I
    if group == "AQ0" and aq0_primary_demo == "invent_halt_apply_continuous_cage":
        if aq0_invent_halt_cage_reject and would_reject_by_continuous_cage(side, limit_px, baseline_px, board, cage_impl):
            return "invent_halt_cage_reject"
        return "halt_accept_or_other_gate"
    if group == "AQ1" and aq1_nolimit_halt_cage_only:
        if is_nolimit_day and would_reject_by_continuous_cage(side, limit_px, baseline_px, board, cage_impl):
            return "invent_nolimit_halt_cage_reject"
        return "honest_no_continuous_cage_or_ai_band"
    # AQ2
    return "honest_no_continuous_cage"
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺临停钟/拟挂限价/基准价标记却硬判连续笼子可拒、把 I 连续时段笼子 / AI 无板日 ±10% / J 临停触发 / AJ 复牌撮合 / AM 停牌窗假连续成交 / A 板上 / Q 转债混进本页主表、日频无代理声明却假装 L2 复盘临停簿、诚实组临停窗仍按连续笼子拒远限价 → **跳过该日该券该腿**，不静默记假拒单。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AQ）

| 组 | 临停窗笼子适用 | 说明 |
|----|----------------|------|
| AQ0 天真 | 临停仍套连续笼子拒远限价（按 `aq0_primary_demo` 单一主报） | 发明临停假拒单路径 |
| AQ1 半泄露/混口径 | 仅无板日临停仍套连续笼子；有板日临停可诚实 | 混口径假路径；对照声明交 AI |
| AQ2 PIT 诚实 | 临停阶段 no_continuous_cage | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测临时停牌阶段连续价格笼子是否被误套**，不主测连续未停牌时段笼子带宽/切日（见 I）、不主测无板日临停 ±10% 主规则（见 AI）、不主测 30%/60% 触发（见 J）、不主测复牌撮合（见 AJ）、不主测停牌窗假连续成交（见 AM）、不主测板上枯竭（见 A）、不主测可转债（见 Q）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/Q/I/AI/J/AJ/AM/AP/AO/AN/AK/AL/AH/AG/F/L/H/X/E/M/O/R/AC/AD/AE/AF/G/D/N/Y/K/AA/P）**。

**待预检键（拉数前须冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 待预检建议；可成交名义/冲击差显著门槛；≠实验字母 AQ
params.G                            = 0.01                      # 待预检建议；临停误套笼子桶相对对照差
params.N                            = 0.05                      # 待预检建议；失败/废单率差门槛；≠实验字母 AQ
params.Y2                           = 0.015                     # 待预检建议；AQ1（无板日临停误套笼子）相对 AQ2 专项门槛
params.aq0_primary_demo             = invent_halt_apply_continuous_cage  # 待预检建议主报：临停仍套连续笼子；禁与 invent_halt_as_always_accept_far 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_halt_cage_check`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺临停钟/拟挂限价/基准价；连续未停牌却未声明 handoff I；把 I/AI/J/AJ/AM/A/Q 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：临停阶段笼子适用性按成交日当时交易规则文本；**连续时段笼子切日/科创十价位交 I**；**无板日临停 ±10% 交 AI**；**禁止**用核对日规则铺满。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `aq0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AQ0 − AQ2**：临停仍套连续笼子拒远限价相对诚实 no_continuous_cage——假拒单 / 可成交名义低估。  
2. **AQ1 − AQ2**：仅无板日临停仍套连续笼子相对诚实——混口径假路径（对照声明交 AI）。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_halt_apply_continuous_cage",   # 临停误套连续笼子拒远限价（主病）
  "invent_nolimit_halt_cage_reject",     # 无板日临停仍套连续笼子（AQ1；对照交 AI）
  "honest_no_continuous_cage",           # 对照诚实临停不适用连续笼子
  "vs_I_continuous_cage",                # 对照声明：连续未停牌笼子另页 I
  "vs_AI_nolimit_halt_band",            # 对照声明：无板日临停 ±10% 另页 AI
  "vs_J_halt_trigger",                   # 对照声明：临停触发另页 J
  "vs_AJ_resume_match",                  # 对照声明：复牌撮合另页 AJ
  "vs_AM_halt_cont",                     # 对照声明：停牌窗假连续成交另页 AM
  "vs_A_fill",                           # 对照声明：板上枯竭另页 A（AQ≠A）
  "vs_Q_cb",                             # 对照声明：可转债另页 Q（AQ≠Q）
  "vs_AP_aft_side",                      # 对照声明：盘后错侧另页 AP
  "day_freq_proxy_only",                 # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AQ0/AQ1 相对 AQ2）；  
2. 临停误套笼子假拒单腿贡献差 ΔFakeHaltCage；  
3. 废单/失败率差 ΔFail；  
4. （可选）复牌簿深度/冲击差 ΔImpact（声明为代理，不冒充 L2）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeHaltCage 桶贡献| **≥ params.G** 或 |ΔNotional_(AQ1−AQ2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「临停阶段笼子适用性执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AQ 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AQ） | **待预检建议** `0.02` |
| params.G | 临停误套笼子桶相对对照差 | **待预检建议** `0.01` |
| params.N | 失败/废单率差门槛（≠实验字母 AQ） | **待预检建议** `0.05` |
| params.Y2 | AQ1−AQ2 专项门槛 | **待预检建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-12` |
| fill_time | 成交时点 | **写死** `next_open` |
| aq0_primary_demo | 天真主报枚举 | **待预检建议** `invent_halt_apply_continuous_cage`（禁双挂） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组临停窗须 no_continuous_cage；禁与 I/AI/J/AJ/AM/A/Q 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分临停窗与连续未停牌腿，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把连续时段笼子（I）、无板日临停 ±10%（AI）、临停触发（J）、复牌撮合（AJ）、停牌窗假连续成交（AM）、板上枯竭（A）、可转债（Q）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「临停误套连续笼子」写成「连续未停牌远限价笼子带宽」为主病而不声明另页 I → 与 I 撞题，设计失效。  
4. 把「临停误套连续笼子」写成「无板日临停 ±10% 有效申报范围」而不声明另页 AI → 与 AI 撞题，设计失效。  
5. 把「临停误套连续笼子」写成「临停触发」或「复牌假连续」或「停牌窗假连续成交」而不声明另页 J/AJ/AM → 与 J/AJ/AM 撞题，设计失效。  
6. holdout 反调 `aq0_primary_demo` / Y·G·N·Y2 → 结论无效。  
7. 用复权价算基准价或冲击 → 标签与执行双错，结论无效。  
8. 把实验字母 AQ 与单字母 A 或单字母 Q 或双字母 AP 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、拟挂限价、买卖方向、交易所、板块；  
- 临时停牌起止钟或公告时段（Asia/Shanghai）；是否无板日标签（可复用 G，不重开）；  
- 连续笼子「若套上会否拒」代理所需基准价字段（或显式消费 I 的 cage_impl，不重开切日主测）；  
- 交易日历。

可选：逐笔/盘口（精确复盘临停进簿）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日现行规则铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 I 的「连续时段笼子」或 AI 的「无板日临停 ±10%」或 J 的「临停触发」或 AJ 的「复牌撮合」或 AM 的「停牌窗假连续成交」或 A 的「板上枯竭」或 Q 的「可转债」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AQ`  
- **组**：AQ0 / AQ1 / AQ2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-12`；`halt_cage_honest=no_continuous_cage`；`continuous_cage_handoff=i_page`；`nolimit_halt_band_handoff=ai_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_halt_cage_check`；`missing_halt_cage_policy=skip`；`day_freq_proxy=halt_cage_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 待预检建议 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AQ；**params.N≠实验字母 AQ**；禁 null/holdout）；**`params.aq0_primary_demo` 待预检建议 `invent_halt_apply_continuous_cage`**（禁与 invent_halt_as_always_accept_far 双挂）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AQ0/AQ1/AQ2 可成交名义/路径质量、ΔFakeHaltCage、ΔFail；分桶（临停误套笼子 / 无板日临停误套 / vs I·AI·J·AJ·AM·A·Q）。  
- 自检布尔：AQ2 是否临停窗 no_continuous_cage；AQ0 是否单一主报；AQ1 是否仅无板日临停误套；是否未与 I/AI/J/AJ/AM/A/Q 混主结论；holdout 是否未反调；**是否未把实验字母 AQ 与 A 或 Q 或 AP 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AP 冻结补丁正文**；**是否未改假设-H / 假设-I / 假设-J / 假设-AI / 假设-AJ / 假设-AM / 假设-A / 假设-Q**。  
- **禁止输出**：具体买卖标的列表当「建议」；把临停误套连续笼子当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AP 及其他 A/D–AP 已交正文**；**不改假设-H**；**不改假设-I**；**不改假设-J**；**不改假设-AI**；**不改假设-AJ**；**不改假设-AM**；**不改假设-A**；**不改假设-Q**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：开市期间临时停牌阶段的限价不适用连续竞价有效申报价格范围两款；连续未停牌时段笼子另页 I；无板日临停 ±10% 另页 AI。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AP，本页**新增实验 AQ** 收成标准件，**不改口径主线**，**不改假设 A–AP 正文**。与实验 I/AI/J/AJ/AM/A/Q 分工：**I=连续未停牌时段笼子；AI=无板日集合/临停 ±10%；J=临停触发；AJ=复牌撮合；AM=停牌窗假连续成交；A=板上枯竭；Q=可转债；AQ=临停阶段误套连续笼子（AQ≠A≠Q≠I≠AI≠J≠AJ≠AM）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；临停钟+拟挂限价+笼子代理或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-12；**fill_time=next_open 写死**；**halt_cage_honest=no_continuous_cage 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 待预检建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AQ；params.N≠实验字母 AQ）**；**aq0_primary_demo 待预检建议 invent_halt_apply_continuous_cage（禁双挂）** |

---

## 待预检键（草稿占位；拉数前须写死冻结）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**待预检建议** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AQ**；**`params.N` ≠ 实验字母 AQ**；禁 null / holdout 标定。  
2. **`params.aq0_primary_demo`**：**待预检建议** **`invent_halt_apply_continuous_cage`**；禁与 **`invent_halt_as_always_accept_far`** 双挂争主表。

---

## 变更

- 2026-11-02：新建标准件（总管线：AP 补丁已交后写下一纸面 AQ；Y/Z/AA–AP 补丁已交不改；清单止于 AP → 自 `事实与坑`「临停阶段连续笼子不适用」选题，**与 A/H/X/E/M/O/R/Q/AC–AP/I/AI/J/AJ/AM 硬分列**；**双字母 AQ ≠ 单字母 A ≠ 单字母 Q**；结论栏空；不开回测；不抢 A）。
