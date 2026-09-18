---
name: positioner-rd
description: 阀门定位器 / FY301 / HART 研发约定与坑。含重要任务双模型盯梢。定位器固件、仿真、选型相关任务优先读本 Skill。
---

# 定位器研发（FY301 / HART）

## 路径约定

| 用途 | 路径 |
|------|------|
| 本 Skill（本机） | `~\.cursor\skills\positioner-rd\` |
| 知识库 | `ValvePositioner\docs\kb\`（仓库镜像：`AI研发产品/docs/kb/`） |
| 通用双模型流程 | `~\.cursor\skills\dual-model-watch\` |

增量改本目录与 kb；禁止整篇重写。一次性试错不入库。

## 本目录文件索引

| 文件 | 内容 |
|------|------|
| `SKILL.md` | 总索引（本文件） |
| `dual-model-watch.md` | 重要任务双模型盯梢（做+盯） |
| `hart-fy301.md` | FY301 / HART 相关约定 |
| `disc1-abb.md` | ABB / disc1 相关笔记 |

（若还有其它 `.md`，保持原样，勿删。）

## 重要任务：双模型盯梢（强制）

**触发**：FY301 firmware skeleton、固件骨架、HART 协议、仿真入口、要合主分支的大改。  
**现象**：单模型做完易留编译失败、模块空洞、验收未达标。

### 流程

1. **做（Doer）**：模型 A 实现 + 自测，给出编译/运行证据。
2. **盯（Watcher）**：另开 Agent，选**不同**模型 B；或 `/agent-review` **Deep**。
3. 盯方只出阻断/应修/建议；做方再修。
4. **收工门槛**：盯方无阻断项；未验证项须标明。

细则见同目录 `dual-model-watch.md`，以及 `~\.cursor\skills\dual-model-watch\SKILL.md`。

### 禁止

- 同一聊天、同一模型既实现又自称审查通过
- 用 `/best-of-n` 代替盯梢（那是多方案竞赛）

## FY301 资料（仓库内）

- 手册：`AI研发产品/FY301ME.pdf`、翻译版
- 仿真：`AI研发产品/研发仿真视频/`
- 具体命令表/工具链：有稳定结论后增量写入本目录或 kb，勿整篇重写
