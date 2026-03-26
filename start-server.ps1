# ReadLens Pro - Local Development Server
Write-Host ""
Write-Host "  ============================================" -ForegroundColor Cyan
Write-Host "    ReadLens Pro - Local Development Server" -ForegroundColor Cyan
Write-Host "  ============================================" -ForegroundColor Cyan
Write-Host ""

$port = 8091
$appDir = $PSScriptRoot

# Kill existing process on port
$existing = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "  [!] Port $port is in use. Stopping..." -ForegroundColor Yellow
    $existing | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
    Start-Sleep -Seconds 2
}

Write-Host "  URL: http://127.0.0.1:$port" -ForegroundColor Green
Write-Host "  Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

Set-Location $appDir
python -m http.server $port --bind 127.0.0.1
