from datetime import date, time
from sqlalchemy.orm import Session
from app import models
from app.schemas.consome import ConsomeCreate, ConsomeUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Consome).all()


def buscar(db: Session, r_numero: int, i_codigo: str, data_pedido: date, hora_pedido: time):
    return db.query(models.Consome).filter(
        models.Consome.r_numero == r_numero,
        models.Consome.i_codigo == i_codigo,
        models.Consome.data_pedido == data_pedido,
        models.Consome.hora_pedido == hora_pedido,
    ).first()


def criar(db: Session, dados: ConsomeCreate):
    if dados.quantidade is not None and dados.quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")
    if not db.query(models.Reserva).filter(models.Reserva.numero == dados.r_numero).first():
        raise ValueError("Reserva informada não existe.")
    if not db.query(models.Item).filter(models.Item.codigo == dados.i_codigo).first():
        raise ValueError("Item informado não existe.")
    if buscar(db, dados.r_numero, dados.i_codigo, dados.data_pedido, dados.hora_pedido):
        raise ValueError("Consumo já cadastrado com essa chave composta.")
    obj = models.Consome(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, r_numero: int, i_codigo: str, data_pedido: date, hora_pedido: time, dados: ConsomeUpdate):
    obj = buscar(db, r_numero, i_codigo, data_pedido, hora_pedido)
    if not obj:
        return None
    if dados.quantidade is not None and dados.quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")
    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, r_numero: int, i_codigo: str, data_pedido: date, hora_pedido: time):
    obj = buscar(db, r_numero, i_codigo, data_pedido, hora_pedido)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj
