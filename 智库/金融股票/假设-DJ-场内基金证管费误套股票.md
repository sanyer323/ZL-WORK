# 假设-DJ · 场内基金证管费误套股票（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `5bf9b20` 上清单 #118=DI 已收口（A/D–DI纸面齐已合入该 tip；**不改假设-DI 正文**，亦不改已齐 A–DI / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-T / 假设-S / 假设-AX / 假设-AC / 假设-R / 假设-J 及其他已存在假设页；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**）后写下一草稿 DJ；清单 #118=DI，本页占用 **#119=DJ**；选题是场内基金（ETF / 封闭式 / LOF）被误套或发明股票证管费；假设-T 只收股票证管费切日（其切日 ≠ 本页「对基金/ETF 发明证管费」），假设-DE 只收可转债证管费，假设-AX 只收基金经手费，假设-DA 只收场内基金过户费，假设-DI 只收股票大宗经手下浮，假设-S 只收股票竞价经手费切日；**新建实验 DJ**；不写下一字母；不预留 #120  
状态：**预检有条件通过·三条已冻·待复检**（结论栏空；禁止把「对场内基金/ETF 发明或误套股票证管费」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**三条已冻**；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DJ纸面齐**；**禁止标任何纸面齐**；**不改已齐 A–DI / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH**；尤其不改假设-T / 假设-DE / 假设-AX / 假设-DA / 假设-DI / 假设-S / 假设-AC / 假设-R / 假设-D / 假设-J；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DJ（#119）。一句话误开：回测对场内基金/ETF 发明或误套股票证管费，或缺证券类别 / 官方证管费栏仍不 skip，系统性改写基金腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DJ** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DJ**；**勿把 `params.Y` 读成实验字母 DJ**；**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**——量纲与语义都不同：`params.Y=0.02` 是无量纲相对门槛，不是股票证管费率 0.02‰，也不是本页要冻的基金费率）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DJ**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DJ**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DJ ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 J**（无板日临停；**双字母 DJ ≠ 单字母假设-J；严禁复用假设-J**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DJ ≠ 单字母假设-A**）≠ **单字母实验 T**（证管费主报股票；**双字母 DJ ≠ 单字母假设-T；严禁复用假设-T；不重开假设-T**）≠ 双字母 **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债经手费沪深分列）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **AX**（基金经手费）≠ **S**（沪深股票竞价经手费切日）≠ **AC**（北交所涨跌幅与盘后）≠ **U**（股票过户费）≠ **V**（股票印花税）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）。**DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠T≠AX≠S≠AC≠U≠V≠Q≠R≠A≠D**。**双字母 DJ ≠ 单字母 D/J**。**params.Y/G/N ≠ 实验字母 DJ；亦 ≠ 单字母 D/J**。**勿把 `params.Y` 读成实验字母 DJ，亦勿把单字母假设-D / 假设-J 读成双字母 DJ**。**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**。**场内基金证管费误套 ≠ T股票证管 ≠ DE转债证管 ≠ AX基金经手 ≠ DA过户 ≠ DI大宗折扣**。**尤重：T 的股票证管费切日 ≠ 本页「对基金/ETF 发明证管费」——禁止合成/混读升格进 `dj0`**。**尤重：DE 可转债证管费 ≠ 本页基金/ETF 证管费——禁止合成/混读升格进 `dj0`**。

### 专节 · 双字母 DJ ≠ 单字母假设-D / 假设-J；且 ≠ 假设-T / 假设-DE / 假设-AX / 假设-DA / 假设-DI（硬）

