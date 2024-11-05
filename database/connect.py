import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings, SettingsConfigDict



load_dotenv()
login = os.environ.get('FSTR_DB_LOGIN')
passwd = os.environ.get('FSTR_DB_PASS')
host = os.environ.get('FSTR_DB_HOST')
port = os.environ.get('FSTR_DB_PORT')

DATABASE_URL = f'postgresql+psycopg://{login}:{passwd}@{host}:{port}/pereval'

# class EnvSetting(BaseSettings):
#     model_config = SettingsConfigDict(env_file='.env', extra='ignore')
#
#
# class Environment(EnvSetting):
#     FSTR_DB_HOST: str
#     FSTR_DB_PORT: str
#     FSTR_DB_LOGIN: str
#     FSTR_DB_PASS: str
#
#     @property
#     def DATABASE_URL(self):
#         return f'postgresql+psycopg://{self.FSTR_DB_LOGIN}:{self.FSTR_DB_PASS}@{self.FSTR_DB_HOST}:{self.FSTR_DB_PORT}/pereval'


# settings = Environment()
# engine = create_engine(url=settings.DATABASE_URL, echo=True)
engine = create_engine(url=DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
