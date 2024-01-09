import streamlit as st
from llm.ai import aihelp
from langchain.memory import StreamlitChatMessageHistory

from llm.customai import customai
history = StreamlitChatMessageHistory(key="dev_messages")
ai = aihelp()
if "dev_msg" not in st.session_state:
    st.session_state["dev_msg"] =[]
    

def send_msg(msg,role,save = True):
    with st.chat_message(role):
        if role == 'human':
            st.write(msg)
        else:
            st.write(msg[0])
            st.code(msg[1])
        
    #저장
    if save:
        st.session_state["dev_msg"].append({"msg":msg,"role":role})
    
for msg in st.session_state["dev_msg"]:
    send_msg(msg["msg"],msg['role'],False) 
    

msg = st.chat_input('대화를 입력하세요')

if msg:
    send_msg(msg,"human")
    #캐쉬작업 추가
    history.add_user_message(msg)
    with st.spinner("물어보는중"):
        #ai에 묻기
        data = ai.messageai(msg)
        # data = ai.convertenlish(msg)
        history.add_ai_message(data)
        send_msg(data,"ai")
        # for i in range(len(data)):
        #     send_msg(data[i],"ai")
