from fastapi import HTTPException


def not_found(message: str = "Registro não encontrado."):
    raise HTTPException(status_code=404, detail=message)


def bad_request(error: Exception):
    raise HTTPException(status_code=400, detail=str(error))
