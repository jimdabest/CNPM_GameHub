from typing import List, Optional
from domain.models.designer import Designer
from domain.models.idesigner_repository import IDesignerRepository


class DesignerService:
    def __init__(self, designer_repository: IDesignerRepository):
        self.designer_repository = designer_repository
    
    def add_designer(self, user_id: int, paymentinfo: Optional[str]) -> Designer:
        designer = Designer(id=None, user_id=user_id, paymentinfo=paymentinfo)
        return self.designer_repository.add(designer)
    
    def get_designer_by_id(self, designer_id: int) -> Optional[Designer]:
        return self.designer_repository.get_by_id(designer_id)
    
    def list_designers(self) -> List[Designer]:
        return self.designer_repository.list()
    
    def update_designer(self, designer_id: int, user_id: int, paymentinfo: Optional[str]) -> Designer:
        designer = Designer(id=designer_id, user_id=user_id, paymentinfo=paymentinfo)
        return self.designer_repository.update(designer)
    
    def delete_designer(self, designer_id: int) -> None:
        self.designer_repository.delete(designer_id)
