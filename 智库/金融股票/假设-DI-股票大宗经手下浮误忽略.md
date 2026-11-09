# 假设-DI · 股票大宗经手下浮误忽略（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `ec654b33` 上清单 #117=DH 已收口（A/D–DH纸面齐已合入该 tip；**不改假设-DH 正文**，亦不改已齐 A–DH / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-T / 假设-S / 假设-AX / 假设-O / 假设-AC / 假设-R / 假设-I 及其他已存在假设页；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**）后写下一草稿 DI；清单 #117=DH，本页占用 **#118=DI**；选题是股票大宗经手费相对竞价标准的下浮被忽略、按竞价全额抽；假设-S 只收竞价经手费切日（其「降幅 30%」≠ 本页「大宗折扣 30%」），假设-AX 只收基金档（基金大宗下浮 50%），假设-O 只收大宗通道，假设-DH 只收佣金双计，假设-DG 只收北交所档；**新建实验 DI**；不写下一字母；不预留下一号  
状态：**A/D–DI纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「股票大宗经手费按竞价全额抽、从而忽略大宗相对竞价标准下浮 30%」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改已齐 A–DH / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG**；尤其不改假设-S / 假设-AX / 假设-O / 假设-DH / 假设-DG / 假设-DF / 假设-DE / 假设-DD / 假设-DC / 假设-DB / 假设-DA / 假设-T / 假设-AC / 假设-R / 假设-D / 假设-I；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DI（#118）。一句话误开：回测把股票大宗经手费按竞价全额抽（忽略大宗相对竞价标准下浮 30%），或缺成交类型 / 官方‰仍不 skip，系统性改写大宗腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DI** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DI**；**勿把 `params.Y` 读成实验字母 DI**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DI**；**尤重：`params.G` 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是大宗经手费率，也不是竞价经手费率）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DI**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DI ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 I**（价格笼子远限价；**双字母 DI ≠ 单字母假设-I；严禁复用假设-I**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DI ≠ 单字母假设-A**）≠ **单字母实验 T**（证管费主报股票；**双字母 DI ≠ 单字母假设-T；严禁复用假设-T；不重开假设-T**）≠ 双字母 **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债经手费沪深分列）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **S**（沪深股票竞价经手费切日）≠ **AX**（基金经手费；基金大宗下浮 50%）≠ **O**（大宗通道 / 假流动性）≠ **AC**（北交所涨跌幅与盘后）≠ **U**（股票过户费）≠ **V**（股票印花税）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）。**DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠O≠AC≠T≠U≠V≠Q≠R≠A≠D**。**双字母 DI ≠ 单字母 D/I**。**params.Y/G/N ≠ 实验字母 DI；亦 ≠ 单字母 D/I**。**勿把 `params.G` 读成实验字母 DI，亦勿把单字母假设-D / 假设-I 读成双字母 DI**。**尤重：`params.G` 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰**。**股票大宗折扣 ≠ S切日 ≠ AX基金大宗50% ≠ O通道 ≠ DH双计**。**尤重：S 的「降幅 30%」≠ 本页「大宗折扣 30%」——禁止合成/混读升格进 `di0`**。

### 专节 · 双字母 DI ≠ 单字母假设-D / 假设-I；且 ≠ 假设-S / 假设-AX / 假设-O / 假设-DH（硬）

