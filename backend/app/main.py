# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.database import engine
from app.db.session import get_db
from app.api.routes.employee import router as employee_router   # ← this was missing

app = FastAPI(
    title="HR System API",
    description="Backend for FaceLock HR System",
    version="0.1.0"
)
app.include_router(employee_router, prefix="/api", tags=["employees"])

@app.get("/")
def root():
    return {"message": "HR System API is running", "database": "PostgreSQL"}

@app.get("/db-check")
def db_check():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1")).fetchone()
        return {
            "status": "connected",
            "result": result[0],
            "database": "PostgreSQL",
            "engine": "SQLAlchemy"
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

@app.get("/db-check-orm")
def db_check_orm(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT version()")).fetchone()
        return {
            "status": "connected",
            "postgres_version": result[0],
            "database": "PostgreSQL",
            "orm": "SQLAlchemy ORM"
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

@app.get("/health")
def health():
    return {"status": "healthy", "database": "PostgreSQL"}

