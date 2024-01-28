# pylint: disable=missing-module-docstring
import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercices_sql_tables.duckdb",read_only=False)


ANSWER_STR = """
SELECT * FROM beverages 
CROSS JOIN food_items"""

#solutions_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would u like to review ?",
        ["cross_joins", "Group by", "Windows Functions"],
        index=None,
        placeholder="Select a theme ",
    )
    st.write("You selected : ", theme)

    exercice = con.execute(f"SELECT * FROM memory_state where theme = '{theme}'").df()

    st.write(exercice)

st.header("enter your code:")

query = st.text_area(label="votre code SQL ici,", key="user_input")
#
# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)
#
#     if len(result.columns) != len(solutions_df.columns):
#         st.write("Some columns are missing")
#     try:
#         result = result[solutions_df.columns]
#     except KeyError as e:
#         st.write("Some columns are missing")
#     n_lines_difference = result.shape[0] - solutions_df.shape[0]
#     if n_lines_difference != 0:
#         st.write(
#             f" result has {n_lines_difference} lines difference with the solution)"
#         )
#
#     st.dataframe(result.compare(solutions_df))
#
#
# st.write("App SQL practice")
#
#
# tab2, tab3 = st.tabs(["Tables", "Solutions"])
#
#
# with tab2:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("expected")
#     st.dataframe(solutions_df)
#
# with tab3:
#     st.write(ANSWER_STR)
