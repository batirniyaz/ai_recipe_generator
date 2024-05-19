from pydantic import BaseModel


class DescriptionRequest(BaseModel):
    description: str
