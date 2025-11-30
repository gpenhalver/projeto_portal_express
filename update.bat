@echo off
cd /d "%~dp0"
git add .
git commit -m "update automático"
git push
echo.
echo Atualização enviada com sucesso!
pause
