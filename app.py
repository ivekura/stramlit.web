import streamlit as st
from PIL import Image

st.title('みずのサイト')
st.caption('みずぼんの擬人垢です')
st.subheader('みずボンの紹介')
st.text('みず　関東出身　好きな食べ物まるふぉい')

#画像
image=Image.open('みずと.jpg')
st.image(image,width=200)

#テキストボックス
name =st.text_input('名前')
print(name)

#セレクトボックス
osi=st.selectbox(
    '推し',
    ('ガウル','レイ','イソ','ウォニョン','みず','ユジン'))

#ボタン
submit_bth=st.button('送信')
cancel_btn=st.button('キャンセル')
print(f'submit_btn:{submit_bth}')
print(f'cancel_btn:{cancel_btn}')
if submit_bth:
    st.text(f'ようこそ{name}さん!!')
    st.text(f'推し:{osi}')
if osi=='みず':
    st.text('しね')    
    
      



    
    