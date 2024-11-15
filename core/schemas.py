from enum import Enum
from typing import Any, Dict, Union
from pydantic import BaseModel, Json, Field

class ModerStatus(str, Enum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'


class PassGet(BaseModel):
    moder_status: Union[str, ModerStatus]  = ModerStatus.new


class PassAdded(PassGet):
    raw_data: Union[Dict[str, Any], Json] = None
    images: Union[list[Dict], Json] = None

    class Config:
        from_attributes = True


user = {
    "email": "user@email.tld",
    "phone": "79031234567",
    "fam": "ПупкинПупкин",
    "name": "Василий",
    "otc": "Иванович"
}


class PassUpdate(BaseModel):
    moder_status: Union[str, ModerStatus] = Field(default=ModerStatus.accepted)
    raw_data: Union[Dict[str, Any], Json] = None
    user: Union[Dict[str, Any], Json] = Field(default=user, frozen=True)
    coords: Union[Dict[str, Any], Json] = Field(default=None)
    level: Union[Dict[str, Any], Json] = Field(default=None)
    images: Union[list[Dict], Json] = None

    class Config:
        from_attributes = True
