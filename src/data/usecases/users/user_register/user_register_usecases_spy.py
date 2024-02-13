from typing import Dict
from src.domain.contracts.user_register_contracts import UserRegisterContract


class UserRegisterUseCaseSpy(UserRegisterContract):
    def __init__(self) -> None:
        self.register_attributes = {}

    def register(
        self, name: str, phone: str, cpf: str, email: str, password: str
    ) -> Dict:
        self.register_attributes["name"] = name
        self.register_attributes["phone"] = phone
        self.register_attributes["cpf"] = cpf
        self.register_attributes["email"] = email
        self.register_attributes["password"] = password

        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "name": name,
                "phone": phone,
                "cpf": cpf,
                "email": email,
                "password": password,
            },
        }

        return response
