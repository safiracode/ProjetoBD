from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class AuxiliarServicosGerais(Base):
    __tablename__ = "auxiliar_servicos_gerais"

    matricula = Column(String(20), ForeignKey("funcionario.matricula"), primary_key=True)
    area_atuacao = Column(String(100))
    id_equipe = Column(String(20), ForeignKey("pessoa_operacional.id_equipe"))

    funcionario = relationship("Funcionario", back_populates="auxiliar_servicos_gerais")
    equipe = relationship("PessoaOperacional", back_populates="auxiliares")
