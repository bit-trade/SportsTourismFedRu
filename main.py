from typing import Any
from fastapi import FastAPI
from app.data import PerevalRead, PerevalCreate
from database.connect import SessionLocal, get_db
from database.models import  PerevalAdded

pereval = FastAPI()


@pereval.post('/pereval/', response_model=PerevalRead)
async def submit_data(passage: PerevalCreate, db: SessionLocal = next(get_db())) -> Any:
    pereval = PerevalAdded(raw_data=passage.raw_data, images=passage.images)
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval

@pereval.get('/pereval/', response_model=list[PerevalRead])
async def pass_list(skip: int = 0, limit: int = 10, db: SessionLocal = next(get_db())) -> Any:
    pereval = db.query(PerevalAdded).offset(skip).limit(limit).all()
    return pereval

