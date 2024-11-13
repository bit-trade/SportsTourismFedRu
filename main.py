from typing import Annotated
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from core.schemas import PassGet, PassAdded
from database.connect import get_db
from database.models import  PerevalAdded

pereval = FastAPI()


@pereval.get('/')
def get_home(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    passages = db.query(PerevalAdded).offset(skip).limit(limit).all()
    if passages:
        return passages
    else:
        return {'message': 'информация в базе отсутствует'}

@pereval.post('/pereval/')
def submit_data(passage: Annotated[PassAdded, Depends()], db: Session = Depends(get_db)):
    pereval = PerevalAdded(raw_data=passage.raw_data, images=passage.images, moder_status=passage.moder_status)
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval

