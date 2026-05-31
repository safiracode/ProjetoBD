from sqlalchemy import Column, Date, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from app.database import Base


class Funcionario(Base):
    __tablename__ = "funcionario"

    matricula = Column(String(20), primary_key=True, index=True)
    numero_documento = Column(String(20), ForeignKey("pessoa.numero_documento"), nullable=False, unique=True)
    cargo = Column(String(50))
    salario = Column(Numeric(10, 2))
    data_contratacao = Column(Date)

    pessoa = relationship("Pessoa", back_populates="funcionario")
    dependentes = relationship("Dependente", back_populates="funcionario")
    diretor = relationship("Diretor", back_populates="funcionario", uselist=False)
    gerente = relationship("Gerente", back_populates="funcionario", uselist=False)
    cozinheiro = relationship("Cozinheiro", back_populates="funcionario", uselist=False)
    camareiro = relationship("Camareiro", back_populates="funcionario", uselist=False)
    auxiliar_servicos_gerais = relationship("AuxiliarServicosGerais", back_populates="funcionario", uselist=False)
    recepcionista = relationship("Recepcionista", back_populates="funcionario", uselist=False)
