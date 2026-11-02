# 假设 O · 大宗量价并进竞价 / 三条盘后通道混用（大宗假流动性）

更新：2026-11-02（风控补丁）  
来源：总管线 / 假设 O 纸面预检有条件通过；清单实验 O  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「日量含大宗 / 按大宗价成交 / 三条盘后通道合成一句」当实盘预期；不抢实验 A 真数队列；本页不开回测；O 不开回测）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 O 对齐。与假设 M（盘后固定价格补成交）、N（收盘机制+假 GTC）、A（板上可成交）互补：本页专测两件事——（1）把**大宗量/价并进竞价**估冲击或回放普通日频信号（假流动性）；（2）把**盘后固定价格、深市盘后定价大宗、沪市大宗固定价格申报**混成同一张表却不标注通道，或把 **16:00–17:00 / VWAP 固定价格**误写成已实施。**比较通道写死分列；禁止与实验 M 主表混报却不标注。**

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1 下，用「日成交量（含大宗结束后计入的那截）」估冲击/换手，并允许按大宗成交价（或含大宗的量加权价）回放普通日频信号，相对「只用竞价量价、大宗腿记不可按此价成交，且每个交易日按当时确认时点 + 三条盘后通道分列」的 PIT 诚实组，会**显著高估竞价可冲击流动性与「大宗价腿」贡献**；再把核对日现行确认时点（创业板盘中确认 + 科创板固定价格大宗已开）铺满全样本（泄露组），会在创业板 `<2026-07-06`、沪市主板尾盘确认、科创板固定价格大宗切日前进一步错标。

证伪方向：若天真组 / 泄露组相对诚实组的换手差、冲击差、「大宗价腿」贡献差在标定噪声带内可忽略，且「创业板 2026-07-06 前 / 沪市主板 / 科创板」分桶不改变结论，则本假设在该样本与撮合设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 大宗量价 vs 竞价；确认时点 PIT；三条盘后通道分列（未复权）

