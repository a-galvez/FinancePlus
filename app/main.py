from fastapi import FastAPI
from app.api import auth
from app.db.session import engine
from app.models.base import Base

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])

Base.metadata.create_all(bind=engine)
