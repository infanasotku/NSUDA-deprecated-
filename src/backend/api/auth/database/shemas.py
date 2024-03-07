from typing import Any, Optional
from pydantic import BaseModel

# Google shemas
class BaseUserModel(BaseModel):
    name: str
    surname: str
    email: str
    picture_uri: str
    service:  Optional[str] = None

class GoogleOIDCModel(BaseUserModel):
    def model_post_init(self, _: Any) -> None:
        self.service = 'google'


class GoogleOAuthModel(BaseUserModel):
    # TODO:
    # make oauth
    pass

#-