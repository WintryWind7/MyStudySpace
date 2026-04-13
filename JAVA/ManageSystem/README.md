# ManageSystem 管理系统

## 项目简介
基于 Java + MySQL 的员工管理系统，支持员工信息管理和考勤管理功能。

## 项目结构
```
ManageSystem/
├── src/
│   ├── model/          # 实体类
│   │   ├── Admin.java           # 管理员类
│   │   ├── Employee.java        # 员工类
│   │   └── Attendance.java      # 考勤类
│   ├── dao/            # 数据访问层
│   │   ├── AdminDAO.java        # 管理员数据访问
│   │   ├── EmployeeDAO.java     # 员工数据访问
│   │   └── AttendanceDAO.java   # 考勤数据访问
│   ├── util/           # 工具类
│   │   └── DatabaseHelper.java  # 数据库连接工具
│   ├── view/           # 视图层
│   │   ├── MainApp.java                    # 主程序入口
│   │   ├── LoginView.java                  # 登录注册界面
│   │   ├── EmployeeManagementView.java     # 员工管理界面
│   │   └── AttendanceManagementView.java   # 考勤管理界面
│   └── database.properties      # 数据库配置
├── config/
│   └── database.properties      # 数据库配置（备份）
├── lib/
│   └── mysql-connector-j-8.0.33.jar  # MySQL驱动
├── sql/
│   ├── complete_database.sql    # 完整数据库脚本（推荐使用）
│   ├── create_database.sql      # 数据库创建脚本
│   ├── employee_database_setup.sql   # 员工表脚本
│   └── attendance_table_setup.sql    # 考勤表脚本
├── bin/                # 编译输出目录
├── compile.bat         # 编译脚本
├── run.bat            # 运行脚本
└── setup_database.bat # 数据库初始化脚本
```

## 功能模块

### 1. 用户认证
- 管理员登录（支持输入0返回）
- 管理员注册（支持输入0返回）

### 2. 员工管理
- 显示所有员工
- 添加员工信息
- 查找员工（按工号）
- 删除员工
- 修改员工信息

### 3. 考勤管理
- 显示所有考勤状态
- 员工签到（状态变为"在岗"）
- 员工签退（状态变为"离岗"）
- 查询员工状态
- 显示在岗员工列表

## 数据库设计

### 表1：adminInfo（管理员表）
| 字段名 | 数据类型 | 长度 | 约束 | 说明 |
|--------|----------|------|------|------|
| adminID | VARCHAR | 20 | PRIMARY KEY | 管理员账号 |
| adminName | VARCHAR | 50 | NOT NULL | 管理员姓名 |
| adminPWD | VARCHAR | 100 | NOT NULL | 管理员密码 |

### 表2：employeeinfo（员工表）
| 字段名 | 数据类型 | 长度 | 约束 | 说明 |
|--------|----------|------|------|------|
| empID | VARCHAR | 20 | PRIMARY KEY | 员工工号 |
| empName | VARCHAR | 50 | NOT NULL | 员工姓名 |
| department | VARCHAR | 50 | NOT NULL | 所属部门 |
| position | VARCHAR | 50 | NOT NULL | 职位 |
| salary | DECIMAL | 10,2 | NOT NULL | 薪资 |

### 表3：attendance（考勤表）
| 字段名 | 数据类型 | 长度 | 约束 | 说明 |
|--------|----------|------|------|------|
| empID | VARCHAR | 20 | PRIMARY KEY / FOREIGN KEY | 员工工号 |
| status | VARCHAR | 20 | NOT NULL DEFAULT '离岗' | 考勤状态（在岗/离岗） |
| lastUpdateTime | DATETIME | - | DEFAULT CURRENT_TIMESTAMP | 最后更新时间 |

## 使用说明

### 首次使用

#### 1. 初始化数据库
```bash
cd ManageSystem
setup_database.bat
```

或手动执行：
```bash
mysql -u root -p < sql/complete_database.sql
```

#### 2. 编译项目
```bash
compile.bat
```

#### 3. 运行程序
```bash
run.bat
```

### 数据库配置
如需修改数据库连接信息，编辑 `src/database.properties`：
```properties
driverClassName=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/student?useSSL=false&serverTimezone=UTC
username=root
password=123456
```

修改后需要重新编译：
```bash
compile.bat
```

## 技术栈
- **语言**: Java SE 8+
- **数据库**: MySQL 8.0
- **JDBC驱动**: mysql-connector-j-8.0.33
- **架构**: MVC三层架构
  - Model: 实体类
  - DAO: 数据访问层
  - View: 视图层（控制台界面）

## 测试数据
系统初始化后会自动创建5个测试员工：
- E001 - 张三 - 技术部 - 软件工程师 - 8000元
- E002 - 李四 - 人事部 - 人事专员 - 6000元
- E003 - 王五 - 财务部 - 会计 - 7000元
- E004 - 赵六 - 技术部 - 项目经理 - 12000元
- E005 - 钱七 - 市场部 - 市场专员 - 5500元

## 注意事项
1. 确保 MySQL 服务已启动
2. 确保数据库用户名密码正确
3. 首次运行前必须执行数据库初始化
4. 添加员工时会自动创建考勤记录（默认离岗）
5. 删除员工时会自动删除对应的考勤记录

## 作者信息
- 作者：why
- 学号：2513313045
- 完成时间：2025年12月
