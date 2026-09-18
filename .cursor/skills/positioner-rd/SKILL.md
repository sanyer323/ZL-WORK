---
name: positioner-rd
description: 阀门定位器 / FY301 / HART 研发约定与坑。重要任务默认两版+主模型取舍。定位器固件、仿真、选型相关任务优先读本 Skill。
---

# 定位器研发（FY301 / HART）

## 路径约定

| 用途 | 路径 |
|------|------|
| 本 Skill（本机） | `~\.cursor\skills\positioner-rd\` |
| 知识库 | `ValvePositioner\docs\kb\`（仓库镜像：`AI研发产品/docs/kb/`） |
| 通用双模型流程 | `~\.cursor\skills\dual-model-watch\` |

增量改本目录与 kb；禁止整篇重写。一次性试错不入库。

跨任务「懂人、懂我、积攒知识」及重要任务两版+主模型：见 `owner-prefs` Skill；笔记习惯对齐 Obsidian。

## 本目录文件索引

| 文件 | 内容 |
|------|------|
| `SKILL.md` | 总索引（本文件） |
| `dual-model-watch.md` | 重要任务双模型盯梢（做+盯） |
| `hart-fy301.md` | FY301 / HART 相关约定 |
| `disc1-abb.md` | ABB / disc1 相关笔记 |

（若还有其它 `.md`，保持原样，勿删。）

## 重要任务：两版 + 主模型取舍（强制）

**经验**：FY301 电路板——两模型各改一版，再问主模型；主模型能说清为啥改、怎么取舍。  
主人可不懂技术；要的是这种万无一失的综合，**不是**两边机械互辩。

开场：

```text
按 positioner-rd / dual-model-watch：两版实现，主模型综合取舍并定稿。
```

细则见 `dual-model-watch` Skill 与同目录 `dual-model-watch.md`。

### 禁止

- 同一模型既实现又自称审查通过即收工
- 无休止互传清单互改
- 逼主人做电路级二选一

## FY301 资料（仓库内）

- 手册：`AI研发产品/FY301ME.pdf`、翻译版
- 仿真：`AI研发产品/研发仿真视频/`
- 具体命令表/工具链：有稳定结论后增量写入本目录或 kb，勿整篇重写
