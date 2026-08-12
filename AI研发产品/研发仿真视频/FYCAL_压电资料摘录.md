# FYCAL / 压电陶瓷技术资料摘录

> **来源 PDF**：`C:\Users\sanye\Desktop\SMAR\AI研发产品\fycalme.pdf`  
> **文档标题**：Microsoft Word - FYCALMEx_Tercio_final（Operation Manual FYCAL ME）  
> **页数**：22  
> **创建日期元数据**：2014-04-14  
> **语言**：英文原版；本摘录将关键技术事实译为中文，关键数值保留原文并附中文说明。  
> **提取工具**：PyMuPDF (fitz)；pypdf 可用但未作为主提取。  
> **提取范围**：仅收录与压电 / piezo / FYCAL 标定 / 先导压力 / 节流（restriction）相关内容。原文未出现 “nozzle-flapper / 喷嘴挡板” 字样，但描述的是压电驱动挡板高度 `h` + 节流孔（restriction）调节先导压力的结构。

---

## 0. 同目录相关文件扫描（含 FYCAL / fycal / 压电 / piezo）

| 文件 | 说明 |
|------|------|
| `fycalme.pdf` | FYCAL 操作手册（本摘录主源） |
| `研发仿真视频\压电陶瓷研发笔记.md` | 既有研发笔记（含与本手册不同的 V–P 表，见文末对照） |
| `研发仿真视频\out\01_压电陶瓷原理.mp4` | 压电原理相关视频 |

未发现其他文件名含 FYCAL/fycal/压电/piezo 的新建文档。

---

## 1. FYCAL 是什么，与 FY301 压电的关系

**FYCAL** = **Calibration Device for Pressure Transducer（压力变送器/压电底座标定装置）**。

- 标定对象是定位器中的 **piezo base（压电底座 / 压力换能器部分）**。
- 适用 Smar FY 系列定位器用户：
  - HART：`FY301`、`FY400`
  - FOUNDATION fieldbus：`FY302`
  - PROFIBUS-PA：`FY303`
- 用途：在仪表车间标定 piezo base，使工程师/仪表技师能自行维护。
- 与 FY301 的关系：FY301 等 FY 定位器以压电元件为工作原理核心；FYCAL 是专门给这些定位器的 **压电底座做离线标定/检修** 的工装，不是定位器本体。

原文要点：

> The FYCAL is a Calibration Device for Pressure Transducer – the piezo base – the part of the electro-pneumatic positioner, Smar FY.

> The FYCAL, therefore, is destined for Smar FY positioner users for HART® (FY301 and FY400), FOUNDATION™ fieldbus (FY302), PROFIBUS-PA (FY303) technologies.

---

## 2. 压电电压范围、测试点与程序

### 2.1 工作原理与控制电压

- Smar 定位器基于压电元件：施加电压产生挠曲（deflection）。
- **压电工作电压范围：0 ~ 100 Vdc**。
- 当 `PV = SP`（阀位正确）时，加在压电上的电压称为 **control voltage（控制电压）**。
- 此时膜片对滑阀（spool）的力与弹簧力平衡；滑阀处于无气流通向输出、也无气从执行器腔室排大气的位置。
- **推荐控制电压尽量接近 50 Vdc，或落在 30 ~ 70 Vdc**，以保证良好运行。
- 出厂已按上述参数标定；现场因振动、仪表气质量差、环境因素等，控制电压可能偏离推荐范围，此时需重新标定 piezo base。
- 标定实质：调整高度 **`h`**（见 Figure 03），使控制电压接近理想值 **50 Vdc**。
- 可通过 HART / PROFIBUS / Fieldbus 组态器在运行中查看压电电压。

### 2.2 运行中检查压电电压的方法

1. 将设定值设到量程内任意值（**10% ~ 90%**）。
2. 待阀杆停止运动后，用组态器读取压电电压。

### 2.3 按控制电压判定是否需要维护（关键门槛）

