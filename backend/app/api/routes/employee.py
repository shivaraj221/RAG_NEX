from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.employee import Employee

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()
