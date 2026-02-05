from pydantic import BaseModel, ConfigDict
from datetime import date
from decimal import Decimal
from typing import Optional


class EmployeeOut(BaseModel):
    id: int
    company_code: str
    full_name: str
    email: str
    phone: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    join_date: date
    monthly_salary: Decimal
    status: Optional[str] = None
    face_id: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,   # Allows conversion from SQLAlchemy objects
        json_encoders={
            Decimal: str,       # Prevent Decimal serialization issues
            date: lambda v: v.isoformat()
        }
    )