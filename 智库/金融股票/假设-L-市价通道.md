# 假设 L · 市价申报当「穿过整本档位的无限价」（市价通道）

更新：2026-11-02  
来源：总管线 / K 风控四条已交后下一可离线纸面；清单实验 L  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「市价=从买一吃到涨跌停」当实盘预期；不抢实验 A 真数队列）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 实验 L 对齐。与假设 I（**限价**笼子/远限价）、A（板上可成交）、G（无板日 PIT）、J（无板日临停）、K（融券禁市价）互补：本页专测**市价申报通道**被当成「穿过整本档位的无限价」时，对废单率与冲击路径的扭曲。**比较通道写死为市价；禁止与 I 的限价笼子混成同一张主表却不标注通道。**

---

## 1. 一句话假设（可检验、可证伪）

同一信号、同一持有期、同一 T+1 下，把市价当成「按当日最高买 / 最低卖连续吃穿整本档位」，相对「沪市仅连续竞价且成交/转限价不得超过保护限价（无保护限价记废单）；深市仅有涨跌幅限制证券的连续竞价可市价，无涨跌幅日与开盘/收盘集合竞价记失败」的诚实组，**废单低估与冲击高估会显著升高**；再把沪市现行保护限价规则铺满全样本（泄露组），会在沪市主板 `<2023-04-10`、深市无板日等切片进一步错标可成交。

证伪方向：若天真组 / 泄露组相对诚实组的废单率差、成交价相对盘口（或远市价敏感性）偏离差、净值差在标定噪声带内可忽略，且「深市无板日 / 沪市主板切日前 / 科创板」分桶不改变结论，则本假设在该样本与撮合设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 市价通道（按成交日当时规则；未复权；与限价笼子分列）

```
# 配置写死（见 §7）
# params.asof_check_date              写死默认 2026-10-16  # 事实与坑市价核对日；泄露组「现行」锚点
# params.sh_protect_cut_date          写死默认 2023-04-10  # 沪市主板保护限价+本方/对手方最优落地日（与首只注册制主板同日）；科创开市起即要保护限价
# params.sz_mkt_only_with_limit       写死默认 True       # 深市：仅有涨跌幅限制证券的连续竞价可市价
# params.auction_mkt_allowed          写死默认 False      # 开盘/收盘集合竞价禁市价
# params.short_leg_mkt_allowed        写死默认 False      # 融券腿禁市价（与 K 同向）
# params.fill_time                     写死 next_open      # 与 A/D 次日开对齐；不用 next_close
# params.protect_limit_mode           写死 default_pct    # 日频无盘口时的保护限价假设；见下
# params.protect_limit_pct_buy        写死默认 1.02       # 买入保护上限相对参考价（日频占位；≠限价笼子基准）
# params.protect_limit_pct_sell       写死默认 0.98       # 卖出保护下限相对参考价
# params.protect_ref                  写死默认 last_or_preclose  # 日频参考：有最新成交用最新，否则前收；禁把买卖一臆造成真盘口
# params.day_freq_mode                写死 far_mkt_sensitivity  # 无买卖一时只做远市价敏感性，禁声称精确吃档复盘
# params.far_mkt_mult                 写死默认 [1.0, 1.02, 1.05, 1.10]  # 相对参考价的「愿接受多远」敏感性；拉数前冻结
# params.diff_buckets                 写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2               拉数前写入具体数并冻结；禁 holdout 标定
# 拉数前冻结；禁 holdout / 事后改口 / 禁跑后改 fill_time·protect_*·far_mkt_mult·auction_mkt_allowed

tick = 0.01  # A 股股票默认；基金/ETF/可转债勿混入本页主样本
fill_time = next_open
auction_mkt_allowed = False
short_leg_mkt_allowed = False

def is_no_limit_day(i, t, no_limit_table):
    # 复用假设 G 的 PIT 无板表
    return no_limit_table.get((i, t), False)

def is_continuous_auction_slot(session):
    # 本页日频最小集：信号腿若标注 open_auction / close_auction → 市价失败
    return session == "continuous"

def sh_protect_required(board, asof_date):
    # 科创开市起；沪市主板随 2023-04-10 引入保护限价
    if board == "STAR":
        return True
    if board in ("Main", "SH_Main"):
        return asof_date >= params.sh_protect_cut_date
    # 沪市其他股票类：切日后按现行须带保护限价；切日前按「无保护限价字段」诚实组记废单或仅连续竞价敏感性（见 L1）
    return asof_date >= params.sh_protect_cut_date

def sz_market_allowed(board, asof_date, no_limit):
    # 深市：仅有涨跌幅限制证券的连续竞价；无板日主机不接受市价
    if no_limit:
        return False
    return True  # 有板 + 连续竞价；集合竞价仍由 auction_mkt_allowed=False 挡

def protect_cap(side, ref_px):
    # 日频占位：买入成交/转限价 ≤ ref * protect_limit_pct_buy；卖出 ≥ ref * protect_limit_pct_sell
    # 有真实保护限价字段时优先生效；本函数只服务 day_freq_mode=far_mkt_sensitivity
    if ref_px is None or ref_px <= 0:
        return None
    if side == "buy":
        return ref_px * params.protect_limit_pct_buy
    return ref_px * params.protect_limit_pct_sell

def naive_mkt_fill(side, high, low):
    # L0：市价=吃穿到当日极值
    return high if side == "buy" else low
```