| 维度 | 对照页 | 本页假设-DJ（双字母） |
|------|--------|----------------------|
| 题面 T | **证管费主报股票**（股票切日、股票 0.02‰ 档留在 T；2023-08-28 没改证管费也是 T 的题） | 股票证管费切日 ≠ 对基金/ETF 发明证管费。本页专测：场内基金被误套或发明股票证管费。**DJ≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；**禁把 T 的股票证管费切日与本页「对基金/ETF 发明证管费」合成/混读升格进 `dj0`**；`stock_csrc_fee_handoff=t_page`；诊断桶 `vs_T_stock_csrc` 不升格 |
| 题面 DE | **可转债证管费**（转债现货不要套股票证管费；缺官方‰则 skip） | 可转债证管费 ≠ 基金/ETF 证管费。**DJ≠DE**；**不改 DE**；**禁把 DE 可转债证管费与本页基金/ETF 证管费合成/混读升格进 `dj0`**；`cb_csrc_fee_handoff=de_page`；诊断桶 `vs_DE_cb_csrc` 不升格 |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 基金证管费。**DJ≠AX**；**不改 AX**；`fund_handling_fee_handoff=ax_page`；诊断桶 `vs_AX_fund_handling` 不升格 |
| 题面 DA | **场内基金过户费** | 场内基金过户 ≠ 基金证管费。**DJ≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page`；诊断桶 `vs_DA_etf_transfer` 不升格 |
| 题面 DI | **股票大宗经手下浮**（大宗折扣 30%） | 大宗折扣 ≠ 基金证管费误套。**DJ≠DI**；**不改 DI**；`block_discount_handoff=di_page` |
| 题面 S | **沪深 A 股竞价经手费切日**（2023-08-28 的降幅是经手费，不是证管费） | 经手费切日 ≠ 证管费。**DJ≠S**；**不改 S**；`ashare_fee_handoff=s_page`；诊断桶 `copy_20230828_handling_cut_onto_csrc` 不升格 |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 基金证管费误套。**DJ≠DH**；**不改 DH**；`commission_double_handoff=dh_page` |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 基金证管费误套。**DJ≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DF | **可交换债经手费沪深分列** | 可交换债经手费 ≠ 本机制。**DJ≠DF**；**不改 DF**；`exch_handling_fee_handoff=df_page` |
| 题面 DD | **可转债过户费** | 转债过户费 ≠ 本机制。**DJ≠DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DC | **可转债印花税** | 转债印花税 ≠ 本机制。**DJ≠DC**；**不改 DC**；`cb_stamp_handoff=dc_page` |
| 题面 DB | **可转债经手费** | 转债经手费 ≠ 本机制。**DJ≠DB**；**不改 DB**；`cb_handling_fee_handoff=db_page` |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 基金证管费。**DJ≠AC**；**不改 AC**；**不重开假设-AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 U | **股票过户费** | 股票过户费 ≠ 基金证管费。**DJ≠U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 V | **股票印花税** | 印花税 ≠ 基金证管费。**DJ≠V**；**不改 V**；`stock_stamp_handoff=v_page` |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 基金证管费。**DJ≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 基金证管费。**DJ≠R**；**不改 R**；**不重开假设-R**；`stock_etf_rotation_handoff=r_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 基金证管费误套。**DJ≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 基金证管费抽在哪一档。**双字母 DJ ≠ 单字母假设-D**；**严禁复用假设-D**；**DJ≠D**；**不改 D** |
| 题面 J | **无板日临停** | 临停窗口 ≠ 基金证管费。**双字母 DJ ≠ 单字母假设-J**；**严禁复用假设-J**；**不改 J**；`intraday_halt_handoff=j_page` |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_ashare_csrc_fee_on_fund`（**写死冻结**单一主报，单挂写死；禁与 `invent_asof_leak_fund_csrc_fee` 双挂；DJ1 不升格；`charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer` 只作诊断对照，不升格主报；**尤重禁止把 T 股票证管费切日、DE 转债证管费合成进 `dj0`**） |
| 文档 | 清单实验 DI / DH / DG / DF / DE / DD / DC / DB / DA / T / AX / S / AC / U / V / Q / R / A / D / J（**只读；禁止改写**） | `假设-DJ-场内基金证管费误套股票.md`（新建） |
| 预检键 | 实验字母 DI / DH / DG / DF / DE / DD / DC / DB / DA / T / AX / S / AC / U / V / Q / R / A / D / J / Y / G / N | 实验字母 **DJ** / `dj0_primary_demo`；**不得**占用或改写预检 DI/DH/DG/DF/DE/DD/DC/DB/DA/T/AX/S/AC/U/V/Q/R/A/D/J |

**禁止**：把 DJ 写成「DI / DH / DG / DF / DE / DD / DC / DB / DA / T / AX / S / AC / U / V / Q / R / A / D / J 的续篇」；把「股票证管费切日已诚实（T）/ 转债证管费已诚实（DE）/ 基金经手费已诚实（AX）/ 场内基金过户已诚实（DA）/ 大宗折扣已诚实（DI）」写成「场内基金证管费已诚实」；把实验字母 DJ 与单字母 D/J 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-J 读成双字母 DJ**；**尤重勿把 `params.Y` 读成实验字母 DJ**；**尤重 `params.Y` 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同）**；**尤重 T 的股票证管费切日 ≠ 本页「对基金/ETF 发明证管费」，禁止合成/混读升格进 `dj0`**；**尤重 DE 可转债证管费 ≠ 本页基金/ETF 证管费，禁止合成/混读升格进 `dj0`**；把 `invent_asof_leak_fund_csrc_fee` 升格进 `dj0` 或与主报双挂；把诊断桶 `charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer` 升格进 `dj0`。本页主键只用 `dj0` / `dj1` / `dj2` 与 `fund_csrc_fee_*`。不写下一字母。不预留 #120。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权成交金额下，回测对场内基金（ETF / 封闭式 / LOF）发明或误套股票证管费档，或缺证券类别 / 官方证管费栏仍不 skip，相对「缺证券类别或官方证管费栏则 skip；基金/债券依法免收、不套股票档」的诚实组，会**系统性改写基金腿成本**——相对诚实锚偏误。

核对日方向（随锚写死；禁止把免收或股票 0.02‰ 写成全历史唯一费率）：基金和债券依法免收，不套股票证管费档。这不是把某一档‰冻成全历史唯一费率，也不是把 `params.Y` 的 0.02 读成证管费 0.02‰。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误套截在标定噪声带内可忽略，且「对 ETF 套股票证管费 / 对债券套股票证管费 / 把 2023-08-28 经手费降幅抄到证管费 / 核对日泄露 / vs T·DE·AX·DA」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dj0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DJ ≠ 单字母假设-D / 假设-J**；勿把 params.Y 读成实验字母 DJ
# 【消歧】尤重：params.Y 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同：无量纲相对门槛 ≠ 股票证管费率‰）
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DJ ≠ 单字母 D/J**
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DJ ≠ 单字母 D/J**
# params.Y2 写死冻结 0.015
# params.Y / G / N / Y2               写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误套截 ΔFundCsrcFee / 净收益差 / DJ1−DJ2；**params.Y/G/N ≠ 实验字母 DJ ≠ 单字母假设-D / 假设-J**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成证管费率‰）
# params.fill_time                    写死冻结 next_open
# params.asof_check_date              写死冻结 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  写死冻结 skip
# params.fund_csrc_fee_honest         写死冻结 pit_fund_bond_exempt_not_stock_tier
#   诚实锚方向（已写死冻结；禁止把免收或股票 0.02‰ 写成全历史唯一费率）：
#   基金/债券依法免收，不套股票证管费档
#   缺证券类别或官方证管费栏 → skip
#   禁止把核对日「免收」或股票 0.02‰ 铺满全历史（那是半泄露或误套，不得进 dj0）
#   枚举已写死冻结
#   不把 T 的股票证管费切日、DE 的转债证管费、AX 的基金经手费、DA 的过户费、DI 的大宗折扣写成基金证管费诚实锚
# params.fund_csrc_fee_scope          写死冻结 etf_closed_lof_bond_apart_from_ashare_csrc
#   ETF / 封闭式 / LOF / 债券与股票证管费分开
#   场内基金证管费误套 ≠ T股票证管 ≠ DE转债证管 ≠ AX基金经手 ≠ DA过户 ≠ DI大宗折扣 ≠ S经手费切日
# params.fund_csrc_fee_over_policy    写死冻结 skip_if_sec_type_or_official_csrc_row_missing
#   缺证券类别或官方证管费栏则 skip；禁在缺栏时仍对基金发明股票证管费
# params.stock_csrc_fee_handoff       建议 t_page
#   消费 T 的股票证管费切日，或显式旁路；股票证管费切日 ≠ 对基金/ETF 发明证管费；不重开假设-T；不改 T
#   T 的股票证管费切日禁止合成/混读升格进 dj0；诊断桶 vs_T_stock_csrc 不得升格进 dj0
# params.cb_csrc_fee_handoff          建议 de_page
#   消费 DE 的可转债证管费，或显式旁路；可转债证管费 ≠ 基金/ETF 证管费；不改 DE
#   DE 禁止合成/混读升格进 dj0；诊断桶 vs_DE_cb_csrc 不得升格进 dj0
# params.fund_handling_fee_handoff    建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；基金经手费 ≠ 基金证管费；不改 AX
#   诊断桶 vs_AX_fund_handling 不得升格进 dj0
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；过户费 ≠ 证管费；不改 DA
#   诊断桶 vs_DA_etf_transfer 不得升格进 dj0
# params.ashare_fee_handoff           建议 s_page
#   消费 S 的沪深股票竞价经手费切日，或显式旁路；经手费切日 ≠ 证管费；不改 S
#   诊断桶 copy_20230828_handling_cut_onto_csrc 不得升格进 dj0
# params.block_discount_handoff       建议 di_page
#   消费 DI 的股票大宗经手下浮，或显式旁路；大宗折扣 ≠ 基金证管费；不改 DI
# params.commission_double_handoff    建议 dh_page
#   消费 DH 的佣金双计，或显式旁路；不改 DH
# params.bse_fee_handoff              建议 dg_page
#   消费 DG 的北交所经手费档，或显式旁路；不改 DG
# params.exch_handling_fee_handoff    建议 df_page
#   消费 DF 的可交换债经手费沪深分列，或显式旁路；不改 DF
# params.cb_transfer_fee_handoff      建议 dd_page
#   消费 DD 的转债过户费，或显式旁路；不改 DD
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的转债印花税，或显式旁路；不改 DC
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的可转债经手费，或显式旁路；不改 DB
# params.bse_limit_aft_handoff        建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；不重开假设-AC；不改 AC
# params.stock_transfer_fee_handoff   建议 u_page
# params.stock_stamp_handoff          建议 v_page
# params.cb_rule_handoff              建议 q_page
# params.stock_etf_rotation_handoff   建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 基金证管费；不重开假设-R；不改 R
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
#   成交时点与停牌交 D；双字母 DJ ≠ 单字母假设-D；不改 D
# params.intraday_halt_handoff        建议 j_page
#   无板日临停交 J；双字母 DJ ≠ 单字母假设-J；不改 J
# params.fund_csrc_fee_handoff        建议 self
# params.dj0_primary_demo             写死冻结 invent_ashare_csrc_fee_on_fund
#   单一主报写死，单挂；禁与 invent_asof_leak_fund_csrc_fee 双挂；DJ1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_fund_csrc_fee 只作对照，不得升格进 dj0，不得双挂
#   诊断桶 charge_etf_as_stock_csrc / charge_bond_as_stock_csrc / copy_20230828_handling_cut_onto_csrc / vs_T_stock_csrc / vs_DE_cb_csrc / vs_AX_fund_handling / vs_DA_etf_transfer 不得升格进 dj0
#   尤重：禁止把 T 的股票证管费切日与「对基金/ETF 发明证管费」合成/混读后写进 dj0
#   尤重：禁止把 DE 可转债证管费与本页基金/ETF 证管费合成/混读后写进 dj0
# params.dj0_invent_ashare_csrc_fee_on_fund 建议 True
# params.dj1_asof_leak_fund_csrc_fee_only 建议 True
#   半泄露对照；DJ1 不升格并列主报；不得把 invent_asof_leak_fund_csrc_fee 写进 dj0
# params.dj2_pit_fund_bond_exempt     建议 True
# params.merge_with_DI                建议 False
# params.merge_with_DH                建议 False
# params.merge_with_DG                建议 False
# params.merge_with_DF                建议 False
# params.merge_with_DE                建议 False
# params.merge_with_DD                建议 False
# params.merge_with_DC                建议 False
# params.merge_with_DB                建议 False
# params.merge_with_DA                建议 False
# params.merge_with_T                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_S                 建议 False
# params.merge_with_AC                建议 False
# params.merge_with_U                 建议 False
# params.merge_with_V                 建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_R                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_J                 建议 False
# params.missing_sec_type_or_csrc_row_policy 建议 skip
# params.day_freq_proxy               建议 fund_csrc_fee_sensitivity
# params.universe_rule                建议 fund_csrc_fee_misapply_check
# params.redline_v0_exempt_scope      建议 position_industry_dj_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DJ；勿把这个键读成实验 DJ
#   不另挂主报，不预留 #120，不写下一字母
```

