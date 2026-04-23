import os
import shutil
import zipfile

# 解压模板
src = '../template/实验一done.docx'
dst = '../unpacked_exp2_fix'

if os.path.exists(dst):
    shutil.rmtree(dst)

with zipfile.ZipFile(src, 'r') as zf:
    zf.extractall(dst)

with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 正确的位置：
# 实验二五部分段落结束: 266203 (在 </w:p> 之后)
# 实验二六部分段落开始: 266969 (<w:p ...> 标签开始)

five_end = 266203
six_start = 266969

print(f'五部分结束: {five_end}')
print(f'六部分开始: {six_start}')
print(f'要替换的长度: {six_start - five_end}')

# XML转义
def xml_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# 使用与实验一相同的简单段落格式
def make_para(text):
    escaped = xml_escape(text)
    return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'

def make_para_cn(text):
    escaped = xml_escape(text)
    return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="Times New Roman" w:hint="eastAsia"/><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'

# 第五部分内容
lines = [
    "(一)查询操作",
    "1.在studentsdb数据库中使用SELECT语句进行基本查询。",
    "(1)在student_info表中，查询每个学生的学号、姓名、出生日期信息。",
    "SELECT SNO, SNAME, BIRTH FROM student_info;",
    "(2)查询student_info表学号为0002的学生的姓名和家庭住址。",
    "SELECT SNAME, ADDRESS FROM student_info WHERE SNO='0002';",
    "(3)查询student_info表所有出生日期在95年以后的女同学的姓名和出生日期。",
    "SELECT SNAME, BIRTH FROM student_info WHERE BIRTH>'1995-12-31' AND SEX='女';",
    "2.使用SELECT语句进行条件查询。",
    "(1)在grade表中查询分数在70-80范围内的学生的学号、课程编号和成绩。",
    "SELECT SNO, KCH, SCORE FROM grade WHERE SCORE BETWEEN 70 AND 80;",
    "(2)在grade表中查询课程编号为0002的学生的平均成绩。",
    "SELECT AVG(SCORE) FROM grade WHERE KCH='0002';",
    "(3)在grade表中查询选修课程编号为0003的人数和该课程有成绩的人数。",
    "SELECT COUNT(*), COUNT(SCORE) FROM grade WHERE KCH='0003';",
    "(4)查询student_info的姓名和出生日期，查询结果按出生日期从大到小排序。",
    "SELECT SNAME, BIRTH FROM student_info ORDER BY BIRTH DESC;",
    "(5)查询所有姓\"张\"的学生的学号和姓名。",
    "SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '张%';",
    "3.对student_info表，查询学生的学号、姓名、性别、出生日期及家庭住址，查询结果先按照性别的由小到大排序，性别相同的再按学号由大到小排序。",
    "SELECT SNO, SNAME, SEX, BIRTH, ADDRESS FROM student_info ORDER BY SEX ASC, SNO DESC;",
    "4.使用GROUP BY子句分组查询grade表中各个学生的平均成绩。",
    "SELECT SNO, AVG(SCORE) AS avg_score FROM grade GROUP BY SNO;",
    "5.使用UNION运算符将student_info表中姓\"刘\"的学生的学号、姓名与姓\"张\"的学生的学号、姓名返回在一个表中。",
    "SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '刘%' UNION SELECT SNO, SNAME FROM student_info WHERE SNAME LIKE '张%';",
    "6.嵌套查询",
    "(1)在student_info表中查找与\"刘东阳\"性别相同的所有学生的姓名、出生日期。",
    "SELECT SNAME, BIRTH FROM student_info WHERE SEX=(SELECT SEX FROM student_info WHERE SNAME='刘东阳');",
    "(2)使用IN子查询查找所修课程编号为0002、0005的学生学号、姓名、性别。",
    "SELECT SNO, SNAME, SEX FROM student_info WHERE SNO IN (SELECT SNO FROM grade WHERE KCH IN ('0002','0005'));",
    "(3)使用ANY子查询查找学号为0001的学生的分数比0002号的学生的最低分数高的课程编号和分数。",
    "SELECT KCH, SCORE FROM grade WHERE SNO='0001' AND SCORE>ANY(SELECT SCORE FROM grade WHERE SNO='0002');",
    "(4)使用ALL子查询查找学号为0001的学生的分数比学号为0002的学生的最高成绩还要高的课程编号和分数。",
    "SELECT KCH, SCORE FROM grade WHERE SNO='0001' AND SCORE>ALL(SELECT SCORE FROM grade WHERE SNO='0002');",
    "7.连接查询",
    "(1)查询分数在80-90范围内的学生的学号、姓名、分数。",
    "SELECT s.SNO, s.SNAME, g.SCORE FROM student_info s, grade g WHERE s.SNO=g.SNO AND g.SCORE BETWEEN 80 AND 90;",
    "(2)使用INNER JOIN连接方式查询学习\"数据库原理及应用\"课程的学生学号、姓名、分数。",
    "SELECT s.SNO, s.SNAME, g.SCORE FROM student_info s INNER JOIN grade g ON s.SNO=g.SNO INNER JOIN curriculum c ON g.KCH=c.KCH WHERE c.KCMC='数据库原理及应用';",
    "(3)查询每个学生所选课程的最高成绩，要求列出学号、姓名、最高成绩。",
    "SELECT s.SNO, s.SNAME, MAX(g.SCORE) AS max_score FROM student_info s, grade g WHERE s.SNO=g.SNO GROUP BY s.SNO, s.SNAME;",
    "(4)使用左外连接查询每个学生的总成绩，要求列出学号、姓名、总成绩，没有选修课程的学生的总成绩为空。",
    "SELECT s.SNO, s.SNAME, SUM(g.SCORE) AS total_score FROM student_info s LEFT JOIN grade g ON s.SNO=g.SNO GROUP BY s.SNO, s.SNAME;",
    "(5)为grade表添加数据行：学号为0004、课程编号为0006、分数为76。",
    "INSERT INTO grade VALUES('0004','0006',76);",
    "(6)使用右外连接查询所有课程的选修情况，要求列出课程编号、课程名称、选修人数，curriculum表中没有的课程列值为空。",
    "SELECT c.KCH, c.KCMC, COUNT(g.SNO) AS count FROM grade g RIGHT JOIN curriculum c ON g.KCH=c.KCH GROUP BY c.KCH, c.KCMC;",
    "(二)实验思考",
    "1.查询所有没有选修课程的学生的学号、姓名。",
    "SELECT SNO, SNAME FROM student_info WHERE SNO NOT IN (SELECT DISTINCT SNO FROM grade);",
    "2.查询选修课程的人数。",
    "SELECT COUNT(DISTINCT SNO) FROM grade;",
    "3.查询选课人数大于等于3人的课程编号、课程名称、人数。",
    "SELECT c.KCH, c.KCMC, COUNT(g.SNO) AS count FROM curriculum c, grade g WHERE c.KCH=g.KCH GROUP BY c.KCH, c.KCMC HAVING COUNT(g.SNO)>=3;",
    "4.在查询的FROM子句中实现表与表之间的连接有哪几种方式？对应的关键字分别是什么？",
    "FROM子句中实现表连接有以下几种方式：内连接使用INNER JOIN或JOIN关键字，返回两表中匹配的记录；左外连接使用LEFT JOIN关键字，返回左表所有记录及右表匹配记录；右外连接使用RIGHT JOIN关键字，返回右表所有记录及左表匹配记录；交叉连接使用CROSS JOIN关键字，返回两表的笛卡尔积。",
]

