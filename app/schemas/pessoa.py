from datetime import date
from app.schemas.base import ORMBase
from app.schemas.endereco import EnderecoCreate, EnderecoResponse


class PessoaBase(ORMBase):
    numero_documento: str
    nome: str
    tipo_documento: str
    data_nascimento: date | None = None


class PessoaCreate(PessoaBase):
    endereco: EnderecoCreate | None = None
    id_endereco: int | None = None


class PessoaUpdate(ORMBase):
    nome: str | None = None
    tipo_documento: str | None = None
    data_nascimento: date | None = None
    endereco: EnderecoCreate | None = None
    id_endereco: int | None = None


class PessoaResponse(PessoaBase):
    id_endereco: int | None = None
    idade: int | None = None
    endereco: EnderecoResponse | None = None
