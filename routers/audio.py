import logging
import watchtower
from fastapi import (
    status,
    APIRouter,
    UploadFile,
    File
)

from schemas.responses import BaseResponse


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = watchtower.CloudWatchLogHandler(
    log_group_name="/audio-debugging-server",
    log_stream_name="audio"
)
logger.addHandler(handler)

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
    logger.info("successfully received the audio file.")
    return BaseResponse(
        detail="ok"
    )
