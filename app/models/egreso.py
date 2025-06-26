from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base


class Egreso(Base):
    __tablename__ = "egresos"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    descripcion = Column(String)
    monto = Column(Float, nullable=False)
    fecha = Column(Date)

    usuario = relationship("Usuario")
