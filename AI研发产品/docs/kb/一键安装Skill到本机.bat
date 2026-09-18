@echo off
chcp 65001 >nul
setlocal
title 安装 Cursor Skills（positioner-rd）

REM 本脚本放在：ZL-WORK\AI研发产品\docs\kb\
REM 双击即可把 Skill 装到：%USERPROFILE%\.cursor\skills\

set "REPO=%~dp0..\..\.."
set "DEST=%USERPROFILE%\.cursor\skills"

echo.
echo 仓库目录: %REPO%
echo 安装到:   %DEST%
echo.

if not exist "%REPO%\.cursor\skills\positioner-rd\SKILL.md" (
  echo [错误] 找不到 Skill 文件。
  echo 请先把本仓库更新到最新，或确认您是在 ZL-WORK 里双击本文件。
  echo.
  pause
  exit /b 1
)

mkdir "%DEST%\positioner-rd" 2>nul
mkdir "%DEST%\dual-model-watch" 2>nul

xcopy /E /I /Y "%REPO%\.cursor\skills\positioner-rd\*" "%DEST%\positioner-rd\" >nul
xcopy /E /I /Y "%REPO%\.cursor\skills\dual-model-watch\*" "%DEST%\dual-model-watch\" >nul

echo [完成] 已安装：
echo   %DEST%\positioner-rd\
echo   %DEST%\dual-model-watch\
echo.
echo 请重新打开 Cursor，或新开一个对话后再用。
echo.
pause
