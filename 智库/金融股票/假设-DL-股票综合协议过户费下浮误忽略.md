# 假设-DL · 股票综合协议过户费下浮误忽略（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `6bdc1c2` 上清单 #120=DK 已收口（A/D–DK纸面齐已合入该 tip；**不改假设-DK 正文**，亦不改已齐 A–DK / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ / 假设-U / 假设-O / 假设-T / 假设-V / 假设-S / 假设-AX / 假设-AC / 假设-R / 假设-L 及其他已存在假设页；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-V**）后写下一草稿 DL；清单 #120=DK，本页占用 **#121=DL**；选题是股票综合协议过户费相对竞价过户标准的再下浮被忽略、按竞价全额抽；假设-U 只收股票过户费切日（其切日 ≠ 本页「综合协议再下浮 30%」），假设-DI 只收股票大宗经手下浮（经手 ≠ 过户），假设-O 只收大宗通道（通道 ≠ 本页费率），假设-DA 只收场内基金过户费；**新建实验 DL**；不写下一字母；不预留 #122  
状态：**A/D–DL纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「股票综合协议过户费按竞价全额抽、从而忽略综合协议相对竞价过户标准再下浮 30%」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改已齐 A–DK / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ**；尤其不改假设-U / 假设-DI / 假设-O / 假设-DA / 假设-DK / 假设-T / 假设-AC / 假设-R / 假设-V / 假设-D / 假设-L；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-V**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DL（#121）。一句话误开：回测把股票综合协议过户费按竞价全额抽（忽略综合协议相对竞价过户标准再下浮 30%），或缺成交类型 / 官方‰仍不 skip，系统性改写综合协议腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DL** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DL**；**勿把 `params.Y` 读成实验字母 DL**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DL**；**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰**——量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户费率‰，也不是综合协议下浮后的数；**禁把占位读成 0.01‰/0.007‰**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DL**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DL ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 L**（市价通道；**双字母 DL ≠ 单字母假设-L；严禁复用假设-L**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DL ≠ 单字母假设-A**）≠ **单字母实验 U**（股票过户费切日；**双字母 DL ≠ 单字母假设-U；严禁复用假设-U；不重开假设-U**）≠ 双字母 **DK**（场内基金印花税）≠ **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债经手费沪深分列）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **O**（大宗通道 / 假流动性）≠ **T**（股票证管费）≠ **V**（股票印花税）≠ **AX**（基金经手费）≠ **S**（沪深股票竞价经手费切日）≠ **AC**（北交所涨跌幅与盘后）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）。**DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠U≠O≠T≠V≠AX≠S≠AC≠Q≠R≠A≠D**。**双字母 DL ≠ 单字母 D/L**。**params.Y/G/N ≠ 实验字母 DL；亦 ≠ 单字母 D/L**。**勿把 `params.G` 读成实验字母 DL，亦勿把单字母假设-D / 假设-L 读成双字母 DL**。**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰**。**禁把占位读成 0.01‰/0.007‰**。**股票综合协议过户费下浮误忽略 ≠ U股票过户切日 ≠ DI大宗经手下浮 ≠ O大宗通道 ≠ DA基金过户**。**尤重：U 的股票过户费切日 ≠ 本页「综合协议再下浮 30%」——禁止合成/混读升格进 `dl0`**。**尤重：DI 股票大宗经手下浮 ≠ 本页过户费下浮（经手≠过户）——禁止合成/混读升格进 `dl0`**。**尤重：O 大宗通道 ≠ 本页费率——禁止合成/混读升格进 `dl0`**。

### 专节 · 双字母 DL ≠ 单字母假设-D / 假设-L；且 ≠ 假设-U / 假设-DI / 假设-O / 假设-DA（硬）

| 维度 | 对照页 | 本页假设-DL（双字母） |
|------|--------|----------------------|
| 题面 U | **股票过户费切日**（买卖双边；切日留在 U：竞价档何时从旧档换到现行档） | 股票过户费切日 ≠ 综合协议再下浮 30%。本页专测：综合协议过户费被按竞价全额抽。**DL≠U**；**严禁复用假设-U**；**不重开假设-U**；**不改 U**；**禁把 U 的股票过户费切日与本页「综合协议再下浮 30%」合成/混读升格进 `dl0`**；`stock_transfer_fee_handoff=u_page`；诊断桶 `vs_U_stock_transfer` / `confuse_U_cut_with_agreement_discount` 不升格 |
| 题面 DI | **股票大宗经手下浮**（经手费相对竞价标准下浮；经手 ≠ 过户） | 大宗经手下浮 ≠ 本页过户费下浮。**经手≠过户**。**DL≠DI**；**不改 DI**；**禁把 DI 股票大宗经手下浮与本页过户费下浮合成/混读升格进 `dl0`**；`stock_block_handling_handoff=di_page`；诊断桶 `vs_DI_stock_block_handling` / `confuse_DI_block_handling_discount_with_agreement_transfer` 不升格 |
| 题面 O | **大宗通道 / 假流动性**（量价并进竞价、通道混表） | 大宗通道 ≠ 本页费率。**DL≠O**；**严禁复用假设-O**；**不重开假设-O**；**不改 O**；**禁把 O 大宗通道与本页费率合成/混读升格进 `dl0`**；`block_channel_handoff=o_page`；诊断桶 `vs_O_block_channel` 不升格 |
| 题面 DA | **场内基金过户费** | 基金过户 ≠ 股票综合协议过户费下浮。**DL≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page`；诊断桶 `vs_DA_etf_transfer` 不升格 |
| 题面 DK | **场内基金印花税** | 基金印花 ≠ 综合协议过户费下浮。**DL≠DK**；**不改 DK**；`fund_stamp_handoff=dk_page` |
| 题面 DJ | **场内基金证管费** | 基金证管费 ≠ 本机制。**DL≠DJ**；**不改 DJ**；`fund_csrc_fee_handoff=dj_page` |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 综合协议过户费下浮。**DL≠DH**；**不改 DH**；`commission_double_handoff=dh_page` |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 本机制。**DL≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DF | **可交换债经手费沪深分列** | 可交换债经手费 ≠ 本机制。**DL≠DF**；**不改 DF**；`exch_handling_fee_handoff=df_page` |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 本机制。**DL≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债过户费** | 转债过户费 ≠ 股票综合协议过户费下浮。**DL≠DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DC | **可转债印花税** | 转债印花税 ≠ 本机制。**DL≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 DB | **可转债经手费** | 转债经手费 ≠ 本机制。**DL≠DB**；**不改 DB**；`cb_handling_fee_handoff=db_page` |
| 题面 T | **证管费主报股票** | 股票证管费 ≠ 综合协议过户费下浮。**DL≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 V | **股票印花税切日** | 印花税 ≠ 综合协议过户费下浮。**DL≠V**；**严禁复用假设-V**；**不重开假设-V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 本机制。**DL≠AX**；**不改 AX**；`fund_handling_fee_handoff=ax_page` |
| 题面 S | **沪深 A 股竞价经手费切日** | 经手费切日 ≠ 综合协议过户费下浮。**DL≠S**；**不改 S**；`ashare_fee_handoff=s_page` |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 综合协议过户费下浮。**DL≠AC**；**不改 AC**；**不重开假设-AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 本机制。**DL≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 本机制。**DL≠R**；**不改 R**；**不重开假设-R**；`stock_etf_rotation_handoff=r_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 综合协议过户费下浮。**DL≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 综合协议过户费是否再下浮。**双字母 DL ≠ 单字母假设-D**；**严禁复用假设-D**；**DL≠D**；**不改 D** |
| 题面 L | **市价通道** | 市价保护 / 废单 ≠ 综合协议过户费下浮。**双字母 DL ≠ 单字母假设-L**；**严禁复用假设-L**；**不改 L**；`mkt_channel_handoff=l_page` |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_full_transfer_fee_on_ashare_agreement`（**写死冻结**单一主报，单挂写死；禁与 `invent_asof_leak_ashare_agreement_transfer` 双挂；DL1 不升格；`ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer` 只作诊断对照，不升格主报；**尤重禁止把 U 股票过户切日、DI 大宗经手下浮、O 大宗通道合成进 `dl0`**） |
| 文档 | 清单实验 DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / U / O / T / V / AX / S / AC / Q / R / A / D / L（**只读；禁止改写**） | `假设-DL-股票综合协议过户费下浮误忽略.md`（新建） |
| 预检键 | 实验字母 DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / U / O / T / V / AX / S / AC / Q / R / A / D / L / Y / G / N | 实验字母 **DL** / `dl0_primary_demo`；**不得**占用或改写预检 DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/U/O/T/V/AX/S/AC/Q/R/A/D/L |

**禁止**：把 DL 写成「DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / U / O / T / V / AX / S / AC / Q / R / A / D / L 的续篇」；把「股票过户费切日已诚实（U）/ 大宗经手下浮已诚实（DI）/ 大宗通道已诚实（O）/ 场内基金过户已诚实（DA）」写成「股票综合协议过户费下浮已诚实」；把实验字母 DL 与单字母 D/L 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-L 读成双字母 DL**；**尤重勿把 `params.G` 读成实验字母 DL**；**尤重 `params.G` 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰（量纲与语义不同）**；**禁把占位读成 0.01‰/0.007‰**；**尤重 U 的股票过户费切日 ≠ 本页「综合协议再下浮 30%」，禁止合成/混读升格进 `dl0`**；**尤重 DI 股票大宗经手下浮 ≠ 本页过户费下浮（经手≠过户），禁止合成/混读升格进 `dl0`**；**尤重 O 大宗通道 ≠ 本页费率，禁止合成/混读升格进 `dl0`**；把 `invent_asof_leak_ashare_agreement_transfer` 升格进 `dl0` 或与主报双挂；把诊断桶 `ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer` 升格进 `dl0`。本页主键只用 `dl0` / `dl1` / `dl2` 与 `agreement_transfer_*`。不写下一字母。不预留 #122。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权成交金额下，回测把股票综合协议过户费按竞价全额抽（忽略综合协议相对竞价过户标准再下浮 30%），或缺成交类型 / 官方‰仍不 skip，相对「缺成交类型或官方‰则 skip；综合协议相对竞价过户标准再下浮 30%，禁止静默按全额 0.01‰」的诚实组，会**系统性改写综合协议腿成本**——相对诚实锚偏误。

核对日方向（随锚写死；禁止把「再下浮 30%」或 0.01‰/0.007‰ 写成全历史唯一费率）：综合协议相对竞价过户标准再下浮 30%。缺成交类型或官方‰则 skip。这不是把 0.01‰ 或 0.007‰ 冻成全历史唯一费率，也不是把 `params.G` 的 0.01 读成过户费 0.01‰。**禁把占位读成 0.01‰/0.007‰**。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误抽截在标定噪声带内可忽略，且「忽略再下浮 30% / 把竞价过户档抄到综合协议 / 把 DI 大宗经手折扣混进过户 / 把 U 切日混进再下浮 / 核对日泄露 / vs U·DI·O·DA」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dl0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DL ≠ 单字母假设-D / 假设-L**；勿把 params.Y 读成实验字母 DL
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DL ≠ 单字母 D/L**
# 【消歧】尤重：params.G 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰（量纲与语义不同：无量纲相对门槛 ≠ 过户费率‰）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成 0.01‰/0.007‰（这两个‰是过户费口径里会被误读的数，不是本页门槛，也不是本页要冻的费率）
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DL ≠ 单字母 D/L**
# params.Y2 写死冻结 0.015
# params.Y / G / N / Y2               写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误抽截 ΔAgreementTransfer / 净收益差 / DL1−DL2；**params.Y/G/N ≠ 实验字母 DL ≠ 单字母假设-D / 假设-L**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰**；**禁把占位读成 0.01‰/0.007‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成过户费率‰）
# params.fill_time                    写死冻结 next_open
# params.asof_check_date              写死冻结 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  写死冻结 skip
# params.agreement_transfer_honest    写死冻结 pit_auction_minus_30pct_not_full
#   诚实锚方向（已写死冻结；禁止把「再下浮 30%」或 0.01‰/0.007‰ 写成全历史唯一费率）：
#   综合协议相对竞价过户标准再下浮 30%
#   缺成交类型或官方‰ → skip
#   禁止静默按全额 0.01‰（那是按竞价全额抽，不得进 dl0 当诚实锚）
#   禁止把核对日下浮方向或 0.01‰/0.007‰ 铺满全历史（那是半泄露或误抽，不得进 dl0）
#   枚举已写死冻结
#   不把 U 的股票过户费切日、DI 的大宗经手下浮、O 的大宗通道、DA 的基金过户写成综合协议过户费诚实锚
# params.agreement_transfer_scope     写死冻结 ashare_comprehensive_agreement_apart_from_auction
#   股票综合协议与竞价过户分开
#   股票综合协议过户费下浮误忽略 ≠ U股票过户切日 ≠ DI大宗经手下浮 ≠ O大宗通道 ≠ DA基金过户
# params.agreement_transfer_over_policy 写死冻结 skip_if_trade_type_or_official_bps_missing
#   缺成交类型或官方‰则 skip；禁在缺字段时仍按全额 0.01‰ 把综合协议腿填上
# params.stock_transfer_fee_handoff   建议 u_page
#   消费 U 的股票过户费切日，或显式旁路；股票过户费切日 ≠ 综合协议再下浮 30%；不重开假设-U；不改 U
#   U 的股票过户费切日禁止合成/混读升格进 dl0；诊断桶 vs_U_stock_transfer / confuse_U_cut_with_agreement_discount 不得升格进 dl0
# params.stock_block_handling_handoff 建议 di_page
#   消费 DI 的股票大宗经手下浮，或显式旁路；大宗经手下浮 ≠ 本页过户费下浮；经手≠过户；不改 DI
#   DI 禁止合成/混读升格进 dl0；诊断桶 vs_DI_stock_block_handling / confuse_DI_block_handling_discount_with_agreement_transfer 不得升格进 dl0
# params.block_channel_handoff        建议 o_page
#   消费 O 的大宗通道，或显式旁路；大宗通道 ≠ 本页费率；不重开假设-O；不改 O
#   O 禁止合成/混读升格进 dl0；诊断桶 vs_O_block_channel 不得升格进 dl0
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；基金过户 ≠ 股票综合协议过户费下浮；不改 DA
#   诊断桶 vs_DA_etf_transfer 不得升格进 dl0
# params.fund_stamp_handoff           建议 dk_page
#   消费 DK 的场内基金印花税，或显式旁路；不改 DK
# params.fund_csrc_fee_handoff        建议 dj_page
#   消费 DJ 的场内基金证管费，或显式旁路；不改 DJ
# params.commission_double_handoff    建议 dh_page
#   消费 DH 的佣金双计，或显式旁路；不改 DH
# params.bse_fee_handoff              建议 dg_page
#   消费 DG 的北交所经手费档，或显式旁路；不改 DG
# params.exch_handling_fee_handoff    建议 df_page
#   消费 DF 的可交换债经手费沪深分列，或显式旁路；不改 DF
# params.cb_csrc_fee_handoff          建议 de_page
#   消费 DE 的转债证管费，或显式旁路；不改 DE
# params.cb_transfer_fee_handoff      建议 dd_page
#   消费 DD 的转债过户费，或显式旁路；不改 DD
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的可转债印花税，或显式旁路；不改 DC
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的可转债经手费，或显式旁路；不改 DB
# params.stock_csrc_fee_handoff       建议 t_page
#   消费 T 的股票证管费，或显式旁路；不重开假设-T；不改 T
# params.stock_stamp_handoff          建议 v_page
#   消费 V 的股票印花税切日，或显式旁路；不重开假设-V；不改 V
# params.fund_handling_fee_handoff    建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；不改 AX
# params.ashare_fee_handoff           建议 s_page
#   消费 S 的沪深股票竞价经手费切日，或显式旁路；不改 S
# params.bse_limit_aft_handoff        建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；不重开假设-AC；不改 AC
# params.cb_rule_handoff              建议 q_page
# params.stock_etf_rotation_handoff   建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 综合协议过户费下浮；不重开假设-R；不改 R
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
#   成交时点与停牌交 D；双字母 DL ≠ 单字母假设-D；不改 D
# params.mkt_channel_handoff          建议 l_page
#   市价通道交 L；双字母 DL ≠ 单字母假设-L；不改 L
# params.agreement_transfer_handoff   建议 self
# params.dl0_primary_demo             写死冻结 invent_full_transfer_fee_on_ashare_agreement
#   单一主报写死，单挂；禁与 invent_asof_leak_ashare_agreement_transfer 双挂；DL1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_ashare_agreement_transfer 只作对照，不得升格进 dl0，不得双挂
#   诊断桶 ignore_30pct_agreement_transfer_discount / copy_auction_transfer_tier_onto_agreement / confuse_DI_block_handling_discount_with_agreement_transfer / confuse_U_cut_with_agreement_discount / vs_U_stock_transfer / vs_DI_stock_block_handling / vs_O_block_channel / vs_DA_etf_transfer 不得升格进 dl0
#   尤重：禁止把 U 的股票过户费切日与「综合协议再下浮 30%」合成/混读后写进 dl0
#   尤重：禁止把 DI 股票大宗经手下浮与本页过户费下浮合成/混读后写进 dl0（经手≠过户）
#   尤重：禁止把 O 大宗通道与本页费率合成/混读后写进 dl0
# params.dl0_invent_full_transfer_fee_on_ashare_agreement 建议 True
# params.dl1_asof_leak_ashare_agreement_transfer_only 建议 True
#   半泄露对照；DL1 不升格并列主报；不得把 invent_asof_leak_ashare_agreement_transfer 写进 dl0
# params.dl2_pit_auction_minus_30pct  建议 True
# params.merge_with_DK                建议 False
# params.merge_with_DJ                建议 False
# params.merge_with_DI                建议 False
# params.merge_with_DH                建议 False
# params.merge_with_DG                建议 False
# params.merge_with_DF                建议 False
# params.merge_with_DE                建议 False
# params.merge_with_DD                建议 False
# params.merge_with_DC                建议 False
# params.merge_with_DB                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_U                 建议 False
# params.merge_with_O                 建议 False
# params.merge_with_T                 建议 False
# params.merge_with_V                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_S                 建议 False
# params.merge_with_AC                建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_R                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_L                 建议 False
# params.missing_trade_type_or_official_bps_policy 建议 skip
# params.day_freq_proxy               建议 agreement_transfer_sensitivity
# params.universe_rule                建议 agreement_transfer_misapply_check
# params.redline_v0_exempt_scope      建议 position_industry_dl_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DL；勿把这个键读成实验 DL
#   不另挂主报，不预留 #122，不写下一字母
```

