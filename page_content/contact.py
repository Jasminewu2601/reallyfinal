import streamlit as st
from components.styles import load_css
def contact_page():
    load_css() 
    st.markdown("## Contact Me")
    
    st.markdown("""
    Feel free to reach out to me through any of the following channels:
    
    ### Direct Contact
    - **Email**: [Wdj_jasmine2026@163.com](mailto:Wdj_jasmine2026@163.com)
    - **Phone**: +86 15925028589
    - **Wechat**: [wdj15925028589]
    - **GitHub**: [github.com/Jasminewu2601](https://github.com/Jasminewu2601)
    """)
    
    st.markdown("### Send Me a Message")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            
        with col2:
            subject = st.text_input("Subject")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
    
    st.markdown("---")
    
