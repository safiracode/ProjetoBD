from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class Recepcionista(Base):
    __tablename__ = "recepcionista"

    matricula = Column(String(20), ForeignKey("funcionario.matricula"), primary_key=True)
    turno = Column(String(20))
    conhecimento_sistema = Column(String(100))
    id_equipe = Column(String(20), ForeignKey("pessoa_operacional.id_equipe"))

    funcionario = relationship("Funcionario", back_populates="recepcionista")
    equipe = relationship("PessoaOperacional", back_populates="recepcionistas")
    idiomas = relationship("IdiomaRecepcionista", back_populates="recepcionista")
    reservas = relationship("Reserva", back_populates="recepcionista")
    pagamentos = relationship("Pagamento", back_populates="recepcionista")
