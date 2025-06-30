from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.ingreso import Ingreso
from app.models.egreso import Egreso


def calcular_balance(db: Session, usuario_id: int) -> float:
    total_ingresos = (
        db.query(func.coalesce(func.sum(Ingreso.monto), 0))
        .filter(Ingreso.usuario_id == usuario_id)
        .scalar()
    )
    total_egresos = (
        db.query(func.coalesce(func.sum(Egreso.monto), 0))
        .filter(Egreso.usuario_id == usuario_id)
        .scalar()
    )
    return total_ingresos - total_egresos
