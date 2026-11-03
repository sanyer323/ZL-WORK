# 假设 AZ · 开盘集合失败假抄前收或假理论开盘（执行鸿沟）

更新：2026-11-03  
来源：总管线 / AY 补丁已收、写下一纸面 AZ；清单撞题规则另选正交微观结构缺口（开盘集合失败回落链 ≠ 收盘失败回落）；选题自 `事实与坑`「开盘价 = 当日竞价第一笔成交，先走集合竞价，走不成再走连续竞价」公开规则；与假设 A（板上可成交/枯竭）/ H（退市整理）/ Z（融资保证金比例误铺；**实验字母 Z ≠ 本页 AZ**）/ E（整手）/ M（盘后）/ O（大宗）/ N（收盘机制切日与假 GTC）/ Q（可转债）/ R（股票 ETF 假回转）/ S/T/U/V（费用层；**避开预检T旧题**）/ W（除权判板）/ L（市价通道）/ D（开/收时点与停牌假可交易）/ AN（开盘集合**剩单**假即时成）/ AO（收盘集合剩单）/ AK（集合时段假连续）/ AV（集合撮合三原则）/ AW（**收盘**集合失败假抄前收或假末笔）/ AY（基金ETF最小价位）/ AX（ETF基金经手费）/ Y（集合量计入日线；**实验字母 Y ≠ params.Y**）/ AA–AX / AC–AV 等**分列**；**新建实验 AZ**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「开盘集合失败 → 抄前收盘 / 假理论未成交开盘价」当诚实开盘价产生链；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AY 及其他 A/D–AY 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-Z；不改假设-AW；不改假设-AN；不改假设-D；不改假设-AV；勿再改 AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 AZ。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **开盘集合竞价未能产生成交价时**，开盘价是否按**随后连续竞价第一笔**诚实回落，还是发明**前收盘 / 未成交理论集合价**冒充。**双字母 AZ ≠ 单字母 A**。与假设 **Z（融资保证金比例误铺）** **硬分列**：Z = 融资保证金/担保比例 PIT；本页 = **开盘价产生失败回落链**，不主测两融保证金。**双字母 AZ ≠ 单字母 Z**。与假设 **AW（收盘集合失败假抄前收或假末笔）** **硬分列**：AW = **收盘**集合失败 → last1min_vwap / 仅全日无成交才 prev；本页 = **开盘**集合失败 → first continuous trade；开≠收，禁止捆。与假设 **AN（开盘集合剩单假即时成）** **硬分列**：AN = 集合**结束后剩单**是否假即时成/假清空；本页 = **开盘价字段**在集合无成交时怎么定，不重开剩单假即时成。与假设 **D（开/收时点与停牌）** **硬分列**：D = 次日开 vs 次日收、停牌日假可交易；本页 = 开盘价**产生失败回落**口径，消费 D 的 open 字段定义但不重开开/收主对照。与假设 **AV（集合撮合三原则）** **硬分列**：AV = 集合**撮合本身**三原则是否被中间价/前收盘替换；本页 = 集合**未能产生价**后的开盘回落链。与假设 **AK（集合时段假连续）** **分列**：AK = 集合窗内假连续多价撮合；本页 = 集合失败后的开盘价回落。与假设 **AY/AX** **硬分列**：价位/经手费 ≠ 开盘失败回落。**明确避开预检T旧题（证管费误抽）**。与假设 AN–AY **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/基金经手费/基金 tick。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AZ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 Z**（融资保证金）。全文凡写「实验 AZ / 假设-AZ / hypothesis_id=AZ / 组 AZ0·AZ1·AZ2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AZ 混读或互改。亦**禁止**把实验字母 AZ 与单字母 **A**、单字母 **Z**、双字母 **AW**、双字母 **AN**、双字母 **AY**、或 params 键名 `az0_*` 以外的实验页混读。**双字母 AZ ≠ 单字母 A ≠ 单字母 Z ≠ 双字母 AW ≠ 双字母 AN ≠ 双字母 AY**；**params.Y ≠ 实验字母 AZ**；**params.N ≠ 实验字母 AZ**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，把「开盘集合竞价未能产生成交、但随后连续竞价已有第一笔成交」的开盘价按**前收盘**或**未成交理论集合价**发明（跳过「走不成集合则取连续竞价第一笔」），相对「开盘集合产生则用集合开盘价；产生不了则取当日连续竞价第一笔成交价；全日仍无成交则无开盘/记失败或 skip；缺分钟成交 skip/敏感性档」的 PIT 诚实组，会**系统性错标开盘价与开盘可成交名义/冲击**；差异应**集中在开盘集合失败回落误设桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假回落贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且「假抄前收 / 假理论开盘 / 集合失败但有连续首笔 / 全日无成交 / vs A·Z·AW·AN·D·AV·AK·AY·AX·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 开盘集合失败回落 ≠ 收盘失败回落；≠ 开盘剩单假即时成；≠ 开/收主对照；≠ 集合三原则；≠ 板上枯竭；≠ 融资保证金；≠ 证管费

