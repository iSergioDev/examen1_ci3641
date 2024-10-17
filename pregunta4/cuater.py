import math


class Cuaternion:
    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0):
        self.a = a  # Parte real
        self.b = b  # Coeficiente de i
        self.c = c  # Coeficiente de j
        self.d = d  # Coeficiente de k

    def __add__(self, other):
        """Suma de cuaterniones."""
        if isinstance(other, (int, float)):
            return Cuaternion(self.a + other, self.b, self.c, self.d)
        return Cuaternion(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d
        )

    def __radd__(self, other):
        """Suma desde la derecha."""
        return self.__add__(other)

    def __invert__(self):
        """Conjugado de un cuaternión."""
        return Cuaternion(self.a, -self.b, -self.c, -self.d)

    def __mul__(self, other):
        """Producto de cuaterniones."""
        if isinstance(other, (int, float)):
            return Cuaternion(self.a * other, self.b * other, self.c * other, self.d * other)

        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = other.a, other.b, other.c, other.d

        return Cuaternion(
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2
        )

    def __rmul__(self, other):
        """Producto desde la derecha."""
        return self.__mul__(other)

    def __abs__(self):
        """Valor absoluto (módulo) de un cuaternión."""
        return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)

    def __repr__(self):
        """Representación en forma de cadena del cuaternión."""
        return f"{self.a} + {self.b}i + {self.c}j + {self.d}k"


# Ejemplo de uso
if __name__ == "__main__":
    # Definir a, b y c
    a = Cuaternion(1, 2, 3, 4)
    b = Cuaternion(5, 6, 7, 8)
    c = Cuaternion(1, 1, 1, 1)

    # Valores de los cuaterniones
    print(f"Cuaterniones:")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

    # Respuesta b
    print("\n")
    print(f"Respuesta b:")
    print(f"b + c = {b + c}")
    print(f"a * b + c = {a * b + c}")
    print(f"(b + b) * (c + ~a) = {(b + b) + (c + ~a)}")
    print(f"&(c * b = {c + b}")

    # Respuesta c
    print("\n")
    print(f"Respuesta c:")
    print(f"b + 3 = {b + 3}")
    print(f"a * 3.0 + 7.0 = {a * 3.0 + 7.0}")
    print(f"(b + b) * &c = {(b + b) * abs(c)}")
