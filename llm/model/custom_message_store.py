from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.orm import declarative_base

class CustomMessage(declarative_base()):
    __tablename__ = "custom_message_store"

    id = Column(Integer, primary_key=True)
    session_id = Column(Text)
    type = Column(Text)
    content = Column(Text)
    created_at = Column(DateTime)
    author_email = Column(Text)