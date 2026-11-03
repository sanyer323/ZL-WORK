# 假设 BM · 追保通知后仍假可新开仓误开 / 用核对日追保开仓禁令规则铺满（执行鸿沟）

更新：2026-11-03  
来源：总管线 / BL 补丁已收、写下一纸面 BM；清单撞题规则另选正交执行缺口（**追保通知/维持担保追保期内禁止新开融资或融券** ≠ 维持担保比例强制平仓 ≠ 担保品提取转出限制 ≠ 客户单票集中度 ≠ 两融授信额度 ≠ 开仓保证金比例 ≠ 融资买入标的名单 ≠ 转融券券源 ≠ 担保品折算率 ≠ 可充抵保证金证券名单 ≠ 融券卖出所得用途 ≠ 融资买入卖出还债优先 ≠ 市场25pct暂停 ≠ 合约期限 ≠ 融券空头名单）；选题自两融业务风控公开口径：维持担保比例低于追保线（常见约 150%，会员可加严）时须追保，**追保到位前不得新开仓**（含融资买入/融券卖出加仓）；规则按**施行日/生效日** PIT，不得用核对日更宽「追保期内仍可新开」回放全历史；2010-03-31 前无此通道；与假设 A（板上可成交/枯竭）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 BM ≠ 单字母 B**）/ **M（盘后补成交；双字母 BM ≠ 单字母假设-M）** / Z（**开仓**融资/融券保证金比例；**BM≠Z**）/ BA–BL（两融族已冻；**BM≠BA…BL**）/ **K（融券空头名单 PIT；BM≠K；并带过 BK≠K 消歧）** / AB（融券卖出价限 / 当日平；**BM≠AB**）/ BC（**维持担保比例强制平仓**；**BM≠BC**；低维持强平 ≠ 追保期内禁新开）/ BL（**担保品提取转出限制**；**BM≠BL**；高维持提取 ≠ 追保禁开；并带过 **BL≠BC**）/ BD（**担保品折算率**；**BM≠BD**）/ BG（**可充抵保证金证券名单**；**BM≠BG**）/ E（整手）/ AN–BL（集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等）/ S/T/U/V（费用层；**避开预检T旧题**）等**分列**；**新建实验 BM**  
状态：**草稿 · 预检有条件通过 · 两条已冻结待复检**（结论栏空；禁止把「追保通知后仍可任意新开两融」当诚实执行能力；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BL 及其他 A/D–BL 已交正文与冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-M；不改假设-K；不改假设-Z；不改假设-BA–BL；不改假设-AB；勿再改 BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 BM（约 #70）。与假设 **A（涨停可成交性）** **硬分列**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **追保通知后是否仍允许新开融资/融券**。**双字母 BM ≠ 单字母 A**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 BM ≠ 单字母 B**。与假设 **M（盘后补成交）** **硬分列**：M = 盘后固定价格交易/补成交通道；本页 = 信用账户**追保期内禁新开**闸门；盘后补成交 ≠ 追保开仓禁令。**双字母 BM ≠ 单字母假设-M**。与假设 **K（融券空头名单 PIT）** **硬分列**：K = 当日是否在**交易所融券标的名单**内；本页 = 追保未到位时能否**新开**；名单内可空 ≠ 追保期内可新开。**BM≠K**；并**带过**：双字母 **BK ≠ 单字母假设-K / 预检K**（BK=客户单票集中度；K=融券名单；本页不覆盖、不混读二者）。与假设 **Z（开仓保证金比例）** **硬分列**：Z = **新开**融资/融券时的保证金**比例**数值；本页 = 比例够之后、因**追保状态**仍禁新开；比例够 ≠ 追保期内可开。与假设 **BC（维持担保比例强制平仓）** **硬分列（专节强调）**：BC = **低维持线**追保失败后的**强制平仓**（主演示 invent_no_force_close；130%/150%）；本页 = **追保通知已发、强平尚未触发**窗口内**禁止新开仓**；强平误关 ≠ 追保禁开误关。与假设 **BL（担保品提取转出限制）** **硬分列**：BL = **高维持线**提取/转出闸门（超过 300% 可提取）；本页 = **低/中维持追保期**禁新开；提取 ≠ 新开禁令；并**带过 BL≠BC**（提取≠强平）。与假设 **BD（担保品折算率）** **硬分列**：BD = 折算率计入保证金可用；本页 = 追保状态下新开禁令。与假设 **BG（可充抵保证金证券名单）** **硬分列**：BG = **哪些证券可以充抵**；本页 = 追保期内能否新开。与假设 **BK（客户单票两融集中度）** **硬分列**：BK = 单票敞口占比上限；本页 = 追保禁开；集中度 ≠ 追保状态；**带过 BK≠K**。与假设 **BA/BB/BE/BF/BH/BI/BJ** **硬分列**：融资名单 / 转融券源 / 市场25pct / 合约期限 / 总授信 / 融券所得用途 / 融资卖出还债优先 ≠ 追保期内禁新开。与假设 **AB** **硬分列**：不重开空头价限/当日平。与假设 AN–BL **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 BM** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 M**（盘后补成交）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）。全文凡写「实验 BM / 假设-BM / hypothesis_id=BM / 组 BM0·BM1·BM2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 BM 混读或互改。亦**禁止**把实验字母 BM 与单字母 **A**、单字母 **B**、单字母 **M**、单字母 **K**、单字母 **Z**、双字母 **BA–BL**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `bm0_*` 以外的实验页混读。**双字母 BM ≠ 单字母 A ≠ 单字母 B ≠ 单字母 M ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BL ≠ 双字母 BC ≠ 双字母 BK ≠ 双字母 AB**；**params.Y ≠ 实验字母 BM**；**params.G ≠ 实验字母 BM**；**params.N ≠ 实验字母 BM**。**带过：双字母 BL ≠ 双字母 BC**（提取≠强平）；**双字母 BK ≠ 单字母假设-K / 预检K**（本页只引用、不改写）。

### 专节 · 双字母 BM ≠ 单字母假设-M；且 ≠ 假设-BC；带过 BL≠BC、BK≠K（硬）

| 维度 | 对照页 | 本页假设-BM（双字母） |
|------|--------|----------------------|
| 题面 M | 盘后补成交 / 盘后固定价通道 | **追保通知后仍假可新开仓**误关：追保期内假可新开 vs 按生效日追保禁开 PIT |
| 题面 BC | 维持担保**低线**追保失败后**强制平仓**（invent_no_force_close） | 追保通知已发、**强平尚未触发**窗口内**禁止新开**融资/融券 |
| 题面 BL | 维持担保**高线**提取/转出限制（invent_unlimited_collateral_withdrawal；**BL≠BC**） | 追保禁新开；提取闸门 ≠ 新开禁令；**BM≠BL**；**带过 BL≠BC** |
| 题面 K / BK | K=融券空头**名单**；BK=客户**单票集中度**（**BK≠K**） | 追保禁开；本页**不覆盖** K/BK；**BM≠K≠BK**；**带过 BK≠K** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_new_open_after_margin_call` |
| 文档 | `假设-M-盘后补成交.md` / `假设-BC-…` / `假设-BL-…` / `假设-K-…` / `假设-BK-…`（**只读；禁止改写**） | `假设-BM-追保通知后仍假可新开仓误开.md`（新建） |
| 预检键 | 实验字母 M / BC / BL / K / BK | 实验字母 **BM** / `bm0_primary_demo`；**不得**占用或改写预检 M/BC/BL/K/BK |

**禁止**：把 BM 写成「M/BC/BL/K/BK 的续篇」；把「维持比例未触发强平」静默写成「追保期内可新开」；把「提取线未触 / 集中度未触顶 / 在融券名单内」静默写成「追保禁开已解除」；覆盖或补丁改写假设-M / 假设-BC / 假设-BL / 假设-K / 假设-BK 正文。

---

## 1. 一句话假设（可检验、可证伪）

同一拟新开/加仓融资或融券路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/融券名单/授信/维持强平/提取线输入（Z/BA/K/BH/BC/BL 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/融券名单/总授信/低维持强平/高维持提取」）下，把「追保通知后仍可任意新开两融、永不检查追保开仓禁令」或「全样本用核对日当天追保禁开规则（含券商当日更宽仍可开口径）回放历史」当成默认，相对「每个交易日按当时有效追保开仓禁令 PIT（维持担保比例低于追保线且追保未到位 → 新开拒开/记失败；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假可于追保期内新开路径并高估可执行两融名义、低估因追保禁开导致的开仓失败率**；差异应**集中在追保通知后仍假可新开仓误关桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假追保期新开贡献差、可执行名义差、失败率差在标定噪声带内可忽略，且「假追保期新开 / 核对日泄露 / 追保未到位仍开窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·K·AB·M·B·H·T」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 追保期内禁新开 ≠ 低维持强平；≠ 高维持提取；≠ 开仓保证金比例；≠ 客户单票集中度；≠ 授信额度；≠ 融资买入名单；≠ 转融券券源；≠ 担保品折算率；≠ 可充抵名单；≠ 融券所得用途；≠ 融资卖出还债优先；≠ 市场25pct暂停；≠ 合约期限；≠ 融券名单；≠ 盘后补成交；≠ 板上枯竭；≠ 证管费

```
# 配置写死键（见 §7；两条已冻结待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 BM；≠ 实验字母 A；≠ 实验字母 B；≠ 实验字母 M；≠ 实验字母 Z
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 BM
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 BM
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.margin_call_open_ban_honest     写死 pit_by_effective_date
# params.margin_call_line                写死 1.50
# params.margin_call_open_ban_scope      写死 new_fin_or_short_while_call_unmet
# params.margin_call_open_over_policy    写死 reject_or_fail
# params.broker_tighter_call_bucket      写死 separate_sensitivity
# params.margin_ratio_handoff            写死 z_page
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page
# params.haircut_handoff                 写死 bd_page
# params.balance_pause_handoff           写死 be_page
# params.contract_term_handoff           写死 bf_page
# params.collateral_list_handoff         写死 bg_page
# params.credit_quota_handoff            写死 bh_page
# params.short_proceeds_use_handoff      写死 bi_page
# params.financing_sale_repay_handoff    写死 bj_page
# params.client_conc_handoff             写死 bk_page
# params.collateral_withdraw_handoff     写死 bl_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.aft_fill_handoff                写死 m_page
# params.exit_period_handoff             写死 h_page
# params.bm0_primary_demo                写死冻结 invent_new_open_after_margin_call  # 主报：追保通知后仍可任意新开/永不检查追保开仓禁令；禁与 invent_asof_leak_margin_call_open_ban 双挂争主表；BM1半泄露不得升格并列主报
# params.bm0_invent_new_open_after_call  写死 True
# params.bm1_asof_leak_margin_call_open_ban_only 写死 True
# params.bm2_pit_margin_call_open_ban    写死 True
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
# params.merge_with_BK_client_conc       写死 False
# params.merge_with_BL_collateral_withdraw 写死 False
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_M_aft                写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_AD_50w               写死 False
# params.merge_with_AE_stock_t0          写死 False
# params.merge_with_T_csrc_fee           写死 False
# params.merge_with_S_handling_fee       写死 False
# params.merge_with_U_transfer_fee       写死 False
# params.merge_with_V_stamp_tax          写死 False
# params.merge_with_N_close_gtc          写死 False
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
# params.merge_with_BK_client_conc       写死 False
# params.merge_with_BL_withdraw          写死 False
# params.universe_rule                   写死 sse_szse_margin_call_open_ban_check
# params.missing_margin_call_open_ban_policy 写死 skip
# params.day_freq_proxy                  写死 margin_call_open_ban_eligibility_sensitivity
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母BM；params.G≠实验字母BM；params.N≠实验字母BM；亦≠单字母实验A/B/M/Z；禁null/holdout/跑后改口
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.fail_policy                     写死 skip
```

伪代码骨架：

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
margin_call_open_ban_honest = "pit_by_effective_date"
params.bm0_primary_demo = "invent_new_open_after_margin_call"  # 写死冻结；禁与 invent_asof_leak_margin_call_open_ban 双挂争主表；BM1半泄露不得升格并列主报
```

