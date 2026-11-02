# 假设 AI · 无涨跌幅日集合竞价有效申报范围假进簿（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AH 补丁已交后写下一纸面 AI；清单原止于 AH，无 AI 节 → 自立实验 AI；选题自 `事实与坑`「无涨跌幅日开盘集合竞价有效申报范围为前收盘 900% 以内（上交所另写不低于前收盘 50%）；临停期间与收盘集合竞价为最近成交价上下 10%；连续竞价笼子不套到这些时段；科创板不适用该 900%/50% 开盘集合范围（上交所 3.3.15 / 深交所 3.3.17；核对日 2026-10-12）」+ 口径「执行鸿沟」；与假设 A（板上可成交）/ H（退市整理）/ X（主板 ST 涨跌幅）/ E（整手）/ M（盘后补成交）/ O（大宗）/ R（股票 ETF 假回转）/ Q（可转债）/ AC（北交所）/ AD（风险警示 50 万）/ AE（普通股票假 T+0）/ AF（单笔数量上限）/ AG（超涨跌停价无效）/ AH（集合不可撤窗假撤改）/ I（连续竞价价格笼子）/ F（涨跌停价取整）/ L（市价保护限价）/ G（无板日误套板块默认板）/ J（无板日盘中临停 30%/60%）**分列**；**新建实验 AI**  
状态：**草稿 · 待数据 · 待跑 · 待风控预检**（结论栏空；禁止把「无板日开盘集合可任意远价进簿/成交」或「把连续竞价笼子套到开盘集合」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AH 及其他 A/D–AH 已交正文与冻结补丁；不改假设-H**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AH，本页自立实验 AI 标准件。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/排队能否按板上价成交；本页 = **无涨跌幅日**集合竞价（开盘/收盘）与临停集合阶段的**有效申报价格范围**是否被忽略。双字母 **AI ≠ 单字母 A**。与假设 **I（价格笼子远限价）** **硬分列**：I = **连续竞价**限价相对买卖一/基准价的 2%/十价位笼子；本页 = 无板日**集合竞价/临停集合**专用有效申报范围（开盘集合相对前收盘 900%/50%；临停与收盘集合相对最近成交 ±10%），**连续竞价笼子不套到这些时段**。双字母 **AI ≠ 单字母 I**。与假设 **J（无板日盘中临停）** **分列**：J 主测较开盘价 30%/60% 临停窗是否被当成全日连续可按极值成交；本页主测临停/复牌**集合竞价申报价**是否超出最近成交 ±10% 仍进簿，不重开 30%/60% 触发。与假设 **G（无板日误套板块默认板）** **分列**：G 主测把 ±10%/±20% 假板套到无板日；本页在已承认无板的前提下测集合有效申报范围。与假设 **AG（超涨跌停价无效）** **分列**：AG 主测有板日超涨跌停限制价拒单；本页主测无板日集合范围。与假设 **AH（不可撤窗假撤改）** **分列**：AH 主测 9:20–9:25 / 14:57–15:00 能否撤改；本页主测申报价是否在有效范围内。与假设 H/X/E/M/O/R/Q/AC/AD/AE/AF/F/L **分列**：各自主测，不并表。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AI** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AI / 假设-AI / hypothesis_id=AI / 组 AI0·AI1·AI2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AI 与单字母实验 **A**、单字母实验 **I**、或 params 键名 `ai0_*` 以外的实验页混读。**双字母 AI ≠ 单字母 A ≠ 单字母 I**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1 下，在**无涨跌幅日**把开盘集合竞价限价当成「任意远离前收盘也能进簿/成交」，或把**连续竞价价格笼子**误套到开盘集合，或忽略临停期间/收盘集合「最近成交价 ±10%」有效申报范围，相对「开盘集合：申报价须在前收盘 **900% 以内**（上交所另含不低于前收盘 **50%**）；临停期间与收盘集合：相对最近成交价 **±10%**；超范围 = 无效申报拒单；科创板不适用该 900%/50% 开盘集合范围；连续竞价笼子另页 I」的 PIT 诚实组，会**系统性发明超范围假进簿路径并高估可成交名义 / 低估废单**；差异应**集中在开盘集合超范围 / 临停·收盘集合 ±10% 被忽略 / 连续笼子误套集合桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的超范围假进簿贡献差、可成交名义差、废单率差在标定噪声带内可忽略，且分桶不改变结论（差异不集中在集合有效申报范围相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 无板日集合有效申报范围 ≠ 连续竞价笼子；≠ 盘中临停触发；≠ 有板日超板拒单

