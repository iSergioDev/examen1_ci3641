import unittest
import math
from cuater import Cuaternion


class TestCuaternion(unittest.TestCase):
    def test_add_cuaternions(self):
        """Prueba de la suma de dos cuaterniones."""
        a = Cuaternion(1, 2, 3, 4)
        b = Cuaternion(5, 6, 7, 8)
        result = a + b
        expected = Cuaternion(6, 8, 10, 12)
        self.assertEqual(result.a, expected.a)
        self.assertEqual(result.b, expected.b)
        self.assertEqual(result.c, expected.c)
        self.assertEqual(result.d, expected.d)

    def test_add_scalar(self):
        """Prueba de la suma de un cuaternión y un escalar."""
        a = Cuaternion(1, 2, 3, 4)
        result = a + 3
        expected = Cuaternion(4, 2, 3, 4)
        self.assertEqual(result.a, expected.a)
        self.assertEqual(result.b, expected.b)
        self.assertEqual(result.c, expected.c)
        self.assertEqual(result.d, expected.d)

    def test_conjugate(self):
        """Prueba del conjugado de un cuaternión."""
        a = Cuaternion(1, 2, 3, 4)
        result = ~a
        expected = Cuaternion(1, -2, -3, -4)
        self.assertEqual(result.a, expected.a)
        self.assertEqual(result.b, expected.b)
        self.assertEqual(result.c, expected.c)
        self.assertEqual(result.d, expected.d)

    def test_mul_cuaternions(self):
        """Prueba del producto de dos cuaterniones."""
        a = Cuaternion(1, 2, 3, 4)
        b = Cuaternion(5, 6, 7, 8)
        result = a * b
        expected = Cuaternion(-60, 12, 30, 24)
        self.assertEqual(result.a, expected.a)
        self.assertEqual(result.b, expected.b)
        self.assertEqual(result.c, expected.c)
        self.assertEqual(result.d, expected.d)

    def test_mul_scalar(self):
        """Prueba del producto de un cuaternión por un escalar."""
        a = Cuaternion(1, 2, 3, 4)
        result = a * 2
        expected = Cuaternion(2, 4, 6, 8)
        self.assertEqual(result.a, expected.a)
        self.assertEqual(result.b, expected.b)
        self.assertEqual(result.c, expected.c)
        self.assertEqual(result.d, expected.d)

    def test_abs(self):
        """Prueba del valor absoluto (módulo) de un cuaternión."""
        a = Cuaternion(1, 2, 3, 4)
        result = abs(a)
        expected = math.sqrt(1**2 + 2**2 + 3**2 + 4**2)
        self.assertAlmostEqual(result, expected, places=6)


# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
