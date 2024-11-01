from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


engine = create_engine(url=settings.database_url, echo=True)
session = sessionmaker(engine)
