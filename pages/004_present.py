import streamlit as st
import pymysql
import pandas as pd

from llm.ai import aihelp
st.set_page_config(
    page_title='10XAI ',
    page_icon='🏝️',
)

HOST=st.secrets["host"]
PORT=st.secrets["port"]
USER=st.secrets["user"]
PASSWORD=st.secrets["password"]
DATABASE=st.secrets["database"]

connection = pymysql.connect(
    host=HOST,
    port=int(PORT),
    user=USER,
    password =PASSWORD,
    database=DATABASE
)

cursor = connection.cursor(pymysql.cursors.DictCursor)
st.title('🦜🔗 langchain을 이용해서 Database 정보를 조회 및 표현')

st.header("1.라벨링 작업 💾")
tab1, tab2, tab3,tab4 = st.tabs(["테이블 목록", "5분", "1시간","하루"])

with tab1:
   st.subheader("테이블 목록 및 라벨링")
   cursor.execute(
            """
            SELECT 
                table_name as 테이블이름, table_comment as '라벨링'
            FROM
                information_schema.tables
            WHERE
                table_schema = 'hairdb'
            """
        )
   datas = cursor.fetchall()
   st.write(pd.DataFrame(datas))

with tab2:
   st.subheader("5분 테이블 (비트코인,이더리움,도지코인,솔라나,리플)")
   cursor.execute(
            """
            SELECT
            count(*) as '데이터 갯수'
            FROM
                btcusdt_kline_5min
            """
        )
   datas = cursor.fetchall()
   st.write(pd.DataFrame(datas))
   cursor.execute(
            """
            SELECT
            column_name as '컬럼이름', column_comment as '컬럼라벨링'
            FROM
                information_schema.columns
            WHERE
                table_schema = 'hairdb' and table_name in ('btcusdt_kline_5min');
            """
        )
   datas = cursor.fetchall()
   st.subheader("컬럼이름과 라벨링")
   st.write(pd.DataFrame(datas))
   cursor.execute(
            """
            SELECT
            *
            FROM
                btcusdt_kline_5min
                limit 5
            """
        )
   datas = cursor.fetchall()
   st.subheader("데이터 샘플")
   st.write(pd.DataFrame(datas))

with tab3:
   st.subheader("1시간 테이블 (비트코인,이더리움,도지코인,솔라나,리플)")
   cursor.execute(
            """
            SELECT
            count(*) as '데이터 갯수'
            FROM
                btcusdt_kline_1h
            """
        )
   datas = cursor.fetchall()
   st.write(pd.DataFrame(datas))
   cursor.execute(
            """
            SELECT
            column_name as '컬럼이름', column_comment as '컬럼라벨링'
            FROM
                information_schema.columns
            WHERE
                table_schema = 'hairdb' and table_name in ('btcusdt_kline_1h');
            """
        )
   datas = cursor.fetchall()
   st.subheader("컬럼이름과 라벨링")
   st.write(pd.DataFrame(datas))
   cursor.execute(
            """
            SELECT
            *
            FROM
                btcusdt_kline_1h
                limit 5
            """
        )
   datas = cursor.fetchall()
   st.subheader("데이터 샘플")
   st.write(pd.DataFrame(datas))

with tab4:
   st.subheader("하루 테이블 (비트코인,이더리움,도지코인,솔라나,리플)")
   cursor.execute(
            """
            SELECT
            count(*) as '데이터 갯수'
            FROM
                btcusdt_kline_1d
            """
        )
   datas = cursor.fetchall()
   st.write(pd.DataFrame(datas))
   cursor.execute(
            """
            SELECT
            column_name as '컬럼이름', column_comment as '컬럼라벨링'
            FROM
                information_schema.columns
            WHERE
                table_schema = 'hairdb' and table_name in ('btcusdt_kline_1d');
            """
        )
   datas = cursor.fetchall()
   st.subheader("컬럼이름과 라벨링")
   st.write(pd.DataFrame(datas))
   cursor.execute(
            """
            SELECT
            *
            FROM
                btcusdt_kline_1d
                limit 5
            """
        )
   datas = cursor.fetchall()
   st.subheader("데이터 샘플")
   st.write(pd.DataFrame(datas))

st.divider()
st.header("2.메인 작업 💻")
st.subheader("질문 ->2023년 11월1일부터 2023년 11월30일까지 이더리움 종가 가격을 알려줘")
llm1, llm2, llm3,llm4,llm5 = st.tabs(["영어로 변환 👉🏻","table 선택  👉🏻","쿼리생성 👉🏻","쿼리실행 및 결과👉🏻","실제 구현"])
with llm1:
   "prompt 내용"
   st.code("""
            Translate incoming Question to English without changing the meaning.
            Question: {question}
            -------------------------------------------------
            의미를 변경하지 않고 들어오는 질문을 영어로 번역합니다.
           """)
   "question 내용"
   st.header("""
        결과 : Please tell me the closing price of Ethereum from November 1, 2023, to November 30, 2023.
             """)
