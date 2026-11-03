# 假设 AW · 收盘集合失败假抄前收或假末笔（执行鸿沟）

更新：2026-11-03  
来源：总管线 / AV 补丁已收、写下一纸面 AW；清单原止于 AV，无 AW 节 → 自立实验 AW；选题自 `事实与坑`「收盘价默认由收盘集合竞价产生；产生不了则以当日最后一笔前一分钟成交量加权（含最后一笔）；当日无成交以前收盘为收盘价」公开规则；与假设 A（板上可成交/枯竭）/ H（退市整理）/ X（主板 ST）/ E（整手）/ M（盘后）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ N（收盘机制切日与假 GTC）/ S（经手费）/ T（证管费；**避开预检T旧题**）/ U（过户费）/ V（印花税 PIT）/ W（除权日复权价误判板）/ L（市价通道）/ AS–AV（剩撤假留/五档转限/本方对手最优空簿/集合撮合三原则）/ AN–AO（开盘/收盘集合**剩单**假即时成）/ AK（集合时段假连续）/ Y（集合量计入日线分母）/ D（开/收时点与停牌假可交易）/ AH（不可撤窗假撤改）/ AI（无板日集合有效申报范围）/ AC–AR（北交所/50万/假T+0/单笔上限/超板无效/…/板上假队首）/ I（价格笼子）/ F（涨跌停价取整）/ G（无板日误套默认板）/ J（无板日临停）/ K（融券空头名单）/ AA（分钟 bar 时区）/ P（指数停牌假成交权重）/ AB（融券卖出价限）**分列**；**新建实验 AW**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-03）**（结论栏空；禁止把「收盘集合失败 → 抄前收盘 / 末笔价」当诚实收盘价产生链；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AV 及其他 A/D–AV 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-W；不改假设-N；不改假设-AV；勿再改 AV**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AV，本页自立实验 AW 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **收盘集合竞价未能产生成交价时**，收盘价是否按**最后一分钟成交量加权（含末笔）**诚实回落，还是发明**前收盘 / 末笔价 / 开盘价**冒充。双字母 **AW ≠ 单字母 A**。与假设 **W（除权日复权价误判板）** **硬分列**：W = 用复权价/自造除权参考价误标涨跌停；本页 = **收盘价产生失败回落链**，不主测除权判板。双字母 **AW ≠ 单字母 W**。与假设 **N（收盘机制切日与假 GTC）** **硬分列**：N = 「何时开始用 14:57 收盘集合」的 PIT 切日 + 限价假 GTC；本页 = 在**已承认当日走收盘集合**前提下，**集合失败后的回落价**是否诚实；不重开切日/GTC 主病。与假设 **AV（集合撮合最大量原则误设）** **硬分列**：AV = 集合**撮合本身**三原则是否被中间价/前收盘替换；本页 = 集合**未能产生价**后的回落链；不重开三原则主病。与假设 **AO（收盘集合剩单假即时成）** **硬分列**：AO = 集合**结束后剩单**是否假即时成进连续/盘后；本页 = **收盘价字段**怎么定，不重开剩单假即时成。与假设 **D（开/收时点与停牌）** **硬分列**：D = 次日开 vs 次日收、停牌日假可交易；本页 = 收盘价**产生失败回落**口径，消费 D 的「无成交≠可交易」但不重开开/收主对照。与假设 **Y（集合量分母）** **分列**：Y = 日线成交量分母是否含集合量；本页 = 收盘价失败回落。**明确避开预检T旧题（证管费误抽）**。与假设 AS–AV **硬分列**：不重开剩撤/五档转限/空簿假成/撮合三原则。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AW** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）。全文凡写「实验 AW / 假设-AW / hypothesis_id=AW / 组 AW0·AW1·AW2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 AW 混读或互改。亦**禁止**把实验字母 AW 与单字母实验 **A**、单字母实验 **W**、双字母实验 **AV**、双字母实验 **AO/N**、或 params 键名 `aw0_*` 以外的实验页混读。**双字母 AW ≠ 单字母 A ≠ 单字母 W ≠ 双字母 AV**；**params.Y ≠ 实验字母 AW**；**params.N ≠ 实验字母 AW**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，把「收盘集合竞价未能产生成交价、但当日连续竞价已有成交」的收盘价按**前收盘**或**末笔价**发明（跳过「最后一分钟成交量加权含末笔」），相对「收盘集合产生则用集合价；产生不了则 last_1min_vwap（含末笔）；仅全日无成交才抄前收盘；缺分钟成交 skip/敏感性档」的 PIT 诚实组，会**系统性错标收盘价与尾盘可成交名义/冲击**；差异应**集中在收盘集合失败回落误设桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假回落贡献差、可成交名义差、冲击差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在集合失败回落相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 收盘集合失败回落 ≠ 收盘机制切日；≠ 集合三原则；≠ 集合剩单假即时成；≠ 除权判板；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-03）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AW；≠ 实验字母 A；≠ 实验字母 W
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 AW
# params.asof_check_date                 写死默认 2026-10-19
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.close_fail_honest               写死 call_then_last1min_vwap_else_prev
# params.close_mech_pit_handoff          写死 n_page
# params.call_match_principle_handoff    写死 av_page
# params.close_call_leftover_handoff     写死 ao_page
# params.exright_tag_handoff             写死 w_page
# params.open_vs_close_handoff           写死 d_page
# params.aw0_primary_demo                写死 invent_close_fail_as_prev_close  # 风控补丁冻结；主报：集合失败假抄前收；禁与 invent_close_fail_as_last_tick 双挂
# params.aw0_invent_prev_on_fail         写死 True
# params.aw1_last_tick_only              写死 True
# params.aw2_close_fail_policy           写死 call_then_last1min_vwap_else_prev
# params.merge_with_A_fill               写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_AV_call_match        写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AU_own_opp_best      写死 False
# params.merge_with_AS_ioc_fok           写死 False
# params.merge_with_AT_best5_to_limit    写死 False
# params.merge_with_AR_queue             写死 False
# params.merge_with_AQ_halt_cage         写死 False
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
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_K_short_list         写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_P_index_halt         写死 False
# params.merge_with_AB_short_px          写死 False
# params.universe_rule                   写死 sse_szse_common_stock_close_fail_check
# params.missing_minbar_policy           写死 skip
# params.day_freq_proxy                  写死 close_fail_fallback_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y=相对门槛键 ≠ 实验字母 AW；params.N≠实验字母 AW；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-19"
px_basis = "unadj"
tick = 0.01
close_fail_honest = "call_then_last1min_vwap_else_prev"
close_mech_pit_handoff = "n_page"
call_match_principle_handoff = "av_page"
close_call_leftover_handoff = "ao_page"
exright_tag_handoff = "w_page"
open_vs_close_handoff = "d_page"
aw0_primary_demo = "invent_close_fail_as_prev_close"  # 风控补丁冻结；禁双挂
aw0_invent_prev_on_fail = True
aw1_last_tick_only = True
aw2_close_fail_policy = "call_then_last1min_vwap_else_prev"
universe_rule = "sse_szse_common_stock_close_fail_check"
missing_minbar_policy = "skip"
day_freq_proxy = "close_fail_fallback_sensitivity"

# 拉数前已冻结（风控补丁 2026-11-03）；禁 holdout / 事后改口 / 禁跑后改 aw0_primary_demo
Y = 0.02   # 风控补丁冻结；相对门槛 ≠ 实验字母 AW
G = 0.01
N = 0.05   # 风控补丁冻结；失败率门槛键 params.N ≠ 实验字母 AW
Y2 = 0.015

def invent_close_px(group, call_clear_px, last1min_vwap, last_tick, prev_close, had_day_trades):
    """
    AW0：按 aw0_primary_demo 单一主报（写死 invent_close_fail_as_prev_close）
    AW1：仅末笔价冒充失败回落（非主报前收）
    AW2：call_then_last1min_vwap_else_prev；缺分钟成交 → skip（或日频敏感性档）
    """
    if call_clear_px is not None:
        return ("honest_call", call_clear_px)
    if group == "AW0" and aw0_primary_demo == "invent_close_fail_as_prev_close":
        if prev_close is None:
            return "skip_or_day_freq_proxy"
        return ("fake_prev_on_fail", prev_close)
    if group == "AW1" and aw1_last_tick_only:
        if last_tick is None:
            return "skip_or_day_freq_proxy"
        return ("fake_last_tick", last_tick)
    if not had_day_trades:
        if prev_close is None:
            return "skip_or_day_freq_proxy"
        return ("honest_prev_no_trades", prev_close)
    if last1min_vwap is None:
        return "skip_or_day_freq_proxy"
    return ("honest_last1min_vwap", last1min_vwap)
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺分钟成交却硬记前收/末笔为集合失败回落、把「全日无成交才抄前收」与「集合失败但当日有成交」混为一谈、把 N 切日/假GTC / AV 三原则 / AO 剩单假即时成 / W 除权判板 / A 板上枯竭 / D 开收主对照 / T 证管费混进本页主表、日频无代理声明却假装 last1min_vwap 精确复盘 → **跳过该日该券该腿**，不静默记假路径。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AW）

