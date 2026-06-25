from fastapi import APIRouter
from fastapi import UploadFile, File

router = APIRouter(prefix="/resume",tags=["Resume"])


@router.get("/")
def home():
    return {
        "message": "Resume Router Working"
    }