| Vpiezo | 处理 |
|--------|------|
| **30 Vdc < Vpiezo < 70 Vdc** | 无需标定 |
| **20 Vdc < Vpiezo < 30 Vdc** 或 **70 Vdc < Vpiezo < 80 Vdc** | 仍可正常工作，但应安排预防性维护 |
| **Vpiezo < 20 Vdc** 或 **Vpiezo > 80 Vdc** | 必须拆下定位器，解体并标定 piezo base |

### 2.4 压电绝缘测试（Procedures for measuring the Piezo Insulation）

**MODE 1**

- 用 **0~100 Vdc** 电源、**最大电流 1 µA**，对 piezo base 施加 **100 VDC**。
- 若电压跌落 **≥ 2 V**，必须更换新的 piezo base。

**MODE 2**

- 用兆欧表，档位 **100 V**，测量 piezo base **helmet pin（金属盔帽针脚）** 与 **housing（壳体）** 间电阻。
- 若电阻 **< 50 MΩ**，判定绝缘偏低，必须更换 piezo base。

### 2.5 在气路块上标定 piezo base（assembled on block）

1. 拆下连接罩、模拟板、断开 Hall 扁平电缆后，用 **M4×35 mm** 螺丝把 piezo base 固定在组件上（可用 Hall 罩同类螺丝；建议备 4 颗新螺丝，或对角取用 Hall 罩两颗）。
2. 用 FYCAL 电源供电：**可变 0~100 Vdc，1 µA**。
   - **负极** → 金属盔帽中心（metallic helmet center）
   - **正极** → piezo base 任意未喷漆金属部位
3. **先加 50 VDC**。
4. 给定位器供气（建议接近实际工作压力）。
5. 用 FYCAL 标定工具旋转金属盔帽，调到 **OUT1 与 OUT2 压力最小且相等** → 即标定完成。
6. 验证：上下改变电压，两路输出压力应随之变化：
   - **V > 50 VDC**：OUT1 压力 > OUT2
   - **V < 50 VDC**：OUT2 压力 > OUT1
7. 若块上无法标定，改为在 FYCAL 结构上单独标定（见下节）以定位问题。

### 2.6 在 FYCAL 上单独标定 / 测试 piezo base

前置：

1. 取下 **restriction（节流孔）**，检查是否堵塞（详见 FY 手册维护节）。
2. 将节流孔装回 piezo base。
3. 用四颗螺丝把 piezo base 紧固到 FYCAL 上。
4. 连接 FYCAL **0~100 V** 输出电缆：
   - **黑线（负）** → 底座中心（针状接头，便于插入中心）
   - **红线（正）** → 任意底座固定螺丝

测试判据（供气 **20 PSI**）：

| 步骤 | 条件 | 期望先导压力 |
|------|------|----------------|
| 1 | 输入压力 20 PSI | — |
| 2 | 施加 **50 Vdc**，用标定工具旋转调节 | 先导压力约 **8 PSI** |
| 3 | 施加 **100 V** | 先导压力 **降至 3 PSI 以下** |
| 4 | 施加 **0 V** | 先导压力 **超过 12 PSI** |

手册结论：性能接近上表则 piezo base 正常；再回到块上标定。若块上仍失败，问题可能在 **膜片或滑阀**。若单独测试就不达标，则需拆解清洗压电元件。

### 2.7 压电元件拆解清洗（仅当无法调制输出压力时）

目的：清除杂质或运行中累积的湿气。

拆盔帽：

1. 用卡簧钳取下卡簧（snap ring）。
2. 取出含 piezo、垫圈、弹簧的 “helmet” 组件（有 O 型圈，可能较紧）。

清洁：

- 底座内部：中性洗涤剂湿布擦拭，干燥压缩空气吹干。
- 压电片：干燥干净布小心擦拭，干燥压缩空气去除杂质/油/湿气。

重装顺序（装在金属盔帽上）：

1. O’ring  
2. 第一垫圈  
3. 调节弹簧  
4. 第二垫圈  

然后插入底座腔，保证盔帽导向销落入缺口，盔帽可自由旋转；装卡簧并压到位；再标定。标定仍失败则更换整套 piezo base。

