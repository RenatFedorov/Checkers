from uuid import UUID
from pydantic import BaseModel


class IDModel(BaseModel):
    id: UUID
