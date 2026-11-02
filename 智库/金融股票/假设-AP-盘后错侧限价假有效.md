# 假设 AP · 盘后错侧限价假有效（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AO 补丁已交后写下一纸面 AP；清单原止于 AO，无 AP 节 → 自立实验 AP；选题自 `事实与坑`「盘后固定价格：买入限价低于收盘价、卖出限价高于收盘价 → 该笔无效；当日 15:00 仍停牌则不做盘后，已接受的收盘定价申报无效（上交所 3.7 / 深交所 3.6；核对日锚 2026-10-19）」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后通道 PIT / 竞价剩单自动进盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AJ（临停复牌假连续）/ AK（集合竞价时段假连续）/ AL（午休与开盘空窗假连续）/ AM（停牌期间假连续）/ AN（开盘集合剩单假即时成）/ AO（收盘集合剩单假即时成 / 假进盘后）/ I（价格笼子）/ F（涨跌停价取整）/ L（市价通道）/ G（无板日误套板块默认板）/ J（无板日临停触发）/ D（成交时点与停牌）/ N（收盘机制与假 GTC）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区误标）/ P（指数点位停牌假成交权重）**分列**；**新建实验 AP**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「错侧收盘定价申报仍按收盘价成交 / 停牌至 15:00 仍做盘后」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AO 及其他 A/D–AO 已交正文与冻结补丁；不改假设-H；不改假设-M；不改假设-AO；不改假设-O；不改假设-A；不改假设-P；不改假设-AE；不改假设-AM**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AO，本页自立实验 AP 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **盘后固定价格通道内**错侧限价（买低于收盘 / 卖高于收盘）是否被发明成有效并可成。双字母 **AP ≠ 单字母 A**。与假设 **P（指数点位停牌假成交权重）** **硬分列**：P = 把指数点位当可交易组合、停牌按收盘/前收盘假成交进指数权重；本页 = **盘后收盘定价申报的侧向有效性**，不主测指数权重、不主测停牌进指数。双字母 **AP ≠ 单字母 P**。与假设 **M（盘后补成交）** **硬分列**：M = 盘后通道**是否按板块/切日可用** + 竞价剩单**自动进 15:05**；本页**默认通道已可用**（消费 M 的通道可用性，不重开），主测错侧限价是否仍被发明有效/成交，以及（半泄露）停牌至 15:00 是否仍发明盘后成。与假设 **AO（收盘集合剩单假即时成）** **分列**：AO = 收盘集合清算后剩单假按收盘价即时全成 / 假进盘后；本页 = **另下的收盘定价申报**在盘后窗的侧向有效性，不重开收盘集合剩单命运。与假设 **O（大宗）** **分列**：O = 大宗/盘后定价大宗通道；本页 = 盘后**固定价格**通道内错侧限价，**不**主测大宗门槛。与假设 **AE（普通股票假 T+0）** **分列**：AE = 当日回转；本页不改变 T+1。与假设 **AM（停牌期间假连续）** **分列**：AM = 停牌窗内假连续竞价；本页 AP1 仅诊断「停牌至 15:00 仍发明盘后」，不重开竞价窗。与假设 A/H/X/E/M/O/R/Q/AC–AO/I/F/L/G/J/N/Y/AA/D/K/P **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AP** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AP / 假设-AP / hypothesis_id=AP / 组 AP0·AP1·AP2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AP 混读或互改。亦**禁止**把实验字母 AP 与单字母实验 **A**、单字母实验 **P**、双字母实验 **AO**、或 params 键名 `ap0_*` 以外的实验页混读。**双字母 AP ≠ 单字母 A ≠ 单字母 P ≠ 双字母 AO**；**params.Y ≠ 实验字母 AP**；**params.N ≠ 实验字母 AP**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权收盘价、同一 T+1 下，在**盘后固定价格通道已可用**的前提下，把**买入限价低于收盘价**或**卖出限价高于收盘价**的收盘定价申报仍当成有效并按收盘价成交（或把停牌至 15:00 的证券仍发明盘后成交），相对「错侧限价 → 该笔无效；停牌至 15:00 → 当日不做盘后、已接受收盘定价申报无效」的 PIT 诚实组，会**系统性发明盘后错侧假有效（或停牌至收假盘后）路径并高估可成交名义 / 错价冲击**；差异应**集中在盘后错侧假有效 / 停牌至 15:00 假盘后桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的错侧假有效贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在盘后侧向有效性相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 盘后错侧限价假有效 ≠ 盘后通道落地；≠ 剩单自动进盘后；≠ 收盘集合剩单假进盘后；≠ 板上枯竭；≠ 大宗；≠ 指数停牌假成交

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AP；≠ 实验字母 A；≠ 实验字母 P
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AP
# params.asof_check_date                 写死默认 2026-10-19  # 事实与坑「盘后错侧无效 / 停牌至15:00不做盘后」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；盘后错侧有效性作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.aft_match_window                写死 15:05-15:30
# params.aft_match_px                    写死 day_close       # 盘后撮合价=当日收盘价
# params.aft_side_check_honest           写死 True            # 诚实：买限价>=收盘；卖限价<=收盘
# params.aft_halted_to_1500_honest       写死 no_aft          # 诚实：停牌至15:00不做盘后
# params.aft_channel_assumed_available   写死 True            # 本页默认通道已可用（消费 M；不重开通道切日）
# params.ap0_primary_demo                写死 invent_aft_wrong_side_fill  # 风控补丁冻结；主报：错侧限价假有效可成；禁与 invent_aft_halted_to_1500_fill 双挂
# params.ap0_invent_wrong_side_fill      写死 True           # 天真主路径（随 primary_demo）
# params.ap1_halted_to_1500_only         写死 True           # 半泄露：仅停牌至15:00假盘后；侧向检查可诚实（对照交 AM/M）
# params.ap2_side_policy                 写死 reject_wrong_side_and_no_aft_if_halted_1500
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AP≠A）
# params.merge_with_P_index_halt         写死 False          # 指数停牌假成交另页 P（AP≠P）
# params.merge_with_M_aft_channel        写死 False          # 盘后通道落地/剩单进盘后另页 M
# params.merge_with_AO_close_leftover    写死 False          # 收盘集合剩单另页 AO
# params.merge_with_O_block              写死 False          # 大宗另页 O
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_AM_halt              写死 False          # 停牌窗假连续另页 AM
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_AL_session_gap       写死 False
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
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.universe_rule                   写死 sse_szse_common_stock_aft_side_check
# params.missing_aft_side_policy         写死 skip           # 缺收盘价/拟挂限价/停牌至15:00标记 → skip（禁静默当错侧可成）
# params.day_freq_proxy                  写死 aft_side_sensitivity  # 日频无 L2 时只报敏感性档；禁假装精确复盘盘后簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AP；params.N≠实验字母 AP；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-19"
px_basis = "unadj"
tick = 0.01
aft_match_window = "15:05-15:30"
aft_match_px = "day_close"
aft_side_check_honest = True
aft_halted_to_1500_honest = "no_aft"
aft_channel_assumed_available = True
ap0_primary_demo = "invent_aft_wrong_side_fill"  # 风控补丁冻结；禁双挂
ap0_invent_wrong_side_fill = True
ap1_halted_to_1500_only = True
ap2_side_policy = "reject_wrong_side_and_no_aft_if_halted_1500"
universe_rule = "sse_szse_common_stock_aft_side_check"
missing_aft_side_policy = "skip"
day_freq_proxy = "aft_side_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 ap0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AP
G = 0.01
N = 0.05   # 风控补丁冻结；失败率门槛键 params.N ≠ 实验字母 AP
Y2 = 0.015

