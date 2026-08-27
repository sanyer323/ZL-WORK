# FY301 仿真视频流程：对照 `fy301-simulation-video` skill 缺口检查

对照文件：`.agents/skills/fy301-simulation-video/SKILL.md`  
检查对象：`AI研发产品/研发仿真视频/` 现有脚本、素材与成片链路  
日期：2026-08-27（P4 更新）

## 总评

**主链路已经打通，skill 里大部分「正确做法」你们已经在用。**  
P0–P3 产线项已落地；P4 补齐 05 段 Blender 与审片门禁。

成熟度粗评：**原理讲解可交付约 90%；可复用产线约 88%；Blender 级观感约 75%（01–05 可渲，网格可替换，真实 CAD 待你放入 meshes/）。**

---

## 已具备（对齐 skill，可保留）

| Skill 要求 | 现状 | 证据 |
|------------|------|------|
| 五段因果链 | 有 | `01`–`05` mp4 + `render_sims.py` |
| 每段一件事 + takeaway | 有 | `storyboard.json` + `build_principle_edition.py` |
| 手册关键数据进旁白 | 有 | 旁白 + HUD；`check_review_gate.py` 门禁 |
| 左仿真右实物 | 有 | FYCAL / Excel 零件分屏 |
| 零件指认 | 有 | `out/_excel_parts` |
| 原理版 vs 排故障版分工 | 有 | 默认交付门禁 |
| 合成 / 字幕 / 配音脚本 | 有 | `build_master.py`、`add_sapi_voice.py` |
| 互动调参台 | 有 | `FY301_研发仿真工作台.html` |
| 文档入口 | 有 | `README.md` |
| 审片清单 | 有 | `REVIEW_CHECKLIST.md` + 自动门禁 |

---

## 缺口清单（按优先级）

### P0 — 影响正确性 / 可复现

1. **正式 skill 原先缺失** — ✅  
2. **图片引用名与 manifest 不一致** — ✅  
3. **FYCAL 图路径写死本机绝对路径** — ✅  

### P1 — 影响「原理 + 爆炸图」完整度

4. **03–05 段实物/爆炸图偏弱** — ✅  
5. **01–02 的 `parts` 为空** — 仍主要靠 FYCAL 图（足够）  
6. **关键数据多在旁白，少在画面角标** — ✅ HUD + 审片门禁  

### P2 — 影响产线效率

7. **独立分镜表** — ✅ `storyboard.json`  
8. **一键流水线** — ✅ `run_principle_pipeline.py`  
9. **自动验收** — ✅ `verify_fycal_assets.py` + `check_review_gate.py`（SRT 软检查）  
10. **CJK 字体** — 部分缓解（Windows 雅黑 / Linux 文泉驿回退）

### P3 — 「国外片那种观感」运动部件

11. **Blender 01–04** — ✅ 压电 / 先导 / 滑阀 / Hall + 可替换网格  

### P4 — 全链路三维 + 审片固化（本轮）

12. **Blender 05 全系统信号流** — ✅ `render_signal_flow.py` + `pcb_board` / `pneumatic_block` / `actuator_hint`  
13. **审片缺陷清单 + 门禁** — ✅ `REVIEW_CHECKLIST.md` + `check_review_gate.py`（流水线 verify 会跑）  
14. **产品部件透明动作台并入主片** — 仍独立（`render_product_parts.py` / HTML）；05 段照片板 + 网格部分吸收实物对照  
15. **默认交付门禁** — ✅ `check_default_deliverable.py`（已含 05 网格）

---

## 对照 skill「标准流程」逐步打分

| 步骤 | 状态 | 说明 |
|------|------|------|
| 1. 写清总因果链 | ✅ | README + 笔记 + 五段标题 |
| 2. 齐手册数与图 | ✅ | 数进分镜；图相对路径 + verify |
| 3. 写分镜再渲染 | ✅ | `storyboard.json` |
| 4. `render_sims` | ✅ | 五段 mp4；可选 Blender 01–05 |
| 5. `build_principle_edition` | ✅ | 侧栏 + HUD + 优先 blender 片段 |
| 6. master / 配音 | ✅ | 脚本与成片在 |
| 7. 人工审片清单 | ✅ | `REVIEW_CHECKLIST.md` + 自动门禁 |

---

## 建议落地顺序（不改叙事，只补产线）

1. ~~P0–P2 产线~~ ✅  
2. ~~P3：01–04 Blender~~ ✅  
3. ~~P4：05 全链路 + 审片门禁~~ ✅  
4. **持续**：把真实 CAD 丢进 `blender/meshes/` 同名替换；按 `REVIEW_CHECKLIST.md` 增量修；禁止无缺陷清单全盘重写。  
5. **可选**：把 `product_parts` 透明台选镜头挂进完整版 master（非默认原理片主线）。

---

## 结论

- **不是不会做 FY301 原理片**——现有原理讲解版已经按正确因果在做。  
- **产线与审片门禁已齐**；观感差距主要在 **你本机用真实 CAD 替换占位网格并渲 Blender**。  
- 补三维时仍应服从本 skill，避免重做成宣传片。
