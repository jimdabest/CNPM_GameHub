from domain.models.iadmin_repository import IAdminRepository
from domain.models.admin import Admin
from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.admin_model import AdminModel
from infrastructure.databases.mssql import session


class AdminRepository(IAdminRepository):
    def __init__(self, session: Session = session):
        self._admins = []
        self._id_counter = 1
        self.session = session

    def add(self, admin: Admin) -> AdminModel:
        try:
            admin = AdminModel(
                user_id=getattr(admin, "user_id", None)
            )
            self.session.add(admin)
            self.session.commit()
            self.session.refresh(admin)
            return admin
        except Exception:
            self.session.rollback()
            raise ValueError("Admin insert failed")
        finally:
            self.session.close()

    def get_by_id(self, admin_id: int) -> Optional[AdminModel]:
        return self.session.query(AdminModel).filter_by(id=admin_id).first()

    def list(self) -> List[AdminModel]:
        self._admins = session.query(AdminModel).all()
        return self._admins

    def update(self, admin: AdminModel) -> AdminModel:
        try:
            admin = AdminModel(
                id=getattr(admin, "id", None),
                user_id=getattr(admin, "user_id", None),
            )
            self.session.merge(admin)
            self.session.commit()
            return admin
        except Exception:
            self.session.rollback()
            raise ValueError("Admin update failed")
        finally:
            self.session.close()

    def delete(self, admin_id: int) -> None:
        try:
            admin = self.session.query(AdminModel).filter_by(id=admin_id).first()
            if admin:
                self.session.delete(admin)
                self.session.commit()
            else:
                raise ValueError("Admin not found")
        except Exception:
            self.session.rollback()
            raise ValueError("Admin delete failed")
        finally:
            self.session.close()
