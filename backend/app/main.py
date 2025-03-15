from fastapi import FastAPI
from .database import Base, engine
from .routes import blocks, cards

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Anki API")

app.include_router(blocks.router, prefix="/api")
app.include_router(cards.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Anki!"}
