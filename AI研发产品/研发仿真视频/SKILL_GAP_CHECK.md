# FY301 仿真视频流程：对照 `fy301-simulation-video` skill 缺口检查

对照文件：`.agents/skills/fy301-simulation-video/SKILL.md`  
检查对象：`AI研发产品/研发仿真视频/` 现有脚本、素材与成片链路  
日期：2026-08-26

## 总评

**主链路已经打通，skill 里大部分「正确做法」你们已经在用。**  
缺口主要在：流程尚未写成 skill、资源可移植性、后段实物绑定、高保真三维未产品化、缺少一键验收。

成熟度粗评：**原理讲解可交付约 85%；可复用产线约 80%；Blender 级观感约 65%（01–04 可渲，网格可替换，真实 CAD 待你放入 meshes/）。**

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
   - 状态：✅ 已补 `.agents/skills/fy301-simulation-video/SKILL.md`

2. **图片引用名与 manifest 不一致**  
   - 状态：✅ 已修  
   - `fig14_piezo_base_labeled.png` 已在磁盘且已写入 `out/_fycal_figs/_named/manifest.json`  
   - `build_principle_edition.py` 启动前校验 SEGMENTS 引用均在 manifest 中

3. **FYCAL 图路径写死本机绝对路径**  
   - 状态：✅ 已修  
   - manifest 改为相对文件名；可用 `python rebuild_fycal_manifest.py` 重建  
   - 校验：`python verify_fycal_assets.py`

### P1 — 影响「原理 + 爆炸图」完整度

4. **03–05 段实物/爆炸图偏弱**  
   - 状态：✅ 已修  
   - 03/04/05 改为与 01/02 相同的「左仿真 + 右实物栏」：膜片/滑阀/Hall/线路板等 Excel 零件分屏  
   - `side_images()` 统一 FYCAL 图与零件图来源

5. **01–02 的 `parts` 为空**  
   - 状态：仍主要靠 FYCAL 图（足够）；未强制挂 Excel 别名  
   - 02 已补第三张 `fig10_supply_piezo.png` 强化侧栏

6. **关键数据多在旁白，少在画面角标**  
   - 状态：✅ 已修  
   - 各段增加 `hud` 角标，经 `burn_hud()` 烧到原理镜头左上角  
   - 例：`0–100 V` / `FYCAL @20 psi` / `Hall 间隙 2–4 mm` / `环路 ~3.8 mA`

### P2 — 影响产线效率

7. **分镜锁在 Python 里，没有独立分镜表**  
   - 状态：✅ 已修 → [`storyboard.json`](./storyboard.json)  
   - `build_principle_edition.py` 经 `load_segments()` 读取

8. **无一键流水线入口**  
   - 状态：✅ 已修 → `run_principle_pipeline.py` / `run_principle_pipeline.ps1`  
   - 默认：verify →（缺则）render_sims → build_principle_edition

9. **无自动验收脚本**  
   - 状态：✅ 基础版已有 → `verify_fycal_assets.py`（storyboard + 侧栏 + HUD + 相对路径）  
   - 仍可增强：成片时长/字幕关键字抽检

10. **CJK 字体依赖 Windows 字体名**  
    - 状态：部分缓解（build 已加 Linux Noto/文泉驿回退）；云端仍建议捆绑字体

### P3 — 影响「国外片那种观感」

11. **主视觉仍是 matplotlib 2D，不是 Blender 产线**  
   - 状态：✅ P3 深化（01–04 可选增强 + 可替换网格包）  
   - `blender/meshes/` 占位 OBJ；同名替换即可导入真实 CAD  
   - 动作 + 真实照片板 + HUD；合成优先 `out/blender/<sim>`

12. **产品部件透明动作台未并入主片**  
    - 状态：仍独立（`render_product_parts.py` / HTML 工作台）  
    - Blender 段已用零件照片板部分吸收“实物对照”需求

13. **工程师版与原理版并存**  
    - 状态：✅ 门禁 → `check_default_deliverable.py`（流水线 verify 会跑）  
    - 默认交付必须是原理讲解版

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

1. ~~立刻：统一 Fig.14 文件名；manifest 改相对路径。~~ ✅  
2. ~~短期：03–05 补零件/照片分屏；关键数画面角标。~~ ✅  
3. ~~短期：抽出 `storyboard.json` + 一键 pipeline + 资源存在性检查。~~ ✅  
4. ~~中期：选定 1–2 个运动部件进 Blender，导出后仍走同一五段合成。~~ ✅（01–04 + meshes 可替换）  
5. **持续**：把真实 CAD 网格丢进 `blender/meshes/` 同名替换；按 skill 审片；禁止无缺陷清单全盘重写。

---

## 结论

- **不是不会做 FY301 原理片**——现有原理讲解版已经按正确因果在做。  
- **缺的是 skill 固化 + 资源可移植 + 后段三件套补强 + 验收/一键化**。  
- 若目标是「更像国外三维演示」，缺口在 **Blender 素材层**，不在五段机理；补三维时仍应服从本 skill，避免重做成宣传片。