- **沪市诚实（L1）**：市价**只适用于连续竞价**；须带买入/卖出保护限价；成交价与转限价不得突破保护限价；无保护限价 → **废单**（`fail_policy=skip`）。科创开市起即要保护限价；沪市主板保护限价与本方/对手方最优自 **`params.sh_protect_cut_date=2023-04-10`** 落地（非印发日）。切日前主板：诚实组**不得**用现行保护限价规则假装当时已有；无字段则该市价腿 skip 或仅报「无保护限价通道」失败（与 L3 泄露对照）。  
- **深市诚实（L2）**：市价**只适用于有价格涨跌幅限制证券的连续竞价**；**无涨跌幅日**与**开盘/收盘集合竞价** → 记失败。**2026 修订深市 3.3 没有「保护限价」句——禁止把沪市保护限价抄到深市。**  
- **日频最小集**：没有买卖一/最新成交盘口时，**只做** `day_freq_mode=far_mkt_sensitivity`（`far_mkt_mult` 敏感性），**禁止**声称精确吃档复盘。有盘口时可增强，但不得事后改主结论口径。  
- **与 I 分列**：I = **限价**能挂多远（笼子）；L = **市价**通道与保护限价/交易所接受条件。主报告分表；稳健性叠加须声明 `overlay_I`。  
- **禁止**：用复权价；集合竞价下市价；融券腿市价；深市无板日仍按市价成交；把沪市保护限价抄到深市；把差异写成「这类票能买」。

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺交易所/板块、缺无板旗却硬判深市可市价、沪市须保护限价却无保护限价且无事先写死的 `protect_limit_mode`、集合竞价腿、融券市价腿 → **跳过该腿**，不成交、不用 high/low 填「假无限价市价」。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完净值再改口**。未写明则以 skip 为准。

### 2.3 四组对照（本实验编码）

| 组 | 市价假设 | 保护限价 / 接受条件 | 无板日与集合竞价 |
|----|----------|---------------------|------------------|
| L0 天真-无限价吃穿 | 按当日最高买 / 最低卖（或目标价夹在 high-low 内即成） | 无 | 仍可「市价」成 |
| L1 沪市诚实 | 仅连续竞价；成交≤保护限价 | **每个交易日**用当日已生效沪市规则；无保护限价→废单；切日前不套现行 | 沪市切日后无板证券可市价但仍受保护限价；集合竞价仍废 |
| L2 深市诚实 | 仅有板证券连续竞价 | **不**套沪市保护限价 | 无板日与集合竞价 → 失败 |
| L3 泄露-现行沪市铺满 | 受「保护限价」约束 | **全样本**（含深市、含沪市 `<2023-04-10`）抄核对日沪市现行保护限价口径 | 可能把深市无板日/切日前错标成「有保护即可市价」 |

同一信号、同一 T+1、同一成本开关（本页可先零成本只比市价通道差）。成交时点 **`fill_time=next_open` 写死**。无板日判定见 G；限价笼子见 I；融券禁市价见 K——**勿把 I/K/A 主结论混进 L 主报告**。

