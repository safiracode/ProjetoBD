from datetime import date, time
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import consome as crud
from app.schemas.consome import ConsomeCreate, ConsomeUpdate, ConsomeResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/consumos", tags=["Consumo"])


@router.get("", response_model=list[ConsomeResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{r_numero}/{i_codigo}/{data_pedido}/{hora_pedido}", response_model=ConsomeResponse)
def buscar(r_numero: int, i_codigo: str, data_pedido: date, hora_pedido: time, db: Session = Depends(get_db)):
    registro = crud.buscar(db, r_numero, i_codigo, data_pedido, hora_pedido)
    if not registro:
        not_found("Consumo não encontrado.")
    return registro


@router.post("", response_model=ConsomeResponse, status_code=201)
def criar(dados: ConsomeCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{r_numero}/{i_codigo}/{data_pedido}/{hora_pedido}", response_model=ConsomeResponse)
def atualizar(r_numero: int, i_codigo: str, data_pedido: date, hora_pedido: time, dados: ConsomeUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, r_numero, i_codigo, data_pedido, hora_pedido, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Consumo não encontrado.")
    return registro


@router.delete("/{r_numero}/{i_codigo}/{data_pedido}/{hora_pedido}")
def deletar(r_numero: int, i_codigo: str, data_pedido: date, hora_pedido: time, db: Session = Depends(get_db)):
    registro = crud.deletar(db, r_numero, i_codigo, data_pedido, hora_pedido)
    if not registro:
        not_found("Consumo não encontrado.")
    return {"message": "Consumo removido com sucesso."}
