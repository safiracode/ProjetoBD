from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import empresa as crud
from app.schemas.empresa import EmpresaCreate, EmpresaUpdate, EmpresaResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/empresas", tags=["Empresa"])


@router.get("", response_model=list[EmpresaResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{id_titular}", response_model=EmpresaResponse)
def buscar(id_titular: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, id_titular)
    if not registro:
        not_found("Empresa não encontrada.")
    return registro


@router.post("", response_model=EmpresaResponse, status_code=201)
def criar(dados: EmpresaCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{id_titular}", response_model=EmpresaResponse)
def atualizar(id_titular: str, dados: EmpresaUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, id_titular, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Empresa não encontrada.")
    return registro


@router.delete("/{id_titular}")
def deletar(id_titular: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, id_titular)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Empresa não encontrada.")
    return {"message": "Empresa removida com sucesso."}
