# 假设 S · 经手费按现行档铺满 / 把 30% 当减半（成本诚信）

更新：2026-11-02  
来源：总管线 / R 草稿已交预检后写下一纸面 S；清单实验 S  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「经手费=0 / 现行 0.0341‰ 铺满 / 2023-08-28 当减半 / 已含代收佣金再加一遍经手费」当实盘成本预期；不抢实验 A 真数队列；本页不开回测；不催 8765；R 预检回来后优先补 R，不改 R 正文）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 S 对齐。与假设 B 类「印花税切片」、过户费（2022-04-29 切片）互补：本页专测**沪深 A 股竞价经手费**——用现行 0.0341‰ 铺满历史、把 2023-08-28 的 30% 当成印花税那种减半、或在已含代收费的佣金上再叠一遍经手费。**证管费（股票 0.02‰ 双边、2023-08-28 不改、ETF/债券免收）属实验 T；股票 ETF 假回转属实验 R；印花税只打卖方属既有费用切片。本页主结论不混。**

---

## 1. 一句话假设（可检验、可证伪）

同一因子、同一持有期、同一 T+1、同一印花税/过户费切片下，用现行 0.0341‰ 回放全历史（或把 2023-08-28 当成减半到 0.02435‰，或在已含代收的佣金上再加一遍经手费），相对「每个交易日用当日已生效经手费档、佣金若已含代收则不再叠加经手费」的 PIT 诚实组，会**系统性改写「成本吃掉的那截」——早年低估、误切日低估、双计则高换手被罚两次**。

证伪方向：若天真组 / 泄露组 / 误切组相对诚实组的成本差、净值差在标定噪声带内可忽略，且「2015-08-01 前 / 2015-08-01～2023-08-27 / 2023-08-28 后 / 高换手」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 经手费 ≠ 佣金；沪深 A 股竞价三切日；30% ≠ 减半；已含代收禁双计（未复权成交金额）

