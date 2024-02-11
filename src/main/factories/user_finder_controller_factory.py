from src.data.usecases.user_finder_usecases import UserFinderUseCase
from src.infra.repositories.users_repository import UsersRepository
from src.presentation.controller.user_finder_controller import UserFinderController

def user_finder_controller_factory() -> UserFinderController:
    userRepository = UsersRepository
    user_use_case = UserFinderUseCase(userRepository)
    return UserFinderController(user_use_case) 
