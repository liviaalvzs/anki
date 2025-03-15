from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Block(Base):
    __tablename__ = "blocks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    cards = relationship("Card", back_populates="block")

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    front = Column(String, nullable=False)
    back = Column(String, nullable=False)
    block_id = Column(Integer, ForeignKey("blocks.id"))

    block = relationship("Block", back_populates="cards")
