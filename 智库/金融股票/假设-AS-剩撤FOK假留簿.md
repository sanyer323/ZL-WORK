# 假设 AS · 剩撤/FOK 假留簿续成（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AR 补丁已交后写下一纸面 AS；清单原止于 AR，无 AS 节 → 自立实验 AS；选题自 `事实与坑`「申报当日有效、未成交部分继续参加当日竞价——**部分市价类型除外，那些剩撤/FOK 本来就不留**」+ 口径「执行鸿沟」；与假设 A（板上可成交/枯竭）/ H（退市整理）/ X（主板 ST）/ E（整手）/ M（盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ N（收盘机制与假 GTC）/ S（经手费）/ L（市价通道·保护限价/穿过整本档位）/ AC–AR（北交所/50万/假T+0/单笔上限/超板无效/不可撤窗/无板集合范围/复牌假连续/集合假连续/空窗假连续/停牌假连续/开盘集合剩单/收盘集合剩单/盘后错侧/临停笼子/板上假队首）/ I（价格笼子）/ F（涨跌停价取整）/ G（无板日误套默认板）/ J（无板日临停）/ D（成交时点与停牌）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区）/ P（指数停牌假成交权重）/ AB（融券卖出价限）**分列**；**新建实验 AS**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「剩撤/FOK 未成部分继续留簿当日续成」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AR 及其他 A/D–AR 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-S；不改假设-L；不改假设-AR；勿再改 AR**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AR，本页自立实验 AS 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **即时成交剩余撤销（IOC/最优五档剩撤等）与全额成交或撤销（FOK）** 在未即时全成时，是否诚实**撤销未成部分**，还是发明**假留簿**并按当日后续竞价（含板上）续成。双字母 **AS ≠ 单字母 A**。与假设 **S（经手费现行档误铺）** **硬分列**：S = 成本侧经手费 PIT；本页 = **申报类型剩撤语义**，不主测费率。双字母 **AS ≠ 单字母 S**。与假设 **L（市价通道）** **硬分列**：L = 市价当「穿过整本档位的无限价」及保护限价/集合禁市价等通道约束；本页 = 在已承认该腿为**剩撤类/FOK 类型**前提下，**未成部分是否留簿续成**；不重开保护限价带宽与「吃穿档位」主病。与假设 **AR（板上排队假队首）** **硬分列**：AR = 已留簿限价在板上的队序分配；本页 = **本不该留簿的剩撤/FOK 是否被发明成留簿**（发明留簿之后的队序交 AR，不重开）。与假设 AN–AQ **硬分列**：AN/AO=开/收盘**集合**剩单假即时成或假进盘后；本页 = **连续竞价市价剩撤/FOK** 类型语义，不重开集合清算剩单规则。与假设 AH/N **分列**：AH=不可撤窗假撤改；N=收盘切日/隔夜假 GTC；本页不主测撤改窗或隔夜有效。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AS** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AS / 假设-AS / hypothesis_id=AS / 组 AS0·AS1·AS2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AS 混读或互改。亦**禁止**把实验字母 AS 与单字母实验 **A**、单字母实验 **S**、双字母实验 **AR**、或 params 键名 `as0_*` 以外的实验页混读。**双字母 AS ≠ 单字母 A ≠ 单字母 S ≠ 双字母 AR**；**params.Y ≠ 实验字母 AS**；**params.N ≠ 实验字母 AS**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，把**即时成交剩余撤销 / 最优五档剩撤等剩撤类**或**全额成交或撤销（FOK）**申报的未即时成交部分，当成普通限价**留簿并参加当日后续竞价（含板上）续成**，相对「剩撤类未成部分立即撤销；FOK 未全成则整笔撤销、不留簿；缺类型标记则 skip/敏感性档，禁止静默当留簿」的 PIT 诚实组，会**系统性发明假留簿续成路径并高估可成交名义（尤其板上日）**；差异应**集中在假留簿 / 假部分成后续成桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假留簿贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在剩撤/FOK 类型相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 剩撤/FOK 假留簿 ≠ 市价保护通道；≠ 板上假队首；≠ 集合剩单；≠ 经手费；≠ 板上枯竭门槛

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AS；≠ 实验字母 A；≠ 实验字母 S
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AS
# params.asof_check_date                 写死默认 2026-10-19  # 事实与坑「剩撤/FOK 本来就不留」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.ioc_fok_honest                  写死 cancel_unfilled  # 诚实：剩撤未成撤销；FOK 未全成整笔撤
# params.mkt_channel_handoff             写死 l_page          # 保护限价/吃穿档位/集合禁市价交 L，不重开
# params.queue_handoff                   写死 ar_page         # 若已诚实留簿后的队序交 AR，不重开
# params.as0_primary_demo                写死 invent_ioc_as_resting_limit  # 风控补丁冻结；主报：剩撤未成假留簿续成；禁与 invent_fok_as_partial_rest 双挂
# params.as0_invent_ioc_rest             写死 True           # 天真主路径（随 primary_demo）
# params.as1_fok_partial_only            写死 True           # 半泄露：仅 FOK 假部分成并留/续（非主报剩撤留簿）
# params.as2_ioc_fok_policy              写死 cancel_unfilled
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AS≠A）
# params.merge_with_S_handling_fee       写死 False          # 经手费另页 S（AS≠S）
# params.merge_with_L_mkt                写死 False          # 市价保护/通道另页 L
# params.merge_with_AR_queue             写死 False          # 板上假队首另页 AR
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AQ_halt_cage         写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_AL_session_gap       写死 False
# params.merge_with_AM_halt              写死 False
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_R_etf_rotation       写死 False
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
# params.merge_with_AB_short_px          写死 False
# params.universe_rule                   写死 sse_szse_common_stock_ioc_fok_check
# params.missing_ordtype_policy          写死 skip           # 缺申报类型标记 → skip（禁静默当留簿）
# params.day_freq_proxy                  写死 ioc_fok_rest_sensitivity  # 日频无类型明细时只报敏感性档；禁假装精确复盘类型
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AS；params.N≠实验字母 AS；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-19"
px_basis = "unadj"
tick = 0.01
ioc_fok_honest = "cancel_unfilled"
mkt_channel_handoff = "l_page"
queue_handoff = "ar_page"
as0_primary_demo = "invent_ioc_as_resting_limit"  # 风控补丁冻结；禁双挂
as0_invent_ioc_rest = True
as1_fok_partial_only = True
as2_ioc_fok_policy = "cancel_unfilled"
universe_rule = "sse_szse_common_stock_ioc_fok_check"
missing_ordtype_policy = "skip"
day_freq_proxy = "ioc_fok_rest_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 as0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AS
G = 0.01
N = 0.05   # 风控补丁冻结；失败率门槛键 params.N ≠ 实验字母 AS
Y2 = 0.015

