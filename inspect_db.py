# inspect_db.py
from sqlalchemy import create_engine, inspect, text

engine = create_engine("postgresql://postgres:123456789@localhost/hr_system")

# Connect and inspect
with engine.connect() as conn:
    # List all tables
    result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public';"))
    tables = result.fetchall()
    print("📊 Tables in hr_system database:")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Check employees table columns
    print("\n🔍 Checking employees table structure...")
    result = conn.execute(text("""
        SELECT column_name, data_type, is_nullable 
        FROM information_schema.columns 
        WHERE table_name = 'employees' 
        ORDER BY ordinal_position;
    """))
    columns = result.fetchall()
    for col in columns:
        print(f"  {col[0]} ({col[1]}) - Nullable: {col[2]}")
    
    # Count records
    result = conn.execute(text("SELECT COUNT(*) FROM employees;"))
    count = result.fetchone()[0]
    print(f"\n👥 Total employees: {count}")
    
    # Show sample data
    print("\n📋 Sample employees (first 5):")
    result = conn.execute(text("SELECT * FROM employees LIMIT 5;"))
    for row in result:
        print(f"  {row}")