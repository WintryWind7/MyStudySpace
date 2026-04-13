@echo off
echo 正在编译项目...
javac -encoding UTF-8 -d bin -cp "lib\mysql-connector-j-8.0.33.jar" src\model\*.java src\util\*.java src\dao\*.java src\view\*.java
if %errorlevel% == 0 (
    echo 编译成功！
    copy src\database.properties bin\ >nul 2>&1
    echo 配置文件已复制
) else (
    echo 编译失败！
)
pause
