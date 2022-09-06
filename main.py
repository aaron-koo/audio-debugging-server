"""
main module
"""
import logging
from fastapi import (
    FastAPI,
    status,
)
from fastapi.middleware.cors import CORSMiddleware #pylint: disable=C0412

from routers import audio

logger = logging.getLogger(__name__)

app = FastAPI(
    title="audio transfer debugging server"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(audio.router)

@app.get("/",
    status_code=status.HTTP_200_OK,
)
async def health_check():
    return "hello world!"
