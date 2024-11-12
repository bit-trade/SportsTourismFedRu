from enum import Enum
from typing import Any, Dict, Union

from datetime import datetime
from pydantic import BaseModel, Json, Field


class ModerStatus(str, Enum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'


class PassGet(BaseModel):
    id: int | None
    data_added: Union[str, datetime] = datetime.now()
    moder_status: Union[str, ModerStatus]  = ModerStatus.new


class PassAdded(PassGet):
    raw_data: dict[str, str]
    images: dict[str, str]

    class Config:
        from_attributes = True


class PasslAreasAdd(BaseModel):
    title: str = Field(max_length=80)
    id_parent: int


class PassAreasResponse(BaseModel):
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

class PassImagesAdd(BaseModel):
    pass


class ItemEnum(str, Enum):
    new = 'new'
    old = 'old'
    used = 'used'


class TestSchema(BaseModel):
    title: str = Field(max_length=50)
    description: Union[str, None] = Field(default=' ')
    data_stamp: Union[str, datetime] = datetime.now()
    status: Union[str, ItemEnum] = ItemEnum.new

    class Config:
        from_attributes = True
