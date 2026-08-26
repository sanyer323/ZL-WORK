# FY301 Blender 增强层（P3）

目标：只增强 **1–2 个运动部件** 的三维观感，不改五段因果与 `storyboard.json` 讲解结构。

## 先做哪两段

| 段 | 运动 | 脚本 | 输出 |
|----|------|------|------|
| 01 | 压电盘弯曲 | `render_piezo_bend.py` | `out/blender/01_压电陶瓷原理.mp4` |
| 03 | 滑阀行程 | `render_spool_valve.py` | `out/blender/03_膜片放大与滑阀.mp4` |

合成时：若 `out/blender/` 下对应文件存在，`build_principle_edition.py` **优先**使用它；否则回退 matplotlib 的 `out/01_*.mp4`。

## 本机渲染

要求：Blender **3.6+**（推荐 4.x），并可用命令行。

```powershell
cd AI研发产品\研发仿真视频

# 只检查能否找到 Blender / 脚本
python render_blender_clips.py --dry-run

# 渲染 01 + 03
python render_blender_clips.py

# 指定 Blender 路径
python render_blender_clips.py --blender "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe"

# 只渲一段
python render_blender_clips.py --only 01
```

或直接：

```powershell
blender --background --python blender\render_piezo_bend.py -- --out out\blender\01_压电陶瓷原理.mp4
blender --background --python blender\render_spool_valve.py -- --out out\blender\03_膜片放大与滑阀.mp4
```

然后走原流水线：

```powershell
python run_principle_pipeline.py --with-blender
```

## 约束（服从 fy301-simulation-video skill）

1. 不改旁白因果；三维只加强“看得见的动作”。
2. 先 procedural 占位几何，再逐步替换为真实拆解网格。
3. 导出分辨率建议 1280×720，便于与现有分屏合成对齐。
4. 禁止为了炫改写手册数据或讲解顺序。
