from fastapi import FastAPI
from contextlib import asynccontextmanager
from chackers.core.logger import LOGGING
from chackers.core.config import settings
from logging import config as logging_config
import uvicorn
from chackers.api.v1.checkers import checkers_router
from chackers.api.v1.session.session import auth_router


@asynccontextmanager
async def lifespan(_):
    logging_config.dictConfig(LOGGING)

    yield


app = FastAPI(
    root_path=settings.fast_api.root_path,
    title=settings.fast_api.project_name,
    summary=settings.fast_api.project_summary,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    version="0.1",
    lifespan=lifespan,
)

app.include_router(checkers_router)
app.include_router(auth_router)


@app.get("/healthcheck")
async def health() -> None:
    return  # noqa


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
