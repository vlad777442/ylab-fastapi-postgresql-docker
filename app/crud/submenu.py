from app.models.models import Submenu
from sqlalchemy.orm import Session
# from app.schemas import schemas
from app.schemas import submenu

def get_submenus(db: Session):
    return db.query(Submenu).all()


def get_submenu(db: Session, submenu_id: int):
    return db.query(Submenu).filter(Submenu.id == submenu_id).first()


def get_submenu_by_title(db: Session, title: str):
    return db.query(Submenu).filter(Submenu.title == title).first()


def create_submenu(menu_id: str, submenu: submenu.SubmenuCreate, db: Session):
    db_submenu = Submenu(menu_id=menu_id, **submenu.dict())
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu



def update_submenu(db: Session, submenu: submenu.SubmenuUpdate, submenu_id: int):
    db_submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    submenu_data = submenu.dict(exclude_unset=True)
    for key, value in submenu_data.items():
        setattr(db_submenu, key, value)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def delete_submenu(db: Session, submenu_id: int):
    db_submenu = db.query(Submenu).filter(Submenu.id == submenu_id).first()
    db.delete(db_submenu)
    db.commit()
