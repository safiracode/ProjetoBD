from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import titular_financeiro as crud
from app.schemas.titular_financeiro import TitularFinanceiroCreate, TitularFinanceiroUpdate, TitularFinanceiroResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/titulares-financeiros", tags=["Titular financeiro"])


@router.get("", response_model=list[TitularFinanceiroResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{id_titular}", response_model=TitularFinanceiroResponse)
def buscar(id_titular: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, id_titular)
    if not registro:
        not_found("Titular financeiro não encontrado.")
    return registro


@router.post("", response_model=TitularFinanceiroResponse, status_code=201)
def criar(dados: TitularFinanceiroCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{id_titular}", response_model=TitularFinanceiroResponse)
def atualizar(id_titular: str, dados: TitularFinanceiroUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, id_titular, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Titular financeiro não encontrado.")
    return registro


@router.delete("/{id_titular}")
def deletar(id_titular: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, id_titular)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Titular financeiro não encontrado.")
    return {"message": "Titular financeiro removido com sucesso."}
