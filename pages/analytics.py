import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:#050912;
    color:white;
}

.title {
    font-size:42px;
    color:#00c6ff;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">📈 Learning Analytics</div>',
    unsafe_allow_html=True
)

try:

    df = pd.read_csv("data/students.csv")

    st.subheader("Student Scores")

    st.bar_chart(
        df.set_index("name")["score"]
    )

    st.subheader("Performance Distribution")

    st.line_chart(
        df.set_index("name")["score"]
    )

except Exception:

    st.warning(
        "Please create data/students.csv first."
    )