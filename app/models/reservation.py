from sqlalchemy import Column, DateTime, Integer, String, Text, func

from app.db.base import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    visitor_name = Column(String(50), nullable=False)
    company = Column(String(100), nullable=False)
    phone = Column(String(30), nullable=False)
    visit_date = Column(String(10), nullable=False)
    visit_time = Column(String(5), nullable=False)
    purpose = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())