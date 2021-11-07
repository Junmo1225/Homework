import streamlit as st
import seaborn as sns
import pandas as pd

car_crashes = sns.load_dataset('car_crashes')

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(car_crashes)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='car_crashes.csv',
    mime='text/csv',
    )

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, encoding = 'utf-8)')
    st.write(dataframe)