from src.domain.contracts import UserRegisterContract
from src.presentation.http_type.http_request_types import HttpRequest
from src.presentation.http_type.http_response_types import HttpResponse


class UserRegisterController:
    def __init__(self, user_register_use_case: UserRegisterContract) -> None:
        self.user_register_use_case = user_register_use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        name = request.body["name"]
        phone = request.body["phone"]
        cpf = request.body["cpf"]
        email = request.body["email"]
        password = request.body["password"]

        response = self.user_register_use_case.register(
            name, phone, cpf, email, password
        )

        return HttpResponse(status_code=200, body={"data": response})
