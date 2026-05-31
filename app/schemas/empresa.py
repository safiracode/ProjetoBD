from app.schemas.base import ORMBase


class EmpresaBase(ORMBase):
    id_titular: str
    cnpj: str
    razao_social: str | None = None
    telefone: str | None = None


class EmpresaCreate(EmpresaBase):
    pass


class EmpresaUpdate(ORMBase):
    cnpj: str | None = None
    razao_social: str | None = None
    telefone: str | None = None


class EmpresaResponse(EmpresaBase):
    pass