| 维度 | 对照页 | 本页假设-DI（双字母） |
|------|--------|----------------------|
| 题面 S | **沪深 A 股竞价经手费切日**（2023-08-28 的「降幅 30%」是竞价档下调，不是大宗折扣） | 切日降幅 ≠ 大宗折扣。本页专测：股票大宗经手费被按竞价全额抽。**DI≠S**；**不改 S**；**禁把 S 的「降幅 30%」与本页「大宗折扣 30%」合成/混读升格进 `di0`**；`ashare_fee_handoff=s_page`；诊断桶 `vs_S_auction_handling` / `confuse_S_cut30_with_block_discount30` 不升格 |
| 题面 AX | **基金/ETF 经手费档**；基金大宗按竞价下浮 **50%** | 基金大宗 50% ≠ 股票大宗 30%。**DI≠AX**；**不改 AX**；`fund_block_fee_handoff=ax_page`；诊断桶 `vs_AX_fund_block_50` 不升格 |
| 题面 O | **大宗通道 / 假流动性**（量价并进竞价、三条盘后通道） | 通道 ≠ 经手下浮。**DI≠O**；**不改 O**；`block_channel_handoff=o_page`；诊断桶 `vs_O_block_channel` 不升格 |
| 题面 DH | **佣金已含代收费再外加经手费** | 双计 ≠ 大宗折扣。**DI≠DH**；**不改 DH**；`commission_double_handoff=dh_page` |
| 题面 DG | **北交所经手费档**（与沪深分列） | 北交所档 ≠ 股票大宗折扣。**DI≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DF | **可交换债经手费沪深分列** | 可交换债经手费 ≠ 本机制。**DI≠DF**；**不改 DF**；`exch_handling_fee_handoff=df_page` |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 本机制。**DI≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债过户费** | 转债过户费 ≠ 本机制。**DI≠DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DC | **可转债印花税** | 转债印花税 ≠ 本机制。**DI≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 DB | **可转债经手费** | 转债经手费 ≠ 本机制。**DI≠DB**；**不改 DB**；`cb_handling_fee_handoff=db_page` |
| 题面 DA | **场内基金过户费** | 场内基金过户 ≠ 本机制。**DI≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page` 只旁路消费 |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 大宗经手下浮。**DI≠AC**；**不改 AC**；**不重开假设-AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 T | **证管费主报股票** | 证管费 ≠ 大宗经手下浮。**DI≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`csrc_fee_handoff=t_page` |
| 题面 U | **股票过户费** | 过户费下浮 ≠ 经手下浮。**DI≠U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 V | **股票印花税** | 印花税 ≠ 大宗经手下浮。**DI≠V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 大宗经手下浮。**DI≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 大宗经手下浮。**DI≠R**；**不改 R**；**不重开假设-R**；`stock_etf_rotation_handoff=r_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 大宗经手下浮。**DI≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 大宗经手是否按下浮。**双字母 DI ≠ 单字母假设-D**；**严禁复用假设-D**；**DI≠D**；**不改 D** |
| 题面 I | **价格笼子远限价** | 远限价进簿 ≠ 大宗经手下浮。**双字母 DI ≠ 单字母假设-I**；**严禁复用假设-I**；**不改 I**；`price_cage_handoff=i_page` |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_full_handling_fee_on_stock_block`（**写死冻结**单一主报，单挂写死；禁与 `invent_asof_leak_stock_block_handling` 双挂；DI1 不升格；`ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel` 只作诊断对照，不升格主报；**尤重禁止把 S 切日降幅 30% 与大宗折扣 30% 合成进 `di0`**） |
| 文档 | 清单实验 S / AX / O / DH / DG / DF / DE / DD / DC / DB / DA / AC / T / U / V / Q / R / A / D / I（**只读；禁止改写**） | `假设-DI-股票大宗经手下浮误忽略.md`（新建） |
| 预检键 | 实验字母 S / AX / O / DH / DG / DF / DE / DD / DC / DB / DA / AC / T / U / V / Q / R / A / D / I / Y / G / N | 实验字母 **DI** / `di0_primary_demo`；**不得**占用或改写预检 S/AX/O/DH/DG/DF/DE/DD/DC/DB/DA/AC/T/U/V/Q/R/A/D/I |

**禁止**：把 DI 写成「S / AX / O / DH / DG / DF / DE / DD / DC / DB / DA / AC / T / U / V / Q / R / A / D / I 的续篇」；把「竞价切日已诚实（S）/ 基金大宗 50% 已诚实（AX）/ 大宗通道已分列（O）/ 佣金双计已诚实（DH）/ 北交所档已诚实（DG）」写成「股票大宗经手下浮已诚实」；把实验字母 DI 与单字母 D/I 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-I 读成双字母 DI**；**尤重勿把 `params.G` 读成实验字母 DI**；**尤重 `params.G` 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰（量纲与语义不同）**；**尤重 S 的「降幅 30%」≠ 本页「大宗折扣 30%」，禁止合成/混读升格进 `di0`**；把 `invent_asof_leak_stock_block_handling` 升格进 `di0` 或与主报双挂；把诊断桶 `ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel` 升格进 `di0`。本页主键只用 `di0` / `di1` / `di2` 与 `stock_block_handling_*`。不写下一字母。不预留下一号。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权成交金额下，回测把股票大宗经手费按竞价全额抽（忽略大宗相对当时竞价标准下浮 30%），或缺成交类型 / 官方‰仍不 skip，相对「缺成交类型或官方‰则 skip；大宗按竞价标准下浮、不按全额抽」的诚实组，会**系统性改写大宗腿成本**——相对诚实锚偏误。

核对日方向（随锚写死；禁止把 0.002387% 写成全历史唯一费率）：大宗按竞价标准下浮 30% → 现行 **0.002387% 双向**。这不是把 0.002387% 铺满全历史。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、全额截在标定噪声带内可忽略，且「忽略下浮 / 抄竞价全额 / 把 S 切日 30% 混成大宗折扣 / 核对日泄露 / vs S·AX·O·DH」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · di0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DI ≠ 单字母假设-D / 假设-I**；勿把 params.Y 读成实验字母 DI
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DI ≠ 单字母 D/I**
# 【消歧】尤重：params.G 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰（量纲与语义不同：无量纲相对门槛 ≠ 大宗经手费率% ≠ 竞价经手费率‰）
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DI ≠ 单字母 D/I**
# params.Y2 写死冻结 0.015
# params.Y / G / N / Y2               写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 全额截 ΔStockBlockHandling / 净收益差 / DI1−DI2；**params.Y/G/N ≠ 实验字母 DI ≠ 单字母假设-D / 假设-I**；**尤重 params.G 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成费率）
# params.fill_time                    写死冻结 next_open
# params.asof_check_date              写死冻结 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  写死冻结 skip
# params.stock_block_handling_honest  写死冻结 pit_auction_minus_30pct_not_full
#   诚实锚方向（已写死冻结；禁止把 0.002387% 写成全历史唯一费率）：
#   大宗按当时竞价标准下浮 30%，不按竞价全额抽
#   核对日方向：现行 0.002387% 双向
#   缺成交类型或官方‰ → skip
#   禁止把核对日 0.002387% 铺满全历史（那是半泄露，不得进 di0）
#   枚举已写死冻结
#   不把 S 的竞价切日降幅、AX 的基金大宗 50%、O 的通道、DH 的双计写成大宗折扣诚实锚
# params.stock_block_handling_scope   写死冻结 sse_szse_ashare_block_apart_from_auction
#   沪深 A 股股票大宗经手，与竞价档分开
#   股票大宗折扣 ≠ 竞价切日（S）≠ 基金大宗 50%（AX）≠ 大宗通道（O）≠ 佣金双计（DH）≠ 北交所档（DG）
# params.stock_block_handling_over_policy 写死冻结 skip_if_trade_type_or_official_bps_missing
#   缺成交类型或官方‰则 skip；禁在缺字段时仍按竞价全额抽
# params.ashare_fee_handoff           建议 s_page
#   消费 S 的沪深股票竞价经手费切日，或显式旁路；切日降幅 ≠ 大宗折扣；不改 S
#   S 的「降幅 30%」与本页「大宗折扣 30%」禁止合成/混读升格进 di0；不改 S
# params.fund_block_fee_handoff       建议 ax_page
#   消费 AX 的基金大宗下浮 50%，或显式旁路；基金大宗 50% ≠ 股票大宗 30%；不改 AX
#   诊断桶 vs_AX_fund_block_50 不得升格进 di0
# params.block_channel_handoff        建议 o_page
#   消费 O 的大宗通道/假流动性，或显式旁路；通道 ≠ 经手下浮；不改 O
#   诊断桶 vs_O_block_channel 不得升格进 di0
# params.commission_double_handoff    建议 dh_page
#   消费 DH 的佣金双计，或显式旁路；双计 ≠ 大宗折扣；不改 DH
# params.bse_fee_handoff              建议 dg_page
#   消费 DG 的北交所经手费档，或显式旁路；北交所档 ≠ 股票大宗折扣；不改 DG
# params.exch_handling_fee_handoff    建议 df_page
#   消费 DF 的可交换债经手费沪深分列，或显式旁路；不改 DF
# params.cb_csrc_fee_handoff          建议 de_page
#   消费 DE 的转债证管费，或显式旁路；不改 DE
# params.cb_transfer_fee_handoff      建议 dd_page
#   消费 DD 的转债过户费，或显式旁路；不改 DD
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的转债印花税，或显式旁路；不改 DC
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的可转债经手费，或显式旁路；不改 DB
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；不改 DA
# params.bse_limit_aft_handoff        建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；不重开假设-AC；不改 AC
# params.csrc_fee_handoff             建议 t_page
#   消费 T 的股票证管费，或显式旁路；不在本页重开假设-T，也不改 T
# params.stock_transfer_fee_handoff   建议 u_page
# params.stock_stamp_handoff          建议 v_page
# params.cb_rule_handoff              建议 q_page
# params.stock_etf_rotation_handoff   建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 大宗经手下浮；不重开假设-R；不改 R
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
#   成交时点与停牌交 D；双字母 DI ≠ 单字母假设-D；不改 D
# params.price_cage_handoff           建议 i_page
#   价格笼子交 I；双字母 DI ≠ 单字母假设-I；不改 I
# params.stock_block_handling_handoff 建议 self
# params.di0_primary_demo             写死冻结 invent_full_handling_fee_on_stock_block
#   单一主报写死，单挂；禁与 invent_asof_leak_stock_block_handling 双挂；DI1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_stock_block_handling 只作对照，不得升格进 di0，不得双挂
#   诊断桶 ignore_30pct_block_discount / copy_auction_tier_onto_block / confuse_S_cut30_with_block_discount30 / vs_S_auction_handling / vs_AX_fund_block_50 / vs_O_block_channel 不得升格进 di0
#   尤重：禁止把 S 切日「降幅 30%」与本页「大宗折扣 30%」合成/混读后写进 di0
# params.di0_invent_full_handling_fee_on_stock_block 建议 True
# params.di1_asof_leak_stock_block_handling_only 建议 True
#   半泄露对照；DI1 不升格并列主报；不得把 invent_asof_leak_stock_block_handling 写进 di0
# params.di2_pit_auction_minus_30pct  建议 True
# params.merge_with_S                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_O                 建议 False
# params.merge_with_DH                建议 False
# params.merge_with_DG                建议 False
# params.merge_with_DF                建议 False
# params.merge_with_DE                建议 False
# params.merge_with_DD                建议 False
# params.merge_with_DC                建议 False
# params.merge_with_DB                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_AC                建议 False
# params.merge_with_T                 建议 False
# params.merge_with_U                 建议 False
# params.merge_with_V                 建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_R                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_I                 建议 False
# params.missing_trade_type_or_bps_policy 建议 skip
# params.day_freq_proxy               建议 stock_block_handling_discount_sensitivity
# params.universe_rule                建议 stock_block_handling_discount_check
# params.redline_v0_exempt_scope      建议 position_industry_di_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DI；勿把这个键读成实验 DI
#   不另挂主报，不预留下一号，不写下一字母
```

