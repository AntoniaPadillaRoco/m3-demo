# Demo del ciclo rojo verde con un agente

Este repositorio es el punto de partida de una demostración de 10 minutos sobre desarrollo guiado por pruebas con un agente de IA.

Implementaremos `calcular_vencimiento` según [criterios.md](criterios.md). El código inicial está incompleto de forma deliberada. CA3 fija un caso que debe devolver **2026-11-25**. No se consideran feriados.

## Requisitos

Python 3.10 o posterior y Git. No se necesitan paquetes externos.

## Recorrido

1. Escribe `tests/test_plazos.py` desde los criterios y ejecuta `python3 -m unittest discover -s tests -v`.
2. Revisa las pruebas. Guarda el estado rojo con un commit y la etiqueta `pruebas-revisadas`.
3. Entrega [INSTRUCCION_AGENTE.txt](INSTRUCCION_AGENTE.txt) al agente. El único archivo de implementación permitido es `src/plazos.py`.
4. Repite la ejecución y la corrección hasta que las pruebas originales pasen.
5. Revisa `git diff pruebas-revisadas -- src/plazos.py tests criterios.md`. Conserva las pruebas y la fecha de CA3.
6. Guarda la salida en `evidencia/pruebas-finales.txt` y completa [convergencia.md](convergencia.md) con resultados reales.

Antes de escribir las pruebas, la carpeta `tests/` está vacía. Una ejecución con cero pruebas no constituye evidencia de cumplimiento.

Las soluciones, el guion de grabación y el ejemplo simulado de la trampa de CA3 se mantienen fuera de este repo. Este caso es didáctico y no reproduce criterios oficiales de R6.

