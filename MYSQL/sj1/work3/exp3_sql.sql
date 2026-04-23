-- 实验三 视图和索引 SQL命令
-- =============================================

USE studentsdb;

-- =============================================
-- (一) 索引的创建与维护
-- =============================================

-- 1. 删除主键索引
ALTER TABLE student_info DROP PRIMARY KEY;
ALTER TABLE grade DROP PRIMARY KEY;
ALTER TABLE curriculum DROP PRIMARY KEY;

-- 2. 创建唯一性索引
CREATE UNIQUE INDEX cno_idx ON curriculum(KCH);

-- 3. 创建普通索引
CREATE INDEX grade_idx ON grade(SCORE);

-- 4. 创建复合唯一索引
CREATE UNIQUE INDEX grade_sid_cid_idx ON grade(SNO, KCH);

-- 5. 查看索引信息
SHOW INDEX FROM grade;

-- 6. 删除索引
DROP INDEX grade_idx ON grade;
SHOW INDEX FROM grade;

-- =============================================
-- (二) 视图的创建与维护
-- =============================================

-- 1. 创建视图v_stu_c
CREATE VIEW v_stu_c AS
SELECT s.SNO, s.SNAME, g.KCH
FROM student_info s, grade g
WHERE s.SNO=g.SNO;

-- 查询学号0003的学生信息
SELECT * FROM v_stu_c WHERE SNO='0003';

-- 2. 创建视图v_stu_g
CREATE VIEW v_stu_g AS
SELECT s.SNO, s.SNAME, c.KCMC, g.SCORE
FROM student_info s, grade g, curriculum c
WHERE s.SNO=g.SNO AND g.KCH=c.KCH;

-- 查询学号0001的课程平均分
SELECT SNO, SNAME, AVG(SCORE) FROM v_stu_g WHERE SNO='0001';

-- 3. 修改视图v_stu_g
ALTER VIEW v_stu_g AS
SELECT SNO, SNAME, SEX FROM student_info;

-- 4. 通过视图插入数据
INSERT INTO v_stu_g VALUES('0010', '曾一', '女');

-- 5. 通过视图删除数据
DELETE FROM v_stu_g WHERE SNO='0010';

-- 6. 通过视图修改数据
-- 注意：需要先恢复原视图才能修改分数
ALTER VIEW v_stu_g AS
SELECT s.SNO, s.SNAME, c.KCMC, g.SCORE
FROM student_info s, grade g, curriculum c
WHERE s.SNO=g.SNO AND g.KCH=c.KCH;

UPDATE v_stu_g SET SCORE=87 WHERE SNO='0001' AND KCMC='计算机基础';

-- 7. 删除视图
DROP VIEW v_stu_c;
DROP VIEW v_stu_g;

-- =============================================
-- (三) 实验思考
-- =============================================

-- 思考题1: 索引的作用和适用场景
-- 答：索引可以加快数据查询速度，适用于频繁查询但很少更新的字段，
--     不适用于频繁更新、数据量小或重复值多的字段。

-- 思考题2: 能否在视图上创建索引
-- 答：MySQL不支持在视图上直接创建索引，但可以对视图引用的基表创建索引。

-- 思考题3: 通过视图修改表数据需要的条件
-- 答：视图必须包含基表的主键或唯一键，不能包含聚合函数、DISTINCT、
--     GROUP BY、HAVING、UNION等，且视图必须与基表一一对应。

-- 思考题4: 视图的作用
-- 答：简化复杂查询、保护数据安全、提供数据独立性、隐藏表结构细节。