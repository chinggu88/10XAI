import pymysql
import pandas as pd
from langchain.chat_models import ChatOpenAI
class customai:
    def __init__(self,host,port,user,pw,db):
        try:
            self.connection = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password =pw,
            database=db
            )
            # self.llm = ChatOpenAI(temperature=0.1, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo',verbose=True)
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        except:
            print('error connect')
        
    def getconnect(self):
        try:
         return self.connection.open
        except:
            return False
        