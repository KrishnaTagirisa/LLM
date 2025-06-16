import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "FirstColumn": [1,2,3,4],
    "SecondColumn": [10,20,30,40]
})
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)