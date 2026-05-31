from sqlalchemy.orm import Session
from app import models
from app.crud import pessoa as pessoa_crud
from app.crud.base import apply_updates
from app.schemas.hospede import HospedeCreate, HospedeUpdate


def listar(db: Session):
    return db.query(models.Hospede).all()


def buscar(db: Session, numero_documento: str):
    return db.query(models.Hospede).filter(models.Hospede.numero_documento == numero_documento).first()


def criar(db: Session, dados: HospedeCreate):
    if buscar(db, dados.numero_documento):
        raise ValueError("Hóspede já cadastrado.")

    pessoa = db.query(models.Pessoa).filter(models.Pessoa.numero_documento == dados.numero_documento).first()
    if not pessoa:
        if not dados.pessoa:
            raise ValueError("Pessoa informada não existe. Envie uma pessoa existente ou preencha o campo pessoa.")
        pessoa = pessoa_crud.criar(db, dados.pessoa)

    if dados.id_titular is not None:
        titular = db.query(models.TitularFinanceiro).filter(models.TitularFinanceiro.id_titular == dados.id_titular).first()
        if not titular:
            raise ValueError("Titular financeiro informado não existe.")

    obj = models.Hospede(
        numero_documento=dados.numero_documento,
        id_titular=dados.id_titular,
        e_mail=dados.e_mail,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, numero_documento: str, dados: HospedeUpdate):
    obj = buscar(db, numero_documento)
    if not obj:
        return None
    if dados.id_titular is not None:
        titular = db.query(models.TitularFinanceiro).filter(models.TitularFinanceiro.id_titular == dados.id_titular).first()
        if not titular:
            raise ValueError("Titular financeiro informado não existe.")
    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, numero_documento: str):
    obj = buscar(db, numero_documento)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj
