import re
import os
import shutil
import zipfile

# Read the generated doc
dst = '../unpacked_exp2'

with open(f'{dst}/word/document.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Find 六部分 position (after exp2's 六、实验体会和收获)
exp2_title = content.find('数据查询')
exp2_six = content.find('六、实验体会和收获', exp2_title)

# Find the paragraph end
six_end_p = content.find('</w:p>', exp2_six)
print(f"六部分标题位置: {exp2_six}")
print(f"六部分段落结束: {six_end_p}")

# Find next paragraph (exp3 title)
exp3_start = content.find('实验项目名称', exp2_six + 50)
exp3_p_start = content.rfind('<w:p', 0, exp3_start)
print(f"实验三标题段落开始: {exp3_p_start}")

# XML escape
def xml_escape(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text

def make_paragraph(text):
    escaped = xml_escape(text)
    font = 'w:ascii="宋体" w:eastAsia="宋体" w:hAnsi="Times New Roman" w:hint="eastAsia"'
    return f'<w:p w:rsidR="008E0228" w:rsidRDefault="008E0228"><w:pPr><w:spacing w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts {font}/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr><w:t xml:space="preserve">{escaped}</w:t></w:r></w:p>'

# 实验体会内容
exp2_experience = [
    "通过本次实验，我系统学习和掌握了MySQL数据库的查询操作。实验涵盖了基本查询、条件查询、排序查询、分组查询、嵌套查询和连接查询等多种查询方式，让我对SQL查询语句有了全面的认识。",
    "在基本查询和条件查询中，我学会了使用SELECT语句配合WHERE子句进行数据筛选，掌握了比较运算符、逻辑运算符和BETWEEN、LIKE等特殊运算符的使用方法。ORDER BY子句让我理解了单字段和多字段排序的实现，GROUP BY子句则帮助我理解了分组统计的概念。",
    "嵌套查询是本次实验的重点内容。通过IN、ANY、ALL等子查询操作符，我学会了如何在查询中嵌套另一个查询，实现更复杂的数据筛选逻辑。连接查询部分让我掌握了内连接、左外连接、右外连接等不同连接方式的应用场景和实现方法。",
    "实验过程中遇到一些问题，如多表连接时字段名冲突需要使用别名，GROUP BY分组时SELECT字段必须包含在GROUP BY子句或聚合函数中等。这些问题加深了我对SQL语法的理解，为后续学习更复杂的数据库操作奠定了基础。",
]

# Generate XML
new_xml_parts = []
for para in exp2_experience:
    new_xml_parts.append(make_paragraph(para))

new_xml = ''.join(new_xml_parts)

# Insert after 六、标题段落
new_doc = content[:six_end_p+6] + new_xml + content[exp3_p_start:]

# Write back
with open(f'{dst}/word/document.xml', 'w', encoding='utf-8') as f:
    f.write(new_doc)

print(f"Added {len(exp2_experience)} experience paragraphs")

# Pack back
output = '../output/实验二报告.docx'
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(dst):
        for file in files:
            file_path = os.path.join(root, file)
            arc_path = os.path.relpath(file_path, dst)
            zf.write(file_path, arc_path)

print(f"Packed to {output}")
print(f"Size: {os.path.getsize(output)} bytes")