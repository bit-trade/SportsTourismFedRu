from connect import engine
from models import ModelBase


def drop_tables():
    ModelBase.metadata.drop_all(bind=engine)

def create_tables():
    ModelBase.metadata.create_all(bind=engine)


if __name__ == '__main__':
    drop_tables()
    print('База очищена')
    create_tables()
    print('База создана')
