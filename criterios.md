Criterios para implementar calcular_vencimiento(inicio: str, dias: int) -> str: en plazos.py

CA1: Recibe una fecha AAAA-MM-DD y un entero positivo de días hábiles. Como output devuelve otra fecha en el mismo formato de ingreso. El conteo de días va a excluir el día inicial. Rechazar fechas inválidas, cantidades en cero, negativas, no enteras o booleanas.

CA2: Cuenta solamente lunes a viernes. Si el inicio cae en fin de semana, el siguiente lunes cuenta como primer día. No vamos a considerar feriados.

CA3: Para la fecha de inicio 2026-11-20 y 3 días habiles, devuelve exactamente 2026-11-25. El día viernes 20 es el inicio, lunes 23, martes 24 y miercoles 25 son los tres días contados.