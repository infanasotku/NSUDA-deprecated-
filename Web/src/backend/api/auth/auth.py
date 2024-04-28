from fastapi import HTTPException, Request
import aiohttp
from database.shemas import BaseUserModel, GoogleOIDCModel
from jose.utils import base64url_decode
from settings import get_settings
import json


class Auth():
    def __init__(self, request: Request) -> None:
        self.request = request

    async def __call__(self) -> BaseUserModel:
        return await self.auth(self.request)

    async def auth(self, request: Request) -> BaseUserModel:
        """
        Provides auth by service.

        Returns: `BaseUserModel` with specified info, if user authed,
        throw `HTTPException(status_code=401)` otherwise.
        """
        raise NotImplementedError()


class GoogleAuth(Auth):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.auth_code = None

    async def auth(
        self
    ) -> BaseUserModel:
        auth_code = self.auth_code

        if not auth_code:
            data = await self._update_token(
                self.request.session['refresh_token']
            )
        else:
            # When we collect google token we can collect also user data.
            data = await self._get_token(auth_code)
            self.request.session['refresh_token'] = data['refresh_token']

            token: str = data['id_token']
            encoded_sig = token.split('.', 2)[1].encode()
            decoded_sig = base64url_decode(encoded_sig)
            user_data = json.loads(decoded_sig.decode("utf-8"))

            self.request.session['name'] = user_data['given_name']
            self.request.session['username'] = user_data['family_name']
            self.request.session['email'] = user_data['email']
            self.request.session['picture_uri'] = user_data['picture']

        self.request.session['access_token'] = data['access_token']
        self.request.session['auth_service'] = 'google'

        if 'name' not in self.request.session:
            raise HTTPException(status_code=401)

        model = GoogleOIDCModel(
            name=self.request.session['name'],
            surname=self.request.session['username'],
            email=self.request.session['email'],
            picture_uri=self.request.session['picture_uri']
        )

        return model

    async def _get_token(self, auth_code: str) -> tuple[str, str]:
        token_uri = await self._get_endpoint('token_endpoint')
        params = [
            ('code', auth_code),
            ('client_id', get_settings().google_client_id),
            ('client_secret', get_settings().google_client_secret),
            ('grant_type', get_settings().google_auth_grant_type),
            ('redirect_uri', get_settings().google_redirect_uri),
        ]
        async with aiohttp.ClientSession() as session:
            async with session.post(token_uri, params=params) as resp:
                data = await resp.json()
                if resp.status >= 400:
                    raise HTTPException(status_code=resp.status)
                return data

    async def _update_token(self, refresh_token: str) -> tuple[str, str]:
        token_uri = await self._get_endpoint('token_endpoint')

        params = [
            ('client_id', get_settings().google_client_id),
            ('client_secret', get_settings().google_client_secret),
            ('grant_type', get_settings().google_refresh_token_grant_type),
            ('refresh_token', refresh_token),
        ]
        async with aiohttp.ClientSession() as session:
            async with session.post(token_uri, params=params) as resp:
                data = await resp.json()
                if resp.status >= 400:
                    raise HTTPException(status_code=resp.status)
                return data

    async def _get_endpoint(self, field: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                get_settings().google_endpoints_info_uri
            ) as resp:
                if resp.status >= 400:
                    raise HTTPException(status_code=resp.status)
                return (await resp.json())[field]


class AuthFactory():
    @staticmethod
    async def build(request: Request) -> Auth:
        '''
        Builds auth by user authed type in `request`.

        Returns: auth handler.
        '''
        if 'auth_service' not in request.session:
            raise HTTPException(status_code=401)

        service_name = request.session['auth_service']

        match service_name:
            case 'google':
                handler = GoogleAuth(request)
                return await handler.auth()
            case _:
                raise HTTPException(
                    status_code=401,
                    detail="Not allowed auth service."
                )
