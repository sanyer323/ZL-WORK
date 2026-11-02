# 假设 AR · 板上排队假队首（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AQ 补丁已交后写下一纸面 AR；清单原止于 AQ，无 AR 节 → 自立实验 AR；选题自 `事实与坑`「涨停时卖方枯竭，买单排队不成交通常发生；回测用收盘价一律成交，等于假设你永远排在队头。现行撮合：价格优先、时间优先」+ 口径「执行鸿沟」；与假设 A（板上可成交/枯竭能否按板上价成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ N（收盘机制与假 GTC）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AJ（临停复牌假连续）/ AK（集合竞价时段假连续）/ AL（午休与开盘空窗假连续）/ AM（停牌期间假连续）/ AN（开盘集合剩单假即时成）/ AO（收盘集合剩单假即时成）/ AP（盘后错侧限价假有效）/ AQ（临停阶段误套连续笼子）/ I（价格笼子远限价）/ F（涨跌停价取整）/ L（市价通道）/ G（无板日误套板块默认板）/ J（无板日临停）/ D（成交时点与停牌）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区误标）/ P（指数点位停牌假成交权重）**分列**；**新建实验 AR**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「板上排队永远排在队头 / 可吃满对手剩余」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AQ 及其他 A/D–AQ 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-R；不改假设-AQ；勿再改 AQ**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AQ，本页自立实验 AR 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成（含一字开盘买记 0 等容量门槛）；本页 = 在**已承认板上存在有限对手剩余**的前提下，回测是否**发明信号腿永远排在队头**（或按申报量比例分配）而吃满该剩余。双字母 **AR ≠ 单字母 A**。与假设 **R（股票 ETF 假回转）** **硬分列**：R = 股票 ETF 回转交易规则误套；本页 = 普通 A 股**板上排队分配规则**，不主测 ETF。双字母 **AR ≠ 单字母 R**。与假设 AN–AQ **硬分列**：AN=开盘集合剩单假即时成；AO=收盘集合剩单假即时成；AP=盘后错侧限价假有效；AQ=临停阶段误套连续笼子；本页不重开集合剩单/盘后错侧/临停笼子，主测**连续竞价（及板上）排队位次诚实性**。与假设 E/AF/L **分列**：E=整手；AF=单笔上限；L=市价通道保护限价；本页不重开手数/上限/市价保护，主测**时间优先排队 vs 假队首/假比例**。与假设 A/H/X/E/M/O/R/Q/N/AC–AQ/I/F/L/G/J/D/Y/K/AA/P **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AR** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AR / 假设-AR / hypothesis_id=AR / 组 AR0·AR1·AR2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AR 混读或互改。亦**禁止**把实验字母 AR 与单字母实验 **A**、单字母实验 **R**、双字母实验 **AQ**、或 params 键名 `ar0_*` 以外的实验页混读。**双字母 AR ≠ 单字母 A ≠ 单字母 R ≠ 双字母 AQ**；**params.Y ≠ 实验字母 AR**；**params.N ≠ 实验字母 AR**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权板上价、同一 T+1 下，在**涨停（跌停）板上存在有限对手剩余可成交量**时，把本信号腿当成**永远排在队头**并吃满该剩余（或按申报量比例发明分配），相对「价格优先、时间优先；信号腿无队首特权，按到达时点排队；缺到达时点则 skip/敏感性档，禁止静默当队首」的 PIT 诚实组，会**系统性发明假队首（或假比例）成交路径并高估板上可成交名义**；差异应**集中在假队首 / 假比例分配桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假队首贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在排队位次相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 板上排队假队首 ≠ 板上枯竭门槛；≠ ETF 回转；≠ 集合剩单；≠ 盘后错侧；≠ 临停笼子；≠ 整手/单笔上限/市价保护

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AR；≠ 实验字母 A；≠ 实验字母 R
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AR
# params.asof_check_date                 写死默认 2026-10-19  # 事实与坑「价格优先、时间优先 / 排队≠队头」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；板上排队分配作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.queue_honest                    写死 time_priority   # 诚实：价格优先、时间优先；无队首特权
# params.board_capacity_handoff          写死 a_page          # 板上是否有对手剩余/枯竭门槛交 A，不重开 A 主测
# params.ar0_primary_demo                写死 invent_limit_queue_as_front  # 风控补丁冻结；主报：假队首吃满对手剩余；禁与 invent_limit_queue_as_pro_rata 双挂
# params.ar0_invent_queue_front          写死 True           # 天真主路径（随 primary_demo）
# params.ar1_pro_rata_only               写死 True           # 半泄露：仅按申报量比例分配（非队首特权）
# params.ar2_queue_policy                写死 time_priority
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AR≠A）
# params.merge_with_R_etf_rotation       写死 False          # ETF 回转另页 R（AR≠R）
# params.merge_with_AQ_halt_cage         写死 False          # 临停笼子另页 AQ
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_AL_session_gap       写死 False
# params.merge_with_AM_halt              写死 False
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_P_index_halt         写死 False
# params.universe_rule                   写死 sse_szse_common_stock_limit_queue_check
# params.missing_queue_policy            写死 skip           # 缺到达时点/对手剩余标记 → skip（禁静默当队首）
# params.day_freq_proxy                  写死 limit_queue_sensitivity  # 日频无 L2/到达时点时只报敏感性档；禁假装精确复盘队序
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AR；params.N≠实验字母 AR；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-19"
px_basis = "unadj"
tick = 0.01
queue_honest = "time_priority"
board_capacity_handoff = "a_page"
ar0_primary_demo = "invent_limit_queue_as_front"  # 风控补丁冻结；禁双挂
ar0_invent_queue_front = True
ar1_pro_rata_only = True
ar2_queue_policy = "time_priority"
universe_rule = "sse_szse_common_stock_limit_queue_check"
missing_queue_policy = "skip"
day_freq_proxy = "limit_queue_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 ar0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AR
G = 0.01
N = 0.05   # 风控补丁冻结；失败率门槛键 params.N ≠ 实验字母 AR
Y2 = 0.015