### 2.2 三组对照（DJ0 / DJ1 / DJ2）

| 组 | 角色 | 口径 |
|----|------|------|
| DJ0 | 天真 / 对基金发明股票证管费 | 按 `dj0_primary_demo` **写死冻结**单一主报 `invent_ashare_csrc_fee_on_fund`（单挂写死）：对场内基金/ETF 发明或误套股票证管费。**禁**与 `invent_asof_leak_fund_csrc_fee` 双挂主报。**禁把 T 股票证管费切日、DE 转债证管费合成进 `dj0`**（只作对照/旁路，不得升格进 `dj0` 或另挂主报） |
| DJ1 | 半泄露 | 仅核对日把「基金/债券免收」或现行证管费栏铺到全历史（`invent_asof_leak_fund_csrc_fee`）；**不得升格并列主报**，也不得写进 `dj0`（写死冻结：DJ1 不升格），不得双挂 |
| DJ2 | 诚实 / 依法免收、不套股票档 | `fund_csrc_fee_honest=pit_fund_bond_exempt_not_stock_tier`（写死冻结）：缺证券类别或官方证管费栏则 skip；基金/债券依法免收，不套股票档。股票证管费切日只消费 T，转债证管费只消费 DE，基金经手费只消费 AX，场内基金过户只消费 DA，股票经手费切日只消费 S，大宗折扣只消费 DI，或显式旁路 |

