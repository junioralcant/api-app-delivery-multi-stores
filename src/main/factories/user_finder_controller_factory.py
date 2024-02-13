from src.data.usecases.users import UserFinderUseCase
from src.infra.repositories.users_repository import UsersRepository
from src.presentation.controller import UserFinderController


def user_finder_controller_factory() -> UserFinderController:
    user_repository = UsersRepository
    user_use_case = UserFinderUseCase(user_repository)
    return UserFinderController(user_use_case)
