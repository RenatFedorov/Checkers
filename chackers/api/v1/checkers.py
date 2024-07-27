import uuid

from fastapi import APIRouter, Depends, status
from chackers.api.v1.models import IDModel

checkers_router = APIRouter(prefix="/api/v1/checkers", tags=["checkers"])


@checkers_router.get(
    "/",
    response_model=IDModel,
    status_code=status.HTTP_200_OK,
    description="Create a new game for 2 players in checkers. Return a unique id for the game to connect",
)
async def start_game():
    return IDModel(id=uuid.uuid4())


@checkers_router.post(
    "/",
    response_model=IDModel,
    status_code=status.HTTP_200_OK,
    description="Connect to already created game.",
)
async def connect_to_game(game_id: uuid.UUID):
    pass
