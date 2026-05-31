from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class Hospede(Base):
    __tablename__ = "hospede"

    numero_documento = Column(String(20), ForeignKey("pessoa.numero_documento"), primary_key=True)
    id_titular = Column(String(20), ForeignKey("titular_financeiro.id_titular"))
    e_mail = Column(String(100))

    pessoa = relationship("Pessoa", back_populates="hospede")
    titular = relationship("TitularFinanceiro", back_populates="hospedes")
