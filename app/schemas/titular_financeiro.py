from app.schemas.base import ORMBase


class TitularFinanceiroBase(ORMBase):
    id_titular: str
    r_numero: int | None = None


class TitularFinanceiroCreate(TitularFinanceiroBase):
    pass


class TitularFinanceiroUpdate(ORMBase):
    r_numero: int | None = None


class TitularFinanceiroResponse(TitularFinanceiroBase):
    pass
