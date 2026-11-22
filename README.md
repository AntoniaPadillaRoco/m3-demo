# Demo del ciclo rojo verde con un agente

Este repositorio es el punto de partida de una demostración de 10 minutos sobre desarrollo guiado por pruebas con un agente de IA.

Implementaremos `calcular_vencimiento`. El código inicial está incompleto de forma deliberada. Los criterios y las instrucciones al agente se escribirán durante la demostración, consultando el material de apoyo que está fuera de este repo.

## Requisitos

Python 3.10 o posterior y Git. No se necesitan paquetes externos.

## Recorrido

1. Crea `criterios.md` a mano y guárdalo en un commit antes de pedir las pruebas.
2. Escribe la instrucción para que el agente genere `tests/test_plazos.py`, con unittest, sin modificar la implementación. Debe detenerse para la revisión humana.
3. Revisa las pruebas, confirma el rojo y guarda la referencia `pruebas-revisadas`.
4. Escribe una segunda instrucción autorizando modificar únicamente `src/plazos.py`, conservando las pruebas revisadas.
5. Repite la ejecución y la corrección hasta que las pruebas originales pasen.
6. Revisa `git diff pruebas-revisadas -- src/plazos.py tests criterios.md`. Conserva las expectativas originales.
7. Completa [convergencia.md](convergencia.md) con los resultados observados en la terminal.

Antes de escribir las pruebas, la carpeta `tests/` está vacía. Una ejecución con cero pruebas no constituye evidencia de cumplimiento.

El guion y el material de apoyo se mantienen fuera de este repo. Este caso es didáctico y no reproduce criterios oficiales de R6.