---

## 3. 先导压力 vs 电压（表 / 曲线）

手册 **未给出连续曲线图或完整查表**，仅给出 FYCAL 单独测试的离散判据点（输入固定 **20 PSI**）：

| V_piezo | Pilot pressure（先导压力） | 备注 |
|---------|---------------------------|------|
| **50 Vdc** | **约 8 PSI** | 用标定工具旋转调到此点 |
| **100 V** | **< 3 PSI** | 相对 50 V 下降 |
| **0 V** | **> 12 PSI** | 相对 50 V 上升 |

**趋势（据本手册）**：在 20 PSI 供气、FYCAL 单独测试条件下，**电压升高 → 先导压力降低**；电压降低 → 先导压力升高。

块上标定的定性关系（不是先导压力表，而是 OUT1/OUT2）：

| 电压相对 50 V | 输出压力关系 |
|---------------|--------------|
| > 50 VDC | OUT1 > OUT2 |
| < 50 VDC | OUT2 > OUT1 |
| = 50 VDC（标定目标） | OUT1 与 OUT2 最小且相等 |

FYCAL 面板指示（Figure 13 / 19）：

- **Pilot Pressure Indication（先导压力指示）**
- **Input Pressure Indication（输入压力指示）**
- **0 to 100 Vdc Output**（规格正文）；尺寸图面板标注另有 **OUTPUT 0-140 Vdc** 字样（以规格表 0~100 Vdc 为准）
- **4 to 20 mA Output**

---

## 4. 硬件连接 / 压电模块识别

### 4.1 定位器拆解中的模块识别（Figure 07 / 09）

手册标注部件包括：

- **Piezo Base**（压电底座）
- **Restriction**（节流孔）
- **Analog Board**（模拟板）
- **Connection Cover**（连接罩）
- **Pneumatic Block**（气路块）
- **Assembled Diaphragm**（膜片组件）
- **Spool Valve and Spring**（滑阀与弹簧）
- **Hall Sensor / Flat Cable / Sensor Cover / Hall Cover**
- **Housing / Main Board and Display LCD**
- **Housing Rotary Locking Screw**（壳体旋转锁定螺钉）

关键紧固件：

- Hall 罩螺丝：**M4×35 mm**
- 连接罩螺丝：**M4×50 mm**

### 4.2 FYCAL 供电接线（标定压电）

| 极性 | 连接点 |
|------|--------|
| 负极（黑，针状） | 金属盔帽中心 / 底座中心 |
| 正极（红） | piezo base 未喷漆金属部位，或底座固定螺丝 |

电源能力：**0~100 Vdc，1 µA**（绝缘测试同样限流 1 µA）。

### 4.3 FYCAL 产品构成与规格

| 项目 | 规格 |
|------|------|
| 电源 | 110 或 220 Vac，50/60 Hz |
| 压力输入 | **0 ~ 100 psi** |
| 输出 | **0 ~ 100 Vdc**（连续电位器调节，供压电） |
| 输出 | **4 ~ 20 mA**（分辨率 **1 µA**；连续或按键步进） |
| 附件 | 标定工具 1 件；接 piezo base 电缆一对；接定位器 4–20 mA 电缆一对；入口调压过滤器 |
| 压力表精度（ABNT B 级） | 量程 25%~75%：±2.0% F.S.；其余：±3.0% F.S. |

备件代码（与压电标定相关）：

| 描述 | 代码 |
|------|------|
| Accuracy potentiometer - FYCAL | 400-1172 |
| Electronic circuit board – FYCAL | 400-0906 |
| Pressure regulator | 400-1181 |
| Power supply cable for 4 to 20 mA | 400-1182 |
| Power supply cable for 0 to 100 V | 400-1183 |
| Tool for transducer calibration, new version | 400-1185 |
| Sealing joint | 400-1186 |

### 4.4 拆装注意（与压电模块相关）

