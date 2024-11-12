from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from core.schemas import PassGet, PassAdded
from database.connect import get_db
from database.models import  PerevalAdded

pereval = FastAPI()


@pereval.get("/")
async def get_home(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    passages = db.query(PerevalAdded).offset(skip).limit(limit).all()
    if passages:
        return passages
    else:
        return {'message': 'информация в базе отсутствует'}

@pereval.post('/pereval/')
async def submit_data(passage: PassAdded, db: Session = Depends(get_db)):
    pereval = PassAdded(raw_data=passage.raw_data, images=passage.images)
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval
