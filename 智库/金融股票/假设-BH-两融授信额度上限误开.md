# 假设 BH · 两融授信额度上限误开 / 用核对日授信额度铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BG 补丁已收、写下一纸面 BH；清单撞题规则另选正交执行缺口（**客户融资融券授信额度 / 可用融资·融券额度上限** ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 单标的两融余额25pct暂停 ≠ 两融合约期限到期强制了结 ≠ 可充抵保证金证券名单）；选题自交易所融资融券细则与会员风控公开口径：会员对客户进行授信、约定融资与融券额度；客户融资买入/融券卖出占用额度，了结后释放；申报或成交不得突破当时有效授信/可用额度；额度按**合同/授信生效日与调整生效日** PIT，不得用核对日额度铺满全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理；**双字母 BH ≠ 单字母 H**）/ B（历史清单「实验 B」旧位；**双字母 BH ≠ 单字母 B**）/ Z（**开仓**融资/融券保证金比例；**BH≠Z**）/ BA（**融资买入**标的名单；**BH≠BA**）/ BB（**转融券暂停后券源**；**BH≠BB**）/ BC（**维持担保比例强制平仓**；**BH≠BC**）/ BD（**担保品折算率**；**BH≠BD**）/ BE（**单标的两融余额25pct暂停**；**BH≠BE**）/ BF（**两融合约期限到期强制了结**；**BH≠BF**）/ BG（**可充抵保证金证券名单**；**BH≠BG**）/ K（融券空头名单；**BH≠K**）/ AB（融券卖出价限 / 当日平；**BH≠AB**）/ E（整手）/ AN–BG（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停/合约期限/可充抵名单等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BH**  
状态：**草稿 · 待入库预检**（结论栏空；禁止把「客户两融授信额度无限 / 可用融资·融券额度永不检查 / 用核对日授信额度铺满全历史」当诚实可开两融能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BG 及其他 A/D–BG 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-Z；不改假设-BA；不改假设-BB；不改假设-BC；不改假设-BD；不改假设-BE；不改假设-BF；不改假设-BG；不改假设-K；不改假设-AB；勿再改 BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BH。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **拟开两融是否突破客户当时有效授信/可用融资·融券额度**。**双字母 BH ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BH ≠ 单字母 B**。与假设 **H（退市整理期）** **硬分列**：H = 退市整理窗口被当成普通可交易日；本页 = 两融**授信额度上限闸门**；整理期可交易性 ≠ 授信额度。**双字母 BH ≠ 单字母 H**；**尤其不改假设-H**。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 客户层面**授信/可用额度上限**（名义额度闸门）；比例够 ≠ 额度未用尽。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开**融资买入**腿（标的闸门）；本页 = 标的已可买时，客户**额度是否还够开**。与假设 **BB（转融券暂停后假无限券源）** **硬分列**：BB = 空头**券源可借量**（市场/通道层）；本页 = 客户**授信额度**（账户层）；券源 ≠ 授信。与假设 **BC（维持担保比例强制平仓）** **硬分列**：BC = 持仓存续期**维持担保比例**是否触发追保/强平；本页 = **新开/加仓时授信额度是否够**；维持线 ≠ 授信额度。与假设 **BD（担保品折算率）** **硬分列**：BD = 已在可充抵范围内的证券按什么**折算率**计入保证金可用；本页 = 授信额度上限；折算率算得出可用保证金 ≠ 未突破授信额度。与假设 **BE（单标的两融余额25pct暂停）** **硬分列**：BE = 市场层单标的余额/余量集中度暂停**新开**；本页 = 账户层授信额度；市场暂停 ≠ 客户额度。与假设 **BF（两融合约期限到期强制了结）** **硬分列**：BF = 已开合约的**存续期限上限与到期了结**；本页 = 开仓前额度闸门；期限 ≠ 授信。与假设 **BG（可充抵保证金证券名单）** **硬分列**：BG = **哪些证券可以充抵**（名单闸门）；本页 = 客户**能开多大名义**（额度闸门）；可充抵 ≠ 授信额度未用尽。与假设 **K / AB** **硬分列**：不重开融券名单与空头价限/当日平。与假设 AN–BG **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/融资买入名单/转融券假无限券源/维持强平/折算率/余额25pct暂停/合约期限/可充抵名单等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BH** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 H**（退市整理期）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BH / 假设-BH / hypothesis_id=BH / 组 BH0·BH1·BH2」均指本实验；凡写 **`params.Y`** / **`params.N`** 均指门槛数值键，**禁止**把二者与实验字母 BH 混读或互改。亦**禁止**把实验字母 BH 与单字母 **A**、单字母 **B**、单字母 **H**、单字母 **Z**、单字母 **K**、双字母 **BA**、双字母 **BB**、双字母 **BC**、双字母 **BD**、双字母 **BE**、双字母 **BF**、双字母 **BG**、双字母 **AB**、双字母 **AZ**、双字母 **AY**、双字母 **AX**、双字母 **AW**、或 params 键名 `bh0_*` 以外的实验页混读。**双字母 BH ≠ 单字母 A ≠ 单字母 B ≠ 单字母 H ≠ 单字母 Z ≠ 双字母 BA ≠ 双字母 BB ≠ 双字母 BC ≠ 双字母 BD ≠ 双字母 BE ≠ 双字母 BF ≠ 双字母 BG**；**params.Y ≠ 实验字母 BH**；**params.N ≠ 实验字母 BH**。

