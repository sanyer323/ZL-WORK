# 假设 Q · 可转债按股票规则回放（规则混用 / 执行鸿沟）

更新：2026-11-02（风控补丁）  
来源：总管线 / P 草稿已收后继续写 Q；清单实验 Q  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「转债当股票 / 假 T+1 / 假转股 T+0」当实盘预期；不抢实验 A 真数队列；本页不开回测；P 不开回测）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 Q 对齐。与假设 A（涨停可成交）、F/G（涨跌停取整与 PIT）、N（收盘机制）、M/O（盘后通道分列）互补：本页专测**可转债规则混用**——把转债推进股票池，用股票 T+1、板块默认涨跌停、股票收盘价定义回放；再把转股所得股票当成当日可卖（发明正股 T+0）。**ETF 回转属实验 R；深市转债盘后定价 vs 股票盘后固定价格混表属通道标注禁项，不并进本页主结论。**

---

## 1. 一句话假设（可检验、可证伪）

同一信号与持有期下，把可转债按股票规则回放（T+1 + 主板 ±10%/创业科创 ±20% + 沪市股票 14:57 集合收盘），相对「当日回转 + 2022-08-01 后次日 ±20% + 沪/深首日分列 + 转股所得股票次日才可卖」的 PIT 诚实组，会**系统性压低可交易次数、标错板、用错收盘价**；再把转股腿当日可卖，会把正股 T+0 吹进收益。

证伪方向：若天真组 / 泄露组相对诚实组的换手差、板标签差异、假 T+1 / 假转股 T+0 贡献在标定噪声带内可忽略，且「2022-08-01 前 / 沪市首日 / 深市首日」分桶不改变结论，则本假设在该样本与撮合设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 可转债 ≠ 股票；回转；板；收盘；转股腿（未复权）

