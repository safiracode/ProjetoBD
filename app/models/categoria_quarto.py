from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship
from app.database import Base


class CategoriaQuarto(Base):
    __tablename__ = "categoria_quarto"

    tipo = Column(String(50), primary_key=True, index=True)
    capacidade_maxima = Column(Integer)
    valor_diaria = Column(Numeric(10, 2))

    quartos = relationship("Quarto", back_populates="categoria")
