@echo off
chcp 65001 >nul
title 安装知识库（Obsidian + 智库）
echo.
echo [1/3] 尝试用 winget 安装 Obsidian...
winget install --id Obsidian.Obsidian -e --accept-package-agreements --accept-source-agreements
echo.
echo [2/3] 请确认已打开/更新 ZL-WORK 仓库（含「智库」文件夹）
echo     常见路径: %USERPROFILE%\Downloads\ZL-WORK\智库
echo.
echo [3/3] 安装完成后：打开 Obsidian -^> 打开本地仓库 -^> 选择「智库」文件夹
echo.
echo 说明见仓库: 智库\本机安装说明.md
echo.
pause
