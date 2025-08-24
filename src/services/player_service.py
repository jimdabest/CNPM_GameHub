from domain.models.player import Player
from domain.models.iplayer_repository import IPlayerRepository
from typing import List, Optional

class PlayerService:
    def __init__(self, repository: IPlayerRepository, user_service=None):
        self.repository = repository
        self.user_service = user_service

    def create_player(self, user_id: int, scores: int, points: int, created_at, updated_at) -> Player:
        player = Player(id=None, user_id=user_id, scores=scores, points=points, created_at=created_at, updated_at=updated_at)
        result = self.repository.add(player)
        
        # Cập nhật role của user thành 'player'
        if self.user_service:
            self.user_service.update_user_role(user_id, 'player')
        
        return result

    def get_player(self, player_id: int) -> Optional[Player]:
        return self.repository.get_by_id(player_id)

    def list_players(self) -> List[Player]:
        return self.repository.list()

    def update_player(self, player_id: int, user_id: int, scores: int, points: int, created_at, updated_at) -> Player:
        player = Player(id=player_id, user_id=user_id, scores=scores, points=points, created_at=created_at, updated_at=updated_at)
        return self.repository.update(player)

    def delete_player(self, player_id: int) -> None:
        self.repository.delete(player_id)
    
    def deduct_points(self, player_id: int, points: int) -> None:
        """Trừ points của player"""
        player = self.repository.get_by_id(player_id)
        if player and player.points >= points:
            from datetime import datetime
            self.repository.update(Player(
                id=player_id,
                user_id=player.user_id,
                scores=player.scores,
                points=player.points - points,
                created_at=player.created_at,
                updated_at=datetime.utcnow()
            ))
        else:
            raise ValueError(f'Player does not have enough points. Required: {points}')
    
    def add_points(self, player_id: int, points: int) -> None:
        """Thêm points cho player"""
        player = self.repository.get_by_id(player_id)
        if player:
            from datetime import datetime
            self.repository.update(Player(
                id=player_id,
                user_id=player.user_id,
                scores=player.scores,
                points=player.points + points,
                created_at=player.created_at,
                updated_at=datetime.utcnow()
            ))
        else:
            raise ValueError(f'Player with id {player_id} not found')
    
    def update_total_scores(self, player_id: int, new_score: int) -> None:
        """Cập nhật total scores của player"""
        player = self.repository.get_by_id(player_id)
        if player:
            from datetime import datetime
            self.repository.update(Player(
                id=player_id,
                user_id=player.user_id,
                scores=player.scores + new_score,
                points=player.points,
                created_at=player.created_at,
                updated_at=datetime.utcnow()
            ))
        else:
            raise ValueError(f'Player with id {player_id} not found')
    
    def add_achievement_points(self, player_id: int, bonus_points: int) -> None:
        """Thưởng points cho achievement"""
        self.add_points(player_id, bonus_points)