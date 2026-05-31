from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class Empresa(Base):
    __tablename__ = "empresa"

    id_titular = Column(String(20), ForeignKey("titular_financeiro.id_titular"), primary_key=True)
    cnpj = Column(String(20), nullable=False, unique=True)
    razao_social = Column(String(150))
    telefone = Column(String(20))

    titular = relationship("TitularFinanceiro", back_populates="empresa")
