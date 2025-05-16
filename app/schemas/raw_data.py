from datetime import datetime

from pydantic import BaseModel


class RawDataSchema(BaseModel):
    id: int
    created_at: datetime
    temperature: float
    light_level_raw: int
    voltage: float
    amperage: float
    wattage: float

    class Config:
        orm_mode = True


class RawDataCreateSchema(BaseModel):
    temperature: float
    light_level_raw: int
    voltage: float
    amperage: float
    wattage: float