```
# 配置写死（见 §7）
# params.asof_check_date                 写死默认 2026-10-23  # 事实与坑大宗核对日；泄露组「现行」锚点
# params.block_threshold_shares          写死默认 300000     # A 股单笔不低于 30 万股（或）
# params.block_threshold_notional        写死默认 2000000    # 金额不低于 200 万元；基金档另桶（本页主样本股票）
# params.chinext_block_intraday_start    写死默认 2026-07-06 # 创业板协议大宗改盘中确认
# params.sh_main_confirm_window          写死默认 "15:00-15:30"
# params.star_confirm_intraday           写死默认 True       # 科创板开市起盘中确认
# params.star_fixed_price_block_start    写死默认 2026-07-06 # 科创板增加大宗固定价格类型；此前不适用
# params.sh_1600_1700_enabled            写死默认 False      # 16:00–17:00 成交申报继续暂缓
# params.sh_vwap_fixed_enabled           写死默认 False      # 沪市固定价格申报 VWAP 继续暂缓
# params.fill_time                        写死 next_open      # 信号主腿与 A/D 对齐；本页测量价/通道，不抢 A 板上队列
# params.o0_volume_includes_block        写死默认 True       # 天真：日量含大宗
# params.o0_allow_block_px_fill          写死默认 True       # 天真：可按大宗价或含大宗量加权回放
# params.o1_auction_only                 写死默认 True       # 半诚实：只用竞价量价；大宗腿不可按此价成交
# params.o2_leak_confirm_asof            写死默认 True       # 泄露：全样本抄 asof_check_date 现行确认时点
# params.o3_pit_confirm                  写死默认 True       # PIT：每交易日按当日已生效确认窗
# params.channel_split_mode              写死 three_named    # aft_fixed | sz_aft_pricing_block | sh_block_fixed 分列
# params.merge_three_channels            写死 False          # 禁合成一句/一张主表不标注
# params.block_into_index                写死 False          # 大宗不进指数（与实验 P 分列；本页只诊断）
# params.day_vol_timing                  写死 after_block_end  # 日总量在大宗结束后才计入；估竞价冲击须拆
# params.missing_block_fields_policy     写死 skip_block_leg # 缺大宗分列字段 → 跳过大宗腿，不静默并进日量
# params.o0_channel_mix_mode             写死 volume_price_only  # 消解 O0「可混通道」与 merge_three_channels=False；禁双挂 o0_allow_unlabeled_merge
# params.liq_redline_vol_basis           写死 auction_only_ex_block  # 红线流动性分母=前日竞价量剔大宗；禁含大宗日量标诚实
# params.redline_v0_exempt_scope         写死 position_industry_dd_only  # 仅仓位/行业/回撤豁免；流动性5%诚信不豁免
# params.block_vol_source                写死 vendor_block_field  # 优先 §6 vol_block/分列；禁门槛从日总量反推
# params.block_gt_day_vol_policy         写死 skip_block_leg  # 大宗量>日总量 → 跳过该腿；禁跑后改 clamp_zero
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  写死具体数并冻结；禁 holdout 标定
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 fill_time·确认切日·三通道合并开关·o0_channel_mix_mode·liq_redline_vol_basis·redline_v0_exempt_scope·block_vol_source·block_gt_day_vol_policy·门槛·Y/G/N/Y2·主窗/oos

tick = 0.01  # A 股股票默认；基金价位另案，本页主样本股票
fill_time = "next_open"
asof_check_date = "2026-10-23"
block_threshold_shares = 300000
block_threshold_notional = 2000000
chinext_block_intraday_start = "2026-07-06"
sh_main_confirm_window = "15:00-15:30"
star_confirm_intraday = True
star_fixed_price_block_start = "2026-07-06"
sh_1600_1700_enabled = False
sh_vwap_fixed_enabled = False
channel_split_mode = "three_named"
merge_three_channels = False
block_into_index = False
day_vol_timing = "after_block_end"
missing_block_fields_policy = "skip_block_leg"
o0_channel_mix_mode = "volume_price_only"          # 单一枚举；禁双挂 o0_allow_unlabeled_merge
liq_redline_vol_basis = "auction_only_ex_block"    # 红线分母；禁 day_total_incl_block 标诚实
redline_v0_exempt_scope = "position_industry_dd_only"  # 流动性5%不豁免
block_vol_source = "vendor_block_field"            # 禁门槛从日总量反推
block_gt_day_vol_policy = "skip_block_leg"         # 大宗>日总量 → skip；禁跑后改 clamp_zero

CHANNEL_AFT_FIXED = "aft_fixed"                    # 盘后固定价格（实验 M 主通道；无 30万/200万门槛）
CHANNEL_SZ_AFT_PRICING_BLOCK = "sz_aft_pricing_block"  # 深市盘后定价大宗 15:05–15:30；收盘价或当日 VWAP
CHANNEL_SH_BLOCK_FIXED = "sh_block_fixed"          # 沪市大宗固定价格申报 15:00–15:30；收盘价；VWAP 暂缓

def block_confirm_window(board, asof_date):
    # 返回确认窗标签；未知 → None → fail_policy=skip
    if board in ("Main", "SH_Main"):
        return sh_main_confirm_window  # 15:00-15:30；15:00 仍停牌 → 当日不再接受
    if board == "STAR":
        if star_confirm_intraday:
            return "09:30-11:30|13:00-15:30"  # 开市起盘中
        return None
    if board in ("ChiNext", "CYB"):
        if asof_date >= chinext_block_intraday_start:
            return "09:30-11:30|13:00-15:30"  # 2026-07-06 起盘中确认
        return "15:00-15:30"  # 切日前仍收盘后确认
    return None

def leak_confirm_window(board):
    # O2：全样本抄核对日现行（创业板已盘中；科创盘中；沪主板仍 15:00-15:30）
    return block_confirm_window(board, asof_check_date)

def star_fixed_price_block_on(asof_date):
    # 科创板大宗固定价格：2026-07 技术实施指南起才增加；此前不适用
    return asof_date >= star_fixed_price_block_start

def auction_volume(day_vol_total, block_vol):
    # 竞价量 = 日总量剔大宗（大宗结束后才计入日总量）
    # block_vol 来源见 params.block_vol_source=vendor_block_field；缺字段 → None → skip
    if day_vol_total is None:
        return None
    if block_vol is None:
        return None  # missing_block_fields_policy=skip_block_leg → 上层 skip，禁静默当竞价-only
    if block_vol > day_vol_total:
        # params.block_gt_day_vol_policy=skip_block_leg（写死）：分列异常 → 上层 skip 该腿；禁静默 clamp
        if block_gt_day_vol_policy == "skip_block_leg":
            return None
        if block_gt_day_vol_policy == "clamp_zero":
            return 0  # 本页不用；若选用须自检报异常笔数
        raise ValueError("block_gt_day_vol_policy must be skip_block_leg|clamp_zero")
    return day_vol_total - block_vol

def naive_liquidity_vol(day_vol_total, block_vol):
    # O0：日量含大宗，直接当竞价可冲击流动性
    return day_vol_total

def naive_fill_px(auction_close, block_px, vwap_incl_block):
    # O0：可取大宗价或含大宗量加权
    if o0_allow_block_px_fill:
        if block_px is not None and block_px > 0:
            return block_px
        if vwap_incl_block is not None and vwap_incl_block > 0:
            return vwap_incl_block
    return auction_close

def auction_only_fill_px(auction_close):
    # O1：只用竞价价；大宗腿记不可按此价成交
    return auction_close

def channel_tag(intent_channel, group=None):
    # 全局 merge_three_channels=False 写死；遇 True 即 raise
    # o0_channel_mix_mode=volume_price_only：O0 也强制分列标签；混用仅叙事/诊断桶，禁未标注并进主表
    # （若改选 o0_allow_unlabeled_merge：仅 O0 组可混表，O1–O3/主报告仍 False——本页不用，禁双挂）
    if merge_three_channels:
        raise ValueError("merge_three_channels must stay False")
    if o0_channel_mix_mode == "o0_allow_unlabeled_merge" and group == "O0":
        return "o0_unlabeled_merge_diagnostic"  # 本页默认不用
    if o0_channel_mix_mode not in ("volume_price_only", "o0_allow_unlabeled_merge"):
        raise ValueError("o0_channel_mix_mode must be volume_price_only|o0_allow_unlabeled_merge")
    if intent_channel not in (CHANNEL_AFT_FIXED, CHANNEL_SZ_AFT_PRICING_BLOCK, CHANNEL_SH_BLOCK_FIXED, "auction", "block_negotiate"):
        return "unknown_skip"
    return intent_channel

def forbidden_implemented_windows():
    # 硬禁：不得写成已实施
    assert sh_1600_1700_enabled is False
    assert sh_vwap_fixed_enabled is False
```

- **天真（O0）**：日成交量含大宗；成交价可取大宗价或含大宗量加权；不拆确认时点（发明假流动性）。**`params.o0_channel_mix_mode=volume_price_only`（写死冻结）**——O0 **只**发明「日量含大宗 / 按大宗价回放」；三通道仍强制分列标签（与全局 `merge_three_channels=False` 同向）；通道混用仅允许叙事或进诊断桶，**禁止**未标注并进 O0/主表。**禁止**双挂 `o0_allow_unlabeled_merge`；**禁止**把 O0 混表口径写进 O3/主结论。
- **竞价-only（O1）**：只用竞价量价估冲击/换手；大宗腿记「不可按此价成交」；**不**按大宗价回放普通信号。确认时点本档可不做全 PIT（与 O3 分列）。
- **泄露（O2）**：量价可与 O1 同向拆大宗，但确认时点/科创固定价格大宗**全样本**用 `asof_check_date=2026-10-23` 现行文本铺满（创业板盘中确认 + 科创固定价格大宗已开）。
- **PIT 诚实（O3）**：每个交易日用当日已生效确认窗；盘后固定价格 / 深市盘后定价大宗 / 沪市大宗固定价格申报**分列**；`sh_1600_1700_enabled=False`、`sh_vwap_fixed_enabled=False`；科创板 `<star_fixed_price_block_start` 不适用固定价格大宗；大宗**不进**即时行情/指数。
- **禁止**：用复权价；把 16:00–17:00 或 VWAP 固定价格写成已实施；把差异写成「这类票能买」；与实验 M 盘后固定价格混成同一张主表却不标注通道。

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺板块/确认窗、缺大宗分列字段却要估竞价冲击、未知通道、把暂缓窗写成已实施、三通道合并开关被打开 → **跳过该腿**，不按大宗价假成、不把大宗量并进竞价流动性。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 四组对照（本实验编码）

