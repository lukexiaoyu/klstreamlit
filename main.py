'''
# This is the document title

This is some _markdown_.
'''

import streamlit as st
import pandas as pd

a=90
b=60
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
st.write(a+b)
st.write(a-b)
st.write(df)