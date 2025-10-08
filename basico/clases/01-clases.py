"""Clases"""
# Una clase es como un molde o platilla para crear objetos.

# class Persona: → defines la clase.
# __init__() → es el constructor: se ejecuta automáticamente al crear un objeto.
# self → representa al objeto mismo (como “yo”).
# saludar() → es un método (una función dentro de la clase).


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

    def cumplir_años(self):
        self.edad += 1
        print(
            f"Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años")


persona1 = Persona("bear", 17)
persona2 = Persona("Elliot", 30)
persona = Persona("darlene", 20)

persona.cumplir_años()
persona1.saludar()
persona2.saludar()


class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def trabajar(self):
        print(f"{self.nombre} está trabajando como {self.puesto}")


empleado = Empleado("Susan", 30, "Programador")
empleado.saludar()
empleado.trabajar()
