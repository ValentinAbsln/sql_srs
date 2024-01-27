# pylint: disable=missing-module-docstring
import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice, 2.5
Expression, 2
Tea, 3
"""

beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie juice, 2.5
chocolatine, 2
muffin, 3"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages 
CROSS JOIN food_items"""

solutions_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    option = st.selectbox(
        "What would u like to review ?",
        ["Joins", "Group by", "Windows Functions"],
        index=None,
        placeholder="Select a theme ",
    )
    st.write("You selected : ", option)


st.header("enter your code:")

query = st.text_area(label="votre code SQL ici,", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    if len(result.columns) != len(solutions_df.columns):
        st.write("Some columns are missing")
    try:
        result = result[solutions_df.columns]
    except KeyError as e:
        st.write("Some columns are missing")
    n_lines_difference = result.shape[0] - solutions_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f" result has {n_lines_difference} lines difference with the solution)"
        )

    st.dataframe(result.compare(solutions_df))


st.write("App SQL practice")


tab2, tab3 = st.tabs(["Tables", "Solutions"])


with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solutions_df)

with tab3:
    st.write(ANSWER_STR)