def is_cancel_remainder_type(ordtype):
    """剩撤类：即时成交剩余撤销、最优五档即时成交剩余撤销等；不含「最优五档剩余转限价」。"""
    return ordtype in ("ioc", "best5_cancel_remainder", "immediate_cancel_remainder")

def is_fok_type(ordtype):
    return ordtype in ("fok", "fill_or_kill", "all_or_none_cancel")

def leftover_policy(group, ordtype, filled_qty, signal_qty):
    """
    AS0：按 as0_primary_demo 单一主报（写死 invent_ioc_as_resting_limit）
    AS1：仅 FOK 假部分成并续（非主报剩撤留簿）
    AS2：cancel_unfilled；缺类型 → skip（或日频敏感性档）
    """
    unfilled = max(0, signal_qty - filled_qty)
    if unfilled <= 0:
        return 0
    if group == "AS0" and as0_primary_demo == "invent_ioc_as_resting_limit":
        if is_cancel_remainder_type(ordtype) and as0_invent_ioc_rest:
            return unfilled  # 假留簿续成数量
        return 0
    if group == "AS1" and as1_fok_partial_only:
        if is_fok_type(ordtype):
            return unfilled  # 假：FOK 未全成仍部分成并续/留
        return 0
    # AS2
    if ordtype is None:
        return "skip_or_day_freq_proxy"
    if is_cancel_remainder_type(ordtype) or is_fok_type(ordtype):
        return 0  # 诚实撤销未成
    return "out_of_scope_resting_limit"  # 普通限价留簿不属本页主测
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺申报类型标记却硬记留簿续成、把 L 市价保护通道 / AR 板上假队首 / A 板上枯竭 / AN–AQ 集合剩单·盘后错侧·临停笼子 / S 经手费混进本页主表、日频无代理声明却假装逐笔类型复盘、诚实组对剩撤/FOK 仍留簿 → **跳过该日该券该腿**，不静默记假留簿成。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AS）

