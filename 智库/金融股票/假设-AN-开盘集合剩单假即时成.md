# 假设 AN · 开盘集合剩单假即时成（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AM 补丁已交后写下一纸面 AN；清单原止于 AM，无 AN 节 → 自立实验 AN；选题自 `事实与坑`「申报当日有效：不能一次全部成交的，未成交部分继续参加当日竞价；当前竞价阶段未成交的买卖申报，自动进入当日后续竞价阶段（上交所 3.3.18 / 3.4.2；深交所 2026 年修订 3.3.21 同向）。核对日锚 2026-10-19」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交 / 竞价剩单自动进盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AJ（临停复牌假连续）/ AK（集合竞价时段假连续）/ AL（午休与开盘空窗假连续）/ AM（停牌期间假连续）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价通道）/ G（无板日误套板块默认板）/ J（无板日临停触发）/ D（成交时点与停牌）/ N（收盘机制与假 GTC）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区误标）**分列**；**新建实验 AN**  
状态：**草稿 · 待数据 · 待跑 · 待预检（2026-11-02）**（结论栏空；禁止把「开盘集合未成交部分按开盘价即时全成 / 假清空」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AM 及其他 A/D–AM 已交正文与冻结补丁；不改假设-H；不改假设-N；不改假设-M；不改假设-AK；不改假设-AL；不改假设-Y**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AM，本页自立实验 AN 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **开盘集合撮合后未成交部分**是否被发明成按开盘价即时全成或不转入 9:30 起连续竞价。双字母 **AN ≠ 单字母 A**。与假设 **N（收盘机制与假 GTC）** **硬分列**：N = 收盘价产生方式误套 + **隔夜**假 GTC；本页 = **当日**开盘集合→连续的剩单交接，**不**主测隔夜有效、**不**主测收盘切日。双字母 **AN ≠ 单字母 N**。与假设 **M（盘后补成交）** **分列**：M = 竞价剩单**自动进盘后 15:05**；本页 = 开盘集合剩单在**当日竞价会话内**假即时成/假不转入连续，**不**开盘后通道。与假设 **AK（集合时段假连续）** **分列**：AK = 集合**窗内**改成连续多价撮合；本页 = 集合**清算后**剩单命运（即时成 / 不转入），不重开窗内撮合方式。与假设 **AL（空窗假连续）** **分列**：AL = 9:25–9:30 / 午休空窗发明成交；本页 = 剩单是否按规则进入 9:30 连续簿，不主测空窗钟点假成交。与假设 **Y（集合量分母）** **分列**：Y = 集合成交量是否计入日线分母；本页 = 剩单执行路径，不重开量口径。与假设 A/H/X/E/M/O/R/Q/AC–AM/I/F/L/G/J/N/Y/AA/D/K **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AN** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AN / 假设-AN / hypothesis_id=AN / 组 AN0·AN1·AN2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AN 混读或互改。亦**禁止**把实验字母 AN 与单字母实验 **A**、单字母实验 **N**、或 params 键名 `an0_*` 以外的实验页混读。**双字母 AN ≠ 单字母 A ≠ 单字母 N**；**params.N ≠ 实验字母 AN**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，在**开盘集合竞价清算后**，把未成交部分当成按**开盘价即时全成**（或假清空/作废而不转入连续），相对「未成交部分继续参加当日后续竞价；开盘集合未成交申报自动进入 9:30 起连续竞价排队；**不**按开盘价即时发明全成、**不**隔夜、**不**自动进盘后」的 PIT 诚实组，会**系统性发明开盘集合剩单假即时成（或不转入）路径并高估可成交名义 / 错价冲击**；差异应**集中在开盘集合剩单假即时成 / 假不转入连续桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的剩单假即时成贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在开盘集合剩单交接相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 开盘集合剩单假即时成 ≠ 集合窗假连续；≠ 空窗假连续；≠ 隔夜假 GTC；≠ 剩单进盘后；≠ 板上枯竭

```
# 配置写死键（见 §7；待预检两条见文末）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AN；≠ 实验字母 A；≠ 实验字母 N
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AN
# params.asof_check_date                 写死默认 2026-10-19  # 事实与坑「申报当日有效 / 未成交进当日后续竞价」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；开盘集合剩单交接作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.open_call_start                 写死 09:15
# params.open_call_end                   写死 09:25
# params.continuous_am_start             写死 09:30
# params.call_leftover_honest            写死 transfer_to_continuous  # 诚实：未成交自动进入当日后续连续竞价
# params.call_leftover_instant_fill_honest 写死 False
# params.call_leftover_vanish_honest     写死 False
# params.an0_primary_demo                待预检（建议 invent_call_leftover_instant_fill）；禁与 invent_call_leftover_vanish 双挂
# params.an0_invent_instant_fill         写死 True           # 天真主路径（随 primary_demo）
# params.an1_vanish_only                 写死 True           # 半泄露：仅假清空/不转入；不发明按开盘价即时全成
# params.an2_leftover_policy             写死 transfer_to_continuous
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AN≠A）
# params.merge_with_N_close_gtc          写死 False          # 收盘切日/隔夜假 GTC 另页 N（AN≠N）
# params.merge_with_M_aft                写死 False          # 剩单进盘后另页 M
# params.merge_with_AK_call_cont         写死 False          # 集合窗假连续另页 AK
# params.merge_with_AL_session_gap       写死 False          # 空窗假连续另页 AL
# params.merge_with_Y_call_volume        写死 False          # 集合量分母另页 Y
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AM_halt              写死 False
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
# params.merge_with_J_halt               写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.universe_rule                   写死 sse_szse_common_stock_open_call_leftover
# params.missing_call_leftover_policy    写死 skip           # 缺开盘集合/未成标记 → skip（禁静默当即时全成）
# params.day_freq_proxy                  写死 open_call_leftover_sensitivity  # 日频无 L2 时只报敏感性档；禁假装精确复盘簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  待预检（建议 0.02/0.01/0.05/0.015）；params.Y≠实验字母 AN；params.N≠实验字母 AN；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-19"
px_basis = "unadj"
tick = 0.01
open_call_start = "09:15"
open_call_end = "09:25"
continuous_am_start = "09:30"
call_leftover_honest = "transfer_to_continuous"
call_leftover_instant_fill_honest = False
call_leftover_vanish_honest = False
an0_primary_demo = "invent_call_leftover_instant_fill"  # 待预检建议值；禁双挂
an0_invent_instant_fill = True
an1_vanish_only = True
an2_leftover_policy = "transfer_to_continuous"
universe_rule = "sse_szse_common_stock_open_call_leftover"
missing_call_leftover_policy = "skip"
day_freq_proxy = "open_call_leftover_sensitivity"

# 拉数前待冻结（预检建议）；禁 holdout / 事后改口 / 禁跑后改 an0_primary_demo
Y = 0.02   # 待预检建议；相对门槛 ≠ 实验字母 AN
G = 0.01
N = 0.05   # 待预检建议；失败率门槛键 params.N ≠ 实验字母 AN
Y2 = 0.015

def after_open_call_clearing(ts):
    """集合清算完成后、连续开始前的交接点（逻辑点，不等于空窗假成交）。"""
    return open_call_end <= ts < continuous_am_start

def leftover_policy(group, has_open_call_unfilled):
    """
    AN0：按 an0_primary_demo 单一主报（建议 invent_call_leftover_instant_fill）
    AN1：仅假清空/不转入（vanish），不发明按开盘价即时全成
    AN2：transfer_to_continuous
    """
    if not has_open_call_unfilled:
        return "no_leftover"
    if group == "AN0" and an0_primary_demo == "invent_call_leftover_instant_fill":
        if an0_invent_instant_fill:
            return "invent_instant_fill_at_open"
    if group == "AN1" and an1_vanish_only:
        return "invent_vanish_no_transfer"
    return "honest_transfer_to_continuous"
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺开盘集合未成标记/会话钟却硬判剩单即时全成、把 M 剩单进盘后 / N 隔夜假 GTC / AK 集合窗假连续 / AL 空窗假连续 / A 板上 / Y 集合量分母混进本页主表、日频无代理声明却假装 L2 复盘开盘簿、诚实组剩单仍按开盘价即时全成或假清空 → **跳过该日该券该腿**，不静默记假即时成。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AN）

| 组 | 开盘集合剩单 | 说明 |
|----|--------------|------|
| AN0 天真 | 剩单假即时成（按 `an0_primary_demo` 单一主报） | 发明按开盘价即时全成路径 |
| AN1 半泄露/混口径 | 仅假清空/不转入；不发明即时全成 | 混口径假路径 |
| AN2 PIT 诚实 | `transfer_to_continuous`；不即时全成、不假清空 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测开盘集合清算后未成交部分的命运**，不主测集合窗内撮合方式（见 AK）、不主测空窗钟点假成交（见 AL）、不主测隔夜假 GTC / 收盘切日（见 N）、不主测剩单进盘后（见 M）、不主测板上枯竭（见 A）、不主测集合量分母（见 Y）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/N/M/AK/AL/Y/AH/AI/AJ/AM/AG/I/F/L/H/X/E/O/R/Q/AC/AD/AE/AF/G/J/D/K/AA）**。

**待预检两条（拉数前不补则打回；建议值如下；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 建议；可成交名义/冲击差显著门槛；≠实验字母 AN
params.G                            = 0.01                      # 建议；开盘集合剩单假即时成桶相对对照差
params.N                            = 0.05                      # 建议；失败/废单率差门槛；≠实验字母 AN
params.Y2                           = 0.015                     # 建议；AN1（假清空）相对 AN2 专项门槛
params.an0_primary_demo             = invent_call_leftover_instant_fill  # 建议主报；禁与 invent_call_leftover_vanish 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_open_call_leftover`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺开盘集合/未成标记；把 M/N/AK/AL/A/Y 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：申报有效期与阶段交接按成交日当时交易规则文本；**禁止**用核对日规则铺满；隔夜有效交 N、盘后交 M，本页只测开盘集合→连续的剩单交接。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `an0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AN0 ? AN2**：开盘集合剩单假即时成相对诚实转入连续——假路径 / 可成交名义吹胖。  
2. **AN1 ? AN2**：仅假清空/不转入相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_call_leftover_instant_fill",  # 开盘集合剩单假即时成（主病）
  "invent_call_leftover_vanish",        # 假清空/不转入（AN1）
  "honest_transfer_to_continuous",      # 对照诚实转入连续
  "vs_M_auto_roll_aft",                 # 对照声明：剩单进盘后另页 M
  "vs_N_overnight_gtc",                 # 对照声明：隔夜假 GTC 另页 N（AN≠N）
  "vs_AK_call_cont",                    # 对照声明：集合窗假连续另页 AK
  "vs_AL_session_gap",                  # 对照声明：空窗假连续另页 AL
  "vs_A_fill",                          # 对照声明：板上枯竭另页 A（AN≠A）
  "vs_Y_call_volume",                   # 对照声明：集合量分母另页 Y
  "day_freq_proxy_only",                # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AN0/AN1 相对 AN2）；  
2. 开盘集合剩单假即时成腿贡献差 ΔFakeLeftover；  
3. 废单/失败率差 ΔFail；  
4. （可选）开盘交接冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeLeftover 桶贡献| **≥ params.G** 或 |ΔNotional_(AN1?AN2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「开盘集合剩单交接执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AN 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AN） | **待预检建议** `0.02` |
| params.G | 开盘集合剩单假即时成桶相对对照差 | **待预检建议** `0.01` |
| params.N | 失败/废单率差门槛（≠实验字母 AN） | **待预检建议** `0.05` |
| params.Y2 | AN1?AN2 专项门槛 | **待预检建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19` |
| fill_time | 成交时点 | **写死** `next_open` |
| an0_primary_demo | 天真主报枚举 | **待预检建议** `invent_call_leftover_instant_fill`（禁双挂） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组剩单须 transfer_to_continuous；禁与 M/N/AK/AL/A/Y 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分开盘集合未成与连续首笔，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把剩单进盘后（M）、隔夜假 GTC（N）、集合窗假连续（AK）、空窗假连续（AL）、板上枯竭（A）、集合量分母（Y）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「开盘集合剩单假即时成」写成「隔夜仍在簿」而不声明另页 N → 与 N 撞题，设计失效。  
4. 把「开盘集合剩单假即时成」写成「剩单自动进盘后」而不声明另页 M → 与 M 撞题，设计失效。  
5. holdout 反调 `an0_primary_demo` / Y·G·N·Y2 → 结论无效。  
6. 用复权价算开盘价或冲击 → 标签与执行双错，结论无效。  
7. 把实验字母 AN 与单字母 A 或单字母 N 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权 OHLC（含开盘价）、交易所、买卖方向、拟挂限价；  
- 开盘集合是否产生成交、集合后未成交数量/标记（或日频代理声明）；会话钟（Asia/Shanghai）；  
- 交易日历。

可选：L2/逐笔（精确复盘开盘集合清算后剩单是否转入连续）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日现行规则铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 M 的「剩单进盘后」或 N 的「隔夜假 GTC」或 AK 的「集合窗假连续」或 AL 的「空窗假连续」或 A 的「板上枯竭」或 Y 的「集合量分母」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AN`  
- **组**：AN0 / AN1 / AN2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-19`；`call_leftover_honest=transfer_to_continuous`；`call_leftover_instant_fill_honest=False`；`call_leftover_vanish_honest=False`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_open_call_leftover`；`missing_call_leftover_policy=skip`；`day_freq_proxy=open_call_leftover_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 待预检建议 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AN；**params.N≠实验字母 AN**；禁 null/holdout）；**`params.an0_primary_demo` 待预检建议 `invent_call_leftover_instant_fill`**（禁与 invent_call_leftover_vanish 双挂）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AN0/AN1/AN2 可成交名义/路径质量、ΔFakeLeftover、ΔFail；分桶（假即时成 / 假清空 / vs M·N·AK·AL·A·Y）。  
- 自检布尔：AN2 是否 transfer_to_continuous；AN0 是否单一主报；AN1 是否仅假清空；是否未与 M/N/AK/AL/A/Y 混主结论；holdout 是否未反调；**是否未把实验字母 AN 与 A 或 N 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AM 冻结补丁正文**；**是否未改假设-H / 假设-N / 假设-M / 假设-AK / 假设-AL / 假设-Y**。  
- **禁止输出**：具体买卖标的列表当「建议」；把开盘集合剩单假即时成当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AM 及其他 A/D–AM 已交正文**；**不改假设-H**；**不改假设-N**；**不改假设-M**；**不改假设-AK**；**不改假设-AL**；**不改假设-Y**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：申报当日有效；不能一次全部成交的，未成交部分继续参加当日竞价；当前竞价阶段未成交申报自动进入当日后续竞价阶段；不隔夜、不自动进盘后。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AM，本页**新增实验 AN** 收成标准件，**不改口径主线**，**不改假设 A–AM 正文**。与实验 M/N/AK/AL/A/Y 分工：**M=剩单进盘后；N=收盘切日+隔夜假 GTC；AK=集合窗假连续；AL=空窗假连续；A=板上枯竭；Y=集合量分母；AN=开盘集合剩单假即时成/不转入连续（AN≠A≠N）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；开盘集合未成标记或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**call_leftover_honest=transfer_to_continuous 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 待预检建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AN；params.N≠实验字母 AN）**；**an0_primary_demo 待预检建议 invent_call_leftover_instant_fill（禁双挂）** |

---

## 待预检键（拉数前不补则打回）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：键名稳；建议值 `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AN**；**`params.N` ≠ 实验字母 AN**；须写死冻结；禁 null / holdout 标定。  
2. **`params.an0_primary_demo`**：待预检；建议 **`invent_call_leftover_instant_fill`**；禁与 **`invent_call_leftover_vanish`** 双挂争主表。

---

## 变更

- 2026-11-02：新建标准件（总管线：AM 补丁已交后写下一纸面 AN；Y/Z/AA–AM 补丁已交不改；清单止于 AM → 自 `事实与坑`「申报当日有效 / 未成交进当日后续竞价」选题，**与 A/H/X/E/M/O/AC–AM/R/Q/I/F/L/J/G/D/N/Y/AA/K 不撞主结论**；**明确双字母 AN ≠ 单字母 A ≠ 单字母 N**；**明确 params.N ≠ 实验字母 AN**；近邻 M=剩单进盘后、N=隔夜假 GTC、AK=集合窗假连续、AL=空窗假连续、A=板上、Y=集合量，本页主测开盘集合剩单假即时成/不转入；**实验字母 AN ≠ params.Y ≠ params.N ≠ 实验字母 A ≠ 实验字母 N**；机制类预埋 fail_policy/oos/红线豁免/params 键；**待预检两条**见上；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA–AM/A/D–AM 正文**；**不改假设-H**；**不改假设-N**；**不改假设-M**；**不改假设-AK**；**不改假设-AL**；**不改假设-Y**）。
