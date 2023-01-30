from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.crud import submenu
from app.schemas.submenu import SubmenuGet, SubmenuCreate, SubmenuUpdate
from app.db.cache_redis.cache_utils import get_cache, set_cache, is_cached, delete_cache

router = APIRouter()


@router.get('/submenus', response_model=list[SubmenuGet])
def get_submenus(menu_id: int, db: Session = Depends(get_db)):
    if is_cached(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus"):
        return get_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus")

    submenus = submenu.get_submenus(db)

    set_cache(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus", submenus)
    return submenus


@router.get("/submenus/{submenu_id}", response_model=SubmenuGet)
def get_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    if is_cached(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}"):
        return get_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}")

    db_submenu = submenu.get_submenu(db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")

    set_cache(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}", db_submenu)
    return db_submenu


@router.post("/submenus", response_model=SubmenuGet, status_code=201)
def create_submenu(menu_id: int, subm: SubmenuCreate, db: Session = Depends(get_db)):
    db_submenu = submenu.get_submenu_by_title(db, title=subm.title)
    if db_submenu:
        raise HTTPException(
            status_code=400, detail="submenu with this title already exist")

    new_submenu = submenu.create_submenu(db=db, submenu=subm, menu_id=menu_id)

    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus")
    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}")
    delete_cache("http://127.0.0.1:8000/api/v1/menus")

    return new_submenu


@router.patch("/submenus/{submenu_id}", response_model=SubmenuGet)
def update_submenu(menu_id: int, submenu_id: int, subm: SubmenuUpdate, db: Session = Depends(get_db)):
    db_submenu = submenu.get_submenu(db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    updated_submenu = submenu.update_submenu(
        db=db, submenu=subm, submenu_id=submenu_id)

    set_cache(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}", updated_submenu)
    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus")

    return updated_submenu


@router.delete("/submenus/{submenu_id}")
def delete_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = submenu.get_submenu(db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    submenu.delete_submenu(db=db, submenu_id=submenu_id)

    delete_cache(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}")
    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus")
    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}")
    delete_cache("http://127.0.0.1:8000/api/v1/menus")

    return {"message": "The submenu has been deleted"}
