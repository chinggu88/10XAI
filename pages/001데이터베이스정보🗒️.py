import streamlit as st
import pymysql
import pandas as pd



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

st.subheader('1️⃣.테이블 정보 확인하기')
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

st.subheader('2️⃣.테이블 전체적인 구상도')
st.image('img/erd.png')
st.link_button('ERD상세 확인 링크','https://dbdiagram.io/d/10XAI-659d421eac844320ae8ade2b')

st.subheader('3️⃣.테이블을 확인 후 질문하러 가기')
st.write('🫵개발자에게눈치보지말라 페이지로 이동 후 사용해보기')
st.write('더욱더 검색이 잘되는 팁👀')
st.write('테이블의 단어를 활용하여 검색하기')
st.write('ex)월급최고 높은사람(🙅‍♂️)->임금최고높은 직원(🙆‍♂️)')

st.subheader('4️⃣.개발자분들 주목👏')
st.write('이 답변이 맞는지 궁금하죠❓❓ ')
st.write('질문결과와 어떤 쿼리가 실행되었는지 쿼리까지 보여드립니다.🖥️')
st.write('개발자들만드러오기 페이지로 이동 후 사용해보기')

st.title("📌📌📌📌📌📌📌📌📌📌📌📌📌📌📌📌")
st.subheader("주의) 완성도 높은 프로젝트를 위해서 질문에 대한 에러가 발생할시  ")
st.subheader("database에 저장되오니 개인정보와 같은 민감한 정보는 사용을 자제 부탁드립니다.")
st.title("📌📌📌📌📌📌📌📌📌📌📌📌📌📌📌📌")