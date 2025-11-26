import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

st.title("2重軸チャートのサンプル")

# サンプルデータの作成
dates = pd.date_range(start="2023-01-01", periods=30, freq="D")
np.random.seed(42)
# 第1軸用データ (例: 気温)
data1 = np.random.normal(20, 5, 30)
# 第2軸用データ (例: 湿度 - 異なるスケール)
data2 = np.random.normal(60, 10, 30)

# チャートの作成
# make_subplotsを使って2重軸(secondary_y=True)を設定
fig = make_subplots(specs=[[{"secondary_y": True}]])

# 第1軸のトレースを追加
fig.add_trace(
    go.Scatter(x=dates, y=data1, name="気温 (℃)", mode="lines+markers"),
    secondary_y=False,
)

# 第2軸のトレースを追加
fig.add_trace(
    go.Bar(x=dates, y=data2, name="湿度 (%)", opacity=0.5),
    secondary_y=True,
)

# レイアウトの設定
fig.update_layout(
    title_text="気温と湿度の推移 (2重軸)",
    hovermode="x unified" # ホバー時にX軸で同期して表示
)

# 軸のタイトル設定
fig.update_yaxes(title_text="気温 (℃)", secondary_y=False)
fig.update_yaxes(title_text="湿度 (%)", secondary_y=True)
fig.update_xaxes(title_text="日付")

# Streamlitで表示
st.plotly_chart(fig, use_container_width=True)

st.info("Plotlyを使用することで、2重軸のチャートを作成し、軸の同期やインタラクティブな操作が可能になります。")
