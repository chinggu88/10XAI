import streamlit as st
st.set_page_config(
    page_title='10XAI ',
    page_icon='🏝️',
)

"""
Memory 기능 구현\n
->중복된 답변을 최소화 하면 비용절감에 도움됨
1. ConversationBufferMemory -> 단순 저장, 대화 전체가 무제한으로 저장됨
2. ConversationBufferwindowMemory -> 대화전체가 지정한 수 만큼 저장됨 자원은 효과적으로 쓰지만 예전 대화를 알 수 없음
3. ConversationSummaryMemory -> ai와의 대화를 요약해서 저장함
4. ConversationSummaryBufferMemory -> 지정한 대화의 수는 최신순으로 저장되면 과거 대화는 요약해서 저장함

cache기능이외 db연동하여 저장할 수 있으면 백업도 가능함
"""