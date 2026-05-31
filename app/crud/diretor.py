from sqlalchemy.orm import Session
from app import models
from app.schemas.diretor import DiretorCreate, DiretorUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Diretor).all()


def buscar(db: Session, matricula):
    return db.query(models.Diretor).filter(models.Diretor.matricula == matricula).first()


def criar(db: Session, dados: DiretorCreate):
    if buscar(db, dados.matricula):
        raise ValueError("Registro já cadastrado.")

    if dados.matricula is not None:
        existe = db.query(models.Funcionario).filter(models.Funcionario.matricula == dados.matricula).first()
        if not existe:
            raise ValueError("Funcionário informado não existe.")

    if dados.g_matricula is not None:
        existe = db.query(models.Gerente).filter(models.Gerente.matricula == dados.g_matricula).first()
        if not existe:
            raise ValueError("Gerente informado não existe.")

    obj = models.Diretor(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, matricula, dados: DiretorUpdate):
    obj = buscar(db, matricula)
    if not obj:
        return None

    if dados.g_matricula is not None:
        existe = db.query(models.Gerente).filter(models.Gerente.matricula == dados.g_matricula).first()
        if not existe:
            raise ValueError("Gerente informado não existe.")

    apply_updates(obj, dados)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, matricula):
    obj = buscar(db, matricula)
    if not obj:
        return None

    if obj.gerente_liderado:
        raise ValueError("Não é possível deletar diretor com gerente vinculado.")

    db.delete(obj)
    db.commit()
    return obj
