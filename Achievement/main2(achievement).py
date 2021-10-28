import db2
import datetime as dt
import streamlit as st

db = db2.db_pd() #make copy, instance

st.title('메모장 v0.1')

option = st.sidebar.selectbox('메뉴',['추가', '읽기', '수정', '삭제','파일 저장','파일 불러오기'])

if option == '추가':
    st.write('추가')
elif option == '읽기':
    st.write('읽기')
else:
    st.write('추가 아님')

#db.read()
#b = db.create('abc', 'class test', dt.datetime(2021,3,10))

#a = db.read()

#db.save('test.csv')

#b = db.load('test.csv')

#ddd = db2.db_pd()
#ddd.read()