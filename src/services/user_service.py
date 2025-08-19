from typing import List, Optional
from domain.models.user import User
from domain.models.iuser_repository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
    
    def add_user(self, user: User) -> User:
        return self.user_repository.add(user)
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_id(user_id)
    
    def list_users(self) -> List[User]:
        return self.user_repository.list()
    
    def update_user(self, user: User) -> User:
        return self.user_repository.update(user)
    
    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete(user_id)
        