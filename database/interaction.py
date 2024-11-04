from connect import engine
from models import BaseModel


BaseModel.metadata.create_all(engine)

