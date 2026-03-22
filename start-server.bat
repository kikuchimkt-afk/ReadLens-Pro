@echo off
chcp 65001 >nul
echo.
echo   ============================================
echo     ReadLens Pro - Local Development Server
echo   ============================================
echo.

set PORT=8091

:: Kill existing process on port (if any)
for /f "tokens=5" %%a in ('netstat -aon 2^>nul ^| findstr ":%PORT% " ^| findstr "LISTENING"') do (
    echo   [!] Port %PORT% is in use (PID: %%a). Stopping...
    taskkill /PID %%a /F >nul 2>&1
    timeout /t 2 /nobreak >nul
)

echo   URL: http://127.0.0.1:%PORT%
echo   Press Ctrl+C to stop
echo.

:: Serve the directory where this batch file is located
npx -y http-server "%~dp0." -p %PORT% --cors -c-1
pause
