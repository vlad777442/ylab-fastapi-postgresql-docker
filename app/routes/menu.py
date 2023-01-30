from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.crud import menu
from app.schemas.menu import MenuGet, MenuCreate, MenuUpdate
from app.db.database import get_db
from app.db.cache_redis.cache_utils import get_cache, set_cache, is_cached, delete_cache

router = APIRouter()
menu_url = "http://127.0.0.1:8000/api/v1/menus"


@router.get('/menus', response_model=list[MenuGet])
def get_menus(request: Request, db: Session = Depends(get_db)):
    """
        Возвращает список всех меню
    """
    if not (get_cache(request.url._url)) is None:
        return get_cache(request.url._url)

    if is_cached("http://127.0.0.1:8000/api/v1/menus"):
        return get_cache("http://127.0.0.1:8000/api/v1/menus")

    menus_cache = menu.get_menus(db)

    set_cache(request.url._url, menus_cache)
    return menus_cache


@router.get("/menus/{menu_id}", response_model=MenuGet)
def get_menu(request: Request, menu_id: int, db: Session = Depends(get_db)):
    """
        Возвращает список меню по id
    """
    if is_cached(request.url._url):
        return get_cache(request.url._url)

    db_menu = menu.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    set_cache(request.url._url, db_menu)

    return db_menu


@router.post("/menus", response_model=MenuGet, status_code=201)
def create_menu(new_menu: MenuCreate, db: Session = Depends(get_db)):
    """
        Создает новое меню
    """
    db_menu = menu.get_menu_by_title(db, title=new_menu.title)
    if db_menu:
        raise HTTPException(
            status_code=400, detail="menu with this title already exist")

    new_menu = menu.create_menu(db=db, menu=new_menu)
    delete_cache("http://127.0.0.1:8000/api/v1/menus")

    return new_menu


@router.patch("/menus/{menu_id}", response_model=MenuGet)
def update_menu(menu_id: int, new_menu: MenuUpdate, db: Session = Depends(get_db)):
    """
        Обновляет определенное менб по id
    """
    db_menu = menu.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")

    updated_menu = menu.update_menu(db=db, menu=new_menu, menu_id=menu_id)
    delete_cache("http://127.0.0.1:8000/api/v1/menus")

    set_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}", updated_menu)

    return updated_menu


@router.delete("/menus/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    """
        Удаляет определенное меню
    """
    db_menu = menu.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    menu.delete_menu(db=db, menu_id=menu_id)

    delete_cache("http://127.0.0.1:8000/api/v1/menus")
    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}")

    return {"message": "The menu has been deleted"}
