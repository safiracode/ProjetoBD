from __future__ import annotations
from fastapi import FastAPI, HTTPException

from app.database import check_database_connection
from app.routes import (
    endereco,
    pessoa,
    funcionario,
    dependente,
    diretor,
    gerente,
    pessoa_operacional,
    cozinheiro,
    camareiro,
    auxiliar_servicos_gerais,
    recepcionista,
    idioma_recepcionista,
    reserva,
    titular_financeiro,
    hospede,
    empresa,
    pagamento,
    categoria_quarto,
    quarto,
    reserva_quarto,
    item,
    consome,
)

app = FastAPI(
    title="API do Sistema Hoteleiro",
    description="API FastAPI + SQLAlchemy fiel ao minimundo, modelo lógico e normalização do projeto de Banco de Dados.",
    version="2.0.0",
)


@app.get("/")
def home():
    return {"message": "API do Sistema Hoteleiro funcionando."}


@app.get("/health")
def health_check():
    try:
        check_database_connection()
        return {"database": "connected"}
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Erro na conexão com o banco: {error}")


app.include_router(endereco.router)
app.include_router(pessoa.router)
app.include_router(funcionario.router)
app.include_router(dependente.router)
app.include_router(diretor.router)
app.include_router(gerente.router)
app.include_router(pessoa_operacional.router)
app.include_router(cozinheiro.router)
app.include_router(camareiro.router)
app.include_router(auxiliar_servicos_gerais.router)
app.include_router(recepcionista.router)
app.include_router(idioma_recepcionista.router)
app.include_router(reserva.router)
app.include_router(titular_financeiro.router)
app.include_router(hospede.router)
app.include_router(empresa.router)
app.include_router(pagamento.router)
app.include_router(categoria_quarto.router)
app.include_router(quarto.router)
app.include_router(reserva_quarto.router)
app.include_router(item.router)
app.include_router(consome.router)
