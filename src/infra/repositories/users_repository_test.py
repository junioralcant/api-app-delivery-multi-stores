
from src.infra.repositories.users_repository import UsersRepository

def test_insert_user():
    mocked_name = "João"
    mocked_phone = "11999999999"
    mocked_cpf = "11111111111"
    mocked_email = "a@a.com"
    mocked_password = "123456"

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_name, mocked_phone, mocked_cpf, mocked_email, mocked_password)
