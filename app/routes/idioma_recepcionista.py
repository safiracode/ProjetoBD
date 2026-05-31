from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import idioma_recepcionista as crud
from app.schemas.idioma_recepcionista import IdiomaRecepcionistaCreate, IdiomaRecepcionistaResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/idiomas-recepcionista", tags=["Idiomas do recepcionista"])


@router.get("", response_model=list[IdiomaRecepcionistaResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{r_matricula}/{idioma}", response_model=IdiomaRecepcionistaResponse)
def buscar(r_matricula: str, idioma: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, r_matricula, idioma)
    if not registro:
        not_found("Idioma da recepcionista não encontrado.")
    return registro


@router.post("", response_model=IdiomaRecepcionistaResponse, status_code=201)
def criar(dados: IdiomaRecepcionistaCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.delete("/{r_matricula}/{idioma}")
def deletar(r_matricula: str, idioma: str, db: Session = Depends(get_db)):
    registro = crud.deletar(db, r_matricula, idioma)
    if not registro:
        not_found("Idioma da recepcionista não encontrado.")
    return {"message": "Idioma removido com sucesso."}