def is_wrong_side_aft(side, limit_px, close_px):
    """买：limit 低于 close → 错侧；卖：limit 高于 close → 错侧。"""
    if side == "buy":
        return limit_px < close_px
    if side == "sell":
        return limit_px > close_px
    return True

def aft_side_policy(group, side, limit_px, close_px, halted_to_1500):
    """
    AP0：按 ap0_primary_demo 单一主报（写死 invent_aft_wrong_side_fill）
    AP1：仅停牌至15:00假盘后；侧向可按诚实拒错侧（对照交 AM/M）
    AP2：拒错侧 + 停牌至15:00 no_aft
    """
    if not aft_channel_assumed_available:
        return "channel_unavailable_handoff_M"
    if group == "AP0" and ap0_primary_demo == "invent_aft_wrong_side_fill":
        if ap0_invent_wrong_side_fill and is_wrong_side_aft(side, limit_px, close_px):
            return "invent_wrong_side_fill_at_close"
        if halted_to_1500:
            return "invent_aft_despite_halt_1500_optional"  # 不争主表；主病仍是错侧
        return "side_ok_or_no_order"
    if group == "AP1" and ap1_halted_to_1500_only:
        if halted_to_1500:
            return "invent_aft_despite_halt_1500"
        if is_wrong_side_aft(side, limit_px, close_px):
            return "honest_reject_wrong_side"
        return "side_ok"
    # AP2
    if halted_to_1500:
        return "honest_no_aft"
    if is_wrong_side_aft(side, limit_px, close_px):
        return "honest_reject_wrong_side"
    return "honest_aft_eligible"
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺收盘价/拟挂限价/停牌至 15:00 标记却硬判错侧可成、把 M 通道落地 / AO 收盘集合剩单假进盘后 / A 板上 / O 大宗 / P 指数停牌假成交 / AE 假 T+0 / AM 停牌窗假连续混进本页主表、日频无代理声明却假装 L2 复盘盘后簿、诚实组错侧仍记成交或停牌至 15:00 仍做盘后 → **跳过该日该券该腿**，不静默记假盘后成。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AP）

