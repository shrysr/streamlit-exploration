import streamlit as st
import numpy as np
import pandas as pd

st.title("App no. 3")
"## Playing around with charts and data"

chart_data = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['col1', 'col2', 'col3']
)

"### Line chart "
"Printing the chart table"
chart_data

st.line_chart(chart_data)

# Using st.map()
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [27.76, -122.4],
    columns  = ['lat', 'lon']
)

" ### Checking out a map"
map_data
st.map(map_data)
