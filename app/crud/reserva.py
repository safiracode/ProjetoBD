from sqlalchemy.orm import Session
from app import models
from app.crud.base import apply_updates
from app.schemas.reserva import ReservaCreate, ReservaUpdate


def listar(db: Session):
    return db.query(models.Reserva).all()


def buscar(db: Session, numero: int):
    return db.query(models.Reserva).filter(models.Reserva.numero == numero).first()


def _validar_reserva(db: Session, dados, ignorar_numero: int | None = None):
    fields_set = dados.model_fields_set if hasattr(dados, "model_fields_set") else set(dados.model_fields.keys())

    data_entrada = getattr(dados, "data_entrada", None)
    data_saida = getattr(dados, "data_saida", None)
    if data_entrada and data_saida and data_saida <= data_entrada:
        raise ValueError("Data de saída deve ser posterior à data de entrada.")

    if "quantidade_pessoas" in fields_set and dados.quantidade_pessoas is not None and dados.quantidade_pessoas <= 0:
        raise ValueError("Quantidade de pessoas deve ser maior que zero.")

    if "r_matricula" in fields_set and dados.r_matricula is not None:
        recepcionista = db.query(models.Recepcionista).filter(models.Recepcionista.matricula == dados.r_matricula).first()
        if not recepcionista:
            raise ValueError("Recepcionista informada não existe.")


def _vincular_quartos(db: Session, reserva: models.Reserva, quartos: list[int]):
    for q_numero in quartos:
        quarto = db.query(models.Quarto).filter(models.Quarto.numero == q_numero).first()
        if not quarto:
            raise ValueError(f"Quarto {q_numero} não existe.")
        if quarto.status == "Manutenção":
            raise ValueError(f"Quarto {q_numero} está em manutenção.")
        vinculo = models.ReservaQuarto(r_numero=reserva.numero, q_numero=q_numero)
        db.add(vinculo)


def criar(db: Session, dados: ReservaCreate):
    if buscar(db, dados.numero):
        raise ValueError("Reserva já cadastrada.")
    _validar_reserva(db, dados)

    values = dados.model_dump(exclude={"quartos"})
    reserva = models.Reserva(**values)
    db.add(reserva)
    db.flush()

    if dados.quartos:
        _vincular_quartos(db, reserva, dados.quartos)

    db.commit()
    db.refresh(reserva)
    return reserva


def atualizar(db: Session, numero: int, dados: ReservaUpdate):
    reserva = buscar(db, numero)
    if not reserva:
        return None
    _validar_reserva(db, dados, ignorar_numero=numero)

    values = dados.model_dump(exclude_unset=True)
    quartos = values.pop("quartos", None)
    for field, value in values.items():
        setattr(reserva, field, value)

    if quartos is not None:
        db.query(models.ReservaQuarto).filter(models.ReservaQuarto.r_numero == numero).delete()
        _vincular_quartos(db, reserva, quartos)

    db.commit()
    db.refresh(reserva)
    return reserva


def deletar(db: Session, numero: int):
    reserva = buscar(db, numero)
    if not reserva:
        return None
    if reserva.titulares or reserva.consumos:
        raise ValueError("Não é possível deletar reserva com titular financeiro ou consumo vinculado.")
    db.query(models.ReservaQuarto).filter(models.ReservaQuarto.r_numero == numero).delete()
    db.delete(reserva)
    db.commit()
    return reserva
