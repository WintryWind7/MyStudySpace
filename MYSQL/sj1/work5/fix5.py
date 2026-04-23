import zipfile
import os
import shutil
from xml.etree import ElementTree as ET
import re

# 解压
src = '../template/实验五done.docx'
dst = 'fix_final'

if os.path.exists(dst):
    shutil.rmtree(dst)

with zipfile.ZipFile(src, 'r') as zf:
    zf.extractall(dst)

# 读取document.xml
with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 定位：实验五五部分是最后一个（索引4），位置493977
# avg_func在五部分后面，大约501303开始

# 找avg_func函数定义部分（实验五五部分中的第5题）
# 找到CREATE FUNCTION avg_func的位置
avg_func_create = content.find('CREATE FUNCTION avg_func', 493977)
print(f'CREATE FUNCTION avg_func位置: {avg_func_create}')

# 往前找对应的DELIMITER @@
# 在avg_func_create往前找最近的DELIMITER @@
search_start = max(493977, avg_func_create - 500)
delimiter_start = content.rfind('DELIMITER @@', search_start, avg_func_create)
print(f'DELIMITER @@开始位置: {delimiter_start}')

# 往后找DROP FUNCTION avg_func
drop_func = content.find('DROP FUNCTION avg_func', avg_func_create)
print(f'DROP FUNCTION位置: {drop_func}')

# 找DROP后面的段落结束
drop_para_end = content.find('</w:p>', drop_func) + 6
print(f'段落结束位置: {drop_para_end}')

if delimiter_start > 0 and drop_para_end > delimiter_start:
    # 提取要替换的旧XML
    old_xml = content[delimiter_start:drop_para_end]
    print(f'旧XML长度: {len(old_xml)}')

    # 生成游标版本的段落
    cursor_lines = [
        'DELIMITER @@',
        'CREATE FUNCTION avg_func(cname VARCHAR(50)) RETURNS DECIMAL(10,2)',
        'DETERMINISTIC',
        'READS SQL DATA',
        'BEGIN',
        'DECLARE done INT DEFAULT 0;',
        'DECLARE total DECIMAL(10,2) DEFAULT 0;',
        'DECLARE cnt INT DEFAULT 0;',
        'DECLARE score_val INT;',
        'DECLARE cur CURSOR FOR SELECT g.SCORE FROM grade g, curriculum c WHERE g.KCH=c.KCH AND c.KCMC=cname;',
        'DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;',
        'OPEN cur;',
        'FETCH cur INTO score_val;',
        'WHILE done=0 DO',
        'SET total=total+score_val;',
        'SET cnt=cnt+1;',
        'FETCH cur INTO score_val;',
        'END WHILE;',
        'CLOSE cur;',
        'IF cnt=0 THEN RETURN 0;',
        'ELSE RETURN total/cnt;',
        'END IF;',
        'END @@',
        'DELIMITER ;',
        "SELECT avg_func('高等数学');",
        'DROP FUNCTION avg_func;',
    ]

    # 从旧XML中提取段落属性格式
    # 取第一个段落作为模板
    first_para_match = re.search(r'<w:p[^>]*>', old_xml)
    para_attrs = first_para_match.group(0) if first_para_match else '<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228">'

    new_paragraphs = []
    for line in cursor_lines:
        escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        new_p = f'{para_attrs}<w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'
        new_paragraphs.append(new_p)

    new_xml = '\n'.join(new_paragraphs)

    # 替换
    new_content = content[:delimiter_start] + new_xml + '\n' + content[drop_para_end:]

    print(f'新文档长度: {len(new_content)}')

    # 验证XML
    try:
        ET.fromstring(new_content)
        print('XML验证成功')
    except ET.ParseError as e:
        print(f'XML错误: {e}')

    # 写回
    with open(f'{dst}/word/document.xml', 'w', encoding='utf-8') as f:
        f.write(new_content)

    # 打包
    output = '../output/fix.docx'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(dst):
            for file in files:
                file_path = os.path.join(root, file)
                arc_path = os.path.relpath(file_path, dst)
                zf.write(file_path, arc_path)

    print(f'输出: {output}')