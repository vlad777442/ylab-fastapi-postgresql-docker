from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import menu
from app.schemas.menu import MenuGet, MenuCreate, MenuUpdate
from app.db.database import get_db


router = APIRouter()


@router.get('/menus', response_model=List[MenuGet])
def get_menus(db: Session = Depends(get_db)):
    return menu.get_menus(db)

@router.get("/menus/{menu_id}", response_model=MenuGet)
def get_menu(menu_id: int, db: Session = Depends(get_db)):
    db_menu = menu.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu

@router.post("/menus", response_model=MenuGet, status_code=201)
def create_menu(new_menu: MenuCreate, db: Session = Depends(get_db)):
    db_menu = menu.get_menu_by_title(db, title=new_menu.title)
    if db_menu:
        raise HTTPException(status_code=400, detail="menu with this title already exist")
    return menu.create_menu(db=db, menu=new_menu)

@router.patch("/menus/{menu_id}", response_model=MenuGet)
def update_menu(menu_id: int, new_menu: MenuUpdate, db: Session = Depends(get_db)):
    db_menu = menu.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu.update_menu(db=db, menu=new_menu, menu_id=menu_id)

@router.delete("/menus/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    db_menu = menu.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    menu.delete_menu(db=db, menu_id=menu_id)
    return {"message": "The menu has been deleted"}