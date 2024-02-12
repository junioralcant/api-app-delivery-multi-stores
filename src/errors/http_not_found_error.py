class HttpNotFoundError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.name = "BadRequest"
        self.status_code = 404
