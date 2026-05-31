from app.schemas.base import ORMBase


class CozinheiroBase(ORMBase):
    matricula: str
    certificacao_gastronomica: str | None = None
    id_equipe: str | None = None


class CozinheiroCreate(CozinheiroBase):
    pass


class CozinheiroUpdate(ORMBase):
    certificacao_gastronomica: str | None = None
    id_equipe: str | None = None


class CozinheiroResponse(CozinheiroBase):
    pass
