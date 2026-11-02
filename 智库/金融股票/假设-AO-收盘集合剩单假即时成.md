# 假设 AO · 收盘集合剩单假即时成（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AN 补丁已交后写下一纸面 AO；清单原止于 AN，无 AO 节 → 自立实验 AO；选题自 `事实与坑`「申报当日有效：不能一次全部成交的，未成交部分继续参加当日竞价；当前竞价阶段未成交的买卖申报，自动进入当日后续竞价阶段；**不隔夜**；竞价剩下的限价单**不会自动变成盘后单**（核对日锚 2026-10-19）」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交 / 竞价剩单自动进盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AJ（临停复牌假连续）/ AK（集合竞价时段假连续）/ AL（午休与开盘空窗假连续）/ AM（停牌期间假连续）/ AN（开盘集合剩单假即时成）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价通道）/ G（无板日误套板块默认板）/ J（无板日临停触发）/ D（成交时点与停牌）/ N（收盘机制与假 GTC）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区误标）**分列**；**新建实验 AO**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「收盘集合未成交部分按收盘价即时全成」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AN 及其他 A/D–AN 已交正文与冻结补丁；不改假设-H；不改假设-N；不改假设-M；不改假设-AN；不改假设-AK；不改假设-O；不改假设-A**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AN，本页自立实验 AO 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **收盘集合撮合后未成交部分**是否被发明成按收盘价即时全成。双字母 **AO ≠ 单字母 A**。与假设 **O（大宗）** **硬分列**：O = 大宗/盘后大宗通道可成交性；本页 = 收盘集合剩单在**当日竞价会话收束后**的命运，**不**主测大宗。双字母 **AO ≠ 单字母 O**。与假设 **AN（开盘集合剩单假即时成）** **硬分列**：AN = **开盘**集合清算后剩单 → 应转入 9:30 连续；本页 = **收盘**集合清算后剩单 → 当日有效结束应作废，**不**发明按收盘价全成、**不**隔夜、**不**自动进盘后。双字母 **AO ≠ AN**。与假设 **M（盘后补成交）** **分列**：M = 盘后通道 PIT + 竞价剩单**自动进盘后 15:05**；本页主病 = 收盘集合剩单**假按收盘价即时全成**；AO1 半泄露桶可诊断「假进盘后」，主结论仍交 M。与假设 **N（收盘机制与假 GTC）** **分列**：N = 收盘价产生方式误套 + **隔夜**假 GTC；本页 = 收盘集合清算后**当日**剩单是否被发明成交，**不**主测隔夜有效、**不**主测收盘切日公式。与假设 **AK（集合时段假连续）** **分列**：AK = 集合**窗内**改成连续多价撮合；本页 = 收盘集合**清算后**剩单命运。与假设 **Y（集合量分母）** **分列**：Y = 集合成交量是否计入日线分母；本页 = 剩单执行路径。与假设 A/H/X/E/M/O/R/Q/AC–AN/I/F/L/G/J/N/Y/AA/D/K **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AO** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AO / 假设-AO / hypothesis_id=AO / 组 AO0·AO1·AO2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AO 混读或互改。亦**禁止**把实验字母 AO 与单字母实验 **A**、单字母实验 **O**、双字母实验 **AN**、或 params 键名 `ao0_*` 以外的实验页混读。**双字母 AO ≠ 单字母 A ≠ 单字母 O ≠ 双字母 AN**；**params.Y ≠ 实验字母 AO**；**params.N ≠ 实验字母 AO**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，在**收盘集合竞价清算后**，把未成交部分当成按**收盘价即时全成**（或假滚进盘后而不另下收盘定价申报），相对「收盘集合未成交部分随**申报当日有效**结束而失效；**不**按收盘价即时发明全成、**不**隔夜、**不**自动变成盘后单」的 PIT 诚实组，会**系统性发明收盘集合剩单假即时成（或假进盘后）路径并高估可成交名义 / 错价冲击**；差异应**集中在收盘集合剩单假即时成 / 假进盘后桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的剩单假即时成贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在收盘集合剩单交接相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 收盘集合剩单假即时成 ≠ 开盘集合剩单假即时成；≠ 剩单进盘后；≠ 隔夜假 GTC；≠ 集合窗假连续；≠ 板上枯竭；≠ 大宗

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AO；≠ 实验字母 A；≠ 实验字母 O
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AO
# params.asof_check_date                 写死默认 2026-10-19  # 事实与坑「申报当日有效 / 竞价剩单不自动进盘后」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；收盘集合剩单交接作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.close_call_start                写死 14:57
# params.close_call_end                  写死 15:00
# params.close_call_leftover_honest      写死 expire_after_close_call  # 诚实：当日有效结束，未成交失效
# params.close_call_leftover_instant_fill_honest 写死 False
# params.close_call_leftover_to_aft_honest        写死 False
# params.ao0_primary_demo                写死 invent_close_call_leftover_instant_fill  # 风控补丁冻结；主报：收盘集合剩单假即时成；禁与 invent_close_call_leftover_as_aft 双挂
# params.ao0_invent_instant_fill         写死 True           # 天真主路径（随 primary_demo）
# params.ao1_as_aft_only                 写死 True           # 半泄露：仅假进盘后；不发明按收盘价即时全成（对照交 M）
# params.ao2_leftover_policy             写死 expire_after_close_call
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AO≠A）
# params.merge_with_O_block              写死 False          # 大宗另页 O（AO≠O）
# params.merge_with_AN_open_leftover     写死 False          # 开盘集合剩单另页 AN（AO≠AN）
# params.merge_with_M_aft                写死 False          # 盘后通道/剩单进盘后另页 M
# params.merge_with_N_close_gtc          写死 False          # 收盘切日/隔夜假 GTC 另页 N
# params.merge_with_AK_call_cont         写死 False          # 集合窗假连续另页 AK
# params.merge_with_AL_session_gap       写死 False
# params.merge_with_AM_halt              写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_Q_cb_rotation        写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.universe_rule                   写死 sse_szse_common_stock_close_call_leftover
# params.missing_close_call_leftover_policy 写死 skip       # 缺收盘集合/未成标记 → skip（禁静默当即时全成）
# params.day_freq_proxy                  写死 close_call_leftover_sensitivity  # 日频无 L2 时只报敏感性档；禁假装精确复盘簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AO；params.N≠实验字母 AO；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-19"
px_basis = "unadj"
tick = 0.01
close_call_start = "14:57"
close_call_end = "15:00"
close_call_leftover_honest = "expire_after_close_call"
close_call_leftover_instant_fill_honest = False
close_call_leftover_to_aft_honest = False
ao0_primary_demo = "invent_close_call_leftover_instant_fill"  # 风控补丁冻结；禁双挂
ao0_invent_instant_fill = True
ao1_as_aft_only = True
ao2_leftover_policy = "expire_after_close_call"
universe_rule = "sse_szse_common_stock_close_call_leftover"
missing_close_call_leftover_policy = "skip"
day_freq_proxy = "close_call_leftover_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 ao0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AO
G = 0.01
N = 0.05   # 风控补丁冻结；失败率门槛键 params.N ≠ 实验字母 AO
Y2 = 0.015

