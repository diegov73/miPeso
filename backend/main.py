from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List

from data_base import engine
from models import modelo_peso
import data_base
import schemas

modelo_peso.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "backend funcionando", "framawork": "FastAPI"}

@app.post("/peso/")
def post_peso(datos: schemas.RegistroPeso_create, db: Session = Depends(data_base.get_db)):

    new_registro = modelo_peso.RegistroPeso(
        peso = datos.peso
    )

    db.add(new_registro)
    db.commit()
    db.refresh(new_registro)

    return new_registro

@app.get("/pesos/", response_model=List[schemas.RegistroPeso_response])
def get_pesos(dias: int = Query(default=7, gt=0), db: Session = Depends(data_base.get_db)):

    fecha_inicio = datetime.now() - timedelta(days=dias)

    registros = db.query(modelo_peso.RegistroPeso).filter(
        modelo_peso.RegistroPeso.fecha >= fecha_inicio
    ).order_by(modelo_peso.RegistroPeso.fecha.asc()).all()

    return registros