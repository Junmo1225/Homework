import db2
import datetime as dt
import streamlit as st
import pandas as pd

db = db2.db_pd()

st.title('메모장 v0.1')

option = st.sidebar.selectbox('메뉴',['추가', '읽기', '수정', '삭제','파일 저장','파일 불러오기','취소'])

topic = st.text_input('Type your topic')
body = st.text_input('Type your body')
target_date = st.date_input('Choose your target date')

df = pd.DataFrame({'topic':[topic], 'body':[body], 'target_date':[target_date], 'created_date':[dt.datetime.now()]})


if option == '추가':
    st.write('추가')
    topic = st.text_input('Type your topic (add)')
    body = st.text_input('Type your body (add)')
    target_date = st.date_input('Choose your target date (add)')
    new_data = {'topic':topic, 'body':body, 'target_date':target_date,
                'created_date':dt.datetime.now()}
    df = df.append(new_data, ignore_index=True)
elif option == '읽기':
    st.write('읽기')
    st.write(df)
elif option == '수정':
    body = st.text_input('Type your body (edit)')
    target_date = st.date_input('Choose your target date (edit)')
    st.write('수정')
    select_row = df[df.topic==topic].index
    df.loc[select_row, 'body'] = body
    df.loc[select_row, 'target_date'] = target_date
elif option == '삭제':
    st.write('삭제')
    st.write(df)
    topic = st.text_input('Type your topic (delete)')
    select_row = df[df.topic==topic].index
    df = df.drop(select_row)
elif option == '파일 저장':
    st.write('파일 저장')
    file = st.text_input('Type file name')
    df.to_csv(file)
elif option == '파일 불러오기':
    file = st.text_input('Type file name (load)')
    df = pd.read_csv(file, index_col=0)
elif option == '취소':
    st.write('취소')
    quit()