```
# 配置写死（见 §7）
# params.asof_check_date                 写死默认 2026-10-26  # 清单可转债核对日锚；泄露组诊断用，主结论禁只靠泄露
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；收盘定义差异另做 close_px_source 诊断
# params.cb_rotation                      写死 same_day       # 可转债当日回转（T+0）；禁 stock_t1 进诚实组
# params.cb_limit_cut_date                写死 2022-08-01     # 此前无次日 ±20% 板；之后次日 ±20%
# params.cb_limit_pct_post_cut            写死 0.20
# params.sh_first_day_up_pct              写死 0.573          # 沪市首日涨幅板 57.3%
# params.sh_first_day_dn_pct              写死 0.433          # 沪市首日跌幅板 43.3%
# params.sh_first_day_close_def           写死 last_min_vwap  # 沪市首日收盘=最后一分钟加权；禁 14:57 集合
# params.sz_first_day_board               写死 none           # 深市首日无 20% 板
# params.sz_first_day_order_range_up      写死 1.573          # 有效申报上限相对发行价 157.3%
# params.sz_first_day_order_range_dn      写死 0.567          # 有效申报下限相对发行价 56.7%
# params.sz_first_day_close_def           写死 auction_1457   # 深市首日收盘先走 14:57 集合
# params.copy_sh_first_day_to_sz          写死 False          # 禁把沪市首日板抄到深市
# params.q0_treat_as_stock                写死 True           # 天真：转债当股票
# params.q0_rotation                      写死 stock_t1
# params.q0_limit_source                  写死 stock_board_default  # ±10%/创业科创±20%
# params.q0_close_def                     写死 stock_1457_auction
# params.q0_convert_stock_same_day_sell   写死 True           # 天真：转股所得当日可卖（假正股 T+0）
# params.q1_asof_leak_rules               写死 True           # 泄露：全样本用核对日现行转债规则
# params.q2_pit                           写死 True           # 诚实 PIT
# params.q2_convert_stock_same_day_sell   写死 False          # 转股所得股票次日才可卖
# params.q1_convert_stock_same_day_sell   写死 False          # Q1转股所得次日可卖；与§2.3表同向；禁缺键静默继承q0/q2
# params.q1_rotation                      写死 same_day       # Q1现行转债回转；禁缺键误套stock_t1
# params.missing_last_min_vwap_policy     写死 skip_first_day_close_leg  # 无last_min_vwap→skip首日收盘腿；禁静默auction_1457标Q2
# params.cb_face_value                    写死 100            # 可转债面值（元）
# params.cb_lot_size                      写死 10             # 可转债一手=10张
# params.q0_unit_source                   写死 stock_share_lot # 天真组用股票100股一手混用；暴露执行鸿沟
# params.merge_sz_cb_aft_with_stock_aft   写死 False          # 禁与股票盘后固定价格合成一张表却不标注
# params.missing_exch_policy              写死 skip           # 缺沪/深标记 → skip
# params.missing_ipo_flag_policy          写死 skip           # 缺上市首日标记 → skip 首日腿
# params.diff_buckets                     写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                   写死具体数并冻结；禁 holdout 标定
# params.date_start / date_end            写死主窗并冻结
# params.oos_split.*                      写死四日期并冻结；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 fill_time·回转·板切日·首日沪深分列·转股可卖日·q1_convert_stock_same_day_sell·q1_rotation·missing_last_min_vwap_policy·cb_face_value·cb_lot_size·q0_unit_source·Y/G/N/Y2·主窗/oos

tick = 0.01  # A 股可转债价格最小变动默认；基金 0.001 不进本页
fill_time = "next_open"
asof_check_date = "2026-10-26"
cb_limit_cut_date = "2022-08-01"
cb_limit_pct_post_cut = 0.20
sh_first_day_up_pct = 0.573
sh_first_day_dn_pct = 0.433
sh_first_day_close_def = "last_min_vwap"
sz_first_day_board = "none"
sz_first_day_order_range_up = 1.573
sz_first_day_order_range_dn = 0.567
sz_first_day_close_def = "auction_1457"
copy_sh_first_day_to_sz = False
merge_sz_cb_aft_with_stock_aft = False

def is_post_limit_cut(d):
    return d >= cb_limit_cut_date

def stock_like_limit_pct(board):
    # 天真组：股票板块默认
    if board in ("chinext", "star"):
        return 0.20
    return 0.10  # 主板等

def cb_pit_limit_pct(d, is_first_day, exch):
    if is_first_day:
        if exch == "SSE":
            return ("board", sh_first_day_up_pct, sh_first_day_dn_pct)
        if exch == "SZSE":
            # 深市首日无板；有效申报范围相对发行价
            return ("order_range", sz_first_day_order_range_up, sz_first_day_order_range_dn)
        return None  # missing → skip
    if not is_post_limit_cut(d):
        return ("no_20pct_board", None, None)  # 2022-08-01 前不套 ±20%
    return ("board", cb_limit_pct_post_cut, cb_limit_pct_post_cut)

def close_px_source(group, d, is_first_day, exch, official_close, last_min_vwap, auction_1457_px):
    # params.missing_last_min_vwap_policy=skip_first_day_close_leg（写死）：无 last_min_vwap → skip 首日收盘腿
    if group == "Q0":
        return auction_1457_px if auction_1457_px is not None else official_close
    if group == "Q1":
        # 泄露：按核对日现行细则（含沪市首日 last_min_vwap / 深市首日 14:57）
        if is_first_day and exch == "SSE":
            if last_min_vwap is None:
                return None  # skip_first_day_close_leg；禁 fallback official_close / auction_1457 标诚实源
            return last_min_vwap
        if is_first_day and exch == "SZSE":
            return auction_1457_px if auction_1457_px is not None else official_close
        return official_close
    # Q2 PIT
    if is_first_day and exch == "SSE":
        if last_min_vwap is None:
            return None  # skip_first_day_close_leg
        return last_min_vwap
    if is_first_day and exch == "SZSE":
        return auction_1457_px if auction_1457_px is not None else official_close
    return official_close

def rotation_allows_same_day_sell(group, instrument_kind):
    # params.q1_rotation=same_day；params.q1_convert_stock_same_day_sell=False；params.q0_unit_source=stock_share_lot
    if instrument_kind == "cb":
        if group == "Q0":
            return False  # q0_rotation=stock_t1 → T+1，压低可交易次数
        # Q1: q1_rotation=same_day；Q2: cb_rotation=same_day
        return True
    if instrument_kind == "stock_from_convert":
        if group == "Q0":
            return True   # q0_convert_stock_same_day_sell=True（假正股 T+0）
        # Q1: q1_convert_stock_same_day_sell=False；Q2: q2_convert_stock_same_day_sell=False
        return False
    return False

def forbid_copy_sh_first_day_to_sz(exch, using_sh_first_day_board):
    if copy_sh_first_day_to_sz:
        raise ValueError("copy_sh_first_day_to_sz must stay False")
    if exch == "SZSE" and using_sh_first_day_board:
        raise ValueError("SH first-day board must not apply to SZSE")
```

