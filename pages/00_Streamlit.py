import streamlit as st
import pandas as pd
import numpy as np

# ========================================
# ページ設定
# ========================================
st.set_page_config(
    page_title="Streamlit基本ガイド",
    page_icon="📚",
    layout="wide"  # "centered" or "wide"
)

# ========================================
# タイトルと見出し
# ========================================
st.title("📚 Streamlit 基本ガイド")
st.markdown("---")

st.header("1️⃣ テキスト表示")
st.write("st.write() は最も汎用的な表示関数です")
st.text("st.text() は固定幅フォントで表示します")
st.markdown("**st.markdown()** は *マークダウン* で `書式設定` ができます")
st.code("print('st.code() でコードを表示')", language="python")

st.markdown("---")

# ========================================
# 入力ウィジェット
# ========================================
st.header("2️⃣ 入力ウィジェット")

# テキスト入力
text_input = st.text_input("テキスト入力", "ここに入力してください")
st.write(f"入力された値: {text_input}")

# テキストエリア（複数行）
text_area = st.text_area("テキストエリア", "複数行の\nテキストを入力")
st.write(f"入力された値: {text_area}")

# 数値入力
number = st.number_input("数値入力", min_value=0, max_value=100, value=50, step=1)
st.write(f"選択された数値: {number}")

# スライダー
slider_value = st.slider("スライダー", min_value=0, max_value=100, value=50)
st.write(f"スライダーの値: {slider_value}")

# セレクトボックス
option = st.selectbox(
    "選択してください",
    ["オプション1", "オプション2", "オプション3"]
)
st.write(f"選択されたオプション: {option}")

# マルチセレクト
multi_select = st.multiselect(
    "複数選択",
    ["りんご", "バナナ", "オレンジ", "ぶどう"],
    default=["りんご"]
)
st.write(f"選択された項目: {multi_select}")

# チェックボックス
checkbox = st.checkbox("チェックボックス")
if checkbox:
    st.write("✅ チェックされています")

# ラジオボタン
radio = st.radio(
    "ラジオボタン",
    ["選択肢A", "選択肢B", "選択肢C"]
)
st.write(f"選択: {radio}")

st.markdown("---")

# ========================================
# ボタンとアクション
# ========================================
st.header("3️⃣ ボタンとアクション")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("通常のボタン"):
        st.success("ボタンがクリックされました！")

with col2:
    if st.button("警告ボタン", type="primary"):
        st.warning("プライマリボタンです")

with col3:
    # ダウンロードボタン
    sample_data = "これはサンプルテキストです"
    st.download_button(
        label="ファイルをダウンロード",
        data=sample_data,
        file_name="sample.txt",
        mime="text/plain"
    )

st.markdown("---")

# ========================================
# レイアウト
# ========================================
st.header("4️⃣ レイアウト")

# カラムレイアウト
st.subheader("カラム分割")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.info("カラム A")
    st.write("左側のカラム")
with col_b:
    st.success("カラム B")
    st.write("中央のカラム")
with col_c:
    st.warning("カラム C")
    st.write("右側のカラム")

# エキスパンダー
st.subheader("エキスパンダー（折りたたみ）")
with st.expander("クリックして展開"):
    st.write("ここに隠れているコンテンツがあります")
    st.image("https://via.placeholder.com/300x150", caption="サンプル画像")

# タブ
st.subheader("タブ")
tab1, tab2, tab3 = st.tabs(["タブ1", "タブ2", "タブ3"])
with tab1:
    st.write("タブ1の内容")
with tab2:
    st.write("タブ2の内容")
with tab3:
    st.write("タブ3の内容")

st.markdown("---")

# ========================================
# データ表示
# ========================================
st.header("5️⃣ データ表示")

# サンプルデータフレーム作成
df = pd.DataFrame({
    '名前': ['田中', '佐藤', '鈴木', '高橋'],
    '年齢': [25, 30, 35, 28],
    '都市': ['東京', '大阪', '名古屋', '福岡']
})

st.subheader("データフレーム")
st.dataframe(df)  # インタラクティブな表示

st.subheader("静的なテーブル")
st.table(df)  # 静的な表示

# JSONデータ
st.subheader("JSON表示")
json_data = {
    "name": "Streamlit",
    "version": "1.0",
    "features": ["簡単", "高速", "美しい"]
}
st.json(json_data)

st.markdown("---")

# ========================================
# チャート
# ========================================
st.header("6️⃣ チャート")

# ラインチャート
st.subheader("ラインチャート")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# エリアチャート
st.subheader("エリアチャート")
st.area_chart(chart_data)

# バーチャート
st.subheader("バーチャート")
st.bar_chart(chart_data)

st.markdown("---")

# ========================================
# セッション状態
# ========================================
st.header("7️⃣ セッション状態（状態管理）")

# カウンターの例
if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.write(f"現在のカウント: {st.session_state.counter}")

col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if st.button("➕ 増やす"):
        st.session_state.counter += 1
        st.rerun()
with col_btn2:
    if st.button("➖ 減らす"):
        st.session_state.counter -= 1
        st.rerun()
with col_btn3:
    if st.button("🔄 リセット"):
        st.session_state.counter = 0
        st.rerun()

st.markdown("---")

# ========================================
# メッセージ表示
# ========================================
st.header("8️⃣ メッセージ表示")

st.success("✅ 成功メッセージ (st.success)")
st.info("ℹ️ 情報メッセージ (st.info)")
st.warning("⚠️ 警告メッセージ (st.warning)")
st.error("❌ エラーメッセージ (st.error)")

st.markdown("---")

# ========================================
# プログレスバーとスピナー
# ========================================
st.header("9️⃣ プログレスバーとスピナー")

import time

if st.button("プログレスバーを表示"):
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(101):
        progress_bar.progress(i)
        status_text.text(f"進行中: {i}%")
        time.sleep(0.01)

    status_text.text("完了！")
    st.balloons()  # お祝いのバルーン

st.markdown("---")

# ========================================
# サイドバー
# ========================================
st.header("🔟 サイドバー")
st.write("左側のサイドバーを確認してください →")

# サイドバーに要素を追加
st.sidebar.title("サイドバー")
st.sidebar.write("ここはサイドバーです")
sidebar_option = st.sidebar.selectbox(
    "サイドバーの選択",
    ["オプション1", "オプション2", "オプション3"]
)
st.sidebar.slider("サイドバーのスライダー", 0, 100, 50)

st.write(f"サイドバーで選択されたオプション: {sidebar_option}")

st.markdown("---")

# フッター
st.markdown("""
### 💡 補足情報
- すべてのウィジェットは自動的に再実行をトリガーします
- `st.session_state` で状態を保持できます
- より詳しい情報は [Streamlit公式ドキュメント](https://docs.streamlit.io) を参照してください
""")
