from sqlalchemy import Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class Dependente(Base):
    __tablename__ = "dependentes"

    numero_documento = Column(String(20), primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    tipo_documento = Column(String(20))
    data_nascimento = Column(Date)
    parentesco = Column(String(30))
    f_matricula = Column(String(20), ForeignKey("funcionario.matricula"))

    funcionario = relationship("Funcionario", back_populates="dependentes")
