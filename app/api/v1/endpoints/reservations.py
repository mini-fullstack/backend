from fastapi import APIRouter

from app.schemas.reservation import ReservationCreate

router = APIRouter()

@router.get("/")
def read_reservations():
    return {
        "message": "예약 목록 조회 API",
        "items": [],
    }

@router.post("/")
def create_reservation(reservation: ReservationCreate):
    return {
        "message": "예약 등록 완료",
        "reservation": reservation,
    }
