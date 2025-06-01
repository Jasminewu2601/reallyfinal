import streamlit as st
from components.styles import load_css
import os


def education_page():
    load_css()
    st.markdown('<h1 class="big-title">📚 Education</h1>', unsafe_allow_html=True)

    timeline = [
        {
            "logo": os.path.join("static","images","cuhk.png"),
            "institution": "The Chinese University of Hong Kong",
            "degree": "MSc Marketing",
            "period": "Sep 2024 – Jul 2025",
            "details": "GPA: 3.5/4.0; Core courses: Digital Marketing, Marketing Research, Big Data Strategy, Marketing Management"
        },
        {
            "logo": os.path.join("static","images","shu.png"),
            "institution": "Shanghai University",
            "degree": "BSc Economics, Major in International Economics and Trade",
            "period": "Sep 2019 – Jun 2023",
            "details": "GPA: 3.6/4.0; Core courses: Economics for Business, Econometrics, International Trade Theory"
        },
    ]

    for item in timeline:
        # 1: 两列布局：左 1 份宽度放 logo，右 6 份放文字
        col1, col2 = st.columns([1, 6])
        with col1:
            # 2: 直接用 Streamlit 渲染图片，宽度 80px
            st.image(item["logo"], width=80)
        with col2:
            # 3: 用 Markdown + HTML 来排版文字
            st.markdown(f"""
                <h3 style="margin:0; color:var(--primary-color);">
                  {item['institution']}
                </h3>
                <p style="margin:0.2rem 0; font-weight:600; font-size:1rem;">
                  {item['degree']} | <em>{item['period']}</em>
                </p>
                <p style="margin:0.5rem 0; font-size:0.95rem; line-height:1.5;">
                  {item['details']}
                </p>
            """, unsafe_allow_html=True)

        # 4: 每条记录间加条分割线
        st.markdown("<hr style='margin:2rem 0;'>", unsafe_allow_html=True)
    
    st.markdown('<h1 class="big-title">🏆 Honors & Awards</h1>', unsafe_allow_html=True)
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### Academic Honors

        **Outstanding Graduate**, Shanghai University — Jun 2023  
        **Outstanding Class Committee Member** — May 2023  
        **Outstanding Student** — Dec 2020 | Feb 2022 | Mar 2023  

        """)
        
    with cert2:
        st.markdown("""
        ### Scholarships
        **Single-Item Scholarship** — Dec 20 2020 | Dec 15 2021  
        **Merit Scholarship (Second-Class)** — Dec 12 2022  
        """)
        
    with cert3:
        st.markdown("""
        ### Competitions
        **National Business Elite Challenge** (International Trade, English) — First Prize — May 10 2021  
        **Chia Tai Cup** National Market Survey & Analysis (Shanghai) — First Prize — Apr 23 2022  
        **Challenge Cup** Shanghai Student Entrepreneurship Competition — Bronze Medal — Nov 2020   
        """)
    
    st.markdown("---")
    
    st.markdown('<h2 class="big-title">📝 Academic Projects</h2>',
  unsafe_allow_html=True)
    
    st.markdown("""
    ### Academic Paper - Can the Establishment of a Personal Data Protection System Promote Corporate Innovation?
    - Research Policy, 2024
    - Investigated how a self-regulated personal data protection system (PDPS) affects corporate innovation.Found that PDPS significantly increases innovation **quantity** by lowering financial constraints and risks.Noted that PDPS may hinder innovation **novelty** when data access becomes limited.
    
    ### Entrepreneurial Project - Beating the Damp
    - As Project Manager, led an 8-member team to develop a greenhouse humidity-control solution that prevents crop disease caused by excess moisture.Conducted market research and data analysis to refine the business model and optimize core technology.Ran field trials to validate the product, secured Shanghai municipal innovation funding, and won multiple university- and city-level startup awards.
    """)
    
    st.markdown("---") 