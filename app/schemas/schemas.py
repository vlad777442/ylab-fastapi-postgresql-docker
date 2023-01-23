# from pydantic import BaseModel
#
# class MenuGet(BaseModel):
#     id: str
#     title: str
#     description: str
#
#     class Config:
#         orm_mode = True
#
#
# class MenuCreate(BaseModel):
#     title: str
#     description: str
#
#     class Config:
#         orm_mode = True
#
#
# class MenuUpdate(MenuCreate):
#     pass
#
#     class Config:
#         orm_mode = True
#
#
# class SubmenuGet(BaseModel):
#     id: str
#     title: str
#     description: str
#
#     class Config:
#         orm_mode = True
#
#
# class SubmenuCreate(BaseModel):
#     title: str
#     description: str
#
#     class Config:
#         orm_mode = True
#
#
# class SubmenuUpdate(SubmenuCreate):
#     pass
#
#     class Config:
#         orm_mode = True
#
#
# class DishGet(BaseModel):
#     id: str
#     title: str
#     description: str
#     price: str
#
#     class Config:
#         orm_mode = True
#
#
# class DishCreate(BaseModel):
#     title: str
#     description: str
#     price: float
#
#     class Config:
#         orm_mode = True
#
#
# class DishUpdate(DishCreate):
#     pass
#
#     class Config:
#         orm_mode = True
