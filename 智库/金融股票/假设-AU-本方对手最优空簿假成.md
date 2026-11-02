# 假设 AU · 本方/对手方最优空簿假成（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AT 正式【交】已收、可继续写可离线假设草稿；清单原止于 AT，无 AU 节 → 自立实验 AU；选题自 `事实与坑`「市价类型含最优 5 档剩撤 / 最优 5 档转限、**本方最优、对手方最优**；深市本方无申报或（其他类型）对手方无申报则撤」+ AT/AS/L 标准件交接（本方/对手方最优另桶，非五档转限、非剩撤/FOK、非通道有无主病）；与假设 A（板上可成交/枯竭）/ H（退市整理）/ X（主板 ST）/ E（整手）/ M（盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ N（收盘机制与假 GTC）/ S（经手费）/ T（证管费）/ U（过户费）/ L（市价通道·保护限价/穿过整本档位）/ AS（剩撤/FOK 假留簿）/ AT（五档转限价假撤或假转价）/ AC–AR（北交所/50万/假T+0/单笔上限/超板无效/不可撤窗/无板集合范围/复牌假连续/集合假连续/空窗假连续/停牌假连续/开盘集合剩单/收盘集合剩单/盘后错侧/临停笼子/板上假队首）/ I（价格笼子）/ F（涨跌停价取整）/ G（无板日误套默认板）/ J（无板日临停）/ D（成交时点与停牌）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区）/ P（指数停牌假成交权重）/ AB（融券卖出价限）**分列**；**新建实验 AU**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「本方最优/对手方最优」在空簿侧仍发明成交或不撤留簿；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AT 及其他 A/D–AT 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-U；不改假设-L；不改假设-AS；不改假设-AT；勿再改 AS/AT**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AT，本页自立实验 AU 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **本方最优 / 对手方最优** 市价子类型在**本方无申报**或**对手方无申报**时是否诚实**撤销**，还是发明**空簿假成**或**空簿假留簿续成**。双字母 **AU ≠ 单字母 A**。与假设 **U（过户费现行档误铺）** **硬分列**：U = 成本侧过户费 PIT；本页 = **市价子类型空簿语义**，不主测任何费率。双字母 **AU ≠ 单字母 U**。与假设 **L（市价通道）** **硬分列**：L = 市价当「穿过整本档位的无限价」及保护限价有无/集合禁市价等通道约束；本页 = 在已承认该腿为**本方最优或对手方最优**前提下，**空簿侧是否撤**；不重开「吃穿档位」主病与通道有无切日。与假设 **AS（剩撤/FOK 假留簿）** **硬分列**：AS = 剩撤类/FOK 未成部分本不该留簿却假留；本页 = **本方/对手方最优在空簿应撤却假成或假留**；不重开剩撤/FOK 主病。与假设 **AT（五档转限价假撤或假转价）** **硬分列**：AT = 最优五档剩余转限价的假撤/假转远价；本页 = **本方最优/对手方最优**空簿语义，不重开五档转限主病。与假设 **AR（板上排队假队首）** **分列**：AR = 已留簿限价队序；本页 = 空簿是否进簿/假成，队序交 AR。与假设 AN–AQ **硬分列**：不重开集合剩单/盘后错侧/临停笼子。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AU** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AU / 假设-AU / hypothesis_id=AU / 组 AU0·AU1·AU2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AU 混读或互改。亦**禁止**把实验字母 AU 与单字母实验 **A**、单字母实验 **U**、双字母实验 **AT**、双字母实验 **AS**、或 params 键名 `au0_*` 以外的实验页混读。**双字母 AU ≠ 单字母 A ≠ 单字母 U ≠ 双字母 AT ≠ 双字母 AS**；**params.Y ≠ 实验字母 AU**；**params.N ≠ 实验字母 AU**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，把**本方最优**在**本方无申报**、或**对手方最优**在**对手方无申报**时，仍当成可即时成交（空簿假成），或当成普通限价/本方最优价留簿并参加当日后续竞价（含板上）续成，相对「本方无申报或对手方无申报则撤销；缺类型/簿侧字段则 skip/敏感性档，禁止静默假成或假留」的 PIT 诚实组，会**系统性发明空簿假成路径（高估可成交名义）或空簿假留簿续成路径（错标/高估，尤其板上日）**；差异应**集中在空簿假成 / 空簿假留桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的空簿假成·假留贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在本方/对手方最优空簿相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 本方/对手方最优空簿假成 ≠ 市价保护通道有无；≠ 剩撤假留簿；≠ 五档转限价假撤/假转价；≠ 过户费；≠ 板上枯竭门槛

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AU；≠ 实验字母 A；≠ 实验字母 U
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AU
# params.asof_check_date                 写死默认 2026-10-16  # 事实与坑「市价申报约束 / 本方·对手方最优」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.own_opp_best_honest             写死 cancel_when_side_empty  # 诚实：本方无申报或对手方无申报 → 撤
# params.mkt_channel_handoff             写死 l_page          # 通道有无/吃穿档位/集合禁市价/保护限价切日交 L，不重开
# params.ioc_fok_handoff                 写死 as_page         # 剩撤/FOK 假留簿交 AS，不重开
# params.best5_to_limit_handoff          写死 at_page         # 五档转限价假撤/假转价交 AT，不重开
# params.queue_handoff                   写死 ar_page         # 若已诚实进簿后的队序交 AR，不重开
# params.au0_primary_demo                写死 invent_own_opp_best_fill_when_empty  # 风控补丁冻结；主报：空簿假成；禁与 invent_own_opp_best_as_resting 双挂
# params.au0_invent_fill_when_empty      写死 True           # 天真主路径（随 primary_demo）
# params.au1_rest_only                   写死 True           # 半泄露：仅空簿假留簿（非主报假成）
# params.au2_own_opp_best_policy         写死 cancel_when_side_empty
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AU≠A）
# params.merge_with_U_transfer_fee       写死 False          # 过户费另页 U（AU≠U）
# params.merge_with_L_mkt                写死 False          # 市价保护/通道另页 L
# params.merge_with_AS_ioc_fok           写死 False          # 剩撤/FOK 假留簿另页 AS
# params.merge_with_AT_best5_to_limit    写死 False          # 五档转限价另页 AT（AU≠AT）
# params.merge_with_AR_queue             写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_T_csrc_fee           写死 False
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
# params.universe_rule                   写死 sse_szse_common_stock_own_opp_best_check
# params.missing_ordtype_policy          写死 skip           # 缺申报类型标记 → skip（禁静默假成或假留）
# params.missing_book_side_policy        写死 skip           # 缺本方/对手方簿侧有无字段 → skip（禁静默假成）
# params.day_freq_proxy                  写死 own_opp_best_empty_sensitivity  # 日频无类型/簿侧明细时只报敏感性档；禁假装精确复盘
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AU；params.N≠实验字母 AU；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
own_opp_best_honest = "cancel_when_side_empty"
mkt_channel_handoff = "l_page"
ioc_fok_handoff = "as_page"
best5_to_limit_handoff = "at_page"
queue_handoff = "ar_page"
au0_primary_demo = "invent_own_opp_best_fill_when_empty"  # 风控补丁冻结；禁双挂
au0_invent_fill_when_empty = True
au1_rest_only = True
au2_own_opp_best_policy = "cancel_when_side_empty"
universe_rule = "sse_szse_common_stock_own_opp_best_check"
missing_ordtype_policy = "skip"
missing_book_side_policy = "skip"
day_freq_proxy = "own_opp_best_empty_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 au0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AU
G = 0.01
N = 0.05   # 风控补丁冻结；失败率门槛键 params.N ≠ 实验字母 AU
Y2 = 0.015

