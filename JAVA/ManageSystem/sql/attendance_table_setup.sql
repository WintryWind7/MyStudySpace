-- Attendance Status Table Setup
USE student;

-- Create attendance status table
CREATE TABLE IF NOT EXISTS attendance (
    empID VARCHAR(20) PRIMARY KEY,
    status VARCHAR(20) NOT NULL DEFAULT '离岗',
    lastUpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (empID) REFERENCES employeeinfo(empID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Initialize attendance records for existing employees
INSERT INTO attendance (empID, status)
SELECT empID, '离岗' FROM employeeinfo
ON DUPLICATE KEY UPDATE status = status;

SELECT 'ManageSystem attendance table setup completed!' AS message;
