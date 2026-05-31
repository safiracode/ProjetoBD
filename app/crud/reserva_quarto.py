from sqlalchemy.orm import Session
from app import models
from app.schemas.reserva_quarto import ReservaQuartoCreate


def listar(db: Session):
    return db.query(models.ReservaQuarto).all()


def buscar(db: Session, r_numero: int, q_numero: int):
    return db.query(models.ReservaQuarto).filter(
        models.ReservaQuarto.r_numero == r_numero,
        models.ReservaQuarto.q_numero == q_numero,
    ).first()


def criar(db: Session, dados: ReservaQuartoCreate):
    if not db.query(models.Reserva).filter(models.Reserva.numero == dados.r_numero).first():
        raise ValueError("Reserva informada não existe.")
    if not db.query(models.Quarto).filter(models.Quarto.numero == dados.q_numero).first():
        raise ValueError("Quarto informado não existe.")
    if buscar(db, dados.r_numero, dados.q_numero):
        raise ValueError("Vínculo entre reserva e quarto já existe.")
    obj = models.ReservaQuarto(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, r_numero: int, q_numero: int):
    obj = buscar(db, r_numero, q_numero)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj
