# app/db/database.py
from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base

# Debug: Show what URL is being used
print(f"🔧 Database URL: {settings.DATABASE_URL}")

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=True  # This shows SQL queries in console
)

Base = declarative_base()