### 2.2 三组对照（DI0 / DI1 / DI2）

| 组 | 角色 | 口径 |
|----|------|------|
| DI0 | 天真 / 按竞价全额抽 | 按 `di0_primary_demo` **写死冻结**单一主报 `invent_full_handling_fee_on_stock_block`：股票大宗经手费按竞价全额抽，忽略下浮。**禁**与 `invent_asof_leak_stock_block_handling` 双挂主报。**禁把 S 切日降幅 30% 与大宗折扣 30% 合成进 `di0`**（只作对照/旁路，不得升格进 `di0` 或另挂主报） |
| DI1 | 半泄露 | 仅核对日把现行大宗经手（方向：0.002387% 双向，或现行下浮开关）铺到全历史（`invent_asof_leak_stock_block_handling`）；**不得升格并列主报**，也不得写进 `di0`（写死冻结：DI1 不升格），不得双挂 |
| DI2 | 诚实 / 按下浮、不按全额 | `stock_block_handling_honest=pit_auction_minus_30pct_not_full`（写死冻结）：缺成交类型或官方‰则 skip；大宗按当时竞价标准下浮 30%，不按全额抽。核对日方向是现行 0.002387% 双向，不铺满全历史。竞价切日只消费 S，基金大宗 50% 只消费 AX，大宗通道只消费 O，佣金双计只消费 DH，北交所档只消费 DG，或显式旁路 |

