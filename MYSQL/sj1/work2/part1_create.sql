-- 实验(一) 建库、建表及表结构维护
-- 第1题: 创建数据库studentsdb
CREATE DATABASE studentsdb;

-- 第2题: 选择studentsdb为当前使用数据库
USE studentsdb;

-- 第3题: 创建数据表student_info、curriculum、grade
CREATE TABLE student_info (
    SNO CHAR(4) NOT NULL PRIMARY KEY COMMENT '学号',
    SNAME CHAR(8) NOT NULL COMMENT '姓名',
    SEX CHAR(2) COMMENT '性别',
    BIRTH DATE COMMENT '出生日期',
    ADDRESS VARCHAR(50) COMMENT '家庭住址'
);

CREATE TABLE curriculum (
    KCH CHAR(4) NOT NULL PRIMARY KEY COMMENT '课程编号',
    KCM VARCHAR(50) COMMENT '课程名称',
    CREDIT INT COMMENT '学分'
);

CREATE TABLE grade (
    SNO CHAR(4) NOT NULL COMMENT '学号',
    KCH CHAR(4) NOT NULL COMMENT '课程编号',
    SCORE INT COMMENT '分数',
    PRIMARY KEY (SNO, KCH)
);

-- 第4题: 修改curriculum表的"KCM"列名称改为"KCMC"
ALTER TABLE curriculum CHANGE KCM KCMC VARCHAR(50);

-- 第5题: 修改grade表的"SCORE"列数据类型为decimal(5,2)
ALTER TABLE grade MODIFY SCORE DECIMAL(5,2);

-- 第6题: 为student_info表添加"Remark"列
ALTER TABLE student_info ADD Remark VARCHAR(50);

-- 第7题: 创建数据库studb并创建表stu1
CREATE DATABASE studb;
CREATE TABLE studb.stu1 LIKE studentsdb.student_info;

-- 第8题: 删除表stu1的"备注"列
ALTER TABLE studb.stu1 DROP COLUMN Remark;

-- 第9题: 删除表stu1
DROP TABLE studb.stu1;

-- 第10题: 删除数据库studb
DROP DATABASE studb;