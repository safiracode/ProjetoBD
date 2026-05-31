from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import funcionario as crud
from app.schemas.funcionario import FuncionarioCreate, FuncionarioUpdate, FuncionarioResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/funcionarios", tags=["Funcionário"])


@router.get("", response_model=list[FuncionarioResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{matricula}", response_model=FuncionarioResponse)
def buscar(matricula: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, matricula)
    if not registro:
        not_found("Funcionário não encontrado.")
    return registro


@router.post("", response_model=FuncionarioResponse, status_code=201)
def criar(dados: FuncionarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{matricula}", response_model=FuncionarioResponse)
def atualizar(matricula: str, dados: FuncionarioUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, matricula, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Funcionário não encontrado.")
    return registro


@router.delete("/{matricula}")
def deletar(matricula: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, matricula)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Funcionário não encontrado.")
    return {"message": "Funcionário removido com sucesso."}
