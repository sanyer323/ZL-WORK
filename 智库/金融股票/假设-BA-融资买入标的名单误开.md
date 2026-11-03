# 假设 BA · 融资买入标的名单误开 / 用今天的融资标的回放（执行鸿沟）

更新：2026-11-03  
来源：总管线 / AZ 补丁已收、写下一纸面 BA；清单撞题规则另选正交执行缺口（融资买入标的名单 ≠ 融券空头名单 ≠ 保证金比例）；选题自 `事实与坑`「标的须经交易所认可并公布；会员向客户公布的名单不得超出本所范围；风险警示当日调出；进入终止上市程序自公告当日调出；名单按施行日不按印发日；2010-03-31 起才接受融资融券申报」公开规则；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」印花税时点·财务可见日·除权误判等旧位；**双字母 BA ≠ 单字母 B**）/ K（**融券空头**名单 PIT；**BA≠K**）/ Z（融资/融券**保证金比例**误铺；**BA≠Z**）/ AB（融券卖出价限 / 禁市价 / 当日平；**BA≠AB**）/ E（整手）/ M（盘后）/ O（大宗）/ N（收盘切日/假 GTC）/ Q（可转债）/ R（股票 ETF 假回转）/ S/T/U/V（费用层；**避开预检T旧题**）/ W（除权判板）/ L（市价通道）/ D（开/收时点与停牌）/ AN–AZ（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick 等）/ Y（集合量计入日线；**实验字母 Y ≠ params.Y**）/ AA–AZ / AC–AZ 等**分列**；**新建实验 BA**  
状态：**草稿 · 待数据 · 待跑 · 风控补丁两条已写死待复检（2026-11-03）**（结论栏空；禁止把「全 A 任意日可融资买入 / 用核对日融资标的回放十年」当诚实两融能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–AZ 及其他 A/D–AZ 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-K；不改假设-Z；不改假设-AB；勿再改 AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BA。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **融资买入腿是否落在当日已生效融资标的名单内**。**双字母 BA ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BA ≠ 单字母 B**。与假设 **K（融券空头名单）** **硬分列**：K = **空头/融券**可空名单；本页 = **多头融资买入**可融名单；可融资 ≠ 可融券，禁止捆成「两融名单一张表」。与假设 **Z（保证金比例）** **硬分列**：Z = 已允许融资/融券后的**比例/可开名义**；本页 = **能不能开融资买入腿**（名单闸门），不主测 80%/100% 比例。**双字母 BA ≠ 单字母 Z**。与假设 **AB（融券卖出价限）** **硬分列**：AB = 融券卖出价限/禁市价/当日平；本页不主测空头价限。与假设 AN–AZ **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BA** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 Z**（保证金比例）。全文凡写「实验 BA / 假设-BA / hypothesis_id=BA / 组 BA0·BA1·BA2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 BA 混读或互改。亦**禁止**把实验字母 BA 与单字母 **A**、单字母 **B**、单字母 **K**、单字母 **Z**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `ba0_*` 以外的实验页混读。**双字母 BA ≠ 单字母 A ≠ 单字母 B ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 AB ≠ 双字母 AZ**；**params.Y ≠ 实验字母 BA**；**params.N ≠ 实验字母 BA**。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权价、同一 T+1、同一保证金比例输入（Z 层诚实或显式旁路声明）下，把「全 A 任意日任意量可融资买入」或「全样本用核对日当天融资标的名单回放历史」当成默认融资能力，相对「每个交易日只用当日已生效融资标的名单；2010-03-31 前无此通道；风险警示当日调出；进入终止上市程序自公告当日调出；缺名单 skip/敏感性」的 PIT 诚实组，会**系统性发明名单外融资买入路径并高估可开融资名义 / 低估融资失败率**；差异应**集中在融资买入标的名单误开桶**，而不是随机散开。