with llm2:
   "prompt 내용"
   st.code("""
            Based on the database schema below, 
           write just a table_name that would answer the user's question:
        {schema}

        Question: {question}
        -------------------------------------------------
        아래 데이터베이스 스키마를 기반으로,사용자의 질문에 답할 table_name만 작성하세요.
           """)
   "schema 내용"
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
   st.write(pd.DataFrame(datas))

   st.header("""
        결과 : 'ethusdt_kline_1d'
             """)
with llm3:
   "prompt 내용"
   st.code("""
        Based on the table schema below, 
        Write a query that matches the rules,
        DON'T make anything up.

        1. write a SQL query that would answer the user's question:
        2. SQL query style is MariaDB server
        3. query is only english but Add Korean alias to all columns
        5. You must select {tbnm} table and use all of them unconditionally.
        6. The WHERE clause can only be selected within {colum}.
        7. The WHERE clause is not required to be written
        {schema}

        Question: {question}
        -----------------------------------------------------------
        아래 테이블 스키마를 기반으로,
        규칙과 일치하는 쿼리를 작성하고,
        아무것도 꾸며내지 마세요.

        1. 사용자의 질문에 대답하는 SQL 쿼리를 작성합니다.
        2. SQL 쿼리 스타일은 MariaDB 서버입니다.
        3. 쿼리는 영어로만 되어 있지만 모든 열에 한국어 별칭을 추가합니다.
        5. 반드시 {tbnm} 테이블을 선택하여 무조건 모두 사용해야 합니다.
        6. WHERE 절은 {colum} 내에서만 선택할 수 있습니다.
        7. WHERE 절을 반드시 작성할 필요는 없습니다.
           """)
   
   "schema 내용"
   st.code(
       """
       SELECT
            table_name, column_name, column_comment
            FROM
                information_schema.columns
            WHERE
                table_schema = 'hairdb' and table_name in ('ethusdt_kline_1d');
        ----------------------------------------------
        """ 
   )
   cursor.execute(
            """
             SELECT
            table_name, column_name, column_comment
            FROM
                information_schema.columns
            WHERE
                table_schema = 'hairdb' and table_name in ('ethusdt_kline_1d');
            """
        )
   datas = cursor.fetchall()
   st.write(pd.DataFrame(datas))
   
   st.header("""
        결과 : SELECT close AS 종가 FROM ethusdt_kline_1d WHERE time >= '2023-11-01' AND time <= '2023-11-30'
             """)
with llm4:
    """
    SELECT close AS '이더리움 종가 가격'
              FROM ethusdt_kline_1d
              WHERE time >= '2023-11-01' AND time <= '2023-11-30'
    """

    st.text('mysql 패키지로 위에 쿼리문을 실행시키고 pandas패키지로 dataframe으로 결과물 생성')

    st.dataframe(data=pd.DataFrame(
      {'이더리움 종가 가격':[                 
    1848.200000000000000000
    ,1800.680000000000000000
    ,1832.490000000000000000
    ,1856.080000000000000000
    ,1892.490000000000000000
    ,1901.710000000000000000
    ,1885.790000000000000000
    ,1888.420000000000000000
    ,2122.920000000000000000
    ,2079.100000000000000000
    ,2054.520000000000000000
    ,2046.080000000000000000
    ,2055.180000000000000000
    ,1980.110000000000000000
    ,2059.290000000000000000
    ,1962.130000000000000000
    ,1961.210000000000000000
    ,1963.190000000000000000
    ,2012.460000000000000000
    ,2022.410000000000000000
    ,1933.440000000000000000
    ,2063.910000000000000000
    ,2062.680000000000000000
    ,2081.160000000000000000
    ,2082.870000000000000000
    ,2061.970000000000000000
    ,2027.570000000000000000
    ,2048.200000000000000000
    ,2028.410000000000000000
    ,2051.760000000000000000]
    }
   )
)
with llm5:
    ai = aihelp()
    data = ai.messageai("2023년 11월1일부터 2023년 11월30일까지 이더리움 종가 가격을 알려줘")
    for i in range(len(data)):
        data[i]

st.divider()   
st.header("3.느낀점 및 앞으로 계획💭")
"""
✅ 질문은 잘게 쪼게서 여러번 실행하는게 좋은거 같다\n
✅ join 복잡한 where절은 복불복인다...\n
✅ 결과 값을 분석하는 방법 추가 작업\n
✅ 쿼리를 이용해서 사용하는게 아니라 그냥 데이터베이스 내용을 전체를 불러들여서 RAG방식으로 처리하는게 더 좋을까?\n
✅ 결과 쿼리, 질문, 쿼리 결과를 통해서 RAG기법을 활용해서 결과를 표출해야되나?\n
"""

st.image('img/ret.png')