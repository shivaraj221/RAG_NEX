# app/models/employee.py
from sqlalchemy import Column, Integer, String, Date, Numeric
from app.db.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    company_code = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    department = Column(String)
    designation = Column(String)
    join_date = Column(Date)
    monthly_salary = Column(Numeric)
    status = Column(String)
    face_id = Column(String)