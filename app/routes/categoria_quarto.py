from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import categoria_quarto as crud
from app.schemas.categoria_quarto import CategoriaQuartoCreate, CategoriaQuartoUpdate, CategoriaQuartoResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/categorias-quarto", tags=["Categoria de quarto"])


@router.get("", response_model=list[CategoriaQuartoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{tipo}", response_model=CategoriaQuartoResponse)
def buscar(tipo: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, tipo)
    if not registro:
        not_found("Categoria de quarto não encontrada.")
    return registro


@router.post("", response_model=CategoriaQuartoResponse, status_code=201)
def criar(dados: CategoriaQuartoCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{tipo}", response_model=CategoriaQuartoResponse)
def atualizar(tipo: str, dados: CategoriaQuartoUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, tipo, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Categoria de quarto não encontrada.")
    return registro


@router.delete("/{tipo}")
def deletar(tipo: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, tipo)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Categoria de quarto não encontrada.")
    return {"message": "Categoria de quarto removida com sucesso."}