**成交时点（写死）**：`fill_time=next_open`（与假设 A/D 次日开对齐；**本页不用** `next_close`；拉数前冻结；禁跑后改口）。

**`params.protect_limit_mode`（写死；拉数前冻结）**：日频无投资者真实保护限价字段时的处理：
- `default_pct`：用 `protect_limit_pct_buy/sell` × `protect_ref`（本页默认）；
- `require_field`：无字段则 skip（更严；改此须拉数前写入）；
- **禁止** `infinite`（那是 L0）。

**`params.far_mkt_mult`（写死默认列表；拉数前冻结）**：`[1.0, 1.02, 1.05, 1.10]`。用于远市价敏感性；**禁 holdout 改列表**；**禁**与假设 I 的 `far_limit_mult` 混用同一输出列名却不标注通道。

---

## 3. 样本区间

- **宇宙（默认）**：沪深 A 股股票。不含可转债主样本、不含股票 ETF 主样本（ETF 市价/收盘机制另案）。  
- **排除（默认）**：调仓日未上市；成交日缺 high/low（L0 需要）或无法识别交易所/板块；融券卖出腿（本页多头/普通买卖市价；空头市价直接 fail）；把集合竞价腿硬标成连续竞价。  
- **股票池 PIT**：每个调仓日只用当日已生效名单（可与实验 C 共用）。  
- **区间建议**：待数据接入后锁定起止。建议复现默认（可改，须写入配置）：  
  - 主窗：覆盖 `params.sh_protect_cut_date=2023-04-10` 前后，并含足够深市无板日（G 表）与科创样本；  
  - 稳健分桶：见 `params.diff_buckets`。  
- **PIT 切片原则**：该日该所是否接受市价、是否须保护限价、无板日是否可市价，一律按成交日当时规则。

### 3.1 oos_split 占位（拉数前冻结；禁 holdout 反调）

配置占位字段（数值待锁，先占位）：

- `oos_split.is_start` / `oos_split.is_end`：样本内（IS）起止交易日  
- `oos_split.holdout_start` / `oos_split.holdout_end`：样本外 / holdout 起止  

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调切日、四组定义、`far_mkt_mult`、`protect_limit_*`、显著性阈值或任何事后标定。切分一经写入 params 即冻结，不得因 IS 结果改 holdout 边界。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **L0 − L1/L2**：天真无限价相对沪/深诚实——废单率差、冲击/偏离差、（可选）净值差。  
2. **L3 − L1/L2**：现行沪市保护限价铺满相对 PIT——看深市无板日、沪市 `<2023-04-10` 是否被系统性错标。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "sz_no_limit_day",       # 深市无板日（L2 应废；L0/L3 易错成）
  "sh_main_pre_20230410",  # 沪市主板保护限价落地前
  "board_star",            # 科创板（开市起须保护限价）
  "board_chinext",         # 创业板（深市规则）
  "auction_session",       # 开盘/收盘集合竞价腿（应废）
  "far_mkt_1p00",          # far_mkt_mult=1.0
  "far_mkt_1p02_plus",     # far_mkt_mult∈{1.02,1.05,1.10}
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 废单率差 ΔFail（诚实通道拒单 / skip）；  
2. 成交价相对参考价/盘口偏离差 ΔDev（L0 用 high/low 多吃到的那截；无盘口则报 far_mkt 敏感性差）；  
3. 净值差 ΔNAV（L0−诚实、L3−诚实）——**可选**，有信号臂时才报，不得单独当「能买」证据。

**相对判据（草稿）**：若 |ΔFail| **≥ N** 或 |ΔDev| **≥ G** 或 |ΔNAV| **≥ Y**，记「市价通道执行鸿沟显著」。

