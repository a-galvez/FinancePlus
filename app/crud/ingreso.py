from sqlalchemy.orm import Session
from app.models.ingreso import Ingreso
from app.schemas.ingreso import CrearIngreso
from datetime import date


def crear_ingreso(db: Session, ingreso: CrearIngreso, id_usuario: int):
    nuevo = Ingreso(
        monto=ingreso.monto,
        descripcion=ingreso.descripcion,
        fecha=ingreso.fecha,
        id_usuario=id_usuario,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def obtener_ingresos(db: Session, id_usuario: int):
    return db.query(Ingreso).filter(Ingreso.id_usuario == id_usuario).all()


def obtener_ingreso_por_id(db: Session, ingreso_id: int):
    return db.query(Ingreso).filter(Ingreso.id == id).first()


def eliminar_ingreso(db: Session, ingreso_id: int):
    ingreso = db.query(Ingreso).filter(Ingreso.id == id).first()
    if ingreso:
        db.delete(ingreso)
        db.commit()
    return ingreso
