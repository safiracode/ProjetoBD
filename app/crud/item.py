from sqlalchemy.orm import Session
from app import models
from app.schemas.item import ItemCreate, ItemUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Item).all()


def buscar(db: Session, codigo):
    return db.query(models.Item).filter(models.Item.codigo == codigo).first()


def criar(db: Session, dados: ItemCreate):
    if buscar(db, dados.codigo):
        raise ValueError("Registro já cadastrado.")

    obj = models.Item(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, codigo, dados: ItemUpdate):
    obj = buscar(db, codigo)
    if not obj:
        return None

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, codigo):
    obj = buscar(db, codigo)
    if not obj:
        return None

    if obj.consumos:
        raise ValueError("Não é possível deletar item vinculado a consumo.")

    db.delete(obj)
    db.commit()
    return obj
