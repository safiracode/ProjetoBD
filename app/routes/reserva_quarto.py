from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import reserva_quarto as crud
from app.schemas.reserva_quarto import ReservaQuartoCreate, ReservaQuartoResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/reservas-quartos", tags=["Reserva x Quarto"])


@router.get("", response_model=list[ReservaQuartoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{r_numero}/{q_numero}", response_model=ReservaQuartoResponse)
def buscar(r_numero: int, q_numero: int, db: Session = Depends(get_db)):
    registro = crud.buscar(db, r_numero, q_numero)
    if not registro:
        not_found("Vínculo reserva-quarto não encontrado.")
    return registro


@router.post("", response_model=ReservaQuartoResponse, status_code=201)
def criar(dados: ReservaQuartoCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.delete("/{r_numero}/{q_numero}")
def deletar(r_numero: int, q_numero: int, db: Session = Depends(get_db)):
    registro = crud.deletar(db, r_numero, q_numero)
    if not registro:
        not_found("Vínculo reserva-quarto não encontrado.")
    return {"message": "Vínculo removido com sucesso."}
