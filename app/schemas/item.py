from decimal import Decimal
from app.schemas.base import ORMBase


class ItemBase(ORMBase):
    codigo: str
    valor_unitario: Decimal
    descricao: str | None = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ORMBase):
    valor_unitario: Decimal | None = None
    descricao: str | None = None


class ItemResponse(ItemBase):
    pass
