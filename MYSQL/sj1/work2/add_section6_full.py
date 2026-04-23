import zipfile
import os
import re

# Step 1: Unpack the previous document (实验一报告.docx) into a new directory
prev_doc = '../output/实验一报告.docx'
new_unpacked = 'unpacked_new'

# Remove old unpacked_new if exists
if os.path.exists(new_unpacked):
    import shutil
    shutil.rmtree(new_unpacked)

# Unpack
with zipfile.ZipFile(prev_doc, 'r') as zf:
    zf.extractall(new_unpacked)
print(f"Unpacked {prev_doc} to {new_unpacked}")

# Step 2: Read document.xml
doc_xml_path = os.path.join(new_unpacked, 'word', 'document.xml')
with open(doc_xml_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 3: Find "六、实验体会和收获" position
pattern = r'<w:p[^>]*>.*?六、实验体会和收获.*?</w:p>'
match = re.search(pattern, content, re.DOTALL)
if match:
    insert_pos = match.end()
    print(f"Found '六' paragraph, ends at position: {insert_pos}")
else:
    print("Pattern not found with regex, trying simple search...")
    idx = content.find('六、实验体会和收获')
    if idx != -1:
        end_p = content.find('</w:p>', idx)
        if end_p != -1:
            insert_pos = end_p + 6
            print(f"Found at {idx}, paragraph ends at {insert_pos}")
    else:
        print("ERROR: '六' not found")
        exit(1)

# XML escape function
def xml_escape(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text

# Three paragraphs content
paragraphs = [
    "通过本次实验，我系统学习和实践了MySQL数据库的基本操作，包括数据库和表的创建、修改与删除。在建表操作中，我掌握了如何使用CREATE TABLE语句定义表结构，以及如何通过ALTER TABLE语句修改表的列名、数据类型、添加或删除列。在数据操作方面，我学会了使用INSERT语句插入数据、DELETE语句删除数据以及UPDATE语句更新数据，特别是结合子查询进行数据操作的方法，加深了对SQL语句灵活应用的理解。",
    "本次实验还让我深入理解了数据库完整性约束的重要性。通过建立主键约束、外键约束、唯一约束和检查约束，我认识到这些约束机制能够有效保证数据的完整性和一致性。外键约束的级联更新功能让我理解了表之间的关联关系如何维护，而检查约束则确保了数据符合特定条件，防止不合理数据的插入。",
    "在实验过程中，我遇到了一些问题，如外键约束要求参照列必须具有唯一性或主键约束，这让我更加理解了约束之间的依赖关系。通过完成实验思考题，我进一步巩固了对数据库基本概念的理解，如主键与唯一约束的区别、删除数据库后的恢复可能性等。总体而言，本次实验为后续学习更复杂的数据库操作奠定了坚实的基础。"
]

# Generate XML paragraphs
new_xml_parts = []
for para in paragraphs:
    escaped = xml_escape(para)
    xml_para = f'''<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:pPr><w:spacing w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="Times New Roman" w:hint="eastAsia"/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr><w:t xml:space="preserve">{escaped}</w:t></w:r></w:p>'''
    new_xml_parts.append(xml_para)

new_xml = ''.join(new_xml_parts)

# Insert new content
new_doc = content[:insert_pos] + new_xml + content[insert_pos:]

# Write back
with open(doc_xml_path, 'w', encoding='utf-8') as f:
    f.write(new_doc)
print(f"Added {len(paragraphs)} paragraphs to document.xml")

# Step 4: Pack back to new docx
output_doc = '../output/实验一报告_完整.docx'
with zipfile.ZipFile(output_doc, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(new_unpacked):
        for file in files:
            file_path = os.path.join(root, file)
            arc_path = os.path.relpath(file_path, new_unpacked)
            zf.write(file_path, arc_path)

print(f"Packed to: {output_doc}")
print(f"Size: {os.path.getsize(output_doc)} bytes")