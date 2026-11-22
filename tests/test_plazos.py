import unittest

from src.plazos import calcular_vencimiento


class CalcularVencimientoTests(unittest.TestCase):
    def test_ca1_rechaza_fecha_invalida(self):
        for inicio in ("2026-02-30", "2026/11/20", "20-11-2026", "20261120"):
            with self.subTest(inicio=inicio):
                with self.assertRaises((ValueError, TypeError)):
                    calcular_vencimiento(inicio, 1)

    def test_ca1_rechaza_dias_no_positivos(self):
        for dias in (0, -1):
            with self.subTest(dias=dias):
                with self.assertRaises((ValueError, TypeError)):
                    calcular_vencimiento("2026-11-20", dias)

    def test_ca1_rechaza_dias_no_enteros_o_booleanos(self):
        for dias in (1.5, "2", True, False):
            with self.subTest(dias=dias):
                with self.assertRaises((ValueError, TypeError)):
                    calcular_vencimiento("2026-11-20", dias)

    def test_ca1_excluye_el_dia_inicial_y_conserva_el_formato(self):
        self.assertEqual(calcular_vencimiento("2026-11-23", 1), "2026-11-24")

    def test_ca2_cuenta_solo_dias_de_lunes_a_viernes(self):
        self.assertEqual(calcular_vencimiento("2026-11-19", 2), "2026-11-23")

    def test_ca2_inicio_en_fin_de_semana_cuenta_desde_el_lunes(self):
        self.assertEqual(calcular_vencimiento("2026-11-21", 1), "2026-11-23")

    def test_ca3_calcula_fecha_de_vencimiento_especificada(self):
        self.assertEqual(calcular_vencimiento("2026-11-20", 3), "2026-11-25")


if __name__ == "__main__":
    unittest.main()
