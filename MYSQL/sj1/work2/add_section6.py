import re

# Read document.xml from parent directory
with open('../unpacked/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position after "六、实验体会和收获" paragraph
# Search for the paragraph containing this text
pattern = r'<w:p[^>]*>.*?六、实验体会和收获.*?</w:p>'
match = re.search(pattern, content, re.DOTALL)
if match:
    insert_pos = match.end()
    print(f"Found '六' paragraph, ends at position: {insert_pos}")
else:
    print("Pattern not found, trying alternative search...")
    # Try simpler search
    idx = content.find('六、实验体会和收获')
    if idx != -1:
        # Find the </w:p> after this text
        end_p = content.find('</w:p>', idx)
        if end_p != -1:
            insert_pos = end_p + 6  # After </w:p>
            print(f"Alternative: found at {idx}, paragraph ends at {insert_pos}")

print(f"Insert position: {insert_pos}")

# XML escape function
def xml_escape(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text

# Three paragraphs content (Chinese only, so use 宋体 font)
paragraphs = [
    "通过本次实验，我系统学习和实践了MySQL数据库的基本操作，包括数据库和表的创建、修改与删除。在建表操作中，我掌握了如何使用CREATE TABLE语句定义表结构，以及如何通过ALTER TABLE语句修改表的列名、数据类型、添加或删除列。在数据操作方面，我学会了使用INSERT语句插入数据、DELETE语句删除数据以及UPDATE语句更新数据，特别是结合子查询进行数据操作的方法，加深了对SQL语句灵活应用的理解。",
    "本次实验还让我深入理解了数据库完整性约束的重要性。通过建立主键约束、外键约束、唯一约束和检查约束，我认识到这些约束机制能够有效保证数据的完整性和一致性。外键约束的级联更新功能让我理解了表之间的关联关系如何维护，而检查约束则确保了数据符合特定条件，防止不合理数据的插入。",
    "在实验过程中，我遇到了一些问题，如外键约束要求参照列必须具有唯一性或主键约束，这让我更加理解了约束之间的依赖关系。通过完成实验思考题，我进一步巩固了对数据库基本概念的理解，如主键与唯一约束的区别、删除数据库后的恢复可能性等。总体而言，本次实验为后续学习更复杂的数据库操作奠定了坚实的基础。"
]

# Generate XML paragraphs (Chinese text with 宋体)
new_xml_parts = []
for para in paragraphs:
    escaped = xml_escape(para)
    # Chinese paragraph: 宋体 font, 5号 (10.5pt = sz="21"), single line spacing
    xml_para = f'''<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:pPr><w:spacing w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="Times New Roman" w:hint="eastAsia"/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr><w:t xml:space="preserve">{escaped}</w:t></w:r></w:p>'''
    new_xml_parts.append(xml_para)

new_xml = ''.join(new_xml_parts)

# Insert new content
new_doc = content[:insert_pos] + new_xml + content[insert_pos:]

# Write back to parent directory
with open('../unpacked/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print("Document updated successfully")
print(f"Added {len(paragraphs)} paragraphs")