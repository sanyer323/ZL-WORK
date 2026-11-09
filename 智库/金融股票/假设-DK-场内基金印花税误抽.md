# 假设-DK · 场内基金印花税误抽（成本诚信）

更新：2026-11-09  
来源：总管线 / 默认分支 HEAD `4cf0270` 上清单 #119=DJ 已收口（A/D–DJ纸面齐已合入该 tip；**不改假设-DJ 正文**，亦不改已齐 A–DJ / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI / 假设-V / 假设-T / 假设-S / 假设-AX / 假设-AC / 假设-R / 假设-K 及其他已存在假设页；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-V**）后写下一草稿 DK；清单 #119=DJ，本页占用 **#120=DK**；选题是场内基金（ETF / 封闭式 / LOF / 债券基金）被发明印花税；假设-V 只收股票印花税切日（其切日 ≠ 本页「对基金/ETF 发明印花税」），假设-DC 只收可转债印花税，假设-DJ 只收场内基金证管费，假设-AX 只收基金经手费，假设-DA 只收场内基金过户费；**新建实验 DK**；不写下一字母；不预留 #121  
状态：**A/D–DK纸面齐（预检有条件通过·三条已冻）**（结论栏空；禁止把「对场内基金/ETF 发明印花税」当诚实成本；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改已齐 A–DJ / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI**；尤其不改假设-V / 假设-DC / 假设-DJ / 假设-AX / 假设-DA / 假设-T / 假设-AC / 假设-R / 假设-D / 假设-K；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-V**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单开跑前本序号挂实验 DK（#120）。一句话误开：回测对场内基金/ETF 发明印花税，或缺证券类别 / 买卖方向仍不 skip，系统性改写基金腿成本（相对诚实锚偏误）。

> **字母消歧（硬）**：本页**实验字母 DK** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族；写死冻结 0.02；**params.Y ≠ 实验字母 DK**；**勿把 `params.Y` 读成实验字母 DK**；**尤重：`params.Y` 的 0.02 ≠ 印花税率‰**——量纲与语义都不同：`params.Y=0.02` 是无量纲相对门槛，不是印花税率‰，也不是股票印花税 1‰/0.5‰；**禁把占位读成 1‰/0.5‰**）≠ **`params.G`**（同族门槛，写死冻结 0.01；**params.G ≠ 实验字母 DK**）≠ **`params.N`**（失败/废单率差门槛；写死冻结 0.05；**params.N ≠ 实验字母 DK**）≠ **单字母实验 D**（成交时点与停牌；**双字母 DK ≠ 单字母假设-D；严禁复用假设-D**）≠ **单字母实验 K**（融券空头名单 PIT；**双字母 DK ≠ 单字母假设-K；严禁复用假设-K**）≠ **单字母实验 A**（板上枯竭/涨停可成交；**双字母 DK ≠ 单字母假设-A**）≠ **单字母实验 V**（股票印花税切日；**双字母 DK ≠ 单字母假设-V；严禁复用假设-V；不重开假设-V**）≠ 双字母 **DJ**（场内基金证管费）≠ **DI**（股票大宗经手下浮）≠ **DH**（佣金双计）≠ **DG**（北交所经手费）≠ **DF**（可交换债经手费沪深分列）≠ **DE**（可转债证管费）≠ **DD**（可转债过户费）≠ **DC**（可转债印花税）≠ **DB**（可转债经手费）≠ **DA**（场内基金过户费）≠ **T**（股票证管费）≠ **AX**（基金经手费）≠ **S**（沪深股票竞价经手费切日）≠ **AC**（北交所涨跌幅与盘后）≠ **U**（股票过户费）≠ **Q**（可转债规则混用）≠ **R**（股票 ETF 回转）。**DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠V≠T≠AX≠S≠AC≠U≠Q≠R≠A≠D**。**双字母 DK ≠ 单字母 D/K**。**params.Y/G/N ≠ 实验字母 DK；亦 ≠ 单字母 D/K**。**勿把 `params.Y` 读成实验字母 DK，亦勿把单字母假设-D / 假设-K 读成双字母 DK**。**尤重：`params.Y` 的 0.02 ≠ 印花税率‰**。**禁把占位读成 1‰/0.5‰**。**场内基金印花税误抽 ≠ V股票印花 ≠ DC转债印花 ≠ DJ基金证管 ≠ AX经手 ≠ DA过户**。**尤重：V 的股票印花税切日 ≠ 本页「对基金/ETF 发明印花税」——禁止合成/混读升格进 `dk0`**。**尤重：DC 可转债印花税 ≠ 本页基金/ETF 印花税——禁止合成/混读升格进 `dk0`**。**尤重：DJ 基金证管费 ≠ 本页基金印花税——禁止合成/混读升格进 `dk0`**。

### 专节 · 双字母 DK ≠ 单字母假设-D / 假设-K；且 ≠ 假设-V / 假设-DC / 假设-DJ / 假设-AX / 假设-DA（硬）

