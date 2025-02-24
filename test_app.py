import streamlit as st

st.title("Hello World")
st.write("これは初アプリです")

name = st.text_input("あなたの名前を教えてください")
st.write("あなたの名前",name)

if st.button("クリック！"):
    st.write("クリックされました！")

age = st.slider("あなたの年齢は?",0,100,20)
st.write("あなたの年齢は",age,"歳")