import zipfile
import os
import shutil
from xml.etree import ElementTree as ET

# 解压到新目录
src = '../template/实验五done.docx'
dst = 'fix_new'

if os.path.exists(dst):
    shutil.rmtree(dst)

with zipfile.ZipFile(src, 'r') as zf:
    zf.extractall(dst)

# 读取document.xml
with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 找avg_func代码块（使用正则表达式找到完整的段落序列）
import re

# 找实验五五部分avg_func的XML段落块
# 格式: <w:p ...><w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>DELIMITER @@</w:t></w:r></w:p>
# ... 到 DROP FUNCTION avg_func;

# 找到包含avg_func的存储函数定义的开始
# 先找实验五五部分区域
five_pos = content.find('五、问题解答及实验结果', content.find('存储过程和触发器'))
six_pos = content.find('六、实验体会和收获', five_pos)

print(f'五部分位置: {five_pos}')
print(f'六部分位置: {six_pos}')

# 在五部分区域找avg_func
exp5_area = content[five_pos:six_pos]

# 找avg_func定义的段落块
# 匹配模式：从包含DELIMITER @@的段落开始，到DROP FUNCTION avg_func结束

# 更简单的方法：找所有段落
paragraphs = re.findall(r'<w:p[^>]*>.*?</w:p>', exp5_area, re.DOTALL)

# 找avg_func相关的段落索引
avg_start_idx = None
avg_end_idx = None

for i, p in enumerate(paragraphs):
    if 'CREATE FUNCTION avg_func' in p:
        # 往前找DELIMITER @@
        for j in range(i-1, -1, -1):
            if 'DELIMITER @@' in paragraphs[j] and 'CREATE' not in paragraphs[j]:
                avg_start_idx = j
                break
    if 'DROP FUNCTION avg_func' in p:
        avg_end_idx = i

print(f'avg_func段落索引: {avg_start_idx} 到 {avg_end_idx}')

if avg_start_idx is not None and avg_end_idx is not None:
    # 生成游标版本段落
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
        'SELECT avg_func(\'高等数学\');',
        'DROP FUNCTION avg_func;',
    ]

    # 使用和原文档相同的段落格式
    # 从原文档中取一个段落模板
    para_template = paragraphs[avg_start_idx]
    # 提取段落属性
    para_match = re.match(r'<w:p([^>]*)>', para_template)
    para_attrs = para_match.group(1) if para_match else ''

    new_paragraphs = []
    for line in cursor_lines:
        # XML转义
        escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        new_p = f'<w:p{para_attrs}><w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'
        new_paragraphs.append(new_p)

    # 替换
    new_exp5_area = paragraphs[:avg_start_idx] + new_paragraphs + paragraphs[avg_end_idx+1:]
    new_exp5_xml = '\n'.join(new_exp5_area)

    # 组合完整文档
    # 找原文档中五部分到六部分之间的内容
    before_five = content[:five_pos]
    # 找五部分标题段落结束
    five_title_end = content.find('</w:p>', five_pos) + 6
    before_content = content[:five_title_end]

    # 找六部分标题段落开始
    six_title_start = content.rfind('<w:p ', 0, six_pos)

    after_content = content[six_title_start:]

    new_content = before_content + '\n' + new_exp5_xml + '\n' + after_content

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