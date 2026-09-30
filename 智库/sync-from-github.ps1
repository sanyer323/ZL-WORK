# 把 GitHub 上已合入的智库拉进 Obsidian 正在看的那份库。
# 本机计划任务 21:40 / 08:00 会跑；也可手动执行。
$ErrorActionPreference = "Stop"
& "$env:USERPROFILE\.cursor\skills\domain-think-tank\sync-thinktank.ps1"
