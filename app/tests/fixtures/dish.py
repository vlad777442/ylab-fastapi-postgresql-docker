import pytest
# from app.models.models import Dish
#
# @pytest.fixture(scope="session")
# def dish_1(db, submenu_1):
#     title = 'New dish'
#     description = 'New dish description'
#     price = '13.99'
#     new_dish = Dish(
#         title=title,
#         description=description,
#         price=price,
#         submenu_id=submenu_1.id
#     )
#     db.add(new_dish)
#     db.commit()
#
#     return Dish(
#         id=new_dish.id,
#         title=title,
#         description=description,
#         price=price
#     )