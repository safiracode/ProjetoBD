from datetime import date
from app.schemas.base import ORMBase


class ReservaBase(ORMBase):
    numero: int
    data_entrada: date | None = None
    data_saida: date | None = None
    quantidade_pessoas: int | None = None
    status_atual: str | None = None
    r_matricula: str | None = None


class ReservaCreate(ReservaBase):
    quartos: list[int] = []


class ReservaUpdate(ORMBase):
    data_entrada: date | None = None
    data_saida: date | None = None
    quantidade_pessoas: int | None = None
    status_atual: str | None = None
    r_matricula: str | None = None
    quartos: list[int] | None = None


class ReservaResponse(ReservaBase):
    pass