### 2.2 三组对照（DL0 / DL1 / DL2）

| 组 | 角色 | 口径 |
|----|------|------|
| DL0 | 天真 / 按竞价全额抽综合协议过户费 | 按 `dl0_primary_demo` **写死冻结**单一主报 `invent_full_transfer_fee_on_ashare_agreement`（单挂写死）：股票综合协议过户费按竞价全额抽，忽略再下浮 30%。**禁**与 `invent_asof_leak_ashare_agreement_transfer` 双挂主报。**禁把 U 股票过户切日、DI 大宗经手下浮、O 大宗通道合成进 `dl0`**（只作对照/旁路，不得升格进 `dl0` 或另挂主报） |
| DL1 | 半泄露 | 仅核对日把「综合协议再下浮 30%」或现行过户费率铺到全历史、铺到全部成交类型（`invent_asof_leak_ashare_agreement_transfer`）；**不得升格并列主报**，也不得写进 `dl0`（写死冻结：DL1 不升格），不得双挂 |
| DL2 | 诚实 / 再下浮、不按全额 | `agreement_transfer_honest=pit_auction_minus_30pct_not_full`（写死冻结）：缺成交类型或官方‰则 skip；综合协议相对竞价过户标准再下浮 30%，禁止静默按全额 0.01‰。股票过户费切日只消费 U，大宗经手下浮只消费 DI，大宗通道只消费 O，场内基金过户只消费 DA，或显式旁路 |

