from typing import Callable
from api.auth.database.shemas import BaseUserModel
from fastapi import Request

auth_services: dict[Callable[[Request], BaseUserModel]] = {}