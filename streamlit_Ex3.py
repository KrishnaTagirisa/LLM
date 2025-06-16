import streamlit as st
import pandas as pd

st.title("Example for sample Widget")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}!, How are you today!")

data = {

    "Name": ["Krishna", "Usha", "Gita", "Aarush"],
    "Age":  [12,10,14,9],
    "City": ["Newyork", "Bapatla", "London", "Hyderabad"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
