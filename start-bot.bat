@echo off
setlocal

for /f "tokens=1,2 delims==" %%a in (config.cfg) do (
    if "%%a"=="BOT_PATH" set BOT_PATH=%%b
)

REM
powershell -NoProfile -ExecutionPolicy Bypass -Command "Import-Module BurntToast; New-BurntToastNotification -Text 'PRACTA Monitor', 'The beta bot is down and is being launched locally.'"

cd /d "%BOT_PATH%"
npm start

endlocal
