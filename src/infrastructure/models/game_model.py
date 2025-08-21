from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from infrastructure.databases.base import Base

class game_model(Base):
    __tablename__ = 'game'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey('developer.id'), nullable=False)  
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    sources = Column(String(255), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    

