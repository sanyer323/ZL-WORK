# 假设 AT · 五档转限价假撤或假转价（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AS 补丁已交后写下一纸面 AT；清单原止于 AS，无 AT 节 → 自立实验 AT；选题自 `事实与坑`「市价类型含最优 5 档剩撤 / **最优 5 档转限**、本方最优、对手方最优；沪市成交价和转限价不得突破保护限价」+ AS 标准件明确「**最优五档剩余转限价**另桶/剔除（非剩撤）」交接；与假设 A（板上可成交/枯竭）/ H（退市整理）/ X（主板 ST）/ E（整手）/ M（盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ N（收盘机制与假 GTC）/ S（经手费）/ T（证管费）/ L（市价通道·保护限价/穿过整本档位）/ AS（剩撤/FOK 假留簿）/ AC–AR（北交所/50万/假T+0/单笔上限/超板无效/不可撤窗/无板集合范围/复牌假连续/集合假连续/空窗假连续/停牌假连续/开盘集合剩单/收盘集合剩单/盘后错侧/临停笼子/板上假队首）/ I（价格笼子）/ F（涨跌停价取整）/ G（无板日误套默认板）/ J（无板日临停）/ D（成交时点与停牌）/ Y（集合量分母）/ K（融券空头名单）/ AA（分钟 bar 时区）/ P（指数停牌假成交权重）/ AB（融券卖出价限）**分列**；**新建实验 AT**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-02）**（结论栏空；禁止把「最优五档剩余转限价」当剩撤撤销或不按保护限价转限；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AS 及其他 A/D–AS 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-T；不改假设-L；不改假设-AS；勿再改 AS**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AS，本页自立实验 AT 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **「最优五档即时成交剩余转限价」** 类型在五档内部分成交后，剩余是否诚实**按规则转限价留簿**（沪市转限价不得突破保护限价），还是发明**假撤**（当成剩撤不留）或**假转价**（突破保护限价/发明远价留簿续成）。双字母 **AT ≠ 单字母 A**。与假设 **T（证管费误抽）** **硬分列**：T = 成本侧证管费 PIT（预检-假设T 旧题）；本页 = **市价子类型转限价语义**，不主测任何费率。双字母 **AT ≠ 单字母 T**；**明确避开「预检T」旧题（证管费误抽）**。与假设 **L（市价通道）** **硬分列**：L = 市价当「穿过整本档位的无限价」及保护限价有无/集合禁市价等通道约束；本页 = 在已承认该腿为**最优五档剩余转限价**前提下，**剩余是否留簿、转限价是否诚实**；不重开「吃穿档位」主病与通道有无切日。与假设 **AS（剩撤/FOK 假留簿）** **硬分列**：AS = 剩撤类/FOK 未成部分本不该留簿却假留；本页 = **转限价本可留簿**却被假撤，或留簿时转限价假远；AS 已声明转限价另桶，本页承接该另桶，不重开剩撤/FOK 主病。与假设 **AR（板上排队假队首）** **分列**：AR = 已留簿限价队序；本页 = 转限后是否进簿及进簿价，队序交 AR。与假设 AN–AQ **硬分列**：不重开集合剩单/盘后错侧/临停笼子。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AT** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AT / 假设-AT / hypothesis_id=AT / 组 AT0·AT1·AT2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AT 混读或互改。亦**禁止**把实验字母 AT 与单字母实验 **A**、单字母实验 **T**、双字母实验 **AS**、或 params 键名 `at0_*` 以外的实验页混读。**双字母 AT ≠ 单字母 A ≠ 单字母 T ≠ 双字母 AS**；**params.Y ≠ 实验字母 AT**；**params.N ≠ 实验字母 AT**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，把**最优五档即时成交剩余转限价**在五档内部分成交后的剩余，当成**剩撤类撤销不留簿**，或转限后按**突破保护限价 / 发明远价**留簿并参加当日后续竞价（含板上）续成，相对「五档内即时成；剩余以规则转限价留簿；沪市转限价不得突破保护限价；缺类型/保护限价字段则 skip/敏感性档，禁止静默当撤或当远价」的 PIT 诚实组，会**系统性发明假撤路径（低估可续成名义）或假转价续成路径（错标/高估可成交名义，尤其板上日）**；差异应**集中在假撤 / 假转价桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假撤·假转价贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在转限价类型相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 五档转限价假撤/假转价 ≠ 剩撤假留簿；≠ 市价保护通道有无；≠ 板上假队首；≠ 证管费；≠ 板上枯竭门槛

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-02）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AT；≠ 实验字母 A；≠ 实验字母 T
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AT
# params.asof_check_date                 写死默认 2026-10-16  # 事实与坑「市价申报约束 / 最优5档转限」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.best5_to_limit_honest           写死 convert_at_protect_or_rule  # 诚实：剩余转限留簿；沪市≤保护限价
# params.mkt_channel_handoff             写死 l_page          # 通道有无/吃穿档位/集合禁市价交 L，不重开
# params.ioc_fok_handoff                 写死 as_page         # 剩撤/FOK 假留簿交 AS，不重开
# params.queue_handoff                   写死 ar_page         # 若已诚实转限留簿后的队序交 AR，不重开
# params.at0_primary_demo                写死 invent_best5_to_limit_as_cancel  # 风控补丁冻结；主报：转限价假撤；禁与 invent_best5_to_limit_far_px 双挂
# params.at0_invent_as_cancel            写死 True           # 天真主路径（随 primary_demo）
# params.at1_far_px_only                 写死 True           # 半泄露：仅假转远价留簿（非主报假撤）
# params.at2_best5_to_limit_policy       写死 convert_at_protect_or_rule
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AT≠A）
# params.merge_with_T_csrc_fee           写死 False          # 证管费另页 T（AT≠T；避开预检T旧题）
# params.merge_with_L_mkt                写死 False          # 市价保护/通道另页 L
# params.merge_with_AS_ioc_fok           写死 False          # 剩撤/FOK 假留簿另页 AS
# params.merge_with_AR_queue             写死 False
# params.merge_with_S_handling_fee       写死 False
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
# params.universe_rule                   写死 sse_szse_common_stock_best5_to_limit_check
# params.missing_ordtype_policy          写死 skip           # 缺申报类型标记 → skip（禁静默当撤或当远价）
# params.missing_protect_px_policy       写死 skip           # 沪市缺保护限价字段 → skip（禁静默远价）
# params.day_freq_proxy                  写死 best5_to_limit_sensitivity  # 日频无类型明细时只报敏感性档；禁假装精确复盘类型
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AT；params.N≠实验字母 AT；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
best5_to_limit_honest = "convert_at_protect_or_rule"
mkt_channel_handoff = "l_page"
ioc_fok_handoff = "as_page"
queue_handoff = "ar_page"
at0_primary_demo = "invent_best5_to_limit_as_cancel"  # 风控补丁冻结；禁双挂
at0_invent_as_cancel = True
at1_far_px_only = True
at2_best5_to_limit_policy = "convert_at_protect_or_rule"
universe_rule = "sse_szse_common_stock_best5_to_limit_check"
missing_ordtype_policy = "skip"
missing_protect_px_policy = "skip"
day_freq_proxy = "best5_to_limit_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-02）；禁 holdout / 事后改口 / 禁跑后改 at0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AT
G = 0.01
N = 0.05   # 风控补丁冻结；失败率门槛键 params.N ≠ 实验字母 AT
Y2 = 0.015

def is_best5_to_limit_type(ordtype):
    """最优五档即时成交剩余转限价；不含剩撤类、不含 FOK、不含本方/对手方最优主病。"""
    return ordtype in ("best5_to_limit", "best5_convert_remainder", "optimal_5_to_limit")

def remainder_policy(group, ordtype, filled_qty, signal_qty, protect_px, convert_px):
    """
    AT0：按 at0_primary_demo 单一主报（写死 invent_best5_to_limit_as_cancel）
    AT1：仅假转远价留簿（非主报假撤）
    AT2：convert_at_protect_or_rule；缺类型/保护限价 → skip（或日频敏感性档）
    """
    unfilled = max(0, signal_qty - filled_qty)
    if unfilled <= 0:
        return 0
    if group == "AT0" and at0_primary_demo == "invent_best5_to_limit_as_cancel":
        if is_best5_to_limit_type(ordtype) and at0_invent_as_cancel:
            return 0  # 假撤：剩余记 0、不留簿（低估续成）
        return "out_of_scope"
    if group == "AT1" and at1_far_px_only:
        if is_best5_to_limit_type(ordtype):
            return ("rest_far", unfilled, invent_far_convert_px(protect_px, convert_px))
        return "out_of_scope"
    # AT2
    if ordtype is None:
        return "skip_or_day_freq_proxy"
    if not is_best5_to_limit_type(ordtype):
        return "out_of_scope_other_ordtype"  # 剩撤/FOK 交 AS；普通限价不属本页主测
    return ("rest_honest", unfilled, honest_convert_px(protect_px, convert_px))
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺申报类型标记却硬记假撤/假转价、把 L 市价保护通道 / AS 剩撤假留簿 / AR 板上假队首 / A 板上枯竭 / T 证管费 / AN–AQ 混进本页主表、日频无代理声明却假装逐笔类型复盘、诚实组对转限价仍假撤或突破保护限价静默成功 → **跳过该日该券该腿**，不静默记假路径。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AT）