### 2.2 三组对照（BM0 / BM1 / BM2）

| 组 | 口径 | 说明 |
|----|------|------|
| BM0 天真 | `invent_new_open_after_margin_call`（单一主报·已冻结） | 追保通知后仍可任意新开融资/融券；永不检查追保开仓禁令 |
| BM1 半泄露 | `invent_asof_leak_margin_call_open_ban` | 仅用核对日追保禁开规则（含券商当日更宽仍可开口径）铺满全历史；**不得升格并列主报** |
| BM2 诚实 PIT | `pit_by_effective_date` | 按当日已生效追保开仓禁令；追保未到位仍开拒开/记失败；缺字段 skip |

### 2.3 标签与样本区间口径

- **样本主窗（写死）**：`date_start=2019-01-01` … `date_end=2026-09-30`（含两融通道全开后多年；本页不重开 Z/BA/K/BH/BC/BL）。  
- **oos_split（写死四日期；禁 holdout 反调）**：  
  - `is_start=2019-01-01` / `is_end=2024-12-31`  
  - `holdout_start=2025-01-01` / `holdout_end=2026-09-30`  
- **价基**：未复权。  
- **fill_time**：`next_open`。  
- **通道起日**：`margin_channel_start=2010-03-31`；此前 skip。  
- **规则生效**：细则/合同/券商风控表施行日或生效日；禁用核对日更宽「追保期内仍可新开」提前纳入。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

