from fastapi import FastAPI
from contextlib import asynccontextmanager
from chackers.core.logger import LOGGING
from chackers.core.config import settings
from logging import config as logging_config


@asynccontextmanager
async def lifespan(_):
    logging_config.dictConfig(LOGGING)

    yield


app = FastAPI(
    root_path=settings.app.root_path,
    title=settings.app.project_name,
    summary=settings.app.project_summary,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    version="0.1",
    lifespan=lifespan,
)


@app.get("/healthcheck")
async def health() -> None:
    return  # noqa
