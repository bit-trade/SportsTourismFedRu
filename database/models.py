from enum import Enum
from datetime import datetime
from sqlalchemy.types import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, LargeBinary


ModelBase = declarative_base()


class StatusPass(Enum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'


class PerevalAdded(ModelBase):
    __tablename__ = 'pereval_added'
    id = Column(Integer, primary_key=True, index=True)
    date_added = Column(DateTime, default=datetime.now)
    raw_data = Column(JSON, nullable=True)
    images = Column(JSON, nullable=True)
    moder_status = Column(PgEnum(StatusPass, name='moderation_status'), nullable=False, default=StatusPass.new)


class PerevalAreas(ModelBase):
    __tablename__ = 'pereval_areas'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), index=True)
    id_parent = Column(Integer, ForeignKey('pereval_areas.id'), nullable=False)


class PerevalImages(ModelBase):
    __tablename__ = 'pereval_images'
    id = Column(Integer, primary_key=True, index=True)
    date_added = Column(DateTime, default=datetime.now)
    title = Column(String(50), index=True)
    img = Column(LargeBinary, nullable=False)


class SprActivitiesTypes(ModelBase):
    __tablename__ = 'spr_activities_types'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))


