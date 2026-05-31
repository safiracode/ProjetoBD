from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import quarto as crud
from app.schemas.quarto import QuartoCreate, QuartoUpdate, QuartoResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/quartos", tags=["Quarto"])


@router.get("", response_model=list[QuartoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{numero}", response_model=QuartoResponse)
def buscar(numero: int, db: Session = Depends(get_db)):
    registro = crud.buscar(db, numero)
    if not registro:
        not_found("Quarto não encontrado.")
    return registro


@router.post("", response_model=QuartoResponse, status_code=201)
def criar(dados: QuartoCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{numero}", response_model=QuartoResponse)
def atualizar(numero: int, dados: QuartoUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, numero, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Quarto não encontrado.")
    return registro


@router.delete("/{numero}")
def deletar(numero: int, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, numero)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Quarto não encontrado.")
    return {"message": "Quarto removido com sucesso."}
