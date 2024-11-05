from enum import Enum
from typing import Any, Dict
from datetime import datetime
from pydantic import BaseModel, Json, Field


class ModerStatus(Enum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'


class PerevalCreate(BaseModel):
    raw_data: Json[Dict]
    images: Json[Dict]
    moder_status: ModerStatus = ModerStatus.new


class PerevalResponse(BaseModel):
    id: int
    data_added: datetime
    raw_data: Json[Dict]
    images: Json[Dict]
    moder_status: ModerStatus = ModerStatus.new

    class Config:
        from_attributes = True


class PerevalAreasAdd(BaseModel):
    title: str = Field(max_length=80)
    id_parent: int


class PerevalAreasResponse(BaseModel):
    id: int
    title: str
    id_parent: int

    class Config:
        from_attributes = True


class SprActivTypesAdd(BaseModel):
    title: str = Field(max_length=20)


class SprActivTypesResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True

# class PerevalImagesAdd(BaseModel):
#     img:

