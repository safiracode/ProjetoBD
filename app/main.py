from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

app = FastAPI(
    title="API do Sistema Hoteleiro",
    description="API criada para conectar o projeto de Banco de Dados com Python usando FastAPI e SQLAlchemy.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "API do Sistema Hoteleiro funcionando."
    }


# =========================
# QUARTOS
# =========================

@app.get("/quartos", response_model=list[schemas.QuartoResponse])
def listar_quartos(db: Session = Depends(get_db)):
    return crud.listar_quartos(db)


@app.get("/quartos/{numero}", response_model=schemas.QuartoResponse)
def buscar_quarto(numero: int, db: Session = Depends(get_db)):
    quarto = crud.buscar_quarto(db, numero)

    if not quarto:
        raise HTTPException(status_code=404, detail="Quarto não encontrado.")

    return quarto


@app.post("/quartos", response_model=schemas.QuartoResponse)
def criar_quarto(quarto: schemas.QuartoCreate, db: Session = Depends(get_db)):
    novo_quarto = crud.criar_quarto(db, quarto)

    if not novo_quarto:
        raise HTTPException(
            status_code=400,
            detail="Categoria de quarto inexistente."
        )

    return novo_quarto


@app.put("/quartos/{numero}", response_model=schemas.QuartoResponse)
def atualizar_quarto(
    numero: int,
    dados: schemas.QuartoUpdate,
    db: Session = Depends(get_db)
):
    quarto = crud.atualizar_quarto(db, numero, dados)

    if not quarto:
        raise HTTPException(status_code=404, detail="Quarto não encontrado.")

    return quarto


@app.delete("/quartos/{numero}")
def deletar_quarto(numero: int, db: Session = Depends(get_db)):
    quarto = crud.deletar_quarto(db, numero)

    if not quarto:
        raise HTTPException(status_code=404, detail="Quarto não encontrado.")

    return {
        "message": "Quarto removido com sucesso."
    }