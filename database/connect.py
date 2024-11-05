from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


engine = create_engine(url=settings.database_url, echo=True)
session = sessionmaker(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
