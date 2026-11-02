# 假设 T · 证管费跟着 2023-08-28 改 / 对 ETF 误抽（成本诚信）

更新：2026-11-02  
来源：总管线 / S 草稿已交后并行写下一纸面 T；清单实验 T  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「证管费=0 / 2023-08-28 改档或免收 / ETF·债券按股票 0.02‰ 抽」当实盘成本预期；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 R/S/A/P/Q 正文**；**风控补丁四条已冻结 2026-11-02**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 T 对齐。与假设 S「经手费现行档误铺 / 30% 当减半」**分列**：本页专测**证券交易监管费（证管费）**——股票 0.02‰ 双边自 2012-01-01、**2023-08-28 不改档**、基金/ETF/债券免收；严禁把证管费写成和印花税/经手费同一天改档，或对股票 ETF 按股票费率误抽。**经手费三切日三档属实验 S；股票 ETF 假回转属实验 R；印花税只打卖方属既有费用切片。本页主结论不混。**

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1、同一印花税/过户费/经手费（S 层）切片下，把证管费写成和 2023-08-28 经手费/印花税同日改档（改 0.01‰ 或免收），或对 ETF/债券按股票 0.02‰ 抽，相对「股票 0.02‰ 双边且 2023-08-28 不改、ETF/债券记 0」的 PIT 诚实组，会**系统性改写高换手与 ETF 对冲腿的成本——误切偏乐观、ETF 误抽偏悲观；漏掉证管费则与「只写印花税+过户费」一样偏乐观**。

证伪方向：若天真组 / 误切组相对诚实组的成本差、净值差在标定噪声带内可忽略，且「2012-01-01 前窗 / 2012-01-01～2023-08-27 / 2023-08-28 后 / ETF 腿 / 高换手」分桶不改变结论，则本假设在该样本与费率设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 证管费 ≠ 经手费 ≠ 印花税；2012-01-01 起股票 0.02‰ 双边；2023-08-28 不改；ETF/债券免收（未复权成交金额）

