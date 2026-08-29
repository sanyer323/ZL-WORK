# FY301 仿真视频流程：对照 `fy301-simulation-video` skill 缺口检查

对照文件：`.agents/skills/fy301-simulation-video/SKILL.md`  
检查对象：`AI研发产品/研发仿真视频/` 现有脚本、素材与成片链路  
日期：2026-08-28（P5 更新）

## 总评

**主链路已经打通，P0–P5 产线项已落地。**  
默认交付仍是原理讲解版；完整版 master 可选接入透明实物 B-roll + Blender 增强。

成熟度粗评：**原理讲解可交付约 92%；可复用产线约 92%；Blender 级观感约 75%（待本机 CAD 网格 + Blender 渲染）。**

---

## 缺口清单状态

| 阶段 | 内容 | 状态 |
|------|------|------|
| P0 | skill / manifest / 相对路径 | ✅ |
| P1 | 03–05 侧栏 + HUD | ✅ |
| P2 | storyboard + 一键 pipeline + 验收 | ✅ |
| P3 | Blender 01–04 + 可替换网格 | ✅ |
| P4 | Blender 05 + 审片门禁 | ✅ |
| P5 | 共享路径/字体、product_parts 接入 master、成片验收、parts_index 可移植 | ✅ |

---

## P5 新增（本轮）

1. **`fy301_common.py`** — `find_sim` / CJK 字体 / `probe_duration` / SKD 路径解析  
2. **`rebuild_parts_index.py`** — 从 `AI研发产品/SMAR SKD/` 重建相对路径索引  
3. **`check_principle_deliverable.py`** — 原理成片 mp4 时长、SRT 关键词（软门禁）  
4. **`build_master.py`** — 优先 Blender 仿真 + 各段前插入 `product_parts` B-roll（见 storyboard）  
5. **`render_product_parts.py`** — 去掉 Windows 绝对路径，走 `load_parts_index()`  
6. **`parts_index.json`** — 路径改为 `../SMAR SKD/...`  
7. **流水线** — `--with-product-parts` / `--build-master` / `--strict-deliverable`

---

## 持续项（需你本机）

1. 把真实 CAD 放入 `blender/meshes/` 同名替换后 `render_blender_clips.py`  
2. 确保 `AI研发产品/SMAR SKD/` 有照片后 `python rebuild_parts_index.py`  
3. 按 `REVIEW_CHECKLIST.md` 增量审片修补

---

## 结论

产线、门禁、master B-roll 挂钩已齐。观感差距主要在 **本机 Blender + 真实 CAD + SKD 照片渲染**。
