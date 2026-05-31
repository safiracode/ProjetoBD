from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Endereco(Base):
    __tablename__ = "endereco"

    id_endereco = Column(Integer, primary_key=True, index=True)
    tipo_logradouro = Column(String(20))
    nome_logradouro = Column(String(100))
    numero = Column(String(20))
    bairro = Column(String(50))
    cidade = Column(String(50))
    cep = Column(String(15))

    pessoas = relationship("Pessoa", back_populates="endereco")
