-- 1. 创建数据库
DROP DATABASE IF EXISTS student;
CREATE DATABASE student DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE student;

-- ========================================
-- 2. 创建表结构
-- ========================================

-- 2.1 管理员表 (adminInfo)
CREATE TABLE IF NOT EXISTS adminInfo (
    adminID   VARCHAR(20)  PRIMARY KEY COMMENT '管理员账号',
    adminName VARCHAR(50)  NOT NULL COMMENT '管理员姓名',
    adminPWD  VARCHAR(100) NOT NULL COMMENT '管理员密码'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='管理员信息表';

-- 2.2 员工表 (employeeinfo)
CREATE TABLE IF NOT EXISTS employeeinfo (
    empID      VARCHAR(20)   PRIMARY KEY COMMENT '员工工号',
    empName    VARCHAR(50)   NOT NULL COMMENT '员工姓名',
    department VARCHAR(50)   NOT NULL COMMENT '所属部门',
    position   VARCHAR(50)   NOT NULL COMMENT '职位',
    salary     DECIMAL(10,2) NOT NULL COMMENT '薪资'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='员工信息表';

-- 2.3 考勤表 (attendance)
CREATE TABLE IF NOT EXISTS attendance (
    empID          VARCHAR(20) PRIMARY KEY COMMENT '员工工号',
    status         VARCHAR(20) NOT NULL DEFAULT '离岗' COMMENT '考勤状态（在岗/离岗）',
    lastUpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    FOREIGN KEY (empID) REFERENCES employeeinfo(empID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='考勤状态表';

-- ========================================
-- 3. 插入测试数据
-- ========================================

-- 3.1 插入测试员工数据
INSERT INTO employeeinfo (empID, empName, department, position, salary) VALUES 
('E001', '张三', '技术部', '软件工程师', 8000.00),
('E002', '李四', '人事部', '人事专员', 6000.00),
('E003', '王五', '财务部', '会计', 7000.00),
('E004', '赵六', '技术部', '项目经理', 12000.00),
('E005', '钱七', '市场部', '市场专员', 5500.00)
ON DUPLICATE KEY UPDATE empName = VALUES(empName);

-- 3.2 初始化考勤记录（默认离岗状态）
INSERT INTO attendance (empID, status)
SELECT empID, '离岗' FROM employeeinfo
ON DUPLICATE KEY UPDATE status = status;
