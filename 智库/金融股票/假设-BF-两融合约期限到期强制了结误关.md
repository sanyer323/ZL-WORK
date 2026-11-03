# 假设 BF · 两融合约期限到期强制了结误关 / 用核对日展期惯例铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BE 补丁已收、写下一纸面 BF；清单撞题规则另选正交执行缺口（**融资融券合约期限到期强制了结** ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 单标的两融余额25pct暂停）；选题自交易所融资融券细则公开规则：客户融资融券**合约期限**一般不超过 **6 个月**；合约到期前经会员同意可展期，展期期限累计仍受合同与监管上限约束；到期未了结的，会员可按规定**强制了结**（上交所《融资融券交易实施细则》合约期限与了结条款；深市同口径；券商合同可更短，本页以**交易所/行业常见最长 6 个月**为最宽可持有窗，券商更短另桶）；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BF ≠ 单字母 B**）/ F（涨跌停价取整；**双字母 BF ≠ 单字母 F**）/ Z（**开仓**融资/融券保证金比例；**BF≠Z**）/ BA（**融资买入**标的名单；**BF≠BA**）/ BB（**转融券暂停后券源**；**BF≠BB**）/ BC（**维持担保比例强制平仓**；**BF≠BC**）/ BD（**担保品折算率**；**BF≠BD**）/ BE（**单标的两融余额25pct暂停**；**BF≠BE**）/ K（融券空头名单；**BF≠K**）/ AB（融券卖出价限 / 当日平；**BF≠AB**）/ E（整手）/ AN–BE（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BF**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「两融合约永不到期 / 可无限展期 / 到期永不强制了结 / 用核对日展期惯例铺满全历史」当诚实可持有杠杆能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BE 及其他 A/D–BE 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-F；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-K；不改假设-AB；勿再改 BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BF。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **已开两融合约是否因期限到期须了结/强制了结**。**双字母 BF ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BF ≠ 单字母 B**。与假设 **F（涨跌停价取整）** **硬分列**：F = 涨跌停价 tick 取整；本页 = 两融合约期限/到期强制了结；**双字母 BF ≠ 单字母 F**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = **已开合约的存续期限上限与到期了结**；开仓比例 ≠ 合约期限。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开**融资买入**腿（标的闸门）；本页 = 开仓后合约能不能无限期持有到过期仍不了结。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 空头**券源可借量**；本页 = 多空合约**期限到期了结**；券源 ≠ 合约期限。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = 持仓存续期**维持担保比例**是否触发追保/强平（市值/负债比）；本页 = **日历期限**到期是否强制了结（即使维持担保比例仍高于 130%）；维持线强平 ≠ 到期强制了结。与假设 **BD（担保品折算率）** **硬分列**：BD = 可充抵保证金证券**折算率**；本页 = 合约期限；折算率 ≠ 期限。与假设 **BE（单标的两融余额25pct暂停）** **硬分列**：BE = 市场层单标的余额/余量集中度暂停**新开**；本页 = 账户已开合约的**到期了结**；新开暂停 ≠ 到期了结。与假设 **K / AB** **硬分列**：不重开融券名单与空头价限/当日平。与假设 AN–BE **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BF** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 F**（涨跌停价取整）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BF / 假设-BF / hypothesis_id=BF / 组 BF0·BF1·BF2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 BF 混读或互改。亦**禁止**把实验字母 BF 与单字母 **A**、单字母 **B**、单字母 **F**、单字母 **Z**、单字母 **K**、双字母 **BA**、双字母 **BB**、双字母 **BC**、双字母 **BD**、双字母 **BE**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `bf0_*` 以外的实验页混读。**双字母 BF ≠ 单字母 A ≠ 单字母 B ≠ 单字母 F ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BE**；**params.Y ≠ 实验字母 BF**；**params.N ≠ 实验字母 BF**。

---

## 1. 一句话假设（可检验、可证伪）

同一两融持仓路径、同一未复权价、同一 T+1、同一开仓保证金与维持担保输入（Z/BC 层诚实或显式旁路声明「本页不重开开仓比例/维持强平」）下，把「融资融券合约永不检查期限 / 可无限展期 / 到期永不强制了结」或「全样本用核对日当天展期惯例（含券商默认自动展期）回放历史」当成默认，相对「每个交易日按当时有效合约期限上限 PIT（最长不超过 6 个月；到期未展期或展期拒绝 → 强制了结/记到期失败；展期须显式事件且累计期限不突破上限；缺字段 skip/敏感性）」的诚实组，会**系统性发明假可无限期持有杠杆仓并高估可持有名义 / 低估因合约到期强制了结导致的被动减仓冲击与失败率**；差异应**集中在两融合约期限到期强制了结误关桶**，而不是随机散开。

