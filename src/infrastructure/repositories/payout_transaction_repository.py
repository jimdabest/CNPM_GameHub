from domain.models.ipayout_transaction_repository import IPayoutTransactionRepository
from domain.models.payout_transaction import PayoutTransaction
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases import Base
from sqlalchemy.orm import Session
from infrastructure.models.payout_transactions_model import PayoutModel
from infrastructure.databases.mssql import session
load_dotenv()

class PayoutTransactionRepository(IPayoutTransactionRepository):
    def __init__(self, session: Session = session):
        self._payout_transactions = []
        self._id_counter = 1
        self.session = session

    def add(self, payout_transaction: PayoutTransaction) -> PayoutModel:
        try:
            # Manual mapping from PayoutTransaction to PayoutModel
            payout_model = PayoutModel(
                recipient_id=payout_transaction.recipient_id,
                recipient_type=payout_transaction.recipient_type,
                amount=payout_transaction.amount,
                transaction_date=payout_transaction.transaction_date,
                status=payout_transaction.status,
                processed_by_admin_id=payout_transaction.processed_by_admin_id
            )
            self.session.add(payout_model)
            self.session.commit()
            self.session.refresh(payout_model)
            return payout_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Payout transaction not found')
        finally:
            self.session.close()

    def get_by_id(self, transaction_id: int) -> Optional[PayoutModel]:
        return self.session.query(PayoutModel).filter_by(transactions_id=transaction_id).first()

    def list(self) -> List[PayoutModel]:
        self._payout_transactions = session.query(PayoutModel).all()
        # select * from payout_transactions
        return self._payout_transactions

    def update(self, payout_transaction: PayoutTransaction) -> PayoutModel:
        try:
            # Manual mapping from PayoutTransaction to PayoutModel
            payout_model = PayoutModel(
                transactions_id=payout_transaction.transactions_id,
                recipient_id=payout_transaction.recipient_id,
                recipient_type=payout_transaction.recipient_type,
                amount=payout_transaction.amount,
                transaction_date=payout_transaction.transaction_date,
                status=payout_transaction.status,
                processed_by_admin_id=payout_transaction.processed_by_admin_id
            )
            self.session.merge(payout_model)
            self.session.commit()
            return payout_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Payout transaction not found')
        finally:
            self.session.close()

    def delete(self, transaction_id: int) -> None:
        try:
            payout_transaction = self.session.query(PayoutModel).filter_by(transactions_id=transaction_id).first()
            if payout_transaction:
                self.session.delete(payout_transaction)
                self.session.commit()
            else:
                raise ValueError('Payout transaction not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Payout transaction not found')
        finally:
            self.session.close()