忽略下浮、把竞价档抄到大宗、把 S 的切日降幅 30% 混成大宗折扣 30%，以及相对 S / AX / O 的对照截（`ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `di0_primary_demo`。`confuse_S_cut30_with_block_discount30` 只标记「有人把 S 的降幅 30% 和本页大宗折扣 30% 合成/混读」这一类失效，**不得升格进 `di0`**。S 的切日、AX 的基金大宗 50%、O 的通道、DH 的双计只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`di0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺成交类型或官方‰则 skip；大宗按竞价标准下浮 30%，不按竞价全额抽。核对日方向：现行 **0.002387% 双向**；**不要写成全历史唯一费率**，也不要把这个数铺满全历史。竞价切日留在 S：S 的「降幅 30%」是 2023-08-28 竞价档下调，不是本页大宗折扣。基金大宗 50% 留在 AX，大宗通道留在 O，佣金双计留在 DH，北交所档留在 DG，都不改。可交换债经手费留在 DF，转债证管费留在 DE，转债过户费留在 DD，转债印花税留在 DC，转债经手费留在 DB，场内基金过户留在 DA，都不改。`params.G` 的 0.01 是无量纲相对门槛，不是大宗 0.002387%，也不是竞价 0.0341‰。缺成交类型或官方‰则 skip，不用竞价全额或自造‰把腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `di0_primary_demo` / `params.Y`·G·N·Y2 / 下浮开关 / 桶 / 0.002387% 是否铺历史）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DI0）/ 半泄露组（DI1）相对诚实组（DI2）的成本差、全额截**显著且集中在按竞价全额抽的桶**；分桶「忽略下浮 / 抄竞价全额 / S 切日 30% 与大宗折扣 30% 混读 / 核对日泄露 / vs S·AX·O·DH」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 0.002387% 冻成全历史唯一费率。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 S 的竞价切日、AX 的基金大宗 50%、O 的大宗通道、DH 的佣金双计、DG 的北交所档、DF 的可交换债经手费、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、DA 的场内基金过户、AC 的北交所涨跌幅与盘后、T 的证管费、U/V 的股票过户与印花税、Q 的回转与涨跌幅、R 的股票 ETF 回转、A 的板上容量、D 的成交时点、I 的价格笼子解释；或 `di0_primary_demo` 与 `invent_asof_leak_stock_block_handling` 双挂；或 DI1 升格并列主报；或 `ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel` 诊断桶升格主报；或把 S 的「降幅 30%」与本页「大宗折扣 30%」合成进 `di0`；或实验字母 DI 与单字母 D/I 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成大宗 0.002387% 或竞价 0.0341‰；或把核对日 0.002387% 铺满全历史冒充唯一费率；或缺成交类型 / 官方‰仍按全额抽；或重开假设-T / 假设-AC / 假设-R。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DI0/DI1/DI2。沪深股票竞价经手费走 S 的诚实切日或显式旁路，不在本页改 S，也不把 S 的切日降幅 30% 升成主报。报告成本差、全额截。不把 0.002387% 标成全历史唯一费率。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_full_handling_fee_on_stock_block` / `invent_asof_leak_stock_block_handling` / `ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel` / `missing_trade_type_or_official_bps_not_skip` / `vs_DH_commission_double` / `vs_DG_bse_handling` / `vs_DF_exch_handling` / `vs_DE_cb_csrc` / `vs_DD_cb_transfer` / `vs_DC_cb_stamp` / `vs_DB_cb_handling` / `vs_DA_etf_transfer` / `vs_AC_bse_limit_aft` / `vs_T_stock_csrc` / `vs_U_stock_transfer` / `vs_V_stock_stamp` / `vs_Q_cb_rule` / `vs_R_stock_etf_rotation` / `vs_A_board_capacity` / `vs_D_fill_time` / `vs_I_price_cage`

`ignore_30pct_block_discount`、`copy_auction_tier_onto_block`、`confuse_S_cut30_with_block_discount30`、`vs_S_auction_handling`、`vs_AX_fund_block_50`、`vs_O_block_channel`、`missing_trade_type_or_official_bps_not_skip` 只作诊断桶：它们不是 `di0`，也不是 DI1，**不得升格主报**。`confuse_S_cut30_with_block_discount30` 没有对应的合成主报。S 的竞价切日只作诊断，**不得与大宗折扣 30% 合成后升格进 `di0`**。`invent_asof_leak_stock_block_handling` 只服务 DI1，**不得升格进 `di0`，不得双挂**。`invent_full_handling_fee_on_stock_block` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把股票大宗经手费按竞价全额抽，并拿去当诚实锚。
- 把 `params.G` 的 0.01 当成大宗 0.002387% 或竞价 0.0341‰。**尤重：`params.G` 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰**。
- 缺成交类型或官方‰仍不 skip，并用竞价全额或自造‰把腿填上。
- 把核对日 0.002387% 双向写成全历史唯一费率，并铺满全历史。方向是核对日现行，不是全历史已冻费率。锚六键已写死冻结。
- 把「竞价切日已诚实（S）/ 基金大宗 50% 已诚实（AX）/ 大宗通道已分列（O）/ 佣金双计已诚实（DH）/ 北交所档已诚实（DG）」写成「股票大宗经手下浮已诚实」。不改 S / AX / O / DH / DG。
- 把 S 的「降幅 30%」和本页「大宗折扣 30%」合成或混读后升格进 `di0`。诊断桶 `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` 只作对照。
- 把「可交换债经手费已诚实（DF）/ 转债证管费已诚实（DE）/ 转债过户费已诚实（DD）/ 转债印花税已诚实（DC）/ 转债经手费已诚实（DB）/ 场内基金过户已诚实（DA）」写成「股票大宗经手下浮已诚实」。不改 DF / DE / DD / DC / DB / DA。
- `di0_primary_demo` 与 `invent_asof_leak_stock_block_handling` 双挂主报；DI1 升格并列主报；诊断桶（`ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel`）升格为第二个主报。
- 实验字母 DI 与单字母 D/I 或 params.Y/G/N 混读。
- 改 S / AX / O / DH / DG / DF / DE / DD / DC / DB / DA / AC / T / U / V / Q / R / A / D / I 正文；重开假设-T；重开假设-AC；重开假设-R；抢 A 真数队列；标纸面齐；开真数/回测/实盘；用复权价当费用基数；结论写成「大宗费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权成交金额、交易日、证券类别、**成交类型**（竞价 / 股票大宗；仅用于把腿分回 S 或本页）、官方经手费率或「是否大宗、相对哪一档竞价标准」。
- 没有成交类型或官方‰时，按写死冻结的 `stock_block_handling_over_policy=skip_if_trade_type_or_official_bps_missing` skip，不得按竞价全额抽，也不得用核对日 0.002387% 把腿填满全历史。
- 旁路消费：S 的沪深股票竞价经手费切日、AX 的基金大宗下浮 50%、O 的大宗通道、DH 的佣金双计、DG 的北交所经手费、DF 的可交换债经手费、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、DA 的场内基金过户费、AC 的北交所涨跌幅与盘后、T 的股票证管费、U 的股票过户费、V 的股票印花税、Q 的转债规则、R 的股票 ETF 回转、I 的价格笼子之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** S 的切日降幅不收到本页主报。
- 未复权价；asof **写死冻结** `2026-10-16`。核对日方向 0.002387% 双向是现行方向，不是已冻全历史费率。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`stock_block_handling_honest=pit_auction_minus_30pct_not_full`（大宗按竞价标准下浮 30%，不按全额；核对日方向现行 0.002387% 双向；**禁止把 0.002387% 写成全历史唯一费率**）；`stock_block_handling_scope=sse_szse_ashare_block_apart_from_auction`（沪深 A 股股票大宗与竞价分开）；`stock_block_handling_over_policy=skip_if_trade_type_or_official_bps_missing`（缺成交类型或官方‰则 skip）；`di0_primary_demo=invent_full_handling_fee_on_stock_block`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_stock_block_handling` 双挂；DI1 不升格；诊断桶不升格主报；**禁把 S 切日降幅 30% 与大宗折扣 30% 合成进 `di0`**，只作对照/旁路，不得升格进 `di0` 或另挂主报）；`ashare_fee_handoff=s_page`；`fund_block_fee_handoff=ax_page`；`block_channel_handoff=o_page`；`commission_double_handoff=dh_page`；`bse_fee_handoff=dg_page`；`merge_with_S/AX/O/DH/DG/DF/DE/DD/DC/DB/DA/AC/T/U/V/Q/R/A/D/I=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 全额截 ΔStockBlockHandling / 净收益差 / DI1−DI2；**尤重 params.G 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DI ≠ 单字母 D/I**；**勿把 params.G 读成实验字母 DI，亦勿把单字母假设-D / 假设-I 读成双字母 DI**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成费率）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留下一号。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`ec654b33`（A/D–DH纸面齐已合）；三冻补丁基 tip=`e5872ea` / `e5872eae87ea277d4c263c42ef7de1cb6d13cd9c`；分支起点 HEAD=`3b1452f8` / `3b1452f87c5dcd46d8b57a7d7d5dd16c35dc76df`。

---

## 8. 结论

（空；**A/D–DI纸面齐（预检有条件通过·三条已冻）**。）

## 风控预检补丁·冻结（三条已写死 · 2026-11-09）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DI-20261109.md`（原样落入，不改结论；SHA256=`f6cbdcfb7dd1b0707ce62d016c5b4e7bf29f245b0d067aee51095993106b6271`；预检 2026-11-09；**结论：有条件通过**；tip基=`e5872ea` / `e5872eae87ea277d4c263c42ef7de1cb6d13cd9c`；本补丁分支起点 HEAD=`3b1452f8` / `3b1452f87c5dcd46d8b57a7d7d5dd16c35dc76df`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、全额截 ΔStockBlockHandling、净收益差、DI1−DI2 专项。**`params.Y` ≠ 实验字母 DI**；**`params.G` ≠ 实验字母 DI**；**`params.N` ≠ 实验字母 DI**；亦 ≠ 单字母假设-D / 假设-I。**勿把 `params.G` 读成实验字母 DI，亦勿把单字母假设-D / 假设-I 读成双字母 DI**。**尤重：`params.G` 的 `0.01` ≠ 大宗 `0.002387%` ≠ 竞价 `0.0341‰`**（**params.G 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰**）。三者量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，0.002387% 是大宗经手费核对日现行方向（不是全历史唯一费率），0.0341‰ 是竞价经手费率，禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.di0_primary_demo`**：**写死冻结** **`invent_full_handling_fee_on_stock_block`**（单一主报，单挂写死）。**禁止**与 **`invent_asof_leak_stock_block_handling`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DI1 核对日把现行大宗经手方向或现行下浮开关铺到全历史只作半泄露对照，**不得升格与 di0 并列主报**，也不得把 `invent_asof_leak_stock_block_handling` 写进 `di0`。`ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel` / `missing_trade_type_or_official_bps_not_skip` **只作诊断桶，不得升格主报**。DI1 / 诊断桶 **不升格**。**禁把 S「降幅 30%」与大宗折扣 30% 合成/混读升格进 `di0`**：这些只作对照/旁路，**不得升格进 `di0`，不得另挂主报**。

3. **股票大宗经手下浮诚实锚六键升格写死（不可再写「建议」）**：`params.stock_block_handling_honest=pit_auction_minus_30pct_not_full`；`params.stock_block_handling_scope=sse_szse_ashare_block_apart_from_auction`；`params.stock_block_handling_over_policy=skip_if_trade_type_or_official_bps_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺成交类型或官方‰ → skip；大宗按竞价标准下浮 30%→现行 0.002387% 双向。禁止把核对日 0.002387% 铺满全历史。禁止跑后改锚，或用竞价全额 / 核对日现行费率铺满全历史 / 发明‰ / 缺成交类型仍硬抽 / 把 S 切日 30% 混成大宗折扣冒充诚实 PIT。

