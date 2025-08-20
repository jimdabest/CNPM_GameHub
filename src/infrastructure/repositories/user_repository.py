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
        self.session = session

    def add(self, user: User) -> UserModel:
        try:
            #Manual mapping from User to UserModel
            user = UserModel(
                username = user.username,
                password = user.password,
                role = user.role,
                status = user.status,
                created_at = user.created_at,
                updated_at = user.created_at
            )
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            self.session.rollback()
            raise ValueError('User not found')
        finally:
            self.session.close()

    def get_by_id(self, user_id: int) -> Optional[UserModel]:
        return self.session.query(UserModel).filter_by(id=user_id).first()

    def list(self) -> List[User]:
        return self.session.query(UserModel).all()

    def update(self, user: UserModel) -> UserModel:
        try:
               # Manual map User -> UserModel
            user = UserModel(
                id=user.id,
                username=user.username,
                password=user.password,
                role=user.role,
                status=user.status,
                created_at=user.created_at,
                updated_at=user.updated_at
        )
            merged = self.session.merge(user)
            self.session.commit()
            self.session.refresh(merged)
            return user
        except Exception as e:
            self.session.rollback()
            raise ValueError('User not found')
        finally:
            self.session.close()

    def delete(self, user_id: int) -> None:
        user = self.get_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
        else:
            raise ValueError('User not found')