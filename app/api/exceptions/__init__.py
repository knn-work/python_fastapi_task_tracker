from fastapi import FastAPI

from app.api.exceptions.base import AppError
from app.api.exceptions.handlers import http_base_exception_handler
from app.api.exceptions.project_errors import ProjectNotFoundError
from app.api.exceptions.project_manegment_errors import (
    ProjectConnectionNotFoundError,
    ProjectConnectionAlreadyExist,
)
from app.api.exceptions.user_errors import UserAlreadyExistsError, UserNotFoundError

exceptions_and_handlers = {
    UserAlreadyExistsError: http_base_exception_handler,
    ProjectNotFoundError: http_base_exception_handler,
    UserNotFoundError: http_base_exception_handler,
    ProjectConnectionNotFoundError: http_base_exception_handler,
    ProjectConnectionAlreadyExist: http_base_exception_handler,
}


# Функция для добавления миддлваров в приложение
def setup_handlers(app: FastAPI):
    for exception in exceptions_and_handlers:
        app.add_exception_handler(exception, exceptions_and_handlers[exception])