- 防静电：戴腕带或触摸接地物；避免直接触碰板卡元件/针脚。
- 主板上 **Local Adjust Sensor（本地调整传感器 / reed switch）** 很脆弱（FY300 系列专有）。
- 拆连接罩时注意密封圈与 Hall 扁平电缆易损。
- 取 piezo base 可用 tip/stylus，勿戳破膜片。
- 检查滑阀是否在气路块内自由运动；否则拆下滑阀与弹簧，用温和洗涤剂清洗块内腔。

---

## 5. 与压电相关的故障模式 / 诊断（仅手册事实）

| 现象 / 判据 | 手册给出的含义或处理 |
|-------------|----------------------|
| 控制电压偏出 30–70 V（尤其 <20 或 >80） | 需标定或维护 piezo base |
| 绝缘测试 100 V 下压降 ≥ 2 V | 更换 piezo base |
| 盔帽针脚–壳体电阻 < 50 MΩ | 绝缘低，更换 piezo base |
| FYCAL 单独测试不符合 50V≈8 psi / 100V<3 psi / 0V>12 psi | 需拆解清洗压电元件；仍失败则更换 piezo base |
| 单独测试合格但块上标定失败 | 可能膜片或滑阀问题 |
| 膜片有孔/撕裂 | 更换膜片 |
| 滑阀卡滞/污染 | 一般清洗；损坏则更换 |
| 节流孔堵塞 | 检查/清理 restriction（详见 FY 手册） |
| 振动、气源质量差、环境因素 | 可使出厂标定漂移，需重标定 |
| 无法在 OUT1/OUT2 间调制压力 | 才建议拆压电元件清洗湿气/杂质 |
| 清洗重装后仍无法标定 | 更换新 piezo base |

静电风险：可能损坏电路板半导体元件（预防措施见上节）。

---

## 6. 图注 / 照片说明（与压电组件相关）

| 图号 | 英文图注 | 内容含义 |
|------|----------|----------|
| Figure 01 | FYCAL and Calibration Tool | FYCAL 整机与标定工具 |
| Figure 02 | Calibration Tool (Detail) | 标定工具细节 |
| Figure 03 | Schematic of Equilibrium Position | 平衡位置示意（含高度 **h** 调节） |
| Figure 04 | Flowchart - Procedures to Calibrate the Piezo Base | 压电底座标定流程图 |
| Figure 05 | Local Adjust Sensor of the Main Board | 主板本地调整传感器（reed switch） |
| Figure 06 | Disassembled housing with disconnected transducer | 壳体已拆、换能器断开 |
| Figure 07 | Disassembled connection cover | 连接罩分解（标注 Piezo Base、Restriction 等） |
| Figure 08 | Disassembly connection cover and Analog Board | 连接罩与模拟板拆解 |
| Figure 09 | Disassembled Positioner | 定位器全部分解图（含 Piezo Base） |
| Figure 10 | Assembling to supply the piezo base - using the FYCAL power supply | 用 FYCAL 电源给压电底座供电的装配 |
| Figure 11 | Assembled Piezo base to use the FYCAL power supply | 已装好的压电底座接 FYCAL 电源 |
| Figure 12 | Piezo Base Calibration on the block with help the Base Tool Calibration | 在气路块上用底座标定工具标定 |
| Figure 13 | FYCAL | FYCAL 面板：入口压力、先导压力、0–100 V、4–20 mA 等 |
| Figure 14 | Calibration of the Piezo Base separately in the FYCAL | 压电底座单独装在 FYCAL 上标定（Piezo Base / Assembly Base） |
| Figure 15 | Removing the “helmet” that contains the piezo | 取下含压电片的金属盔帽 |
| Figure 16 | Cleaning Piezo | 清洁压电片 |
| Figure 17 | Reassembling of the piezo base | 压电底座重装 |
| Figure 18 | Exploded view of the assembled piezo base | 压电底座爆炸图 |
| Figure 19 | FYCAL Dimensional Drawing | FYCAL 外形尺寸图（面板含 PILOT PRESSURE 等刻度） |

原文未提供可用 OCR 的零件编号长列表；爆炸图/装配图以图注识别为主。

---

## 7. 关键参数原文摘录（Exact quotes）

