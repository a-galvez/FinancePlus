from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.usuario import CrearUsuario, MostrarUsuario
from app.crud.usuario import (
    obtener_usuario_por_correo,
    obtener_usuario_por_id,
    crear_usuario,
)

router = APIRouter()


@router.post("/registrar", response_model=MostrarUsuario)
def registrar_usuario(usuario: CrearUsuario, db: Session = Depends(get_db)):
    db_usuario = obtener_usuario_por_correo(db, usuario.correo)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    nuevo_usuario = crear_usuario(db, usuario)
    return nuevo_usuario
