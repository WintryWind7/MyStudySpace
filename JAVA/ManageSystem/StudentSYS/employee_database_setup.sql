-- Employee Management System Database Setup
USE student;

-- Create employee table
CREATE TABLE IF NOT EXISTS employeeinfo (
    empID VARCHAR(20) PRIMARY KEY,
    empName VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    position VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert test employee data
INSERT INTO employeeinfo (empID, empName, department, position, salary) VALUES 
('E001', '张三', '技术部', '软件工程师', 8000.00),
('E002', '李四', '人事部', '人事专员', 6000.00),
('E003', '王五', '财务部', '会计', 7000.00),
('E004', '赵六', '技术部', '项目经理', 12000.00),
('E005', '钱七', '市场部', '市场专员', 5500.00)
ON DUPLICATE KEY UPDATE empName = VALUES(empName);

SELECT 'Employee database setup completed!' AS message;