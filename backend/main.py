from fastapi import FastAPI
from data_base import engine
from models import peso

peso.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "backend funcionando", "framawork": "FastAPI"}