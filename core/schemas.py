from enum import Enum
from typing import Any, Dict, Union
from pydantic import BaseModel, Json

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