```
# 配置写死键（见 §7；待风控预检后冻结 Y/G/N/Y2 与 ai0_primary_demo）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AI；≠ 实验字母 A；≠ 实验字母 I
# params.asof_check_date                 写死默认 2026-10-12  # 事实与坑「无板日集合/临停有效申报范围」核对锚
# params.fill_time                        写死 next_open      # 主腿与 A/D 对齐；开盘集合冲击作主测；不抢 A 板上真数
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01           # A 股股票默认；禁基金主宇宙
# params.open_call_band_upper_mult       写死 9.0            # 开盘集合：前收盘 ×900% 以内（=×9）
# params.open_call_band_lower_mult_sse   写死 0.5            # 上交所：不低于前收盘 50%；深交所主测上界，下界按当时文本（缺则 skip 另桶）
# params.halt_close_call_band_pct        写死 0.10           # 临停期间与收盘集合：最近成交价 ±10%
# params.star_open_call_900_50_applies   写死 False          # 科创板不适用 3.3.15 开盘集合 900%/50%；禁抄套
# params.band_round                      写死 round_half_up_to_tick  # 与 F 同向
# params.no_limit_day_source             写死 g_pit_table    # 无板日标签复用实验 G 的 PIT；本页不重开 G 主结论
# params.ai0_primary_demo                待预检建议 invent_open_call_band_bypass  # 主报：开盘集合超范围仍进簿/成交；禁与 misapply_continuous_cage_to_call 双挂争主表
# params.ai0_invent_open_call_band_bypass 写死 True
# params.ai0_invent_halt_close_band_bypass 写死 False        # 诊断可叠；主报以 ai0_primary_demo 为准
# params.ai1_misapply_continuous_cage_to_call 写死 True      # 半泄露：把连续竞价 2% 笼子套到开盘集合
# params.ai1_ignore_halt_close_10pct     写死 True           # AI1 可同向诊断：临停/收盘集合忽略 ±10%
# params.ai2_open_call_band_policy       写死 reject_outside_band
# params.ai2_halt_close_call_band_policy 写死 reject_outside_band
# params.merge_with_A_fill               写死 False          # 板上枯竭另页 A（AI≠A）
# params.merge_with_I_cage               写死 False          # 连续竞价笼子另页 I（AI≠I）
# params.merge_with_J_halt               写死 False          # 无板日 30%/60% 临停触发另页 J
# params.merge_with_G_nolimit_pct        写死 False          # 无板日误套板块默认板另页 G
# params.merge_with_AG_beyond_limit      写死 False          # 有板日超涨跌停价另页 AG
# params.merge_with_AH_nocancel          写死 False          # 不可撤窗另页 AH
# params.merge_with_F_round              写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_Q_cb_rotation        写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.universe_rule                   写死 sse_szse_common_stock_nolimit_days  # 主宇宙=沪深普通 A 股无涨跌幅日样本；ETF/转债/北交所不进主宇宙
# params.missing_preclose_policy         写死 skip           # 缺前收/最近成交 → skip（禁静默当可挂）
# params.day_freq_proxy                  写死 open_call_band_sensitivity  # 日频无 L2 时只报「开盘集合超范围」敏感性档；禁假装精确复盘簿
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  待预检建议 0.02/0.01/0.05/0.015  # params.Y=相对门槛键 ≠ 实验字母 AI；禁 null/holdout
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-12"
px_basis = "unadj"
tick = 0.01
open_call_band_upper_mult = 9.0
open_call_band_lower_mult_sse = 0.5
halt_close_call_band_pct = 0.10
star_open_call_900_50_applies = False
band_round = "round_half_up_to_tick"
no_limit_day_source = "g_pit_table"
ai0_primary_demo = "invent_open_call_band_bypass"  # 待预检；禁双挂
ai0_invent_open_call_band_bypass = True
ai0_invent_halt_close_band_bypass = False
ai1_misapply_continuous_cage_to_call = True
ai1_ignore_halt_close_10pct = True
ai2_open_call_band_policy = "reject_outside_band"
ai2_halt_close_call_band_policy = "reject_outside_band"
universe_rule = "sse_szse_common_stock_nolimit_days"
missing_preclose_policy = "skip"
day_freq_proxy = "open_call_band_sensitivity"

# 待预检建议值（拉数前须冻结；禁 holdout / 事后改口 / 禁跑后改 ai0_primary_demo）
Y = 0.02   # 相对门槛 ≠ 实验字母 AI
G = 0.01
N = 0.05
Y2 = 0.015

def round_to_tick(x, tick=0.01):
    from math import floor
    return floor(x / tick + 0.5) * tick

def open_call_band(preclose, exch, board):
    """无板日开盘集合有效申报范围。科创板不适用 900%/50%。"""
    if board == "STAR" and not star_open_call_900_50_applies:
        return None, None, "star_exempt_open_call_band"
    upper = round_to_tick(preclose * open_call_band_upper_mult, tick)
    lower = None
    if exch in ("SSE", "SH"):
        lower = round_to_tick(preclose * open_call_band_lower_mult_sse, tick)
    # 深交所：事实与坑写明上界 900%；下界若未核到同款 50% → 另桶/ skip，禁默填
    return lower, upper, "ok"

def halt_or_close_call_band(last_trade):
    """临停期间或收盘集合：最近成交价 ±10%。"""
    lo = round_to_tick(last_trade * (1.0 - halt_close_call_band_pct), tick)
    hi = round_to_tick(last_trade * (1.0 + halt_close_call_band_pct), tick)
    return lo, hi

def apply_call_band(order_px, session, preclose, last_trade, exch, board, group):
    """
    session in {open_call, halt_call, close_call}
    AI0：开盘集合超范围仍进簿（按 ai0_primary_demo）
    AI1：把连续竞价笼子误套到开盘集合 / 或忽略临停·收盘 ±10%
    AI2：超范围 reject
    """
    if session == "open_call":
        lo, hi, tag = open_call_band(preclose, exch, board)
        if tag == "star_exempt_open_call_band":
            return "star_exempt_skip_or_other_rule", order_px
        if group == "AI0" and ai0_invent_open_call_band_bypass:
            return "invent_open_call_ok", order_px
        if group == "AI1" and ai1_misapply_continuous_cage_to_call:
            # 误用 2% 连续笼子当开盘集合闸门（泄露/混口径）
            return "misapplied_cage_as_open_call_gate", order_px
        if hi is not None and order_px > hi:
            return "reject_above_open_call_band", None
        if lo is not None and order_px < lo:
            return "reject_below_open_call_band", None
        return "ok_open_call", order_px
    # halt_call / close_call
    lo, hi = halt_or_close_call_band(last_trade)
    if group == "AI0" and ai0_invent_halt_close_band_bypass:
        return "invent_halt_close_ok", order_px
    if group == "AI1" and ai1_ignore_halt_close_10pct:
        return "ignore_halt_close_band", order_px
    if order_px > hi or order_px < lo:
        return "reject_outside_halt_close_band", None
    return "ok_halt_close_call", order_px
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺前收/最近成交/无板日标签却硬判可挂、把 I 连续笼子 / J 临停触发 / G 假板 / AG 有板超板 / A 板上枯竭混进本页主表、日频无代理声明却假装 L2 复盘簿内超范围成交、诚实组超范围仍静默成功、科创板误套 900%/50% 进主表 → **跳过该日该券该腿**，不静默记超范围成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AI）

| 组 | 集合有效申报范围 | 说明 |
|----|------------------|------|
| AI0 天真 | 开盘集合超 900%/50% 仍进簿/成交（按 `ai0_primary_demo` 单一主报） | 发明超范围路径 |
| AI1 半泄露/混口径 | 把连续竞价笼子误套到开盘集合；并可诊断忽略临停/收盘集合 ±10% | 混口径假路径 |
| AI2 PIT 诚实 | 开盘集合拒超范围；临停/收盘集合拒超 ±10%；科创板不开 900%/50% 主测 | 与事实与坑同向 |

同一信号、同一无涨跌幅日沪深普通 A 股宇宙。本页**主测无板日集合竞价有效申报范围执行诚信**，不主测连续竞价笼子（见 I）、不主测 30%/60% 临停触发（见 J）、不主测有板超涨跌停（见 AG）、不主测板上枯竭（见 A）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_A_fill=False` / `merge_with_I_cage=False` / `merge_with_J_halt=False` / `merge_with_G_nolimit_pct=False` / `merge_with_AG_beyond_limit=False` / `merge_with_AH_nocancel=False` / `merge_with_F_round=False` / `merge_with_L_mkt=False` / `merge_with_H_exit=False` / `merge_with_X_st_limit=False` / `merge_with_E_lot=False` / `merge_with_M_aft=False` / `merge_with_O_block=False` / `merge_with_R_etf_rotation=False` / `merge_with_Q_cb_rotation=False` / `merge_with_AC_bse=False` / `merge_with_AD_50w=False` / `merge_with_AE_stock_t0=False` / `merge_with_AF_qty_cap=False`（写死）**。

