# 假设 U · 过户费按现行档铺满 / 漏计双边 / 对 ETF 误抽（成本诚信）

更新：2026-11-02  
来源：总管线 / R·S·T 补丁链暂齐后写下一纸面 U；清单止于 T，选题自 `事实与坑`「过户费买卖都收，且 2022-04-29 换过费率」+ `口径` 费用分层；**新建实验 U**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「过户费=0 / 现行 0.01‰ 铺满全历史 / ETF·债券按股票过户费抽」当实盘成本预期；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 R/S/T/A 及已交补丁正文**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` 对齐；清单原无 U 节，本页自立实验 U 标准件。与假设 S「经手费现行档误铺」、假设 T「证管费误抽」、印花税卖方切片**分列**：本页专测**中国结算股票交易过户费**——买卖双边、2015-08-01 起沪深 A 股 0.02‰、**2022-04-29** 起下调为 0.01‰；漏计、用现行档铺满切日前、或对 ETF/债券按股票档误抽，都会改写成本截。**经手费三切日属实验 S；证管费 0.02‰/切日不改属实验 T；股票 ETF 假回转属实验 R。本页主结论不混。**

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1、同一印花税/经手费（S）/证管费（T）切片下，把过户费漏成 0、或用现行 0.01‰ 铺满 2022-04-29 之前、或对 ETF/债券按股票过户费抽，相对「每个成交日用当日已生效过户费档（2015-08-01～2022-04-28：0.02‰ 双边；2022-04-29 起：0.01‰ 双边）、ETF/债券不按股票档硬抽」的 PIT 诚实组，会**系统性改写高换手成本——漏计/现行档误铺偏乐观（切日前低估），ETF·债券误抽偏悲观**。

证伪方向：若天真组 / 误铺组相对诚实组的成本差、净值差在标定噪声带内可忽略，且「2015-08-01 前窗 / 2015-08-01～2022-04-28 / 2022-04-29 后 / 高换手 / ETF 腿」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 过户费 ≠ 佣金 ≠ 经手费 ≠ 证管费；2015-08-01 / 2022-04-29 切片；买卖双边（未复权成交金额）

```
# 配置写死键（见 §7；风控补丁五条已冻结 2026-11-02）
# params.asof_check_date                 写死默认 2026-10-02  # 事实与坑「过户费」核对日；费用分层再核见 2026-10-30
# params.fill_time                        写死 next_open      # 成交腿与 A/D/S/T 对齐；不抢 A 板上真数
# params.transfer_unify_start            写死 2015-08-01     # 沪深 A 股过户费统一 0.02‰ 双边起点
# params.transfer_cut_20220429           写死 2022-04-29     # 0.02‰ → 0.01‰（下调 50%）
# params.transfer_bps_20150801           写死 0.02           # 单位：‰；买卖双边各收
# params.transfer_bps_20220429           写死 0.01           # 现行核对日档
# params.transfer_bps_pre_20150801       写死（窗外置）      # 主窗自 2015-08-01；见 params.pre_20150801_window；不写具体‰
# params.pre_20150801_window             写死 skip_or_out_of_scope  # 主窗不含 2015-08-01 前；禁未冻结静默用 0.02 前推标 U2
# params.u0_transfer_fee                 写死 0.0            # 天真：过户费=0（只留印花税+佣金等）
# params.u1_asof_leak_bps                写死 0.01           # 泄露/误铺：全样本用核对日现行 0.01‰
# params.u1_apply_stock_fee_to_etf       写死 True           # 误铺可叠加：ETF 按股票档抽（暴露误抽）
# params.u1_apply_stock_fee_to_bond      写死 True           # 同上，债券腿
# params.u2_pit                          写死 True           # 诚实 PIT
# params.side                            写死 both           # 买卖双边
# params.transfer_bps_etf_pit            写死 None→skip      # PIT：ETF/基金另表未核死 → skip，禁静默用股票档
# params.transfer_bps_bond_pit           写死 None→skip      # 同上债券
# params.missing_etf_transfer_schedule   写死 skip           # 缺 ETF 过户费表 → skip 该腿
# params.broker_bundles_transfer_fee     写死 False          # 过户费属中国结算；与「佣金含经手费/证管费」不同层；禁缺键静默双计/漏计
# params.u2_stack_if_bundled             写死 False          # 若券商报价已代收过户费且开关 True，诚实组不再叠；默认按未捆处理
# params.merge_with_S_handling_fee       写死 False          # 经手费另页 S
# params.merge_with_T_csrc_fee           写死 False          # 证管费另页 T
# params.merge_with_stamp                写死 False          # 印花税本页当对照输入，不重开
# params.merge_with_R_etf_rotation       写死 False
# params.missing_notional_policy         写死 skip
# params.missing_sec_type_policy         写死 skip
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死 0.02/0.01/0.05/0.015  # 相对门槛；禁 holdout 标定；禁 null
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only
# params.u1_primary_demo                 写死 asof_leak_flat_001  # 主报现行档误铺；禁双挂 omit_zero / etf_wrong_charge
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 0.02/0.01 档、切日、ETF 误抽开关、Y/G/N/Y2、主窗/oos、pre_20150801_window、broker_bundles_transfer_fee、u1_primary_demo

