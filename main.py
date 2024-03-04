import io
from PIL import Image
import streamlit as st
from docx.shared import Pt 
from scripts import reformat

def main():
    st.title('NAAB-Natural language processing Ai Assistant for Bertha')
    tab1, tab2 = st.tabs(["格式转写", "按需添加"])
    with tab1:
        st.header("将字幕格式整理为文档格式")
        document = st.file_uploader(label="上传原始docx文件，目前只支持上传单个文件", accept_multiple_files=False, type=["docx"], key="document uploader")
        if st.button("转换格式"):
            if document is not None:
                st.write('Processing, please wait...')
                doc_detail = {"filename": document.name, "filetype":document.type, "filesize":document.size}
                st.write(doc_detail)
                new_doc = reformat(document)
                bio = io.BytesIO()
                new_doc.save(bio)
                st.write('处理完成，请使用下载键进行下载')
                st.download_button(label="下载键", data=bio.getvalue(), file_name=f'new_{document.name}')
            else:
                st.write("Upload first baby!")
        if st.button("利用AI助手获取大纲"):
            qr_image = Image.open('data/QRcode.jpg')
            st.image(qr_image)
            st.write("开发中....，给点奖励作者开发更快哦")
            
if __name__ == "__main__":
    main()