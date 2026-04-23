import os
import shutil
import zipfile

# 解压模板
src = '../template/实验二done.docx'
dst = 'unpacked_exp3_gen'

if os.path.exists(dst):
    shutil.rmtree(dst)

with zipfile.ZipFile(src, 'r') as zf:
    zf.extractall(dst)

# 读取document.xml
with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 实验三关键位置（已分析得出）
exp3_five_end = 395302    # 五部分段落结束
exp3_six_p_start = 396632  # 六部分段落开始
exp3_six_end = 397112      # 六部分段落结束
exp4_p_start = 463356      # 实验四段落开始

print(f'五结束: {exp3_five_end}, 六开始: {exp3_six_p_start}')
print(f'六结束: {exp3_six_end}, 实验四开始: {exp4_p_start}')

# XML转义
def xml_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# 段落格式
def make_para(text):
    escaped = xml_escape(text)
    return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'

def make_para_cn(text):
    escaped = xml_escape(text)
    return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="Times New Roman" w:hint="eastAsia"/><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'

# 第五部分内容
lines = [
    "(一)索引的创建与维护",
    "1.使用SQL语句ALTER TABLE分别删除studentsdb数据库的student_info表、grade表和curriculum表的主键索引。",
    "ALTER TABLE student_info DROP PRIMARY KEY;",
    "ALTER TABLE grade DROP PRIMARY KEY;",
    "ALTER TABLE curriculum DROP PRIMARY KEY;",
    "2.使用SQL语句为curriculum表的课程编号创建唯一性索引，索引名为cno_idx。",
    "CREATE UNIQUE INDEX cno_idx ON curriculum(KCH);",
    "3.使用SQL语句为grade表的"分数"字段创建一个普通索引，索引名为grade_idx。",
    "CREATE INDEX grade_idx ON grade(SCORE);",
    "4.使用SQL语句为grade表的"学号"和"课程编号"字段创建一个复合唯一索引，索引名为grade_sid_cid_idx。",
    "CREATE UNIQUE INDEX grade_sid_cid_idx ON grade(SNO, KCH);",
    "5.查看grade表上的索引信息。",
    "SHOW INDEX FROM grade;",
    "6.使用SQL语句删除索引grade_idx，再次查看grade表上的索引信息。",
    "DROP INDEX grade_idx ON grade;",
    "SHOW INDEX FROM grade;",
    "(二)视图的创建与维护",
    "1.使用SQL语句CREATE VIEW创建一个名为v_stu_c的视图，显示学生的学号、姓名及其选修课程的课程编号，并利用该视图查询学号为0003的学生信息。",
    "CREATE VIEW v_stu_c AS SELECT s.SNO, s.SNAME, g.KCH FROM student_info s, grade g WHERE s.SNO=g.SNO;",
    "SELECT * FROM v_stu_c WHERE SNO='0003';",
    "2.基于student_info表、curriculum表和grade表，创建一个名为v_stu_g的视图，视图包括学生的学号、姓名、课程名称、分数，并使用该视图v_stu_g查询学号为0001的学生的课程平均分。",
    "CREATE VIEW v_stu_g AS SELECT s.SNO, s.SNAME, c.KCMC, g.SCORE FROM student_info s, grade g, curriculum c WHERE s.SNO=g.SNO AND g.KCH=c.KCH;",
    "SELECT SNO, SNAME, AVG(SCORE) FROM v_stu_g WHERE SNO='0001';",
    "3.使用SQL语句修改视图v_stu_g，显示学生的学号、姓名、性别。",
    "ALTER VIEW v_stu_g AS SELECT SNO, SNAME, SEX FROM student_info;",
    "4.利用视图v_stu_g为student_info表插入一条数据，学号为0010，姓名为"曾一"，性别为女。",
    "INSERT INTO v_stu_g VALUES('0010', '曾一', '女');",
    "5.利用视图v_stu_g删除学号为0010的学生记录。",
    "DELETE FROM v_stu_g WHERE SNO='0010';",
    "6.利用视图v_stu_g修改曾一学号为0001的高等数学的分数为87。",
    "ALTER VIEW v_stu_g AS SELECT s.SNO, s.SNAME, c.KCMC, g.SCORE FROM student_info s, grade g, curriculum c WHERE s.SNO=g.SNO AND g.KCH=c.KCH;",
    "UPDATE v_stu_g SET SCORE=87 WHERE SNO='0001' AND KCMC='高等数学';",
    "7.使用SQL语句删除视图v_stu_c和v_stu_g。",
    "DROP VIEW v_stu_c;",
    "DROP VIEW v_stu_g;",
    "(三)实验思考",
    "1.简述索引的目的。什么情况下不适合在表上建立索引？",
    "索引可以加快数据查询速度，提高数据库性能。不适合建立索引的情况包括：数据量小的表、频繁更新的表、重复值多的字段、查询很少但更新频繁的字段。",
    "2.能否在视图上建立索引？",
    "MySQL不支持在视图上直接建立索引，但可以对视图引用的基表建立索引来间接提高视图查询效率。",
    "3.通过视图修改表数据，视图应具备哪些条件？",
    "视图必须包含基表的主键或唯一键字段；不能包含聚合函数、DISTINCT、GROUP BY、HAVING、UNION等；视图必须与基表一一对应（不能是多表连接的复杂视图）；不能包含子查询。",
    "4.简述视图的作用。",
    "视图的作用包括：简化复杂查询，将多表连接封装为单一视图；保护数据安全，限制用户只能访问特定数据；提供数据独立性，隐藏底层表结构变化；方便数据展示，自定义数据呈现方式。",
]

# 生成段落
new_paras = []
for line in lines:
    is_sql = line.startswith('SELECT') or line.startswith('INSERT') or line.startswith('UPDATE') or line.startswith('DELETE') or line.startswith('CREATE') or line.startswith('ALTER') or line.startswith('DROP') or line.startswith('SHOW')
    if is_sql:
        new_paras.append(make_para(line))
    else:
        new_paras.append(make_para_cn(line))

five_xml = ''.join(new_paras)

# 插入五部分内容
new_doc = content[:exp3_five_end] + five_xml + content[exp3_six_p_start:]

print(f'添加了 {len(new_paras)} 个五部分段落')

# 写回
with open(f'{dst}/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc)

# 验证XML
from xml.etree import ElementTree as ET
try:
    ET.fromstring(new_doc)
    print('五部分XML验证成功')
except ET.ParseError as e:
    print(f'XML错误: {e}')
    exit(1)

# 添加六部分（实验体会）
# 重新读取
with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content2 = f.read()

# 找实验三六部分结束位置
import re
six_matches = [(m.start(), m.group()) for m in re.finditer(r'六、实验体会和收获', content2)]
print(f'六部分标题数量: {len(six_matches)}')

# 实验三六部分是第三个
exp3_six_pos = six_matches[2][0]
exp3_six_p_end = content2.find('</w:p>', exp3_six_pos) + 6
print(f'六段落结束: {exp3_six_p_end}')

# 找实验四段落开始（第四个五部分）
five_matches = [(m.start(), m.group()) for m in re.finditer(r'五、问题解答及实验结果', content2)]
exp4_five_pos = five_matches[3][0]
exp4_p_start_new = content2.rfind('<w:p ', 0, exp4_five_pos)
print(f'实验四段落开始: {exp4_p_start_new}')

# 心得内容
exp_lines = [
    "通过本次实验，我系统学习了MySQL数据库中索引和视图的创建与管理方法。索引部分让我理解了如何通过创建索引来提高查询效率，以及不同类型索引（普通索引、唯一索引、复合索引）的应用场景和使用方法。",
    "在索引实验中，我掌握了使用ALTER TABLE删除主键索引、使用CREATE INDEX创建各种类型索引、使用SHOW INDEX查看索引信息、使用DROP INDEX删除索引的操作。理解了索引虽然能提高查询速度，但会降低更新效率，需要在实际应用中权衡。",
    "视图部分让我理解了视图作为虚拟表的概念，掌握了CREATE VIEW创建视图、ALTER VIEW修改视图、DROP VIEW删除视图的操作。实验中还学习了如何通过视图进行数据的查询、插入、删除和修改，理解了可更新视图的条件限制。",
    "实验过程中遇到一些问题，如删除主键时需要考虑表的外键约束关系，通过视图修改数据时视图必须满足可更新条件等。这些问题加深了我对索引和视图的理解，为后续学习存储过程和触发器奠定了基础。",
]

exp_xml = ''.join([make_para_cn(line) for line in exp_lines])

# 插入六部分内容
new_doc2 = content2[:exp3_six_p_end] + exp_xml + content2[exp4_p_start_new:]

print(f'添加了 {len(exp_lines)} 个心得段落')

# 写回
with open(f'{dst}/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc2)

# 验证
try:
    ET.fromstring(new_doc2)
    print('完整文档XML验证成功')
except ET.ParseError as e:
    print(f'XML错误: {e}')
    exit(1)

# 打包
output = '../output/实验三报告.docx'
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(dst):
        for file in files:
            file_path = os.path.join(root, file)
            arc_path = os.path.relpath(file_path, dst)
            zf.write(file_path, arc_path)

print(f'输出: {output}')
print(f'大小: {os.path.getsize(output)} bytes')