---

## 1. 一句话假设（可检验、可证伪）

同一拟开两融路径、同一未复权价、同一 T+1、同一开仓保证金比例与可充抵/折算输入（Z/BD/BG 层诚实或显式旁路声明「本页不重开开仓比例/折算率/可充抵名单」）下，把「客户融资融券授信额度无限 / 可用融资·融券额度永不检查」或「全样本用核对日当天授信额度（含券商当日更高额度）回放历史」当成默认，相对「每个交易日按当时有效授信额度与已占用额度 PIT（开仓占用、了结释放；超额度拒开或记失败；额度调整按生效日；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明超授信假可开路径并高估可开两融名义、低估因授信额度不足导致的开仓失败率**；差异应**集中在两融授信额度上限误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假超授信贡献差、可开名义差、失败率差在标定噪声带内可忽略，且「永不检查额度 / 核对日授信泄露 / 额度用尽窗 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·K·AB·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 授信额度上限 ≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 维持担保强平；≠ 担保品折算率；≠ 单标的余额25pct暂停；≠ 合约期限；≠ 可充抵名单；≠ 融券名单；≠ 板上枯竭；≠ 退市整理；≠ 证管费

```
# 配置写死键（见 §7；纸面占位建议；拉数前须冻结）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BH；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 H；≠ 实验字母 Z
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BH
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 授信腿
# params.credit_quota_honest             写死 pit_by_effective_date  # 授信/可用额度按生效日 PIT
# params.credit_quota_scope              写死 financing_and_securities_lending  # 融资额度与融券额度分计或合同合计另桶
# params.credit_quota_occupy_on          写死 open_fill       # 开仓成交占用；了结释放
# params.credit_quota_over_policy        写死 reject_or_fail  # 超额度 → 拒开/记失败；禁静默放大
# params.broker_higher_quota_bucket      写死 separate_sensitivity  # 券商更高额度另桶；不得默认=核对日更宽
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BH≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BH≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BH≠BB
# params.maint_force_handoff             写死 bc_page        # 维持担保强平交 BC；BH≠BC
# params.haircut_handoff                 写死 bd_page        # 担保品折算率交 BD；BH≠BD
# params.balance_pause_handoff           写死 be_page        # 单标的余额25pct暂停交 BE；BH≠BE
# params.contract_term_handoff           写死 bf_page        # 合约期限交 BF；BH≠BF
# params.collateral_list_handoff         写死 bg_page        # 可充抵名单交 BG；BH≠BG
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K
# params.short_px_handoff                写死 ab_page        # 融券卖出价限/当日平交 AB
# params.exit_period_handoff             写死 h_page         # 退市整理交 H；BH≠H
# params.bh0_primary_demo                纸面建议 invent_unlimited_credit_quota  # 主报建议：永不检查授信/可用额度=无限；禁与 invent_asof_leak_credit_quota 双挂争主表；BH1半泄露不得升格并列主报
# params.bh0_invent_unlimited_credit     写死 True
# params.bh1_asof_leak_credit_quota_only 写死 True           # 半泄露：仅用核对日授信额度铺满历史
# params.bh2_pit_credit_quota            写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_BF_contract_term     写死 False
# params.merge_with_BG_collateral_list   写死 False
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
# params.merge_with_BF_term              写死 False
# params.merge_with_BG_collateral        写死 False
# params.universe_rule                   写死 sse_szse_credit_quota_check
# params.missing_credit_quota_policy     写死 skip
# params.day_freq_proxy                  写死 credit_quota_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  纸面建议 0.02/0.01/0.05/0.015  # params.Y≠实验字母BH；params.N≠实验字母BH；亦≠单字母实验A/B/H/Z；禁null/holdout/跑后改口；拉数前须冻结
# params.date_start / date_end           写死主窗并待冻结
# params.oos_split.*                     写死四日期并待冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
credit_quota_honest = "pit_by_effective_date"
params.bh0_primary_demo = "invent_unlimited_credit_quota"  # 纸面建议；禁与 invent_asof_leak_credit_quota 双挂
```

