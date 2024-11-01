from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped, mapped_column


BaseModel = declarative_base()


class PerevalAdded(BaseModel):
    __tablename__ = 'pereval_added'
    id = Column(Integer, primary_key=True)
    date_added = Column(DateTime)
    raw_data = Column(JSONB)
    images = Column(JSONB)


class PerevalAreas(BaseModel):
    __tablename__ = 'pereval_areas'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    id_parent = Column(Integer, ForeignKey('pereval_areas.id'), nullable=False)


class PerevalImages(BaseModel):
    __tablename__ = 'pereval_images'
    id = Column(Integer, primary_key=True)
    date_added = Column(DateTime, default=datetime.now)
    img = Column(LargeBinary, nullable=False)


class SprActivitiesTypes(BaseModel):
    __tablename__ = 'spr_activities_types'
    id = Column(Integer, primary_key=True)
    title = Column(Text)

