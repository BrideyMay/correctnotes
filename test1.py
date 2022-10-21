import streamlit as st
import pandas as pd


#st.header("Metrics File Anonymization")

st.write("""
# Metrics File Anonymization
Use this tool to remove any company, project, or user specific information from your iC Data Center metrics files. 
""")



st.subheader("Upload your CSV for Experiment History")
uploaded_data = st.file_uploader(
    "Drag and Drop or Click to Upload", type=".csv", accept_multiple_files=False
)

if uploaded_data is None:
    st.info("The ExperimentHistory.csv file is usually located in C:\ProgramData\METTLER TOLEDO\iC Data Center\6.1")
    # uploaded_data = open("example.csv", "r")
else:
    st.success("Uploaded your file!")

df = pd.read_csv(uploaded_data)
with st.expander("Raw Dataframe"):
    st.write(df.head)

#df = clean_data(df)
#with st.expander("Cleaned Data"):
#    st.write(df)

# df= pd.read_csv("my_data.csv")
# st.line_chart(df)