def is_own_or_opp_best_type(ordtype):
    """本方最优 / 对手方最优；不含剩撤类、不含 FOK、不含最优五档转限价主病。"""
    return ordtype in ("own_best", "opp_best", "best_own", "best_counterparty", "benfang_zuiyou", "duishoufang_zuiyou")

def side_empty(ordtype, own_side_has_quote, opp_side_has_quote):
    """本方最优看本方簿；对手方最优看对手方簿。缺字段 → None（走 skip）。"""
    if own_side_has_quote is None and opp_side_has_quote is None:
        return None
    if ordtype in ("own_best", "best_own", "benfang_zuiyou"):
        return (own_side_has_quote is False)
    if ordtype in ("opp_best", "best_counterparty", "duishoufang_zuiyou"):
        return (opp_side_has_quote is False)
    return None

def empty_side_policy(group, ordtype, signal_qty, own_side_has_quote, opp_side_has_quote, ref_px):
    """
    AU0：按 au0_primary_demo 单一主报（写死 invent_own_opp_best_fill_when_empty）
    AU1：仅空簿假留簿（非主报假成）
    AU2：cancel_when_side_empty；缺类型/簿侧 → skip（或日频敏感性档）
    """
    empty = side_empty(ordtype, own_side_has_quote, opp_side_has_quote)
    if group == "AU0" and au0_primary_demo == "invent_own_opp_best_fill_when_empty":
        if is_own_or_opp_best_type(ordtype) and au0_invent_fill_when_empty and empty is True:
            return ("fake_fill", signal_qty, ref_px)  # 空簿假成：高估可成交名义
        return "out_of_scope"
    if group == "AU1" and au1_rest_only:
        if is_own_or_opp_best_type(ordtype) and empty is True:
            return ("rest_fake", signal_qty, ref_px)  # 空簿假留簿续成
        return "out_of_scope"
    # AU2
    if ordtype is None:
        return "skip_or_day_freq_proxy"
    if not is_own_or_opp_best_type(ordtype):
        return "out_of_scope_other_ordtype"  # 剩撤/FOK 交 AS；五档转限交 AT；普通限价不属本页主测
    if empty is None:
        return "skip_or_day_freq_proxy"
    if empty is True:
        return ("cancel", 0, None)  # 诚实：空簿撤
    return ("match_or_rule", signal_qty, ref_px)  # 非空簿：按规则撮合；通道/保护限价交 L
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺申报类型标记却硬记空簿假成/假留、缺簿侧有无却静默假成、把 L 市价保护通道 / AS 剩撤假留簿 / AT 五档转限 / AR 板上假队首 / A 板上枯竭 / U 过户费 / AN–AQ 混进本页主表、日频无代理声明却假装逐笔类型复盘、诚实组对空簿仍假成或假留静默成功 → **跳过该日该券该腿**，不静默记假路径。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AU）

