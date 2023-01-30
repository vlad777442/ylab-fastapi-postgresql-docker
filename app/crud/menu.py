from sqlalchemy.orm import Session
from app.models.models import Menu
from app.schemas import menu


def get_menus(db: Session):
    return db.query(Menu).all()


def get_menu(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()


def get_menu_by_title(db: Session, title: str):
    return db.query(Menu).filter(Menu.title == title).first()


def create_menu(db: Session, menu: menu.MenuCreate):
    # new_menu = Menu(**menu.dict())
    new_menu = Menu(title=menu.title, description=menu.description)
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)

    return new_menu


def update_menu(db: Session, menu: menu.MenuUpdate, menu_id: int):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    menu_data = menu.dict(exclude_unset=True)
    for key, value in menu_data.items():
        setattr(db_menu, key, value)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: str):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    db.delete(menu)
    db.commit()
