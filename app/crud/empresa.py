from sqlalchemy.orm import Session
from app import models
from app.schemas.empresa import EmpresaCreate, EmpresaUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Empresa).all()


def buscar(db: Session, id_titular):
    return db.query(models.Empresa).filter(models.Empresa.id_titular == id_titular).first()


def criar(db: Session, dados: EmpresaCreate):
    if buscar(db, dados.id_titular):
        raise ValueError("Registro já cadastrado.")

    if dados.id_titular is not None:
        existe = db.query(models.TitularFinanceiro).filter(models.TitularFinanceiro.id_titular == dados.id_titular).first()
        if not existe:
            raise ValueError("Titular financeiro informado não existe.")

    obj = models.Empresa(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, id_titular, dados: EmpresaUpdate):
    obj = buscar(db, id_titular)
    if not obj:
        return None

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, id_titular):
    obj = buscar(db, id_titular)
    if not obj:
        return None

    db.delete(obj)
    db.commit()
    return obj
