from fastapi import FastAPI

app = FastAPI()

################ Introduction to FastAPI ################
# @app.get("/")
# async def root():
#     return {"message": "hello world"}


# @app.post("/")
# async def post():
#     return {"message": "hello from the post route"}


# @app.put("/")
# async def put():
#     return {"message": "hello from the put route"}

################## Path Parameters ##################
# Path parameters are used to capture values from the URL.

# from enum import Enum

# @app.get("/users")
# async def list_users():
#     return {"message": "list users route"}


# @app.get("/users/me")
# async def get_current_user():
#     return {"Message": "this is the current user"}


# @app.get("/users/{user_id}")
# async def get_user(user_id: str):
#     return {"user_id": user_id}


# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"


# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}

#     if food_name.value == "fruits":
#         return {
#             "food_name": food_name,
#             "message": "you are still healthy, but like sweet things",
#         }
#     return {"food_name": food_name, "message": "i like chocolate milk"}

################## Query Parameters ##################
# Query parameters are used to capture values from the URL query string.

# from enum import Enum

# fake_items_db = [{"item_name_01": "Foo"}, {"item_name_02": "Bar"}, {"item_name_03": "Baz"},
#                  {"item_name_04": "Zoo"}, {"item_name_05": "Tar"}, {"item_name_06": "Naz"},
#                  {"item_name_07": "Soo"}, {"item_name_08": "Lar"}, {"item_name_09": "Maz"}
#                  ]

# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# '''
# GET /items/{item_id} 엔드포인트를 생성
# item_id는 경로 매개변수이며 문자열(str)로 전달됨
# sample_query_param은 필수 쿼리 매개변수
# q는 선택적 쿼리 매개변수 (None이 기본값)
# short는 False가 기본값인 부울형(bool) 매개변수

# item = {"item_id": item_id, "sample_query_param": sample_query_param}
# item_id와 sample_query_param을 포함한 기본 응답 객체 생성.
# '''
# @app.get("/items/{item_id}")
# async def get_item(
#     item_id: str, sample_query_param: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
#             }
#         )
#     return item


# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
#             }
#         )
#         return item
    
############# Request Body Parameters #############
# Request body parameters are used to capture values from the request body.

# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict() # item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

################## Response Model with DB ##################
# Response models are used to define the structure of the response data.
# 간단한 메모리 내 데이터 저장소

# from pydantic import BaseModel

# fake_db = {}

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     """새로운 아이템을 생성하고 fake_db에 저장"""
#     item_dict = item.dict()
#     if item.tax:
#         item_dict["price_with_tax"] = item.price + item.tax
#     fake_db[item_id] = item_dict  # 아이템 저장
#     return {"message": "Item created", "item_id": item_id, "item": item_dict}

# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     """저장된 아이템을 조회"""
#     item = fake_db.get(item_id)
#     if not item:
#         return {"error": "Item not found"}
#     return {"item_id": item_id, "item": item}

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: str | None = None):
#     """기존 아이템을 업데이트"""
#     if item_id not in fake_db:
#         return {"error": "Item not found"}
    
#     result = {"item_id": item_id, **item.dict()}
#     if item.tax:
#         result["price_with_tax"] = item.price + item.tax
#     if q:
#         result["q"] = q
    
#     fake_db[item_id] = result  # 기존 데이터 업데이트
#     return {"message": "Item updated", "item": result}

################## Path, Query Module ##################
# 경로 매개변수(Path Parameters) 와 쿼리 매개변수(Query Parameters) 를 처리할 때 Path, Query 모듈
# from fastapi import Query, Path
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# # item은 FastAPI에서 요청 본문(body) 데이터를 받을 때 사용하는 Pydantic 모델
# # Pydantic의 BaseModel 객체를 Python의 딕셔너리로 변환 하는 역할
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items")
# async def read_items(
#     q: str
#     | None = Query(
#         None,
#         min_length=3,
#         max_length=10,
#         title="Sample query string",
#         description="This is a sample query string.",
#         alias="item-query",
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#  # include_in_schema=False: FastAPI의 자동 문서(Swagger UI, ReDoc)에 이 매개변수를 표시하지 않음
# @app.get("/items_hidden")
# async def hidden_query_route(
#     hidden_query: str | None = Query(None, include_in_schema=False)
# ):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}

# '''
# Path(...): item_id를 경로 매개변수로 지정
# int: item_id는 정수 타입이어야 함
# title="The ID of the item to get": API 문서에서 설명을 추가
# gt=10: item_id는 10보다 커야 함, le=100: item_id는 100 이하여야 함
# 즉 10 < item_id <= 100

# Query(...): 쿼리 매개변수로 지정
# float: size 값은 실수형이어야 함
# gt=0: size는 0보다 커야 함
# lt=7.75: size는 7.75보다 작아야 함
# 즉 0 < size < 7.75
# '''

# # Python에서 함수 정의 시 * (별표)는 키워드 전용 인자(Keyword-Only Arguments) 를 강제하는 역할
# # * 뒤에 오는 매개변수들은 반드시 키워드 인자로만 전달
# # 즉, 함수 호출 시 위치 인자로 전달할 수 없고, 반드시 key=value 형식으로 전달

# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", gt=10, le=100),
#     q: str = "hello",
#     size: float = Query(..., gt=0, lt=7.75)
# ):
#     results = {"item_id": item_id, "size": size}
#     if q:
#         results.update({"q": q})
#     return results
