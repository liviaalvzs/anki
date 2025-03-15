from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database, models

router = APIRouter()

@router.post("/blocks/{block_id}/cards/", response_model=schemas.CardResponse)
def create_card(block_id: int, card: schemas.CardCreate, db: Session = Depends(database.get_db)):
    # verify if existent block
    block = db.query(models.Block).filter(models.Block.id == block_id).first()
    if not block:
        raise HTTPException(status_code=404, detail="Bloco não encontrado")

    return crud.create_card(db, card, block_id)

@router.get("/blocks/{block_id}/cards/", response_model=list[schemas.CardResponse])
def get_cards(block_id: int, db: Session = Depends(database.get_db)):
    return crud.get_cards_by_block(db, block_id)

@router.delete("/cards/{card_id}/", response_model=dict)
def delete_card(card_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_card(db, card_id)
