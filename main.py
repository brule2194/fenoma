from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    item: str
    quantity: int
    status: str
    price: float



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/solution/{criterion}')
def process_orders(orders: list[Item], criterion: str):
    aux_list: list = []
    if criterion == "all":
        aux_list = orders
    total = 0.00
    for order in orders:
        if criterion == "all":
            total += order.quantity * order.price
        elif order.status == criterion:
            total += order.quantity * order.price

    return {"suma": total}
