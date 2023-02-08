import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid, JsCode, GridOptionsBuilder

def slice_for_link_only(link):
    _, link = link[:-2].split("](")
    return link


st.title("Movie Board")

col_names = ["Name", "Rating", "Link"]
df = pd.read_csv("output.txt", delimiter=";", names=col_names)
df["Name"] = df["Name"].str.replace("- ", "")
df["Link"] = df["Link"].apply(slice_for_link_only)


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