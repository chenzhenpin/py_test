#coding=utf-8
from docx import Document

d = Document('newd.docx')
find_target = 'zwname'
substitute = '想替换成的文字'

# 遍历每段，在每段中执行替换动作
for para in d.paragraphs:
    para.text = para.text.replace(find_target, substitute)

d.save('new_file_path.docx')

