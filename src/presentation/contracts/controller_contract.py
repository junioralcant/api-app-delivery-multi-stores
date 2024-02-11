from abc import ABC, abstractmethod
from src.presentation.http_type.http_request_types import HttpRequest
from src.presentation.http_type.http_response_types import HttpResponse

class ControllerContract(ABC):
    @abstractmethod
    def handle(self, request: HttpRequest) -> HttpResponse: pass
