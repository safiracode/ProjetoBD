from sqlalchemy.orm import Session
from app import models
from app.schemas.quarto import QuartoCreate, QuartoUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Quarto).all()


def buscar(db: Session, numero):
    return db.query(models.Quarto).filter(models.Quarto.numero == numero).first()


def criar(db: Session, dados: QuartoCreate):
    if buscar(db, dados.numero):
        raise ValueError("Registro já cadastrado.")

    if dados.tipo is not None:
        existe = db.query(models.CategoriaQuarto).filter(models.CategoriaQuarto.tipo == dados.tipo).first()
        if not existe:
            raise ValueError("Categoria de quarto informada não existe.")

    obj = models.Quarto(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, numero, dados: QuartoUpdate):
    obj = buscar(db, numero)
    if not obj:
        return None

    if dados.tipo is not None:
        existe = db.query(models.CategoriaQuarto).filter(models.CategoriaQuarto.tipo == dados.tipo).first()
        if not existe:
            raise ValueError("Categoria de quarto informada não existe.")

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, numero):
    obj = buscar(db, numero)
    if not obj:
        return None

    if obj.reservas:
        raise ValueError("Não é possível deletar quarto vinculado a reserva.")

    db.delete(obj)
    db.commit()
    return obj
