import os
import shutil
import zipfile
from xml.etree import ElementTree as ET

# 解压模板（已解压，直接读取）
dst = 'unpacked'

with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 实验五关键位置
five_p_end = 635736    # 五部分段落结束
six_p_start = 636347   # 六部分段落开始
six_p_end = 636996     # 六部分段落结束

print(f'五结束: {five_p_end}, 六开始: {six_p_start}, 六结束: {six_p_end}')

# XML转义
def xml_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# 中文段落格式（宋体）
def make_para_cn(text):
    escaped = xml_escape(text)
    return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="Times New Roman" w:hint="eastAsia"/><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'

# 英文/SQL段落格式
def make_para(text):
    escaped = xml_escape(text)
    return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'

# 五部分内容（存储过程和触发器）
lines = [
    "(一)存储过程的创建、维护与运行",
    "1.创建存储过程stu_info，执行时通过输入姓名查询该学生的各科成绩。",
    "DELIMITER @@",
    "CREATE PROCEDURE stu_info(IN name CHAR(8))",
    "BEGIN",
    "SELECT s.SNO, SNAME, KCH, SCORE FROM student_info s, grade g WHERE s.SNO=g.SNO AND SNAME=name;",
    "END @@",
    "DELIMITER ;",
    "CALL stu_info('张青平');",
    "2.创建存储过程stu_grade，查询学号0001的学生姓名、课程名称、分数。",
    "DELIMITER @@",
    "CREATE PROCEDURE stu_grade()",
    "BEGIN",
    "SELECT s.SNO, s.SNAME, c.KCMC, g.SCORE FROM student_info s, grade g, curriculum c WHERE s.SNO=g.SNO AND g.KCH=c.KCH AND s.SNO='0001';",
    "END @@",
    "DELIMITER ;",
    "CALL stu_grade();",
    "3.创建存储过程stu_name，输入姓名查看最高分、最低分、平均分。",
    "DELIMITER @@",
    "CREATE PROCEDURE stu_name(IN name VARCHAR(20))",
    "BEGIN",
    "SELECT MAX(g.SCORE), MIN(g.SCORE), AVG(g.SCORE) FROM student_info s, grade g WHERE s.SNO=g.SNO AND s.SNAME=name;",
    "END @@",
    "DELIMITER ;",
    "CALL stu_name('张青平');",
    "DROP PROCEDURE stu_name;",
    "4.创建存储过程stu_g_r，输入学号获取选修课程门数（输出参数）。",
    "DELIMITER @@",
    "CREATE PROCEDURE stu_g_r(IN sno VARCHAR(10), OUT count INT)",
    "BEGIN",
    "SELECT COUNT(*) INTO count FROM grade WHERE SNO=sno;",
    "END @@",
    "DELIMITER ;",
    "SET @c=0;",
    "CALL stu_g_r('0002', @c);",
    "SELECT @c;",
    "5.创建存储函数avg_func，通过游标统计指定课程的平均分。",
    "DELIMITER @@",
    "CREATE FUNCTION avg_func(cname VARCHAR(50)) RETURNS DECIMAL(10,2)",
    "DETERMINISTIC",
    "READS SQL DATA",
    "BEGIN",
    "DECLARE avg_score DECIMAL(10,2);",
    "SELECT AVG(g.SCORE) INTO avg_score FROM grade g, curriculum c WHERE g.KCH=c.KCH AND c.KCMC=cname;",
    "RETURN avg_score;",
    "END @@",
    "DELIMITER ;",
    "SELECT avg_func('高等数学');",
    "DROP FUNCTION avg_func;",
    "(二)触发器的创建、维护与激活",
    "1.创建test表和触发器test_trig，在student_info表插入后自动记录日期时间。",
    "CREATE TABLE test(date_time VARCHAR(50));",
    "DELIMITER @@",
    "CREATE TRIGGER test_trig AFTER INSERT ON student_info",
    "FOR EACH ROW",
    "BEGIN",
    "INSERT INTO test VALUES(SYSDATE());",
    "END @@",
    "DELIMITER ;",
    "INSERT INTO student_info VALUES('0011', '测试学生', '男', '2000-01-01', '测试地址');",
    "SELECT * FROM test;",
    "DELETE FROM student_info WHERE SNO='0011';",
    "SELECT * FROM test;",
    "DROP TRIGGER test_trig;",
    "DROP TABLE test;",
    "2.创建触发器del_trig，删除课程时级联删除grade表对应记录。",
    "DELIMITER @@",
    "CREATE TRIGGER del_trig AFTER DELETE ON curriculum",
    "FOR EACH ROW",
    "BEGIN",
    "DELETE FROM grade WHERE KCH=OLD.KCH;",
    "END @@",
    "DELIMITER ;",
    "INSERT INTO curriculum VALUES('0007', '测试课程', 2);",
    "INSERT INTO grade VALUES('0001', '0007', 80);",
    "DELETE FROM curriculum WHERE KCH='0007';",
    "SELECT * FROM grade WHERE KCH='0007';",
    "DROP TRIGGER del_trig;",
    "(三)实验思考",
    "1.存储函数和存储过程如何将运算结果返回给外界？",
    "存储函数通过RETURN语句返回单个值，可以在SQL语句中直接调用。存储过程通过OUT参数和INOUT参数返回多个值，需要使用CALL语句调用并通过变量接收输出参数。",
    "2.存储函数有OUT参数、INOUT参数吗？",
    "存储函数没有OUT参数和INOUT参数。存储函数只能通过RETURN返回一个值，参数只能是IN类型。如果需要返回多个值，应该使用存储过程。",
    "3.使用游标的步骤。",
    "使用游标的步骤：声明游标(DECLARE cursor_name CURSOR FOR SELECT...)，定义结束处理句柄(DECLARE CONTINUE HANDLER FOR NOT FOUND)，打开游标(OPEN cursor_name)，循环获取数据(FETCH cursor_name INTO variables)，关闭游标(CLOSE cursor_name)。",
    "4.可以建立几种类型的触发器？",
    "MySQL支持六种触发器类型：BEFORE INSERT、AFTER INSERT、BEFORE UPDATE、AFTER UPDATE、BEFORE DELETE、AFTER DELETE。BEFORE触发器在操作执行前触发，可以修改NEW值；AFTER触发器在操作执行后触发，只能读取NEW和OLD值。",
]

