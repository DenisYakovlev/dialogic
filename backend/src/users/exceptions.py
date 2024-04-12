from src.exceptions import BaseHTTPException

class PasswordsDoNotMatchError(ValueError):
    ...

class PasswordIsEmptyError(Exception):
    ...


class EmailIsTakenError(BaseHTTPException):
    status_code = 409
    detail = [{
        "msg": "User with given Email already exists"
    }]