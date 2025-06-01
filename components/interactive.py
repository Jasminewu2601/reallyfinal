import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

def display_skill_radar():
    st.subheader("🔺 Skill Radar")
    skills = {"Python": 90, "Machine Learning": 75, "R": 85, "PR": 70, "Communication": 90}
    df = pd.DataFrame({
        'skill': list(skills.keys()),
        'level': list(skills.values())
    })

    categories = df['skill'].tolist()
    values = df['level'].tolist()
    values += values[:1]  # 闭合

    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw={'polar':True})
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories)
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    st.pyplot(fig)