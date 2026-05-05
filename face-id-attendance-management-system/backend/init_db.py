# init_db.py
from app.database import Base, engine
from app import models

print("🧩 Creating tables in attendance.db ...")

# Create all tables (only if they don't exist)
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
