import logging
from fastapi import (
    status,
    APIRouter,
    UploadFile,
    File
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/audio"
)

@router.post("/upload",
    status_code=status.HTTP_200_OK,
)
def post_audio(
    audio: UploadFile = File(...)
):
    return "ok"
