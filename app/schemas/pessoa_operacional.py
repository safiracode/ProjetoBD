from app.schemas.base import ORMBase


class PessoaOperacionalBase(ORMBase):
    id_equipe: str
    g_matricula: str | None = None


class PessoaOperacionalCreate(PessoaOperacionalBase):
    pass


class PessoaOperacionalUpdate(ORMBase):
    g_matricula: str | None = None


class PessoaOperacionalResponse(PessoaOperacionalBase):
    pass
