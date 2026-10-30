# HART 主机 · FY301 第一台（再扩 DD）

目标：电脑 + USB HART modem + **一台 FY301**，用中文命令读写现场仪表。  
打通这一台之后，扩展其它品牌 = 换/加 DD（或再学一张设备表），主机栈不用重写。

```
你（中文） → CLI/AI 意图  →  HART 帧  →  USB modem  →  FY301
                              ↑
                     先：通用命令 0/1/2/3
                     再：对着实机把 FY301 专用命令填进 fy301_learned.json
                     后：接 DD/EDD 引擎覆盖全库
```

---

## 1. 你买 modem 时怎么选

FY301 是 **两线 4–20 mA 回路供电**。电脑侧 modem 只负责 FSK，**通常不给仪表供电**。

| 方案 | 适合 | 备注 |
|------|------|------|
| **USB HART + 本安隔离**（如 ProComSol HM-USB-ISO） | 仪表已在 24 V + 250 Ω 回路上 | 开发最常见 |
| **USB HART 带回路供电**（Viator USB PowerXpress 一类） | 实验台只有 FY301、没有 24 V 源 | 一台 USB 搞定供电+通信 |
| SMAR **HI331** 蓝牙 | 已有 SMAR 生态 | 也是虚拟串口，本仓库同样走 COM |

**实验台最少接线（无带电 PowerXpress 时）：**

```
24V+ ── FY301(+) ── FY301(-) ── 250Ω ── 24V-
                    │              │
                    └── modem 夹在电阻两端或 COMM 端子（手册通信端子）
```

- 回路电阻 **≥ 250 Ω**，否则常报 No Device  
- modem 并在回路上，极性一般无所谓  
- FY301 等效阻抗约 **550 Ω**，供电要留足压降  

到货后请记下：**品牌型号、Windows 分配的 COM 号**。发给我，我按实机改串口参数（多数 USB HART 为 **1200 8O1**）。

---

## 2. 软件（本目录）

```bash
cd AI助手/hart-host
pip install -r requirements.txt

# 无 modem：只练意图解析
python cli.py --dry-run say "读压电电压"

# 有 modem：探测（Command 0）
python cli.py --port COM5 poll
python cli.py --port COM5 read
python cli.py --port COM5 say "读阀门位置"
```

**写操作默认关闭。** 需要改参数时显式 `--write`，避免误动现场。

会话记录写到 `learn_log/`（已 gitignore），把日志贴回来就能继续填 `devices/fy301_learned.json`。

---

## 3. 训练我（对着这一台 FY301）

建议顺序，每步把 **CLI 输出全文**发我：

| 步 | 命令 | 我们要得到什么 |
|----|------|----------------|
| 1 | `poll` | 厂家 ID、设备类型、短/长地址（Command 0） |
| 2 | `read` | PV / 电流 / 四变量（Cmd 1,2,3） |
| 3 | 你在 Trex/原厂软件里读「压电电压」「霍尔值」 | 对照我们 probe 到的设备变量 |
| 4 | `probe` 扫常用命令号 | 填进 `fy301_learned.json` |
| 5 | 中文：`say "读压电电压"` | 意图 → 已学会的命令 |

手册写明：监控里选 **霍尔值** 与 **压电电压**；压电 **30–70 V**；霍尔原始值大约 **26000–38000**。专用命令在 SMAR《HART Command Specification - FY301》里，没有纸质手册时就用第 3–4 步对着实机学。

---

## 4. 和「所有 HART 产品」的关系

| 阶段 | 覆盖 |
|------|------|
| **现在** | FY301：通用 HART + 实机学会的专用命令 |
| **下一台** | 再连 3051 等，同样 poll/read；专用功能靠 **该型号 DD** |
| **产品化** | 接入 FieldComm DD/FDI 引擎，菜单/方法不再手写 |

FY301 不是产品边界，是 **第一条可训练的回路**。
