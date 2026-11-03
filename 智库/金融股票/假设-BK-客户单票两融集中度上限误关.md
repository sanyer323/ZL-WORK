# 假设 BK · 客户单票两融集中度上限误关 / 用核对日集中度规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BJ 补丁已收、写下一纸面 BK；清单撞题规则另选正交执行缺口（**客户信用账户对单一证券融资/融券集中度上限** ≠ 市场层单标的两融余额25pct暂停 ≠ 两融授信额度总上限 ≠ 融券空头名单 ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 维持担保比例强制平仓 ≠ 担保品折算率 ≠ 两融合约期限 ≠ 可充抵保证金证券名单 ≠ 融券卖出所得用途 ≠ 融资买入卖出还债优先）；选题自两融业务风控公开口径：券商/会员对**单一客户持有单一证券**的融资余额、融券余量或担保品市值占净资产/信用账户权益等设集中度上限；规则按**施行日/生效日** PIT，不得用核对日更宽「可无限集中」回放全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BK ≠ 单字母 B**）/ **K（融券空头名单 PIT；双字母 BK ≠ 单字母假设-K / 预检K；尤其硬分列，不得混用或覆盖假设-K）** / Z（**开仓**融资/融券保证金比例；**BK≠Z**）/ BA–BJ（两融族已冻；**BK≠BA…BJ**）/ AB（融券卖出价限 / 当日平；**BK≠AB**）/ BE（**市场层**单标的两融余额25pct暂停；**BK≠BE**；账户集中度 ≠ 市场余额比）/ BH（**客户授信额度总上限**；**BK≠BH**；总授信够 ≠ 单票可无限集中）/ E（整手）/ AN–BJ（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BK**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「客户单票两融可无限集中 / 永不检查集中度上限」当诚实执行能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BJ 及其他 A/D–BJ 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-K（尤其禁止覆盖/混读预检K）；不改假设-Z；不改假设-BA–BJ；不改假设-AB；勿再改 BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BK（约 #68）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **客户信用账户对单一证券融资/融券集中度上限是否检查**。**双字母 BK ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BK ≠ 单字母 B**。与假设 **K（融券空头名单 PIT）** **硬分列（专节强调）**：K = 当日是否在**交易所融券标的名单**内（可不可空的名单闸门）；本页 = 已可两融前提下，**同一客户对单一证券**的融资/融券敞口是否触达集中度上限；名单内可空 ≠ 可对该票无限集中。**双字母 BK ≠ 单字母假设-K ≠ 预检键里的实验字母 K**；**禁止**把本页写成「假设-K 补丁/续写」或覆盖 `假设-K-融券空头名单PIT.md`。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 开仓比例够之后的**单票敞口占比上限**；比例够 ≠ 可无限集中。与假设 **BE（单标的两融余额25pct暂停）** **硬分列**：BE = **市场层**该标的融资余额/融券余量占可流通市值·量达 25% 后暂停**市场新开**；本页 = **账户层**客户对该标的的集中度；市场未暂停 ≠ 客户可无限集中。与假设 **BH（两融授信额度上限）** **硬分列**：BH = 客户**总授信/可用额度**；本页 = 额度内对**单一证券**的集中度上限；总授信未用尽 ≠ 单票可无限加仓。与假设 **BA（融资买入标的名单）** **硬分列**：BA = 能不能开**融资买入**腿；本页 = 已在名单内后的集中度。与假设 **BB/BC/BD/BF/BG/BI/BJ** **硬分列**：券源 / 维持强平 / 折算率 / 合约期限 / 可充抵名单 / 融券所得用途 / 融资卖出还债优先 ≠ 客户单票集中度。与假设 **AB** **硬分列**：不重开空头价限/当日平。与假设 AN–BJ **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BK** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 K**（融券空头名单 PIT；**尤其 BK≠K**）≠ **单字母实验 Z**（开仓保证金比例）。全文凡写「实验 BK / 假设-BK / hypothesis_id=BK / 组 BK0·BK1·BK2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BK 混读或互改。亦**禁止**把实验字母 BK 与单字母 **A**、单字母 **B**、单字母 **K**、单字母 **Z**、双字母 **BA–BJ**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bk0_*` 以外的实验页混读。**双字母 BK ≠ 单字母 A ≠ 单字母 B ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BJ ≠ 双字母 BE ≠ 双字母 BH ≠ 双字母 AB**；**params.Y ≠ 实验字母 BK**；**params.G ≠ 实验字母 BK**；**params.N ≠ 实验字母 BK**。

