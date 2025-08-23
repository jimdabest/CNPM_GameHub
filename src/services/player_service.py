from domain.models.player import Player
from domain.models.iplayer_repository import IPlayerRepository
from typing import List, Optional

class PlayerService:
    def __init__(self, repository: IPlayerRepository):
        self.repository = repository

    def create_player(self, user_id: int, scores: int, points: int, created_at, updated_at) -> Player:
        player = Player(id=None, user_id=user_id, scores=scores, points=points, created_at=created_at, updated_at=updated_at)
        return self.repository.add(player)

    def get_player(self, player_id: int) -> Optional[Player]:
        return self.repository.get_by_id(player_id)

    def list_players(self) -> List[Player]:
        return self.repository.list()

    def update_player(self, player_id: int, user_id: int, scores: int, points: int, created_at, updated_at) -> Player:
        player = Player(id=player_id, user_id=user_id, scores=scores, points=points, created_at=created_at, updated_at=updated_at)
        return self.repository.update(player)

    def delete_player(self, player_id: int) -> None:
        self.repository.delete(player_id)