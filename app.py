# app.py
import streamlit as st
st.title("🎉 Hello Streamlit!")
st.write("これがWebアプリです")

name = st.text_input("名前を入力")
if st.button("挨拶"):
    st.write(f"こんにちは、{name}さん!")
