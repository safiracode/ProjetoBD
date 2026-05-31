from sqlalchemy.orm import Session
from app import models
from app.schemas.pessoa_operacional import PessoaOperacionalCreate, PessoaOperacionalUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.PessoaOperacional).all()


def buscar(db: Session, id_equipe):
    return db.query(models.PessoaOperacional).filter(models.PessoaOperacional.id_equipe == id_equipe).first()


def criar(db: Session, dados: PessoaOperacionalCreate):
    if buscar(db, dados.id_equipe):
        raise ValueError("Registro já cadastrado.")

    if dados.g_matricula is not None:
        existe = db.query(models.Gerente).filter(models.Gerente.matricula == dados.g_matricula).first()
        if not existe:
            raise ValueError("Gerente informado não existe.")

    obj = models.PessoaOperacional(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def atualizar(db: Session, id_equipe, dados: PessoaOperacionalUpdate):
    obj = buscar(db, id_equipe)
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


def deletar(db: Session, id_equipe):
    obj = buscar(db, id_equipe)
    if not obj:
        return None

    if obj.cozinheiros or obj.camareiros or obj.auxiliares or obj.recepcionistas:
        raise ValueError("Não é possível deletar equipe com funcionários operacionais vinculados.")

    db.delete(obj)
    db.commit()
    return obj
