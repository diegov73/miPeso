from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class RegistroPeso_create(BaseModel):
    peso: float

class RegistroPeso_response(BaseModel):
    id: UUID
    peso: float
    fecha: datetime

    class Config:
        from_attributes = True