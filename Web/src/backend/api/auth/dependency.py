from fastapi import HTTPException, Request
import aiohttp

from api.env.google_env import *
from jose.utils import base64url_decode
import json


# General auth
from api.auth.settings import auth_services
from api.auth.database.shemas import BaseUserModel
async def auth(request: Request) -> BaseUserModel:
    if 'auth_service' in request.session:
        return await auth_services[request.session['auth_service']](request)
    raise HTTPException(status_code=401)
#-

# Google auth
from api.auth.database.shemas import GoogleOIDCModel
async def auth_by_google(request: Request, auth_code: str = None):  
    if not auth_code:
        if 'auth_service' in request.session:
            data = await _update_token(request.session['refresh_token'])
        else:
            raise HTTPException(status_code=401)
    else:
        # When we collect google token we can collect also user data.
        data = await _get_google_token(auth_code)
        request.session['refresh_token'] = data['refresh_token']

        token: str = data['id_token']
        encoded_sig = token.split('.', 2)[1].encode()
        decoded_sig = base64url_decode(encoded_sig)
        user_data = json.loads(decoded_sig.decode("utf-8"))

        request.session['name'] = user_data['given_name']
        request.session['username'] = user_data['family_name']
        request.session['email'] = user_data['email']
        request.session['picture_uri'] = user_data['picture']



        
    request.session['access_token'] = data['access_token']
    request.session['auth_service'] = 'google'

    if not 'name' in request.session:
        raise HTTPException(status_code=401)

    model = GoogleOIDCModel(
        name=request.session['name'],
        surname=request.session['username'],
        email=request.session['email'],
        picture_uri=request.session['picture_uri']
    )
    
    return model


async def _get_google_token(auth_code: str) -> tuple[str, str]:
    token_uri = await _get_google_endpoint('token_endpoint')
    params = [
        ('code', auth_code),
        ('client_id', GOOGLE_CLIENT_ID),
        ('client_secret', GOOGLE_CLIENT_SECRET),
        ('grant_type', GOOGLE_AUTH_GRANT_TYPE),
        ('redirect_uri', DEBUG_REDIRECT_URI),
    ]
    async with aiohttp.ClientSession() as session:
        async with session.post(token_uri, params=params) as resp:
            data = await resp.json()
            if resp.status >= 400:
                raise HTTPException(status_code=resp.status)
            return data


async def _update_token(refresh_token: str) -> tuple[str, str]:
    token_uri = await _get_google_endpoint('token_endpoint')

    params = [
        ('client_id', GOOGLE_CLIENT_ID),
        ('client_secret', GOOGLE_CLIENT_SECRET),
        ('grant_type', GOOGLE_REFRESH_TOKEN_GRANT_TYPE),
        ('refresh_token', refresh_token),
    ]
    async with aiohttp.ClientSession() as session:
        async with session.post(token_uri, params=params) as resp:
            data = await resp.json()
            if resp.status >= 400:
                raise HTTPException(status_code=resp.status)
            return data


async def _get_google_endpoint(field: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(GOOGLE_ENDPOINTS_INFO_URI) as resp:
            if resp.status >= 400:
                raise HTTPException(status_code=resp.status)
            return (await resp.json())[field]
#-
