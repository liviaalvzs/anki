from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/blocks/", response_model=schemas.BlockResponse)
def create_block(block: schemas.BlockCreate, db: Session = Depends(database.get_db)):
    return crud.create_block(db, block)

@router.get("/blocks/", response_model=list[schemas.BlockResponse])
def get_blocks(db: Session = Depends(database.get_db)):
    return crud.get_blocks(db)