| 组 | 五档转限价剩余 | 说明 |
|----|----------------|------|
| AT0 天真 | 转限价假撤不留簿（按 `at0_primary_demo` 单一主报） | 发明假撤路径（低估续成） |
| AT1 半泄露/混口径 | 仅假转远价留簿续成 | 混口径假路径（错标/高估） |
| AT2 PIT 诚实 | convert_at_protect_or_rule；缺类型/保护限价 skip/敏感性 | 与事实与坑同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测最优五档剩余转限价语义**，不主测市价通道有无/吃穿档位（见 L）、不主测剩撤/FOK 假留簿（见 AS）、不主测板上队序（见 AR）、不主测板上枯竭门槛（见 A）、不主测证管费（见 T）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/T/L/AS/AR/S/AN/AO/AP/AQ/AK/AL/AM/AJ/AH/AI/AG/AF/E/I/F/H/X/M/O/Q/R/AC/AD/AE/G/J/D/N/Y/K/AA/P/AB）**。

**风控补丁两条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 写死冻结；可成交名义/冲击差显著门槛；≠实验字母 AT
params.G                            = 0.01                      # 写死冻结；假撤/假转价桶相对对照差
params.N                            = 0.05                      # 写死冻结；失败/废单率差门槛；≠实验字母 AT
params.Y2                           = 0.015                     # 写死冻结；AT1（假转远价）相对 AT2 专项门槛
params.at0_primary_demo             = invent_best5_to_limit_as_cancel  # 写死冻结主报：转限价假撤；禁与 invent_best5_to_limit_far_px 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_best5_to_limit_check`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺申报类型且未声明日频代理；把 A/T/L/AS/AR/AN–AQ 主结论并进本页主表；日频无代理声明却假装逐笔类型复盘；把剩撤/FOK 默认并进转限价主病（交 AS）；把证管费/经手费并进主病（交 T/S）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：最优五档转限价语义按成交日当时交易规则文本；**沪市保护限价有无/切日交 L**；**禁止**用核对日「凡市价皆撤」或「转限可任意远价」铺满。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `at0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AT0 − AT2**：转限价假撤相对诚实 convert——假撤 / 可续成名义低估。  
2. **AT1 − AT2**：仅假转远价留簿相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_best5_to_limit_as_cancel",   # 转限价假撤（主病）
  "invent_best5_to_limit_far_px",      # 假转远价留簿（AT1）
  "honest_convert_at_protect",         # 对照诚实转限
  "board_day_convert_path",            # 板上日转限路径放大
  "vs_A_fill",                         # 对照声明：板上枯竭另页 A（AT≠A）
  "vs_T_csrc_fee",                     # 对照声明：证管费另页 T（AT≠T；避开预检T）
  "vs_L_mkt",                          # 对照声明：市价通道另页 L
  "vs_AS_ioc_fok",                     # 对照声明：剩撤/FOK 另页 AS
  "vs_AR_queue",                       # 对照声明：板上假队首另页 AR
  "vs_AN_open_leftover",
  "vs_AO_close_leftover",
  "vs_AP_aft_side",
  "vs_AQ_halt_cage",
  "ioc_fok_exempt",                    # 剩撤/FOK 剔除（非本页主病）
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AT0/AT1 相对 AT2）；  
2. 假撤·假转价腿贡献差 ΔFakeConvert；  
3. 废单/失败率差 ΔFail；  
4. （可选）冲击差 ΔImpact（声明为代理，不冒充逐笔类型复盘）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeConvert 桶贡献| **≥ params.G** 或 |ΔNotional_(AT1−AT2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「五档转限价执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AT 无关；风控补丁 2026-11-02）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AT） | **写死冻结** `0.02`（风控补丁 2026-11-02） |
| params.G | 假撤/假转价桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-02） |
| params.N | 失败/废单率差门槛（≠实验字母 AT） | **写死冻结** `0.05`（风控补丁 2026-11-02） |
| params.Y2 | AT1−AT2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-02） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-16` |
| fill_time | 成交时点 | **写死** `next_open` |
| at0_primary_demo | 天真主报枚举 | **写死冻结** `invent_best5_to_limit_as_cancel`（禁双挂；风控补丁 2026-11-02） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 convert_at_protect_or_rule；禁与 A/T/L/AS/AR/AN–AQ 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分「最优五档转限价」腿与剩撤/普通限价腿，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把市价保护通道有无/吃穿档位（L）、剩撤/FOK 假留簿（AS）、板上假队首（AR）、板上枯竭（A）、证管费（T）、集合剩单（AN/AO）、盘后错侧（AP）、临停笼子（AQ）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「假撤/假转价」写成「板上能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
4. 把「假撤/假转价」写成「证管费 PIT」而不声明另页 T → 与 T / 预检T旧题撞题，设计失效。  
5. 把「假撤/假转价」写成「市价保护限价/穿过整本档位」为主病而不声明另页 L → 与 L 撞题，设计失效。  
6. 把「假撤/假转价」写成「剩撤/FOK 假留簿」而不声明另页 AS → 与 AS 撞题，设计失效。  
7. 把「假撤/假转价」写成「板上排队假队首」而不声明另页 AR → 与 AR 撞题，设计失效。  
8. holdout 反调 `at0_primary_demo` / Y·G·N·Y2 → 结论无效。  
9. 用复权价算冲击或板上价 → 标签与执行双错，结论无效。  
10. 把实验字母 AT 与单字母 A 或单字母 T 或双字母 AS 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 申报类型标记或代理（最优五档转限价 / 剩撤类 / FOK / 普通限价）；  
- 保护限价字段或代理（沪市；缺则 skip）；  
- 即时可成交量（五档内）代理（或日频 `best5_to_limit_sensitivity`）；  
- 交易日历；可选板上日标签（消费 A，不重开）。

可选：逐笔/盘口（精确复盘五档内成与转限）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日「凡市价皆撤」或「转限可任意远价」铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 L 的「通道有无/吃穿档位」或 AS 的「剩撤假留簿」或 AR 的「假队首」或 A 的「板上枯竭」或 T 的「证管费」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AT`  
- **组**：AT0 / AT1 / AT2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`best5_to_limit_honest=convert_at_protect_or_rule`；`mkt_channel_handoff=l_page`；`ioc_fok_handoff=as_page`；`queue_handoff=ar_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_best5_to_limit_check`；`missing_ordtype_policy=skip`；`missing_protect_px_policy=skip`；`day_freq_proxy=best5_to_limit_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AT；**params.N≠实验字母 AT**；禁 null/holdout；**风控补丁冻结 2026-11-02**）；**`params.at0_primary_demo` 写死 `invent_best5_to_limit_as_cancel`**（禁与 invent_best5_to_limit_far_px 双挂；**风控补丁冻结 2026-11-02**）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AT0/AT1/AT2 可成交名义/路径质量、ΔFakeConvert、ΔFail；分桶（假撤 / 假转远价 / 板上日 / vs A·T·L·AS·AR·AN–AQ）。  
- 自检布尔：AT2 是否 convert_at_protect_or_rule；AT0 是否单一主报；AT1 是否仅假转远价；是否未与 A/T/L/AS/AR/AN–AQ 混主结论；holdout 是否未反调；**是否未把实验字母 AT 与 A 或 T 或 AS 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AS 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-T / 假设-L / 假设-AS**；**是否未重做预检T（证管费）旧题**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假撤/假转价当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AS 及其他 A/D–AS 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-T**；**不改假设-L**；**不改假设-AS**；**勿再改 AS**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：市价不是穿过整本档位的无限价；沪市须保护限价且转限价不得突破；类型含最优 5 档转限（与剩撤分列）。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AS，本页**新增实验 AT** 收成标准件，**不改口径主线**，**不改假设 A–AS 正文**。与实验 A/T/L/AS/AR 分工：**A=板上枯竭门槛；T=证管费（预检T旧题，本页避开）；L=市价保护/通道；AS=剩撤/FOK 假留簿；AR=板上排队假队首；AT=五档转限价假撤或假转价（AT≠A≠T≠L≠AS≠AR）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；申报类型+保护限价+五档内可成代理或日频敏感性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**best5_to_limit_honest=convert_at_protect_or_rule 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死 0.02/0.01/0.05/0.015（params.Y≠实验字母 AT；params.N≠实验字母 AT；风控补丁冻结 2026-11-02）**；**at0_primary_demo 写死 invent_best5_to_limit_as_cancel（禁双挂；风控补丁冻结 2026-11-02）** |

---

## 风控补丁两条（已写死冻结 · 2026-11-02）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AT**；**`params.N` ≠ 实验字母 AT**；禁 null / holdout 标定。  
2. **`params.at0_primary_demo`**：**写死冻结** **`invent_best5_to_limit_as_cancel`**；禁与 **`invent_best5_to_limit_far_px`** 双挂争主表（只挂一个 primary）。

---

## 变更

- 2026-11-02：风控补丁两条写死冻结——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 AT**；**params.N≠实验字母 AT**；禁 null/holdout）；② `params.at0_primary_demo=invent_best5_to_limit_as_cancel`（禁与 `invent_best5_to_limit_far_px` 双挂）。参考总管派令 / 预检有条件通过。未改 Y/Z/AA–AS 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-T；不改假设-L；不改假设-AS；不改假设-AU（若有半成品）；结论栏仍空；不开回测；不抢 A。
- 2026-11-02：新建标准件（总管线：AS 补丁已交后写下一纸面 AT；Y/Z/AA–AS 补丁已交不改；清单止于 AS → 自 `事实与坑`「最优 5 档转限」+ AS「转限价另桶」交接选题，**与 A/H/X/E/M/O/R/Q/N/S/T/L/AS/AC–AR 硬分列**；**双字母 AT ≠ 单字母 A ≠ 单字母 T**；**不与 AN–AS 重复**；**明确避开预检T旧题（证管费误抽）**；结论栏空；不开回测；不抢 A；**勿再改 AS**）。
