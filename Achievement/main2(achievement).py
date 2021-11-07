import db2
import datetime as dt
import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def connect_db():
    db = db2.db_pd()
    return db

db = connect_db()

st.title('Memo v0.1')

option = st.sidebar.selectbox('Menu',['Choose one option','add', 'read', 'edit', 'delete','save file','load file','quit'])

if option == 'Choose one option':
    st.write('Choose one option')

if option == 'add':
    st.write('add')
    topic = st.text_input('Type your topic (add)')
    body = st.text_input('Type your body (add)')
    target_date = st.date_input('Choose your target date (add)')
    button = st.button('Add')
    if button:
        st.write(target_date)
        st.write(type(target_date))
        db.create(topic, body, target_date)

elif option == 'read':
    st.write('read')
    df = db.read()
    st.write(df.astype('str'))

elif option == 'edit':
    df = db.read()
    st.write(df.astype('str'))
    topic = st.text_input('Type your topic (edit)')
    body = st.text_input('Type your body (edit)')
    target_date = st.date_input('Choose your target date (edit)')
    db.update(topic, body, target_date)

elif option == 'delete':
    df = db.read()
    st.write(df.astype('str'))
    topic = st.text_input('Type your topic (delete)')
    button4 = st.button('Delete')
    if button4:
        db.delete(topic)
            
elif option == 'save file':
    file = st.text_input('Type your file name (save)')
    button2 = st.button('Save')
    if button2:
        db.save(file)

elif option == 'load file':
    file = st.text_input('Type your file name (load)')
    button3 = st.button('Load')
    if button3:
        db.load(file)
elif option == 'quit':
    st.write('Do you want to quit')
    button7 = st.button('Quit')
    if button7:
        quit()