- **天真（Q0）**：可转债当股票——`stock_t1` + 板块默认涨跌停 + 股票 14:57 集合收盘；转股所得股票当日可卖（假正股 T+0）。  
- **泄露（Q1）**：全样本用核对日（`asof_check_date`）现行可转债规则（含 ±20% 与沪市首日板）；不按 2022-08-01 前真实无板切片。  
- **诚实 PIT（Q2）**：当日回转；2022-08-01 前不套 ±20%；之后次日 ±20%；沪市首日 57.3%/43.3% + 最后一分钟加权收盘；深市首日无 20% 板、用 157.3%/56.7% 有效申报范围 + 14:57 集合收盘；转股所得股票**次日**才可卖。  
- **禁止**：用复权价；把沪市首日板抄到深市；把深市可转债盘后定价与股票盘后固定价格合成一张表却不标注通道；结论写成「这类转债能买」。

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺交易所（沪/深）、缺上市首日标记却要做首日腿、缺发行价却要算深市首日申报范围、把沪市首日板抄到深市、把深市转债盘后与股票盘后混表却标本页主结论 → **跳过该腿/该日该券**，不静默当股票规则。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 三组对照（本实验编码）

| 组 | 回转 | 涨跌停 / 申报范围 | 收盘价定义 | 转股所得股票 |
|----|------|-------------------|------------|--------------|
| Q0 天真 | 当股票 T+1 | 板块默认 ±10%/±20% | 股票 14:57 集合 | 当日可卖（假 T+0） |
| Q1 泄露 | 现行转债回转 | 全样本用核对日现行（含 ±20%+沪市首日板） | 按现行细则 | 次日可卖 |
| Q2 PIT | 当日回转 | 2022-08-01 前无 ±20%；之后 ±20%；沪/深首日分列 | 沪首日 last_min_vwap；深首日 14:57 | **次日**可卖 |

同一信号、同一成本开关（本页可先零成本只比换手 / 板标签 / 假 T+1·假转股 T+0 贡献）。**`params.fill_time=next_open` 写死**（与 A/D 对齐；不抢 A 板上真数队列）。

**`params.copy_sh_first_day_to_sz=False`（写死）**：深市首日不得套用 57.3%/43.3% 板。

**`params.merge_sz_cb_aft_with_stock_aft=False`（写死）**：深市转债盘后定价与股票盘后固定价格必须分列标注；混表不得进本页主结论。

**`params.q1_convert_stock_same_day_sell`（写死；拉数前冻结）**：`False`。与 §2.3 表「Q1 转股所得次日可卖」同向；**禁止**缺键时由实现静默继承 `q0_convert_stock_same_day_sell` / `q2_convert_stock_same_day_sell`；**禁止**跑后因假转股 T+0 贡献改口。枚举另有 `True`（本页不选）。

**`params.q1_rotation`（写死；拉数前冻结）**：`same_day`。与现行转债回转 / 全局 `cb_rotation=same_day` 同向；**禁止**缺键时误套 `stock_t1` 或与 Q0 缠死事后改口。

**`params.missing_last_min_vwap_policy`（写死；拉数前冻结；禁双挂）**：`skip_first_day_close_leg`。与 §6「无 last_min_vwap 字段时沪市首日收盘诊断 skip」同向；**禁止**无字段时静默用 `auction_1457` 标 Q2；**禁止**双挂 `fallback_official_close_tagged`。枚举另有 `fallback_official_close_tagged`（须打 mech/来源标签且禁止把 fallback 当成 `last_min_vwap` 诚实源），本页不用。