def board_opp_residual(side, limit_px, day_book_or_proxy):
    """板上对手剩余可成交量代理；枯竭门槛/是否允许按板上价记成交 A，本页只消费「有限剩余 >0」时的分配。"""
    return day_book_or_proxy.opp_residual(side, limit_px)

def queue_alloc(group, signal_qty, opp_residual, arrival_rank_or_none, declared_qty_share):
    """
    AR0：按 ar0_primary_demo 单一主报（写死 invent_limit_queue_as_front）
    AR1：仅按申报量比例分配（非队首特权）
    AR2：time_priority；无到达时点 → skip（或日频敏感性档）
    """
    if opp_residual <= 0:
        return 0  # 无剩余；枯竭路径交 A
    if group == "AR0" and ar0_primary_demo == "invent_limit_queue_as_front":
        if ar0_invent_queue_front:
            return min(signal_qty, opp_residual)  # 假队首
        return 0
    if group == "AR1" and ar1_pro_rata_only:
        share = max(0.0, min(1.0, declared_qty_share))
        return min(signal_qty, int(opp_residual * share))
    # AR2
    if arrival_rank_or_none is None:
        return "skip_or_day_freq_proxy"
    if arrival_rank_or_none == 0:
        return min(signal_qty, opp_residual)
    return 0  # 非队首：本页日频代理下记 0；有 L2 时可按真实队序部分成
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺到达时点/对手剩余标记却硬记队首全成、把 A 板上枯竭门槛 / R ETF 回转 / AN–AQ 集合剩单·盘后错侧·临停笼子 / E 整手 / AF 单笔上限 / L 市价保护混进本页主表、日频无代理声明却假装 L2 复盘队序、诚实组无到达时点仍当队首 → **跳过该日该券该腿**，不静默记假队首成。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AR）

