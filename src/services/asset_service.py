from typing import List, Optional
from domain.models.asset import Asset
from domain.models.iasset_repository import IAssetRepository

class AssetService:
    def __init__(self, asset_repository: IAssetRepository):
        self.asset_repository = asset_repository
    def create_asset(self, designer_id: int, name: str, type: str, price: float, download_count: int, created_at, updated_at) -> Asset: return self.add_asset(designer_id, name, type, price, download_count, created_at, updated_at)

    def add_asset(self, designer_id: int, name: str, type: str, price: float, download_count: int, created_at, updated_at) -> Asset:
        asset = Asset(id=None, designer_id=designer_id, name=name, type=type, price=price, download_count=download_count, created_at=created_at, updated_at=updated_at)
        return self.asset_repository.add(asset)
    def get_asset_by_id(self, asset_id: int) -> Optional[Asset]:
        return self.asset_repository.get_by_id(asset_id)
    def list_assets(self) -> List[Asset]:
        return self.asset_repository.list()
    def update_asset(self, asset_id: int, designer_id: int, name: str, type: str, price: float, download_count: int, created_at, updated_at) -> Asset:
        asset = Asset(id=asset_id, designer_id=designer_id, name=name, type=type, price=price, download_count=download_count, created_at=created_at, updated_at=updated_at)
        return self.asset_repository.update(asset)
    def delete_asset(self, asset_id: int) -> None:
        self.asset_repository.delete(asset_id)

