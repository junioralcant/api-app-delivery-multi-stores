from typing import List
from src.domain.contracts.user_finder_contract import UserFinderContract
from src.domain.models.user_model import UserModel
from src.infra.contracts.user_repository_contract import UsersRepositoryContract

class UserFinderUseCase(UserFinderContract):
    def __init__(self, user_repository: UsersRepositoryContract) -> None:
        self.__user_repository = user_repository
    
    def find(self, user_id: int) -> List[UserModel]:
        users = self.__user_repository.select_user(user_id)
        if users == []:
            raise Exception("User not found!")
        
        return self.__format_response(users)
    
    @classmethod
    def __format_response(cls, users: List[UserModel]) -> List[UserModel]:
        attributes = []
        for user in users:
            attributes.append({
                "name": user.name,
                "phone": user.phone,
                "cpf": user.cpf,
                "email": user.email
            })

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }

        return response
