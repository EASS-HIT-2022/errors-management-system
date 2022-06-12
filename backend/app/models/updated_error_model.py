from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4
#from priority_model import Priority
from models.priority_model import Priority
import datetime

'''Only the parameters we should be able to change'''
class ErrorUpdateRequest(BaseModel):
    name: Optional[str]
    priority: Optional[Priority]
    involved: Optional[List[str]]
    next_step: Optional[str]
    update_date: datetime.datetime

