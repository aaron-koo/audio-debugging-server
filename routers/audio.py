import logging
from fastapi import (
    status,
    APIRouter,
    UploadFile,
    File
)

from schemas.responses import BaseResponse

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/audio"
)

@router.post("/upload",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "model": BaseResponse
        }
    }
)
def post_audio(
    audio: UploadFile = File(...)
):
    return BaseResponse(
        detail="ok"
    )
