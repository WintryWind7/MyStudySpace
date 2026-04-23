-- 实验二 数据查询 SQL命令
-- =============================================
-- 注意：请确保先执行完实验一，数据库studentsdb已存在并包含数据
-- 实验一后的数据状态：
--   - 学号0008已删除
--   - "计算机应用基础"课程选课已删除
--   - 学号0002地址已更新为"滨江市新建路196号"
--   - "数据库原理及应用"课程成绩已更新为0
-- =============================================

USE studentsdb;

-- =============================================
-- (一) 查询操作
-- =============================================

-- 1. 基本查询
-- (1) 查询每个学生的学号、姓名、出生日期
SELECT SNO, SNAME, BIRTH FROM student_info;

-- (2) 查询学号0002的学生的姓名和家庭住址
SELECT SNAME, ADDRESS FROM student_info WHERE SNO='0002';

-- (3) 查询出生日期在95年以后的女同学的姓名和出生日期
SELECT SNAME, BIRTH FROM student_info WHERE BIRTH>'1995-12-31' AND SEX='女';

-- 2. 条件查询
-- (1) 查询分数在70-80范围内的学生学号、课程编号和成绩
SELECT SNO, KCH, SCORE FROM grade WHERE SCORE BETWEEN 70 AND 80;

-- (2) 查询课程编号0002的平均成绩
SELECT AVG(SCORE) FROM grade WHERE KCH='0002';

-- (3) 查询选修课程编号0003的人数和有成绩的人数
SELECT COUNT(*), COUNT(SCORE) FROM grade WHERE KCH='0003';

-- (4) 查询姓名和出生日期，按出生日期从大到小排序
SELECT SNAME, BIRTH FROM student_info ORDER BY BIRTH DESC;

-- (5) 查询所有姓"张"的学生学号和姓名
SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '张%';

-- 3. 复合排序：先按性别升序，再按学号降序
SELECT SNO, SNAME, SEX, BIRTH, ADDRESS FROM student_info ORDER BY SEX ASC, SNO DESC;

-- 4. 分组查询各学生的平均成绩
SELECT SNO, AVG(SCORE) AS avg_score FROM grade GROUP BY SNO;

-- 5. UNION查询姓"刘"和姓"张"的学生
SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '刘%'
UNION
SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '张%';

-- 6. 嵌套查询
-- (1) 与"刘东阳"性别相同的学生的姓名、出生日期
SELECT SNAME, BIRTH FROM student_info
WHERE SEX=(SELECT SEX FROM student_info WHERE SNAME='刘东阳');

-- (2) IN子查询：选修课程0002或0005的学生
SELECT SNO, SNAME, SEX FROM student_info
WHERE SNO IN (SELECT SNO FROM grade WHERE KCH IN ('0002','0005'));

-- (3) ANY子查询：0001号学生分数比0002号最低分高的课程
SELECT KCH, SCORE FROM grade WHERE SNO='0001'
AND SCORE>ANY(SELECT SCORE FROM grade WHERE SNO='0002');

-- (4) ALL子查询：0001号学生分数比0002号最高分还高的课程
SELECT KCH, SCORE FROM grade WHERE SNO='0001'
AND SCORE>ALL(SELECT SCORE FROM grade WHERE SNO='0002');

-- 7. 连接查询
-- (1) 分数80-90范围内的学生学号、姓名、分数
SELECT s.SNO, s.SNAME, g.SCORE
FROM student_info s, grade g
WHERE s.SNO=g.SNO AND g.SCORE BETWEEN 80 AND 90;

-- (2) INNER JOIN查询"数据库原理及应用"课程的学生
SELECT s.SNO, s.SNAME, g.SCORE
FROM student_info s
INNER JOIN grade g ON s.SNO=g.SNO
INNER JOIN curriculum c ON g.KCH=c.KCH
WHERE c.KCMC='数据库原理及应用';

-- (3) 每个学生所选课程的最高成绩
SELECT s.SNO, s.SNAME, MAX(g.SCORE) AS max_score
FROM student_info s, grade g
WHERE s.SNO=g.SNO
GROUP BY s.SNO, s.SNAME;

-- (4) 左外连接查询每个学生的总成绩
SELECT s.SNO, s.SNAME, SUM(g.SCORE) AS total_score
FROM student_info s
LEFT JOIN grade g ON s.SNO=g.SNO
GROUP BY s.SNO, s.SNAME;

-- (5) 为grade表添加数据：学号0004、课程0006、分数76
INSERT INTO grade VALUES('0004','0006',76);

-- (6) 右外连接查询所有课程的选修情况
SELECT c.KCH, c.KCMC, COUNT(g.SNO) AS count
FROM grade g
RIGHT JOIN curriculum c ON g.KCH=c.KCH
GROUP BY c.KCH, c.KCMC;

-- =============================================
-- (二) 实验思考
-- =============================================

-- 1. 查询没有选修课程的学生
SELECT SNO, SNAME FROM student_info
WHERE SNO NOT IN (SELECT DISTINCT SNO FROM grade);

-- 2. 查询选修课程的人数
SELECT COUNT(DISTINCT SNO) FROM grade;

-- 3. 查询选课人数>=3的课程
SELECT c.KCH, c.KCMC, COUNT(g.SNO) AS count
FROM curriculum c, grade g
WHERE c.KCH=g.KCH
GROUP BY c.KCH, c.KCMC
HAVING COUNT(g.SNO)>=3;