| 组 | 剩撤/FOK 未成部分 | 说明 |
|----|-------------------|------|
| AS0 天真 | 剩撤未成假留簿续成（按 `as0_primary_demo` 单一主报） | 发明假留簿路径 |
| AS1 半泄露/混口径 | 仅 FOK 假部分成并续 | 混口径假路径 |
| AS2 PIT 诚实 | cancel_unfilled；缺类型 skip/敏感性 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测剩撤/FOK 未成部分是否留簿**，不主测市价保护限价/吃穿档位（见 L）、不主测板上队序（见 AR）、不主测板上枯竭门槛（见 A）、不主测集合剩单（见 AN/AO）、不主测经手费（见 S）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/S/L/AR/AN/AO/AP/AQ/AK/AL/AM/AJ/AH/AI/AG/AF/E/I/F/H/X/M/O/Q/R/AC/AD/AE/G/J/D/N/Y/K/AA/P/AB）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 写死冻结；可成交名义/冲击差显著门槛；≠实验字母 AS
params.G                            = 0.01                      # 写死冻结；假留簿桶相对对照差
params.N                            = 0.05                      # 写死冻结；失败/废单率差门槛；≠实验字母 AS
params.Y2                           = 0.015                     # 写死冻结；AS1（FOK 假部分）相对 AS2 专项门槛
params.as0_primary_demo             = invent_ioc_as_resting_limit  # 写死冻结主报：剩撤假留簿；禁与 invent_fok_as_partial_rest 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_ioc_fok_check`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺申报类型且未声明日频代理；把 A/S/L/AR/AN–AQ 主结论并进本页主表；日频无代理声明却假装逐笔类型复盘；把「最优五档剩余**转限价**」默认并进剩撤主病（转限价本可留簿，须另桶或剔除）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：剩撤/FOK 语义按成交日当时交易规则文本；**市价保护/集合禁市价交 L**；**禁止**用核对日「凡市价皆留簿」铺满。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `as0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AS0 − AS2**：剩撤假留簿续成相对诚实 cancel_unfilled——假留簿 / 可成交名义高估。  
2. **AS1 − AS2**：仅 FOK 假部分成并续相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_ioc_as_resting_limit",       # 剩撤未成假留簿续成（主病）
  "invent_fok_as_partial_rest",        # FOK 假部分成并续（AS1）
  "honest_cancel_unfilled",            # 对照诚实撤销未成
  "board_day_rest_invent",             # 板上日假留簿续成放大
  "vs_A_fill",                         # 对照声明：板上枯竭另页 A（AS≠A）
  "vs_S_handling_fee",                 # 对照声明：经手费另页 S（AS≠S）
  "vs_L_mkt",                          # 对照声明：市价通道另页 L
  "vs_AR_queue",                       # 对照声明：板上假队首另页 AR
  "vs_AN_open_leftover",               # 对照声明：开盘集合剩单另页 AN
  "vs_AO_close_leftover",              # 对照声明：收盘集合剩单另页 AO
  "vs_AP_aft_side",                    # 对照声明：盘后错侧另页 AP
  "vs_AQ_halt_cage",                   # 对照声明：临停笼子另页 AQ
  "best5_to_limit_exempt",             # 「剩余转限价」另桶/剔除（非剩撤）
  "day_freq_proxy_only",               # 日频敏感性档（无类型明细）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AS0/AS1 相对 AS2）；  
