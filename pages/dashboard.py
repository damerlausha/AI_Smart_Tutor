import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
    font-weight:bold;
    color:#00c6ff;
}

.card {
    padding:25px;
    border-radius:20px;
    background:#0b1627;
    border:1px solid #173454;
    transition:.3s;
}

.card:hover {
    transform:translateY(-5px);
    border-color:#00b7ff;
    box-shadow:0 0 25px rgba(0,183,255,.2);
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">📊 Student Dashboard</div>',
    unsafe_allow_html=True
)

st.write("")

try:
    df = pd.read_csv("data/students.csv")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Students", len(df))

    with col2:
        st.metric("Average Score", f"{df['score'].mean():.1f}%")

    with col3:
        st.metric("Highest Score", f"{df['score'].max()}%")

    with col4:
        st.metric("Lowest Score", f"{df['score'].min()}%")

    st.write("")

    st.subheader("Student Performance")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

except Exception:
    st.warning("students.csv not found.")