**Y / G / N / Y2（拉数前写入 params；禁 holdout 标定）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| Y | 净值差显著门槛 | 拉数前写入 `params.Y` 并冻结 |
| G | 偏离/冲击差门槛 | 拉数前写入 `params.G` 并冻结 |
| N | 废单率/笔数差门槛 | 拉数前写入 `params.N` 并冻结 |
| Y2 | 稳健子窗净值差门槛（可选） | 拉数前写入 `params.Y2` 并冻结 |
| asof_check_date | 泄露组「现行」核对日 | **写死默认** `params.asof_check_date=2026-10-16`；拉数前冻结 |
| sh_protect_cut_date | 沪市主板保护限价落地 | **写死默认** `2023-04-10` |
| far_mkt_mult | 远市价敏感性列表 | **写死默认** `[1.0,1.02,1.05,1.10]`；拉数前冻结 |
| fill_time | 成交时点 | **写死** `next_open` |
| protect_limit_mode | 无字段时保护限价假设 | **写死** `default_pct` |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

**`params.Y` / `params.G` / `params.N` / `params.Y2` 写入冻结（本页占位槽已开；拉数前必须落入具体数）**：

```
# 拉数前在 IS 标定窗约定噪声带后写入具体数，一经写入即冻结
params.Y  = null   # 净值差显著门槛；拉数前替换为具体数并冻结
params.G  = null   # 偏离/冲击差门槛；拉数前替换为具体数并冻结
params.N  = null   # 废单率/笔数差门槛；拉数前替换为具体数并冻结
params.Y2 = null   # 稳健子窗净值差门槛（可选）；拉数前替换为具体数并冻结
```

门槛可在 **IS 标定窗**（非 holdout）内事先约定噪声带后写入；**禁止用 holdout / OOS 段标定或反调**。Y/G/N/Y2、`fill_time`、`far_mkt_mult`、`protect_limit_*` 开工拉数前必须落进 params 并冻结；**禁止跑后改口**。

**失败/不显著**：差异落在噪声带内——结论栏写明，不得改口称「市价通道无关」。

结论栏：空。跑完只写「该假设下差多少」，不写「这类票因市价能买/该规避」。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验市价申报通道 / 保护限价与交易所接受条件**，**不为组合策略放行实盘**。

- **显式豁免**：数值红线 v0（单票仓位、行业集中、回撤熔断等组合约束）**对本实验纸面/干跑豁免**——不因净值/IC 红线否决本机制对照。  
- **不豁免**：回测诚信（未复权、PIT 切日、禁 holdout 反调、禁荐股/禁当实盘预期、日频不假装精确吃档复盘、禁沪市规则抄深市）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **把沪市保护限价抄到深市**：与事实与坑明确冲突；L2 不得套 L1 的 protect 字段当深市主机条件。  
2. **深市无板日仍记市价成交**：L2 必须失败；记成则实验设定作废。  
3. **开盘/收盘集合竞价下市价当成交**：`auction_mkt_allowed=False`；违者失效。  
4. **融券腿市价**：`short_leg_mkt_allowed=False`；空头规则见 K，不进 L 主结论。  
5. **用复权 high/low**：一律未复权。  
6. **无盘口却报「精确吃档复盘」**：只允许 `far_mkt_sensitivity`；违者结论不可用。  
7. **与 I（限价笼子）混报主结论且不标注通道**：笼子≠市价保护限价。  
8. **沪市 `<2023-04-10` 进 L1 却套现行保护限价**：该段属 L3 泄露敏感，不是 L1。  
9. **宇宙泄露 / holdout 反调**：看完 OOS 再改切日、`far_mkt_mult` 或保护限价假设。  
10. **把差异写成选股/「这类票能买」**。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | |
| exchange (SH/SZ) | 市价规则路由 | **必填** |
| board / market | 科创/主板/创业 | 按日 PIT |
| open/high/low/close（未复权） | L0 极值路径；参考价 | |
| pre_close（未复权） | protect_ref 回退 | |
| is_no_limit_day 或可推导 | 深市无板拒市价 | **可与假设 G PIT 表共用** |
| session 标签（可选） | 集合竞价 vs 连续 | 无则日频默认当连续腿 + 另报 auction 诊断桶 |
| bid1/ask1/last（可选） | 增强盘口偏离 | **非纸面最小集**；无则 far_mkt_sensitivity |
| 投资者保护限价字段（可选） | 真保护限价 | 无则 `protect_limit_mode=default_pct` |
| 信号表（可选） | 选股臂 | 无信号可先跑「市价腿 × 通道标签」差 |
| 市价规则表 | 切日与接受条件 | 可用本页 §2.1 编码，不必新开数据商 |

