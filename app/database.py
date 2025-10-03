from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)  # echo=True prints SQL queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
