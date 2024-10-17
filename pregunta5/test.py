import unittest
from maldad import narayana, tribonacci_tail


# Clase de prueba
class PruebasUnitarias(unittest.TestCase):
    def test_narayana(self):
        """Pruebas para varios valores de n y k del triángulo de los numeros de narayana hasta la fila n = 10."""

        # Casos de prueba (n, k) -> resultado esperado
        casos_prueba = {
            (1, 1): 1,
            (2, 1): 1, (2, 2): 1,
            (3, 1): 1, (3, 2): 3, (3, 3): 1,
            (4, 1): 1, (4, 2): 6, (4, 3): 6, (4, 4): 1,
            (5, 1): 1, (5, 2): 10, (5, 3): 20, (5, 4): 10, (5, 5): 1,
            (6, 1): 1, (6, 2): 15, (6, 3): 50, (6, 4): 50, (6, 5): 15, (6, 6): 1,
            (7, 1): 1, (7, 2): 21, (7, 3): 105, (7, 4): 175, (7, 5): 105, (7, 6): 21, (7, 7): 1,
            (8, 1): 1, (8, 2): 28, (8, 3): 196, (8, 4): 490, (8, 5): 490, (8, 6): 196, (8, 7): 28, (8, 8): 1,
            (9, 1): 1, (9, 2): 36, (9, 3): 336, (9, 4): 1176, (9, 5): 1764, (9, 6): 1176, (9, 7): 336, (9, 8): 36, (9, 9): 1,
            (10, 1): 1, (10, 2): 45, (10, 3): 540, (10, 4): 2520, (10, 5): 5292, (10, 6): 5292, (10, 7): 2520, (10, 8): 540, (10, 9): 45, (10, 10): 1
        }

        # Ejecutar las pruebas
        for (n, k), esperado in casos_prueba.items():
            with self.subTest(n=n, k=k):
                self.assertEqual(narayana(n, k), esperado)

    def test_tribonacci_base_cases(self):
        """Prueba los casos base de la secuencia Tribonacci."""
        self.assertEqual(tribonacci_tail(0), 0)
        self.assertEqual(tribonacci_tail(1), 1)
        self.assertEqual(tribonacci_tail(2), 2)

    def test_tribonacci_recursive_cases(self):
        """Prueba algunos casos calculados recursivamente."""
        self.assertEqual(tribonacci_tail(3), 3)   # 0 + 1 + 2
        self.assertEqual(tribonacci_tail(4), 6)   # 1 + 2 + 3
        self.assertEqual(tribonacci_tail(5), 11)  # 2 + 3 + 6
        self.assertEqual(tribonacci_tail(6), 20)  # 3 + 6 + 11
        self.assertEqual(tribonacci_tail(7), 37)  # 6 + 11 + 20

    def test_large_n(self):
        """Prueba la función con un n grande xD."""
        self.assertEqual(tribonacci_tail(8), 68)       # Tribonacci(8) = 68
        self.assertEqual(tribonacci_tail(10), 230)     # Tribonacci(10) = 230
        # Tribonacci(20) = 101902
        self.assertEqual(tribonacci_tail(20), 101902)


# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
