import streamlit as st
import numpy as np
import pandas as pd

st.title("App no. 3")
"## Playing with charts"

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['col1', 'col2', 'col3']
)

"### Line chart "
"Printing the chart table"
st.dataframe(chart_data, width = 500)

st.line_chart(chart_data, height = 0)
st.area_chart(chart_data)
st.bar_chart(chart_data)

# Using st.map()
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [27.76, -122.4],
    columns  = ['lat', 'lon']
)

" ### Checking out a map"
"Using the st.dataframe function. Changing the default height."
st.dataframe(map_data, height = 1000)
st.map(map_data)
