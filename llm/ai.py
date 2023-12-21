import streamlit as st
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts.chat import HumanMessagePromptTemplate
import pymysql
import pandas as pd
import logging
class aihelp:
    def __init__(self):
        OPENAI_API_KEY=st.secrets["OPENAI_API_KEY"]
        HOST=st.secrets["host"]
        PORT=st.secrets["port"]
        USER=st.secrets["user"]
        PASSWORD=st.secrets["password"]
        DATABASE=st.secrets["database"]
        self.llm = ChatOpenAI(temperature=0.1, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo',verbose=True)
        self.connection = pymysql.connect(
            host=HOST,
            port=int(PORT),
            user=USER,
            password =PASSWORD,
            database=DATABASE

        )
        
        self.connection = pymysql.connect(
            host=HOST,
            port=int(PORT),
            user=USER,
            password =PASSWORD,
            database=DATABASE
        )
        self.llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo',verbose=True)
        
    def retrieve_from_db(self,query: str) -> str:
        db_context = self.db(query)
        db_context = self,db_context['result'].strip()
        return db_context

    def get_dbinfo(self,_):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT 
                table_name, table_comment
            FROM
                information_schema.tables
            WHERE
                table_schema = 'hairdb'
            """
        )
        datas = cursor.fetchall() 
        cursor.close()
        return datas
            
        
    def get_tbinfo(self,_):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        tblist = str(self.tbnm.content).split(',')
        tbnms =""""""
        for i in range(len(tblist)):
            tbnms +=f"'{tblist[i]}'"
            if i <len(tblist)-1:
                tbnms +=","
        cursor.execute(
            f"""
            SELECT
            table_name, column_name, column_comment
            FROM
                information_schema.columns
            WHERE
                table_schema = 'hairdb' and table_name in ({tbnms});
            """
        )
        
        datas = cursor.fetchall() 
        # for i in range(len(tblist)):
        #     self.cursor.execute(
        #     f"""
        #     SELECT
        #     *
        #     FROM
        #         {tblist[i]}
        #     LIMIT 5
        #     """
        #     )
        #     datas += self.cursor.fetchall()
        cursor.close()
        logging.info(pd.DataFrame(datas))
        return pd.DataFrame(datas)

    def run_query(self,query):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        datas = cursor.fetchall() 
        cursor.close()
        return pd.DataFrame(datas)
    
    def messageai(self,ask):
        try:
            #답변
            result =[]
            #table 선택   
            template = """Based on the database schema below, write just a table_name that would answer the user's question:
            {schema}

            Question: {question}
            """
            prompt = ChatPromptTemplate.from_template(template)

            sql_response = (
            RunnablePassthrough.assign(schema=self.get_dbinfo)
            | prompt
            | self.llm
            )
            

            self.tbnm = sql_response.invoke({"question": ask})
            logging.info(f'table is here : {self.tbnm.content}' )
            # result.append("Table Name:"+self.tbnm.content)

            # #해당 테이블에서 스키마를 검색하고 스키마를 통해서 쿼리를 가지고온다
            template = """Based on the table schema below, Write a query that matches the rules
            1. write a SQL query that would answer the user's question:
            2. SQL query style is MariaDB server
            3. query is only english 
            5. Add Korean alias to all columns
            6. only use table in list variables {tbnm}
            7. only use where  in schema
            {schema}

            Question: {question}
            SQL Query:"""
            prompt = ChatPromptTemplate.from_template(template)
            
            sql_response = (
            RunnablePassthrough.assign(schema=self.get_tbinfo)
            | prompt
            | self.llm
            )
            
            sql = sql_response.invoke({"question": ask,"tbnm":self.tbnm})
            logging.warning(f'query :{sql.content}')
            # result.append("final sql:"+sql.content)
            result.append(self.run_query(sql.content))
            return result
        except Exception as e:
            logging.warning(e)
            return ['데이터를 불러오는데 실패했습니다.']
        
    def messageaiplus(self,ask):
        return self.db_chain.run(ask)