| 维度 | 对照页 | 本页假设-DK（双字母） |
|------|--------|----------------------|
| 题面 V | **股票印花税切日**（税目里的股票和股票 CDR；出让方；2023-08-28 的 1‰/0.5‰ 切日留在 V） | 股票印花税切日 ≠ 对基金/ETF 发明印花税。本页专测：场内基金被发明印花税。**DK≠V**；**严禁复用假设-V**；**不重开假设-V**；**不改 V**；**禁把 V 的股票印花税切日与本页「对基金/ETF 发明印花税」合成/混读升格进 `dk0`**；`stock_stamp_handoff=v_page`；诊断桶 `vs_V_stock_stamp` / `stock_cut_20230828_copied_onto_fund_stamp` 不升格 |
| 题面 DC | **可转债印花税**（转债现货不在税目内；缺证券类别或方向则 skip） | 可转债印花税 ≠ 基金/ETF 印花税。**DK≠DC**；**不改 DC**；**禁把 DC 可转债印花税与本页基金/ETF 印花税合成/混读升格进 `dk0`**；`cb_stamp_handoff=dc_page`；诊断桶 `vs_DC_cb_stamp` 不升格 |
| 题面 DJ | **场内基金证管费**（基金/债券依法免收，不套股票证管费） | 基金证管费 ≠ 基金印花税。**DK≠DJ**；**不改 DJ**；**禁把 DJ 基金证管费与本页基金印花税合成/混读升格进 `dk0`**；`fund_csrc_fee_handoff=dj_page`；诊断桶 `vs_DJ_fund_csrc` 不升格 |
| 题面 AX | **基金/ETF 经手费档** | 基金经手费 ≠ 基金印花税。**DK≠AX**；**不改 AX**；`fund_handling_fee_handoff=ax_page`；诊断桶 `vs_AX_fund_handling` 不升格 |
| 题面 DA | **场内基金过户费** | 场内基金过户 ≠ 基金印花税。**DK≠DA**；**不改 DA**；`etf_transfer_fee_handoff=da_page`；诊断桶 `vs_DA_etf_transfer` 不升格 |
| 题面 DI | **股票大宗经手下浮**（大宗折扣 30%） | 大宗折扣 ≠ 基金印花税误抽。**DK≠DI**；**不改 DI**；`block_discount_handoff=di_page` |
| 题面 DH | **佣金已含代收费再外加经手费** | 佣金双计 ≠ 基金印花税误抽。**DK≠DH**；**不改 DH**；`commission_double_handoff=dh_page` |
| 题面 DG | **北交所经手费档** | 北交所经手费 ≠ 基金印花税误抽。**DK≠DG**；**不改 DG**；`bse_fee_handoff=dg_page` |
| 题面 DF | **可交换债经手费沪深分列** | 可交换债经手费 ≠ 本机制。**DK≠DF**；**不改 DF**；`exch_handling_fee_handoff=df_page` |
| 题面 DE | **可转债证管费** | 转债证管费 ≠ 本机制。**DK≠DE**；**不改 DE**；`cb_csrc_fee_handoff=de_page` |
| 题面 DD | **可转债过户费** | 转债过户费 ≠ 本机制。**DK≠DD**；**不改 DD**；`cb_transfer_fee_handoff=dd_page` |
| 题面 DB | **可转债经手费** | 转债经手费 ≠ 本机制。**DK≠DB**；**不改 DB**；`cb_handling_fee_handoff=db_page` |
| 题面 T | **证管费主报股票** | 股票证管费 ≠ 基金印花税。**DK≠T**；**严禁复用假设-T**；**不重开假设-T**；**不改 T**；`stock_csrc_fee_handoff=t_page` |
| 题面 S | **沪深 A 股竞价经手费切日** | 经手费切日 ≠ 基金印花税。**DK≠S**；**不改 S**；`ashare_fee_handoff=s_page` |
| 题面 AC | **北交所涨跌幅与盘后** | 涨跌幅、盘后 ≠ 基金印花税。**DK≠AC**；**不改 AC**；**不重开假设-AC**；`bse_limit_aft_handoff=ac_page` |
| 题面 U | **股票过户费** | 股票过户费 ≠ 基金印花税。**DK≠U**；**不改 U**；`stock_transfer_fee_handoff=u_page` |
| 题面 Q | **可转债按股票规则回放** | 规则混用 ≠ 基金印花税。**DK≠Q**；**不改 Q**；`cb_rule_handoff=q_page` |
| 题面 R | **股票 ETF 假回转** | 回转规则 ≠ 基金印花税。**DK≠R**；**不改 R**；**不重开假设-R**；`stock_etf_rotation_handoff=r_page` |
| 题面 A | **涨停可成交 / 板上枯竭**（真数队列） | 容量门槛 ≠ 基金印花税误抽。**DK≠A**；**不抢 A 真数队列**；**不改 A** |
| 题面 D | **成交时点与停牌** | 何时成交 ≠ 基金印花税抽在哪一档。**双字母 DK ≠ 单字母假设-D**；**严禁复用假设-D**；**DK≠D**；**不改 D** |
| 题面 K | **融券空头名单 PIT** | 名单闸门 ≠ 基金印花税。**双字母 DK ≠ 单字母假设-K**；**严禁复用假设-K**；**不改 K**；`shortable_list_handoff=k_page` |
| 主演示 | （各页自有；本页不引用覆盖） | `invent_stamp_tax_on_fund`（**写死冻结**单一主报，单挂写死；禁与 `invent_asof_leak_fund_stamp` 双挂；DK1 不升格；`bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling` 只作诊断对照，不升格主报；**尤重禁止把 V 股票印花税切日、DC 转债印花税、DJ 基金证管费合成进 `dk0`**） |
| 文档 | 清单实验 DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / V / T / AX / S / AC / U / Q / R / A / D / K（**只读；禁止改写**） | `假设-DK-场内基金印花税误抽.md`（新建） |
| 预检键 | 实验字母 DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / V / T / AX / S / AC / U / Q / R / A / D / K / Y / G / N | 实验字母 **DK** / `dk0_primary_demo`；**不得**占用或改写预检 DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/V/T/AX/S/AC/U/Q/R/A/D/K |

**禁止**：把 DK 写成「DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / V / T / AX / S / AC / U / Q / R / A / D / K 的续篇」；把「股票印花税切日已诚实（V）/ 转债印花税已诚实（DC）/ 基金证管费已诚实（DJ）/ 基金经手费已诚实（AX）/ 场内基金过户已诚实（DA）」写成「场内基金印花税已诚实」；把实验字母 DK 与单字母 D/K 或 params.Y/G/N 混读；**尤重勿把单字母假设-D / 假设-K 读成双字母 DK**；**尤重勿把 `params.Y` 读成实验字母 DK**；**尤重 `params.Y` 的 0.02 ≠ 印花税率‰（量纲与语义不同）**；**禁把占位读成 1‰/0.5‰**；**尤重 V 的股票印花税切日 ≠ 本页「对基金/ETF 发明印花税」，禁止合成/混读升格进 `dk0`**；**尤重 DC 可转债印花税 ≠ 本页基金/ETF 印花税，禁止合成/混读升格进 `dk0`**；**尤重 DJ 基金证管费 ≠ 本页基金印花税，禁止合成/混读升格进 `dk0`**；把 `invent_asof_leak_fund_stamp` 升格进 `dk0` 或与主报双挂；把诊断桶 `bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling` 升格进 `dk0`。本页主键只用 `dk0` / `dk1` / `dk2` 与 `fund_stamp_*`。不写下一字母。不预留 #121。

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一未复权成交金额下，回测对场内基金（ETF / 封闭式 / LOF / 债券基金）发明印花税，或缺证券类别 / 买卖方向仍不 skip，相对「缺证券类别或买卖方向则 skip；基金/ETF 不在印花税税目内」的诚实组，会**系统性改写基金腿成本**——相对诚实锚偏误。

