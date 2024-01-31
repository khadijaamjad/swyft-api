from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, status
from ..dependencies import get_token_header
from pydantic import BaseModel

fake_secret_token="pikachu"

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {
    "fruit": { "id":"fruit", "name": "Apple", "description": "An apple a day keeps sickness away." }, 
    "game": { "id": "game", "name": "CS2", "description": "Lets be competitive." },
    "tool": { "id": "tool", "name": "Screw Driver", "description": "Small screw driver." },
    "plant": { "id": "plant", "name": "Cactus", "description": "The good one." },
}

class Item(BaseModel):
    id: str
    name: str
    description: str | None = None


@router.get("/")
async def read_items():
    return fake_items_db

@router.get("/{item_id}", response_model=Item)
async def read_items(item_id: str, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid X-Token header")
    if item.id in fake_items_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Item already exists")
    fake_items_db[item.id] = item
    return item

@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "fruit":
        raise HTTPException(
            status_code=403, detail="You can only update the item: fruit"
        )
    return {"item_id": item_id, "name": "Red Apple"}