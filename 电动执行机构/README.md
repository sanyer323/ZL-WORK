# 电动执行机构研发

对标 Rotork IQ3 Pro / AUMA SA，自研智能电动执行机构。  
**当前进度：Step 0–4。接口已冻结 F10 / φ20。下一步：Step 5 传感。**

| 步骤 | 文件 | 状态 |
|------|------|------|
| 0 | [00_研发路线.md](00_研发路线.md) | 决策已冻结 |
| 1 | [01_产品定义_EA10.md](01_产品定义_EA10.md) | 已冻结（F10 φ20） |
| 2 | [02_机电原理与定型计算.md](02_机电原理与定型计算.md) · [sim/sizing.py](sim/sizing.py) · [EA10_研发仿真工作台.html](EA10_研发仿真工作台.html) | 已交付 |
| 3 | [03_总成方案.md](03_总成方案.md) · [DXF/EA10_总成半剖.dxf](DXF/EA10_总成半剖.dxf) | 已交付 |
| 4 | [04_传动详细设计.md](04_传动详细设计.md) · [sim/drive.py](sim/drive.py) · [DXF/EA10_传动剖视.dxf](DXF/EA10_传动剖视.dxf) | 本轮交付 |
| — | [罗托克_奥玛_技术差异对比.md](罗托克_奥玛_技术差异对比.md) | 已完成 |

```bash
python3 sim/sizing.py
python3 sim/drive.py
python3 draw_EA10_assembly.py
python3 draw_EA10_drive.py
```