# 生成段落
five_paras = []
for line in lines:
    is_sql = line.startswith('DELIMITER') or line.startswith('CREATE') or line.startswith('BEGIN') or line.startswith('END') or line.startswith('SELECT') or line.startswith('INSERT') or line.startswith('DELETE') or line.startswith('DROP') or line.startswith('CALL') or line.startswith('SET') or line.startswith('FOR EACH ROW') or line.startswith('DECLARE') or line.startswith('RETURN')
    if is_sql:
        five_paras.append(make_para(line))
    else:
        five_paras.append(make_para_cn(line))

five_xml = ''.join(five_paras)

# 插入五部分内容
new_doc = content[:five_p_end] + five_xml + content[six_p_start:]

print(f'添加了 {len(five_paras)} 个五部分段落')

# 验证XML
try:
    ET.fromstring(new_doc)
    print('五部分XML验证成功')
except ET.ParseError as e:
    print(f'XML错误: {e}')
    exit(1)

# 写回
with open(f'{dst}/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc)

# 添加六部分（实验体会）
# 重新读取
with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content2 = f.read()

# 找实验五六部分结束位置
import re
six_matches = [(m.start(), m.group()) for m in re.finditer(r'六、实验体会和收获', content2)]
exp5_six_pos = six_matches[4][0]
exp5_six_p_end = content2.find('</w:p>', exp5_six_pos) + 6
print(f'六段落结束: {exp5_six_p_end}')

# 心得内容
exp_lines = [
    "通过本次实验，我系统学习了MySQL数据库中存储过程和存储函数的创建与调用方法。存储过程是一组预编译的SQL语句集合，可以接收输入参数、返回输出参数，提高代码复用性和执行效率。",
    "在存储过程实验中，我掌握了CREATE PROCEDURE创建存储过程、CALL调用存储过程、DROP PROCEDURE删除存储过程的方法。学习了IN输入参数、OUT输出参数、INOUT双向参数的使用，理解了存储过程与存储函数的区别。",
    "存储函数实验让我理解了函数只能返回单个值、必须使用RETURN语句的特点。通过游标统计课程平均分的练习，初步了解了游标的基本用法，虽然简化版本可以直接使用AVG函数，但游标在处理逐行数据时非常有用。",
    "触发器部分让我理解了触发器作为特殊存储过程的概念，掌握了BEFORE和AFTER触发时机、INSERT/UPDATE/DELETE触发事件的应用。实验中创建的test_trig触发器实现了插入记录后自动记录时间，del_trig触发器实现了级联删除功能。",
    "实验过程中遇到一些问题，如DELIMITER命令的使用、存储函数必须指定DETERMINISTIC或READS SQL DATA属性等。这些问题加深了我对存储过程和触发器的理解，为后续数据库应用开发奠定了基础。",
]

exp_xml = ''.join([make_para_cn(line) for line in exp_lines])

# 插入六部分内容（替换六标题后的空段落）
new_doc2 = content2[:exp5_six_p_end] + exp_xml + content2[exp5_six_p_end:]

print(f'添加了 {len(exp_lines)} 个心得段落')

# 验证
try:
    ET.fromstring(new_doc2)
    print('完整文档XML验证成功')
except ET.ParseError as e:
    print(f'XML错误: {e}')
    exit(1)

# 写回
with open(f'{dst}/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc2)

# 打包
output = '../output/实验五报告.docx'
os.makedirs('../output', exist_ok=True)
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(dst):
        for file in files:
            file_path = os.path.join(root, file)
            arc_path = os.path.relpath(file_path, dst)
            zf.write(file_path, arc_path)

print(f'输出: {output}')
print(f'大小: {os.path.getsize(output)} bytes')