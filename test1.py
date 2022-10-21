import streamlit as st
import pandas as pd


st.header("Metrics File Anonymization")

st.write("""
# My first app
Hello *world!*
""")



st.subheader("Upload your CSV for Experiment History")
uploaded_data = st.file_uploader(
    "Drag and Drop or Click to Upload", type=".csv", accept_multiple_files=False
)

if uploaded_data is None:
    st.info("Using example data. Upload a file above to use your own data!")
    # uploaded_data = open("example.csv", "r")
else:
    st.success("Uploaded your file!")


# df= pd.read_csv("my_data.csv")
# st.line_chart(df)
