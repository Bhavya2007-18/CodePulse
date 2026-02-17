from pydantic import BaseModel


# Schema for creating a developer (request body)
class DeveloperCreate(BaseModel):
    name: str
    skill: str


# Schema for returning developer data (response)
class DeveloperResponse(BaseModel):
    id: int
    name: str
    skill: str

    class Config:
        from_attributes = True  # Pydantic v2 version of orm_mode
