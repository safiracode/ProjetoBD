from app.schemas.base import ORMBase


class RecepcionistaBase(ORMBase):
    matricula: str
    turno: str | None = None
    conhecimento_sistema: str | None = None
    id_equipe: str | None = None


class RecepcionistaCreate(RecepcionistaBase):
    pass


class RecepcionistaUpdate(ORMBase):
    turno: str | None = None
    conhecimento_sistema: str | None = None
    id_equipe: str | None = None


class RecepcionistaResponse(RecepcionistaBase):
    pass
