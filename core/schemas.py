import json
from enum import Enum
from datetime import datetime
from typing import Any, List, Dict, Union
from pydantic import BaseModel, Json, Field, JsonValue


class ModerStatus(str, Enum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'


class PassGet(BaseModel):
    data_added: Union[str, datetime] = datetime.now()
    moder_status: Union[str, ModerStatus]  = ModerStatus.new


class PassAdded(PassGet):
    raw_data: Union[Dict[str, Any], Json] = None
    images: Union[list[Dict], Json] = None

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
