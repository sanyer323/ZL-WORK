# 假设 AV · 集合撮合最大量原则误设（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AU 补丁已收、写下一纸面 AV；清单原止于 AU，无 AV 节 → 自立实验 AV；选题自 `事实与坑`「开盘价/收盘价来自集合竞价」+ 沪深竞价撮合三原则（最大成交量 / 最低剩余 / 市场压力）公开规则；与假设 A（板上可成交/枯竭）/ H（退市整理）/ X（主板 ST）/ E（整手）/ M（盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ N（收盘机制与假 GTC）/ S（经手费）/ T（证管费；**避开预检T旧题**）/ U（过户费）/ V（印花税 PIT）/ L（市价通道）/ AS–AU（剩撤假留/五档转限/本方对手最优空簿）/ AN–AO（开盘/收盘集合**剩单**假即时成）/ AK（集合时段假连续撮合）/ Y（集合量计入日线分母）/ AH（不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AC–AR（北交所/50万/假T+0/单笔上限/超板无效/…/板上假队首）/ I（价格笼子）/ F（涨跌停价取整）/ G（无板日误套默认板）/ J（无板日临停）/ D（成交时点与停牌）/ K（融券空头名单）/ AA（分钟 bar 时区）/ P（指数停牌假成交权重）/ AB（融券卖出价限）**分列**；**新建实验 AV**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把集合竞价撮合价/量按中间价或前收盘发明；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AU 及其他 A/D–AU 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-V；不改假设-AU；勿再改 AU**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AU，本页自立实验 AV 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **开盘/收盘集合竞价撮合原则**是否按**最大成交量原则 + 最低剩余原则 + 市场压力原则**诚实确定成交价与成交量，还是发明**中间价/前收盘价/最新价**当集合成交。双字母 **AV ≠ 单字母 A**。与假设 **V（印花税 PIT 误切）** **硬分列**：V = 成本侧印花税时点；本页 = **集合撮合原则**，不主测任何费率。双字母 **AV ≠ 单字母 V**。与假设 **AN / AO（开盘/收盘集合剩单假即时成）** **硬分列**：AN/AO = 集合**结束后剩单**是否假即时成进连续；本页 = 集合**撮合本身**的价量原则是否诚实；不重开剩单假即时成主病。与假设 **AK（集合时段假连续撮合）** **硬分列**：AK = 集合窗内误套连续撮合引擎；本页 = 仍承认集合引擎，但**撮合三原则**被中间价/前收盘替换。与假设 **Y（集合量计入日线）** **分列**：Y = 日线成交量分母是否含集合量；本页 = 集合撮合价/量怎么定，不重开分母口径。与假设 **AH（不可撤窗假撤改）** **分列**：AH = 不可撤窗内假撤/假改；本页不测撤改窗。**明确避开预检T旧题（证管费误抽）**。与假设 AS–AU **硬分列**：不重开剩撤/五档转限/本方对手最优空簿。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AV** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AV / 假设-AV / hypothesis_id=AV / 组 AV0·AV1·AV2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AV 混读或互改。亦**禁止**把实验字母 AV 与单字母实验 **A**、单字母实验 **V**、双字母实验 **AU**、双字母实验 **AN/AO/AK**、或 params 键名 `av0_*` 以外的实验页混读。**双字母 AV ≠ 单字母 A ≠ 单字母 V ≠ 双字母 AU**；**params.Y ≠ 实验字母 AV**；**params.N ≠ 实验字母 AV**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，把开盘集合或收盘集合的成交价/成交量按**买卖中间价、前收盘价或最新价**发明（忽略最大成交量原则、最低剩余原则、市场压力原则），相对「按公开撮合三原则确定集合成交价与可成交量；缺簿侧深度则 skip/敏感性档，禁止静默用中间价/前收盘冒充集合价」的 PIT 诚实组，会**系统性错标集合成交价与可成交量，并扭曲板上日可成交名义与冲击**；差异应**集中在集合撮合原则误设桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假撮合贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在集合撮合原则相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 集合撮合最大量原则误设 ≠ 集合剩单假即时成；≠ 集合时段假连续；≠ 集合量分母；≠ 印花税；≠ 板上枯竭门槛