证伪方向：若天真组 / 混口径组相对诚实组的假可无限持有贡献差、可持有名义差、到期了结/失败率差在标定噪声带内可忽略，且「永不检查期限 / 核对日展期惯例泄露 / 满6个月未展期窗 / vs A·Z·BA·BB·BC·BD·BE·K·AB·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 合约期限到期强制了结 ≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 维持担保强平；≠ 担保品折算率；≠ 单标的余额25pct暂停；≠ 融券名单；≠ 板上枯竭；≠ 证管费；≠ 涨跌停取整

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BF；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 F；≠ 实验字母 Z
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BF
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 期限腿
# params.contract_term_max_months        写死 6              # 交易所/行业常见最长合约期限（月）
# params.contract_term_unit              写死 calendar_month # 自开仓日起算；券商合同日更短另桶
# params.contract_rollover_policy        写死 explicit_event_only  # 展期须显式事件；禁默认自动无限展期
# params.contract_term_honest            写死 max_months_pit_then_force_settle
# params.broker_shorter_term_bucket      写死 separate_sensitivity  # 券商更短期限另桶；不得默认=交易所更宽
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BF≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BF≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BF≠BB
# params.maint_force_handoff             写死 bc_page        # 维持担保强平交 BC；BF≠BC
# params.haircut_handoff                 写死 bd_page        # 担保品折算率交 BD；BF≠BD
# params.balance_pause_handoff           写死 be_page        # 单标的余额25pct暂停交 BE；BF≠BE
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K
# params.short_px_handoff                写死 ab_page        # 融券卖出价限/当日平交 AB
# params.round_limit_handoff             写死 f_page         # 涨跌停取整交 F；BF≠F
# params.bf0_primary_demo                写死冻结 invent_unlimited_contract_term  # 主报：永不检查合约期限/无限展期/到期永不强制了结；禁与 invent_asof_leak_contract_term 双挂争主表；BF1半泄露不得升格并列主报
# params.bf0_invent_unlimited_term       写死 True
# params.bf1_asof_leak_contract_term_only 写死 True           # 半泄露：仅用核对日展期惯例/默认自动展期铺满历史
# params.bf2_pit_contract_term           写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_F_round              写死 False
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
# params.merge_with_BE_balance           写死 False
# params.universe_rule                   写死 sse_szse_margin_contract_term_check
# params.missing_contract_open_date_policy 写死 skip
# params.day_freq_proxy                  写死 contract_term_force_settle_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BF；params.N≠实验字母BF；亦≠单字母实验A/B/F/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip

