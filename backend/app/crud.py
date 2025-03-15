from sqlalchemy.orm import Session
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