| 组 | 收盘集合失败回落 | 说明 |
|----|------------------|------|
| AW0 天真 | 集合失败假抄前收（按 `aw0_primary_demo` 单一主报） | 发明假回落路径（错标/扭曲名义与冲击） |
| AW1 半泄露/混口径 | 仅末笔价冒充失败回落 | 混口径假路径（跳过 VWAP） |
| AW2 PIT 诚实 | call → last1min_vwap → 仅全日无成交才 prev_close；缺分钟 skip/敏感性 | 与公开规则同向 |

同一信号、同一沪深普通 A 股宇宙。本页**主测收盘集合失败后的回落链是否被前收/末笔替换**，不主测收盘机制切日与假 GTC（见 N）、不主测集合撮合三原则（见 AV）、不主测集合结束后剩单假即时成（见 AO）、不主测除权判板（见 W）、不主测板上枯竭门槛（见 A）、不主测开/收主对照与停牌假可交易（见 D）、不主测证管费（见 T）。**`params.fill_time=next_open` 写死**。

**全部 `merge_with_*=False`（写死；含 A/W/N/AV/AO/AN/AK/Y/D/T/V/M/AP/AU/AS/AT/AR/AQ/AL/AM/AJ/AH/AI/AG/AF/E/I/F/L/H/X/O/Q/R/S/U/AC/AD/AE/G/J/K/AA/P/AB）**。

