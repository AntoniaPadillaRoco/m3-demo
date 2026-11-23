# Convergencia del cálculo de plazos hábiles

Estado final: Ejecución realizada.

| Criterio | Prueba prevista | Resultado observado |
|---|---|---|
|CA1|test_ca1_rechaza_fecha_invalida|OK|
|CA1|test_ca1_rechaza_dias_no_positivos|OK|
|CA1|test_ca1_rechaza_dias_no_enteros_o_booleanos|OK|
|CA1|test_ca1_excluye_el_dia_inicial_y_conserva_el_formato|OK|
|CA2|test_ca2_cuenta_solo_dias_de_lunes_a_viernes|OK|
|CA2|test_ca2_inicio_en_fin_de_semana_cuenta_desde_el_lunes|OK|
|CA3|test_ca3_calcula_fecha_de_vencimiento_especificada|OK|

## Verificación

- Referencia de las pruebas revisadas: pruebas-revisadas
- Comando ejecutado: python3 -m unittest discover -s tests -v
- Resultado de la ejecución observado en la terminal: 7 pruebas aprobadas, observado en la terminal
- Diff revisado: git diff pruebas-revisadas -- src/plazos.py tests criterios.md
- Confirmación de pruebas y criterios intactos: Todo intacto, único cambio en descripción del archivo