**明确**：不依赖聚宽；**不要求新开盘口数据商**——日频未复权 OHLC + 交易所/板块 + G 无板表 + 本页规则表即可起步「远市价敏感性」。买卖一/真保护限价为增强项。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=L`，`groups=[L0,L1,L2,L3]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-16`**，**`params.sh_protect_cut_date=2023-04-10`**，**`params.sz_mkt_only_with_limit=True`**，**`params.auction_mkt_allowed=False`**，**`params.short_leg_mkt_allowed=False`**，**`params.protect_limit_mode=default_pct`**，**`params.protect_limit_pct_buy=1.02`**，**`params.protect_limit_pct_sell=0.98`**，**`params.protect_ref=last_or_preclose`**，**`params.day_freq_mode=far_mkt_sensitivity`**，**`params.far_mkt_mult=[1.0,1.02,1.05,1.10]`（写死默认；拉数前冻结）**，**`fill_time=next_open`（写死；不用 next_close）**，**`params.diff_buckets=[sz_no_limit_day,sh_main_pre_20230410,board_star,board_chinext,auction_session,far_mkt_1p00,far_mkt_1p02_plus]`（写死默认；拉数前冻结）**，**`params.Y` / `params.G` / `params.N` / `params.Y2`（占位槽已开；拉数前写入具体数并冻结；禁 holdout 标定）**，`universe_rule`，`date_start/date_end`（可空=待锁），`oos_split.{is_start,is_end,holdout_start,holdout_end}`（占位，禁 holdout 反调），`redline_v0_exempt=true`（仅本机制实验；见 §4.3），`overlay_G=on`（建议 on：无板表共用），`overlay_I=off|on`（默认 off；限价笼子分表），`overlay_K=off`（默认 off；融券另案），`overlay_A=off|on`（默认 off）。  
- 行情与规则表：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- L0/L1/L2/L3 废单率、偏离/远市价敏感性、（可选）净值；分桶（深市无板日 / 沪市切日前 / 科创 / 集合竞价 / far_mkt）。  
- 自检布尔：是否未复权；是否未把沪市保护限价抄深市；深市无板日是否废单；集合竞价是否废；融券市价是否废；`fill_time` 是否 `next_open`；无盘口是否仅 far_mkt_sensitivity；`far_mkt_mult`/保护限价参数是否已冻结；holdout 是否未反调；是否未与 I 混主表不标注。  
- **禁止输出**：具体买卖标的列表当「建议」；把天真无限价市价当实盘预期；催跑抢 A 真数队列。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` 一致：市价申报不是穿过整本档位的无限价；沪市要保护限价且只走连续竞价；深市无涨跌幅日不接受市价。与 `事实与坑.md` 2026-10-16 条一致：沪市 3.3.5/3.3.6；深市 3.3.5（无保护限价句）；科创开市起须保护限价；沪市主板保护限价与 2023-04-10 同日；禁集合竞价市价、禁融券市价、禁与周一限价笼子合成一句。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层对齐清单实验 L 已有假设；本页只把定义、样本、标签、失效条件与回测接口收成一页标准件，**不改口径主线**，**不改假设 A/D/E/F/G/H/I/J/K 正文**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；日频 OHLC + 交易所/板块 + G 无板表即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；oos_split 占位+禁 holdout 反调；红线 v0 机制豁免；asof_check_date=2026-10-16 / sh_protect_cut_date=2023-04-10 / sz_mkt_only_with_limit=True / auction_mkt_allowed=False / short_leg_mkt_allowed=False；**fill_time=next_open 写死**；**protect_limit_mode=default_pct** + pct 1.02/0.98；**day_freq_mode=far_mkt_sensitivity**；**far_mkt_mult=[1.0,1.02,1.05,1.10] 写死+拉数前冻结**；diff_buckets 七桶写死+拉数前冻结；**Y/G/N/Y2 占位槽已开、拉数前写入具体数并冻结、禁 holdout 标定** |

---

## 变更

- 2026-11-02：新建标准件（总管线：K 风控四条已交后继续可离线下一纸面；选型 L 优先于 B 消歧/C/M/N——清单定义清晰、可复用 G、日频不依赖新盘口商；机制类预埋 fail_policy/oos/红线豁免/params 冻结；**不抢实验 A**）。