### 2.2 三组对照（BH0 / BH1 / BH2）

| 组 | 口径 | 说明 |
|----|------|------|
| BH0 天真 | `invent_unlimited_credit_quota`（单一主报建议） | 客户授信/可用融资·融券额度永不检查=无限；忽略额度占用与上限 |
| BH1 半泄露 | `invent_asof_leak_credit_quota` | 仅用核对日授信额度（含券商当日更高额度）铺满全历史；**不得升格并列主报** |
| BH2 诚实 PIT | `pit_by_effective_date` | 按当日已生效授信额度−已占用；超额度拒开/记失败；缺额度字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年与多轮保证金/标的切日；本页不重开 Z/BA/BG/BD）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **额度生效**：合同/授信生效日与调整生效日；禁用核对日更高额度提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BH0 相对 BH2 的假超授信贡献差、开仓失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「两融授信额度上限误开」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeOverQuota / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/BG/K/AB/H/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BH0 / BH1 / BH2。报告名义/路径质量差、假超授信贡献差、开仓失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_unlimited_credit_quota",
  "invent_asof_leak_credit_quota",
  "quota_exhausted_window",
  "pre_margin_channel_20100331",
  "vs_A_limit_up_fill",
  "vs_Z_margin_ratio",
  "vs_BA_margin_buy_list",
  "vs_BB_refinance_borrow",
  "vs_BC_maint_force",
  "vs_BD_haircut",
  "vs_BE_balance_pause",
  "vs_BF_contract_term",
  "vs_BG_collateral_list",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_H_exit_period",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺授信/可用额度字段却静默当「无限授信」→ 设计失效。  
2. 把「开仓保证金比例够 / 保证金可用余额够」静默写成「授信额度未用尽」且不声明另页 Z/BD → 与 Z/BD 撞题（比例/折算够 ≠ 额度未突破）。  
3. 把「在融资买入名单内」静默写成「额度无限可开」且不声明另页 BA → 与 BA 撞题（可融资买入 ≠ 授信未用尽）。  
4. 把「可充抵名单内 / 折算率有值」静默写成「授信额度够」且不声明另页 BG/BD → 与 BG/BD 撞题。  
5. 把「维持担保比例够」静默写成「可继续新开超授信」且不声明另页 BC → 与 BC 撞题（维持线 ≠ 授信额度）。  
6. 把「转融券未暂停 / 券源够」静默写成「客户授信够」且不声明另页 BB → 与 BB 撞题（券源 ≠ 授信）。  
7. 把「单标的余额未达 25% 暂停」静默写成「客户可无限开」且不声明另页 BE → 与 BE 撞题。  
8. 把「合约未到期」静默写成「授信额度未用尽」且不声明另页 BF → 与 BF 撞题。  
9. 把「融券空头名单可空 / 空头价限」写成主病而不声明另页 K/AB → 与 K/AB 撞题。  
10. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
11. 把「退市整理期当普通可交易」写成主病而不声明另页 H → 与 H 撞题（**双字母 BH ≠ 单字母 H**；**尤其不改假设-H**）。  
12. 把「两融授信额度上限误开」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
13. 把实验字母 BH 与单字母 A/B/H/Z 或双字母 BA/BB/BC/BD/BE/BF/BG/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.N` 混读互改 → 文档失效，须重标。  
14. holdout 反调 `bh0_primary_demo` / Y·G·N·Y2 → 结论无效。  
15. 用复权价算占用名义/可开名义 → 标签与执行双错，结论无效。  
16. 用核对日更高授信额度当诚实 PIT、或把券商临时提额提前铺满历史 → 设计失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 拟开融资/融券名义（金额或数量×价）；  
- 客户**授信额度**（融资额度、融券额度或合同合计）及**生效日/调整生效日**；  
- 已占用融资/融券额度代理（持仓名义累计）；  
- 开仓保证金比例 / 可充抵名单 / 折算率输入（消费 Z/BG/BD 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商提额/降额流水；分户分产品额度；授信合同编号与到期日（合同到期≠BF 合约期限，另桶敏感性）。

**禁止**：用核对日「今天授信额度」铺满当唯一诚实组；用复权价；把开仓保证金比例/维持担保/折算率数值/融资名单/转融券通道暂停/余额25pct暂停/合约期限/可充抵名单当成授信额度；把 Z/BA/BB/BC/BD/BE/BF/BG/K/AB/A/H/T/AN–BG 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BH`  
- **组**：BH0 / BH1 / BH2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`credit_quota_honest=pit_by_effective_date`；`credit_quota_occupy_on=open_fill`；`credit_quota_over_policy=reject_or_fail`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_credit_quota_check`；`missing_credit_quota_policy=skip`；`day_freq_proxy=credit_quota_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 纸面建议 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BH**；**params.N≠实验字母 BH**；亦≠单字母实验 A/B/H/Z；禁 null/holdout/跑后改口；拉数前须冻结）；**`params.bh0_primary_demo` 纸面建议 `invent_unlimited_credit_quota`**（禁与 invent_asof_leak_credit_quota 双挂；BH1半泄露不得升格并列主报；拉数前须冻结）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BH0/BH1/BH2 可开名义/路径质量、ΔFakeOverQuota、ΔFail；分桶（授信误开 / 核对日泄露 / 额度用尽窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·K·AB·H·T）。  
- 自检布尔：BH2 是否 pit_by_effective_date；BH0 是否单一主报；BH1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/BF/BG/K/AB/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BH 与 A 或 B 或 H 或 Z 或 BA 或 BB 或 BC 或 BD 或 BE 或 BF 或 BG 或 params.Y 或 params.N 混用**；**是否未改 Y/Z/AA–BG 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-Z / 假设-BA / 假设-BB / 假设-BC / 假设-BD / 假设-BE / 假设-BF / 假设-BG / 假设-K / 假设-AB**；**是否未再改 BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**。  
- **禁止输出**：具体买卖标的列表当「建议」；把授信误开或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BG 及其他 A/D–BG 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-Z**；**不改假设-BA**；**不改假设-BB**；**不改假设-BC**；**不改假设-BD**；**不改假设-BE**；**不改假设-BF**；**不改假设-BG**；**不改假设-K**；**不改假设-AB**；**勿再改 BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）之外，**客户授信/可用融资·融券额度**须按当时有效规则 PIT；不得默认无限授信。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BH** 标准件，**不改口径主线**，**不改假设 A–BG 正文**。与实验 A/Z/BA/BB/BC/BD/BE/BF/BG/K/AB/H/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓；BD=担保品折算率；BE=单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；BG=可充抵保证金证券名单；K=融券空头名单；AB=融券卖出价限；H=退市整理；T=证管费（避开）；BH=两融授信额度上限误开（BH≠A≠B≠H≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠K≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 待入库预检 |
| 数据 | 待接入（字段见 §6；日频拟开名义+授信额度生效日+占用代理即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**credit_quota_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 纸面建议 0.02/0.01/0.05/0.015（params.Y≠实验字母 BH；params.N≠实验字母 BH；亦≠单字母实验 A/B/H/Z；禁 null/holdout/跑后改口；拉数前须冻结）**；**bh0_primary_demo 纸面建议 invent_unlimited_credit_quota（禁双挂 invent_asof_leak_credit_quota；BH1半泄露不得升格并列主报；拉数前须冻结）**；锚点保留 credit_quota_honest=pit_by_effective_date / credit_quota_occupy_on=open_fill / credit_quota_over_policy=reject_or_fail / margin_channel_start=2010-03-31 / fail_policy=skip |

