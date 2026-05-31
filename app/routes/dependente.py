from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import dependente as crud
from app.schemas.dependente import DependenteCreate, DependenteUpdate, DependenteResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/dependentes", tags=["Dependente"])


@router.get("", response_model=list[DependenteResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{numero_documento}", response_model=DependenteResponse)
def buscar(numero_documento: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, numero_documento)
    if not registro:
        not_found("Dependente não encontrado.")
    return registro


@router.post("", response_model=DependenteResponse, status_code=201)
def criar(dados: DependenteCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{numero_documento}", response_model=DependenteResponse)
def atualizar(numero_documento: str, dados: DependenteUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, numero_documento, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Dependente não encontrado.")
    return registro


@router.delete("/{numero_documento}")
def deletar(numero_documento: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, numero_documento)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Dependente não encontrado.")
    return {"message": "Dependente removido com sucesso."}