在 IS 窗内，BM0 相对 BM2 的假追保期新开贡献差、开仓失败率差超过 `params.Y` / `params.N` 标定带，且主贡献落在「追保通知后仍假可新开仓误关」桶；holdout 同向不反号到噪声带内。

### 3.2 失败（假设不成立 / 设计失效）

见 §5 失效条件。数值上若 ΔFakeNewOpenAfterMarginCall / ΔFail 在 `params.Y`/`params.G`/`params.N`/`params.Y2` 噪声带内可忽略，或分桶后主病迁到 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/K/AB/M/B/H/T，则本假设在该设定下不成立或设计失效。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 BM0 / BM1 / BM2。报告名义/路径质量差、假追保期新开贡献差、开仓失败率差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_new_open_after_margin_call",
  "invent_asof_leak_margin_call_open_ban",
  "call_unmet_still_open",
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
  "vs_BK_client_conc",
  "vs_BL_collateral_withdraw",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_M_aft_fill",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_T_csrc_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 缺追保状态/追保线字段却静默当「追保通知后仍可任意新开」→ 设计失效。  
2. 把「维持担保比例未触发强平 / 高于强平线」静默写成「追保期内可新开」且不声明另页 BC → **与 BC 撞题**（强平 ≠ 追保禁开；**尤其 BM≠BC**）。  
3. 把「维持担保比例够提取 / 高于提取线」静默写成「可新开」且不声明另页 BL → 与 BL 撞题（提取 ≠ 新开禁令；**尤其 BM≠BL**；**带过 BL≠BC**）。  
4. 把「开仓保证金比例够」静默写成「追保禁开解除」且不声明另页 Z → 与 Z 撞题。  
5. 把「总授信未用尽 / 集中度未触顶」静默写成「追保期内可新开」且不声明另页 BH/BK → 与 BH/BK 撞题；亦不得混读 K（**带过 BK≠K**）。  
6. 把「在融资买入名单内 / 转融券未暂停 / 市场未达25pct / 合约未到期 / 可充抵 / 折算率有值」静默写成「追保期内可新开」且不声明另页 BA/BB/BE/BF/BG/BD → 与对应页撞题。  
7. 把「融券所得用途放开 / 融资卖出还债优先放开」写成主病而不声明另页 BI/BJ → 与 BI/BJ 撞题。  
8. 把「在融券空头名单内」静默写成「追保期内可新开」且不声明另页 K → 与 K 撞题。  
9. 把「盘后补成交可成」写成主病而不声明另页 M → 与 M 撞题（**双字母 BM ≠ 单字母 M**）。  
10. 把「空头价限 / 当日平」写成主病而不声明另页 AB → 与 AB 撞题。  
11. 把「板上能否按板上价成交」写成主病而不声明另页 A → 与 A 撞题。  
12. 把「退市整理期当普通可交易」写成主病而不声明另页 H → 与 H 撞题。  
13. 把「追保通知后仍假可新开仓误关」写成「证管费误抽」→ **撞预检T旧题 / 假设-T**，设计失效。  
14. 把实验字母 BM 与单字母 A/B/M/K/Z 或双字母 BA–BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
15. holdout 反调 `bm0_primary_demo` / Y·G·N·Y2 → 结论无效。  
16. 用复权价算维持担保/可开名义 → 标签与执行双错，结论无效。  
17. 用核对日更宽「追保期内仍可开」当诚实 PIT、或把券商临时放宽追保禁开提前铺满历史 → 设计失效。  
18. **改写或覆盖 `假设-M` / `假设-BC` / `假设-BL` / `假设-K` / `假设-BK` / 已冻 AA–BL** → 硬边界违规，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户拟新开/加仓融资或融券腿名义；  
- 维持担保比例代理及是否已发**追保通知**/追保是否到位代理；  
- 当时有效**追保线**与**追保期内禁新开**规则及生效日（细则/合同/券商风控表；默认追保线约 150%）；  
- 开仓保证金比例 / 融资名单 / 融券名单 / 总授信 / 低维持强平 / 高维持提取输入（消费 Z/BA/K/BH/BC/BL 诚实 PIT，或显式旁路声明本页不重开）；  
- 交易日历。

