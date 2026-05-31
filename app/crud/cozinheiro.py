from sqlalchemy.orm import Session
from app import models
from app.schemas.cozinheiro import CozinheiroCreate, CozinheiroUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Cozinheiro).all()


def buscar(db: Session, matricula):
    return db.query(models.Cozinheiro).filter(models.Cozinheiro.matricula == matricula).first()


def criar(db: Session, dados: CozinheiroCreate):
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

    obj = models.Cozinheiro(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, matricula, dados: CozinheiroUpdate):
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

    db.delete(obj)
    db.commit()
    return obj
