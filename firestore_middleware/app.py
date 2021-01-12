"""Google OIDC Authentication.
"""
import json

from authlib.integrations.starlette_client import OAuth
from authlib.integrations.starlette_client import OAuthError
from fastapi import FastAPI
from starlette.config import Config
from starlette.datastructures import Secret
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.responses import RedirectResponse

app = FastAPI()

config = Config('.env')
oauth = OAuth(config)

app.add_middleware(
    SessionMiddleware,
    secret_key=config.get('APP_SECRET_KEY', cast=Secret, default='!sekret'))

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'prompt': 'select_account',
        'include_granted_scopes': 'true',
        'access_type': 'offline',
        'scope':
            ' email'
            ' profile'
            ' offline'
            ' https://www.googleapis.m/auth/calendar'
    })


@app.route('/')
async def homepage(request: Request):
    user = request.session.get('user')
    if user:
        data = json.dumps(user)
        html = f'<pre>{data}</pre>' '<a href="/logout">logout</a>'
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')


@app.route('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.route('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f'<h1>{error.error}</h1>')
    user = await oauth.google.parse_id_token(request, token)
    request.session['user'] = dict(user)
    return RedirectResponse(url='/')


@app.route('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8000,
    )
