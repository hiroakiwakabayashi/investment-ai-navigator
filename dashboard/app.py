import streamlit as st

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="Investment AI Navigator",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

/* 全体 */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* KPIカード */
div[data-testid="metric-container"]{
    background:#1B1F2A;
    border-radius:12px;
    padding:20px;
    border:1px solid #30363d;
}

/* メトリック文字 */
div[data-testid="metric-container"] label{
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Header
# ==========================

st.title("📈 Investment AI Navigator")

st.caption(
    "AI-powered investment dashboard for overseas investors."
)

st.divider()

# ==========================
# Welcome
# ==========================

left, right = st.columns([2, 1])

with left:

    st.subheader("Welcome")

    st.write("""
Investment AI Navigator analyzes global financial news,
calculates investment scores,
and generates AI-powered daily market reports.

Use the sidebar to explore:

- 📄 Reports
- 📰 News
- 📊 Analytics
- 💼 Portfolio
- ⚙ Settings
""")

with right:

    st.info("""
Today's Features

✅ AI News Analysis

✅ Investment Score

✅ Daily Report

✅ Market Sentiment

✅ Risk Analysis
""")

st.divider()

# ==========================
# Quick Start
# ==========================

col1, col2, col3 = st.columns(3)

with col1:

    st.success("📄 Reports")

    st.write(
        "Browse historical AI-generated reports."
    )

with col2:

    st.info("📰 News")

    st.write(
        "View analyzed market news."
    )

with col3:

    st.warning("📊 Analytics")

    st.write(
        "Explore investment trends and market insights."
    )

st.divider()

# ==========================
# Footer
# ==========================

st.caption(
    "Investment AI Navigator Pro v1.0"
)