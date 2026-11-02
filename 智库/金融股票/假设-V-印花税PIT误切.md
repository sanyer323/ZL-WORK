# 假设 V · 印花税按现行档铺满 / 双边误抽 / 对 ETF 误抽（成本诚信）

更新：2026-11-02  
来源：总管线 / U 已交预检中并行写下一纸面 V；清单止于 U，选题自 `事实与坑`「印花税只打在卖出，且 2023-08-28 换过费率」+ `口径` 费用分层 + 清单早期实验 B「印花税时点」；**新建实验 V**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「印花税=0 / 现行 0.5‰ 铺满全历史 / 买卖双边计税 / ETF·债券按股票印花税抽」当实盘成本预期；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 U/R/S/T/A 及已交补丁正文**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` 对齐；清单原无 V 节，本页自立实验 V 标准件。与假设 S「经手费现行档误铺」、假设 T「证管费误抽」、假设 U「过户费现行档误铺」**分列**：本页专测**证券交易印花税**——只向**出让方（卖方）**征收、法定 1‰、自 **2023-08-28** 起减半为卖方 0.5‰；税目=转让股票及以股票为基础的存托凭证，**不含 ETF/债券基金**。漏计、用现行 0.5‰ 铺满切日前、买卖双边计税、或对 ETF/债券按股票印花税抽，都会改写高换手成本截。**经手费属实验 S；证管费属实验 T；过户费属实验 U；股票 ETF 假回转属实验 R。本页主结论不混。**

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1、同一经手费（S）/证管费（T）/过户费（U）切片下，把印花税漏成 0、或用现行 0.5‰ 铺满 2023-08-28 之前、或按买卖双边计税、或对 ETF/债券按股票印花税抽，相对「只在卖出计、2023-08-28 前 1‰ / 后 0.5‰、ETF/债券记 0」的 PIT 诚实组，会**系统性改写高换手成本——漏计/现行档误铺/只计半边偏乐观（切日前低估），双边误抽与 ETF·债券误抽偏悲观**。

证伪方向：若天真组 / 误铺组相对诚实组的成本差、净值差在标定噪声带内可忽略，且「2023-08-28 前 / 2023-08-28 后 / 高换手 / ETF 腿 / 双边误抽」分桶不改变结论，则本假设在该样本与税率设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 印花税 ≠ 佣金 ≠ 经手费 ≠ 证管费 ≠ 过户费；只打卖方；2023-08-28 减半；ETF/债券不抽（未复权成交金额）

```
# 配置写死键（见 §7；Y/G/N/Y2 与若干枚举待预检冻结）
# params.asof_check_date                 写死默认 2026-10-02  # 事实与坑「印花税只抽卖出」核对锚（费用层早期条目）；再核见罐内 10-30 分层
# params.fill_time                        写死 next_open      # 成交腿与 A/D/S/T/U 对齐；不抢 A 板上真数
# params.stamp_cut_20230828              写死 2023-08-28     # 财政部税务总局公告 2023 年第 39 号减半生效日
# params.stamp_bps_pre_cut               写死 1.0            # 单位：‰；法定千分之一；只打卖方
# params.stamp_bps_post_cut              写死 0.5            # 减半后卖方实际 0.5‰
# params.v0_stamp_fee                    写死 0.0            # 天真：印花税=0
# params.v1_asof_leak_bps                写死 0.5            # 泄露/误铺：全样本用核对日现行 0.5‰
# params.v1_side                         写死 both           # 误铺可叠加：买卖双边计税（暴露双边坑）
# params.v1_apply_stamp_to_etf           写死 True           # 误铺可叠加：ETF 按股票印花税抽
# params.v1_apply_stamp_to_bond          写死 True           # 同上，债券/债基腿
# params.v2_pit                          写死 True           # 诚实 PIT
# params.v2_side                         写死 sell           # PIT：只打出让方
# params.stamp_bps_etf_pit               写死 0.0            # PIT：税目不含 ETF/基金 → 0（禁静默用股票档）
# params.stamp_bps_bond_pit              写死 0.0            # 同上债券
# params.stamp_bps_dr_as_stock           写死 True           # 以股票为基础的存托凭证按股票税目；本页主宇宙默认 A 股
# params.merge_with_S_handling_fee       写死 False          # 经手费另页 S
# params.merge_with_T_csrc_fee           写死 False          # 证管费另页 T
# params.merge_with_U_transfer_fee       写死 False          # 过户费另页 U
# params.merge_with_R_etf_rotation       写死 False
# params.missing_notional_policy         写死 skip
# params.missing_sec_type_policy         写死 skip
# params.missing_side_policy             写死 skip           # 缺买卖方向却要分卖方税 → skip
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  键名稳值待预检      # 建议占位 0.02/0.01/0.05/0.015；禁 holdout 标定
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 1.0/0.5 档、切日、双边/ETF 误抽开关、Y/G/N/Y2、主窗/oos、v1_primary_demo

