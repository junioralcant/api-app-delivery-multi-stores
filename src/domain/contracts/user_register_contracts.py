
from abc import ABC, abstractmethod
from ast import Dict

class UserRegisterContract(ABC):
    @abstractmethod
    def register(self, name: str, phone: str, cpf: str, email: str, password: str) -> Dict: pass
