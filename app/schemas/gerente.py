from app.schemas.base import ORMBase


class GerenteBase(ORMBase):
    matricula: str
    certificacao_gestao: str | None = None
    d_matricula: str | None = None


class GerenteCreate(GerenteBase):
    pass


class GerenteUpdate(ORMBase):
    certificacao_gestao: str | None = None
    d_matricula: str | None = None


class GerenteResponse(GerenteBase):
    pass