fill_time = "next_open"
asof_check_date = "2026-10-16"
contract_term_max_months = 6
contract_term_honest = "max_months_pit_then_force_settle"
params.bf0_primary_demo = "invent_unlimited_contract_term"  # 写死冻结；禁与 invent_asof_leak_contract_term 双挂
```

### 2.2 三组对照（BF0 / BF1 / BF2）

| 组 | 口径 | 说明 |
|----|------|------|
| BF0 天真 | `invent_unlimited_contract_term`（单一主报） | 永不检查合约期限；默认可无限展期；到期永不强制了结 |
| BF1 半泄露 | `invent_asof_leak_contract_term` | 仅用核对日展期惯例/默认自动展期铺满全历史；**不得升格并列主报** |
| BF2 诚实 PIT | `max_months_pit_then_force_settle` | 按开仓日+当时有效最长月数 PIT；满期未显式展期 → 强制了结；展期事件累计不突破上限；缺开仓日 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年与多轮保证金/转融券切日；本页不重开 Z/BB）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **期限起算**：自该笔融资/融券合约开仓日起算日历月；到期日对齐下一可交易日了结（`force_settle_on=next_trading_day_on_or_after_expiry`）。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BF0 相对 BF2 的假可无限持有贡献差、到期了结失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「两融合约期限到期强制了结误关」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeHold / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/K/AB/T/F，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BF0 / BF1 / BF2。报告名义/路径质量差、假可无限持有贡献差、到期了结失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_unlimited_contract_term",
  "invent_asof_leak_contract_term",
  "full_6m_no_rollover_window",
  "explicit_rollover_within_cap",
  "vs_A_limit_up_fill",
  "vs_Z_margin_ratio",
  "vs_BA_margin_buy_list",
  "vs_BB_refinance_borrow",
  "vs_BC_maint_force",
  "vs_BD_haircut",
  "vs_BE_balance_pause",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_F_round_limit",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺合约开仓日/期限字段却静默当「永不到期」→ 设计失效。  
2. 把「维持担保比例够」静默写成「合约未到期可继续持有」且不声明另页 BC → 与 BC 撞题/设计失效（维持线够 ≠ 期限未满）。  
3. 把「在融资买入名单内」静默写成「合约可无限展期」且不声明另页 BA → 与 BA 撞题。  
4. 把「转融券 2024-07-11 暂停」静默写成「合约期限到期」且不声明另页 BB → 与 BB 撞题。  
5. 把「折算率=1」静默写成「合约未到期」且不声明另页 BD → 与 BD 撞题。  
6. 把「单标的余额未达 25% 暂停」静默写成「合约可无限持有」且不声明另页 BE → 与 BE 撞题。  
7. 把「开仓保证金比例够」静默写成「合约未到期」且不声明另页 Z → 与 Z 撞题。  
8. 把「融券空头名单可空 / 空头价限」写成主病而不声明另页 K/AB → 与 K/AB 撞题。  
9. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
10. 把「涨跌停价取整」写成主病而不声明另页 F → 与 F 撞题（**双字母 BF ≠ 单字母 F**）。  
11. 把「两融合约期限到期强制了结误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
12. 把实验字母 BF 与单字母 A/B/F/Z 或双字母 BA/BB/BC/BD/BE/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
13. holdout 反调 `bf0_primary_demo` / Y·G·N·Y2 → 结论无效。  
14. 用复权价算持仓名义/了结冲击 → 标签与执行双错，结论无效。  
15. 把「默认自动无限展期」静默写成诚实展期政策、或不要求显式展期事件 → 设计失效。  
16. 把券商更短期限静默写成「等于交易所 6 个月更宽」且不另桶 → 设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 融资/融券持仓腿与**合约开仓日**（或可复原开仓日的成交流水）；  
- 合约约定期限（月）或默认最长月数代理；  
- 展期事件日（若有；缺则按「未展期」）；  
- 开仓保证金比例 / 维持担保输入（消费 Z/BC 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商合同更短期限；强制了结成交冲击代理；会员展期拒绝率。

**禁止**：用核对日「今天默认自动展期」铺满当唯一诚实组；用复权价；把开仓保证金比例/维持担保/折算率/融资名单/转融券通道暂停/余额25pct暂停当成合约期限；把 Z/BA/BB/BC/BD/BE/K/AB/A/F/T/AN–BE 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BF`  
- **组**：BF0 / BF1 / BF2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`contract_term_max_months=6`；`contract_term_unit=calendar_month`；`contract_rollover_policy=explicit_event_only`；`contract_term_honest=max_months_pit_then_force_settle`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`round_limit_handoff=f_page`；`broker_shorter_term_bucket=separate_sensitivity`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_margin_contract_term_check`；`missing_contract_open_date_policy=skip`；`day_freq_proxy=contract_term_force_settle_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（params.Y≠实验字母 BF；**params.N≠实验字母 BF**；亦≠单字母实验 A/B/F/Z；禁 null/holdout/跑后改口）；**`params.bf0_primary_demo` 写死冻结 `invent_unlimited_contract_term`**（禁与 invent_asof_leak_contract_term 双挂；BF1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BF0/BF1/BF2 可持有名义/路径质量、ΔFakeHold、ΔFail；分桶（期限误关 / 核对日泄露 / 满6个月未展期 / 显式展期在上限内 / vs A·Z·BA·BB·BC·BD·BE·K·AB·F·T）。  
- 自检布尔：BF2 是否 max_months_pit_then_force_settle；BF0 是否单一主报；BF1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/K/AB/F/T 混主结论；holdout 是否未反调；**是否未把实验字母 BF 与 A 或 B 或 F 或 Z 或 BA 或 BB 或 BC 或 BD 或 BE 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–BE 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-F / 假设-Z / 假设-BA / 假设-BB / 假设-BC / 假设-BD / 假设-BE / 假设-K / 假设-AB**；**是否未再改 BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把期限误关或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BE 及其他 A/D–BE 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-F**；**不改假设-Z**；**不改假设-BA**；**不改假设-BB**；**不改假设-BC**；**不改假设-BD**；**不改假设-BE**；**不改假设-K**；**不改假设-AB**；**勿再改 BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、单标的余额25pct暂停（BE）之外，两融合约**期限上限与到期强制了结**须按当时有效规则 PIT；不得默认永不到期/无限展期。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BF** 标准件，**不改口径主线**，**不改假设 A–BE 正文**。与实验 A/Z/BA/BB/BC/BD/BE/K/AB/F/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓；BD=担保品折算率；BE=单标的两融余额25pct暂停；K=融券空头名单；AB=融券卖出价限；F=涨跌停价取整；T=证管费（避开）；BF=两融合约期限到期强制了结误关（BF≠A≠B≠F≠Z≠BA≠BB≠BC≠BD≠BE≠K≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频持仓+开仓日+期限月数代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**contract_term_honest=max_months_pit_then_force_settle 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BF；params.N≠实验字母 BF；亦≠单字母实验 A/B/F/Z；禁 null/holdout/跑后改口）**；**bf0_primary_demo 写死冻结 invent_unlimited_contract_term（禁双挂 invent_asof_leak_contract_term；BF1半泄露不得升格并列主报）**；锚点保留 contract_term_max_months=6 / contract_rollover_policy=explicit_event_only / contract_term_honest=max_months_pit_then_force_settle / margin_channel_start=2010-03-31 / fail_policy=skip |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BF**；**`params.Y` ≠ 单字母实验 A/B/F/Z**；**`params.N` ≠ 实验字母 BF**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bf0_primary_demo`**：**写死冻结** **`invent_unlimited_contract_term`**；禁与 **`invent_asof_leak_contract_term`** 双挂争主表（只挂一个 primary）；**BF1 半泄露不得升格并列主报**。

**合约期限锚保留（已通写死）**：`params.contract_term_max_months=6`；`params.contract_rollover_policy=explicit_event_only`；`params.contract_term_honest=max_months_pit_then_force_settle`；`params.margin_channel_start=2010-03-31`；`params.fail_policy=skip`（及正文已有 `contract_term_unit=calendar_month` / `broker_shorter_term_bucket=separate_sensitivity` 等锚点；不改口）。

**与 BA/BB/BC/BD/BE/Z/K/AB/B/F 硬分列（保留）**：本页 = **两融合约期限到期强制了结**；Z = **开仓**保证金比例；BA = **融资买入**标的名单；BB = **转融券暂停后券源**；BC = **维持担保比例强制平仓**；BD = **担保品折算率**；BE = **单标的两融余额25pct暂停**；A = **板上枯竭**；K = **融券空头名单**；AB = **融券卖出价限**；B = 历史实验 B 旧位；F = 涨跌停价取整；合约期限到期了结 ≠ 开仓比例 ≠ 融资可买名单 ≠ 转融券源 ≠ 维持强平 ≠ 折算率 ≠ 余额25pct暂停 ≠ 板上枯竭 ≠ 融券名单 ≠ 空头价限 ≠ 涨跌停取整；**双字母 BF ≠ 单字母 A ≠ 单字母 B ≠ 单字母 F ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BE ≠ 双字母 AB ≠ 单字母 K**；禁止捆成「两融一张表=永不到期/无限展期」；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-A；不改假设-K；不改假设-AB；不改假设-B；不改假设-F。

---

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BF**；亦≠单字母实验 A/B/F/Z；**params.N≠实验字母 BF**；禁 null/holdout/跑后改口）；② `params.bf0_primary_demo=invent_unlimited_contract_term`（禁与 `invent_asof_leak_contract_term` 双挂争主表；BF1半泄露不得升格并列主报）。合约期限锚保留：`contract_term_max_months=6`；`contract_rollover_policy=explicit_event_only`；`contract_term_honest=max_months_pit_then_force_settle`；`margin_channel_start=2010-03-31`；`fail_policy=skip`。与 BA/BB/BC/BD/BE/Z/K/AB/B/F 硬分列保留。参考总管派令 / 风控预检有条件通过。未改 Y/Z/AA–BE 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-F；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-K；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BE 补丁已收 → 写假设-BF；自立 BF，勿占 BE/BD/BC/BB/BA/B/F/A/Z；避开预检T；不开回测；禁实盘/荐股；params.Y/N≠实验字母 BF）。选题：两融合约期限到期强制了结误关（正交于 BA 名单 / BB 转融券源 / BC 维持强平 / BD 折算率 / BE 余额25pct暂停 / Z 开仓比例；**双字母 BF ≠ 单字母 B ≠ 单字母 F**）。
