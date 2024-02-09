
from abc import ABC, abstractmethod
from typing import Dict


class UserFinderContract(ABC):
    @abstractmethod
    def find(self, user_id: int) -> Dict: pass
