# 假设 BE · 单标的两融余额25pct暂停误关 / 用核对日余额比铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BD 补丁已收、写下一纸面 BE；清单撞题规则另选正交执行缺口（**单只标的证券融资余额/融券余量相对上市可流通市值·可流通量的 25% 暂停闸门** ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率）；选题自交易所融资融券细则公开规则：单只标的证券的**融资余额**达到该证券上市可流通市值的 **25%** 时，交易所可于次一交易日**暂停其融资买入**并向市场公布；融资余额降低至 **20%** 以下时可于次一交易日恢复；单只标的证券的**融券余量**达到该证券上市可流通量的 **25%** 时，可于次一交易日**暂停其融券卖出**；降低至 **20%** 以下可恢复（上交所《融资融券交易实施细则》规模控制章；深市同口径）；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BE ≠ 单字母 B**）/ E（整手与科创板200股；**双字母 BE ≠ 单字母 E**）/ Z（**开仓**融资/融券保证金比例；**BE≠Z**）/ BA（**融资买入**标的名单；**BE≠BA**）/ BB（**转融券暂停后券源**；**BE≠BB**）/ BC（**维持担保比例强制平仓**；**BE≠BC**）/ BD（**担保品折算率**；**BE≠BD**）/ K（融券空头名单；**BE≠K**）/ AB（融券卖出价限；**BE≠AB**）/ AN–BD（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BE**  
状态：**草稿 · 待数据 · 待跑 · 待预检**（结论栏空；禁止把「单标的两融余额 25% 暂停闸门永不检查 / 用核对日余额比铺满全历史」当诚实可成交性；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BD 及其他 A/D–BD 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-E；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-K；不改假设-AB；勿再改 BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BE。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **单标的融资余额/融券余量相对可流通是否触发 25% 暂停**。**双字母 BE ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BE ≠ 单字母 B**。与假设 **E（整手与科创板200股）** **硬分列**：E = 整手/科创起买股数；本页 = 单标的两融余额集中度暂停；**双字母 BE ≠ 单字母 E**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 市场层单标的余额/余量是否已达暂停阈值；开仓比例 ≠ 余额集中度暂停。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开**融资买入**腿（标的闸门/名单 PIT）；本页 = 标的虽在名单内，但因**全市场融资余额**达可流通市值 25% 而被暂停融资买入；名单可买 ≠ 余额未达暂停。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = **2024-07-11** 起转融券通道暂停后的空头**券源可借量**；本页 = 单标的**融券余量**达可流通量 25% 的市场层暂停；转融券通道暂停 ≠ 单标的余量集中度暂停。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = 账户持仓存续期**维持担保比例**是否触发追保/强平；本页 = 交易所对**单标的**融资/融券规模的市场层暂停；账户维持线 ≠ 单标的余额暂停。与假设 **BD（担保品折算率）** **硬分列**：BD = 可充抵保证金证券**折算率**进保证金可用；本页 = 单标的两融余额相对可流通的集中度暂停；折算率 ≠ 余额集中度。与假设 **K / AB** **硬分列**：不重开融券名单与空头价限。与假设 AN–BD **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BE** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 E**（整手与科创板200股）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BE / 假设-BE / hypothesis_id=BE / 组 BE0·BE1·BE2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 BE 混读或互改。亦**禁止**把实验字母 BE 与单字母 **A**、单字母 **B**、单字母 **E**、单字母 **Z**、单字母 **K**、双字母 **BA**、双字母 **BB**、双字母 **BC**、双字母 **BD**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `be0_*` 以外的实验页混读。**双字母 BE ≠ 单字母 A ≠ 单字母 B ≠ 单字母 E ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD**；**params.Y ≠ 实验字母 BE**；**params.N ≠ 实验字母 BE**。

---

## 1. 一句话假设（可检验、可证伪）

