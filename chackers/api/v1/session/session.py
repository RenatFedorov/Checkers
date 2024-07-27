from uuid import uuid4, UUID

from fastapi import APIRouter, Depends, Response, status

from chackers.api.v1.session.models import (
    SessionData,
    backend,
    cookie,
    verifier,
)

auth_router = APIRouter(
    prefix="/api/v1/session",
    tags=["session"],
)


@auth_router.post(
    "/create/{name}",
    status_code=status.HTTP_201_CREATED,
    description="Create a new session for user.",
)
async def create_session(name: str, response: Response):
    session: UUID = uuid4()
    data = SessionData(username=name)

    await backend.create(session, data)
    cookie.attach_to_response(response, session)
    return {"message": session}


@auth_router.get(
    "/check/",
    description="Check if session is valid.",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(cookie)],
)
async def check_session(session_data: SessionData = Depends(verifier)):
    return session_data


@auth_router.delete(
    "/delete/",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete session",
)
async def delete_session(response: Response, session_id: UUID = Depends(cookie)):
    await backend.delete(session_id)
    cookie.delete_from_response(response)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
