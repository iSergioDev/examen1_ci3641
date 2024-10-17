import sys
import time
from math import floor, log2, comb


def narayana(n: int, k: int) -> int:
    """
    Calcula el número de Narayana N(n, k).

    Los números de Narayana forman una familia de números que cuentan ciertos tipos de
    particiones de un conjunto y están relacionados con los números de Catalan.

    La fórmula para calcular el número de Narayana es:

    N(n, k) = (1 / n) * C(n, k) * C(n, k-1)

    Donde C(n, k) es el coeficiente binomial (combinatorio) que cuenta el número de formas
    de elegir k elementos de un conjunto de n elementos.

    Parámetros:
    - n (int): Número total de elementos.
    - k (int): Número de elementos a seleccionar en cada combinación.

    Retorna:
    - int: El número de Narayana N(n, k), redondeado al número entero más cercano.

    Ejemplo:
    >>> narayana(5, 3)
    20
    >>> narayana(7, 4)
    175
    """
    return round((1 / n) * comb(n, k) * comb(n, k - 1))


def tribonacci_tail(n: int, a: int = 0, b: int = 1, c: int = 2) -> int:
    """
    Calcula el n-ésimo número de la secuencia de Tribonacci usando recursión de cola.

    En cada llamada, se pasan los tres últimos valores calculados como parámetros adicionales,
    de esta forma se evita la creación de una pila de llamadas profunda.

    Parámetros:
    - n (int): El índice del número en la secuencia de Tribonacci que se desea calcular.
    - a (int): Valor correspondiente a trib(n-3).
    - b (int): Valor correspondiente a trib(n-2).
    - c (int): Valor correspondiente a trib(n-1).

    Retorna:
    - int: El n-ésimo número de la secuencia de Tribonacci.

    Ejemplo:
    >>> tribonacci_tail(4)
    6
    >>> tribonacci_tail(7)
    37
    """

    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    else:
        return tribonacci_tail(n-1, b, c, a + b + c)


def maldad(n: int) -> int:
    """
    Calcula la maldad(n) según la definición dada.

    La función "maldad" se calcula en tres pasos:
    1. Se calcula el valor de k de Narayana(n, k) que viene dado por floor(log2(n))
    2. Se calcula el número de narayana de Narayana(n, k)
    3. Se calcula el logaritmo base 2 de N(n, k) y se redondea hacia abajo
    4. Se usa este valor como entrada para la función Tribonacci, y se retorna el resultado como maldad(n).

    Parámetros:
    - n (int): Un entero positivo que determina el tamaño del conjunto para calcular Narayana y la secuencia de Tribonacci.

    Retorna:
    - int: El valor de la maldad(n), basado en los números de Narayana y la secuencia de Tribonacci.

    Ejemplo:
    >>> maldad(15)
    778
    >>> maldad(50)
    516743378
    """

    k = floor(log2(n))
    N_n_k = narayana(n, k)
    log_value = floor(log2(N_n_k))

    return tribonacci_tail(log_value + 1)


def main():
    # Verificar si se proporcionó un argumento en la línea de comandos
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            # Validar que n sea estrictamente mayor que 1
            if n <= 1:
                raise ValueError(
                    "El valor de n debe ser estrictamente mayor que 1.")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        print("Error: Debes proporcionar un valor de n como argumento.")
        sys.exit(1)

    # Mide el tiempo de inicio
    start_time = time.time()

    # Calcula y muestra el resultado
    result = maldad(n)

    # Mide el tiempo final
    end_time = time.time()

    # Calcula el tiempo de ejecución
    execution_time = end_time - start_time

    # Salidas
    print(f"maldad({n}) = {result}")
    print(f"Tiempo de ejecución = {execution_time:.6f} segundos")


if __name__ == "__main__":
    main()