同一两融开仓路径、同一未复权价、同一 T+1、同一融资买入/融券卖出标的名单输入（BA/K 层诚实或显式旁路声明「本页不重开名单」）下，把「单只标的证券融资余额相对上市可流通市值 / 融券余量相对上市可流通量的 25% 暂停闸门永不检查、余额触顶仍可继续融资买入/融券卖出」或「全样本用核对日当天余额比与暂停/恢复状态回放历史」当成默认，相对「每个交易日按当时有效交易所公布的单标的融资余额/融券余量与可流通分母 PIT（触达 25% → 次一交易日起暂停该方向；降至 20% 以下 → 次一交易日可恢复；缺字段 skip/敏感性）」的诚实组，会**系统性发明假可开名义并低估因余额集中度暂停导致的开仓失败率**；差异应**集中在单标的两融余额25pct暂停误关桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假可开名义贡献差、开仓失败率差在标定噪声带内可忽略，且「余额暂停误关 / 核对日余额比泄露 / 融资25pct暂停 / 融券25pct暂停 / 20pct恢复窗 / vs A·Z·BA·BB·BC·BD·K·AB·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 单标的两融余额集中度暂停 ≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 维持担保强平；≠ 担保品折算率；≠ 融券名单；≠ 板上枯竭；≠ 证管费；≠ 整手

```
# 配置写死键（见 §7；待预检；纸面占位建议如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BE；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 E；≠ 实验字母 Z
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BE
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 余额集中度腿
# params.balance_pause_pct               写死 0.25           # 触达可流通 25% → 次一交易日可暂停
# params.balance_resume_pct              写死 0.20           # 降至 20% 以下 → 次一交易日可恢复
# params.balance_pause_effective         写死 next_trading_day  # 暂停/恢复均自次一交易日起生效
# params.fin_balance_denoms              写死 listed_free_float_mktcap  # 融资余额 / 上市可流通市值
# params.short_balance_denoms            写死 listed_free_float_shares  # 融券余量 / 上市可流通量
# params.balance_pause_honest            写死 exchange_25pct_pause_pit_then_resume_20pct
# params.broker_stricter_balance_bucket  写死 separate_sensitivity  # 券商加严另桶；不得默认=交易所更松
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BE≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BE≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BE≠BB
# params.maint_force_handoff             写死 bc_page        # 维持担保强平交 BC；BE≠BC
# params.haircut_handoff                 写死 bd_page        # 担保品折算率交 BD；BE≠BD
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K
# params.short_px_handoff                写死 ab_page        # 融券卖出价限交 AB
# params.lot_size_handoff                写死 e_page         # 整手交 E；BE≠E
# params.be0_primary_demo                待预检建议 invent_ignore_25pct_balance_pause  # 主报：永不检查25%暂停；禁与 invent_asof_leak_balance_pause 双挂争主表；BE1半泄露不得升格并列主报
# params.be0_invent_ignore_25pct_pause   写死 True
# params.be1_asof_leak_balance_pause_only 写死 True           # 半泄露：仅用核对日余额比/暂停状态铺满历史
# params.be2_pit_balance_pause           写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_K_shortable_list     写死 False
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
# params.merge_with_BA_margin_buy        写死 False
# params.merge_with_BB_refinance         写死 False
# params.merge_with_BC_maint             写死 False
# params.merge_with_BD_haircut           写死 False
# params.universe_rule                   写死 sse_szse_single_security_balance_pause_check
# params.missing_balance_policy          写死 skip
# params.day_freq_proxy                  写死 single_security_balance_pause_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  纸面占位建议 0.02/0.01/0.05/0.015  # 待预检写死；params.Y≠实验字母BE；params.N≠实验字母BE；亦≠单字母实验A/B/E/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip

fill_time = "next_open"
asof_check_date = "2026-10-16"
balance_pause_pct = 0.25
balance_resume_pct = 0.20
balance_pause_honest = "exchange_25pct_pause_pit_then_resume_20pct"
params.be0_primary_demo = "invent_ignore_25pct_balance_pause"  # 待预检；禁与 invent_asof_leak_balance_pause 双挂
```

### 2.2 三组对照（BE0 / BE1 / BE2）

