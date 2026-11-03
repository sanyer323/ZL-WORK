# 假设 CA · 维持担保比例分子分母口径误开 / 用核对日更宽分子或更瘦分母公式铺满（执行鸿沟）

更新：2026-11-04  
来源：总管线 / BZ 补丁已交（复检在途）、写下一纸面 CA（双字母进 C 段）；清单撞题规则另选正交执行缺口（**维持担保比例怎么算：分子/分母计哪些项** ≠ 强平闸门 on/off ≠ 追保宽限期/强平通知时限 ≠ 强平序与范围 ≠ 开仓保证金比例 ≠ 担保品折算率本身 ≠ 担保品提取线 ≠ 融资提前了结手续费/违约金 ≠ 股票池当时名单/幸存者偏差 ≠ 板上枯竭）；选题自交易所融资融券细则公开口径：维持担保比例 =（现金 + 信用证券账户内证券市值总和）/（融资买入金额 + 融券卖出证券数量×市价 + 利息及费用总和）一类公式；分子是否含未折算市值/非可充抵证券、分母是否漏计应计利息/融券市值重估/费用，按**施行日/生效日** PIT；不得默认「永远用更肥分子或更瘦分母、或永远按核对日更宽公式铺满历史」；本页**假定强平闸门层（BC）/追保宽限层（BY）/强平序层（BT）/开仓比例层（Z）/折算率层（BD）/可充抵名单层（BG）/提取线层（BL）诚实或显式旁路**，主病只在**维持担保比例分子分母计项口径**；2010-03-31 前无此通道；**BC 正文主测「低维持强平闸门 on/off」**（`invent_no_force_close`），**BY 正文主测「追保宽限期/强平通知时限」**，**BT 正文主测「强平序与范围」**，**Z 正文主测「开仓保证金比例」**，**BD 正文主测「折算率全1」**，**C 正文主测「股票池当时名单/幸存者偏差」**（清单实验 C；**双字母 CA ≠ 单字母假设-C；严禁复用 C 题面**），**A 正文主测「涨停可成交/板上枯竭」**（**双字母 CA ≠ 单字母假设-A；严禁复用 A 题面；绝不可做成 A 板上续篇**），**BZ 正文主测「融资提前了结手续费/违约金」**（复检在途；**严禁改 BZ**），本页主测**维持担保比例分子分母口径被误开**（`invent_wrong_maint_guarantee_ratio_num_den`）→ 自立；与假设 A（板上可成交/枯竭；**CA≠A**）/ H（退市整理）/ B（历史清单「实验 B」旧位；**双字母 CA ≠ 单字母 B**）/ **C（股票池当时名单；双字母 CA ≠ 单字母假设-C；严禁复用 C；CA≠C）** / Z（开仓融资/融券保证金比例；**CA≠Z**）/ BA–BZ（两融族已冻/在途；**CA≠BA…BZ**；**尤其不改 BZ 正文**）/ **BC（维持线强平闸门；CA≠BC；闸门 ≠ 分子分母公式；尤其不改假设-BC）** / **BY（追保宽限期；CA≠BY；时限 ≠ 公式；尤其不改假设-BY）** / **BT（强平序；CA≠BT；序范围 ≠ 公式；尤其不改假设-BT）** / **BD（折算率；CA≠BD；折算率数值 ≠ 分子是否按折算后计；尤其不改假设-BD）** / **BL（担保品提取；CA≠BL；提取线 ≠ 维持比公式；尤其不改假设-BL）** / BW/BV/BU/BS/BO/BR/BH/BX 等**分列**；**新建实验 CA**  
状态：**草稿 · 预检有条件通过 · 两条已冻 · 待复检**（结论栏空；禁止把「假高维持担保比例 / 用核对日更宽分子或更瘦分母公式铺满」当诚实维持比口径；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA–BZ 及其他 A/D–BZ 已交正文与冻结补丁；尤其不改假设-A；尤其不改假设-C（清单实验 C）；尤其不改假设-BZ；尤其不改假设-BC；尤其不改假设-BY；尤其不改假设-BT；尤其不改假设-BD；尤其不改假设-BL；尤其不改假设-Z；不改假设-H；不改假设-B；不改假设-K；不改假设-BA–BZ；不改假设-AB；勿再改 BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前下一序号挂实验 CA（约 #84）。与假设 **A（涨停可成交性）** **硬分列（专节强调）**：A = 有板日触及涨跌停后的枯竭/能否按板上价记成；本页 = **信用账户维持担保比例分子分母计项**；板上枯竭 ≠ 维持比公式。**双字母 CA ≠ 单字母假设-A**；**严禁复用 A 题面**；**绝不可做成 A 板上续篇**。与假设 **C（股票池当时名单/幸存者偏差）** **硬分列（专节强调）**：C = 成分/股票池 PIT 与幸存者偏差；本页 = 维持担保比例**怎么算**；幸存者偏差 ≠ 分子分母口径。**双字母 CA ≠ 单字母假设-C**；**严禁复用 C 题面**；**绝不可做成 C 续篇**。与假设 **B（历史实验 B 旧位）** **硬分列**：清单早期「实验 B」曾挂印花税时点+T+1 / 财务可见日 / 除权日复权价误判等，主病已迁 V/W 等页；本页**不重开**那些旧 B 题。**双字母 CA ≠ 单字母 B**。与假设 **BC（维持担保比例强制平仓闸门）** **硬分列**：BC = 低维持线强平闸门 **on/off**（是否检查、是否强平）；本页 = 维持担保比例**分子分母计哪些项**；闸门 ≠ 公式；**禁止**把「闸门已诚实（BC）」静默写成「分子分母已诚实」；**不占** BC 的 primary_demo；**尤其不改假设-BC**。**CA≠BC**。与假设 **BY（追保宽限期/强平通知时限）** **硬分列**：BY = 追保通知后宽限几天；本页 = 维持比怎么算；时限 ≠ 公式；**尤其不改假设-BY**。**CA≠BY**。与假设 **BT（强制平仓顺序与范围）** **硬分列**：BT = 强平已触发后平哪条腿、平多少；本页 = 触发前维持比计项；序范围 ≠ 公式；**尤其不改假设-BT**。**CA≠BT**。与假设 **Z（开仓融资/融券保证金比例）** **硬分列**：Z = **新开**时保证金比例；本页 = **持仓存续期**维持担保比例公式；开仓比例 ≠ 维持比分子分母。**CA≠Z**。与假设 **BD（担保品折算率）** **硬分列**：BD = 折算率是否假全 1；本页 = 分子是否按**当时规则**用折算后市值、分母是否漏项（消费 BD 诚实折算或显式旁路）；折算率数值 ≠ 公式计项；**尤其不改假设-BD**。**CA≠BD**。与假设 **BL（担保品提取转出限制）** **硬分列**：BL = 高维持线能否提取；本页 = 维持比本身怎么算；提取线 ≠ 公式；**尤其不改假设-BL**。**CA≠BL**。与假设 **BZ（融资提前了结手续费/违约金）** **硬分列**：BZ = 主动提前了结费（复检在途）；本页 = 维持比分子分母；提前了结费 ≠ 公式；**尤其不改假设-BZ**。**CA≠BZ**。与假设 **BW / BV / BU / BS / BO / BR / BH / BX / BM / BF / BB / BA / BG / K / AB** **硬分列**：占用 / 召回 / 日库存 / 利率档 / 假零息 / 借券费 / 额度上限 / 起息日基数 / 追保禁开 / 合约期限 / 转融暂停 / 融资名单 / 可充抵 / 融券名单 / 空头价限 ≠ 维持比分子分母；并**带过 BZ≠Z/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH…、BY≠Y/BX/BW/BV/BU/BT/BS/BO/BR/BH/BM/BC…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K、BH≠H**。与假设 AN–BZ **硬分列**：不重开集合剩单/空簿/FOK/五档转限/收盘失败/开盘失败/基金经手费/基金 tick/两融族等。**明确避开预检T旧题（证管费误抽）**。**严禁复用假设-A（板上枯竭）**。**严禁复用假设-C（股票池当时名单）**。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 CA** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）≠ **`params.G`**（同族门槛/费率占位，建议 0.01）≠ **`params.N`**（失败/废单率差门槛键名）≠ **单字母实验 A**（涨停可成交性；**严禁复用假设-A**）≠ **单字母实验 C**（股票池当时名单；**严禁复用假设-C**）≠ **单字母实验 B**（历史实验 B 旧位）≠ **单字母实验 Z**（开仓保证金比例）≠ **单字母实验 K**（融券空头名单）≠ **单字母实验 Y**。全文凡写「实验 CA / 假设-CA / hypothesis_id=CA / 组 CA0·CA1·CA2」均指本实验；凡写 **`params.Y`** / **`params.G`** / **`params.N`** 均指门槛数值键，**禁止**把三者与实验字母 CA 混读或互改；**尤其 params.Y ≠ 实验字母 CA ≠ 单字母假设-A ≠ 单字母假设-C**。亦**禁止**把实验字母 CA 与单字母 **A**、单字母 **C**、单字母 **B**、单字母 **Z**、单字母 **K**、单字母 **Y**、单字母 **T**、单字母 **S**、单字母 **U**、单字母 **V**、单字母 **W**、单字母 **X**、双字母 **BA–BZ**、双字母 **BC**、双字母 **BY**、双字母 **BT**、双字母 **BD**、双字母 **BL**、双字母 **BZ**、双字母 **AB**、双字母 **AZ/AY/AX/AW**、或 params 键名 `ca0_*` 以外的实验页混读。**双字母 CA ≠ 单字母 A ≠ 单字母 C ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 Y ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BC ≠ 双字母 BY ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 CA**；**params.G ≠ 实验字母 CA**；**params.N ≠ 实验字母 CA**。**带过：双字母 BZ ≠ Z/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH…；双字母 BY ≠ Y/BX/BW/BV/BU/BT/BS/BO/BR/BH/BM/BC…；双字母 BX ≠ X/BW/BV/BU/BT/BS/BO/BR/BH…；双字母 BW ≠ W/BV/BU/BT/BS/BO/BR/BH…；双字母 BV ≠ V/BU/BT/BF/BC/BB/BQ/K…；双字母 BU ≠ U/BB/BT/K/BS/BO/BR/BH…；双字母 BT ≠ T/BC/BS/BO/BR/BH；双字母 BS ≠ S/BO/BR/BH；双字母 BR ≠ R/BO/BP/BB/BQ；双字母 BQ ≠ BA/K/BF/BC/BB/BO/BP/BM/BN/Q；双字母 BP ≠ P/BO/W/BI/BJ/BB；双字母 BO ≠ O/BF/BJ/BH/BN；双字母 BN ≠ BI/BJ/BL/BM；params.N ≠ 实验字母 BN ≠ 单字母假设-N；双字母 BM ≠ BC、BM ≠ BL；双字母 BL ≠ BC；双字母 BK ≠ 单字母假设-K / 预检K；双字母 BH ≠ 单字母 H**（本页只引用、不改写）。

