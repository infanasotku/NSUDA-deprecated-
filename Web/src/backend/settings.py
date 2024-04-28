from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache
import logging
import sys


class Settings(BaseSettings):
    # main
    host: str = Field(validation_alias="HOST", default="127.0.0.1")
    port: int = Field(validation_alias="PORT", default=5000)

    # security
    session_secret: str = Field(validation_alias="SESSION_SECRET")
    cors_origins: list[str] = [
        'http://localhost:5001',
        'https://infanasotku.com',
        'https://infanasotku.ru',
        'https://www.infanasotku.ru',
        'https://www.infanasotku.com'
    ]
    cors_allow_methods: list[str] = [
        'GET',
        'POST',
        'PATCH',
        'PUT',
        'DELETE'
    ]
    cors_allow_headers: list[str] = [
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Authorization'
    ]
    # google data
    google_client_id: str = Field(validation_alias="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field(validation_alias="GOOGLE_CLIENT_SECRET")
    google_scope: str = Field(validation_alias="GOOGLE_SCOPE")
    google_endpoints_info_uri: str = Field(
        validation_alias="GOOGLE_ENDPOINTS_INFO_URI"
    )
    google_auth_grant_type: str = Field(
        validation_alias="GOOGLE_AUTH_GRANT_TYPE"
    )
    google_refresh_token_grant_type: str = Field(
        validation_alias="GOOGLE_REFRESH_TOKEN_GRANT_TYPE"
    )
    google_redirect_uri: str = Field(validation_alias="GOOGLE_REDIRECT_URI")


@lru_cache
def get_settings() -> Settings:
    '''Returns settings of app.

    Settings will be generate only for first call.
    '''
    try:
        settings = Settings()
        return settings
    except Exception as e:
        logging.critical(f"Settings generated with error: {e}")
        sys.exit()
