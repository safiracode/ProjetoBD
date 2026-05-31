from app.schemas.base import ORMBase
from app.schemas.pessoa import PessoaCreate


class HospedeBase(ORMBase):
    numero_documento: str
    id_titular: str | None = None
    e_mail: str | None = None


class HospedeCreate(HospedeBase):
    pessoa: PessoaCreate | None = None


class HospedeUpdate(ORMBase):
    id_titular: str | None = None
    e_mail: str | None = None


class HospedeResponse(HospedeBase):
    pass
