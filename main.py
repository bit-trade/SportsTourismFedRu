from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from core.schemas import PassGet, PassAdded, TestSchema
from database.connect import get_db
from database.models import  PerevalAdded, TestTable

# pereval = FastAPI()


# @pereval.get("/")
# async def get_home(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     passages = db.query(PerevalAdded).offset(skip).limit(limit).all()
#     if passages:
#         return passages
#     else:
#         return {'message': 'информация в базе отсутствует'}
#
# @pereval.post('/pereval/')
# async def submit_data(passage: PassAdded, db: Session = Depends(get_db)):
#     pereval = PassAdded(raw_data=passage.raw_data, images=passage.images)
#     db.add(pereval)
#     db.commit()
#     db.refresh(pereval)
#     return pereval


test = FastAPI()


@test.get('/')
def test_home():
    return {'id': 0, 'server': 'OK', 'message': 'Hi there and everyone'}

@test.get('/tests')
def test_get(db: Session = Depends(get_db)):
    tests = db.query(TestTable).all()
    return tests


@test.post('/ittest')
def test_post(test: TestSchema, db: Session = Depends(get_db)):
    item = TestTable(title=test.title, description=test.description, status=test.status)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

