from datetime import date
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Pessoa(Base):
    __tablename__ = "pessoa"

    numero_documento = Column(String(20), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    tipo_documento = Column(String(20), nullable=False)
    data_nascimento = Column(Date)
    id_endereco = Column(Integer, ForeignKey("endereco.id_endereco"))

    endereco = relationship("Endereco", back_populates="pessoas")
    funcionario = relationship("Funcionario", back_populates="pessoa", uselist=False)
    hospede = relationship("Hospede", back_populates="pessoa", uselist=False)

    @property
    def idade(self):
        if not self.data_nascimento:
            return None

        hoje = date.today()

        return (
            hoje.year
            - self.data_nascimento.year
            - (
                (hoje.month, hoje.day)
                < (self.data_nascimento.month, self.data_nascimento.day)
            )
        )