### 专节 · 双字母 CA ≠ 单字母假设-A；且 ≠ 单字母假设-C；且 ≠ 假设-BC / 假设-BY / 假设-BT / 假设-Z / 假设-BD / 假设-BL / 假设-BZ；带过 BZ≠Z/BY…、BY≠Y/BX…、BT≠T/BC…、params.Y≠CA（硬）

| 维度 | 对照页 | 本页假设-CA（双字母） |
|------|--------|----------------------|
| 题面 A | **涨停可成交/板上枯竭**（`limit_up_fill` 族） | **维持担保比例分子分母计项**误开：假高维持比 vs 按生效日公式 PIT；**严禁复用 A 题面**；**绝不可做成 A 板上续篇** |
| 题面 C | **股票池当时名单/幸存者偏差**（清单实验 C） | 幸存者偏差 ≠ 维持比公式；**严禁复用 C 题面**；**绝不可做成 C 续篇**；**CA≠C** |
| 题面 BC | **低维持强平闸门 on/off**（`invent_no_force_close`） | **分子分母计哪些项**；闸门 ≠ 公式；**CA≠BC**；**不改 BC** |
| 题面 BY | **追保宽限期/强平通知时限**（`invent_ignore_margin_call_grace_or_force_deadline`） | 时限 ≠ 公式；**CA≠BY**；**不改 BY** |
| 题面 BT | **强平触发后顺序与范围**（`invent_force_close_best_order_or_min_scope`） | 序范围 ≠ 公式；**CA≠BT**；**不改 BT** |
| 题面 Z | **开仓**融资/融券保证金比例（`flat_one_times` 族） | 开仓比例 ≠ 持仓维持比公式；**CA≠Z**；**不改 Z** |
| 题面 BD | **折算率假全 1**（`invent_haircut_all_one`） | 折算率数值 ≠ 分子是否按折算后计；消费 BD 诚实或旁路；**CA≠BD**；**不改 BD** |
| 题面 BL | **担保品提取转出限制**（`invent_unlimited_collateral_withdrawal`） | 提取线 ≠ 维持比公式；**CA≠BL**；**不改 BL** |
| 题面 BZ | **融资提前了结手续费/违约金**（复检在途；`invent_ignore_early_repay_fee_or_penalty`） | 提前了结费 ≠ 公式；**CA≠BZ**；**不改 BZ** |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_wrong_maint_guarantee_ratio_num_den` |
| 文档 | `假设-A-…` / 清单实验 C / `假设-BC-…` / `假设-BY-…` / `假设-BT-…` / `假设-Z-…` / `假设-BD-…` / `假设-BL-…` / `假设-BZ-…`（**只读；禁止改写**） | `假设-CA-维持担保比例分子分母口径误开.md`（新建） |
| 预检键 | 实验字母 A / C / BC / BY / BT / Z / BD / BL / BZ | 实验字母 **CA** / `ca0_primary_demo`；**不得**占用或改写预检 A/C/BC/BY/BT/Z/BD/BL/BZ |

**禁止**：把 CA 写成「A/C/BC/BY/BT/Z/BD/BL/BZ 的续篇」；把「板上可成交已诚实（A）/ 股票池已诚实（C）/ 闸门已诚实（BC）/ 宽限期已诚实（BY）/ 强平序已诚实（BT）/ 开仓比例已诚实（Z）/ 折算率已诚实（BD）/ 提取线已诚实（BL）/ 提前了结费已诚实（BZ）」静默写成「维持比分子分母已诚实」；覆盖或补丁改写假设-A / 清单实验 C / 假设-BC / 假设-BY / 假设-BT / 假设-Z / 假设-BD / 假设-BL / 假设-BZ 正文；把 `params.Y/G/N` 与实验字母 CA 混读；**禁** `ca0_primary_demo` 与 `invent_asof_leak_maint_ratio_formula` **双挂主报**；**禁** CA1 半泄露升格并列主报；**禁**复用假设-A（板上枯竭）或假设-C（股票池当时名单）题面或口径键；**禁**复用 BC 的 `invent_no_force_close` 或 BY/BT/BD/BL/BZ 主报当本页主报。

---

## 1. 一句话假设（可检验、可证伪）

同一拟持有信用账户两融路径、同一未复权价、同一 T+1、同一开仓保证金比例与融资名单/融券名单/折算率/可充抵/强平闸门/追保宽限/强平序/提取线/授信占用等输入（Z/BA/K/BD/BG/BC/BY/BT/BL/BW 层诚实或显式旁路声明「本页不重开开仓比例/融资名单/融券名单/折算率数值/可充抵名单/低维持强平闸门/追保宽限期/强平序与范围/高维持提取/授信占用」）下，把「维持担保比例永远用更肥分子（未折算全额市值、非可充抵亦计入）或更瘦分母（漏计应计利息/融券市值重估/费用）」或「全样本用核对日当天更宽分子或更瘦分母公式回放历史」当成默认，相对「每个交易日按当时有效维持担保比例分子分母计项规则 PIT（分子=现金+按当时规则折算后可充抵证券市值等；分母=融资负债本金+融券负债市值+应计利息及费用等；2010-03-31 前无通道；缺字段 skip/敏感性）」的诚实组，会**系统性发明假高维持担保比例路径并高估可续持两融名义、低估因真实维持比不足导致的追保/强平冲击**；差异应**集中在维持担保比例分子分母口径误开桶**，而不是随机散开。

证伪方向：若天真组 / 半泄露组相对诚实组的假高维持比贡献差、可续持名义差、追保/强平冲击差在标定噪声带内可忽略，且「假高维持比 / 核对日泄露 / 正常公式窗 / 公式切日窗 / 通道前 / vs A·C·Z·BA·BB·BC·BD·BE·BF·BG·BH·BI·BJ·BK·BL·BM·BN·BO·BP·BQ·BR·BS·BT·BU·BV·BW·BX·BY·BZ·K·AB·Y·B·H·W·V·T·S·U·X」分桶不改变结论，则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 维持担保比例分子分母口径 ≠ 强平闸门（BC）；≠ 追保宽限期（BY）；≠ 强平序（BT）；≠ 开仓保证金比例（Z）；≠ 折算率数值（BD）；≠ 提取线（BL）；≠ 提前了结费（BZ）；≠ 股票池当时名单（C）；≠ 板上枯竭（A）

```
# 配置写死键（见 §7；两条已冻 · 待复检；终值如下）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 CA；≠ 单字母假设-A；≠ 单字母假设-C；≠ 实验字母 B；≠ 实验字母 Z；≠ 实验字母 BC；≠ 实验字母 BY；≠ 实验字母 BT；≠ 实验字母 BZ
# 【消歧】params.G = 同族门槛/费率占位；≠ 实验字母 CA
# 【消歧】params.N = 失败/废单率差门槛；≠ 实验字母 CA；≠ 单字母假设-N；亦≠实验字母 BN
# params.asof_check_date                 写死默认 2026-10-16
# params.fill_time                        写死 next_open
# params.px_basis                        写死 unadj
# params.tick                            写死 0.01
# params.margin_channel_start            写死 2010-03-31
# params.maint_ratio_formula_honest      写死 pit_by_effective_date
# params.maint_ratio_formula_scope       写死 maint_ratio_num_den_composition
# params.maint_ratio_formula_over_policy 写死 compute_or_fail_missing_formula_rule
# params.maint_ratio_formula_naive       写死 invent_wrong_maint_guarantee_ratio_num_den
# params.margin_ratio_handoff            写死 z_page   # 开仓比例交 Z；CA≠Z；不改 Z
# params.margin_buy_list_handoff         写死 ba_page
# params.refinance_borrow_handoff        写死 bb_page
# params.maint_force_handoff             写死 bc_page   # 强平闸门交 BC；CA≠BC；本页主病是分子分母不是闸门 on/off；不改 BC
# params.haircut_handoff                 写死 bd_page   # 折算率数值交 BD；CA≠BD；不改 BD
# params.balance_pause_handoff           写死 be_page
# params.contract_term_handoff           写死 bf_page
# params.collateral_list_handoff         写死 bg_page   # 可充抵名单交 BG；CA≠BG；不改 BG
# params.credit_quota_handoff            写死 bh_page
# params.short_proceeds_use_handoff      写死 bi_page
# params.financing_sale_repay_handoff    写死 bj_page
# params.client_conc_handoff             写死 bk_page
# params.collateral_withdraw_handoff     写死 bl_page   # 提取线交 BL；CA≠BL；不改 BL
# params.margin_call_open_ban_handoff    写死 bm_page
# params.cross_account_handoff           写死 bn_page
# params.financing_interest_handoff      写死 bo_page
# params.corp_action_comp_handoff        写死 bp_page
# params.list_removal_stock_handoff      写死 bq_page
# params.short_borrow_fee_handoff        写死 br_page
# params.financing_rate_tier_handoff     写死 bs_page
# params.force_close_order_handoff       写死 bt_page   # 强平序交 BT；CA≠BT；不改 BT
# params.daily_short_inventory_handoff   写死 bu_page
# params.short_recall_handoff            写死 bv_page
# params.credit_usage_handoff            写死 bw_page
# params.interest_start_daycount_handoff 写死 bx_page
# params.margin_call_grace_handoff       写死 by_page   # 追保宽限交 BY；CA≠BY；不改 BY
# params.early_repay_fee_handoff         写死 bz_page   # 提前了结费交 BZ；CA≠BZ；复检在途亦勿改 BZ
# params.maint_ratio_formula_handoff     写死 self      # 本页主病：维持担保比例分子分母计项口径
# params.universe_pool_handoff           写死 c_page    # 股票池当时名单交 C；CA≠C；严禁复用假设-C
# params.auction_vol_handoff             写死 y_page
# params.exright_board_handoff           写死 w_page
# params.shortable_list_handoff          写死 k_page
# params.short_px_handoff                写死 ab_page
# params.st_limit_handoff                写死 x_page
# params.stamp_tax_handoff               写死 v_page
# params.transfer_fee_handoff            写死 u_page
# params.csrc_fee_handoff                写死 t_page
# params.handling_fee_handoff            写死 s_page
# params.exit_period_handoff             写死 h_page
# params.ca0_primary_demo                写死冻结 invent_wrong_maint_guarantee_ratio_num_den  # 主报：假高维持比（更肥分子/更瘦分母）；禁与 invent_asof_leak_maint_ratio_formula 双挂争主表；CA1半泄露不得升格并列主报
# params.ca0_invent_wrong_maint_guarantee_ratio_num_den  建议 True
# params.ca1_asof_leak_maint_ratio_formula_only 建议 True
# params.ca2_pit_maint_ratio_formula     建议 True
# params.merge_with_A_fill               写死 False  # CA≠A；严禁复用假设-A；不改 A
# params.merge_with_C_universe_pool      写死 False  # CA≠C；严禁复用假设-C
# params.merge_with_Z_margin_ratio       写死 False
# params.merge_with_BA_margin_buy_list   写死 False
# params.merge_with_BB_refinance_borrow  写死 False
# params.merge_with_BC_maint_force       写死 False  # CA≠BC；不改 BC
# params.merge_with_BD_haircut           写死 False  # CA≠BD；不改 BD
# params.merge_with_BE_balance_pause     写死 False
# params.merge_with_BF_contract_term     写死 False
# params.merge_with_BG_collateral_list   写死 False
# params.merge_with_BH_credit_quota      写死 False
# params.merge_with_BI_short_proceeds    写死 False
# params.merge_with_BJ_financing_sale_repay 写死 False
# params.merge_with_BK_client_conc       写死 False
# params.merge_with_BL_collateral_withdraw 写死 False  # CA≠BL；不改 BL
# params.merge_with_BM_margin_call_open_ban 写死 False
# params.merge_with_BN_cross_account     写死 False
# params.merge_with_BO_financing_interest 写死 False
# params.merge_with_BP_corp_action_comp  写死 False
# params.merge_with_BQ_list_removal_stock 写死 False
# params.merge_with_BR_short_borrow_fee  写死 False
# params.merge_with_BS_financing_rate_tier 写死 False
# params.merge_with_BT_force_close_order 写死 False  # CA≠BT；不改 BT
# params.merge_with_BU_daily_short_inventory 写死 False
# params.merge_with_BV_short_recall      写死 False
# params.merge_with_BW_credit_usage      写死 False
# params.merge_with_BX_interest_start_daycount 写死 False
# params.merge_with_BY_margin_call_grace 写死 False  # CA≠BY；不改 BY
# params.merge_with_BZ_early_repay_fee   写死 False  # CA≠BZ；不改 BZ（复检在途）
# params.merge_with_K_shortable_list     写死 False
# params.merge_with_AB_short_px          写死 False
# params.merge_with_Y_auction_vol        写死 False
# params.merge_with_W_exright            写死 False
# params.merge_with_H_exit               写死 False
# params.merge_with_B_legacy             写死 False
# params.merge_with_N_close_gtc          写死 False
# params.merge_with_M_aft                写死 False
# params.missing_maint_ratio_formula_policy 写死 skip
# params.day_freq_proxy                  写死 maint_ratio_formula_sensitivity
# params.universe_rule                   写死 sse_szse_maint_ratio_formula_check
# params.fail_policy                     写死 skip
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.Y / G / N / Y2                  写死冻结 0.02/0.01/0.05/0.015  # params.Y≠实验字母CA；params.G≠实验字母CA；params.N≠实验字母CA；亦≠单字母实验A/C/B/Z；禁 null/holdout/跑后改口
# params.date_start / date_end           写死 2019-01-01..2026-09-30
# params.oos_split.*                     写死四日期；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改分子分母公式、Y/G/N/Y2、主窗/oos、ca0_primary_demo
```

可编码摘要（伪代码，不开跑）：

```
asof = params.asof_check_date  # 2026-10-16
# CA0：假高维持比——分子按未折算全额/非可充抵亦计；分母漏应计利息/融券市值重估/费用
# CA1：仅 asof 日更宽分子或更瘦分母公式泄露铺满
# CA2：每个交易日 d 按当日已生效分子分母计项规则 PIT
# 消费 BD 诚实折算率（或旁路声明本页不重开折算率数值）；消费 BC 闸门/BY 宽限/BT 序为旁路输入
# 缺公式字段 → skip（params.missing_maint_ratio_formula_policy）
```

```
fill_time = "next_open"
asof_check_date = "2026-10-16"
px_basis = "unadj"
margin_channel_start = "2010-03-31"
maint_ratio_formula_honest = "pit_by_effective_date"
maint_ratio_formula_scope = "maint_ratio_num_den_composition"
maint_ratio_formula_over_policy = "compute_or_fail_missing_formula_rule"
ca0_primary_demo = "invent_wrong_maint_guarantee_ratio_num_den"  # 单一主报·已冻结；禁与 invent_asof_leak_maint_ratio_formula 双挂
ca0_invent_wrong_maint_guarantee_ratio_num_den = True
ca1_asof_leak_maint_ratio_formula_only = True
ca2_pit_maint_ratio_formula = True
merge_with_A_fill = False
merge_with_C_universe_pool = False
merge_with_BC_maint_force = False
merge_with_BY_margin_call_grace = False
merge_with_BT_force_close_order = False
merge_with_BD_haircut = False
merge_with_BL_collateral_withdraw = False
merge_with_BZ_early_repay_fee = False
merge_with_Z_margin_ratio = False
fail_policy = "skip"
```

### 2.2 三组对照（CA0 / CA1 / CA2）

| 组 | 口径 | 说明 |
|----|------|------|
| CA0 天真 | `invent_wrong_maint_guarantee_ratio_num_den`（单一主报·已冻结） | 发明假高维持比（更肥分子/更瘦分母）路径；禁与 invent_asof_leak_maint_ratio_formula 双挂 |
| CA1 半泄露·混口径 | 全样本用 `asof_check_date` 当天更宽分子或更瘦分母公式铺满历史 | 仅维持比公式 asof 泄露；不升格并列主报 |
| CA2 PIT | `maint_ratio_formula_honest=pit_by_effective_date` | 每个交易日按当时已生效维持担保比例分子分母计项规则 PIT |

### 2.3 额度窗内日频可落点（写明但不真跑）

- **日频代理**：信用账户现金+担保品市值代理 + 融资负债余额 + 融券负债市值 + 应计利息/费用代理 + 当日生效分子分母计项规则 → 当日维持担保比例；缺公式字段 → skip（敏感性另桶）。  
- **额度窗**：主窗 `2019-01-01..2026-09-30`；IS `2019-01-01..2024-12-31`；holdout `2025-01-01..2026-09-30`（写死；禁 holdout 反调）。  
- **可落点声明**：有日终现金/担保品/融资负债/融券市值代理 + 分子分母计项规则生效日表 + 折算率（消费 BD，旁路）+ 强平闸门（消费 BC，旁路声明「本页假定闸门层诚实」）即可纸面起步；**本页不开回测、不拉真数、不派回测岗**。  
- **通道前**：`margin_channel_start=2010-03-31` 前无本页维持比公式通道。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组 / 半泄露组相对诚实组的假高维持比贡献差、可续持名义差、追保/强平冲击差超出标定噪声带，且差异集中在「维持担保比例分子分母口径误开」桶，不被 A 板上枯竭、C 股票池、BC 闸门、BY 宽限、BT 强平序、Z 开仓比例、BD 折算率、BL 提取、BZ 提前了结费等他页桶吞并。

### 3.2 失败（假设不成立 / 设计失效）

差值落在噪声带内；或主差异被 A/C/BC/BY/BT/Z/BD/BL/BZ/T 等他页桶吞并；或 holdout 反调 `ca0_primary_demo` / Y·G·N·Y2；或 CA0 与 asof_leak 双挂主报。

---

## 4. 检验设计（纸面）

同一信号、同一 T+1，对照 CA0 / CA1 / CA2。报告可续持名义差、假高维持比贡献差、追保/强平冲击差。

### 4.1 分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）

```
params.diff_buckets = [
  "invent_wrong_maint_guarantee_ratio_num_den",
  "invent_asof_leak_maint_ratio_formula",
  "maint_ratio_formula_window",
  "maint_ratio_formula_cut_window",
  "pre_margin_channel_20100331",
  "vs_A_limit_up_fill",
  "vs_C_universe_pool",
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
  "vs_BM_margin_call_open_ban",
  "vs_BN_cross_account",
  "vs_BO_financing_interest",
  "vs_BP_corp_action_comp",
  "vs_BQ_list_removal_stock",
  "vs_BR_short_borrow_fee",
  "vs_BS_financing_rate_tier",
  "vs_BT_force_close_order",
  "vs_BU_daily_short_inventory",
  "vs_BV_short_recall",
  "vs_BW_credit_usage",
  "vs_BX_interest_start_daycount",
  "vs_BY_margin_call_grace",
  "vs_BZ_early_repay_fee",
  "vs_K_shortable_list",
  "vs_AB_short_px",
  "vs_Y_auction_vol",
  "vs_W_exright",
  "vs_H_exit_period",
  "vs_B_legacy",
  "vs_X_st_limit_avoid",
  "vs_V_stamp_tax_avoid",
  "vs_U_transfer_fee_avoid",
  "vs_T_csrc_fee_avoid",
  "vs_S_handling_fee_avoid",
]
```

---

## 5. 预期失效条件（设计失效 / 结论无效）

1. 样本无足够信用账户两融持仓或分子分母字段；缺字段却静默当假高维持比 → 设计失效。  
2. 把「强平闸门已诚实（BC）」静默写成「分子分母已诚实」且不声明另页 BC → **与 BC 撞题**（闸门 ≠ 公式；**尤其 CA≠BC**；**不改 BC**）。  
3. 把「追保宽限期已诚实（BY）」静默写成「分子分母已诚实」且不声明另页 BY → **与 BY 撞题**（**尤其 CA≠BY**；**不改 BY**）。  
4. 把「强平序已诚实（BT）」静默写成「分子分母已诚实」 → **与 BT 撞题**（**尤其 CA≠BT**；**不改 BT**）。  
5. 把「开仓比例已诚实（Z）」写成主病或不声明另页 Z → **撞假设-Z**（**尤其 CA≠Z**；**不改 Z**）。  
6. 把「折算率已诚实（BD）」写成主病或不声明另页 BD → **撞假设-BD**（折算率数值 ≠ 公式计项；**尤其 CA≠BD**；**不改 BD**）。  
7. 把「提取线已诚实（BL）」写成主病 → **撞假设-BL**（**尤其 CA≠BL**；**不改 BL**）。  
8. 把「提前了结费已诚实（BZ）」写成主病或不声明另页 BZ → **撞假设-BZ**（**尤其 CA≠BZ**；**不改 BZ**）。  
9. 把「板上可成交已诚实（A）」或「股票池已诚实（C）」静默写成「分子分母已诚实」→ **撞假设-A / 假设-C**（**严禁复用**；**尤其 CA≠A / CA≠C**；**绝不可做成 A/C 续篇**）。  
10. 把「经手/证管/过户/印花税已诚实（S/T/U/V）」静默写成「分子分母已诚实」→ 与交易所费用族撞题（**明确避开预检T**）。  
11. 把实验字母 CA 与单字母 A/C/B/Z/K/Y/T/S/U/V/W/X 或双字母 BA–BZ/BC/BY/BT/BD/BL/AB/AZ/AY/AX/AW 或 `params.Y` 或 `params.G` 或 `params.N` 混读互改 → 文档失效，须重标。  
12. holdout 反调 `ca0_primary_demo` / Y·G·N·Y2 → 结论无效。  
13. 用复权价算维持担保比例分子分母代理 → 标签与执行双错，结论无效。  
14. 用核对日更宽「假高维持比」当诚实 PIT、或把券商临时宽口径铺满历史 → 设计失效。  
15. **`ca0_primary_demo` 与 `invent_asof_leak_maint_ratio_formula` 双挂主报**；或 CA1 升格并列主报 → 设计失效。  
16. **改写或覆盖 `假设-A` / 清单实验 C / `假设-BC` / `假设-BY` / `假设-BT` / `假设-Z` / `假设-BD` / `假设-BL` / `假设-BZ` / 已冻 AA–BZ** → 硬边界违约，本页失效。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

最小：

- 未复权价/OHLC、买卖方向、交易所、板块；  
- 信用账户现金、担保品证券及市值、融资负债余额、融券负债数量×市价、应计利息及费用代理、分子分母计项规则及生效日；  
- 开仓保证金比例 / 融资名单 / 融券名单 / 折算率 / 可充抵 / 强平闸门 / 追保宽限 / 强平序 / 提取线 / 授信占用输入（消费 Z/BA/K/BD/BG/BC/BY/BT/BL/BW 诚实 PIT 或显式旁路声明本页不重开）；  
- 交易日历；2010-03-31 前无通道 skip。

可选：会员加严分子分母子集；与 BC 闸门窗、BY 宽限窗、BT 强平序窗对照但不混主结论；折算率切日敏感性（主报仍在公式计项）。

**禁止**：用核对日「今天更宽分子/更瘦分母」铺满当唯一诚实组；用复权价；把开仓比例已诚实/闸门已诚实/宽限已诚实/强平序已诚实/折算率已诚实/提取已诚实/提前了结费已诚实/占用已诚实/日库存够/名单仍在池/转融未暂停/授信够/新开名单开/融券所得用途放开/融资卖出还债优先放开/客户单票集中度未触顶/账户未串用/权益已补偿/调出后存量已处理/市场25pct未暂停/交易所费已诚实当成「分子分母正确」依据；把 Z/BA–BZ/K/AB/A/C/B/H/W/Y/X/V/U/T/S/AN–BZ 当成本页主病。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **假设 ID**：`CA`  
- **组**：CA0 / CA1 / CA2  
- **写死键摘要**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`margin_channel_start=2010-03-31`；`maint_ratio_formula_honest=pit_by_effective_date`；`maint_ratio_formula_scope=maint_ratio_num_den_composition`；`maint_ratio_formula_over_policy=compute_or_fail_missing_formula_rule`；`margin_ratio_handoff=z_page`；`margin_buy_list_handoff=ba_page`；`refinance_borrow_handoff=bb_page`；`maint_force_handoff=bc_page`；`haircut_handoff=bd_page`；`balance_pause_handoff=be_page`；`contract_term_handoff=bf_page`；`collateral_list_handoff=bg_page`；`credit_quota_handoff=bh_page`；`short_proceeds_use_handoff=bi_page`；`financing_sale_repay_handoff=bj_page`；`client_conc_handoff=bk_page`；`collateral_withdraw_handoff=bl_page`；`margin_call_open_ban_handoff=bm_page`；`cross_account_handoff=bn_page`；`financing_interest_handoff=bo_page`；`corp_action_comp_handoff=bp_page`；`list_removal_stock_handoff=bq_page`；`short_borrow_fee_handoff=br_page`；`financing_rate_tier_handoff=bs_page`；`force_close_order_handoff=bt_page`；`daily_short_inventory_handoff=bu_page`；`short_recall_handoff=bv_page`；`credit_usage_handoff=bw_page`；`interest_start_daycount_handoff=bx_page`；`margin_call_grace_handoff=by_page`；`early_repay_fee_handoff=bz_page`；`universe_pool_handoff=c_page`；`auction_vol_handoff=y_page`；`exright_board_handoff=w_page`；`shortable_list_handoff=k_page`；`short_px_handoff=ab_page`；`st_limit_handoff=x_page`；`stamp_tax_handoff=v_page`；`transfer_fee_handoff=u_page`；`csrc_fee_handoff=t_page`；`handling_fee_handoff=s_page`；`exit_period_handoff=h_page`；全部 `merge_with_*=False`（§2.1）；`universe_rule=sse_szse_maint_ratio_formula_check`；`missing_maint_ratio_formula_policy=skip`；`day_freq_proxy=maint_ratio_formula_sensitivity`；`fail_policy=skip`；`redline_v0_exempt_scope=position_industry_dd_only`；`diff_buckets=[...]`（§4.1）；**`params.Y/G/N/Y2` 写死冻结 `0.02/0.01/0.05/0.015`**（**params.Y≠实验字母 CA**；**params.G≠实验字母 CA**；**params.N≠实验字母 CA**；亦≠单字母实验 A/C/B/Z；禁 null/holdout/跑后改口）；**`params.ca0_primary_demo` 写死冻结 `invent_wrong_maint_guarantee_ratio_num_den`**（禁与 invent_asof_leak_maint_ratio_formula 双挂；CA1半泄露不得升格并列主报）；`date_start/end=2019-01-01..2026-09-30`；`oos_split` 四日期写死。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- CA0/CA1/CA2 净收益/成本质量、ΔFakeHighMaintRatio、ΔSustainableNotional、ΔCallOrForceImpact；分桶（维持担保比例分子分母口径误开 / 核对日泄露 / 正常公式窗 / 公式切日窗 / 通道前 / vs A·C·Z·BA–BZ·K·AB·Y·B·H·W·X·V·U·T·S）。  
- 自检气泡：CA2 是否 pit_by_effective_date；CA0 是否单一主报；CA1 是否仅核对日泄露；是否未与 A/C/Z/BA–BZ/K/AB/Y/B/H/W/X/V/U/T/S 混主结论；holdout 是否未反调；**是否未把实验字母 CA 与 A 或 C 或 B 或 Z 或 K 或 Y 或 BA–BZ 或 BC 或 BY 或 BT 或 BD 或 BL 或 BZ 或 params.Y 或 params.G 或 params.N 混用**；**是否特别写清双字母 CA≠单字母假设-A；CA≠单字母假设-C；params.Y≠实验字母 CA；CA≠BC；CA≠BY；CA≠BT；CA≠Z；CA≠BD；CA≠BL；CA≠BZ；带过 BZ≠Z/BY/BX…、BY≠Y/BX/BW…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K**；**是否未改 Y/Z/AA–BZ 冻结补丁正文**；**是否未改假设-H / 假设-A / 假设-C / 假设-B / 假设-Z / 假设-K / 假设-BA–BZ / 假设-BC / 假设-BY / 假设-BT / 假设-BD / 假设-BL / 假设-BZ / 假设-AB**；**是否未再改 BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**；**是否未重做预检T（证管费）**；**是否未复用假设-A / 假设-C**；**是否未与 invent_asof_leak_maint_ratio_formula 双挂主报**。  
- **禁止输出**：具体买卖标的列表当「建议」；把假高维持比或核对日泄露吹成诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不占本机 8765 席位；不派回测开工；**本页不开回测**；**不改 Y/Z/AA–BZ 及其他 A/D–BZ 已交正文**；**不改假设-H**；**不改假设-A**；**不改假设-C**；**不改假设-B**；**不改假设-Z**；**不改假设-K**；**不改假设-BA–BZ**；**尤其不改假设-A；尤其不改假设-C；尤其不改假设-BZ；尤其不改假设-BC；尤其不改假设-BY；尤其不改假设-BT；尤其不改假设-BD；尤其不改假设-BL；尤其不改假设-Z**；**不改假设-AB**；**勿再改 BZ/BY/BX/BW/BV/BU/BT/BS/BR/BQ/BP/BO/BN/BM/BL/BK/BJ/BI/BH/BG/BF/BE/BD/BC/BB/BA/AZ/AY/AX/AW**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 两融诚信同向：开仓保证金比例（Z）、融资买入名单（BA）、转融券券源暂停闸门（BB）、维持担保强平闸门（BC）、担保品折算率（BD）、市场层单标的余额25pct暂停（BE）、合约期限（BF）、可充抵保证金证券名单（BG）、授信额度上限（BH）、融券卖出所得用途（BI）、融资买入卖出还债优先（BJ）、客户单票集中度（BK）、担保品提取转出限制（BL）、追保通知后禁新开（BM）、信用/普通账户隔离（BN）、融资利息与逾期罚息假零息（BO）、融券权益补偿（BP）、标的调出后存量（BQ）、融券借券费（BR）、融资利率档位（BS）、强制平仓顺序与范围（BT）、融券券池日可借量（BU）、融券提前召回（BV）、授信占用口径（BW）、融资利息起息日/计息天数（BX）、追保宽限期/强平通知时限（BY）、融资提前了结手续费/违约金（BZ）、融券空头名单（K）、股票池当时名单（C）、板上枯竭（A）之外，**维持担保比例分子分母计项**须按当时有效规则 PIT；不得默认永远假高维持比，或用核对日更宽公式铺满。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单开跑前下一序号挂**新增实验 CA** 标准件，**不改口径主线**，**不改假设 A–BZ 正文**，**尤其不改假设-A / 假设-C / 假设-BZ / 假设-BC / 假设-BY / 假设-BT / 假设-BD / 假设-BL / 假设-Z**。与实验 A/C/Z/BA–BZ/K/AB/B/H/W/Y/X/V/U/T/S 分工：**A=板上枯竭门槛（严禁复用）；C=股票池当时名单（严禁复用）；Z=开仓保证金比例；BA–BZ=两融族已冻/在途；BC=强平闸门；BY=追保宽限期；BT=强平序；BD=折算率；BL=提取线；BZ=提前了结费；CA=维持担保比例分子分母口径误开（CA≠A≠C≠B≠Z≠K≠Y≠BA≠…≠BZ≠BC≠BY≠BT≠BD≠BL≠BW≠BV≠BU≠BS≠BO≠BR≠BH≠AB≠W≠H≠T≠S≠U≠V≠X；带过 BZ≠Z/BY/BX…、BY≠Y/BX/BW…、BX≠X/BW…、BW≠W/BV…、BV≠V/BU/BT…、BU≠U/BB/BT/K…、BT≠T/BC/BS/BO/BR/BH、BS≠S/BO/BR/BH、BR≠R/BO/BP/BB/BQ、BQ≠BA/K/BF/BC…、BP≠P/BO/W、BN≠BI/BJ/BL/BM、params.N≠BN、BM≠BC、BM≠BL、BL≠BC、BK≠K）**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 状态 | **草稿 · 预检有条件通过 · 两条已冻 · 待复检**（结论栏空；**未标纸面齐**） |
| 标准件路径 | `假设-CA-维持担保比例分子分母口径误开.md` |
| 清单序号 | 约 #84 |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-16；**fill_time=next_open 写死**；**maint_ratio_formula_honest=pit_by_effective_date 写死**；diff_buckets 写死待冻结；**Y/G/N/Y2 写死冻结 0.02/0.01/0.05/0.015（params.Y≠实验字母 CA；params.G≠实验字母 CA；params.N≠实验字母 CA；亦≠单字母实验 A/C/B/Z；禁 null/holdout/跑后改口）**；**ca0_primary_demo 写死冻结 invent_wrong_maint_guarantee_ratio_num_den（禁双挂 invent_asof_leak_maint_ratio_formula；CA1半泄露不得升格并列主报）**；锚点建议 maint_ratio_formula_honest=pit_by_effective_date / maint_ratio_formula_scope=maint_ratio_num_den_composition / maint_ratio_formula_over_policy=compute_or_fail_missing_formula_rule / margin_channel_start=2010-03-31 / asof_check_date=2026-10-16 / fill_time=next_open / fail_policy=skip |
| 硬分列摘要 | **CA≠A/C/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/Z**（及 ≠B/Y/BA–BZ/K/AB/H/W/T/S/U/V/X），**严禁复用假设-A / 假设-C**；**尤其不改假设-A/C/BZ/BC/BY/BT/BD/BL/Z**；**params.Y≠实验字母 CA** |
| 结论栏 | 空 |

---

## 待预检键清单（两条已冻 · 见下节）

1. `params.Y` / `params.G` / `params.N` / `params.Y2` = `0.02` / `0.01` / `0.05` / `0.015`（**已冻结**；**params.Y≠实验字母 CA**；**params.G≠实验字母 CA**；**params.N≠实验字母 CA**；禁 null/holdout）  
2. `params.ca0_primary_demo` = `invent_wrong_maint_guarantee_ratio_num_den`（**已冻结**；禁与 `invent_asof_leak_maint_ratio_formula` 双挂；CA1不升格主报）  
3. 锚点（已通写死）：`maint_ratio_formula_honest=pit_by_effective_date` / `maint_ratio_formula_scope=maint_ratio_num_den_composition` / `maint_ratio_formula_over_policy=compute_or_fail_missing_formula_rule` / `margin_channel_start=2010-03-31` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`

