from src.infra.repositories.users_repository_spy import UsersRepositorySpy
from .user_finder_usecases import UserFinderUseCase


def test_find():
    user_id = 2
    repo = UsersRepositorySpy()
    user_finder = UserFinderUseCase(repo)

    response = user_finder.find(user_id)

    assert repo.select_user_attributes["user_id"] == user_id

    assert response["type"] == "Users"
    assert response["count"] == 2
    assert response["attributes"]


def test_return_error_if_list_is_empty():
    repo = UsersRepositorySpy()
    user_finder = UserFinderUseCase(repo)
    repo.select_user_response = []

    try:
        user_finder.find(1)
        assert False
    except Exception as error:
        assert str(error) == "User not found!"