**待预检键（拉数前须冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                      # 可成交名义/冲击差显著门槛；≠实验字母 AI
params.G                            = 0.01                      # 超范围假进簿桶相对对照差
params.N                            = 0.05                      # 失败/废单率差门槛
params.Y2                           = 0.015                     # AI1（笼子误套集合）相对 AI2 专项门槛
params.ai0_primary_demo             = invent_open_call_band_bypass  # 主报开盘集合超范围假进簿；禁与 misapply_continuous_cage_to_call 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深普通 A 股在**无涨跌幅日**的样本（`universe_rule=sse_szse_common_stock_nolimit_days`；无板日标签复用 G 的 PIT）。ETF、可转债、北交所不进主宇宙。科创板开盘集合 900%/50% **不适用** → 科创无板日开盘集合腿进 `star_exempt` 桶或 skip，不进 AI0 主病。  
- **排除（默认）**：缺前收/最近成交；把 I/J/G/AG/A/AH 主结论并进本页主表；日频无代理声明却假装 L2 复盘。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：无板日集合/临停有效申报范围按成交日当时交易规则文本；**禁止**用核对日规则铺满；科创板不适用 900%/50% 开盘集合范围写死；深市开盘集合下界若未核到同款 50% → 另桶，禁默填。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ai0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AI0 ? AI2**：开盘集合超范围假进簿相对诚实拒单——假路径 / 可成交名义吹胖。  
2. **AI1 ? AI2**：连续笼子误套开盘集合（及可选忽略临停·收盘 ±10%）相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_open_call_outside_900_50",  # 开盘集合超范围假进簿
  "ignore_halt_close_call_10pct",     # 临停/收盘集合 ±10% 被忽略
  "misapply_cage_to_open_call",       # AI1：连续笼子误套集合
  "star_exempt_open_call_band",       # 科创板不适用 900%/50%
  "honest_reject_outside_band",       # 对照诚实废单
  "vs_I_continuous_cage",             # 对照声明：连续竞价笼子另页 I（AI≠I）
  "vs_J_halt_30_60",                  # 对照声明：临停触发另页 J
  "vs_G_fake_board_pct",              # 对照声明：无板误套板块板另页 G
  "vs_AG_beyond_day_limit",           # 对照声明：有板超涨跌停另页 AG
  "vs_A_fill",                        # 对照声明：板上枯竭另页 A（AI≠A）
  "vs_AH_nocancel",                   # 对照声明：不可撤窗另页 AH
  "day_freq_proxy_only",              # 日频敏感性档（无 L2）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可成交名义/路径质量差 ΔNotional（AI0/AI1 相对 AI2）；  