fill_time = "next_open"
asof_check_date = "2026-10-02"
transfer_unify_start = "2015-08-01"
transfer_cut_20220429 = "2022-04-29"
transfer_bps_20150801 = 0.02   # ‰
transfer_bps_20220429 = 0.01
side = "both"
u0_transfer_fee = 0.0
u1_asof_leak_bps = 0.01
u1_apply_stock_fee_to_etf = True
u1_apply_stock_fee_to_bond = True
u2_pit = True
merge_with_S_handling_fee = False
merge_with_T_csrc_fee = False
merge_with_stamp = False
merge_with_R_etf_rotation = False
missing_notional_policy = "skip"
missing_sec_type_policy = "skip"
missing_etf_transfer_schedule = "skip"
Y = 0.02
G = 0.01
N = 0.05
Y2 = 0.015
pre_20150801_window = "skip_or_out_of_scope"  # 不写 transfer_bps_pre_20150801 ‰
broker_bundles_transfer_fee = False
u1_primary_demo = "asof_leak_flat_001"  # 禁双挂 omit_zero / etf_wrong_charge

def pit_transfer_bps(sec_type, d):
    """当日已生效过户费（‰，单边；双边各收）。股票按切日；ETF/债券未核死 → None(skip)。"""
    if sec_type in ("etf", "fund", "bond", "bond_etf"):
        return None  # 品种另表；禁静默用股票档
    if d < transfer_unify_start:
        return None  # pre-2015-08-01 → params.pre_20150801_window
    if d >= transfer_cut_20220429:
        return transfer_bps_20220429
    return transfer_bps_20150801

def transfer_bps_for_group(group, sec_type, d):
    if group == "U0":
        return u0_transfer_fee
    if group == "U1":
        # 泄露：全样本现行 0.01‰；并可对 ETF/债券按股票档误抽
        if sec_type in ("etf", "fund"):
            return transfer_bps_20220429 if u1_apply_stock_fee_to_etf else 0.0
        if sec_type in ("bond", "bond_etf"):
            return transfer_bps_20220429 if u1_apply_stock_fee_to_bond else 0.0
        return u1_asof_leak_bps  # 含切日前低估
    # U2 PIT
    return pit_transfer_bps(sec_type, d)

def transfer_cost(notional, bps, side="both"):
    if bps is None:
        return None  # skip
    mult = 2.0 if side == "both" else 1.0
    return notional * (bps / 1000.0) * mult
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺未复权成交金额、缺证券类别却要分 ETF/债券、2015-08-01 前窗外置（`pre_20150801_window=skip_or_out_of_scope`）却硬跑、把经手费 S / 证管费 T / 印花税重开混进本页主结论、ETF/债券过户费表未核却静默用股票 0.01‰ → **跳过该腿/该日该券**，不静默当 0 成本或改档。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 三组对照（本实验编码；自立实验 U）

