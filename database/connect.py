import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()
login = os.environ.get('FSTR_DB_LOGIN')
passwd = os.environ.get('FSTR_DB_PASS')
host = os.environ.get('FSTR_DB_HOST')
port = os.environ.get('FSTR_DB_PORT')

DATABASE_URL = f'postgresql+psycopg://{login}:{passwd}@{host}:{port}/pereval'

engine = create_engine(url=DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