**风控补丁两条已冻结（2026-11-03；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 写死冻结；可成交名义/冲击差显著门槛；≠实验字母 AW
params.G                            = 0.01                      # 写死冻结；假回落桶相对对照差
params.N                            = 0.05                      # 写死冻结；失败/废单率差门槛；≠实验字母 AW
params.Y2                           = 0.015                     # 写死冻结；AW1（末笔冒充）相对 AW2 专项门槛
params.aw0_primary_demo             = invent_close_fail_as_prev_close  # 写死冻结主报：集合失败假抄前收；禁与 invent_close_fail_as_last_tick 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股（`universe_rule=sse_szse_common_stock_close_fail_check`）。ETF、可转债、北交所不进主宇宙（ETF/转债收盘产生方式另见 N/Q 分列诊断，不并进主表）。  
- **排除（默认）**：缺分钟成交且未声明日频代理；把 A/W/N/AV/AO/D/T 主结论并进本页主表；日频无代理声明却假装 last1min_vwap 精确复盘；把证管费误抽并进主病（交 T；**避开预检T**）；把除权判板并进主病（交 W）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：收盘集合失败回落按成交日当时交易规则文本；收盘集合 **14:57–15:00**（Asia/Shanghai；与事实与坑同向）；「何时开始用收盘集合」切日**交 N，本页不重开**；**禁止**用核对日「凡集合失败皆抄前收」或「凡集合失败皆末笔」铺满。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `aw0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AW0 − AW2**：集合失败假抄前收相对诚实回落——假回落 / 名义与冲击错标。  
2. **AW1 − AW2**：仅末笔冒充相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_close_fail_as_prev_close",
  "invent_close_fail_as_last_tick",
  "honest_call_then_last1min_vwap_else_prev",
  "call_fail_but_had_day_trades",
  "no_trades_all_day_prev_ok",
  "board_day_close_path",
  "vs_A_fill",
  "vs_W_exright",
  "vs_N_close_gtc",
  "vs_AV_call_match",
  "vs_AO_close_leftover",
  "vs_D_open_close",
  "vs_Y_call_volume",
  "vs_T_csrc_fee",
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AW0/AW1 相对 AW2）；  
2. 假回落腿贡献差 ΔFakeFallback；  
3. 废单/失败率差 ΔFail；  
4. （可选）冲击差 ΔImpact（声明为代理，不冒充 last1min_vwap 精确复盘）。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeFallback 桶贡献| **≥ params.G** 或 |ΔNotional_(AW1−AW2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「收盘集合失败回落执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结；与实验字母 AW 无关；风控补丁 2026-11-03）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AW） | **写死冻结** `0.02`（风控补丁 2026-11-03） |
| params.G | 假回落桶相对对照差 | **写死冻结** `0.01`（风控补丁 2026-11-03） |
| params.N | 失败/废单率差门槛（≠实验字母 AW） | **写死冻结** `0.05`（风控补丁 2026-11-03） |
| params.Y2 | AW1−AW2 专项门槛 | **写死冻结** `0.015`（风控补丁 2026-11-03） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-19` |
| fill_time | 成交时点 | **写死** `next_open` |
| aw0_primary_demo | 天真主报枚举 | **写死冻结** `invent_close_fail_as_prev_close`（禁双挂；风控补丁 2026-11-03） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 call_then_last1min_vwap_else_prev；禁与 A/W/N/AV/AO/D/T 混主结论）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实 last1min_vwap 回落」与「假抄前收/末笔」，或日频无法做敏感性档且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把收盘机制切日/假 GTC（N）、集合撮合三原则（AV）、收盘集合剩单假即时成（AO）、除权判板（W）、板上枯竭（A）、开/收主对照与停牌假可交易（D）、证管费（T）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「收盘集合失败回落误设」写成「板上能否按板上价成交」为主病而不声明另页 A → 与 A 撞题，设计失效。  
4. 把「收盘集合失败回落误设」写成「除权日复权价误判板」而不声明另页 W → 与 W 撞题，设计失效。  
5. 把「收盘集合失败回落误设」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
6. 把「收盘集合失败回落误设」写成「收盘机制切日/假 GTC」而不声明另页 N → 与 N 撞题，设计失效。  
7. 把「收盘集合失败回落误设」写成「集合撮合三原则被中间价替换」而不声明另页 AV → 与 AV 撞题，设计失效。  
8. 把「收盘集合失败回落误设」写成「集合结束后剩单假即时成」而不声明另页 AO → 与 AO 撞题，设计失效。  
9. holdout 反调 `aw0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算冲击或收盘价 → 标签与执行双错，结论无效。  
11. 把实验字母 AW 与单字母 A 或单字母 W 或双字母 AV 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 收盘集合标记与会话钟（Asia/Shanghai）；  
- 收盘集合是否产生成交价（或诚实集合收盘价字段）；  
- 当日是否有连续竞价成交；最后一分钟成交量加权代理或日频 `close_fail_fallback_sensitivity`；  
- 末笔价、前收盘；  
- 交易日历；可选板上日标签（消费 A，不重开）。

可选：分钟 bar / 逐笔（精确复盘 last1min_vwap；须声明与 AA 分列）；收盘机制切日标签（消费 N，不重开）。

**禁止**：用核对日「凡集合失败皆抄前收」或「凡集合失败皆末笔」铺满历史；用复权价；把 ETF/转债/北交所混进主宇宙却不标注；把 N 的切日/假GTC 或 AV 的三原则或 AO 的剩单假即时成或 W 的除权判板或 A 的板上枯竭或 D 的开收主对照或 T 的证管费当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AW`  
- **组**：AW0 / AW1 / AW2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-19`；`close_fail_honest=call_then_last1min_vwap_else_prev`；`close_mech_pit_handoff=n_page`；`call_match_principle_handoff=av_page`；`close_call_leftover_handoff=ao_page`；`exright_tag_handoff=w_page`；`open_vs_close_handoff=d_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_close_fail_check`；`missing_minbar_policy=skip`；`day_freq_proxy=close_fail_fallback_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 AW；**params.N≠实验字母 AW**；禁 null/holdout；风控补丁冻结 2026-11-03）；**`params.aw0_primary_demo` 写死 `invent_close_fail_as_prev_close`**（禁与 invent_close_fail_as_last_tick 双挂；风控补丁冻结 2026-11-03）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AW0/AW1/AW2 可成交名义/路径质量、ΔFakeFallback、ΔFail；分桶（假抄前收 / 假末笔 / 集合失败但有成交 / 全日无成交 / 板上日 / vs A·W·N·AV·AO·D·Y·T）。  
- 自检布尔：AW2 是否 call_then_last1min_vwap_else_prev；AW0 是否单一主报；AW1 是否仅末笔冒充；是否未与 A/W/N/AV/AO/D/T 混主结论；holdout 是否未反调；**是否未把实验字母 AW 与 A 或 W 或 AV 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AV 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-W / 假设-N / 假设-AV**；**是否未再改 AV**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把前收/末笔冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AV 及其他 A/D–AV 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-W**；**不改假设-N**；**不改假设-AV**；**勿再改 AV**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：收盘价默认由收盘集合竞价产生；产生不了则以当日最后一笔前一分钟成交量加权（含末笔）；当日无成交才以前收盘为收盘价。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AV，本页**新增实验 AW** 收成标准件，**不改口径主线**，**不改假设 A–AV 正文**。与实验 A/W/N/AV/AO/D/T 分工：**A=板上枯竭门槛；W=除权判板；N=收盘切日+假GTC；AV=集合撮合三原则；AO=收盘集合剩单假即时成；D=开/收时点与停牌假可交易；T=证管费（避开）；AW=收盘集合失败假抄前收或假末笔（AW≠A≠W≠N≠AV≠AO≠D≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；分钟成交代理或日频敏感性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-19；**fill_time=next_open 写死**；**close_fail_honest=call_then_last1min_vwap_else_prev 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死 0.02/0.01/0.05/0.015（params.Y≠实验字母 AW；params.N≠实验字母 AW；风控补丁冻结 2026-11-03）**；**aw0_primary_demo 写死 invent_close_fail_as_prev_close（禁双挂；风控补丁冻结 2026-11-03）** |

