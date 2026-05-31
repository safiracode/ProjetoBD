from sqlalchemy.orm import Session
from app import models
from app.schemas.idioma_recepcionista import IdiomaRecepcionistaCreate


def listar(db: Session):
    return db.query(models.IdiomaRecepcionista).all()


def buscar(db: Session, r_matricula: str, idioma: str):
    return db.query(models.IdiomaRecepcionista).filter(
        models.IdiomaRecepcionista.r_matricula == r_matricula,
        models.IdiomaRecepcionista.idioma == idioma,
    ).first()


def criar(db: Session, dados: IdiomaRecepcionistaCreate):
    recepcionista = db.query(models.Recepcionista).filter(models.Recepcionista.matricula == dados.r_matricula).first()
    if not recepcionista:
        raise ValueError("Recepcionista informada não existe.")
    if buscar(db, dados.r_matricula, dados.idioma):
        raise ValueError("Idioma já cadastrado para essa recepcionista.")
    obj = models.IdiomaRecepcionista(**dados.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def deletar(db: Session, r_matricula: str, idioma: str):
    obj = buscar(db, r_matricula, idioma)
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj
