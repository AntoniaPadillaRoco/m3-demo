"""Punto de partida deliberadamente incompleto para observar el rojo."""
from datetime import date


def calcular_vencimiento(inicio: str, dias: int) -> str:
    # Pendiente: validar dias y calcular el plazo excluyendo fines de semana.
    return date.fromisoformat(inicio).isoformat()

