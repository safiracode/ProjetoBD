from sqlalchemy.orm import Session
from app import models
from app.schemas.pagamento import PagamentoCreate, PagamentoUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Pagamento).all()


def buscar(db: Session, id_pagamento):
    return db.query(models.Pagamento).filter(models.Pagamento.id_pagamento == id_pagamento).first()


def criar(db: Session, dados: PagamentoCreate):
    if buscar(db, dados.id_pagamento):
        raise ValueError("Registro já cadastrado.")

    if dados.id_titular is not None:
        existe = db.query(models.TitularFinanceiro).filter(models.TitularFinanceiro.id_titular == dados.id_titular).first()
        if not existe:
            raise ValueError("Titular financeiro informado não existe.")

    if dados.r_matricula is not None:
        existe = db.query(models.Recepcionista).filter(models.Recepcionista.matricula == dados.r_matricula).first()
        if not existe:
            raise ValueError("Recepcionista informada não existe.")

    obj = models.Pagamento(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, id_pagamento, dados: PagamentoUpdate):
    obj = buscar(db, id_pagamento)
    if not obj:
        return None

    if dados.id_titular is not None:
        existe = db.query(models.TitularFinanceiro).filter(models.TitularFinanceiro.id_titular == dados.id_titular).first()
        if not existe:
            raise ValueError("Titular financeiro informado não existe.")

    if dados.r_matricula is not None:
        existe = db.query(models.Recepcionista).filter(models.Recepcionista.matricula == dados.r_matricula).first()
        if not existe:
            raise ValueError("Recepcionista informada não existe.")

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, id_pagamento):
    obj = buscar(db, id_pagamento)
    if not obj:
        return None

    db.delete(obj)
    db.commit()
    return obj
