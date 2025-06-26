from pydantic import BaseModel
from datetime import date
from typing import Optional


class CrearIngreso(BaseModel):
    monto: float
    descripcion: Optional[str] = None
    fecha: date


class MostrarIngreso(BaseModel):
    id: int
    id_usuario: int
    monto: float
    descripcion: Optional[str] = None
    fecha: date

    class Config:
        orm_mode = True
