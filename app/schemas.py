from datetime import date
from decimal import Decimal
from pydantic import BaseModel


class EnderecoBase(BaseModel):
    tipo_logradouro: str | None = None
    nome_logradouro: str | None = None
    numero: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    cep: str | None = None


class EnderecoCreate(EnderecoBase):
    pass


class EnderecoResponse(EnderecoBase):
    id_endereco: int

    class Config:
        from_attributes = True


class CategoriaQuartoBase(BaseModel):
    tipo: str
    capacidade_maxima: int | None = None
    valor_diaria: Decimal | None = None


class CategoriaQuartoCreate(CategoriaQuartoBase):
    pass


class CategoriaQuartoResponse(CategoriaQuartoBase):
    class Config:
        from_attributes = True


class QuartoBase(BaseModel):
    numero: int
    tipo: str
    status: str | None = None


class QuartoCreate(QuartoBase):
    pass


class QuartoUpdate(BaseModel):
    tipo: str | None = None
    status: str | None = None


class QuartoResponse(QuartoBase):
    class Config:
        from_attributes = True