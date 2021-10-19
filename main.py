import streamlit as st
import time
st.title('Streamlit 超入門!!!!')

st.write('プログレスバーの表示')
'Start'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'

# st.write('DataFrame')
# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目':[10,20,30,40]
# })

#st.write(df) 細かい設定ができない
#st.dataframe(df.style.highlight_max(axis=0))

#静的なテーブル。並び替えなどはできない
# st.table(df)

"""
# 章
## 節
### 項目

```python
import streamlit as st
import numpy as np
import pandas as pd
```
- 項目を記載する
- 
 
"""
# グラフ表示
# df1 = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['A', 'B', 'C']
# )

# st.line_chart(df1)
# st.area_chart(df1)
# st.bar_chart(df1)

# df2 = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69,139.70],
#     columns=['lat', 'lon']
# )
# #st.table(df2)
# st.map(df2)


#画像を表示する
# if st.checkbox('Show Image'):
#     st.write('Display Image')
#     img = Image.open('grunpa.png')
#     st.image(img, caption='ぐるんぱのようちえん', use_column_width=True)

st.write('InteractiveWidgets.')
#セレクトボックス
option = st.selectbox(
    'あなたの好きな数字をおしえてください',
    options=list(range(1, 11))
)
'あなたの好きな数字は' , option , 'です'
# option_text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('今のあなたの調子は？', 0, 100, 50)
# 'あなたの趣味:', option_text
# 'コンディション:', condition

st.write('アンケート')

# カラム表示
left_coumn, right_column = st.columns(2)
btn_pressed = left_coumn.button('右カラムに文字を表示')
if btn_pressed:
    right_column.write('ここは右カラムです')

# expander??
expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ全部回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ回答２')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ回答３')
