# pylint: disable=line-too-long

class Aria2Error(Exception):
    """Base exception for all exceptions raised by this library."""

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(self.__str__())

    def __str__(self) -> str:
        return f"{self.message} ({self.code})"


class ClientSentInvalidRequestError(Aria2Error):
    """Raised when the client sends an invalid request with malformed data to the server."""

    def __init__(self) -> None:
        super().__init__(-32600, "Invalid Request")


class UnauthorizedClientError(Aria2Error):
    """Raised when the client is unauthorized/passed incorrect secret."""

    def __init__(self) -> None:
        super().__init__(1, "Unauthorized")
