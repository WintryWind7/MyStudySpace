@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ========================================
echo   ManageSystem 数据库初始化
echo ========================================
echo.
echo 正在初始化数据库...
echo.

"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p123456 < sql/complete_database.sql

if %errorlevel% == 0 (
    echo.
    echo ========================================
    echo   数据库初始化成功！
    echo ========================================
    echo.
    echo 已创建：
    echo   - 数据库: student
    echo   - 表: adminInfo (管理员表)
    echo   - 表: employeeinfo (员工表)
    echo   - 表: attendance (考勤表)
    echo   - 测试数据: 5个员工记录
    echo.
) else (
    echo.
    echo ========================================
    echo   数据库初始化失败！
    echo ========================================
    echo.
    echo 请检查：
    echo   1. MySQL服务是否已启动
    echo   2. 用户名密码是否正确 (当前: root/123456)
    echo   3. MySQL路径是否正确
    echo.
)

pause
