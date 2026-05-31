from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class PessoaOperacional(Base):
    __tablename__ = "pessoa_operacional"

    id_equipe = Column(String(20), primary_key=True, index=True)
    g_matricula = Column(String(20), ForeignKey("gerente.matricula"))

    gerente = relationship("Gerente", back_populates="equipes")
    cozinheiros = relationship("Cozinheiro", back_populates="equipe")
    camareiros = relationship("Camareiro", back_populates="equipe")
    auxiliares = relationship("AuxiliarServicosGerais", back_populates="equipe")
    recepcionistas = relationship("Recepcionista", back_populates="equipe")