```
# 配置写死键（见 §7；风控补丁四条已冻结 2026-11-02）
# params.asof_check_date                 写死默认 2026-10-30  # 事实与坑「证管费切片」核对日；与 S 同周五复盘锚
# params.fill_time                        写死 next_open      # 成交腿与 A/D/S 对齐；不抢 A 板上真数
# params.csrc_fee_start                   写死 2012-01-01     # 投资者侧本页默认档起点（发改价格〔2012〕2119 号执行日）
# params.fee_cut_20230828                 写死 2023-08-28     # 经手费/印花税切日；证管费**不改**（对照锚，非本页降档日）
# params.csrc_fee_bps_stock               写死 0.02           # 单位：‰；股票双边各收
# params.csrc_fee_bps_etf                 写死 0.0            # 基金/ETF 免收
# params.csrc_fee_bps_bond                写死 0.0            # 债券免收
# params.csrc_fee_bps_pre_20120101        写死（窗外置）      # 主窗自 2012-01-01；见 params.pre_20120101_window
# params.pre_20120101_window             写死 skip_or_out_of_scope  # 主窗不含 2012 前；禁未冻结静默用 0.02 前推标 T2
# params.t0_csrc_fee                      写死 0.0            # 天真：证管费=0（只留印花税+过户费）
# params.t1_wrong_post_cut_bps            写死 0.01           # 误切主测「误改档=当减半」；禁双挂 0.0；禁跑后改口
# params.t1_apply_stock_fee_to_etf        写死 True           # 误切：ETF/债券按股票 0.02‰ 抽
# params.t1_apply_stock_fee_to_bond       写死 True           # 同上，债券腿
# params.t2_pit                           写死 True           # 诚实 PIT
# params.t2_unchanged_on_20230828         写死 True           # 硬约束：切日后仍 0.02‰
# params.side                             写死 both           # 买卖双边
# params.commission_includes_agency       写死 True           # 佣金已含代收经手费/证管费 → T2 不再叠；与 S 同向；禁缺键静默双计/漏计
# params.t2_stack_csrc_if_included        写死 False          # 诚实组：已含代收则禁止再加证管费
# params.t0_double_count_demo             写死 False          # 本页天真主路径=漏计；双计演示留给 S（经手费）
# params.merge_with_S_handling_fee        写死 False          # 经手费另页 S；本页只动证管费层
# params.merge_with_R_etf_rotation        写死 False          # ETF 回转另页 R
# params.merge_with_stamp_transfer        写死 False          # 印花税/过户费本页当对照输入，不重开实验
# params.missing_notional_policy          写死 skip
# params.missing_sec_type_policy          写死 skip           # 缺证券类别却要分 ETF/债券 → skip
# params.diff_buckets                     写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                   写死 0.02/0.01/0.05/0.015  # 相对门槛；禁 holdout 标定；禁 null
# params.date_start / date_end            写死主窗并冻结
# params.oos_split.*                      写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope          写死 position_industry_dd_only
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 0.02‰ 档、2023-08-28 不改约束、ETF/债券免收、误切错档值、已含代收双计开关、Y/G/N/Y2、主窗/oos、pre_20120101_window

fill_time = "next_open"
asof_check_date = "2026-10-30"
csrc_fee_start = "2012-01-01"
fee_cut_20230828 = "2023-08-28"   # 对照锚；证管费不改
csrc_fee_bps_stock = 0.02         # ‰
csrc_fee_bps_etf = 0.0
csrc_fee_bps_bond = 0.0
side = "both"
t2_unchanged_on_20230828 = True
t1_apply_stock_fee_to_etf = True
t1_apply_stock_fee_to_bond = True
t2_stack_csrc_if_included = False
merge_with_S_handling_fee = False
merge_with_R_etf_rotation = False
merge_with_stamp_transfer = False
missing_notional_policy = "skip"
missing_sec_type_policy = "skip"

def pit_csrc_bps(sec_type, d):
    """当日已生效证管费（‰，单边；双边各收）。股票 0.02；ETF/债券 0；切日不改。"""
    if d < csrc_fee_start:
        return None  # pre-2012 未核死 → skip 或 params.csrc_fee_bps_pre_20120101
    if sec_type in ("etf", "fund"):
        return csrc_fee_bps_etf
    if sec_type in ("bond", "bond_etf"):
        return csrc_fee_bps_bond
    # stock / preferred 等 A 股主类
    return csrc_fee_bps_stock  # 含 d >= fee_cut_20230828；不改档

def csrc_bps_for_group(group, sec_type, d, commission_includes_agency, t1_wrong_post_cut_bps):
    if group == "T0":
        return t0_csrc_fee  # 0
    if group == "T1":
        # 误切：2023-08-28 起改错档；且 ETF/债券按股票抽
        if sec_type in ("etf", "fund", "bond", "bond_etf"):
            if t1_apply_stock_fee_to_etf or t1_apply_stock_fee_to_bond:
                base = csrc_fee_bps_stock  # 误抽
            else:
                base = 0.0
        else:
            base = csrc_fee_bps_stock
        if d >= fee_cut_20230828:
            return t1_wrong_post_cut_bps  # 写死 0.01；禁双挂 0.0
        return base
    # T2 PIT
    bps = pit_csrc_bps(sec_type, d)
    if bps is None:
        return None
    if commission_includes_agency and (not t2_stack_csrc_if_included):
        return 0.0  # 已含代收 → 不再叠证管费
    return bps

def csrc_cost(notional, bps, side="both"):
    """notional=未复权成交金额；bps 单位‰。"""
    if bps is None:
        return None  # skip
    mult = 2.0 if side == "both" else 1.0
    return notional * (bps / 1000.0) * mult

def assert_t2_unchanged(d, bps):
    if t2_unchanged_on_20230828 and d >= fee_cut_20230828 and bps not in (0.0, csrc_fee_bps_stock):
        raise ValueError("T2 must keep stock 0.02‰ (or 0 for ETF/bond) on/after 2023-08-28")
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺未复权成交金额、缺证券类别却要分 ETF/债券、2012-01-01 前费率未冻结却硬跑、把经手费实验 S / ETF 回转实验 R / 印花税过户费重开混进本页主结论、把发改委「对交易所按年交易额收取」理解成日频可忽略而静默置 0 → **跳过该腿/该日该券**，不静默当 0 成本或改档。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 三组对照（本实验编码；对齐清单实验 T）

| 组 | 证管费 | 2023-08-28 后股票 | ETF / 债券 |
|----|--------|-------------------|------------|
| T0 天真 | =0（只留印花税+过户费） | 仍为 0 | 0（漏计乐观） |
| T1 误切 | 切日前可走股票 0.02‰；切日起按**错档** | **`t1_wrong_post_cut_bps=0.01`（写死；禁双挂 0.0）** | **按股票 0.02‰ 误抽** |
| T2 PIT | 股票 **0.02‰ 双边** | **仍 0.02‰（不改）** | **记 0**；已含代收则不再叠 |

同一信号、同一 T+1、**同一印花税（卖方、2023-08-28 前 1‰ / 后 0.5‰）、过户费（2022-04-29 前 0.02‰ / 后 0.01‰ 双边）、经手费（S 层 PIT 或罐内已冻结切片）**作对照输入；本页只动证管费层。**`params.fill_time=next_open` 写死**（与 A/D/S 对齐；不抢 A 板上真数队列）。

**`params.t2_unchanged_on_20230828=True`（写死）**：诚实组切日后股票仍 0.02‰，禁止写成减半或免收。

**`params.t1_apply_stock_fee_to_etf=True` / `params.t1_apply_stock_fee_to_bond=True`（写死）**：误切组对 ETF/债券按股票费率抽。

**`params.merge_with_S_handling_fee=False` / `params.merge_with_R_etf_rotation=False`（写死）**：经手费、ETF 回转不得混进本页主表。

**风控补丁四条已冻结（2026-11-02；拉数前冻结；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                # 成本差显著门槛 ≥ 2pp（同系列纸面占位；来源 L/M/N/O/P/R/S；禁 holdout 标定）
params.G                            = 0.01                # 费率/类别标签差异率门槛 ≥ 1pp
params.N                            = 0.05                # 失败/跳过率差门槛 ≥ 5pp
params.Y2                           = 0.015               # ETF 腿误抽成本差专项门槛 ≥ 1.5pp
params.t1_wrong_post_cut_bps        = 0.01                # 误切主测「误改档=当减半」；禁双挂 0.0（误免收）；禁跑后因切日后成本差改口
params.pre_20120101_window          = skip_or_out_of_scope  # 主窗自 2012-01-01；2012 前窗外置；禁未冻结静默用 0.02 前推标 T2；若前推样本须另写 csrc_fee_bps_pre_20120101 ‰ 并冻结
params.commission_includes_agency   = True                # 佣金已含代收经手费/证管费；与 t2_stack_csrc_if_included=False 同向 → T2 不再叠；与 S 同向；禁缺键静默双计/漏计；禁跑后改口
```

