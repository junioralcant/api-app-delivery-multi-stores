from src.data.usecases.user_finder_usecases import UserFinderUseCase
from src.infra.repositories.users_repository import UsersRepository
from src.presentation.controller.user_register_controller import UserRegisterController

def user_register_controller_factory() -> UserRegisterController:
    userRepository = UsersRepository
    user_use_case = UserFinderUseCase(userRepository)
    return UserRegisterController(user_use_case) 
