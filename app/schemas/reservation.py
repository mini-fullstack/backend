from pydantic import BaseModel

class ReservationCreate(BaseModel):
    visitor_name: str
    company: str
    visit_date: str
    purpose: str