**`params.Y` / `params.G` / `params.N` / `params.Y2`（写死；拉数前冻结）**：`0.02` / `0.01` / `0.05` / `0.015`。预检禁 holdout 标定且未给推荐数 → 与同系列 L/M/N/O/P/R/S 纸面占位一致。单位：Y=abs(ΔCost) 成本差；G=abs(ΔFeeTag) 费率/类别标签差异率；N=abs(ΔFail) 失败/跳过率差；Y2=abs(ΔCost_ETF) ETF 腿误抽成本差。**禁止** null 开工；**禁止**用 holdout/OOS 标定或跑后因显著性改口。

**`params.t1_wrong_post_cut_bps`（写死；拉数前冻结；禁双挂）**：`0.01`。主测「误改档」（把 2023-08-28 当成减半错档）；误切组切日后股票腿一律用该错档。枚举另有 `0.0`（误免收），本页不选。**禁止** 0.01 与 0.0 双挂争主表；**禁止**跑后因切日后成本差改口。

**`params.pre_20120101_window`（写死；拉数前冻结）**：`skip_or_out_of_scope`。主窗 `date_start=2012-01-01` 不含 2012 前，该窗外置；`params.csrc_fee_bps_pre_20120101` 本页不写入具体‰。若前推样本，须另写具体‰并冻结。**禁止**未冻结时静默用 `0.02` 前推却标 T2 PIT。

