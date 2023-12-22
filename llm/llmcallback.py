from langchain.callbacks.base import BaseCallbackHandler
import streamlit as st
class ChatCallbackHandler(BaseCallbackHandler):
    message = ""

    def on_llm_start(self, *args, **kwargs):
        self.message_box = st.empty()

    def on_llm_end(self, *args, **kwargs):
        st.session_state["messages"].append({"message": self.message, "role":  "ai"})

    def on_llm_new_token(self, token, *args, **kwargs):
        self.message += token
        self.message_box.markdown(self.message)