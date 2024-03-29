from src.domain.contracts import UserFinderContract
from src.presentation.contracts import ControllerContract
from src.presentation.http_type.http_request_types import HttpRequest
from src.presentation.http_type.http_response_types import HttpResponse


class UserFinderController(ControllerContract):
    def __init__(self, user_use_case: UserFinderContract) -> None:
        self.user_use_case = user_use_case

    def handle(self, request: HttpRequest) -> HttpResponse:
        user_id = request.query_params["user_id"]
        response = self.user_use_case.find(int(user_id))
        return HttpResponse(status_code=200, body={"data": response})
