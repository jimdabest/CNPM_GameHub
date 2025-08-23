from domain.models.redeem import Redeem
from domain.models.iredeem_repository import IRedeemRepository
from typing import List, Optional

class RedeemService:
    def __init__(self, repository: IRedeemRepository):
        self.repository = repository

    def create_redeem(self, player_id: int, reward_id: int, points_used: int, status: str, created_at) -> Redeem:
        redeem = Redeem(id=None, player_id=player_id, reward_id=reward_id, points_used=points_used, status=status, created_at=created_at)
        return self.repository.add(redeem)

    def get_redeem(self, redeem_id: int) -> Optional[Redeem]:
        return self.repository.get_by_id(redeem_id)

    def list_redeems(self) -> List[Redeem]:
        return self.repository.list()

    def update_redeem(self, redeem_id: int, player_id: int, reward_id: int, points_used: int, status: str, created_at) -> Redeem:
        redeem = Redeem(id=redeem_id, player_id=player_id, reward_id=reward_id, points_used=points_used, status=status, created_at=created_at)
        return self.repository.update(redeem)

    def delete_redeem(self, redeem_id: int) -> None:
        self.repository.delete(redeem_id)