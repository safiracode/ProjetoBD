from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import camareiro as crud
from app.schemas.camareiro import CamareiroCreate, CamareiroUpdate, CamareiroResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/camareiros", tags=["Camareiro"])


@router.get("", response_model=list[CamareiroResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{matricula}", response_model=CamareiroResponse)
def buscar(matricula: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, matricula)
    if not registro:
        not_found("Camareiro não encontrado.")
    return registro


@router.post("", response_model=CamareiroResponse, status_code=201)
def criar(dados: CamareiroCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{matricula}", response_model=CamareiroResponse)
def atualizar(matricula: str, dados: CamareiroUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, matricula, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Camareiro não encontrado.")
    return registro


@router.delete("/{matricula}")
def deletar(matricula: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, matricula)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Camareiro não encontrado.")
    return {"message": "Camareiro removido com sucesso."}
