from typing import List, Optional
from domain.models.developer import Developer
from domain.models.ideveloper_repository import IDeveloperRepository

class DeveloperService:
    def __init__(self, developer_repository: IDeveloperRepository):
        self.developer_repository = developer_repository
    
    def add_developer(self, user_id: int, payment_info: str, created_at, updated_at) -> Developer:
        developer = Developer(
            id=None,
            user_id=user_id,
            payment_info=payment_info,
            created_at=created_at,
            updated_at=updated_at
        )
        return self.developer_repository.add(developer)
    
    def get_developer_by_id(self, developer_id: int) -> Optional[Developer]:
        return self.developer_repository.get_by_id(developer_id)
    
    def list_developers(self) -> List[Developer]:
        return self.developer_repository.list()
    
    def update_developer(self, developer_id: int, user_id: int, payment_info: str, created_at, updated_at) -> Developer:
        developer = Developer(
            id=developer_id,
            user_id=user_id,
            payment_info=payment_info,
            created_at=created_at,
            updated_at=updated_at
        )
        return self.developer_repository.update(developer)
    
    def delete_developer(self, developer_id: int) -> None:
        self.developer_repository.delete(developer_id)
