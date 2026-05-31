from sqlalchemy.orm import Session
from app import models
from app.schemas.recepcionista import RecepcionistaCreate, RecepcionistaUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Recepcionista).all()


def buscar(db: Session, matricula):
    return db.query(models.Recepcionista).filter(models.Recepcionista.matricula == matricula).first()


def criar(db: Session, dados: RecepcionistaCreate):
    if buscar(db, dados.matricula):
        raise ValueError("Registro já cadastrado.")

    if dados.matricula is not None:
        existe = db.query(models.Funcionario).filter(models.Funcionario.matricula == dados.matricula).first()
        if not existe:
            raise ValueError("Funcionário informado não existe.")

    if dados.id_equipe is not None:
        existe = db.query(models.PessoaOperacional).filter(models.PessoaOperacional.id_equipe == dados.id_equipe).first()
        if not existe:
            raise ValueError("Equipe informada não existe.")

    obj = models.Recepcionista(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, matricula, dados: RecepcionistaUpdate):
    obj = buscar(db, matricula)
    if not obj:
        return None

    if dados.id_equipe is not None:
        existe = db.query(models.PessoaOperacional).filter(models.PessoaOperacional.id_equipe == dados.id_equipe).first()
        if not existe:
            raise ValueError("Equipe informada não existe.")

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, matricula):
    obj = buscar(db, matricula)
    if not obj:
        return None

    if obj.reservas or obj.pagamentos or obj.idiomas:
        raise ValueError("Não é possível deletar recepcionista com reservas, pagamentos ou idiomas vinculados.")

    db.delete(obj)
    db.commit()
    return obj
