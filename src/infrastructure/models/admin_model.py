from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base


class admin(Base):
    __tablename__ = 'admin'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False, unique=True)

    user = relationship('user_model', back_populates='admin')
    payout_transactions = relationship('payout_transactions', back_populates='admin')
