import zipfile
import os
import shutil
from xml.etree import ElementTree as ET

# 重新解压
src = '../template/实验五done.docx'
dst = 'fix_unpacked'

if os.path.exists(dst):
    shutil.rmtree(dst)

with zipfile.ZipFile(src, 'r') as zf:
    zf.extractall(dst)

# 读取document.xml
with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 找实验五五部分的avg_func（在存储过程部分）
# 实验五是最后一个"五、问题解答及实验结果"
import re
five_matches = list(re.finditer(r'五、问题解答及实验结果', content))
six_matches = list(re.finditer(r'六、实验体会和收获', content))

# 实验五的索引是最后一个
exp5_five_end = five_matches[-1].end()
exp5_six_start = six_matches[-1].start()

print(f'实验五五部分结束: {exp5_five_end}')
print(f'实验五六部分开始: {exp5_six_start}')

# 在这个范围内找avg_func
exp5_content = content[exp5_five_end:exp5_six_start]

# 找avg_func函数定义的开始和结束
# 开始: DELIMITER @@ 后面的 CREATE FUNCTION avg_func
# 结束: DROP FUNCTION avg_func

# 找所有DELIMITER @@位置
delimiter_pos = [m.start() for m in re.finditer(r'DELIMITER @@', exp5_content)]
print(f'DELIMITER @@ 位置: {delimiter_pos}')

# 找avg_func的位置
avg_func_pos = [m.start() for m in re.finditer(r'CREATE FUNCTION avg_func', exp5_content)]
print(f'avg_func位置: {avg_func_pos}')

# 找DROP FUNCTION avg_func的位置
drop_pos = [m.start() for m in re.finditer(r'DROP FUNCTION avg_func', exp5_content)]
print(f'DROP位置: {drop_pos}')

# 确定要替换的范围
# avg_func是最后一个存储过程（第5题）
# 对应的DELIMITER @@应该在avg_func_pos之前最近的一个

if avg_func_pos and delimiter_pos:
    # 找avg_func前面最近的DELIMITER @@
    avg_start = None
    for d in delimiter_pos:
        if d < avg_func_pos[-1]:
            avg_start = d
    print(f'avg_func开始位置（相对）: {avg_start}')

    if drop_pos:
        avg_end = drop_pos[-1] + len('DROP FUNCTION avg_func;')
        # 找后面的</w:p>
        avg_end = exp5_content.find('</w:p>', avg_end) + 6
        print(f'avg_func结束位置（相对）: {avg_end}')

        # 绝对位置
        abs_start = exp5_five_end + avg_start
        abs_end = exp5_five_end + avg_end

        print(f'绝对位置: {abs_start} 到 {abs_end}')

        # 生成游标版本的XML段落
        def make_para(text):
            return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>{text}</w:t></w:r></w:p>'

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

        new_xml = '\n'.join([make_para(line) for line in cursor_lines])

        # 替换
        new_content = content[:abs_start] + new_xml + '\n' + content[abs_end:]

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

        print('文件已更新')

        # 打包
        output = '../output/fix.docx'
        with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(dst):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_path = os.path.relpath(file_path, dst)
                    zf.write(file_path, arc_path)

        print(f'输出: {output}')