-- 实验(三) 建表同时实现完整性约束
-- 第1题: 创建students数据库和stu表
CREATE DATABASE students;
USE students;

CREATE TABLE stu (
    SNO CHAR(4) NOT NULL PRIMARY KEY,
    SNAME CHAR(8),
    SEX CHAR(2),
    BIRTH DATE
);

-- 第2题: 创建表sc
CREATE TABLE sc (
    SNO CHAR(4) NOT NULL,
    KCH CHAR(4) NOT NULL,
    SCORE DECIMAL(5,2),
    PRIMARY KEY (SNO, KCH),
    CONSTRAINT fk_sno FOREIGN KEY (SNO) REFERENCES stu(SNO),
    CHECK (SCORE >= 0 AND SCORE <= 100)
);

-- 第3题: 创建表course
CREATE TABLE course (
    KCH CHAR(4) NOT NULL,
    KCM CHAR(20),
    CREDIT INT,
    CONSTRAINT uq_cname UNIQUE (KCM)
);

-- 第4题: 在course表课号列建立主键约束
ALTER TABLE course ADD PRIMARY KEY (KCH);

-- 第5题: 在sc表课号列建立外键约束fk_cno，级联更新
ALTER TABLE sc ADD CONSTRAINT fk_cno FOREIGN KEY (KCH) REFERENCES course(KCH) ON UPDATE CASCADE;

-- 第6题: 在stu表姓名列建立唯一约束uq_sname
ALTER TABLE stu ADD CONSTRAINT uq_sname UNIQUE (SNAME);

-- 第7题: 在course表学分列建立检查约束ck_xf
ALTER TABLE course ADD CONSTRAINT ck_xf CHECK (CREDIT > 0);

-- 第8题: 删除sc表的外键约束fk_cno和fk_sno
ALTER TABLE sc DROP FOREIGN KEY fk_cno;
ALTER TABLE sc DROP FOREIGN KEY fk_sno;

-- 第9题: 删除stu表的主键约束
ALTER TABLE stu DROP PRIMARY KEY;

-- 第10题: 删除course表的唯一约束uq_cname
ALTER TABLE course DROP INDEX uq_cname;