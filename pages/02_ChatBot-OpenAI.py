import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# APIキーの設定
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# メッセージ入力
user_message = st.text_input("メッセージ", "")

if st.button("送信"):
	with st.spinner("考え中..."):
		#API呼び出し
		response = client.chat.completions.create(
			model="gpt-3.5-turbo",
			messages=[
				{"role": "user", "content": user_message}
			]
		)
		ai_response = (
			response.choices[0].message.content
		)
		st.write(f"AI: {ai_response}")
