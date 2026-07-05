import streamlit as st


def metric_card(title: str, value: str, icon: str = ""):
    """
    KPI Card

    Parameters
    ----------
    title : str
        Card title

    value : str
        Display value

    icon : str
        Emoji icon
    """

    st.markdown(
        f"""
        <div style="
            background-color:#1B1F2A;
            border:1px solid #30363d;
            border-radius:15px;
            padding:20px;
            height:140px;
            box-shadow:0 2px 6px rgba(0,0,0,.25);
        ">

        <div style="
            font-size:18px;
            color:#BBBBBB;
            margin-bottom:12px;
        ">
            {icon} {title}
        </div>

        <div style="
            font-size:34px;
            font-weight:bold;
            color:white;
        ">
            {value}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )