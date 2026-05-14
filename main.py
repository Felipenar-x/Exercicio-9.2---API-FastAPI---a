from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: Optional[int] = None
    name: str

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

@app.get("/")
def read_root():
    return {"message": "API FastAPI rodando!", "endpoint": "/items"}

@app.get("/items", response_model=dict)
def get_items():
    return {"items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return {"item": item}
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.post("/items", status_code=201)
def create_item(item: Item):
    new_id = items[-1]["id"] + 1 if items else 1
    new_item = {"id": new_id, "name": item.name}
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}")
def update_item(item_id: int, item_update: Item):
    for item in items:
        if item["id"] == item_id:
            item["name"] = item_update.name
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    items = [item for item in items if item["id"] != item_id]
    return {"result": "Sucesso", "message": f"Item {item_id} removido"}