from src.errors import HttpNotFoundError, HttpBadRequestError
from src.presentation.http_type.http_response_types import HttpResponse


def handle_erros(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError)):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Server error", "detail": str(error)}]},
    )
