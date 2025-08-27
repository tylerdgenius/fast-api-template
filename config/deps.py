# app/deps.py
from contextlib import contextmanager
from sqlalchemy.orm import Session, sessionmaker
from .db import Database

# Create our DB (single instance for app lifespan)
db = Database()
SessionLocal = sessionmaker(bind=db.engine, expire_on_commit=False)

@contextmanager
def session_scope():
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def get_session():
    # FastAPI will treat generators as dependencies
    with session_scope() as s:
        yield s