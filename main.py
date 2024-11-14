from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from core.schemas import PassAdded
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

@pereval.post('/submitData')
def submit_data(passage: PassAdded, db: Session = Depends(get_db)):
    pereval = PerevalAdded(raw_data=passage.raw_data, images=passage.images, moder_status=passage.moder_status)
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
