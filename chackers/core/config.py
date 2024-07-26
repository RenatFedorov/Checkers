from pydantic_settings import BaseSettings, SettingsConfigDict


class FastApiSettings(BaseSettings):
    project_name: str
    project_summary: str
    root_path: str

    model_config = SettingsConfigDict(env_prefix="fastapi_")


class AppSettings:
    fast_api = FastApiSettings()


settings = AppSettings()