import pandas as pd
from llm.ragllm import ragllm
from langchain.prompts import ChatPromptTemplate
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings import CacheBackedEmbeddings, OpenAIEmbeddings
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.storage import LocalFileStore
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models import ChatOpenAI

import streamlit as st


l = ragllm()
def creattxtfile():
    # Open text file in write mode
    text_file = open(".cache/files/dbtableinfo.txt", "w")

    # Take content
    content = l.dbinfo()

    # Write content to file
    text_file.write(content)

    # Close file
    text_file.close()
    
def format_docs(docs):
    # "\n\n".join(document.page_content for document in docs)
    print(docs)
    return "\n\n".join(document.page_content for document in docs)

def get_retriever():
    cache_dir = LocalFileStore(f"./.cache/embeddings/dbtableinfo.txt")

    splitter = CharacterTextSplitter(
        separator = "\n\n",
        chunk_size = 1400,
        chunk_overlap  = 200,
        length_function = len,
        is_separator_regex = False,
    )
    file_path = f"./.cache/files/dbtableinfo.txt"
    loader = UnstructuredFileLoader(file_path)
    docs = loader.load_and_split(text_splitter=splitter)
    embeddings = OpenAIEmbeddings()
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)
    vectorstore = FAISS.from_documents(docs, cached_embeddings)
    retriever = vectorstore.as_retriever()
    return retriever

def aksai(msg):
    #테이브 선택
    dbprompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                Based on the database schema below, write just a table_name that would answer the user's question:
                {schema}
                """,
            ),
            ("human", "{question}"),
        ]
    )
    dbchain = (
            {
                "schema": ret | RunnableLambda(format_docs),
                "question": RunnablePassthrough(),
            }
            | dbprompt
            | l.llm
        )


    dbnm =dbchain.invoke(msg)
    st.write(dbnm.content)
    
    st.write(dbnm)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                Based on the table Context below, 
                Write a query that matches the rules,
                DON'T make anything up.

                1. write a SQL query that would answer the user's question:
                2. SQL query style is MariaDB server
                3. query is only english 
                5. Add Korean alias to all columns
                6.You must select table from variable a and use all of them unconditionally.
                7. The WHERE clause does not need to be written.
                
                Context: {context}
                """
                +f'table :{dbnm}',
            ),
            ("human", "{question}"),
        ]
    )
    chain = (
            {
                "context": ret | RunnableLambda(format_docs),
                "question": RunnablePassthrough(),
            }
            | prompt
            | l.llm
        )


    sql =chain.invoke(msg)
    st.write(sql.content)
    respone = l.run_query(sql.content)
    st.write(respone)
    
#데이터베이스 스키마정보 txt파일로 저장
creattxtfile()

ret =get_retriever()

m = "2023년 11월 1일 비트코인 종가정보"
st.header(m)
aksai(m)

# m = "2023년 11월 1일 이더리움 종가정보"
# st.header(m)
# aksai(m)

# m = "2023년 11월 1일 이더리움과비트코인 종가정보"
# st.header(m)
# aksai(m)

# m = "2023년 11월 1일부터 일주일간 이더리움 종가정보"
# st.header(m)
# aksai(m)

# m = "2023년 11월 1일부터 일주일간 이더리움과비트코인 정보"
# st.header(m)
# aksai(m)

# m = "restaurant 정보 5개만 알려줘"
# st.header(m)
# aksai(m)