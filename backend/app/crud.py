from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def create_block(db: Session, block: schemas.BlockCreate):
    db_block = models.Block(name=block.name)
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block

def get_blocks(db: Session):
    return db.query(models.Block).all()

def create_card(db: Session, card: schemas.CardCreate, block_id: int):
    db_card = models.Card(front=card.front, back=card.back, block_id=block_id)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

def get_cards_by_block(db: Session, block_id: int):
    return db.query(models.Card).filter(models.Card.block_id == block_id).all()

def delete_card(db: Session, card_id: int):
    card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail='Card Not Found.')
    
    db.delete(card)
    db.commit()
    return {'message': 'Card Deleted! 🗑️'}

def delete_block(db: Session, block_id: int):
    block = db.query(models.Block).filter(models.Block.id == block_id).first()
    if not block:
        raise HTTPException(statuscode=404, detail='Block not Found.')
    
    # verify if there is cards. only delete block with no cards associated. 
    has_cards = db.query(models.Card).filter(models.Card.block_id == block_id).first()
    if has_cards:
        raise HTTPException(status_code=400, detail='The block has cards. Only allow to delete blocks with no cards.')
    
    db.delete(block)
    db.commit()
    return {'message': f'Block "{block.name}" deleted! 🗑️'}