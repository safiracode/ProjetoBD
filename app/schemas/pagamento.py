from datetime import date
from decimal import Decimal
from app.schemas.base import ORMBase


class PagamentoBase(ORMBase):
    id_pagamento: str
    tipo_pagamento: str | None = None
    valor: Decimal | None = None
    data: date | None = None
    id_titular: str | None = None
    r_matricula: str | None = None


class PagamentoCreate(PagamentoBase):
    pass


class PagamentoUpdate(ORMBase):
    tipo_pagamento: str | None = None
    valor: Decimal | None = None
    data: date | None = None
    id_titular: str | None = None
    r_matricula: str | None = None


class PagamentoResponse(PagamentoBase):
    pass