| 组 | 板上排队分配 | 说明 |
|----|--------------|------|
| AR0 天真 | 假队首吃满对手剩余（按 `ar0_primary_demo` 单一主报） | 发明假队首路径 |
| AR1 半泄露/混口径 | 仅按申报量比例分配 | 混口径假路径 |
| AR2 PIT 诚实 | time_priority；无到达时点 skip/敏感性 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测板上有限对手剩余下的排队分配**，不主测板上枯竭门槛本身（见 A）、不主测 ETF 回转（见 R）、不主测集合剩单/盘后错侧/临停笼子（见 AN–AQ）、不主测整手/单笔上限/市价保护（见 E/AF/L）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/R/AQ/AN/AO/AP/AK/AL/AM/AJ/AH/AI/AG/AF/E/L/I/F/H/X/M/O/Q/AC/AD/AE/G/J/D/N/Y/K/AA/P）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 写死冻结；可成交名义/冲击差显著门槛；≠实验字母 AR
params.G                            = 0.01                      # 写死冻结；假队首桶相对对照差
params.N                            = 0.05                      # 写死冻结；失败/废单率差门槛；≠实验字母 AR
params.Y2                           = 0.015                     # 写死冻结；AR1（假比例）相对 AR2 专项门槛
params.ar0_primary_demo             = invent_limit_queue_as_front  # 写死冻结主报：假队首；禁与 invent_limit_queue_as_pro_rata 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_limit_queue_check`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺对手剩余/到达时点且未声明日频代理；把 A/R/AN–AQ/E/AF/L 主结论并进本页主表；日频无代理声明却假装 L2 复盘队序。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：排队规则按成交日当时交易规则文本（价格优先、时间优先）；**板上枯竭门槛交 A**；**禁止**用核对日「永远队首」铺满。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ar0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AR0 − AR2**：假队首吃满相对诚实 time_priority——假队首 / 可成交名义高估。  
2. **AR1 − AR2**：仅假比例分配相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_limit_queue_as_front",         # 假队首吃满对手剩余（主病）
  "invent_limit_queue_as_pro_rata",      # 假比例分配（AR1）
  "honest_time_priority",                # 对照诚实时间优先
  "vs_A_fill",                           # 对照声明：板上枯竭另页 A（AR≠A）
  "vs_R_etf_rotation",                   # 对照声明：ETF 回转另页 R（AR≠R）
  "vs_AQ_halt_cage",                     # 对照声明：临停笼子另页 AQ
  "vs_AN_open_leftover",                 # 对照声明：开盘集合剩单另页 AN
  "vs_AO_close_leftover",                # 对照声明：收盘集合剩单另页 AO
  "vs_AP_aft_side",                      # 对照声明：盘后错侧另页 AP
  "vs_E_lot",                            # 对照声明：整手另页 E
  "vs_AF_qty_cap",                       # 对照声明：单笔上限另页 AF
  "vs_L_mkt",                            # 对照声明：市价通道另页 L
  "day_freq_proxy_only",                 # 日频敏感性档（无 L2/到达时点）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AR0/AR1 相对 AR2）；  
