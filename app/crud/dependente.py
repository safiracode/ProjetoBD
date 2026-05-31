from sqlalchemy.orm import Session
from app import models
from app.schemas.dependente import DependenteCreate, DependenteUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Dependente).all()


def buscar(db: Session, numero_documento):
    return db.query(models.Dependente).filter(models.Dependente.numero_documento == numero_documento).first()


def criar(db: Session, dados: DependenteCreate):
    if buscar(db, dados.numero_documento):
        raise ValueError("Registro já cadastrado.")

    if dados.f_matricula is not None:
        existe = db.query(models.Funcionario).filter(models.Funcionario.matricula == dados.f_matricula).first()
        if not existe:
            raise ValueError("Funcionário informado não existe.")

    obj = models.Dependente(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, numero_documento, dados: DependenteUpdate):
    obj = buscar(db, numero_documento)
    if not obj:
        return None

    if dados.f_matricula is not None:
        existe = db.query(models.Funcionario).filter(models.Funcionario.matricula == dados.f_matricula).first()
        if not existe:
            raise ValueError("Funcionário informado não existe.")

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, numero_documento):
    obj = buscar(db, numero_documento)
    if not obj:
        return None

    db.delete(obj)
    db.commit()
    return obj
