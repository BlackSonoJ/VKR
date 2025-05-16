import serial
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.raw_data import RawData
from app.schemas.raw_data import RawDataCreateSchema


def _read_data(ser: serial.Serial):
    metrics = ser.readline().decode("utf-8").strip().split()
    return {metric.split(":")[0]: metric.split(":")[1] for metric in metrics}


def _validate_data(ser: serial.Serial):
    return RawDataCreateSchema(**_read_data(ser))


def add_to_db(
    ser: serial.Serial = serial.Serial("COM1", 9600, timeout=1),
    session: Session = None,
):
    session = session if session else SessionLocal()
    try:
        new_data = RawData(**_validate_data(ser))
        session.add(new_data)
        session.commit()
        session.refresh(new_data)
    finally:
        session.close()
