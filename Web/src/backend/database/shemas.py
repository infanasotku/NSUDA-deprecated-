from typing import Optional
from pydantic import BaseModel


# Google shemas
class BaseUserModel(BaseModel):
    name: str
    surname: str
    email: str
    picture_uri: str
    service: Optional[str]


class GoogleOIDCModel(BaseUserModel):
    pass


class GoogleOAuthModel(BaseUserModel):
    # TODO:
    # make oauth
    pass
