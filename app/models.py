from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4
import datetime

'''All kinds of priority'''
class Priority(str, Enum):
    blocker = "Blocker"
    high = "High"
    medium = "Medium"
    low = "Low"

'''The basic information about error'''
class Error(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    priority: Priority
    involved: List[str]
    next_step: str
    accept_date: datetime.date
    update_date: Optional[datetime.datetime]

'''Only the parameters we should be able to change'''
class ErrorUpdateRequest(BaseModel):
    name: Optional[str]
    priority: Optional[Priority]
    involved: Optional[List[str]]
    next_step: Optional[str]
    update_date: datetime.datetime

