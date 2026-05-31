from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class Camareiro(Base):
    __tablename__ = "camareiro"

    matricula = Column(String(20), ForeignKey("funcionario.matricula"), primary_key=True)
    velocidade_troca_lencol = Column(String(50))
    id_equipe = Column(String(20), ForeignKey("pessoa_operacional.id_equipe"))

    funcionario = relationship("Funcionario", back_populates="camareiro")
    equipe = relationship("PessoaOperacional", back_populates="camareiros")
