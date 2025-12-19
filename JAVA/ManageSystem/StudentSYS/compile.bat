@echo off
cd /d "%~dp0"
echo 正在编译...
javac -encoding UTF-8 -cp "lib/mysql-connector-j-8.0.33.jar" -d bin src/mqx/pojo/Admin.java src/mqx/pojo/Employee.java src/mqx/dao/DbHelperByMySQL.java src/mqx/dao/AdminDAO.java src/mqx/dao/EmployeeDAO.java src/mqx/view/EmployeeSysView.java src/mqx/view/EmpMenuLogin.java src/mqx/view/EmployeeAPP.java
if %errorlevel% equ 0 (
    echo 编译成功！
    copy src\jdbc.config bin\jdbc.config >nul 2>&1
) else (
    echo 编译失败！
)
pause
