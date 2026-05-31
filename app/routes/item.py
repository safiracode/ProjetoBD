from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import item as crud
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/itens", tags=["Item"])


@router.get("", response_model=list[ItemResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{codigo}", response_model=ItemResponse)
def buscar(codigo: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, codigo)
    if not registro:
        not_found("Item não encontrado.")
    return registro


@router.post("", response_model=ItemResponse, status_code=201)
def criar(dados: ItemCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{codigo}", response_model=ItemResponse)
def atualizar(codigo: str, dados: ItemUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, codigo, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Item não encontrado.")
    return registro


@router.delete("/{codigo}")
def deletar(codigo: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, codigo)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Item não encontrado.")
    return {"message": "Item removido com sucesso."}
