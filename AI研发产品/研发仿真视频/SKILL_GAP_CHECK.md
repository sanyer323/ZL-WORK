# FY301 仿真视频流程：对照 `fy301-simulation-video` skill 缺口检查

对照文件：`.agents/skills/fy301-simulation-video/SKILL.md`  
检查对象：`AI研发产品/研发仿真视频/` 现有脚本、素材与成片链路  
日期：2026-08-26

## 总评

**主链路已经打通，skill 里大部分「正确做法」你们已经在用。**  
缺口主要在：流程尚未写成 skill、资源可移植性、后段实物绑定、高保真三维未产品化、缺少一键验收。

成熟度粗评：**原理讲解可交付约 80%；可复用产线约 60%；Blender 级观感约 30%。**

---

## 已具备（对齐 skill，可保留）

| Skill 要求 | 现状 | 证据 |
|------------|------|------|
| 五段因果链 | 有 | `01`–`05` mp4 + `render_sims.py` |
| 每段一件事 + takeaway | 有 | `build_principle_edition.py` → `SEGMENTS` |
| 手册关键数据进旁白 | 有 | `旁白文案_原理讲解版.txt`、笔记/FYCAL 摘录 |
| 左仿真右实物（前段） | 有 | 01/02 使用 `_fycal_figs` |
| 零件指认 | 部分有 | Excel `out/_excel_parts`，03–05 用到膜片/滑阀/Hall 等 |
| 原理版 vs 排故障版分工 | 有 | `build_principle_edition.py` vs `build_engineer_edition*.py` |
| 合成 / 字幕 / 配音脚本 | 有 | `build_master.py`、`add_sapi_voice.py` |
| 互动调参台 | 有 | `FY301_研发仿真工作台.html` |
| 文档入口 | 有 | `README.md` |

---

## 缺口清单（按优先级）

### P0 — 影响正确性 / 可复现

1. **正式 skill 原先缺失**  
   - 状态：本次已补 `.agents/skills/fy301-simulation-video/SKILL.md`  
   - 作用：把「喂养出来的正确做法」固化，避免每次从零教。

2. **图片引用名与 manifest 不一致**  
   - 代码：`build_principle_edition.py` 引用 `fig14_piezo_base_labeled.png`  
   - 资源：`out/_fycal_figs/_named/manifest.json` 实际为 `fig14_piezo_on_fycal` 等  
   - 风险：换机重跑或清缓存后 01 段右栏缺图/报错。

3. **FYCAL 图路径写死本机绝对路径**  
   - `manifest.json` 内含 `C:\\Users\\sanye\\Desktop\\SMAR\\...`  
   - 风险：云端/其他电脑无法直接合成；应改为相对 `out/_fycal_figs/_named/`。

### P1 — 影响「原理 + 爆炸图」完整度

4. **03–05 段实物/爆炸图偏弱**  
   - `fycal_imgs` 在 03–05 为空，主要靠少量 Excel 零件  
   - Skill 要求后段仍尽量「动作 + 零件 + 数据」三件套  
   - 建议：为膜片/滑阀/Hall/线路板补分屏照片或爆炸指认节拍。

5. **01–02 的 `parts` 为空**  
   - 压电相关主要靠 FYCAL 图，未挂 Excel 零件别名  
   - 建议：把「压电片/盔帽/底座」与 `parts_index` / Excel 标签对齐，避免两套命名。

6. **关键数据多在旁白，少在画面角标**  
   - Skill 允许旁白或画面；审片时工程师更容易漏听数字  
   - 建议：FYCAL 三点、30–70 V、3.8 mA、2–4 mm 做持久角标。

### P2 — 影响产线效率

7. **分镜锁在 Python 里，没有独立分镜表**  
   - `SEGMENTS` 同时含旁白、照片节拍、takeaway  
   - 改文案要改代码；建议抽 `storyboard.json`（或 YAML）供非程序员改旁白。

8. **无一键流水线入口**  
   - 需依次跑 `render_sims` → `build_principle_edition` →（可选）`build_master` / `add_sapi_voice`  
   - 建议：`run_principle_pipeline.py` 或 Makefile/ps1，带「是否重渲仿真」开关。

9. **无自动验收脚本**  
   - Skill 有验收标准，仓库无 checklist 自动化  
   - 建议：检查五段文件存在、关键数字是否出现在旁白/字幕、引用图片是否都在磁盘上。

10. **CJK 字体依赖 Windows 字体名**  
    - 换 Linux/云端易方框字；需字体回退或捆绑开源中文字体。

### P3 — 影响「国外片那种观感」

11. **主视觉仍是 matplotlib 2D，不是 Blender 产线**  
    - 脚本原文已提到 Blender/Three.js/COMSOL，但未接入当前默认合成  
    - 与 skill 一致：三维是增强层；要追观感需单独立项「运动部件 Blender 素材 → 仍按五段合成」。

12. **产品部件透明动作台未并入主片**  
    - 有 `FY301_产品部件透明动作台.html`、`render_product_parts.py`  
    - 与原理讲解版默认成片仍是两条线，未统一分镜。

13. **工程师版与原理版并存，缺少「默认交付」强提示以外的门禁**  
    - README 已推荐原理版；可在 skill/流水线默认只发布原理版产物名，避免误发排故障口吻片。

---

## 对照 skill「标准流程」逐步打分

| 步骤 | 状态 | 说明 |
|------|------|------|
| 1. 写清总因果链 | ✅ | README + 笔记 + 五段标题 |
| 2. 齐手册数与图 | ⚠️ | 数较齐；图路径/文件名有坑 |
| 3. 写分镜再渲染 | ⚠️ | 有分镜，但嵌在代码中 |
| 4. `render_sims` | ✅ | 五段 mp4 已存在 |
| 5. `build_principle_edition` | ⚠️ | 能出片；P0 资源一致性待修 |
| 6. master / 配音 | ✅ | 脚本与成片在 |
| 7. 人工审片清单 | ❌ | 无固定缺陷清单文件/门禁 |

---

## 建议落地顺序（不改叙事，只补产线）

1. **立刻**：统一 Fig.14 文件名；manifest 改相对路径。  
2. **短期**：03–05 补零件/照片分屏；关键数画面角标。  
3. **短期**：抽出 `storyboard.json` + 一键 pipeline + 资源存在性检查。  
4. **中期**：选定 1–2 个运动部件进 Blender，导出后仍走同一五段合成。  
5. **持续**：按 skill 审片模板迭代，禁止无缺陷清单的全盘重写。

---

## 结论

- **不是不会做 FY301 原理片**——现有原理讲解版已经按正确因果在做。  
- **缺的是 skill 固化 + 资源可移植 + 后段三件套补强 + 验收/一键化**。  
- 若目标是「更像国外三维演示」，缺口在 **Blender 素材层**，不在五段机理；补三维时仍应服从本 skill，避免重做成宣传片。
