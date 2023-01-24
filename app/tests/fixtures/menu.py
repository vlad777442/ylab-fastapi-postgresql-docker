import pytest
# from app.models.models import Menu
#
# @pytest.fixture(scope="session")
# def menu_1(db):
#     title = 'New menu'
#     description = 'New menu description'
#     new_menu = Menu(title=title, description=description)
#     db.add(new_menu)
#     db.commit()
#
#     return Menu(
#         id=new_menu.id,
#         title=title,
#         description=description,
#         dishes_count=new_menu.dishes_count,
#         submenus_count=new_menu.submenus_count
#     )