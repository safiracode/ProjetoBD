from sqlalchemy import Column, Date, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from app.database import Base


class Pagamento(Base):
    __tablename__ = "pagamento"

    id_pagamento = Column(String(20), primary_key=True, index=True)
    tipo_pagamento = Column(String(30))
    valor = Column(Numeric(10, 2))
    data = Column(Date)
    id_titular = Column(String(20), ForeignKey("titular_financeiro.id_titular"))
    r_matricula = Column(String(20), ForeignKey("recepcionista.matricula"))

    titular = relationship("TitularFinanceiro", back_populates="pagamentos")
    recepcionista = relationship("Recepcionista", back_populates="pagamentos")
