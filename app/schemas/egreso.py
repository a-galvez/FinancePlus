from pydantic import BaseModel
from datetime import date
from typing import Optional


class CrearEgreso(BaseModel):
    monto: float
    descripcion: Optional[str] = None
    fecha: date


class MostrarEgreso(BaseModel):
    id: int
    id_usuario: int
    monto: float
    descripcion: Optional[str] = None
    fecha: date

    class Config:
        orm_mode = True