核对日方向（随锚写死；禁止把「不在税目内」或 V 的 1‰/0.5‰ 写成全历史唯一费率）：基金/ETF 不在印花税税目内。税目是股票和以股票为基础的存托凭证，不是场内基金。这不是把 1‰ 或 0.5‰ 冻成全历史唯一费率，也不是把 `params.Y` 的 0.02 读成印花税率‰。**禁把占位读成 1‰/0.5‰**。

证伪方向：若天真组 / 半泄露组相对诚实组的成本差、误抽截在标定噪声带内可忽略，且「对 ETF 双边抽印花税 / 把 2023-08-28 股票切日抄到基金印花税 / 对债券基金套股票印花税 / 核对日泄露 / vs V·DC·DJ·DA·AX」分桶不改变结论，则本假设在该样本与开关设定下不成立。

---

## 2. 口径与可检验设计（纸面骨架）

### 2.1 写死键（拉数前冻结；本页不开跑；Y/G/N/Y2 · dk0 与锚 **三条已冻**）

```
# 配置写死键（见 §7 与文末风控预检补丁；预检有条件通过·三条已冻·待复检；下列三冻已写死冻结）
# 【消歧】params.Y = 显著性门槛；写死冻结 0.02；**≠ 实验字母 DK ≠ 单字母假设-D / 假设-K**；勿把 params.Y 读成实验字母 DK
# 【消歧】尤重：params.Y 的 0.02 ≠ 印花税率‰（量纲与语义不同：无量纲相对门槛 ≠ 印花税率‰）
# 【消歧】禁把占位 0.02/0.01/0.05/0.015 读成 1‰/0.5‰（1‰/0.5‰ 是 V 页股票印花税切日用的数，不是本页门槛，也不是本页要冻的基金费率）
# 【消歧】params.G = 同族门槛；写死冻结 0.01；**≠ 实验字母 DK ≠ 单字母 D/K**
# 【消歧】params.N = 失败/废单率差门槛；写死冻结 0.05；**≠ 实验字母 DK ≠ 单字母 D/K**
# params.Y2 写死冻结 0.015
# params.Y / G / N / Y2               写死冻结 0.02/0.01/0.05/0.015（相对门槛：成本差 / 误抽截 ΔFundStamp / 净收益差 / DK1−DK2；**params.Y/G/N ≠ 实验字母 DK ≠ 单字母假设-D / 假设-K**；**尤重 params.Y 的 0.02 ≠ 印花税率‰**；**禁把占位读成 1‰/0.5‰**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成印花税率‰）
# params.fill_time                    写死冻结 next_open
# params.asof_check_date              写死冻结 2026-10-16
# params.px_basis                     建议 unadj
# params.fail_policy                  写死冻结 skip
# params.fund_stamp_honest            写死冻结 pit_fund_out_of_stamp_tax_scope
#   诚实锚方向（已写死冻结；禁止把「不在税目内」或 V 的 1‰/0.5‰ 写成全历史唯一费率）：
#   基金/ETF 不在印花税税目内
#   缺证券类别或买卖方向 → skip
#   禁止把核对日「不在税目内」或 V 的 1‰/0.5‰ 铺满全历史（那是半泄露或误抽，不得进 dk0）
#   枚举已写死冻结
#   不把 V 的股票印花税切日、DC 的转债印花税、DJ 的基金证管费、AX 的基金经手费、DA 的过户费写成基金印花税诚实锚
# params.fund_stamp_scope             写死冻结 etf_closed_lof_bond_fund_not_stock_cdr
#   ETF / 封闭式 / LOF / 债券基金与股票、股票 CDR 分开
#   场内基金印花税误抽 ≠ V股票印花 ≠ DC转债印花 ≠ DJ基金证管 ≠ AX经手 ≠ DA过户
# params.fund_stamp_over_policy       写死冻结 skip_if_sec_type_or_side_missing
#   缺证券类别或买卖方向则 skip；禁在缺字段时仍对基金发明印花税
# params.stock_stamp_handoff          建议 v_page
#   消费 V 的股票印花税切日，或显式旁路；股票印花税切日 ≠ 对基金/ETF 发明印花税；不重开假设-V；不改 V
#   V 的股票印花税切日禁止合成/混读升格进 dk0；诊断桶 vs_V_stock_stamp / stock_cut_20230828_copied_onto_fund_stamp 不得升格进 dk0
# params.cb_stamp_handoff             建议 dc_page
#   消费 DC 的可转债印花税，或显式旁路；可转债印花税 ≠ 基金/ETF 印花税；不改 DC
#   DC 禁止合成/混读升格进 dk0；诊断桶 vs_DC_cb_stamp 不得升格进 dk0
# params.fund_csrc_fee_handoff        建议 dj_page
#   消费 DJ 的场内基金证管费，或显式旁路；基金证管费 ≠ 基金印花税；不改 DJ
#   DJ 禁止合成/混读升格进 dk0；诊断桶 vs_DJ_fund_csrc 不得升格进 dk0
# params.etf_transfer_fee_handoff     建议 da_page
#   消费 DA 的场内基金过户费，或显式旁路；过户费 ≠ 印花税；不改 DA
#   诊断桶 vs_DA_etf_transfer 不得升格进 dk0
# params.fund_handling_fee_handoff    建议 ax_page
#   消费 AX 的基金经手费，或显式旁路；基金经手费 ≠ 基金印花税；不改 AX
#   诊断桶 vs_AX_fund_handling 不得升格进 dk0
# params.block_discount_handoff       建议 di_page
#   消费 DI 的股票大宗经手下浮，或显式旁路；大宗折扣 ≠ 基金印花税；不改 DI
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
# params.cb_handling_fee_handoff      建议 db_page
#   消费 DB 的可转债经手费，或显式旁路；不改 DB
# params.stock_csrc_fee_handoff       建议 t_page
#   消费 T 的股票证管费，或显式旁路；不重开假设-T；不改 T
# params.ashare_fee_handoff           建议 s_page
#   消费 S 的沪深股票竞价经手费切日，或显式旁路；不改 S
# params.bse_limit_aft_handoff        建议 ac_page
#   消费 AC 的北交所涨跌幅与盘后，或显式旁路；不重开假设-AC；不改 AC
# params.stock_transfer_fee_handoff   建议 u_page
# params.cb_rule_handoff              建议 q_page
# params.stock_etf_rotation_handoff   建议 r_page
#   股票 ETF 回转交 R；回转 ≠ 基金印花税；不重开假设-R；不改 R
# params.board_capacity_handoff       建议 a_page
# params.fill_time_suspend_handoff    建议 d_page
#   成交时点与停牌交 D；双字母 DK ≠ 单字母假设-D；不改 D
# params.shortable_list_handoff       建议 k_page
#   融券名单交 K；双字母 DK ≠ 单字母假设-K；不改 K
# params.fund_stamp_handoff           建议 self
# params.dk0_primary_demo             写死冻结 invent_stamp_tax_on_fund
#   单一主报写死，单挂；禁与 invent_asof_leak_fund_stamp 双挂；DK1 不升格；诊断桶不升格
#   半泄露名 invent_asof_leak_fund_stamp 只作对照，不得升格进 dk0，不得双挂
#   诊断桶 bilateral_stamp_on_etf / stock_cut_20230828_copied_onto_fund_stamp / charge_bond_fund_as_stock_stamp / vs_V_stock_stamp / vs_DC_cb_stamp / vs_DJ_fund_csrc / vs_DA_etf_transfer / vs_AX_fund_handling 不得升格进 dk0
#   尤重：禁止把 V 的股票印花税切日与「对基金/ETF 发明印花税」合成/混读后写进 dk0
#   尤重：禁止把 DC 可转债印花税与本页基金/ETF 印花税合成/混读后写进 dk0
#   尤重：禁止把 DJ 基金证管费与本页基金印花税合成/混读后写进 dk0
# params.dk0_invent_stamp_tax_on_fund 建议 True
# params.dk1_asof_leak_fund_stamp_only 建议 True
#   半泄露对照；DK1 不升格并列主报；不得把 invent_asof_leak_fund_stamp 写进 dk0
# params.dk2_pit_fund_out_of_stamp    建议 True
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
# params.merge_with_V                 建议 False
# params.merge_with_T                 建议 False
# params.merge_with_AX                建议 False
# params.merge_with_S                 建议 False
# params.merge_with_AC                建议 False
# params.merge_with_U                 建议 False
# params.merge_with_Q                 建议 False
# params.merge_with_R                 建议 False
# params.merge_with_A                 建议 False
# params.merge_with_D                 建议 False
# params.merge_with_K                 建议 False
# params.missing_sec_type_or_side_policy 建议 skip
# params.day_freq_proxy               建议 fund_stamp_sensitivity
# params.universe_rule                建议 fund_stamp_misapply_check
# params.redline_v0_exempt_scope      建议 position_industry_dk_only
#   既有红线豁免范围名（行业回撤），≠ 实验字母 DK；勿把这个键读成实验 DK
#   不另挂主报，不预留 #121，不写下一字母
```

