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
    moder_status: Union[str, ModerStatus] = ModerStatus.accepted
    basic_info: Union[Dict[str, Any], None] = None
    coords: Union[Dict[str, Any], None] = None
    level: Union[Dict[str, Any], None] = None
    images: Union[list[Dict], None] = None

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "basic_info": {
                        "beautyTitle": "пер. ",
                        "title": "Пхия",
                        "other_titles": "Триев",
                        "connect": "",
                        "add_time": "2021-09-22 13:18:13"
                    },
                    "user": {
                        "email": "user@email.tld",
                        "phone": "79031234567",
                        "fam": "Иванов",
                        "name": "Василий",
                        "otc": "Иванович"
                    },
                    "coords": {
                        "latitude": "45.3842",
                        "longitude": "7.1525",
                        "height": "1200"
                    },
                    "level": {
                        "winter": "",
                        "summer": "1А",
                        "autumn": "1А",
                        "spring": ""
                    },
                    "images": [
                        {
                            "id": 1,
                            "title": "Седловина"
                        },
                        {
                            "id": 2,
                            "title": "Подъем"
                        }]
                }
            ]
        }
    }
