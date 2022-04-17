import db
import streamlit as st
import datetime as dt

sm = db.user_db()

#sm.create('프로젝트1', 'task1', '책임자1', 협업='abc',일정 = dt.date(2021,11,14))
#sm.create('프로젝트2', 'task2', '책임자2', 협업='abc',일정 = dt.date(2021,11,14))
#sm.create('프로젝트3', 'task3', '책임자3', 협업='abc',일정 = dt.date(2021,11,14))
#sm.create('프로젝트4', 'task4', '책임자4', 협업='abc',일정 = dt.date(2021,11,14))
#sm.create('프로젝트5', 'task5', '책임자5', 협업='abc',일정 = dt.date(2021,11,14))

#a = sm.read()

option = st.sidebar.selectbox('Select one', ['New Data', 'Read', 'Delete'])
if option == 'New Data':
    pro = st.text_input('Type project name')
    task = st.text_input('Type task')
    responsible = st.text_input('Type who is responsible')
    cooperation = st.text_input('Type cooperation')
    date = st.date_input('Choose date')
    if pro=='':
        st.write('Type project name')
    if task=='':
        st.write('Type task name')
    if responsible=='':
        st.write('Who is responsible')  
    add = st.button('Add')
    if pro != '':
        if task != '':
            if responsible != '':
                if add:
                    sm.create(pro, task, responsible, cooperation, date)
                    st.title('Data is created')
    
elif option == 'Read':
    keyword = st.text_input('Choose project to read')
    searched = sm.read(keyword)
    st.write(searched)
    
elif option == 'Delete':
    searched = sm.read()
    options = st.multiselect('Choose data to delete', searched.프로젝트)
    delete_button = st.button('Delete')
    if delete_button:
        sm.delete(options)
    st.write(options)