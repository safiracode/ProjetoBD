from datetime import date, time
from app.schemas.base import ORMBase


class ConsomeBase(ORMBase):
    r_numero: int
    i_codigo: str
    data_pedido: date
    hora_pedido: time
    quantidade: int | None = None


class ConsomeCreate(ConsomeBase):
    pass


class ConsomeUpdate(ORMBase):
    quantidade: int | None = None


class ConsomeResponse(ConsomeBase):
    pass
