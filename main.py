from fastapi import FastAPI
from app.routes import dish, submenu, menu

from app.db.database import Base, engine

app = FastAPI()

# @app.on_event("startup")
# def startup():
#     db = get_db()
#     db.query(Menu).delete()
#     db.query(Submenu).delete()
#     db.query(Dish).delete()
#     db.commit()
#     db.close()
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)



app.include_router(
        menu.router,
        prefix='/api/v1',
        tags=['menu']
    )
app.include_router(
    submenu.router,
    prefix='/api/v1/menus/{menu_id}',
    tags=['submenu']
)
app.include_router(
    dish.router,
    prefix='/api/v1/menus/{menu_id}/submenus/{submenu_id}',
    tags=['dish']
)



#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