**`params.cb_face_value` / `params.cb_lot_size` / `params.q0_unit_source`（写死；拉数前冻结）**：`cb_face_value=100`（元）、`cb_lot_size=10`（张/手）、`q0_unit_source=stock_share_lot`（天真组用股票 100 股一手规则混用，暴露执行鸿沟）。枚举另有 `cb_native_lot`（Q0 仍用转债张），本页不选。**禁止**跑后因手数/面值换算改口；**禁止**把基金 0.001 tick 混进本页主结论（`tick=0.01` 仍写死）。

---

## 3. 样本区间

- **宇宙（默认）**：样本内出现的可转债（沪/深）；正股仅作转股腿对照，不扩成全 A 选债。  
- **排除（默认）**：缺未复权匹配成交 OHLC；缺交易所；把复权价当撮合；把沪市首日板抄到深市却声称 PIT。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖 2022-08-01 切日前后；稳健分桶见 `params.diff_buckets`。  
- **PIT 切片原则**：回转、板/申报范围、收盘定义、转股可卖日，一律按成交日/转股申报日当时规则。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调回转定义、板切日、首日沪深分列、转股可卖日或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **Q0 − Q2**：天真「转债当股票 + 假转股 T+0」相对 PIT 诚实——换手差、板标签差异、收盘价源差异、假 T+1 / 假转股 T+0 贡献、失败/跳过笔数差。  
2. **Q1 − Q2**：泄露（全样本现行规则）相对 PIT——看 2022-08-01 前被 ±20% / 首日板「吹胖或压错」的那截。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "pre_20220801",            # 2022-08-01 前（无次日 ±20% 板）
  "post_20220801",           # 2022-08-01 后次日 ±20%
  "sh_first_day",            # 沪市上市首日（57.3%/43.3% + last_min_vwap）
  "sz_first_day",            # 深市上市首日（无 20% 板；申报范围 + 14:57）
  "fake_t1_on_cb",           # 转债被套股票 T+1 压掉的当日回转
  "fake_convert_t0",         # 转股所得当日可卖（假正股 T+0）
  "close_def_mismatch",      # 收盘价定义误套（14:57 vs last_min_vwap）
  "vs_R_etf_rotation",       # 与实验 R 分列（ETF 回转不进本页主结论）
  "vs_M_O_aft_channel",      # 盘后通道分列诊断（禁混表）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 换手差 ΔTO（Q0/Q1 相对 Q2）；  
2. 板/申报范围标签差异率 ΔBoard；  
3. 假 T+1 / 假转股 T+0 贡献差 ΔFake；  
4. 失败/跳过笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔTO| **≥ Y** 或 |ΔBoard| **≥ G** 或 |ΔFake| **≥ Y2** 或 |ΔFail| **≥ N**，记「可转债规则混用执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 换手差显著门槛 | **写死** `params.Y=0.02` 并冻结 |
| G | 板标签差异率门槛 | **写死** `params.G=0.01` 并冻结 |
| N | 失败笔数率差门槛 | **写死** `params.N=0.05` 并冻结 |
| Y2 | 假 T+1/假转股 T+0 贡献门槛 | **写死** `params.Y2=0.015` 并冻结 |
| asof_check_date | 核对日锚点（泄露诊断） | **写死默认** `2026-10-26`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| cb_limit_cut_date | ±20% 切日 | **写死** `2022-08-01` |
| copy_sh_first_day_to_sz | 是否抄沪市首日到深市 | **写死** `False` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**`params.Y` / `params.G` / `params.N` / `params.Y2` 写入冻结（具体数已写入；禁继续 null；禁 holdout 标定）**：

```
# 纸面冻结默认（机制实验相对门槛；一经写入即冻结）
# 单位：Y/Y2 = abs(ΔTO) 或 abs(ΔFake) 相对；G = abs(ΔBoard) 相对；N = abs(ΔFail) 失败率（小数）
params.Y  = 0.02    # 换手差显著门槛 ≥ 2pp
params.G  = 0.01    # 板标签差异率门槛 ≥ 1pp
params.N  = 0.05    # 失败率差门槛 ≥ 5pp
params.Y2 = 0.015   # 假 T+1/假转股 T+0 贡献门槛 ≥ 1.5pp
```

