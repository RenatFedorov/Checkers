from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class FastApiSettings(BaseSettings):
    project_name: str
    project_summary: str
    root_path: str

    model_config = SettingsConfigDict(env_prefix="fastapi_")


class SessionSettings(BaseSettings):
    secret_key: str
    cookie_name: str
    identifier: str
    max_age: int
    path: str
    secure: bool
    http_only: bool
    auto_error: bool

    model_config = SettingsConfigDict(env_prefix="session_")


class AppSettings:
    fast_api = FastApiSettings()
    session = SessionSettings()


settings = AppSettings()
