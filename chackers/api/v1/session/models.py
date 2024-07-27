from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from fastapi_sessions.frontends.implementations.cookie import SameSiteEnum
from fastapi_sessions.session_verifier import SessionVerifier
from pydantic import BaseModel

from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.frontends.implementations import SessionCookie
from chackers.core.config import settings


class SessionData(BaseModel):
    username: str
    game_count: int = 0
    wins: int = 0


class CookieParameters(BaseModel):
    max_age: int = settings.session.max_age
    path: str = settings.session.path
    domain: Optional[str] = None
    secure: bool = settings.session.secure
    httponly: bool = settings.session.http_only
    samesite: SameSiteEnum = SameSiteEnum.lax


cookie_params = CookieParameters()

cookie = SessionCookie(
    cookie_name=settings.session.cookie_name,
    secret_key=settings.session.secret_key,
    identifier=settings.session.identifier,
    auto_error=True,
    cookie_params=cookie_params,
)


class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: SessionData) -> bool:
        """If the session exists, it is valid"""
        return True


backend = InMemoryBackend[UUID, SessionData]()

verifier = BasicVerifier(
    identifier=settings.session.identifier,
    auto_error=True,
    backend=backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)
