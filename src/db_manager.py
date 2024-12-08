import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./local_data.db")

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()

class ConversationHistory(Base):
    __tablename__ = 'conversation_history'
    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(Text)
    model_response = Column(Text)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def save_interaction(user_input, model_response):
    session = SessionLocal()
    record = ConversationHistory(user_input=user_input, model_response=model_response)
    session.add(record)
    session.commit()
    session.close()

def load_recent_interactions(limit=5):
    session = SessionLocal()
    records = session.query(ConversationHistory).order_by(ConversationHistory.id.desc()).limit(limit).all()
    session.close()
    return records
