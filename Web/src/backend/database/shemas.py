from typing import Optional
from pydantic import BaseModel


# Google shemas
class BaseUserModel(BaseModel):
    name: str
    surname: str
    email: str
    picture_uri: str
    service: Optional[str] = None


class GoogleOIDCModel(BaseUserModel):
    service: str = "google"


class GoogleOAuthModel(BaseUserModel):
    # TODO:
    # make oauth
    pass