### 专节 · 双字母 BK ≠ 单字母假设-K / 预检K（硬）

| 维度 | 假设-K（单字母） | 本页假设-BK（双字母） |
|------|------------------|----------------------|
| 题面 | 融券空头**名单** PIT：全 A 可空 / 核对日名单铺满 vs 当日已生效名单 | **客户单票**融资/融券**集中度上限**误关：假可无限集中 vs 按生效日集中度上限 PIT |
| 闸门层 | 交易所/会员**可融券标的集合** | 信用账户对**已准入标的**的敞口占比上限 |
| 主演示 | （K 页自有主演示；本页不引用、不覆盖） | `invent_unlimited_client_single_name_concentration` |
| 文档 | `假设-K-融券空头名单PIT.md`（**只读；禁止改写**） | `假设-BK-客户单票两融集中度上限误关.md`（新建） |
| 预检键 | 实验字母 **K** / K 页 params | 实验字母 **BK** / `bk0_primary_demo`；**不得**占用或改写预检K |

**禁止**：把 BK 写成「K 的续篇」；把「在融券名单内」静默写成「集中度未触顶」；把预检键 `K` 与 `BK` 混挂；覆盖或补丁改写假设-K 正文。

---

## 1. 一句话假设（可检验、可证伪）

同一拟开/加仓融资或融券路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/融券名单/授信/市场余额暂停输入（Z/BA/K/BH/BE 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/融券名单/总授信/市场25pct暂停」）下，把「客户对单一证券融资/融券可无限集中、永不检查集中度上限」或「全样本用核对日当天集中度规则（含券商当日更宽上限）回放历史」当成默认，相对「每个交易日按当时有效客户单票集中度上限 PIT（触顶拒开/记失败；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假可无限单票集中路径并高估可执行两融名义、低估因集中度上限导致的开仓失败率**；差异应**集中在客户单票两融集中度上限误关桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假无限集中贡献差、可执行名义差、失败率差在标定噪声带内可忽略，且「假无限集中 / 核对日泄露 / 触顶仍开窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·K·AB·B·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 客户单票集中度 ≠ 市场层25pct暂停；≠ 总授信；≠ 融券名单；≠ 开仓保证金比例；≠ 融资买入名单；≠ 转融券券源；≠ 维持担保强平；≠ 担保品折算率；≠ 合约期限；≠ 可充抵名单；≠ 融券所得用途；≠ 融资卖出还债优先；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BK；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 K；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BK
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BK
# params.asof_check_date                 写死默认 2026-10-16  # 与事实与坑「两融/保证金」核对日同向
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31     # 此前无融资融券通道 → skip 集中度腿
# params.client_conc_honest              写死 pit_by_effective_date  # 客户单票集中度按生效日 PIT
# params.client_conc_scope               写死 single_name_fin_short_vs_net_assets  # 单票融资/融券敞口相对净资产或信用权益
# params.client_conc_over_policy         写死 reject_or_fail  # 触顶仍开 → 拒开/记失败；禁静默无限集中
# params.broker_wider_conc_bucket        写死 separate_sensitivity  # 券商更宽集中度另桶；不得默认=核对日更宽
# params.margin_ratio_handoff            写死 z_page         # 开仓保证金比例交 Z；BK≠Z
# params.margin_buy_list_handoff         写死 ba_page        # 融资买入名单交 BA；BK≠BA
# params.refinance_borrow_handoff        写死 bb_page        # 转融券券源交 BB；BK≠BB
# params.maint_force_handoff             写死 bc_page        # 维持担保强平交 BC；BK≠BC
# params.haircut_handoff                 写死 bd_page        # 担保品折算率交 BD；BK≠BD
# params.balance_pause_handoff           写死 be_page        # 市场层余额25pct暂停交 BE；BK≠BE
# params.contract_term_handoff           写死 bf_page        # 合约期限交 BF；BK≠BF
# params.collateral_list_handoff         写死 bg_page        # 可充抵名单交 BG；BK≠BG
# params.credit_quota_handoff            写死 bh_page        # 授信额度交 BH；BK≠BH
# params.short_proceeds_use_handoff      写死 bi_page        # 融券所得用途交 BI；BK≠BI
# params.financing_sale_repay_handoff    写死 bj_page        # 融资卖出还债优先交 BJ；BK≠BJ
# params.shortable_list_handoff          写死 k_page         # 融券空头名单交 K；BK≠K（硬）
# params.short_px_handoff                写死 ab_page        # 融券卖出价限/当日平交 AB
# params.exit_period_handoff             写死 h_page         # 退市整理交 H；BK≠H
# params.bk0_primary_demo                写死冻结 invent_unlimited_client_single_name_concentration  # 主报：客户单票可无限集中/永不检查集中度；禁与 invent_asof_leak_client_concentration 双挂争主表；BK1半泄露不得升格并列主报
# params.bk0_invent_unlimited_client_conc 写死 True
# params.bk1_asof_leak_client_conc_only  写死 True   # 半泄露：仅用核对日集中度规则铺满历史
# params.bk2_pit_client_conc             写死 True
# params.merge_with_A_fill               写死 False
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False
# params.merge_with_BD_haircut           写死 False
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_BF_contract_term     写死 False
# params.merge_with_BG_collateral_list   写死 False
# params.merge_with_BH_credit_quota      写死 False
# params.merge_with_BI_short_proceeds    写死 False
# params.merge_with_BJ_financing_sale_repay 写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
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
# params.merge_with_BH_credit            写死 False
# params.merge_with_BI_short_proceeds    写死 False
# params.merge_with_BJ_financing_sale    写死 False
# params.universe_rule                   写死 sse_szse_client_single_name_conc_check
# params.missing_client_conc_policy      写死 skip
# params.day_freq_proxy                  写死 client_conc_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BK；params.G≠实验字母BK；params.N≠实验字母BK；亦≠单字母实验A/B/K/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
client_conc_honest = "pit_by_effective_date"
params.bk0_primary_demo = "invent_unlimited_client_single_name_concentration"  # 写死冻结；禁与 invent_asof_leak_client_concentration 双挂
```

### 2.2 三组对照（BK0 / BK1 / BK2）

| 组 | 口径 | 说明 |
|----|------|------|
| BK0 天真 | `invent_unlimited_client_single_name_concentration`（单一主报·已冻结） | 客户对单一证券融资/融券可无限集中；永不检查集中度上限 |
| BK1 半泄露 | `invent_asof_leak_client_concentration` | 仅用核对日集中度规则（含券商当日更宽上限）铺满全历史；**不得升格并列主报** |
| BK2 诚实 PIT | `pit_by_effective_date` | 按当日已生效客户单票集中度上限；触顶拒开/记失败；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/BA/K/BH/BE）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **规则生效**：细则/合同/券商风控表施行日或生效日；禁用核对日更宽「可无限集中」提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BK0 相对 BK2 的假无限集中贡献差、开仓失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「客户单票两融集中度上限误关」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeUnlimitedClientConc / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/K/AB/B/H/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BK0 / BK1 / BK2。报告名义/路径质量差、假无限集中贡献差、开仓失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_unlimited_client_single_name_concentration",
  "invent_asof_leak_client_concentration",
  "conc_cap_hit_still_open",
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
  "vs_BH_credit_quota",
  "vs_BI_short_proceeds_use",
  "vs_BJ_financing_sale_repay",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺集中度字段却静默当「客户单票可无限集中」→ 设计失效。  
2. 把「在融券空头名单内」静默写成「集中度未触顶」且不声明另页 K → **与假设-K 撞题**（名单 ≠ 集中度；**双字母 BK ≠ 单字母 K**）。  
3. 把「市场层单标的余额未达 25% 暂停」静默写成「客户可无限集中」且不声明另页 BE → 与 BE 撞题。  
4. 把「总授信额度未用尽」静默写成「单票可无限集中」且不声明另页 BH → 与 BH 撞题。  
5. 把「开仓保证金比例够」静默写成「集中度放开」且不声明另页 Z → 与 Z 撞题。  
6. 把「在融资买入名单内」静默写成「集中度未触顶」且不声明另页 BA → 与 BA 撞题。  
7. 把「维持担保比例够 / 可提取」静默写成「可无限集中」且不声明另页 BC → 与 BC 撞题。  
8. 把「可充抵名单内 / 折算率有值」静默写成「可无限集中」且不声明另页 BG/BD → 与 BG/BD 撞题。  
9. 把「转融券未暂停 / 券源够」静默写成「可无限集中」且不声明另页 BB → 与 BB 撞题。  
10. 把「合约未到期」静默写成「集中度放开」且不声明另页 BF → 与 BF 撞题。  
11. 把「融券所得用途放开 / 融资卖出还债优先放开」写成主病而不声明另页 BI/BJ → 与 BI/BJ 撞题。  
12. 把「空头价限 / 当日平」写成主病而不声明另页 AB → 与 AB 撞题。  
13. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
14. 把「退市整理期当普通可交易」写成主病而不声明另页 H → 与 H 撞题。  
15. 把「客户单票两融集中度上限误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
16. 把实验字母 BK 与单字母 A/B/K/Z 或双字母 BA–BJ/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
17. holdout 反调 `bk0_primary_demo` / Y·G·N·Y2 → 结论无效。  
18. 用复权价算敞口/可开名义 → 标签与执行双错，结论无效。  
19. 用核对日更宽集中度当诚实 PIT、或把券商临时放宽集中度提前铺满历史 → 设计失效。  
20. **改写或覆盖 `假设-K-融券空头名单PIT.md` / 预检K** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 客户信用账户拟开/加仓融资或融券腿名义；  
- 该客户对该证券已有融资余额/融券余量/担保品市值代理；  
- 净资产或信用账户权益代理（集中度分母）；  
- 当时有效**客户单票集中度上限**规则及生效日（细则/合同/券商风控表）；  
- 开仓保证金比例 / 融资名单 / 融券名单 / 总授信 / 市场余额暂停输入（消费 Z/BA/K/BH/BE 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商加严单票集中度；行业集中度另桶（本页主测单票，不主测行业）。

**禁止**：用核对日「今天可无限集中」铺满当唯一诚实组；用复权价；把开仓保证金比例/维持担保/折算率数值/融资名单/融券名单/转融券通道暂停/市场余额25pct暂停/合约期限/可充抵名单/总授信/融券所得用途/融资卖出还债优先当成客户单票集中度放开；把 Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/K/AB/A/B/H/T/AN–BJ 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BK`  
- **组**：BK0 / BK1 / BK2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`client_conc_honest=pit_by_effective_date`；`client_conc_scope=single_name_fin_short_vs_net_assets`；`client_conc_over_policy=reject_or_fail`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_client_single_name_conc_check`；`missing_client_conc_policy=skip`；`day_freq_proxy=client_conc_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BK**；**params.G≠实验字母 BK**；**params.N≠实验字母 BK**；亦≠单字母实验 A/B/K/Z；禁 null/holdout/跑后改口）；**`params.bk0_primary_demo` 写死冻结 `invent_unlimited_client_single_name_concentration`**（禁与 invent_asof_leak_client_concentration 双挂；BK1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BK0/BK1/BK2 可执行名义/路径质量、ΔFakeUnlimitedClientConc、ΔFail；分桶（客户单票集中度误关 / 核对日泄露 / 触顶仍开窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·K·AB·B·H·T）。  
- 自检布尔：BK2 是否 pit_by_effective_date；BK0 是否单一主报；BK1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/K/AB/B/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BK 与 A 或 B 或 K 或 Z 或 BA–BJ 或 params.Y 或 params.G 或 params.N 混用**；**是否未改 Y/Z/AA–BJ 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-K / 假设-Z / 假设-BA–BJ / 假设-AB**；**是否未再改 BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未覆盖假设-K / 预检K**。  
- **禁止输出**：具体买卖标的列表当「建议」；把集中度误关或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BJ 及其他 A/D–BJ 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-K**；**不改假设-Z**；**不改假设-BA–BJ**；**不改假设-AB**；**勿再改 BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、融券空头名单（K）之外，**客户单票两融集中度上限**须按当时有效规则 PIT；不得默认可无限集中。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BK** 标准件，**不改口径主线**，**不改假设 A–BJ 正文**，**尤其不改假设-K**。与实验 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/K/AB/B/H/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓；BD=担保品折算率；BE=市场层单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；BG=可充抵保证金证券名单；BH=两融授信额度上限；BI=融券卖出所得资金用途限制；BJ=融资买入卖出所得优先偿还融资负债；K=融券空头名单；AB=融券卖出价限；B=历史实验B旧位；H=退市整理；T=证管费（避开）；BK=客户单票两融集中度上限误关（BK≠A≠B≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠AB≠T）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频客户单票敞口+净资产代理+集中度上限生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**client_conc_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BK；params.G≠实验字母 BK；params.N≠实验字母 BK；亦≠单字母实验 A/B/K/Z；禁 null/holdout/跑后改口）**；**bk0_primary_demo 写死冻结 invent_unlimited_client_single_name_concentration（禁双挂 invent_asof_leak_client_concentration；BK1半泄露不得升格并列主报）**；锚点保留 client_conc_honest=pit_by_effective_date / client_conc_scope=single_name_fin_short_vs_net_assets / client_conc_over_policy=reject_or_fail / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BK**；**`params.G` ≠ 实验字母 BK**；**`params.N` ≠ 实验字母 BK**；**`params.Y` ≠ 单字母实验 A/B/K/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bk0_primary_demo`**：**写死冻结** **`invent_unlimited_client_single_name_concentration`**；禁与 **`invent_asof_leak_client_concentration`** 双挂争主表（只挂一个 primary）；**BK1 半泄露不得升格并列主报**。

**客户单票集中度锚保留（已通写死）**：`params.client_conc_honest=pit_by_effective_date`；`params.client_conc_scope=single_name_fin_short_vs_net_assets`；`params.client_conc_over_policy=reject_or_fail`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有 `missing_client_conc_policy=skip` 等锚点；不改口）。

**与 BA–BJ/Z/AB/B/A/H 硬分列（保留）**：本页 = **客户单票两融集中度上限**；BE = **市场层**单标的两融余额25pct暂停（**尤其 BK≠BE**）；BH = **客户授信额度总上限**（**尤其 BK≠BH**）；Z = **开仓**保证金比例；BA = **融资买入**标的名单；BB = **转融券暂停后券源**；BC = **维持担保比例强制平仓**；BD = **担保品折算率**；BF = **两融合约期限到期强制了结**；BG = **可充抵保证金证券名单**；BI = **融券卖出所得资金用途**；BJ = **融资买入卖出所得优先偿还融资负债**；A = **板上枯竭**；AB = **融券卖出价限**；B = 历史实验 B 旧位；H = **退市整理期**；客户单票集中度 ≠ 市场余额比 ≠ 总授信 ≠ 开仓比例 ≠ 融资可买名单 ≠ 转融券源 ≠ 维持强平 ≠ 折算率 ≠ 合约期限 ≠ 可充抵名单 ≠ 融券所得用途 ≠ 融资卖出还债优先 ≠ 板上枯竭 ≠ 空头价限 ≠ 退市整理；**双字母 BK ≠ 单字母 A ≠ 单字母 B ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BJ ≠ 双字母 BE ≠ 双字母 BH ≠ 双字母 AB**；**params.Y ≠ 实验字母 BK**；**params.G ≠ 实验字母 BK**；**params.N ≠ 实验字母 BK**；禁止捆成「两融一张表=可无限单票集中」；**尤其不改假设-H**；不改假设-B；不改假设-Z；不改假设-BA–BJ；不改假设-A；不改假设-AB。

**专节保留 · 双字母 BK ≠ 单字母假设-K / 预检K（硬）**：K = 融券空头**名单** PIT；BK = **客户单票**集中度上限；名单内可空 ≠ 可对该票无限集中；**禁止**覆盖/混读/改写 `假设-K-融券空头名单PIT.md` 或预检键 K；正文「### 专节 · 双字母 BK ≠ 单字母假设-K / 预检K」保留不删。

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BK**；**params.G≠实验字母 BK**；**params.N≠实验字母 BK**；亦≠单字母实验 A/B/K/Z；禁 null/holdout/跑后改口）；② `params.bk0_primary_demo=invent_unlimited_client_single_name_concentration`（禁与 `invent_asof_leak_client_concentration` 双挂争主表；BK1半泄露不得升格并列主报）。集中度锚保留：`client_conc_honest=pit_by_effective_date`；`client_conc_scope=single_name_fin_short_vs_net_assets`；`client_conc_over_policy=reject_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。与 BA–BJ/Z/AB/B/A/H 硬分列保留；**专节保留双字母 BK ≠ 单字母假设-K / 预检K**。参考总管派令 / 风控预检有条件通过。未改 Y/Z/AA–BJ 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-K（尤其）；不改假设-Z；不改假设-BA–BJ；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BJ 补丁已收 → 写假设-BK；自立 BK，勿占 BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/K/A/Z；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BK**；**双字母 BK ≠ 单字母假设-K**）。选题：客户单票两融集中度上限误关（正交于 BE 市场层25pct / BH 总授信 / K 融券名单 / Z 开仓比例）。
