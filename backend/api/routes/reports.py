from fastapi import APIRouter
from backend.usecases.get_latest_usecase import execute
from backend.usecases.get_report_history_usecase import execute as get_history


router = APIRouter(prefix="/reports")


@router.get("/latest")
def latest():
    return execute()

@router.get("/history")
def history():
    return execute()