对 ETF 套股票证管费、对债券套股票证管费、把 2023-08-28 经手费降幅抄到证管费，以及相对 T / DE / AX / DA 的对照截（`charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dj0_primary_demo`。`vs_T_stock_csrc` 只标记「有人把 T 的股票证管费切日和本页对基金/ETF 发明证管费合成/混读」这一类失效，**不得升格进 `dj0`**。`vs_DE_cb_csrc` 只标记「有人把 DE 可转债证管费和本页基金/ETF 证管费合成/混读」，**不得升格进 `dj0`**。T 的切日、DE 的转债证管费、AX 的基金经手费、DA 的过户费、DI 的大宗折扣只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dj0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺证券类别或官方证管费栏则 skip；基金/债券依法免收，不套股票证管费档。方向随锚写死：**不要把核对日免收或股票 0.02‰ 铺满全历史**。`事实与坑` 2026-10-30 已写基金和债券免收、不要按股票证管费抽；股票切日和「2023-08-28 没改证管费」留在假设-T，本页不重开。可转债证管费留在 DE，基金经手费留在 AX，场内基金过户留在 DA，大宗折扣留在 DI，股票经手费切日留在 S，都不改。`params.Y` 的 0.02 是无量纲相对门槛，不是证管费 0.02‰。缺证券类别或官方证管费栏则 skip，不用股票档或自造‰把腿填上，也不要看见表上没这一栏就发明一条已核过的 0 费率冒充诚实。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dj0_primary_demo` / `params.Y`·G·N·Y2 / 免收开关 / 桶 / 是否把股票 0.02‰ 铺到基金）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DJ0）/ 半泄露组（DJ1）相对诚实组（DJ2）的成本差、误套截**显著且集中在对基金发明股票证管费的桶**；分桶「对 ETF 套股票证管费 / 对债券套股票证管费 / 2023-08-28 经手费降幅抄到证管费 / 核对日泄露 / vs T·DE·AX·DA」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 0.02‰ 或「免收=0」冻成全历史唯一费率，也不把 `params.Y` 的 0.02 读成证管费。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 T 的股票证管费切日、DE 的转债证管费、AX 的基金经手费、DA 的场内基金过户、DI 的大宗折扣、S 的竞价经手费切日、DH 的佣金双计、DG 的北交所档、DF 的可交换债经手费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、AC 的北交所涨跌幅与盘后、U/V 的股票过户与印花税、Q 的回转与涨跌幅、R 的股票 ETF 回转、A 的板上容量、D 的成交时点、J 的无板日临停解释；或 `dj0_primary_demo` 与 `invent_asof_leak_fund_csrc_fee` 双挂；或 DJ1 升格并列主报；或 `charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer` 诊断桶升格主报；或把 T 的股票证管费切日与「对基金/ETF 发明证管费」合成进 `dj0`；或把 DE 可转债证管费合成进 `dj0`；或实验字母 DJ 与单字母 D/J 或 params.Y/G/N 混读；或把 `params.Y` 的 0.02 读成证管费 0.02‰；或把核对日免收写成已冻并铺满全历史；或缺证券类别 / 官方证管费栏仍对基金发明股票证管费；或重开假设-T / 假设-AC / 假设-R。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DJ0/DJ1/DJ2。股票证管费走 T 的诚实切日或显式旁路，不在本页改 T，也不把 T 的切日升成主报。报告成本差、误套截。不把 0.02‰ 标成已冻的基金费率，也不把 `params.Y` 的 0.02 读成证管费。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_ashare_csrc_fee_on_fund` / `invent_asof_leak_fund_csrc_fee` / `charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer` / `missing_sec_type_or_official_csrc_row_not_skip` / `vs_DI_block_discount` / `vs_S_auction_handling` / `vs_DH_commission_double` / `vs_DG_bse_handling` / `vs_DF_exch_handling` / `vs_DD_cb_transfer` / `vs_DC_cb_stamp` / `vs_DB_cb_handling` / `vs_AC_bse_limit_aft` / `vs_U_stock_transfer` / `vs_V_stock_stamp` / `vs_Q_cb_rule` / `vs_R_stock_etf_rotation` / `vs_A_board_capacity` / `vs_D_fill_time` / `vs_J_intraday_halt`

