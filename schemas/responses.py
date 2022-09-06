from pydantic import (
    BaseModel,
    Field,
)

class BaseResponse(BaseModel):
    detail: str =  Field(..., example="ok")