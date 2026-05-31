from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import pessoa as crud
from app.schemas.pessoa import PessoaCreate, PessoaUpdate, PessoaResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/pessoas", tags=["Pessoa"])


@router.get("", response_model=list[PessoaResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{numero_documento}", response_model=PessoaResponse)
def buscar(numero_documento: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, numero_documento)
    if not registro:
        not_found("Pessoa não encontrada.")
    return registro


@router.post("", response_model=PessoaResponse, status_code=201)
def criar(dados: PessoaCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{numero_documento}", response_model=PessoaResponse)
def atualizar(numero_documento: str, dados: PessoaUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, numero_documento, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Pessoa não encontrada.")
    return registro


@router.delete("/{numero_documento}")
def deletar(numero_documento: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, numero_documento)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Pessoa não encontrada.")
    return {"message": "Pessoa removida com sucesso."}