**硬分列保住**：DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠O≠AC≠T≠U≠V≠Q≠R≠A≠D≠I；**双字母 DI ≠ 单字母假设-D / 假设-I / 假设-T**；**params.Y / params.G / params.N ≠ 实验字母 DI ≠ 单字母 D/I**；**尤重 params.G 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰**；**股票大宗折扣 ≠ S切日 ≠ AX基金大宗50% ≠ O通道 ≠ DH双计**；不抢 A；不改已齐 A–DH / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG 正文；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**禁把 S「降幅 30%」与大宗折扣 30% 合成/混读升格进 di0**。

**状态**：**A/D–DI纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 复检/纸面齐——**A/D–DI纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设DI-20261109.md` 原样落入，SHA256=`34786f34641dce4e5f42a454f683872ef56db15200a51cb02b6e4ad8e23f2097`；三冻 tip=`bfff8e4` / `bfff8e4c768fe0c4f4618868f33a904064b29c94`。只改状态标签；未改写已冻三条/六键数值与机制；不改已齐 A–DH / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH；不改 #110–#117；不重开假设-T；不重开假设-AC；不重开假设-R；禁把 S「降幅 30%」与大宗折扣 30% 合成/混读升格进 di0；不开回测/真数/实盘。 |
| 2026-11-09 | 风控预检补丁·冻结三条写死——依据 `预检-假设DI-20261109.md`（SHA256=`f6cbdcfb7dd1b0707ce62d016c5b4e7bf29f245b0d067aee51095993106b6271`；结论=有条件通过；tip基=`e5872ea` / `e5872eae87ea277d4c263c42ef7de1cb6d13cd9c`；分支起点 HEAD=`3b1452f8` / `3b1452f87c5dcd46d8b57a7d7d5dd16c35dc76df`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔStockBlockHandling / 净收益差 / DI1−DI2；**params.Y/G/N ≠ 实验字母 DI ≠ 单字母 D/I**；**勿把 params.G 读成实验字母 DI，亦勿把单字母假设-D / 假设-I 读成双字母 DI**；**尤重 params.G 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰（量纲与语义不同）**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成费率）；② `params.di0_primary_demo=invent_full_handling_fee_on_stock_block`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_stock_block_handling` 双挂；DI1 不升格；诊断桶 `ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel` 不升格；**禁把 S「降幅 30%」与大宗折扣 30% 合成/混读升格进 di0**，只作对照/旁路，不得升格进 di0 或另挂主报）；③ 锚六键写死 `stock_block_handling_honest=pit_auction_minus_30pct_not_full` / `stock_block_handling_scope=sse_szse_ashare_block_apart_from_auction` / `stock_block_handling_over_policy=skip_if_trade_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`（缺成交类型或官方‰ → skip；大宗按竞价标准下浮 30%→现行 0.002387% 双向；禁止把核对日 0.002387% 铺满全历史）。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；不改已齐 A–DH / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG；不重开假设-T；不重开假设-AC；不重开假设-R；不开回测/真数/实盘。基于 tip=`e5872ea`。 |
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；股票大宗经手下浮误忽略；`di0_primary_demo` 建议 `invent_full_handling_fee_on_stock_block`，单一主报，单挂，禁与 `invent_asof_leak_stock_block_handling` 双挂，DI1 不升格；诊断桶 `ignore_30pct_block_discount` / `copy_auction_tier_onto_block` / `confuse_S_cut30_with_block_discount30` / `vs_S_auction_handling` / `vs_AX_fund_block_50` / `vs_O_block_channel` 不升格；**尤重 S 的「降幅 30%」≠ 本页「大宗折扣 30%」，禁止合成/混读升格进 di0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DI ≠ 单字母 D/I**，且 **params.G 的 0.01 ≠ 大宗 0.002387% ≠ 竞价 0.0341‰**；锚建议 `stock_block_handling_honest=pit_auction_minus_30pct_not_full` / scope=`sse_szse_ashare_block_apart_from_auction` / over_policy=`skip_if_trade_type_or_official_bps_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；口径：缺成交类型或官方‰则 skip；大宗按竞价标准下浮 30%→现行 0.002387% 双向（**草稿方向，尚未冻，不要写成已冻**）；handoff：`ashare_fee_handoff=s_page`，`fund_block_fee_handoff=ax_page`，`block_channel_handoff=o_page`，`commission_double_handoff=dh_page`，`bse_fee_handoff=dg_page`；`merge_with_S/AX/O/DH/DG/DF/DE/DD/DC/DB/DA/AC/T/U/V/Q/R/A/D/I=False`；**DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠S≠AX≠O≠AC≠T≠U≠V≠Q≠R≠A≠D**；**双字母 DI ≠ 单字母假设-D / 假设-I**；**股票大宗折扣 ≠ S切日 ≠ AX基金大宗50% ≠ O通道 ≠ DH双计**；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；不改已齐 A–DH / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG 及其他已存在假设页；不重开假设-T；不重开假设-AC；不重开假设-R；不写下一字母；不预留下一号；不开真数/回测/实盘）。基 tip=`ec654b33`（A/D–DH纸面齐已合，全长 `ec654b336d9a0e638046826779ad261143bca1ae`；不改该 tip 上的 #110–#117，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文） |
