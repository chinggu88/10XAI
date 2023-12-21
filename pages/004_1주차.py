import streamlit as st
st.divider() 
st.title("1.프로젝트 진행상황")
st.subheader('🙇강훈')
st.subheader('📱테스트 사이트 생성')
st.code('https://7yymfoyzx2fm2pp3fjm7pf.streamlit.app/chatting')
st.subheader('💻FAST API를 통해 서버 구현')
st.subheader('💸GPT 제한 설정')
st.image('img/limit.png')
st.subheader('🐣GPT-4 - 데이터베이스 연동 완료 및 테스트 코드 작성완료')
st.code("""
db = SQLDatabase.from_uri(MYSQL_URL)


OPENAI_API_KEY="sk-blabla"
llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo')
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
db_chain.run(ask)
""")
st.divider() 
st.subheader('🙇예찬')
st.subheader('💾데이터 전처리 - 더미 데이터 라벨링 진행')
st.subheader('📘RAG 방식으로 라벨링한 데이터 삽입')

st.divider() 
st.title("3.프로젝트 예정")
st.subheader('📔GPT 전체 흐름 파악하기')
st.subheader('📘캐싱, 임베디드, prompt기술적용')
st.subheader('📗다양한 타입의 데이터가 나올 수 있게 셋팅')