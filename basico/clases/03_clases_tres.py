"""Atributos y metodos"""
# Atributos de instacia, definidos en init y unicos para cada objeto
# Atributos de clase, compartidos por todas las instacias


class Coche:
    ruedas = 4  # atributo de clase

    def __init__(self, marca, color):
        self.marca = marca  # atributo de instancia
        self.color = color


auto1 = Coche("MANTJA", "Rojo")
auto2 = Coche("Mazda", "Negro")

print(auto1.ruedas)  # 4
print(auto2.ruedas)  # 4
print(auto1.marca)  # MANTJA
print(auto2.marca)  # Mazda


# Metodos especiales (como __init__, __str__, etc.)

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"


p = Persona("Sam")
print(p)


# Encapsulamiento (atributos privados)
# _atributo -- protegido(no usar fuera de la clase)
# __atributo -- privado(Python lo renombra internamente)

class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")


cuenta = Cuenta(100)
cuenta.mostrar_saldo()
# cuenta.__saldo # Error: no accesible directamente


# Polimorfismo
# Permite usar un mismo metodo con diferentes comportamientos segun la clase

class Gato:
    def hablar(self):
        return "Miau"


class Perro:
    def hablar(self):
        return "Guau"


animales = [Gato(), Perro()]

for animal in animales:
    print(animal.hablar())