### 2.2 三组对照（DK0 / DK1 / DK2）

| 组 | 角色 | 口径 |
|----|------|------|
| DK0 | 天真 / 对基金发明印花税 | 按 `dk0_primary_demo` **写死冻结**单一主报 `invent_stamp_tax_on_fund`（单挂写死）：对场内基金/ETF 发明印花税。**禁**与 `invent_asof_leak_fund_stamp` 双挂主报。**禁把 V 股票印花税切日、DC 转债印花税、DJ 基金证管费合成进 `dk0`**（只作对照/旁路，不得升格进 `dk0` 或另挂主报） |
| DK1 | 半泄露 | 仅核对日把「基金/ETF 不在税目内」或现行股票印花税率铺到全历史、铺到基金腿（`invent_asof_leak_fund_stamp`）；**不得升格并列主报**，也不得写进 `dk0`（写死冻结：DK1 不升格），不得双挂 |
| DK2 | 诚实 / 不在税目内 | `fund_stamp_honest=pit_fund_out_of_stamp_tax_scope`（写死冻结）：缺证券类别或买卖方向则 skip；基金/ETF 不在印花税税目内。股票印花税切日只消费 V，转债印花税只消费 DC，基金证管费只消费 DJ，场内基金过户只消费 DA，基金经手费只消费 AX，或显式旁路 |

对 ETF 双边抽印花税、把 2023-08-28 股票切日抄到基金印花税、对债券基金套股票印花税，以及相对 V / DC / DJ / DA / AX 的对照截（`bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling`），放进 §4.1 分桶，**只作诊断桶，不得升格为第二个主报**，也不得改写 `dk0_primary_demo`。`vs_V_stock_stamp` 只标记「有人把 V 的股票印花税切日和本页对基金/ETF 发明印花税合成/混读」这一类失效，**不得升格进 `dk0`**。`vs_DC_cb_stamp` 只标记「有人把 DC 可转债印花税和本页基金/ETF 印花税合成/混读」，**不得升格进 `dk0`**。`vs_DJ_fund_csrc` 只标记「有人把 DJ 基金证管费和本页基金印花税合成/混读」，**不得升格进 `dk0`**。V 的切日、DC 的转债印花税、DJ 的基金证管费、DA 的过户费、AX 的基金经手费只作对照/旁路。

