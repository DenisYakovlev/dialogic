

from typing import Any, Dict, Optional
from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    status_code: int = 400
    detail: Any = []

    def __init__(self, status_code: Optional[int] = None, detail: Any = None, headers: Dict[str, str] | None = None) -> None:
        if status_code is None:
            status_code = self.status_code
        
        if detail is None:
            detail = self.detail

        super().__init__(status_code, detail, headers)


class DBSessionInitError(Exception):
    detail = "DatabaseSessionManager is not initialized"

    def __init__(self, message=detail) -> None:
        super().__init__(message)
