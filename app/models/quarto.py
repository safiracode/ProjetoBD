from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Quarto(Base):
    __tablename__ = "quarto"

    numero = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), ForeignKey("categoria_quarto.tipo"))
    status = Column(String(30))

    categoria = relationship("CategoriaQuarto", back_populates="quartos")
    reservas = relationship("ReservaQuarto", back_populates="quarto")
