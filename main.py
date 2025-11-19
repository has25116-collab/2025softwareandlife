import streamlit as st

st.title("はじめのウェブアプリです!")
name = st.text_input("なまえを入力してぐださい! : ")
menu = st.selectbox("好きなことを選んで具ださい: ", ["アモンドボンボン"、"ままはアイリアン"])
if st.button("sentence make"):
  st.write(name + "さん、ごん日は。好きなテイストは" + menu + "ですね！")
  
