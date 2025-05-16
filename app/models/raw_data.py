from datetime import datetime

from sqlalchemy import DateTime, Integer, Float
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.db.base import Base


class RawData(Base):
    __tablename__ = "raw_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    temperature: Mapped[float] = mapped_column(Float)
    light_level_raw: Mapped[int] = mapped_column(Integer)
    voltage: Mapped[float] = mapped_column(Float)
    amperage: Mapped[float] = mapped_column(Float)
    wattage: Mapped[float] = mapped_column(Float)
