import zipfile
import os
import shutil

# 读取document.xml
with open('fix_v2/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 重新定位：找到avg_func相关段落的正确边界
# 找最后一个五部分后的avg_func
five_pos = 493977  # 实验五五部分位置

# 找avg_func前一个段落的结束位置（</w:p>）
# 先找到题目段落："5.创建存储函数avg_func，通过游标统计指定课程的平均分。"
title_pos = content.find('5.创建存储函数avg_func', five_pos)
title_para_end = content.find('</w:p>', title_pos) + 6

print(f'题目段落结束: {title_para_end}')

# 找DROP FUNCTION avg_func后面的段落结束
drop_func = content.find('DROP FUNCTION avg_func', title_pos)
drop_para_end = content.find('</w:p>', drop_func) + 6

print(f'DROP段落结束: {drop_para_end}')

# 游标版本代码
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

# 使用完整的段落格式
def make_para(text):
    escaped = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<w:p w14:paraId="CUR001" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'

new_xml = '\n'.join([make_para(line) for line in cursor_lines])

# 替换：从题目段落结束到DROP段落结束
new_content = content[:title_para_end] + '\n' + new_xml + '\n' + content[drop_para_end:]

print(f'新文档长度: {len(new_content)}')

# 写回
with open('fix_v2/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('文件已更新')

# 打包
output = '../output/fix.docx'
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk('fix_v2'):
        for file in files:
            file_path = os.path.join(root, file)
            arc_path = os.path.relpath(file_path, 'fix_v2')
            zf.write(file_path, arc_path)

print(f'输出: {output}')