from pydantic import BaseModel

# Google shemas
class GoogleBaseModel(BaseModel):
    name: str
    surname: str
    email: str
    picture_uri: str

class GoogleOIDCModel(GoogleBaseModel):
    pass

class GoogleOAuthModel(GoogleBaseModel):
    # TODO:
    # make oauth
    pass

#-