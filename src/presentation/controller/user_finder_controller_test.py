
from src.data.usecases.user_finder_usecases_spy import UserFinderUseCaseSPY
from src.presentation.controller.user_finder_controller import UserFinderController
from src.presentation.http_type.http_response_types import HttpResponse

class HTTPRequestMock():
    def __init__(self) -> None:
        self.query_params = {"user_id": "2"}

def test_handle():
    user_finder_use_case = UserFinderUseCaseSPY()
    user_finder_controller = UserFinderController(user_finder_use_case)
    http_request = HTTPRequestMock()

    response = user_finder_controller.handle(http_request)

    assert user_finder_use_case.find_attributes["user_id"] == "2"

    assert response.status_code == 200
    assert response.body["data"] != []
    assert response.body["data"]["type"] == "Users"

    assert isinstance(response, HttpResponse)

    assert response.body["data"]["attributes"][0].name == "Jhon"
    assert response.body["data"]["attributes"][0].phone == "(99)999999999"
    assert response.body["data"]["attributes"][0].cpf == "044.044.044-44"
    assert response.body["data"]["attributes"][0].email == "nUqQ7@example.com"
    