**`params.commission_includes_agency`（写死；拉数前冻结）**：`True`。官方口径佣金常含代收经手费/证管费；与 `t2_stack_csrc_if_included=False` 同向时 T2 不再叠证管费；与假设 S 同向。**禁止**缺键时实现静默双计或静默漏计；**禁止**跑后因成本差改口。

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股竞价成交样本 + 需分桶的 ETF/债券腿（用于误抽对照；主股票池与 ETF 池分列报告）。  
- **排除（默认）**：缺未复权成交金额；用复权价当成交金额；把经手费实验 S 并进主表；把「年交易额口径」当成日频可忽略。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2012-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖 2012-01-01 档起点与 2023-08-28 对照切日；**`params.pre_20120101_window=skip_or_out_of_scope`（写死）**；若前推样本须另写 `csrc_fee_bps_pre_20120101` ‰ 并冻结。  
- **PIT 切片原则**：证管费档一律按**成交日**当时已生效文本；**2023-08-28 对证管费不是降档日**（仅作误切对照锚）。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2012-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调 0.02‰ 档、2023-08-28 不改约束、ETF/债券免收、误切错档值或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **T0 ↔ T2**：天真零证管费相对 PIT——「漏计乐观」的那截成本、净值差。  
2. **T1 ↔ T2**：误切（切日改档 + ETF/债券按股票抽）相对 PIT——股票腿切日后被低估的那截 + ETF 腿被误抽的那截。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "pre_20120101",              # 窗外置；params.pre_20120101_window=skip_or_out_of_scope
  "20120101_to_20230827",      # 股票 0.02‰ 稳定窗
  "post_20230828",             # 误切对照主战场（真实不改 vs 错档）
  "etf_leg_wrong_charge",      # ETF 按股票抽的那截
  "bond_leg_wrong_charge",     # 债券按股票抽的那截
  "high_turnover",             # 高换手（漏计/误切最敏感）
  "leak_omit_vs_pit",          # T0 相对 T2 成本差
  "wrong_cut_vs_pit",          # T1 相对 T2（股票腿）
  "vs_S_handling_fee",         # 与实验 S 分列
  "vs_R_etf_rotation",         # 与实验 R 分列
  "vs_stamp_transfer",         # 与印花税/过户费切片分列
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 成本差 ΔCost（T0/T1 相对 T2；「成本吃掉的那截」）；  
2. 费率/类别标签差异率 ΔFeeTag（含「切日后是否改档」「ETF 是否免收」）；  
3. ETF 腿误抽成本差 ΔCost_ETF；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔCost| **≥ Y** 或 |ΔFeeTag| **≥ G** 或 |ΔCost_ETF| **≥ Y2** 或 |ΔFail| **≥ N**，记「证管费误改档 / ETF·债券误抽执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 成本差显著门槛 | **写死** `params.Y=0.02` 并冻结 |
| G | 费率/类别标签差异率门槛 | **写死** `params.G=0.01` 并冻结 |
| N | 失败笔数率差门槛 | **写死** `params.N=0.05` 并冻结 |
| Y2 | ETF 腿误抽成本差门槛 | **写死** `params.Y2=0.015` 并冻结 |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-30`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| csrc_fee_start | 本页默认档起点 | **写死** 2012-01-01 |
| csrc_fee_bps_stock | 股票档 | **写死** 0.02（‰） |
| t2_unchanged_on_20230828 | 切日不改 | **写死** `True` |
| t1_apply_stock_fee_to_etf | ETF 误抽？ | **写死** `True`（仅 T1） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名与具体数值已按预检有条件通过冻结；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、`t1_wrong_post_cut_bps`、`pre_20120101_window`、`commission_includes_agency`、主窗/`oos_split` 开工拉数前必须保持冻结；**禁止跑后改口**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「证管费跟着经手费改差不多」或「这类品种费更低所以能买」。

结论栏：空。跑完只写「该假设下成本差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验证管费 PIT / 误切 / ETF·债券误抽**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权成交金额、PIT 不改档、ETF/债券免收、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价当成交金额计费**。  
2. **把 2023-08-28 写成证管费降档日却标 T2 诚实**（真实：股票仍 0.02‰）。  
3. **对 ETF / 债券按股票 0.02‰ 抽却标 PIT**（2012 通知免收基金和债券；深交所 2026-01 表只把 0.02‰ 写在 A 股/B 股/优先股）。  
4. **佣金已含代收证管费仍再加一遍却标诚实**（违反 `t2_stack_csrc_if_included=False`）。  
5. **把发改委「对交易所按年交易额收取」理解成日频回测可忽略**而静默置 0。  
6. **用券商帮助页当切日**，不用核对日交易所收费表 / 官方通知。  
7. **把经手费（实验 S）或 ETF 回转（实验 R）或印花税/过户费重开实验混进本页主表**。  
8. **宇宙泄露 / holdout 反调**：看完 OOS 再改 0.02‰ 档、误切错档值或显著性门槛。  
9. **把差异写成「这类品种费更低所以能买」或选股公式**。  
10. **2012-01-01 前费率未冻结却硬跑并标 PIT**（本页 `pre_20120101_window=skip_or_out_of_scope`，不得静默用 0.02‰ 前推）。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | A 股 / ETF / 债券分列 |
| exchange (SSE/SZSE) | 沪深分列 | 北交所默认不进主跑 |
| notional / amount（未复权成交金额） | 计费基数 | **禁复权**；缺 → skip |
| side (buy/sell) | 双边计费 | 证管费买卖都收 |
| sec_type | 股票 / ETF / 债券 | 误抽与免收对照核心 |
| turnover 或持仓换手代理 | 高换手分桶 | 可选 |
| commission_includes_agency 标志 | 双计开关 | 策略级配置亦可；建议与 S 同向 |
| 证管费 PIT 表 | 2012-01-01 起 0.02‰；切日不改；ETF/债券 0 | 本页 §2.1 已锁默认 |
| 印花税/过户费/经手费切片（对照输入） | 控制变量 | 不重开实验；经手费走 S 或罐内已有切片 |

**明确**：不依赖聚宽；**不要求新开 Level-2 / 新数据商**——日频未复权成交金额 + 证券类别 + 本页证管费规则表即可起步。主窗自 2012-01-01；**`params.pre_20120101_window=skip_or_out_of_scope`（写死冻结）**，不得静默用 0.02‰ 前推标 T2。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=T`，`groups=[T0,T1,T2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-30`**，**`params.fill_time=next_open`（写死）**，**`params.csrc_fee_start=2012-01-01`**，**`params.fee_cut_20230828=2023-08-28`（对照锚）**，**`params.csrc_fee_bps_stock=0.02`**，**`params.csrc_fee_bps_etf=0.0`**，**`params.csrc_fee_bps_bond=0.0`**，**`params.t0_csrc_fee=0.0`**，**`params.t1_wrong_post_cut_bps=0.01`（写死冻结；禁双挂 0.0）**，**`params.t1_apply_stock_fee_to_etf=True`**，**`params.t1_apply_stock_fee_to_bond=True`**，**`params.t2_pit=True`**，**`params.t2_unchanged_on_20230828=True`**，**`params.side=both`**，**`params.t2_stack_csrc_if_included=False`**，**`params.t0_double_count_demo=False`**，**`params.commission_includes_agency=True`（写死冻结；与 S 同向）**，**`params.pre_20120101_window=skip_or_out_of_scope`（写死冻结；不写 `csrc_fee_bps_pre_20120101` ‰）**，**`params.missing_notional_policy=skip`**，**`params.missing_sec_type_policy=skip`**，**`params.merge_with_S_handling_fee=False`**，**`params.merge_with_R_etf_rotation=False`**，**`params.merge_with_stamp_transfer=False`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[pre_20120101,20120101_to_20230827,post_20230828,etf_leg_wrong_charge,bond_leg_wrong_charge,high_turnover,leak_omit_vs_pit,wrong_cut_vs_pit,vs_S_handling_fee,vs_R_etf_rotation,vs_stamp_transfer]`（写死默认；拉数前冻结）**，**`params.Y=0.02` / `params.G=0.01` / `params.N=0.05` / `params.Y2=0.015`（写死具体数并冻结；禁 holdout 标定；禁 null）**，`universe_rule`，**`params.date_start=2012-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2012-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_S=off`，`overlay_R=off`，`stamp_transfer_handling_control=on`（印花税/过户费/经手费按罐内或 S 切片作控制变量）。  
- 行情与费率表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- T0/T1/T2 成本、「成本吃掉的那截」、费率/类别一致率、ETF 腿误抽、失败笔数；分桶（时段、ETF/债券误抽、高换手、漏计、误切、vs S/R/印花税过户费）。  
- 自检布尔：是否未复权金额；T2 是否 2023-08-28 后仍 0.02‰；ETF/债券是否为 0；T1 是否同时错档+误抽；是否未与 S 经手费混表；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把零证管费/误改档当实盘成本预期；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 R/S/A/P/Q 正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：证管费是证监会监管费、交易所代收；股票 0.02‰ 双边自 2012-01-01；**2023-08-28 没改**；基金和债券免收；不能和经手费/印花税捆成一句改档。券商佣金官方口径已含代收经手费/证管费，回测若再叠等于罚两次。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 T 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A–S 正文**。与实验 S（经手费）分工：**S 只动经手费层，T 只动证管费层**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权成交金额 + 证券类别 + 本页证管费规则表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2012-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-30；**fill_time=next_open 写死**；**csrc_fee_bps_stock=0.02**；**t2_unchanged_on_20230828=True**；**ETF/债券免收写死**；**t1 误抽开关写死**；diff_buckets 十一桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死冻结**；**t1_wrong_post_cut_bps=0.01 写死（禁双挂）**；**pre_20120101_window=skip_or_out_of_scope 写死**；**commission_includes_agency=True 写死（与 S 同向）** |

---

## 变更

- 2026-11-02：新建标准件（总管线：并行写 T=证管费误抽；选型严格对齐清单实验 T「证管费跟着 2023-08-28 改 / 对 ETF 误抽」；与 S 经手费分列；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 R/S/A/P/Q 正文**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设T-20261102.md` 有条件通过补四条——① `params.Y=0.02` / `G=0.01` / `N=0.05` / `Y2=0.015` 写入具体数并冻结（预检禁 holdout 标定且未给推荐数；与同系列 L/M/N/O/P/R/S 纸面占位一致；禁 null）；② `params.t1_wrong_post_cut_bps=0.01`（主测误改档=当减半；禁双挂 0.0）；③ `params.pre_20120101_window=skip_or_out_of_scope`（主窗不含 2012 前，不写 `csrc_fee_bps_pre_20120101` ‰）；④ `params.commission_includes_agency=True`（与 S 同向）。**不抢实验 A**；**T 不开回测**；未动 S/R/A。
