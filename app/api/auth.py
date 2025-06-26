from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import verificar_password, crear_token_acceso
from app.schemas.usuario import UsuarioLogin, UsuarioToken
from app.crud.usuario import obtener_usuario_por_email

router = APIRouter()


@router.post("/login", response_model=UsuarioToken)
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    user = obtener_usuario_por_correo(db, usuario.correo)
    if not user or not verificar_password(usuario.contrasenia, user.contrasenia):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = crear_token_acceso(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
