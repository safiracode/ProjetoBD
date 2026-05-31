from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class ReservaQuarto(Base):
    __tablename__ = "reserva_quarto"

    r_numero = Column(Integer, ForeignKey("reserva.numero"), primary_key=True)
    q_numero = Column(Integer, ForeignKey("quarto.numero"), primary_key=True)

    reserva = relationship("Reserva", back_populates="quartos")
    quarto = relationship("Quarto", back_populates="reservas")
