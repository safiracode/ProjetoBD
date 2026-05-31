from datetime import date
from app.schemas.base import ORMBase


class DependenteBase(ORMBase):
    numero_documento: str
    nome: str
    tipo_documento: str | None = None
    data_nascimento: date | None = None
    parentesco: str | None = None
    f_matricula: str | None = None


class DependenteCreate(DependenteBase):
    pass


class DependenteUpdate(ORMBase):
    nome: str | None = None
    tipo_documento: str | None = None
    data_nascimento: date | None = None
    parentesco: str | None = None
    f_matricula: str | None = None


class DependenteResponse(DependenteBase):
    pass
