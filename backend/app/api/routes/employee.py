# app/api/routes/employee.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Correct relative/absolute import for model
from app.models.employee import Employee           # ← this line was failing

# If the above still fails, try one of these alternatives:
# from ...models.employee import Employee          # relative (3 levels up)
# from app.models.employee import Employee         # absolute (recommended)

from app.db.session import get_db
# from app.schemas.employee import EmployeeOut     # if you have schemas

router = APIRouter()

@router.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    print(f"Found {len(employees)} employees")     # debug
    return employees

# Optional: add one more endpoint for testing single employee
@router.get("/employees/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp