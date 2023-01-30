from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.crud import dish
from app.schemas.dish import DishGet, DishCreate, DishUpdate
from app.db.cache_redis.cache_utils import get_cache, set_cache, is_cached, delete_cache

router = APIRouter()


@router.get('/dishes', response_model=list[DishGet])
def get_dishes(request: Request, db: Session = Depends(get_db)):
    if get_cache(request.url._url):
        return get_cache(request.url._url)

    dishes = dish.get_dishes(db)

    set_cache(request.url._url, dishes)
    return dishes


@router.get("/dishes/{dish_id}", response_model=DishGet)
def get_dish(request: Request, dish_id: int, db: Session = Depends(get_db)):

    if is_cached(request.url._url):
        return get_cache(request.url._url)

    db_dish = dish.get_dish(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")

    set_cache(request.url._url, db_dish)
    return db_dish


@router.post("/dishes", response_model=DishGet, status_code=201)
def create_dish(request: Request, menu_id: int, submenu_id: int, d: DishCreate, db: Session = Depends(get_db)):
    db_dish = dish.get_dish_by_title(db, title=d.title)
    if db_dish:
        raise HTTPException(
            status_code=400, detail="dish with this title already exist")

    delete_cache("http://127.0.0.1:8000/api/v1/menus")
    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}")
    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus")
    delete_cache(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}")
    delete_cache(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes")

    return dish.create_dish(db=db, dish=d, submenu_id=submenu_id)


@router.patch("/dishes/{dish_id}", response_model=DishGet)
def update_dish(request: Request, menu_id: int, submenu_id: int, dish_id: int, d: DishUpdate,
                db: Session = Depends(get_db)):
    db_dish = dish.get_dish(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")

    updated_dish = dish.update_dish(db=db, dish=d, dish_id=dish_id)
    set_cache(request.url._url, updated_dish)
    delete_cache(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes")

    return updated_dish


@router.delete("/dishes/{dish_id}")
def delete_submenu(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
    db_dish = dish.get_dish(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    dish.delete_dish(db=db, dish_id=dish_id)

    delete_cache("http://127.0.0.1:8000/api/v1/menus")
    delete_cache(f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus")
    delete_cache(
        f"http://127.0.0.1:8000/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes")

    return {"message": "The dish has been deleted"}
