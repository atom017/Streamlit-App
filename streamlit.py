import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
barChart = st.container()

df = pd.read_csv('us_school_budget.csv')

with header:
    st.title('My first Streamlit App')

with dataset:
    st.header('US school budget dataset')

    st.dataframe(df)

with barChart:
    if st.button('Get Chart'):
        st.write('Shown are budget spent on education in US.')
        st.bar_chart(df['BUDGET_ON_EDUCATION'])



