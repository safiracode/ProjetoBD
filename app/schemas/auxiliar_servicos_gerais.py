from app.schemas.base import ORMBase


class AuxiliarServicosGeraisBase(ORMBase):
    matricula: str
    area_atuacao: str | None = None
    id_equipe: str | None = None


class AuxiliarServicosGeraisCreate(AuxiliarServicosGeraisBase):
    pass


class AuxiliarServicosGeraisUpdate(ORMBase):
    area_atuacao: str | None = None
    id_equipe: str | None = None


class AuxiliarServicosGeraisResponse(AuxiliarServicosGeraisBase):
    pass
