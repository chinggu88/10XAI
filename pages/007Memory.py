import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory,SQLChatMessageHistory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain.schema.runnable import passthrough,RunnablePassthrough




st.set_page_config(
    page_title="Memory Test Page",
    page_icon="🙉",
)
def load_memory(input):
    print(input)
    return m.load_memory_variables({})['chain_history']

def invoke_chain(question):
    res = chain.invoke({
        "question":question
    })
    m.save_context({"inpurt":question},{"ouput":res.content})
    print(res)
# def add_msg(input,output):
#     wm.save_context({"input":input},{'output':output})
# def get_histoty():
#     return wm.load_memory_variables({})

st.title("메모리 기능 구현🐒")

OPENAI_API_KEY=st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(temperature=0.1,api_key=OPENAI_API_KEY)


m = ConversationSummaryBufferMemory(llm=llm,memory_key="chain_history",return_messages=True)
temp = """
        you are a helpful AI talking to human
        {chain_history}
        Human:{question}
        you:
        """
pormpttemp =ChatPromptTemplate.from_messages([
    ("system","you are a helpful AI talking to human"),
    MessagesPlaceholder(variable_name="chain_history"),
    ("human","{question}"),
])

chain = RunnablePassthrough.assign(chain_history=load_memory) | pormpttemp | llm



invoke_chain("my name is lee kang hun")
invoke_chain("what is my name?")