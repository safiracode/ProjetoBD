from sqlalchemy import Column, Date, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship
from app.database import Base


class Consome(Base):
    __tablename__ = "consome"

    r_numero = Column(Integer, ForeignKey("reserva.numero"), primary_key=True)
    i_codigo = Column(String(20), ForeignKey("item.codigo"), primary_key=True)
    data_pedido = Column(Date, primary_key=True)
    hora_pedido = Column(Time, primary_key=True)
    quantidade = Column(Integer)

    reserva = relationship("Reserva", back_populates="consumos")
    item = relationship("Item", back_populates="consumos")
