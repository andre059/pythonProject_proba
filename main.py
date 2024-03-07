# from typing import Union
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#     await send({
#         'type': 'http.response.start',
#         'status': 200,
#         'headers': [
#             [b'content-type', b'text/plain'],
#         ]
#     })
#     await send({
#         'type': 'http.response.body',
#         'body': b'Hello, world!',
#     })

# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/hello")
# async def hello():
#     return {"message": "Hello, World!"}

# from fastapi import FastAPI
# from pydantic import BaseModel
#
#
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = None
#
#
# app = FastAPI()
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.is_offer:
#         item_dict.update({"message": "Special offer"})
#     return item_dict