`charge_etf_as_stock_csrc`、`charge_bond_as_stock_csrc`、`copy_20230828_handling_cut_onto_csrc`、`vs_T_stock_csrc`、`vs_DE_cb_csrc`、`vs_AX_fund_handling`、`vs_DA_etf_transfer`、`missing_sec_type_or_official_csrc_row_not_skip` 只作诊断桶：它们不是 `dj0`，也不是 DJ1，**不得升格主报**。`vs_T_stock_csrc` 没有对应的「T 切日 + 基金发明证管费」合成主报。T 的股票证管费切日只作诊断，**不得与对基金/ETF 发明证管费合成后升格进 `dj0`**。DE 的可转债证管费只作诊断，**不得升格进 `dj0`**。`invent_asof_leak_fund_csrc_fee` 只服务 DJ1，**不得升格进 `dj0`，不得双挂**。`invent_ashare_csrc_fee_on_fund` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 对场内基金/ETF 发明或误套股票证管费，并拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成证管费 0.02‰。**尤重：`params.Y` 的 0.02 ≠ 证管费 0.02‰**。
- 缺证券类别或官方证管费栏仍不 skip，并用股票档、自造‰或发明「免费=0」把腿填上。
- 把核对日「基金/债券依法免收」写成全历史唯一费率，并铺满全历史。方向是核对日依法免收，不是全历史已冻费率。锚六键已写死冻结。
- 把「股票证管费切日已诚实（T）/ 转债证管费已诚实（DE）/ 基金经手费已诚实（AX）/ 场内基金过户已诚实（DA）/ 大宗折扣已诚实（DI）」写成「场内基金证管费已诚实」。不改 T / DE / AX / DA / DI。
- 把 T 的股票证管费切日和本页「对基金/ETF 发明证管费」合成或混读后升格进 `dj0`。诊断桶 `vs_T_stock_csrc` 只作对照。
- 把 DE 可转债证管费和本页基金/ETF 证管费合成或混读后升格进 `dj0`。诊断桶 `vs_DE_cb_csrc` / `charge_bond_as_stock_csrc` 只作对照。
- 把 2023-08-28 经手费降幅抄成证管费改档，并升格进 `dj0`。诊断桶 `copy_20230828_handling_cut_onto_csrc` 只作对照。不改 S。
- 把「可交换债经手费已诚实（DF）/ 转债过户费已诚实（DD）/ 转债印花税已诚实（DC）/ 转债经手费已诚实（DB）」写成「场内基金证管费已诚实」。不改 DF / DD / DC / DB。
- `dj0_primary_demo` 与 `invent_asof_leak_fund_csrc_fee` 双挂主报；DJ1 升格并列主报；诊断桶（`charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer`）升格为第二个主报。
- 实验字母 DJ 与单字母 D/J 或 params.Y/G/N 混读。
- 改 DI / DH / DG / DF / DE / DD / DC / DB / DA / T / AX / S / AC / U / V / Q / R / A / D / J 正文；重开假设-T；重开假设-AC；重开假设-R；抢 A 真数队列；标纸面齐；写 A/D–DJ纸面齐；开真数/回测/实盘；用复权价当费用基数；结论写成「基金证管费更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权成交金额、交易日、**证券类别**（股票 / ETF / 封闭式 / LOF / 债券 / 可转债；仅用于把腿分回 T、DE、AX、DA 或本页）、官方证管费栏（有没有这一栏、栏上写的是股票档还是基金/债券免收）。
- 没有证券类别或官方证管费栏时，按写死冻结的 `fund_csrc_fee_over_policy=skip_if_sec_type_or_official_csrc_row_missing` skip，不得对基金发明股票证管费，也不得用核对日免收把腿填满全历史，更不得把缺栏写成已核过的 0。
- 旁路消费：T 的股票证管费切日、DE 的转债证管费、AX 的基金经手费、DA 的场内基金过户费、S 的沪深股票竞价经手费切日、DI 的大宗折扣、DH 的佣金双计、DG 的北交所经手费、DF 的可交换债经手费、DD 的转债过户费、DC 的转债印花税、DB 的转债经手费、AC 的北交所涨跌幅与盘后、U 的股票过户费、V 的股票印花税、Q 的转债规则、R 的股票 ETF 回转、J 的无板日临停之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** T 的股票证管费切日、DE 的转债证管费不收到本页主报。
- 未复权价；asof **写死冻结** `2026-10-16`。核对日方向「基金/债券依法免收」是写死冻结的机制方向，不是已冻全历史费率。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`fund_csrc_fee_honest=pit_fund_bond_exempt_not_stock_tier`（基金/债券依法免收，不套股票档；**禁止把核对日免收或股票 0.02‰ 写成全历史唯一费率**）；`fund_csrc_fee_scope=etf_closed_lof_bond_apart_from_ashare_csrc`（ETF / 封闭式 / LOF / 债券与股票证管费分开）；`fund_csrc_fee_over_policy=skip_if_sec_type_or_official_csrc_row_missing`（缺证券类别或官方证管费栏则 skip）；`dj0_primary_demo=invent_ashare_csrc_fee_on_fund`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_fund_csrc_fee` 双挂；DJ1 不升格；诊断桶不升格主报；**禁把 T 股票证管费切日、DE 转债证管费合成进 `dj0`**，只作对照/旁路，不得升格进 `dj0` 或另挂主报）；`stock_csrc_fee_handoff=t_page`；`cb_csrc_fee_handoff=de_page`；`fund_handling_fee_handoff=ax_page`；`etf_transfer_fee_handoff=da_page`；`ashare_fee_handoff=s_page`；`merge_with_DI/DH/DG/DF/DE/DD/DC/DB/DA/T/AX/S/AC/U/V/Q/R/A/D/J=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误套截 ΔFundCsrcFee / 净收益差 / DJ1−DJ2；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同）**；**params.Y/G/N ≠ 实验字母 DJ ≠ 单字母 D/J**；**勿把 params.Y 读成实验字母 DJ，亦勿把单字母假设-D / 假设-J 读成双字母 DJ**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成证管费率‰）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #120。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`5bf9b20`（A/D–DI纸面齐已合，全长 `5bf9b20eedc214525a8d0053c5147cc3add03d56`）；三冻补丁基 tip=`474421ea` / `474421ea046af22b6138602ae83630ffbdb804ec`；分支起点 HEAD=`5a3f313d` / `5a3f313d2cc33121515ac68566af84c44e7dbfa6`。

