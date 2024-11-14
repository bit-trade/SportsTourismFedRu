from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from core.schemas import PassAdded
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
def update_pass(pass_id: int, passage: Annotated[PassAdded, Depends()] , db: Session = Depends(get_db)):
    pereval = db.get(PerevalAdded, pass_id)
    if not pereval:
        raise HTTPException(status_code=404, detail="Passage not found")

    print('\n', pereval, type(pereval), '\n')
    print(f'raw_data is {pereval.raw_data}' , type(pereval.raw_data), '\n')
    print(f'moder_status is {pereval.moder_status}', type(pereval.moder_status), '\n')

    if pereval.moder_status == StatusPass.new:
        pereval = PerevalAdded(date_added=passage.data_added, raw_data=passage.raw_data,
                               images=passage.images, moder_status=passage.moder_status)
        db.add(pereval) # !!!!
        db.commit()
        db.refresh(pereval)
        return pereval

