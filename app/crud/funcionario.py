from sqlalchemy.orm import Session
from app import models
from app.schemas.funcionario import FuncionarioCreate, FuncionarioUpdate
from app.crud.base import apply_updates


def listar(db: Session):
    return db.query(models.Funcionario).all()


def buscar(db: Session, matricula: str):
    return db.query(models.Funcionario).filter(models.Funcionario.matricula == matricula).first()


def criar(db: Session, dados: FuncionarioCreate):
    if buscar(db, dados.matricula):
        raise ValueError("Funcionário já cadastrado.")
    pessoa = db.query(models.Pessoa).filter(models.Pessoa.numero_documento == dados.numero_documento).first()
    if not pessoa:
        raise ValueError("Pessoa informada não existe.")
    if pessoa.funcionario:
        raise ValueError("Pessoa já vinculada a outro funcionário.")
    funcionario = models.Funcionario(**dados.model_dump())
    db.add(funcionario)
    db.commit()
    db.refresh(funcionario)
    return funcionario


def atualizar(db: Session, matricula: str, dados: FuncionarioUpdate):
    funcionario = buscar(db, matricula)
    if not funcionario:
        return None
    apply_updates(funcionario, dados)
    db.commit()
    db.refresh(funcionario)
    return funcionario


def deletar(db: Session, matricula: str):
    funcionario = buscar(db, matricula)
    if not funcionario:
        return None
    if funcionario.dependentes or funcionario.diretor or funcionario.gerente or funcionario.cozinheiro or funcionario.camareiro or funcionario.auxiliar_servicos_gerais or funcionario.recepcionista:
        raise ValueError("Não é possível deletar funcionário com vínculos em especializações ou dependentes.")
    db.delete(funcionario)
    db.commit()
    return funcionario