---

## 8. 结论

（空；预检有条件通过·三条已冻·待复检；复检通过前不得标纸面齐；**禁止标纸面齐**；**未标纸面齐**；**不写 A/D–DJ纸面齐**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-09）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DJ-20261109.md`（原样落入，不改结论；SHA256=`75ed3efb4e8beeaa4860bfd1b4c1ca8953e0039d8dcfd818c11715d480f13474`；预检 2026-11-09；**结论：有条件通过**；tip基=`474421ea` / `474421ea046af22b6138602ae83630ffbdb804ec`；本补丁分支起点 HEAD=`5a3f313d` / `5a3f313d2cc33121515ac68566af84c44e7dbfa6`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、误套截 ΔFundCsrcFee、净收益差、DJ1−DJ2 专项。**`params.Y` ≠ 实验字母 DJ**；**`params.G` ≠ 实验字母 DJ**；**`params.N` ≠ 实验字母 DJ**；亦 ≠ 单字母假设-D / 假设-J。**勿把 `params.Y` 读成实验字母 DJ，亦勿把单字母假设-D / 假设-J 读成双字母 DJ**。**尤重：`params.Y` 的 `0.02` ≠ 证管费 `0.02‰`**（**params.Y 的 0.02 ≠ 证管费 0.02‰**）。二者量纲与语义都不同：`params.Y=0.02` 是无量纲相对门槛，0.02‰ 是股票证管费率，禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dj0_primary_demo`**：**写死冻结** **`invent_ashare_csrc_fee_on_fund`**（单一主报，单挂写死）。**禁止**与 **`invent_asof_leak_fund_csrc_fee`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DJ1 核对日把「基金/债券免收」或现行证管费栏铺到全历史只作半泄露对照，**不得升格与 dj0 并列主报**，也不得把 `invent_asof_leak_fund_csrc_fee` 写进 `dj0`。`charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer` / `missing_sec_type_or_official_csrc_row_not_skip` **只作诊断桶，不得升格主报**。DJ1 / 诊断桶 **不升格**。**禁把 T 股票证管切日 / DE 转债证管 合成/混读升格进 `dj0`**：这些只作对照/旁路，**不得升格进 `dj0`，不得另挂主报**。