def after_close_call_clearing(ts):
    """收盘集合清算完成后的交接点（当日有效结束；不等于盘后窗）。"""
    return ts >= close_call_end

def leftover_policy(group, has_close_call_unfilled):
    """
    AO0：按 ao0_primary_demo 单一主报（写死 invent_close_call_leftover_instant_fill）
    AO1：仅假进盘后（as_aft），不发明按收盘价即时全成；对照声明交 M
    AO2：expire_after_close_call
    """
    if not has_close_call_unfilled:
        return "no_leftover"
    if group == "AO0" and ao0_primary_demo == "invent_close_call_leftover_instant_fill":
        if ao0_invent_instant_fill:
            return "invent_instant_fill_at_close"
    if group == "AO1" and ao1_as_aft_only:
        return "invent_as_aft_without_new_order"
    return "honest_expire_after_close_call"
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺收盘集合未成标记/会话钟却硬判剩单即时全成、把 M 剩单进盘后 / N 隔夜假 GTC / AN 开盘集合剩单 / AK 集合窗假连续 / A 板上 / O 大宗 / Y 集合量分母混进本页主表、日频无代理声明却假装 L2 复盘收盘簿、诚实组剩单仍按收盘价即时全成或假进盘后 → **跳过该日该券该腿**，不静默记假即时成。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AO）

