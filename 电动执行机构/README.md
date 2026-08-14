# 电动执行机构研发

对标 Rotork IQ3 Pro / AUMA SA。  
**方案已全部写完（Step 0–9）。人要干的活见 [10_你现在该做什么.md](10_你现在该做什么.md)。**

| 步骤 | 文件 | 状态 |
|------|------|------|
| 0 | [00_研发路线.md](00_研发路线.md) | 完成 |
| 1 | [01_产品定义_EA10.md](01_产品定义_EA10.md) | 完成 |
| 2 | [02_机电原理与定型计算.md](02_机电原理与定型计算.md) · [sim/sizing.py](sim/sizing.py) | 完成 |
| 3 | [03_总成方案.md](03_总成方案.md) · [DXF/EA10_总成半剖.dxf](DXF/EA10_总成半剖.dxf) | 完成 |
| 4 | [04_传动详细设计.md](04_传动详细设计.md) · [sim/drive.py](sim/drive.py) | 完成 |
| 5 | [05_传感方案.md](05_传感方案.md) · [sim/sense.py](sim/sense.py) | 完成 |
| 6 | [06_控制电子.md](06_控制电子.md) · [EA10_控制电子框图.html](EA10_控制电子框图.html) | 完成 |
| 7 | [07_固件最小集.md](07_固件最小集.md) · [fw/](fw/) · [sim/fsm.py](sim/fsm.py) | 完成 |
| 8 | [08_机加与密封.md](08_机加与密封.md) | 完成 |
| 9 | [09_样机BOM与试验.md](09_样机BOM与试验.md) | 完成 |
| — | [10_你现在该做什么.md](10_你现在该做什么.md) | 交接 |
| — | [罗托克_奥玛_技术差异对比.md](罗托克_奥玛_技术差异对比.md) | 完成 |

```bash
python3 sim/sizing.py && python3 sim/drive.py && python3 sim/sense.py && python3 sim/fsm.py
```
