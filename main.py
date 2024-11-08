from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.data import PerevalCreate, PerevalResponse
from database.connect import get_db
from database.models import  PerevalAdded

pereval = FastAPI()


@pereval.get("/")
async def get_home():
   return {"Service": "OK"}

@pereval.post('/pereval/', response_model=PerevalResponse)
async def submit_data(passage: PerevalCreate, db: Session = Depends(get_db)):
    pereval = PerevalAdded(raw_data=passage.raw_data, images=passage.images)
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval
