# import pytest
# from app.db.database import Base, engine, SessionLocal
# @pytest.fixture(scope='module')
# def db():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#
#     db = SessionLocal
#     try:
#         yield db
#     finally:
#         db.close()