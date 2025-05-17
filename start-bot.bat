@echo off
setlocal

set BOT_PATH=C:\Users\mmath\drive\Projects\MITPA\bot-beta

REM
powershell -NoProfile -ExecutionPolicy Bypass -Command "Import-Module BurntToast; New-BurntToastNotification -Text 'MITPA Monitor', 'The beta bot is down and is being launched locally.'"

REM
cd /d "%BOT_PATH%"
npm start

endlocal