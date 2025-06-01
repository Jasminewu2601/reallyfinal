import streamlit as st
from components.styles import load_css    # ← 如果还没 import，加在文件顶部
import time        
from PIL import Image #loading ima
import os

def home_page():
    load_css() 
    # —— 英雄区 Hero Section ——
    st.markdown('<h1 class="big-title">Welcome! Let’s Make Things Interesting</h1>', unsafe_allow_html=True)

    placeholder = st.empty()
    message = "Storyteller · Data Tinkerer · Daydream Believer"
    display = ""
    for ch in message:
        display += ch
        placeholder.markdown(f"<h2>{display}▌</h2>", unsafe_allow_html=True)
        time.sleep(0.05)
    placeholder.markdown(f"<h2>{message}</h2>", unsafe_allow_html=True)

    st.markdown("---")

    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4 style="margin:0; color:var(--primary-color);">Dongjing WU</h4>
        <p style="margin:0.25rem 0; font-weight:600;">
          Master of Science in Marketing<br>
          Chinese University of Hong Kong<br>
          12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
          <a href="mailto:1155220570@link.cuhk.edu.hk">1155220570@link.cuhk.edu.hk</a>
        </p>
        <p style="margin:0.75rem 0; font-size:0.95rem; line-height:1.4;">
          <strong>MBTI:</strong> ENTJ &nbsp;|&nbsp;
          <strong>Zodiac:</strong> Aquarius &nbsp;|&nbsp;
          <strong>Birthday:</strong> Feb 6, 2001
        </p>
        """, unsafe_allow_html=True)  

    # add a photo to the right column
    image_path = os.path.join("static", "images", "wdj.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I’m currently pursuing an MSc in Marketing at The Chinese University of Hong Kong, where I’ve built a solid academic foundation and developed versatile expertise in marketing strategy, project management, and data analysis. My coursework and collaborative research projects have sharpened my ability to translate insights into actionable plans and measurable growth.

        During internships at Unilever and Nike, I led multiple cross-functional initiatives—working closely with brand, operations, and analytics teams to launch campaigns and optimize processes. These experiences taught me how to coordinate across departments, manage tight deadlines, and exceed stakeholder expectations.

        A natural quick-study, I thrive in dynamic environments and adapt rapidly to new challenges. I enjoy combining creative thinking with data-driven rigor to solve problems efficiently. Looking ahead, I’m excited to continue growing professionally and to bring innovative, measurable value to forward-thinking organizations.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming & Analysis - Python · R 
        - Statistical Software - SPSS · Stata
        - Data Visualization - Tableau · Excel (PivotTables & charts) · Google Data Studio
        - Design & Media - Adobe Photoshop · Adobe Premiere Pro · Canva
        - Office & Productivity - Microsoft Excel · PowerPoint · Word
        - Communication & Research - Presentation skills · Technical writing · Survey design
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 