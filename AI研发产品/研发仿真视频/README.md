# FY301 研发仿真视频包

基于 `FY301ME` 手册与 `SMAR_FY301_3D动画视频脚本.docx`，面向研发的**可计算仿真**（非营销三维宣传片）。

**Agent skill（正确做法说明书）：** [`.agents/skills/fy301-simulation-video/SKILL.md`](../../.agents/skills/fy301-simulation-video/SKILL.md)  
**对照缺口检查：** [`SKILL_GAP_CHECK.md`](./SKILL_GAP_CHECK.md)

资源校验（不渲染、不配音）：

```powershell
python verify_fycal_assets.py
python rebuild_fycal_manifest.py   # 如需按磁盘 PNG 重建相对路径 manifest
```

一键流水线（校验 → 缺仿真则渲染 → 合成原理讲解版）：

```powershell
python run_principle_pipeline.py
# 或
.\run_principle_pipeline.ps1

python run_principle_pipeline.py --verify-only
python run_principle_pipeline.py --force-sims
python run_principle_pipeline.py --with-blender
```

Blender 增强层（可选，P3：01 压电弯曲 / 03 滑阀）：

```powershell
python render_blender_clips.py --dry-run
python render_blender_clips.py
```

说明见 [`blender/README.md`](./blender/README.md)。有 `out/blender/` 对应片段时，合成会优先用三维片段。

分镜文案/旁白/角标请改：[`storyboard.json`](./storyboard.json)（不要再把长旁白写死在 Python 里）。

## 输出内容

### 原理讲解版（推荐：讲清楚怎么工作）
| 文件 | 说明 |
|------|------|
| `out/FY301_原理讲解版.mp4` | Excel 零件指认 → 原理动作 → **本段要点（机理）**；非排故障 |
| `out/FY301_原理讲解版.srt` | 字幕 |
| `旁白文案_原理讲解版.txt` | 旁白 |

```powershell
python build_principle_edition.py
```

### 故障排查口吻版（上一版，可作对照）
| 文件 | 说明 |
|------|------|
| `out/FY301_工程师培训版.mp4` | 偏「坏了查哪里」；若要原理请看上面的原理讲解版 |

### 研发原理讲解成片
| 文件 | 说明 |
|------|------|
| `out/FY301_研发原理讲解_完整版.mp4` | 章节片头 + 5 段拉长仿真 + **烧录字幕** + 旁白（若已跑 `add_sapi_voice.py`） |
| `out/FY301_研发原理讲解_软字幕.mp4` | 可开关字幕轨，便于后期 |
| `out/FY301_研发原理讲解.srt` | 中文字幕时间轴 |
| `旁白文案_完整版.txt` | 分镜旁白文案（可人工配音） |

生成：
```powershell
python build_master.py          # 拼接 + 字幕成片
python add_sapi_voice.py        # Windows 系统中文语音混音（可选）
```

### 互动仿真（推荐研发日常调参）
- `FY301_研发仿真工作台.html` — 浏览器打开即可
  - 调：压电电压、供气压力、节流孔、膜片面积比、死区、设定阀位
  - 看：间隙 / 先导压 / 滑阀 / OUT1·OUT2 / 阀位
  - 按钮：电压扫描、失电故障安全、FYCAL 标定点跳转

### 分镜仿真素材（`out/`）
| 文件 | 内容 |
|------|------|
| `01_压电陶瓷原理.mp4` | 晶格逆压电、盘弯曲、电容充放电、手册参数 |
| `02_喷嘴挡板先导级.mp4` | 节流孔分流、间隙→先导压、FYCAL 曲线 |
| `03_膜片放大与滑阀.mp4` | 力平衡放大、OUT1/OUT2、失电安全位 |
| `04_霍尔反馈与闭环.mp4` | 2–4 mm 磁间隙、PID 阶跃收敛 |
| `05_全系统闭环信号流.mp4` | 电–气–机全链路 |

## 生成视频

```powershell
cd "C:\Users\sanye\Desktop\SMAR\AI研发产品\研发仿真视频"
python render_sims.py
```

依赖：`matplotlib` `numpy` `imageio-ffmpeg`（脚本会找 ffmpeg）。

## 压电核心链路（研发一句话）

> **V↑ → 压电盘弯曲 → 挡板靠近喷嘴 → 先导室压力↑ → 大/小膜片力放大 → 滑阀位移 → OUT1/OUT2 差动 → Hall 反馈闭环**

关键手册数：驱动监控约 **30–70 V**；FYCAL@20 psi：**0 V≤2 / 50 V≈6 / 100 V≈12–13 psi**；回路最低 **3.8 mA**；压电近似电容故稳态近零功耗。