# 生成段落
new_paras = []
for line in lines:
    is_sql = line.startswith('SELECT') or line.startswith('INSERT') or line.startswith('UPDATE') or line.startswith('DELETE')
    if is_sql:
        new_paras.append(make_para(line))
    else:
        new_paras.append(make_para_cn(line))

five_xml = ''.join(new_paras)

# 插入：替换 five_end 到 six_start 之间的内容
new_doc = content[:five_end] + five_xml + content[six_start:]

print(f'添加了 {len(new_paras)} 个段落')

# 写回
with open(f'{dst}/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc)

# 验证XML
from xml.etree import ElementTree as ET
try:
    ET.fromstring(new_doc)
    print('五部分XML验证成功')
except ET.ParseError as e:
    print(f'五部分XML错误: {e}')
    exit(1)

# 添加第六部分
# 重新读取并找到新的位置
with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content2 = f.read()

# 找实验二的六部分（数据查询之后的第一个六、）
data_query_pos = content2.find('数据查询')
six_text_pos = content2.find('六、实验体会和收获', data_query_pos)
print(f'六部分文本位置: {six_text_pos}')

# 找段落结束
six_p_end = content2.find('</w:p>', six_text_pos) + 6
print(f'六段落结束: {six_p_end}')

# 找实验三标题（视图和索引）
exp3_pos = content2.find('视图和索引', six_p_end)
# 找段落开始
exp3_p_start = content2.rfind('<w:p ', 0, exp3_pos)
print(f'实验三段落开始: {exp3_p_start}')

# 心得内容
exp_lines = [
    "通过本次实验，我系统学习和掌握了MySQL数据库的查询操作。实验涵盖了基本查询、条件查询、排序查询、分组查询、嵌套查询和连接查询等多种查询方式，让我对SQL查询语句有了全面的认识。",
    "在基本查询和条件查询中，我学会了使用SELECT语句配合WHERE子句进行数据筛选，掌握了比较运算符、逻辑运算符和BETWEEN、LIKE等特殊运算符的使用方法。",
    "嵌套查询是本次实验的重点内容。通过IN、ANY、ALL等子查询操作符，我学会了如何在查询中嵌套另一个查询，实现更复杂的数据筛选逻辑。连接查询部分让我掌握了内连接、左外连接、右外连接等不同连接方式的应用场景。",
    "实验过程中遇到一些问题，如多表连接时字段名冲突需要使用别名，GROUP BY分组时SELECT字段必须包含在GROUP BY子句或聚合函数中等。这些问题加深了我对SQL语法的理解。",
]

exp_xml = ''.join([make_para_cn(line) for line in exp_lines])

# 插入
new_doc2 = content2[:six_p_end] + exp_xml + content2[exp3_p_start:]

print(f'添加了 {len(exp_lines)} 个心得段落')

# 写回
with open(f'{dst}/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc2)

# 验证
try:
    ET.fromstring(new_doc2)
    print('完整文档XML验证成功')
except ET.ParseError as e:
    print(f'完整文档XML错误: {e}')
    exit(1)

# 打包
output = '../output/实验二报告.docx'
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(dst):
        for file in files:
            file_path = os.path.join(root, file)
            arc_path = os.path.relpath(file_path, dst)
            zf.write(file_path, arc_path)

print(f'输出: {output}')
print(f'大小: {os.path.getsize(output)} bytes')