| 组 | 收盘集合剩单 | 说明 |
|----|--------------|------|
| AO0 天真 | 剩单假即时成（按 `ao0_primary_demo` 单一主报） | 发明按收盘价即时全成路径 |
| AO1 半泄露/混口径 | 仅假进盘后；不发明即时全成 | 混口径假路径；主结论交 M |
| AO2 PIT 诚实 | `expire_after_close_call`；不即时全成、不假进盘后、不隔夜 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测收盘集合清算后未成交部分的命运**，不主测开盘集合剩单交接（见 AN）、不主测盘后通道 PIT（见 M）、不主测隔夜假 GTC / 收盘切日（见 N）、不主测集合窗内撮合方式（见 AK）、不主测板上枯竭（见 A）、不主测大宗（见 O）、不主测集合量分母（见 Y）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/O/AN/M/N/AK/AL/AM/Y/AH/AI/AJ/AG/I/F/L/H/X/E/R/Q/AC/AD/AE/AF/G/J/D/K/AA）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 可成交名义/冲击差显著门槛；≠实验字母 AO
params.G                            = 0.01                      # 收盘集合剩单假即时成桶相对对照差
params.N                            = 0.05                      # 失败/废单率差门槛；≠实验字母 AO
params.Y2                           = 0.015                     # AO1（假进盘后）相对 AO2 专项门槛
params.ao0_primary_demo             = invent_close_call_leftover_instant_fill  # 主报：收盘集合剩单假即时成；禁与 invent_close_call_leftover_as_aft 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_close_call_leftover`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺收盘集合/未成标记；把 M/N/AN/AK/A/O/Y 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：申报有效期与阶段交接按成交日当时交易规则文本；**禁止**用核对日规则铺满；隔夜有效交 N、盘后交 M、开盘集合剩单交 AN，本页只测收盘集合清算后剩单是否被发明成交。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ao0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AO0 ? AO2**：收盘集合剩单假即时成相对诚实作废——假路径 / 可成交名义吹胖。  
2. **AO1 ? AO2**：仅假进盘后相对诚实——混口径假路径（对照声明交 M）。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_close_call_leftover_instant_fill",  # 收盘集合剩单假即时成（主病）
  "invent_close_call_leftover_as_aft",        # 假进盘后（AO1；对照交 M）
  "honest_expire_after_close_call",          # 对照诚实作废
  "vs_AN_open_leftover",                     # 对照声明：开盘集合剩单另页 AN（AO≠AN）
  "vs_M_auto_roll_aft",                      # 对照声明：剩单进盘后另页 M
  "vs_N_overnight_gtc",                      # 对照声明：隔夜假 GTC 另页 N
  "vs_AK_call_cont",                         # 对照声明：集合窗假连续另页 AK
  "vs_A_fill",                               # 对照声明：板上枯竭另页 A（AO≠A）
  "vs_O_block",                              # 对照声明：大宗另页 O（AO≠O）
  "vs_Y_call_volume",                        # 对照声明：集合量分母另页 Y
  "day_freq_proxy_only",                     # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AO0/AO1 相对 AO2）；  
