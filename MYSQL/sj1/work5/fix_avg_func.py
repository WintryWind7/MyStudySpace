import os

# 读取document.xml
with open('fix_unpacked/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# 要替换的内容（旧版本 - 无游标）
old_text = '''    <w:p w14:paraId="223FD8B4" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DELIMITER @@</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="0669452A" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>CREATE FUNCTION avg_func(cname VARCHAR(50)) RETURNS DECIMAL(10,2)</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="0F8F1296" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="宋体" w:hint="eastAsia"/>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DETERMINISTIC</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="7EC8AC0D" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="宋体" w:hint="eastAsia"/>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>READS SQL DATA</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="737D6B53" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>BEGIN</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="2D8B520E" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DECLARE avg_score DECIMAL(10,2);</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="54D7A326" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>SELECT AVG(g.SCORE) INTO avg_score FROM grade g, curriculum c WHERE g.KCH=c.KCH AND c.KCMC=cname;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="6F9ACE41" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>RETURN avg_score;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="20E79192" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>END @@</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="6EC84E8D" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DELIMITER ;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="157A6020" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>SELECT avg_func('高等数学');</w:t>
      </w:r>



    </w:p>
    <w:p w14:paraId="12C66A7E" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DROP FUNCTION avg_func;</w:t>
      </w:r>
    </w:p>'''

# 新版本（带游标）
new_text = '''    <w:p w14:paraId="223FD8B4" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DELIMITER @@</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="0669452A" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>CREATE FUNCTION avg_func(cname VARCHAR(50)) RETURNS DECIMAL(10,2)</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="0F8F1296" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="宋体" w:hint="eastAsia"/>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DETERMINISTIC</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="7EC8AC0D" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="宋体" w:hint="eastAsia"/>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>READS SQL DATA</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="737D6B53" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>BEGIN</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR001" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DECLARE done INT DEFAULT 0;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR002" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DECLARE total DECIMAL(10,2) DEFAULT 0;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR003" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DECLARE cnt INT DEFAULT 0;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR004" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DECLARE score_val INT;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR005" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DECLARE cur CURSOR FOR SELECT g.SCORE FROM grade g, curriculum c WHERE g.KCH=c.KCH AND c.KCMC=cname;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR006" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR007" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>OPEN cur;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR008" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>FETCH cur INTO score_val;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR009" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>WHILE done=0 DO</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR010" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>SET total=total+score_val;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR011" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>SET cnt=cnt+1;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR012" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>FETCH cur INTO score_val;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR013" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>END WHILE;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR014" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>CLOSE cur;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR015" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>IF cnt=0 THEN RETURN 0;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR016" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>ELSE RETURN total/cnt;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="CUR017" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>END IF;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="20E79192" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>END @@</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="6EC84E8D" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DELIMITER ;</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="157A6020" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>SELECT avg_func('高等数学');</w:t>
      </w:r>
    </w:p>
    <w:p w14:paraId="12C66A7E" w14:textId="77777777" w:rsidR="008E0228" w:rsidRDefault="008E0228">
      <w:r>
        <w:rPr>
          <w:szCs w:val="21"/>
        </w:rPr>
        <w:t>DROP FUNCTION avg_func;</w:t>
      </w:r>
    </w:p>'''

# 替换
if old_text in content:
    content = content.replace(old_text, new_text)
    print('替换成功')
else:
    print('未找到匹配内容')
    # 尝试查找位置
    idx = content.find('DELIMITER @@')
    idx2 = content.find('CREATE FUNCTION avg_func')
    print(f'DELIMITER @@ 位置: {idx}')
    print(f'CREATE FUNCTION avg_func 位置: {idx2}')

# 写回
with open('fix_unpacked/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(content)

print('文件已更新')