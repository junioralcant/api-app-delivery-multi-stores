from typing import Dict
from src.domain.contracts.user_register_contracts import UserRegisterContract
from src.infra.contracts.user_repository_contract import UsersRepositoryContract

class UserRegisterUseCase(UserRegisterContract):
    def __init__(self, user_repository: UsersRepositoryContract) -> None:
        self.__user_repository = user_repository

    def register(self, name: str, phone: str, cpf: str, email: str, password: str) -> Dict: 
        self.__validate_name(name)
        return self.__register_user_information(name, phone, cpf, email, password)
    
    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha(): 
            raise ValueError("Name must be only letters")

    def __register_user_information(self, name: str, phone: str, cpf: str, email: str, password: str) -> None:
        self.__user_repository.insert_user(name, phone, cpf, email, password)
        return self.__format_response(name, phone, cpf, email)
    
    @classmethod
    def __format_response(cls, name: str, phone: str, cpf: str, email: str) -> Dict:
        response = {
            "type": "User",
            "count": 1,
            "attributes": {
                "name": name,
                "phone": phone,
                "cpf": cpf,
                "email": email
            }
        }

        return response
