from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.reservation import Reservation
from app.schemas.reservation import ReservationCreate

router = APIRouter()

@router.get("/")
def read_reservations(
    db: Session = Depends(get_db),
):
    reservations = db.query(Reservation).order_by(Reservation.id.desc()).all()

    return {
        "message": "예약 조회 API",
        "items": reservations,
    }

@router.post("/")
def create_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(get_db),
    ):
    db_reservation = Reservation(
        visitor_name=reservation.visitor_name,
        company=reservation.company,
        phone=reservation.phone,
        visit_date=reservation.visit_date,
        visit_time=reservation.visit_time,
        purpose=reservation.purpose,
    )

    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)

    return {
        "message":"예약 등록 완료",
        "reservation": db_reservation
    }
    