| 组 | 本方/对手方最优空簿 | 说明 |
|----|---------------------|------|
| AU0 天真 | 空簿假成（按 `au0_primary_demo` 单一主报） | 发明假成路径（高估名义） |
| AU1 半泄露/混口径 | 仅空簿假留簿续成 | 混口径假路径（错标/高估） |
| AU2 PIT 诚实 | cancel_when_side_empty；缺类型/簿侧 skip/敏感性 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测本方最优/对手方最优空簿语义**，不主测市价通道有无/吃穿档位（见 L）、不主测剩撤/FOK 假留簿（见 AS）、不主测五档转限价假撤/假转价（见 AT）、不主测板上队序（见 AR）、不主测板上枯竭门槛（见 A）、不主测过户费（见 U）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/U/L/AS/AT/AR/S/T/AN/AO/AP/AQ/AK/AL/AM/AJ/AH/AI/AG/AF/E/I/F/H/X/M/O/Q/R/AC/AD/AE/G/J/D/N/Y/K/AA/P/AB）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 写死冻结；可成交名义/冲击差显著门槛；≠实验字母 AU
params.G                            = 0.01                      # 写死冻结；空簿假成/假留桶相对对照差
params.N                            = 0.05                      # 写死冻结；失败/废单率差门槛；≠实验字母 AU
params.Y2                           = 0.015                     # 写死冻结；AU1（空簿假留）相对 AU2 专项门槛
params.au0_primary_demo             = invent_own_opp_best_fill_when_empty  # 写死冻结主报：空簿假成；禁与 invent_own_opp_best_as_resting 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_own_opp_best_check`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺申报类型且未声明日频代理；把 A/U/L/AS/AT/AR/AN–AQ 主结论并进本页主表；日频无代理声明却假装逐笔类型复盘；把剩撤/FOK/五档转限默认并进本方·对手方最优主病（交 AS/AT）；把过户费/经手费/证管费并进主病（交 U/S/T）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：本方/对手方最优空簿语义按成交日当时交易规则文本；**沪市保护限价有无/切日交 L**（主板约 2023-04-10 起与本方/对手方最优同批落地，切日不重开）；**禁止**用核对日「凡市价皆可空簿成」或「空簿皆留」铺满。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `au0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AU0 − AU2**：空簿假成相对诚实 cancel——假成 / 可成交名义高估。  
2. **AU1 − AU2**：仅空簿假留簿相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_own_opp_best_fill_when_empty",  # 空簿假成（主病）
  "invent_own_opp_best_as_resting",       # 空簿假留簿（AU1）
  "honest_cancel_when_side_empty",        # 对照诚实撤
  "board_day_empty_path",                 # 板上日空簿路径放大
  "vs_A_fill",                            # 对照声明：板上枯竭另页 A（AU≠A）
  "vs_U_transfer_fee",                    # 对照声明：过户费另页 U（AU≠U）
  "vs_L_mkt",                             # 对照声明：市价通道另页 L
  "vs_AS_ioc_fok",                        # 对照声明：剩撤/FOK 另页 AS
  "vs_AT_best5_to_limit",                 # 对照声明：五档转限另页 AT（AU≠AT）
  "vs_AR_queue",                          # 对照声明：板上假队首另页 AR
  "vs_AN_open_leftover",
  "vs_AO_close_leftover",
  "vs_AP_aft_side",
  "vs_AQ_halt_cage",
  "best5_ioc_fok_exempt",                 # 五档转限/剩撤/FOK 剔除（非本页主病）
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AU0/AU1 相对 AU2）；  
2. 空簿假成·假留腿贡献差 ΔFakeEmpty；  
3. 废单/失败率差 ΔFail；  
4. （可选）冲击差 ΔImpact（声明为代理，不冒充逐笔类型复盘）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeEmpty 桶贡献| **≥ params.G** 或 |ΔNotional_(AU1−AU2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「本方/对手方最优空簿执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AU 无关；风控补丁 2026-11-02）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AU） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 空簿假成/假留桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛（≠实验字母 AU） | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AU1−AU2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-16` |
| fill_time | 成交时点 | **写死** `next_open` |
| au0_primary_demo | 天真主报枚举 | **写死冻结** `invent_own_opp_best_fill_when_empty`（禁双挂；风控补丁 2026-11-02） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 cancel_when_side_empty；禁与 A/U/L/AS/AT/AR/AN–AQ 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分「本方最优/对手方最优」腿与剩撤/五档转限/普通限价腿，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把市价保护通道有无/吃穿档位（L）、剩撤/FOK 假留簿（AS）、五档转限价假撤/假转价（AT）、板上假队首（AR）、板上枯竭（A）、过户费（U）、集合剩单（AN/AO）、盘后错侧（AP）、临停笼子（AQ）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「空簿假成/假留」写成「板上能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
4. 把「空簿假成/假留」写成「过户费 PIT」而不声明另页 U → 与 U 撞题，设计失效。  
5. 把「空簿假成/假留」写成「市价保护限价/穿过整本档位」为主病而不声明另页 L → 与 L 撞题，设计失效。  
6. 把「空簿假成/假留」写成「剩撤/FOK 假留簿」而不声明另页 AS → 与 AS 撞题，设计失效。  
7. 把「空簿假成/假留」写成「五档转限价假撤或假转价」而不声明另页 AT → 与 AT 撞题，设计失效。  
8. 把「空簿假成/假留」写成「板上排队假队首」而不声明另页 AR → 与 AR 撞题，设计失效。  
9. holdout 反调 `au0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算冲击或板上价 → 标签与执行双错，结论无效。  
11. 把实验字母 AU 与单字母 A 或单字母 U 或双字母 AT 或双字母 AS 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 申报类型标记或代理（本方最优 / 对手方最优 / 剩撤类 / FOK / 最优五档转限价 / 普通限价）；  
- 本方簿侧有无 / 对手方簿侧有无代理（或日频 `own_opp_best_empty_sensitivity`）；  
- 交易日历；可选板上日标签（消费 A，不重开）；可选保护限价字段（消费 L，不重开主病）。

可选：逐笔/盘口（精确复盘空簿撤与撮合）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日「凡市价皆可空簿成」或「空簿皆留」铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 L 的「通道有无/吃穿档位」或 AS 的「剩撤假留簿」或 AT 的「五档转限假撤/假转价」或 AR 的「假队首」或 A 的「板上枯竭」或 U 的「过户费」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AU`  
- **组**：AU0 / AU1 / AU2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`own_opp_best_honest=cancel_when_side_empty`；`mkt_channel_handoff=l_page`；`ioc_fok_handoff=as_page`；`best5_to_limit_handoff=at_page`；`queue_handoff=ar_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_own_opp_best_check`；`missing_ordtype_policy=skip`；`missing_book_side_policy=skip`；`day_freq_proxy=own_opp_best_empty_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AU；**params.N≠实验字母 AU**；禁 null/holdout；风控补丁冻结 2026-11-02）；**`params.au0_primary_demo` 写死 `invent_own_opp_best_fill_when_empty`**（禁与 invent_own_opp_best_as_resting 双挂；风控补丁冻结 2026-11-02）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AU0/AU1/AU2 可成交名义/路径质量、ΔFakeEmpty、ΔFail；分桶（空簿假成 / 空簿假留 / 板上日 / vs A·U·L·AS·AT·AR·AN–AQ）。  
- 自检布尔：AU2 是否 cancel_when_side_empty；AU0 是否单一主报；AU1 是否仅空簿假留；是否未与 A/U/L/AS/AT/AR/AN–AQ 混主结论；holdout 是否未反调；**是否未把实验字母 AU 与 A 或 U 或 AT 或 AS 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AT 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-U / 假设-L / 假设-AS / 假设-AT**；**是否未再改 AS/AT**。  
- **禁止输出**：具体买卖标的列表当「建议」；把空簿假成/假留当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AT 及其他 A/D–AT 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-U**；**不改假设-L**；**不改假设-AS**；**不改假设-AT**；**勿再改 AS/AT**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：市价不是穿过整本档位的无限价；类型含本方最优、对手方最优；深市本方无申报或（其他类型）对手方无申报则撤。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AT，本页**新增实验 AU** 收成标准件，**不改口径主线**，**不改假设 A–AT 正文**。与实验 A/U/L/AS/AT/AR 分工：**A=板上枯竭门槛；U=过户费；L=市价保护/通道；AS=剩撤/FOK 假留簿；AT=五档转限价假撤或假转价；AR=板上排队假队首；AU=本方/对手方最优空簿假成（AU≠A≠U≠L≠AS≠AT≠AR）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；申报类型+簿侧有无代理或日频敏感性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**own_opp_best_honest=cancel_when_side_empty 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死 0.02/0.01/0.05/0.015（params.Y≠实验字母 AU；params.N≠实验字母 AU；风控补丁冻结 2026-11-02）**；**au0_primary_demo 写死 invent_own_opp_best_fill_when_empty（禁双挂；风控补丁冻结 2026-11-02）** |

---

## 风控补丁两条（已写死冻结 · 2026-11-02）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AU**；**`params.N` ≠ 实验字母 AU**；禁 null / holdout 标定。  
2. **`params.au0_primary_demo`**：**写死冻结** **`invent_own_opp_best_fill_when_empty`**；禁与 **`invent_own_opp_best_as_resting`** 双挂争主表（只挂一个 primary）。

---

## 变更

- 2026-11-02：风控补丁两条写死冻结——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 AU**；**params.N≠实验字母 AU**；禁 null/holdout）；② `params.au0_primary_demo=invent_own_opp_best_fill_when_empty`（禁与 `invent_own_opp_best_as_resting` 双挂）。参考总管派令 / 预检有条件通过。未改 Y/Z/AA–AT 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-U；不改假设-L；不改假设-AS；不改假设-AT；结论栏仍空；不开回测；不抢 A。
- 2026-11-02：新建标准件（总管线：AT 正式【交】已收后写下一纸面 AU；Y/Z/AA–AT 补丁/正文已交不改；清单止于 AT → 自 `事实与坑`「本方最优、对手方最优；空簿则撤」+ AT/AS/L「本方·对手方最优另桶」交接选题，**与 A/H/X/E/M/O/R/Q/N/S/T/U/L/AS/AT/AC–AR 硬分列**；**双字母 AU ≠ 单字母 A ≠ 单字母 U**；**不与 AN–AT 重复**；结论栏空；不开回测；不抢 A；**勿再改 AS/AT**）。