| 组 | 量价假设 | 确认时点 / 通道 |
|----|----------|-----------------|
| O0 天真-含大宗 | 日量含大宗；可按大宗价/含大宗 VWAP 回放 | 不切片；**`o0_channel_mix_mode=volume_price_only`**：通道仍分列标签，混用仅叙事/诊断（消解与 `merge_three_channels=False` 冲突） |
| O1 竞价-only | **只用竞价量价**；大宗腿不可按此价成交 | 本档不做全 PIT 确认窗（与 O3 分列） |
| O2 泄露-现行确认铺满 | 量价建议同 O1 拆大宗 | **全样本**抄核对日现行确认 + 科创固定价格大宗已开 |
| O3 PIT 诚实 | 竞价量价；大宗分列 | **每交易日**当时确认窗；三通道分列；暂缓窗关闭 |

同一信号、同一 T+1、同一成本开关（本页可先零成本只比量价/通道差）。**`params.fill_time=next_open` 写死**（主腿与 A/D 对齐；不抢 A 板上真数队列）。禁止把「按大宗价成交」报成诚实竞价腿。

**`params.channel_split_mode=three_named`（写死；拉数前冻结）**：必须能区分 `aft_fixed` / `sz_aft_pricing_block` / `sh_block_fixed`。**`params.merge_three_channels=False`（写死）**——禁止合成一句。

**`params.o0_channel_mix_mode`（写死；拉数前冻结；禁双挂）**：`volume_price_only`。枚举仅允许 `volume_price_only` / `o0_allow_unlabeled_merge`。本页选定前者以消解正文旧述「O0 可不标注混三通道」与全局 `merge_three_channels=False`（`channel_tag` 遇 True 即 raise）的冲突——O0 **只**发明量价（日量含大宗 / 按大宗价回放），三通道仍强制分列标签；混用仅叙事或诊断桶。**禁止**选用 `o0_allow_unlabeled_merge` 却不自检注明；**禁止**把 O0 混表口径写进 O3/主结论；**禁止**双挂。

**`params.liq_redline_vol_basis` + `params.redline_v0_exempt_scope`（写死；拉数前冻结）**：`auction_only_ex_block` + `position_industry_dd_only`。红线「流动性≤前日竞价量 5% 剔大宗」分母用**竞价剔大宗量**（与 O1/O3 同向）；豁免范围仅单票仓位 / 行业集中 / 回撤熔断。**流动性 5% 诚信不豁免**，且不得改口用 `day_total_incl_block` 当红线分母却标 O1/O3。`full_incl_liq` 本页不用。

**`params.block_vol_source`（写死；拉数前冻结）**：`vendor_block_field`（优先 §6 `vol_block` / 分列字段）。缺字段 → 与 `missing_block_fields_policy=skip_block_leg` 对齐，跳过大宗腿与「竞价量=日量−大宗」推导。**禁止**无分列字段时用 30 万股/200 万元门槛从日总量反推大宗并标 O1/O3；`infer_threshold_from_ticks` 本页不要求 L2、不选用。

**`params.block_gt_day_vol_policy`（写死；拉数前冻结）**：`skip_block_leg`。分列字段异常、大宗量 > 日总量时跳过该腿（`auction_volume` 返回 None → 上层 skip）。枚举另有 `clamp_zero`（旧伪码 `max(0,…)`），本页不用；若改选须自检注明并报异常笔数。**禁止**跑后因冲击/换手差改口。