2. 假队首腿贡献差 ΔFakeQueueFront；  
3. 废单/失败率差 ΔFail；  
4. （可选）冲击差 ΔImpact（声明为代理，不冒充 L2 队序）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeQueueFront 桶贡献| **≥ params.G** 或 |ΔNotional_(AR1−AR2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「板上排队位次执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AR 无关；风控补丁 2026-11-02）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AR） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 假队首桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛（≠实验字母 AR） | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AR1−AR2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19` |
| fill_time | 成交时点 | **写死** `next_open` |
| ar0_primary_demo | 天真主报枚举 | **写死冻结** `invent_limit_queue_as_front`（禁双挂；风控补丁 2026-11-02） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 time_priority；禁与 A/R/AN–AQ/E/AF/L 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分「有限对手剩余」日与「全枯竭」日，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把板上枯竭门槛（A）、ETF 回转（R）、集合剩单（AN/AO）、盘后错侧（AP）、临停笼子（AQ）、整手（E）、单笔上限（AF）、市价保护（L）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「假队首」写成「板上能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
4. 把「假队首」写成「ETF 回转」而不声明另页 R → 与 R 撞题，设计失效。  
5. 把「假队首」写成「开盘/收盘集合剩单假即时成」或「盘后错侧」或「临停误套连续笼子」而不声明另页 AN–AQ → 与 AN–AQ 撞题，设计失效。  
6. holdout 反调 `ar0_primary_demo` / Y·G·N·Y2 → 结论无效。  
7. 用复权价算板上价或冲击 → 标签与执行双错，结论无效。  
8. 把实验字母 AR 与单字母 A 或单字母 R 或双字母 AQ 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权板上价/OHLC、买卖方向、交易所、板块；  
- 板上对手剩余可成交量代理（或显式消费 A 的 capacity 标记，不重开 A 主测）；  
- 订单到达时点/队序代理（有则精确；无则日频 `limit_queue_sensitivity`）；  
- 交易日历。

可选：逐笔/盘口（精确复盘队序）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日「永远队首」铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 A 的「板上枯竭」或 R 的「ETF 回转」或 AN–AQ 的集合剩单/盘后错侧/临停笼子或 E/AF/L 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AR`  
- **组**：AR0 / AR1 / AR2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-19`；`queue_honest=time_priority`；`board_capacity_handoff=a_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_limit_queue_check`；`missing_queue_policy=skip`；`day_freq_proxy=limit_queue_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AR；**params.N≠实验字母 AR**；禁 null/holdout；风控补丁 2026-11-02）；**`params.ar0_primary_demo` 写死冻结 `invent_limit_queue_as_front`**（禁与 invent_limit_queue_as_pro_rata 双挂；风控补丁 2026-11-02）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AR0/AR1/AR2 可成交名义/路径质量、ΔFakeQueueFront、ΔFail；分桶（假队首 / 假比例 / vs A·R·AQ·AN·AO·AP·E·AF·L）。  
- 自检布尔：AR2 是否 time_priority；AR0 是否单一主报；AR1 是否仅假比例；是否未与 A/R/AN–AQ/E/AF/L 混主结论；holdout 是否未反调；**是否未把实验字母 AR 与 A 或 R 或 AQ 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AQ 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-R / 假设-AQ**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假队首当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AQ 及其他 A/D–AQ 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-R**；**不改假设-AQ**；**勿再改 AQ**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：涨停排队成交率不是 100%；回测一律收盘成交等于假设永远排在队头；现行撮合价格优先、时间优先。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AQ，本页**新增实验 AR** 收成标准件，**不改口径主线**，**不改假设 A–AQ 正文**。与实验 A/R/AN–AQ 分工：**A=板上枯竭门槛；R=ETF 回转；AN–AQ=集合剩单/盘后错侧/临停笼子；AR=板上排队假队首（AR≠A≠R≠AQ≠AN≠AO≠AP）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；对手剩余+到达时点或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**queue_honest=time_priority 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 AR；params.N≠实验字母 AR；风控补丁 2026-11-02）**；**ar0_primary_demo 写死冻结 invent_limit_queue_as_front（禁双挂；风控补丁 2026-11-02）** |

---

## 已冻结键（风控补丁 2026-11-02；已写死待复检）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AR**；**`params.N` ≠ 实验字母 AR**；禁 null / holdout 标定。  
2. **`params.ar0_primary_demo`**：**写死冻结** **`invent_limit_queue_as_front`**；禁与 **`invent_limit_queue_as_pro_rata`** 双挂争主表。

---

## 变更

- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AR-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` **写死冻结**（**params.Y≠实验字母 AR**；**params.N≠实验字母 AR**；禁 null/holdout）；② `params.ar0_primary_demo=invent_limit_queue_as_front` **写死冻结**（禁与 `invent_limit_queue_as_pro_rata` 双挂）。**已写死待复检**。**不改 Y/Z/AA–AQ 冻结补丁**；**不改假设-H**；**不改假设-A**；**不改假设-R**；**不改假设-AQ**；**勿再改 AQ**；不开回测；不抢 A；禁实盘。
- 2026-11-02：新建标准件（总管线：AQ 补丁已交后写下一纸面 AR；Y/Z/AA–AQ 补丁已交不改；清单止于 AQ → 自 `事实与坑`「排队≠队头 / 价格优先时间优先」选题，**与 A/H/X/E/M/O/R/Q/N/AC–AQ 硬分列**；**双字母 AR ≠ 单字母 A ≠ 单字母 R**；**不与 AN–AQ 重复**；结论栏空；不开回测；不抢 A；**勿再改 AQ**）。
