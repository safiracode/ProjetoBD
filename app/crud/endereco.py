from sqlalchemy.orm import Session
from app import models
from app.schemas.endereco import EnderecoCreate, EnderecoUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Endereco).all()


def buscar(db: Session, id_endereco: int):
    return db.query(models.Endereco).filter(models.Endereco.id_endereco == id_endereco).first()


def criar(db: Session, dados: EnderecoCreate):
    endereco = models.Endereco(**dados.model_dump())
    db.add(endereco)
    db.commit()
    db.refresh(endereco)
    return endereco


def atualizar(db: Session, id_endereco: int, dados: EnderecoUpdate):
    endereco = buscar(db, id_endereco)
    if not endereco:
        return None
    apply_updates(endereco, dados)
    db.commit()
    db.refresh(endereco)
    return endereco


def deletar(db: Session, id_endereco: int):
    endereco = buscar(db, id_endereco)
    if not endereco:
        return None
    if endereco.pessoas:
        raise ValueError("Não é possível deletar endereço vinculado a pessoa.")
    db.delete(endereco)
    db.commit()
    return endereco
