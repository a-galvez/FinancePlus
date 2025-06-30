from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.models.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(300))
    correo: Mapped[str] = mapped_column(String(100), unique=True)
    contrasenia: Mapped[str] = mapped_column(String(300))

    ingresos: Mapped[List["Ingreso"]] = relationship(
        back_populates="usuario", cascade="all, delete-orphan"
    )
    egresos: Mapped[List["Egreso"]] = relationship(
        back_populates="usuario", cascade="all, delete-orphan"
    )
