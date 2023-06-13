import streamlit as st
from PIL import Image

st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')

image = Image.open('./data/kirin.png')
st.image(image, width=600)

# col1 , col2 = st.columns(2)

# with col1:
#     with st.form(key='profile_form'):
#         # テキストボックス
#         name = st.text_input('名前')
#         address = st.text_input('住所')

#         # ラジオボタン
#         age_category = st.radio(
#             '年齢層',
#             ('子ども(18才未満)', '大人(18才以上)'))

#         # 複数選択
#         hobby = st.multiselect(
#             '趣味',
#             ('スポーツ', '読書', 'プログラミング', 'アニメ・映画', '釣り', '料理'))

#         # ボタン
#         submit_btn = st.form_submit_button('送信')
#         cancel_btn = st.form_submit_button('キャンセル')
#         if submit_btn:
#             st.text(f'ようこそ！{name}さん！{address}に書籍を贈りました！')
#             st.text(f'年齢層: {age_category}')
#             st.text(f'趣味: {", ".join(hobby)}')

# with col2:
#     # データ分析関連
#     df = pd.read_csv('../data.csv', encoding='shift_jis', index_col='年月日')
#     # st.dataframe(df)
#     st.title('1ヶ月間の千葉市の平均気温')
#     st.line_chart(df)
#     # st.bar_chart(df)

#     # matplotlib
#     # fig, ax = plt.subplots()
#     # ax.plot(df.index, df)
#     # ax.set_title('Average temperature in Chiba')
#     # st.pyplot(fig)
