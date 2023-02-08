# pip3 install streamlit streamlit-aggrid
import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid, JsCode, GridOptionsBuilder

def slice_for_link_only(link: str) -> str:
    """Helper function to slice the string we are using as link formatted in markdown in our
    output.txt so we can use it to generate clickable hyperlinks in a table later on.

    Args:
        link (str): String with Markdown-Syntax containing the link to IMDb

    Returns:
        str: Hyperlink to IMDb
    """
    _, link = link[:-2].split("](")
    return link


st.title("Movie Board")

col_names = ["Name", "Rating", "Link"]
df = pd.read_csv("output.txt", delimiter=";", names=col_names)
df["Name"] = df["Name"].str.replace("- ", "")
df["Link"] = df["Link"].apply(slice_for_link_only)


# Could find a solution to build a grid with st_aggrid on the streamlit
# forums proposed by the user edsaac:
# https://discuss.streamlit.io/t/how-to-display-a-clickable-link-pandas-dataframe/32612/5
gb = GridOptionsBuilder.from_dataframe(df)

gb.configure_column("Link",
                    headerName="Link",
                    cellRenderer=JsCode(
                        """
                        function(params) {
                            return '<a target=_blank href=' + params.value + '>IMDb</a>'
                            }
                        """))

gridOptions = gb.build()

AgGrid(df, gridOptions=gridOptions, allow_unsafe_jscode=True)