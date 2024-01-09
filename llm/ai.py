import streamlit as st
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts.chat import HumanMessagePromptTemplate
import pymysql
import pandas as pd
import logging
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS
import json
from llm.llmcallback import ChatCallbackHandler
from langchain.memory import ConversationSummaryBufferMemory,SQLChatMessageHistory

class aihelp:
    def __init__(self):
        OPENAI_API_KEY=st.secrets["OPENAI_API_KEY"]
        HOST=st.secrets["host"]
        PORT=st.secrets["port"]
        USER=st.secrets["user"]
        PASSWORD=st.secrets["password"]
        DATABASE=st.secrets["database"]
        self.connection = pymysql.connect(
            host=HOST,
            port=int(PORT),
            user=USER,
            password =PASSWORD,
            database=DATABASE

        )
        self.llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo',verbose=True,streaming=True,callbacks=[ChatCallbackHandler(),],)
        self.m = ConversationSummaryBufferMemory(llm=self.llm,memory_key="chain_history",return_messages=True)
        
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
            
    def get_tbEx(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        tblist = str(self.tbnm.content).split(',')
        tbnms =""""""
        datas=[]
        for i in range(len(tblist)):
            tbnms +=f"'{tblist[i]}'"
            if i <len(tblist)-1:
                tbnms +=","
        for i in range(len(tblist)):
            cursor.execute(
            f"""
            SELECT
            *
            FROM
                {tblist[i]}
            Order by rand()
            LIMIT 10
            """
            )
            datas += cursor.fetchall()
        cursor.close()
        return pd.DataFrame(datas)    
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
        cursor.close()
        return pd.DataFrame(datas)
    def get_columinfo(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        tblist = str(self.tbnm.content).split(',')
        tbnms =""""""
        for i in range(len(tblist)):
            tbnms +=f"'{tblist[i]}'"
            if i <len(tblist)-1:
                tbnms +=","
        cursor.execute(
            f"""
            SELECT COLUMN_NAME,COLUMN_COMMENT
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA='hairdb'  
            AND TABLE_NAME in ({tbnms});
            """
        )
        datas = cursor.fetchall() 
        cursor.close()
        return pd.DataFrame(datas)
    def run_query(self,query,ask):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        datas = cursor.fetchall() 
        
        #데이터가 없을경우 예외처리 
        if len(pd.DataFrame(datas)) == 0:
            insertquery =f"""
                        INSERT INTO miss_ask(ask,query,insert_date)
                        VALUES ('{ask}','{query}',now())
                        """
            cursor.execute(insertquery)
        cursor.close()
        return pd.DataFrame(datas)
    
    def convertenlish(self,ask):
        translate = """
            Translate incoming Question to English without changing the meaning.
            Question: {question}
            """
        translate_prompt = ChatPromptTemplate.from_template(translate)

        translate_response = (
         translate_prompt
        | self.llm
        )
        res = translate_response.invoke({"question":ask})
        return res.content
    
    def load_memory(self,input):
        return self.m.load_memory_variables({})['chain_history']
    def messageai(self,ask):
        try:
            few_shots = {
                "총직원의수":"select count(*) from employees",
                "직원의 정보": """
                            SELECT emp_no AS '직원 고유 번호', birth_date AS '태어난 날짜', first_name AS '성', last_name AS '이름', gender AS '성별', hire_date AS '입사날짜'
                            FROM employees   
                            """,
                "name의 정보":"""
                            SELECT a.emp_no AS '직원 고유 번호',a.first_name AS '성', a.last_name AS '이름', a.hire_date AS '입사날짜',
                            FROM employees as a
                            where a.first_name like '%name%' or a.last_name like '%name%'
                            """,
                "직원의 임금 정보":"""
                                SELECT a.emp_no AS '직원 고유 번호',a.first_name AS '성', a.last_name AS '이름', a.hire_date AS '입사날짜',
                                b.salary as '임금'
                                FROM employees as a, salaries as b
                                where  a.emp_no = b.emp_no and a.emp_no ='10003'
                                order by b.salary desc 
                                limit 1
                                """,
                "직원의 부서 정보":"""
                SELECT a.emp_no AS '직원 고유 번호',a.first_name AS '성', a.last_name AS '이름', a.hire_date AS '입사날짜',
                            c.dept_name as '부서',
                            b.from_date as '발령날짜',
                            b.to_date as '종료날짜'
                            FROM employees as a, dept_emp as b,departments as c
                            where  a.emp_no = b.emp_no and b.dept_no = c.dept_no
                                """,
                "매니저 정보":"""
                            SELECT a.emp_no AS '직원 고유 번호',a.first_name AS '성', a.last_name AS '이름', a.hire_date AS '입사날짜'
                            FROM employees as a, dept_manager as b
                            where  a.emp_no = b.emp_no 
                            """,
                "전체 정보":"""""",
                "테이블 정보":"""""",
                "매니저 임금정보":"""""",
                
            }
            embeddings = OpenAIEmbeddings()

            few_shot_docs = [
                Document(page_content=question, metadata={"sql_query": few_shots[question]})
                for question in few_shots.keys()
            ]
            
            vector_db = FAISS.from_documents(few_shot_docs, embeddings)
            retriever = vector_db.as_retriever()
            #예상답변을 만들수 있는가?
            ex_prompt = ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        """
                        Let's think step by step 
                        1.Answer the question using ONLY the following context. 
                        Context: {context}
                        2. If you don't know the answer just say "N".
                        3. write a SQL query that would answer the user's question
                        4. query is only english but Add Korean alias to all columns
                        5. Do not change the WHERE clause
                        6. Score how similar they are on a scale of 0-100.
                        7. Your answer should be in JSON format like this
                         - json key is query,score
                         - query is your answer query or "N"
                         - score is similar number in Context
                        
                        """,
                    ),
                    ("human", "{question}"),
                ]
            )
            ex_chain = (
                {
                    "context": retriever,
                    "question": RunnablePassthrough(),
                }
                | ex_prompt
                | self.llm
            )
            ex = ex_chain.invoke(ask)
            print(f'json anser {ex.content}')
            json_object = json.loads(ex.content)
            print(json_object)
            #답변
            result =[]
            # json_object={"query":"N","score":"50"}
            if json_object["query"]== "N" or json_object["score"] < 90:
                #영어로 변역
                translate = """
                Translate incoming Question to English without changing the meaning.
                Question: {question}
                """
                translate_prompt = ChatPromptTemplate.from_template(translate)

                translate_response = (
                translate_prompt
                | self.llm
                )
                task = translate_response.invoke({"question":ask})
                print(f'convert to eng : ${task}')
                #table 선택   
                template = """A schema is a list of tables in a database and the information that describes them. 
                Based on the database schema below, Answer only table names that can answer the user's question.
                {schema}

                Question: {question}
                example: btcusdt_kline_1d,dogeusdt_kline_1d,ethusdt_kline_1d
                """
                
                prompt = ChatPromptTemplate.from_template(template)

                sql_response = (
                RunnablePassthrough.assign(schema=self.get_dbinfo)
                | prompt
                | self.llm
                )
                

                self.tbnm = sql_response.invoke({"question": task})
                print(f'tbnm  : ${self.tbnm.content}')
                self.column = self.get_columinfo()
                print(f'colum : ${self.column}')
                self.tbex = self.get_tbEx()
                print(f'tbex : ${self.tbex}')
                # logging.error(f'table is here : {self.tbnm.content}' )
                # logging.error(f'colum is here : {self.colum }' )
                # result.append("Table Name:"+self.tbnm.content)

                # #해당 테이블에서 스키마를 검색하고 스키마를 통해서 쿼리를 가지고온다
                template = """
                Based on the table schema below, 
                Write a query that matches the rules,
                DON'T make anything up.
                {schema}
                
                1. write a SQL query that would answer the user's question:
                2. SQL query style is MariaDB server
                3. query is only english but Add Korean alias to all columns
                5. You must select {tbnm} table and use all of them unconditionally.
                6. The WHERE clause is not required to be written
                7. The WHERE clause can only select the colum_name of the contents of {column}.
                8. The value of each column is represented by the {columex}, which we'll refer to as the

                

                Question: {question}
                SQL Query:
                """
                # prompt = ChatPromptTemplate.from_template(template)
                prompt =ChatPromptTemplate.from_messages([
                    ("system","""
                        Based on the table schema below, 
                        Write a query that matches the rules,
                        DON'T make anything up.
                        {schema}
                        
                        1. write a SQL query that would answer the user's question:
                        2. SQL query style is MariaDB server
                        3. query is only english but Add Korean alias to all columns
                        5. You must select {tbnm} table and use all of them unconditionally.
                        6. The WHERE clause is not required to be written
                        7. The WHERE clause can only select the colum_name of the contents of {column}.
                    """),
                        MessagesPlaceholder(variable_name="chain_history"),
                    ("human","{question}"),
                ])
                
                sql_response = (
                RunnablePassthrough.assign(schema=self.get_tbinfo)|
                RunnablePassthrough.assign(chain_history=self.load_memory)
                | prompt
                | self.llm
                )
                
                sql = sql_response.invoke({"question": task,"tbnm":self.tbnm,"column":self.column,"columex":self.tbex})
                self.m.save_context({"inpurt":ask},{"ouput":sql.content})
                # print(self.m.load_memory_variables({})['chain_history'])
                logging.error(f'query :{sql.content}')
                result.append(self.run_query(sql.content,ask))
            else:
                self.m.save_context({"inpurt":ask},{"ouput":json_object['query']})
                result.append(self.run_query(json_object['query'],ask))
            return result
        except Exception as e:
            logging.warning(e)
            
            insertquery =f"""
                        INSERT INTO miss_ask(ask,query,insert_date)
                        VALUES ({ask},{str(e)},now())
                        """
            print('=================================')
            print(insertquery)
            cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(insertquery)
            cursor.close()
            return [f'데이터를 불러오는데 실패했습니다. ${e}']
        
    def messageaiplus(self,ask):
        return self.db_chain.run(ask)