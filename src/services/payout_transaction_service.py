from domain.models.payout_transaction import PayoutTransaction
from domain.models.ipayout_transaction_repository import IPayoutTransactionRepository
from typing import List, Optional

class PayoutTransactionService:
    def __init__(self, repository: IPayoutTransactionRepository):
        self.repository = repository

    def create_payout_transaction(self, recipient_id: int, recipient_type: str, amount: float, transaction_date, status: str, processed_by_admin_id: int) -> PayoutTransaction:
        payout_transaction = PayoutTransaction(
            transactions_id=None, 
            recipient_id=recipient_id, 
            recipient_type=recipient_type, 
            amount=amount, 
            transaction_date=transaction_date, 
            status=status, 
            processed_by_admin_id=processed_by_admin_id
        )
        return self.repository.add(payout_transaction)

    def get_payout_transaction(self, transaction_id: int) -> Optional[PayoutTransaction]:
        return self.repository.get_by_id(transaction_id)

    def list_payout_transactions(self) -> List[PayoutTransaction]:
        return self.repository.list()

    def update_payout_transaction(self, transaction_id: int, recipient_id: int, recipient_type: str, amount: float, transaction_date, status: str, processed_by_admin_id: int) -> PayoutTransaction:
        payout_transaction = PayoutTransaction(
            transactions_id=transaction_id, 
            recipient_id=recipient_id, 
            recipient_type=recipient_type, 
            amount=amount, 
            transaction_date=transaction_date, 
            status=status, 
            processed_by_admin_id=processed_by_admin_id
        )
        return self.repository.update(payout_transaction)

    def delete_payout_transaction(self, transaction_id: int) -> None:
        self.repository.delete(transaction_id)