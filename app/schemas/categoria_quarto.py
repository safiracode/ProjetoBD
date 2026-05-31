from decimal import Decimal
from app.schemas.base import ORMBase


class CategoriaQuartoBase(ORMBase):
    tipo: str
    capacidade_maxima: int | None = None
    valor_diaria: Decimal | None = None


class CategoriaQuartoCreate(CategoriaQuartoBase):
    pass


class CategoriaQuartoUpdate(ORMBase):
    capacidade_maxima: int | None = None
    valor_diaria: Decimal | None = None


class CategoriaQuartoResponse(CategoriaQuartoBase):
    pass
