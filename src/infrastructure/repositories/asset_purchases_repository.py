from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from infrastructure.models.asset_purchases_model import AssetPurchasesModel
from domain.models.asset_purchases import Asset_Purchase

class AssetPurchaseRepository:
    def __init__(self, session: Session = session):
        self.session = session

    def add(self, asset_purchase: Asset_Purchase) -> AssetPurchasesModel:
        try:
            ap = AssetPurchasesModel(
                dev_id=asset_purchase.dev_id,
                asset_id=asset_purchase.asset_id,
                purchase_date=asset_purchase.purchase_date,
                amount_paid=asset_purchase.amount_paid
            )
            self.session.add(ap)
            self.session.commit()
            self.session.refresh(ap)
            return ap
        except Exception as e:
            self.session.rollback()
            raise ValueError("AssetPurchase add failed") from e
        finally:
            self.session.close()

    def get_by_id(self, ap_id: int) -> Optional[AssetPurchasesModel]:
        return self.session.query(AssetPurchasesModel).filter_by(id=ap_id).first()

    def list(self) -> List[AssetPurchasesModel]:
        return self.session.query(AssetPurchasesModel).all()

    def update(self, asset_purchase: AssetPurchasesModel) -> AssetPurchasesModel:
        try:
            self.session.merge(asset_purchase)
            self.session.commit()
            return asset_purchase
        except Exception as e:
            self.session.rollback()
            raise ValueError("AssetPurchase update failed") from e
        finally:
            self.session.close()

    def delete(self, ap_id: int) -> None:
        try:
            ap = self.session.query(AssetPurchasesModel).filter_by(id=ap_id).first()
            if ap:
                self.session.delete(ap)
                self.session.commit()
            else:
                raise ValueError("AssetPurchase not found")
        except Exception as e:
            self.session.rollback()
            raise
        finally:
            self.session.close()
