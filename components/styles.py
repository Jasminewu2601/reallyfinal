import streamlit as st

# ——— 主题变量 ———
FONT_TITLE    = "Playfair Display, serif"
FONT_TEXT     = "Lora, serif"
COLOR_BG      = "#FFF8F5"    # 奶油白
COLOR_PRIMARY = "#D291BC"    # 柔和粉紫
COLOR_SECOND  = "#F4C2C2"    # 淡玫瑰金
COLOR_TEXT    = "#4A4A4A"    # 深灰

CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora&display=swap');

[data-testid="stAppViewContainer"] {{
  background-color: var(--bg-color) !important;
}}

[data-testid="stSidebar"] {{
  background-color: var(--bg-color) !important;
}}
:root {{
  --bg-color: {COLOR_BG};
  --primary-color: {COLOR_PRIMARY};
  --secondary-color: {COLOR_SECOND};
  --text-color: {COLOR_TEXT};
}}

body, .main {{
  background-color: var(--bg-color);
  color: var(--text-color);
  font-family: 'Lora', serif;
  padding: 2rem;
}}

h1, h2, h3, h4, .big-title {{
  font-family: 'Playfair Display', serif;
  color: var(--primary-color);
}}

a {{
  color: var(--secondary-color);
  text-decoration: none;
}}

.sidebar .sidebar-content {{
  background-color: var(--primary-color);
  color: white;
}}

.stButton>button {{
  background-color: var(--secondary-color) !important;
  color: white !important;
  border-radius: 8px;
}}

.footer {{
  text-align: center;
  padding: 1rem 0;
  color: var(--text-color);
  font-size: 0.8rem;
}}
.stTabs [role="tab"] {{
  font-size: 1.25rem !important;
    font-weight: 600 !important;
    padding: 0.5rem 1rem !important; 
}}

.project-box summary {{
  font-size: 1.4rem !important;
  font-weight: 600 !important;
  color: var(--primary-color);
}}

.project-box p {{
  margin: 0.5em 0;
  font-size: 1.2rem;
  line-height: 1.6;
}}
details.project-box > summary.big-title {{
  display: list-item; 
  list-style-position: inside;                        
  font-family: 'Playfair Display', serif; 
  font-size: 1.5rem !important;          
  font-weight: 700 !important;            
  line-height: 1.2 !important;            
  color: var(--primary-color) !important; 
  margin: 1rem 0 !important;              
}}

details.project-box > summary.big-title::-webkit-details-marker {{
  font-size: 1.5rem;                     
  color: var(--primary-color);
}}

details.project-box p {{
  font-family: 'Lora', serif !important;    
  font-size: 1rem !important;               
  line-height: 1.5 !important;              
  margin: 0.5rem 0 !important;              
  color: var(--text-color) !important;     
}}
</style>
"""

def load_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)