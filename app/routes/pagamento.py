from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import pagamento as crud
from app.schemas.pagamento import PagamentoCreate, PagamentoUpdate, PagamentoResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/pagamentos", tags=["Pagamento"])


@router.get("", response_model=list[PagamentoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{id_pagamento}", response_model=PagamentoResponse)
def buscar(id_pagamento: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, id_pagamento)
    if not registro:
        not_found("Pagamento não encontrado.")
    return registro


@router.post("", response_model=PagamentoResponse, status_code=201)
def criar(dados: PagamentoCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{id_pagamento}", response_model=PagamentoResponse)
def atualizar(id_pagamento: str, dados: PagamentoUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, id_pagamento, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Pagamento não encontrado.")
    return registro


@router.delete("/{id_pagamento}")
def deletar(id_pagamento: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, id_pagamento)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Pagamento não encontrado.")
    return {"message": "Pagamento removido com sucesso."}
