from flask import Request as FlaskRequest
from src.presentation.contracts.controller_contract import ControllerContract
from src.presentation.http_type.http_request_types import HttpRequest
from src.presentation.http_type.http_response_types import HttpResponse


def request_http_adapter(
    request: FlaskRequest, controller: ControllerContract
) -> HttpResponse:
    body = None
    if request.data:
        body = request.json

    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path,
    )

    http_response = controller.handle(http_request)

    return http_response
