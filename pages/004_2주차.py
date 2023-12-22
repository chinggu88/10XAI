import streamlit as st
import pymysql
import pandas as pd
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
   st.write(pd.DataFrame(datas))

st.header("질문 ->2023년 11월1일부터 2023년 11월30일까지 이더리움 종가 가격을 알려줘")
llm1, llm2, llm3,llm4 = st.tabs(["table 선택  👉🏻","쿼리생성 👉🏻","쿼리실행 👉🏻","결과"])

with llm1:
   "prompt 내용"
   st.code("""
            Based on the database schema below, 
           write just a table_name that would answer the user's question:
        {schema}

        Question: {question}
           """)
   "schema 내용"
   st.code(
       """
        SELECT 
            table_name, table_comment
        FROM
            information_schema.tables
        WHERE
            table_schema = 'hairdb'
        """ 
   )
   st.header("""
        결과 : 'btcusdt_kline_1d','dogeusdt_kline_1d'
             """)
with llm2:
   "prompt 내용"
   st.code("""
            Based on the table schema below, Write a query that matches the rules
        1. write a SQL query that would answer the user's question:
        2. SQL query style is MariaDB server
        3. For column names use only the contents of the schema.
        4. Add Korean alias to all columns
        {schema}

        Question: {question}

           """)
   "schema 내용"
   st.code(
       """
       SELECT
            table_name, column_name, column_comment
            FROM
                information_schema.columns
            WHERE
                table_schema = 'hairdb' and table_name in ({tbnms});
        """ 
   )
   st.header("""
        결과 : SELECT close AS '이더리움 종가 가격'
              FROM ethusdt_kline_1d
              WHERE time >= '2023-11-01' AND time <= '2023-11-30'
             """)
with llm3:
    """
    SELECT close AS '이더리움 종가 가격'
              FROM ethusdt_kline_1d
              WHERE time >= '2023-11-01' AND time <= '2023-11-30'
    """

    st.text('mysql 패키지로 위에 쿼리문을 실행시키고 pandas패키지로 dataframe으로 결과물 생성')
with llm4:
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
,2051.760000000000000000]}
   )
)
   