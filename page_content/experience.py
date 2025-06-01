import streamlit as st
from components.styles import load_css
from components.interactive import display_skill_radar

def experience_page():
    load_css()                  # ← 第一行

    st.markdown('<h1 class="big-title">💼 Professional Experience</h1>', unsafe_allow_html=True)

    tabs = st.tabs(["Internships", "Projects", "Skills"])
    with tabs[0]:
      st.markdown("""
    ### Domestos Marketing Intern 
    **Unilever (China)** | *February 2024 - May 2024*
    
    - Marketing creation:leading the creation of four seeding videos and one product launch video, which drove 3,000+ sales. Designed visual assets for the entire product line, Gained 50+ positive reviews within a week, with 97.4% approval rate at Sam’s. Club.
    - Project management: streamlined marketing materials for different products across various sales channels. Created a sharedcloud drive for suppliers to access customized marketing content. Collected over 2,000 pieces of sales feedback to track markettrends in real time.
    - Shipping coordination: managed the allocation and internal receipt. Coordinated and distributed products to various e-commerce warehouses, including PDD, Taobao flagship store, etc. Maintained optimal inventory levels and updated stock data promptly.
    """)
    
      st.markdown("""
    ### Digital Marketing Intern
    **Nike Sports (China)** | *July 2022 - February 2023*
    
    - Livestream execution: coordinated over 10 live streams on the NIKE APP, covering key promotional events like D11, D12, and CNY. Led cross-departmental collaboration to finalize stream themes, create preheat assets, and manage product selection, mechanics, confirmation and setup. Each stream averaged 10,000+ viewers.
    - Data analysis: collected and analyzed livestream data, including appointment volume, viewer & interaction count, and age distribution Gathered livestream tag data, including types, guests, and shoe releases, providing deeper insights into the preferences and needs of target audience.
    - New product promotion: contributed to NIKE’s Spring and Summer 2023 key visual shooting project. Involved in conceptualizing story themes, monitoring new product readiness. Creative materials yielded over 54,000 readings on WeChat.
    """)
    
      st.markdown("""
    ### Domestic Appliances Marketing Intern 
    **Philips Domestic Appliances (China) Investment Co., Ltd.** | *May 2022 - July 2022*
    
    - Market insight: used e-commerce data platforms to monitor and analyze the daily business performance. Investigated market dynamics and understood parameter performance of top competitors. Collected and analyzed data on customer demographics, preferences, and buying habits to identify potential markets and affecting factors
    - Promotion events support: coordinated and connect with the external agencies and participated in the planning of "618" promotion marketing activities for Tmall and JD.com. Independently completed the updates and launch of the first 8 products' PDPs (Product Detail Pages) and tracked the promotion mechanism of Philips' own products and other 6 competing products.
    - Launch of new products: engage in the market analysis for the launch of 2 new products. Collected information of the product sales, growth rate, market share through e-platforms and output analysis reports providing support for the pre-launch research.
    """)
    
      st.markdown("---")
        
    with tabs[1]:
      st.markdown("""
      <details class="project-box">
        <summary class="big-title">“Zheng Da Cup” 12th National College Student Market Research and Analysis Competition</summary>
        <p><strong>Outcome:</strong> 1st Prize in Shanghai, Nov 2020</p>
        <p><strong>Description:</strong>Led a team of 5. Combined online questionnaires & offline interviews with 1,400+ consumers to gauge fragrance product preferences (perfume, personal care, home fragrance). Applied consumer behavior theory, structural equation modeling, and SVM to analyze key drivers.</p>
      </details>

      <details class="project-box">
        <summary class="big-title">National Business Elite Challenge International Trade Competition</summary>
        <p><strong>Outcome:</strong> 1st Prize (National), May 2021</p>
        <p><strong>Description:</strong>Selected ideal commodities for exhibition & export. Drafted business plans, designed posters, and planned product launches. Collected international transport data, prepared quotations and contracts, and led negotiations with importers.</p>
      </details>

      <details class="project-box">
        <summary class="big-title">Enactus Student Club – “Beating the Damp” Greenhouse Project</summary>
        <p><strong>Description:</strong> Project Manager, led an 8-member team to tackle crop disease from excess humidity in greenhouses.Conducted market research and data analysis to refine the business model and core technology. Ran field trials, partnered with “Fan Oath” brand on eco-friendly packaging, secured municipal innovation funding, and won multiple university & city startup awards.</p>
      </details>
      """, unsafe_allow_html=True)
        
    with tabs[2]: 
        display_skill_radar()

    
    st.markdown("---") 
