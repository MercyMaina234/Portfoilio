import streamlit as st

st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded",
    page_title="Mercy Maina Portfolio",
    page_icon="🖥️",
)
st.title("Mercy Maina Portfolio")
st.write("---------------------")
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.write("Data Scientist | Data Analyst | Software developer | Python  ")
column1,column2 = st.columns(2)
with column1:
    st.image("mee.jpg", width=500)
with column2:
    st.subheader("About Me")
    st.write("""I'm a passionate and detail-oriented developer with a strong foundation in Python, Laravel, and data analysis. 
With hands-on experience in building user-friendly web applications, I enjoy turning ideas into functional solutions.  
I thrive in collaborative environments, value clean code, and am constantly learning to keep up with evolving technologies.

Whether it's building a responsive front-end or handling logic in the back-end, I aim to deliver impactful digital experiences.
""")
st.subheader("My Skills")
with st.expander("Click to see my skills"):
    st.markdown("**Languages & Frameworks**")
    st.markdown("""
        - Python (data analysis, scripting)
        - Laravel (PHP backend)
        - HTML & CSS
        - JavaScript (basic)
        """)
    st.markdown("**Tools & IDEs**")
    st.markdown("""
        - PyCharm
        - Jupyter Notebook
        - Android Studio
        - MS Office (Excel, Word)
        """)
    st.markdown("**Libraries & Technologies**")
    st.markdown("""
       - pandas
       - Streamlit
       - SQL / MySQL
       - Bootstrap (via Laravel)
       """)
    st.markdown("**DevOps & Backend**")
    st.markdown("""
        - Authentication & Session Handling
        - Database design (ERD modeling)
        - Interest in DevOps roles
        """)
    st.markdown("""
    - Analytical & Critical Thinking  
    - Documentation & System Design  
    - Problem Solving & Troubleshooting  
    - Team Collaboration  
    - Project Planning  
    """)

    st.success("Always learning and growing — eager to take on new challenges!")


