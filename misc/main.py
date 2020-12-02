from typing import Optional

from fastapi import FastAPI

app = FastAPI()


# Fast API : https://fastapi.tiangolo.com/
# uvicorn main:app --reload

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return {"order_id": order_id, "status": "status_from_database"}