以下为手册中的关键数值原句/原短语（英文照录）：

1. **电压范围**  
   > voltage varies of 0 to 100 Vdc.

2. **推荐控制电压**  
   > It is recommended that this control voltage is as close as possible to 50 Vdc, or in the range 30 to 70 Vdc

3. **标定目标**  
   > This adjustment allows the control voltage will be approximate to the ideal value 50 Vdc.

4. **运行检查设定范围**  
   > Put the setpoint to any value, 10 to 90% range

5. **电压诊断门槛**  
   > 30Vdc <Vpiezo <70Vdc: no need calibration;  
   > 20Vdc<Vpiezo<30Vdc or 70Vdc<Vpiezo<80Vdc: positioner is still working properly but indicates the need to schedule a preventive maintenance;  
   > Vpiezo<20Vdc or Vpiezo>80Vdc: is necessary to remove the valve positioner, disassemble and calibrate the piezo base

6. **绝缘 MODE 1**  
   > Apply 100 VDC piezo base with 0 to 100 Vdc power supply and 1 uA maximum current.  
   > If there is a voltage drop of 2 volts or more, the piezo base needs to be replaced

7. **绝缘 MODE 2**  
   > configured in 100 Volts scale ... If the measurement is less than 50 MΩ, the piezo base is insulation low.

8. **FYCAL 供电**  
   > FYCAL power supply (variable 0 to 100 Vdc, 1 μA)

9. **块上初加电压**  
   > Initially, apply 50 VDC on the piezo base.

10. **OUT1/OUT2 与 50 V 关系**  
    > With voltages greater than 50 VDC output 1 must be greater pressure than the output 2, and with less than 50 VDC voltage output 2 will have higher pressure compared to the output 1.

11. **FYCAL 单独测试（先导压力）**  
    > Apply 20 PSI input pressure;  
    > Apply 50 Vdc to the piezo base;  
    > ... until the pilot pressure measured at the gauge is at about 8 PSI;  
    > Apply 100 V voltage and check that the pilot pressure dropped to below 3 PSI;  
    > Apply 0 V voltage and check that the pilot pressure exceeds 12 PSI.

12. **产品规格**  
    > Pressure Input 0 to 100 psi  
    > 0 to 100 Vdc input for the piezoelectric sensor  
    > 4 to 20 mA (1µA resolution)

13. **适用机型**  
    > HART® (FY301 and FY400), FOUNDATION™ fieldbus (FY302), PROFIBUS-PA (FY303)

14. **螺丝规格**  
    > Hall Cover Screw (M4x35 mm)  
    > Connection Cover Screw (M4x50 mm)

---

## 8. 与 FY301ME 维护节的对照（重要）

`FY301ME.pdf`「Piezo Electric Calibration - FYCAL」给出（供气 20 psi）：

| V_piezo | P_pilot |
|---------|---------|
| 0 V | ≤ 2 psi |
| 50 V | 5.8–6.2 psi |
| 100 V | 12–13 psi |

而 **本 fycalme.pdf** 工装手册写的是：

| V_piezo | P_pilot |
|---------|---------|
| 0 V | > 12 psi |
| 50 V | ≈ 8 psi |
| 100 V | < 3 psi |

**方向相反。** 本仓库讲解与仿真 **默认采用 FY301ME**；fycalme 数值仅作工装手册存档，引用时必须注明来源与接线极性。

详见：`压电陶瓷研发笔记.md`。
---

## 9. 关于喷嘴挡板（nozzle-flapper）

`fycalme.pdf` **全文未出现** “nozzle”、“flapper”、“喷嘴”、“挡板” 字样。  
与该机构对应的手册用语为：

- piezoelectric element / piezo base（压电元件 / 压电底座）
- restriction（节流孔）
- pilot pressure（先导压力）
- height “h” adjustment（高度 h 调节）
- metallic helmet（金属盔帽）

即：通过电压使压电挠曲 → 调节盔帽/高度 h → 改变节流后的先导压力 → 再经膜片/滑阀放大到 OUT1/OUT2。
