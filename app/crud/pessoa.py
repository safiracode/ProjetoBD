from sqlalchemy.orm import Session
from app import models
from app.crud import endereco as endereco_crud
from app.crud.base import apply_updates
from app.schemas.pessoa import PessoaCreate, PessoaUpdate


def listar(db: Session):
    return db.query(models.Pessoa).all()


def buscar(db: Session, numero_documento: str):
    return db.query(models.Pessoa).filter(models.Pessoa.numero_documento == numero_documento).first()


def criar(db: Session, dados: PessoaCreate):
    if buscar(db, dados.numero_documento):
        raise ValueError("Pessoa já cadastrada.")

    id_endereco = dados.id_endereco
    if dados.endereco:
        novo_endereco = endereco_crud.criar(db, dados.endereco)
        id_endereco = novo_endereco.id_endereco
    elif id_endereco and not endereco_crud.buscar(db, id_endereco):
        raise ValueError("Endereço informado não existe.")

    pessoa = models.Pessoa(
        numero_documento=dados.numero_documento,
        nome=dados.nome,
        tipo_documento=dados.tipo_documento,
        data_nascimento=dados.data_nascimento,
        id_endereco=id_endereco,
    )
    db.add(pessoa)
    db.commit()
    db.refresh(pessoa)
    return pessoa


def atualizar(db: Session, numero_documento: str, dados: PessoaUpdate):
    pessoa = buscar(db, numero_documento)
    if not pessoa:
        return None

    values = dados.model_dump(exclude_unset=True)
    endereco_data = values.pop("endereco", None)
    id_endereco = values.pop("id_endereco", None)

    for field, value in values.items():
        setattr(pessoa, field, value)

    if endereco_data is not None:
        novo_endereco = models.Endereco(**endereco_data)
        db.add(novo_endereco)
        db.flush()
        pessoa.id_endereco = novo_endereco.id_endereco
    elif id_endereco is not None:
        if not endereco_crud.buscar(db, id_endereco):
            raise ValueError("Endereço informado não existe.")
        pessoa.id_endereco = id_endereco

    db.commit()
    db.refresh(pessoa)
    return pessoa


def deletar(db: Session, numero_documento: str):
    pessoa = buscar(db, numero_documento)
    if not pessoa:
        return None
    if pessoa.funcionario or pessoa.hospede:
        raise ValueError("Não é possível deletar pessoa vinculada a funcionário ou hóspede.")
    db.delete(pessoa)
    db.commit()
    return pessoa
