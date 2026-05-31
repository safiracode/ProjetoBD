from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class IdiomaRecepcionista(Base):
    __tablename__ = "idiomas_rec"

    r_matricula = Column(String(20), ForeignKey("recepcionista.matricula"), primary_key=True)
    idioma = Column(String(50), primary_key=True)

    recepcionista = relationship("Recepcionista", back_populates="idiomas")
