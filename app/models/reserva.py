from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Reserva(Base):
    __tablename__ = "reserva"

    numero = Column(Integer, primary_key=True, index=True)
    data_entrada = Column(Date)
    data_saida = Column(Date)
    quantidade_pessoas = Column(Integer)
    status_atual = Column(String(30))
    r_matricula = Column(String(20), ForeignKey("recepcionista.matricula"))

    recepcionista = relationship("Recepcionista", back_populates="reservas")
    quartos = relationship("ReservaQuarto", back_populates="reserva")
    titulares = relationship("TitularFinanceiro", back_populates="reserva")
    consumos = relationship("Consome", back_populates="reserva")
