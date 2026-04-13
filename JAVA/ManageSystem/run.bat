@echo off
echo 正在启动ManageSystem管理系统...
cd /d "%~dp0"
java -cp "bin;lib\mysql-connector-j-8.0.33.jar" view.MainApp
pause
