from app.schemas.base import ORMBase


class CamareiroBase(ORMBase):
    matricula: str
    velocidade_troca_lencol: str | None = None
    id_equipe: str | None = None


class CamareiroCreate(CamareiroBase):
    pass


class CamareiroUpdate(ORMBase):
    velocidade_troca_lencol: str | None = None
    id_equipe: str | None = None


class CamareiroResponse(CamareiroBase):
    pass