可选：券商加严追保线；部分追保到位流水；追保宽限期另桶（本页主测禁新开，不主测宽限期长短）。

**禁止**：用核对日「今天追保期内仍可新开」铺满当唯一诚实组；用复权价；把开仓保证金比例/低维持强平/高维持提取/折算率/可充抵名单/融资名单/转融券通道暂停/市场余额25pct暂停/合约期限/总授信/融券所得用途/融资卖出还债优先/客户单票集中度当成追保禁开解除；把 Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/K/AB/A/M/B/H/T/AN–BL 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`BM`  
- **组**：BM0 / BM1 / BM2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`margin_call_open_ban_honest=pit_by_effective_date`；`margin_call_line=1.50`；`margin_call_open_ban_scope=new_fin_or_short_while_call_unmet`；`margin_call_open_over_policy=reject_or_fail`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`aft_fill_handoff=m_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_margin_call_open_ban_check`；`missing_margin_call_open_ban_policy=skip`；`day_freq_proxy=margin_call_open_ban_eligibility_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 BM**；**params.G≠实验字母 BM**；**params.N≠实验字母 BM**；亦≠单字母实验 A/B/M/Z；禁 null/holdout/跑后改口）；**`params.bm0_primary_demo` 写死冻结 `invent_new_open_after_margin_call`**（禁与 invent_asof_leak_margin_call_open_ban 双挂；BM1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- BM0/BM1/BM2 可执行名义/路径质量、ΔFakeNewOpenAfterMarginCall、ΔFail；分桶（追保期假新开误关 / 核对日泄露 / 追保未到位仍开窗 / 通道前 / vs A·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·K·AB·M·B·H·T）。  
- 自检布尔：BM2 是否 pit_by_effective_date；BM0 是否单一主报；BM1 是否仅核对日泄露；是否未与 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/K/AB/M/B/H/T 混主结论；holdout 是否未反调；**是否未把实验字母 BM 与 A 或 B 或 M 或 K 或 Z 或 BA–BL 或 params.Y 或 params.G 或 params.N 混用**；**是否未改 Y/Z/AA–BL 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-B / 假设-M / 假设-K / 假设-Z / 假设-BA–BL / 假设-AB**；**是否未再改 BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否带过并尊重 BL≠BC、BK≠K**。  
- **禁止输出**：具体买卖标的列表当「建议」；把追保禁开误关或核对日泄露冒充当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BL 及其他 A/D–BL 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-B**；**不改假设-M**；**不改假设-K**；**不改假设-Z**；**不改假设-BA–BL**；**不改假设-AB**；**勿再改 BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源（BB）、维持担保强平（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、融券空头名单（K）之外，**追保通知后禁新开**须按当时有效规则 PIT；不得默认追保期内仍可任意新开。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 BM** 标准件，**不改口径主线**，**不改假设 A–BL 正文**，**尤其不改假设-M / 假设-BC / 假设-BL / 假设-K / 假设-BK**。与实验 A/Z/BA/BB/BC/BD/BE/BF/BG/BH/BI/BJ/BK/BL/K/AB/M/B/H/T 分工：**A=板上枯竭门槛；Z=开仓保证金比例；BA=融资买入标的名单；BB=转融券暂停后券源；BC=维持担保比例强制平仓（低线）；BD=担保品折算率；BE=市场层单标的两融余额25pct暂停；BF=两融合约期限到期强制了结；BG=可充抵保证金证券名单；BH=两融授信额度上限；BI=融券卖出所得资金用途限制；BJ=融资买入卖出所得优先偿还融资负债；BK=客户单票两融集中度上限；BL=担保品提取转出限制；K=融券空头名单；AB=融券卖出价限；M=盘后补成交；B=历史实验B旧位；H=退市整理；T=证管费（避开）；BM=追保通知后仍假可新开仓误开（BM≠A≠B≠M≠K≠Z≠BA≠BB≠BC≠BD≠BE≠BF≠BG≠BH≠BI≠BJ≠BK≠BL≠AB≠T；带过 BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|-----|
| 文档状态 | 草稿 · 预检有条件通过 · 两条已冻结待复检 |
| 数据 | 待接入（字段见 §6；日频维持担保比例代理+追保通知/到位标记+拟新开名义+追保禁开规则生效日即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**margin_call_open_ban_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 BM；params.G≠实验字母 BM；params.N≠实验字母 BM；亦≠单字母实验 A/B/M/Z；禁 null/holdout/跑后改口）**；**bm0_primary_demo 写死冻结 invent_new_open_after_margin_call（禁双挂 invent_asof_leak_margin_call_open_ban；BM1半泄露不得升格并列主报）**；锚点保留 margin_call_open_ban_honest=pit_by_effective_date / margin_call_line=1.50 / margin_call_open_ban_scope=new_fin_or_short_while_call_unmet / margin_call_open_over_policy=reject_or_fail / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |

---

## 待预检键清单（两条已冻结 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已写死冻结**；**params.Y≠BM**；**params.G≠BM**；**params.N≠BM**；禁 null/holdout）  
2. `params.bm0_primary_demo` = `invent_new_open_after_margin_call`（**已写死冻结**；禁与 `invent_asof_leak_margin_call_open_ban` 双挂；BM1不升格主报）  
3. 追保禁开锚：`margin_call_open_ban_honest=pit_by_effective_date`；`margin_call_line=1.50`；`margin_call_open_ban_scope=new_fin_or_short_while_call_unmet`；`margin_call_open_over_policy=reject_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`  
4. 硬分列：≠B/M/A/Z/BA–BL/K/AB/H；**尤其 BM≠BC（追保禁开≠强平）**；**尤其 BM≠BL（追保禁开≠提取）**；**尤其 BM≠M**；**带过 BL≠BC、BK≠K**；避开预检T  
5. `oos_split` 四日期；`diff_buckets`；全部 `merge_with_*=False`

## 风控预检补丁·冻结（两条已写死 · 2026-11-03）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 BM**；**`params.G` ≠ 实验字母 BM**；**`params.N` ≠ 实验字母 BM**；**`params.Y` ≠ 单字母实验 A/B/M/Z**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.bm0_primary_demo`**：**写死冻结** **`invent_new_open_after_margin_call`**；禁与 **`invent_asof_leak_margin_call_open_ban`** 双挂争主表（只挂一个 primary）；**BM1 半泄露不得升格并列主报**。

