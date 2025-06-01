import streamlit as st
import streamlit.components.v1 as components
import os
from components.styles import load_css
def resume_page():
    load_css()  
    st.markdown("## 📄 My Resume")

    # 1) 指定你自己的简历 PDF 路径
    pdf_path = os.path.join("static", "docs", "wdj1.pdf")

    if not os.path.exists(pdf_path):
        st.error(f"⚠️ 找不到简历文件：{pdf_path}")
        return

    # 2) 读取文件字节
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    # 3) 下载按钮
    st.download_button(
        label="Download Resume (PDF)",
        data=pdf_bytes,
        file_name="wdj1.pdf",
        mime="application/pdf",
    )

    # 4) 内嵌预览
    img_path = os.path.join("static", "images", "wdj1.png")
    if os.path.exists(img_path):
        st.image(img_path, caption="My Resume", use_column_width=True)
    else:
        st.warning(f"尚未找到预览图片：{img_path}，请确保已上传 `resume.png`。")