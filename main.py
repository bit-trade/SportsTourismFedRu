from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from pydantic import Field
from sqlalchemy.orm import Session
from core.schemas import PassAdded, PassUpdate
from database.connect import get_db
from database.models import PerevalAdded, StatusPass

pereval = FastAPI()


@pereval.get('/')
def get_home(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    passages = db.query(PerevalAdded).offset(skip).limit(limit).all()
    if passages:
        return passages
    else:
        return {'message': 'информация в базе отсутствует'}


@pereval.post('/submitData')
def submit_data(passage: PassAdded, db: Session = Depends(get_db)):
    pereval = PerevalAdded(raw_data=passage.raw_data, images=passage.images)
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval


@pereval.get('/submitData/{pass_id}')
def get_pass(pass_id: int, db: Session = Depends(get_db)):
    pereval = db.get(PerevalAdded, pass_id)
    if not pereval:
        raise HTTPException(status_code=404, detail="Passage not found")

    return pereval


@pereval.patch('/submitData/{pass_id}')
def update_pass(pass_id: int, passage: PassUpdate, db: Session = Depends(get_db)):
    pereval = db.get(PerevalAdded, pass_id)
    if not pereval:
        raise HTTPException(status_code=404, detail="запись не найдена")

    if pereval.moder_status == StatusPass.new:
        pereval.moder_status = passage.moder_status
        raw_data = passage.basic_info
        raw_data["coords"] = passage.coords
        raw_data["level"] = passage.level
        pereval.raw_data = raw_data
        pereval.images = passage.images
        db.commit()
        db.refresh(pereval)
        return [pereval, {'state': 1}]
    else:
        return {'state': 0, 'message': 'статус записи не соответствует значению new'}