证伪方向：若天真组 / 泄露组相对诚实组的假融资腿贡献差、可开名义差、失败率差在标定噪声带内可忽略，且「名单外历史融资腿 / ST·风险警示当日调出 / 2010-03-31 前 / vs A·K·Z·AB·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 融资买入标的名单 ≠ 融券空头名单；≠ 保证金比例；≠ 融券卖出价限；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；风控补丁两条已冻结 2026-11-03）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BA；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 Z
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BA
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融标的/名单施行日」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券申报通道
# params.margin_buy_list_honest          写死 pit_by_effective_date
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K；BA≠K
# params.margin_ratio_handoff            写死 z_page         # 保证金比例交 Z；BA≠Z
# params.short_px_handoff                写死 ab_page        # 融券卖出价限交 AB
# params.ba0_primary_demo                写死 invent_all_ashare_marginable  # 风控补丁冻结；主报：全 A 默认可融资买入；禁与 invent_asof_leak_margin_buy_list 双挂争主表；BA1半泄露不得升格并列主报
# params.ba0_invent_all_marginable       写死 True
# params.ba1_asof_leak_list_only         写死 True           # 半泄露：仅用核对日融资标的铺满历史
# params.ba2_pit_list                    写死 True
# params.risk_warning_delist_same_day    写死 True           # ST/风险警示当日调出；终止上市程序公告当日调出
# params.list_notice_apply               写死 effective_date_not_print_date
# params.merge_with_A_fill               写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_O_block              写死 False
# params.merge_with_Q_cb                 写死 False
# params.merge_with_R_etf_rotation       写死 False
# params.merge_with_L_mkt                写死 False
# params.merge_with_E_lot                写死 False
# params.merge_with_I_cage               写死 False
# params.merge_with_F_round              写死 False
# params.merge_with_G_nolimit_pct        写死 False
# params.merge_with_J_halt               写死 False
# params.merge_with_D_halt_timing        写死 False
# params.merge_with_Y_call_volume        写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_X_st_limit           写死 False
# params.merge_with_AA_bar_tz            写死 False
# params.merge_with_AC_bse               写死 False
# params.merge_with_AF_qty_cap           写死 False
# params.merge_with_AG_beyond_limit      写死 False
# params.merge_with_AH_nocancel          写死 False
# params.merge_with_AI_call_band         写死 False
# params.merge_with_AJ_resume            写死 False
# params.merge_with_AK_call_cont         写死 False
# params.merge_with_AL_session_gap       写死 False
# params.merge_with_AM_halt              写死 False
# params.merge_with_AN_open_leftover     写死 False
# params.merge_with_AO_close_leftover    写死 False
# params.merge_with_AP_aft_side          写死 False
# params.merge_with_AQ_halt_cage         写死 False
# params.merge_with_AR_queue             写死 False
# params.merge_with_AS_ioc_fok           写死 False
# params.merge_with_AT_best5_to_limit    写死 False
# params.merge_with_AU_own_opp_best      写死 False
# params.merge_with_AV_call_match        写死 False
# params.merge_with_AW_close_fail        写死 False
# params.merge_with_AX_fund_fee          写死 False
# params.merge_with_AY_fund_tick         写死 False
# params.merge_with_AZ_open_fail         写死 False
# params.universe_rule                   写死 sse_szse_margin_buy_list_check
# params.missing_list_policy             写死 skip
# params.day_freq_proxy                  写死 margin_buy_list_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 风控补丁冻结；params.Y≠实验字母BA；params.N≠实验字母BA；亦≠单字母实验A/B/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
tick = 0.01
margin_channel_start = "2010-03-31"
margin_buy_list_honest = "pit_by_effective_date"
shortable_list_handoff = "k_page"
margin_ratio_handoff = "z_page"
short_px_handoff = "ab_page"
ba0_primary_demo = "invent_all_ashare_marginable"  # 写死冻结；禁与 invent_asof_leak_margin_buy_list 双挂；BA1半泄露不得升格并列主报
ba0_invent_all_marginable = True
ba1_asof_leak_list_only = True
ba2_pit_list = True
risk_warning_delist_same_day = True
list_notice_apply = "effective_date_not_print_date"
universe_rule = "sse_szse_margin_buy_list_check"
missing_list_policy = "skip"
day_freq_proxy = "margin_buy_list_sensitivity"

# 风控补丁写死冻结（2026-11-03；禁 null/holdout/跑后改口）
Y = 0.02   # 写死；相对门槛 ≠ 实验字母 BA；≠ 单字母实验 A/B/Z
G = 0.01   # 写死
N = 0.05   # 写死；失败/废单率差门槛 ≠ 实验字母 BA
Y2 = 0.015 # 写死
```

### 2.2 组定义（BA0 / BA1 / BA2）

| 组 | 融资买入标的 | 说明 |
|----|--------------|------|
| BA0 天真 | 按 `ba0_primary_demo` 单一主报（**写死冻结** `invent_all_ashare_marginable`） | 发明名单闸门不存在；禁与 invent_asof_leak_margin_buy_list 双挂 |
| BA1 半泄露/混口径 | 全样本用 `asof_check_date` 当天融资标的名单铺满历史 | 仅名单 asof 泄露；不升格并列主报 |
| BA2 PIT 诚实 | 按成交日/调仓日已生效融资标的；通道日起算；ST/终止上市当日调出；缺名单 skip | 诚实闸门 |

### 2.3 与近邻硬分列（merge_with_* 全 False）

- **≠A**：板上枯竭 ≠ 融资标的闸门。  
- **≠B**：不重开历史实验 B（印花税时点/财务可见/除权误判）旧题。  
- **≠K**：融券空头名单 ≠ 融资买入名单。  
- **≠Z**：保证金比例 ≠ 名单可融。  
- **≠AB**：融券卖出价限 ≠ 融资买入名单。  
- **≠T**：证管费误抽（**避开预检T**）≠ 本页。  
- **≠AN–AZ**：不重开集合/失败回落/基金费用价位链。

**风控补丁两条（已写死冻结 · 2026-11-03；禁 holdout；禁 null；禁双挂；禁跑后改口）**：

```
params.Y                            = 0.02                         # 写死冻结；名义差显著门槛；≠实验字母 BA；≠单字母实验 A/B/Z
params.G                            = 0.01                         # 写死冻结；假融资腿桶相对对照差
params.N                            = 0.05                         # 写死冻结；失败/废单率差门槛；≠实验字母 BA
params.Y2                           = 0.015                        # 写死冻结；BA1（asof泄露）相对 BA2 专项门槛
params.ba0_primary_demo             = invent_all_ashare_marginable  # 写死冻结主报：全 A 默认可融资买入；禁与 invent_asof_leak_margin_buy_list 双挂争主表；BA1半泄露不得升格并列主报
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股拟开**融资买入腿**的样本（`universe_rule=sse_szse_margin_buy_list_check`）。ETF 融资标的可作分桶诊断，不并进与股票混名的主表除非显式标注。融券空头腿交 K，不进本页主宇宙。  
- **排除（默认）**：把 K/Z/AB/A/T 主结论并进本页主表；缺名单却静默当可融；把「可融资」写成「可融券」；把证管费误抽并进主病（交 T；**避开预检T**）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
- **PIT 切片原则**：融资标的按**施行日已生效**名单；**禁止**用印发日当天当生效；**禁止**用核对日现行融资标的铺满；2010-03-31 前记通道不存在。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 `ba0_primary_demo`、混口径开关、显著性门槛（含 **`params.Y`** / **`params.N`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **BA0 ? BA2**：全 A 默认可融资相对诚实名单——假融资腿 / 可开名义吹胖、失败率低估。  
2. **BA1 ? BA2**：核对日名单泄露相对诚实——混口径假路径。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "invent_all_ashare_marginable",
  "invent_asof_leak_margin_buy_list",
  "honest_pit_margin_buy_list",
  "off_list_historical_margin_buy",
  "risk_warning_same_day_delist",
  "pre_20100331_no_channel",
  "board_day_margin_path",
  "vs_A_fill",
  "vs_K_shortable",
  "vs_Z_margin_ratio",
  "vs_AB_short_px",
  "vs_T_csrc_fee",
  "vs_H_exit",
  "vs_AD_50w",
  "day_freq_proxy_only",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 可开融资名义/路径质量差 ΔNotional（BA0/BA1 相对 BA2）；  