**追保禁开锚保留（已通写死）**：`params.margin_call_open_ban_honest=pit_by_effective_date`；`params.margin_call_line=1.50`；`params.margin_call_open_ban_scope=new_fin_or_short_while_call_unmet`；`params.margin_call_open_over_policy=reject_or_fail`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有 `missing_margin_call_open_ban_policy=skip` 等锚点；不改口）。

**与 BA–BL/Z/AB/B/A/H/M/K 硬分列（保留）**：本页 = **追保通知后禁新开**；BC = **维持担保低线追保/强制平仓**（**尤其 BM≠BC**）；BL = **担保品提取/转出限制**（**尤其 BM≠BL**；高维持提取 ≠ 追保禁开；并**带过 BL≠BC**）；BK = **客户单票集中度**（**尤其 BM≠BK**；并**带过 BK≠K**）；M = **盘后补成交**（**尤其双字母 BM ≠ 单字母假设-M**）；K = **融券空头名单**（**尤其 BM≠K**）；Z = **开仓**保证金比例；BA/BB/BD/BE/BF/BG/BH/BI/BJ = 融资名单/转融券源/折算率/市场25pct/合约期限/可充抵名单/总授信/融券所得用途/融资卖出还债优先；A = **板上枯竭**；AB = **融券卖出价限**；B = 历史实验 B 旧位；H = **退市整理期**；追保禁开 ≠ 低维持强平 ≠ 高维持提取 ≠ 集中度 ≠ 盘后补成交 ≠ 融券名单 ≠ 开仓比例 ≠ 总授信 ≠ 板上枯竭 ≠ 空头价限 ≠ 退市整理；**双字母 BM ≠ 单字母 A ≠ 单字母 B ≠ 单字母 M ≠ 单字母 K ≠ 单字母 Z ≠ 双字母 BA ≠ … ≠ 双字母 BL ≠ 双字母 BC ≠ 双字母 BK ≠ 双字母 AB**；**params.Y ≠ 实验字母 BM**；**params.G ≠ 实验字母 BM**；**params.N ≠ 实验字母 BM**；禁止捆成「两融一张表=追保期内可任意新开」；**尤其不改假设-H**；**尤其不改假设-M**；**尤其不改假设-K**；不改假设-B；不改假设-Z；不改假设-BA–BL；不改假设-A；不改假设-AB；不改假设-BC；不改假设-BL。

