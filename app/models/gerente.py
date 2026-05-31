from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class Gerente(Base):
    __tablename__ = "gerente"

    matricula = Column(String(20), ForeignKey("funcionario.matricula"), primary_key=True)
    certificacao_gestao = Column(String(100))
    d_matricula = Column(String(20), ForeignKey("diretor.matricula"))

    funcionario = relationship("Funcionario", back_populates="gerente")
    diretor_lider = relationship("Diretor", foreign_keys=[d_matricula], back_populates="gerente_liderado")
    equipes = relationship("PessoaOperacional", back_populates="gerente")
