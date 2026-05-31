from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import recepcionista as crud
from app.schemas.recepcionista import RecepcionistaCreate, RecepcionistaUpdate, RecepcionistaResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/recepcionistas", tags=["Recepcionista"])


@router.get("", response_model=list[RecepcionistaResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{matricula}", response_model=RecepcionistaResponse)
def buscar(matricula: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, matricula)
    if not registro:
        not_found("Recepcionista não encontrado(a).")
    return registro


@router.post("", response_model=RecepcionistaResponse, status_code=201)
def criar(dados: RecepcionistaCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{matricula}", response_model=RecepcionistaResponse)
def atualizar(matricula: str, dados: RecepcionistaUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, matricula, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Recepcionista não encontrado(a).")
    return registro


@router.delete("/{matricula}")
def deletar(matricula: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, matricula)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Recepcionista não encontrado(a).")
    return {"message": "Recepcionista removido(a) com sucesso."}
