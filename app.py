# pylint: disable=missing-module-docstring
import ast
import logging
import os

import duckdb
import streamlit as st

if "data" not in os.listdir():
    print("creating folder data")
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercices_sql_tables" not in os.listdir("data"):
    exec(open("init_db.py").read())
con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)


ANSWER_STR = """
SELECT * FROM beverages 
CROSS JOIN food_items"""

# solutions_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme_list = con.execute("SELECT distinct theme FROM memory_state").df()
    theme = st.selectbox(
        "What would u like to review ?",
        theme_list["theme"].unique(),
        index=None,
        placeholder="Select a theme ",
    )
    st.write("You selected : ", theme)

    exercice = (
        con.execute(f"SELECT * FROM memory_state where theme = '{theme}'")
        .df()
        .sort_values("last_reviewed")
        .reset_index()
    )

    st.write(exercice)
    try:
        exercice_name = exercice.loc[0, "exercice_name"]
        with open(f"answer/{exercice_name}.sql", "r") as f:
            answer = f.read()
            solutions_df = con.execute(answer).df()
    except KeyError as e:
        st.write("Select exercice")


st.header("enter your code:")

query = st.text_area(label="votre code SQL ici,", key="user_input")
#
if query:
    result = con.execute(query).df()
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
                f" result has {n_lines_difference} lines difference with the solution"
            )

    # st.dataframe(result.compare(solutions_df))


# st.write("App SQL practice")
#
#
tab2, tab3 = st.tabs(["Tables", "Solutions"])
#
#
with tab2:
    try:
        exercice_tables = exercice.loc[0, "tables"]

        for table in exercice_tables:
            st.write(f"table: {table}")
            print(f"{table}")
            df_table = con.execute(f"SELECT * FROM {table}").df()
            st.dataframe(df_table)
    except KeyError as k:
        st.write("Select exercice")
#     st.dataframe(food_items)
#     st.write("expected")
#     st.dataframe(solutions_df)
#
with tab3:

    try:
        st.write(answer)
    except NameError as n:
        st.write("Select exercice")
