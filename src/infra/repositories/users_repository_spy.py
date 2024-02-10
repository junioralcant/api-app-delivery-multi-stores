from typing import List
from src.domain.models.user_model import UserModel
from src.infra.contracts.user_repository_contract import UsersRepositoryContract

class UsersRepositorySpy (UsersRepositoryContract): 
    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}
        self.select_user_response = [
            UserModel(1, "Jhon", "(99)999999999", "044.044.044-44", "nUqQ7@example.com", "123456"),
            UserModel(2, "Jhon2", "(99)444444444", "333.044.044-44", "nUqQ33@example.com", "1234"),
        ]


    def insert_user(self, name: str, phone: str, cpf: str, email: str, password: str) -> None: 
        self.insert_user_attributes["name"] = name
        self.insert_user_attributes["phone"] = phone
        self.insert_user_attributes["cpf"] = cpf
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["password"] = password
            
    def select_user(self, user_id: int) -> List[UserModel]:
        self.select_user_attributes["user_id"] = user_id 

        return self.select_user_response