```
# 配置写死键（见 §7；params.Y/G/N/Y2 与 av0_primary_demo **待预检**）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AV；≠ 实验字母 A；≠ 实验字母 V
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AV
# params.asof_check_date                 写死默认 2026-10-02
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.call_match_honest               写死 max_vol_min_residual_pressure
# params.open_call_handoff               写死 an_page
# params.close_call_handoff              写死 ao_page
# params.call_as_continuous_handoff      写死 ak_page
# params.call_volume_denom_handoff       写死 y_page
# params.av0_primary_demo                待预检建议 invent_call_match_as_mid
# params.av0_invent_mid_clear            写死 True
# params.av1_prev_close_only             写死 True
# params.av2_call_match_policy           写死 max_vol_min_residual_pressure
# params.merge_with_A_fill               写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AU_own_opp_best      写死 False
# params.merge_with_AS_ioc_fok           写死 False
# params.merge_with_AT_best5_to_limit    写死 False
# params.merge_with_AR_queue             写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AQ_halt_cage         写死 False
# params.merge_with_AL_session_gap       写死 False
# params.merge_with_AM_halt              写死 False
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_P_index_halt         写死 False
# params.merge_with_AB_short_px          写死 False
# params.universe_rule                   写死 sse_szse_common_stock_call_match_check
# params.missing_book_depth_policy       写死 skip
# params.day_freq_proxy                  写死 call_match_principle_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  待预检建议 0.02/0.01/0.05/0.015
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-02"
px_basis = "unadj"
tick = 0.01
call_match_honest = "max_vol_min_residual_pressure"
open_call_handoff = "an_page"
close_call_handoff = "ao_page"
call_as_continuous_handoff = "ak_page"
call_volume_denom_handoff = "y_page"
av0_primary_demo = "invent_call_match_as_mid"  # 待预检；禁双挂
av0_invent_mid_clear = True
av1_prev_close_only = True
av2_call_match_policy = "max_vol_min_residual_pressure"
universe_rule = "sse_szse_common_stock_call_match_check"
missing_book_depth_policy = "skip"
day_freq_proxy = "call_match_principle_sensitivity"

Y = 0.02   # 待预检建议；相对门槛 ≠ 实验字母 AV
G = 0.01
N = 0.05   # 待预检建议；params.N ≠ 实验字母 AV
Y2 = 0.015

def invent_clear_px(group, bid, ask, prev_close, last_px, honest_clear_px):
    """
    AV0：按 av0_primary_demo 单一主报（建议 invent_call_match_as_mid）
    AV1：仅前收盘冒充集合价（非主报中间价）
    AV2：max_vol_min_residual_pressure；缺簿侧深度 → skip（或日频敏感性档）
    """
    if group == "AV0" and av0_primary_demo == "invent_call_match_as_mid":
        if bid is None or ask is None:
            return "skip_or_day_freq_proxy"
        return ("fake_mid", (bid + ask) / 2.0)
    if group == "AV1" and av1_prev_close_only:
        if prev_close is None:
            return "skip_or_day_freq_proxy"
        return ("fake_prev_close", prev_close)
    if honest_clear_px is None:
        return "skip_or_day_freq_proxy"
    return ("honest_clear", honest_clear_px)
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺集合簿侧深度却硬记中间价/前收盘集合价、把 AN/AO 剩单假即时成 / AK 集合假连续 / Y 集合量分母 / A 板上枯竭 / V 印花税 / T 证管费 / AU 空簿假成混进本页主表、日频无代理声明却假装三原则精确复盘、诚实组仍用中间价/前收盘冒充集合价 → **跳过该日该券该腿**，不静默记假路径。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AV）

| 组 | 集合撮合价/量 | 说明 |
|----|---------------|------|
| AV0 天真 | 中间价冒充集合价（按 `av0_primary_demo` 单一主报） | 发明假撮合路径（错标/高估或低估名义与冲击） |
| AV1 半泄露/混口径 | 仅前收盘冒充集合价 | 混口径假路径 |
| AV2 PIT 诚实 | max_vol_min_residual_pressure；缺深度 skip/敏感性 | 与公开撮合三原则同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测集合撮合三原则是否被中间价/前收盘替换**，不主测集合结束后剩单假即时成（见 AN/AO）、不主测集合窗假连续引擎（见 AK）、不主测集合量是否进日线分母（见 Y）、不主测板上枯竭门槛（见 A）、不主测印花税/证管费（见 V/T）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/V/T/AN/AO/AK/Y/AH/AI/AU/AS/AT/AR/AP/AQ/AL/AM/AJ/AG/AF/E/I/F/L/H/X/M/O/Q/R/S/U/AC/AD/AE/G/J/D/N/K/AA/P/AB）**。

**待预检键（纸面占位；拉数前须预检写死；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 待预检建议；≠实验字母 AV
params.G                            = 0.01                      # 待预检建议
params.N                            = 0.05                      # 待预检建议；≠实验字母 AV
params.Y2                           = 0.015                     # 待预检建议
params.av0_primary_demo             = invent_call_match_as_mid  # 待预检建议；禁与 invent_call_match_as_prev_close 双挂
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_call_match_check`）。ETF、可转债、北交所不进主宇宙。  
- **排除（默认）**：缺集合簿侧深度且未声明日频代理；把 A/V/T/AN/AO/AK/Y/AU 主结论并进本页主表；日频无代理声明却假装三原则精确复盘；把证管费误抽并进主病（交 T；**避开预检T**）；把印花税并进主病（交 V）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：集合撮合三原则按成交日当时交易规则文本；开盘集合 **9:15–9:25**、收盘集合 **14:57–15:00**（Asia/Shanghai；与事实与坑同向）；**禁止**用核对日「凡开收盘价皆中间价」或「凡开收盘价皆前收盘」铺满。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `av0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AV0 − AV2**：中间价冒充集合价相对诚实三原则——假撮合 / 名义与冲击错标。  
2. **AV1 − AV2**：仅前收盘冒充相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_call_match_as_mid",
  "invent_call_match_as_prev_close",
  "honest_max_vol_min_residual_pressure",
  "board_day_call_path",
  "open_call_bucket",
  "close_call_bucket",
  "vs_A_fill",
  "vs_V_stamp_tax",
  "vs_T_csrc_fee",
  "vs_AN_open_leftover",
  "vs_AO_close_leftover",
  "vs_AK_call_cont",
  "vs_Y_call_volume",
  "vs_AU_own_opp_best",
  "vs_AH_nocancel",
  "vs_AI_call_band",
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AV0/AV1 相对 AV2）；  
2. 假撮合腿贡献差 ΔFakeClear；  
3. 废单/失败率差 ΔFail；  
4. （可选）冲击差 ΔImpact（声明为代理，不冒充三原则精确复盘）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeClear 桶贡献| **≥ params.G** 或 |ΔNotional_(AV1−AV2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「集合撮合原则执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AV 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AV） | **待预检建议** `0.02` |
| params.G | 假撮合桶相对对照差 | **待预检建议** `0.01` |
| params.N | 失败/废单率差门槛（≠实验字母 AV） | **待预检建议** `0.05` |
| params.Y2 | AV1−AV2 专项门槛 | **待预检建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-02` |
| fill_time | 成交时点 | **写死** `next_open` |
| av0_primary_demo | 天真主报枚举 | **待预检建议** `invent_call_match_as_mid`（禁双挂） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 max_vol_min_residual_pressure；禁与 A/V/T/AN/AO/AK/Y/AU 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实三原则集合价」与「中间价/前收盘冒充」，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把开盘/收盘集合剩单假即时成（AN/AO）、集合时段假连续（AK）、集合量分母（Y）、板上枯竭（A）、印花税（V）、证管费（T）、本方对手最优空簿（AU）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「集合撮合原则误设」写成「板上能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
4. 把「集合撮合原则误设」写成「印花税 PIT」而不声明另页 V → 与 V 撞题，设计失效。  
5. 把「集合撮合原则误设」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
6. 把「集合撮合原则误设」写成「集合结束后剩单假即时成」而不声明另页 AN/AO → 与 AN/AO 撞题，设计失效。  
7. 把「集合撮合原则误设」写成「集合窗内假连续撮合」而不声明另页 AK → 与 AK 撞题，设计失效。  
8. 把「集合撮合原则误设」写成「集合量是否进日线分母」而不声明另页 Y → 与 Y 撞题，设计失效。  
9. holdout 反调 `av0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算冲击或集合价 → 标签与执行双错，结论无效。  
11. 把实验字母 AV 与单字母 A 或单字母 V 或双字母 AU 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 开盘/收盘集合标记与会话钟（Asia/Shanghai）；  
- 集合簿侧深度代理或诚实集合成交价字段（或日频 `call_match_principle_sensitivity`）；  
- 前收盘/买一卖一（用于构造天真中间价/前收盘冒充对照）；  
- 交易日历；可选板上日标签（消费 A，不重开）。

可选：逐笔/集合阶段揭示（精确复盘三原则）；分钟 bar（若做敏感性，须声明与 AA 分列）。

**禁止**：用核对日「凡开收盘价皆中间价」或「凡开收盘价皆前收盘」铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 AN/AO 的「剩单假即时成」或 AK 的「集合假连续」或 Y 的「集合量分母」或 A 的「板上枯竭」或 V/T 的费率或 AU 的「空簿假成」当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AV`  
- **组**：AV0 / AV1 / AV2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-02`；`call_match_honest=max_vol_min_residual_pressure`；`open_call_handoff=an_page`；`close_call_handoff=ao_page`；`call_as_continuous_handoff=ak_page`；`call_volume_denom_handoff=y_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_call_match_check`；`missing_book_depth_policy=skip`；`day_freq_proxy=call_match_principle_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 待预检建议 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AV；**params.N≠实验字母 AV**；禁 null/holdout）；**`params.av0_primary_demo` 待预检建议 `invent_call_match_as_mid`**（禁与 invent_call_match_as_prev_close 双挂）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AV0/AV1/AV2 可成交名义/路径质量、ΔFakeClear、ΔFail；分桶（中间价冒充 / 前收盘冒充 / 开盘·收盘集合 / 板上日 / vs A·V·T·AN·AO·AK·Y·AU）。  
- 自检布尔：AV2 是否 max_vol_min_residual_pressure；AV0 是否单一主报；AV1 是否仅前收盘冒充；是否未与 A/V/T/AN/AO/AK/Y/AU 混主结论；holdout 是否未反调；**是否未把实验字母 AV 与 A 或 V 或 AU 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AU 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-V / 假设-AU**；**是否未再改 AU**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把中间价/前收盘冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AU 及其他 A/D–AU 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-V**；**不改假设-AU**；**勿再改 AU**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：开盘价/收盘价来自集合竞价；集合撮合须服从最大成交量等公开原则，不得用中间价/前收盘静默冒充。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AU，本页**新增实验 AV** 收成标准件，**不改口径主线**，**不改假设 A–AU 正文**。与实验 A/V/AN/AO/AK/Y/AU/T 分工：**A=板上枯竭门槛；V=印花税；AN/AO=集合剩单假即时成；AK=集合假连续；Y=集合量分母；AU=本方对手最优空簿；T=证管费（避开）；AV=集合撮合最大量原则误设（AV≠A≠V≠AN≠AO≠AK≠Y≠AU≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；集合簿侧深度代理或日频敏感性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-02；**fill_time=next_open 写死**；**call_match_honest=max_vol_min_residual_pressure 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 待预检建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AV；params.N≠实验字母 AV）**；**av0_primary_demo 待预检建议 invent_call_match_as_mid（禁双挂）** |

---

## 变更

- 2026-11-02：新建标准件（总管线：AU 补丁已收后写下一纸面 AV；Y/Z/AA–AU 补丁/正文已交不改；清单止于 AU → 自 `事实与坑`「开盘/收盘集合竞价」+ 公开撮合三原则选题，**与 A/H/X/E/M/O/R/Q/N/S/T/U/V/L/AS–AU/AN–AO/AK/Y/AH/AI/AC–AR 硬分列**；**双字母 AV ≠ 单字母 A ≠ 单字母 V**；**不与 AN–AU 重复**；**明确避开预检T旧题（证管费误抽）**；结论栏空；不开回测；不抢 A；**勿再改 AU**）。
