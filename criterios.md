# Criterios del cálculo de plazos hábiles

Caso didáctico creado para este módulo. Estas reglas y fechas no se atribuyen al proyecto R6.

Implementar `calcular_vencimiento(inicio: str, dias: int) -> str` en `src/plazos.py`.

| Criterio | Comportamiento verificable |
|---|---|
| CA1 | Recibe una fecha ISO `AAAA-MM-DD` y un entero positivo de días hábiles. Devuelve otra fecha ISO. El conteo excluye el día inicial. Rechaza fechas inválidas y cantidades cero, negativas, no enteras o booleanas con `ValueError`. |
| CA2 | Cuenta solamente lunes a viernes. Si el inicio cae en fin de semana, el siguiente lunes cuenta como primer día. No se consideran feriados. |
| CA3 | Para inicio `2026-11-20` y `3` días hábiles, devuelve exactamente `2026-11-25`. Viernes 20 es el inicio; lunes 23, martes 24 y miércoles 25 son los tres días contados. |

Las pruebas conservan estos criterios durante la implementación. Una discrepancia se somete a revisión humana antes de modificar el contrato.

