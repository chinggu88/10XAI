import requests
import streamlit as st
import pandas as pd
import numpy as np
import time

st.header('요약')
col1, col2= st.columns(2)
col1.metric("비트코인", "54,412,834.45KRW", "+199,489.63 (0.37%)오늘")
col2.metric("이더리움", "2,888,008.74KRW", "−36,732.42 (1.26%)오늘")

st.header('데이터 검색')
df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

st.table(df)

chart_data = pd.DataFrame(
   {
       "PRICE": np.random.randn(20),
       "DATE": np.random.randn(20),
       "COIN": np.random.choice(["BTC", "ETC"], 20),
   }
)

st.header('차트')
st.line_chart(chart_data, x="DATE", y="PRICE", color="COIN")

progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()