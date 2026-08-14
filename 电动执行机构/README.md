# 电动执行机构研发

对标 Rotork IQ3 Pro / AUMA SA。  
**当前：Step 0–5 完成。下一步 Step 6 控制电子。**

| 步骤 | 文件 | 状态 |
|------|------|------|
| 0 | [00_研发路线.md](00_研发路线.md) | 完成 |
| 1 | [01_产品定义_EA10.md](01_产品定义_EA10.md) | 完成（F10 φ20） |
| 2 | [02_机电原理与定型计算.md](02_机电原理与定型计算.md) · [sim/sizing.py](sim/sizing.py) · [EA10_研发仿真工作台.html](EA10_研发仿真工作台.html) | 完成 |
| 3 | [03_总成方案.md](03_总成方案.md) · [DXF/EA10_总成半剖.dxf](DXF/EA10_总成半剖.dxf) | 完成 |
| 4 | [04_传动详细设计.md](04_传动详细设计.md) · [sim/drive.py](sim/drive.py) · [DXF/EA10_传动剖视.dxf](DXF/EA10_传动剖视.dxf) | 完成 |
| 5 | [05_传感方案.md](05_传感方案.md) · [sim/sense.py](sim/sense.py) · [DXF/EA10_传感布置.dxf](DXF/EA10_传感布置.dxf) | 完成 |
| 6–9 | 电子 / 固件 / 机加详图 / 样机 | 未做 |
| — | [罗托克_奥玛_技术差异对比.md](罗托克_奥玛_技术差异对比.md) | 完成 |
| — | [99_本阶段完成与缺项.md](99_本阶段完成与缺项.md) | 总清单 |

```bash
python3 sim/sizing.py
python3 sim/drive.py
python3 sim/sense.py
python3 draw_EA10_assembly.py
python3 draw_EA10_drive.py
python3 draw_EA10_sense.py
```
