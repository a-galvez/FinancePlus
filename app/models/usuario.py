from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False)
    contrasenia = Column(String, nullable=False)
