# FY301 Blender 增强层（P3）

目标：增强 **关键运动部件** 的三维观感，并把 **真实 FYCAL/零件照片 + HUD 角标** 放进同一镜头；不改五段因果与 `storyboard.json` 讲解结构。

## 当前片段

| 段 | 运动 | 脚本 | 输出 | 参考图 |
|----|------|------|------|--------|
| 01 | 压电盘弯曲 | `render_piezo_bend.py` | `out/blender/01_压电陶瓷原理.mp4` | FYCAL 清洁片/爆炸图 |
| 02 | 喷嘴挡板→先导压 | `render_nozzle_flapper.py` | `out/blender/02_喷嘴挡板先导级.mp4` | FYCAL 标定/供气 |
| 03 | 滑阀行程 | `render_spool_valve.py` | `out/blender/03_膜片放大与滑阀.mp4` | Excel 膜片/滑阀 |

合成时：若 `out/blender/` 下对应文件存在，`build_principle_edition.py` **优先**使用；否则回退 matplotlib。

## 本机渲染

要求：Blender **3.6+**（推荐 4.x）+ Python 依赖 `pillow`（用于烘焙 HUD 卡）。

```powershell
cd AI研发产品\研发仿真视频
pip install pillow

python render_blender_clips.py --dry-run
python render_blender_clips.py
python render_blender_clips.py --only 02
python render_blender_clips.py --blender "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe"

python run_principle_pipeline.py --with-blender
```

## 约束

1. 不改旁白因果；三维只加强“看得见的动作 + 实物对照”。
2. 先 procedural 动作几何，再用真实照片板对照；有 CAD 网格后再替换。
3. 导出 1280×720，便于与现有分屏合成对齐。
4. 禁止为了炫改写手册数据或讲解顺序。
