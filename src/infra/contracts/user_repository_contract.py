from abc import ABC, abstractmethod
from typing import List

from src.domain.models.user_model import UserModel

class UsersRepositoryContract(ABC): 
    @abstractmethod
    def insert_user(self, name: str, phone: str, cpf: str, email: str, password: str) -> None: pass
            
    @abstractmethod
    def select_user(self, user_id: int) -> List[UserModel]: pass
