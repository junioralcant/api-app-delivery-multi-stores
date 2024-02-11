
from src.infra.repositories.users_repository_spy import UsersRepositorySpy
from .user_register_usecases import UserRegisterUseCase

MOCKED_NAME = "Junior"
MOCKED_PHONE = "119999"
MOCKED_CPF = "11111111"
MOCKED_EMAIL = "e@a.com"
MOCKED_PASSWORD = "1234"

def test_should_call_register_with_correct_params(): 
    users_repository = UsersRepositorySpy()

    user_register_usecases = UserRegisterUseCase(users_repository)

    user_register_params = users_repository.insert_user_attributes

    user_register_usecases.register(MOCKED_NAME, MOCKED_PHONE, MOCKED_CPF, MOCKED_EMAIL, MOCKED_PASSWORD)

    assert user_register_params["name"] == MOCKED_NAME
    assert user_register_params["phone"] == MOCKED_PHONE
    assert user_register_params["cpf"] == MOCKED_CPF
    assert user_register_params["email"] == MOCKED_EMAIL
    assert user_register_params["password"] == MOCKED_PASSWORD

def test_register(): 

    users_repository = UsersRepositorySpy()

    user_register_usecases = UserRegisterUseCase(users_repository)

    response = user_register_usecases.register(MOCKED_NAME, MOCKED_PHONE, MOCKED_CPF, MOCKED_EMAIL, MOCKED_PASSWORD)

    assert response == {
        "type": "Users",
        "count": 1,
        "attributes": {
            "name": MOCKED_NAME,
            "phone": MOCKED_PHONE,
            "cpf": MOCKED_CPF,
            "email": MOCKED_EMAIL
        }
    }

def test_should_trow_error_if_name_is_alphabetic():
    users_repository = UsersRepositorySpy()

    user_register_usecases = UserRegisterUseCase(users_repository)

    try:
        user_register_usecases.register("Junior 99484", MOCKED_PHONE, MOCKED_CPF, MOCKED_EMAIL, MOCKED_PASSWORD)
        assert False
    except Exception as error:
        assert str(error) == "Name must be only letters"