3. **场内基金证管费诚实锚六键升格写死（不可再写「建议」）**：`params.fund_csrc_fee_honest=pit_fund_bond_exempt_not_stock_tier`；`params.fund_csrc_fee_scope=etf_closed_lof_bond_apart_from_ashare_csrc`；`params.fund_csrc_fee_over_policy=skip_if_sec_type_or_official_csrc_row_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺证券类型或官方证管行 → skip；基金/债券依法免收。禁止把核对日免收或股票 0.02‰ 铺满全历史。禁止跑后改锚，或用股票档 / 核对日现行费率 / 发明‰ / 缺证券类别仍硬抽 / 把 T 股票证管切日或 DE 转债证管升格进 dj0 冒充诚实 PIT。

**硬分列保住**：DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠T≠AX≠S≠AC≠U≠V≠Q≠R≠A≠D≠J；**双字母 DJ ≠ 单字母假设-D / 假设-J / 假设-T**；**params.Y / params.G / params.N ≠ 实验字母 DJ ≠ 单字母 D/J**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰**；**场内基金证管费误套 ≠ T股票证管 ≠ DE转债证管 ≠ AX基金经手 ≠ DA过户 ≠ DI大宗折扣**；不抢 A；不改已齐 A–DI / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH 正文；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**禁把 T 股票证管切日 / DE 转债证管 合成/混读升格进 dj0**。

**状态**：**预检有条件通过·三条已冻·待复检**；**禁止标任何纸面齐**；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DJ纸面齐**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 风控预检补丁·冻结三条写死——依据 `预检-假设DJ-20261109.md`（SHA256=`75ed3efb4e8beeaa4860bfd1b4c1ca8953e0039d8dcfd818c11715d480f13474`；结论=有条件通过；tip基=`474421ea` / `474421ea046af22b6138602ae83630ffbdb804ec`；分支起点 HEAD=`5a3f313d` / `5a3f313d2cc33121515ac68566af84c44e7dbfa6`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔFundCsrcFee / 净收益差 / DJ1−DJ2；**params.Y/G/N ≠ 实验字母 DJ ≠ 单字母 D/J**；**勿把 params.Y 读成实验字母 DJ，亦勿把单字母假设-D / 假设-J 读成双字母 DJ**；**尤重 params.Y 的 0.02 ≠ 证管费 0.02‰（量纲与语义不同）**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成证管费率‰）；② `params.dj0_primary_demo=invent_ashare_csrc_fee_on_fund`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_fund_csrc_fee` 双挂；DJ1 不升格；诊断桶 `charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer` 不升格；**禁把 T 股票证管切日 / DE 转债证管 合成/混读升格进 dj0**，只作对照/旁路，不得升格进 dj0 或另挂主报）；③ 锚六键写死 `fund_csrc_fee_honest=pit_fund_bond_exempt_not_stock_tier` / `fund_csrc_fee_scope=etf_closed_lof_bond_apart_from_ashare_csrc` / `fund_csrc_fee_over_policy=skip_if_sec_type_or_official_csrc_row_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`（缺证券类型或官方证管行 → skip；基金/债券依法免收；禁止把核对日免收或股票 0.02‰ 铺满全历史）。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DJ纸面齐**；不改已齐 A–DI / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH；不重开假设-T；不重开假设-AC；不重开假设-R；不开回测/真数/实盘。基于 tip=`474421ea`。 |
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；场内基金证管费误套股票；`dj0_primary_demo` 建议 `invent_ashare_csrc_fee_on_fund`，单一主报，单挂，禁与 `invent_asof_leak_fund_csrc_fee` 双挂，DJ1 不升格；诊断桶 `charge_etf_as_stock_csrc` / `charge_bond_as_stock_csrc` / `copy_20230828_handling_cut_onto_csrc` / `vs_T_stock_csrc` / `vs_DE_cb_csrc` / `vs_AX_fund_handling` / `vs_DA_etf_transfer` 不升格；**尤重 T 的股票证管费切日 ≠ 本页「对基金/ETF 发明证管费」，禁止合成/混读升格进 dj0**；**尤重 DE 可转债证管费 ≠ 本页基金/ETF 证管费，禁止合成进 dj0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DJ ≠ 单字母 D/J**，且 **params.Y 的 0.02 ≠ 证管费 0.02‰**；锚建议 `fund_csrc_fee_honest=pit_fund_bond_exempt_not_stock_tier` / scope=`etf_closed_lof_bond_apart_from_ashare_csrc` / over_policy=`skip_if_sec_type_or_official_csrc_row_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；口径：缺证券类别或官方证管费栏则 skip；基金/债券依法免收、不套股票档（**草稿方向，尚未冻，不要写成已冻**）；handoff：`stock_csrc_fee_handoff=t_page`，`cb_csrc_fee_handoff=de_page`，`fund_handling_fee_handoff=ax_page`，`etf_transfer_fee_handoff=da_page`，`ashare_fee_handoff=s_page`；`merge_with_DI/DH/DG/DF/DE/DD/DC/DB/DA/T/AX/S/AC/U/V/Q/R/A/D/J=False`；**DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠T≠AX≠S≠AC≠U≠V≠Q≠R≠A≠D**；**双字母 DJ ≠ 单字母假设-D / 假设-J**；**场内基金证管费误套 ≠ T股票证管 ≠ DE转债证管 ≠ AX基金经手 ≠ DA过户 ≠ DI大宗折扣**；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DJ纸面齐**；不改已齐 A–DI / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH 及其他已存在假设页；不重开假设-T；不重开假设-AC；不重开假设-R；不写下一字母；不预留 #120；不开真数/回测/实盘）。基 tip=`5bf9b20`（A/D–DI纸面齐已合，全长 `5bf9b20eedc214525a8d0053c5147cc3add03d56`；不改该 tip 上的 #110–#118，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文） |
