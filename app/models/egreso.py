from typing import Optional
from sqlalchemy import ForeignKey, String, Float, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from app.models.usuario import Usuario


class Egreso(Base):
    __tablename__ = "egresos"

    id: Mapped[int] = mapped_column(primary_key=True)
    monto: Mapped[float] = mapped_column(Float)
    descripcion: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
    fecha: Mapped[Optional[str]] = mapped_column(Date)

    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuario: Mapped["Usuario"] = relationship(back_populates="egresos")
