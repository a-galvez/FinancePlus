from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import CrearUsuario


def crear_usuario(db: Session, usuario: CrearUsuario):
    nuevo = Usuario(
        nombre=usuario.nombre, correo=usuario.correo, contrasenia=usuario.contrasenia
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def obtener_usuario_por_id(db: Session, id_usuario: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()


def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()
