import streamlit as st

st.title("ナンピン後の価格はいかに")

current_shares = st.number_input(
    "元々の株数",
    min_value=0,
    value=200,
    step=100
)

current_price = st.number_input(
    "元々の価格",
    min_value=0.0,
    value=208.0,
    step=1.0
)

add_shares = st.number_input(
    "追加の株数",
    min_value=0,
    value=100,
    step=100
)

add_price = st.number_input(
    "追加の価格",
    min_value=0.0,
    value=197.0,
    step=1.0
)

total_shares = current_shares + add_shares

if total_shares > 0:
    new_average = (
        current_shares * current_price
        + add_shares * add_price
    ) / total_shares

    st.header("計算結果")

    st.markdown(
        f"""
        <div style="
            background-color:#0e4025;
            padding:20px;
            border-radius:10px;
            text-align:center;
        ">
            <h3 style="color:white;">
                ナンピン後平均取得単価
            </h3>
            <h1 style="color:#00ff88;
                       font-size:140px;
            ">
                {new_average:.2f}円
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.warning("株数を入力してください")