from domain.models.reward import Reward
from domain.models.ireward_repository import IRewardRepository
from typing import List, Optional

class RewardService:
    def __init__(self, repository: IRewardRepository):
        self.repository = repository

    def create_reward(self, name: str, description: str, point_required: int, quantity: int, created_at, updated_at) -> Reward:
        reward = Reward(id=None, name=name, description=description, point_required=point_required, quantity=quantity, created_at=created_at, updated_at=updated_at)
        return self.repository.add(reward)

    def get_reward(self, reward_id: int) -> Optional[Reward]:
        return self.repository.get_by_id(reward_id)

    def list_rewards(self) -> List[Reward]:
        return self.repository.list()

    def update_reward(self, reward_id: int, name: str, description: str, point_required: int, quantity: int, created_at, updated_at) -> Reward:
        reward = Reward(id=reward_id, name=name, description=description, point_required=point_required, quantity=quantity, created_at=created_at, updated_at=updated_at)
        return self.repository.update(reward)

    def delete_reward(self, reward_id: int) -> None:
        self.repository.delete(reward_id)