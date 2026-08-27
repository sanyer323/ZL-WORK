# FY301 原理讲解版 · 审片缺陷清单

对照 skill：`.agents/skills/fy301-simulation-video/SKILL.md`  
规则：**只修本清单勾出的项**，禁止无缺陷清单全盘重写。

自动门禁（关键数据是否进分镜）：

```powershell
python check_review_gate.py
```

流水线 `run_principle_pipeline.py` 的 verify 阶段会跑该门禁。

---

## 本轮审片（复制一份改日期）

- 日期：
- 成片：`out/FY301_原理讲解版.mp4`
- 审片人：

### 必须过关

- [ ] 工程师能复述完整电–气–机闭环
- [ ] 01 压电 / 02 先导 / 03 滑阀 / 04 Hall 四段可单独看懂
- [ ] 关键手册数据均出现在旁白或画面（见下表）
- [ ] 爆炸图/零件图与讲解一一对应，无张冠李戴
- [ ] 默认成片是原理片，不是广告片/排故障片
- [ ] 每段结束有清晰 takeaway
- [ ] 旁白说完再切（无明显抢切）

### 关键手册数据核对

| 项 | 过？ | 备注 |
|----|------|------|
| 0–100 Vdc | [ ] | |
| 目标 ~50 V / 正常 30–70 V | [ ] | |
| FYCAL @20 psi | [ ] | |
| 0 V ≤2 / 50 V≈5.8–6.2 / 100 V≈12–13 | [ ] | |
| Hall 间隙 2–4 mm | [ ] | |
| 环路 ~3.8 mA | [ ] | |

### 分段缺陷（增量修补用）

- [ ] 01 —
- [ ] 02 —
- [ ] 03 —
- [ ] 04 —
- [ ] 05 —
- [ ] 字幕/配音 —
- [ ] Blender 增强（可选）—

### 修完后

```powershell
python verify_fycal_assets.py
python check_review_gate.py
python run_principle_pipeline.py
# 若本机有 Blender 且要三维增强：
python run_principle_pipeline.py --with-blender
```
