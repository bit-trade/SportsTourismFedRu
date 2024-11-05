from connect import engine
from models import BaseModel


def drop_tables():
    BaseModel.metadata.drop_all(bind=engine)

def create_tables():
    BaseModel.metadata.create_all(bind=engine)


if __name__ == '__main__':
    drop_tables()
    print('База очищена')
    create_tables()
    print('База создана')
