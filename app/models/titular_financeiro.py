from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class TitularFinanceiro(Base):
    __tablename__ = "titular_financeiro"

    id_titular = Column(String(20), primary_key=True, index=True)
    r_numero = Column(Integer, ForeignKey("reserva.numero"))

    reserva = relationship("Reserva", back_populates="titulares")
    hospedes = relationship("Hospede", back_populates="titular")
    empresa = relationship("Empresa", back_populates="titular", uselist=False)
    pagamentos = relationship("Pagamento", back_populates="titular")