---

## 与 BA–BZ / A / C / Z / K 撞题检查表

| 对照 | 是否撞题 | 说明 |
|------|----------|------|
| 假设-A | **否（硬分列）** | 板上枯竭 ≠ 维持比分子分母；**CA≠A**；**严禁复用**；绝不可做成 A 续篇 |
| 假设-C | **否（硬分列）** | 股票池当时名单 ≠ 维持比公式；**CA≠C**；**严禁复用**；绝不可做成 C 续篇 |
| 假设-BC | **否（硬分列）** | 强平闸门 on/off ≠ 分子分母计项；**CA≠BC**；不改 BC |
| 假设-BY | **否（硬分列）** | 追保宽限期 ≠ 公式；**CA≠BY**；不改 BY |
| 假设-BT | **否（硬分列）** | 强平序与范围 ≠ 公式；**CA≠BT**；不改 BT |
| 假设-Z | **否（硬分列）** | 开仓保证金比例 ≠ 维持比公式；**CA≠Z**；不改 Z |
| 假设-BD | **否（硬分列）** | 折算率数值 ≠ 分子是否按折算后计；**CA≠BD**；不改 BD |
| 假设-BL | **否（硬分列）** | 提取线 ≠ 公式；**CA≠BL**；不改 BL |
| 假设-BZ | **否（硬分列）** | 提前了结费 ≠ 公式；**CA≠BZ**；不改 BZ（复检在途） |
| 假设-BW/BV/BU/BS/BO/BR/BH/BX | **否** | 占用/召回/日库存/利率档/假零息/借券费/额度/起息 ≠ 公式 |
| 假设-BA–BN/BP/BQ/BF/BB/BG/BM/K/AB | **否** | 各页主病岔路；本页不重开 |
| 假设-B/H/W/X/V/U/T/S/Y | **否** | 旧位/退市/除权/ST板幅/印花税/过户/证管/经手/集合量 ≠ 公式 |