| 组 | 盘后侧向 / 停牌至收 | 说明 |
|----|---------------------|------|
| AP0 天真 | 错侧限价假有效可成（按 `ap0_primary_demo` 单一主报） | 发明错侧按收盘价成交路径 |
| AP1 半泄露/混口径 | 仅停牌至 15:00 假盘后；错侧可诚实拒 | 混口径假路径；对照声明交 AM/M |
| AP2 PIT 诚实 | 拒错侧；停牌至 15:00 → no_aft | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测盘后固定价格通道内错侧限价有效性**（默认通道已可用），不主测通道按板块切日落地（见 M）、不主测收盘集合剩单假进盘后（见 AO）、不主测板上枯竭（见 A）、不主测大宗（见 O）、不主测指数停牌假成交（见 P）、不主测假 T+0（见 AE）、不主测停牌窗假连续竞价（见 AM）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/P/M/AO/O/AE/AM/AN/N/AK/AL/Y/AH/AI/AJ/AG/I/F/L/H/X/E/R/Q/AC/AD/AF/G/J/D/K/AA）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 写死冻结；可成交名义/冲击差显著门槛；≠实验字母 AP
params.G                            = 0.01                      # 写死冻结；盘后错侧假有效桶相对对照差
params.N                            = 0.05                      # 写死冻结；失败/废单率差门槛；≠实验字母 AP
params.Y2                           = 0.015                     # 写死冻结；AP1（停牌至15:00假盘后）相对 AP2 专项门槛
params.ap0_primary_demo             = invent_aft_wrong_side_fill  # 写死冻结主报：盘后错侧假有效；禁与 invent_aft_halted_to_1500_fill 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_aft_side_check`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺收盘价/拟挂限价/停牌至 15:00 标记；通道不可用却未声明 handoff M；把 M/AO/A/O/P/AE/AM 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：盘后侧向规则与停牌至收规则按成交日当时交易规则文本；**通道可用性切片交 M**，本页默认 `aft_channel_assumed_available=True` 或显式过滤到通道已可用日；**禁止**用核对日规则铺满。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ap0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AP0 − AP2**：盘后错侧假有效相对诚实拒侧——假路径 / 可成交名义吹胖。  
2. **AP1 − AP2**：仅停牌至 15:00 假盘后相对诚实——混口径假路径（对照声明交 AM/M）。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_aft_wrong_side_fill",          # 盘后错侧假有效（主病）
  "invent_aft_halted_to_1500_fill",      # 停牌至15:00假盘后（AP1；对照交 AM/M）
  "honest_reject_wrong_side",            # 对照诚实拒侧
  "honest_no_aft_halt_1500",             # 对照诚实停牌至收不做盘后
  "vs_M_aft_channel",                    # 对照声明：通道落地/剩单进盘后另页 M
  "vs_AO_close_leftover_as_aft",         # 对照声明：收盘集合剩单假进盘后另页 AO
  "vs_A_fill",                           # 对照声明：板上枯竭另页 A（AP≠A）
  "vs_P_index_halt",                     # 对照声明：指数停牌假成交另页 P（AP≠P）
  "vs_O_block",                          # 对照声明：大宗另页 O
  "vs_AE_stock_t0",                      # 对照声明：假 T+0 另页 AE
  "vs_AM_halt_cont",                     # 对照声明：停牌窗假连续另页 AM
  "day_freq_proxy_only",                 # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AP0/AP1 相对 AP2）；  
