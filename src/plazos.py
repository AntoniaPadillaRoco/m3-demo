"""Cálculo de vencimientos en días hábiles."""
import re
from datetime import date, timedelta


def calcular_vencimiento(inicio: str, dias: int) -> str:
    if not isinstance(inicio, str) or re.fullmatch(r"\d{4}-\d{2}-\d{2}", inicio) is None:
        raise ValueError("inicio debe tener formato AAAA-MM-DD")

    fecha = date.fromisoformat(inicio)

    if isinstance(dias, bool) or not isinstance(dias, int):
        raise TypeError("dias debe ser un entero")
    if dias <= 0:
        raise ValueError("dias debe ser positivo")

    contados = 0
    while contados < dias:
        fecha += timedelta(days=1)
        if fecha.weekday() < 5:
            contados += 1

    return fecha.isoformat()