```
# 配置写死 / 待预检键（见 §7）
# params.asof_check_date                 写死默认 2026-10-30  # 事实与坑「经手费≠佣金」核对日；泄露组「现行」锚
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；不抢 A 板上真数
# params.fee_cut_20120901                 写死 2012-09-01     # 0.087‰ → 0.0696‰
# params.fee_cut_20150801                 写死 2015-08-01     # 0.0696‰ → 0.0487‰
# params.fee_cut_20230828                 写死 2023-08-28     # 0.0487‰ → 0.0341‰（降 30%，非减半）
# params.handling_bps_pre_20120901        待预检             # 2012-09-01 前档；未核死则 skip 该窗或拉数前冻结
# params.handling_bps_20120901            写死 0.0696         # 单位：‰（千分之）；双边各收
# params.handling_bps_20150801            写死 0.0487
# params.handling_bps_20230828            写死 0.0341         # 现行核对日档
# params.s2_wrong_half_bps                写死 0.02435        # 误切：把 30% 当减半 → 0.0487×0.5
# params.s0_handling_fee                  写死 0.0            # 天真：经手费=0（或折进不确定佣金不单列）
# params.s1_asof_leak_bps                 写死 0.0341         # 泄露：全样本用核对日现行
# params.s2_treat_30pct_as_half           写死 True           # 误切开关：2023-08-28 起用 s2_wrong_half_bps
# params.s3_pit                           写死 True           # 诚实 PIT
# params.side                             写死 both           # 买卖双边
# params.block_discount_pct               写死 0.30           # 大宗再下浮 30%（竞价主跑可 off）
# params.block_in_main_run                写死 False          # 主跑竞价-only；大宗另桶
# params.commission_includes_agency       待预检             # True=佣金已含代收经手费/证管费 → PIT 不再叠经手费
# params.s3_stack_handling_if_included    写死 False          # 诚实组：已含代收则禁止再加经手费
# params.s0_double_count_demo             写死 True           # 天真可演示「已含仍再加」（暴露双计）
# params.apply_ashare_fee_to_etf          写死 False          # 禁把 A 股 0.0341‰ 套股票 ETF（基金另档）
# params.copy_bse_fee_to_hs               写死 False          # 禁把北交所 0.0125% 抄到沪深
# params.missing_notional_policy          写死 skip           # 缺未复权成交金额 → skip
# params.missing_sec_type_policy          写死 skip           # 缺证券类别却要分 ETF → skip
# params.merge_with_T_csrc_fee            写死 False          # 证管费另页 T
# params.merge_with_R_etf_rotation        写死 False          # ETF 回转另页 R
# params.merge_with_stamp_transfer        写死 False          # 印花税/过户费本页当对照输入，不重开实验
# params.diff_buckets                     写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                   待预检             # 相对门槛；键名稳；值拉数前冻结；禁 holdout 标定
# params.date_start / date_end            写死主窗并冻结
# params.oos_split.*                      写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope          写死 position_industry_dd_only
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改切日·费率档·30%当减半定义·已含代收双计开关·ETF/北交所禁项·Y/G/N/Y2·主窗/oos

fill_time = "next_open"
asof_check_date = "2026-10-30"
fee_cut_20120901 = "2012-09-01"
fee_cut_20150801 = "2015-08-01"
fee_cut_20230828 = "2023-08-28"
handling_bps_20120901 = 0.0696   # ‰
handling_bps_20150801 = 0.0487
handling_bps_20230828 = 0.0341
s2_wrong_half_bps = 0.02435      # 0.0487 * 0.5（误切）
side = "both"
block_discount_pct = 0.30
block_in_main_run = False
apply_ashare_fee_to_etf = False
copy_bse_fee_to_hs = False
s3_stack_handling_if_included = False
merge_with_T_csrc_fee = False
merge_with_R_etf_rotation = False
merge_with_stamp_transfer = False
missing_notional_policy = "skip"
missing_sec_type_policy = "skip"

def pit_handling_bps(d):
    """当日已生效沪深 A 股竞价经手费（‰，单边；双边各收）。"""
    if d >= fee_cut_20230828:
        return handling_bps_20230828
    if d >= fee_cut_20150801:
        return handling_bps_20150801
    if d >= fee_cut_20120901:
        return handling_bps_20120901
    return None  # pre-2012 未核死 → skip 或 params.handling_bps_pre_20120901

def handling_bps_for_group(group, d, commission_includes_agency):
    if group == "S0":
        return s0_handling_fee  # 0；或双计演示见下
    if group == "S1":
        return s1_asof_leak_bps  # 全样本现行 0.0341
    if group == "S2":
        # 误切：切日前仍按 PIT 前档；切日起当减半
        if d >= fee_cut_20230828:
            return s2_wrong_half_bps
        # 切日前可与 PIT 同档，突出「只错在减半」；也可全样本 leak——本页写死：切日前走 PIT
        return pit_handling_bps(d)
    # S3 PIT
    bps = pit_handling_bps(d)
    if bps is None:
        return None
    if commission_includes_agency and (not s3_stack_handling_if_included):
        return 0.0  # 已含代收 → 不再叠经手费
    return bps

def handling_cost(notional, bps, side="both"):
    """notional=未复权成交金额；bps 单位‰。"""
    if bps is None:
        return None  # skip
    mult = 2.0 if side == "both" else 1.0
    return notional * (bps / 1000.0) * mult

def forbid_etf_ashare_fee(sec_type, apply_flag):
    if sec_type in ("etf", "fund") and apply_flag:
        raise ValueError("apply_ashare_fee_to_etf must stay False")
    if sec_type in ("etf", "fund"):
        return "skip_or_exclude"  # 基金另档；本页主跑剔除或记失败

def forbid_copy_bse(copy_flag):
    if copy_flag:
        raise ValueError("copy_bse_fee_to_hs must stay False")
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺未复权成交金额、缺证券类别却要分 ETF、2012-09-01 前费率未冻结却硬跑、把 A 股经手费套 ETF、把北交所费率抄到沪深、把证管费/印花税/ETF 回转混进本页主结论 → **跳过该腿/该日该券**，不静默当 0 成本或现行档。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 四组对照（本实验编码）

| 组 | 经手费 | 2023-08-28 后 | 已含代收佣金时 |
|----|--------|---------------|----------------|
| S0 天真 | =0（或不单列，折进「不确定佣金」） | 仍为 0 | 可演示再叠一遍（双计暴露） |
| S1 泄露 | 全样本用核对日 **0.0341‰** | 0.0341‰ | 仍单列叠经手费（泄露乐观/悲观视佣金设定） |
| S2 误切 | 切日前走 PIT；切日起按**减半 0.02435‰** | **低估** | 同左 |
| S3 PIT | 每交易日用当日已生效档 | **0.0341‰（降 30%）** | **不再叠加经手费** |

同一信号、同一 T+1、**同一印花税（卖方、2023-08-28 前 1‰ / 后 0.5‰）与过户费（2022-04-29 前 0.02‰ / 后 0.01‰ 双边）切片**作对照输入；本页只动经手费层。**`params.fill_time=next_open` 写死**（与 A/D 对齐；不抢 A 板上真数队列）。

**`params.s2_treat_30pct_as_half=True`（写死）**：误切组把 2023-08-28 的 30% 降幅当成印花税那种减半。

**`params.apply_ashare_fee_to_etf=False` / `params.copy_bse_fee_to_hs=False`（写死）**：股票 ETF 不得套 A 股 0.0341‰；北交所 0.0125% 不得抄到沪深。

**`params.merge_with_T_csrc_fee=False` / `params.merge_with_R_etf_rotation=False`（写死）**：证管费、ETF 回转不得混进本页主表。

**待预检冻结键（值可暂「待预检」，键名稳；拉数前必须写入具体值并冻结）**：

```
params.commission_includes_agency = 待预检   # 建议 True（官方：佣金含代收经手费/证管费）；拉数前二选一写死
params.handling_bps_pre_20120901  = 待预检   # 2012-09-01 前；未核则该窗 skip
params.Y                          = 待预检   # 成本差 / 「成本吃掉的那截」门槛
params.G                          = 待预检   # 费率档标签差异率门槛
params.N                          = 待预检   # 失败/跳过率差门槛
params.Y2                         = 待预检   # 高换手桶成本差专项门槛
```

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股竞价成交样本（主跑）；ETF/基金默认剔除或 `skip`（`apply_ashare_fee_to_etf=False`）。  
- **排除（默认）**：缺未复权成交金额；用复权价当成交金额；把北交所费率抄入；把证管费实验 T 并进主表。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2012-09-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖 2015-08-01、2023-08-28 切日；若跑 2012-09-01 前须先冻结 `handling_bps_pre_20120901`。  
- **PIT 切片原则**：经手费档一律按**成交日**当时已生效文本；切日按施行日不按印发日。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2012-09-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调费率档、30%≠减半定义、已含代收双计开关或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **S0 ↔ S3**：天真零经手费（或双计）相对 PIT——「成本吃掉的那截」、净值差、换手×费率敏感。  
2. **S1 ↔ S3**：泄露（现行 0.0341‰ 铺满）相对 PIT——早年成本被低估的那截。  
3. **S2 ↔ S3**：误切（30% 当减半）相对 PIT——2023-08-28 后被低估的那截。  
4. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "pre_20150801",              # 2015-08-01 前（含 2012-09-01 起 0.0696‰ 窗）
  "20150801_to_20230827",      # 0.0487‰ 窗
  "post_20230828",             # 0.0341‰ 窗；误切对照主战场
  "high_turnover",             # 高换手（双计/零费率最敏感）
  "leak_vs_pit_cost",          # 泄露相对 PIT 成本差
  "half_vs_30pct",             # 减半误切 vs 真实 30%
  "double_count_agency",       # 已含代收仍再加经手费
  "vs_T_csrc_fee",             # 与实验 T 分列
  "vs_R_etf_rotation",         # 与实验 R 分列（禁 ETF 套 A 股档）
  "vs_stamp_transfer",         # 与印花税/过户费切片分列
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 成本差 ΔCost（S0/S1/S2 相对 S3；「成本吃掉的那截」）；  
2. 费率档标签差异率 ΔFeeTag；  
3. 高换手桶成本差 ΔCost_HT；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔCost| **≥ Y** 或 |ΔFeeTag| **≥ G** 或 |ΔCost_HT| **≥ Y2** 或 |ΔFail| **≥ N**，记「经手费现行档误铺 / 30% 当减半 / 双计执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 成本差显著门槛 | 键名 `params.Y`；**值待预检**；拉数前写死并冻结 |
| G | 费率档标签差异率门槛 | 键名 `params.G`；**值待预检**；拉数前写死并冻结 |
| N | 失败笔数率差门槛 | 键名 `params.N`；**值待预检**；拉数前写死并冻结 |
| Y2 | 高换手桶成本差门槛 | 键名 `params.Y2`；**值待预检**；拉数前写死并冻结 |
| asof_check_date | 核对日锚点（泄露诊断） | **写死默认** `2026-10-30`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| fee_cut_* | 三切日 | **写死** 2012-09-01 / 2015-08-01 / 2023-08-28 |
| handling_bps_* | 三档费率 | **写死** 0.0696 / 0.0487 / 0.0341（‰） |
| s2_wrong_half_bps | 误切减半档 | **写死** 0.02435 |
| apply_ashare_fee_to_etf | ETF 套 A 股档？ | **写死** `False` |
| copy_bse_fee_to_hs | 北交所抄沪深？ | **写死** `False` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名已稳；**具体数值待风控预检后写入并冻结**；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、切日/费率档、30%≠减半、已含代收双计、`commission_includes_agency`、主窗/`oos_split` 开工拉数前必须保持冻结；**禁止跑后改口**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「经手费按现行档差不多」或「这类票费更低所以能买」。

结论栏：空。跑完只写「该假设下成本差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验经手费 PIT / 误切 / 双计**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权成交金额、PIT 切日、30%≠减半、禁 ETF 套 A 股档、禁北交所抄沪深、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价当成交金额计费**。  
2. **用现行 0.0341‰ 铺满 2015-08-01 前却标 S3 诚实**。  
3. **把 2023-08-28 写成减半（0.02435‰）却标 PIT**（真实是降 30% → 0.0341‰）。  
4. **佣金已含代收经手费仍再加一遍却标诚实**（违反 `s3_stack_handling_if_included=False`）。  
5. **把 A 股 0.0341‰ 套股票 ETF / 基金**（违反 `apply_ashare_fee_to_etf=False`；基金另档）。  
6. **把北交所 0.0125% 抄到沪深**（违反 `copy_bse_fee_to_hs=False`）。  
7. **把证管费（实验 T）或 ETF 回转（实验 R）或印花税/过户费重开实验混进本页主表**。  
8. **宇宙泄露 / holdout 反调**：看完 OOS 再改切日、费率档或显著性门槛。  
9. **把差异写成「这类票/品种费更低所以能买」或选股公式**。  
10. **2012-09-01 前费率未冻结却硬跑并标 PIT**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股 |
| exchange (SSE/SZSE) | 沪深分列 | 北交所默认不进主跑 |
| notional / amount（未复权成交金额） | 计费基数 | **禁复权**；缺 → skip |
| side (buy/sell) | 双边计费 | 经手费买卖都收 |
| sec_type | 股票 / ETF / 债券 | ETF → skip/剔除；禁套 A 股档 |
| turnover 或持仓换手代理 | 高换手分桶 | 可选 |
| commission_includes_agency 标志 | 双计开关 | 策略级配置亦可 |
| 经手费 PIT 表 | 三切日三档 | 本页 §2.1 已锁默认 |
| 印花税/过户费切片（对照输入） | 控制变量 | 不重开实验；按罐内已有切片 |

**明确**：不依赖聚宽；**不要求新开 Level-2 / 新数据商**——日频未复权成交金额 + 证券类别 + 本页经手费规则表即可起步。2012-09-01 前缺档时 **`params.handling_bps_pre_20120901` 待预检冻结或该窗 skip**，不得静默用 0.0696‰ 前推。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗；待预检项标出）：`hypothesis_id=S`，`groups=[S0,S1,S2,S3]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-30`**，**`params.fill_time=next_open`（写死）**，**`params.fee_cut_20120901=2012-09-01`**，**`params.fee_cut_20150801=2015-08-01`**，**`params.fee_cut_20230828=2023-08-28`**，**`params.handling_bps_20120901=0.0696`**，**`params.handling_bps_20150801=0.0487`**，**`params.handling_bps_20230828=0.0341`**，**`params.s2_wrong_half_bps=0.02435`**，**`params.s0_handling_fee=0.0`**，**`params.s1_asof_leak_bps=0.0341`**，**`params.s2_treat_30pct_as_half=True`**，**`params.s3_pit=True`**，**`params.side=both`**，**`params.block_discount_pct=0.30`**，**`params.block_in_main_run=False`**，**`params.s3_stack_handling_if_included=False`**，**`params.s0_double_count_demo=True`**，**`params.apply_ashare_fee_to_etf=False`**，**`params.copy_bse_fee_to_hs=False`**，**`params.commission_includes_agency=待预检`**，**`params.handling_bps_pre_20120901=待预检`**，**`params.missing_notional_policy=skip`**，**`params.missing_sec_type_policy=skip`**，**`params.merge_with_T_csrc_fee=False`**，**`params.merge_with_R_etf_rotation=False`**，**`params.merge_with_stamp_transfer=False`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[pre_20150801,20150801_to_20230827,post_20230828,high_turnover,leak_vs_pit_cost,half_vs_30pct,double_count_agency,vs_T_csrc_fee,vs_R_etf_rotation,vs_stamp_transfer]`（写死默认；拉数前冻结）**，**`params.Y/G/N/Y2=待预检`（键名稳；值拉数前冻结；禁 holdout 标定）**，`universe_rule`，**`params.date_start=2012-09-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2012-09-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_R=off`，`overlay_T=off`，`stamp_transfer_control=on`（印花税/过户费按罐内切片作控制变量）。  
- 行情与费率表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- S0/S1/S2/S3 成本、「成本吃掉的那截」、费率档一致率、失败笔数；分桶（三时段、高换手、泄露差、减半误切、双计、vs T/R/印花税过户费）。  
- 自检布尔：是否未复权金额；S3 是否三切日三档；2023-08-28 是否按 0.0341 而非 0.02435；已含代收是否未双计；是否未套 ETF/北交所；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把零经手费/现行档铺满当实盘成本预期；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 R 正文**；R 预检条件回来后由研究岗优先补 R。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：经手费是交易所标准费率、买卖双边、按日子切片；2023-08-28 降的是 **30%**，不是印花税那种减半；券商佣金官方口径已含代收经手费/证管费，回测若再叠等于罚两次；不能把「佣金因券商而异」写成连经手费也不写。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 S 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A–R 正文**。与实验 T（证管费）分工：S 只动经手费层，T 只动证管费层。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权成交金额 + 证券类别 + 本页经手费三切日表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2012-09-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-30；**fill_time=next_open 写死**；三切日三档写死；**s2_wrong_half_bps=0.02435**；**apply_ashare_fee_to_etf=False**；**copy_bse_fee_to_hs=False**；**s3_stack_handling_if_included=False**；diff_buckets 十桶写死冻结；**Y/G/N/Y2 与 commission_includes_agency / handling_bps_pre_20120901 键名稳、值待预检** |

---

## 变更

- 2026-11-02：新建标准件（总管线：R 已交预检后写 S；选型严格对齐清单实验 S「经手费按现行档铺满 / 把 30% 当减半」；与 T 证管费分列；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 R/A/P/Q 正文**）。