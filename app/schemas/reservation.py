from pydantic import BaseModel


class ReservationCreate(BaseModel):
    visitor_name: str
    company: str
    phone: str
    visit_date: str
    visit_time: str
    purpose: str