### 2.3 费用窗可落点（写明但不真跑）

主窗建议占位、待预检，起止日仍空着。asof **写死冻结** `2026-10-16`；fill_time **写死冻结** `next_open`；fail **写死冻结** `skip`。诚实锚六键与 Y/G/N/Y2、`dk0_primary_demo` 同属三条，**已写死冻结**。机制红线只有一句：缺证券类别或买卖方向则 skip；基金/ETF 不在印花税税目内。方向随锚写死：**不要把核对日「不在税目内」或 V 的 1‰/0.5‰ 铺满全历史**。`事实与坑` 已写证券交易印花税税目是股票和以股票为基础的存托凭证、只对出让方，并对「ETF/债券基金按股票印花税抽」标过坑；股票切日和 1‰/0.5‰ 留在假设-V，本页不重开。可转债印花税留在 DC，基金证管费留在 DJ，基金经手费留在 AX，场内基金过户留在 DA，都不改。`params.Y` 的 0.02 是无量纲相对门槛，不是印花税率‰。**禁把占位读成 1‰/0.5‰**。缺证券类别或买卖方向则 skip，不用股票档、双边印花税或自造‰把腿填上。本页**不开回测**；不拉真数；不做实盘。

### 2.4 oos_split（建议四日期；拉数前再定；禁 holdout 反调）

建议四日期占位（待预检；禁 holdout 反调 `dk0_primary_demo` / `params.Y`·G·N·Y2 / 税目开关 / 桶 / 是否把 1‰/0.5‰ 铺到基金）。本页不开跑。

---

## 3. 成功 / 失败判据

### 3.1 成功（假设成立方向）

天真组（DK0）/ 半泄露组（DK1）相对诚实组（DK2）的成本差、误抽截**显著且集中在对基金发明印花税的桶**；分桶「对 ETF 双边抽印花税 / 2023-08-28 股票切日抄到基金印花税 / 对债券基金套股票印花税 / 核对日泄露 / vs V·DC·DJ·DA·AX」不改变主结论方向。方向是相对诚实锚偏误。成功不依赖把 1‰/0.5‰ 冻成全历史唯一费率，也不把 `params.Y` 的 0.02 读成印花税率。

### 3.2 失败（假设不成立 / 设计失效）

差异落在噪声带内；或主差被 V 的股票印花税切日、DC 的转债印花税、DJ 的基金证管费、DA 的场内基金过户、AX 的基金经手费、DI 的大宗折扣、DH 的佣金双计、DG 的北交所档、DF 的可交换债经手费、DE 的转债证管费、DD 的转债过户费、DB 的转债经手费、T 的股票证管费、S 的竞价经手费切日、AC 的北交所涨跌幅与盘后、U 的股票过户费、Q 的回转与涨跌幅、R 的股票 ETF 回转、A 的板上容量、D 的成交时点、K 的融券名单解释；或 `dk0_primary_demo` 与 `invent_asof_leak_fund_stamp` 双挂；或 DK1 升格并列主报；或 `bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling` 诊断桶升格主报；或把 V 的股票印花税切日与「对基金/ETF 发明印花税」合成进 `dk0`；或把 DC 可转债印花税合成进 `dk0`；或把 DJ 基金证管费合成进 `dk0`；或实验字母 DK 与单字母 D/K 或 params.Y/G/N 混读；或把 `params.Y` 的 0.02 读成印花税率‰；或把占位读成 1‰/0.5‰；或把核对日「不在税目内」写成已冻并铺满全历史；或缺证券类别 / 买卖方向仍对基金发明印花税；或重开假设-T / 假设-AC / 假设-R / 假设-V。

---

## 4. 检验设计（纸面）

同一信号、同一未复权金额，对照 DK0/DK1/DK2。股票印花税走 V 的诚实切日或显式旁路，不在本页改 V，也不把 V 的切日升成主报。报告成本差、误抽截。不把 1‰/0.5‰ 标成已冻的基金费率，也不把 `params.Y` 的 0.02 读成印花税率。

### 4.1 分桶（须报；`params.diff_buckets` 建议默认名；拉数前再定；禁 holdout 改桶）

建议默认桶名（待预检）：`invent_stamp_tax_on_fund` / `invent_asof_leak_fund_stamp` / `bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling` / `missing_sec_type_or_side_not_skip` / `vs_DI_block_discount` / `vs_DH_commission_double` / `vs_DG_bse_handling` / `vs_DF_exch_handling` / `vs_DE_cb_csrc` / `vs_DD_cb_transfer` / `vs_DB_cb_handling` / `vs_T_stock_csrc` / `vs_S_auction_handling` / `vs_AC_bse_limit_aft` / `vs_U_stock_transfer` / `vs_Q_cb_rule` / `vs_R_stock_etf_rotation` / `vs_A_board_capacity` / `vs_D_fill_time` / `vs_K_shortable_list`

`bilateral_stamp_on_etf`、`stock_cut_20230828_copied_onto_fund_stamp`、`charge_bond_fund_as_stock_stamp`、`vs_V_stock_stamp`、`vs_DC_cb_stamp`、`vs_DJ_fund_csrc`、`vs_DA_etf_transfer`、`vs_AX_fund_handling`、`missing_sec_type_or_side_not_skip` 只作诊断桶：它们不是 `dk0`，也不是 DK1，**不得升格主报**。`vs_V_stock_stamp` 没有对应的「V 切日 + 基金发明印花税」合成主报。V 的股票印花税切日只作诊断，**不得与对基金/ETF 发明印花税合成后升格进 `dk0`**。DC 的可转债印花税只作诊断，**不得升格进 `dk0`**。DJ 的基金证管费只作诊断，**不得升格进 `dk0`**。`invent_asof_leak_fund_stamp` 只服务 DK1，**不得升格进 `dk0`，不得双挂**。`invent_stamp_tax_on_fund` 才是写死冻结的单一主报名。