2. 假留簿腿贡献差 ΔFakeRest；  
3. 废单/失败率差 ΔFail；  
4. （可选）冲击差 ΔImpact（声明为代理，不冒充逐笔类型复盘）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeRest 桶贡献| **≥ params.G** 或 |ΔNotional_(AS1−AS2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「剩撤/FOK 留簿执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AS 无关；风控补丁 2026-11-02）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AS） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 假留簿桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛（≠实验字母 AS） | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AS1−AS2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19` |
| fill_time | 成交时点 | **写死** `next_open` |
| as0_primary_demo | 天真主报枚举 | **写死冻结** `invent_ioc_as_resting_limit`（禁双挂；风控补丁 2026-11-02） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 cancel_unfilled；禁与 A/S/L/AR/AN–AQ 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分剩撤/FOK 腿与普通限价腿，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把市价保护/吃穿档位（L）、板上假队首（AR）、板上枯竭（A）、集合剩单（AN/AO）、盘后错侧（AP）、临停笼子（AQ）、经手费（S）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「假留簿」写成「板上能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
4. 把「假留簿」写成「经手费 PIT」而不声明另页 S → 与 S 撞题，设计失效。  
5. 把「假留簿」写成「市价保护限价/穿过整本档位」为主病而不声明另页 L → 与 L 撞题，设计失效。  
6. 把「假留簿」写成「板上排队假队首」而不声明另页 AR → 与 AR 撞题，设计失效。  
7. 把「假留簿」写成「开盘/收盘集合剩单假即时成」而不声明另页 AN/AO → 与 AN/AO 撞题，设计失效。  
8. 把「最优五档剩余转限价」默认并进剩撤主病且不另桶 → 标签污染，结论无效。  
9. holdout 反调 `as0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算冲击或板上价 → 标签与执行双错，结论无效。  
11. 把实验字母 AS 与单字母 A 或单字母 S 或双字母 AR 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 申报类型标记或代理（剩撤类 / FOK / 普通限价 / 转限价）；  
- 即时可成交量代理（或日频 `ioc_fok_rest_sensitivity`）；  
- 交易日历；可选板上日标签（消费 A，不重开）。

可选：逐笔/盘口（精确复盘即时成与撤销）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日「凡市价皆留簿」铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 L 的「保护限价/吃穿档位」或 AR 的「假队首」或 A 的「板上枯竭」或 AN/AO 的集合剩单或 S 的经手费当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AS`  
- **组**：AS0 / AS1 / AS2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-19`；`ioc_fok_honest=cancel_unfilled`；`mkt_channel_handoff=l_page`；`queue_handoff=ar_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_ioc_fok_check`；`missing_ordtype_policy=skip`；`day_freq_proxy=ioc_fok_rest_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AS；**params.N≠实验字母 AS**；禁 null/holdout；**风控补丁冻结 2026-11-02**）；**`params.as0_primary_demo` 写死 `invent_ioc_as_resting_limit`**（禁与 invent_fok_as_partial_rest 双挂；**风控补丁冻结 2026-11-02**）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AS0/AS1/AS2 可成交名义/路径质量、ΔFakeRest、ΔFail；分桶（假留簿 / FOK 假部分 / 板上日 / vs A·S·L·AR·AN·AO·AP·AQ）。  
- 自检布尔：AS2 是否 cancel_unfilled；AS0 是否单一主报；AS1 是否仅 FOK 假部分；是否未与 A/S/L/AR/AN–AQ 混主结论；holdout 是否未反调；**是否未把实验字母 AS 与 A 或 S 或 AR 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AR 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-S / 假设-L / 假设-AR**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假留簿当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AR 及其他 A/D–AR 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-S**；**不改假设-L**；**不改假设-AR**；**勿再改 AR**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：申报当日有效、未成交部分继续参加当日竞价——**部分市价类型除外，那些剩撤/FOK 本来就不留**。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AR，本页**新增实验 AS** 收成标准件，**不改口径主线**，**不改假设 A–AR 正文**。与实验 A/S/L/AR/AN–AQ 分工：**A=板上枯竭门槛；S=经手费；L=市价保护/通道；AR=板上排队假队首；AN/AO=集合剩单；AS=剩撤/FOK 假留簿续成（AS≠A≠S≠L≠AR≠AN≠AO）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；申报类型+即时可成代理或日频敏感性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**ioc_fok_honest=cancel_unfilled 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死 0.02/0.01/0.05/0.015（params.Y≠实验字母 AS；params.N≠实验字母 AS；风控补丁冻结 2026-11-02）**；**as0_primary_demo 写死 invent_ioc_as_resting_limit（禁双挂；风控补丁冻结 2026-11-02）** |

---

## 风控补丁两条（已写死冻结 · 2026-11-02）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AS**；**`params.N` ≠ 实验字母 AS**；禁 null / holdout 标定。  
2. **`params.as0_primary_demo`**：**写死冻结** **`invent_ioc_as_resting_limit`**；禁与 **`invent_fok_as_partial_rest`** 双挂争主表（只挂一个 primary）。

---

## 变更

- 2026-11-02：风控补丁两条写死冻结——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 AS**；**params.N≠实验字母 AS**；禁 null/holdout）；② `params.as0_primary_demo=invent_ioc_as_resting_limit`（禁与 `invent_fok_as_partial_rest` 双挂）。参考 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AS-20261102.md`。未改 Y/Z/AA–AR 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-S；不改假设-L；不改假设-AR；结论栏仍空；不开回测；不抢 A。
- 2026-11-02：新建标准件（总管线：AR 补丁已交后写下一纸面 AS；Y/Z/AA–AR 补丁已交不改；清单止于 AR → 自 `事实与坑`「剩撤/FOK 本来就不留」选题，**与 A/H/X/E/M/O/R/Q/N/S/L/AC–AR 硬分列**；**双字母 AS ≠ 单字母 A ≠ 单字母 S**；**不与 AN–AR 重复**；结论栏空；不开回测；不抢 A；**勿再改 AR**）。