2. 超范围假进簿腿贡献差 ΔFakeBand；  
3. 废单/失败率差 ΔFail；  
4. （可选）开盘冲击差 ΔImpact。

**相对判据（草稿）**：若 |ΔNotional| 或 |ΔImpact| **≥ params.Y** 或 |ΔFakeBand 桶贡献| **≥ params.G** 或 |ΔNotional_(AI1?AI2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「无板日集合有效申报范围执行鸿沟显著」。

**params.Y / G / N / Y2（待预检建议；与实验字母 AI 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义/冲击差显著门槛（≠实验字母 AI） | **待预检建议** `0.02`；拉数前冻结；禁 null/holdout |
| params.G | 假进簿桶相对对照差 | **待预检建议** `0.01` |
| params.N | 失败/废单率差门槛 | **待预检建议** `0.05` |
| params.Y2 | AI1?AI2 专项门槛 | **待预检建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-12` |
| fill_time | 成交时点 | **写死** `next_open` |
| ai0_primary_demo | 天真主报枚举 | **待预检建议** `invent_open_call_band_bypass`；禁与 `misapply_continuous_cage_to_call` 双挂 |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组超范围须拒；科创不开 900%/50% 主病；禁与 I/J/G/AG/A/AH 混主结论）。

---

## 5. 失效条件

1. 样本几乎无无涨跌幅日，或日频无法区分开盘集合申报价与连续成交价，且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把连续竞价笼子（I）、临停 30%/60%（J）、有板超涨跌停（AG）、板上枯竭（A）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 科创板被默认套上 900%/50% 开盘集合范围进 AI0 主病 → 与事实与坑冲突，设计失效。  
4. holdout 反调 `ai0_primary_demo` / Y·G·N·Y2 → 结论无效。  
5. 用复权价算前收盘/最近成交或有效申报边界 → 标签与执行双错，结论无效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权前收盘（除权日=除权参考价）、拟挂限价、买卖方向、交易所、板块、是否无涨跌幅日（G PIT）、是否科创板；  
- 会话类型标签或代理：`open_call` / `halt_call` / `close_call`（日频可用开盘价路径敏感性代理，须声明）；  
- 临停/收盘集合腿需要最近成交价（有则用；无则该腿 skip）；  
- 交易日历与 Asia/Shanghai 会话钟（若做时戳级）。

可选：L2/逐笔（精确复盘簿）；临停公告时段。

**禁止**：用核对日现行笼子代替无板日集合范围；用复权价；把 ETF/转债/北交所混进主宇宙却不标注。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`AI`  
- **组**：AI0 / AI1 / AI2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-12`；`open_call_band_upper_mult=9.0`；`open_call_band_lower_mult_sse=0.5`；`halt_close_call_band_pct=0.10`；`star_open_call_900_50_applies=False`；`band_round=round_half_up_to_tick`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_common_stock_nolimit_days`；`missing_preclose_policy=skip`；`day_freq_proxy=open_call_band_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 待预检建议 0.02/0.01/0.05/0.015**（params.Y≠实验字母 AI）；**`params.ai0_primary_demo` 待预检建议 invent_open_call_band_bypass**（禁双挂）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AI0/AI1/AI2 可成交名义/路径质量、ΔFakeBand、ΔFail；分桶（开盘集合超范围 / 临停·收盘 ±10% / 笼子误套 / star_exempt / vs I·J·G·AG·A·AH）。  
- 自检布尔：AI2 是否超范围拒单；AI0 是否单一主报；AI1 是否笼子误套集合；是否未与 I/J/G/AG/A/AH 混主结论；holdout 是否未反调；**是否未把实验字母 AI 与 A 或 I 或 params.Y 混用**；**是否未改 Y/Z/AA–AH 冻结补丁正文**。  
- **禁止输出**：具体买卖标的列表当「建议」；把无板日任意远价进簿当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AH 及其他 A/D–AH 已交正文**；**不改假设-H**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：无板日开盘集合有效申报范围相对前收盘 900%（上交所另含 50% 下界）；临停与收盘集合相对最近成交 ±10%；连续竞价笼子不套到这些时段；科创板不适用该开盘集合 900%/50%。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AH，本页**新增实验 AI** 收成标准件，**不改口径主线**，**不改假设 A–AH 正文**。与实验 I/J/G/AG/A/AH 分工：**I=连续竞价笼子；J=无板日 30%/60% 临停触发；G=无板日误套板块默认板；AG=有板日超涨跌停拒单；A=板上枯竭；AH=不可撤窗假撤改；AI=无板日集合竞价有效申报范围假进簿（AI≠A≠I）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；无板日标签+前收或日频代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-12；**fill_time=next_open 写死**；**开盘集合 900%/50% + 临停·收盘 ±10% 写死**；diff_buckets 十二桶写死待冻结；**Y/G/N/Y2 待预检建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 AI）**；**ai0_primary_demo 待预检建议 invent_open_call_band_bypass（禁双挂）**；**待风控预检** |

---

## 变更

- 2026-11-02：新建标准件（总管线：AH 补丁已交后写下一纸面 AI；Y/Z/AA–AH 补丁已交不改；清单止于 AH → 自 `事实与坑`「无板日开盘集合 900%/50%；临停与收盘集合 ±10%；连续笼子不套集合」选题，**与 A/H/X/E/M/O/AC/AD/AE/AF/AG/AH/R/Q 及 I/F/L 及 G/J 不撞主结论**；**明确双字母 AI ≠ 单字母 A ≠ 单字母 I**；近邻 I=连续笼子、J=临停 30%/60%、G=假板、AG=有板超板、AH=不可撤窗，本页主测无板日集合有效申报范围；**实验字母 AI ≠ params.Y ≠ 实验字母 A ≠ 实验字母 I**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA–AH/A/D–AH 正文**；**不改假设-H**）。

