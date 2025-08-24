from abc import ABC, abstractmethod
from .payout_transaction import PayoutTransaction
from typing import List, Optional

class IPayoutTransactionRepository(ABC):
    @abstractmethod
    def add(self, payout_transaction: PayoutTransaction) -> PayoutTransaction:
        pass

    @abstractmethod
    def get_by_id(self, transaction_id: int) -> Optional[PayoutTransaction]:
        pass

    @abstractmethod
    def list(self) -> List[PayoutTransaction]:
        pass

    @abstractmethod
    def update(self, payout_transaction: PayoutTransaction) -> PayoutTransaction:
        pass

    @abstractmethod
    def delete(self, transaction_id: int) -> None:
        pass