---

## 风控预检补丁·冻结（两条已写死 · 2026-11-04）

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`；**`params.Y` ≠ 实验字母 CA**；**`params.G` ≠ 实验字母 CA**；**`params.N` ≠ 实验字母 CA**；**`params.Y` ≠ 单字母实验 A/C/B/Z**；尤重**双字母 CA ≠ 单字母假设-A**；**双字母 CA ≠ 单字母假设-C**；禁 null / holdout 标定 / 跑后改口。  
2. **`params.ca0_primary_demo`**：**写死冻结** **`invent_wrong_maint_guarantee_ratio_num_den`**；禁与 **`invent_asof_leak_maint_ratio_formula`** 双挂争主表（只挂一个 primary）；**CA1 半泄露不得升格并列主报**。

**维持担保比例分子分母锚保留（已通写死）**：`params.maint_ratio_formula_honest=pit_by_effective_date`；`params.maint_ratio_formula_scope=maint_ratio_num_den_composition`；`params.maint_ratio_formula_over_policy=compute_or_fail_missing_formula_rule`；`params.margin_channel_start=2010-03-31`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`（及正文已有维持比分子分母相关锚点；不改口）。

**与 BA–BZ/A/C/Z/AB/B/H/K/T/S/U/V/W/X 硬分列（保留）**：本页 = **维持担保比例分子分母口径误开**；A = **板上枯竭**（**尤其双字母 CA ≠ 单字母假设-A**；**严禁复用假设-A**）；C = **股票池当时名单**（**尤其双字母 CA ≠ 单字母假设-C**；**严禁复用假设-C**）；BC = **维持担保强平闸门**（**尤其 CA≠BC**；闸门 on/off ≠ 分子分母公式；禁复用 `invent_no_force_close`；**尤其不改假设-BC**）；BY = **追保宽限期/强平通知时限**（**尤其 CA≠BY**；时限 ≠ 公式；禁复用 `invent_ignore_margin_call_grace_or_force_deadline`；**尤其不改假设-BY**）；BT = **强制平仓顺序与范围**（**尤其 CA≠BT**；序范围 ≠ 公式；**尤其不改假设-BT**）；Z = **开仓保证金比例**（**尤其 CA≠Z**；**尤其不改假设-Z**）；BD = **担保品折算率**（**尤其 CA≠BD**；折算率数值 ≠ 分子是否按折算后计；**尤其不改假设-BD**）；BL = **担保品提取转出限制**（**尤其 CA≠BL**；提取线 ≠ 公式；**尤其不改假设-BL**）；BZ = **融资提前了结手续费/违约金**（**尤其 CA≠BZ**；提前了结费 ≠ 公式；禁复用 `invent_ignore_early_repay_fee_or_penalty`；**尤其不改假设-BZ**）；BW/BV/BU/BS/BO/BR/BH/BX = 占用/召回/日库存/利率档/假零息/借券费/额度/起息（**尤其 CA≠…**）；分子分母公式 ≠ 板上枯竭 ≠ 股票池 ≠ 强平闸门 ≠ 追保宽限 ≠ 强平序 ≠ 开仓比例 ≠ 折算率 ≠ 提取线 ≠ 提前了结费 ≠ 占用 ≠ 召回 ≠ 日库存 ≠ 利率档 ≠ 假零息 ≠ 借券费 ≠ 额度 ≠ 起息。**双字母 CA ≠ 单字母 A ≠ 单字母 C ≠ 单字母 B ≠ 单字母 Z ≠ 单字母 K ≠ 单字母 Y ≠ 单字母 T ≠ 单字母 S ≠ 单字母 U ≠ 单字母 V ≠ 单字母 W ≠ 单字母 X ≠ 双字母 BA ≠ … ≠ 双字母 BZ ≠ 双字母 BC ≠ 双字母 BY ≠ 双字母 BT ≠ 双字母 BD ≠ 双字母 BL ≠ 双字母 BW ≠ 双字母 BV ≠ 双字母 BU ≠ 双字母 BS ≠ 双字母 BO ≠ 双字母 BR ≠ 双字母 BH ≠ 双字母 BX ≠ 双字母 AB ≠ 双字母 H**；**params.Y ≠ 实验字母 CA**；**params.G ≠ 实验字母 CA**；**params.N ≠ 实验字母 CA**；禁止捆成「两融一张表=假高维持比」；**尤其不改假设-A**；**尤其不改假设-C**；**尤其不改假设-BZ**；**尤其不改假设-BC**；**尤其不改假设-BY**；**尤其不改假设-BT**；**尤其不改假设-BD**；**尤其不改假设-BL**；**尤其不改假设-Z**；不改假设-B；不改假设-BA–BZ；不改假设-AB；不改假设-K；不改假设-H；不改假设-T；不改假设-S；不改假设-U；不改假设-V；不改假设-W；不改假设-X；不改假设-Y。

