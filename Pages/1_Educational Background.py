import streamlit as st
st.title("Educational Background")
col1,col2 = st.columns(2)
with col1:
    st.header("1.")
    st.header("Bachelor of Software Development")
    with st.expander("More Details"):
        st.write("KCA University")
        st.write("May 2022 - July 2025")
        st.write("Honours:Second Class Upper")
    st.header("2.")
    st.header("Data Science Certification")
    with st.expander("More Details"):
        st.write("Emobilis Technology Training Institute")
        st.write("May 2025 - August 2025")
with col2:
    st.header("3.")
    st.header("High School")
    with st.expander("More Details"):
        st.write("Stella Maris Othaya Girls High School")
        st.write("Jan 2018 - April 2022")
        st.write("KCSE Grade: B-")
    st.header("4.")
    st.header("Primary School")
    with st.expander("More Details"):
        st.write("PCEA Karatina Academy")
        st.write("KCPE Score: 360")
