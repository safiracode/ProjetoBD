from app.schemas.base import ORMBase


class EnderecoBase(ORMBase):
    tipo_logradouro: str | None = None
    nome_logradouro: str | None = None
    numero: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    cep: str | None = None


class EnderecoCreate(EnderecoBase):
    pass


class EnderecoUpdate(EnderecoBase):
    pass


class EnderecoResponse(EnderecoBase):
    id_endereco: int