| 组 | 过户费 | 2022-04-29 前股票 | 2022-04-29 后股票 | ETF / 债券 |
|----|--------|-------------------|-------------------|------------|
| U0 天真 | =0 | 0 | 0 | 0（漏计乐观） |
| U1 误铺 | 全样本现行档 | **0.01‰（低估）** | 0.01‰ | **可按股票档误抽** |
| U2 PIT | 按切日 | **0.02‰** | **0.01‰** | **未核死 → skip**（禁静默股票档） |

同一信号、同一 T+1、**同一印花税（卖方、2023-08-28 前 1‰ / 后 0.5‰）、经手费（S 层 PIT）、证管费（T 层 PIT）**作对照输入；本页只动过户费层。**`params.fill_time=next_open` 写死**（与 A/D/S/T 对齐；不抢 A 板上真数队列）。

**`params.merge_with_S_handling_fee=False` / `params.merge_with_T_csrc_fee=False` / `params.merge_with_stamp=False`（写死）**：经手费、证管费、印花税不得混进本页主表。

**风控补丁五条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                # 成本差显著门槛 ≥ 2pp（同系列纸面占位；来源 L/M/N/O/P/R/S/T；禁 holdout 标定）
params.G                            = 0.01                # 费率/类别标签差异率门槛 ≥ 1pp
params.N                            = 0.05                # 失败/跳过率差门槛 ≥ 5pp
params.Y2                           = 0.015               # ETF 腿误抽成本差专项门槛 ≥ 1.5pp
params.pre_20150801_window          = skip_or_out_of_scope  # 主窗自 2015-08-01；2015-08-01 前窗外置；禁未冻结静默用 0.02 前推标 U2
params.transfer_bps_pre_20150801    = （窗外置·不依赖）      # 与 pre_20150801_window=skip_or_out_of_scope 对称；不写具体‰；若前推样本须另写‰并冻结
params.broker_bundles_transfer_fee  = False               # 过户费=中国结算，与「佣金含经手费/证管费」不同层；与 u2_stack_if_bundled=False 同向；禁缺键静默双计/漏计
params.u1_primary_demo              = asof_leak_flat_001  # 主报现行档误铺/asof 泄漏；枚举另有 omit_zero / etf_wrong_charge；禁双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股竞价成交样本 + 需分桶的 ETF/债券腿（用于误抽对照；主股票池与 ETF 池分列报告）。  
- **排除（默认）**：缺未复权成交金额；用复权价当成交金额；把经手费 S / 证管费 T 并进主表；北交所主跑（切日数字可另桶，默认不进）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2015-08-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖统一 0.02‰ 起点与 2022-04-29 切日；**`params.pre_20150801_window=skip_or_out_of_scope`（写死冻结）**；不依赖 `transfer_bps_pre_20150801` ‰。  
- **PIT 切片原则**：过户费档一律按**成交日**当时已生效文本；**2022-04-29 是过户费降档日**（与印花税 2023-08-28、经手费三切日、证管费不改档分列）。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2015-08-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 0.02/0.01 档、切日、ETF 误抽开关或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **U0 ↔ U2**：天真零过户费相对 PIT——「漏计乐观」的那截成本、净值差。  
2. **U1 ↔ U2**：现行档误铺（+可选 ETF/债券误抽）相对 PIT——切日前被低估的那截 + ETF 腿被误抽的那截。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "pre_20150801",              # 窗外置；pre_20150801_window=skip_or_out_of_scope
  "20150801_to_20220428",      # 0.02‰ 窗；误铺主战场（现行 0.01 低估）
  "post_20220429",             # 真实 0.01‰ 窗
  "etf_leg_wrong_charge",      # ETF 按股票抽的那截
  "bond_leg_wrong_charge",
  "high_turnover",
  "leak_omit_vs_pit",          # U0 相对 U2
  "flat_001_vs_pit",           # U1 相对 U2（股票腿）
  "vs_S_handling_fee",
  "vs_T_csrc_fee",
  "vs_stamp",
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 成本差 ΔCost（U0/U1 相对 U2；「成本吃掉的那截」）；  
2. 费率/类别标签差异率 ΔFeeTag（含「切日前是否仍用 0.01」「ETF 是否误抽」）；  
3. ETF 腿误抽成本差 ΔCost_ETF；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔCost| **≥ Y** 或 |ΔFeeTag| **≥ G** 或 |ΔCost_ETF| **≥ Y2** 或 |ΔFail| **≥ N**，记「过户费现行档误铺 / 漏计 / ETF·债券误抽执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 成本差显著门槛 | **写死冻结** `0.02` |
| G | 费率/类别标签差异率门槛 | **写死冻结** `0.01` |
| N | 失败笔数率差门槛 | **写死冻结** `0.05` |
| Y2 | ETF 腿误抽成本差门槛 | **写死冻结** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-02`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| transfer_unify_start | 统一档起点 | **写死** 2015-08-01 |
| transfer_cut_20220429 | 降档日 | **写死** 2022-04-29 |
| transfer_bps_20150801 / 20220429 | 两档 | **写死** 0.02 / 0.01（‰） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与数值已写死冻结（风控补丁 2026-11-02）；**禁止用 holdout / OOS 段标定或反调**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「过户费跟佣金捆着差不多」或「这类品种费更低所以能买」。

结论栏：空。跑完只写「该假设下成本差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验过户费 PIT / 现行档误铺 / 漏计 / ETF·债券误抽**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（未复权成交金额、PIT 切日、ETF/债券禁静默股票档、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价当成交金额计费**。  
2. **把 0.01‰ 铺满 2022-04-29 之前却标 U2 诚实**。  
3. **对 ETF / 债券按股票过户费抽却标 PIT**（品种另表；本页未核死精确档 → skip）。  
4. **只计印花税漏掉过户费却当「完整成本」报告**。  
5. **把过户费和佣金/经手费/证管费捆成一句「费用不确定就不写」**。  
6. **把经手费（S）或证管费（T）或印花税重开实验混进本页主表**。  
7. **宇宙泄露 / holdout 反调**：看完 OOS 再改 0.02/0.01 档或显著性门槛。  
8. **把差异写成「这类品种费更低所以能买」或选股公式**。  
9. **2015-08-01 前费率未冻结却硬跑并标 PIT**（本页 `pre_20150801_window=skip_or_out_of_scope`，不得静默用 0.02‰ 前推）。  
10. **把北交所/股转旧档 0.025‰ 与沪深合成一句却不另桶**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股 / ETF / 债券分列 |
| exchange (SSE/SZSE) | 沪深分列 | 北交所默认另桶/不进主跑 |
| notional / amount（未复权成交金额） | 计费基数 | **禁复权**；缺 → skip |
| side (buy/sell) | 双边计费 | 过户费买卖都收 |
| sec_type | 股票 / ETF / 债券 | 误抽与 skip 对照核心 |
| turnover 或持仓换手代理 | 高换手分桶 | 可选 |
| 过户费 PIT 表 | 2015-08-01:0.02‰；2022-04-29:0.01‰；ETF/债券另表或 skip | 本页 §2.1 已锁股票默认 |
| 印花税/经手费/证管费切片（对照输入） | 控制变量 | 不重开；走罐内或 S/T |

**明确**：不依赖聚宽；**不要求新开 Level-2 / 新数据商**——日频未复权成交金额 + 证券类别 + 本页过户费规则表即可起步。主窗自 2015-08-01；**`params.pre_20150801_window=skip_or_out_of_scope`（写死冻结）**，不得静默用 0.02‰ 前推标 U2；不依赖 `transfer_bps_pre_20150801` ‰。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=U`，`groups=[U0,U1,U2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-02`**，**`params.fill_time=next_open`（写死）**，**`params.transfer_unify_start=2015-08-01`**，**`params.transfer_cut_20220429=2022-04-29`**，**`params.transfer_bps_20150801=0.02`**，**`params.transfer_bps_20220429=0.01`**，**`params.u0_transfer_fee=0.0`**，**`params.u1_asof_leak_bps=0.01`**，**`params.u1_apply_stock_fee_to_etf=True`**，**`params.u1_apply_stock_fee_to_bond=True`**，**`params.u2_pit=True`**，**`params.side=both`**，**`params.missing_etf_transfer_schedule=skip`**，**`params.missing_notional_policy=skip`**，**`params.missing_sec_type_policy=skip`**，**`params.merge_with_S_handling_fee=False`**，**`params.merge_with_T_csrc_fee=False`**，**`params.merge_with_stamp=False`**，**`params.merge_with_R_etf_rotation=False`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y=0.02` / `params.G=0.01` / `params.N=0.05` / `params.Y2=0.015`（写死具体数并冻结；禁 holdout 标定；禁 null）**，**`params.pre_20150801_window=skip_or_out_of_scope`（写死冻结；不写 `transfer_bps_pre_20150801` ‰）**，**`params.broker_bundles_transfer_fee=False`（写死冻结）**，**`params.u1_primary_demo=asof_leak_flat_001`（写死冻结；禁双挂）**，`universe_rule`，**`params.date_start=2015-08-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2015-08-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_S=off`，`overlay_T=off`，`overlay_R=off`，`stamp_S_T_control=on`（印花税/经手费/证管费按罐内或 S/T 切片作控制变量）。  
- 行情与费率表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- U0/U1/U2 成本、「成本吃掉的那截」、费率/类别一致率、ETF 腿误抽、失败笔数；分桶（时段、ETF/债券误抽、高换手、漏计、误铺、vs S/T/印花税）。  
- 自检布尔：是否未复权金额；U2 切日前是否 0.02‰、切日后是否 0.01‰；ETF/债券是否未静默用股票档；是否未与 S/T 混表；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把零过户费/现行档误铺当实盘成本预期；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 R/S/T/A 已冻结正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：过户费是中国结算标准费率、买卖双边；2015-08-01 起沪深 A 股 0.02‰，**2022-04-29** 起 0.01‰；不能和「佣金因券商而异」捆成一句不写；不能与经手费（S）、证管费（T）、印花税（卖方）混层。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 T，本页**新增实验 U** 收成标准件，**不改口径主线**，**不改假设 A–T 正文**。与实验 S/T 分工：**S 只动经手费，T 只动证管费，U 只动过户费**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权成交金额 + 证券类别 + 本页过户费规则表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2015-08-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-02；**fill_time=next_open 写死**；**两档 0.02/0.01‰ + 切日 2022-04-29 写死**；diff_buckets 十一桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死冻结**；**pre_20150801_window=skip_or_out_of_scope 写死**；**transfer_bps_pre_20150801 窗外置不依赖**；**broker_bundles_transfer_fee=False 写死**；**u1_primary_demo=asof_leak_flat_001 写死（禁双挂）** |

---

## 变更

- 2026-11-02：新建标准件（总管线：R/S/T 补丁链暂齐后写 U；清单止于 T → 自 `事实与坑` 过户费坑选题，**与 A–T 不撞**；近邻 S=经手费、T=证管费，本页只动中国结算过户费层；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 R/S/T/A 正文**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设U-20261102.md` 有条件通过补五条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写入具体数并冻结（预检禁 holdout 标定且建议 0.02/0.01/0.05/0.015；与同系列 R/S/T 纸面占位一致；禁 null）；② `params.pre_20150801_window=skip_or_out_of_scope`；③ `params.transfer_bps_pre_20150801` 窗外置不依赖（与 S/T 对称；主窗不含 2015-08-01 前，不写具体‰）；④ `params.broker_bundles_transfer_fee=False`；⑤ `params.u1_primary_demo=asof_leak_flat_001`（主报现行档误铺/asof 泄漏；禁双挂 omit_zero / etf_wrong_charge）。**不抢实验 A**；**U 不开回测**；未动 V/R/S/T/A。
