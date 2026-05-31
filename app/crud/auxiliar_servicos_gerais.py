from sqlalchemy.orm import Session
from app import models
from app.schemas.auxiliar_servicos_gerais import AuxiliarServicosGeraisCreate, AuxiliarServicosGeraisUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.AuxiliarServicosGerais).all()


def buscar(db: Session, matricula):
    return db.query(models.AuxiliarServicosGerais).filter(models.AuxiliarServicosGerais.matricula == matricula).first()


def criar(db: Session, dados: AuxiliarServicosGeraisCreate):
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

    obj = models.AuxiliarServicosGerais(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, matricula, dados: AuxiliarServicosGeraisUpdate):
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
