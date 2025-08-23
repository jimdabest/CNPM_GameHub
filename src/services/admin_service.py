from typing import List, Optional
from domain.models.admin import Admin
from domain.models.iadmin_repository import IAdminRepository


class AdminService:
    def __init__(self, admin_repository: IAdminRepository):
        self.admin_repository = admin_repository

    def add_admin(self, username: str, password: str, role: str, status: str, created_at, updated_at) -> Admin:
        admin = Admin(id=None, username=username, password=password, role=role, status=status,
                      created_at=created_at, updated_at=updated_at)
        return self.admin_repository.add(admin)

    def get_admin_by_id(self, admin_id: int) -> Optional[Admin]:
        return self.admin_repository.get_by_id(admin_id)

    def list_admins(self) -> List[Admin]:
        return self.admin_repository.list()

    def update_admin(self, admin_id: int, username: str, password: str, role: str, status: str, created_at, updated_at) -> Admin:
        admin = Admin(id=admin_id, username=username, password=password, role=role, status=status,
                      created_at=created_at, updated_at=updated_at)
        return self.admin_repository.update(admin)

    def delete_admin(self, admin_id: int) -> None:
        self.admin_repository.delete(admin_id)
