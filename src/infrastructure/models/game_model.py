from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base

class GameModel(Base):
    __tablename__ = 'games'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=False)
    release_date = Column(DateTime, nullable=False)

   