from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import endereco as crud
from app.schemas.endereco import EnderecoCreate, EnderecoUpdate, EnderecoResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/enderecos", tags=["Endereço"])


@router.get("", response_model=list[EnderecoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.post("", response_model=EnderecoResponse, status_code=201)
def criar(dados: EnderecoCreate, db: Session = Depends(get_db)):
    return crud.criar(db, dados)


@router.get("/{id_endereco}", response_model=EnderecoResponse)
def buscar(id_endereco: int, db: Session = Depends(get_db)):
    registro = crud.buscar(db, id_endereco)
    if not registro:
        not_found("Endereço não encontrado.")
    return registro


@router.put("/{id_endereco}", response_model=EnderecoResponse)
def atualizar(id_endereco: int, dados: EnderecoUpdate, db: Session = Depends(get_db)):
    registro = crud.atualizar(db, id_endereco, dados)
    if not registro:
        not_found("Endereço não encontrado.")
    return registro


@router.delete("/{id_endereco}")
def deletar(id_endereco: int, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, id_endereco)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Endereço não encontrado.")
    return {"message": "Endereço removido com sucesso."}
