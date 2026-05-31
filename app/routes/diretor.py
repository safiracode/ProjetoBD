from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import diretor as crud
from app.schemas.diretor import DiretorCreate, DiretorUpdate, DiretorResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/diretores", tags=["Diretor"])


@router.get("", response_model=list[DiretorResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{matricula}", response_model=DiretorResponse)
def buscar(matricula: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, matricula)
    if not registro:
        not_found("Diretor não encontrado.")
    return registro


@router.post("", response_model=DiretorResponse, status_code=201)
def criar(dados: DiretorCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{matricula}", response_model=DiretorResponse)
def atualizar(matricula: str, dados: DiretorUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, matricula, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Diretor não encontrado.")
    return registro


@router.delete("/{matricula}")
def deletar(matricula: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, matricula)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Diretor não encontrado.")
    return {"message": "Diretor removido com sucesso."}
