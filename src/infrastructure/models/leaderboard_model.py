from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, FLOAT
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class LeaderboardModel(Base):
    __tablename__ = 'leaderboard'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    game_id = Column(Integer, ForeignKey('game.id'), nullable=False)
    score = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=False)

    game = relationship("GameModel", back_populates="leaderboards")
    player = relationship("PlayerModel", back_populates="leaderboards")