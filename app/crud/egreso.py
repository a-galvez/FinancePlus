from sqlalchemy.orm import Session
from app.models.egreso import Egreso
from app.schemas.egreso import CrearEgreso
from datetime import date


def crear_egreso(db: Session, egreso: CrearEgreso, id_usuario: int):
    nuevo = Egreso(
        monto=egreso.monto,
        descripcion=egreso.descripcion,
        fecha=egreso.fecha,
        id_usuario=id_usuario,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def obtener_egresos(db: Session, id_usuario: int):
    return db.query(Egreso).filter(Egreso.id_usuario == id_usuario).all()


def obtener_egreso_por_id(db: Session, egreso_id: int):
    return db.query(Egreso).filter(Egreso.id == id).first()


def eliminar_egreso(db: Session, egreso_id: int):
    egreso = db.query(Egreso).filter(Egreso.id == id).first()
    if egreso:
        db.delete(egreso)
        db.commit()
    return egreso
