# 假设 AC · 北交所涨跌幅 / 盘后误套沪深（执行鸿沟）

更新：2026-11-02  
来源：总管线 / AB 补丁已交后并行写下一纸面 AC；清单原止于 AB，无 AC 节 → 自立实验 AC；选题自总管候选「北交所涨跌幅/交易时段」+ `事实与坑`「主板 ST 10% 切日后不要把北交所 30% 合成全市场 ST 都 10%；北交所股票 2026-07-06 盘后暂不实施；北交所经手费另档」+ `清单` 实验 M/X 旁路「北交所另桶」；与假设 X（主板 ST 5%→10%）/ M（盘后通道沪深主测）/ S（经手费）**分列**；**新建实验 AC**  
状态：**草稿 · 待数据 · 待跑**（结论栏空；禁止把「北交所按沪深 ±10%/±20% 标板 / 2026-07-06 北交所已有盘后 / 北交所经手费=沪深 0.0341‰」当诚实执行；不抢实验 A 真数队列；本页不开回测；不催 8765；**不改 Y/Z/AA/AB 及其他 A/D–AB 已交正文与冻结补丁**）

> 增量笔记。不荐股、不写买卖标的/仓位、不依赖聚宽真数、不跑回测结论。与 `口径.md` / `事实与坑.md` / `清单与配方.md` 对齐；清单原止于 AB，本页自立实验 AC 标准件。与假设 X（主板 ST/*ST 涨跌幅 PIT）**分列**：X 主测沪深主板风险警示 5%→10% 切日，并把 `bse_risk_warn_pct=0.30` **另桶不进主跑**；本页**主测**北交所宇宙被误套沪深 ±10%/±20%（或主板 ST 现行 10%）、以及把 **2026-07-06 盘后固定价格**写成北交所已开通。与假设 M（盘后补成交）**分列**：M 主测沪深盘后通道可用性 / 剩单自动进 15:05；本页只测「北交所误开盘后」腿，不重开科创/创业/主板扩围切日。与假设 S（经手费）**分列**：北交所 0.0125% 另档只作诊断桶对照声明，**不**重开沪深经手费主表。板上可成交属 A；新股无板窗属 G；费用四层属 S/T/U/V。**本页主结论不混。**

> **字母消歧（硬）**：本页**实验字母 AC** ≠ 费用/显著性参数 **`params.Y`**（相对门槛，与 G/N/Y2 同族）。全文凡写「实验 AC / 假设-AC / hypothesis_id=AC / 组 AC0·AC1·AC2」均指本实验；凡写 **`params.Y`** 均指相对门槛，**禁止**把二者混读或互改。亦**禁止**把实验字母 AC 与 params 键名 `ac0_*` 以外的单字母/双字母实验页混读。

---

## 1. 一句话假设（可检验、可证伪）

同一北交所股票宇宙、同一未复权价、同一 T+1 下，把涨跌幅按沪深主板 ±10% / 创业·科创 ±20%（或主板 ST 现行 ±10%）去标板，并把 **2026-07-06 起盘后固定价格**写成北交所已开通，相对「北交所风险警示/板上按事实口径 **30%** 另键；**2026-07-06 北交所盘后=off**」的 PIT 诚实组，会**系统性误标板上区间并发明盘后补成交路径**；差异应**集中在「涨跌幅误套沪深 / 盘后误开 / 对照诚实 30%+盘后 off」桶**，而不是随机散开。

证伪方向：若天真组 / 泄露组相对诚实组的板标签差异率、盘后假成交贡献差、失败笔数差在标定噪声带内可忽略，且「涨跌幅误套 / 盘后误开 / 经手费另档对照」分桶不改变结论（差异不集中在北交所误套相关桶），则本假设在该样本与执行设定下不成立。

---

## 2. 可编码概念 / 定义

### 2.1 北交所 ≠ 沪深抄写；涨跌幅 30% 另键；盘后 2026-07-06=off；经手费另档只诊断

```
# 配置写死键（见 §7；待风控预检后冻结补丁）
# 【消歧】params.Y = 显著性门槛；≠ 实验字母 AC
# params.asof_check_date                 写死默认 2026-10-09  # 与 X/G 同批「ST/涨跌幅」核对锚；盘后条款同向引用 2026-07-06 事实
# params.fill_time                        写死 next_open      # 成交腿与 A/D 对齐；本页主测北交所标板+盘后误开，不抢 A 板上真数
# params.tick                            写死 0.01           # A 股默认；北交所最小价位若另核则以 vendor 为准，缺→skip
# params.tag_cmp                         写死 ge_le
# params.round_half_up_to_tick           写死 True           # 板上价先取整（对齐 F）；本页不主测取整差
# params.bse_limit_pct_honest            写死 0.30           # 事实与坑「北交所 30%」；诚实组板上比例
# params.bse_aft_on_20260706             写死 False          # 新华社/中证报：北交所 7-6 暂不实施
# params.bse_aft_start                   写死 None           # leave_unsliced；启动日另行通知 → 本窗一律 off
# params.ac0_primary_demo                写死 copy_main_10pct  # 建议主报：把北交所按沪深主板 ±10% 标板；禁与 invent_aft_on 双挂争主表（待预检确认）
# params.ac0_limit_pct                   写死 0.10           # 天真主路径：沪深主板抄写
# params.ac0_invent_aft                  写死 True           # 天真可叠诊断：发明盘后已开（须进诊断桶；主报仍以 ac0_primary_demo 为准）
# params.ac1_limit_pct                   写死 0.20           # 半泄露：按创业/科创 20% 抄到北交所
# params.ac1_invent_aft                  写死 True           # 半泄露：盘后当已实施
# params.ac2_limit_pct                   写死 0.30           # PIT 诚实
# params.ac2_aft_on                      写死 False          # PIT：盘后 off
# params.merge_with_X_main_st            写死 False          # 主板 ST 切日另页 X
# params.merge_with_M_aft                写死 False          # 沪深盘后通道另页 M
# params.merge_with_S_fee                写死 False          # 经手费另页 S；北交所 0.0125% 只诊断
# params.merge_with_G_ipo_window         写死 False
# params.merge_with_A_fill               写死 False
# params.universe_rule                   写死 bse_only       # 主宇宙=北交所；沪深只作对照声明桶
# params.missing_bse_flag_policy         写死 skip           # 缺交易所/北交所标记 → skip
# params.px_basis                        写死 unadj
# params.diff_buckets                    写死默认桶名（§4.1）；拉数前冻结
# params.Y / G / N / Y2                  键名稳；建议 0.02/0.01/0.05/0.015；params.Y≠实验字母 AC；禁 null/holdout；待预检写死
# params.date_start / date_end           写死主窗并冻结
# params.oos_split.*                     写死四日期并冻结；禁 holdout 反调
# params.redline_v0_exempt_scope         写死 position_industry_dd_only

fill_time = "next_open"
asof_check_date = "2026-10-09"
bse_limit_pct_honest = 0.30
bse_aft_on_20260706 = False
bse_aft_start = None
ac0_primary_demo = "copy_main_10pct"  # 待预检冻结；禁双挂
ac0_limit_pct = 0.10
ac0_invent_aft = True
ac1_limit_pct = 0.20
ac1_invent_aft = True
ac2_limit_pct = 0.30
ac2_aft_on = False
merge_with_X_main_st = False
merge_with_M_aft = False
merge_with_S_fee = False
merge_with_G_ipo_window = False
merge_with_A_fill = False
universe_rule = "bse_only"
missing_bse_flag_policy = "skip"
px_basis = "unadj"

# 拉数前待风控补丁写死；草稿建议值如下（禁 holdout 标定）
Y = 0.02   # 相对门槛 ≠ 实验字母 AC
G = 0.01
N = 0.05
Y2 = 0.015

def limit_pct_for_group(group, is_risk_warn):
    """北交所板上比例：诚实组 30%；天真/泄露抄沪深。"""
    if group == "AC0":
        return ac0_limit_pct  # 0.10 主板抄写（主报）
    if group == "AC1":
        return ac1_limit_pct  # 0.20 创业/科创抄写
    return ac2_limit_pct      # 0.30 PIT

def aft_allowed(group, trade_date):
    """北交所盘后：诚实组本窗一律 off；天真/泄露可发明已开。"""
    if group == "AC2":
        return False
    if group == "AC0":
        return bool(ac0_invent_aft) and trade_date >= "2026-07-06"
    if group == "AC1":
        return bool(ac1_invent_aft) and trade_date >= "2026-07-06"
    return False
```

### 2.2 fail_policy（写死默认）

- 默认 **`fail_policy=skip`**：缺北交所/交易所标记、缺未复权前收盘却硬标板、把 X 主板 ST 切日 / M 沪深盘后主结论 / S 沪深经手费混进本页主表、用复权价判板、把北交所盘后写成 AC2 诚实已开 → **跳过该日该券执行腿**，不静默记成交。  
- 允许拉数前改为 `defer` 等，**必须写入 params 并冻结**；**禁止跑后/看完差异率再改口**。未写明则以 skip 为准。

### 2.3 对照组（本实验编码；自立实验 AC）

| 组 | 涨跌幅 / 盘后 | 说明 |
|----|----------------|------|
| AC0 天真 | 主板 ±10% 抄写（+可发明盘后，按 `ac0_primary_demo` 单一主报） | 把北交所当沪深主板 |
| AC1 半泄露 | 创业/科创 ±20% 抄写 + 盘后当已实施 | 板块默认误落北交所 |
| AC2 PIT 诚实 | ±30%；盘后=off（本窗） | 与事实与坑同向 |

同一信号、同一 T+1、同一北交所宇宙。本页**主测北交所误套沪深涨跌幅 + 盘后误开**，不主测主板 ST 切日（见 X）、不主测沪深盘后扩围（见 M）、不主测经手费档（见 S）。**`params.fill_time=next_open` 写死**。

**`params.merge_with_X_main_st=False` / `merge_with_M_aft=False` / `merge_with_S_fee=False` / `merge_with_G_ipo_window=False` / `merge_with_A_fill=False`（写死）**。

**待风控预检冻结（建议；禁 holdout 标定；禁 null；禁双挂）**：

```
params.Y                            = 0.02                 # 板标签/净值差显著门槛；≠实验字母 AC
params.G                            = 0.01                 # 盘后假成交桶相对对照差
params.N                            = 0.05                 # 失败/跳过率差门槛
params.Y2                           = 0.015                # AC1（20% 误套）相对 AC2 专项门槛
params.ac0_primary_demo             = copy_main_10pct      # 主报按主板 10% 抄写；禁与 invent_aft_on 双挂争主表
```

---

## 3. 样本区间

- **宇宙（默认）**：北交所股票（`universe_rule=bse_only`）。沪深主板/创业/科创只进「对照声明」桶，不进主跑。  
- **排除（默认）**：非北交所；缺交易所标记；用复权价；把 X/M/S/A 主结论并进本页主表。  
- **主窗（写死；拉数前冻结）**：  
  - `params.date_start=2021-11-15`（北交所开市后可交易窗；若数据更晚则以实际可取首日为准并写入 params）  
  - `params.date_end=2026-09-30`  
  - **覆盖 2026-07-06 盘后扩围日**（沪深已开、北交所仍 off——本页主测点）。  
- **PIT 切片原则**：北交所涨跌幅按事实口径 30% 另键；盘后以「2026-07-06 暂不实施、启动日另行通知」为准，**禁止**按沪深扩围回放为已开。

### 3.1 oos_split（写死四日期；拉数前冻结；禁 holdout 反调）

```
params.oos_split.is_start       = 2021-11-15
params.oos_split.is_end         = 2024-12-31
params.oos_split.holdout_start  = 2025-01-01
params.oos_split.holdout_end    = 2026-09-30
```

**硬规则**：holdout / OOS 段**只用于一次性报告**；**禁止**用 holdout 反调涨跌幅枚举、`ac0_primary_demo`、盘后开关、显著性门槛（含 **`params.Y`**）。切分一经写入 params 即冻结。

---

## 4. 标签 / 对照设计

### 4.1 主对比

1. **AC0 ? AC2**：主板 10% 抄写（±发明盘后）相对 PIT 30%+盘后 off——板上误标与假盘后。  
2. **AC1 ? AC2**：创业/科创 20% 抄写 + 盘后误开 相对 PIT。  
3. **分桶（须报；`params.diff_buckets` 写死默认名；拉数前冻结；禁 holdout 改桶）**：

```
params.diff_buckets = [
  "limit_copy_main_10",          # 按主板 10% 误套
  "limit_copy_chinext_star_20",  # 按创业/科创 20% 误套
  "aft_false_on_20260706",       # 盘后误开
  "honest_30_aft_off",           # 对照诚实
  "vs_X_main_st",                # 对照声明：主板 ST 另页 X
  "vs_M_sse_szse_aft",           # 对照声明：沪深盘后另页 M
  "vs_S_fee_bse_0125",           # 对照声明：经手费另档另页 S
  "vs_A_fill",                   # 对照声明：板上可成交另页 A
]
```

### 4.2 成功 / 失败判据（相对）

主指标：

1. 板标签差异率 ΔTag（AC0/AC1 相对 AC2）；  
2. 盘后假成交贡献差 ΔAftFake；  
3. （可选）腿净值差 ΔPnL；  
4. 跳过/废单笔数差 ΔFail。

**相对判据（草稿）**：若 |ΔTag| 或 |ΔPnL| **≥ params.Y** 或 |ΔAftFake| **≥ params.G** 或 |ΔTag_(AC1−AC2)| **≥ params.Y2** 或 |ΔFail| **≥ params.N**，记「北交所误套沪深执行鸿沟显著」。

**params.Y / G / N / Y2（键名稳；建议值待预检冻结；禁 holdout 标定；与实验字母 AC 无关）**

| 符号 | 含义（占位） | 规则 |
|------|--------------|------|
| params.Y | 板标签/净值差显著门槛（≠实验字母 AC） | **建议** `0.02`；待预检写死冻结 |
| params.G | 盘后假成交桶相对对照差 | **建议** `0.01` |
| params.N | 失败笔数率差门槛 | **建议** `0.05` |
| params.Y2 | AC1−AC2 专项门槛 | **建议** `0.015` |
| asof_check_date | 核对日锚点 | **写死默认** `2026-10-09` |
| fill_time | 成交时点 | **写死** `next_open` |
| bse_limit_pct_honest | 诚实涨跌幅 | **写死** `0.30` |
| bse_aft_on_20260706 | 诚实盘后 | **写死** `False` |
| ac0_primary_demo | 天真主报枚举 | **建议** `copy_main_10pct`（禁双挂；待预检） |
| diff_buckets | 分桶名 | 见 §4.1；拉数前冻结 |

门槛键名已写入 params；**具体数值待风控预检后冻结**；**禁止用 holdout / 事后显著性改口**；**`ac0_primary_demo` 单一主报，禁与 invent_aft_on 双挂争主表**。

**失败/不显著**：差异落在噪声带内或均匀散在非北交所误套对照桶——结论栏写明，不得改口称「北交所差不多能按沪深板回放」或「这类票更能买」。

结论栏：空。跑完只写「该假设下板标签/盘后假成交差多少」，不写选股公式。

### 4.3 数值红线 v0 豁免（本机制实验）

本实验**只验北交所执行诚信**，**不为交易策略放行实盘**。

- **显式豁免**：数值红线 v0 中单票仓位、行业集中、回撤熔断等组合约束（**`params.redline_v0_exempt_scope=position_industry_dd_only`**）**对本实验纸面/干跑豁免**。  
- **不豁免**：回测诚信（PIT 涨跌幅/盘后 off、禁 holdout 反调、禁荐股/禁当实盘预期）一律照做。  
- **不得沿用**：本豁免**不得**被组合策略或其他假设页拿去绕开红线 v0。

---

## 5. 预期失效条件

本假设或实验设定在下列情形下失效/须重切，不得硬套：

1. **用复权价判板**。  
2. **把 X 主板 ST 切日、M 沪深盘后主通道、S 沪深经手费重开混进本页主结论**。  
3. **把北交所盘后按沪深扩围写成 AC2 诚实已实施**。  
4. **把北交所诚实涨跌幅改成 10%/20% 却不改表述**。  
5. **缺北交所标记却静默当沪深主板回放**。  
6. **宇宙泄露 / holdout 反调**：看完 OOS 再改 `ac0_primary_demo` 或 **`params.Y` 等门槛**。  
7. **差异不集中在误套·盘后桶却仍写「系统性北交所执行鸿沟」而不改表述**。  
8. **把差异写成「这类票能买」或选股公式**。  
9. **把实验字母 AC 与 `params.Y` 混改**；或改写 Y/Z/AA/AB 及其他 A/D–AB 已冻正文。

---

## 6. 数据需求清单（字段级；不绑死供应商；优先不依赖新数据商）

| 字段 | 用途 | 备注 |
|------|------|------|
| trade_date, code | 键 | 北交所为主 |
| exchange / market | 北交所过滤 | 缺 → skip |
| unadj_preclose / unadj_close | 判板 | 禁复权 |
| is_risk_warn（可选） | 风险警示分桶 | 缺则整板按 30% 诚实键 |
| aft_fill_flag / aft_volume（可选） | 盘后误开诊断 | 无字段→只报通道可用性差 |
| fee_leg（可选） | vs S 对照声明 | 不进主结论 |

**明确**：不依赖聚宽；**不要求新开 Level-2**——有未复权前收/收盘 + 交易所标记即可起步；缺北交所标记 → `fail_policy=skip`。主窗自 2021-11-15（可按数据首日下调并冻进 params）。

---

## 7. 交给 [@量化-回测] 的接口说明

**输入期望**

- 配置块（写死项加粗）：`hypothesis_id=AC`（**实验字母**），`groups=[AC0,AC1,AC2]`，**`fail_policy=skip`（默认写死）**，**`params.asof_check_date=2026-10-09`**，**`params.fill_time=next_open`（写死）**，**`params.bse_limit_pct_honest=0.30`**，**`params.bse_aft_on_20260706=False`**，**`params.bse_aft_start=None`**，**`params.merge_with_X_main_st=False`**，**`params.merge_with_M_aft=False`**，**`params.merge_with_S_fee=False`**，**`params.merge_with_G_ipo_window=False`**，**`params.merge_with_A_fill=False`**，**`params.universe_rule=bse_only`**，**`params.missing_bse_flag_policy=skip`**，**`params.px_basis=unadj`**，**`params.redline_v0_exempt_scope=position_industry_dd_only`**，**`params.diff_buckets=[...]`（§4.1 写死默认；拉数前冻结）**，**`params.Y` / `G` / `N` / `Y2`（键名稳；建议 0.02/0.01/0.05/0.015；待预检冻结；禁 holdout；禁 null；params.Y≠实验字母 AC）**，**`params.ac0_primary_demo=copy_main_10pct`（建议；待预检；禁双挂）**，`universe_rule`，**`params.date_start=2021-11-15` / `params.date_end=2026-09-30`（写死）**，**`oos_split.{is_start=2021-11-15,is_end=2024-12-31,holdout_start=2025-01-01,holdout_end=2026-09-30}`（写死四日期；禁 holdout 反调）**，`redline_v0_exempt=true`（仅本机制实验；§4.3），`overlay_X=off`，`overlay_M=off`，`overlay_S=off`，`overlay_A=off`。  
- 字段：见 §6。  

**输出期望（结论栏仍空，由回测岗填）**

- AC0/AC1/AC2 板标签差异率、ΔTag、ΔAftFake、ΔFail；分桶（10% 误套 / 20% 误套 / 盘后误开 / vs X·M·S·A）。  
- 自检布尔：AC2 是否 30%+盘后 off；AC0 是否单一主报；AC1 是否 20%+盘后误开；是否未与 X/M/S/A 混主结论；holdout 是否未反调；**是否未把实验字母 AC 与 params.Y 混用**；**是否未改 Y/Z/AA/AB 冻结补丁正文**。  
- **禁止输出**：具体买卖标的列表当「建议」；把沪深板抄写当诚实 PIT；催跑抢 A 真数队列；催 8765。

**队列声明**：本页纸面就绪 ≠ 开工指令；**不抢实验 A 真数队列**；不催本机 8765 鉴权；不派回测开工；**本页不开回测**；**不改 Y/Z/AA/AB 及其他 A/D–AB 已交正文**。

---

## 8. 与口径是否冲突

**否。** 与 `口径.md` / `事实与坑.md` 一致：涨跌幅按板块×日子切片；北交所 30% 不要合成「全市场 ST 都 10%」；北交所 2026-07-06 盘后暂不实施；北交所经手费另档。阶段 0 只做可复现实验设计、不抢跑实盘结论。

表述层：清单原止于实验 AB，本页**新增实验 AC** 收成标准件，**不改口径主线**，**不改假设 A–AB 正文**。与实验 X/M/S 分工：**X=主板 ST 切日；M=沪深盘后通道；S=经手费；AC=北交所误套沪深涨跌幅 + 盘后误开**。

---

## 9. 状态

| 项 | 值 |
|----|----|
| 文档状态 | 草稿 |
| 数据 | 待接入（字段见 §6；未复权前收/收盘 + 北交所标记即可起步） |
| 回测 | 待跑（**不抢实验 A 真数队列**；不催 8765；不派回测；本页不开回测） |
| 结论栏 | （空） |
| 风控预埋 | fail_policy=skip；**主窗 date_start/end=2021-11-15..2026-09-30 写死**；**oos_split 四日期写死+禁 holdout 反调**；红线 v0 机制豁免（**`redline_v0_exempt_scope=position_industry_dd_only`**）；asof_check_date=2026-10-09；**fill_time=next_open 写死**；**bse_limit_pct_honest=0.30 / bse_aft_on_20260706=False 写死**；diff_buckets 八桶写死冻结；**Y/G/N/Y2 键名稳建议 0.02/0.01/0.05/0.015（待预检冻结；params.Y≠实验字母 AC）**；**ac0_primary_demo=copy_main_10pct 建议（禁双挂；待预检）** |

---

## 变更

- 2026-11-02：新建标准件（总管线：并行写下一纸面 AC；Y/Z/AA/AB 补丁已交不改；清单止于 AB → 自 `事实与坑`「北交所 30% / 盘后 7-6 暂不实施 / 经手费另档」+ 总管候选「北交所涨跌幅/交易时段」选题，**与 A/D–AB 不撞主结论**；近邻 X=主板 ST、M=沪深盘后、S=经手费，本页主测北交所误套；**实验字母 AC ≠ params.Y**；机制类预埋 fail_policy/oos/红线豁免/params 键；**不抢实验 A**；**不派回测**；**本页不开回测**；**不催 8765**；**不改 Y/Z/AA/AB/A/D–X 正文**）。
