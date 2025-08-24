from typing import List, Optional
from domain.models.user import User
from domain.models.iuser_repository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
    
    def add_user(self, username: str, password: str, role: str, status: str, created_at, updated_at) -> User:
        user = User(id=None, username=username, password=password, role=role, status=status, created_at=created_at, updated_at=updated_at)
        return self.user_repository.add(user)
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_id(user_id)
    
    def list_users(self) -> List[User]:
        return self.user_repository.list()
    
    def update_user(self, user_id: int, username: str, password: str, role: str, status: str, created_at, updated_at) -> User:
        return self.user_repository.update(user_id, username, password, role, status, updated_at)
    
    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete(user_id)
    
    def update_user_role(self, user_id: int, role: str) -> None:
        """Cập nhật role của user"""
        user = self.user_repository.get_by_id(user_id)
        if user:
            # Cập nhật user với role mới, giữ nguyên các field khác
            from datetime import datetime
            self.user_repository.update(
                user_id=user_id,
                username=user.username,
                password=user.password,
                role=role,  # Role mới
                status=user.status,
                updated_at=datetime.utcnow()
            )
        else:
            raise ValueError(f'User with id {user_id} not found')