---

## 5. 预期失效条件（设计失效 / 结论无效）

- 对场内基金/ETF 发明印花税，并拿去当诚实锚。
- 把 `params.Y` 的 0.02 当成印花税率‰。**尤重：`params.Y` 的 0.02 ≠ 印花税率‰**。
- 把占位 `0.02/0.01/0.05/0.015` 读成 1‰/0.5‰。**禁把占位读成 1‰/0.5‰**。
- 缺证券类别或买卖方向仍不 skip，并用股票档、双边印花税或自造‰把腿填上。
- 把核对日「基金/ETF 不在印花税税目内」写成全历史唯一费率，并铺满全历史。方向是核对日不在税目内，不是全历史已冻费率。锚六键已写死冻结。
- 把「股票印花税切日已诚实（V）/ 转债印花税已诚实（DC）/ 基金证管费已诚实（DJ）/ 基金经手费已诚实（AX）/ 场内基金过户已诚实（DA）」写成「场内基金印花税已诚实」。不改 V / DC / DJ / AX / DA。
- 把 V 的股票印花税切日和本页「对基金/ETF 发明印花税」合成或混读后升格进 `dk0`。诊断桶 `vs_V_stock_stamp` / `stock_cut_20230828_copied_onto_fund_stamp` 只作对照。
- 把 DC 可转债印花税和本页基金/ETF 印花税合成或混读后升格进 `dk0`。诊断桶 `vs_DC_cb_stamp` 只作对照。
- 把 DJ 基金证管费和本页基金印花税合成或混读后升格进 `dk0`。诊断桶 `vs_DJ_fund_csrc` 只作对照。
- 对 ETF 双边抽印花税，或对债券基金套股票印花税，并升格进 `dk0`。诊断桶 `bilateral_stamp_on_etf` / `charge_bond_fund_as_stock_stamp` 只作对照。不改 V。
- `dk0_primary_demo` 与 `invent_asof_leak_fund_stamp` 双挂主报；DK1 升格并列主报；诊断桶（`bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling`）升格为第二个主报。
- 实验字母 DK 与单字母 D/K 或 params.Y/G/N 混读。
- 改 DJ / DI / DH / DG / DF / DE / DD / DC / DB / DA / V / T / AX / S / AC / U / Q / R / A / D / K 正文；重开假设-T；重开假设-AC；重开假设-R；重开假设-V；抢 A 真数队列；标纸面齐；写 A/D–DK纸面齐；开真数/回测/实盘；用复权价当费用基数；结论写成「基金印花税更低所以能买」。

---

## 6. 数据需求（字段级；不依赖聚宽真数）

- 标的代码、未复权成交金额、交易日、**证券类别**（股票 / 股票 CDR / ETF / 封闭式 / LOF / 债券基金 / 可转债；仅用于把腿分回 V、DC、DJ、AX、DA 或本页）、**买卖方向**。
- 没有证券类别或买卖方向时，按写死冻结的 `fund_stamp_over_policy=skip_if_sec_type_or_side_missing` skip，不得对基金发明印花税，也不得用核对日「不在税目内」或 1‰/0.5‰ 把腿填满全历史。
- 旁路消费：V 的股票印花税切日、DC 的转债印花税、DJ 的基金证管费、DA 的场内基金过户费、AX 的基金经手费、DI 的大宗折扣、DH 的佣金双计、DG 的北交所经手费、DF 的可交换债经手费、DE 的转债证管费、DD 的转债过户费、DB 的转债经手费、T 的股票证管费、S 的沪深股票竞价经手费切日、AC 的北交所涨跌幅与盘后、U 的股票过户费、Q 的转债规则、R 的股票 ETF 回转、K 的融券名单之诚实结果或显式旁路（见 §2.1 handoff）。**本页不改写这些页。** V 的股票印花税切日、DC 的转债印花税、DJ 的基金证管费不收到本页主报。
- 未复权价；asof **写死冻结** `2026-10-16`。核对日方向「基金/ETF 不在印花税税目内」是写死冻结的机制方向，不是已冻全历史费率。

---

## 7. 回测配置骨架（纸面；本页不开回测）

- **写死键摘要（三条已冻）**：`fill_time=next_open`；`asof_check_date=2026-10-16`；`fail_policy=skip`；`fund_stamp_honest=pit_fund_out_of_stamp_tax_scope`（基金/ETF 不在印花税税目内；**禁止把核对日「不在税目内」或 V 的 1‰/0.5‰ 写成全历史唯一费率**）；`fund_stamp_scope=etf_closed_lof_bond_fund_not_stock_cdr`（ETF / 封闭式 / LOF / 债券基金与股票、股票 CDR 分开）；`fund_stamp_over_policy=skip_if_sec_type_or_side_missing`（缺证券类别或买卖方向则 skip）；`dk0_primary_demo=invent_stamp_tax_on_fund`（**写死冻结**单一主报，单挂；禁与 `invent_asof_leak_fund_stamp` 双挂；DK1 不升格；诊断桶不升格主报；**禁把 V 股票印花税切日、DC 转债印花税、DJ 基金证管费合成进 `dk0`**，只作对照/旁路，不得升格进 `dk0` 或另挂主报）；`stock_stamp_handoff=v_page`；`cb_stamp_handoff=dc_page`；`fund_csrc_fee_handoff=dj_page`；`etf_transfer_fee_handoff=da_page`；`fund_handling_fee_handoff=ax_page`；`merge_with_DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/V/T/AX/S/AC/U/Q/R/A/D/K=False`。
- `params.Y/G/N/Y2` **写死冻结** `0.02/0.01/0.05/0.015`（相对门槛，不是费率表：成本差 / 误抽截 ΔFundStamp / 净收益差 / DK1−DK2；**尤重 params.Y 的 0.02 ≠ 印花税率‰（量纲与语义不同）**；**禁把占位读成 1‰/0.5‰**；**params.Y/G/N ≠ 实验字母 DK ≠ 单字母 D/K**；**勿把 params.Y 读成实验字母 DK，亦勿把单字母假设-D / 假设-K 读成双字母 DK**；禁 null；禁 holdout/OOS 标定；勿改他页已有数值；禁止把这四个数读成印花税率‰）。
- oos_split 四日期建议占位；禁 holdout 反调。不写下一字母。不预留 #121。
- **本页不开回测**；不拉真数；不做实盘；不催 8765。本草稿基 tip=`4cf0270`（A/D–DJ纸面齐已合，全长 `4cf0270398e81949ca65f0cd9ada355bb402f983`）；三冻补丁基 tip=`bb630833` / `bb630833b9e4dee79cb7e1611b00b8dca035ae42`；分支起点 HEAD=`6dd74a57` / `6dd74a57980b93f25c9f1f21f42ea71e664d5a8a`。

