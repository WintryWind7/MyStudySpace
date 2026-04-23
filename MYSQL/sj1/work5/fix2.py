import re

# 读取document.xml
with open('fix_unpacked/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 找avg_func相关内容的位置
# 找到实验五五部分的avg_func代码块
start_marker = 'DELIMITER @@\nCREATE FUNCTION avg_func'
end_marker = 'DROP FUNCTION avg_func;'

# 找开始位置
start_idx = content.find('DELIMITER @@')
# 从开始位置找avg_func
while True:
    idx = content.find('CREATE FUNCTION avg_func', start_idx)
    if idx == -1:
        break
    # 检查前面是否有DELIMITER @@
    delimiter_idx = content.rfind('DELIMITER @@', 0, idx)
    if delimiter_idx > 0 and idx - delimiter_idx < 100:
        # 这是我们要找的位置
        # 找结束位置
        end_idx = content.find('DROP FUNCTION avg_func;', idx)
        if end_idx != -1:
            end_idx += len('DROP FUNCTION avg_func;')
            # 再往后找到</w:p>
            end_idx = content.find('</w:p>', end_idx) + 6

            print(f'找到位置: 开始 {delimiter_idx}, 结束 {end_idx}')

            # 提取要替换的片段
            old_fragment = content[delimiter_idx:end_idx]
            print(f'旧片段长度: {len(old_fragment)}')

            # 新内容（游标版本）
            new_fragment = '''DELIMITER @@
CREATE FUNCTION avg_func(cname VARCHAR(50)) RETURNS DECIMAL(10,2)
DETERMINISTIC
READS SQL DATA
BEGIN
DECLARE done INT DEFAULT 0;
DECLARE total DECIMAL(10,2) DEFAULT 0;
DECLARE cnt INT DEFAULT 0;
DECLARE score_val INT;
DECLARE cur CURSOR FOR SELECT g.SCORE FROM grade g, curriculum c WHERE g.KCH=c.KCH AND c.KCMC=cname;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
OPEN cur;
FETCH cur INTO score_val;
WHILE done=0 DO
SET total=total+score_val;
SET cnt=cnt+1;
FETCH cur INTO score_val;
END WHILE;
CLOSE cur;
IF cnt=0 THEN RETURN 0;
ELSE RETURN total/cnt;
END IF;
END @@
DELIMITER ;
SELECT avg_func('高等数学');
DROP FUNCTION avg_func;'''

            # 但是我们需要保持XML格式
            # 更好的方法是替换XML段落

            # 生成新的XML段落
            def make_para(text):
                escaped = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:r><w:rPr><w:szCs w:val="21"/></w:rPr><w:t>{escaped}</w:t></w:r></w:p>'

            lines = new_fragment.strip().split('\n')
            new_xml = '\n'.join([make_para(line) for line in lines])

            # 替换
            new_content = content[:delimiter_idx] + new_xml + '\n' + content[end_idx:]

            # 写回
            with open('fix_unpacked/word/document.xml', 'w', encoding='utf-8') as f:
                f.write(new_content)

            print('替换完成')
            break
    start_idx = idx + 1