**专节保留 · 双字母 BM ≠ 单字母假设-M；且 ≠ 假设-BC；带过 BL≠BC、BK≠K（硬）**：正文「### 专节 · 双字母 BM ≠ 单字母假设-M；且 ≠ 假设-BC；带过 BL≠BC、BK≠K」保留不删；**禁止**覆盖/混读/改写 `假设-M` / `假设-BC` / `假设-BL` / `假设-K` / `假设-BK`。

## 变更

- 2026-11-03：风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 BM**；**params.G≠实验字母 BM**；**params.N≠实验字母 BM**；亦≠单字母实验 A/B/M/Z；禁 null/holdout/跑后改口）；② `params.bm0_primary_demo=invent_new_open_after_margin_call`（禁与 `invent_asof_leak_margin_call_open_ban` 双挂争主表；BM1半泄露不得升格并列主报）。追保禁开锚保留：`margin_call_open_ban_honest=pit_by_effective_date`；`margin_call_line=1.50`；`margin_call_open_ban_scope=new_fin_or_short_while_call_unmet`；`margin_call_open_over_policy=reject_or_fail`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。与 BA–BL/Z/AB/B/A/H/M/K 硬分列保留；**专节保留 BM≠M / BM≠BC / BM≠BL / 带过 BL≠BC、BK≠K**。参考总管派令 / 风控预检有条件通过（`预检-假设BM-20261103.md`；草稿 HEAD=1b42bb6 只读对齐）。未改 Y/Z/AA–BL 及其他已冻结补丁；不改假设-H；不改假设-A；不改假设-B；不改假设-M；不改假设-K（尤其）；不改假设-Z；不改假设-BA–BL；不改假设-AB；不改假设-AZ；不改假设-AY；不改假设-AX；不改假设-AW；结论栏仍空；不开回测；不抢 A。

- 2026-11-03：新建纸面草稿（总管续派：BL 补丁已收 → 写假设-BM；自立 BM，勿占 BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/B/M/A/Z/K；避开预检T；不开回测；禁实盘/荐股；**params.Y/G/N≠实验字母 BM**；**双字母 BM ≠ 单字母 M**；**BM≠BC**；**BM≠BL**；**带过 BL≠BC、BK≠K**）。选题：追保通知后仍假可新开仓误开（正交于 BC 低维持强平 / BL 高维持提取 / BK 客户单票集中度 / Z 开仓比例）。
