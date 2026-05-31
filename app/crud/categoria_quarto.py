from sqlalchemy.orm import Session
from app import models
from app.schemas.categoria_quarto import CategoriaQuartoCreate, CategoriaQuartoUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.CategoriaQuarto).all()


def buscar(db: Session, tipo):
    return db.query(models.CategoriaQuarto).filter(models.CategoriaQuarto.tipo == tipo).first()


def criar(db: Session, dados: CategoriaQuartoCreate):
    if buscar(db, dados.tipo):
        raise ValueError("Registro já cadastrado.")

    obj = models.CategoriaQuarto(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, tipo, dados: CategoriaQuartoUpdate):
    obj = buscar(db, tipo)
    if not obj:
        return None

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, tipo):
    obj = buscar(db, tipo)
    if not obj:
        return None

    if obj.quartos:
        raise ValueError("Não é possível deletar categoria usada por quartos.")

    db.delete(obj)
    db.commit()
    return obj
