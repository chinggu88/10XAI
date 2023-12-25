import streamlit as st
import pymysql
import pandas as pd
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
st.set_page_config(
    page_title='10XAI ',
    page_icon='🏝️',
)

"""

"""
llm1, llm2, llm3,llm4 = st.tabs(["TABLE정보불러오기  👉🏻","TABLE정보불러오기 👉🏻","쿼리실행 👉🏻","결과"])

with llm1:
    splitter = CharacterTextSplitter(
    separator = "\n\n",
    # chunk_size = 1000,
    # chunk_overlap  = 200,
    # length_function = len,
    is_separator_regex = False,
    )
    file_path = f"./.cache/files/dbtableinfo.txt"
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load_and_split(text_splitter=splitter)
    docs
# with llm2:
   
# with llm3:
   
# with llm4:
   