import streamlit as st
import numpy
import pandas

st.title('First app using streamlit')
st.write('This explores creating a table and adding a title')

# Creating a table

st.write("Creating a table")
st.write(pandas.DataFrame({
    'col 1': [100,200,456,678],
    'col 2': ['a', 'b', 'c', 'd']
}))
