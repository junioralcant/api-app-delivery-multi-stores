from src.data.usecases.users import UserRegisterUseCase
from src.infra.repositories.users_repository import UsersRepository
from src.presentation.controller.user_register_controller import UserRegisterController


def user_register_controller_factory() -> UserRegisterController:
    userRepository = UsersRepository
    user_use_case = UserRegisterUseCase(userRepository)
    return UserRegisterController(user_use_case)
