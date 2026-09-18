---
name: positioner-rd
description: 阀门定位器 / FY301 / HART 研发约定与坑。含重要任务双模型盯梢。定位器固件、仿真、选型相关任务优先读本 Skill。
---

# 定位器研发（FY301 / HART）

## 路径约定

| 用途 | 路径 |
|------|------|
| 本 Skill（本机） | `~\.cursor\skills\positioner-rd\` |
| 知识库 | `ValvePositioner\docs\kb\`（本仓库镜像：`AI研发产品/docs/kb/`） |
| 通用双模型流程 | `.cursor/skills/dual-model-watch/` |

增量改本目录与 kb；禁止整篇重写。一次性试错不入库。

## 重要任务：双模型盯梢（强制）

**触发**：FY301 firmware skeleton、固件骨架、HART 协议、仿真入口、要合主分支的大改。  
**现象**：单模型做完易留编译失败、模块空洞、验收未达标。

### 流程

1. **做（Doer）**：模型 A 实现 + 自测，给出编译/运行证据。
2. **盯（Watcher）**：另开 Agent，选**不同**模型 B；或 `/agent-review` **Deep**。
3. 盯方只出阻断/应修/建议；做方再修。
4. **收工门槛**：盯方无阻断项；未验证项须标明。

### 盯梢提示词（FY301）

```text
你是盯梢审查员。审查当前分支相对 base 的 FY301/定位器相关改动。
对照验收：固件骨架可编译或明确桩边界；目录/模块与约定一致；关键路径有入口。
输出：阻断项 / 应修项 / 建议项 / 未验证项。不要重写整单。
```

细则与通用规则见：`dual-model-watch` Skill；kb 条目：`AI研发产品/docs/kb/workflow-dual-model-watch.md`。

### 禁止

- 同一聊天、同一模型既实现又自称审查通过
- 用 `/best-of-n` 代替盯梢（那是多方案竞赛）

## FY301 相关（待增量）

- 手册：`AI研发产品/FY301ME.pdf`、翻译版
- 仿真视频工作台：`AI研发产品/研发仿真视频/`
- 具体固件树、工具链、HART 命令表：有稳定结论后再增量写入本目录或 `docs/kb/`