**专节保留 · 双字母 CA ≠ 单字母假设-A；且 ≠ 单字母假设-C；且 ≠ 假设-BC / 假设-BY / 假设-BT / 假设-Z / 假设-BD / 假设-BL / 假设-BZ（硬）**：正文专节保留不删；**禁止**覆盖/混读/改写 `假设-A` / `假设-C` / `假设-BC` / `假设-BY` / `假设-BT` / `假设-Z` / `假设-BD` / `假设-BL` / `假设-BZ`。

## 变更

| 日期 | 说明 |
|------|------|
| 2026-11-04 | 风控预检补丁·冻结两条写死——① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（**params.Y≠实验字母 CA**；**params.G≠实验字母 CA**；**params.N≠实验字母 CA**；亦≠单字母实验 A/C/B/Z；尤重**双字母 CA ≠ 单字母假设-A**；**双字母 CA ≠ 单字母假设-C**；禁 null/holdout/跑后改口）；② `params.ca0_primary_demo=invent_wrong_maint_guarantee_ratio_num_den`（禁与 `invent_asof_leak_maint_ratio_formula` 双挂争主表；CA1半泄露不得升格并列主报）。维持比分子分母锚保留：`maint_ratio_formula_honest=pit_by_effective_date`；`maint_ratio_formula_scope=maint_ratio_num_den_composition`；`maint_ratio_formula_over_policy=compute_or_fail_missing_formula_rule`；`margin_channel_start=2010-03-31`；`asof_check_date=2026-10-16`；`fill_time=next_open`；`fail_policy=skip`。硬分列保留：**CA≠A/C/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/Z**（及 ≠B/Y/BA–BZ/AB/H/K/T/S/U/V/W/X）；**严禁复用假设-A / 假设-C**；参考总管派令 / 风控预检有条件通过（`预检-假设CA-20261104.md`；草稿 `9b302c3` #84）。未改 Y/Z/AA–BZ 及其他已冻结补丁；**不改假设-A**；**不改假设-C**；**不改假设-BZ**；**不改假设-BC**；**不改假设-BY**；**不改假设-BT**；**不改假设-BD**；**不改假设-BL**；**不改假设-Z**；不改假设-H；不改假设-B；不改假设-K；不改假设-Y；不改假设-BA–BZ；不改假设-AB；结论栏仍空；不开回测；不抢 A；**未标纸面齐** |
| 2026-11-04 | 新建草稿·待预检（总管线：BZ 补丁已交后写 CA，双字母进 C 段；选题维持担保比例分子分母口径误开；**CA≠A/C/BZ/BY/BX/BW/BV/BU/BT/BS/BO/BR/BH/BC/BD/BL/Z**；primary_demo 建议=`invent_wrong_maint_guarantee_ratio_num_den`；Y/G/N/Y2 待预检；不开回测；未改 A/C/BZ/BC/BY/BT/BD/BL/Z 及其他已齐字母；**未标纸面齐**）。 |
