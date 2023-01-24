import pytest
# from app.models.models import Submenu
#
# @pytest.fixture(scope="session")
# def submenu_1(db, menu_1):
#     title = 'New submenu'
#     description = 'New submenu description'
#
#     new_submenu = Submenu(
#         title=title,
#         description=description,
#         menu_id=menu_1.id
#     )
#     db.add(new_submenu)
#     db.commit()
#
#     return Submenu(
#         id=new_submenu.id,
#         title=title,
#         description=description,
#         dishes_count=new_submenu.dishes_count,
#     )