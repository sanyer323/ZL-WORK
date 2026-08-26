# FY301 Blender 增强层（P3）

目标：增强关键运动部件三维观感；支持 **可替换网格** + 真实照片板 + HUD；不改五段因果。

## 当前片段

| 段 | 运动 | 脚本 | 默认网格 stem |
|----|------|------|----------------|
| 01 | 压电盘弯曲 | `render_piezo_bend.py` | `piezo_disk` / `nozzle_body` |
| 02 | 喷嘴挡板→先导压 | `render_nozzle_flapper.py` | `restriction_tube` / `nozzle_body` / `flapper_disk` |
| 03 | 滑阀行程 | `render_spool_valve.py` | `sleeve` / `spool` / `diaphragm_*` |
| 04 | Hall 间隙反馈 | `render_hall_feedback.py` | `hall_housing` / `magnet_block` |

## 用真实 CAD 网格替换

1. 生成占位网格（仓库已可提交）：

```powershell
python blender\build_placeholder_meshes.py
```

2. 把你们的零件导出为同名文件，放到 `blender/meshes/`：
   - 支持：`.obj` `.stl` `.fbx` `.glb` `.gltf` `.ply`
   - 例如用真实压电底座替换 `piezo_disk.obj`

3. 再渲染：

```powershell
python render_blender_clips.py
python run_principle_pipeline.py --with-blender
```

## 本机渲染

```powershell
cd AI研发产品\研发仿真视频
pip install pillow
python blender\build_placeholder_meshes.py
python render_blender_clips.py --dry-run
python render_blender_clips.py
python check_default_deliverable.py
python run_principle_pipeline.py --with-blender
```

## 约束

1. 默认交付永远是 **原理讲解版**，不是工程师排故障版。  
2. 三维只加强动作与实物对照，不改手册因果。  
3. 有真实网格就替换同名文件；没有则用占位 OBJ / 原始几何回退。