2. 假融资腿贡献差 ΔFakeMarginBuy；  
3. 失败/废单率差 ΔFail；  
4. （可选）占用/可开倍数代理差 ΔCapacity（声明消费 Z 诚实比例或不测比例，不重开 Z）。

**相对判据（草稿）**：若 |ΔNotional| **≥ params.Y** 或 |ΔFakeMarginBuy 桶贡献| **≥ params.G** 或 |ΔNotional_(BA1?BA2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「融资买入标的名单执行鸿沟显著」。

**params.Y / G / N / Y2（写死冻结 2026-11-03；与实验字母 BA / 单字母实验 A/B/Z 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 名义差显著门槛（≠实验字母 BA；≠单字母实验 A/B/Z） | **写死冻结** `0.02` |
| params.G | 假融资腿桶相对对照差 | **写死冻结** `0.01` |
| params.N | 失败/废单率差门槛（≠实验字母 BA） | **写死冻结** `0.05` |
| params.Y2 | BA1?BA2 专项门槛 | **写死冻结** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-16` |
| fill_time | 成交时点 | **写死** `next_open` |
| ba0_primary_demo | 天真主报枚举 | **写死冻结** `invent_all_ashare_marginable`（禁与 invent_asof_leak_margin_buy_list 双挂；BA1半泄露不得升格并列主报） |

### 4.3 红线 v0

`params.redline_v0_exempt_scope=position_industry_dd_only`：本机制实验豁免仓位/行业/回撤类数值红线；**不豁免**执行诚信自检（诚实组须 pit_by_effective_date；禁与 A/K/Z/AB/T 混主结论；禁荐股）。

---

## 5. 失效条件

1. 样本几乎无法区分「诚实 PIT 融资标的」与「全 A 可融 / asof 泄露」，或无名单源且未声明 `day_freq_proxy` → 本假设不可检。  
2. 把融券空头名单（K）、保证金比例（Z）、融券卖出价限（AB）、板上枯竭（A）、证管费（T）、退市整理（H）并进主表当「同一结论」→ 设计失效，须拆页。  
3. 把「融资买入标的名单误开」写成「融券空头名单可空」为主病而不声明另页 K → 与 K 撞题，设计失效。  
4. 把「融资买入标的名单误开」写成「保证金比例误铺」而不声明另页 Z → 与 Z 撞题，设计失效。  
5. 把「融资买入标的名单误开」写成「融券卖出价限/当日平」而不声明另页 AB → 与 AB 撞题，设计失效。  
6. 把「融资买入标的名单误开」写成「板上能否按板上价成交」而不声明另页 A → 与 A 撞题，设计失效。  
7. 把「融资买入标的名单误开」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
8. 把实验字母 BA 与单字母 A 或单字母 B 或单字母 K 或单字母 Z 或双字母 AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
9. holdout 反调 `ba0_primary_demo` / Y·G·N·Y2 → 结论无效。  
10. 用复权价算名义 → 标签与执行双错，结论无效。  
11. 把印发日当天当成名单已生效 → 与公开规则冲突，设计失效。  
12. 把「可融资」静默写成「可融券」或反过来 → 与 K 撞题/设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资买入腿标记（或拟开融资买入信号）；  
- 沪深融资标的名单表（含施行日/生效日，非整印发日）；  
- 风险警示/ST 调出日、终止上市程序公告日；  
- 交易日历；可选保证金比例输入（消费 Z，不重开）；可选融券名单（消费 K，仅对照分桶）。

可选：季度定期调整通知施行日表；不定期调整公告；ETF 融资标的分桶。

**禁止**：用核对日「今天的融资标的」铺满历史；用印发日当生效日；用复权价；把融券名单当融资名单；把 K/Z/AB/A/T/AN–AZ 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BA`  
- **组**：BA0 / BA1 / BA2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`margin_buy_list_honest=pit_by_effective_date`；`shortable_list_handoff=k_page`；`margin_ratio_handoff=z_page`；`short_px_handoff=ab_page`；全部 `merge_with_*=False`（§2.3）；`universe_rule=sse_szse_margin_buy_list_check`；`missing_list_policy=skip`；`day_freq_proxy=margin_buy_list_sensitivity`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 BA；**params.N≠实验字母 BA**；亦≠单字母实验 A/B/Z；禁 null/holdout；风控补丁冻结 2026-11-03）；**`params.ba0_primary_demo` 写死 `invent_all_ashare_marginable`**（禁与 invent_asof_leak_margin_buy_list 双挂；BA1半泄露不得升格并列主报；风控补丁冻结 2026-11-03）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BA0/BA1/BA2 可开融资名义/路径质量、ΔFakeMarginBuy、ΔFail；分桶（全 A 可融 / asof 泄露 / 名单外历史腿 / ST 当日调出 / 2010-03-31 前 / vs A·K·Z·AB·T）。  
- 自检布尔：BA2 是否 pit_by_effective_date；BA0 是否单一主报；BA1 是否仅 asof 泄露；是否未与 A/K/Z/AB/T 混主结论；holdout 是否未反调；**是否未把实验字母 BA 与 A 或 B 或 K 或 Z 或 AB 或 AZ 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–AZ 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-K / 假设-Z / 假设-AB**；**是否未再改 AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把全 A 可融或核对日名单冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–AZ 及其他 A/D–AZ 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-K**；**不改假设-Z**；**不改假设-AB**；**勿再改 AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：两融标的须经交易所认可并公布；名单按施行日；可融资与可融券分列；保证金比例另页。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BA** 标准件，**不改口径主线**，**不改假设 A–AZ 正文**。与实验 A/K/Z/AB/T 分工：**A=板上枯竭门槛；K=融券空头名单；Z=保证金比例；AB=融券卖出价限；T=证管费（避开）；BA=融资买入标的名单误开（BA≠A≠B≠K≠Z≠AB≠T）**。

---

## 9. ״̬

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；融资标的施行日表或日频敏感性即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**margin_buy_list_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死 0.02/0.01/0.05/0.015（params.Y≠实验字母 BA；params.N≠实验字母 BA；亦≠单字母实验 A/B/Z；风控补丁冻结 2026-11-03）**；**ba0_primary_demo 写死 invent_all_ashare_marginable（禁双挂；BA1半泄露不得升格并列主报；风控补丁冻结 2026-11-03）** |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BA**；**`params.Y` ≠ 单字母实验 A/B/Z**；**`params.N` ≠ 实验字母 BA**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.ba0_primary_demo`**：**写死冻结** **`invent_all_ashare_marginable`**；禁与 **`invent_asof_leak_margin_buy_list`** 双挂争主表（只挂一个 primary）；**BA1 半泄露不得升格并列主报**。

**与 AB/K 硬分列（保留）**：本页 = **融资买入**标的名单闸门；AB = **融券卖出价限**；K = **融券空头**名单；融资买入 ≠ 融券卖出价限 ≠ 融券空头名单；禁止捆成「两融名单一张表」或「空头价限=多头可融」；不改假设-AB；不改假设-K。

---

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BA**；亦≠单字母实验 A/B/Z；**params.N≠实验字母 BA**；禁 null/holdout/跑后改口）；② `params.ba0_primary_demo=invent_all_ashare_marginable`（禁与 `invent_asof_leak_margin_buy_list` 双挂争主表；BA1半泄露不得升格并列主报）。与 AB/K 硬分列保留。参考总管派令 / 风控预检有条件通过。未改 Y/Z/AA–AZ 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-K；不改假设-Z；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建标准件（总管线：AZ 补丁已收后写下一纸面 BA；Y/Z/AA–AZ 补丁/正文已交不改；清单撞题规则另选「融资买入标的名单误开」；选题自 `事实与坑`；**与 A/H/B/K/Z/AB/E/M/O/N/Q/R/S/T/U/V/W/L/D/AN–AZ/Y/AA–AZ 硬分列**；**双字母 BA ≠ 单字母 A ≠ 单字母 B**；**不与 AN–AZ 重复**；**明确避开预检T旧题（证管费误抽）**；**勿占 AZ（开盘集合失败假抄前收）/AY/AX/AW**；结论栏空；不开回测；不抢 A；**勿再改 AZ/AY/AX/AW**）。
