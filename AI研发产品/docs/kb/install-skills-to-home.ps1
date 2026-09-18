# Install Cursor skills to Windows user profile
# Copies repo skills into ~\.cursor\skills\ (positioner-rd + dual-model-watch)
# Run in PowerShell from the ZL-WORK repo root:
#   powershell -ExecutionPolicy Bypass -File "AI研发产品\docs\kb\install-skills-to-home.ps1"

$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..")
$destRoot = Join-Path $env:USERPROFILE ".cursor\skills"

$pairs = @(
  @{ Src = "\.cursor\skills\positioner-rd"; Name = "positioner-rd" },
  @{ Src = "\.cursor\skills\dual-model-watch"; Name = "dual-model-watch" }
)

New-Item -ItemType Directory -Force -Path $destRoot | Out-Null

foreach ($p in $pairs) {
  $src = Join-Path $repoRoot $p.Src.TrimStart('\')
  $dst = Join-Path $destRoot $p.Name
  if (-not (Test-Path $src)) {
    Write-Warning "Skip missing: $src"
    continue
  }
  New-Item -ItemType Directory -Force -Path $dst | Out-Null
  Copy-Item -Path (Join-Path $src "*") -Destination $dst -Recurse -Force
  Write-Host "Installed: $dst"
}

$kbHint = Join-Path $env:USERPROFILE "ValvePositioner\docs\kb"
Write-Host ""
Write-Host "Done. Skills are in: $destRoot"
Write-Host "If you keep ValvePositioner kb separately, copy:"
Write-Host "  AI研发产品\docs\kb\workflow-dual-model-watch.md"
Write-Host "  -> $kbHint\workflow-dual-model-watch.md"
