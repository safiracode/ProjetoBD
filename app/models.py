from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
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


class Pessoa(Base):
    __tablename__ = "pessoa"

    numero_documento = Column(String(20), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    tipo_documento = Column(String(20), nullable=False)
    data_nascimento = Column(Date)
    id_endereco = Column(Integer, ForeignKey("endereco.id_endereco"))

    endereco = relationship("Endereco", back_populates="pessoas")


class CategoriaQuarto(Base):
    __tablename__ = "categoria_quarto"

    tipo = Column(String(50), primary_key=True, index=True)
    capacidade_maxima = Column(Integer)
    valor_diaria = Column(Numeric(10, 2))

    quartos = relationship("Quarto", back_populates="categoria")


class Quarto(Base):
    __tablename__ = "quarto"

    numero = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), ForeignKey("categoria_quarto.tipo"))
    status = Column(String(30))

    categoria = relationship("CategoriaQuarto", back_populates="quartos")
    reservas = relationship("ReservaQuarto", back_populates="quarto")


class Reserva(Base):
    __tablename__ = "reserva"

    numero = Column(Integer, primary_key=True, index=True)
    data_entrada = Column(Date)
    data_saida = Column(Date)
    quantidade_pessoas = Column(Integer)
    status_atual = Column(String(30))
    r_matricula = Column(String(20), ForeignKey("recepcionista.matricula"))

    quartos = relationship("ReservaQuarto", back_populates="reserva")


class ReservaQuarto(Base):
    __tablename__ = "reserva_quarto"

    r_numero = Column(Integer, ForeignKey("reserva.numero"), primary_key=True)
    q_numero = Column(Integer, ForeignKey("quarto.numero"), primary_key=True)

    reserva = relationship("Reserva", back_populates="quartos")
    quarto = relationship("Quarto", back_populates="reservas")