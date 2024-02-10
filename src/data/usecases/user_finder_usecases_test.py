
from src.infra.repositories.users_repository_spy import UsersRepositorySpy
from .user_finder_usecases import UserFinderUseCase

def test_find(): 
    user_id = 2
    repo = UsersRepositorySpy()
    user_finder = UserFinderUseCase(repo)

    response = user_finder.find(user_id)
    print(response)

    assert repo.select_user_attributes["user_id"] == user_id

    assert response["type"] == "Users"
    assert response["count"] == 2
    assert response["attributes"] != []
