from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud import auxiliar_servicos_gerais as crud
from app.schemas.auxiliar_servicos_gerais import AuxiliarServicosGeraisCreate, AuxiliarServicosGeraisUpdate, AuxiliarServicosGeraisResponse
from app.routes.helpers import bad_request, not_found

router = APIRouter(prefix="/auxiliares-servicos-gerais", tags=["Auxiliar de serviços gerais"])


@router.get("", response_model=list[AuxiliarServicosGeraisResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)


@router.get("/{matricula}", response_model=AuxiliarServicosGeraisResponse)
def buscar(matricula: str, db: Session = Depends(get_db)):
    registro = crud.buscar(db, matricula)
    if not registro:
        not_found("Auxiliar de serviços gerais não encontrado.")
    return registro


@router.post("", response_model=AuxiliarServicosGeraisResponse, status_code=201)
def criar(dados: AuxiliarServicosGeraisCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar(db, dados)
    except ValueError as error:
        bad_request(error)


@router.put("/{matricula}", response_model=AuxiliarServicosGeraisResponse)
def atualizar(matricula: str, dados: AuxiliarServicosGeraisUpdate, db: Session = Depends(get_db)):
    try:
        registro = crud.atualizar(db, matricula, dados)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Auxiliar de serviços gerais não encontrado.")
    return registro


@router.delete("/{matricula}")
def deletar(matricula: str, db: Session = Depends(get_db)):
    try:
        registro = crud.deletar(db, matricula)
    except ValueError as error:
        bad_request(error)
    if not registro:
        not_found("Auxiliar de serviços gerais não encontrado.")
    return {"message": "Auxiliar de serviços gerais removido com sucesso."}