fill_time = "next_open"
asof_check_date = "2026-10-02"
stamp_cut_20230828 = "2023-08-28"
stamp_bps_pre_cut = 1.0    # ‰
stamp_bps_post_cut = 0.5
v0_stamp_fee = 0.0
v1_asof_leak_bps = 0.5
v1_side = "both"
v2_side = "sell"
v1_apply_stamp_to_etf = True
v1_apply_stamp_to_bond = True
v2_pit = True
merge_with_S_handling_fee = False
merge_with_T_csrc_fee = False
merge_with_U_transfer_fee = False
merge_with_R_etf_rotation = False
missing_notional_policy = "skip"
missing_sec_type_policy = "skip"
missing_side_policy = "skip"

def pit_stamp_bps(sec_type, d):
    """当日已生效印花税（‰，只打卖方）。股票/股票存托凭证按切日；ETF/债券 → 0。"""
    if sec_type in ("etf", "fund", "bond", "bond_etf"):
        return 0.0  # 税目不含；禁静默用股票档
    if d >= stamp_cut_20230828:
        return stamp_bps_post_cut
    return stamp_bps_pre_cut

def stamp_bps_for_group(group, sec_type, d):
    if group == "V0":
        return v0_stamp_fee
    if group == "V1":
        # 泄露：全样本现行 0.5‰；并可对 ETF/债券按股票档误抽
        if sec_type in ("etf", "fund"):
            return stamp_bps_post_cut if v1_apply_stamp_to_etf else 0.0
        if sec_type in ("bond", "bond_etf"):
            return stamp_bps_post_cut if v1_apply_stamp_to_bond else 0.0
        return v1_asof_leak_bps  # 含切日前低估
    # V2 PIT
    return pit_stamp_bps(sec_type, d)

def stamp_cost(notional, bps, trade_side, group):
    """trade_side: buy|sell。PIT 只对 sell 计；V1 可按 both 误抽。"""
    if bps is None:
        return None  # skip
    side_mode = v1_side if group == "V1" else v2_side
    if group == "V0":
        return 0.0
    if side_mode == "sell" and trade_side != "sell":
        return 0.0
    if side_mode == "buy" and trade_side != "buy":
        return 0.0
    # both：买卖各收一档（误抽）
    return notional * (bps / 1000.0)
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺未复权成交金额、缺买卖方向却要分卖方税、缺证券类别却要分 ETF/债券、把经手费 S / 证管费 T / 过户费 U 混进本页主结论、ETF/债券税目未核却静默用股票 0.5‰ → **跳过该腿/该日该券**，不静默当 0 成本或改档。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 三组对照（本实验编码；自立实验 V）

| 组 | 印花税 | 2023-08-28 前股票卖出 | 2023-08-28 后股票卖出 | 买入腿 | ETF / 债券 |
|----|--------|----------------------|----------------------|--------|------------|
| V0 天真 | =0 | 0 | 0 | 0 | 0（漏计乐观） |
| V1 误铺 | 全样本现行档 | **0.5‰（低估）** | 0.5‰ | **可双边误抽** | **可按股票档误抽** |
| V2 PIT | 按切日+只打卖方 | **1.0‰** | **0.5‰** | **0** | **0**（税目不含） |

同一信号、同一 T+1、**同一经手费（S 层 PIT）、证管费（T 层 PIT）、过户费（U 层 PIT）**作对照输入；本页只动印花税层。**`params.fill_time=next_open` 写死**（与 A/D/S/T/U 对齐；不抢 A 板上真数队列）。

**`params.merge_with_S_handling_fee=False` / `params.merge_with_T_csrc_fee=False` / `params.merge_with_U_transfer_fee=False`（写死）**：经手费、证管费、过户费不得混进本页主表。

