import re

# Read document.xml
with open('unpacked_exp2/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Find insertion positions
five_pos = content.find('五、问题解答及实验结果', 222000)
five_end_p = content.find('</w:p>', five_pos) + 6  # After </w:p>

six_text_pos = content.find('六、实验体会和收获', five_end_p)
six_start_p = content.rfind('<w:p', 0, six_text_pos)

print(f"Insert position: {five_end_p}")
print(f"Keep position (six start): {six_start_p}")

# XML escape function
def xml_escape(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text

def make_paragraph(text, is_sql=False):
    """Create a paragraph with proper formatting."""
    escaped = xml_escape(text)
    # Font: Chinese 宋体, English Times New Roman; Size: 21 (10.5pt); Line spacing: 240 (single)
    if is_sql:
        # SQL text - use Times New Roman for English parts
        font = 'w:ascii="Times New Roman" w:eastAsia="宋体" w:hAnsi="Times New Roman"'
    else:
        # Chinese text - use 宋体
        font = 'w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="Times New Roman" w:hint="eastAsia"'

    return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:pPr><w:spacing w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts {font}/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr><w:t xml:space="preserve">{escaped}</w:t></w:r></w:p>'

# Experiment 2 content
# (一) 查询操作
exp2_content = []

# 1. 基本查询
exp2_content.append("(一)查询操作")
exp2_content.append("1.在studentsdb数据库中使用SELECT语句进行基本查询。")
exp2_content.append("（1）在student_info表中，查询每个学生的学号、姓名、出生日期信息。")
exp2_content.append("SELECT SNO, SNAME, BIRTH FROM student_info;", is_sql=True)
exp2_content.append("（2）查询student_info表学号为0002的学生的姓名和家庭住址。")
exp2_content.append("SELECT SNAME, ADDRESS FROM student_info WHERE SNO='0002';", is_sql=True)
exp2_content.append("（3）查询student_info表所有出生日期在95年以后的女同学的姓名和出生日期。")
exp2_content.append("SELECT SNAME, BIRTH FROM student_info WHERE BIRTH>'1995-12-31' AND SEX='女';", is_sql=True)

# 2. 条件查询
exp2_content.append("2.使用SELECT语句进行条件查询。")
exp2_content.append("（1）在grade表中查询分数在70-80范围内的学生的学号、课程编号和成绩。")
exp2_content.append("SELECT SNO, KCH, SCORE FROM grade WHERE SCORE BETWEEN 70 AND 80;", is_sql=True)
exp2_content.append("（2）在grade表中查询课程编号为0002的学生的平均成绩。")
exp2_content.append("SELECT AVG(SCORE) FROM grade WHERE KCH='0002';", is_sql=True)
exp2_content.append("（3）在grade表中查询选修课程编号为0003的人数和该课程有成绩的人数。")
exp2_content.append("SELECT COUNT(*), COUNT(SCORE) FROM grade WHERE KCH='0003';", is_sql=True)
exp2_content.append("（4）查询student_info的姓名和出生日期，查询结果按出生日期从大到小排序。")
exp2_content.append("SELECT SNAME, BIRTH FROM student_info ORDER BY BIRTH DESC;", is_sql=True)
exp2_content.append("（5）查询所有姓"张"的学生的学号和姓名。")
exp2_content.append("SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '张%';", is_sql=True)

# 3. 复合排序
exp2_content.append("3.对student_info表，查询学生的学号、姓名、性别、出生日期及家庭住址，查询结果先按照性别的由小到大排序，性别相同的再按学号由大到小排序。")
exp2_content.append("SELECT SNO, SNAME, SEX, BIRTH, ADDRESS FROM student_info ORDER BY SEX ASC, SNO DESC;", is_sql=True)

# 4. GROUP BY
exp2_content.append("4.使用GROUP BY子句分组查询grade表中各个学生的平均成绩。")
exp2_content.append("SELECT SNO, AVG(SCORE) AS avg_score FROM grade GROUP BY SNO;", is_sql=True)

# 5. UNION
exp2_content.append("5.使用UNION运算符将student_info表中姓"刘"的学生的学号、姓名与姓"张"的学生的学号、姓名返回在一个表中。")
exp2_content.append("SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '刘%' UNION SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '张%';", is_sql=True)

# 6. 嵌套查询
exp2_content.append("6.嵌套查询")
exp2_content.append("（1）在student_info表中查找与"刘东阳"性别相同的所有学生的姓名、出生日期。")
exp2_content.append("SELECT SNAME, BIRTH FROM student_info WHERE SEX=(SELECT SEX FROM student_info WHERE SNAME='刘东阳');", is_sql=True)
exp2_content.append("（2）使用IN子查询查找所修课程编号为0002、0005的学生学号、姓名、性别。")
exp2_content.append("SELECT SNO, SNAME, SEX FROM student_info WHERE SNO IN (SELECT SNO FROM grade WHERE KCH IN ('0002','0005'));", is_sql=True)
exp2_content.append("（3）使用ANY子查询查找学号为0001的学生的分数比0002号的学生的最低分数高的课程编号和分数。")
exp2_content.append("SELECT KCH, SCORE FROM grade WHERE SNO='0001' AND SCORE>ANY(SELECT SCORE FROM grade WHERE SNO='0002');", is_sql=True)
exp2_content.append("（4）使用ALL子查询查找学号为0001的学生的分数比学号为0002的学生的最高成绩还要高的课程编号和分数。")
exp2_content.append("SELECT KCH, SCORE FROM grade WHERE SNO='0001' AND SCORE>ALL(SELECT SCORE FROM grade WHERE SNO='0002');", is_sql=True)

# 7. 连接查询
exp2_content.append("7.连接查询")
exp2_content.append("（1）查询分数在80-90范围内的学生的学号、姓名、分数。")
exp2_content.append("SELECT s.SNO, s.SNAME, g.SCORE FROM student_info s, grade g WHERE s.SNO=g.SNO AND g.SCORE BETWEEN 80 AND 90;", is_sql=True)
exp2_content.append("（2）使用INNER JOIN连接方式查询学习"数据库原理及应用"课程的学生学号、姓名、分数。")
exp2_content.append("SELECT s.SNO, s.SNAME, g.SCORE FROM student_info s INNER JOIN grade g ON s.SNO=g.SNO INNER JOIN curriculum c ON g.KCH=c.KCH WHERE c.KCMC='数据库原理及应用';", is_sql=True)
exp2_content.append("（3）查询每个学生所选课程的最高成绩，要求列出学号、姓名、最高成绩。")
exp2_content.append("SELECT s.SNO, s.SNAME, MAX(g.SCORE) AS max_score FROM student_info s, grade g WHERE s.SNO=g.SNO GROUP BY s.SNO, s.SNAME;", is_sql=True)
exp2_content.append("（4）使用左外连接查询每个学生的总成绩，要求列出学号、姓名、总成绩，没有选修课程的学生的总成绩为空。")
exp2_content.append("SELECT s.SNO, s.SNAME, SUM(g.SCORE) AS total_score FROM student_info s LEFT JOIN grade g ON s.SNO=g.SNO GROUP BY s.SNO, s.SNAME;", is_sql=True)
exp2_content.append("（5）为grade表添加数据行：学号为0004、课程编号为0006、分数为76。")
exp2_content.append("INSERT INTO grade VALUES('0004','0006',76);", is_sql=True)
exp2_content.append("（6）使用右外连接查询所有课程的选修情况，要求列出课程编号、课程名称、选修人数，curriculum表中没有的课程列值为空。")
exp2_content.append("SELECT c.KCH, c.KCMC, COUNT(g.SNO) AS count FROM grade g RIGHT JOIN curriculum c ON g.KCH=c.KCH GROUP BY c.KCH, c.KCMC;", is_sql=True)

# (二) 实验思考
exp2_content.append("(二)实验思考")
exp2_content.append("1.查询所有没有选修课程的学生的学号、姓名。")
exp2_content.append("SELECT SNO, SNAME FROM student_info WHERE SNO NOT IN (SELECT DISTINCT SNO FROM grade);", is_sql=True)
exp2_content.append("2.查询选修课程的人数。")
exp2_content.append("SELECT COUNT(DISTINCT SNO) FROM grade;", is_sql=True)
exp2_content.append("3.查询选课人数大于等于3人的课程编号、课程名称、人数。")
exp2_content.append("SELECT c.KCH, c.KCMC, COUNT(g.SNO) AS count FROM curriculum c, grade g WHERE c.KCH=g.KCH GROUP BY c.KCH, c.KCMC HAVING COUNT(g.SNO)>=3;", is_sql=True)
exp2_content.append("4.在查询的FROM子句中实现表与表之间的连接有哪几种方式？对应的关键字分别是什么？")
exp2_content.append("FROM子句中实现表连接有以下几种方式：（1）内连接：使用INNER JOIN或JOIN关键字，返回两表中匹配的记录。（2）左外连接：使用LEFT JOIN或LEFT OUTER JOIN关键字，返回左表所有记录及右表匹配记录。（3）右外连接：使用RIGHT JOIN或RIGHT OUTER JOIN关键字，返回右表所有记录及左表匹配记录。（4）交叉连接：使用CROSS JOIN关键字，返回两表的笛卡尔积。（5）自然连接：使用NATURAL JOIN关键字，自动按同名列连接。")

# Generate XML paragraphs
new_xml_parts = []
for item in exp2_content:
    if isinstance(item, tuple):
        text, is_sql = item
    else:
        text = item
        is_sql = False
    new_xml_parts.append(make_paragraph(text, is_sql))

new_xml = ''.join(new_xml_parts)

# Insert new content - replace empty paragraphs between five and six
new_doc = content[:five_end_p] + new_xml + content[six_start_p:]

# Write back
with open('unpacked_exp2/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print(f"Added {len(exp2_content)} paragraphs")
print("Document updated")