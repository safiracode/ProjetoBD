from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class Cozinheiro(Base):
    __tablename__ = "cozinheiro"

    matricula = Column(String(20), ForeignKey("funcionario.matricula"), primary_key=True)
    certificacao_gastronomica = Column(String(100))
    id_equipe = Column(String(20), ForeignKey("pessoa_operacional.id_equipe"))

    funcionario = relationship("Funcionario", back_populates="cozinheiro")
    equipe = relationship("PessoaOperacional", back_populates="cozinheiros")
