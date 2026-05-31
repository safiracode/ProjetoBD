from sqlalchemy import Column, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from app.database import Base


class Diretor(Base):
    __tablename__ = "diretor"

    matricula = Column(String(20), ForeignKey("funcionario.matricula"), primary_key=True)
    percentual_participacao = Column(Numeric(5, 2))
    g_matricula = Column(String(20), ForeignKey("gerente.matricula"))

    funcionario = relationship("Funcionario", back_populates="diretor")
    gerente_liderado = relationship("Gerente", foreign_keys=[g_matricula], back_populates="diretor_lider")
