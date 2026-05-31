from app.schemas.base import ORMBase


class QuartoBase(ORMBase):
    numero: int
    tipo: str | None = None
    status: str | None = None


class QuartoCreate(QuartoBase):
    pass


class QuartoUpdate(ORMBase):
    tipo: str | None = None
    status: str | None = None


class QuartoResponse(QuartoBase):
    pass
