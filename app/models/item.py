from sqlalchemy import Column, Numeric, String
from sqlalchemy.orm import relationship
from app.database import Base


class Item(Base):
    __tablename__ = "item"

    codigo = Column(String(20), primary_key=True, index=True)
    valor_unitario = Column(Numeric(10, 2), nullable=False)
    descricao = Column(String(255))

    consumos = relationship("Consome", back_populates="item")
