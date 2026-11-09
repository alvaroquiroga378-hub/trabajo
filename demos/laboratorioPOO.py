class NaveEspacial:
    def __init__(self, nombre, piloto, nivel_escudo):
        self.nombre = nombre
        self.piloto = piloto
        self.nivel_escudo = nivel_escudo

    def mostrar_caracteristicas(self):
        print(f"Nave: {self.nombre}")
        print(f"Piloto: {self.piloto}")
        print(f"Nivel de escudo: {self.nivel_escudo}")
        print("-" * 30)


# Instanciar dos naves distintas
nave1 = NaveEspacial("Halcón Milenario", "Han Solo", 100)
nave2 = NaveEspacial("X-Wing", "Luke Skywalker", 80)

# Imprimir las características iniciales
print("=== Características iniciales ===")
nave1.mostrar_caracteristicas()
nave2.mostrar_caracteristicas()