from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = Config()

engine = create_engine(config.POSTGRES_DB_URL)

SessionLocal = sessionmaker(bind=engine, autocommit= False, autoFlush = False)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()