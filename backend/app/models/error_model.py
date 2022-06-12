import imp
from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4
from .priority_model import Priority
import datetime

'''The basic information about error'''
class Error(BaseModel):
    #id: Optional[UUID] = uuid4()
    name: str
    priority: Priority
    involved: List[str]
    next_step: str
    accept_date: datetime.datetime
    update_date: Optional[datetime.datetime]

