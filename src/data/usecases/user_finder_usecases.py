from typing import Dict
from src.domain.contracts.user_finder_contract import UserFinderContract
from src.infra.contracts.user_repository_contract import UsersRepositoryContract

class UserFinderUseCase(UserFinderContract):
    def __init__(self, user_repository: UsersRepositoryContract) -> None:
        self.__user_repository = user_repository
    
    def find(self, user_id: int) -> Dict:
        users = self.__user_repository.select_user(user_id)
        if users == []:
            raise Exception("User not found!")
        
        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }

        return response