**待预检冻结键（草稿占位；拉数前必须写入具体值；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            # 建议 0.02；成本差显著门槛；禁 holdout 标定
params.G                            # 建议 0.01；税率/方向/类别标签差异率门槛
params.N                            # 建议 0.05；失败/跳过率差门槛
params.Y2                           # 建议 0.015；ETF 腿误抽或双边误抽成本差专项门槛
params.v1_primary_demo              # 建议 asof_leak_flat_05（主报现行档误铺）；枚举另有 bilateral_both / etf_wrong_charge / omit_zero；禁双挂
params.v1_side                      # 已写死默认 both（误抽演示）；若预检要求主测只报 asof_leak，可改 sell 并冻结，禁双挂
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股竞价成交样本 + 需分桶的 ETF/债券腿（用于误抽对照；主股票池与 ETF 池分列报告）。  
- **排除（默认）**：缺未复权成交金额；缺买卖方向；用复权价当成交金额；把经手费 S / 证管费 T / 过户费 U 并进主表；北交所主跑（另桶，默认不进）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2020-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖 2023-08-28 减半切日前后；切日前用 1‰、切日后用 0.5‰ 对照主战场。  
- **PIT 切片原则**：印花税一律按**成交日**当时已生效文本；**2023-08-28 是印花税减半日**（与经手费同日降 30% 的 S、证管费不改档的 T、过户费 2022-04-29 降档的 U **分列**——同日≠同机制）。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2020-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 1.0/0.5 档、切日、双边/ETF 误抽开关或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **V0 ↔ V2**：天真零印花税相对 PIT——「漏计乐观」的那截成本、净值差。  
2. **V1 ↔ V2**：现行档误铺（+可选双边/ETF·债券误抽）相对 PIT——切日前被低估的那截 + 双边误抽/ETF 腿被误抽的那截。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "pre_20230828",              # 1‰ 窗；现行 0.5 误铺主战场
  "post_20230828",             # 真实 0.5‰ 窗
  "sell_leg_only",             # PIT 卖方腿
  "buy_leg_wrong_charge",      # V1 双边误抽的买入腿
  "etf_leg_wrong_charge",
  "bond_leg_wrong_charge",
  "high_turnover",
  "leak_omit_vs_pit",          # V0 相对 V2
  "flat_05_vs_pit",            # V1 相对 V2（股票卖出腿）
  "vs_S_handling_fee",
  "vs_T_csrc_fee",
  "vs_U_transfer_fee",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 成本差 ΔCost（V0/V1 相对 V2；「成本吃掉的那截」）；  
