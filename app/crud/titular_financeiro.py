from sqlalchemy.orm import Session
from app import models
from app.schemas.titular_financeiro import TitularFinanceiroCreate, TitularFinanceiroUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.TitularFinanceiro).all()


def buscar(db: Session, id_titular):
    return db.query(models.TitularFinanceiro).filter(models.TitularFinanceiro.id_titular == id_titular).first()


def criar(db: Session, dados: TitularFinanceiroCreate):
    if buscar(db, dados.id_titular):
        raise ValueError("Registro já cadastrado.")

    if dados.r_numero is not None:
        existe = db.query(models.Reserva).filter(models.Reserva.numero == dados.r_numero).first()
        if not existe:
            raise ValueError("Reserva informada não existe.")

    obj = models.TitularFinanceiro(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, id_titular, dados: TitularFinanceiroUpdate):
    obj = buscar(db, id_titular)
    if not obj:
        return None

    if dados.r_numero is not None:
        existe = db.query(models.Reserva).filter(models.Reserva.numero == dados.r_numero).first()
        if not existe:
            raise ValueError("Reserva informada não existe.")

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, id_titular):
    obj = buscar(db, id_titular)
    if not obj:
        return None

    if obj.hospedes or obj.empresa or obj.pagamentos:
        raise ValueError("Não é possível deletar titular financeiro com vínculos.")

    db.delete(obj)
    db.commit()
    return obj
