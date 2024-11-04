from connect import engine
from models import BaseModel


def create_tables():
    BaseModel.metadata.create_all(engine)