```
# 配置写死键（见 §7；待预检建议值；拉数前冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AZ；≠ 实验字母 A；≠ 实验字母 Z
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AZ
# params.asof_check_date                 写死默认 2026-10-02  # 与事实与坑「开盘价来自集合」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.open_fail_honest                写死 call_then_first_continuous_else_skip
# params.close_fail_handoff              写死 aw_page        # 收盘失败回落交 AW；开≠收
# params.open_leftover_handoff           写死 an_page        # 开盘集合剩单交 AN
# params.call_match_principle_handoff    写死 av_page
# params.open_vs_close_handoff           写死 d_page
# params.margin_ratio_handoff            写死 z_page         # 融资保证金交 Z；AZ≠Z
# params.az0_primary_demo                建议 invent_open_fail_as_prev_close  # 主报：开盘集合失败假抄前收；禁与 invent_open_fail_as_theory_uncross 双挂争主表；AZ1半泄露不得升格并列主报
# params.az0_invent_prev_on_fail         写死 True
# params.az1_theory_uncross_only         写死 True           # 半泄露：仅假理论未成交开盘价
# params.az2_open_fail_policy            写死 call_then_first_continuous_else_skip
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin             写死 False
# params.merge_with_AW_close_fail        写死 False
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AV_call_match        写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_AY_fund_tick         写死 False
# params.merge_with_AX_fund_fee          写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_N_close_gtc          写死 False
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
# params.merge_with_L_mkt                写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AU_own_opp_best      写死 False
# params.merge_with_AS_ioc_fok           写死 False
# params.merge_with_AT_best5_to_limit    写死 False
# params.merge_with_AR_queue             写死 False
# params.merge_with_AQ_halt_cage         写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_P_index_halt         写死 False
# params.merge_with_AB_short_px          写死 False
# params.universe_rule                   写死 sse_szse_common_stock_open_fail_check
# params.missing_minbar_policy           写死 skip
# params.day_freq_proxy                  写死 open_fail_fallback_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  建议 0.02/0.01/0.05/0.015  # 待预检写死；params.Y≠实验字母AZ；params.N≠实验字母AZ；亦≠单字母实验A/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-02"
px_basis = "unadj"
tick = 0.01
open_fail_honest = "call_then_first_continuous_else_skip"
close_fail_handoff = "aw_page"
open_leftover_handoff = "an_page"
call_match_principle_handoff = "av_page"
open_vs_close_handoff = "d_page"
margin_ratio_handoff = "z_page"
az0_primary_demo = "invent_open_fail_as_prev_close"  # 待预检写死；禁双挂
az0_invent_prev_on_fail = True
az1_theory_uncross_only = True
az2_open_fail_policy = "call_then_first_continuous_else_skip"
universe_rule = "sse_szse_common_stock_open_fail_check"
missing_minbar_policy = "skip"
day_freq_proxy = "open_fail_fallback_sensitivity"

# 待预检建议（纸面占位；禁 null；禁 holdout 标定；禁跑后改口）
Y = 0.02   # 建议；相对门槛 ≠ 实验字母 AZ；≠ 单字母实验 A/Z
G = 0.01   # 建议
N = 0.05   # 建议；失败率门槛键 params.N ≠ 实验字母 AZ
Y2 = 0.015 # 建议

def invent_open_px(group, call_clear_px, first_continuous_px, theory_uncross_px, prev_close, had_post_call_trades):
    """
    AZ0：按 az0_primary_demo 单一主报（建议 invent_open_fail_as_prev_close）
    AZ1：仅假理论未成交开盘价冒充失败回落（非主报前收）
    AZ2：call_then_first_continuous_else_skip；缺分钟成交 → skip（或日频敏感性档）
    """
    if call_clear_px is not None:
        return ("honest_call_open", call_clear_px)
    if group == "AZ0" and az0_primary_demo == "invent_open_fail_as_prev_close":
        if prev_close is None:
            return "skip_or_day_freq_proxy"
        return ("fake_prev_on_open_fail", prev_close)
    if group == "AZ1" and az1_theory_uncross_only:
        if theory_uncross_px is None:
            return "skip_or_day_freq_proxy"
        return ("fake_theory_uncross", theory_uncross_px)
    if not had_post_call_trades:
        return "skip_or_no_open"  # 全日仍无成交：无诚实开盘；不静默抄前收当开盘
    if first_continuous_px is None:
        return "skip_or_day_freq_proxy"
    return ("honest_first_continuous", first_continuous_px)
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺连续首笔/分钟成交却硬记前收/理论价为开盘集合失败回落、把「全日无成交无开盘」与「集合失败但连续已有首笔」混为一谈、把 AW 收盘失败回落 / AN 开盘剩单假即时成 / AV 三原则 / D 开收主对照 / A 板上枯竭 / Z 融资保证金 / AK 集合窗假连续 / T 证管费混进本页主表、日频无代理声明却假装连续首笔精确复盘 → **跳过该日该券该腿**，不静默记假路径。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AZ）

| 组 | 开盘集合失败回落 | 说明 |
|----|------------------|------|
| AZ0 天真 | 集合失败假抄前收（按 `az0_primary_demo` 单一主报） | 发明假回落路径（错标/扭曲开盘名义与冲击） |
| AZ1 半泄露/混口径 | 仅假理论未成交开盘价冒充失败回落 | 混口径假路径（无成交却发明开盘） |
| AZ2 PIT 诚实 | call → first continuous；全日无成交则无开盘/skip；缺分钟 skip/敏感性 | 与公开规则同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测开盘集合失败后的回落链是否被前收/理论价替换**，不主测收盘失败回落（见 AW）、不主测开盘集合剩单假即时成（见 AN）、不主测集合撮合三原则（见 AV）、不主测开/收主对照与停牌假可交易（见 D）、不主测板上枯竭门槛（见 A）、不主测融资保证金（见 Z）、不主测证管费（见 T）、不主测基金 tick/经手费（见 AY/AX）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/Z/AW/AN/AO/AV/AK/D/Y/AY/AX/T/N/AL/AM/AJ/AH/AI/AG/AF/E/I/F/L/H/X/O/Q/R/S/U/V/W/M/AP/AU/AS/AT/AR/AQ/AC/AD/AE/G/J/K/AA/P/AB）**。

**待预检键建议（纸面占位；拉数前须写死冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                         # 建议；可成交名义/冲击差显著门槛；≠实验字母 AZ；≠单字母实验 A/Z
params.G                            = 0.01                         # 建议；假回落桶相对对照差
params.N                            = 0.05                         # 建议；失败/废单率差门槛；≠实验字母 AZ
params.Y2                           = 0.015                        # 建议；AZ1（假理论开盘）相对 AZ2 专项门槛
params.az0_primary_demo             = invent_open_fail_as_prev_close  # 建议主报：开盘集合失败假抄前收；禁与 invent_open_fail_as_theory_uncross 双挂争主表；AZ1半泄露不得升格并列主报
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_open_fail_check`）。ETF、可转债、北交所不进主宇宙（ETF/转债开盘产生方式另页分列诊断，不并进主表）。  
- **排除（默认）**：缺连续首笔且未声明日频代理；把 A/Z/AW/AN/AV/D/T/AY/AX 主结论并进本页主表；日频无代理声明却假装 first_continuous 精确复盘；把证管费误抽并进主病（交 T；**避开预检T**）；把收盘失败回落并进主病（交 AW）；把融资保证金并进主病（交 Z）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：开盘集合失败回落按成交日当时交易规则文本；开盘集合 **9:15–9:25**（Asia/Shanghai；与事实与坑同向）；**禁止**用核对日「凡开盘集合失败皆抄前收」或「凡失败皆用理论未成交价」铺满；**禁止**把收盘失败回落链（AW）抄到开盘侧。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `az0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AZ0 − AZ2**：开盘集合失败假抄前收相对诚实回落——假回落 / 开盘名义与冲击错标。  
2. **AZ1 − AZ2**：仅假理论开盘冒充相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_open_fail_as_prev_close",
  "invent_open_fail_as_theory_uncross",
  "honest_call_then_first_continuous",
  "call_fail_but_had_continuous_first",
  "no_trades_all_day_no_open",
  "board_day_open_path",
  "vs_A_fill",
  "vs_Z_margin",
  "vs_AW_close_fail",
  "vs_AN_open_leftover",
  "vs_D_open_close",
  "vs_AV_call_match",
  "vs_AK_call_cont",
  "vs_AY_fund_tick",
  "vs_AX_fund_fee",
  "vs_T_csrc_fee",
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AZ0/AZ1 相对 AZ2）；  
2. 假回落腿贡献差 ΔFakeFallback；  
3. 废单/失败率差 ΔFail；  
4. （可选）冲击差 ΔImpact（声明为代理，不冒充 first_continuous 精确复盘）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeFallback 桶贡献| **≥ params.G** 或 |ΔNotional_(AZ1−AZ2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「开盘集合失败回落执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AZ / 单字母实验 A/Z 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AZ；≠单字母实验 A/Z） | **建议** `0.02`（待预检写死） |
| params.G | 假回落桶相对对照差 | **建议** `0.01` |
| params.N | 失败/废单率差门槛（≠实验字母 AZ） | **建议** `0.05` |
| params.Y2 | AZ1−AZ2 专项门槛 | **建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-02` |
| fill_time | 成交时点 | **写死** `next_open` |
| az0_primary_demo | 天真主报枚举 | **建议** `invent_open_fail_as_prev_close`（禁与 invent_open_fail_as_theory_uncross 双挂；AZ1半泄露不得升格并列主报） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 call_then_first_continuous_else_skip；禁与 A/Z/AW/AN/AV/D/T 混主结论；禁荐股）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实连续首笔回落」与「假抄前收/假理论开盘」，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把收盘失败回落（AW）、开盘集合剩单假即时成（AN）、集合撮合三原则（AV）、开/收主对照与停牌假可交易（D）、板上枯竭（A）、融资保证金（Z）、证管费（T）、基金 tick（AY）、基金经手费（AX）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「开盘集合失败回落误设」写成「板上能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
4. 把「开盘集合失败回落误设」写成「融资保证金比例误铺」而不声明另页 Z → 与 Z 撞题，设计失效。  
5. 把「开盘集合失败回落误设」写成「收盘集合失败假抄前收」而不声明另页 AW → 与 AW 撞题，设计失效。  
6. 把「开盘集合失败回落误设」写成「开盘集合剩单假即时成」而不声明另页 AN → 与 AN 撞题，设计失效。  
7. 把「开盘集合失败回落误设」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
8. 把实验字母 AZ 与单字母 A 或单字母 Z 或双字母 AW/AN/AY 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
9. holdout 反调 `az0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算冲击或开盘价 → 标签与执行双错，结论无效。  
11. 把收盘失败回落链公式直接抄到开盘侧却不声明开≠收 → 与 AW 撞题/设计失效。  
12. 全日无成交却静默把前收盘当诚实开盘价（诚实组）→ 与公开规则冲突，设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 开盘集合标记与会话钟（Asia/Shanghai）；  
- 开盘集合是否产生成交价（或诚实集合开盘价字段）；  
- 开盘集合后是否有连续竞价第一笔成交价；  
- 理论集合未成交价代理（仅 AZ1 诊断；缺则 skip）；前收盘；  
- 交易日历；可选板上日标签（消费 A，不重开）。

可选：分钟 bar / 逐笔（精确复盘 first_continuous；须声明与 AA 分列）；收盘失败回落标签（消费 AW，不重开）。

**禁止**：用核对日「凡开盘集合失败皆抄前收」或「凡失败皆理论价」铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 AW 收盘失败 / AN 开盘剩单 / AV 三原则 / D 开收主对照 / A 板上 / Z 保证金 / T 证管费 / AY tick / AX 经手费当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AZ`  
- **组**：AZ0 / AZ1 / AZ2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-02`；`open_fail_honest=call_then_first_continuous_else_skip`；`close_fail_handoff=aw_page`；`open_leftover_handoff=an_page`；`call_match_principle_handoff=av_page`；`open_vs_close_handoff=d_page`；`margin_ratio_handoff=z_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_open_fail_check`；`missing_minbar_policy=skip`；`day_freq_proxy=open_fail_fallback_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 建议 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AZ；**params.N≠实验字母 AZ**；亦≠单字母实验 A/Z；禁 null/holdout；待预检写死）；**`params.az0_primary_demo` 建议 `invent_open_fail_as_prev_close`**（禁与 invent_open_fail_as_theory_uncross 双挂；AZ1半泄露不得升格并列主报；待预检写死）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AZ0/AZ1/AZ2 可成交名义/路径质量、ΔFakeFallback、ΔFail；分桶（假抄前收 / 假理论开盘 / 集合失败但有连续首笔 / 全日无成交 / 板上日 / vs A·Z·AW·AN·D·AV·AK·AY·AX·T）。  
- 自检布尔：AZ2 是否 call_then_first_continuous_else_skip；AZ0 是否单一主报；AZ1 是否仅假理论开盘；是否未与 A/Z/AW/AN/AV/D/T 混主结论；holdout 是否未反调；**是否未把实验字母 AZ 与 A 或 Z 或 AW 或 AN 或 AY 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AY 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-Z / 假设-AW / 假设-AN / 假设-D / 假设-AV**；**是否未再改 AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把前收/理论价冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AY 及其他 A/D–AY 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-Z**；**不改假设-AW**；**不改假设-AN**；**不改假设-D**；**不改假设-AV**；**勿再改 AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：开盘价 = 当日竞价第一笔成交，先走集合竞价，走不成再走连续竞价；不得把收盘侧「全日无成交才抄前收」误抄成开盘失败默认回落。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 AZ** 标准件，**不改口径主线**，**不改假设 A–AY 正文**。与实验 A/Z/AW/AN/D/AV/T 分工：**A=板上枯竭门槛；Z=融资保证金；AW=收盘集合失败回落；AN=开盘集合剩单假即时成；D=开/收时点与停牌假可交易；AV=集合撮合三原则；T=证管费（避开）；AZ=开盘集合失败假抄前收或假理论开盘（AZ≠A≠Z≠AW≠AN≠D≠AV≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；连续首笔代理或日频敏感性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-02；**fill_time=next_open 写死**；**open_fail_honest=call_then_first_continuous_else_skip 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AZ；params.N≠实验字母 AZ；亦≠单字母实验 A/Z；待预检写死）**；**az0_primary_demo 建议 invent_open_fail_as_prev_close（禁双挂；AZ1半泄露不得升格并列主报；待预检写死）** |

---

## 变更

- 2026-11-03：新建标准件（总管线：AY 补丁已收后写下一纸面 AZ；Y/Z/AA–AY 补丁/正文已交不改；清单撞题规则另选「开盘集合失败假抄前收或假理论开盘」；选题自 `事实与坑`；**与 A/H/Z/E/M/O/N/Q/R/S/T/U/V/W/L/D/AN/AO/AK/AV/AW/AY/AX/Y/AA–AX/AC–AV 硬分列**；**双字母 AZ ≠ 单字母 A ≠ 单字母 Z**；**不与 AN–AY 重复**；**明确避开预检T旧题（证管费误抽）**；**勿占 AY（基金ETF最小价位）/AX（ETF基金经手费）/AW（收盘集合失败）**；结论栏空；不开回测；不抢 A；**勿再改 AY/AX/AW**）。