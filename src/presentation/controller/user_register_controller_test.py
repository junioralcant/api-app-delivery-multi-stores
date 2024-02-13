from src.data.usecases.users import UserRegisterUseCaseSpy
from .user_register_controller import UserRegisterController


class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            "name": "any_name",
            "phone": "any_phone",
            "cpf": "any_cpf",
            "email": "any_email",
            "password": "any_password",
        }


def make_sut():
    user_register_use_case = UserRegisterUseCaseSpy()
    user_register_controller = UserRegisterController(user_register_use_case)
    http_request = HttpRequestMock()

    sut = user_register_controller.handle(http_request)

    return {
        "user_register_use_case": user_register_use_case,
        "user_register_controller": user_register_controller,
        "http_request": http_request,
        "sut": sut,
    }


def test_should_call_params_with_correct_values():
    user_register_use_case = make_sut()["user_register_use_case"]

    assert user_register_use_case.register_attributes["name"] == "any_name"
    assert user_register_use_case.register_attributes["phone"] == "any_phone"
    assert user_register_use_case.register_attributes["cpf"] == "any_cpf"
    assert user_register_use_case.register_attributes["email"] == "any_email"
    assert user_register_use_case.register_attributes["password"] == "any_password"


def test_should_return_handle_method_with_correct_response():
    sut = make_sut()["sut"]
    http_request = make_sut()["http_request"]

    assert sut.status_code == 200

    assert sut.body["data"]["type"] == "Users"
    assert sut.body["data"]["count"] == 1
    assert sut.body["data"]["attributes"]["name"] == http_request.body["name"]
    assert sut.body["data"]["attributes"]["phone"] == http_request.body["phone"]
    assert sut.body["data"]["attributes"]["cpf"] == http_request.body["cpf"]
    assert sut.body["data"]["attributes"]["email"] == http_request.body["email"]
    assert sut.body["data"]["attributes"]["password"] == http_request.body["password"]