2. 收盘集合剩单假即时成腿贡献差 ΔFakeLeftover；  
3. 废单/失败率差 ΔFail；  
4. （可选）收盘交接冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeLeftover 桶贡献| **≥ params.G** 或 |ΔNotional_(AO1?AO2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「收盘集合剩单交接执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AO 无关；风控补丁 2026-11-02）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AO） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 收盘集合剩单假即时成桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛（≠实验字母 AO） | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AO1?AO2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19` |
| fill_time | 成交时点 | **写死** `next_open` |
| ao0_primary_demo | 天真主报枚举 | **写死冻结** `invent_close_call_leftover_instant_fill`（禁双挂；风控补丁 2026-11-02） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组剩单须 expire_after_close_call；禁与 M/N/AN/AK/A/O/Y 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分收盘集合未成与收盘价成交腿，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把剩单进盘后（M）、隔夜假 GTC（N）、开盘集合剩单（AN）、集合窗假连续（AK）、板上枯竭（A）、大宗（O）、集合量分母（Y）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「收盘集合剩单假即时成」写成「开盘集合剩单假即时成」而不声明另页 AN → 与 AN 撞题，设计失效。  
4. 把「收盘集合剩单假即时成」写成「剩单自动进盘后」为主病而不声明另页 M → 与 M 撞题，设计失效。  
5. 把「收盘集合剩单假即时成」写成「板上枯竭」或「大宗可补」而不声明另页 A/O → 与 A/O 撞题，设计失效。  
6. holdout 反调 `ao0_primary_demo` / Y·G·N·Y2 → 结论无效。  
7. 用复权价算收盘价或冲击 → 标签与执行双错，结论无效。  
8. 把实验字母 AO 与单字母 A 或单字母 O 或双字母 AN 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权 OHLC（含收盘价）、交易所、买卖方向、拟挂限价；  
- 收盘集合是否产生成交、集合后未成交数量/标记（或日频代理声明）；会话钟（Asia/Shanghai）；  
- 交易日历。

可选：L2/逐笔（精确复盘收盘集合清算后剩单是否作废）；分钟 bar（若做敏感性，须声明与 AA 分列）；盘后成交标记（仅 AO1 对照声明用，不重开 M）。

**禁止**：用核对日现行规则铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 M 的「剩单进盘后」或 N 的「隔夜假 GTC」或 AN 的「开盘集合剩单」或 AK 的「集合窗假连续」或 A 的「板上枯竭」或 O 的「大宗」或 Y 的「集合量分母」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AO`  
- **组**：AO0 / AO1 / AO2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-19`；`close_call_leftover_honest=expire_after_close_call`；`close_call_leftover_instant_fill_honest=False`；`close_call_leftover_to_aft_honest=False`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_close_call_leftover`；`missing_close_call_leftover_policy=skip`；`day_freq_proxy=close_call_leftover_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AO；**params.N≠实验字母 AO**；禁 null/holdout；风控补丁 2026-11-02）；**`params.ao0_primary_demo` 写死冻结 `invent_close_call_leftover_instant_fill`**（禁与 invent_close_call_leftover_as_aft 双挂；风控补丁 2026-11-02）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AO0/AO1/AO2 可成交名义/路径质量、ΔFakeLeftover、ΔFail；分桶（假即时成 / 假进盘后 / vs AN·M·N·AK·A·O·Y）。  
- 自检布尔：AO2 是否 expire_after_close_call；AO0 是否单一主报；AO1 是否仅假进盘后；是否未与 M/N/AN/AK/A/O/Y 混主结论；holdout 是否未反调；**是否未把实验字母 AO 与 A 或 O 或 AN 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AN 冻结补丁正文**；**是否未改假设-H / 假设-N / 假设-M / 假设-AN / 假设-AK / 假设-O / 假设-A**。  
- **禁止输出**：具体买卖标的列表当「建议」；把收盘集合剩单假即时成当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AN 及其他 A/D–AN 已交正文**；**不改假设-H**；**不改假设-N**；**不改假设-M**；**不改假设-AN**；**不改假设-AK**；**不改假设-O**；**不改假设-A**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：申报当日有效；不能一次全部成交的，未成交部分继续参加当日竞价；收盘集合之后当日竞价结束 → 未成交失效；竞价剩下的限价单不会自动变成盘后单；不隔夜。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AN，本页**新增实验 AO** 收成标准件，**不改口径主线**，**不改假设 A–AN 正文**。与实验 AN/M/N/AK/A/O/Y 分工：**AN=开盘集合剩单假即时成；M=盘后通道+剩单进盘后；N=收盘切日+隔夜假 GTC；AK=集合窗假连续；A=板上枯竭；O=大宗；Y=集合量分母；AO=收盘集合剩单假即时成（AO≠A≠O≠AN）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；收盘集合未成标记或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**close_call_leftover_honest=expire_after_close_call 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 AO；params.N≠实验字母 AO；风控补丁 2026-11-02）**；**ao0_primary_demo 写死冻结 invent_close_call_leftover_instant_fill（禁双挂；风控补丁 2026-11-02）** |

---

## 已冻结键（风控补丁 2026-11-02；已写死待复检）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AO**；**`params.N` ≠ 实验字母 AO**；禁 null / holdout 标定。  
2. **`params.ao0_primary_demo`**：**写死冻结** **`invent_close_call_leftover_instant_fill`**；禁与 **`invent_close_call_leftover_as_aft`** 双挂争主表。

---

## 变更

- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AO-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` **写死冻结**（**params.Y≠实验字母 AO**；**params.N≠实验字母 AO**；禁 null/holdout）；② `params.ao0_primary_demo=invent_close_call_leftover_instant_fill` **写死冻结**（禁与 `invent_close_call_leftover_as_aft` 双挂）。**已写死待复检**。**不改 Y/Z/AA–AN 冻结补丁**；**不改假设-H**；**不改假设-N**；**不改假设-M**；**不改假设-AN**；**不改假设-AK**；**不改假设-O**；**不改假设-A**；不开回测；不抢 A；禁实盘。
- 2026-11-02：新建标准件（总管线：AN 补丁已交后写下一纸面 AO；Y/Z/AA–AN 补丁已交不改；清单止于 AN → 自 `事实与坑`「申报当日有效 / 竞价剩单不自动进盘后」选题，**与 A/H/X/E/M/O/AC–AN/R/Q/I/F/L/J/G/D/N/Y/AA/K 不撞主结论**；**明确双字母 AO ≠ 单字母 A ≠ 单字母 O ≠ 双字母 AN**；**明确 params.Y ≠ 实验字母 AO；params.N ≠ 实验字母 AO**；近邻 AN=开盘集合剩单、M=剩单进盘后、N=隔夜假 GTC、AK=集合窗假连续、A=板上、O=大宗、Y=集合量，本页主测收盘集合剩单假即时成；**实验字母 AO ≠ params.Y ≠ params.N ≠ 实验字母 A ≠ 实验字母 O ≠ 实验字母 AN**；机制类预埋 fail_policy/oos/红线豁免/params 键；**待预检两条**见上；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA–AN/A/D–AN 正文**；**不改假设-H**；**不改假设-N**；**不改假设-M**；**不改假设-AN**；**不改假设-AK**；**不改假设-O**；**不改假设-A**）。
