from domain.models.iuser_repository import IUserRepository
from domain.models.user import User
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases import Base
from sqlalchemy.orm import Session
from infrastructure.models.user_model import UserModel
from infrastructure.databases.mssql import session
load_dotenv()

class UserRepository(IUserRepository):
    def __init__(self, session: Session = session):
        self._users = []
        self._id_counter = 1
        self.session = session

    def add(self, user: User) -> UserModel:
        try:
            # Manual mapping from User (domain) to UserModel (infra)
            user_model = UserModel(
                username=user.username,
                password=user.password,
                role=user.role,
                status=user.status,
                created_at=user.created_at,
                updated_at=user.updated_at
            )
            self.session.add(user_model)
            self.session.commit()
            self.session.refresh(user_model)
            return user_model
        except Exception as e:
            self.session.rollback()
            raise ValueError(f'Error adding user: {str(e)}')
        finally:
            self.session.close()

    def get_by_id(self, user_id: int) -> Optional[UserModel]:
        try:
            return self.session.query(UserModel).filter_by(id=user_id).first()
        except Exception as e:
            raise ValueError(f'Error getting user by id: {str(e)}')

    def list(self) -> List[UserModel]:
        try:
            self._users = self.session.query(UserModel).all()
            # select * from user
            return self._users
        except Exception as e:
            raise ValueError(f'Error listing users: {str(e)}')

    def update(self, user_id: int, username: str, password: str, role: str, status: str, updated_at) -> UserModel:
        try:
            # Find existing user
            existing_user = self.session.query(UserModel).filter_by(id=user_id).first()
            if not existing_user:
                raise ValueError('User not found')
            
            # Update fields
            existing_user.username = username
            existing_user.password = password
            existing_user.role = role
            existing_user.status = status
            existing_user.updated_at = updated_at
            
            self.session.commit()
            self.session.refresh(existing_user)
            return existing_user
        except Exception as e:
            self.session.rollback()
            raise ValueError(f'Error updating user: {str(e)}')
        finally:
            self.session.close()

    def delete(self, user_id: int) -> None:
        try:
            user = self.session.query(UserModel).filter_by(id=user_id).first()
            if user:
                self.session.delete(user)
                self.session.commit()
            else:
                raise ValueError('User not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError(f'Error deleting user: {str(e)}')
        finally:
            self.session.close()