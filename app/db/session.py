from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base

engine = create_engine("sqlite:///./database.db", echo=True)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Example: Insert a new RawData entry
# def create_sample_raw_data():
#     session = SessionLocal()
#     try:
#         new_data = RawData(
#             temperature=23.5,
#             light_level_raw=150,
#             voltage=220.0,
#             amperage=5.5,
#             wattage=1210.0,
#         )
#         session.add(new_data)
#         session.commit()
#         session.refresh(new_data)
#         print(f"Inserted RawData with ID: {new_data.id}")
#     finally:
#         session.close()