2. 盘后错侧假有效腿贡献差 ΔFakeWrongSide；  
3. 废单/失败率差 ΔFail；  
4. （可选）盘后冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeWrongSide 桶贡献| **≥ params.G** 或 |ΔNotional_(AP1−AP2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「盘后错侧/停牌至收执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AP 无关；风控补丁 2026-11-02）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AP） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 盘后错侧假有效桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛（≠实验字母 AP） | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AP1−AP2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19` |
| fill_time | 成交时点 | **写死** `next_open` |
| ap0_primary_demo | 天真主报枚举 | **写死冻结** `invent_aft_wrong_side_fill`（禁双挂；风控补丁 2026-11-02） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组错侧须拒、停牌至 15:00 须 no_aft；禁与 M/AO/A/O/P/AE/AM 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分错侧限价与侧向合格盘后腿，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把盘后通道落地/剩单进盘后（M）、收盘集合剩单假进盘后（AO）、板上枯竭（A）、大宗（O）、指数停牌假成交（P）、假 T+0（AE）、停牌窗假连续（AM）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「盘后错侧假有效」写成「盘后通道全历史可用」为主病而不声明另页 M → 与 M 撞题，设计失效。  
4. 把「盘后错侧假有效」写成「收盘集合剩单假进盘后」而不声明另页 AO → 与 AO 撞题，设计失效。  
5. 把「盘后错侧假有效」写成「板上枯竭」或「指数停牌假成交」而不声明另页 A/P → 与 A/P 撞题，设计失效。  
6. holdout 反调 `ap0_primary_demo` / Y·G·N·Y2 → 结论无效。  
7. 用复权价算收盘价或冲击 → 标签与执行双错，结论无效。  
8. 把实验字母 AP 与单字母 A 或单字母 P 或双字母 AO 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权收盘价/OHLC、交易所、买卖方向、拟挂盘后限价；  
- 盘后通道是否可用（或显式过滤到可用日；消费 M，不重开切日表）；  
- 是否停牌至 15:00（或公告/停牌钟）；会话钟（Asia/Shanghai）；  
- 交易日历。

可选：盘后成交明细/逐笔（精确复盘侧向拒单）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日现行规则铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 M 的「通道落地/剩单进盘后」或 AO 的「收盘集合剩单假进盘后」或 A 的「板上枯竭」或 P 的「指数停牌假成交」或 O 的「大宗」或 AE 的「假 T+0」或 AM 的「停牌窗假连续」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AP`  
- **组**：AP0 / AP1 / AP2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-19`；`aft_side_check_honest=True`；`aft_halted_to_1500_honest=no_aft`；`aft_channel_assumed_available=True`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_aft_side_check`；`missing_aft_side_policy=skip`；`day_freq_proxy=aft_side_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AP；**params.N≠实验字母 AP**；禁 null/holdout；风控补丁 2026-11-02）；**`params.ap0_primary_demo` 写死冻结 `invent_aft_wrong_side_fill`**（禁与 invent_aft_halted_to_1500_fill 双挂；风控补丁 2026-11-02）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AP0/AP1/AP2 可成交名义/路径质量、ΔFakeWrongSide、ΔFail；分桶（错侧假有效 / 停牌至收假盘后 / vs M·AO·A·P·O·AE·AM）。  
- 自检布尔：AP2 是否拒错侧且停牌至 15:00 no_aft；AP0 是否单一主报；AP1 是否仅停牌至收假盘后；是否未与 M/AO/A/O/P/AE/AM 混主结论；holdout 是否未反调；**是否未把实验字母 AP 与 A 或 P 或 AO 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AO 冻结补丁正文**；**是否未改假设-H / 假设-M / 假设-AO / 假设-O / 假设-A / 假设-P / 假设-AE / 假设-AM**。  
- **禁止输出**：具体买卖标的列表当「建议」；把盘后错侧假有效当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AO 及其他 A/D–AO 已交正文**；**不改假设-H**；**不改假设-M**；**不改假设-AO**；**不改假设-O**；**不改假设-A**；**不改假设-P**；**不改假设-AE**；**不改假设-AM**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：盘后固定价格按当日收盘价、时间优先撮合；买入限价低于收盘价、卖出限价高于收盘价 → 该笔无效；停牌至 15:00 不做盘后。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AO，本页**新增实验 AP** 收成标准件，**不改口径主线**，**不改假设 A–AO 正文**。与实验 M/AO/A/P/O/AE/AM 分工：**M=盘后通道落地+剩单进盘后；AO=收盘集合剩单假即时成/假进盘后；A=板上枯竭；P=指数停牌假成交权重；O=大宗；AE=假 T+0；AM=停牌窗假连续；AP=盘后错侧限价假有效（AP≠A≠P≠AO≠M）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；收盘价+拟挂限价+停牌至15:00标记或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**aft_side_check_honest=True 写死**；**aft_halted_to_1500_honest=no_aft 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 AP；params.N≠实验字母 AP；风控补丁 2026-11-02）**；**ap0_primary_demo 写死冻结 invent_aft_wrong_side_fill（禁双挂；风控补丁 2026-11-02）** |

---

## 已冻结键（风控补丁 2026-11-02；已写死待复检）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AP**；**`params.N` ≠ 实验字母 AP**；禁 null / holdout 标定。  
2. **`params.ap0_primary_demo`**：**写死冻结** **`invent_aft_wrong_side_fill`**；禁与 **`invent_aft_halted_to_1500_fill`** 双挂争主表。

---

## 变更

- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AP-20261102.md` 有条件通过补两条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` **写死冻结**（**params.Y≠实验字母 AP**；**params.N≠实验字母 AP**；禁 null/holdout）；② `params.ap0_primary_demo=invent_aft_wrong_side_fill` **写死冻结**（禁与 `invent_aft_halted_to_1500_fill` 双挂）。**已写死待复检**。**不改 Y/Z/AA–AO 冻结补丁**；**不改假设-H**；**不改假设-M**；**不改假设-AO**；**不改假设-O**；**不改假设-A**；**不改假设-P**；**不改假设-AE**；**不改假设-AM**；不开回测；不抢 A；禁实盘。
- 2026-11-02：新建标准件（总管线：AO 补丁已交后写下一纸面 AP；Y/Z/AA–AO 补丁已交不改；清单止于 AO → 自 `事实与坑`「盘后错侧无效 / 停牌至15:00不做盘后」选题，**与 A/H/X/E/M/O/AC–AO/R/Q/I/F/L/J/G/D/N/Y/AA/K/P 不撞主结论**；**明确双字母 AP ≠ 单字母 A ≠ 单字母 P ≠ 双字母 AO**；**明确 params.Y ≠ 实验字母 AP；params.N ≠ 实验字母 AP**；近邻 M=通道落地/剩单进盘后、AO=收盘集合剩单、A=板上、P=指数停牌假成交、O=大宗、AE=假 T+0、AM=停牌窗假连续，本页主测盘后错侧限价假有效；**实验字母 AP ≠ params.Y ≠ params.N ≠ 实验字母 A ≠ 实验字母 P ≠ 实验字母 AO**；机制类预埋 fail_policy/oos/红线豁免/params 键；**待预检两条**见上；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA–AO/A/D–AO 正文**；**不改假设-H**；**不改假设-M**；**不改假设-AO**；**不改假设-O**；**不改假设-A**；**不改假设-P**；**不改假设-AE**；**不改假设-AM**）。
