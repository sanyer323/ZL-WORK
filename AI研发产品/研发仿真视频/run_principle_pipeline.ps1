# FY301 原理讲解版一键流水线（Windows）
# 用法：
#   .\run_principle_pipeline.ps1
#   .\run_principle_pipeline.ps1 -VerifyOnly
#   .\run_principle_pipeline.ps1 -ForceSims

param(
    [switch]$VerifyOnly,
    [switch]$ForceSims,
    [switch]$SkipSims,
    [switch]$SkipCompose,
    [switch]$RebuildManifest,
    [switch]$WithBlender,
    [switch]$RequireBlender,
    [string]$BlenderPath = ""
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

$argsList = @()
if ($VerifyOnly) { $argsList += "--verify-only" }
if ($ForceSims) { $argsList += "--force-sims" }
if ($SkipSims) { $argsList += "--skip-sims" }
if ($SkipCompose) { $argsList += "--skip-compose" }
if ($RebuildManifest) { $argsList += "--rebuild-manifest" }
if ($WithBlender) { $argsList += "--with-blender" }
if ($RequireBlender) { $argsList += "--require-blender" }
if ($BlenderPath) { $argsList += @("--blender", $BlenderPath) }

python run_principle_pipeline.py @argsList
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
