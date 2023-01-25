import pytest
from fastapi.testclient import TestClient
from main import app

import pytest
import os
from fastapi.testclient import TestClient
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db

load_dotenv()

SQLALCHEMY_DATABASE_URL = (f'postgresql://{os.getenv("DB_USER")}:'
                                f'{os.getenv("DB_PASS")}@'
                                f'{os.getenv("DB_HOST")}:'
                                f'{os.getenv("DB_PORT")}/'
                                f'{os.getenv("DB_NAME")}')

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()


@pytest.fixture(scope="session")
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



@pytest.fixture(scope='module')
def client():
    client = TestClient(app=app)
    yield client



from app.models.models import Submenu

@pytest.fixture(scope="session")
def submenu_1(db, menu_1):
    title = 'New submenu'
    description = 'New submenu description'

    new_submenu = Submenu(
        title=title,
        description=description,
        menu_id=menu_1.id
    )
    db.add(new_submenu)
    db.commit()

    return Submenu(
        id=new_submenu.id,
        title=title,
        description=description,
        dishes_count=new_submenu.dishes_count,
    )


from app.models.models import Menu

@pytest.fixture(scope="session")
def menu_1(db):
    title = 'New menu'
    description = 'New menu description'
    new_menu = Menu(title=title, description=description)
    db.add(new_menu)
    db.commit()

    return Menu(
        id=new_menu.id,
        title=title,
        description=description,
        dishes_count=new_menu.dishes_count,
        submenus_count=new_menu.submenus_count
    )

from app.models.models import Dish

@pytest.fixture(scope="session")
def dish_1(db, submenu_1):
    title = 'New dish'
    description = 'New dish description'
    price = '13.99'
    new_dish = Dish(
        title=title,
        description=description,
        price=price,
        submenu_id=submenu_1.id
    )
    db.add(new_dish)
    db.commit()

    return Dish(
        id=new_dish.id,
        title=title,
        description=description,
        price=price
    )