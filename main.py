from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.data import PerevalCreate, PerevalResponse
from database.connect import get_db
from database.models import  PerevalAdded

pereval = FastAPI()


@pereval.get("/")
async def get_home():
   return {"Hello": "World"}

@pereval.post('/pereval/', response_model=PerevalResponse)
async def submit_data(passage: PerevalCreate, db: Session = Depends(get_db)):
    pereval = PerevalAdded(raw_data=passage.raw_data, images=passage.images)
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return PerevalResponse(id=pereval.id, data_added=pereval.date_added, raw_data=pereval.raw_data,
                           images=pereval.images, moder_status=pereval.moder_status)