**`params.missing_block_fields_policy=skip_block_leg`（写死）**：日频无大宗分列字段时，跳过大宗腿与「竞价量=日量−大宗」推导；**禁止**静默把日总量当竞价流动性并标 O1/O3。

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股股票为主；基金/ETF 大宗门槛另桶（本页不进主权重）。不含可转债主样本（实验 Q）。  
- **排除（默认）**：调仓日未上市；成交日缺未复权竞价 OHLC；把 16:00–17:00 / VWAP 固定价格写成已实施并进主结论。  
- **股票池 PIT**：每个调仓日只用当日已生效名单（可与实验 C 共用）。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2019-01-01`  
  - `params.date_end=2026-09-30`  
  - 覆盖科创开市后盘中确认、创业板 `2026-07-06` 确认切日、科创固定价格大宗切日、主板盘后固定价格扩围（与 M 对照）。  
  - 稳健分桶：见 `params.diff_buckets`。  
- **PIT 切片原则**：该日该板块大宗如何确认、日量何时计入、三条盘后通道哪条可用，一律按成交日当时规则。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2019-01-01
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调确认切日、四组定义、三通道合并开关、显著性阈值或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。holdout 含 `2026-07-06` 创业板确认切日与主板盘后扩围，便于一次性观察泄露/天真在切日前后的差，**不是**用来回改 O3 定义。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **O0 − O3**：天真「含大宗量价 + 可混通道」相对 PIT——换手差、冲击差、大宗价腿贡献差、失败/跳过笔数差。  
2. **O1 − O3**：竞价-only 相对全 PIT（确认窗 + 三通道分列）——看「只拆量价、不切片确认」是否仍够用。  
3. **O2 − O3**：现行确认铺满相对 PIT——看创业板 `<2026-07-06`、科创固定价格大宗切日前是否被系统性错标。  
4. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "chinext_pre_20260706",       # 创业板协议大宗仍 15:00–15:30 确认
  "chinext_post_20260706",      # 创业板盘中确认后
  "sh_main_confirm_1500",       # 沪市主板尾盘确认窗
  "star_intraday_confirm",      # 科创板盘中确认
  "star_fixed_px_block_pre",    # 科创固定价格大宗切日前（不适用）
  "star_fixed_px_block_post",   # 科创固定价格大宗切日后
  "vs_M_aft_fixed",             # 与 M 盘后固定价格分列诊断（禁混主表）
  "sz_aft_pricing_block",       # 深市盘后定价大宗桶
  "sh_block_fixed",             # 沪市大宗固定价格申报桶（VWAP 暂缓）
  "forbidden_1600_1700",        # 误标 16:00–17:00 已实施（诊断；主结论必须为 0 笔）
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 换手差 ΔTO（O0−O3 等；竞价可冲击量被大宗灌胖的那截）；  
2. 冲击差 ΔImpact（用含大宗日量估冲击 vs 竞价-only）；  
3. 大宗价腿贡献差 ΔBlockPx（被「按大宗价回放」吃到的那截收益/成交量）；  
4. 失败/跳过笔数差 ΔFail（缺字段、未知通道、暂缓窗误开）。

**相对判据（草稿）**：若 |ΔTO| / |ΔImpact| **≥ Y** 或 |ΔBlockPx| **≥ G** 或 |ΔFail| **≥ N**，记「大宗假流动性 / 通道混用执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 换手差 / 冲击差显著门槛 | **写死** `params.Y=0.02` 并冻结 |
| G | 大宗价腿贡献差门槛 | **写死** `params.G=0.01` 并冻结 |
| N | 失败笔数率差门槛 | **写死** `params.N=0.05` 并冻结 |
| Y2 | 稳健子窗换手/冲击差门槛（可选） | **写死** `params.Y2=0.015` 并冻结 |
| asof_check_date | 泄露组「现行」核对日 | **写死默认** `2026-10-23`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| channel_split_mode | 三通道分列 | **写死** `three_named` |
| merge_three_channels | 是否允许混表 | **写死** `False` |
| o0_channel_mix_mode | O0 与三通道冲突消解 | **写死** `volume_price_only`；禁双挂 |
| liq_redline_vol_basis | 红线流动性分母 | **写死** `auction_only_ex_block` |
| redline_v0_exempt_scope | 红线豁免范围 | **写死** `position_industry_dd_only` |
| block_vol_source | 大宗量来源 | **写死** `vendor_block_field` |
| block_gt_day_vol_policy | 大宗>日总量策略 | **写死** `skip_block_leg` |
| sh_1600_1700_enabled | 16:00–17:00 | **写死** `False` |
| sh_vwap_fixed_enabled | VWAP 固定价格 | **写死** `False` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**`params.Y` / `params.G` / `params.N` / `params.Y2` 写入冻结（具体数已写入；禁继续 null；禁 holdout 标定）**：

```
# 纸面冻结默认（机制实验相对门槛；一经写入即冻结）
# 单位：Y/Y2 = abs(ΔTO) 或 abs(ΔImpact) 相对；G = abs(ΔBlockPx) 相对；N = abs(ΔFail) 失败率（小数）
params.Y  = 0.02    # 换手/冲击差显著门槛 ≥ 2pp
params.G  = 0.01    # 大宗价腿贡献差门槛 ≥ 1pp
params.N  = 0.05    # 失败率差门槛 ≥ 5pp
params.Y2 = 0.015   # 稳健子窗门槛 ≥ 1.5pp
```

门槛已在纸面写入并冻结；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、确认切日、三通道开关、`o0_channel_mix_mode`、`liq_redline_vol_basis`/`redline_v0_exempt_scope`、`block_vol_source`、`block_gt_day_vol_policy`、门槛、主窗/`oos_split` 开工拉数前必须保持冻结；**禁止跑后改口**。

**风控补丁四条（2026-11-02；拉数前冻结）**：

```
params.o0_channel_mix_mode      = volume_price_only          # 消解与 merge_three_channels=False；禁双挂
params.liq_redline_vol_basis    = auction_only_ex_block      # 红线分母=竞价剔大宗；禁含大宗日量标诚实
params.redline_v0_exempt_scope  = position_industry_dd_only  # 仅仓位/行业/回撤豁免；流动性5%不豁免
params.block_vol_source         = vendor_block_field         # 禁门槛从日总量反推
params.block_gt_day_vol_policy  = skip_block_leg             # 大宗>日总量 → skip；禁跑后改 clamp_zero
```

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「日量含不含大宗无所谓」或「三条盘后通道可以合成一句」。

结论栏：空。跑完只写「该假设下差多少」，不写「这类票因大宗折价/盘后通道能买/该规避」。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验大宗量价并进竞价（假流动性）+ 三条盘后通道混用**，**不为组合策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权、PIT 确认切日、三通道分列、禁 16:00–17:00/VWAP 已实施、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做；**流动性≤前日竞价量 5% 剔大宗**诚信红线**不豁免**，分母写死 **`params.liq_redline_vol_basis=auction_only_ex_block`**（禁用含大宗日量当分母却标 O1/O3）。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0；`full_incl_liq` 本页不用。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **日成交量含大宗却标成竞价可冲击流动性（O1/O3）**：发明假流动性；仅允许出现在 O0。  
2. **按大宗成交价回放普通日频信号却标诚实**：等于假设总能找到 30 万股/200 万元对手盘。  
3. **创业板 `<2026-07-06` 按盘中确认处理（O3）**：该段属 O0/O2 敏感。  
4. **科创板 `<2026-07-06` 按已有固定价格大宗处理**。  
5. **把盘后固定价格、深市盘后定价大宗、沪市大宗固定价格申报合成一句/一张主表且不标注**（`merge_three_channels` 必须为 False；`o0_channel_mix_mode` 必须为 `volume_price_only`，禁把 O0 混表写进 O3/主结论）。  
5b. **`o0_channel_mix_mode` 与 `merge_three_channels` 双挂**，或无分列字段却用门槛从日总量反推大宗（违反 `block_vol_source=vendor_block_field`），或大宗>日总量却静默 `clamp_zero` 却标 `skip_block_leg`。  
5c. **红线分母改口用含大宗日量却标 O1/O3**（违反 `liq_redline_vol_basis=auction_only_ex_block`），或把流动性 5% 当成已豁免（违反 `redline_v0_exempt_scope=position_industry_dd_only`）。  
6. **把 16:00–17:00 或 VWAP 固定价格写成已实施**（`sh_1600_1700_enabled` / `sh_vwap_fixed_enabled` 必须 False）。  
7. **用复权价撮合或估冲击**。  
8. **与实验 M 混报主结论且不标注**：M=盘后固定价格通道可用性；O=大宗量价假流动性 + 三通道分列。  
9. **缺大宗分列字段却静默把日总量当竞价量（违反 missing_block_fields_policy / block_vol_source）**。  
10. **宇宙泄露 / holdout 反调**：看完 OOS 再改确认切日、四组定义或显著性门槛。  
11. **把差异写成选股/「这类票能买」**。  
12. **把大宗折价写进指数中性收益**（大宗不进指数；那是实验 P，本页只诊断）。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | |
| board / exchange | 确认窗路由、分桶 | **必填** |
| open/high/low/close（未复权，竞价） | 竞价价腿 | **禁复权** |
| vol_auction 或 (vol_day_total + vol_block) | 竞价量 / 拆大宗 | **`block_vol_source=vendor_block_field`**；缺分列 → skip_block_leg；**禁门槛反推** |
| block_px / block_vol（可选分协议/固定价格/盘后定价） | 大宗价腿、假流动性 | 无则不做 O0 价腿，禁发明 |
| vwap_incl_block（可选） | O0 敏感性 | 非最小集 |
| suspend_to_1500 | 沪主板当日是否仍接受大宗 | 有则更好 |
| 盘后固定价格通道表 | 与 M 复用 | **分列标注** aft_fixed |
| 深市盘后定价大宗标记 | 三通道之一 | sz_aft_pricing_block |
| 沪市大宗固定价格申报标记 | 三通道之一 | sh_block_fixed；VWAP 暂缓 |
| 信号表（可选） | 选股臂 | 无信号可先跑「量价口径 × 通道标签」差 |
| 大宗确认规则表 | 切日 | 可用本页 §2.1 编码，不必新开数据商 |

**明确**：不依赖聚宽；**不要求新开 Level-2/逐笔数据商**——日频未复权竞价 OHLC + 日量/大宗分列（有则）+ 板块 + 本页确认/通道表即可起步「假流动性 + 通道混用」对照。无大宗分列时只做通道分列诊断 + skip 大宗腿，不声称精确冲击复盘。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=O`，`groups=[O0,O1,O2,O3]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-23`**，**`params.block_threshold_shares=300000`**，**`params.block_threshold_notional=2000000`**，**`params.chinext_block_intraday_start=2026-07-06`**，**`params.sh_main_confirm_window=15:00-15:30`**，**`params.star_confirm_intraday=True`**，**`params.star_fixed_price_block_start=2026-07-06`**，**`params.sh_1600_1700_enabled=False`**，**`params.sh_vwap_fixed_enabled=False`**，**`params.fill_time=next_open`（写死）**，**`params.o0_volume_includes_block=True`**，**`params.o0_allow_block_px_fill=True`**，**`params.o1_auction_only=True`**，**`params.o2_leak_confirm_asof=True`**，**`params.o3_pit_confirm=True`**，**`params.channel_split_mode=three_named`**，**`params.merge_three_channels=False`**，**`params.block_into_index=False`**，**`params.day_vol_timing=after_block_end`**，**`params.missing_block_fields_policy=skip_block_leg`**，**`params.o0_channel_mix_mode=volume_price_only`（写死冻结；禁双挂）**，**`params.liq_redline_vol_basis=auction_only_ex_block`（写死）**，**`params.redline_v0_exempt_scope=position_industry_dd_only`（写死；流动性5%不豁免）**，**`params.block_vol_source=vendor_block_field`（写死；禁门槛反推）**，**`params.block_gt_day_vol_policy=skip_block_leg`（写死；禁跑后改 clamp_zero）**，**`params.diff_buckets=[chinext_pre_20260706,chinext_post_20260706,sh_main_confirm_1500,star_intraday_confirm,star_fixed_px_block_pre,star_fixed_px_block_post,vs_M_aft_fixed,sz_aft_pricing_block,sh_block_fixed,forbidden_1600_1700]`（写死默认；拉数前冻结）**，**`params.Y=0.02` / `params.G=0.01` / `params.N=0.05` / `params.Y2=0.015`（写死具体数并冻结；禁 holdout 标定；禁 null）**，`universe_rule`，**`params.date_start=2019-01-01` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2019-01-01,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；豁免范围见 `redline_v0_exempt_scope`；§4.3），`overlay_M=off`（默认 off；盘后固定价格分表），`overlay_A=off`，`cost_switch=off`（O 主跑）。  
- 行情与规则表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- O0/O1/O2/O3 换手、冲击、大宗价腿贡献、失败笔数；分桶（创业板切日前/后、沪主板确认、科创盘中、科创固定价格切日前/后、vs M、深市盘后定价大宗、沪市大宗固定价格、禁窗误标）。  
- 自检布尔：是否未复权；是否拆大宗；O3 是否 PIT 确认；三通道是否分列；`o0_channel_mix_mode` 是否 `volume_price_only`（未把 O0 混表写进 O3/主结论）；`liq_redline_vol_basis` 是否 `auction_only_ex_block`；`redline_v0_exempt_scope` 是否 `position_industry_dd_only`（流动性5%未豁免）；`block_vol_source` 是否 `vendor_block_field`（未门槛反推）；`block_gt_day_vol_policy` 是否 `skip_block_leg`；16:00–17:00/VWAP 是否未写成已实施；是否未与 M 混主表；缺大宗字段是否 skip；holdout 是否未反调。  
- **禁止输出**：具体买卖标的列表当「建议」；把天真含大宗/混通道当实盘预期；催跑抢 A 真数队列。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**O 不开回测**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` 一致：大宗不是竞价，也不是盘后固定价格；日成交量在大宗结束后才计入；确认时点按板块切片。与 `事实与坑.md` 2026-10-23 条一致：门槛 30 万股/200 万元；沪主板 15:00–15:30 确认；科创开市起盘中；创业板 2026-07-06 起盘中确认；深市盘后定价大宗 ≠ 盘后固定价格 ≠ 沪市大宗固定价格申报；16:00–17:00 / VWAP 固定价格继续暂缓。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 O 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A/D–N 正文**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频未复权竞价 OHLC + 日量/大宗分列（有则）+ 板块 + 确认/通道表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测；**O 不开回测**） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2019-01-01..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`；流动性5%不豁免；`liq_redline_vol_basis=auction_only_ex_block`**）；asof_check_date=2026-10-23；block 门槛 30万股/200万元；chinext_block_intraday_start=2026-07-06；star_fixed_price_block_start=2026-07-06；sh_1600_1700_enabled=False；sh_vwap_fixed_enabled=False；**fill_time=next_open 写死**；O0 含大宗 / O1 竞价-only / O2 泄露确认 / O3 PIT+三通道分列；merge_three_channels=False；**`o0_channel_mix_mode=volume_price_only`（消解冲突；禁双挂）**；**`block_vol_source=vendor_block_field`**；**`block_gt_day_vol_policy=skip_block_leg`**；missing_block_fields_policy=skip_block_leg；diff_buckets 十桶写死冻结；**Y=0.02 / G=0.01 / N=0.05 / Y2=0.015 写死具体数并冻结、禁 holdout 标定、禁 null** |

---

## 变更

- 2026-11-02：新建标准件（总管线：N 补丁已收后写 O；选型对齐清单实验 O；机制类预埋 fail_policy/oos/红线豁免/params 冻结；**不抢实验 A**；**不派回测**；**本页不开回测**）。
- 2026-11-02（风控补丁）：按 `experiments/backtest/A_limit_up_fill/risk_notes/预检-假设O-20261102.md` 有条件通过补四条——① `params.o0_channel_mix_mode=volume_price_only`（消解与 `merge_three_channels=False` 冲突；禁双挂 `o0_allow_unlabeled_merge`；禁把 O0 混表写进 O3/主结论）；② `params.liq_redline_vol_basis=auction_only_ex_block` + `params.redline_v0_exempt_scope=position_industry_dd_only`（流动性5%诚信不豁免）；③ `params.block_vol_source=vendor_block_field`（禁门槛从日总量反推）；④ `params.block_gt_day_vol_policy=skip_block_leg`（伪码改异常→skip；禁跑后改 `clamp_zero`）。**不抢实验 A**；**O 不开回测**；P 已暂停未动。
