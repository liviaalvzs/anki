from pydantic import BaseModel
from typing import List, Optional

class CardCreate(BaseModel):
    front: str
    back: str

class CardResponse(CardCreate):
    id: int
    class Config:
        orm_mode = True

class BlockCreate(BaseModel):
    name: str

class BlockResponse(BlockCreate):
    id: int
    cards: List[CardResponse] = []
    class Config:
        orm_mode = True
