from app.schemas.base import ORMBase


class IdiomaRecepcionistaBase(ORMBase):
    r_matricula: str
    idioma: str


class IdiomaRecepcionistaCreate(IdiomaRecepcionistaBase):
    pass


class IdiomaRecepcionistaUpdate(ORMBase):
    idioma: str | None = None


class IdiomaRecepcionistaResponse(IdiomaRecepcionistaBase):
    pass
