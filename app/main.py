from fastapi import FastAPI
from app.api import finances
from app.db.session import engine
from app.db.base import Base

app = FastAPI()
app.include_router(finances.router, prefix="/api", tags=["Finanzas"])

Base.metadata.create_all(bind=engine)
