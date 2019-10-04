import streamlit as st
import numpy as np
import pandas as pd
import sys

# Preamble
st.title("App No. 2")
st.write("This app tests simple commands in python")

# Simple commands
st.write("Printing the python and system version")
st.write(sys.version_info)
st.write(sys.version)

# Using magic , similar to the example in the docs

st.write("Trying out magic. This essentially means that any variable or literal value on it's own line is passed to st.write()")
df = pd.DataFrame({
    'col 1':['AA', 'BB', 'CC'],
    'col 2':[1 , 2, 3],
    'col 3':["this", "is", "col3"]
})

df

# Testing literal values

13
"The above was a literal value. i.e 13 was just written."
"Both this and the above are literal strings placed in the script! This is actually quite handy, but it does not appear to be good programming practice, i.e more useful for quick demonstrations and notes."