忽略再下浮 30%、把竞价过户档抄到综合协议、把 DI 的大宗经手折扣混进过户费、把 U 的切日混进「再下浮 30%」，以及相对 U / DI / O / DA 的对照截（`ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dl0_primary_demo`。`vs_U_stock_transfer` 只标记「有人把 U 的股票过户费切日和本页综合协议再下浮 30% 合成/混读」这一类失效，**不得升格进 `dl0`**。`vs_DI_stock_block_handling` 只标记「有人把 DI 大宗经手下浮和本页过户费下浮合成/混读」，**不得升格进 `dl0`**。`vs_O_block_channel` 只标记「有人把 O 大宗通道和本页费率合成/混读」，**不得升格进 `dl0`**。U 的切日、DI 的大宗经手、O 的通道、DA 的基金过户只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dl0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺成交类型或官方‰则 skip；综合协议相对竞价过户标准再下浮 30%，禁止静默按全额 0.01‰。方向随锚写死：**不要把核对日「再下浮 30%」或 0.01‰/0.007‰ 铺满全历史**。`事实与坑` 已写 A 股交易过户费买卖双方、综合协议平台相对该标准再下浮；股票过户费切日留在假设-U，本页不重开。大宗经手下浮留在 DI，大宗通道留在 O，场内基金过户留在 DA，都不改。`params.G` 的 0.01 是无量纲相对门槛，不是过户费 0.01‰，也不是 0.007‰。**禁把占位读成 0.01‰/0.007‰**。缺成交类型或官方‰则 skip，不用竞价全额、自造‰或把占位 0.01 当成费率把腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dl0_primary_demo` / `params.Y`·G·N·Y2 / 下浮开关 / 桶 / 是否把 0.01‰/0.007‰ 铺到综合协议）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DL0）/ 半泄露组（DL1）相对诚实组（DL2）的成本差、误抽截**显著且集中在按竞价全额抽综合协议过户费的桶**；分桶「忽略再下浮 30% / 竞价过户档抄到综合协议 / DI 经手折扣混进过户 / U 切日混进再下浮 / 核对日泄露 / vs U·DI·O·DA」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 0.01‰/0.007‰ 冻成全历史唯一费率，也不把 `params.G` 的 0.01 读成过户费‰。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 U 的股票过户费切日、DI 的大宗经手下浮、O 的大宗通道、DA 的场内基金过户、DK 的基金印花税、DJ 的基金证管费、DH 的佣金双计、DG 的北交所档、DF 的可交换债经手费、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、T 的股票证管费、V 的股票印花税、AX 的基金经手费、S 的竞价经手费切日、AC 的北交所涨跌幅与盘后、Q 的回转与涨跌幅、R 的股票 ETF 回转、A 的板上容量、D 的成交时点、L 的市价通道解释；或 `dl0_primary_demo` 与 `invent_asof_leak_ashare_agreement_transfer` 双挂；或 DL1 升格并列主报；或 `ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer` 诊断桶升格主报；或把 U 的股票过户费切日与「综合协议再下浮 30%」合成进 `dl0`；或把 DI 大宗经手下浮合成进 `dl0`；或把 O 大宗通道合成进 `dl0`；或实验字母 DL 与单字母 D/L 或 params.Y/G/N 混读；或把 `params.G` 的 0.01 读成过户费 0.01‰；或把占位读成 0.01‰/0.007‰；或把核对日「再下浮 30%」写成已冻并铺满全历史；或缺成交类型 / 官方‰仍按全额把综合协议腿填上；或重开假设-T / 假设-AC / 假设-R / 假设-U / 假设-O / 假设-V。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DL0/DL1/DL2。股票过户费切日走 U 的诚实切日或显式旁路，不在本页改 U，也不把 U 的切日升成主报。大宗经手下浮走 DI，大宗通道走 O，场内基金过户走 DA，都不改。报告成本差、误抽截。不把 0.01‰/0.007‰ 标成已冻的综合协议费率，也不把 `params.G` 的 0.01 读成过户费‰。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_full_transfer_fee_on_ashare_agreement` / `invent_asof_leak_ashare_agreement_transfer` / `ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer` / `missing_trade_type_or_official_bps_not_skip`

