from abc import ABC, abstractmethod
from .apiaccess import Apiaccess
from typing import List, Optional

class IUserRepository(ABC):
    @abstractmethod
    def add(self, user: Apiaccess) -> Apiaccess:
        pass

    @abstractmethod
    def get_by_id(self, apiaccess_id: int) -> Optional[Apiaccess]:
        pass

    @abstractmethod
    def list(self) -> List[Apiaccess]:
        pass

    @abstractmethod
    def update(self, apiaccess: Apiaccess) -> Apiaccess:
        pass

    @abstractmethod
    def delete(self, apiaccess_id: int) -> None:
        pass 