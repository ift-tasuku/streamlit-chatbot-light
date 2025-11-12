import streamlit as st

st.title("💬 AIチャットボット")

# メッセージ入力
user_message = st.text_input("メッセージ", "")

# 送信ボタン
if st.button("送信"):
    st.write(f"あなた: {user_message}")
    st.write("AI: 応答がここに表示されます")
