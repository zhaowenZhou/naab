import docx
import docx2txt
import re

def reformat(file_path):
    text = docx2txt.process(file_path)
    text = text.replace('\n', '。').replace(' ', '，')
    # 处理重复的标点符号
    text = re.sub(r'([，。；！？])\1+', r'\1', text)
    document = docx.Document()
    para = document.add_paragraph().add_run( 
        text) 
    return document