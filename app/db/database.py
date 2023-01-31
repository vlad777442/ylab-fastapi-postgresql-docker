from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def clear_db(Base, engine):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# clear_db(Base, engine)
