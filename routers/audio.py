import logging

import watchtower
import boto3
from fastapi import (
    status,
    APIRouter,
    UploadFile,
    File,
    Form
)

from schemas.responses import BaseResponse


boto3_logs_client = boto3.client(
    "logs",
    region_name="ap-northeast-2"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = watchtower.CloudWatchLogHandler(
    log_group_name="/audio-debugging-server",
    log_stream_name="audio",
    boto3_client=boto3_logs_client
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
    audio: UploadFile = File(...),
    seq_num: int = Form(...)
):
    logger.info(f"[SUCCESS] {seq_num}")
    return BaseResponse(
        detail="ok"
    )
