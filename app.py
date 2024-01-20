import streamlit as st
import pandas as pd
import duckdb
from pandas import DataFrame

st.write("App SQL practice")
with st.sidebar:
    option = st.selectbox("What would u like to review ?",
                            ["Joins", "Group by", "Windows Functions"],
                          index=None,
                          placeholder="Select a theme "
                          )
    st.write('You selected : ', option)


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
data = {"a": [1, 2, 3], "b": [4, 5, 6] }
df = pd.DataFrame(data)




with tab1:
    input_text = st.text_area(label="Entrez votre texte")
    tmp = duckdb.query(input_text)
    st.write(f"Votre requête est la suivante :  {input_text}")
    st.dataframe(tmp)
with tab2:
    st.header("A dog")

with tab3:
    st.header("A Owl")
