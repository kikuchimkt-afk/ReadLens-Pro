@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul

cd /d "%~dp0"

set "PORT=8091"
set "URL=http://127.0.0.1:%PORT%/"

echo.
echo   ============================================
echo     ReadLens Pro - Local Development Server
echo   ============================================
echo.
echo   Working dir : %CD%
echo   Port        : %PORT%
echo   URL         : %URL%
echo.

REM ---- Free the port if it is already taken (best-effort) ----
for /f "tokens=5" %%P in ('netstat -ano ^| findstr /R /C:"127.0.0.1:%PORT% .*LISTENING"') do (
    echo   [!] Port %PORT% is in use by PID %%P. Stopping it...
    taskkill /PID %%P /F >nul 2>&1
)

REM ---- Locate a Python interpreter (py launcher, then python, then python3) ----
set "PYBIN="
where py >nul 2>&1 && set "PYBIN=py -3"
if not defined PYBIN (
    where python >nul 2>&1 && set "PYBIN=python"
)
if not defined PYBIN (
    where python3 >nul 2>&1 && set "PYBIN=python3"
)

if not defined PYBIN (
    echo.
    echo   [ERROR] Python 3 is not found in PATH.
    echo   Please install Python 3 from https://www.python.org/downloads/
    echo   then re-run this script.
    echo.
    pause
    exit /b 1
)

echo   Using       : %PYBIN%
echo.
echo   Opening browser ...
start "" "%URL%"
echo.
echo   Press Ctrl+C in this window to stop the server.
echo   --------------------------------------------
echo.

%PYBIN% -m http.server %PORT% --bind 127.0.0.1

echo.
echo   Server stopped.
pause
endlocal
