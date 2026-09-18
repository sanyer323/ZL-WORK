# 工作流：重要任务双模型盯梢

- **日期**：2026-09-18
- **来源**：FY301 firmware skeleton 单模型做完后出错 → 改为做+盯
- **适用范围**：定位器 / FY301 / HART / 固件骨架；其它高成本任务可复用

## 结论

重要任务必须 **模型 A 实现 + 模型 B（或 Agent Review Deep）审查**，审查无阻断项才收工。

## 操作

1. Doer 完成并自测
2. `/agent-review` Deep，或新开 Agent 换模型盯梢
3. 修阻断项后再合入

## 禁止

- 单模型自审通过即收工
- 用 `/best-of-n` 当审查

## 交流讨论

先对齐出发点（做方取舍 vs 盯方验收），**您拍板**后再有限修改（≤2 轮）。  
禁止无上限互传清单改到乱。详见 Skill「先对齐出发点，再改」。

## 关联

- Skill：`positioner-rd`、`dual-model-watch`
- 本机安装：见 `AI研发产品/docs/kb/install-skills-to-home.ps1`
