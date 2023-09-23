from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Item(BaseModel):
    item: str
    quantity: int
    price: float
    status: bool




@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/solution")
def process_orders(orders, criterion):
    return {"item_name"}