| 组 | 口径 | 说明 |
|----|------|------|
| BE0 天真 | `invent_ignore_25pct_balance_pause`（单一主报） | 永不检查单标的融资余额/融券余量 25% 暂停；名单内即任意量可开 |
| BE1 半泄露 | `invent_asof_leak_balance_pause` | 仅用核对日余额比与暂停/恢复状态铺满全历史；**不得升格并列主报** |
| BE2 诚实 PIT | `exchange_25pct_pause_pit_then_resume_20pct` | 按日 PIT：融资余额/可流通市值、融券余量/可流通量；≥25%→次一交易日暂停该方向；≤20%→次一交易日可恢复；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年与 2024 转融券暂停窗；本页不重开 BB）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权；可流通市值/可流通量用当时有效上市可流通口径。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **生效时点**：暂停/恢复均按「次一交易日」生效（`balance_pause_effective=next_trading_day`）；当日盘中触顶不得静默当成当日即禁。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BE0 相对 BE2 的假可开名义贡献差、开仓失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「单标的两融余额25pct暂停误关」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeOpen / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/K/AB/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BE0 / BE1 / BE2。报告名义/路径质量差、假可开名义贡献差、开仓失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_ignore_25pct_balance_pause",
  "invent_asof_leak_balance_pause",
  "fin_balance_ge_25pct_pause",
  "short_balance_ge_25pct_pause",
  "resume_le_20pct_window",
  "vs_A_limit_up_fill",
  "vs_Z_margin_ratio",
  "vs_BA_margin_buy_list",
  "vs_BB_refinance_borrow",
  "vs_BC_maint_force",
  "vs_BD_haircut",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺单标的融资余额/融券余量或可流通分母字段却静默当「永不暂停」→ 设计失效。  
2. 把「在融资买入名单内」静默写成「余额未达 25% 暂停」且不声明另页 BA → 与 BA 撞题/设计失效。  
3. 把「转融券 2024-07-11 暂停」静默写成「单标的融券余量 25% 暂停」且不声明另页 BB → 与 BB 撞题。  
4. 把「维持担保比例够」静默写成「余额集中度未暂停」且不声明另页 BC → 与 BC 撞题。  
5. 把「折算率=1」静默写成「余额未达暂停」且不声明另页 BD → 与 BD 撞题。  
6. 把「开仓保证金比例够」静默写成「余额未达暂停」且不声明另页 Z → 与 Z 撞题。  
7. 把「融券空头名单可空」写成主病而不声明另页 K → 与 K 撞题。  
8. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
9. 把「单标的两融余额25pct暂停误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
10. 把实验字母 BE 与单字母 A/B/E/Z 或双字母 BA/BB/BC/BD/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
11. holdout 反调 `be0_primary_demo` / Y·G·N·Y2 → 结论无效。  
12. 用复权价算可流通市值/余额比 → 标签与执行双错，结论无效。  
13. 把「触达 25% 当日盘中即禁」静默写成诚实生效、或不写次一交易日生效 → 设计失效。  
14. 把券商加严余额线静默写成「等于交易所 25%/20% 更松」且不另桶 → 设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资/融券拟开腿标记；  
- 单标的融资余额、融券余量（或日频代理）；  
- 上市可流通市值、上市可流通量（或可流通股本×未复权价代理）；  
- 交易所公布的单标的融资/融券暂停与恢复公告日（若有）；  
- 融资买入名单 / 融券名单输入（消费 BA/K 诚实 PIT，或显式旁路声明本页不重开名单）；  
- 交易日历。

可选：券商加严单标的余额线；交易所逐日余额/余量明细。

**禁止**：用核对日「今天余额比/暂停表」铺满当唯一诚实组；用复权价；把开仓保证金比例/维持担保/折算率/融资名单/转融券通道暂停当成余额集中度暂停；把 Z/BA/BB/BC/BD/K/AB/A/T/AN–BD 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BE`  
- **组**：BE0 / BE1 / BE2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`balance_pause_pct=0.25`；`balance_resume_pct=0.20`；`balance_pause_effective=next_trading_day`；`fin_balance_denoms=listed_free_float_mktcap`；`short_balance_denoms=listed_free_float_shares`；`balance_pause_honest=exchange_25pct_pause_pit_then_resume_20pct`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`lot_size_handoff=e_page`；`broker_stricter_balance_bucket=separate_sensitivity`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_single_security_balance_pause_check`；`missing_balance_policy=skip`；`day_freq_proxy=single_security_balance_pause_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 纸面占位建议 `0.02/0.01/0.05/0.015`**（待预检写死；params.Y≠实验字母 BE；**params.N≠实验字母 BE**；亦≠单字母实验 A/B/E/Z；禁 null/holdout/跑后改口）；**`params.be0_primary_demo` 待预检建议 `invent_ignore_25pct_balance_pause`**（禁与 invent_asof_leak_balance_pause 双挂；BE1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BE0/BE1/BE2 可开名义/路径质量、ΔFakeOpen、ΔFail；分桶（余额暂停误关 / 核对日泄露 / 融资25pct / 融券25pct / 20pct恢复 / vs A·Z·BA·BB·BC·BD·K·AB·T）。  
- 自检布尔：BE2 是否 exchange_25pct_pause_pit；BE0 是否单一主报；BE1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/K/AB/T 混主结论；holdout 是否未反调；**是否未把实验字母 BE 与 A 或 B 或 E 或 Z 或 BA 或 BB 或 BC 或 BD 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–BD 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-E / 假设-Z / 假设-BA / 假设-BB / 假设-BC / 假设-BD / 假设-K / 假设-AB**；**是否未再改 BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把余额暂停误关或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BD 及其他 A/D–BD 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-E**；**不改假设-Z**；**不改假设-BA**；**不改假设-BB**；**不改假设-BC**；**不改假设-BD**；**不改假设-K**；**不改假设-AB**；**勿再改 BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）之外，单标的融资余额/融券余量相对可流通的 **25% 暂停 / 20% 恢复** 须按交易所公布 PIT；不得默认永不暂停。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BE** 标准件，**不改口径主线**，**不改假设 A–BD 正文**。与实验 A/Z/BA/BB/BC/BD/K/AB/T/E 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓；BD=担保品折算率；K=融券空头名单；AB=融券卖出价限；E=整手；T=证管费（避开）；BE=单标的两融余额25pct暂停误关（BE≠A≠B≠E≠Z≠BA≠BB≠BC≠BD≠K≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 · 待预检 |
| 数据 | 待接入（字段见 §6；日频单标的余额/余量 + 可流通分母代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**balance_pause_honest=exchange_25pct_pause_pit_then_resume_20pct 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 纸面占位建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BE；params.N≠实验字母 BE；亦≠单字母实验 A/B/E/Z；禁 null/holdout/跑后改口；待预检写死）**；**be0_primary_demo 待预检建议 invent_ignore_25pct_balance_pause（禁双挂 invent_asof_leak_balance_pause；BE1半泄露不得升格并列主报）**；锚点保留 balance_pause_pct=0.25 / balance_resume_pct=0.20 / balance_pause_effective=next_trading_day / margin_channel_start=2010-03-31 |

---

## 待预检键（建议；尚未冻结）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：建议 `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BE**；**`params.Y` ≠ 单字母实验 A/B/E/Z**；**`params.N` ≠ 实验字母 BE**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.be0_primary_demo`**：建议 **`invent_ignore_25pct_balance_pause`**；禁与 **`invent_asof_leak_balance_pause`** 双挂争主表（只挂一个 primary）；**BE1 半泄露不得升格并列主报**。

**余额集中度锚（已通写死建议）**：`params.balance_pause_pct=0.25`；`params.balance_resume_pct=0.20`；`params.balance_pause_effective=next_trading_day`；`params.fin_balance_denoms=listed_free_float_mktcap`；`params.short_balance_denoms=listed_free_float_shares`；`params.balance_pause_honest=exchange_25pct_pause_pit_then_resume_20pct`；`params.margin_channel_start=2010-03-31`。

**与 Z/BA/BB/BC/BD/A/K/AB/B/E 硬分列（保留）**：本页 = **单标的融资余额/融券余量 25% 暂停闸门**；Z = **开仓**保证金比例；BA = **融资买入**标的名单；BB = **转融券暂停后券源**；BC = **维持担保比例强制平仓**；BD = **担保品折算率**；A = **板上枯竭**；K = **融券空头名单**；AB = **融券卖出价限**；B = 历史实验 B 旧位；E = 整手；余额集中度暂停 ≠ 开仓比例 ≠ 融资可买名单 ≠ 转融券源 ≠ 维持强平 ≠ 折算率 ≠ 板上枯竭 ≠ 融券名单 ≠ 空头价限 ≠ 整手；**双字母 BE ≠ 单字母 A ≠ 单字母 B ≠ 单字母 E ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 AB ≠ 单字母 K**；禁止捆成「两融一张表=永不检查25%暂停」；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-A；不改假设-K；不改假设-AB；不改假设-B；不改假设-E。

---

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BD 补丁已收 → 写假设-BE；自立 BE，勿占 BD/BC/BB/BA/B/E/A/Z；避开预检T；不开回测；禁实盘/荐股；params.Y/N≠实验字母 BE）。选题：单标的两融余额/余量相对可流通 25% 暂停误关（正交于 BA 名单 / BB 转融券源 / BC 维持强平 / BD 折算率 / Z 开仓比例）。