门槛已在纸面写入并冻结；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、回转/板切日/首日分列/转股可卖日、`q1_convert_stock_same_day_sell` / `q1_rotation` / `missing_last_min_vwap_policy` / `cb_face_value` / `cb_lot_size` / `q0_unit_source`、主窗/`oos_split` 开工拉数前必须保持冻结；**禁止跑后改口**。

**风控补丁四条（2026-11-02；拉数前冻结）**：

```
params.q1_convert_stock_same_day_sell = False                      # Q1转股所得次日可卖；禁缺键继承
params.missing_last_min_vwap_policy   = skip_first_day_close_leg   # 无last_min_vwap→skip首日收盘腿；禁双挂
params.cb_face_value                  = 100                        # 可转债面值（元）
params.cb_lot_size                    = 10                         # 一手=10张
params.q0_unit_source                 = stock_share_lot            # 天真组股票100股一手混用；暴露鸿沟
params.q1_rotation                    = same_day                   # Q1现行转债回转；禁误套stock_t1
```

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「转债按股票回放差不多」或「这类转债能买」。

结论栏：空。跑完只写「该假设下差多少」，不写「这类转债能买」。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验可转债规则混用（回转 / 板 / 收盘 / 转股腿）**，**不为转债交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权、PIT 切日、禁抄沪市首日到深市、禁盘后混表、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价撮合或判板**。  
2. **把可转债写成股票 T+1 却标 Q2 诚实**。  
3. **2022-08-01 前套次日 ±20% 却标 PIT**。  
4. **把沪市首日 57.3%/43.3% 板抄到深市**（违反 `copy_sh_first_day_to_sz=False`）。  
5. **深市首日当有 20% 板，或忽略 157.3%/56.7% 有效申报范围**。  
6. **沪市首日收盘用 14:57 集合，或深市首日收盘忽略 14:57 集合**（与细则相反）。  
7. **转股所得股票当日可卖却标诚实（发明正股 T+0）**。  
8. **把深市可转债盘后定价与股票盘后固定价格合成一张表却不标注通道**（违反 `merge_sz_cb_aft_with_stock_aft=False`；与 M/O 分列）。  
9. **宇宙泄露 / holdout 反调**：看完 OOS 再改回转、切日、首日分列或显著性门槛。  
10. **把差异写成「这类转债能买」或选债公式**。  
11. **把 ETF 回转结论混进本页主表（实验 R）**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | 可转债代码 |
| exchange (SSE/SZSE) | 沪深分列 | 缺 → skip |
| open/high/low/close（未复权匹配成交） | 价腿 / 板 | **禁复权** |
| issue_price | 深市首日申报范围 | 首日腿需要 |
| ipo_first_day_flag | 上市首日 | 缺 → skip 首日腿 |
| official_close / last_min_vwap / auction_1457_px | 收盘定义对照 | 有则更好；缺则 skip 对应诊断 |
| convert_apply_date / stock_available_date | 转股腿 | 诚实组股票次日可卖 |
| 可转债规则表（回转/切日/首日沪深） | PIT | 本页 §2.1 已锁默认；不必新开数据商 |
| 盘后通道标记（可选） | 禁混表自检 | 与 M/O 分列 |

**明确**：不依赖聚宽；**不要求新开 Level-2 / 新数据商**——日频未复权匹配成交 OHLC + 交易所 + 首日/发行价 + 转股日期 + 本页规则表即可起步。无 last_min_vwap 字段时，沪市首日收盘诊断 skip（**`params.missing_last_min_vwap_policy=skip_first_day_close_leg` 写死**），不得静默用 14:57 却标 Q2。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=Q`，`groups=[Q0,Q1,Q2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-26`**，**`params.fill_time=next_open`（写死）**，**`params.cb_rotation=same_day`**，**`params.cb_limit_cut_date=2022-08-01`**，**`params.cb_limit_pct_post_cut=0.20`**，**`params.sh_first_day_up_pct=0.573` / `params.sh_first_day_dn_pct=0.433`**，**`params.sh_first_day_close_def=last_min_vwap`**，**`params.sz_first_day_board=none`**，**`params.sz_first_day_order_range_up=1.573` / `params.sz_first_day_order_range_dn=0.567`**，**`params.sz_first_day_close_def=auction_1457`**，**`params.copy_sh_first_day_to_sz=False`**，**`params.q0_treat_as_stock=True`**，**`params.q0_rotation=stock_t1`**，**`params.q0_limit_source=stock_board_default`**，**`params.q0_close_def=stock_1457_auction`**，**`params.q0_convert_stock_same_day_sell=True`**，**`params.q1_asof_leak_rules=True`**，**`params.q2_pit=True`**，**`params.q2_convert_stock_same_day_sell=False`**，**`params.q1_convert_stock_same_day_sell=False`（写死冻结；禁缺键继承）**，**`params.q1_rotation=same_day`（写死）**，**`params.missing_last_min_vwap_policy=skip_first_day_close_leg`（写死；禁双挂）**，**`params.cb_face_value=100`**，**`params.cb_lot_size=10`**，**`params.q0_unit_source=stock_share_lot`（写死）**，**`params.merge_sz_cb_aft_with_stock_aft=False`**，**`params.missing_exch_policy=skip`**，**`params.missing_ipo_flag_policy=skip`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[pre_20220801,post_20220801,sh_first_day,sz_first_day,fake_t1_on_cb,fake_convert_t0,close_def_mismatch,vs_R_etf_rotation,vs_M_O_aft_channel]`（写死默认；拉数前冻结）**，**`params.Y=0.02` / `params.G=0.01` / `params.N=0.05` / `params.Y2=0.015`（写死具体数并冻结；禁 holdout 标定；禁 null）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_A=off`，`overlay_R=off`，`overlay_M=off`，`overlay_O=off`，`cost_switch=off`（Q 主跑）。  
- 行情与规则表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- Q0/Q1/Q2 换手、板标签一致率、假 T+1 / 假转股 T+0 贡献、失败笔数；分桶（2022-08-01 前/后、沪市首日、深市首日、假 T+1、假转股 T+0、收盘定义误套、vs R/M/O）。  
- 自检布尔：是否未复权；Q2 是否当日回转；2022-08-01 前是否未套 ±20%；是否未抄沪市首日到深市；转股腿是否次日可卖；盘后是否未混表；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把天真转债当股票当实盘预期；催跑抢 A 真数队列。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**P 不开回测**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` 一致：可转债不是股票那一套（当日回转；2022-08-01 起次日 ±20%，首日沪深写法不同；沪市收盘是最后一分钟加权，不是 14:57 集合）；转股得到的是股票，次日才上市流通，不能靠转股把股票做成 T+0。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 Q 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A/D–P 正文**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权匹配成交 OHLC + 交易所 + 首日/发行价 + 转股日期 + 本页规则表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测；**P 不开回测**） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-26；**fill_time=next_open 写死**；cb_limit_cut_date=2022-08-01；沪市首日 57.3%/43.3%+last_min_vwap；深市首日无板+申报范围+14:57；**copy_sh_first_day_to_sz=False**；**q2_convert_stock_same_day_sell=False**；**`q1_convert_stock_same_day_sell=False`**；**`q1_rotation=same_day`**；**`missing_last_min_vwap_policy=skip_first_day_close_leg`**；**`cb_face_value=100` / `cb_lot_size=10` / `q0_unit_source=stock_share_lot`**；merge_sz_cb_aft_with_stock_aft=False；diff_buckets 九桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死具体数并冻结、禁 holdout 标定、禁 null** |

---

## 变更

- 2026-11-02：新建标准件（总管线：P 草稿已收后写 Q；选型对齐清单实验 Q「可转债按股票规则回放 / 规则混用」；机制类预埋 fail_policy/oos/红线豁免/params 冻结；**不抢实验 A**；**不派回测**；**本页不开回测**；**P 不开回测**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设Q-20261102.md` 有条件通过补四条——① `params.q1_convert_stock_same_day_sell=False`（与§2.3表同向；禁缺键继承）；② `params.missing_last_min_vwap_policy=skip_first_day_close_leg`（与§6同向；禁双挂）；③ `params.cb_face_value=100` / `params.cb_lot_size=10` / `params.q0_unit_source=stock_share_lot`；④ `params.q1_rotation=same_day`。**不抢实验 A**；**Q 不开回测**；未动 P/A。
