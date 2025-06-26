from pydantic import BaseModel
from datetime import date
from typing import Optional


class CrearUsuario(BaseModel):
    nombre: str
    correo: str
    contrasenia: str


class MostrarUsuario(BaseModel):
    id_usuario: int
    nombre: str
    correo: str


class Config:
    orm_mode = True
