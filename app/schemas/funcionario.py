from datetime import date
from decimal import Decimal
from app.schemas.base import ORMBase


class FuncionarioBase(ORMBase):
    matricula: str
    numero_documento: str
    cargo: str | None = None
    salario: Decimal | None = None
    data_contratacao: date | None = None


class FuncionarioCreate(FuncionarioBase):
    pass


class FuncionarioUpdate(ORMBase):
    cargo: str | None = None
    salario: Decimal | None = None
    data_contratacao: date | None = None


class FuncionarioResponse(FuncionarioBase):
    pass
