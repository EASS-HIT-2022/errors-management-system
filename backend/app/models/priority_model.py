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