2. 税率/方向/类别标签差异率 ΔFeeTag（含「切日前是否仍用 0.5」「买入是否误抽」「ETF 是否误抽」）；  
3. ETF 腿 / 双边误抽成本差 ΔCost_ETF_or_bilateral；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔCost| **≥ Y** 或 |ΔFeeTag| **≥ G** 或 |ΔCost_ETF_or_bilateral| **≥ Y2** 或 |ΔFail| **≥ N**，记「印花税现行档误铺 / 漏计 / 双边或 ETF·债券误抽执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 成本差显著门槛 | **待预检写入**具体数并冻结（建议 0.02） |
| G | 税率/方向/类别标签差异率门槛 | **待预检**（建议 0.01） |
| N | 失败笔数率差门槛 | **待预检**（建议 0.05） |
| Y2 | ETF/双边误抽成本差门槛 | **待预检**（建议 0.015） |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-02`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| stamp_cut_20230828 | 减半日 | **写死** 2023-08-28 |
| stamp_bps_pre_cut / post_cut | 两档 | **写死** 1.0 / 0.5（‰） |
| v2_side | PIT 征收方向 | **写死** `sell` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名已列；**具体数值待风控预检有条件通过后写入并冻结**；**禁止用 holdout / OOS 段标定或反调**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「印花税跟佣金捆着差不多」或「这类品种费更低所以能买」。

结论栏：空。跑完只写「该假设下成本差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验印花税 PIT / 现行档误铺 / 漏计 / 双边与 ETF·债券误抽**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（未复权成交金额、PIT 切日、只打卖方、ETF/债券禁静默股票档、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价当成交金额计税**。  
2. **把 0.5‰ 铺满 2023-08-28 之前却标 V2 诚实**。  
3. **买卖双边计税却标 PIT**（法定只打出让方）。  
4. **对 ETF / 债券基金按股票印花税抽却标 PIT**（税目不含；本页记 0）。  
5. **只计印花税漏掉经手费/证管费/过户费却当「完整成本」报告**（对照输入须在，但不重开 S/T/U）。  
6. **把印花税和佣金/经手费/证管费/过户费捆成一句「费用不确定就不写」**。  
7. **把经手费（S）或证管费（T）或过户费（U）重开实验混进本页主表**。  
8. **把 2023-08-28 经手费降 30% 写成印花税「减半」的同一机制**（S 与 V 分列）。  
9. **宇宙泄露 / holdout 反调**：看完 OOS 再改 1.0/0.5 档或显著性门槛。  
10. **把差异写成「这类品种费更低所以能买」或选股公式**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股 / ETF / 债券分列 |
| exchange (SSE/SZSE) | 沪深分列 | 北交所默认另桶/不进主跑 |
| notional / amount（未复权成交金额） | 计税基数 | **禁复权**；缺 → skip |
| side (buy/sell) | 只打卖方 | 缺 → skip |
| sec_type | 股票 / ETF / 债券 | 误抽与 0 税对照核心 |
| turnover 或持仓换手代理 | 高换手分桶 | 可选 |
| 印花税 PIT 表 | 2023-08-28 前 1‰ / 后 0.5‰；只卖；ETF/债券 0 | 本页 §2.1 已锁 |
| 经手费/证管费/过户费切片（对照输入） | 控制变量 | 不重开；走罐内或 S/T/U |

**明确**：不依赖聚宽；**不要求新开 Level-2 / 新数据商**——日频未复权成交金额 + 买卖方向 + 证券类别 + 本页印花税规则表即可起步。主窗自 2020-01-01。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=V`，`groups=[V0,V1,V2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-02`**，**`params.fill_time=next_open`（写死）**，**`params.stamp_cut_20230828=2023-08-28`**，**`params.stamp_bps_pre_cut=1.0`**，**`params.stamp_bps_post_cut=0.5`**，**`params.v0_stamp_fee=0.0`**，**`params.v1_asof_leak_bps=0.5`**，**`params.v1_side=both`**，**`params.v1_apply_stamp_to_etf=True`**，**`params.v1_apply_stamp_to_bond=True`**，**`params.v2_pit=True`**，**`params.v2_side=sell`**，**`params.stamp_bps_etf_pit=0.0`**，**`params.stamp_bps_bond_pit=0.0`**，**`params.missing_notional_policy=skip`**，**`params.missing_sec_type_policy=skip`**，**`params.missing_side_policy=skip`**，**`params.merge_with_S_handling_fee=False`**，**`params.merge_with_T_csrc_fee=False`**，**`params.merge_with_U_transfer_fee=False`**，**`params.merge_with_R_etf_rotation=False`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y/G/N/Y2`（待预检写入具体数并冻结；禁 holdout 标定；禁 null）**，**`params.v1_primary_demo`（待预检；禁双挂）**，`universe_rule`，**`params.date_start=2020-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2020-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_S=off`，`overlay_T=off`，`overlay_U=off`，`overlay_R=off`，`S_T_U_control=on`（经手费/证管费/过户费按罐内或 S/T/U 切片作控制变量）。  
- 行情与税率表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- V0/V1/V2 成本、「成本吃掉的那截」、税率/方向/类别一致率、ETF/双边误抽、失败笔数；分桶（时段、买卖腿、ETF/债券误抽、高换手、漏计、误铺、vs S/T/U）。  
- 自检布尔：是否未复权金额；V2 切日前是否 1‰、切日后是否 0.5‰、买入是否 0；ETF/债券是否未静默用股票档；是否未与 S/T/U 混表；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把零印花税/现行档误铺当实盘成本预期；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 U/R/S/T/A 已冻结正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：印花税只向出让方征收；法定 1‰，自 **2023-08-28** 起减半为卖方 0.5‰；税目不含 ETF/债券基金；不能和「佣金因券商而异」捆成一句不写；不能与经手费（S）、证管费（T）、过户费（U）混层。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 U，本页**新增实验 V** 收成标准件，**不改口径主线**，**不改假设 A–U 正文**。与实验 S/T/U 分工：**S 只动经手费，T 只动证管费，U 只动过户费，V 只动印花税**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权成交金额 + 买卖方向 + 证券类别 + 本页印花税规则表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2020-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-02；**fill_time=next_open 写死**；**两档 1.0/0.5‰ + 切日 2023-08-28 + v2_side=sell 写死**；diff_buckets 十二桶写死冻结；**Y/G/N/Y2·v1_primary_demo 待预检** |

---

## 变更

- 2026-11-02：新建标准件（总管线：U 已交预检中并行写 V；清单止于 U → 自 `事实与坑` 印花税坑选题，**与 A–U 不撞**；近邻 S=经手费、T=证管费、U=过户费，本页只动卖方印花税层；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 U/R/S/T/A 正文**）。