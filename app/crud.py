from sqlalchemy.orm import Session
from app import models, schemas


def listar_quartos(db: Session):
    return db.query(models.Quarto).all()


def buscar_quarto(db: Session, numero: int):
    return db.query(models.Quarto).filter(models.Quarto.numero == numero).first()


def criar_quarto(db: Session, quarto: schemas.QuartoCreate):
    categoria = db.query(models.CategoriaQuarto).filter(
        models.CategoriaQuarto.tipo == quarto.tipo
    ).first()

    if not categoria:
        return None

    novo_quarto = models.Quarto(
        numero=quarto.numero,
        tipo=quarto.tipo,
        status=quarto.status
    )

    db.add(novo_quarto)
    db.commit()
    db.refresh(novo_quarto)

    return novo_quarto


def atualizar_quarto(db: Session, numero: int, dados: schemas.QuartoUpdate):
    quarto = buscar_quarto(db, numero)

    if not quarto:
        return None

    if dados.tipo is not None:
        quarto.tipo = dados.tipo

    if dados.status is not None:
        quarto.status = dados.status

    db.commit()
    db.refresh(quarto)

    return quarto


def deletar_quarto(db: Session, numero: int):
    quarto = buscar_quarto(db, numero)

    if not quarto:
        return None

    db.delete(quarto)
    db.commit()

    return quarto