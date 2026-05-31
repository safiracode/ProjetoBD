from decimal import Decimal
from app.schemas.base import ORMBase


class DiretorBase(ORMBase):
    matricula: str
    percentual_participacao: Decimal | None = None
    g_matricula: str | None = None


class DiretorCreate(DiretorBase):
    pass


class DiretorUpdate(ORMBase):
    percentual_participacao: Decimal | None = None
    g_matricula: str | None = None


class DiretorResponse(DiretorBase):
    pass
