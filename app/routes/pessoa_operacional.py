from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import pessoa_operacional as crud
from app.schemas.pessoa_operacional import PessoaOperacionalCreate, PessoaOperacionalUpdate, PessoaOperacionalResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/equipes-operacionais", tags=["Equipe operacional"])


@router.get("", response_model=list[PessoaOperacionalResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{id_equipe}", response_model=PessoaOperacionalResponse)
def buscar(id_equipe: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, id_equipe)
    if not registro:
        not_found("Equipe operacional não encontrada.")
    return registro


@router.post("", response_model=PessoaOperacionalResponse, status_code=201)
def criar(dados: PessoaOperacionalCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{id_equipe}", response_model=PessoaOperacionalResponse)
def atualizar(id_equipe: str, dados: PessoaOperacionalUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, id_equipe, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Equipe operacional não encontrada.")
    return registro


@router.delete("/{id_equipe}")
def deletar(id_equipe: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, id_equipe)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Equipe operacional não encontrada.")
    return {"message": "Equipe operacional removida com sucesso."}