`ignore_30pct_agreement_transfer_discount`、`copy_auction_transfer_tier_onto_agreement`、`confuse_DI_block_handling_discount_with_agreement_transfer`、`confuse_U_cut_with_agreement_discount`、`vs_U_stock_transfer`、`vs_DI_stock_block_handling`、`vs_O_block_channel`、`vs_DA_etf_transfer`、`missing_trade_type_or_official_bps_not_skip` 只作诊断桶：它们不是 `dl0`，也不是 DL1，**不得升格主报**。`vs_U_stock_transfer` 没有对应的「U 切日 + 综合协议再下浮」合成主报。U 的股票过户费切日只作诊断，**不得与综合协议再下浮 30% 合成后升格进 `dl0`**。DI 的大宗经手下浮只作诊断，**不得升格进 `dl0`**。O 的大宗通道只作诊断，**不得升格进 `dl0`**。DA 的基金过户只作诊断，**不得升格进 `dl0`**。`invent_asof_leak_ashare_agreement_transfer` 只服务 DL1，**不得升格进 `dl0`，不得双挂**。`invent_full_transfer_fee_on_ashare_agreement` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 把股票综合协议过户费按竞价全额抽，并拿去当诚实锚。
- 把 `params.G` 的 0.01 当成过户费 0.01‰。**尤重：`params.G` 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 0.01‰/0.007‰。**禁把占位读成 0.01‰/0.007‰**。
- 缺成交类型或官方‰仍不 skip，并用竞价全额、自造‰或占位 0.01 把综合协议腿填上。
- 把核对日「综合协议相对竞价过户标准再下浮 30%」写成全历史唯一费率，并铺满全历史。方向是核对日相对竞价过户标准再下浮 30%，不是全历史已冻费率。锚六键已写死冻结。
- 把「股票过户费切日已诚实（U）/ 大宗经手下浮已诚实（DI）/ 大宗通道已诚实（O）/ 场内基金过户已诚实（DA）」写成「股票综合协议过户费下浮已诚实」。不改 U / DI / O / DA。
- 把 U 的股票过户费切日和本页「综合协议再下浮 30%」合成或混读后升格进 `dl0`。诊断桶 `vs_U_stock_transfer` / `confuse_U_cut_with_agreement_discount` 只作对照。
- 把 DI 股票大宗经手下浮和本页过户费下浮合成或混读后升格进 `dl0`。经手≠过户。诊断桶 `vs_DI_stock_block_handling` / `confuse_DI_block_handling_discount_with_agreement_transfer` 只作对照。
- 把 O 大宗通道和本页费率合成或混读后升格进 `dl0`。诊断桶 `vs_O_block_channel` 只作对照。
- 把竞价过户档抄到综合协议，或忽略再下浮 30%，并升格进 `dl0`。诊断桶 `copy_auction_transfer_tier_onto_agreement` / `ignore_30pct_agreement_transfer_discount` 只作对照。不改 U。
- 把 DA 基金过户和本页股票综合协议过户费下浮合成后升格进 `dl0`。诊断桶 `vs_DA_etf_transfer` 只作对照。
- `dl0_primary_demo` 与 `invent_asof_leak_ashare_agreement_transfer` 双挂主报；DL1 升格并列主报；诊断桶（`ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer`）升格为第二个主报。
- 实验字母 DL 与单字母 D/L 或 params.Y/G/N 混读。
- 改 DK / DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / U / O / T / V / AX / S / AC / Q / R / A / D / L 正文；重开假设-T；重开假设-AC；重开假设-R；重开假设-U；重开假设-O；重开假设-V；抢 A 真数队列；标纸面齐；写 A/D–DL纸面齐；开真数/回测/实盘；用复权价当费用基数；结论写成「综合协议过户费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权成交金额、交易日、**成交类型**（竞价 / 综合协议；仅用于把腿分回 U 或本页）、**官方过户费‰是否在册**（缺则 skip，不发明数）。
- 证券类别只用于把腿分回 DI / O / DA / DK 等旁路页，不在本页改那些页。
- 没有成交类型或官方‰时，按写死冻结的 `agreement_transfer_over_policy=skip_if_trade_type_or_official_bps_missing` skip，不得按全额 0.01‰ 把综合协议腿填上，也不得用核对日下浮方向或 0.007‰ 把腿填满全历史。
- 旁路消费：U 的股票过户费切日、DI 的大宗经手下浮、O 的大宗通道、DA 的场内基金过户费、DK 的基金印花税、DJ 的基金证管费、DH 的佣金双计、DG 的北交所经手费、DF 的可交换债经手费、DE 的转债证管费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、T 的股票证管费、V 的股票印花税、AX 的基金经手费、S 的沪深股票竞价经手费切日、AC 的北交所涨跌幅与盘后、Q 的转债规则、R 的股票 ETF 回转、L 的市价通道之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** U 的股票过户费切日、DI 的大宗经手下浮、O 的大宗通道不收到本页主报。
- 未复权价；asof **写死冻结** `2026-10-16`。核对日方向「综合协议相对竞价过户标准再下浮 30%」是写死冻结的机制方向，不是已冻全历史费率。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`agreement_transfer_honest=pit_auction_minus_30pct_not_full`（综合协议相对竞价过户标准再下浮 30%，禁止静默按全额 0.01‰；**禁止把核对日「再下浮 30%」或 0.01‰/0.007‰ 写成全历史唯一费率**）；`agreement_transfer_scope=ashare_comprehensive_agreement_apart_from_auction`（股票综合协议与竞价过户分开）；`agreement_transfer_over_policy=skip_if_trade_type_or_official_bps_missing`（缺成交类型或官方‰则 skip）；`dl0_primary_demo=invent_full_transfer_fee_on_ashare_agreement`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_ashare_agreement_transfer` 双挂；DL1 不升格；诊断桶不升格主报；**禁把 U 股票过户切日、DI 大宗经手下浮、O 大宗通道合成进 `dl0`**，只作对照/旁路，不得升格进 `dl0` 或另挂主报）；`stock_transfer_fee_handoff=u_page`；`stock_block_handling_handoff=di_page`；`block_channel_handoff=o_page`；`etf_transfer_fee_handoff=da_page`；`merge_with_DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/U/O/T/V/AX/S/AC/Q/R/A/D/L=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误抽截 ΔAgreementTransfer / 净收益差 / DL1−DL2；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰（量纲与语义不同）**；**禁把占位读成 0.01‰/0.007‰**；**params.Y/G/N ≠ 实验字母 DL ≠ 单字母 D/L**；**勿把 params.G 读成实验字母 DL，亦勿把单字母假设-D / 假设-L 读成双字母 DL**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成过户费率‰）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #122。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`6bdc1c2`（A/D–DK纸面齐已合，全长 `6bdc1c2e7298bd06b4cc11a063866a42ae6ffca4`）；三冻补丁基 tip=`67d37966` / `67d37966d2f72dbb82bd39d1bcb8a22d11dbd167`；分支起点 HEAD=`0980e7dc` / `0980e7dcd6b7126ff0d0b3fc27d53a99457e0918`。

---

## 8. 结论

（空；**A/D–DL纸面齐（预检有条件通过·三条已冻）**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-09）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DL-20261109.md`（原样落入，不改结论；SHA256=`154fd9a590c8e8a1fba50e1f9eb1aae5c6bdfe6d4cfe51371e7967693b658660`；预检 2026-11-09；**结论：有条件通过**；tip基=`67d37966` / `67d37966d2f72dbb82bd39d1bcb8a22d11dbd167`；本补丁分支起点 HEAD=`0980e7dc` / `0980e7dcd6b7126ff0d0b3fc27d53a99457e0918`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、误抽截 ΔAgreementTransfer、净收益差、DL1−DL2 专项。**`params.Y` ≠ 实验字母 DL**；**`params.G` ≠ 实验字母 DL**；**`params.N` ≠ 实验字母 DL**；亦 ≠ 单字母假设-D / 假设-L。**勿把 `params.G` 读成实验字母 DL，亦勿把单字母假设-D / 假设-L 读成双字母 DL**。**尤重：`params.G` 的 `0.01` ≠ 过户费 0.01‰ ≠ 0.007‰**（**params.G 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰**）。二者量纲与语义都不同：`params.G=0.01` 是无量纲相对门槛，不是过户费率‰，也不是综合协议下浮后的数。**禁把占位读成 0.01‰/0.007‰**。禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dl0_primary_demo`**：**写死冻结** **`invent_full_transfer_fee_on_ashare_agreement`**（单一主报，单挂写死）。**禁止**与 **`invent_asof_leak_ashare_agreement_transfer`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DL1 核对日把「综合协议再下浮 30%」或现行过户费率铺到全历史、铺到全部成交类型只作半泄露对照，**不得升格与 dl0 并列主报**，也不得把 `invent_asof_leak_ashare_agreement_transfer` 写进 `dl0`。`ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer` / `missing_trade_type_or_official_bps_not_skip` **只作诊断桶，不得升格主报**。DL1 / 诊断桶 **不升格**。**禁把 U 股票过户切日 / DI 大宗经手下浮 / O 大宗通道 合成/混读升格进 `dl0`**：这些只作对照/旁路，**不得升格进 `dl0`，不得另挂主报**。经手≠过户。

3. **股票综合协议过户费诚实锚六键升格写死（不可再写「建议」）**：`params.agreement_transfer_honest=pit_auction_minus_30pct_not_full`；`params.agreement_transfer_scope=ashare_comprehensive_agreement_apart_from_auction`；`params.agreement_transfer_over_policy=skip_if_trade_type_or_official_bps_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺成交类型或官方‰ → skip；综合协议相对竞价过户标准再下浮 30%，禁止静默按全额 0.01‰。禁止把核对日「再下浮 30%」或 0.01‰/0.007‰ 铺满全历史。禁止跑后改锚，或用竞价全额 / 核对日现行费率 / 发明‰ / 缺成交类型或官方‰仍硬填 / 把 U 股票过户切日、DI 大宗经手下浮或 O 大宗通道升格进 dl0 冒充诚实 PIT。**禁把占位读成 0.01‰/0.007‰**。**经手≠过户**。

**硬分列保住**：DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠U≠O≠T≠V≠AX≠S≠AC≠Q≠R≠A≠D≠L；**双字母 DL ≠ 单字母假设-D / 假设-L / 假设-U / 假设-O**；**params.Y / params.G / params.N ≠ 实验字母 DL ≠ 单字母 D/L**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰**；**禁把占位读成 0.01‰/0.007‰**；**股票综合协议过户费下浮误忽略 ≠ U股票过户切日 ≠ DI大宗经手下浮 ≠ O大宗通道 ≠ DA基金过户**；不抢 A；不改已齐 A–DK / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ 正文；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-U**；**不重开假设-O**；**不重开假设-DI**；**不重开假设-V**；**禁把 U 股票过户切日 / DI 大宗经手下浮 / O 大宗通道 合成/混读升格进 dl0**。

**状态**：**A/D–DL纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 复检/纸面齐——**A/D–DL纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设DL-20261109.md` 原样落入，SHA256=`2595ece6ba632795fde35d15c6ccbcaebd99c75edc60e77002b1d6dbf66c374f`；三冻 tip=`08c50d4` / `08c50d4569399d81ee2ece60c6c5443223d88007`。只改状态标签；未改写已冻三条/六键数值与机制；不改已齐 A–DK；不改 #110–#120；不重开假设-T/AC/R/U/O/DI/V；禁把 U 股票过户切日 / DI 大宗经手下浮 / O 大宗通道 混读升格进 dl0；不开回测/真数/实盘。 |
| 2026-11-09 | 风控预检补丁·冻结三条写死——依据 `预检-假设DL-20261109.md`（SHA256=`154fd9a590c8e8a1fba50e1f9eb1aae5c6bdfe6d4cfe51371e7967693b658660`；结论=有条件通过；tip基=`67d37966` / `67d37966d2f72dbb82bd39d1bcb8a22d11dbd167`；分支起点 HEAD=`0980e7dc` / `0980e7dcd6b7126ff0d0b3fc27d53a99457e0918`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔAgreementTransfer / 净收益差 / DL1−DL2；**params.Y/G/N ≠ 实验字母 DL ≠ 单字母 D/L**；**勿把 params.G 读成实验字母 DL，亦勿把单字母假设-D / 假设-L 读成双字母 DL**；**尤重 params.G 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰（量纲与语义不同）**；**禁把占位读成 0.01‰/0.007‰**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成过户费率‰）；② `params.dl0_primary_demo=invent_full_transfer_fee_on_ashare_agreement`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_ashare_agreement_transfer` 双挂；DL1 不升格；诊断桶 `ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer` 不升格；**禁把 U 股票过户切日 / DI 大宗经手下浮 / O 大宗通道 合成/混读升格进 dl0**，只作对照/旁路，不得升格进 dl0 或另挂主报；经手≠过户）；③ 锚六键写死 `agreement_transfer_honest=pit_auction_minus_30pct_not_full` / `agreement_transfer_scope=ashare_comprehensive_agreement_apart_from_auction` / `agreement_transfer_over_policy=skip_if_trade_type_or_official_bps_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`（缺成交类型或官方‰ → skip；综合协议相对竞价过户标准再下浮 30%，禁止静默按全额 0.01‰；禁止把核对日「再下浮 30%」或 0.01‰/0.007‰ 铺满全历史）。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DL纸面齐**；不改已齐 A–DK / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-U；不重开假设-O；不重开假设-DI；不重开假设-V；不开回测/真数/实盘。基于 tip=`67d37966`。 |
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；股票综合协议过户费下浮误忽略；`dl0_primary_demo` 建议 `invent_full_transfer_fee_on_ashare_agreement`，单一主报，单挂，禁与 `invent_asof_leak_ashare_agreement_transfer` 双挂，DL1 不升格；诊断桶 `ignore_30pct_agreement_transfer_discount` / `copy_auction_transfer_tier_onto_agreement` / `confuse_DI_block_handling_discount_with_agreement_transfer` / `confuse_U_cut_with_agreement_discount` / `vs_U_stock_transfer` / `vs_DI_stock_block_handling` / `vs_O_block_channel` / `vs_DA_etf_transfer` 不升格；**尤重 U 的股票过户费切日 ≠ 本页「综合协议再下浮 30%」，禁止合成/混读升格进 dl0**；**尤重 DI 股票大宗经手下浮 ≠ 本页过户费下浮（经手≠过户），禁止合成进 dl0**；**尤重 O 大宗通道 ≠ 本页费率，禁止合成进 dl0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DL ≠ 单字母 D/L**，且 **params.G 的 0.01 ≠ 过户费 0.01‰ ≠ 0.007‰**，**禁把占位读成 0.01‰/0.007‰**；锚建议 `agreement_transfer_honest=pit_auction_minus_30pct_not_full` / scope=`ashare_comprehensive_agreement_apart_from_auction` / over_policy=`skip_if_trade_type_or_official_bps_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；口径：缺成交类型或官方‰则 skip；综合协议相对竞价过户标准再下浮 30%，禁止静默按全额 0.01‰（**草稿方向，尚未冻，不要写成已冻**）；handoff：`stock_transfer_fee_handoff=u_page`，`stock_block_handling_handoff=di_page`，`block_channel_handoff=o_page`，`etf_transfer_fee_handoff=da_page`；`merge_with_DK/DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/U/O/T/V/AX/S/AC/Q/R/A/D/L=False`；**DL≠DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠U≠O≠T≠V≠AX≠S≠AC≠Q≠R≠A≠D**；**双字母 DL ≠ 单字母假设-D / 假设-L**；**股票综合协议过户费下浮误忽略 ≠ U股票过户切日 ≠ DI大宗经手下浮 ≠ O大宗通道 ≠ DA基金过户**；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DL纸面齐**；不改已齐 A–DK / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-DJ 及其他已存在假设页；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-U；不重开假设-O；不重开假设-V；不写下一字母；不预留 #122；不开真数/回测/实盘）。基 tip=`6bdc1c2`（A/D–DK纸面齐已合，全长 `6bdc1c2e7298bd06b4cc11a063866a42ae6ffca4`；不改该 tip 上的 #110–#120，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文） |
