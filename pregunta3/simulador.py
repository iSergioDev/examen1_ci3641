import logging


class Programa:
    def __init__(self, nombre, lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje


class Interprete:
    def __init__(self, lenguaje_base, lenguaje):
        self.lenguaje_base = lenguaje_base
        self.lenguaje = lenguaje


class Traductor:
    def __init__(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        self.lenguaje_base = lenguaje_base
        self.lenguaje_origen = lenguaje_origen
        self.lenguaje_destino = lenguaje_destino


class Simulador:
    def __init__(self):
        self.programas = {}
        self.interpretes = {}
        self.traductores = {}
        # Configura el nivel de logging
        logging.basicConfig(level=logging.ERROR)

    def definir_programa(self, nombre, lenguaje):
        if nombre in self.programas:
            # print(f"Error: El programa '{nombre}' ya está definido.")
            logging.error(f"Error: El programa '{nombre}' ya está definido.")
            return
        self.programas[nombre] = Programa(nombre, lenguaje)
        print(f"Se definió el programa '{nombre}', ejecutable en '{lenguaje}'")

    def definir_interprete(self, lenguaje_base, lenguaje):
        # Verificar si el intérprete ya existe
        if lenguaje in self.interpretes:
            print(f"Error: El intérprete para '{lenguaje}' ya está definido.")
            return

        # Si no existe, definir el intérprete
        self.interpretes[lenguaje] = Interprete(lenguaje_base, lenguaje)
        print(f"Se definió un intérprete para '{
              lenguaje}', escrito en '{lenguaje_base}'")

    def definir_traductor(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        # Validar si el traductor ya existe
        if (lenguaje_origen, lenguaje_destino) in self.traductores:
            logging.error(f"Error: El traductor de '{lenguaje_origen}' a '{
                          lenguaje_destino}' ya está definido.")
            return

        # Crear el traductor
        self.traductores[(lenguaje_origen, lenguaje_destino)] = Traductor(
            lenguaje_base, lenguaje_origen, lenguaje_destino)
        print(f"Se definió un traductor de '{lenguaje_origen}' hacia '{
              lenguaje_destino}', escrito en '{lenguaje_base}'")

        # Verificar si se pueden crear nuevos traductores a partir de este
        self.crear_nuevos_traductores(
            lenguaje_base, lenguaje_origen, lenguaje_destino)

    def crear_nuevos_traductores(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        # Verificar si hay traductores existentes que pueden ser utilizados
        for (origen, destino), traductor in self.traductores.items():
            if traductor.lenguaje_destino == lenguaje_origen:
                nuevo_destino = lenguaje_destino
                nuevo_traductor = Traductor(
                    lenguaje_base, origen, nuevo_destino)
                if (origen, nuevo_destino) not in self.traductores:
                    self.traductores[(origen, nuevo_destino)] = nuevo_traductor

    def es_ejecutable(self, nombre):
        if nombre not in self.programas:
            logging.error(f"Error: El programa '{nombre}' no está definido.")
            return False

        programa = self.programas[nombre]

        # Regla 1: Si el programa está en LOCAL, es ejecutable
        if programa.lenguaje == 'LOCAL':
            return True

        # Regla 2: Comprobar si hay un intérprete que puede ejecutar el lenguaje del programa
        if self.validar_interpretes(programa.lenguaje):
            return True

        # Regla 3: Comprobar si hay traductores para el lenguaje del programa
        return self.validar_traductores(programa.lenguaje)

    def validar_interpretes(self, lenguaje):
        """Validar si se puede llegar a LOCAL a través de intérpretes anidados."""
        visitados = set()
        lenguajes_a_verificar = [lenguaje]

        while lenguajes_a_verificar:
            lenguaje_actual = lenguajes_a_verificar.pop(0)

            for interprete in self.interpretes.values():
                if interprete.lenguaje == lenguaje_actual:
                    if interprete.lenguaje_base == 'LOCAL':
                        return True
                    if interprete.lenguaje_base not in visitados:
                        lenguajes_a_verificar.append(interprete.lenguaje_base)
                        visitados.add(interprete.lenguaje_base)

        return False

    def validar_traductores(self, lenguaje):
        """Validar si se puede llegar a LOCAL a través de traductores."""
        visitados = set()
        lenguajes_a_verificar = [lenguaje]

        while lenguajes_a_verificar:
            lenguaje_actual = lenguajes_a_verificar.pop(0)

            for traductor in self.traductores.values():
                if traductor.lenguaje_origen == lenguaje_actual:
                    if traductor.lenguaje_destino in self.interpretes:
                        for interprete in self.interpretes.values():
                            if interprete.lenguaje_base == 'LOCAL' and traductor.lenguaje_destino == interprete.lenguaje:
                                return True
                    if traductor.lenguaje_destino not in visitados:
                        lenguajes_a_verificar.append(
                            traductor.lenguaje_destino)
                        visitados.add(traductor.lenguaje_destino)

        return False


def main():
    simulador = Simulador()

    while True:
        accion = input("$> ").strip().split()
        if not accion:
            continue

        comando = accion[0].upper()

        if comando == "DEFINIR":
            tipo = accion[1].upper()
            if tipo == "PROGRAMA":
                nombre = accion[2]
                lenguaje = accion[3]
                simulador.definir_programa(nombre, lenguaje)
            elif tipo == "INTERPRETE":
                lenguaje_base = accion[2]
                lenguaje = accion[3]
                simulador.definir_interprete(lenguaje_base, lenguaje)
            elif tipo == "TRADUCTOR":
                lenguaje_base = accion[2]
                lenguaje_origen = accion[3]
                lenguaje_destino = accion[4]
                simulador.definir_traductor(
                    lenguaje_base, lenguaje_origen, lenguaje_destino)

        elif comando == "EJECUTABLE":
            nombre = accion[1]
            if simulador.es_ejecutable(nombre):
                print(f"Si, es posible ejecutar el programa '{nombre}'")
            else:
                print(f"No es posible ejecutar el programa '{nombre}'")

        elif comando == "SALIR":
            break


if __name__ == "__main__":
    main()
