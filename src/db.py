import os
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Define paths relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # points to src/
DB_PATH = os.path.join(BASE_DIR, "liana_library.db")

# Path to sql_scripts folder (one level up from src/)
PROJECT_ROOT = os.path.dirname(BASE_DIR)
SQL_SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "sql_scripts")


def init_database():
    """Automatically creates and populates the SQLite database if liana_library.db is missing."""
    if not os.path.exists(DB_PATH):
        print("Database missing. Initializing from SQL scripts...")
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        schema_file = os.path.join(SQL_SCRIPTS_DIR, "define_schema.sql")
        populate_file = os.path.join(SQL_SCRIPTS_DIR, "populate_schema.sql")

        # Run define_schema.sql
        if os.path.exists(schema_file):
            with open(schema_file, "r") as f:
                cursor.executescript(f.read())

        # Run populate_schema.sql
        if os.path.exists(populate_file):
            with open(populate_file, "r") as f:
                cursor.executescript(f.read())

        conn.commit()
        conn.close()
        print("Database initialized successfully!")


# 2. Run automatic initialization check on import
init_database()

# 3. Create global SQLAlchemy engine pointing directly to liana_library.db
engine = create_engine(
    f"sqlite:///{DB_PATH}",
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def set_engine(e):
    """Retained for backward compatibility with existing code."""
    global engine
    engine = e


def get_engine():
    """Returns the automatically initialized SQLAlchemy engine."""
    return engine
