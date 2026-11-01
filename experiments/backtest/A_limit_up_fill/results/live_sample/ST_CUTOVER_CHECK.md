# ST 切日抽检 · 实验 A 真数门禁（模板）

- 实验：`A_limit_up_fill`
- 规则：`board_st_day_effective`；未复权 + 除权参考价；round half up 0.01
- 切日：主板 ST/*ST **2026-07-06** 前 5% → 当日及以后 10%
- 落盘目标：`results/live_sample/ST_CUTOVER_CHECK.md`（本模板复制后填真数）
- 状态：离线占位；**真数未到，勿填假结论**

## 样本 A · 切日前（期望 pct=0.05）

| 字段 | 值 |
|------|-----|
| code | （待填） |
| trade_date | （须 < 2026-07-06） |
| board / st_flag | |
| pre_close | |
| pct_used | 0.05 |
| limit_up | |
| limit_down | |
| open / high / low / close | |
| volume | |
| one_word_up / close_seal_up | |
| 判板依据 | 未复权；非复权价 |

## 样本 B · 切日及以后（期望 pct=0.10）

| 字段 | 值 |
|------|-----|
| code | （待填；宜同档或同证券） |
| trade_date | （须 ≥ 2026-07-06） |
| board / st_flag | |
| pre_close | |
| pct_used | 0.10 |
| limit_up | |
| limit_down | |
| open / high / low / close | |
| volume | |
| one_word_up / close_seal_up | |
| 判板依据 | 未复权；非复权价 |

## 结论

| 项 | 值 |
|----|-----|
| 切日前 5% 正确 | 待验 |
| 切日后 10% 正确 | 待验 |
| 未用复权判板 | 待验 |
| 门禁 | **未过**（真数未到） |

失败任一项 → 打回，不进真数 A0/A1 结论。
