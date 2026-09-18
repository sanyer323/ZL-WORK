# 双模型盯梢（positioner-rd 索引）

完整通用流程见仓库 Skill：`.cursor/skills/dual-model-watch/SKILL.md`。

本文件仅保留定位器侧触发条件，避免与通用 Skill 双份漂移。

## 何时强制

- FY301 firmware skeleton / 固件骨架
- HART 协议栈改动
- 仿真与固件接口联调入口
- 准备合入主分支的定位器大改

## 最小检查清单

- [ ] 做方有编译或明确「仅桩、未接线」边界说明
- [ ] 盯方（异模型或 `/agent-review` Deep）无阻断项
- [ ] 有阻断时：盯→做→盯 讨论闭环已跑完（见通用 Skill「发现问题后的交流」）
- [ ] kb 若有新坑，增量写入 `docs/kb/`，不整篇重写

## 交流讨论（发现问题时）

两个 Agent Tab 不能自动互聊。您复制粘贴传话：

1. 盯方出【盯梢问题清单】
2. 贴到做方：只修阻断项并写【做方回复】
3. 贴回盯方复检，直到「无阻断」或您拍板

完整模板见 `dual-model-watch` Skill。
