# ReadLens Pro - Local Development Server (PowerShell)
# Usage: Right-click and "Run with PowerShell", or in a PowerShell prompt:
#   PowerShell -ExecutionPolicy Bypass -File .\start-server.ps1

$ErrorActionPreference = 'Continue'
$Port    = 8091
$AppDir  = $PSScriptRoot
$Url     = "http://127.0.0.1:$Port/"

# UTF-8 console
try { [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new() } catch {}

Write-Host ""
Write-Host "  ============================================" -ForegroundColor Cyan
Write-Host "    ReadLens Pro - Local Development Server" -ForegroundColor Cyan
Write-Host "  ============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host ("  Working dir : {0}" -f $AppDir)
Write-Host ("  Port        : {0}" -f $Port)
Write-Host ("  URL         : {0}" -f $Url) -ForegroundColor Green
Write-Host ""

# --- Free the port if it is already taken (best-effort) -----------------
try {
    $existing = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
    if ($existing) {
        foreach ($c in $existing) {
            Write-Host ("  [!] Port {0} is in use by PID {1}. Stopping..." -f $Port, $c.OwningProcess) -ForegroundColor Yellow
            Stop-Process -Id $c.OwningProcess -Force -ErrorAction SilentlyContinue
        }
        Start-Sleep -Seconds 1
    }
} catch {
    # Get-NetTCPConnection may not be available on very old systems; ignore.
}

# --- Locate Python interpreter ------------------------------------------
function Test-Cmd($name) {
    return [bool](Get-Command $name -ErrorAction SilentlyContinue)
}

$pythonCmd = $null
$pythonArgs = @()
if (Test-Cmd 'py')      { $pythonCmd = 'py';      $pythonArgs = @('-3') }
elseif (Test-Cmd 'python')  { $pythonCmd = 'python';  $pythonArgs = @() }
elseif (Test-Cmd 'python3') { $pythonCmd = 'python3'; $pythonArgs = @() }

if (-not $pythonCmd) {
    Write-Host ""
    Write-Host "  [ERROR] Python 3 is not found in PATH." -ForegroundColor Red
    Write-Host "  Please install Python 3 from https://www.python.org/downloads/" -ForegroundColor Red
    Write-Host "  and re-run this script." -ForegroundColor Red
    Write-Host ""
    Write-Host "  Press Enter to exit..."
    [void](Read-Host)
    exit 1
}

Write-Host ("  Using       : {0} {1}" -f $pythonCmd, ($pythonArgs -join ' '))
Write-Host ""
Write-Host "  Opening browser ..." -ForegroundColor Gray
Start-Process $Url | Out-Null
Write-Host ""
Write-Host "  Press Ctrl+C in this window to stop the server." -ForegroundColor Gray
Write-Host "  --------------------------------------------" -ForegroundColor DarkGray
Write-Host ""

Set-Location -LiteralPath $AppDir

# Run Python http.server in the foreground (Ctrl+C stops it)
& $pythonCmd @pythonArgs -m http.server $Port --bind 127.0.0.1

Write-Host ""
Write-Host "  Server stopped." -ForegroundColor Yellow
Write-Host "  Press Enter to close..."
[void](Read-Host)
