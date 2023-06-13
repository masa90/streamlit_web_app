import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データ分析関連
df = pd.read_csv('./data/data.csv', encoding='shift_jis', index_col='年月日')
st.title('1ヶ月間の千葉市の平均気温')
st.line_chart(df)
# st.bar_chart(df)
# st.dataframe(df)

# matplotlib
# fig, ax = plt.subplots()
# ax.plot(df.index, df)
# ax.set_title('Average temperature in Chiba')
# st.pyplot(fig)
