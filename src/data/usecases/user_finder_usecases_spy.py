from typing import List
from src.domain.contracts.user_finder_contract import UserFinderContract
from src.domain.models.user_model import UserModel


class UserFinderUseCaseSPY(UserFinderContract):
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, user_id: int) -> List[UserModel]:
        self.find_attributes["user_id"] = user_id
        response = [
            UserModel(
                1,
                "Jhon",
                "(99)999999999",
                "044.044.044-44",
                "nUqQ7@example.com",
                "123456",
            ),
            UserModel(
                2,
                "Jhon2",
                "(99)444444444",
                "333.044.044-44",
                "nUqQ33@example.com",
                "1234",
            ),
        ]

        return {"type": "Users", "count": 2, "attributes": response}