---

## 风控补丁两条（已写死冻结 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 AW**；**`params.N` ≠ 实验字母 AW**；禁 null / holdout 标定。  
2. **`params.aw0_primary_demo`**：**写死冻结** **`invent_close_fail_as_prev_close`**；禁与 **`invent_close_fail_as_last_tick`** 双挂争主表（只挂一个 primary）。

---

## 变更

- 2026-11-03：风控补丁两条写死冻结——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 AW**；**params.N≠实验字母 AW**；禁 null/holdout）；② `params.aw0_primary_demo=invent_close_fail_as_prev_close`（禁与 `invent_close_fail_as_last_tick` 双挂）。参考总管派令 / `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设AW-20261103.md` 有条件通过。未改 Y/Z/AA–AV 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-W；不改假设-N；不改假设-AV；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建标准件（总管线：AV 补丁已收后写下一纸面 AW；Y/Z/AA–AV 补丁/正文已交不改；清单止于 AV → 自 `事实与坑`「收盘集合失败 → last1min_vwap；全日无成交才抄前收」选题，**与 A/H/X/E/M/O/R/Q/N/S/T/U/V/W/L/AS–AV/AN–AO/AK/Y/D/AH/AI/AC–AR 硬分列**；**双字母 AW ≠ 单字母 A ≠ 单字母 W**；**不与 AN–AV 重复**；**明确避开预检T旧题（证管费误抽）**；结论栏空；不开回测；不抢 A；**勿再改 AV**）。
