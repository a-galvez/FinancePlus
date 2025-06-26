# todos los endpoints aqui
from fastapi import APIRouter

router = APIRouter()


@router.get("/incomes")
def listar_ingresos():
    return [{"id": 1, "desc": "Salario", "monto": 500}]
