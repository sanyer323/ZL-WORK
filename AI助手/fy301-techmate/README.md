# FY301 TechMate · M0 原型

**AI 智能调试手操器** — 把 FY301 现场调试、故障排查、FYCAL 标定知识做成可语音交互的向导。

## 运行

```bash
cd AI助手/fy301-techmate
python3 -m http.server 8766
```

Chrome/Edge 打开 **http://localhost:8766**

## 试用场景

1. 点 **「⚡ 带电拔霍尔」** — 模拟您昨天的现场故障  
2. 切 **「逐步向导」** — 8 步霍尔恢复 SOP  
3. 切 **「排查链」** — 工程师培训版五步法  

## 版本规划

| 版本 | 能力 |
|------|------|
| **M0**（当前） | FAQ + 向导 + 语音，无 HART |
| **M1** | 蓝牙 HART 读 PV/压电/Hall/报警码 |
| **M2** | Auto Setup / FYCAL 逐步联动 |

产品说明：[../FY301智能调试手操器.md](../FY301智能调试手操器.md)
