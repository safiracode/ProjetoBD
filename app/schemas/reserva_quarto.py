from app.schemas.base import ORMBase


class ReservaQuartoBase(ORMBase):
    r_numero: int
    q_numero: int


class ReservaQuartoCreate(ReservaQuartoBase):
    pass


class ReservaQuartoResponse(ReservaQuartoBase):
    pass
