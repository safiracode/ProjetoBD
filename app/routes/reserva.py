from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import reserva as crud
from app.schemas.reserva import ReservaCreate, ReservaUpdate, ReservaResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/reservas", tags=["Reserva"])


@router.get("", response_model=list[ReservaResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{numero}", response_model=ReservaResponse)
def buscar(numero: int, db: Session = Depends(get_db)):
    registro = crud.buscar(db, numero)
    if not registro:
        not_found("Reserva não encontrada.")
    return registro


@router.post("", response_model=ReservaResponse, status_code=201)
def criar(dados: ReservaCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{numero}", response_model=ReservaResponse)
def atualizar(numero: int, dados: ReservaUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, numero, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Reserva não encontrada.")
    return registro


@router.delete("/{numero}")
def deletar(numero: int, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, numero)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Reserva não encontrada.")
    return {"message": "Reserva removida com sucesso."}
