from sqlalchemy.orm import Session
from app import models
from app.schemas.gerente import GerenteCreate, GerenteUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Gerente).all()


def buscar(db: Session, matricula):
    return db.query(models.Gerente).filter(models.Gerente.matricula == matricula).first()


def criar(db: Session, dados: GerenteCreate):
    if buscar(db, dados.matricula):
        raise ValueError("Registro já cadastrado.")

    if dados.matricula is not None:
        existe = db.query(models.Funcionario).filter(models.Funcionario.matricula == dados.matricula).first()
        if not existe:
            raise ValueError("Funcionário informado não existe.")

    if dados.d_matricula is not None:
        existe = db.query(models.Diretor).filter(models.Diretor.matricula == dados.d_matricula).first()
        if not existe:
            raise ValueError("Diretor informado não existe.")

    obj = models.Gerente(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, matricula, dados: GerenteUpdate):
    obj = buscar(db, matricula)
    if not obj:
        return None

    if dados.d_matricula is not None:
        existe = db.query(models.Diretor).filter(models.Diretor.matricula == dados.d_matricula).first()
        if not existe:
            raise ValueError("Diretor informado não existe.")

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, matricula):
    obj = buscar(db, matricula)
    if not obj:
        return None

    if obj.equipes:
        raise ValueError("Não é possível deletar gerente com equipes operacionais vinculadas.")

    db.delete(obj)
    db.commit()
    return obj