---

## 待预检键（交总管入库预检）

| 键名 | 建议值 | 备注 |
|------|--------|------|
| `params.Y` | `0.02` | **≠实验字母 BH**；亦≠单字母 A/B/H/Z；禁 null/holdout |
| `params.G` | `0.01` | 同族门槛占位 |
| `params.N` | `0.05` | **≠实验字母 BH** |
| `params.Y2` | `0.015` | 同族次门槛 |
| `params.bh0_primary_demo` | `invent_unlimited_credit_quota` | 禁与 `invent_asof_leak_credit_quota` 双挂；BH1 不升格主报 |
| `params.credit_quota_honest` | `pit_by_effective_date` | 已通建议锚 |
| `params.credit_quota_occupy_on` | `open_fill` | 已通建议锚 |
| `params.credit_quota_over_policy` | `reject_or_fail` | 已通建议锚 |
| `params.margin_channel_start` | `2010-03-31` | 已通建议锚 |
| `params.asof_check_date` | `2026-10-16` | 已通建议锚 |
| `params.fail_policy` | `skip` | 已通建议锚 |

---

## 变更

- 2026-11-03：新建纸面草稿（总管续派：BG 补丁已收 → 写假设-BH；自立 BH，勿占 BG/BF/BE/BD/BC/BB/BA/B/H/A/Z；避开预检T；不开回测；禁实盘/荐股；**params.Y/N≠实验字母 BH**）。选题：两融授信额度上限误开（正交于 BA 融资买入名单 / BG 可充抵名单 / BD 折算率 / Z 开仓比例 / BC 维持强平 / BB 转融券源 / BE 余额25pct暂停 / BF 合约期限；**双字母 BH ≠ 单字母 B ≠ 单字母 H**；**尤其不改假设-H**）。