---

## 8. 结论

（空；**A/D–DK纸面齐（预检有条件通过·三条已冻）**。）

---

## 风控预检补丁·冻结（三条已写死 · 2026-11-09）

依据风控稿 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设DK-20261109.md`（原样落入，不改结论；SHA256=`097f2657181e2fa32abb685b030d7146590f25791b394ffc1c4768206085fa93`；预检 2026-11-09；**结论：有条件通过**；tip基=`bb630833` / `bb630833b9e4dee79cb7e1611b00b8dca035ae42`；本补丁分支起点 HEAD=`6dd74a57` / `6dd74a57980b93f25c9f1f21f42ea71e664d5a8a`）。按该稿条件 1–3 升格，不标纸面齐。

1. **`params.Y` / `params.G` / `params.N` / `params.Y2`**：**写死冻结** `0.02` / `0.01` / `0.05` / `0.015`。相对门槛用于成本差、误抽截 ΔFundStamp、净收益差、DK1−DK2 专项。**`params.Y` ≠ 实验字母 DK**；**`params.G` ≠ 实验字母 DK**；**`params.N` ≠ 实验字母 DK**；亦 ≠ 单字母假设-D / 假设-K。**勿把 `params.Y` 读成实验字母 DK，亦勿把单字母假设-D / 假设-K 读成双字母 DK**。**尤重：`params.Y` 的 `0.02` ≠ 印花税率‰**（**params.Y 的 0.02 ≠ 印花税率‰**）。二者量纲与语义都不同：`params.Y=0.02` 是无量纲相对门槛，不是印花税率‰，也不是股票印花税 1‰/0.5‰。**禁把占位读成 1‰/0.5‰**。禁止互读、禁止把门槛改写成费率。禁 null 开工；禁 holdout/OOS 标定或跑后因显著性改口；**勿改他字母已冻 Y/G/N/Y2**。

2. **`params.dk0_primary_demo`**：**写死冻结** **`invent_stamp_tax_on_fund`**（单一主报，单挂写死）。**禁止**与 **`invent_asof_leak_fund_stamp`** 双挂争主表；**禁止**跑后因分桶显著性改口主报。DK1 核对日把「基金/ETF 不在税目内」或现行股票印花税率铺到全历史、铺到基金腿只作半泄露对照，**不得升格与 dk0 并列主报**，也不得把 `invent_asof_leak_fund_stamp` 写进 `dk0`。`bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling` / `missing_sec_type_or_side_not_skip` **只作诊断桶，不得升格主报**。DK1 / 诊断桶 **不升格**。**禁把 V 股票印花切日 / DC 转债印花 / DJ 基金证管 合成/混读升格进 `dk0`**：这些只作对照/旁路，**不得升格进 `dk0`，不得另挂主报**。

3. **场内基金印花税诚实锚六键升格写死（不可再写「建议」）**：`params.fund_stamp_honest=pit_fund_out_of_stamp_tax_scope`；`params.fund_stamp_scope=etf_closed_lof_bond_fund_not_stock_cdr`；`params.fund_stamp_over_policy=skip_if_sec_type_or_side_missing`；`params.asof_check_date=2026-10-16`；`params.fill_time=next_open`；`params.fail_policy=skip`。缺证券类型或买卖方向 → skip；基金/ETF 不在印花税税目内。禁止把核对日「不在税目内」或 V 的 1‰/0.5‰ 铺满全历史。禁止跑后改锚，或用股票档 / 核对日现行费率 / 发明‰ / 缺证券类别或买卖方向仍硬抽 / 把 V 股票印花切日、DC 转债印花或 DJ 基金证管升格进 dk0 冒充诚实 PIT。**禁把占位读成 1‰/0.5‰**。

**硬分列保住**：DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠V≠T≠AX≠S≠AC≠U≠Q≠R≠A≠D≠K；**双字母 DK ≠ 单字母假设-D / 假设-K / 假设-V**；**params.Y / params.G / params.N ≠ 实验字母 DK ≠ 单字母 D/K**；**尤重 params.Y 的 0.02 ≠ 印花税率‰**；**禁把占位读成 1‰/0.5‰**；**场内基金印花税误抽 ≠ V股票印花 ≠ DC转债印花 ≠ DJ基金证管 ≠ AX经手 ≠ DA过户**；不抢 A；不改已齐 A–DJ / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI 正文；**不重开假设-T**；**不重开假设-AC**；**不重开假设-R**；**不重开假设-V**；**禁把 V 股票印花切日 / DC 转债印花 / DJ 基金证管 合成/混读升格进 dk0**。

**状态**：**A/D–DK纸面齐（预检有条件通过·三条已冻）**；本页不开回测/真数/实盘。

## 变更

| 日期 | 变更 |
|------|------|
| 2026-11-09 | 复检/纸面齐——**A/D–DK纸面齐（预检有条件通过·三条已冻）**。复检稿 `experiments/backtest/A_limit_up_fill/risk_notes/复检-假设DK-20261109.md` 原样落入，SHA256=`5090c747b66b3c4a04e4af3332e88e699b756412305faa0d0a5f27a016643bdd`；三冻 tip=`1987d4f` / `1987d4f2aab9cac14b8da0d78dbfe6d0377f4c4d`。只改状态标签；未改写已冻三条/六键数值与机制；不改已齐 A–DJ / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI；不改 #110–#119；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-V；禁把 V 股票印花切日 / DC 转债印花 / DJ 基金证管 合成/混读升格进 dk0；不开回测/真数/实盘。 |
| 2026-11-09 | 风控预检补丁·冻结三条写死——依据 `预检-假设DK-20261109.md`（SHA256=`097f2657181e2fa32abb685b030d7146590f25791b394ffc1c4768206085fa93`；结论=有条件通过；tip基=`bb630833` / `bb630833b9e4dee79cb7e1611b00b8dca035ae42`；分支起点 HEAD=`6dd74a57` / `6dd74a57980b93f25c9f1f21f42ea71e664d5a8a`）条件 1–3。① `params.Y/G/N/Y2=0.02/0.01/0.05/0.015`（相对门槛覆盖成本差 / ΔFundStamp / 净收益差 / DK1−DK2；**params.Y/G/N ≠ 实验字母 DK ≠ 单字母 D/K**；**勿把 params.Y 读成实验字母 DK，亦勿把单字母假设-D / 假设-K 读成双字母 DK**；**尤重 params.Y 的 0.02 ≠ 印花税率‰（量纲与语义不同）**；**禁把占位读成 1‰/0.5‰**；禁 null；禁 holdout/OOS 标定；禁止把这四个数读成印花税率‰）；② `params.dk0_primary_demo=invent_stamp_tax_on_fund`（写死冻结单一主报，单挂；禁与 `invent_asof_leak_fund_stamp` 双挂；DK1 不升格；诊断桶 `bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling` 不升格；**禁把 V 股票印花切日 / DC 转债印花 / DJ 基金证管 合成/混读升格进 dk0**，只作对照/旁路，不得升格进 dk0 或另挂主报）；③ 锚六键写死 `fund_stamp_honest=pit_fund_out_of_stamp_tax_scope` / `fund_stamp_scope=etf_closed_lof_bond_fund_not_stock_cdr` / `fund_stamp_over_policy=skip_if_sec_type_or_side_missing` / `asof_check_date=2026-10-16` / `fill_time=next_open` / `fail_policy=skip`（缺证券类型或买卖方向 → skip；基金/ETF 不在印花税税目内；禁止把核对日「不在税目内」或 V 的 1‰/0.5‰ 铺满全历史）。状态=预检有条件通过·三条已冻·待复检；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DK纸面齐**；不改已齐 A–DJ / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-V；不开回测/真数/实盘。基于 tip=`bb630833`。 |
| 2026-11-09 | 新建纸面草稿（**本草稿首次入库**；场内基金印花税误抽；`dk0_primary_demo` 建议 `invent_stamp_tax_on_fund`，单一主报，单挂，禁与 `invent_asof_leak_fund_stamp` 双挂，DK1 不升格；诊断桶 `bilateral_stamp_on_etf` / `stock_cut_20230828_copied_onto_fund_stamp` / `charge_bond_fund_as_stock_stamp` / `vs_V_stock_stamp` / `vs_DC_cb_stamp` / `vs_DJ_fund_csrc` / `vs_DA_etf_transfer` / `vs_AX_fund_handling` 不升格；**尤重 V 的股票印花税切日 ≠ 本页「对基金/ETF 发明印花税」，禁止合成/混读升格进 dk0**；**尤重 DC 可转债印花税 ≠ 本页基金/ETF 印花税，禁止合成进 dk0**；**尤重 DJ 基金证管费 ≠ 本页基金印花税，禁止合成进 dk0**；Y/G/N/Y2 占位 `0.02/0.01/0.05/0.015`，**params.Y/G/N ≠ 实验字母 DK ≠ 单字母 D/K**，且 **params.Y 的 0.02 ≠ 印花税率‰**，**禁把占位读成 1‰/0.5‰**；锚建议 `fund_stamp_honest=pit_fund_out_of_stamp_tax_scope` / scope=`etf_closed_lof_bond_fund_not_stock_cdr` / over_policy=`skip_if_sec_type_or_side_missing`；asof 建议 `2026-10-16`；fill_time 建议 `next_open`；fail 建议 `skip`；口径：缺证券类别或买卖方向则 skip；基金/ETF 不在印花税税目内（**草稿方向，尚未冻，不要写成已冻**）；handoff：`stock_stamp_handoff=v_page`，`cb_stamp_handoff=dc_page`，`fund_csrc_fee_handoff=dj_page`，`etf_transfer_fee_handoff=da_page`，`fund_handling_fee_handoff=ax_page`；`merge_with_DJ/DI/DH/DG/DF/DE/DD/DC/DB/DA/V/T/AX/S/AC/U/Q/R/A/D/K=False`；**DK≠DJ≠DI≠DH≠DG≠DF≠DE≠DD≠DC≠DB≠DA≠V≠T≠AX≠S≠AC≠U≠Q≠R≠A≠D**；**双字母 DK ≠ 单字母假设-D / 假设-K**；**场内基金印花税误抽 ≠ V股票印花 ≠ DC转债印花 ≠ DJ基金证管 ≠ AX经手 ≠ DA过户**；状态=草稿·待入库预检；**三条尚未冻**；**未标纸面齐**；**禁止标纸面齐**；**不写 A/D–DK纸面齐**；不改已齐 A–DJ / 假设-DA / 假设-DB / 假设-DC / 假设-DD / 假设-DE / 假设-DF / 假设-DG / 假设-DH / 假设-DI 及其他已存在假设页；不重开假设-T；不重开假设-AC；不重开假设-R；不重开假设-V；不写下一字母；不预留 #121；不开真数/回测/实盘）。基 tip=`4cf0270`（A/D–DJ纸面齐已合，全长 `4cf0270398e81949ca65f0cd9ada355bb402f983`；不改该 tip 上的 #110–#119，亦不改「可复现实验条目（2026-11-09 · DC / DF）」原文） |
